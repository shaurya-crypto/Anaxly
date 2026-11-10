import { NextRequest, NextResponse } from 'next/server'

interface ImageResult {
  url: string
  title: string
  description: string
  width: number
  height: number
  source?: string
}

// In-memory cache for fast repeated queries (24-hour TTL for positive hits, 15s for empty)
const imageSearchCache = new Map<string, { timestamp: number; images: ImageResult[] }>()
const CACHE_TTL_MS = 24 * 60 * 60 * 1000 // 24 hours
const EMPTY_CACHE_TTL_MS = 15 * 1000 // 15 seconds for empty results
const MAX_CACHE_ENTRIES = 500

const BROWSER_USER_AGENT =
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
const WIKIMEDIA_USER_AGENT =
  'SobiAITutor/2.0 (https://sobi-ai-tutor.edu; mailto:support@sobi-ai-tutor.edu)'

function sanitizeTitle(raw: string): string {
  return raw
    .replace(/^File:/i, '')
    .replace(/\.[a-zA-Z0-9]{3,4}$/, '')
    .replace(/[_]+/g, ' ')
    .replace(/[\(\)\[\]\{\}]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
}

/**
 * Checks if a URL points to an unsupported non-browser format (e.g. TIFF, PSD, PDF, EPS).
 */
function isDisallowedExtension(url: string): boolean {
  try {
    const pathname = new URL(url).pathname.toLowerCase()
    return (
      pathname.endsWith('.tif') ||
      pathname.endsWith('.tiff') ||
      pathname.endsWith('.psd') ||
      pathname.endsWith('.eps') ||
      pathname.endsWith('.ai') ||
      pathname.endsWith('.djvu') ||
      pathname.endsWith('.pdf')
    )
  } catch {
    const lower = url.toLowerCase().split('?')[0]
    return (
      lower.endsWith('.tif') ||
      lower.endsWith('.tiff') ||
      lower.endsWith('.psd') ||
      lower.endsWith('.eps') ||
      lower.endsWith('.ai') ||
      lower.endsWith('.djvu') ||
      lower.endsWith('.pdf')
    )
  }
}

/**
 * Fast low-latency image link verification (1.8s timeout, parallel execution).
 * Tests HEAD first; if server rejects with 403 or 405, falls back to a 1KB range GET.
 * Strictly verifies browser-renderable image formats (JPEG, PNG, WebP, SVG, AVIF, GIF).
 */
async function verifyImageLink(url: string): Promise<boolean> {
  if (!url || (!url.startsWith('http://') && !url.startsWith('https://'))) return false
  if (isDisallowedExtension(url)) return false

  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 1800)

    let res = await fetch(url, {
      method: 'HEAD',
      signal: controller.signal,
      headers: {
        'User-Agent': BROWSER_USER_AGENT,
        Accept: 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
      },
    })

    // If server rejects HEAD (e.g. 403 Forbidden or 405 Method Not Allowed), retry with a partial Range GET
    if (res.status === 403 || res.status === 405) {
      res = await fetch(url, {
        method: 'GET',
        signal: controller.signal,
        headers: {
          'User-Agent': BROWSER_USER_AGENT,
          Accept: 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
          Range: 'bytes=0-1024',
        },
      })
    }

    clearTimeout(timer)
    if (!res.ok && res.status !== 206 && res.status !== 304) return false

    const contentType = (res.headers.get('content-type') || '').toLowerCase()
    
    // Explicitly reject non-renderable media
    if (
      contentType.includes('tiff') ||
      contentType.includes('djvu') ||
      contentType.includes('photoshop') ||
      contentType.includes('pdf') ||
      contentType.includes('postscript')
    ) {
      return false
    }

    return (
      contentType.startsWith('image/') ||
      contentType.includes('svg')
    )
  } catch {
    return false
  }
}

/**
 * Intelligent query sanitization:
 * Distills raw activity titles (e.g. "Activity 2.1: Onion Epidermal Peel Mount")
 * into prioritized, high-accuracy queries for both broad web search and encyclopedic archives.
 */
function extractSmartImageSearchQueries(raw: string): string[] {
  const queries: string[] = []
  if (!raw || !raw.trim()) return queries
  const clean = raw.trim().replace(/^["']|["']$/g, '')

  // 1. Strip curriculum prefixes like "Activity 2.1: ", "Concept 3: ", "Module 1 - "
  const strippedPrefix = clean
    .replace(/^(?:Activity|Concept|Module|Experiment|Lab|Chapter|Section)\s*[\d\.]*\s*[:\-\)]?\s*/i, '')
    .replace(/[\(\)\[\]\{\}]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()

  // 2. Colon split handling: examine both sides of colon for substantive topics
  const colonParts = clean.split(':').map((s) => s.trim()).filter(Boolean)
  for (const part of [...colonParts].reverse()) {
    const cleanPart = part
      .replace(/^(?:Activity|Concept|Module|Experiment|Lab|Chapter|Section)\s*[\d\.]*\s*/i, '')
      .replace(/[\(\)\[\]\{\}]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim()
    
    const isGeneric =
      /^(?:part|step|subpart|case|fig|figure|section|table|row|col)\s*[\d\w\.]*$/i.test(cleanPart) ||
      /^\d+[\.\d]*$/.test(cleanPart)
    
    if (cleanPart.length >= 3 && !isGeneric) {
      queries.push(cleanPart)
    }
  }

  // 3. Parenthetical expression extraction (e.g. "Activity 10.1 (Concave Mirror)" -> "Concave Mirror")
  const parenMatches = clean.match(/\(([^\)]+)\)/g)
  if (parenMatches) {
    for (const pm of parenMatches) {
      const inside = pm
        .replace(/[\(\)]/g, '')
        .replace(/^(?:activity|module|step|exp|experiment)\s*[\d\.]*/i, '')
        .replace(/\s+/g, ' ')
        .trim()
      const isGeneric =
        /^(?:part|step|subpart|case|fig|figure)\s*[\d\w\.]*$/i.test(inside) ||
        /^\d+[\.\d]*$/.test(inside)
      if (inside.length >= 3 && !isGeneric) {
        queries.push(inside)
      }
    }
  }

  if (strippedPrefix.length >= 3 && !queries.includes(strippedPrefix)) {
    queries.push(strippedPrefix)
  }

  // 4. Domain-specific keyword enrichment (Biology, Physics, Chemistry NCERT/CBSE curriculum)
  const expanded: string[] = []
  for (const q of queries) {
    const lq = q.toLowerCase()
    // Onion epidermal peel / cells
    if (lq.includes('onion') && (lq.includes('peel') || lq.includes('mount') || lq.includes('epiderm'))) {
      expanded.push('Onion peel cells under microscope')
      expanded.push('Onion epidermal peel mount')
      expanded.push('onion peel cells')
    }
    // Cheek epithelial cells
    else if (lq.includes('cheek') && (lq.includes('cell') || lq.includes('mount') || lq.includes('epithel'))) {
      expanded.push('Human cheek cells under microscope')
      expanded.push('Cheek epithelial cells methylene blue')
      expanded.push('cheek cells microscope')
    }
    // Robert Hooke cork cells
    else if (lq.includes('cork') || lq.includes('hooke')) {
      expanded.push('Robert Hooke cork cells Micrographia 1665')
      expanded.push('cork cells under microscope')
    }
    // Plant cell wall ultrastructure
    else if (lq.includes('cell wall')) {
      expanded.push('Plant cell wall ultrastructure diagram')
      expanded.push('plant cell wall structure')
    }
    // Stomata & guard cells
    else if (lq.includes('stomata') || lq.includes('guard cell')) {
      expanded.push('Leaf stomata guard cells under microscope')
      expanded.push('stomata peel microscope')
    }
    // Organelles
    else if (lq.includes('chloroplast')) {
      expanded.push('Chloroplast structure diagram')
      expanded.push('chloroplast ultrastructure')
    } else if (lq.includes('mitochondri')) {
      expanded.push('Mitochondria structure diagram')
    } else if (lq.includes('nucleus') && !lq.includes('atom')) {
      expanded.push('Cell nucleus structure diagram')
    }
    // Compound microscope optical path
    else if (lq.includes('microscope') && (lq.includes('compound') || lq.includes('optical') || lq.includes('path') || lq.includes('ray'))) {
      expanded.push('Compound microscope optical path ray diagram')
      expanded.push('compound microscope parts labeled diagram')
    }
    // Ray optics / reflection / refraction / mirrors / lenses
    else if (lq.includes('reflection') && (lq.includes('mirror') || lq.includes('law') || lq.includes('plane'))) {
      expanded.push('Reflection of light at plane mirror diagram')
      expanded.push('laws of reflection ray diagram')
    } else if (lq.includes('refraction') && (lq.includes('glass') || lq.includes('slab'))) {
      expanded.push('Refraction through glass slab ray diagram')
    } else if (lq.includes('concave mirror') || lq.includes('convex mirror')) {
      expanded.push(`${q.replace(/[\(\)]/g, '').trim()} ray diagram`)
    }
    // Electric circuits / Ohm's law
    else if (lq.includes('ohm') || (lq.includes('circuit') && lq.includes('electric'))) {
      expanded.push("Ohm's law circuit diagram")
      expanded.push('simple electric circuit diagram')
    }
    // Xylem & Phloem
    else if (lq.includes('xylem') || lq.includes('phloem')) {
      expanded.push(`${q} tissue microscope slide`)
    }
    // General mount / peel / specimen -> add "under microscope"
    else if (/mount|peel|specimen|slide|stain/i.test(q) && !lq.includes('microscope')) {
      expanded.push(`${q} under microscope`)
    }
  }

  // Combine expanded queries first (most targeted), then stripped queries, then clean
  const cleanStripped = clean.replace(/[\(\)\[\]\{\}]/g, ' ').replace(/\s+/g, ' ').trim()
  const all = [...expanded, ...queries, cleanStripped]

  // Filter and deduplicate preserving priority order
  const seen = new Set<string>()
  const finalQueries: string[] = []
  for (const item of all) {
    const trimmed = item.replace(/[\(\)\[\]\{\}]/g, ' ').replace(/\s+/g, ' ').trim()
    const lower = trimmed.toLowerCase()
    if (trimmed.length >= 3 && !seen.has(lower)) {
      seen.add(lower)
      finalQueries.push(trimmed)
    }
  }

  return finalQueries
}

/**
 * TIER 1A: Broad Web Image Search Engine (Bing Images Async).
 * Instant, high-yield web image search without API keys or bot tokens.
 */
async function searchBingImages(query: string, limit: number = 10): Promise<ImageResult[]> {
  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 2500)
    const url = `https://www.bing.com/images/async?q=${encodeURIComponent(query)}&first=1&count=${Math.max(
      limit * 2,
      15
    )}&mmasync=1`

    const res = await fetch(url, {
      signal: controller.signal,
      headers: {
        'User-Agent': BROWSER_USER_AGENT,
        Accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      },
    })
    clearTimeout(timer)
    if (!res.ok) return []

    const html = await res.text()
    const results: ImageResult[] = []
    const seenUrls = new Set<string>()

    const murls = [...html.matchAll(/&quot;murl&quot;:&quot;(https?:\/\/[^&"]+)&quot;/g)]
    const titles = [...html.matchAll(/&quot;t&quot;:&quot;([^&"]*)&quot;/g)]

    for (let i = 0; i < murls.length; i++) {
      const imgUrl = murls[i][1]
      if (!imgUrl || seenUrls.has(imgUrl) || isDisallowedExtension(imgUrl)) continue
      seenUrls.add(imgUrl)

      let rawTitle = titles[i] ? titles[i][1] : query
      rawTitle = rawTitle
        .replace(/&amp;/g, '&')
        .replace(/&#39;/g, "'")
        .replace(/&quot;/g, '"')
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>')
        .trim()

      results.push({
        url: imgUrl,
        title: rawTitle || query,
        description: rawTitle || `Web visual for ${query}`,
        width: 800,
        height: 600,
        source: 'Web Search (Bing Images)',
      })

      if (results.length >= limit * 2) break
    }

    return results
  } catch (err) {
    console.warn('[searchBingImages warning]:', err)
    return []
  }
}

/**
 * TIER 1B: Wikipedia PageImages API.
 * High-resolution lead illustrations and scientific diagrams from encyclopedic articles.
 */
async function searchWikipediaPageImages(query: string, limit: number = 6): Promise<ImageResult[]> {
  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 2000)
    const url = `https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch=${encodeURIComponent(
      query
    )}&gsrlimit=${Math.max(limit, 5)}&prop=pageimages&pithumbsize=1200&format=json`

    const res = await fetch(url, {
      signal: controller.signal,
      headers: {
        'User-Agent': WIKIMEDIA_USER_AGENT,
        Accept: 'application/json',
      },
    })
    clearTimeout(timer)
    if (!res.ok) return []

    const data = await res.json().catch(() => ({}))
    const pages = Object.values<any>(data.query?.pages || {})
    const results: ImageResult[] = []

    for (const page of pages) {
      const thumbUrl = page.thumbnail?.source
      if (!thumbUrl || isDisallowedExtension(thumbUrl)) continue

      const title = sanitizeTitle(page.title || query)
      results.push({
        url: thumbUrl,
        title,
        description: `Wikipedia article visual: ${title}`,
        width: page.thumbnail?.width || 800,
        height: page.thumbnail?.height || 600,
        source: 'Wikipedia PageImages',
      })

      if (results.length >= limit) break
    }

    return results
  } catch (err) {
    console.warn('[searchWikipediaPageImages warning]:', err)
    return []
  }
}

/**
 * TIER 1C: Openverse Creative Commons API.
 * Clean, openly licensed educational media with strict web format filtering.
 */
async function searchOpenverse(query: string, limit: number = 10): Promise<ImageResult[]> {
  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 2000)
    const fetchLimit = Math.min(Math.max(limit * 2, 10), 20)
    const url = `https://api.openverse.org/v1/images/?q=${encodeURIComponent(query)}&page_size=${fetchLimit}`

    const res = await fetch(url, {
      signal: controller.signal,
      headers: {
        'User-Agent': WIKIMEDIA_USER_AGENT,
        Accept: 'application/json',
      },
    })
    clearTimeout(timer)
    if (!res.ok) return []

    const data = await res.json().catch(() => ({}))
    const rawResults = data.results || []
    const results: ImageResult[] = []

    for (const r of rawResults) {
      if (!r.url || isDisallowedExtension(r.url)) continue
      const w = r.width || 0
      const h = r.height || 0
      if ((w > 0 && w < 250) || (h > 0 && h < 200)) continue

      results.push({
        url: r.url,
        title: (r.title || query).trim(),
        description: r.attribution || r.title || 'Openverse Creative Commons Visual',
        width: w || 800,
        height: h || 600,
        source: 'Openverse',
      })
    }

    return results
  } catch (err) {
    console.warn('[searchOpenverse warning]:', err)
    return []
  }
}

/**
 * TIER 2: Wikimedia Commons API.
 * Encyclopedic repository with filetype filtering for clean educational vector drawings and photos.
 */
async function searchWikimediaCommons(query: string, limit: number = 10): Promise<ImageResult[]> {
  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 2500)
    const fetchLimit = Math.min(Math.max(limit * 2, 15), 30)

    // Append filetype filter if not present to prioritize clean diagrams and avoid book PDFs
    const searchQuery = query.includes('filetype:') ? query : `${query} filetype:bitmap|drawing`
    const url = `https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=${encodeURIComponent(
      searchQuery
    )}&gsrnamespace=6&prop=imageinfo&iiprop=url|size|mime&format=json&gsrlimit=${fetchLimit}`

    const res = await fetch(url, {
      signal: controller.signal,
      headers: {
        'User-Agent': WIKIMEDIA_USER_AGENT,
        Accept: 'application/json',
      },
    })
    clearTimeout(timer)
    if (!res.ok) return []

    const data = await res.json().catch(() => ({}))
    const pages = data.query?.pages || {}
    const results: ImageResult[] = []

    for (const page of Object.values<any>(pages)) {
      const info = page.imageinfo?.[0]
      if (!info?.url || isDisallowedExtension(info.url)) continue

      const mime = (info.mime || '').toLowerCase()
      // Only accept browser web image formats
      if (!mime.startsWith('image/') || mime.includes('tiff') || mime.includes('djvu')) {
        continue
      }

      const isSvg = mime === 'image/svg+xml'
      const w = info.width || 0
      const h = info.height || 0

      if (!isSvg && w > 0 && h > 0 && Math.max(w, h) < 300) {
        continue
      }

      results.push({
        url: info.url,
        title: sanitizeTitle(page.title || query),
        description: `Wikimedia Commons scientific asset: ${sanitizeTitle(page.title || query)}`,
        width: isSvg ? Math.max(w, 800) : (w || 800),
        height: isSvg ? Math.max(h, 600) : (h || 600),
        source: 'Wikimedia Commons',
      })
    }

    return results
  } catch (err) {
    console.warn('[searchWikimediaCommons warning]:', err)
    return []
  }
}

/**
 * Executes Multi-Tier Image Search:
 * 1. Tier 1 (Primary): Broad web search (Bing Images + Wikipedia PageImages + Openverse)
 * 2. Tier 2 (Fallback): Wikimedia Commons
 * Low-latency parallel verification ensures only valid, 200-OK accessible images are returned.
 */
async function getVerifiedImages(cleanQuery: string, limit: number): Promise<ImageResult[]> {
  const candidateQueries = extractSmartImageSearchQueries(cleanQuery)
  if (candidateQueries.length === 0) candidateQueries.push(cleanQuery.slice(0, 60))

  const prioritizedQueries = candidateQueries.slice(0, 3)

  // ==========================================
  // TIER 1: Broad Web Image Search (Primary)
  // ==========================================
  for (const query of prioritizedQueries) {
    // Run Bing Images & Wikipedia PageImages in parallel
    const [bingRes, wikiPageRes] = await Promise.allSettled([
      searchBingImages(query, limit),
      searchWikipediaPageImages(query, limit),
    ])

    const combinedTier1: ImageResult[] = []
    const seenUrls = new Set<string>()

    if (bingRes.status === 'fulfilled') {
      for (const img of bingRes.value) {
        if (!seenUrls.has(img.url)) {
          seenUrls.add(img.url)
          combinedTier1.push(img)
        }
      }
    }

    if (wikiPageRes.status === 'fulfilled') {
      for (const img of wikiPageRes.value) {
        if (!seenUrls.has(img.url)) {
          seenUrls.add(img.url)
          combinedTier1.push(img)
        }
      }
    }

    if (combinedTier1.length < limit) {
      const ovResults = await searchOpenverse(query, limit)
      for (const ov of ovResults) {
        if (!seenUrls.has(ov.url)) {
          seenUrls.add(ov.url)
          combinedTier1.push(ov)
        }
      }
    }

    if (combinedTier1.length > 0) {
      // Parallel verification of candidates
      const candidateBatch = combinedTier1.slice(0, Math.min(combinedTier1.length, limit * 2))
      const verifications = await Promise.allSettled(
        candidateBatch.map(async (img) => ({
          img,
          ok: await verifyImageLink(img.url),
        }))
      )

      const verified: ImageResult[] = []
      for (const res of verifications) {
        if (res.status === 'fulfilled' && res.value.ok) {
          verified.push(res.value.img)
          if (verified.length >= limit) break
        }
      }

      if (verified.length > 0) {
        return verified
      }
    }
  }

  // ==========================================
  // TIER 2: Wikimedia Commons (Fallback)
  // ==========================================
  for (const query of prioritizedQueries) {
    const wikiResults = await searchWikimediaCommons(query, limit)
    if (wikiResults.length > 0) {
      const candidateBatch = wikiResults.slice(0, Math.min(wikiResults.length, limit * 2))
      const verifications = await Promise.allSettled(
        candidateBatch.map(async (img) => ({
          img,
          ok: await verifyImageLink(img.url),
        }))
      )

      const verified: ImageResult[] = []
      for (const res of verifications) {
        if (res.status === 'fulfilled' && res.value.ok) {
          verified.push(res.value.img)
          if (verified.length >= limit) break
        }
      }

      if (verified.length > 0) {
        return verified
      }
    }
  }

  // Both Tier 1 and Tier 2 exhausted with 0 verified images
  return []
}

export async function GET(req: NextRequest) {
  try {
    const searchParams = req.nextUrl.searchParams
    const query = searchParams.get('q') || searchParams.get('query') || ''
    const limit = parseInt(searchParams.get('limit') || '10', 10)

    if (!query.trim()) {
      return NextResponse.json({ success: true, images: [] })
    }

    const cleanQuery = query.trim().replace(/^["']|["']$/g, '')
    const cacheKey = `${cleanQuery.toLowerCase()}_${limit}`

    const cached = imageSearchCache.get(cacheKey)
    if (cached) {
      const ttl = cached.images.length > 0 ? CACHE_TTL_MS : EMPTY_CACHE_TTL_MS
      if (Date.now() - cached.timestamp < ttl) {
        return NextResponse.json({ success: true, images: cached.images, cached: true })
      }
    }

    const finalImages = await getVerifiedImages(cleanQuery, limit)

    if (imageSearchCache.size >= MAX_CACHE_ENTRIES) {
      const oldestKey = imageSearchCache.keys().next().value
      if (oldestKey) imageSearchCache.delete(oldestKey)
    }
    imageSearchCache.set(cacheKey, { timestamp: Date.now(), images: finalImages })

    return NextResponse.json({ success: true, images: finalImages })
  } catch (err: any) {
    console.error('search-image GET error:', err)
    return NextResponse.json({ success: false, error: err.message, images: [] }, { status: 500 })
  }
}

export async function POST(req: Request) {
  try {
    const body = await req.json().catch(() => ({}))
    const query = body.query || body.q || ''
    const limit = parseInt(body.limit || '10', 10)

    if (!query.trim()) {
      return NextResponse.json({ success: true, images: [] })
    }

    const cleanQuery = query.trim().replace(/^["']|["']$/g, '')
    const cacheKey = `${cleanQuery.toLowerCase()}_${limit}`

    const cached = imageSearchCache.get(cacheKey)
    if (cached) {
      const ttl = cached.images.length > 0 ? CACHE_TTL_MS : EMPTY_CACHE_TTL_MS
      if (Date.now() - cached.timestamp < ttl) {
        return NextResponse.json({ success: true, images: cached.images, cached: true })
      }
    }

    const finalImages = await getVerifiedImages(cleanQuery, limit)

    if (imageSearchCache.size >= MAX_CACHE_ENTRIES) {
      const oldestKey = imageSearchCache.keys().next().value
      if (oldestKey) imageSearchCache.delete(oldestKey)
    }
    imageSearchCache.set(cacheKey, { timestamp: Date.now(), images: finalImages })

    return NextResponse.json({ success: true, images: finalImages })
  } catch (err: any) {
    console.error('search-image POST error:', err)
    return NextResponse.json({ success: false, error: err.message, images: [] }, { status: 500 })
  }
}

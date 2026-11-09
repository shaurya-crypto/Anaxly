import { NextRequest, NextResponse } from 'next/server'

interface ImageResult {
  url: string
  title: string
  description: string
  width: number
  height: number
  source?: string
}

// In-memory cache for fast repeated queries (24-hour TTL)
const imageSearchCache = new Map<string, { timestamp: number; images: ImageResult[] }>()
const CACHE_TTL_MS = 24 * 60 * 60 * 1000 // 24 hours
const MAX_CACHE_ENTRIES = 500

function sanitizeTitle(raw: string): string {
  return raw
    .replace(/^File:/i, '')
    .replace(/\.[a-zA-Z0-9]{3,4}$/, '')
    .replace(/[_]+/g, ' ')
    .trim()
}

const WIKIMEDIA_USER_AGENT = 'SobiAITutor/2.0 (https://sobi-ai-tutor.edu; mailto:support@sobi-ai-tutor.edu)'

// Fast low-latency link verification (1.5s timeout, parallel execution)
async function verifyImageLink(url: string): Promise<boolean> {
  if (!url || (!url.startsWith('http://') && !url.startsWith('https://'))) return false
  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 1800)
    const res = await fetch(url, {
      method: 'HEAD',
      signal: controller.signal,
      headers: {
        'User-Agent': WIKIMEDIA_USER_AGENT,
        'Accept': 'image/*,*/*',
      },
    })
    clearTimeout(timer)
    if (!res.ok) return false
    const contentType = (res.headers.get('content-type') || '').toLowerCase()
    return contentType.startsWith('image/') || contentType.includes('svg')
  } catch {
    return false
  }
}

async function searchWikimediaCommons(query: string, limit: number = 10): Promise<ImageResult[]> {
  try {
    const fetchLimit = Math.min(Math.max(limit * 3, 20), 40)
    const url = `https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=${encodeURIComponent(
      query
    )}&gsrnamespace=6&prop=imageinfo&iiprop=url|size|mime&format=json&gsrlimit=${fetchLimit}`

    const res = await fetch(url, {
      headers: {
        'User-Agent': WIKIMEDIA_USER_AGENT,
        Accept: 'application/json',
      },
      next: { revalidate: 86400 },
    })

    if (!res.ok) return []
    const data = await res.json()
    const pages = data.query?.pages || {}
    const results: ImageResult[] = []

    for (const page of Object.values<any>(pages)) {
      const info = page.imageinfo?.[0]
      if (!info?.url) continue

      const mime = (info.mime || '').toLowerCase()
      // Only accept modern web image formats
      if (!mime.startsWith('image/') || mime.includes('tiff') || mime.includes('djvu')) {
        continue
      }

      const isSvg = mime === 'image/svg+xml'
      const w = info.width || 0
      const h = info.height || 0

      // SVGs have vector scalability; for bitmaps, filter out tiny icons/thumbnails
      if (!isSvg && w > 0 && h > 0 && Math.max(w, h) < 400) {
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
    console.warn('[searchWikimediaCommons error]:', err)
    return []
  }
}

async function searchOpenverse(query: string, limit: number = 10): Promise<ImageResult[]> {
  try {
    const fetchLimit = Math.min(Math.max(limit * 2, 16), 30)
    const url = `https://api.openverse.org/v1/images/?q=${encodeURIComponent(query)}&page_size=${fetchLimit}`
    const res = await fetch(url, {
      headers: {
        'User-Agent': WIKIMEDIA_USER_AGENT,
        Accept: 'application/json',
      },
      next: { revalidate: 86400 },
    })

    if (!res.ok) return []
    const data = await res.json()
    const rawResults = data.results || []
    const results: ImageResult[] = []

    for (const r of rawResults) {
      if (!r.url) continue
      const w = r.width || 0
      const h = r.height || 0

      if ((w > 0 && w < 400) || (h > 0 && h < 300)) {
        continue
      }

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
    console.warn('[searchOpenverse error]:', err)
    return []
  }
}

function extractSmartImageSearchQueries(raw: string): string[] {
  const queries: string[] = []
  if (!raw || !raw.trim()) return queries
  const clean = raw.trim().replace(/^["']|["']$/g, '')

  // 1. Direct parenthetical match (e.g. "(Onion Peel Mount)" -> "Onion Peel cells microscope")
  const parenMatch = clean.match(/\(([^\)]+)\)/)
  if (parenMatch && parenMatch[1]) {
    const inside = parenMatch[1]
      .replace(/^(activity|module|step|exp|experiment)\s*[\d\.]*/i, '')
      .replace(/mount|mounts/i, 'cells')
      .trim()
    if (inside.length > 2) {
      queries.push(`${inside} microscope`)
      queries.push(`${inside} cells`)
      queries.push(inside)
    }
  }

  // 2. Colon prefix/title (e.g. "Activity 2.1 (Onion Peel Mount): Stripping..." -> "Onion Peel cells microscope")
  if (clean.includes(':')) {
    const beforeColon = clean
      .split(':')[0]
      .replace(/^Activity\s*[\d\.]+/i, '')
      .replace(/^Concept\s*[\d\.]+/i, '')
      .replace(/[\(\)]/g, '')
      .replace(/mount|mounts/i, 'cells')
      .trim()
    if (beforeColon.length > 2) {
      queries.push(`${beforeColon} microscope`)
      queries.push(beforeColon)
    }
  }

  // 3. Known subject keyword mappings
  const subjectPatterns: [RegExp, string][] = [
    [/onion\s*peel/i, 'Onion peel cells microscope'],
    [/allium\s*cepa/i, 'Allium cepa cells microscope'],
    [/human\s*cheek.*methylene|cheek.*methylene/i, 'Human Cheek Cells Methylene Blue Stain'],
    [/human\s*cheek/i, 'Human cheek cells microscope'],
    [/cheek\s*cell/i, 'Cheek cells microscope'],
    [/robert\s*hooke.*cork/i, 'Robert Hooke Micrographia cork cells 1665'],
    [/cork\s*cell/i, 'Cork cells microscope'],
    [/plant\s*cell\s*wall/i, 'Plant cell wall ultrastructure diagram'],
    [/plant\s*cell/i, 'Plant cell anatomy diagram'],
    [/animal\s*cell/i, 'Animal cell anatomy diagram'],
    [/chloroplast/i, 'Chloroplast structure diagram'],
    [/mitochondri[ao]/i, 'Mitochondria structure diagram'],
    [/nucleus/i, 'Cell nucleus structure diagram'],
    [/stomata/i, 'Leaf stomata guard cells microscope'],
    [/xylem/i, 'Xylem tissue microscope'],
    [/phloem/i, 'Phloem tissue microscope'],
    [/osmosis/i, 'Osmosis experiment diagram'],
    [/diffusion/i, 'Diffusion experiment diagram'],
  ]

  for (const [pat, target] of subjectPatterns) {
    if (pat.test(clean)) {
      queries.push(target)
      break
    }
  }

  // 4. Concise fallback
  if (clean.length <= 40) {
    queries.push(clean)
  } else {
    const words = clean
      .replace(/^Activity\s*[\d\.]+\s*[:\-\(]?/i, '')
      .replace(/[\(\)\[\]\{\}:,;]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim()
      .split(' ')
      .filter(
        (w) =>
          !/^(stripping|observing|mounting|with|and|the|of|in|to|a|an|is|are|for|by|from|into|large|small|regular)$/i.test(
            w
          )
      )
    if (words.length >= 2) {
      queries.push(words.slice(0, 3).join(' ') + ' microscope')
      queries.push(words.slice(0, 3).join(' '))
    }
  }

  return Array.from(new Set(queries.filter((q) => q && q.trim().length >= 3)))
}

async function getVerifiedImages(cleanQuery: string, limit: number): Promise<ImageResult[]> {
  const candidateQueries = extractSmartImageSearchQueries(cleanQuery)
  if (candidateQueries.length === 0) candidateQueries.push(cleanQuery.slice(0, 50))

  for (const query of candidateQueries) {
    const [wikiResults, ovResults] = await Promise.allSettled([
      searchWikimediaCommons(query, Math.max(limit, 8)),
      searchOpenverse(query, Math.max(limit, 8)),
    ])

    const combined: ImageResult[] = []
    const seenUrls = new Set<string>()

    if (wikiResults.status === 'fulfilled') {
      for (const img of wikiResults.value) {
        if (!seenUrls.has(img.url)) {
          seenUrls.add(img.url)
          combined.push(img)
        }
      }
    }

    if (ovResults.status === 'fulfilled') {
      for (const img of ovResults.value) {
        if (!seenUrls.has(img.url)) {
          seenUrls.add(img.url)
          combined.push(img)
        }
      }
    }

    if (combined.length > 0) {
      combined.sort((a, b) => {
        const aHigh =
          a.width >= 600 || a.height >= 600 || a.url.toLowerCase().endsWith('.svg') ? 1 : 0
        const bHigh =
          b.width >= 600 || b.height >= 600 || b.url.toLowerCase().endsWith('.svg') ? 1 : 0
        return bHigh - aHigh
      })

      // Low latency parallel verification of candidate images
      const candidateBatch = combined.slice(0, Math.min(combined.length, limit * 2))
      const verifications = await Promise.allSettled(
        candidateBatch.map((img) => verifyImageLink(img.url))
      )

      const verified: ImageResult[] = []
      for (let i = 0; i < candidateBatch.length; i++) {
        const v = verifications[i]
        if (v.status === 'fulfilled' && v.value) {
          verified.push(candidateBatch[i])
          if (verified.length >= limit) break
        }
      }

      if (verified.length > 0) {
        return verified
      }
    }
  }

  return []
}

export async function GET(req: NextRequest) {
  const searchParams = req.nextUrl.searchParams
  const query = searchParams.get('q') || searchParams.get('query') || ''
  const limit = parseInt(searchParams.get('limit') || '10', 10)

  if (!query.trim()) {
    return NextResponse.json({ success: true, images: [] })
  }

  const cleanQuery = query.trim().replace(/^["']|["']$/g, '')
  const cacheKey = `${cleanQuery.toLowerCase()}_${limit}`

  const cached = imageSearchCache.get(cacheKey)
  if (cached && Date.now() - cached.timestamp < CACHE_TTL_MS) {
    return NextResponse.json({ success: true, images: cached.images, cached: true })
  }

  const finalImages = await getVerifiedImages(cleanQuery, limit)

  if (imageSearchCache.size >= MAX_CACHE_ENTRIES) {
    const oldestKey = imageSearchCache.keys().next().value
    if (oldestKey) imageSearchCache.delete(oldestKey)
  }
  imageSearchCache.set(cacheKey, { timestamp: Date.now(), images: finalImages })

  return NextResponse.json({ success: true, images: finalImages })
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
    if (cached && Date.now() - cached.timestamp < CACHE_TTL_MS) {
      return NextResponse.json({ success: true, images: cached.images, cached: true })
    }

    const finalImages = await getVerifiedImages(cleanQuery, limit)

    if (imageSearchCache.size >= MAX_CACHE_ENTRIES) {
      const oldestKey = imageSearchCache.keys().next().value
      if (oldestKey) imageSearchCache.delete(oldestKey)
    }
    imageSearchCache.set(cacheKey, { timestamp: Date.now(), images: finalImages })

    return NextResponse.json({ success: true, images: finalImages })
  } catch (err: any) {
    console.error('search-image route error:', err)
    return NextResponse.json({ success: false, error: err.message, images: [] }, { status: 500 })
  }
}

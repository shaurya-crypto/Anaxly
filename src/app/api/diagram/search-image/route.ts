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
 * Fast low-latency image link verification (2.5s timeout, parallel execution).
 * Tests HEAD first; if server rejects with 403 or 405, falls back to a 1KB range GET.
 * Strictly verifies browser-renderable image formats (JPEG, PNG, WebP, SVG, AVIF, GIF).
 */
async function verifyImageLink(url: string): Promise<boolean> {
  if (!url || (!url.startsWith('http://') && !url.startsWith('https://'))) return false
  if (isDisallowedExtension(url)) return false

  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 2500)

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
 * Strict Pedagogical Relevance Filter:
 * Ensures the retrieved image is genuinely about the requested curriculum concept,
 * preventing cross-topic ad or carousel images (e.g. CH4 hybridization returned for cell peel).
 */
function isImageRelevantToQuery(query: string, title: string, url: string): boolean {
  if (!query || !query.trim()) return true

  const stopWords = new Set([
    'the', 'and', 'for', 'with', 'under', 'from', 'into', 'class', 'ncert', 'cbse',
    'diagram', 'figure', 'image', 'picture', 'photo', 'drawing', 'illustration', 'activity',
    'module', 'chapter', 'part', 'step', 'experiment', 'lab', 'section'
  ])

  // Extract substantive tokens (at least 3 characters)
  const queryTokens = query
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, ' ')
    .split(/\s+/)
    .filter((w) => w.length >= 3 && !stopWords.has(w))

  if (queryTokens.length === 0) return true

  const target = `${title} ${url}`.toLowerCase()

  // Match count of query keywords
  const matchedTokens = queryTokens.filter((token) => target.includes(token))

  if (matchedTokens.length === 0) {
    return false
  }

  // Cross-domain mismatch guards
  const isBiologyQuery = /cell|tissue|organelle|plant|animal|onion|cheek|microscope|epiderm|stomata|xylem|phloem/i.test(query)
  if (isBiologyQuery && /hybridization|ch4|alkane|benzene|car|automobile|actor|movie|song|fashion|dress|crypto/i.test(target)) {
    return false
  }

  const isPhysicsOpticsQuery = /mirror|lens|refraction|reflection|prism|light|ray|focal/i.test(query)
  if (isPhysicsOpticsQuery && /cell|tissue|blood|bacteria|organelle/i.test(target)) {
    return false
  }

  // Reject political / election results when query is educational math/science/logic
  if (/\b(?:proposition\s*\d+|ballot|election|referendum|county results|voter|campaign|caucus|primary)\b/i.test(target)) {
    if (!/election|ballot|vote|referendum|politics/i.test(query)) {
      return false
    }
  }

  return true
}

/**
 * Strict Content Safety and Watermark/Anti-Hotlink Filter:
 * Ensures harmful, adult, gambling, violence, or broken watermarked stock images are never returned.
 */
const HARMFUL_IMAGE_PATTERNS = [
  /\b(?:porn|pornography|sex|sexual|nsfw|erotic|nude|nudity|escort|dating|bikini|lingerie)\b/i,
  /\b(?:gore|murder|corpse|execution|suicide|decapitat|mutilat|bloodshed)\b/i,
  /\b(?:casino|gambling|betting|poker|slots|crypto|bitcoin|forex)\b/i,
  /\b(?:shutterstock|gettyimages|alamy|dreamstime|123rf|istockphoto|stock-photo|depositphotos)\b/i,
  /\b(?:pinterest\.com|pinimg\.com)\b/i,
]

function isSafeEducationalImage(title: string, url: string): boolean {
  const combined = `${title} ${url}`.toLowerCase()
  for (const pattern of HARMFUL_IMAGE_PATTERNS) {
    if (pattern.test(combined)) {
      return false
    }
  }
  return true
}

/**
 * Educational Domain Scoring:
 * Computes priority weight for search candidates.
 * User Invariant Mandate: Search Engine FIRST, Wikipedia as SECOND, Wikimedia THIRD.
 */
function scoreEducationalImage(url: string, title: string, query: string, source?: string): number {
  let score = 0
  const lowerUrl = url.toLowerCase()
  const lowerTitle = title.toLowerCase()
  const lowerSource = (source || '').toLowerCase()

  // 1. Search Engine (Bing Images / Web Search Engine) prioritized FIRST (+70 points)
  if (lowerSource.includes('bing') || lowerSource.includes('search engine') || lowerSource.includes('web')) {
    score += 70
  }
  // 2. Authoritative Wikipedia PageImages queried SECOND (+35 points)
  else if (lowerSource.includes('wikipedia')) {
    score += 35
  }
  // 3. Wikimedia Commons queried THIRD (+15 points)
  else if (lowerSource.includes('wikimedia')) {
    score += 15
  }

  // High authority educational domains
  if (lowerUrl.includes('.edu') || lowerUrl.includes('.gov') || lowerUrl.includes('.ac.in')) score += 30
  if (lowerUrl.includes('openstax.org') || lowerUrl.includes('khanacademy.org')) score += 25
  if (lowerUrl.includes('libretexts.org') || lowerUrl.includes('sciencedirect.com')) score += 20
  if (lowerUrl.includes('britannica.com') || lowerUrl.includes('physicsclassroom.com')) score += 20
  if (lowerUrl.includes('phet.colorado.edu') || lowerUrl.includes('ck12.org')) score += 20

  // Diagram / vector / formula / experiment keywords in title
  if (/diagram|schematic|ray diagram|cross section|ultrastructure|circuit|apparatus|truth table|logic diagram|geometry|graph/i.test(lowerTitle)) score += 20
  if (/experiment|observation|microscope|vector|formula|proof|solution|concept/i.test(lowerTitle)) score += 10

  // Strict negative penalty for political ballot propositions, election results, party politics
  if (/\b(?:proposition\s*\d+|ballot|election|referendum|county results|voter|campaign|caucus|primary)\b/i.test(lowerTitle)) {
    score -= 150
  }

  return score
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
    // Propositional logic & truth tables
    else if (lq.includes('proposition') || (lq.includes('statement') && (lq.includes('truth') || lq.includes('logic')))) {
      expanded.push('Propositional logic truth table diagram')
      expanded.push('truth table logic diagram')
      expanded.push('statement proposition logic')
    }
    // Quadrilaterals & parallelograms
    else if (lq.includes('quadrilateral') || lq.includes('parallelogram')) {
      expanded.push('Parallelogram properties geometry diagram')
      expanded.push('types of quadrilaterals geometry diagram')
    }
    // Linear equations
    else if (lq.includes('linear equation') || (lq.includes('linear') && lq.includes('graph'))) {
      expanded.push('Linear equation in two variables graph diagram')
      expanded.push('graph of linear equation coordinate plane')
    }
    // Surface areas and volumes
    else if (lq.includes('surface area') || lq.includes('volume') || lq.includes('cylinder') || lq.includes('cone')) {
      expanded.push('Surface area volume cylinder cone formula diagram')
    }
    // Statistics & Data
    else if (lq.includes('frequency polygon') || lq.includes('histogram') || lq.includes('statistics')) {
      expanded.push('Histogram frequency polygon statistics diagram')
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
 * Prioritized FIRST as primary search engine source.
 */
async function searchBingImages(query: string, limit: number = 8): Promise<ImageResult[]> {
  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 3500)
    const cleanTerm = /diagram|chart|graph|figure|experiment|photo|illustration/i.test(query)
      ? query
      : `${query} diagram`
    const url = `https://www.bing.com/images/async?q=${encodeURIComponent(
      cleanTerm
    )}&first=1&count=${Math.max(limit * 2, 12)}&mmasync=1&adlt=strict`

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

    const matches = [...html.matchAll(/&quot;murl&quot;:&quot;(https?:\/\/[^&"]+)&quot;[\s\S]*?&quot;t&quot;:&quot;([^&"]*)&quot;/g)]
    const altMatches = [...html.matchAll(/&quot;t&quot;:&quot;([^&"]*)&quot;[\s\S]*?&quot;murl&quot;:&quot;(https?:\/\/[^&"]+)&quot;/g)]

    const candidates = [
      ...matches.map((m) => ({ url: m[1], title: m[2] })),
      ...altMatches.map((m) => ({ url: m[2], title: m[1] })),
    ]

    for (const cand of candidates) {
      const imgUrl = cand.url
      if (!imgUrl || seenUrls.has(imgUrl) || isDisallowedExtension(imgUrl)) continue

      let rawTitle = cand.title || query
      rawTitle = rawTitle
        .replace(/&amp;/g, '&')
        .replace(/&#39;/g, "'")
        .replace(/&quot;/g, '"')
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>')
        .trim()

      // Content safety guard
      if (!isSafeEducationalImage(rawTitle, imgUrl)) {
        continue
      }

      // Strict relevance validation: Must match query topic
      if (!isImageRelevantToQuery(query, rawTitle, imgUrl)) {
        continue
      }

      seenUrls.add(imgUrl)
      results.push({
        url: imgUrl,
        title: rawTitle || query,
        description: rawTitle || `Web visual for ${query}`,
        width: 800,
        height: 600,
        source: 'Web Search Engine (Bing Images)',
      })

      if (results.length >= limit) break
    }

    return results
  } catch (err: any) {
    if (err?.name !== 'AbortError') {
      console.warn('[searchBingImages notice]:', err?.message || err)
    }
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
    const timer = setTimeout(() => controller.abort(), 4000)
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
      if (!isImageRelevantToQuery(query, title, thumbUrl)) {
        continue
      }

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
  } catch (err: any) {
    if (err?.name !== 'AbortError') {
      console.warn('[searchWikipediaPageImages notice]:', err?.message || err)
    }
    return []
  }
}

/**
 * TIER 1C: Openverse Creative Commons API.
 * Clean, openly licensed educational media with strict web format filtering.
 */
async function searchOpenverse(query: string, limit: number = 8): Promise<ImageResult[]> {
  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 3500)
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
      const title = (r.title || query).trim()
      if (!isImageRelevantToQuery(query, title, r.url)) {
        continue
      }

      const w = r.width || 0
      const h = r.height || 0
      if ((w > 0 && w < 250) || (h > 0 && h < 200)) continue

      results.push({
        url: r.url,
        title,
        description: r.attribution || r.title || 'Openverse Creative Commons Visual',
        width: w || 800,
        height: h || 600,
        source: 'Openverse',
      })
    }

    return results
  } catch (err: any) {
    if (err?.name !== 'AbortError') {
      console.warn('[searchOpenverse notice]:', err?.message || err)
    }
    return []
  }
}

/**
 * TIER 2: Wikimedia Commons API.
 * Encyclopedic repository with filetype filtering for clean educational vector drawings and photos.
 */
async function searchWikimediaCommons(query: string, limit: number = 8): Promise<ImageResult[]> {
  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 4000)
    const fetchLimit = Math.min(Math.max(limit * 2, 10), 20)

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

      const title = sanitizeTitle(page.title || query)
      if (!isSafeEducationalImage(title, info.url)) {
        continue
      }
      if (!isImageRelevantToQuery(query, title, info.url)) {
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
        title,
        description: `Wikimedia Commons scientific asset: ${title}`,
        width: isSvg ? Math.max(w, 800) : (w || 800),
        height: isSvg ? Math.max(h, 600) : (h || 600),
        source: 'Wikimedia Commons',
      })
      if (results.length >= limit) break
    }

    return results
  } catch (err: any) {
    if (err?.name !== 'AbortError') {
      console.warn('[searchWikimediaCommons notice]:', err?.message || err)
    }
    return []
  }
}

/**
 * Executes Fast Parallel Multi-Source Image Search:
 * 1. Search Engine (Bing Images & Web Image Search) prioritized FIRST per user instruction.
 * 2. Wikipedia Encyclopedic lead illustrations queried SECOND as high-authority reference.
 * 3. Wikimedia Commons scientific diagrams & vector graphics queried THIRD.
 * 4. Verifies top candidate links in parallel with 2.5s timeout.
 * 5. If no verified relevant image is found, cleanly returns [] so live classroom fast AI diagram generation activates!
 */
async function getVerifiedImages(cleanQuery: string, limit: number): Promise<ImageResult[]> {
  const candidateQueries = extractSmartImageSearchQueries(cleanQuery)
  const primaryQuery = candidateQueries[0] || cleanQuery

  // Query top sources in parallel for fast low-latency response
  const [bingRes, wikiPageRes, wikimediaRes] = await Promise.allSettled([
    searchBingImages(primaryQuery, limit),
    searchWikipediaPageImages(primaryQuery, limit),
    searchWikimediaCommons(primaryQuery, limit),
  ])

  const candidates: ImageResult[] = []
  const seenUrls = new Set<string>()

  // 1. Search Engine (Bing Images / Web Search) FIRST
  if (bingRes.status === 'fulfilled') {
    for (const img of bingRes.value) {
      if (!seenUrls.has(img.url)) {
        seenUrls.add(img.url)
        candidates.push(img)
      }
    }
  }

  // 2. Authoritative Wikipedia encyclopedic illustrations SECOND
  if (wikiPageRes.status === 'fulfilled') {
    for (const img of wikiPageRes.value) {
      if (!seenUrls.has(img.url)) {
        seenUrls.add(img.url)
        candidates.push(img)
      }
    }
  }

  // 3. Curated Wikimedia Commons scientific diagrams THIRD
  if (wikimediaRes.status === 'fulfilled') {
    for (const img of wikimediaRes.value) {
      if (!seenUrls.has(img.url)) {
        seenUrls.add(img.url)
        candidates.push(img)
      }
    }
  }

  // If primary query yielded zero candidates and a secondary refined query exists, try secondary
  if (candidates.length === 0 && candidateQueries.length > 1) {
    const secondaryQuery = candidateQueries[1]
    const [secBing, secWiki, secCommons] = await Promise.allSettled([
      searchBingImages(secondaryQuery, limit),
      searchWikipediaPageImages(secondaryQuery, limit),
      searchWikimediaCommons(secondaryQuery, limit),
    ])
    if (secBing.status === 'fulfilled') {
      for (const img of secBing.value) {
        if (!seenUrls.has(img.url)) {
          seenUrls.add(img.url)
          candidates.push(img)
        }
      }
    }
    if (secWiki.status === 'fulfilled') {
      for (const img of secWiki.value) {
        if (!seenUrls.has(img.url)) {
          seenUrls.add(img.url)
          candidates.push(img)
        }
      }
    }
    if (secCommons.status === 'fulfilled') {
      for (const img of secCommons.value) {
        if (!seenUrls.has(img.url)) {
          seenUrls.add(img.url)
          candidates.push(img)
        }
      }
    }
  }

  if (candidates.length === 0) {
    return []
  }

  // Prioritize high-authority educational domains (.edu, .gov, wikipedia, wikimedia, openstax, etc.)
  // with Search Engine prioritized FIRST, Wikipedia SECOND, Wikimedia THIRD.
  candidates.sort((a, b) => {
    const scoreA = scoreEducationalImage(a.url, a.title, primaryQuery, a.source)
    const scoreB = scoreEducationalImage(b.url, b.title, primaryQuery, b.source)
    return scoreB - scoreA
  })

  // Parallel verification of the top candidates
  const batchToVerify = candidates.slice(0, Math.min(candidates.length, limit * 2))
  const verifications = await Promise.allSettled(
    batchToVerify.map(async (img) => ({
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

  return verified
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

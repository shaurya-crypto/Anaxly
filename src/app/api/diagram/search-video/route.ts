import { NextRequest, NextResponse } from 'next/server'

interface VideoResult {
  url: string
  title: string
  description: string
  mimeType: string
  thumbnailUrl?: string
  source?: string
}

// In-memory cache for fast repeated video queries (12-hour TTL)
const videoSearchCache = new Map<string, { timestamp: number; videos: VideoResult[] }>()
const CACHE_TTL_MS = 12 * 60 * 60 * 1000

const WIKIMEDIA_USER_AGENT = 'SobiAITutor/2.0 (https://sobi-ai-tutor.edu; mailto:support@sobi-ai-tutor.edu)'
const BROWSER_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

function sanitizeTitle(raw: string): string {
  return raw
    .replace(/^File:/i, '')
    .replace(/\.[a-zA-Z0-9]{3,4}$/, '')
    .replace(/[_]+/g, ' ')
    .trim()
}

/**
 * Strict Safety Guard for Online Videos:
 * Filters out harmful, adult, violent, prank, gambling, or music content.
 */
const HARMFUL_VIDEO_PATTERNS = [
  /\b(?:porn|pornography|sex|sexual|nsfw|erotic|nude|nudity|stripper|escort|dating)\b/i,
  /\b(?:gore|murder|decapitation|terrorist|isis|execution|beheading|suicide)\b/i,
  /\b(?:casino|gambling|betting|poker|slots|roulette|crypto|bitcoin|forex)\b/i,
  /\b(?:prank|troll|fight|brawl|drama|roast|gossip|vlog|tik\s*tok|challenge)\b/i,
  /\b(?:song|music\s*video|album|remix|dance|lyrics|concert|trailer|teaser)\b/i,
]

function isSafeEducationalVideo(title: string, description: string): boolean {
  const combined = `${title} ${description}`.toLowerCase()
  for (const pattern of HARMFUL_VIDEO_PATTERNS) {
    if (pattern.test(combined)) {
      return false
    }
  }
  return true
}

// Fast low-latency link verification (1.5s timeout, parallel execution)
async function verifyVideoLink(url: string): Promise<boolean> {
  if (!url || (!url.startsWith('http://') && !url.startsWith('https://'))) return false
  // YouTube videos are verified via their existence in search results and embed capability
  if (url.includes('youtube.com') || url.includes('youtu.be')) return true

  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 2000)
    const res = await fetch(url, {
      method: 'HEAD',
      signal: controller.signal,
      headers: {
        'User-Agent': WIKIMEDIA_USER_AGENT,
        'Accept': '*/*',
      },
    })
    clearTimeout(timer)
    if (!res.ok) return false
    const contentType = (res.headers.get('content-type') || '').toLowerCase()
    return contentType.startsWith('video/') || contentType.includes('webm') || contentType.includes('mp4') || contentType.includes('ogg')
  } catch {
    return false
  }
}

/**
 * TIER 1: Online Video Search Engine (YouTube & Web Video Search).
 * Prioritized FIRST per user mandate.
 */
async function searchOnlineVideos(query: string, limit: number = 5): Promise<VideoResult[]> {
  try {
    const cleanQ = query.trim().replace(/[^\w\s-]/g, ' ')
    let contextKeyword = 'educational demonstration'
    if (/math|geometry|algebra|equation|proposition|logic|graph|calculus|trigonometry|quadrilateral|polygon/i.test(cleanQ)) {
      contextKeyword = 'concept animation explanation'
    } else if (/cell|tissue|microscope|plant|animal|biology|organelle|stomata|blood|peel/i.test(cleanQ)) {
      contextKeyword = 'microscope lab experiment demonstration'
    } else if (/acid|base|reaction|chemistry|element|compound|molecule|atom/i.test(cleanQ)) {
      contextKeyword = 'chemistry lab experiment demonstration'
    } else if (/physics|motion|force|optics|light|ray|circuit|electric|lens|mirror|velocity|gravity/i.test(cleanQ)) {
      contextKeyword = 'physics experiment demonstration'
    }
    const searchUrl = `https://www.youtube.com/results?search_query=${encodeURIComponent(`${cleanQ} ${contextKeyword}`)}`
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 4000)

    const res = await fetch(searchUrl, {
      signal: controller.signal,
      headers: {
        'User-Agent': BROWSER_USER_AGENT,
        'Accept-Language': 'en-US,en;q=0.9',
      },
    })
    clearTimeout(timer)

    if (!res.ok) return []
    const html = await res.text()
    const m = html.match(/var ytInitialData = ({.*?});<\/script>/)
    if (!m) return []

    const data = JSON.parse(m[1])
    const sectionList = data?.contents?.twoColumnSearchResultsRenderer?.primaryContents?.sectionListRenderer?.contents || []
    const videos: VideoResult[] = []
    const seenIds = new Set<string>()

    for (const sec of sectionList) {
      const itemSection = sec?.itemSectionRenderer?.contents || []
      for (const item of itemSection) {
        const vr = item?.videoRenderer
        if (vr && vr.videoId && !seenIds.has(vr.videoId)) {
          seenIds.add(vr.videoId)
          const rawTitle = vr.title?.runs?.[0]?.text || vr.title?.simpleText || ''
          const title = rawTitle.replace(/[\(\)\[\]]/g, ' ').replace(/\s+/g, ' ').trim()
          if (!title || title.length < 3 || /playlist|channel|mix/i.test(title)) continue

          const desc = vr.detailedMetadataSnippets?.[0]?.snippetText?.runs?.map((r: any) => r.text).join('') || `Educational experiment demonstration: ${title}`
          if (!isSafeEducationalVideo(title, desc)) continue

          const thumb = vr.thumbnail?.thumbnails?.[0]?.url || `https://i.ytimg.com/vi/${vr.videoId}/hqdefault.jpg`

          videos.push({
            url: `https://www.youtube.com/watch?v=${vr.videoId}`,
            title: title || query,
            description: desc,
            mimeType: 'video/youtube',
            thumbnailUrl: thumb,
            source: 'Online Video Search (YouTube)',
          })

          if (videos.length >= limit) break
        }
      }
      if (videos.length >= limit) break
    }

    return videos
  } catch (err: any) {
    if (err?.name !== 'AbortError') {
      console.warn('[searchOnlineVideos notice]:', err?.message || err)
    }
    return []
  }
}

/**
 * TIER 2: Wikimedia Commons Videos (Secondary Fallback).
 * Curated open-source scientific animations and experimental recordings.
 */
async function searchWikimediaVideos(query: string, limit: number = 6): Promise<VideoResult[]> {
  try {
    const cleanQ = query.trim().replace(/[^\w\s-]/g, ' ')
    const searchTerms = [
      `${cleanQ} filemime:video/webm`,
      `${cleanQ} filemime:video`,
      `${cleanQ} filetype:video`,
    ]

    for (const term of searchTerms) {
      const url = `https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=${encodeURIComponent(
        term
      )}&gsrnamespace=6&prop=imageinfo&iiprop=url|size|mime|canonicaltitle&format=json&gsrlimit=${limit * 2}`

      const res = await fetch(url, {
        headers: {
          'User-Agent': WIKIMEDIA_USER_AGENT,
          Accept: 'application/json',
        },
      })

      if (!res.ok) continue
      const data = await res.json().catch(() => ({}))
      const pages = data.query?.pages || {}
      const results: VideoResult[] = []

      for (const page of Object.values<any>(pages)) {
        const info = page.imageinfo?.[0]
        if (!info?.url) continue
        const mime = (info.mime || '').toLowerCase()
        if (!mime.startsWith('video/')) continue

        const title = sanitizeTitle(page.title || query)
        if (!isSafeEducationalVideo(title, 'Scientific video demonstration')) continue

        results.push({
          url: info.url,
          title,
          description: `Scientific video demonstration: ${title}`,
          mimeType: mime,
          source: 'Wikimedia Commons Science Video',
        })
      }

      if (results.length > 0) {
        return results.slice(0, limit)
      }
    }

    return []
  } catch (err) {
    console.warn('[searchWikimediaVideos notice]:', err)
    return []
  }
}

export async function POST(req: Request) {
  try {
    const body = await req.json().catch(() => ({}))
    const query = (body.query || body.q || '').trim()
    const limit = parseInt(body.limit || '5', 10)

    if (!query) {
      return NextResponse.json({ success: true, videos: [] })
    }

    const cleanQuery = query.toLowerCase().replace(/^["']|["']$/g, '').trim()
    const cacheKey = `video_${cleanQuery}_${limit}`

    const cached = videoSearchCache.get(cacheKey)
    if (cached && Date.now() - cached.timestamp < CACHE_TTL_MS) {
      return NextResponse.json({ success: true, videos: cached.videos, cached: true })
    }

    // 1. Online Video Search Engine FIRST (YouTube / Web)
    const onlineVideos = await searchOnlineVideos(cleanQuery, limit)
    if (onlineVideos.length > 0) {
      videoSearchCache.set(cacheKey, { timestamp: Date.now(), videos: onlineVideos })
      return NextResponse.json({ success: true, videos: onlineVideos, totalFound: onlineVideos.length, source: 'online_search' })
    }

    // 2. Wikimedia Commons Videos SECOND (Fallback)
    const candidates = await searchWikimediaVideos(cleanQuery, limit)

    // Parallel low-latency link verification
    const checks = await Promise.allSettled(candidates.map((v) => verifyVideoLink(v.url)))
    const verified: VideoResult[] = []

    for (let i = 0; i < candidates.length; i++) {
      const ch = checks[i]
      if (ch.status === 'fulfilled' && ch.value) {
        verified.push(candidates[i])
      }
    }

    // Cache the verified results
    videoSearchCache.set(cacheKey, { timestamp: Date.now(), videos: verified })

    return NextResponse.json({ success: true, videos: verified, totalFound: verified.length, source: 'wikimedia_fallback' })
  } catch (err: any) {
    console.error('search-video route error:', err)
    return NextResponse.json({ success: false, error: err.message, videos: [] }, { status: 500 })
  }
}

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url)
  const query = searchParams.get('q') || searchParams.get('query') || ''
  const limit = parseInt(searchParams.get('limit') || '5', 10)

  if (!query) {
    return NextResponse.json({ success: true, videos: [] })
  }

  return POST(new Request(req.url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, limit })
  }))
}

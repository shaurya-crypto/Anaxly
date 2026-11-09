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

function sanitizeTitle(raw: string): string {
  return raw
    .replace(/^File:/i, '')
    .replace(/\.[a-zA-Z0-9]{3,4}$/, '')
    .replace(/[_]+/g, ' ')
    .trim()
}

// Fast low-latency link verification (1.5s timeout, parallel execution)
export async function verifyVideoLink(url: string): Promise<boolean> {
  if (!url || (!url.startsWith('http://') && !url.startsWith('https://'))) return false
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

// Search Wikimedia Commons videos using exact filemime syntax
async function searchWikimediaVideos(query: string, limit: number = 6): Promise<VideoResult[]> {
  try {
    // 1. First attempt: target webm/video files directly
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
    console.warn('[searchWikimediaVideos error]:', err)
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

    // Dynamic search across open scientific video index
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

    return NextResponse.json({ success: true, videos: verified, totalFound: verified.length })
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

  // Delegate to POST logic
  return POST(new Request(req.url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, limit })
  }))
}

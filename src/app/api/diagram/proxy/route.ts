import { NextRequest, NextResponse } from 'next/server'

// SSRF Safety Guard: Disallow private IP ranges and local hostnames
function isAllowedUrl(urlString: string): boolean {
  try {
    const parsed = new URL(urlString)
    if (parsed.protocol !== 'http:' && parsed.protocol !== 'https:') return false
    const host = parsed.hostname.toLowerCase()
    if (
      host === 'localhost' ||
      host === '127.0.0.1' ||
      host === '::1' ||
      host === '0.0.0.0' ||
      host.endsWith('.local') ||
      host.endsWith('.internal') ||
      host.endsWith('.localhost')
    ) {
      return false
    }

    // Comprehensive RFC 1918 CIDR and loopback check
    const ipv4Match = host.match(/^(\d+)\.(\d+)\.(\d+)\.(\d+)$/)
    if (ipv4Match) {
      const o1 = parseInt(ipv4Match[1], 10)
      const o2 = parseInt(ipv4Match[2], 10)
      if (o1 === 10) return false // 10.0.0.0/8
      if (o1 === 127) return false // 127.0.0.0/8 loopback
      if (o1 === 169 && o2 === 254) return false // 169.254.0.0/16 link-local
      if (o1 === 172 && o2 >= 16 && o2 <= 31) return false // 172.16.0.0/12 private
      if (o1 === 192 && o2 === 168) return false // 192.168.0.0/16 private
      if (o1 === 0) return false
    }
    return true
  } catch {
    return false
  }
}

// In-memory cache for proxied base64 data URLs (12-hour TTL)
const proxyCache = new Map<
  string,
  { dataURL: string; contentType: string; sizeBytes: number; timestamp: number }
>()
const PROXY_CACHE_TTL_MS = 12 * 60 * 60 * 1000 // 12 hours
const MAX_PROXY_CACHE = 400
const MAX_MEDIA_BYTES = 10 * 1024 * 1024 // 10MB payload cap

// In-memory cache for upstream 404 / 410 / 504 negative responses (5-minute TTL)
const negativeProxyCache = new Map<
  string,
  { status: number; error: string; timestamp: number }
>()
const NEGATIVE_CACHE_TTL_MS = 5 * 60 * 1000 // 5 minutes

const PROXY_TIMEOUT_MS = 3500 // Fast timeout for images
const PROXY_MEDIA_TIMEOUT_MS = 10000 // Relaxed timeout for audio/video media
const USER_AGENT =
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

export async function GET(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url)
    const targetUrl = searchParams.get('url')
    const returnDataUrl = searchParams.get('dataUrl') === 'true'

    if (!targetUrl || !isAllowedUrl(targetUrl)) {
      return NextResponse.json({ success: false, error: 'Invalid or forbidden URL' }, { status: 400 })
    }

    // Fast-path 1: Negative cache hit (known dead/404 URL fails in 0ms)
    const neg = negativeProxyCache.get(targetUrl)
    if (neg && Date.now() - neg.timestamp < NEGATIVE_CACHE_TTL_MS) {
      return NextResponse.json(
        { success: false, error: neg.error, cached: true },
        { status: neg.status }
      )
    }

    // Fast-path 2: Positive cache hit (repeated base64 dataURL returns in <5ms)
    if (returnDataUrl) {
      const cached = proxyCache.get(targetUrl)
      if (cached && Date.now() - cached.timestamp < PROXY_CACHE_TTL_MS) {
        return NextResponse.json({
          success: true,
          dataURL: cached.dataURL,
          contentType: cached.contentType,
          sizeBytes: cached.sizeBytes,
          cached: true,
        })
      }
    }

    const isMedia = !returnDataUrl || /\.(mp4|webm|ogv|mp3|ogg|wav)$/i.test(targetUrl)
    const timeout = isMedia ? PROXY_MEDIA_TIMEOUT_MS : PROXY_TIMEOUT_MS
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), timeout)

    const response = await fetch(targetUrl, {
      signal: controller.signal,
      headers: {
        'User-Agent': USER_AGENT,
        Accept: 'image/avif,image/webp,image/apng,image/svg+xml,image/*,video/*,audio/*,*/*;q=0.8',
      },
    })
    clearTimeout(timer)

    if (!response.ok) {
      const errStatus = response.status
      const errMsg = `Upstream HTTP ${errStatus}: ${response.statusText}`
      // Cache dead links (400, 403, 404, 410, 502, 503, 504) to avoid repeated upstream latency stalls
      if ([400, 403, 404, 410, 502, 503, 504].includes(errStatus)) {
        negativeProxyCache.set(targetUrl, { status: errStatus, error: errMsg, timestamp: Date.now() })
      }
      return NextResponse.json({ success: false, error: errMsg }, { status: errStatus })
    }

    // Check upstream content-length against 10MB cap
    const contentLength = parseInt(response.headers.get('content-length') || '0', 10)
    if (contentLength > MAX_MEDIA_BYTES) {
      return NextResponse.json({ success: false, error: 'Payload too large (exceeds 10MB cap)' }, { status: 413 })
    }

    const contentType = response.headers.get('content-type') || 'application/octet-stream'

    if (returnDataUrl) {
      const arrayBuffer = await response.arrayBuffer()
      if (arrayBuffer.byteLength > MAX_MEDIA_BYTES) {
        return NextResponse.json({ success: false, error: 'Payload too large (exceeds 10MB cap)' }, { status: 413 })
      }
      const base64 = Buffer.from(arrayBuffer).toString('base64')
      const dataURL = `data:${contentType};base64,${base64}`

      if (proxyCache.size >= MAX_PROXY_CACHE) {
        const oldest = proxyCache.keys().next().value
        if (oldest) proxyCache.delete(oldest)
      }
      proxyCache.set(targetUrl, {
        dataURL,
        contentType,
        sizeBytes: arrayBuffer.byteLength,
        timestamp: Date.now(),
      })

      return NextResponse.json({
        success: true,
        dataURL,
        contentType,
        sizeBytes: arrayBuffer.byteLength,
      })
    }

    // Direct media proxy stream
    const mediaBuffer = await response.arrayBuffer()
    if (mediaBuffer.byteLength > MAX_MEDIA_BYTES) {
      return NextResponse.json({ success: false, error: 'Payload too large (exceeds 10MB cap)' }, { status: 413 })
    }
    return new NextResponse(mediaBuffer, {
      status: 200,
      headers: {
        'Content-Type': contentType,
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Cache-Control': 'public, max-age=86400, stale-while-revalidate=43200',
      },
    })
  } catch (err: any) {
    const isTimeout = err.name === 'AbortError'
    const status = isTimeout ? 504 : 500
    const errorMsg = isTimeout ? `Upstream fetch timed out` : err.message || 'Proxy error'
    if (isTimeout) {
      const { searchParams } = new URL(req.url)
      const targetUrl = searchParams.get('url')
      if (targetUrl) {
        negativeProxyCache.set(targetUrl, { status: 504, error: errorMsg, timestamp: Date.now() })
      }
    }
    return NextResponse.json(
      { success: false, error: errorMsg },
      { status }
    )
  }
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json().catch(() => ({}))
    const targetUrl = body.url
    const returnDataUrl = body.dataUrl !== false

    if (!targetUrl || !isAllowedUrl(targetUrl)) {
      return NextResponse.json({ success: false, error: 'Invalid or forbidden URL' }, { status: 400 })
    }

    // Fast-path 1: Negative cache hit
    const neg = negativeProxyCache.get(targetUrl)
    if (neg && Date.now() - neg.timestamp < NEGATIVE_CACHE_TTL_MS) {
      return NextResponse.json(
        { success: false, error: neg.error, cached: true },
        { status: neg.status }
      )
    }

    // Fast-path 2: Positive cache hit
    if (returnDataUrl) {
      const cached = proxyCache.get(targetUrl)
      if (cached && Date.now() - cached.timestamp < PROXY_CACHE_TTL_MS) {
        return NextResponse.json({
          success: true,
          dataURL: cached.dataURL,
          contentType: cached.contentType,
          sizeBytes: cached.sizeBytes,
          cached: true,
        })
      }
    }

    const isMedia = !returnDataUrl || /\.(mp4|webm|ogv|mp3|ogg|wav)$/i.test(targetUrl)
    const timeout = isMedia ? PROXY_MEDIA_TIMEOUT_MS : PROXY_TIMEOUT_MS
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), timeout)

    const response = await fetch(targetUrl, {
      signal: controller.signal,
      headers: {
        'User-Agent': USER_AGENT,
        Accept: 'image/avif,image/webp,image/apng,image/svg+xml,image/*,video/*,audio/*,*/*;q=0.8',
      },
    })
    clearTimeout(timer)

    if (!response.ok) {
      const errStatus = response.status
      const errMsg = `Upstream HTTP ${errStatus}: ${response.statusText}`
      if ([400, 403, 404, 410, 502, 503, 504].includes(errStatus)) {
        negativeProxyCache.set(targetUrl, { status: errStatus, error: errMsg, timestamp: Date.now() })
      }
      return NextResponse.json({ success: false, error: errMsg }, { status: errStatus })
    }

    const contentLength = parseInt(response.headers.get('content-length') || '0', 10)
    if (contentLength > MAX_MEDIA_BYTES) {
      return NextResponse.json({ success: false, error: 'Payload too large (exceeds 10MB cap)' }, { status: 413 })
    }

    const contentType = response.headers.get('content-type') || 'application/octet-stream'

    if (returnDataUrl) {
      const arrayBuffer = await response.arrayBuffer()
      if (arrayBuffer.byteLength > MAX_MEDIA_BYTES) {
        return NextResponse.json({ success: false, error: 'Payload too large (exceeds 10MB cap)' }, { status: 413 })
      }
      const base64 = Buffer.from(arrayBuffer).toString('base64')
      const dataURL = `data:${contentType};base64,${base64}`

      if (proxyCache.size >= MAX_PROXY_CACHE) {
        const oldest = proxyCache.keys().next().value
        if (oldest) proxyCache.delete(oldest)
      }
      proxyCache.set(targetUrl, {
        dataURL,
        contentType,
        sizeBytes: arrayBuffer.byteLength,
        timestamp: Date.now(),
      })

      return NextResponse.json({
        success: true,
        dataURL,
        contentType,
        sizeBytes: arrayBuffer.byteLength,
      })
    }

    const mediaBuffer = await response.arrayBuffer()
    if (mediaBuffer.byteLength > MAX_MEDIA_BYTES) {
      return NextResponse.json({ success: false, error: 'Payload too large (exceeds 10MB cap)' }, { status: 413 })
    }
    return new NextResponse(mediaBuffer, {
      status: 200,
      headers: {
        'Content-Type': contentType,
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Cache-Control': 'public, max-age=86400, stale-while-revalidate=43200',
      },
    })
  } catch (err: any) {
    const isTimeout = err.name === 'AbortError'
    const status = isTimeout ? 504 : 500
    const errorMsg = isTimeout ? `Upstream fetch timed out` : err.message || 'Proxy error'
    return NextResponse.json(
      { success: false, error: errorMsg },
      { status }
    )
  }
}

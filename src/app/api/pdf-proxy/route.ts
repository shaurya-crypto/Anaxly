import { NextRequest, NextResponse } from 'next/server'

// In-memory cache for recent PDF buffers (6-hour TTL) to make page jumps instantaneous
const pdfCache = new Map<string, { buffer: ArrayBuffer; contentType: string; filename: string; timestamp: number }>()
const PDF_CACHE_TTL_MS = 6 * 60 * 60 * 1000 // 6 hours
const MAX_PDF_CACHE_ENTRIES = 50

export async function GET(req: NextRequest) {
  const urlParam = req.nextUrl.searchParams.get('url')
  if (!urlParam) {
    return new NextResponse('Missing required "url" parameter', { status: 400 })
  }

  try {
    const targetUrl = new URL(urlParam)
    const hostname = targetUrl.hostname.toLowerCase()

    // Strict domain whitelist: Only stream official NCERT textbooks
    if (hostname !== 'ncert.nic.in' && !hostname.endsWith('.ncert.nic.in')) {
      return new NextResponse('Forbidden: Only official NCERT textbook PDFs (ncert.nic.in) may be streamed.', {
        status: 403,
      })
    }

    const filename = targetUrl.pathname.split('/').pop() || 'textbook.pdf'
    const cacheKey = targetUrl.pathname.toLowerCase()

    // Check memory cache
    const cached = pdfCache.get(cacheKey)
    const now = Date.now()
    if (cached && now - cached.timestamp < PDF_CACHE_TTL_MS) {
      const headers = new Headers()
      headers.set('Content-Type', cached.contentType)
      headers.set('Content-Disposition', `inline; filename="${cached.filename}"`)
      headers.set('Cache-Control', 'public, max-age=86400, stale-while-revalidate=604800')
      headers.set('Access-Control-Allow-Origin', '*')

      return new NextResponse(cached.buffer, {
        status: 200,
        headers,
      })
    }

    // Fetch upstream official NCERT PDF
    const upstreamRes = await fetch(targetUrl.toString(), {
      headers: {
        'User-Agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        Accept: 'application/pdf,application/octet-stream,*/*',
      },
    })

    if (!upstreamRes.ok) {
      return new NextResponse(`Upstream NCERT returned status ${upstreamRes.status}: ${upstreamRes.statusText}`, {
        status: upstreamRes.status,
      })
    }

    const contentType = upstreamRes.headers.get('content-type') || 'application/pdf'
    const arrayBuffer = await upstreamRes.arrayBuffer()

    // Save to cache (evict oldest if full)
    if (pdfCache.size >= MAX_PDF_CACHE_ENTRIES) {
      const oldestKey = pdfCache.keys().next().value
      if (oldestKey) pdfCache.delete(oldestKey)
    }
    pdfCache.set(cacheKey, {
      buffer: arrayBuffer,
      contentType,
      filename,
      timestamp: now,
    })

    const headers = new Headers()
    headers.set('Content-Type', contentType)
    headers.set('Content-Disposition', `inline; filename="${filename}"`)
    headers.set('Cache-Control', 'public, max-age=86400, stale-while-revalidate=604800')
    headers.set('Access-Control-Allow-Origin', '*')
    // Omit X-Frame-Options: SAMEORIGIN so it renders seamlessly inside the SideBookViewer iframe

    return new NextResponse(arrayBuffer, {
      status: 200,
      headers,
    })
  } catch (err: any) {
    console.error('[pdf-proxy] Error streaming NCERT PDF:', err)
    return new NextResponse(`PDF Proxy error: ${err.message || 'Unknown error'}`, { status: 500 })
  }
}

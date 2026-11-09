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
      host.endsWith('.local') ||
      host.endsWith('.internal') ||
      host.startsWith('10.') ||
      host.startsWith('192.168.') ||
      host.startsWith('172.16.') ||
      host.startsWith('169.254.')
    ) {
      return false
    }
    return true
  } catch {
    return false
  }
}

export async function GET(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url)
    const targetUrl = searchParams.get('url')
    const returnDataUrl = searchParams.get('dataUrl') === 'true'

    if (!targetUrl || !isAllowedUrl(targetUrl)) {
      return NextResponse.json({ success: false, error: 'Invalid or forbidden URL' }, { status: 400 })
    }

    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 8000)

    const response = await fetch(targetUrl, {
      signal: controller.signal,
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': '*/*',
      },
    })
    clearTimeout(timer)

    if (!response.ok) {
      return NextResponse.json(
        { success: false, error: `Upstream HTTP ${response.status}: ${response.statusText}` },
        { status: response.status }
      )
    }

    const contentType = response.headers.get('content-type') || 'application/octet-stream'

    if (returnDataUrl) {
      const arrayBuffer = await response.arrayBuffer()
      const base64 = Buffer.from(arrayBuffer).toString('base64')
      const dataURL = `data:${contentType};base64,${base64}`
      return NextResponse.json({
        success: true,
        dataURL,
        contentType,
        sizeBytes: arrayBuffer.byteLength,
      })
    }

    // Direct media proxy stream
    const mediaBuffer = await response.arrayBuffer()
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
    console.error('[/api/diagram/proxy error]:', err)
    return NextResponse.json({ success: false, error: err.message || 'Proxy error' }, { status: 500 })
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

    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 8000)

    const response = await fetch(targetUrl, {
      signal: controller.signal,
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': '*/*',
      },
    })
    clearTimeout(timer)

    if (!response.ok) {
      return NextResponse.json(
        { success: false, error: `Upstream HTTP ${response.status}: ${response.statusText}` },
        { status: response.status }
      )
    }

    const contentType = response.headers.get('content-type') || 'application/octet-stream'

    if (returnDataUrl) {
      const arrayBuffer = await response.arrayBuffer()
      const base64 = Buffer.from(arrayBuffer).toString('base64')
      const dataURL = `data:${contentType};base64,${base64}`
      return NextResponse.json({
        success: true,
        dataURL,
        contentType,
        sizeBytes: arrayBuffer.byteLength,
      })
    }

    const mediaBuffer = await response.arrayBuffer()
    return new NextResponse(mediaBuffer, {
      status: 200,
      headers: {
        'Content-Type': contentType,
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'public, max-age=86400',
      },
    })
  } catch (err: any) {
    console.error('[/api/diagram/proxy POST error]:', err)
    return NextResponse.json({ success: false, error: err.message || 'Proxy error' }, { status: 500 })
  }
}

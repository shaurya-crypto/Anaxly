import { NextRequest, NextResponse } from 'next/server'

export const dynamic = 'force-dynamic'

/**
 * PDF Proxy / Redirector for Official NCERT Online Textbooks.
 * Safely redirects client requests directly to official NCERT URLs,
 * preventing server-side socket resets (ECONNRESET) while preserving
 * target page anchors and query parameters.
 */
export async function GET(req: NextRequest) {
  const urlParam = req.nextUrl.searchParams.get('url')
  if (!urlParam) {
    return new NextResponse('Missing required "url" parameter', { status: 400 })
  }

  try {
    const targetUrl = new URL(urlParam)
    const hostname = targetUrl.hostname.toLowerCase()

    // Strict domain whitelist: Only redirect to official NCERT textbook PDFs
    if (hostname !== 'ncert.nic.in' && !hostname.endsWith('.ncert.nic.in')) {
      return new NextResponse('Forbidden: Only official NCERT textbook PDFs (ncert.nic.in) are supported.', {
        status: 403,
      })
    }

    // Direct 307 Temporary Redirect to the official online NCERT PDF
    return NextResponse.redirect(targetUrl.toString(), 307)
  } catch (err: any) {
    console.error('[pdf-proxy] Invalid URL redirect request:', err.message || err)
    return new NextResponse(`Invalid URL: ${err.message || 'Malformed URL'}`, { status: 400 })
  }
}

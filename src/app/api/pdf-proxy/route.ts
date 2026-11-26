import { NextRequest, NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'
import { Readable } from 'stream'

export const dynamic = 'force-dynamic'
export const runtime = 'nodejs'

const ALLOWED_LOCAL_ROOTS = ['9', '10', '11', '12']

/**
 * Safely extracts and validates a canonical NCERT/textbook PDF filename
 * from ?file=... or ?url=... while blocking directory traversal.
 */
function extractSafeFilename(rawParam: string): string | null {
  if (!rawParam) return null
  let cleaned = rawParam.trim()

  // Strip query/hash fragments
  cleaned = cleaned.split('#')[0].split('?')[0]

  // If full URL was passed, validate allowed origins or extract basename
  if (/^https?:\/\//i.test(cleaned)) {
    try {
      const parsed = new URL(cleaned)
      const host = parsed.hostname.toLowerCase()
      const isAllowedHost =
        host === 'ncert.nic.in' ||
        host.endsWith('.ncert.nic.in') ||
        host.endsWith('.supabase.co')
      if (!isAllowedHost) {
        return null
      }
      cleaned = parsed.pathname
    } catch {
      return null
    }
  }

  // Reject path traversal
  if (cleaned.includes('..')) return null

  const base = path.posix.basename(cleaned.replace(/\\/g, '/')).trim()
  const normalized = base.replace(/\s*\(\d+\)/g, '').toLowerCase()
  if (!/^[a-z0-9][a-z0-9_-]{1,64}\.pdf$/i.test(normalized)) {
    return null
  }
  return normalized
}

// In-memory index of local public/{9,10,11,12}/**/*.pdf so repeated Range requests are O(1)
let localPdfIndexCache: Map<string, string> | null = null

function getLocalPdfPath(filename: string): string | null {
  const publicDir = path.join(process.cwd(), 'public')

  // Fast deterministic path map before scanning
  const m = filename.match(/^([a-z]+)(\d)(\d\d)\.pdf$/)
  if (m) {
    const [, code, pt, num] = m
    const candidates: string[] = []
    if (code === 'iemh') candidates.push(path.join(publicDir, '9', 'class9_maths', `pt${pt}`, filename))
    if (code === 'iesc') candidates.push(path.join(publicDir, '9', 'class 9th science', filename))
    if (code === 'jemh') candidates.push(path.join(publicDir, '10', 'class10_maths', filename))
    if (code === 'jesc') candidates.push(path.join(publicDir, '10', 'class10_science', filename))
    if (code === 'kemh') candidates.push(path.join(publicDir, '11', 'class11_maths', filename))
    if (code === 'keph') candidates.push(path.join(publicDir, '11', 'class11_physics', `pt${pt}`, filename))
    if (code === 'kech') candidates.push(path.join(publicDir, '11', 'class11_chem', `pt${pt}`, filename))
    if (code === 'kebo') candidates.push(path.join(publicDir, '11', 'class11_bio', filename))
    if (code === 'lemh') {
      candidates.push(
        pt === '1'
          ? path.join(publicDir, '12', 'maths', filename)
          : path.join(publicDir, '12', 'maths', `pt${pt}`, filename)
      )
    }
    if (code === 'leph') candidates.push(path.join(publicDir, '12', 'phy', `pt${pt}`, filename))
    if (code === 'lech') candidates.push(path.join(publicDir, '12', 'chem', `pt${pt}`, filename))
    if (code === 'lebo') candidates.push(path.join(publicDir, '12', 'bio', filename))

    for (const cand of candidates) {
      if (fs.existsSync(cand)) return cand
    }
    void num
  }

  if (!localPdfIndexCache) {
    localPdfIndexCache = new Map<string, string>()
    const scanDir = (dir: string) => {
      if (!fs.existsSync(dir)) return
      for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
        const full = path.join(dir, entry.name)
        if (entry.isDirectory()) {
          scanDir(full)
        } else if (entry.isFile() && entry.name.toLowerCase().endsWith('.pdf')) {
          localPdfIndexCache!.set(entry.name.toLowerCase(), full)
        }
      }
    }
    for (const root of ALLOWED_LOCAL_ROOTS) {
      scanDir(path.join(publicDir, root))
    }
  }

  return localPdfIndexCache.get(filename) || null
}

function buildPdfHeaders(filename: string, extra: Record<string, string> = {}): Headers {
  const headers = new Headers({
    'Content-Type': 'application/pdf',
    'Content-Disposition': `inline; filename="${filename}"`,
    'Accept-Ranges': 'bytes',
    'Cache-Control': 'public, max-age=86400',
    'X-Frame-Options': 'SAMEORIGIN',
    'X-Content-Type-Options': 'nosniff',
    ...extra,
  })
  return headers
}

function parseRangeHeader(rangeHeader: string | null, fileSize: number): { start: number; end: number } | 'invalid' | null {
  if (!rangeHeader) return null
  const match = /^bytes=(\d*)-(\d*)$/i.exec(rangeHeader.trim())
  if (!match) return 'invalid'

  const [, startStr, endStr] = match
  let start: number
  let end: number

  if (!startStr && !endStr) return 'invalid'
  if (!startStr) {
    // Suffix byte range: bytes=-N
    const suffixLen = parseInt(endStr, 10)
    if (isNaN(suffixLen) || suffixLen <= 0) return 'invalid'
    start = Math.max(0, fileSize - suffixLen)
    end = fileSize - 1
  } else {
    start = parseInt(startStr, 10)
    end = endStr ? parseInt(endStr, 10) : fileSize - 1
    if (isNaN(start) || isNaN(end) || start < 0 || start >= fileSize || end < start) {
      return 'invalid'
    }
    end = Math.min(end, fileSize - 1)
  }

  return { start, end }
}

function serveLocalFile(filePath: string, filename: string, req: NextRequest, isHead: boolean): NextResponse {
  const stat = fs.statSync(filePath)
  const fileSize = stat.size
  const range = parseRangeHeader(req.headers.get('range'), fileSize)

  if (range === 'invalid') {
    return new NextResponse('Range Not Satisfiable', {
      status: 416,
      headers: buildPdfHeaders(filename, { 'Content-Range': `bytes */${fileSize}` }),
    })
  }

  if (range) {
    const chunkSize = range.end - range.start + 1
    const headers = buildPdfHeaders(filename, {
      'Content-Range': `bytes ${range.start}-${range.end}/${fileSize}`,
      'Content-Length': String(chunkSize),
      'X-PDF-Source': 'local',
    })
    if (isHead) {
      return new NextResponse(null, { status: 206, headers })
    }
    const stream = Readable.toWeb(fs.createReadStream(filePath, { start: range.start, end: range.end })) as ReadableStream
    return new NextResponse(stream, { status: 206, headers })
  }

  const headers = buildPdfHeaders(filename, {
    'Content-Length': String(fileSize),
    'X-PDF-Source': 'local',
  })
  if (isHead) {
    return new NextResponse(null, { status: 200, headers })
  }
  const stream = Readable.toWeb(fs.createReadStream(filePath)) as ReadableStream
  return new NextResponse(stream, { status: 200, headers })
}

async function trySupabaseStorage(
  filename: string,
  req: NextRequest,
  isHead: boolean
): Promise<NextResponse | null> {
  const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY
  if (!supabaseUrl || !serviceKey) return null

  const storageUrl = `${supabaseUrl.replace(/\/$/, '')}/storage/v1/object/authenticated/textbooks/chapters/${encodeURIComponent(filename)}`
  const reqHeaders: Record<string, string> = {
    Authorization: `Bearer ${serviceKey}`,
    apikey: serviceKey,
  }
  const rangeHeader = req.headers.get('range')
  if (rangeHeader) {
    reqHeaders['Range'] = rangeHeader
  }

  try {
    const upstream = await fetch(storageUrl, {
      method: isHead ? 'HEAD' : 'GET',
      headers: reqHeaders,
      signal: AbortSignal.timeout(25000),
    })

    if (!upstream.ok && upstream.status !== 206) {
      return null
    }

    const extra: Record<string, string> = { 'X-PDF-Source': 'supabase-storage' }
    const cl = upstream.headers.get('content-length')
    const cr = upstream.headers.get('content-range')
    if (cl) extra['Content-Length'] = cl
    if (cr) extra['Content-Range'] = cr

    return new NextResponse(isHead ? null : upstream.body, {
      status: upstream.status === 206 ? 206 : 200,
      headers: buildPdfHeaders(filename, extra),
    })
  } catch (err) {
    console.warn(`[pdf-proxy] Supabase Storage lookup failed for ${filename}:`, err)
    return null
  }
}

async function tryUpstreamNcert(
  filename: string,
  req: NextRequest,
  isHead: boolean
): Promise<NextResponse | null> {
  const targetUrl = `https://ncert.nic.in/textbook/pdf/${encodeURIComponent(filename)}`
  const reqHeaders: Record<string, string> = {}
  const rangeHeader = req.headers.get('range')
  if (rangeHeader) {
    reqHeaders['Range'] = rangeHeader
  }

  try {
    const upstream = await fetch(targetUrl, {
      method: isHead ? 'HEAD' : 'GET',
      headers: reqHeaders,
      signal: AbortSignal.timeout(30000),
    })
    const ct = (upstream.headers.get('content-type') || '').toLowerCase()
    if ((!upstream.ok && upstream.status !== 206) || ct.includes('text/html') || !ct.includes('pdf')) {
      return null
    }

    const extra: Record<string, string> = { 'X-PDF-Source': 'upstream-ncert' }
    const cl = upstream.headers.get('content-length')
    const cr = upstream.headers.get('content-range')
    if (cl) extra['Content-Length'] = cl
    if (cr) extra['Content-Range'] = cr

    return new NextResponse(isHead ? null : upstream.body, {
      status: upstream.status === 206 ? 206 : 200,
      headers: buildPdfHeaders(filename, extra),
    })
  } catch (err) {
    console.warn(`[pdf-proxy] Upstream NCERT fetch failed for ${filename}:`, err)
    return null
  }
}

async function handlePdfRequest(req: NextRequest, isHead: boolean): Promise<NextResponse> {
  const fileParam = req.nextUrl.searchParams.get('file')
  const urlParam = req.nextUrl.searchParams.get('url')
  const raw = fileParam || urlParam || ''

  if (!raw) {
    return new NextResponse('Missing required "file" or "url" parameter', { status: 400 })
  }

  const filename = extractSafeFilename(raw)
  if (!filename) {
    return new NextResponse('Forbidden: Invalid or disallowed textbook PDF path.', { status: 403 })
  }

  // 1. Local public/ disk (fastest, zero-latency HTTP 206 Range streaming)
  const localPath = getLocalPdfPath(filename)
  if (localPath) {
    return serveLocalFile(localPath, filename, req, isHead)
  }

  // 2. Supabase Storage `textbooks` bucket (production Vercel serverless path)
  const storageRes = await trySupabaseStorage(filename, req, isHead)
  if (storageRes) {
    return storageRes
  }

  // 3. Upstream NCERT server fetch (validated application/pdf only, never HTML or 307 redirect)
  const upstreamRes = await tryUpstreamNcert(filename, req, isHead)
  if (upstreamRes) {
    return upstreamRes
  }

  return new NextResponse(`Textbook PDF "${filename}" is currently unavailable.`, { status: 404 })
}

export async function GET(req: NextRequest) {
  return handlePdfRequest(req, false)
}

export async function HEAD(req: NextRequest) {
  return handlePdfRequest(req, true)
}

import fs from 'fs'
import path from 'path'
import { createClient } from '@supabase/supabase-js'

interface DownloadItem {
  code: string
  destRelPath: string
  urls: string[]
}

function loadEnv(): Record<string, string> {
  const envPath = path.join(process.cwd(), '.env.local')
  if (!fs.existsSync(envPath)) return {}
  return Object.fromEntries(
    fs
      .readFileSync(envPath, 'utf8')
      .split(/\r?\n/)
      .filter((l) => l && !l.startsWith('#') && l.includes('='))
      .map((l) => {
        const idx = l.indexOf('=')
        return [l.slice(0, idx).trim(), l.slice(idx + 1).trim().replace(/^["']|["']$/g, '')]
      })
  )
}

function pad2(n: number): string {
  return n < 10 ? `0${n}` : `${n}`
}

function buildMissingDownloads(): DownloadItem[] {
  const items: DownloadItem[] = []
  const add = (code: string, destRelPath: string, extraUrls: string[] = []) => {
    items.push({
      code,
      destRelPath,
      urls: [`https://ncert.nic.in/textbook/pdf/${code}.pdf`, ...extraUrls],
    })
  }

  // Class 9 Science Ch 1
  add('iesc101', 'public/9/class 9th science/iesc101.pdf')
  // Class 10 Science Ch 5
  add('jesc105', 'public/10/class10_science/jesc105.pdf')

  // Class 11 Biology (19 chapters)
  for (let i = 1; i <= 19; i++) {
    const code = `kebo1${pad2(i)}`
    add(code, `public/11/class11_bio/${code}.pdf`)
  }

  // Class 12 Physics Part 1 (8) & Part 2 (6)
  for (let i = 1; i <= 8; i++) {
    const code = `leph1${pad2(i)}`
    add(code, `public/12/phy/pt1/${code}.pdf`)
  }
  for (let i = 1; i <= 6; i++) {
    const code = `leph2${pad2(i)}`
    add(code, `public/12/phy/pt2/${code}.pdf`)
  }

  // Class 12 Chemistry Part 1 (5) & Part 2 (5)
  for (let i = 1; i <= 5; i++) {
    const code = `lech1${pad2(i)}`
    add(code, `public/12/chem/pt1/${code}.pdf`)
  }
  for (let i = 1; i <= 5; i++) {
    const code = `lech2${pad2(i)}`
    add(code, `public/12/chem/pt2/${code}.pdf`)
  }

  // Class 12 Biology (13 chapters; shifted Archive.org old-edition codes ONLY as verified fallback if ncert.nic.in returns HTML)
  const leboFallbackMap: Record<number, string> = {
    8: 'https://archive.org/download/ncert-lebo1/lebo110.pdf',
    10: 'https://archive.org/download/ncert-lebo1/lebo112.pdf',
    11: 'https://archive.org/download/ncert-lebo1/lebo113.pdf',
    12: 'https://archive.org/download/ncert-lebo1/lebo114.pdf',
    13: 'https://archive.org/download/ncert-lebo1/lebo115.pdf',
  }
  for (let i = 1; i <= 13; i++) {
    const code = `lebo1${pad2(i)}`
    add(code, `public/12/bio/${code}.pdf`, leboFallbackMap[i] ? [leboFallbackMap[i]] : [])
  }

  return items
}

function isValidPdfBuffer(buf: Buffer): boolean {
  return buf.length > 1024 && buf.subarray(0, 5).toString('ascii') === '%PDF-'
}

async function downloadValidPdf(item: DownloadItem): Promise<boolean> {
  const fullDest = path.join(process.cwd(), item.destRelPath)
  if (fs.existsSync(fullDest)) {
    const head = Buffer.alloc(5)
    const fd = fs.openSync(fullDest, 'r')
    fs.readSync(fd, head, 0, 5, 0)
    fs.closeSync(fd)
    if (head.toString('ascii') === '%PDF-') {
      return true
    }
    fs.unlinkSync(fullDest)
  }

  fs.mkdirSync(path.dirname(fullDest), { recursive: true })

  for (const url of item.urls) {
    for (let attempt = 1; attempt <= 3; attempt++) {
      try {
        const res = await fetch(url, {
          signal: AbortSignal.timeout(120000),
        })
        if (!res.ok) break
        const ct = (res.headers.get('content-type') || '').toLowerCase()
        if (ct.includes('text/html')) break
        const buf = Buffer.from(await res.arrayBuffer())
        if (!isValidPdfBuffer(buf)) break
        fs.writeFileSync(fullDest, buf)
        console.log(`[DOWNLOADED] ${item.code} -> ${item.destRelPath} (${(buf.length / 1024 / 1024).toFixed(2)} MB)`)
        return true
      } catch (err: any) {
        console.warn(`[WARN] Attempt ${attempt}/3 failed ${url}: ${err?.message || err}`)
        if (attempt < 3) await new Promise((r) => setTimeout(r, 1200 * attempt))
      }
    }
  }
  console.error(`[ERROR] Could not download valid PDF for ${item.code}`)
  return false
}

function walkChapterPdfs(dir: string, out: string[] = []): string[] {
  if (!fs.existsSync(dir)) return out
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) {
      walkChapterPdfs(full, out)
    } else if (entry.isFile() && /^[ijkl]e(mh|sc|ph|ch|bo)\d{3}\.pdf$/i.test(entry.name)) {
      out.push(full)
    }
  }
  return out
}

async function main() {
  const args = new Set(process.argv.slice(2))
  const skipUpload = args.has('--skip-upload')
  const skipDownload = args.has('--skip-download')

  console.log('=== PHASE 3: CLASS 9-12 NCERT CORPUS NORMALIZATION & SYNC ===\n')

  // 1. Clean up public/ anomalies
  const kephBad = path.join(process.cwd(), 'public/11/class11_physics/pt1/keph101 (1).pdf')
  const kephGood = path.join(process.cwd(), 'public/11/class11_physics/pt1/keph101.pdf')
  if (fs.existsSync(kephBad)) {
    if (!fs.existsSync(kephGood)) {
      fs.renameSync(kephBad, kephGood)
      console.log('[CLEANUP] Renamed keph101 (1).pdf -> keph101.pdf')
    } else {
      fs.unlinkSync(kephBad)
      console.log('[CLEANUP] Removed duplicate keph101 (1).pdf')
    }
  }

  const strayMaths = path.join(process.cwd(), 'public/10/class10_science/Maths_SecP1X_2026-27.pdf')
  if (fs.existsSync(strayMaths)) {
    fs.unlinkSync(strayMaths)
    console.log('[CLEANUP] Removed stray public/10/class10_science/Maths_SecP1X_2026-27.pdf')
  }

  // 2. Download missing PDFs sequentially with gentle pacing so ncert.nic.in WAF does not rate-limit
  if (!skipDownload) {
    const missing = buildMissingDownloads()
    let dlOk = 0
    let dlFail = 0
    for (const item of missing) {
      const ok = await downloadValidPdf(item)
      if (ok) dlOk++
      else dlFail++
      await new Promise((r) => setTimeout(r, 400))
    }
    console.log(`\n[DOWNLOAD SUMMARY] Ready: ${dlOk}/${missing.length}, Failed: ${dlFail}`)
    if (dlFail > 0) {
      process.exitCode = 1
    }
  }

  // 3. Upload to Supabase Storage `textbooks` bucket
  if (!skipUpload) {
    const env = loadEnv()
    const supabaseUrl = env.NEXT_PUBLIC_SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL
    const serviceKey = env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_SERVICE_ROLE_KEY
    if (!supabaseUrl || !serviceKey) {
      console.error('[STORAGE] Missing NEXT_PUBLIC_SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY')
      process.exit(1)
    }
    const supabase = createClient(supabaseUrl, serviceKey)

    const { data: buckets } = await supabase.storage.listBuckets()
    if (!buckets?.some((b) => b.name === 'textbooks')) {
      const { error: createErr } = await supabase.storage.createBucket('textbooks', {
        public: false,
        allowedMimeTypes: ['application/pdf'],
      })
      if (createErr) {
        console.error('[STORAGE] createBucket error:', createErr)
        process.exit(1)
      }
      console.log('[STORAGE] Created private bucket "textbooks"')
    }

    // List existing objects in chapters/
    const existingSet = new Set<string>()
    let offset = 0
    while (true) {
      const { data: listData, error: listErr } = await supabase.storage
        .from('textbooks')
        .list('chapters', { limit: 1000, offset })
      if (listErr || !listData || listData.length === 0) break
      for (const obj of listData) {
        if (obj.name) existingSet.add(obj.name.toLowerCase())
      }
      if (listData.length < 1000) break
      offset += 1000
    }

    const allPdfs = ['9', '10', '11', '12'].flatMap((cls) =>
      walkChapterPdfs(path.join(process.cwd(), 'public', cls))
    )
    console.log(`\n[STORAGE] Found ${allPdfs.length} Class 9-12 chapter PDFs to sync to textbooks/chapters/`)

    let uploaded = 0
    let skipped = 0
    let failed = 0

    for (const fullPath of allPdfs) {
      const fname = path.basename(fullPath).toLowerCase()
      if (existingSet.has(fname)) {
        skipped++
        continue
      }
      const buf = fs.readFileSync(fullPath)
      const sizeMb = (buf.length / 1024 / 1024).toFixed(2)
      const { error: upErr } = await supabase.storage
        .from('textbooks')
        .upload(`chapters/${fname}`, buf, {
          contentType: 'application/pdf',
          upsert: true,
        })
      if (upErr) {
        console.warn(`[STORAGE WARN] Failed uploading ${fname} (${sizeMb} MB): ${upErr.message}`)
        failed++
      } else {
        console.log(`[STORAGE UPLOADED] chapters/${fname} (${sizeMb} MB)`)
        uploaded++
      }
    }

    console.log(`\n[STORAGE SUMMARY] Uploaded: ${uploaded}, Skipped (already present): ${skipped}, Failed: ${failed}`)
  }
}

main().catch((err) => {
  console.error(err)
  process.exit(1)
})

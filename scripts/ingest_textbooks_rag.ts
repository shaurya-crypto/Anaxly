import fs from 'fs'
import path from 'path'
import { execFileSync } from 'child_process'
import { GoogleGenAI } from '@google/genai'
import { createClient } from '@supabase/supabase-js'
import {
  canonicalSubjectForRag,
  chunkTextbookText,
  computeContentHash,
  TextbookChunkType,
} from '../src/lib/rag/textbookRag'

interface TextbookPageText {
  page: number
  text: string
}

interface PendingChunk {
  class_level: number
  subject: string
  chapter_number: number
  book_code: string
  section_title: string
  chunk_type: TextbookChunkType
  page_number: number
  content: string
  content_hash: string
  metadata: Record<string, any>
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

function classifyChunkType(text: string): TextbookChunkType {
  const lower = text.toLowerCase()
  if (/\b(proof|hence proved|q\.e\.d\.|let us prove)\b/.test(lower)) return 'proof'
  if (/\b(theorem|lemma|corollary|postulate|axiom|law states)\b/.test(lower)) return 'theorem'
  if (/\b(example\s+\d+|solution\s*:)\b/.test(lower)) return 'example'
  if (/\b(exercise\s+\d+(?:\.\d+)?|questions\s*$|try these)\b/m.test(lower)) return 'exercise'
  if (/\b(summary|what you have learnt|points to ponder)\b/.test(lower)) return 'summary'
  return 'intuition'
}

function extractPdfPagesWithPython(pdfPath: string): TextbookPageText[] {
  const pyScript = `
import json, sys, pypdfium2 as pdfium
doc = pdfium.PdfDocument(sys.argv[1])
pages = []
for i in range(len(doc)):
    tp = doc[i].get_textpage()
    txt = tp.get_text_range() or ""
    pages.append({"page": i + 1, "text": txt})
print(json.dumps(pages, ensure_ascii=False))
`
  const out = execFileSync('python', ['-c', pyScript, pdfPath], {
    maxBuffer: 32 * 1024 * 1024,
    encoding: 'utf8',
  })
  return JSON.parse(out)
}

function parseChapterMetaFromFilename(filename: string): {
  classLevel: number
  subject: string
  chapterNumber: number
  bookCode: string
} | null {
  const m = filename.toLowerCase().match(/^([ijkl])e(mh|sc|ph|ch|bo)(\d)(\d\d)\.pdf$/)
  if (!m) return null
  const [, clsChar, subCode, ptStr, numStr] = m
  const classLevel = clsChar === 'i' ? 9 : clsChar === 'j' ? 10 : clsChar === 'k' ? 11 : 12
  const pt = parseInt(ptStr, 10)
  const chInPt = parseInt(numStr, 10)
  let subject = 'Science'
  if (subCode === 'mh') subject = 'Mathematics'
  else if (subCode === 'ph') subject = 'Physics'
  else if (subCode === 'ch') subject = 'Chemistry'
  else if (subCode === 'bo') subject = 'Biology'

  let chapterNumber = chInPt
  if (pt === 2) {
    if (classLevel === 9 && subject === 'Mathematics') chapterNumber = 8 + chInPt
    else if (classLevel === 11 && subject === 'Physics') chapterNumber = 7 + chInPt
    else if (classLevel === 11 && subject === 'Chemistry') chapterNumber = 6 + chInPt
    else if (classLevel === 12 && subject === 'Mathematics') chapterNumber = 6 + chInPt
    else if (classLevel === 12 && subject === 'Physics') chapterNumber = 8 + chInPt
    else if (classLevel === 12 && subject === 'Chemistry') chapterNumber = 5 + chInPt
  }

  return {
    classLevel,
    subject: canonicalSubjectForRag(subject, classLevel),
    chapterNumber,
    bookCode: `${clsChar}e${subCode}${ptStr}${numStr}`,
  }
}

function collectChapterPdfs(limit?: number): Array<{ fullPath: string; filename: string }> {
  const out: Array<{ fullPath: string; filename: string }> = []
  const walk = (dir: string) => {
    if (!fs.existsSync(dir)) return
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name)
      if (entry.isDirectory()) walk(full)
      else if (entry.isFile() && /^[ijkl]e(mh|sc|ph|ch|bo)\d{3}\.pdf$/i.test(entry.name)) {
        out.push({ fullPath: full, filename: entry.name.toLowerCase() })
      }
    }
  }
  for (const cls of ['9', '10', '11', '12']) {
    walk(path.join(process.cwd(), 'public', cls))
  }
  out.sort((a, b) => a.filename.localeCompare(b.filename))
  return limit ? out.slice(0, limit) : out
}

async function main() {
  const args = process.argv.slice(2)
  const dryRun = args.includes('--dry-run')
  const limitIdx = args.indexOf('--limit')
  const limit = limitIdx !== -1 ? parseInt(args[limitIdx + 1] || '0', 10) || undefined : undefined

  const env = loadEnv()
  const geminiKey = env.GEMINI_API_KEY || process.env.GEMINI_API_KEY
  const supabaseUrl = env.NEXT_PUBLIC_SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL
  const serviceKey = env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_SERVICE_ROLE_KEY

  const pdfs = collectChapterPdfs(limit)
  console.log(`[RAG Ingest] Found ${pdfs.length} Class 9-12 chapter PDFs (dryRun=${dryRun}).`)

  const allChunks: PendingChunk[] = []
  for (const { fullPath, filename } of pdfs) {
    const meta = parseChapterMetaFromFilename(filename)
    if (!meta) continue
    try {
      const pages = extractPdfPagesWithPython(fullPath)
      for (const pg of pages) {
        const chunks = chunkTextbookText(pg.text, 1000, 120)
        for (const chunkText of chunks) {
          const firstLine = chunkText.split('\n')[0]?.trim().slice(0, 120) || `Chapter ${meta.chapterNumber}`
          const chunkType = classifyChunkType(chunkText)
          const contentHash = computeContentHash([
            meta.classLevel,
            meta.subject,
            meta.chapterNumber,
            pg.page,
            chunkType,
            chunkText,
          ])
          allChunks.push({
            class_level: meta.classLevel,
            subject: meta.subject,
            chapter_number: meta.chapterNumber,
            book_code: meta.bookCode,
            section_title: firstLine,
            chunk_type: chunkType,
            page_number: pg.page,
            content: chunkText,
            content_hash: contentHash,
            metadata: { filename },
          })
        }
      }
    } catch (err: any) {
      console.warn(`[RAG Ingest] Skipped ${filename}:`, err?.message || err)
    }
  }

  console.log(`[RAG Ingest] Prepared ${allChunks.length} semantic chunks.`)
  if (dryRun) {
    console.log('[RAG Ingest] Sample chunk:', JSON.stringify(allChunks[0], null, 2))
    return
  }

  if (!geminiKey || !supabaseUrl || !serviceKey) {
    throw new Error('GEMINI_API_KEY, NEXT_PUBLIC_SUPABASE_URL, and SUPABASE_SERVICE_ROLE_KEY are required.')
  }

  const ai = new GoogleGenAI({ apiKey: geminiKey })
  const supabase = createClient(supabaseUrl, serviceKey)

  const BATCH_SIZE = 20
  let upserted = 0
  for (let i = 0; i < allChunks.length; i += BATCH_SIZE) {
    const batch = allChunks.slice(i, i + BATCH_SIZE)
    const embeddings = await Promise.all(
      batch.map(async (chunk) => {
        try {
          const res = await ai.models.embedContent({
            model: 'gemini-embedding-001',
            contents: `${chunk.subject} Class ${chunk.class_level} Ch ${chunk.chapter_number} (${chunk.chunk_type}): ${chunk.content}`,
            config: { outputDimensionality: 768 },
          })
          return res.embeddings?.[0]?.values || null
        } catch {
          return null
        }
      })
    )

    const rows = batch.map((c, idx) => ({
      ...c,
      embedding: embeddings[idx],
    }))

    const { error } = await supabase
      .from('book_chunks')
      .upsert(rows, { onConflict: 'content_hash', ignoreDuplicates: false })
    if (error) {
      throw new Error(`Supabase upsert error at batch ${i}: ${error.message}`)
    }
    upserted += rows.length
    if (upserted % 100 === 0 || upserted === allChunks.length) {
      console.log(`[RAG Ingest] Upserted ${upserted}/${allChunks.length} chunks`)
    }
  }
}

main().catch((err) => {
  console.error('[RAG Ingest] Failed:', err)
  process.exit(1)
})

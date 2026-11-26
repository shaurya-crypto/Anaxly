import crypto from 'crypto'
import { GoogleGenAI } from '@google/genai'
import { createAdminClient } from '@/utils/supabase/admin'
import { getChaptersBySubject, normalizeSubject, searchIndex } from '@/lib/textbookRegistry'

export type TextbookChunkType =
  | 'intuition'
  | 'theorem'
  | 'proof'
  | 'example'
  | 'exercise'
  | 'solution'
  | 'summary'

export interface RetrievedTextbookChunk {
  id: string
  classLevel: number
  subject: string
  chapterNumber: number
  bookCode: string
  sectionTitle: string
  chunkType: TextbookChunkType
  pageNumber: number | null
  content: string
  rrfScore: number
  source: 'supabase_hybrid_rag' | 'local_page_index'
}

export interface PrerequisiteBridge {
  conceptKey: string
  prerequisiteKey: string
  classLevel: number
  subject: string
  prerequisiteClassLevel: number | null
  bridgeNote: string
}

const BUILTIN_PREREQUISITES: PrerequisiteBridge[] = [
  {
    conceptKey: 'distance_formula',
    prerequisiteKey: 'pythagoras_theorem',
    classLevel: 10,
    subject: 'mathematics',
    prerequisiteClassLevel: 9,
    bridgeNote:
      'The segment joining (x₁, y₁) and (x₂, y₂) is the hypotenuse of a right triangle: d = √[(x₂ - x₁)² + (y₂ - y₁)²].',
  },
  {
    conceptKey: 'circle_through_two_points',
    prerequisiteKey: 'perpendicular_bisector_locus',
    classLevel: 10,
    subject: 'mathematics',
    prerequisiteClassLevel: 9,
    bridgeNote:
      'Any center equidistant from A and B lies on the perpendicular bisector of AB; the smallest circle has center at the midpoint of AB and diameter AB.',
  },
  {
    conceptKey: 'quadratic_roots_discriminant',
    prerequisiteKey: 'parabola_x_intercepts',
    classLevel: 10,
    subject: 'mathematics',
    prerequisiteClassLevel: 9,
    bridgeNote:
      'Real roots of ax^2 + bx + c = 0 are the x-coordinates where the parabola y = ax^2 + bx + c meets the x-axis.',
  },
  {
    conceptKey: 'instantaneous_velocity_derivative',
    prerequisiteKey: 'secant_to_tangent_slope',
    classLevel: 11,
    subject: 'physics',
    prerequisiteClassLevel: 10,
    bridgeNote:
      'Average velocity is the slope of a chord on the x-t graph; shrinking delta-t to zero turns that chord into the tangent slope dx/dt.',
  },
  {
    conceptKey: 'projectile_motion',
    prerequisiteKey: 'independent_x_y_components',
    classLevel: 11,
    subject: 'physics',
    prerequisiteClassLevel: 11,
    bridgeNote:
      'Horizontal velocity u*cos(theta) stays constant (a_x = 0) while vertical motion obeys free fall under g; time t links both axes.',
  },
  {
    conceptKey: 'limits_and_derivatives',
    prerequisiteKey: 'algebraic_factorisation_and_slope',
    classLevel: 11,
    subject: 'mathematics',
    prerequisiteClassLevel: 10,
    bridgeNote:
      'If direct substitution gives 0/0, factor and cancel the common (x - a) term first before taking the limit near x = a.',
  },
  {
    conceptKey: 'integration_by_parts',
    prerequisiteKey: 'product_rule_and_antiderivatives',
    classLevel: 12,
    subject: 'mathematics',
    prerequisiteClassLevel: 11,
    bridgeNote:
      'Integration by parts reverses the derivative product rule d(u*v) = u*dv + v*du: integral(u dv) = u*v - integral(v du).',
  },
  {
    conceptKey: 'gauss_law_electrostatics',
    prerequisiteKey: 'vector_dot_product_and_flux',
    classLevel: 12,
    subject: 'physics',
    prerequisiteClassLevel: 11,
    bridgeNote:
      'Electric flux E dot dA = E*dA*cos(theta) counts field lines crossing a closed surface; symmetry lets E pull outside the surface integral.',
  },
  {
    conceptKey: 'first_order_kinetics_half_life',
    prerequisiteKey: 'natural_logarithm_exponential_decay',
    classLevel: 12,
    subject: 'chemistry',
    prerequisiteClassLevel: 11,
    bridgeNote:
      'For first-order decay, [A] = [A]0 * e^(-kt), so half-life t_1/2 = ln(2)/k = 0.693/k is independent of starting concentration.',
  },
  {
    conceptKey: 'lac_operon_gene_regulation',
    prerequisiteKey: 'transcription_promoter_operator_dna',
    classLevel: 12,
    subject: 'biology',
    prerequisiteClassLevel: 12,
    bridgeNote:
      'Lactose acts as the inducer that binds the repressor protein, clearing the operator so RNA polymerase can transcribe lacZ, lacY, and lacA.',
  },
]

export function normalizeClassLevelInt(classLevel: number | string | undefined): number {
  if (typeof classLevel === 'number' && !isNaN(classLevel)) {
    return Math.min(12, Math.max(9, Math.round(classLevel)))
  }
  const parsed = parseInt(String(classLevel || '').replace(/\D/g, ''), 10)
  if (!isNaN(parsed) && parsed >= 9 && parsed <= 12) return parsed
  return 10
}

export function canonicalSubjectForRag(subject: string | undefined, classLevel?: number): string {
  const norm = normalizeSubject(subject || '')
  if (norm === 'mathematics') return 'Mathematics'
  if (norm === 'physics') return 'Physics'
  if (norm === 'chemistry') return 'Chemistry'
  if (norm === 'biology') return classLevel && classLevel <= 10 ? 'Science' : 'Biology'
  if (norm === 'science') return 'Science'
  return subject?.trim() || 'Science'
}

export function computeContentHash(parts: Array<string | number | null | undefined>): string {
  return crypto
    .createHash('sha256')
    .update(parts.map((p) => String(p ?? '')).join('|'))
    .digest('hex')
}

export async function embedTextbookText(
  text: string,
  apiKey = process.env.GEMINI_API_KEY
): Promise<number[] | null> {
  if (!apiKey || !text.trim()) return null
  try {
    const ai = new GoogleGenAI({ apiKey })
    const res = await ai.models.embedContent({
      model: 'gemini-embedding-001',
      contents: text.slice(0, 6000),
      config: { outputDimensionality: 768 },
    })
    const values = res.embeddings?.[0]?.values
    return Array.isArray(values) && values.length === 768 ? values : null
  } catch (err) {
    console.warn('[TextbookRAG] Embedding generation failed (falling back to FTS/index):', err)
    return null
  }
}

export async function hybridRetrieveTextbookChunks(params: {
  query: string
  classLevel: number | string
  subject: string
  chapterNumber?: number
  chunkType?: TextbookChunkType
  limit?: number
}): Promise<RetrievedTextbookChunk[]> {
  const classInt = normalizeClassLevelInt(params.classLevel)
  const subjectNorm = canonicalSubjectForRag(params.subject, classInt)
  const limit = Math.min(12, Math.max(1, params.limit ?? 5))

  // 1. Try Supabase Hybrid RAG (pgvector + FTS RRF)
  try {
    const supabase = createAdminClient()
    const embedding = await embedTextbookText(params.query)
    const { data, error } = await supabase.rpc('hybrid_search_book_chunks', {
      p_query_text: params.query,
      p_query_embedding: embedding,
      p_class_level: classInt,
      p_subject: subjectNorm,
      p_chapter_number: params.chapterNumber ?? null,
      p_chunk_type: params.chunkType ?? null,
      p_match_count: limit,
    })

    if (!error && Array.isArray(data) && data.length > 0) {
      return data.map((row: any) => ({
        id: String(row.id),
        classLevel: Number(row.class_level),
        subject: String(row.subject),
        chapterNumber: Number(row.chapter_number),
        bookCode: String(row.book_code || ''),
        sectionTitle: String(row.section_title || ''),
        chunkType: (row.chunk_type || 'intuition') as TextbookChunkType,
        pageNumber: row.page_number !== null ? Number(row.page_number) : null,
        content: String(row.content || ''),
        rrfScore: Number(row.rrf_score || 0),
        source: 'supabase_hybrid_rag',
      }))
    }
  } catch (err) {
    console.warn('[TextbookRAG] Supabase hybrid search unavailable, using local page index:', err)
  }

  // 2. Fast deterministic fallback from indexed textbookPageMap.json
  const hits = searchIndex(params.query, {
    classLevel: classInt,
    subject: subjectNorm,
    chapterNumber: params.chapterNumber,
  })

  if (hits.length > 0) {
    return hits.slice(0, limit).map((h, idx) => ({
      id: `${h.chapter.id}-${h.item.id}-${idx}`,
      classLevel: h.chapter.classLevel,
      subject: h.chapter.subject,
      chapterNumber: h.chapter.chapterNumber,
      bookCode: h.chapter.bookCode,
      sectionTitle: h.item.title,
      chunkType:
        h.type === 'example'
          ? 'example'
          : h.type === 'exercise' || h.type === 'question'
          ? 'exercise'
          : 'intuition',
      pageNumber: h.item.page,
      content: [h.item.title, h.item.snippet].filter(Boolean).join(' — '),
      rrfScore: h.relevance,
      source: 'local_page_index',
    }))
  }

  // 3. Fallback: return chapter TOC summary if chapter exists
  const chapters = getChaptersBySubject(classInt, subjectNorm)
  const matchedChapter = params.chapterNumber
    ? chapters.find((c) => c.chapterNumber === params.chapterNumber)
    : chapters[0]

  if (!matchedChapter) return []

  return matchedChapter.sections.slice(0, limit).map((sec, idx) => ({
    id: `${matchedChapter.id}-sec-${idx}`,
    classLevel: matchedChapter.classLevel,
    subject: matchedChapter.subject,
    chapterNumber: matchedChapter.chapterNumber,
    bookCode: matchedChapter.bookCode,
    sectionTitle: `${sec.number} ${sec.title}`,
    chunkType: 'intuition',
    pageNumber: sec.page,
    content: `Section ${sec.number}: ${sec.title} (Page ${sec.page})`,
    rrfScore: 0.4,
    source: 'local_page_index',
  }))
}

export async function lookupConceptPrerequisites(params: {
  query: string
  classLevel: number | string
  subject: string
}): Promise<PrerequisiteBridge[]> {
  const classInt = normalizeClassLevelInt(params.classLevel)
  const subjectNorm = canonicalSubjectForRag(params.subject, classInt)
  const tokens = params.query
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, ' ')
    .split(/\s+/)
    .filter((t) => t.length >= 3)

  // 1. Try Supabase concept_prerequisites
  try {
    const supabase = createAdminClient()
    const { data, error } = await supabase
      .from('concept_prerequisites')
      .select('concept_key, prerequisite_key, class_level, subject, prerequisite_class_level, bridge_note')
      .eq('class_level', classInt)
      .ilike('subject', subjectNorm)
      .limit(30)

    if (!error && Array.isArray(data) && data.length > 0) {
      const scored = data
        .map((row: any) => {
          const hay = `${row.concept_key} ${row.prerequisite_key} ${row.bridge_note}`.toLowerCase()
          const hits = tokens.filter((t) => hay.includes(t)).length
          return { row, hits }
        })
        .filter((x) => x.hits > 0)
        .sort((a, b) => b.hits - a.hits)
        .slice(0, 3)

      if (scored.length > 0) {
        return scored.map(({ row }) => ({
          conceptKey: row.concept_key,
          prerequisiteKey: row.prerequisite_key,
          classLevel: row.class_level,
          subject: row.subject,
          prerequisiteClassLevel: row.prerequisite_class_level ?? null,
          bridgeNote: row.bridge_note,
        }))
      }
    }
  } catch {
    // Fall through to deterministic built-in prerequisites
  }

  // 2. Built-in fallback matching
  const normSubLower = subjectNorm.toLowerCase()
  return BUILTIN_PREREQUISITES.filter((p) => {
    const subMatch = p.subject === normSubLower || (classInt <= 10 && normSubLower === 'science' && p.subject === 'physics')
    if (!subMatch && Math.abs(p.classLevel - classInt) > 1) return false
    const hay = `${p.conceptKey.replace(/_/g, ' ')} ${p.prerequisiteKey.replace(/_/g, ' ')} ${p.bridgeNote}`.toLowerCase()
    return tokens.some((t) => hay.includes(t))
  }).slice(0, 3)
}

export function chunkTextbookText(
  rawText: string,
  maxChars = 1100,
  overlapChars = 150
): string[] {
  const cleaned = rawText.replace(/\r\n/g, '\n').replace(/\n{3,}/g, '\n\n').trim()
  if (!cleaned) return []
  if (cleaned.length <= maxChars) return [cleaned]

  const chunks: string[] = []
  let start = 0
  while (start < cleaned.length) {
    let end = Math.min(cleaned.length, start + maxChars)
    if (end < cleaned.length) {
      const lastBreak = Math.max(cleaned.lastIndexOf('\n\n', end), cleaned.lastIndexOf('. ', end))
      if (lastBreak > start + Math.floor(maxChars * 0.5)) {
        end = lastBreak + 1
      }
    }
    const slice = cleaned.slice(start, end).trim()
    if (slice.length >= 40) {
      chunks.push(slice)
    }
    if (end >= cleaned.length) break
    start = Math.max(end - overlapChars, start + 1)
  }
  return chunks
}

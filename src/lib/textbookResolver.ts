/**
 * Textbook Resolver & Real-Time Auto-Scroll Engine (NCERT STEM Platform)
 * ----------------------------------------------------------------------
 * Resolves pedagogical teaching concepts, exercise numbers, examples, and topics
 * to exact PDF pages, bounding coordinates, and scroll targets in real time.
 */

import {
  TextbookChapter,
  TextbookIndexItem,
  getChapter,
  getChapterByPdf,
  getAllChapters,
  searchIndex,
  normalizeSubject,
} from './textbookRegistry'

export interface TextbookResolveQuery {
  classLevel?: number | string
  subject?: string
  category?: string
  chapterNumber?: number | string
  chapterOrderIndex?: number
  chapterTitle?: string
  topic?: string
  conceptTitle?: string
  conceptName?: string
  capsuleTitle?: string
  sectionNumber?: string
  exampleNumber?: string | number
  exerciseNumber?: string
  questionNumber?: string | number
  pdfPath?: string
  notesSourceFilename?: string
}

export interface ResolvedTextbookTarget {
  chapter: TextbookChapter
  matchedItem: TextbookIndexItem
  pdfPath: string
  page: number
  bbox: [number, number, number, number]
  topPercent: number
  scrollTargetY: number
  scrollUrl: string
  matchType:
    | 'exact_section'
    | 'exact_example'
    | 'exact_exercise'
    | 'exact_question'
    | 'fuzzy_topic'
    | 'proportional'
    | 'chapter_first_page'
  confidence: number
  label: string
}

export interface ResolveBookForChapterParams {
  classLevel?: number | string
  category?: string
  subject?: string
  chapterTitle?: string
  chapterOrderIndex?: number
  notesSourceFilename?: string
}

export interface ResolvedBook {
  id: string
  classLevel: number
  subject: string
  chapterNumber: number
  title: string
  chapterTitle: string
  pdfUrl: string
  totalPages: number
  pageWidth: number
  pageHeight: number
  bookCode: string
}

export interface ResolveTargetPageForLessonParams {
  conceptIndex?: number
  totalConcepts?: number
  moduleIndex?: number
  totalModules?: number
  totalPages: number
  conceptName?: string
  capsuleTitle?: string
  chapterNumber?: number
  classLevel?: number | string
  subject?: string
  pdfPath?: string
  content?: string
  extractedPage?: number
}

function normalizeStr(s: string): string {
  return (s || '')
    .toLowerCase()
    .replace(/[^a-z0-9]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
}

/**
 * Extracts the chapter number from a chapter title, order index, or filename.
 */
export function extractChapterNumber(input: string): number | null {
  if (!input) return null
  const chMatch = input.match(/chapter\s*(\d+)/i) || input.match(/\bch\.?\s*(\d+)/i)
  if (chMatch) return parseInt(chMatch[1], 10)

  const fnMatch = input.match(/([a-z]+)(\d)(\d\d)/i)
  if (fnMatch) {
    const pt = parseInt(fnMatch[2], 10)
    const chInPt = parseInt(fnMatch[3], 10)
    if (pt === 2) {
      const code = fnMatch[1].toLowerCase()
      if (code === 'keph') return 7 + chInPt
      if (code === 'kech') return 6 + chInPt
      if (code === 'lemh') return 6 + chInPt
      if (code === 'iemh') return 8 + chInPt
    }
    return chInPt
  }

  const numMatch = input.match(/\b(\d+)\b/)
  return numMatch ? parseInt(numMatch[1], 10) : null
}

/**
 * Resolves the authentic textbook chapter for a given curriculum chapter.
 */
/**
 * Converts any local textbook path or filename into the official NCERT online PDF URL.
 * e.g. '/9/class9_maths/pt1/iemh101.pdf' -> 'https://ncert.nic.in/textbook/pdf/iemh101.pdf'
 * e.g. 'keph101 (1).pdf' -> 'https://ncert.nic.in/textbook/pdf/keph101.pdf'
 */
export function toNcertPdfUrl(pathOrFilename: string): string {
  if (!pathOrFilename) return ''
  if (pathOrFilename.startsWith('http://') || pathOrFilename.startsWith('https://')) {
    return pathOrFilename
  }
  const clean = pathOrFilename.replace(/\\/g, '/').split('/').pop() || ''
  const filename = clean.replace(/\s*\(\d+\)/, '').trim()
  if (filename.endsWith('.pdf')) {
    return 'https://ncert.nic.in/textbook/pdf/' + filename
  }
  return pathOrFilename
}

/**
 * Constructs the canonical official NCERT textbook PDF URL for any class and subject.
 */
export function constructNcertPdfUrl(
  classLevel: number | string,
  subject: string,
  chapterNumber: number | string
): string {
  const normClass = typeof classLevel === 'string' ? parseInt(classLevel.replace(/\D/g, ''), 10) : classLevel
  const ch = typeof chapterNumber === 'string' ? parseInt(chapterNumber.replace(/\D/g, ''), 10) : chapterNumber
  const sub = normalizeSubject(subject)

  const pad = (n: number) => (n < 10 ? '0' + n : '' + n)

  // Class 9
  if (normClass === 9) {
    if (sub === 'mathematics') {
      if (ch <= 8) return 'https://ncert.nic.in/textbook/pdf/iemh10' + ch + '.pdf'
      return 'https://ncert.nic.in/textbook/pdf/iemh20' + (ch - 8) + '.pdf'
    }
    if (sub === 'science') {
      return 'https://ncert.nic.in/textbook/pdf/iesc1' + pad(ch) + '.pdf'
    }
  }

  // Class 10
  if (normClass === 10) {
    if (sub === 'mathematics') {
      return 'https://ncert.nic.in/textbook/pdf/jemh1' + pad(ch) + '.pdf'
    }
    if (sub === 'science') {
      return 'https://ncert.nic.in/textbook/pdf/jesc1' + pad(ch) + '.pdf'
    }
  }

  // Class 11
  if (normClass === 11) {
    if (sub === 'mathematics') {
      return 'https://ncert.nic.in/textbook/pdf/kemh1' + pad(ch) + '.pdf'
    }
    if (sub === 'physics') {
      if (ch <= 7) return 'https://ncert.nic.in/textbook/pdf/keph10' + ch + '.pdf'
      return 'https://ncert.nic.in/textbook/pdf/keph20' + (ch - 7) + '.pdf'
    }
    if (sub === 'chemistry') {
      if (ch <= 6) return 'https://ncert.nic.in/textbook/pdf/kech10' + ch + '.pdf'
      return 'https://ncert.nic.in/textbook/pdf/kech20' + (ch - 6) + '.pdf'
    }
    if (sub === 'biology' || sub === 'science') {
      return 'https://ncert.nic.in/textbook/pdf/kebo1' + pad(ch) + '.pdf'
    }
  }

  // Class 12
  if (normClass === 12) {
    if (sub === 'mathematics') {
      if (ch <= 6) return 'https://ncert.nic.in/textbook/pdf/lemh10' + ch + '.pdf'
      return 'https://ncert.nic.in/textbook/pdf/lemh20' + (ch - 6) + '.pdf'
    }
    if (sub === 'physics') {
      if (ch <= 8) return 'https://ncert.nic.in/textbook/pdf/leph10' + ch + '.pdf'
      return 'https://ncert.nic.in/textbook/pdf/leph20' + (ch - 8) + '.pdf'
    }
    if (sub === 'chemistry') {
      if (ch <= 5) return 'https://ncert.nic.in/textbook/pdf/lech10' + ch + '.pdf'
      return 'https://ncert.nic.in/textbook/pdf/lech20' + (ch - 5) + '.pdf'
    }
    if (sub === 'biology' || sub === 'science') {
      return 'https://ncert.nic.in/textbook/pdf/lebo1' + pad(ch) + '.pdf'
    }
  }

  return 'https://ncert.nic.in/textbook/pdf/jemh1' + pad(ch) + '.pdf'
}

export function resolveBookForChapter(params: ResolveBookForChapterParams): ResolvedBook | null {
  const { classLevel, category, subject, chapterTitle, chapterOrderIndex, notesSourceFilename } = params
  const targetSub = subject || category || ''

  // 1. Try resolving by notesSourceFilename
  if (notesSourceFilename) {
    const ch = getChapterByPdf(notesSourceFilename)
    if (ch) {
      return {
        id: ch.id,
        classLevel: ch.classLevel,
        subject: ch.subject,
        chapterNumber: ch.chapterNumber,
        title: ch.chapterTitle,
        chapterTitle: ch.chapterTitle,
        pdfUrl: toNcertPdfUrl(ch.pdfPath),
        totalPages: ch.totalPages,
        pageWidth: ch.pageWidth,
        pageHeight: ch.pageHeight,
        bookCode: ch.bookCode,
      }
    }
  }

  // 2. Try resolving by classLevel + subject + chapterOrderIndex
  const chNum = chapterOrderIndex ?? (chapterTitle ? extractChapterNumber(chapterTitle) : undefined)
  if (classLevel && targetSub && chNum) {
    const ch = getChapter(classLevel, targetSub, chNum)
    if (ch) {
      return {
        id: ch.id,
        classLevel: ch.classLevel,
        subject: ch.subject,
        chapterNumber: ch.chapterNumber,
        title: ch.chapterTitle,
        chapterTitle: ch.chapterTitle,
        pdfUrl: toNcertPdfUrl(ch.pdfPath),
        totalPages: ch.totalPages,
        pageWidth: ch.pageWidth,
        pageHeight: ch.pageHeight,
        bookCode: ch.bookCode,
      }
    }
  }

  // 3. Try resolving by chapterTitle fuzzy search
  if (chapterTitle) {
    const normSearch = normalizeStr(chapterTitle)
    const normCls = classLevel ? parseInt(String(classLevel).replace(/\D/g, ''), 10) : undefined
    const normSub = targetSub ? normalizeSubject(targetSub) : undefined

    const match = getAllChapters().find((c) => {
      if (normCls && c.classLevel !== normCls) return false
      if (normSub && normalizeSubject(c.subject) !== normSub) return false
      const cTitle = normalizeStr(c.chapterTitle)
      return cTitle.includes(normSearch) || normSearch.includes(cTitle)
    })

    if (match) {
      return {
        id: match.id,
        classLevel: match.classLevel,
        subject: match.subject,
        chapterNumber: match.chapterNumber,
        title: match.chapterTitle,
        chapterTitle: match.chapterTitle,
        pdfUrl: toNcertPdfUrl(match.pdfPath),
        totalPages: match.totalPages,
        pageWidth: match.pageWidth,
        pageHeight: match.pageHeight,
        bookCode: match.bookCode,
      }
    }
  }

  // 4. Fallback: construct authentic NCERT URL for any unindexed chapter
  if (classLevel && targetSub && chNum) {
    const ncertUrl = constructNcertPdfUrl(classLevel, targetSub, chNum)
    return {
      id: `cbse-class${classLevel}-${normalizeSubject(targetSub)}-ch${chNum}`,
      classLevel: typeof classLevel === 'number' ? classLevel : parseInt(String(classLevel).replace(/\D/g, ''), 10) || 10,
      subject: targetSub,
      chapterNumber: chNum,
      title: chapterTitle || `Chapter ${chNum}`,
      chapterTitle: chapterTitle || `Chapter ${chNum}`,
      pdfUrl: ncertUrl,
      totalPages: 30,
      pageWidth: 595,
      pageHeight: 842,
      bookCode: ncertUrl.split('/').pop()?.slice(0, 4) || '',
    }
  }

  return null
}

/**
 * Resolves a teacher's lesson topic or question into exact PDF page coordinates.
 */
export function resolveTextbookTarget(query: TextbookResolveQuery): ResolvedTextbookTarget | null {
  let chapter: TextbookChapter | undefined

  if (query.pdfPath || query.notesSourceFilename) {
    chapter = getChapterByPdf(query.pdfPath || query.notesSourceFilename || '')
  }

  const sub = query.subject || query.category
  const chNum = query.chapterNumber ?? query.chapterOrderIndex ?? (query.chapterTitle ? extractChapterNumber(query.chapterTitle) : undefined)

  if (!chapter && query.classLevel && sub && chNum) {
    chapter = getChapter(query.classLevel, sub, chNum)
  }

  if (!chapter && query.chapterTitle) {
    const normTitle = normalizeStr(query.chapterTitle)
    chapter = getAllChapters().find((c) => {
      const cTitle = normalizeStr(c.chapterTitle)
      return cTitle.includes(normTitle) || normTitle.includes(cTitle)
    })
  }

  if (!chapter) return null

  // 1. Exact Exercise Match
  if (query.exerciseNumber) {
    const exNumNorm = String(query.exerciseNumber).trim().toLowerCase().replace(/^exercise\s*/i, '')
    const exReg = new RegExp(`\\b(?:exercise|ex\\.?)\\s*${exNumNorm.replace('.', '\\.')}\\b`, 'i')
    const matchedEx = chapter.exercises.find((ex) => {
      const eNum = ex.number.toLowerCase()
      return (
        eNum === exNumNorm ||
        eNum.endsWith(`.${exNumNorm}`) ||
        eNum === `${chapter.chapterNumber}.${exNumNorm}` ||
        exReg.test(ex.title)
      )
    })

    if (matchedEx) {
      if (query.questionNumber) {
        const qNumStr = String(query.questionNumber).trim().replace(/^(?:question|q\.?|problem)\s*/i, '')
        const qReg = new RegExp(`\\b(?:question|q\\.?|problem)?\\s*${qNumStr}\\b`, 'i')
        const matchedQ = matchedEx.questions.find(
          (q) => q.number === qNumStr || q.number.endsWith(`.${qNumStr}`) || qReg.test(q.title)
        )
        if (matchedQ) {
          return createResolvedTarget(chapter, matchedQ, 'exact_question', 1.0, `Exercise ${matchedEx.number} Q${matchedQ.number}`)
        }
      }
      return createResolvedTarget(chapter, matchedEx, 'exact_exercise', 0.98, matchedEx.title)
    }
  }

  // 2. Exact Example Match
  if (query.exampleNumber) {
    const exNumStr = String(query.exampleNumber).trim().replace(/^(?:example|eg\.?)\s*/i, '')
    const egReg = new RegExp(`\\b(?:example|eg\\.?)\\s*${exNumStr.replace('.', '\\.')}\\b`, 'i')
    const matchedEx = chapter.examples.find(
      (ex) =>
        ex.number === exNumStr ||
        ex.number.endsWith(`.${exNumStr}`) ||
        ex.number === `${chapter.chapterNumber}.${exNumStr}` ||
        egReg.test(ex.title)
    )
    if (matchedEx) {
      return createResolvedTarget(chapter, matchedEx, 'exact_example', 0.99, `Example ${matchedEx.number}`)
    }
  }

  // 3. Exact Section Number Match
  if (query.sectionNumber) {
    const sNum = String(query.sectionNumber).trim().replace(/^(?:section|sec\.?)\s*/i, '')
    const matchedSec = chapter.sections.find(
      (s) =>
        s.number === sNum ||
        s.number.endsWith(`.${sNum}`) ||
        s.number === `${chapter.chapterNumber}.${sNum}`
    )
    if (matchedSec) {
      return createResolvedTarget(chapter, matchedSec, 'exact_section', 0.99, `${matchedSec.number} ${matchedSec.title}`)
    }
  }

  // 4. Topic / Concept Title Matching
  const topicQuery = query.conceptName || query.conceptTitle || query.topic || query.capsuleTitle
  if (topicQuery) {
    const normTopic = normalizeStr(topicQuery)
    const topicTokens = normTopic.split(' ').filter((t) => t.length > 2)

    let bestItem: TextbookIndexItem | null = null
    let bestScore = 0

    // Check sections
    for (const sec of chapter.sections) {
      const normSec = normalizeStr(`${sec.number} ${sec.title}`)
      let score = 0
      if (normSec === normTopic || normSec.includes(normTopic) || normTopic.includes(normSec)) {
        score = 0.95
      } else if (topicTokens.length > 0) {
        const matches = topicTokens.filter((tok) => normSec.includes(tok)).length
        score = (matches / topicTokens.length) * 0.8
      }
      if (score > bestScore) {
        bestScore = score
        bestItem = sec
      }
    }

    // Check examples
    for (const ex of chapter.examples) {
      const normEx = normalizeStr(ex.title)
      let score = 0
      if (normEx.includes(normTopic)) {
        score = 0.9
      } else if (topicTokens.length > 0) {
        const matches = topicTokens.filter((tok) => normEx.includes(tok)).length
        score = (matches / topicTokens.length) * 0.75
      }
      if (score > bestScore) {
        bestScore = score
        bestItem = ex
      }
    }

    // Check exercises & questions
    for (const exer of chapter.exercises) {
      const normExer = normalizeStr(exer.title)
      if (normExer.includes(normTopic)) {
        const score = 0.9
        if (score > bestScore) {
          bestScore = score
          bestItem = exer
        }
      }
      for (const q of exer.questions) {
        const normQ = normalizeStr(q.title)
        if (normQ.includes(normTopic)) {
          const score = 0.88
          if (score > bestScore) {
            bestScore = score
            bestItem = q
          }
        }
      }
    }

    if (bestItem && bestScore >= 0.4) {
      return createResolvedTarget(chapter, bestItem, 'fuzzy_topic', bestScore, bestItem.title)
    }

    // Fall back to searchIndex across chapter
    const searchHits = searchIndex(topicQuery, {
      classLevel: chapter.classLevel,
      subject: chapter.subject,
      chapterNumber: chapter.chapterNumber,
    })
    if (searchHits.length > 0 && searchHits[0].relevance >= 0.6) {
      return createResolvedTarget(chapter, searchHits[0].item, 'fuzzy_topic', searchHits[0].relevance, searchHits[0].item.title)
    }
  }

  // Fallback: Chapter Page 1
  const firstItem: TextbookIndexItem = chapter.sections[0] || {
    id: 'ch-start',
    number: '1',
    title: chapter.chapterTitle,
    page: 1,
    bbox: [0, 0, chapter.pageWidth, 50],
    topPercent: 0.0,
  }

  return createResolvedTarget(chapter, firstItem, 'chapter_first_page', 0.5, chapter.chapterTitle)
}

function createResolvedTarget(
  chapter: TextbookChapter,
  item: TextbookIndexItem,
  matchType: ResolvedTextbookTarget['matchType'],
  confidence: number,
  label: string
): ResolvedTextbookTarget {
  const topY = item.bbox ? item.bbox[1] : 0
  const topPercent = item.topPercent ?? (topY / (chapter.pageHeight || 720))
  const scrollTargetY = Math.round(topY)

  const scrollUrl = `${chapter.pdfPath}#page=${item.page}&view=FitH,${scrollTargetY}`

  return {
    chapter,
    matchedItem: item,
    pdfPath: chapter.pdfPath,
    page: item.page,
    bbox: item.bbox,
    topPercent,
    scrollTargetY,
    scrollUrl,
    matchType,
    confidence,
    label,
  }
}

/**
 * Automatically computes the target PDF page for a lesson concept.
 * Combines explicit page instructions, figure manifest extracted pages,
 * exact exercise/example/section lookup, topic search, and proportional interpolation fallback.
 */
export function resolveTargetPageForLesson(params: ResolveTargetPageForLessonParams): number {
  const {
    content,
    extractedPage,
    conceptIndex = 0,
    totalConcepts = 1,
    moduleIndex = 0,
    totalModules = 1,
    totalPages,
    conceptName,
    capsuleTitle,
    chapterNumber,
    classLevel,
    subject,
    pdfPath,
  } = params

  const effectiveTotalPages = Math.max(1, totalPages || 20)

  // 1. Explicit tutor directive: "Page 12", "page 5", "pg. 8"
  if (content) {
    const pageMatch = content.match(/\b(?:page|pg\.?|p\.)\s*(\d+)\b/i)
    if (pageMatch) {
      const parsed = parseInt(pageMatch[1], 10)
      if (!isNaN(parsed) && parsed > 0) {
        return Math.max(1, Math.min(effectiveTotalPages, parsed))
      }
    }
  }

  // 2. Direct extracted figure page from manifest
  if (typeof extractedPage === 'number' && extractedPage > 0) {
    return Math.max(1, Math.min(effectiveTotalPages, extractedPage))
  }

  // 3. Extracted diagram / figure reference in content or filename (e.g. "fig_10_2" or "Fig. 10.2")
  if (content) {
    const figMatch = content.match(/fig(?:ure)?[_\s\.]*(\d+)[_\s\.]+(\d+)/i)
    if (figMatch) {
      const secNum = `${figMatch[1]}.${figMatch[2]}`
      const matched = resolveTextbookTarget({
        classLevel,
        subject,
        chapterNumber,
        pdfPath,
        sectionNumber: secNum,
      })
      if (matched && matched.matchType !== 'chapter_first_page' && matched.page) {
        return Math.max(1, Math.min(effectiveTotalPages, matched.page))
      }
    }
  }

  // 4. Scan content and conceptName for Exercise, Example, Section, or Theorem patterns
  const scanText = [content, conceptName].filter(Boolean).join(' ')
  if (scanText) {
    // Check Exercise & Question
    const exMatch = scanText.match(/\b(?:exercise|ex\.?)\s*(\d+(?:\.\d+)?)/i)
    const qMatch = scanText.match(/\b(?:question|q\.?|problem)\s*(\d+)/i)
    if (exMatch) {
      const matched = resolveTextbookTarget({
        classLevel,
        subject,
        chapterNumber,
        pdfPath,
        exerciseNumber: exMatch[1],
        questionNumber: qMatch ? qMatch[1] : undefined,
      })
      if (matched && matched.matchType !== 'chapter_first_page' && matched.page) {
        return Math.max(1, Math.min(effectiveTotalPages, matched.page))
      }
    }

    // Check Example
    const egMatch = scanText.match(/\b(?:example|eg\.?)\s*(\d+(?:\.\d+)?)/i)
    if (egMatch) {
      const matched = resolveTextbookTarget({
        classLevel,
        subject,
        chapterNumber,
        pdfPath,
        exampleNumber: egMatch[1],
      })
      if (matched && matched.matchType !== 'chapter_first_page' && matched.page) {
        return Math.max(1, Math.min(effectiveTotalPages, matched.page))
      }
    }

    // Check Section
    const secMatch = scanText.match(/\b(?:section|sec\.?)\s*(\d+(?:\.\d+)?)/i)
    if (secMatch) {
      const matched = resolveTextbookTarget({
        classLevel,
        subject,
        chapterNumber,
        pdfPath,
        sectionNumber: secMatch[1],
      })
      if (matched && matched.matchType !== 'chapter_first_page' && matched.page) {
        return Math.max(1, Math.min(effectiveTotalPages, matched.page))
      }
    }
  }

  // 5. Try exact topic match from textbook index
  const topicCandidates: string[] = []
  if (conceptName) topicCandidates.push(conceptName)
  if (capsuleTitle) topicCandidates.push(capsuleTitle)
  if (content) {
    if (content.includes('|')) {
      const parts = content.split('|').map((p) => p.trim()).filter((p) => p.length > 2 && !p.includes('/') && !p.includes('.webp') && !p.includes('.png'))
      topicCandidates.push(...parts)
    } else {
      topicCandidates.push(content)
    }
  }

  for (const cand of topicCandidates) {
    const matched = resolveTextbookTarget({
      classLevel,
      subject,
      chapterNumber,
      conceptName: cand,
      pdfPath,
    })
    if (matched && matched.matchType !== 'chapter_first_page' && matched.confidence >= 0.4) {
      return Math.max(1, Math.min(effectiveTotalPages, matched.page))
    }
  }

  // 6. Mathematical concept progression interpolation across modules:
  const effTotalModules = Math.max(1, totalModules)
  const effTotalConcepts = Math.max(1, totalConcepts)
  const pagesPerModule = effectiveTotalPages / effTotalModules

  const basePage = moduleIndex === 0 ? 1 : Math.round(moduleIndex * pagesPerModule)
  const conceptOffset =
    effTotalConcepts > 1
      ? (conceptIndex / (effTotalConcepts - 1)) * Math.max(0, pagesPerModule - 1)
      : 0
  const targetPage = Math.round(basePage + conceptOffset)

  return Math.max(1, Math.min(effectiveTotalPages, targetPage))
}

/**
 * Computes the auto-scroll target when the teacher moves to a concept or stage in class.
 */
export function getAutoScrollTargetForLesson(params: {
  capsuleTitle?: string
  conceptName?: string
  classLevel?: number | string
  subject?: string
  chapterNumber?: number | string
}): ResolvedTextbookTarget | null {
  const { capsuleTitle, conceptName, classLevel, subject, chapterNumber } = params

  if (conceptName) {
    const res = resolveTextbookTarget({
      classLevel,
      subject,
      chapterNumber,
      conceptTitle: conceptName,
    })
    if (res && res.confidence >= 0.5) return res
  }

  if (capsuleTitle) {
    const res = resolveTextbookTarget({
      classLevel,
      subject,
      chapterNumber,
      topic: capsuleTitle,
    })
    if (res) return res
  }

  return resolveTextbookTarget({
    classLevel,
    subject,
    chapterNumber,
  })
}

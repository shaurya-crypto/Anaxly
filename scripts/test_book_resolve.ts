import {
  resolveBookForChapter,
  constructNcertPdfUrl,
  toNcertPdfUrl,
  resolveLocalPdfUrl,
} from '../src/lib/textbookResolver'

console.log('=== TESTING TEXTBOOK RESOLVER & SAME-ORIGIN PDF PROXY RESOLUTION (CLASSES 9-12) ===\n')

const testCases = [
  { classLevel: 'Class 9', subject: 'Mathematics', chapterTitle: 'Chapter 1: Orienting Yourself: The Use of Coordinates', chapterOrderIndex: 1, expectedFile: 'iemh101.pdf' },
  { classLevel: 'Class 9', subject: 'Mathematics', chapterTitle: 'Chapter 14: Math of Space: Surface Area and Volume', chapterOrderIndex: 14, expectedFile: 'iemh206.pdf' },
  { classLevel: 'Class 9', subject: 'Science', chapterTitle: 'Chapter 1: Matter in Our Surroundings', chapterOrderIndex: 1, expectedFile: 'iesc101.pdf' },
  { classLevel: 'Class 9', subject: 'Science', chapterTitle: 'Chapter 3: Tissues in Action', chapterOrderIndex: 3, expectedFile: 'iesc103.pdf' },
  { classLevel: 'Class 10', subject: 'Mathematics', chapterTitle: 'Chapter 1: Real Numbers', chapterOrderIndex: 1, expectedFile: 'jemh101.pdf' },
  { classLevel: 'Class 10', subject: 'Science', chapterTitle: 'Chapter 1: Chemical Reactions and Equations', chapterOrderIndex: 1, expectedFile: 'jesc101.pdf' },
  { classLevel: 'Class 10', subject: 'Science', chapterTitle: 'Chapter 5: Life Processes', chapterOrderIndex: 5, expectedFile: 'jesc105.pdf' },
  { classLevel: 'Class 11', subject: 'Physics', chapterTitle: 'Chapter 2: Motion in a Straight Line', chapterOrderIndex: 2, expectedFile: 'keph102.pdf' },
  { classLevel: 'Class 11', subject: 'Chemistry', chapterTitle: 'Chapter 1: Some Basic Concepts of Chemistry', chapterOrderIndex: 1, expectedFile: 'kech101.pdf' },
  { classLevel: 'Class 11', subject: 'Biology', chapterTitle: 'Chapter 1: The Living World', chapterOrderIndex: 1, expectedFile: 'kebo101.pdf' },
  { classLevel: 'Class 12', subject: 'Mathematics', chapterTitle: 'Chapter 7: Integrals', chapterOrderIndex: 7, expectedFile: 'lemh201.pdf' },
  { classLevel: 'Class 12', subject: 'Physics', chapterTitle: 'Chapter 9: Ray Optics and Optical Instruments', chapterOrderIndex: 9, expectedFile: 'leph201.pdf' },
  { classLevel: 'Class 12', subject: 'Chemistry', chapterTitle: 'Chapter 1: Solutions', chapterOrderIndex: 1, expectedFile: 'lech101.pdf' },
  { classLevel: 'Class 12', subject: 'Biology', chapterTitle: 'Chapter 5: Molecular Basis of Inheritance', chapterOrderIndex: 5, expectedFile: 'lebo105.pdf' },
]

let allPassed = true

for (const tc of testCases) {
  const book = resolveBookForChapter({
    classLevel: tc.classLevel,
    subject: tc.subject,
    chapterTitle: tc.chapterTitle,
    chapterOrderIndex: tc.chapterOrderIndex,
  })

  if (!book) {
    console.error(`[FAIL] Could not resolve book for ${tc.classLevel} ${tc.subject} ${tc.chapterTitle}`)
    allPassed = false
    continue
  }

  const expectedUrl = `/api/pdf-proxy?file=${tc.expectedFile}`
  const isSameOriginProxy = book.pdfUrl === expectedUrl
  const isDirectExternalBlocked = book.pdfUrl.startsWith('https://ncert.nic.in')

  if (isSameOriginProxy && !isDirectExternalBlocked) {
    console.log(`[PASS] ${tc.classLevel} ${tc.subject} Ch ${book.chapterNumber} -> ${book.pdfUrl}`)
  } else {
    console.error(`[FAIL] ${tc.classLevel} ${tc.subject} Ch ${book.chapterNumber}: expected ${expectedUrl}, got ${book.pdfUrl}`)
    allPassed = false
  }
}

console.log('\n--- Test resolveLocalPdfUrl and toNcertPdfUrl with legacy strings ---')
const sampleLegacy = ['/9/class 9th science/iesc103.pdf', '/10/class10_maths/jemh101.pdf', 'iemh206.pdf', 'keph101 (1).pdf']
for (const s of sampleLegacy) {
  const resolved = resolveLocalPdfUrl(s)
  const ncertUrl = toNcertPdfUrl(s)
  const ok = resolved.startsWith('/api/pdf-proxy?file=') && !resolved.includes('(') && ncertUrl.startsWith('https://ncert.nic.in/textbook/pdf/')
  console.log(`Legacy "${s}" -> proxy="${resolved}" | ncert="${ncertUrl}" [${ok ? 'PASS' : 'FAIL'}]`)
  if (!ok) allPassed = false
}

// Sanity check canonical NCERT URL construction for Class 11/12 Bio/Phy/Chem
const bioUrl = constructNcertPdfUrl(11, 'Biology', 10)
if (bioUrl !== 'https://ncert.nic.in/textbook/pdf/kebo110.pdf') {
  console.error(`[FAIL] constructNcertPdfUrl(11, Biology, 10) returned ${bioUrl}`)
  allPassed = false
}

if (allPassed) {
  console.log('\nALL CLASS 9-12 TEXTBOOK RESOLUTION CHECKS PASSED WITH SAME-ORIGIN /api/pdf-proxy!')
} else {
  console.error('\nSOME CHECKS FAILED!')
  process.exit(1)
}

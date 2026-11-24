import { resolveBookForChapter, constructNcertPdfUrl, toNcertPdfUrl, resolveLocalPdfUrl } from '../src/lib/textbookResolver'

console.log('=== TESTING TEXTBOOK RESOLVER & NCERT ONLINE PDF STREAMING ===\n')

const testCases = [
  { classLevel: 'Class 9', subject: 'Mathematics', chapterTitle: 'Chapter 1: Orienting Yourself: The Use of Coordinates', chapterOrderIndex: 1 },
  { classLevel: 'Class 9', subject: 'Mathematics', chapterTitle: 'Chapter 14: Math of Space: Surface Area and Volume', chapterOrderIndex: 14 },
  { classLevel: 'Class 9', subject: 'Science', chapterTitle: 'Chapter 1: Exploration: Entering the World of Secondary Science', chapterOrderIndex: 1 },
  { classLevel: 'Class 9', subject: 'Science', chapterTitle: 'Chapter 3: Tissues in Action', chapterOrderIndex: 3 },
  { classLevel: 'Class 10', subject: 'Mathematics', chapterTitle: 'Chapter 1: Real Numbers', chapterOrderIndex: 1 },
  { classLevel: 'Class 10', subject: 'Science', chapterTitle: 'Chapter 1: Chemical Reactions and Equations', chapterOrderIndex: 1 },
  { classLevel: 'Class 11', subject: 'Physics', chapterTitle: 'Chapter 2: Motion in a Straight Line', chapterOrderIndex: 2 },
  { classLevel: 'Class 11', subject: 'Chemistry', chapterTitle: 'Chapter 1: Some Basic Concepts of Chemistry', chapterOrderIndex: 1 }
]

let allPassed = true

for (const tc of testCases) {
  const book = resolveBookForChapter({
    classLevel: tc.classLevel,
    subject: tc.subject,
    chapterTitle: tc.chapterTitle,
    chapterOrderIndex: tc.chapterOrderIndex
  })

  if (!book) {
    console.error(`[FAIL] Could not resolve book for ${tc.classLevel} ${tc.subject} ${tc.chapterTitle}`)
    allPassed = false
    continue
  }

  const isOnlineNcert = book.pdfUrl.startsWith('https://ncert.nic.in/textbook/pdf/')
  const isLocalBroken = book.pdfUrl.startsWith('/9/') || book.pdfUrl.startsWith('/10/') || book.pdfUrl.startsWith('/11/') || book.pdfUrl.startsWith('/12/')

  if (isOnlineNcert && !isLocalBroken) {
    console.log(`[PASS] ${tc.classLevel} ${tc.subject} Ch ${book.chapterNumber}:`)
    console.log(`       URL: ${book.pdfUrl}`)
  } else {
    console.error(`[FAIL] Invalid URL resolved for ${tc.classLevel} ${tc.subject} Ch ${book.chapterNumber}: ${book.pdfUrl}`)
    allPassed = false
  }
}

console.log('\n--- Test resolveLocalPdfUrl and toNcertPdfUrl with legacy strings ---')
const sampleLegacy = ['/9/class 9th science/iesc103.pdf', '/10/class10_maths/jemh101.pdf', 'iemh206.pdf', 'keph101 (1).pdf']
for (const s of sampleLegacy) {
  const resolved = resolveLocalPdfUrl(s)
  const ok = resolved.startsWith('https://ncert.nic.in/textbook/pdf/')
  console.log(`Legacy "${s}" -> "${resolved}" [${ok ? 'PASS' : 'FAIL'}]`)
  if (!ok) allPassed = false
}

if (allPassed) {
  console.log('\n🎉 ALL TEXTBOOK RESOLUTION CHECKS PASSED WITH 100% ONLINE NCERT URLS!')
} else {
  console.error('\n❌ SOME CHECKS FAILED!')
  process.exit(1)
}

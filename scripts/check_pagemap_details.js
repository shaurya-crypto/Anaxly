const fs = require('fs');
const data = JSON.parse(fs.readFileSync('src/lib/textbookPageMap.json', 'utf8'));

const p11 = data.chapters.filter(c => c.id && c.id.includes('cbse-class11-physics'));
console.log(`Found ${p11.length} Class 11 Physics chapters in textbookPageMap.json:`);

for (const c of p11) {
  console.log(`\n------------------------------------------------------`);
  console.log(`ID: ${c.id} | Ch ${c.chapterNumber}: ${c.chapterTitle}`);
  console.log(`  PDF: ${c.pdfPath}`);
  console.log(`  Pages: ${c.totalPages} (width: ${c.pageWidth}, height: ${c.pageHeight})`);
  console.log(`  Sections (${c.sections ? c.sections.length : 0}):`);
  if (c.sections && c.sections.length > 0) {
    c.sections.slice(0, 4).forEach(s => {
      console.log(`    Sec ${s.number}: ${s.title} (Page ${s.page})`);
    });
  }
  console.log(`  Examples (${c.examples ? c.examples.length : 0})`);
  console.log(`  Exercises (${c.exercises ? c.exercises.length : 0})`);
  console.log(`  Questions (${c.questions ? c.questions.length : 0})`);
}
const fs = require('fs');

const filePath = 'src/app/dashboard/[id]/class/[moduleId]/page.tsx';
let content = fs.readFileSync(filePath, 'utf8');
const isCrlf = content.includes('\r\n');
if (isCrlf) {
  content = content.replace(/\r\n/g, '\n');
}

// 1. Neutralize nextConceptLockedDossier so upcoming concepts are never leaked
const oldDossierBlock = `    const nextConceptIdx = currentConceptIndex + 1
    const nextConceptName = keyConcepts[nextConceptIdx]
    let nextConceptLockedDossier = ''
    if (nextConceptName) {
      const nextDossierRaw = buildSingleConceptMicroDossier(
        nextConceptIdx,
        keyConcepts,
        activeModule,
        resolvedBoard,
        resolvedClassLevel,
        resolvedSubject,
        chapterName,
        parsedWorkedExamples,
        parsedMisconceptions
      )
      nextConceptLockedDossier = \`\\n========================================================================================\\nUPCOMING CURRICULUM SYLLABUS DATA (PREVIEW ONLY — STRICTLY LOCKED & GATED):\\n========================================================================================\\n[STATUS: [LOCKED] UNTIL CONCEPT \${currentConceptIndex + 1} FULLY COMPLETED & CONFIRMED]\\nDo NOT teach, explain, or mention the following upcoming concept yet. It is provided ONLY so you are aware of the upcoming curriculum trajectory while the background engine synthesizes its visuals in the database:\\n\${nextDossierRaw}\\n[END LOCKED PREVIEW — REMAIN 100% ON CONCEPT \${currentConceptIndex + 1}: "\${currentConcept}"]\\n\`
    }`;

const newDossierBlock = `    const nextConceptIdx = currentConceptIndex + 1
    const nextConceptName = keyConcepts[nextConceptIdx]
    // STRICT SINGLE-CONCEPT ENFORCEMENT: Never inject upcoming concept data into active prompt
    const nextConceptLockedDossier = ''`;

if (!content.includes(oldDossierBlock)) {
  console.error('oldDossierBlock not found in page.tsx');
  process.exit(1);
}
content = content.replace(oldDossierBlock, newDossierBlock);

// 2. Update visual flexibility
const oldVisualBlock = `4. MULTIMEDIA & VISUAL TOOLS:
   - Concept Start Visuals: At the START of every concept, dispatch BOTH:
     1. search_and_show_image(query="<detailed 10-25 word academic query specifying class, subject, labeled parts>", title="...", caption="...") for an authentic scientific diagram.
     2. search_and_show_video(query="<animated short video showing animation to understand <concept>>", title="...", description="...") for an animated demonstration video.
   - Single Image Invariant: Render strictly ONE image per concept unless the student explicitly asks for another image. Do not spawn multiple images.`;

const newVisualBlock = `4. MULTIMEDIA & VISUAL TOOLS:
   - Mandatory Concept Visuals: At the START of every visual concept, dispatch:
     1. search_and_show_image(query="<detailed 10-25 word academic query specifying class, subject, labeled parts>", title="...", caption="...") for an authentic scientific diagram.
     2. search_and_show_video(query="<animated short video showing animation to understand <concept>>", title="...", description="...") for an animated demonstration video.
   - Flexible Visuals: Start with 1 clear diagram so the board stays clean and uncluttered. If the student asks for additional diagrams, comparisons (e.g. plant vs animal cell, xylem vs phloem, different ray positions), or if a follow-up diagram helps explain a doubt, call search_and_show_image freely! Everything is flexible, natural, and responsive like a real master faculty tutor.`;

if (!content.includes(oldVisualBlock)) {
  console.error('oldVisualBlock not found in page.tsx');
  process.exit(1);
}
content = content.replace(oldVisualBlock, newVisualBlock);

if (isCrlf) {
  content = content.replace(/\n/g, '\r\n');
}

fs.writeFileSync(filePath, content, 'utf8');
console.log('page.tsx successfully updated!');

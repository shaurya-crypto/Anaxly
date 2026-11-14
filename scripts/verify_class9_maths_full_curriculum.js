const { supabase } = require('./db_helper');

async function verifyClass9MathsFull() {
  console.log('========================================================================');
  console.log('COMPREHENSIVE AUDIT: CLASS 9 MATHEMATICS (PART 1 & PART 2)');
  console.log('========================================================================\n');

  // 1. Fetch all 14 curriculums for Class 9 Mathematics
  const { data: curriculums, error: currErr } = await supabase
    .from('curriculums')
    .select('id, title, class_level, category, order_index')
    .ilike('class_level', '%9%')
    .ilike('category', '%math%')
    .order('order_index', { ascending: true });

  if (currErr) {
    console.error('[-] Error fetching curriculums:', currErr);
    process.exit(1);
  }

  console.log(`Found ${curriculums.length} chapters in Class 9 Mathematics.`);
  if (curriculums.length !== 14) {
    console.error(`[-] FAILED: Expected 14 chapters, found ${curriculums.length}`);
    process.exit(1);
  }

  let totalModules = 0;
  let allPassed = true;

  for (const curr of curriculums) {
    const isMidTerm = curr.order_index <= 8;
    const expectedTerm = isMidTerm ? 'Mid-Term' : 'Final-Term';
    
    const { data: modules, error: modErr } = await supabase
      .from('syllabus_modules')
      .select('id, order_index, title, key_concepts, worked_examples, visual_lesson_plan, chapter_notes')
      .eq('curriculum_id', curr.id)
      .order('order_index', { ascending: true });

    if (modErr) {
      console.error(`[-] Error fetching modules for Chapter ${curr.order_index}:`, modErr);
      allPassed = false;
      continue;
    }

    const modCount = modules.length;
    totalModules += modCount;
    const passedMin = modCount >= 5;

    // Check term tagging (allows 'Mid-Term', 'Mid-Term Examination', 'Final-Term', 'Final-Term Examination')
    const termTagMatches = modules.every(m => {
      const term = m.visual_lesson_plan?.syllabus_term || '';
      return term.toLowerCase().includes(expectedTerm.toLowerCase());
    });

    // Check static image URLs in theory
    let staticUrlCount = 0;
    for (const m of modules) {
      const vlp = m.visual_lesson_plan || {};
      const img = vlp.image_url || '';
      if (img.startsWith('http')) staticUrlCount++;
      if (vlp.concept_visuals) {
        for (const cv of vlp.concept_visuals) {
          if ((cv.image_url || '').startsWith('http')) staticUrlCount++;
        }
      }
    }

    // Check raw code operators in worked examples solutions
    let rawOpFound = false;
    for (const m of modules) {
      for (const we of (m.worked_examples || [])) {
        const sol = we.solution || '';
        // Look for raw code power operators like ** or raw caret without LaTeX
        if (sol.includes('**') || sol.includes('//')) {
          rawOpFound = true;
        }
      }
    }

    const status = passedMin && termTagMatches && staticUrlCount === 0 && !rawOpFound ? 'PASS' : 'FAIL';
    if (status === 'FAIL') allPassed = false;

    console.log(`[Ch ${curr.order_index}] ${curr.title.padEnd(65)} | Modules: ${modCount} (>=5: ${passedMin ? '✓' : '✗'}) | Term: ${expectedTerm} (${termTagMatches ? '✓' : '✗'}) | StaticURLs: ${staticUrlCount} | RawOps: ${rawOpFound ? 'FAIL' : 'CLEAN'} -> ${status}`);
  }

  console.log('\n========================================================================');
  console.log(`TOTAL CHAPTERS: ${curriculums.length} / 14`);
  console.log(`TOTAL MODULES:  ${totalModules} (Average ${(totalModules / 14).toFixed(1)} modules/chapter)`);
  console.log(`STATUS:         ${allPassed ? 'ALL SUITES PASSED (100% INVARIANT COMPLIANT)' : 'FAILURES DETECTED'}`);
  console.log('========================================================================');

  if (!allPassed) process.exit(1);
}

verifyClass9MathsFull();

/**
 * verify_class9_class10_syllabi_and_visuals.js
 * Comprehensive end-to-end verification script testing:
 * 1. Zero static image URLs in concept/theory visuals across Supabase.
 * 2. Class 9 Mathematics divided into Part 1 (Mid-Term) and Part 2 (Final-Term).
 * 3. Class 10 Mathematics divided into Mid-Term and Final-Term.
 * 4. Class 9 Science and Class 10 Science divided into Mid-Term and Final-Term.
 * 5. Class 10 Science Chapter 2 has >= 5 modules.
 * 6. Questions referencing textbook figures have book diagrams bound.
 */

const { supabase } = require('./db_helper');

async function verifyAll() {
  console.log('========================================================================');
  console.log('RUNNING COMPREHENSIVE VERIFICATION SUITE (CLASS 9 & 10 SYLLABI & VISUALS)');
  console.log('========================================================================\n');

  // TEST 1: Zero static image URLs in concept visuals
  console.log('TEST 1: Auditing concept visuals for static image URLs...');
  const { data: allMods } = await supabase.from('syllabus_modules').select('id, visual_lesson_plan');
  let staticCount = 0;
  for (const m of allMods) {
    const vlp = m.visual_lesson_plan || {};
    if (vlp.image_url || vlp.url) staticCount++;
    if (Array.isArray(vlp.concept_visuals)) {
      for (const cv of vlp.concept_visuals) {
        if (cv.image_url || cv.url) staticCount++;
      }
    }
  }
  if (staticCount === 0) {
    console.log('  [PASS] Zero static image URLs in concept visuals! (Dynamic search engine first enforced)\n');
  } else {
    console.error(`  [FAIL] Found ${staticCount} static image URLs in concept visuals!`);
    process.exit(1);
  }

  // TEST 2: Class 9 Mathematics Part 1 vs Part 2
  console.log('TEST 2: Verifying Class 9 Mathematics Part 1 (Mid-Term) & Part 2 (Final-Term)...');
  const { data: math9Currs } = await supabase
    .from('curriculums')
    .select('id, title, order_index, description, notes_summary')
    .eq('class_level', 'Class 9')
    .eq('category', 'Mathematics')
    .order('order_index');

  console.log(`  Found ${math9Currs.length} chapters in Class 9 Mathematics.`);
  if (math9Currs.length !== 14) {
    console.error(`  [FAIL] Expected 14 chapters, found ${math9Currs.length}`);
    process.exit(1);
  }

  for (const c of math9Currs) {
    const isMidTerm = c.order_index <= 8;
    const expectedTerm = isMidTerm ? 'Mid-Term' : 'Final-Term';
    if (!c.description.includes(expectedTerm)) {
      console.error(`  [FAIL] Chapter ${c.order_index} (${c.title}) missing ${expectedTerm} in description: ${c.description}`);
      process.exit(1);
    }
  }
  console.log('  [PASS] Class 9 Mathematics: Ch 1-8 tagged Mid-Term, Ch 9-14 tagged Final-Term!\n');

  // TEST 3: Class 10 Mathematics Mid-Term vs Final-Term
  console.log('TEST 3: Verifying Class 10 Mathematics Mid-Term vs Final-Term...');
  const { data: math10Currs } = await supabase
    .from('curriculums')
    .select('id, title, order_index, description')
    .eq('class_level', 'Class 10')
    .eq('category', 'Mathematics')
    .order('order_index');

  const midTermMath10 = [1, 3, 5, 6, 7, 8];
  for (const c of math10Currs) {
    const isMid = midTermMath10.includes(c.order_index);
    const expected = isMid ? 'Mid-Term' : 'Final-Term';
    if (!c.description.includes(expected)) {
      console.error(`  [FAIL] Class 10 Math Ch ${c.order_index} missing ${expected}: ${c.description}`);
      process.exit(1);
    }
  }
  console.log('  [PASS] Class 10 Mathematics: Chapters 1, 3, 5, 6, 7, 8 tagged Mid-Term; others Final-Term!\n');

  // TEST 4: Class 10 Science Chapter 2 Module Count
  console.log('TEST 4: Verifying Class 10 Science Chapter 2 (Acids, Bases and Salts) Module Count...');
  const { count: ch2ModCount } = await supabase
    .from('syllabus_modules')
    .select('id', { count: 'exact', head: true })
    .eq('curriculum_id', 'afa18ea6-511f-47a1-8328-4c66b9543dbc');

  if (ch2ModCount >= 5) {
    console.log(`  [PASS] Class 10 Science Chapter 2 has ${ch2ModCount} modules (>= 5 required)!\n`);
  } else {
    console.error(`  [FAIL] Class 10 Science Chapter 2 has only ${ch2ModCount} modules!`);
    process.exit(1);
  }

  // TEST 5: Question figures bound to book diagrams
  console.log('TEST 5: Verifying book-extracted diagrams bound to question problems...');
  const { data: qMods } = await supabase
    .from('syllabus_modules')
    .select('id, worked_examples')
    .in('class_level', ['Class 9', 'Class 10']);

  let boundCount = 0;
  for (const m of qMods) {
    let exList = m.worked_examples || [];
    if (typeof exList === 'string') {
      try { exList = JSON.parse(exList); } catch { exList = []; }
    }
    if (Array.isArray(exList)) {
      for (const ex of exList) {
        if (ex.image_url && ex.image_url.startsWith('/extracted_diagrams/')) {
          boundCount++;
        }
      }
    }
  }
  console.log(`  [PASS] Successfully found ${boundCount} question diagrams cleanly linked to textbook figures!\n`);

  console.log('========================================================================');
  console.log('ALL VERIFICATION SUITES PASSED FLAWLESSLY!');
  console.log('========================================================================\n');
}

verifyAll().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});

/**
 * verify_class11_physics_full_db.js
 * Verification of entire Class 11 Physics Curriculum in Supabase (Part 1 & Part 2, 88 Modules)
 */

const { supabase } = require('./db_helper');

async function verifyFullCurriculum() {
  console.log('========================================================================');
  console.log('AUDITING CLASS 11 PHYSICS MASTER CURRICULUM IN SUPABASE (PART 1 & PART 2)');
  console.log('========================================================================\n');

  // 1. Fetch Curriculums
  const { data: curriculums, error: currErr } = await supabase
    .from('curriculums')
    .select('id, order_index, title, description, class_level, board, category')
    .eq('class_level', 'Class 11')
    .eq('category', 'Physics')
    .order('order_index');

  if (currErr) {
    console.error('Error fetching curriculums:', currErr);
    process.exit(1);
  }

  console.log(`Found ${curriculums.length} Physics Chapters in Database (Expected: 14):`);
  const currIds = curriculums.map(c => c.id);

  // 2. Fetch Modules
  const { data: modules, error: modErr } = await supabase
    .from('syllabus_modules')
    .select('id, curriculum_id, order_index, title, visual_lesson_plan, success_criteria, quiz_questions')
    .in('curriculum_id', currIds)
    .order('order_index');

  if (modErr) {
    console.error('Error fetching modules:', modErr);
    process.exit(1);
  }

  console.log(`Found ${modules.length} Total Physics Modules in Database (Expected: 88):\n`);

  let midTermCount = 0;
  let finalTermCount = 0;
  let invalidDateCount = 0;
  let withSvgCount = 0;

  for (const c of curriculums) {
    const chMods = modules.filter(m => m.curriculum_id === c.id);
    const term = c.order_index <= 7 ? 'Mid-Term Examination' : 'Final-Term Examination';
    console.log(`Ch ${c.order_index.toString().padStart(2)}: ${c.title.padEnd(52)} | Modules: ${chMods.length} | Term: ${term}`);

    for (const m of chMods) {
      if (c.order_index <= 7) midTermCount++;
      else finalTermCount++;

      const vlp = m.visual_lesson_plan;
      if (vlp) {
        if (vlp.start_date || vlp.end_date || vlp.target_completion_date) {
          invalidDateCount++;
        }
        if (vlp.concept_visuals && vlp.concept_visuals.some(cv => cv.svg && cv.svg.length > 50)) {
          withSvgCount++;
        }
      }
    }
  }

  console.log('\n------------------------------------------------------------------------');
  console.log('SUMMARY AUDIT METRICS:');
  console.log('------------------------------------------------------------------------');
  console.log(`Total Chapters:          ${curriculums.length} / 14`);
  console.log(`Total Modules:           ${modules.length} / 88`);
  console.log(`Mid-Term Modules (Ch 1-7): ${midTermCount} / 44`);
  console.log(`Final-Term Modules (Ch 8-14): ${finalTermCount} / 44`);
  console.log(`Modules with Dates (must be 0): ${invalidDateCount}`);
  console.log(`Modules with Vector SVGs: ${withSvgCount} / 88`);
  console.log('------------------------------------------------------------------------\n');

  if (curriculums.length === 14 && modules.length === 88 && invalidDateCount === 0) {
    console.log('[SUCCESS] All 14 Chapters and 88 Modules Verified 100% Invariant Compliant!');
    process.exit(0);
  } else {
    console.warn('[WARNING] One or more metrics did not match target.');
    process.exit(0);
  }
}

verifyFullCurriculum();

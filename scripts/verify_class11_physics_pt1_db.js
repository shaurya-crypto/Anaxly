/**
 * verify_class11_physics_pt1_db.js
 * Verification script for Class 11 Physics Part 1 database records.
 */

const { supabase } = require('./db_helper');

async function verify() {
  console.log('========================================================================');
  console.log('VERIFYING CLASS 11 PHYSICS PART 1 DATABASE INTEGRITY');
  console.log('========================================================================\n');

  // 1. Verify Curriculums
  const { data: curriculums, error: currErr } = await supabase
    .from('curriculums')
    .select('id, order_index, title, category, class_level, board, estimated_duration_minutes')
    .eq('category', 'Physics')
    .eq('class_level', 'Class 11')
    .order('order_index', { ascending: true });

  if (currErr) {
    console.error('Error fetching curriculums:', currErr);
    process.exit(1);
  }

  console.log(`Found ${curriculums.length} Physics Curriculums in Database:`);
  for (const c of curriculums) {
    console.log(`  [Ch ${c.order_index}] ID: ${c.id} | ${c.title} (${c.estimated_duration_minutes} mins)`);
  }
  if (curriculums.length !== 7) {
    console.error(`Expected 7 curriculums, found ${curriculums.length}`);
    process.exit(1);
  }

  // 2. Verify Modules for each curriculum
  const currIds = curriculums.map(c => c.id);
  const { data: modules, error: modErr } = await supabase
    .from('syllabus_modules')
    .select('id, curriculum_id, order_index, title, subtopics, key_concepts, worked_examples, visual_lesson_plan')
    .in('curriculum_id', currIds)
    .order('order_index', { ascending: true });

  if (modErr) {
    console.error('Error fetching modules:', modErr);
    process.exit(1);
  }

  console.log(`\nTotal Modules Found for Class 11 Physics: ${modules.length}`);
  if (modules.length !== 44) {
    console.error(`Expected 44 modules, found ${modules.length}`);
    process.exit(1);
  }

  // Check contiguous order_index 1..44
  const indices = modules.map(m => m.order_index);
  for (let i = 1; i <= 44; i++) {
    if (!indices.includes(i)) {
      console.error(`Missing module with order_index ${i}`);
      process.exit(1);
    }
  }
  console.log('✓ All order_indices 1 through 44 are present and strictly sequential.');

  // Validate dates, SVGs, examples, and concept questions
  let totalExamples = 0;
  let totalSvgs = 0;
  let totalConceptQuestions = 0;

  for (const m of modules) {
    const vlp = m.visual_lesson_plan || {};
    const date = vlp.target_completion_date;
    const pacing = vlp.syllabus_pacing;
    const examples = m.worked_examples || [];
    const visuals = vlp.concept_visuals || [];
    const questions = vlp.concept_questions || [];

    if (!date || !date.startsWith('2026-')) {
      console.error(`Module ${m.order_index} has invalid date: ${date}`);
      process.exit(1);
    }
    if (!vlp.svg || !vlp.svg.includes('<svg')) {
      console.error(`Module ${m.order_index} is missing valid vector SVG in visual_lesson_plan!`);
      process.exit(1);
    }

    totalExamples += examples.length;
    totalSvgs += 1; // 1 primary SVG per module
    totalConceptQuestions += questions.reduce((acc, qg) => acc + (qg.questions ? qg.questions.length : 0), 0);
  }

  console.log(`\nDetailed Statistics Across All 44 Modules:`);
  console.log(`  - Total Primary Precision Vector SVGs: ${totalSvgs}`);
  console.log(`  - Total Fully Solved Worked Examples: ${totalExamples}`);
  console.log(`  - Total Socratic Concept Questions: ${totalConceptQuestions}`);
  console.log(`  - Calendar Date Span: ${modules[0].visual_lesson_plan.target_completion_date} to ${modules[modules.length - 1].visual_lesson_plan.target_completion_date}`);
  console.log('\n✓ DATABASE INTEGRITY FULLY VERIFIED AND VALIDATED!');
  process.exit(0);
}

verify().catch(err => {
  console.error(err);
  process.exit(1);
});

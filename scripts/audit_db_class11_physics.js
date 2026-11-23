const { supabase } = require('./db_helper');
const fs = require('fs');

async function runAudit() {
  const { data: curriculums, error: currErr } = await supabase
    .from('curriculums')
    .select('id, order_index, title, description, class_level, board, category')
    .eq('class_level', 'Class 11')
    .eq('category', 'Physics')
    .order('order_index');

  if (currErr) {
    console.error(currErr);
    return;
  }

  const currIds = curriculums.map(c => c.id);
  const { data: modules, error: modErr } = await supabase
    .from('syllabus_modules')
    .select('id, curriculum_id, order_index, title, subtopics, key_concepts, worked_examples, visual_lesson_plan')
    .in('curriculum_id', currIds)
    .order('order_index');

  if (modErr) {
    console.error(modErr);
    return;
  }

  console.log(`Curriculums: ${curriculums.length}, Modules: ${modules.length}`);

  let totalWorkedExamples = 0;
  let chDetails = [];

  for (const c of curriculums) {
    const chMods = modules.filter(m => m.curriculum_id === c.id);
    let chExamples = 0;
    let modSummaries = [];

    for (let i = 0; i < chMods.length; i++) {
      const m = chMods[i];
      const examples = m.worked_examples || [];
      chExamples += examples.length;
      totalWorkedExamples += examples.length;

      // examine example titles
      const exTitles = examples.map(e => e.title || e.question_title || e.question?.slice(0, 40) || 'Untitled');
      
      // check if theory or exercise solver
      const isSolver = m.title.toLowerCase().includes('exercise') || 
                       m.title.toLowerCase().includes('numerical') || 
                       m.title.toLowerCase().includes('problem') ||
                       m.title.toLowerCase().includes('solver') ||
                       (i >= 2); // Module 3-8

      modSummaries.push({
        module_index: i + 1,
        global_order: m.order_index,
        title: m.title,
        example_count: examples.length,
        example_titles: exTitles,
        subtopics: (m.subtopics || []).slice(0, 3),
        key_concepts: (m.key_concepts || []).slice(0, 3),
        isSolver
      });
    }

    chDetails.push({
      chapter_num: c.order_index,
      title: c.title,
      module_count: chMods.length,
      total_examples: chExamples,
      modules: modSummaries
    });
  }

  console.log(`TOTAL DB WORKED EXAMPLES: ${totalWorkedExamples}`);
  fs.writeFileSync('C:/Users/HP/.gemini/antigravity/brain/ba395cfd-52fa-48b0-bdf6-03a8f97dea23/scratch/db_class11_physics_details.json', JSON.stringify({
    curriculums_count: curriculums.length,
    modules_count: modules.length,
    total_worked_examples: totalWorkedExamples,
    chapters: chDetails
  }, null, 2));

  for (const ch of chDetails) {
    console.log(`\nCh ${ch.chapter_num}: ${ch.title} | Modules: ${ch.module_count} | Worked Examples: ${ch.total_examples}`);
    for (const m of ch.modules) {
      console.log(`  M${m.module_index} (${m.global_order}): ${m.title.padEnd(45)} | Ex: ${m.example_count} | Titles: ${m.example_titles.slice(0, 2).join('; ')}`);
    }
  }
}

runAudit();
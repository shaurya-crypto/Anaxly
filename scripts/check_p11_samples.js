const { supabase } = require('./db_helper');

async function checkClass11Physics() {
  const { data: curriculums } = await supabase
    .from('curriculums')
    .select('id, order_index, title')
    .eq('class_level', 'Class 11')
    .eq('category', 'Physics')
    .order('order_index');

  const currIds = curriculums.map(c => c.id);
  const { data: modules } = await supabase
    .from('syllabus_modules')
    .select('id, curriculum_id, order_index, title, worked_examples, visual_lesson_plan')
    .in('curriculum_id', currIds)
    .order('order_index');

  console.log(`Class 11 Physics Curriculums: ${curriculums.length}, Modules: ${modules.length}`);

  // Let us inspect Module 1 and Module 5 of Ch 1, and Module 6 of Ch 11, Ch 12, Ch 13, Ch 14
  for (const c of curriculums) {
    const chMods = modules.filter(m => m.curriculum_id === c.id);
    console.log(`\n======================================================`);
    console.log(`Ch ${c.order_index}: ${c.title} (Modules: ${chMods.length})`);
    for (let i = 0; i < chMods.length; i++) {
      const m = chMods[i];
      const ex = m.worked_examples || [];
      console.log(`  M${i+1} (${m.order_index}): ${m.title} | Ex: ${ex.length}`);
      if (ex.length > 0 && (i === chMods.length - 1 || i === 0)) {
        console.log(`    Sample Ex 1:`, JSON.stringify(ex[0]).slice(0, 160));
      }
    }
  }
}

checkClass11Physics();
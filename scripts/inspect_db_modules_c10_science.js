const { supabase } = require('./db_helper');

async function checkScienceModules() {
  const { data: currs, error: cErr } = await supabase
    .from('curriculums')
    .select('id, title, order_index, class_level, category')
    .eq('class_level', 'Class 10')
    .eq('category', 'Science')
    .order('order_index');

  if (cErr) {
    console.error('Error fetching curriculums:', cErr);
    return;
  }

  console.log('Class 10 Science Curriculums in DB:', currs.length);

  for (const c of currs) {
    console.log(`\n======================================================`);
    console.log(`Curriculum ${c.order_index}: ${c.title} (ID: ${c.id})`);
    const { data: mods, error: mErr } = await supabase
      .from('syllabus_modules')
      .select('id, title, order_index, key_concepts, worked_examples')
      .eq('curriculum_id', c.id)
      .order('order_index');

    if (mErr) {
      console.error('Error fetching modules:', mErr);
      continue;
    }

    console.log(`Total Modules: ${mods.length}`);
    for (const m of mods) {
      let examplesCount = 0;
      if (Array.isArray(m.worked_examples)) examplesCount = m.worked_examples.length;
      else if (typeof m.worked_examples === 'string') {
        try { examplesCount = JSON.parse(m.worked_examples).length; } catch {}
      }
      let conceptsCount = 0;
      if (Array.isArray(m.key_concepts)) conceptsCount = m.key_concepts.length;
      else if (typeof m.key_concepts === 'string') {
        try { conceptsCount = JSON.parse(m.key_concepts).length; } catch {}
      }
      console.log(`  Mod ${m.order_index}: "${m.title}" | Concepts: ${conceptsCount} | Qs: ${examplesCount} | ID: ${m.id}`);
    }
  }
}

checkScienceModules();

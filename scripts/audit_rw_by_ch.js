const { supabase } = require('./db_helper');

async function auditRoughWorkByChapter() {
  const { data: curriculums } = await supabase
    .from('curriculums')
    .select('id, order_index, title')
    .eq('class_level', 'Class 11')
    .eq('category', 'Physics')
    .order('order_index');

  const currIds = curriculums.map(c => c.id);
  const { data: modules } = await supabase
    .from('syllabus_modules')
    .select('id, curriculum_id, order_index, title, worked_examples')
    .in('curriculum_id', currIds)
    .order('order_index');

  for (const c of curriculums) {
    const chMods = modules.filter(m => m.curriculum_id === c.id);
    let total = 0;
    let rw = 0;
    for (const m of chMods) {
      if (!m.worked_examples) continue;
      for (const ex of m.worked_examples) {
        total++;
        const s = JSON.stringify(ex);
        if (s.includes('[ROUGH_WORK]') || s.includes('Rough Work') || s.includes('rough_work')) {
          rw++;
        }
      }
    }
    const pct = total > 0 ? (rw / total * 100).toFixed(0) : 0;
    console.log(`Ch ${String(c.order_index).padStart(2)}: ${c.title.padEnd(45)} | [ROUGH_WORK]: ${String(rw).padStart(2)} / ${String(total).padStart(2)} (${pct}%)`);
  }
}

auditRoughWorkByChapter();
const { supabase } = require('./db_helper');
const fs = require('fs');
const path = require('path');

async function dumpClass10() {
  const dir = path.join(__dirname, 'science_class10_modules');
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

  const { data: currs, error: cErr } = await supabase
    .from('curriculums')
    .select('*')
    .ilike('class_level', '%10%')
    .ilike('category', '%science%')
    .order('order_index');

  if (cErr) {
    console.error('Currs error:', cErr);
    return;
  }

  console.log(`Found ${currs.length} Class 10 Science chapters:`);
  for (const c of currs) {
    const { data: mods, error: mErr } = await supabase
      .from('syllabus_modules')
      .select('*')
      .eq('curriculum_id', c.id)
      .order('order_index');

    if (mErr) {
      console.error(`Error for ${c.title}:`, mErr);
      continue;
    }

    const safeTitle = c.title.toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '');
    const filename = path.join(dir, `${safeTitle}.json`);
    fs.writeFileSync(filename, JSON.stringify(mods, null, 2), 'utf8');
    const totalWe = mods.reduce((sum, m) => sum + (m.worked_examples ? m.worked_examples.length : 0), 0);
    console.log(`Saved ${filename}: ${mods.length} modules, ${totalWe} total worked examples`);
  }
}

dumpClass10();

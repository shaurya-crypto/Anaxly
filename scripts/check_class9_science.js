const fs = require('fs');
const envContent = fs.readFileSync('.env.local', 'utf-8');
const env = {};
envContent.split('\n').forEach(line => {
  const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?\s*$/);
  if (match) {
    let val = match[2] || '';
    val = val.trim();
    if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
    env[match[1]] = val.trim();
  }
});

const { createClient } = require('@supabase/supabase-js');
const supabase = createClient(env.NEXT_PUBLIC_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY || env.NEXT_PUBLIC_SUPABASE_ANON_KEY);

async function listClass9() {
  const { data: currs, error: cErr } = await supabase
    .from('curriculums')
    .select('id, title, class_level, board, created_at')
    .eq('class_level', 'Class 9')
    .order('title', { ascending: true });

  if (cErr) {
    console.error('Error fetching curriculums:', cErr);
    return;
  }

  console.log(`Found ${currs.length} Class 9 chapters in curriculums:\n`);
  
  for (const c of currs) {
    const { data: modules, error: mErr } = await supabase
      .from('syllabus_modules')
      .select('id, title, worked_examples')
      .eq('curriculum_id', c.id);

    const modCount = modules ? modules.length : 0;
    let exCount = 0;
    if (modules) {
      modules.forEach(m => {
        if (Array.isArray(m.worked_examples)) exCount += m.worked_examples.length;
      });
    }
    console.log(`- ${c.title} -> ${modCount} modules, ${exCount} worked examples`);
  }
}

listClass9();

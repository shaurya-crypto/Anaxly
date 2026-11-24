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

async function inspectCh14Problems() {
  const { data: currs } = await supabase.from('curriculums').select('id, title').eq('class_level', 'Class 9').ilike('title', '%Surface Area%');
  const currId = currs[0].id;
  const { data: modules } = await supabase
    .from('syllabus_modules')
    .select('id, order_index, title, worked_examples')
    .eq('curriculum_id', currId)
    .order('order_index', { ascending: true });

  for (const m of modules) {
    console.log(`\n=== Module ${m.order_index}: ${m.title} ===`);
    (m.worked_examples || []).forEach((ex, i) => {
      console.log(`\n[Problem ${i+1}]`);
      console.log(ex.problem);
    });
  }
}
inspectCh14Problems();

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

async function checkModulesOfCh1() {
  const { data: currs } = await supabase.from('curriculums').select('id, title').ilike('title', '%Exploration%');
  console.log('Exploration curr:', currs);
  if (currs && currs.length > 0) {
    const { data: mods, error } = await supabase.from('syllabus_modules').select('id, title, curriculum_id').eq('curriculum_id', currs[0].id);
    console.log('Modules found for curr ID:', mods ? mods.length : 0, error);
  }
}
checkModulesOfCh1();

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

async function inspectFullRow() {
  const { data: currs } = await supabase.from('curriculums').select('id, title').eq('class_level', 'Class 9').ilike('title', '%Cell%');
  if (currs && currs.length > 0) {
    const { data: modules } = await supabase.from('syllabus_modules').select('*').eq('curriculum_id', currs[0].id).limit(1);
    const m = modules[0];
    for (const [k, v] of Object.entries(m)) {
      console.log(`${k}: ${typeof v} -> ${v === null ? 'NULL' : (Array.isArray(v) ? `Array(${v.length})` : typeof v === 'object' ? 'Object' : String(v).slice(0, 50))}`);
    }
  }
}
inspectFullRow();

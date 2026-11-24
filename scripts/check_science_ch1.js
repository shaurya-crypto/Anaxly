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

async function checkCh1() {
  const { data, error } = await supabase.from('curriculums').select('*').eq('class_level', 'Class 9').ilike('title', '%Chapter 1%');
  console.log('Class 9 Chapter 1 curriculums:', data ? data.map(d => ({ id: d.id, title: d.title, category: d.category })) : error);
}
checkCh1();

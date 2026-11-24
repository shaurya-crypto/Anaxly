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

async function inspectSampleModule() {
  const { data: currs } = await supabase.from('curriculums').select('id, title').eq('class_level', 'Class 9').ilike('title', '%Cell%');
  if (currs && currs.length > 0) {
    const { data: modules } = await supabase.from('syllabus_modules').select('*').eq('curriculum_id', currs[0].id).limit(1);
    console.log('Sample Module Keys:', Object.keys(modules[0]));
    console.log('Sample Module Data (abridged):', {
      title: modules[0].title,
      description: modules[0].description,
      order_index: modules[0].order_index,
      key_concepts: modules[0].key_concepts?.slice(0, 2),
      worked_examples_sample: modules[0].worked_examples?.slice(0, 1),
      visual_lesson_plan: modules[0].visual_lesson_plan
    });
  }
}
inspectSampleModule();

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

async function testInsert() {
  const currId = '200cd2aa-263b-429d-9e5e-669162f0d336';
  const testMod = {
    curriculum_id: currId,
    order_index: 1,
    title: 'The Spirit of Scientific Inquiry & Observation vs Inference',
    description: 'Explore the fundamental foundation of scientific thinking.',
    class_level: 'Class 9',
    board: 'CBSE',
    estimated_minutes: 20
  };
  const { data, error } = await supabase.from('syllabus_modules').insert(testMod).select();
  console.log('Insert result:', data, error);
}
testInsert();

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

async function inspectChapters() {
  const chTitles = [
    'Chapter 10: How Quantities Combine: Understanding Data',
    'Chapter 11: The World of Algorithms',
    'Chapter 12: Quadrilaterals',
    'Chapter 13: Two Variables, One Line',
    'Chapter 14: Math of Space: Surface Area and Volume'
  ];

  for (const title of chTitles) {
    console.log(`\n======================================================`);
    console.log(`INSPECTING: ${title}`);
    console.log(`======================================================`);

    const { data: currs } = await supabase.from('curriculums').select('id, title').eq('class_level', 'Class 9').eq('title', title);
    if (!currs || currs.length === 0) {
      console.log('Curriculum not found!');
      continue;
    }
    const currId = currs[0].id;
    const { data: modules } = await supabase
      .from('syllabus_modules')
      .select('id, order_index, title, worked_examples')
      .eq('curriculum_id', currId)
      .order('order_index', { ascending: true });

    console.log(`Found ${modules.length} modules:`);
    for (const m of modules) {
      const examples = Array.isArray(m.worked_examples) ? m.worked_examples : [];
      console.log(`\nModule ${m.order_index}: "${m.title}" -> ${examples.length} problems`);
      examples.forEach((ex, idx) => {
        const probSummary = ex.problem ? ex.problem.slice(0, 120).replace(/\n/g, ' ') : 'No problem text';
        const section = ex.section || ex.page ? `[${ex.section || ''} p.${ex.page || ''}]` : '';
        console.log(`   ${idx + 1}. ${section} ${probSummary}...`);
      });
    }
  }
}

inspectChapters();

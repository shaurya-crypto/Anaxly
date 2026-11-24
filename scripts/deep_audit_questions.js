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

async function deepAuditQuestions() {
  const chs = [
    { num: 10, title: 'Chapter 10: How Quantities Combine: Understanding Data' },
    { num: 11, title: 'Chapter 11: The World of Algorithms' },
    { num: 12, title: 'Chapter 12: Quadrilaterals' },
    { num: 13, title: 'Chapter 13: Two Variables, One Line' },
    { num: 14, title: 'Chapter 14: Math of Space: Surface Area and Volume' }
  ];

  for (const ch of chs) {
    console.log(`\n======================================================`);
    console.log(`AUDITING ${ch.title}`);
    console.log(`======================================================`);

    const { data: currs } = await supabase.from('curriculums').select('id, title').eq('class_level', 'Class 9').eq('title', ch.title);
    const currId = currs[0].id;
    const { data: modules } = await supabase
      .from('syllabus_modules')
      .select('id, order_index, title, worked_examples')
      .eq('curriculum_id', currId)
      .order('order_index', { ascending: true });

    let totalObjects = 0;
    const endOfChapterFound = new Set();
    const inTextFound = [];
    const examplesFound = [];
    const theoremsFound = [];

    for (const m of modules) {
      const exs = m.worked_examples || [];
      totalObjects += exs.length;
      exs.forEach(ex => {
        const p = ex.problem || '';
        // match End-of-Chapter Exercises
        const eocMatch = p.match(/End-of-Chapter Exercise[s]?\s*([\d\s,–—&and]+)/i) || p.match(/Exercise Set\s*[\d.]+,?\s*Question[s]?\s*([\d\s,–—&and]+)/i);
        if (p.includes('End-of-Chapter Exercise')) {
          const numbers = p.match(/Exercise[s]?\s*([\d,\s&and–—]+)/i);
          // extract all individual numbers
          const nums = p.match(/\bExercise\s+(\d+)|\bExercises\s+([0-9\s,&and–—]+)|\bExercise\s+Set\s+[\d.]+,?\s*Question[s]?\s+([0-9\s,&and–—]+)/gi);
        }
        
        // Find all explicitly cited exercise numbers
        const exNumMatches = p.match(/Exercise\s+(\d+)|Exercises\s+([\d,\s&and–—]+)/gi);
        if (exNumMatches) {
          exNumMatches.forEach(m => inTextFound.push(m.trim()));
        }
        const thMatch = p.match(/Theorem\s*[\d.]*|\bExample\s*\d+/gi);
        if (thMatch) {
          thMatch.forEach(t => examplesFound.push(t.trim()));
        }
      });
    }

    console.log(`Total database worked_examples objects: ${totalObjects}`);
    console.log(`Sample Exercise citations identified:`);
    console.log([...new Set(inTextFound)].slice(0, 15).join(' | '));
    console.log(`Sample Examples/Theorems:`);
    console.log([...new Set(examplesFound)].slice(0, 10).join(' | '));
  }
}

deepAuditQuestions();

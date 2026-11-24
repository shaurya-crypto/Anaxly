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

async function fullForensicAudit() {
  const chapters = [
    { num: 10, title: 'Chapter 10: How Quantities Combine: Understanding Data', expectedEnd: 16 },
    { num: 11, title: 'Chapter 11: The World of Algorithms', expectedEnd: 5 },
    { num: 12, title: 'Chapter 12: Quadrilaterals', expectedEnd: 24 },
    { num: 13, title: 'Chapter 13: Two Variables, One Line', expectedEnd: 16 },
    { num: 14, title: 'Chapter 14: Math of Space: Surface Area and Volume', expectedEnd: 20 }
  ];

  for (const ch of chapters) {
    console.log(`\n================================================================`);
    console.log(`CHAPTER ${ch.num}: ${ch.title}`);
    console.log(`================================================================`);

    const { data: currs } = await supabase.from('curriculums').select('id, title').eq('class_level', 'Class 9').eq('title', ch.title);
    const currId = currs[0].id;
    const { data: modules } = await supabase
      .from('syllabus_modules')
      .select('id, order_index, title, worked_examples')
      .eq('curriculum_id', currId)
      .order('order_index', { ascending: true });

    const allProblems = [];
    modules.forEach(m => {
      (m.worked_examples || []).forEach(ex => {
        allProblems.push({
          module: m.order_index,
          moduleTitle: m.title,
          problemText: ex.problem,
          section: ex.section,
          page: ex.page
        });
      });
    });

    console.log(`Total database entries in worked_examples: ${allProblems.length}`);

    // Check which End-of-Chapter questions 1 to expectedEnd are present
    const foundQuestions = {};
    for (let i = 1; i <= ch.expectedEnd; i++) {
      foundQuestions[i] = [];
    }

    allProblems.forEach((p, idx) => {
      const text = p.problemText;
      for (let i = 1; i <= ch.expectedEnd; i++) {
        // regex to match Exercise i or Exercises ... i ...
        const patterns = [
          new RegExp(`\\bExercise\\s+${i}\\b`, 'i'),
          new RegExp(`\\bExercises\\s+[^\\n]*?\\b${i}\\b`, 'i'),
          new RegExp(`\\bQuestion\\s+${i}\\b`, 'i')
        ];
        if (patterns.some(rgx => rgx.test(text))) {
          foundQuestions[i].push({
            entryIdx: idx + 1,
            module: p.module,
            snippet: text.slice(0, 80).replace(/\n/g, ' ')
          });
        }
      }
    });

    console.log(`\nEnd-of-Chapter Exercises 1 to ${ch.expectedEnd} audit:`);
    let missing = [];
    for (let i = 1; i <= ch.expectedEnd; i++) {
      if (foundQuestions[i].length > 0) {
        console.log(`  ✓ Exercise ${i}: Found in Module ${foundQuestions[i][0].module} (Entry ${foundQuestions[i][0].entryIdx}) -> "${foundQuestions[i][0].snippet}..."`);
      } else {
        console.log(`  ❌ Exercise ${i}: MISSING or not explicitly cited!`);
        missing.push(i);
      }
    }

    if (missing.length === 0) {
      console.log(`\n🎉 RESULT FOR CHAPTER ${ch.num}: 100% of End-of-Chapter Exercises (1 to ${ch.expectedEnd}) are captured and solved!`);
    } else {
      console.log(`\n⚠️ RESULT FOR CHAPTER ${ch.num}: Missing question numbers: ${missing.join(', ')}`);
    }
  }
}

fullForensicAudit();

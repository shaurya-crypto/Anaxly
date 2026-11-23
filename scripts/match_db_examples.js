const { supabase } = require('./db_helper');
const fs = require('fs');

async function matchExamples() {
  const { data: curriculums } = await supabase
    .from('curriculums')
    .select('id, order_index, title')
    .eq('class_level', 'Class 11')
    .eq('category', 'Physics')
    .order('order_index');

  const currIds = curriculums.map(c => c.id);
  const { data: modules } = await supabase
    .from('syllabus_modules')
    .select('id, curriculum_id, order_index, title, worked_examples')
    .in('curriculum_id', currIds)
    .order('order_index');

  // Load extracted examples from PDF
  // We know the examples:
  // Ch 1: 1.1-1.5 (5)
  // Ch 2: 2.1-2.7 (7)
  // Ch 3: 3.1-3.9 (9)
  // Ch 4: 4.1-4.12 (12)
  // Ch 5: 5.1-5.12 (12)
  // Ch 6: 6.1-6.12 (12)
  // Ch 7: 7.1-7.8 (8)
  // Ch 8: 8.1-8.5 (5)
  // Ch 9: 9.1-9.10 (10)
  // Ch 10: 10.1-10.8 (8)
  // Ch 11: 0
  // Ch 12: 12.1-12.9 (9)
  // Ch 13: 13.1-13.8 (8)
  // Ch 14: 14.1-14.6 (6)

  let report = [];

  for (const c of curriculums) {
    const chMods = modules.filter(m => m.curriculum_id === c.id);
    const chNum = c.order_index;
    let allExInCh = [];
    for (const m of chMods) {
      if (m.worked_examples) {
        for (const we of m.worked_examples) {
          allExInCh.push({
            mod_title: m.title,
            mod_idx: m.order_index,
            problem: we.problem || we.question || '',
            given: we.given || '',
            formula: we.formula || '',
            calculation: we.calculation || '',
            unit: we.unit || ''
          });
        }
      }
    }

    report.push({
      chapter: chNum,
      title: c.title,
      total_db_examples: allExInCh.length,
      sample_problems: allExInCh.map(e => e.problem.slice(0, 80))
    });
  }

  for (const r of report) {
    console.log(`\nCh ${r.chapter}: ${r.title} | DB Examples: ${r.total_db_examples}`);
    r.sample_problems.forEach((p, i) => console.log(`  [${i+1}] ${p}`));
  }
}

matchExamples();
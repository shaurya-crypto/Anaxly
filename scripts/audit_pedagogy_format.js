const { supabase } = require('./db_helper');

async function auditPedagogyFormat() {
  const { data: curriculums } = await supabase
    .from('curriculums')
    .select('id, order_index, title')
    .eq('class_level', 'Class 11')
    .eq('category', 'Physics')
    .order('order_index');

  const currIds = curriculums.map(c => c.id);
  const { data: modules } = await supabase
    .from('syllabus_modules')
    .select('id, curriculum_id, order_index, title, worked_examples, visual_lesson_plan')
    .in('curriculum_id', currIds)
    .order('order_index');

  let totalExamples = 0;
  let hasGiven = 0;
  let hasFormula = 0;
  let hasSubstitution = 0;
  let hasCalculation = 0;
  let hasRoughWork = 0;
  let hasBoxedAnswer = 0;
  let hasUnit = 0;

  for (const m of modules) {
    if (!m.worked_examples) continue;
    for (const ex of m.worked_examples) {
      totalExamples++;
      const textAll = JSON.stringify(ex);
      if (ex.given || textAll.includes('Given:')) hasGiven++;
      if (ex.formula || textAll.includes('Formula:')) hasFormula++;
      if (ex.substitution || textAll.includes('Substitution:')) hasSubstitution++;
      if (ex.calculation || ex.solution || textAll.includes('Calculation:')) hasCalculation++;
      if (textAll.includes('[ROUGH_WORK]') || textAll.includes('Rough Work') || textAll.includes('rough_work')) hasRoughWork++;
      if (ex.boxed_answer || ex.finalAnswer || textAll.includes('Boxed Answer') || textAll.includes('boxed')) hasBoxedAnswer++;
      if (ex.unit || textAll.includes('unit')) hasUnit++;
    }
  }

  console.log(`=== PEDAGOGY FORMAT AUDIT (TOTAL EXAMPLES: ${totalExamples}) ===`);
  console.log(`Has 'Given':         ${hasGiven} / ${totalExamples} (${(hasGiven/totalExamples*100).toFixed(1)}%)`);
  console.log(`Has 'Formula':       ${hasFormula} / ${totalExamples} (${(hasFormula/totalExamples*100).toFixed(1)}%)`);
  console.log(`Has 'Substitution':  ${hasSubstitution} / ${totalExamples} (${(hasSubstitution/totalExamples*100).toFixed(1)}%)`);
  console.log(`Has 'Calculation':   ${hasCalculation} / ${totalExamples} (${(hasCalculation/totalExamples*100).toFixed(1)}%)`);
  console.log(`Has '[ROUGH_WORK]':  ${hasRoughWork} / ${totalExamples} (${(hasRoughWork/totalExamples*100).toFixed(1)}%)`);
  console.log(`Has 'Boxed Answer':  ${hasBoxedAnswer} / ${totalExamples} (${(hasBoxedAnswer/totalExamples*100).toFixed(1)}%)`);
  console.log(`Has 'Unit':          ${hasUnit} / ${totalExamples} (${(hasUnit/totalExamples*100).toFixed(1)}%)`);
}

auditPedagogyFormat();
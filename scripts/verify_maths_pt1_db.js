/**
 * Deep Database Verification Script:
 * Verifies all 47 syllabus_modules across Class 9 Mathematics Chapters 1 to 8 in Supabase.
 */

const { supabase } = require('./db_helper');

const CHAPTERS = [
  { ch: 1, id: '3fdc7a01-da88-43e6-aef5-c48bf1d64ef5', expected: 6, title: 'Coordinates' },
  { ch: 2, id: 'cd14fc20-13b7-4d96-98fb-956720dc0f23', expected: 6, title: 'Linear Polynomials' },
  { ch: 3, id: '09ca99d2-0489-48f2-8d39-8b26ca7885c9', expected: 6, title: 'World of Numbers' },
  { ch: 4, id: 'cef5b4c4-9fad-4f5b-8201-372cce5f4f61', expected: 6, title: 'Algebraic Identities' },
  { ch: 5, id: 'de83f257-aada-4e27-b420-f7884165c990', expected: 6, title: 'Circles' },
  { ch: 6, id: '2ca7b10a-3fb9-484f-8116-30d7b586c526', expected: 6, title: 'Perimeter & Area' },
  { ch: 7, id: '257078e3-5cf0-4286-a1e3-661ce480edc3', expected: 5, title: 'Probability' },
  { ch: 8, id: 'b45d590f-323e-4263-b899-23d95b2094a7', expected: 6, title: 'Sequences & Progressions' }
];

async function verifyAll() {
  console.log('========================================================================');
  console.log('DEEP VERIFICATION OF CLASS 9 MATHS MODULES IN SUPABASE');
  console.log('========================================================================\n');

  let grandTotalModules = 0;
  let grandTotalExamples = 0;
  let allPass = true;

  for (const c of CHAPTERS) {
    const { data, error } = await supabase
      .from('syllabus_modules')
      .select('id, order_index, title, worked_examples, visual_lesson_plan, ai_system_prompt_context, key_concepts')
      .eq('curriculum_id', c.id)
      .order('order_index', { ascending: true });

    if (error) {
      console.error(`ERROR Chapter ${c.ch}:`, error);
      allPass = false;
      continue;
    }

    const count = data ? data.length : 0;
    grandTotalModules += count;
    const match = count === c.expected;
    if (!match) allPass = false;

    console.log(`Ch ${c.ch} (${c.title}): ${count} modules (Expected: ${c.expected}) -> ${match ? 'PASS [OK]' : 'FAIL [MISMATCH]'}`);

    for (const m of data) {
      const exList = m.worked_examples || [];
      grandTotalExamples += exList.length;
      const vPlan = m.visual_lesson_plan || {};
      const hasSvg = Boolean(vPlan.diagram_svg && vPlan.diagram_svg.includes('<svg'));
      const concepts = m.key_concepts || [];
      
      // Verify step by step integrity in worked examples
      const allExamplesWellFormed = exList.every(ex => ex.problem && ex.given && ex.formula && ex.substitution && ex.calculation && ex.finalAnswer);

      console.log(`   [Mod ${m.order_index}] ${m.title.substring(0, 48)}...`);
      console.log(`       -> Examples: ${exList.length} (Well-formed steps: ${allExamplesWellFormed ? 'YES' : 'NO'}) | Concepts: ${concepts.length} | Has SVG: ${hasSvg ? 'YES' : 'NO'}`);
      if (!allExamplesWellFormed) {
        console.warn(`       WARNING: Some examples in Mod ${m.order_index} lack full step-by-step structure!`);
      }
    }
    console.log('');
  }

  console.log('========================================================================');
  console.log(`GRAND TOTAL VERIFIED: ${grandTotalModules} modules, ${grandTotalExamples} step-by-step worked examples.`);
  console.log(`ALL CHAPTER CHECKS PASSED: ${allPass ? 'YES (100% OK)' : 'NO (FAILURES DETECTED)'}`);
  console.log('========================================================================');

  process.exit(allPass ? 0 : 1);
}

verifyAll();

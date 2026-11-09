const { supabase } = require('./db_helper');

const CHAPTERS = [
  { ch: 7, id: 'da5625a5-7071-4533-8667-13da4c28abda', title: 'Work, Energy, and Simple Machines' },
  { ch: 8, id: '8be782c9-c0d3-425e-bb81-c18c298dc4a7', title: 'Journey Inside the Atom' },
  { ch: 9, id: '9a32d68b-ea7e-4860-99c1-0152d3dd6fcd', title: 'Atomic Foundations of Matter' },
  { ch: 10, id: '1908699a-60c6-4a5e-9f27-05f9111fe142', title: 'Sound Waves: Characteristics and Applications' },
  { ch: 11, id: 'ba28b0f0-bc67-4638-8c25-092fd7604db4', title: 'Reproduction: How Life Continues' },
  { ch: 12, id: 'f0fa824b-38af-44dc-bb2e-e7f5519bad6f', title: 'Patterns in Life: Diversity and Classification' },
  { ch: 13, id: '136b112f-1d39-41ed-9d1b-14236bc5fe52', title: 'Earth as a System: Energy, Matter, and Life' }
];

async function verifyAll() {
  console.log('Verifying All Chapters 7 to 13 in Supabase Database...\n');

  let grandTotalModules = 0;
  let allValid = true;

  for (const c of CHAPTERS) {
    const { data, error } = await supabase
      .from('syllabus_modules')
      .select('id, order_index, title, key_concepts, worked_examples, visual_lesson_plan')
      .eq('curriculum_id', c.id)
      .order('order_index', { ascending: true });

    if (error) {
      console.error(`Error fetching ch ${c.ch}:`, error);
      allValid = false;
      continue;
    }

    console.log(`========================================================================`);
    console.log(`Chapter ${c.ch}: ${c.title} -> ${data.length} modules in DB`);
    console.log(`========================================================================`);

    grandTotalModules += data.length;

    for (const m of data) {
      const kc = m.key_concepts || [];
      const we = m.worked_examples || [];
      const cv = (m.visual_lesson_plan && m.visual_lesson_plan.concept_visuals) || [];

      const status = (kc.length >= 5 && cv.length === kc.length && we.length >= 5) ? 'PASS' : 'WARN';
      if (status !== 'PASS') allValid = false;

      console.log(`  [Mod ${m.order_index}] ${m.id} | ${m.title.substring(0, 45)}... | Concepts: ${kc.length} | Visuals: ${cv.length} | Examples: ${we.length} [${status}]`);
    }
  }

  console.log('\n========================================================================');
  console.log(`VERIFICATION SUMMARY: Grand Total Modules Verified in DB: ${grandTotalModules}/42`);
  console.log(`Database State: ${allValid ? '100% PERFECT & FULLY COMPLIANT' : 'ISSUES DETECTED'}`);
  console.log('========================================================================\n');
}

verifyAll();

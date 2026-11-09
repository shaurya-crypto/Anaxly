const { supabase } = require('./db_helper');

async function checkModules() {
  const chapterCurriculums = [
    { ch: 7, id: 'da5625a5-7071-4533-8667-13da4c28abda' },
    { ch: 8, id: '8be782c9-c0d3-425e-bb81-c18c298dc4a7' },
    { ch: 9, id: '9a32d68b-ea7e-4860-99c1-0152d3dd6fcd' },
    { ch: 10, id: '1908699a-60c6-4a5e-9f27-05f9111fe142' },
    { ch: 11, id: 'ba28b0f0-bc67-4638-8c25-092fd7604db4' },
    { ch: 12, id: 'f0fa824b-38af-44dc-bb2e-e7f5519bad6f' },
    { ch: 13, id: '136b112f-1d39-41ed-9d1b-14236bc5fe52' },
  ];

  for (const c of chapterCurriculums) {
    const { data, error } = await supabase
      .from('syllabus_modules')
      .select('id, order_index, title')
      .eq('curriculum_id', c.id)
      .order('order_index', { ascending: true });

    if (error) {
      console.error(`Error ch ${c.ch}:`, error);
      continue;
    }

    console.log(`Chapter ${c.ch} (${c.id}): ${data.length} modules found`);
    for (const m of data) {
      console.log(`  [Mod ${m.order_index}] ${m.id} | ${m.title}`);
    }
  }
}

checkModules();

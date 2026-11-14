const { supabase } = require('./db_helper');

async function verify() {
  const ids = [
    { id: '1053ed93-7167-423b-bdf0-0c73f2b179ff', name: 'Chapter 3' },
    { id: 'b1a05ff2-8ca8-4d59-b7c7-cc0e1304c3ae', name: 'Chapter 4' },
    { id: '8d01a5f5-bf82-49c2-9fab-253d26b086f4', name: 'Chapter 5' },
    { id: '7e1d5438-1174-4577-8599-5f05a6642093', name: 'Chapter 6' }
  ];

  console.log('=== VERIFYING DATABASE STATE IN SUPABASE ===\n');

  for (const c of ids) {
    const { data, error } = await supabase
      .from('syllabus_modules')
      .select('id, order_index, title, key_concepts, worked_examples, visual_lesson_plan')
      .eq('curriculum_id', c.id)
      .order('order_index');

    if (error) {
      console.error(`Error querying ${c.name}:`, error);
      continue;
    }

    console.log(`${c.name} (${data.length} modules):`);
    for (const m of data) {
      const plan = m.visual_lesson_plan || {};
      const cvs = plan.concept_visuals || [];
      const wes = m.worked_examples || [];
      const kcs = m.key_concepts || [];
      const firstImg = cvs[0]?.image_url || 'N/A';
      console.log(`  [Mod ${m.order_index}] ${m.title.substring(0, 40)} | KC: ${kcs.length} | CV: ${cvs.length} | WE: ${wes.length} | 1st Img: ${firstImg}`);
    }
    console.log();
  }
}

verify();

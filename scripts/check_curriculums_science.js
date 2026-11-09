const { supabase } = require('./db_helper');

async function checkCurriculums() {
  const { data, error } = await supabase
    .from('curriculums')
    .select('id, title, class_level, category, order_index')
    .ilike('class_level', '%9%')
    .ilike('category', '%science%')
    .order('order_index', { ascending: true });

  if (error) {
    console.error('Error fetching curriculums:', error);
    return;
  }

  console.log(`Found ${data.length} Class 9 Science curriculums:`);
  for (const c of data) {
    console.log(`[Order ${c.order_index}] ID: ${c.id} | Title: ${c.title}`);
  }
}

checkCurriculums();

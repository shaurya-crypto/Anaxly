const { supabase } = require('./db_helper');

async function checkModules() {
  const ids = [
    '51300b78-bda8-4bc0-80bc-f3cb1af21a7e',
    '371d932e-e821-45ad-bb65-3a53ba0ade31',
    '8c3aa719-1f5a-4931-8eea-cfa85e042048',
    'c57dfef2-2585-4f56-8b57-0133596a424f',
    '74b1502a-ed58-4508-b229-e3421be43010',
    'dd776dc7-c0b1-46e5-ae46-3cb865f03cea'
  ];

  const { data, error } = await supabase
    .from('syllabus_modules')
    .select('id, curriculum_id, order_index, title')
    .in('curriculum_id', ids)
    .order('order_index');

  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log(`Found ${data.length} existing modules for Part 2.`);
  data.forEach(m => console.log(`[Curriculum: ${m.curriculum_id}] #${m.order_index}: ${m.title}`));
}
checkModules();

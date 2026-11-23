const { supabase } = require('./db_helper');

async function checkExamples() {
  // Let's sample a module from Ch 1, Ch 5, Ch 11, Ch 13
  const { data: mods, error } = await supabase
    .from('syllabus_modules')
    .select('order_index, title, worked_examples')
    .in('order_index', [1, 5, 26, 31, 65, 70, 77, 82]);

  if (error) {
    console.error(error);
    return;
  }

  for (const m of mods) {
    console.log(`\n======================================================`);
    console.log(`MODULE ${m.order_index}: ${m.title}`);
    console.log(`Examples count: ${m.worked_examples ? m.worked_examples.length : 0}`);
    if (m.worked_examples && m.worked_examples.length > 0) {
      console.log('Sample Example 1:');
      console.log(JSON.stringify(m.worked_examples[0], null, 2).slice(0, 800));
    }
  }
}

checkExamples();
const { supabase } = require('./db_helper');
const fs = require('fs');
const path = require('path');

async function syncClass9() {
  console.log('=== SYNCING CLASS 9 SCIENCE MODULES TO SUPABASE ===');
  
  const files = [
    { ch: 2, file: 'scripts/science_modules_ch2.json', id: 'c0d6c12e-5576-434d-b541-5142fe09f03b' },
    { ch: 3, file: 'scripts/science_modules_ch3.json', id: '1053ed93-7167-423b-bdf0-0c73f2b179ff' },
    { ch: 4, file: 'scripts/science_modules_ch4.json', id: 'b1a05ff2-8ca8-4d59-b7c7-cc0e1304c3ae' },
    { ch: 5, file: 'scripts/science_modules_ch5.json', id: '8d01a5f5-bf82-49c2-9fab-253d26b086f4' },
    { ch: 6, file: 'scripts/science_modules_ch6.json', id: '7e1d5438-1174-4577-8599-5f05a6642093' },
    { ch: 7, file: 'scripts/science_modules_ch7.json', id: 'da5625a5-7071-4533-8667-13da4c28abda' },
    { ch: 8, file: 'scripts/science_modules_ch8.json', id: '8be782c9-c0d3-425e-bb81-c18c298dc4a7' },
    { ch: 9, file: 'scripts/science_modules_ch9.json', id: '9a32d68b-ea7e-4860-99c1-0152d3dd6fcd' },
    { ch: 10, file: 'scripts/science_modules_ch10.json', id: '1908699a-60c6-4a5e-9f27-05f9111fe142' },
    { ch: 11, file: 'scripts/science_modules_ch11.json', id: 'ba28b0f0-bc67-4638-8c25-092fd7604db4' },
    { ch: 12, file: 'scripts/science_modules_ch12.json', id: 'f0fa824b-38af-44dc-bb2e-e7f5519bad6f' },
    { ch: 13, file: 'scripts/science_modules_ch13.json', id: '136b112f-1d39-41ed-9d1b-14236bc5fe52' }
  ];

  for (const item of files) {
    if (!fs.existsSync(item.file)) continue;
    const mods = JSON.parse(fs.readFileSync(item.file, 'utf8'));
    for (const m of mods) {
      const { error } = await supabase
        .from('syllabus_modules')
        .update({
          worked_examples: m.worked_examples,
          title: m.title,
          description: m.description,
          key_concepts: m.key_concepts,
          subtopics: m.subtopics
        })
        .eq('curriculum_id', item.id)
        .eq('order_index', m.order_index);

      if (error) {
        console.error(`Error updating Ch ${item.ch} M${m.order_index}:`, error);
      }
    }
    console.log(`Synced Chapter ${item.ch} (${mods.length} modules) to Supabase.`);
  }
}

async function syncClass10() {
  console.log('\n=== SYNCING CLASS 10 SCIENCE MODULES TO SUPABASE ===');
  const dir = path.join(__dirname, 'science_class10_modules');
  const files = fs.readdirSync(dir).filter(f => f.startsWith('chapter_') && f.endsWith('.json'));

  for (const fname of files) {
    const fpath = path.join(dir, fname);
    const mods = JSON.parse(fs.readFileSync(fpath, 'utf8'));
    if (!mods.length) continue;
    const currId = mods[0].curriculum_id;

    for (const m of mods) {
      const { error } = await supabase
        .from('syllabus_modules')
        .update({
          worked_examples: m.worked_examples,
          title: m.title
        })
        .eq('id', m.id);

      if (error) {
        console.error(`Error updating Class 10 ${fname} M${m.order_index}:`, error);
      }
    }
    console.log(`Synced Class 10 ${fname} (${mods.length} modules) to Supabase.`);
  }
}

async function main() {
  await syncClass9();
  await syncClass10();
  console.log('\nALL CLASS 9 & 10 SCIENCE MODULES SYNCED SUCCESSFULLY TO SUPABASE!');
}

main();

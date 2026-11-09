/**
 * Production Database Upload Script:
 * Uploads all 42 syllabus_modules across Class 9 Science:
 * Chapters 7, 8, 9, 10, 11, 12, and 13 (NCERT / CBSE)
 */

const fs = require('fs');
const path = require('path');
const { supabase } = require('./db_helper');

const CHAPTER_CONFIG = [
  {
    chapter: 7,
    curriculum_id: 'da5625a5-7071-4533-8667-13da4c28abda',
    file: 'scripts/science_modules_ch7.json',
    title: 'Chapter 7: Work, Energy, and Simple Machines'
  },
  {
    chapter: 8,
    curriculum_id: '8be782c9-c0d3-425e-bb81-c18c298dc4a7',
    file: 'scripts/science_modules_ch8.json',
    title: 'Chapter 8: Journey Inside the Atom'
  },
  {
    chapter: 9,
    curriculum_id: '9a32d68b-ea7e-4860-99c1-0152d3dd6fcd',
    file: 'scripts/science_modules_ch9.json',
    title: 'Chapter 9: Atomic Foundations of Matter'
  },
  {
    chapter: 10,
    curriculum_id: '1908699a-60c6-4a5e-9f27-05f9111fe142',
    file: 'scripts/science_modules_ch10.json',
    title: 'Chapter 10: Sound Waves: Characteristics and Applications'
  },
  {
    chapter: 11,
    curriculum_id: 'ba28b0f0-bc67-4638-8c25-092fd7604db4',
    file: 'scripts/science_modules_ch11.json',
    title: 'Chapter 11: Reproduction: How Life Continues'
  },
  {
    chapter: 12,
    curriculum_id: 'f0fa824b-38af-44dc-bb2e-e7f5519bad6f',
    file: 'scripts/science_modules_ch12.json',
    title: 'Chapter 12: Patterns in Life: Diversity and Classification'
  },
  {
    chapter: 13,
    curriculum_id: '136b112f-1d39-41ed-9d1b-14236bc5fe52',
    file: 'scripts/science_modules_ch13.json',
    title: 'Chapter 13: Earth as a System: Energy, Matter, and Life'
  }
];

async function uploadChapters() {
  console.log('Starting Batch Upload of Science Chapters 7 through 13 to Supabase...\n');

  let totalUpdated = 0;
  let totalInserted = 0;

  for (const config of CHAPTER_CONFIG) {
    console.log(`========================================================================`);
    console.log(`Processing ${config.title} (Curriculum ID: ${config.curriculum_id})`);
    console.log(`========================================================================`);

    const rawData = fs.readFileSync(path.resolve(config.file), 'utf8');
    const modules = JSON.parse(rawData);

    console.log(`Loaded ${modules.length} modules from ${config.file}`);

    for (const mod of modules) {
      const order = mod.order_index;
      const title = mod.title;

      // Prepare payload
      const payload = {
        curriculum_id: config.curriculum_id,
        order_index: order,
        title: mod.title,
        description: mod.description,
        key_concepts: mod.key_concepts || [],
        subtopics: mod.subtopics || [],
        success_criteria: mod.success_criteria || '',
        chapter_notes: mod.chapter_notes || '',
        worked_examples: mod.worked_examples || [],
        common_misconceptions: mod.common_misconceptions || [],
        visual_lesson_plan: mod.visual_lesson_plan || {},
        ai_system_prompt_context: mod.ai_system_prompt_context || '',
        class_level: 'Class 9',
        board: 'CBSE'
      };

      // Check if module exists
      const { data: existing, error: checkError } = await supabase
        .from('syllabus_modules')
        .select('id, order_index, title')
        .eq('curriculum_id', config.curriculum_id)
        .eq('order_index', order)
        .maybeSingle();

      if (checkError) {
        console.error(`  [Mod ${order}] Error checking existing record:`, checkError);
        continue;
      }

      if (existing) {
        // Update existing record
        const { error: updateError } = await supabase
          .from('syllabus_modules')
          .update(payload)
          .eq('id', existing.id);

        if (updateError) {
          console.error(`  [Mod ${order}] FAILED to update (${existing.id}):`, updateError);
        } else {
          console.log(`  [Mod ${order}] Successfully UPDATED (${existing.id}): ${title.substring(0, 50)}...`);
          totalUpdated++;
        }
      } else {
        // Insert new record if it does not exist
        const { data: inserted, error: insertError } = await supabase
          .from('syllabus_modules')
          .insert(payload)
          .select('id')
          .single();

        if (insertError) {
          console.error(`  [Mod ${order}] FAILED to insert:`, insertError);
        } else {
          console.log(`  [Mod ${order}] Successfully INSERTED (${inserted.id}): ${title.substring(0, 50)}...`);
          totalInserted++;
        }
      }
    }
  }

  console.log('\n========================================================================');
  console.log(`UPLOAD COMPLETE: ${totalUpdated} updated, ${totalInserted} inserted (Total: ${totalUpdated + totalInserted} modules).`);
  console.log('========================================================================\n');
}

uploadChapters().catch((err) => {
  console.error('Fatal upload error:', err);
  process.exit(1);
});

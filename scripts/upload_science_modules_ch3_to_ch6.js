/**
 * Production Database Upload Script:
 * Updates all 26 syllabus_modules across Class 9 Science:
 * Chapters 3, 4, 5, and 6 (NCERT / CBSE)
 */

const fs = require('fs');
const path = require('path');
const { supabase } = require('./db_helper');

const CHAPTER_CONFIG = [
  {
    chapter: 3,
    curriculum_id: '1053ed93-7167-423b-bdf0-0c73f2b179ff',
    file: 'scripts/science_modules_ch3.json',
    title: 'Chapter 3: Tissues in Action'
  },
  {
    chapter: 4,
    curriculum_id: 'b1a05ff2-8ca8-4d59-b7c7-cc0e1304c3ae',
    file: 'scripts/science_modules_ch4.json',
    title: 'Chapter 4: Describing Motion Around Us'
  },
  {
    chapter: 5,
    curriculum_id: '8d01a5f5-bf82-49c2-9fab-253d26b086f4',
    file: 'scripts/science_modules_ch5.json',
    title: 'Chapter 5: Exploring Mixtures and their Separation'
  },
  {
    chapter: 6,
    curriculum_id: '7e1d5438-1174-4577-8599-5f05a6642093',
    file: 'scripts/science_modules_ch6.json',
    title: 'Chapter 6: How Forces Affect Motion'
  }
];

async function uploadChapters() {
  console.log('Starting Batch Upload of Science Chapters 3, 4, 5, 6 to Supabase...\n');

  let totalUpdated = 0;

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
        const insertPayload = {
          curriculum_id: config.curriculum_id,
          order_index: order,
          ...payload
        };
        const { data: inserted, error: insertError } = await supabase
          .from('syllabus_modules')
          .insert(insertPayload)
          .select('id')
          .single();

        if (insertError) {
          console.error(`  [Mod ${order}] FAILED to insert:`, insertError);
        } else {
          console.log(`  [Mod ${order}] Successfully INSERTED (${inserted.id}): ${title.substring(0, 50)}...`);
          totalUpdated++;
        }
      }
    }
    console.log();
  }

  console.log(`========================================================================`);
  console.log(`Batch Upload Complete! Total modules successfully processed: ${totalUpdated}/26`);
  console.log(`========================================================================\n`);
}

uploadChapters()
  .then(() => {
    console.log('Script execution finished successfully.');
    process.exit(0);
  })
  .catch((err) => {
    console.error('Fatal upload error:', err);
    process.exit(1);
  });

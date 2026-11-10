/**
 * Production Database Upload Script:
 * Uploads all 47 syllabus_modules across Class 9 Mathematics:
 * Chapters 1, 2, 3, 4, 5, 6, 7, and 8 (NCERT Ganita Manjari Grade 9 Part 1 / CBSE)
 */

const fs = require('fs');
const path = require('path');
const { supabase } = require('./db_helper');

const CHAPTER_CONFIG = [
  {
    chapter: 1,
    curriculum_id: '3fdc7a01-da88-43e6-aef5-c48bf1d64ef5',
    file: 'scripts/maths_modules_ch1.json',
    title: 'Chapter 1: Orienting Yourself: The Use of Coordinates'
  },
  {
    chapter: 2,
    curriculum_id: 'cd14fc20-13b7-4d96-98fb-956720dc0f23',
    file: 'scripts/maths_modules_ch2.json',
    title: 'Chapter 2: Introduction to Linear Polynomials'
  },
  {
    chapter: 3,
    curriculum_id: '09ca99d2-0489-48f2-8d39-8b26ca7885c9',
    file: 'scripts/maths_modules_ch3.json',
    title: 'Chapter 3: The World of Numbers'
  },
  {
    chapter: 4,
    curriculum_id: 'cef5b4c4-9fad-4f5b-8201-372cce5f4f61',
    file: 'scripts/maths_modules_ch4.json',
    title: 'Chapter 4: Exploring Algebraic Identities'
  },
  {
    chapter: 5,
    curriculum_id: 'de83f257-aada-4e27-b420-f7884165c990',
    file: 'scripts/maths_modules_ch5.json',
    title: 'Chapter 5: I’m Up and Down, and Round and Round'
  },
  {
    chapter: 6,
    curriculum_id: '2ca7b10a-3fb9-484f-8116-30d7b586c526',
    file: 'scripts/maths_modules_ch6.json',
    title: 'Chapter 6: Measuring Space: Perimeter and Area'
  },
  {
    chapter: 7,
    curriculum_id: '257078e3-5cf0-4286-a1e3-661ce480edc3',
    file: 'scripts/maths_modules_ch7.json',
    title: 'Chapter 7: The Mathematics of Maybe: Introduction to Probability'
  },
  {
    chapter: 8,
    curriculum_id: 'b45d590f-323e-4263-b899-23d95b2094a7',
    file: 'scripts/maths_modules_ch8.json',
    title: 'Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions'
  }
];

async function uploadMathsChapters() {
  console.log('Starting Batch Upload of Class 9 Maths Chapters 1 through 8 to Supabase...\n');

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

      // Extract quiz_questions from concept_questions if not directly provided
      let quizQuestions = mod.quiz_questions || [];
      if ((!quizQuestions || quizQuestions.length === 0) && mod.visual_lesson_plan && mod.visual_lesson_plan.concept_questions) {
        quizQuestions = [];
        for (const cqGroup of mod.visual_lesson_plan.concept_questions) {
          if (cqGroup.questions) {
            for (const q of cqGroup.questions) {
              quizQuestions.push({
                question: q.question,
                type: q.type || 'short_answer',
                options: q.options || [],
                correct_answer: q.ideal_answer || '',
                explanation: q.ideal_answer || '',
                hint: q.socratic_hint || ''
              });
            }
          }
        }
      }

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
        estimated_minutes: mod.estimated_minutes || 25,
        quiz_questions: quizQuestions,
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
  process.exit(0);
}

uploadMathsChapters().catch((err) => {
  console.error('Fatal Upload Error:', err);
  process.exit(1);
});

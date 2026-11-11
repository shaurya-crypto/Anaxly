/**
 * Production Database Upload Script:
 * Uploads all 75 syllabus_modules across Class 10 Mathematics:
 * Chapters 1 to 14 (NCERT Mathematics Class 10 / CBSE)
 * Fully compliant with Invariant 10.
 */

const fs = require('fs');
const path = require('path');
const { supabase } = require('./db_helper');

const CHAPTER_CONFIG = [
  {
    chapter: 1,
    curriculum_id: '4f230f16-2470-4304-b7cd-4aeacbc51831',
    file: 'scripts/maths_class10_modules/ch1_real_numbers.json',
    title: 'Chapter 1: Real Numbers'
  },
  {
    chapter: 2,
    curriculum_id: '71ff1091-5502-490c-bcc1-9624b699620f',
    file: 'scripts/maths_class10_modules/ch2_polynomials.json',
    title: 'Chapter 2: Polynomials'
  },
  {
    chapter: 3,
    curriculum_id: '990a1496-d88d-4665-8176-cd3cae0f488a',
    file: 'scripts/maths_class10_modules/ch3_pair_of_linear_equations_in_two_variables.json',
    title: 'Chapter 3: Pair of Linear Equations in Two Variables'
  },
  {
    chapter: 4,
    curriculum_id: 'f476ad58-425d-44d9-8150-4fc0c478834a',
    file: 'scripts/maths_class10_modules/ch4_quadratic_equations.json',
    title: 'Chapter 4: Quadratic Equations'
  },
  {
    chapter: 5,
    curriculum_id: '916e8989-c22e-4dd9-97a0-f081e63fb77d',
    file: 'scripts/maths_class10_modules/ch5_arithmetic_progressions.json',
    title: 'Chapter 5: Arithmetic Progressions'
  },
  {
    chapter: 6,
    curriculum_id: '5a8a4828-b882-4576-aeaf-fd3a7a2a8354',
    file: 'scripts/maths_class10_modules/ch6_triangles.json',
    title: 'Chapter 6: Triangles'
  },
  {
    chapter: 7,
    curriculum_id: '12f22395-a321-4a9d-85af-cd50b0fdcafe',
    file: 'scripts/maths_class10_modules/ch7_coordinate_geometry.json',
    title: 'Chapter 7: Coordinate Geometry'
  },
  {
    chapter: 8,
    curriculum_id: 'd854ea09-23bd-4eeb-b9b0-0b943b22ed76',
    file: 'scripts/maths_class10_modules/ch8_introduction_to_trigonometry.json',
    title: 'Chapter 8: Introduction to Trigonometry'
  },
  {
    chapter: 9,
    curriculum_id: '28268af8-3331-453a-ad5e-6add84c0c2ba',
    file: 'scripts/maths_class10_modules/ch9_some_applications_of_trigonometry.json',
    title: 'Chapter 9: Some Applications of Trigonometry'
  },
  {
    chapter: 10,
    curriculum_id: '0eba841d-8fcd-4e01-bbc0-247a3f0a29c5',
    file: 'scripts/maths_class10_modules/ch10_circles.json',
    title: 'Chapter 10: Circles'
  },
  {
    chapter: 11,
    curriculum_id: '938ed126-df2f-438f-b6dc-8c7e1273ec24',
    file: 'scripts/maths_class10_modules/ch11_areas_related_to_circles.json',
    title: 'Chapter 11: Areas Related to Circles'
  },
  {
    chapter: 12,
    curriculum_id: 'f30fffde-90c1-402d-83c3-7d2af0e9f423',
    file: 'scripts/maths_class10_modules/ch12_surface_areas_and_volumes.json',
    title: 'Chapter 12: Surface Areas and Volumes'
  },
  {
    chapter: 13,
    curriculum_id: 'ee79fe72-f746-45c7-a36e-b5a11c82d479',
    file: 'scripts/maths_class10_modules/ch13_statistics.json',
    title: 'Chapter 13: Statistics'
  },
  {
    chapter: 14,
    curriculum_id: '019778b1-dc6c-4660-9538-1940ec6cad64',
    file: 'scripts/maths_class10_modules/ch14_probability.json',
    title: 'Chapter 14: Probability'
  }
];

async function uploadAllClass10Maths() {
  console.log('Starting Batch Upload of Class 10 Maths (Chapters 1 to 14) to Supabase...\n');

  let totalUpdated = 0;
  let totalInserted = 0;

  for (const config of CHAPTER_CONFIG) {
    console.log(`========================================================================`);
    console.log(`Processing ${config.title} (Curriculum ID: ${config.curriculum_id})`);
    console.log(`========================================================================`);

    const filePath = path.resolve(config.file);
    if (!fs.existsSync(filePath)) {
      console.error(`ERROR: File not found: ${filePath}`);
      continue;
    }

    const rawData = fs.readFileSync(filePath, 'utf8');
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
        class_level: 'Class 10',
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

uploadAllClass10Maths().catch((err) => {
  console.error('Fatal Upload Error:', err);
  process.exit(1);
});

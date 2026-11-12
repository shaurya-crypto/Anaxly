/**
 * Production Database Upload Script:
 * Uploads all 33 syllabus_modules across Class 9 Mathematics Part 2 (Final-Term):
 * Chapters 9 to 14 (NCERT Ganita Manjari Grade 9 Part II / CBSE)
 * Fully compliant with Invariant 10, 11, 12, 14 & 15.
 */

const fs = require('fs');
const path = require('path');
const { supabase } = require('./db_helper');

const CHAPTER_CONFIG = [
  {
    chapter: 9,
    curriculum_id: '51300b78-bda8-4bc0-80bc-f3cb1af21a7e',
    file: 'scripts/maths_pt2_modules/ch9_propositions.json',
    title: 'Chapter 9: Propositions and their Converses'
  },
  {
    chapter: 10,
    curriculum_id: '371d932e-e821-45ad-bb65-3a53ba0ade31',
    file: 'scripts/maths_pt2_modules/ch10_understanding_data.json',
    title: 'Chapter 10: How Quantities Combine: Understanding Data'
  },
  {
    chapter: 11,
    curriculum_id: '8c3aa719-1f5a-4931-8eea-cfa85e042048',
    file: 'scripts/maths_pt2_modules/ch11_algorithms.json',
    title: 'Chapter 11: The World of Algorithms'
  },
  {
    chapter: 12,
    curriculum_id: 'c57dfef2-2585-4f56-8b57-0133596a424f',
    file: 'scripts/maths_pt2_modules/ch12_quadrilaterals.json',
    title: 'Chapter 12: Quadrilaterals'
  },
  {
    chapter: 13,
    curriculum_id: '74b1502a-ed58-4508-b229-e3421be43010',
    file: 'scripts/maths_pt2_modules/ch13_linear_equations.json',
    title: 'Chapter 13: Two Variables, One Line'
  },
  {
    chapter: 14,
    curriculum_id: 'dd776dc7-c0b1-46e5-ae46-3cb865f03cea',
    file: 'scripts/maths_pt2_modules/ch14_surface_areas_volumes.json',
    title: 'Chapter 14: Math of Space: Surface Area and Volume'
  }
];

async function uploadAllClass9MathsPt2() {
  console.log('========================================================================');
  console.log('UPLOADING CLASS 9 MATHEMATICS PART 2 (FINAL-TERM) MODULES TO SUPABASE');
  console.log('========================================================================\n');

  let totalInserted = 0;
  let totalUpdated = 0;

  for (const config of CHAPTER_CONFIG) {
    console.log(`Processing ${config.title} (Curriculum ID: ${config.curriculum_id})`);
    const filePath = path.resolve(config.file);
    if (!fs.existsSync(filePath)) {
      console.error(`  [-] File not found: ${filePath}`);
      continue;
    }

    const rawData = fs.readFileSync(filePath, 'utf8');
    const modules = JSON.parse(rawData);
    console.log(`  Loaded ${modules.length} modules from ${config.file}`);

    for (const mod of modules) {
      const order = mod.order_index;
      
      const payload = {
        curriculum_id: config.curriculum_id,
        order_index: order,
        title: mod.title,
        description: mod.description,
        key_concepts: mod.key_concepts || [],
        subtopics: mod.subtopics || [],
        success_criteria: mod.success_criteria || [],
        chapter_notes: mod.chapter_notes || '',
        worked_examples: mod.worked_examples || [],
        common_misconceptions: mod.common_misconceptions || [],
        visual_lesson_plan: {
          ...(mod.visual_lesson_plan || {}),
          syllabus_term: 'Final-Term'
        },
        ai_system_prompt_context: `You are the master AI Mathematics Tutor for CBSE Class 9 Final-Term. The student is currently studying ${config.title}, Module ${order}: "${mod.title}". Teach with step-by-step mathematical rigor, Socratic dialogue, zero raw programming signs (*, **, //, ^), and authentic topper layout.`,
        estimated_minutes: mod.estimated_minutes || 25,
        quiz_questions: mod.quiz_questions || [],
        class_level: 'Class 9',
        board: 'CBSE'
      };

      // Check if module already exists
      const { data: existing, error: checkError } = await supabase
        .from('syllabus_modules')
        .select('id, order_index, title')
        .eq('curriculum_id', config.curriculum_id)
        .eq('order_index', order)
        .maybeSingle();

      if (checkError) {
        console.error(`  [-] Error checking module ${order}:`, checkError);
        continue;
      }

      if (existing) {
        const { error: updateError } = await supabase
          .from('syllabus_modules')
          .update(payload)
          .eq('id', existing.id);

        if (updateError) {
          console.error(`  [-] Error updating module ${order}:`, updateError);
        } else {
          console.log(`  [+] Updated Module #${order}: ${mod.title}`);
          totalUpdated++;
        }
      } else {
        const { error: insertError } = await supabase
          .from('syllabus_modules')
          .insert(payload);

        if (insertError) {
          console.error(`  [-] Error inserting module ${order}:`, insertError);
        } else {
          console.log(`  [+] Inserted Module #${order}: ${mod.title}`);
          totalInserted++;
        }
      }
    }
    console.log('');
  }

  console.log('========================================================================');
  console.log(`UPLOAD COMPLETE: ${totalInserted} inserted, ${totalUpdated} updated.`);
  console.log('========================================================================');
}

uploadAllClass9MathsPt2();

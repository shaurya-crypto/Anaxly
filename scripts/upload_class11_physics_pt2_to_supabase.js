/**
 * upload_class11_physics_pt2_to_supabase.js
 * Ingestion script for CBSE Class 11 Physics Part 2:
 * Chapters 8 to 14 (44 Modules, Classified strictly as Final-Term Examination Syllabus)
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { supabase } = require('./db_helper');

const CURRICULUMS_FILE = path.join(__dirname, 'physics_class11_modules', 'class11_physics_pt2_curriculums.json');

async function uploadPhysicsCurriculumAndModules() {
  console.log('========================================================================');
  console.log('UPLOADING CLASS 11 PHYSICS PART 2 (FINAL-TERM EXAMINATION) TO SUPABASE');
  console.log('Chapters 8 to 14 (Modules 45 to 88)');
  console.log('========================================================================\n');

  if (!fs.existsSync(CURRICULUMS_FILE)) {
    console.error(`Curriculums file not found: ${CURRICULUMS_FILE}`);
    process.exit(1);
  }

  const curriculumsMeta = JSON.parse(fs.readFileSync(CURRICULUMS_FILE, 'utf8'));
  const curriculumMap = {}; // order_index -> uuid

  // -------------------------------------------------------------
  // STEP 1: Upsert Curriculums (Chapters 8 to 14)
  // -------------------------------------------------------------
  console.log('STEP 1: Upserting 7 Curriculums for Part 2 (Final-Term Syllabus)...\n');

  for (const c of curriculumsMeta) {
    const { data: existing, error: checkErr } = await supabase
      .from('curriculums')
      .select('id, title')
      .eq('class_level', 'Class 11')
      .eq('category', 'Physics')
      .eq('order_index', c.order_index)
      .maybeSingle();

    if (checkErr) {
      console.error(`Error checking curriculum for Chapter ${c.order_index}:`, checkErr);
      continue;
    }

    let currId;
    if (existing) {
      currId = existing.id;
      console.log(`[Ch ${c.order_index}] Found existing curriculum (${currId}): ${c.title}`);
      
      const { error: updateErr } = await supabase
        .from('curriculums')
        .update({
          title: c.title,
          description: `[CBSE Final-Term Examination Syllabus | ${c.unit_name}] ${c.description}`,
          category: c.category,
          difficulty_level: c.difficulty_level,
          estimated_duration_minutes: c.estimated_duration_minutes,
          is_published: true,
          board: c.board,
          notes_source_filename: c.notes_source_filename,
          notes_summary: `[Final-Term Syllabus | ${c.unit_name} | ${c.weightage_marks}] ${c.notes_summary}`,
          notes_updated_at: new Date().toISOString()
        })
        .eq('id', currId);

      if (updateErr) console.error(`  Error updating curriculum ${currId}:`, updateErr);
      else console.log(`  Updated metadata for Chapter ${c.order_index}`);
    } else {
      currId = crypto.randomUUID();
      console.log(`[Ch ${c.order_index}] Creating new curriculum (${currId}): ${c.title}`);

      const { error: insertErr } = await supabase
        .from('curriculums')
        .insert({
          id: currId,
          title: c.title,
          description: `[CBSE Final-Term Examination Syllabus | ${c.unit_name}] ${c.description}`,
          category: c.category,
          difficulty_level: c.difficulty_level,
          estimated_duration_minutes: c.estimated_duration_minutes,
          is_published: true,
          class_level: c.class_level,
          order_index: c.order_index,
          board: c.board,
          notes_source_filename: c.notes_source_filename,
          notes_summary: `[Final-Term Syllabus | ${c.unit_name} | ${c.weightage_marks}] ${c.notes_summary}`,
          notes_updated_at: new Date().toISOString()
        });

      if (insertErr) {
        console.error(`  Error inserting curriculum for Ch ${c.order_index}:`, insertErr);
        continue;
      }
      console.log(`  Inserted new curriculum for Chapter ${c.order_index}`);
    }

    curriculumMap[c.order_index] = currId;
  }

  console.log('\nCurriculum Mapping Established:', curriculumMap);

  // -------------------------------------------------------------
  // STEP 2: Upsert 44 Modules (Modules 45 to 88)
  // -------------------------------------------------------------
  console.log('\nSTEP 2: Upserting 44 Modules into `syllabus_modules` table...\n');

  let totalUpdated = 0;
  let totalInserted = 0;

  for (let chNum = 8; chNum <= 14; chNum++) {
    const currId = curriculumMap[chNum];
    if (!currId) {
      console.error(`Skipping Chapter ${chNum} - no curriculum ID found.`);
      continue;
    }

    const modFile = path.join(__dirname, 'physics_class11_modules', `physics_modules_ch${chNum}.json`);
    if (!fs.existsSync(modFile)) {
      console.error(`Module file not found: ${modFile}`);
      continue;
    }

    const chapterModules = JSON.parse(fs.readFileSync(modFile, 'utf8'));
    console.log(`------------------------------------------------------------------------`);
    console.log(`Ingesting Chapter ${chNum} (${chapterModules.length} Modules) -> Curriculum ${currId}`);
    console.log(`------------------------------------------------------------------------`);

    for (const mod of chapterModules) {
      const order = mod.order_index;
      const title = mod.title;

      // Extract quiz questions from concept_questions if not directly set
      let quizQuestions = mod.quiz_questions || [];
      if ((!quizQuestions || quizQuestions.length === 0) && mod.concept_questions) {
        quizQuestions = mod.concept_questions.map(q => ({
          question: q.question,
          type: 'multiple_choice',
          options: q.options || [],
          correct_answer: q.correct_answer || (q.options && q.options[0]) || '',
          explanation: q.explanation || '',
          hint: q.explanation || ''
        }));
      }

      // Ensure success_criteria is string formatted
      let successCriteriaStr = '';
      if (Array.isArray(mod.success_criteria)) {
        successCriteriaStr = mod.success_criteria.map((sc, i) => `${i + 1}. ${sc}`).join('\n');
      } else {
        successCriteriaStr = mod.success_criteria || '';
      }

      // Clean visual lesson plan with syllabus term tagging
      const cleanVisualPlan = {
        ...mod.visual_lesson_plan,
        syllabus_term: 'Final-Term Examination',
        unit_name: mod.syllabus_unit || mod.unit_name || '',
        syllabus_pacing: `Final-Term Examination | ${mod.syllabus_unit || mod.unit_name || ''}`
      };
      delete cleanVisualPlan.start_date;
      delete cleanVisualPlan.end_date;
      delete cleanVisualPlan.target_completion_date;

      // Payload
      const payload = {
        curriculum_id: currId,
        order_index: order,
        title: mod.title,
        description: mod.description,
        key_concepts: mod.key_concepts || [],
        subtopics: mod.subtopics || [],
        success_criteria: successCriteriaStr,
        chapter_notes: mod.chapter_notes || '',
        worked_examples: mod.worked_examples || [],
        common_misconceptions: mod.common_misconceptions || [],
        visual_lesson_plan: cleanVisualPlan,
        ai_system_prompt_context: mod.ai_system_prompt_context || `CBSE Class 11 Physics Module ${order}: ${title}. Final-Term Examination Syllabus (${cleanVisualPlan.unit_name}). Senior-level rigor, Socratic cadence, clear NCERT derivation, precision vector SVGs, and clean chalkboard typography.`,
        estimated_minutes: mod.estimated_minutes || 55,
        quiz_questions: quizQuestions,
        class_level: 'Class 11',
        board: 'CBSE'
      };

      // Check if module already exists for this curriculum and order_index
      const { data: existingMod, error: checkModErr } = await supabase
        .from('syllabus_modules')
        .select('id, order_index, title')
        .eq('curriculum_id', currId)
        .eq('order_index', order)
        .maybeSingle();

      if (checkModErr) {
        console.error(`  [Mod ${order}] Error checking existing record:`, checkModErr);
        continue;
      }

      if (existingMod) {
        const { error: updateErr } = await supabase
          .from('syllabus_modules')
          .update(payload)
          .eq('id', existingMod.id);

        if (updateErr) {
          console.error(`  [Mod ${order}] FAILED to update (${existingMod.id}):`, updateErr);
        } else {
          console.log(`  [Mod ${order}] UPDATED (${existingMod.id}): ${title.substring(0, 48)}...`);
          totalUpdated++;
        }
      } else {
        const { data: inserted, error: insertErr } = await supabase
          .from('syllabus_modules')
          .insert(payload)
          .select('id')
          .single();

        if (insertErr) {
          console.error(`  [Mod ${order}] FAILED to insert:`, insertErr);
        } else {
          console.log(`  [Mod ${order}] INSERTED (${inserted.id}): ${title.substring(0, 48)}...`);
          totalInserted++;
        }
      }
    }
  }

  console.log('\n========================================================================');
  console.log(`ALL 44 PART 2 MODULES UPDATED IN SUPABASE (FINAL-TERM SYLLABUS)!`);
  console.log(`Total Updated: ${totalUpdated} | Total Inserted: ${totalInserted} | Total: ${totalUpdated + totalInserted}`);
  console.log('========================================================================\n');

  process.exit(0);
}

uploadPhysicsCurriculumAndModules().catch(err => {
  console.error('Fatal upload error:', err);
  process.exit(1);
});

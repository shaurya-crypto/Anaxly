/**
 * partition_and_update_all_syllabi.js
 * 
 * Partitions and tags all chapters in Class 9 and Class 10 into:
 * - Mid-Term Examination Syllabus
 * - Final-Term Examination Syllabus / Annual Examination
 * 
 * In accordance with:
 * - Directorate of Education GNCT of Delhi & CBSE Secondary 2026-27 Curricular Guidelines
 * - NCERT textbooks & official syllabi
 * - AGENTS.md Invariants 10 and 11
 */

const { supabase } = require('./db_helper');

// Definitions of Mid-Term vs Final-Term for all subjects
const SYLLABUS_PARTITION = {
  'Class 9': {
    'Mathematics': {
      mid_term_orders: [1, 2, 3, 4, 5, 6, 7, 8],
      final_term_orders: [9, 10, 11, 12, 13, 14],
      // Details for Part 2 Chapters (Final-Term)
      pt2_chapters: [
        {
          order_index: 9,
          title: 'Chapter 9: Propositions and their Converses',
          description: 'Explore the foundations of mathematical logic, statements, truth values, propositions, and their converses. Understand conditional statements, biconditional statements, and rigorous proof structures.',
          notes_summary: '[CBSE Final-Term Examination Syllabus | Unit: Mathematical Logic & Geometry] Propositions, truth values, converses, contrapositives, and geometric deductive proofs.',
          estimated_duration_minutes: 240,
          difficulty_level: 'intermediate',
        },
        {
          order_index: 10,
          title: 'Chapter 10: How Quantities Combine: Understanding Data',
          description: 'Master advanced statistical analysis, weighted averages, combining distributions, measures of central tendency, and graphical representations of complex data sets.',
          notes_summary: '[CBSE Final-Term Examination Syllabus | Unit: Statistics & Data Handling] Weighted averages, average of averages, distribution analysis, and variance intuition.',
          estimated_duration_minutes: 220,
          difficulty_level: 'intermediate',
        },
        {
          order_index: 11,
          title: 'Chapter 11: The World of Algorithms',
          description: 'Explore step-by-step mathematical procedures, computational thinking, Euclidean algorithm for division, algorithmic addition/multiplication, and iteration mechanics.',
          notes_summary: '[CBSE Final-Term Examination Syllabus | Unit: Computational Mathematics] Algorithmic design, computational logic, recursion, and step-by-step mathematical solvers.',
          estimated_duration_minutes: 200,
          difficulty_level: 'intermediate',
        },
        {
          order_index: 12,
          title: 'Chapter 12: Quadrilaterals',
          description: 'Investigate properties of quadrilaterals, parallelograms, rectangles, rhombuses, squares, and trapeziums. Derive and apply the Mid-Point Theorem and its converse.',
          notes_summary: '[CBSE Final-Term Examination Syllabus | Unit: Geometry] Angle sum property of quadrilaterals, parallelogram properties, mid-point theorem, and quadrilateral tiling.',
          estimated_duration_minutes: 260,
          difficulty_level: 'advanced',
        },
        {
          order_index: 13,
          title: 'Chapter 13: Two Variables, One Line',
          description: 'Deep dive into linear equations in two variables, graphical representations, slope and intercepts, simultaneous systems, and algebraic solution strategies.',
          notes_summary: '[CBSE Final-Term Examination Syllabus | Unit: Algebra] Linear equations in two variables ax + by + c = 0, Cartesian line graphing, and simultaneous solutions.',
          estimated_duration_minutes: 240,
          difficulty_level: 'intermediate',
        },
        {
          order_index: 14,
          title: 'Chapter 14: Math of Space: Surface Area and Volume',
          description: 'Comprehensive 3D mensuration: surface areas and volumes of cuboids, right circular cylinders, cones, and spheres with real-life application modelling.',
          notes_summary: '[CBSE Final-Term Examination Syllabus | Unit: Mensuration] Surface areas and volumes of combinations of 3D solids with unit conversions and application problems.',
          estimated_duration_minutes: 280,
          difficulty_level: 'advanced',
        }
      ]
    },
    'Science': {
      mid_term_orders: [2, 3, 4, 5, 6],
      final_term_orders: [7, 8, 9, 10, 11, 12, 13]
    }
  },
  'Class 10': {
    'Mathematics': {
      mid_term_orders: [1, 3, 5, 6, 7, 8],
      final_term_orders: [2, 4, 9, 10, 11, 12, 13, 14]
    },
    'Science': {
      mid_term_orders: [1, 2, 3, 5, 6, 9, 10],
      final_term_orders: [4, 7, 8, 11, 12, 13]
    }
  }
};

async function partitionAndTagSyllabi() {
  console.log('========================================================================');
  console.log('PARTITIONING & TAGGING CLASS 9 & 10 SYLLABI (MID-TERM VS FINAL-TERM)');
  console.log('========================================================================\n');

  // STEP 1: Process Class 9 Maths Part 2 (Final-Term) Curriculums
  console.log('--- Step 1: Upserting Class 9 Mathematics Part 2 (Final-Term) Curriculums ---');
  const pt2Defs = SYLLABUS_PARTITION['Class 9']['Mathematics'].pt2_chapters;
  for (const ch of pt2Defs) {
    const { data: existing } = await supabase
      .from('curriculums')
      .select('id, title, order_index')
      .eq('class_level', 'Class 9')
      .eq('category', 'Mathematics')
      .eq('order_index', ch.order_index)
      .maybeSingle();

    if (existing) {
      console.log(`  [Ch ${ch.order_index}] Updating existing curriculum: ${ch.title}`);
      await supabase
        .from('curriculums')
        .update({
          title: ch.title,
          description: ch.description,
          notes_summary: ch.notes_summary,
          is_published: true,
          board: 'CBSE'
        })
        .eq('id', existing.id);
    } else {
      console.log(`  [Ch ${ch.order_index}] Creating new Part 2 curriculum: ${ch.title}`);
      await supabase
        .from('curriculums')
        .insert({
          title: ch.title,
          description: ch.description,
          notes_summary: ch.notes_summary,
          category: 'Mathematics',
          class_level: 'Class 9',
          order_index: ch.order_index,
          estimated_duration_minutes: ch.estimated_duration_minutes,
          difficulty_level: ch.difficulty_level,
          is_published: true,
          board: 'CBSE'
        });
    }
  }

  // STEP 2: Partition and tag all curriculums across Class 9 and 10
  console.log('\n--- Step 2: Tagging Curriculums as Mid-Term vs Final-Term ---');
  const { data: allCurrs, error: currErr } = await supabase
    .from('curriculums')
    .select('id, title, class_level, category, order_index, description, notes_summary')
    .in('class_level', ['Class 9', 'Class 10']);

  if (currErr) {
    console.error('Error fetching curriculums:', currErr);
    process.exit(1);
  }

  for (const c of allCurrs) {
    const classRules = SYLLABUS_PARTITION[c.class_level]?.[c.category];
    if (!classRules) continue;

    const isMidTerm = classRules.mid_term_orders.includes(c.order_index);
    const termLabel = isMidTerm ? 'Mid-Term Examination' : 'Final-Term Examination';
    const tagPrefix = isMidTerm ? '[CBSE Mid-Term Examination Syllabus]' : '[CBSE Final-Term Examination Syllabus]';

    // Clean existing term prefixes to prevent accumulation
    let cleanDesc = (c.description || '')
      .replace(/^\[CBSE (?:Mid|Final)-Term Examination Syllabus(?: \| [^\]]+)?\]\s*/i, '')
      .trim();
    let cleanSummary = (c.notes_summary || '')
      .replace(/^\[(?:CBSE )?(?:Mid|Final)-Term (?:Examination )?Syllabus(?: \| [^\]]+)?\]\s*/i, '')
      .trim();

    const newDesc = `${tagPrefix} ${cleanDesc || c.title}`;
    const newSummary = `[${termLabel} Syllabus] ${cleanSummary || c.title}`;

    await supabase
      .from('curriculums')
      .update({
        description: newDesc,
        notes_summary: newSummary
      })
      .eq('id', c.id);

    console.log(`  [${c.class_level} ${c.category} Ch ${c.order_index}] Tagged as ${termLabel}`);

    // STEP 3: Tag all modules belonging to this curriculum
    const { data: mods } = await supabase
      .from('syllabus_modules')
      .select('id, order_index, title, visual_lesson_plan, ai_system_prompt_context')
      .eq('curriculum_id', c.id);

    if (mods && mods.length > 0) {
      for (const m of mods) {
        const vlp = m.visual_lesson_plan || {};
        vlp.syllabus_term = termLabel;
        vlp.syllabus_pacing = `${termLabel} Syllabus`;

        let aiPrompt = m.ai_system_prompt_context || '';
        if (!aiPrompt.includes(termLabel)) {
          aiPrompt = `CBSE ${c.class_level} ${c.category} Module ${m.order_index}: ${m.title}. ${termLabel} Syllabus. ${aiPrompt}`.trim();
        }

        await supabase
          .from('syllabus_modules')
          .update({
            visual_lesson_plan: vlp,
            ai_system_prompt_context: aiPrompt
          })
          .eq('id', m.id);
      }
      console.log(`    -> Updated ${mods.length} modules with ${termLabel}`);
    }
  }

  console.log('\n========================================================================');
  console.log('SYLLABUS PARTITIONING & TAGGING COMPLETED SUCCESSFULLY!');
  console.log('========================================================================\n');
}

partitionAndTagSyllabi().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});

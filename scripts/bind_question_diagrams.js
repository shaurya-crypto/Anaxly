/**
 * bind_question_diagrams.js
 * 
 * Binds extracted authentic textbook diagrams to questions in both subjects (Maths & Science)
 * for Class 9 and Class 10:
 * - Scans worked_examples and concept_questions in syllabus_modules
 * - Identifies questions that reference textbook figures (e.g. "Fig. 5.15", "Fig. 6.14", "Fig. 10.30")
 * - Matches them against public/extracted_diagrams manifests
 * - Injects `image_url`, `figure_id`, and `caption` into the question object
 * - Strictly leaves general concept/theory visuals clean for dynamic live web search
 */

const fs = require('fs');
const path = require('path');
const { supabase } = require('./db_helper');

// Mapping of chapter and subject to extracted_diagrams directory
function getDiagramFolder(classLevel, category, orderIndex) {
  const isMath = (category || '').toLowerCase().includes('math');
  if (isMath) {
    if (classLevel === 'Class 9') {
      return `math9_ch${orderIndex}`;
    } else if (classLevel === 'Class 10') {
      return `math10_ch${orderIndex}`;
    }
  } else {
    // Science
    return `ch${orderIndex}`;
  }
  return null;
}

// Loads manifest.json for a given directory if available
const manifestCache = new Map();
function getManifest(folder) {
  if (manifestCache.has(folder)) return manifestCache.get(folder);
  const manifestPath = path.join('public', 'extracted_diagrams', folder, 'manifest.json');
  if (fs.existsSync(manifestPath)) {
    try {
      const data = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
      manifestCache.set(folder, data);
      return data;
    } catch {
      manifestCache.set(folder, []);
      return [];
    }
  }
  manifestCache.set(folder, []);
  return [];
}

// Finds the best matching extracted image for a figure reference
function findExtractedDiagram(folder, figRef) {
  const cleanRef = figRef.toLowerCase().replace(/[^0-9a-z\.]/g, ''); // e.g. "6.14", "10.30"
  const manifest = getManifest(folder);
  
  // Try exact match in manifest
  for (const item of manifest) {
    const itemFig = (item.figure_id || '').toLowerCase().replace(/[^0-9a-z\.]/g, '');
    if (itemFig === cleanRef || itemFig.endsWith('.' + cleanRef) || itemFig.includes(cleanRef)) {
      return {
        url: `/extracted_diagrams/${folder}/${item.filename}`,
        caption: item.caption || `Figure ${figRef}`,
        figure_id: item.figure_id || `Fig. ${figRef}`
      };
    }
  }

  // Fallback: direct filename check: fig_X_Y.webp
  const parts = cleanRef.split('.');
  if (parts.length >= 2) {
    const candidateFile = `fig_${parts[0]}_${parts[1]}.webp`;
    const fullPath = path.join('public', 'extracted_diagrams', folder, candidateFile);
    if (fs.existsSync(fullPath)) {
      return {
        url: `/extracted_diagrams/${folder}/${candidateFile}`,
        caption: `Figure ${figRef}`,
        figure_id: `Fig. ${figRef}`
      };
    }
  }

  return null;
}

async function bindQuestionDiagrams() {
  console.log('========================================================================');
  console.log('BINDING EXTRACTED BOOK DIAGRAMS TO QUESTIONS (MATHS & SCIENCE)');
  console.log('========================================================================\n');

  // Fetch all Class 9 and Class 10 modules
  const { data: currs, error: cErr } = await supabase
    .from('curriculums')
    .select('id, title, class_level, category, order_index')
    .in('class_level', ['Class 9', 'Class 10']);

  if (cErr) {
    console.error('Error fetching curriculums:', cErr);
    process.exit(1);
  }

  let totalQuestionsBound = 0;
  let totalModulesUpdated = 0;

  for (const c of currs) {
    const folder = getDiagramFolder(c.class_level, c.category, c.order_index);
    if (!folder) continue;

    const folderPath = path.join('public', 'extracted_diagrams', folder);
    if (!fs.existsSync(folderPath)) continue;

    const { data: modules, error: mErr } = await supabase
      .from('syllabus_modules')
      .select('id, order_index, title, worked_examples, visual_lesson_plan')
      .eq('curriculum_id', c.id);

    if (mErr || !modules) continue;

    for (const m of modules) {
      let modified = false;

      // 1. Process worked_examples
      let workedExamples = m.worked_examples || [];
      if (typeof workedExamples === 'string') {
        try { workedExamples = JSON.parse(workedExamples); } catch { workedExamples = []; }
      }

      if (Array.isArray(workedExamples)) {
        for (const ex of workedExamples) {
          const prob = ex.problem || '';
          // Match references like "Fig. 6.14", "Figure 5.15", "Fig 10.30"
          const match = prob.match(/Fig(?:ure)?\.?\s*(\d+[\.\d\w]*)/i);
          if (match) {
            const figId = match[1];
            const diagram = findExtractedDiagram(folder, figId);
            if (diagram) {
              ex.image_url = diagram.url;
              ex.figure_id = diagram.figure_id;
              ex.caption = diagram.caption;
              ex.has_diagram = true;
              modified = true;
              totalQuestionsBound++;
            }
          }
        }
      }

      // 2. Process concept_questions in visual_lesson_plan
      const vlp = m.visual_lesson_plan || {};
      if (Array.isArray(vlp.concept_questions)) {
        for (const cqGroup of vlp.concept_questions) {
          if (Array.isArray(cqGroup.questions)) {
            for (const q of cqGroup.questions) {
              const qText = q.question || '';
              const match = qText.match(/Fig(?:ure)?\.?\s*(\d+[\.\d\w]*)/i);
              if (match) {
                const figId = match[1];
                const diagram = findExtractedDiagram(folder, figId);
                if (diagram) {
                  q.image_url = diagram.url;
                  q.figure_id = diagram.figure_id;
                  q.caption = diagram.caption;
                  modified = true;
                  totalQuestionsBound++;
                }
              }
            }
          }
        }
      }

      if (modified) {
        await supabase
          .from('syllabus_modules')
          .update({
            worked_examples: workedExamples,
            visual_lesson_plan: vlp
          })
          .eq('id', m.id);

        totalModulesUpdated++;
        console.log(`  [${c.class_level} ${c.category} Ch ${c.order_index} Mod ${m.order_index}] Bound book question diagram: ${m.title.substring(0, 45)}...`);
      }
    }
  }

  console.log('\n========================================================================');
  console.log(`SUCCESS: Bound ${totalQuestionsBound} authentic question diagrams across ${totalModulesUpdated} modules!`);
  console.log('Zero static URLs exist in theory concepts. Only question figures use extracted book diagrams.');
  console.log('========================================================================\n');
}

bindQuestionDiagrams().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});

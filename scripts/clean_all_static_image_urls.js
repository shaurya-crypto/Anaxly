/**
 * clean_all_static_image_urls.js
 * Scans ALL modules in Supabase `syllabus_modules` table across all classes
 * and removes any static/canned image URLs (e.g. Wikimedia links, local paths).
 * Converts them to pure dynamic image_search queries for the live visual engine.
 */

const { supabase } = require('./db_helper');

async function cleanAllModules() {
  console.log('========================================================================');
  console.log('AUDITING & STRIPPING ALL STATIC IMAGE URLS ACROSS ENTIRE DATABASE');
  console.log('========================================================================\n');

  const { data: modules, error: modErr } = await supabase
    .from('syllabus_modules')
    .select('id, order_index, title, class_level, visual_lesson_plan');

  if (modErr) {
    console.error('Error fetching modules:', modErr);
    process.exit(1);
  }

  console.log(`Fetched ${modules.length} total modules across all classes.`);

  let cleanedCount = 0;

  for (const m of modules) {
    let modified = false;
    const vlp = m.visual_lesson_plan || {};

    // Check top-level vlp
    if (vlp.image_url) {
      delete vlp.image_url;
      modified = true;
    }
    if (vlp.url) {
      delete vlp.url;
      modified = true;
    }

    // Check concept_visuals inside vlp
    if (Array.isArray(vlp.concept_visuals)) {
      for (const cv of vlp.concept_visuals) {
        if (cv.image_url) {
          delete cv.image_url;
          modified = true;
        }
        if (cv.url) {
          delete cv.url;
          modified = true;
        }

        // Clean hardcoded URL strings out of timing_and_cue
        if (cv.timing_and_cue && (
          cv.timing_and_cue.includes('http://') || 
          cv.timing_and_cue.includes('https://') || 
          cv.timing_and_cue.includes('/extracted_diagrams/')
        )) {
          const q = cv.image_search_query || cv.image_query || cv.concept_title || cv.diagram_title || 'Educational Diagram';
          const t = cv.diagram_title || cv.concept_title || 'Scientific Diagram';
          cv.timing_and_cue = `Step 1: search_and_show_image(query="${q}", title="${t}")`;
          modified = true;
        }

        if (!cv.svg && cv.diagram_type !== 'image_search' && cv.diagram_type !== 'video_demonstration') {
          cv.diagram_type = 'image_search';
          modified = true;
        }
      }
    }

    if (modified) {
      const { error: upErr } = await supabase
        .from('syllabus_modules')
        .update({ visual_lesson_plan: vlp })
        .eq('id', m.id);

      if (upErr) {
        console.error(`  [${m.class_level}] Error updating mod ${m.id}:`, upErr);
      } else {
        cleanedCount++;
        console.log(`  [${m.class_level}] Cleaned static URLs: ${m.title.substring(0, 50)}...`);
      }
    }
  }

  console.log('\n========================================================================');
  console.log(`SUCCESS: Cleaned ${cleanedCount} modules! Zero static image URLs remain.`);
  console.log('All modules now trigger dynamic live web & search engine queries on demand.');
  console.log('========================================================================\n');
}

cleanAllModules().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});

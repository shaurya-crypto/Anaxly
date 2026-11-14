/**
 * clean_supabase_image_urls.js
 * Strips all static/canned image URLs (Unsplash, static Wikimedia links) from
 * Class 11 Physics modules in Supabase `syllabus_modules` table.
 * Preserves dynamic `image_search_query` so the live tutor searches online.
 */

const { supabase } = require('./db_helper');

async function cleanSupabaseModules() {
  console.log('========================================================================');
  console.log('STRIPPING STATIC IMAGE URLS FROM SUPABASE (CLASS 11 PHYSICS MODULES)');
  console.log('========================================================================\n');

  // 1. Fetch Class 11 Physics curriculums
  const { data: curriculums, error: currErr } = await supabase
    .from('curriculums')
    .select('id, order_index, title')
    .eq('class_level', 'Class 11')
    .eq('category', 'Physics');

  if (currErr) {
    console.error('Error fetching curriculums:', currErr);
    process.exit(1);
  }

  const currIds = curriculums.map(c => c.id);
  console.log(`Found ${currIds.length} Physics Curriculums. Fetching modules...`);

  // 2. Fetch all modules
  const { data: modules, error: modErr } = await supabase
    .from('syllabus_modules')
    .select('id, order_index, title, visual_lesson_plan')
    .in('curriculum_id', currIds);

  if (modErr) {
    console.error('Error fetching modules:', modErr);
    process.exit(1);
  }

  console.log(`Auditing ${modules.length} Modules for static image URLs...\n`);

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
        if (!cv.svg && cv.diagram_type !== 'image_search') {
          cv.diagram_type = 'image_search';
          modified = true;
        }
      }
    }

    if (modified) {
      const { error: updateErr } = await supabase
        .from('syllabus_modules')
        .update({
          visual_lesson_plan: vlp
        })
        .eq('id', m.id);

      if (updateErr) {
        console.error(`  [Mod ${m.order_index}] Error updating:`, updateErr);
      } else {
        cleanedCount++;
        console.log(`  [Mod ${m.order_index.toString().padStart(2)}] Cleaned static image URLs: ${m.title.substring(0, 48)}...`);
      }
    }
  }

  console.log('\n========================================================================');
  console.log(`AUDIT COMPLETE: Cleaned ${cleanedCount} of ${modules.length} Modules in Supabase!`);
  console.log('All modules now rely 100% on dynamic online search for images and videos.');
  console.log('========================================================================\n');

  process.exit(0);
}

cleanSupabaseModules().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});

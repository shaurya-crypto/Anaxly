const { supabase } = require('./db_helper');

async function auditVisualsAndGraphs() {
  const { data: curriculums } = await supabase
    .from('curriculums')
    .select('id, order_index, title')
    .eq('class_level', 'Class 11')
    .eq('category', 'Physics')
    .order('order_index');

  const currIds = curriculums.map(c => c.id);
  const { data: modules } = await supabase
    .from('syllabus_modules')
    .select('id, curriculum_id, order_index, title, visual_lesson_plan')
    .in('curriculum_id', currIds)
    .order('order_index');

  for (const c of curriculums) {
    const chMods = modules.filter(m => m.curriculum_id === c.id);
    let svgCount = 0;
    let graphCount = 0;
    let imageQueryCount = 0;
    let videoQueryCount = 0;

    for (const m of chMods) {
      const vlp = m.visual_lesson_plan || {};
      const s = JSON.stringify(vlp);
      if (vlp.svg || s.includes('<svg')) svgCount++;
      if (s.includes('plot_mathematical_graph') || s.includes('Mafs') || s.includes('graph_type') || s.includes('formula') || s.includes('segments') || s.includes('vectors')) graphCount++;
      if (s.includes('image_search_query') || s.includes('search_and_show_image') || (vlp.concept_visuals && vlp.concept_visuals.some(cv => cv.search_query || cv.image_search_query))) imageQueryCount++;
      if (s.includes('video_search_query') || s.includes('search_and_show_video') || (vlp.concept_visuals && vlp.concept_visuals.some(cv => cv.video_search_query))) videoQueryCount++;
    }

    console.log(`Ch ${String(c.order_index).padStart(2)}: ${c.title.padEnd(45)} | SVGs: ${svgCount}/${chMods.length} | Graphs: ${graphCount}/${chMods.length} | ImgQuery: ${imageQueryCount}/${chMods.length} | VidQuery: ${videoQueryCount}/${chMods.length}`);
  }
}

auditVisualsAndGraphs();
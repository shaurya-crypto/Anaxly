const { supabase } = require('./db_helper');

async function auditClass11Maths() {
  const { data: chapters, error } = await supabase
    .from('curriculums')
    .select('id, title, class_level, category, order_index')
    .ilike('class_level', '%11%')
    .ilike('category', '%math%')
    .order('order_index', { ascending: true });

  if (error) {
    console.error('Error fetching Class 11 Maths chapters:', error);
    return;
  }

  console.log(`Found ${chapters.length} Class 11 Maths chapters in DB:\n`);
  for (const ch of chapters) {
    const { data: modules, error: modErr } = await supabase
      .from('syllabus_modules')
      .select('id, title, order_index, worked_examples, quiz_questions, key_concepts, subtopics')
      .eq('curriculum_id', ch.id)
      .order('order_index', { ascending: true });

    if (modErr) {
      console.error(`Error fetching modules for ${ch.title}:`, modErr);
      continue;
    }

    let totalExamples = 0;
    let totalQuizzes = 0;
    let totalConcepts = 0;

    for (const m of modules || []) {
      const examples = Array.isArray(m.worked_examples) ? m.worked_examples : (typeof m.worked_examples === 'string' ? JSON.parse(m.worked_examples || '[]') : []);
      const quizzes = Array.isArray(m.quiz_questions) ? m.quiz_questions : (typeof m.quiz_questions === 'string' ? JSON.parse(m.quiz_questions || '[]') : []);
      const concepts = Array.isArray(m.key_concepts) ? m.key_concepts : (typeof m.key_concepts === 'string' ? JSON.parse(m.key_concepts || '[]') : []);
      totalExamples += examples.length;
      totalQuizzes += quizzes.length;
      totalConcepts += concepts.length;
    }

    console.log(`[Ch ${ch.order_index}] "${ch.title}": ${modules?.length || 0} modules | ${totalConcepts} concepts | ${totalExamples} worked examples | ${totalQuizzes} quiz Qs`);
    if (modules && modules.length > 0) {
      for (const m of modules) {
        const examples = Array.isArray(m.worked_examples) ? m.worked_examples : (typeof m.worked_examples === 'string' ? JSON.parse(m.worked_examples || '[]') : []);
        console.log(`   - Mod ${m.order_index}: "${m.title}" (${examples.length} examples)`);
      }
    }
    console.log('');
  }
}

auditClass11Maths();

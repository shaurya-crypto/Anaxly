const fs = require('fs');
const env = fs.readFileSync('.env.local', 'utf8').split('\n').reduce((acc, line) => {
  const [k, ...v] = line.split('=');
  if (k && v.length) acc[k.trim()] = v.join('=').trim().replace(/^["']|["']$/g, '');
  return acc;
}, {});
const { createClient } = require('@supabase/supabase-js');
const supabase = createClient(env.NEXT_PUBLIC_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY || env.NEXT_PUBLIC_SUPABASE_ANON_KEY);

async function update() {
  const modId = '87eceed1-83b3-43ad-8cdd-c17b7277b86d';
  const { data: mod, error } = await supabase
    .from('syllabus_modules')
    .select('visual_lesson_plan')
    .eq('id', modId)
    .single();

  if (error || !mod) {
    console.error('Fetch error:', error);
    return;
  }

  const vPlan = mod.visual_lesson_plan || {};
  vPlan.diagram_type = 'graph';
  vPlan.interactive_math_formula = 'x^2 - 3x - 4';

  if (Array.isArray(vPlan.concept_visuals) && vPlan.concept_visuals.length > 0) {
    vPlan.concept_visuals[0].diagram_type = 'graph';
    vPlan.concept_visuals[0].visual_type = 'graph';
    vPlan.concept_visuals[0].interactive_math_formula = 'x^2 - 3x - 4';
    vPlan.concept_visuals[0].mafs_config = {
      formula: 'x^2 - 3x - 4',
      domain: [-4, 6],
      range: [-8, 8],
      title: 'Geometrical Zeroes of Quadratic Polynomial: y = x² - 3x - 4',
      callout: 'Zeroes at x = -1, 4',
      points: [
        { x: -1, y: 0, label: '(-1, 0)' },
        { x: 4, y: 0, label: '(4, 0)' },
        { x: 1.5, y: -6.25, label: 'Vertex (1.5, -6.25)' }
      ]
    };
  }

  if (Array.isArray(vPlan.steps)) {
    vPlan.steps = vPlan.steps.map((st) => {
      if (st.type === 'GRAPH') {
        return {
          ...st,
          boardDirective: {
            action: 'plot_mathematical_graph',
            content: 'formula=x^2 - 3x - 4 | domain=[-4, 6] | range=[-8, 8] | title=Geometrical Zeroes of Quadratic Polynomial: y = x² - 3x - 4 | callout=Zeroes at x = -1, 4',
          },
          content: {
            ...st.content,
            graph: {
              title: 'Geometrical Zeroes of Quadratic Polynomial: y = x² - 3x - 4',
              expression: 'y = x^2 - 3x - 4',
              domain: [-4, 6],
              range: [-8, 8],
              xLabel: 'x',
              yLabel: 'y',
              graphType: 'function',
            }
          }
        };
      }
      return st;
    });
  }

  const { error: updateErr } = await supabase
    .from('syllabus_modules')
    .update({ visual_lesson_plan: vPlan })
    .eq('id', modId);

  if (updateErr) {
    console.error('Update error:', updateErr);
  } else {
    console.log('Successfully updated Chapter 2 Module 2 with explicit plot_mathematical_graph Mafs directive!');
  }
}

update();

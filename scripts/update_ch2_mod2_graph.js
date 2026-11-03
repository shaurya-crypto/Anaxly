const fs = require('fs');
const env = fs.readFileSync('.env.local', 'utf8').split('\n').reduce((acc, line) => {
  const [k, ...v] = line.split('=');
  if (k && v.length) acc[k.trim()] = v.join('=').trim().replace(/^["']|["']$/g, '');
  return acc;
}, {});
const { createClient } = require('@supabase/supabase-js');
const supabase = createClient(env.NEXT_PUBLIC_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY || env.NEXT_PUBLIC_SUPABASE_ANON_KEY);

const animatedGraphSvg = `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <defs>
    <style>
      @keyframes pulseZero {
        0%, 100% { r: 5px; opacity: 1; stroke-width: 1.5px; }
        50% { r: 12px; opacity: 0.15; stroke-width: 3px; }
      }
      @keyframes flowDash {
        to { stroke-dashoffset: -16px; }
      }
      @keyframes auraGlow {
        0%, 100% { filter: drop-shadow(0 0 3px rgba(37,99,235,0.6)); }
        50% { filter: drop-shadow(0 0 8px rgba(37,99,235,0.9)); }
      }
      .pulse-ring { animation: pulseZero 2s ease-in-out infinite; stroke: #DC2626; fill: none; }
      .flowing-axis { stroke-dasharray: 5,4; animation: flowDash 1.8s linear infinite; }
      .tracer-dot { animation: auraGlow 2s ease-in-out infinite; }
      .label-text { font-family: 'JetBrains Mono', 'Segoe UI', system-ui, sans-serif; }
    </style>
    
    <!-- Coordinate Grid Pattern -->
    <pattern id="cartesianGrid" width="35" height="24" patternUnits="userSpaceOnUse">
      <path d="M 35 0 L 0 0 0 24" fill="none" stroke="#F1F5F9" stroke-width="0.8"/>
    </pattern>

    <!-- Arrow Marker for Axes -->
    <marker id="axisArrow" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">
      <polygon points="0 1, 5 3, 0 5" fill="#0F172A" />
    </marker>
  </defs>

  <!-- Clean White Chalkboard Canvas -->
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>

  <!-- Top Header Pill Badge -->
  <rect x="90" y="10" width="360" height="22" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="25" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold" class="label-text">GEOMETRICAL ZEROES OF p(x) = x² - 3x - 4</text>

  <!-- ================= CARTESIAN GRAPH VIEWPORT ================= -->
  <g transform="translate(10, 36)">
    <!-- Graph Background Grid -->
    <rect x="6" y="6" width="374" height="220" rx="6" fill="url(#cartesianGrid)" stroke="#E2E8F0" stroke-width="1"/>

    <!-- Axis of Symmetry x = 1.5 (Flowing Dashes) -->
    <line x1="252.5" y1="12" x2="252.5" y2="220" stroke="#D97706" stroke-width="1.5" class="flowing-axis"/>
    <text x="252.5" y="24" fill="#D97706" font-size="8.5" font-weight="bold" text-anchor="middle" class="label-text">x = 1.5 (Axis of Symmetry)</text>

    <!-- X-Axis (y = 0 at Y = 160) -->
    <line x1="16" y1="160" x2="370" y2="160" stroke="#0F172A" stroke-width="1.6" marker-end="url(#axisArrow)"/>
    <text x="368" y="152" fill="#0F172A" font-size="10" font-weight="bold" class="label-text">X</text>
    <text x="24" y="152" fill="#64748B" font-size="9" class="label-text">X'</text>

    <!-- Y-Axis (x = 0 at X = 200) -->
    <line x1="200" y1="220" x2="200" y2="12" stroke="#0F172A" stroke-width="1.6" marker-end="url(#axisArrow)"/>
    <text x="206" y="20" fill="#0F172A" font-size="10" font-weight="bold" class="label-text">Y</text>
    <text x="206" y="216" fill="#64748B" font-size="9" class="label-text">Y'</text>

    <!-- Origin O (0,0) -->
    <text x="192" y="174" fill="#64748B" font-size="9" font-weight="600" class="label-text">O</text>

    <!-- Tick Marks on X-Axis -->
    <!-- -2 --> <line x1="130" y1="157" x2="130" y2="163" stroke="#64748B" stroke-width="1"/>
    <text x="130" y="173" fill="#64748B" font-size="8" text-anchor="middle" class="label-text">-2</text>
    <!-- -1 --> <line x1="165" y1="157" x2="165" y2="163" stroke="#64748B" stroke-width="1"/>
    <!-- 1 --> <line x1="235" y1="157" x2="235" y2="163" stroke="#64748B" stroke-width="1"/>
    <text x="235" y="173" fill="#64748B" font-size="8" text-anchor="middle" class="label-text">1</text>
    <!-- 2 --> <line x1="270" y1="157" x2="270" y2="163" stroke="#64748B" stroke-width="1"/>
    <text x="270" y="173" fill="#64748B" font-size="8" text-anchor="middle" class="label-text">2</text>
    <!-- 3 --> <line x1="305" y1="157" x2="305" y2="163" stroke="#64748B" stroke-width="1"/>
    <text x="305" y="173" fill="#64748B" font-size="8" text-anchor="middle" class="label-text">3</text>
    <!-- 4 --> <line x1="340" y1="157" x2="340" y2="163" stroke="#64748B" stroke-width="1"/>
    <!-- 5 --> <line x1="375" y1="157" x2="375" y2="163" stroke="#64748B" stroke-width="1"/>

    <!-- Continuous Parabola Curve y = x² - 3x - 4 -->
    <path id="parabolaPath" d="M 116,52 Q 252.5,418 389,52" fill="none" stroke="#2563EB" stroke-width="2.6" stroke-linecap="round"/>

    <!-- Y-Intercept (0, -4) -->
    <circle cx="200" cy="208" r="3.5" fill="#64748B"/>
    <text x="194" y="210" fill="#64748B" font-size="8" text-anchor="end" class="label-text">(0, -4)</text>

    <!-- Parabola Vertex (1.5, -6.25) -->
    <circle cx="252.5" cy="235" r="4.5" fill="#D97706"/>
    <text x="252.5" y="248" fill="#D97706" font-size="8.5" font-weight="bold" text-anchor="middle" class="label-text">Vertex (1.5, -6.25)</text>

    <!-- ZERO 1: (-1, 0) with Pulsing Rings -->
    <circle cx="165" cy="160" r="12" class="pulse-ring"/>
    <circle cx="165" cy="160" r="5" fill="#DC2626"/>
    <rect x="120" y="128" width="56" height="18" rx="4" fill="#FEE2E2" stroke="#FCA5A5" stroke-width="0.8"/>
    <text x="148" y="141" fill="#DC2626" font-size="9" font-weight="bold" text-anchor="middle" class="label-text">(-1, 0)</text>
    <polyline points="148,146 160,156 165,160" fill="none" stroke="#DC2626" stroke-width="1"/>

    <!-- ZERO 2: (4, 0) with Pulsing Rings -->
    <circle cx="340" cy="160" r="12" class="pulse-ring"/>
    <circle cx="340" cy="160" r="5" fill="#DC2626"/>
    <rect x="335" y="128" width="52" height="18" rx="4" fill="#FEE2E2" stroke="#FCA5A5" stroke-width="0.8"/>
    <text x="361" y="141" fill="#DC2626" font-size="9" font-weight="bold" text-anchor="middle" class="label-text">(4, 0)</text>
    <polyline points="361,146 345,156 340,160" fill="none" stroke="#DC2626" stroke-width="1"/>

    <!-- DYNAMIC MOVING TRACE POINT GLIDING ALONG THE PARABOLA -->
    <g class="tracer-dot">
      <circle r="6" fill="#2563EB" stroke="#FFFFFF" stroke-width="2">
        <animateMotion path="M 116,52 Q 252.5,418 389,52" dur="4.5s" repeatCount="indefinite" />
      </circle>
      <circle r="11" fill="none" stroke="#2563EB" stroke-width="1.2" opacity="0.6">
        <animateMotion path="M 116,52 Q 252.5,418 389,52" dur="4.5s" repeatCount="indefinite" />
      </circle>
    </g>
  </g>

  <!-- ================= RIGHT SIDE: PEDAGOGICAL HUD CARD ================= -->
  <g transform="translate(396, 42)">
    <rect x="0" y="0" width="134" height="220" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.2"/>
    
    <!-- Card Title -->
    <rect x="8" y="8" width="118" height="20" rx="4" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="0.8"/>
    <text x="67" y="22" fill="#1E40AF" font-size="9" font-weight="bold" text-anchor="middle" class="label-text">GEOMETRICAL RULE</text>

    <text x="10" y="44" fill="#0F172A" font-size="8.5" font-weight="bold" class="label-text">Zeroes = X-Intercepts</text>
    <text x="10" y="58" fill="#64748B" font-size="7.5" class="label-text">x-coordinates where curve</text>
    <text x="10" y="68" fill="#64748B" font-size="7.5" class="label-text">crosses y = 0.</text>

    <!-- Factorisation Box -->
    <rect x="8" y="78" width="118" height="42" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.8"/>
    <text x="14" y="93" fill="#0F172A" font-size="8" font-family="'JetBrains Mono'" font-weight="bold">p(x) = x² - 3x - 4</text>
    <text x="14" y="106" fill="#16A34A" font-size="8" font-family="'JetBrains Mono'" font-weight="bold">= (x + 1)(x - 4)</text>
    <text x="14" y="117" fill="#DC2626" font-size="7.5" font-family="'JetBrains Mono'" font-weight="bold">⇒ x = -1,  x = 4</text>

    <!-- Case Status Indicator -->
    <rect x="8" y="126" width="118" height="40" rx="4" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="0.8"/>
    <text x="67" y="140" fill="#065F46" font-size="8.5" font-weight="bold" text-anchor="middle" class="label-text">CASE (i): D &gt; 0</text>
    <text x="67" y="152" fill="#047857" font-size="8" text-anchor="middle" class="label-text">Discriminant D = 25</text>
    <text x="67" y="162" fill="#047857" font-size="8" font-weight="bold" text-anchor="middle" class="label-text">2 Distinct Real Zeroes</text>

    <!-- Upward Parabola Tag -->
    <rect x="8" y="172" width="118" height="38" rx="4" fill="#FFFBEB" stroke="#FDE68A" stroke-width="0.8"/>
    <text x="67" y="186" fill="#92400E" font-size="8" font-weight="bold" text-anchor="middle" class="label-text">Orientation (a = 1 &gt; 0)</text>
    <text x="67" y="198" fill="#B45309" font-size="8" text-anchor="middle" class="label-text">Parabola Opens Upwards</text>
    <text x="67" y="207" fill="#D97706" font-size="10" font-weight="bold" text-anchor="middle">∪</text>
  </g>
</svg>`;

async function updateModule() {
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
  vPlan.diagram_svg = animatedGraphSvg;
  vPlan.diagram_type = 'graph';
  vPlan.interactive_math_formula = 'x^2 - 3x - 4';
  vPlan.refined_by_tier2 = true;
  vPlan.tier2_refined_at = new Date().toISOString();

  if (Array.isArray(vPlan.concept_visuals) && vPlan.concept_visuals.length > 0) {
    vPlan.concept_visuals[0] = {
      ...vPlan.concept_visuals[0],
      concept_title: 'Geometrical Definition: The zeroes of p(x) are the x-coordinates of the points where graph of y = p(x) intersects the x-axis',
      diagram_title: 'Geometrical Zeroes of Quadratic Polynomial: y = x² - 3x - 4',
      svg: animatedGraphSvg,
      diagram_svg: animatedGraphSvg,
      diagram_type: 'graph',
      visual_type: 'graph',
      animation_type: 'moving_trace_point_and_pulsing_zeroes',
      interactive_math_formula: 'x^2 - 3x - 4',
      refined_by_tier2: true,
      tier2_refined_at: new Date().toISOString(),
      what_to_make: 'Cartesian coordinate graph of y = x² - 3x - 4 with animated moving tracer dot along the parabola, pulsing concentric rings on roots (-1,0) and (4,0), and flowing axis of symmetry x = 1.5',
      what_to_explain: 'Explain that the zeroes of p(x) are the points where the moving point crosses the x-axis (y = 0), namely x = -1 and x = 4.',
      why_needed: 'Visualizes the fundamental definition of zeroes of a polynomial using a dynamic, moving coordinate parabola.',
    };
  }

  if (Array.isArray(vPlan.steps)) {
    vPlan.steps = vPlan.steps.map((st) => {
      if (st.type === 'GRAPH' || st.type === 'DIAGRAM') {
        return {
          ...st,
          content: {
            ...st.content,
            diagram: {
              ...(st.content?.diagram || {}),
              svg: animatedGraphSvg,
            },
            graph: {
              ...(st.content?.graph || {}),
              expression: 'y = x^2 - 3x - 4',
              domain: [-4, 6],
              range: [-8, 8],
            },
          },
          boardDirective: {
            action: 'render_svg_diagram',
            content: `Geometrical Zeroes of Quadratic Polynomial: y = x² - 3x - 4 | ${animatedGraphSvg} | Coordinates where curve crosses x-axis`,
          },
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
    console.log('Successfully updated Chapter 2 Concept 2 with dynamic animated graph in Supabase!');
  }
}

updateModule();

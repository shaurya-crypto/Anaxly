import { GoogleGenAI } from '@google/genai'
import { resilientGenerateContent } from '@/lib/geminiResilientGenerate'

export interface RefineDiagramInput {
  title: string
  domain?: string
  subject?: string
  classLevel?: string
  context?: string
  existingSvg?: string
  whyNeeded?: string
  whatToExplain?: string
  whatToMake?: string
  refinementPrompt?: string
  visualType?: 'diagram' | 'graph' | 'animation' | 'image' | string
  animationType?: string
  interactiveMathFormula?: string
  isLiveClass?: boolean
  source?: string
}

export interface RefinedDiagramResult {
  title: string
  svg: string
  caption: string
  why_needed: string
  what_to_explain: string
  what_to_make?: string
  visual_type?: string
  interactive_math_formula?: string
  refined_by_tier2: boolean
  tier2_refined_at: string
  modelUsed?: string
}

const TIER2_SYSTEM_INSTRUCTION = `You are a World-Class Academic Textbook Illustrator & Senior Vector Graphic Designer for elite scholastic platforms (Aristotle, Gauth, Desmos).
Your ONLY task is to generate or refine authentic, publication-grade, ultra-detailed vector SVG educational visualizations (images, diagrams, animations, and mathematical graphs).

CRITICAL VECTOR DESIGN SPECIFICATIONS (WHITE CHALKBOARD / ARISTOTLE & GAUTH BENCHMARK):
1. CANVAS & CLEAN WHITE CHALKBOARD THEME (MANDATORY):
   - Must use viewBox="0 0 540 280" and xmlns="http://www.w3.org/2000/svg".
   - Include shape-rendering="geometricPrecision" and text-rendering="geometricPrecision".
   - PURE CLEAN WHITE BACKGROUND (EXACTLY MATCHING THE WHITE CHALKBOARD):
     * Canvas backdrop: <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
     * NEVER use dark green (#13211B) or dark blue! The background MUST be clean white (#FFFFFF) so it seamlessly blends into the white whiteboard!
     * Subtle coordinate graph grid: stroke="#F1F5F9" stroke-width="0.75"
     * Header pill badge at top center: <rect x="110" y="12" width="320" height="22" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/> with <text x="270" y="27" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold" font-family="'JetBrains Mono', 'Segoe UI', system-ui, sans-serif">
   - Clean Scholastic Palette on White:
     * Deep Charcoal / Ink: #0F172A (axes, primary text, formulas)
     * Aristotle Royal Blue: #2563EB (primary vectors, forward paths, active layers)
     * Scholar Emerald Green: #16A34A (motion curves, biological tissues, positive gradients)
     * Crimson / Coral Red: #DC2626 (return paths, nuclei, critical focus points)
     * Warm Chalk Amber / Orange: #D97706 or #F59E0B (actual distance arcs, secondary layers)
     * Muted Slate Gray: #64748B (tick labels, annotations, subtitles)
     * Pointer Leader lines: stroke="#94A3B8" with target dots fill="#2563EB"
   - Fonts: 'JetBrains Mono', 'Segoe UI', system-ui, sans-serif

2. SMART DUAL-SIDED CALLOUT & POINTER SYSTEM:
   - Distribute labels symmetrically (Left and Right sides) with ample spacing.
   - EXACT POINTER TARGET ACCURACY:
     * Small solid circle dot <circle cx="..." cy="..." r="2.5" fill="#2563EB"/> located PRECISELY at the feature.
     * Clean connecting leader line: <polyline points="targetX,targetY elbowX,targetY labelX,labelY" fill="none" stroke="#94A3B8" stroke-width="1"/>
     * Never point to empty space!
   - NO TEXT OVERLAPPING: Minimum 22px vertical separation between adjacent text lines.
   - Labels on the right side: anchor at x >= 400 (text-anchor="start").
   - Labels on the left side: anchor at x <= 140 (text-anchor="end").

3. UNIVERSAL VISUAL MODALITY CAPABILITIES & MANDATORY DYNAMIC MOTION:
   - MANDATORY CSS ANIMATIONS & DYNAMIC MOTION (STRICTLY REQUIRED FOR EVERY VISUALISATION):
     * Every SVG MUST contain an internal <defs><style>...</style></defs> block with fluid, performant CSS animations (@keyframes) or SVG <animate>/<animateMotion>.
     * Completely static SVGs without motion are strictly forbidden.
     * Specific animation requirements by visual type:
       a) Mathematical & Kinematic Graphs:
          - MOVING TRACE POINT: An animated point marker (<circle>) that continuously glides along the plotted curve/parabola/line using <animateMotion path="..." dur="4s" repeatCount="indefinite" /> or CSS translation.
          - PULSING ZEROES / INTERCEPT RINGS: Key roots, intercepts, extrema, and vertices MUST have breathing/pulsing concentric rings (@keyframes pulseZero { 0%, 100% { r: 5; opacity: 0.9; } 50% { r: 9; opacity: 0.25; } }).
          - FLOWING DASHES: Axis of symmetry, asymptotes, or projection lines MUST have animated dash offset (@keyframes flowDash { to { stroke-dashoffset: -16; } }).
       b) Physics & Chemical Processes:
          - Electric current & electron flow: animated dashed lines (stroke-dasharray="6,4", animation: flowDash 1.5s linear infinite).
          - Ray optics & wave propagation: moving wave fronts or harmonic marker beads.
          - Particle trajectories: smooth translation along motion paths.
       c) Biological & Anatomical ultrastructures:
          - Pulsing glow on vital focus regions (organelles, shoot/root apical meristems, articulating nodes).
          - Directional nutrient or signaling transport pulses along vascular or pathway tracks.
       d) Flowcharts & Algorithmic Deductions:
          - Animated pulses traveling along connecting arrows from premise to conclusion.
     * Keep animations smooth, lightweight, and strictly self-contained (no external JavaScript).
   - MATHEMATICAL & KINEMATIC FUNCTION GRAPHS (Desmos & Aristotle Benchmark):
     * Balanced Cartesian grid with numbered tick marks and coordinate labels.
     * Accurately plotted function curves (parabolas, linear functions, sine curves, velocity-time slopes).
     * Marked intercepts, extrema, roots, and slope triangles (Delta y / Delta x).
     * Clear algebraic formula callout badge (e.g. y = x^2 - 3x - 4 or v(t) = u + at).

4. STRICT VISUAL-ONLY INVARIANT:
   - You refine and generate ONLY the visual graphic vector markup (<svg>).
   - NEVER generate, replace, or alter narrative curriculum content, chapter notes, definitions, exercises, or questions.
   - Output ONLY the raw <svg viewBox="0 0 540 280" ...>...</svg> element.
   - NEVER wrap in markdown code fences (\`\`\`xml or \`\`\`svg).
   - Output must be 100% valid XML with closing </svg>.`

/**
 * Core Tier 2 Vector Engine: Generates or refines an educational vector SVG
 * using Gemini with high-thinking budget and multi-model failover cascade.
 */
export async function generateOrRefineDiagramWithTier2(
  input: RefineDiagramInput
): Promise<RefinedDiagramResult> {
  const apiKey = process.env.GEMINI_API_KEY
  if (!apiKey) {
    throw new Error('GEMINI_API_KEY is not configured in environment.')
  }

  const ai = new GoogleGenAI({ apiKey })
  const isRefinement = Boolean(input.existingSvg && input.existingSvg.includes('<svg'))

  const userPromptText = isRefinement
    ? `You are refining this existing educational visual asset to Aristotle/Gauth publication grade:
Title: "${input.title}"
Subject: "${input.subject || 'Science'}" (Grade: ${input.classLevel || 'Class 9/10'})
Context / Concept: "${input.context || input.title}"
Visual Modality: "${input.visualType || 'diagram'}"
${input.animationType ? `Animation Requirement: "${input.animationType}"` : ''}
${input.interactiveMathFormula ? `Mathematical Function to Plot: "${input.interactiveMathFormula}"` : ''}
${input.whyNeeded ? `Pedagogical Reason (Why Needed): "${input.whyNeeded}"` : ''}
${input.whatToExplain ? `Points to Explain: "${input.whatToExplain}"` : ''}
${input.whatToMake ? `What to Make / Elements to draw: "${input.whatToMake}"` : ''}
${input.refinementPrompt ? `Special Refinement Directive: "${input.refinementPrompt}"` : ''}

EXISTING INITIAL SVG TO REFINE:
${input.existingSvg}

REFINEMENT INSTRUCTIONS:
- Retain the pedagogical concept while dramatically elevating vector draftsmanship, precision curves, anatomical or geometric accuracy, and clean symmetrical callouts.
- MANDATORY CSS ANIMATION INVARIANT: You MUST incorporate fluid CSS keyframe animations (<style>@keyframes ...</style>) into the SVG:
  * If a graph: include a moving/tracing point (<circle>) traveling along the curve, breathing/pulsing concentric rings at zeroes/intercepts/roots, and flowing dashed lines for symmetry axes.
  * If a process or system: include flowing dashed lines, pulsing focus points, and motion paths.
  * Completely static SVGs without animation are strictly forbidden.
- If the visual is a graph or function plot, accurately plot the coordinate plane, labeled ticks, curves, intercepts, and equation badge.
- Refine ONLY the visual graphic markup. Do NOT generate or alter narrative notes or curriculum text.
- Keep the background pure white (#FFFFFF).
- Return ONLY the updated raw <svg viewBox="0 0 540 280" ...>...</svg> element.`
    : `Generate an authentic publication-grade educational vector SVG visualization for:
Title: "${input.title}"
${input.domain || input.subject ? `Domain / Discipline: "${input.domain || input.subject}"` : ''}
${input.classLevel ? `Grade Level: "${input.classLevel}"` : ''}
Context: "${input.context || input.title}"
${input.visualType ? `Visual Modality: "${input.visualType}"` : ''}
${input.animationType ? `Animation Requirement: "${input.animationType}"` : ''}
${input.interactiveMathFormula ? `Mathematical Function to Plot: "${input.interactiveMathFormula}"` : ''}
${input.whyNeeded ? `Why Needed: "${input.whyNeeded}"` : ''}
${input.whatToExplain ? `What to Explain: "${input.whatToExplain}"` : ''}
${input.whatToMake ? `What to Make: "${input.whatToMake}"` : ''}

MANDATORY CSS ANIMATION INVARIANT:
- You MUST incorporate fluid CSS keyframe animations (<style>@keyframes ...</style>) into the SVG (moving/tracing point along curve, pulsing rings at critical zeroes/roots, flowing dashed strokes).
- Completely static drawings without motion are strictly forbidden.
- Refine ONLY the visual graphic markup. Do NOT generate or alter narrative notes or curriculum text.
- Return ONLY the raw <svg viewBox="0 0 540 280" ...>...</svg> element with pure white (#FFFFFF) chalkboard canvas.`

  const isLive = Boolean(input.isLiveClass || input.source === 'live_classroom')
  const preferredModels = isLive
    ? ['gemini-2.5-flash', 'gemini-3.5-flash']
    : undefined
  const timeoutMs = isLive ? 30000 : 90000
  const thinkingBudget = isLive ? 1024 : 2048

  const { text: rawOutput, modelUsed } = await resilientGenerateContent(ai, {
    contents: [{ role: 'user', parts: [{ text: userPromptText }] }],
    preferredModels,
    maxRounds: isLive ? 1 : 2,
    config: {
      systemInstruction: TIER2_SYSTEM_INSTRUCTION,
      temperature: 0.15,
      maxOutputTokens: 16384,
      thinkingConfig: {
        thinkingBudget,
      },
    },
    timeoutMs,
    label: isLive ? `Live Class Fast Diagram Generation (${input.title})` : `Tier 2 Diagram Refinement (${input.title})`,
  })

  let cleanSvg = (rawOutput || '').trim()
  // Clean markdown code blocks if any
  cleanSvg = cleanSvg.replace(/^```(?:xml|svg|html)?\s*/i, '').replace(/\s*```$/i, '').trim()

  if (!cleanSvg.includes('<svg') || !cleanSvg.includes('</svg>')) {
    throw new Error(`Tier 2 generator did not produce valid SVG markup for "${input.title}".`)
  }

  // Ensure pure white background if model missed it
  if (!cleanSvg.includes('fill="#FFFFFF"') && !cleanSvg.includes("fill='#FFFFFF'")) {
    cleanSvg = cleanSvg.replace(
      /<rect[^>]+fill=["'](?:#13211B|#0F172A|#000000|#1E293B)["'][^>]*\/>/i,
      '<rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>'
    )
  }

  return {
    title: input.title,
    svg: cleanSvg,
    caption: `Publication-grade vector ${input.visualType || 'diagram'} for ${input.title}, refined by Tier 2 with textbook precision.`,
    why_needed: input.whyNeeded || `Visually grounds the core principles of ${input.title}.`,
    what_to_explain: input.whatToExplain || `Explain key features, labels, and callout pointers shown.`,
    what_to_make: input.whatToMake,
    visual_type: input.visualType || 'diagram',
    interactive_math_formula: input.interactiveMathFormula,
    refined_by_tier2: true,
    tier2_refined_at: new Date().toISOString(),
    modelUsed,
  }
}

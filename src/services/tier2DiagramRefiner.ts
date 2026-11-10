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

const TIER2_SYSTEM_INSTRUCTION = `You are a World-Class Academic Textbook Illustrator & Senior Vector Graphic Designer for elite scholastic platforms (Aristotle, Gauth, Desmos, Hairline).
Your ONLY task is to generate or refine authentic, publication-grade, ultra-detailed vector SVG educational visualizations (images, diagrams, animations, and mathematical graphs) using modern 3D Axonometric Hairline drafting principles.

CRITICAL VECTOR DESIGN SPECIFICATIONS (WHITE CHALKBOARD / HAIRLINE & ARISTOTLE BENCHMARK):
1. CANVAS & CLEAN WHITE CHALKBOARD THEME (MANDATORY):
   - Must use viewBox="0 0 540 280" and xmlns="http://www.w3.org/2000/svg".
   - Include shape-rendering="geometricPrecision" and text-rendering="geometricPrecision".
   - PURE CLEAN WHITE BACKGROUND (EXACTLY MATCHING THE WHITE CHALKBOARD):
     * Canvas backdrop: <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
     * NEVER use dark green (#13211B) or dark blue! The background MUST be clean white (#FFFFFF) so it seamlessly blends into the digital chalkboard!
     * Subtle coordinate drafting grid: <path d="M 60 260 L 270 140 L 480 260" stroke="#F1F5F9" stroke-width="0.8" fill="none"/>
     * Header pill badge at top center: <rect x="110" y="12" width="320" height="22" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/> with <text x="270" y="27" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold" font-family="'JetBrains Mono', 'Segoe UI', system-ui, sans-serif">
   - Clean Scholastic Palette on White:
     * Deep Charcoal / Ink: #0F172A (axes, primary text, formulas)
     * Aristotle Royal Blue: #2563EB (primary vectors, forward paths, active layers)
     * Scholar Emerald Green: #16A34A (motion curves, biological tissues, positive gradients)
     * Crimson / Coral Red: #DC2626 (return paths, laser beams, nuclei, critical focus points)
     * Warm Chalk Amber / Orange: #D97706 or #F59E0B (normal vectors, actual distance arcs, secondary layers)
     * Muted Slate Gray: #64748B (tick labels, annotations, subtitles)
     * Pointer Leader lines: stroke="#94A3B8" with target dots fill="#2563EB"
   - Fonts: 'JetBrains Mono', 'Segoe UI', system-ui, sans-serif

2. HAIRLINE 3D AXONOMETRIC ISOMETRIC DRAFTING ENGINE (MANDATORY FOR ALL PHYSICAL, OPTICAL, MECHANICAL, CHEMICAL & 3D MATHS CONCEPTS):
   - ZERO FLAT 2D CLIPART: NEVER draw flat 2D lines for physical apparatus, lenses, prisms, circuits, or mechanisms. Every physical apparatus MUST be drawn using authentic 30° axonometric isometric projection.
   - ROUNDED 3D SOLIDS & BEVELS:
     * Glass slabs, prisms, blocks, and cylinders must have distinct Top, Front-Left, and Front-Right faces with lighting contrast:
       - Top face: fill="#EFF6FF" (semi-translucent light tint) with stroke="#2563EB" stroke-width="1.75" stroke-linejoin="round"
       - Front-Left face: fill="#BFDBFE" fill-opacity="0.55" stroke="#94A3B8" stroke-width="1.2"
       - Front-Right face: fill="#93C5FD" fill-opacity="0.35" stroke="#94A3B8" stroke-width="1.2"
     * 3D Cylinders / Beakers: Render with rounded isometric top ellipses and vertical silhouette drops.
     * Inclined Planes: 30° isometric ramp with a 3D block sitting on the slope, normal reaction vector perpendicular to the 3D surface plane, and gravity components.
     * Optics & Prisms: Show the 3D glass volume, incident ray striking the 3D face, the refracted ray propagating through the internal glass volume, and the emergent ray exiting with deviation.
   - INTERACTIVE HOVER CONTAINER:
     * Wrap the primary 3D apparatus in <g class="hairline-interactive" style="transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1); transform-origin: 270px 160px;"> to give subtle physical depth.

3. SMART DUAL-SIDED CALLOUT & POINTER SYSTEM:
   - Distribute labels symmetrically (Left and Right sides) with ample spacing.
   - EXACT POINTER TARGET ACCURACY:
     * Small solid circle dot <circle cx="..." cy="..." r="2.5" fill="#2563EB"/> located PRECISELY at the 3D feature.
     * Clean connecting leader line: <polyline points="targetX,targetY elbowX,targetY labelX,labelY" fill="none" stroke="#94A3B8" stroke-width="1"/>
     * Callout badge card: <rect x="..." y="..." width="..." height="22" rx="6" fill="#FFFFFF" stroke="#E2E8F0" filter="drop-shadow(0 1px 3px rgba(0,0,0,0.04))"/>
   - NO TEXT OVERLAPPING: Minimum 22px vertical separation between adjacent text lines.
   - Labels on the right side: anchor at x >= 390 (text-anchor="start").
   - Labels on the left side: anchor at x <= 150 (text-anchor="end").

4. UNIVERSAL VISUAL MODALITY CAPABILITIES & MANDATORY DYNAMIC MOTION:
   - MANDATORY CSS ANIMATIONS & DYNAMIC MOTION:
     * Every SVG MUST contain an internal <defs><style>...</style></defs> block with fluid, performant CSS animations (@keyframes) or SVG <animate>/<animateMotion>.
     * Flowing dash animations for current, rays, or vectors:
       @keyframes flowDash { to { stroke-dashoffset: -20; } }
     * Pulsing focal points / normal rings:
       @keyframes pulseRing { 0%, 100% { r: 3.5; opacity: 1; } 50% { r: 6.5; opacity: 0.3; } }
     * Moving trace points along plotted functions or ray paths using animateMotion.
   - MATHEMATICAL & KINEMATIC FUNCTION GRAPHS:
     * Balanced Cartesian grid with numbered tick marks and coordinate labels.
     * Plotted function curves with marked intercepts, extrema, roots, and slope triangles (Delta y / Delta x).
     * Clear algebraic formula callout badge (e.g. y = x^2 - 3x - 4 or v(t) = u + at).

5. STRICT VISUAL-ONLY INVARIANT:
   - You refine and generate ONLY the visual graphic vector markup (<svg>).
   - NEVER generate, replace, or alter narrative curriculum content, chapter notes, definitions, exercises, or questions.
   - Output ONLY the raw <svg viewBox="0 0 540 280" ...>...</svg> element.
   - NEVER wrap in markdown code fences (triple backticks xml or svg).
   - Output must be 100% valid XML with closing </svg>.`;

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

import { NextResponse } from 'next/server'
import { GoogleGenAI } from '@google/genai'
import { checkRateLimit, getClientIp } from '@/lib/rateLimit'

// In-memory LRU-like cache for generated SVGs to conserve API tokens and render instantly
const svgCache = new Map<string, { svg: string; title: string; caption: string; timestamp: number }>()

export async function POST(req: Request) {
  try {
    const ip = getClientIp(req)
    const ipLimit = checkRateLimit({
      key: `diagram_ip:${ip}`,
      maxRequests: 60,
      windowMs: 60 * 1000,
    })
    if (!ipLimit.success) {
      return NextResponse.json({ error: 'Too many diagram requests. Please wait a moment.' }, { status: 429 })
    }

    const body = await req.json()
    const {
      title = 'Scientific Diagram',
      domain = 'general',
      subject = 'Science',
      classLevel = 'Class 10',
      context = '',
      prompt = '',
      existingSvg = '',
      refinementPrompt = '',
      whyNeeded = '',
      whatToExplain = '',
    } = body

    const cacheKey = `${title.toLowerCase().trim()}|${subject.toLowerCase().trim()}|${classLevel}|${Boolean(existingSvg)}`
    const cached = svgCache.get(cacheKey)
    if (!existingSvg && cached && Date.now() - cached.timestamp < 1000 * 60 * 60) {
      return NextResponse.json(cached)
    }

    const apiKey = process.env.GEMINI_API_KEY
    if (!apiKey) {
      return NextResponse.json({ error: 'GEMINI_API_KEY is not configured.' }, { status: 500 })
    }

    const ai = new GoogleGenAI({ apiKey })

    const isRefinement = Boolean(existingSvg && existingSvg.includes('<svg'))

    const systemPrompt = `You are a World-Class Academic Textbook Illustrator & Senior Vector Graphic Designer for elite scholastic platforms (Aristotle, Gauth, Desmos).
Your ONLY task is to ${isRefinement ? 'refine and enhance an existing vector SVG educational diagram' : 'generate an authentic, publication-grade, ultra-detailed vector SVG educational diagram'} for:
Topic: "${title}"
Subject / Discipline: "${subject}"
Grade Level: "${classLevel}"
Academic Context: "${context || prompt || title}"
${whyNeeded ? `Pedagogical Reason (Why Needed): "${whyNeeded}"` : ''}
${whatToExplain ? `Instructional Explanations (What to Explain): "${whatToExplain}"` : ''}
${isRefinement && refinementPrompt ? `Refinement Directive: "${refinementPrompt}"` : ''}

CRITICAL VECTOR DESIGN SPECIFICATIONS (WHITE CHALKBOARD / ARISTOTLE BENCHMARK):
1. CANVAS & CLEAN WHITE CHALKBOARD THEME (MANDATORY):
   - Must use viewBox="0 0 540 280" and xmlns="http://www.w3.org/2000/svg".
   - Include shape-rendering="geometricPrecision" and text-rendering="geometricPrecision".
   - PURE CLEAN WHITE BACKGROUND (EXACTLY MATCHING THE WHITE CHALKBOARD):
     * Canvas backdrop: <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
     * NEVER use dark green (#13211B) or dark blue! The background MUST be clean white (#FFFFFF) so it seamlessly blends into the white whiteboard!
     * Subtle coordinate graph grid: stroke="#F1F5F9" stroke-width="0.75"
     * Header pill badge at top center: <rect x="130" y="14" width="280" height="22" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/> with <text fill="#1E293B" font-size="11" font-weight="bold">
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
   - NO TEXT OVERLAPPING: Minimum 24px vertical separation between adjacent text lines.
   - Labels on the right side: anchor at x <= 420 (text-anchor="start").
   - Labels on the left side: anchor at x >= 120 (text-anchor="end").

3. UNIVERSAL SUBJECT ADAPTABILITY (ARISTOTLE BENCHMARK):
   - PHYSICS & KINEMATICS:
     * For Motion Graphs & Kinematics: Draw a dual-tier diagram:
       - Top row: 4 mini coordinate line graphs (Distance-Time s vs t or Velocity-Time v vs t) side by side with axes, arrowheads, and emerald green curves (#16A34A):
         1. Stationary body: flat horizontal line
         2. Uniform motion: constant straight diagonal slope
         3. Accelerating non-uniform motion: upward curved parabola
         4. Decelerating non-uniform motion: downward curved line
         Each labeled clearly below the graph!
       - Bottom row: 1D horizontal coordinate axis with numbered ticks (1 to 8), Start dot (x_i), End diamond (x_f), actual path curved arc (orange dashed with arrow and distance/time), net displacement vector arrow (#2563EB), and velocity calculation box (v̄ = Δx / Δt)!
     * For Optics: Principal axis, concave/convex dual curved lens, focal points F and 2F, object arrow, 3 distinct refracted rays, inverted image arrow, Gaussian formula.
     * For Mechanics & Forces: Incline plane with angle theta, block, normal force N perpendicular, mg downward, resolved components, friction vector, and Newton's equations.
     * For Circuits: Battery plates, switch, zigzag resistor, ammeter circle (A), voltmeter circle (V), and Ohm's law.
   - BIOLOGY:
     * Center the anatomical/cellular structure. Dual-sided leader lines pointing accurately to specific membranes, organelles, or layers. Labeled cross-sections with cellular textures.
     * Plant Cell Wall: Middle lamella (#D97706), Primary cell wall (#16A34A mesh), Secondary cell wall (#2563EB layers), Plasma membrane lipid bilayer (#0F172A) with transport proteins (#DC2626).
   - MATHEMATICS & COORDINATE GEOMETRY:
     * Balanced coordinate grid, labeled axes with ticks, quadrant badges, clean curve plots, plotted coordinates P(x, y) with dashed drop-lines to axes. For algebraic equations, plot actual lines and curves with their equations labeled directly beside them (like Desmos/Aristotle).
   - CHEMISTRY: Accurate apparatus, molecular geometry, or electron shells with clear atomic orbitals.

4. STRICT PROHIBITIONS:
   - NEVER use dark green (#13211B) or dark slate background. The canvas MUST be clean WHITE (#FFFFFF).
   - NEVER output generic placeholder boxes or corporate flowchart cards.
   - NEVER wrap your output in markdown code fences (\`\`\`xml or \`\`\`svg). Output ONLY the raw <svg>...</svg> element.
   - Output must be 100% valid XML with closing </svg>.`

    const userPromptText = isRefinement
      ? `Refine this existing SVG diagram for: "${title}". Refinement instructions: ${refinementPrompt || context}. Keep the background pure white (#FFFFFF). Existing SVG:\n${existingSvg}\nReturn ONLY the updated raw <svg viewBox="0 0 540 280" ...>...</svg> element.`
      : `Generate a publication-grade vector SVG diagram for: "${title}". Academic domain: ${domain}. Grade: ${classLevel}. Context: ${context}. Return ONLY the raw <svg viewBox="0 0 540 280" ...>...</svg> element with pure white background.`

    const candidateModels = [
      'gemini-3.8-flash',
      'gemini-3.5-flash',
      'gemini-3-flash-preview',
      'gemini-2.5-flash',
      'gemini-3.6-flash',
      'gemini-3.5-flash-lite',
      'gemini-2.5-flash-lite',
    ]
    let response: any = null
    let lastError: any = null

    for (const candidateModel of candidateModels) {
      try {
        const modelConfig: any = {
          systemInstruction: systemPrompt,
          temperature: 0.15,
          maxOutputTokens: 16384,
        }
        if (candidateModel.startsWith('gemini-3')) {
          modelConfig.thinkingConfig = {
            thinkingBudget: 1024,
          }
        }

        response = await ai.models.generateContent({
          model: candidateModel,
          contents: [
            {
              role: 'user',
              parts: [
                {
                  text: userPromptText,
                },
              ],
            },
          ],
          config: modelConfig,
        })
        if (response?.text) break
      } catch (err: any) {
        lastError = err
        console.warn(`[Diagram Generator] Model ${candidateModel} failed, trying cascade fallback:`, err?.message)
      }
    }

    if (!response?.text) {
      throw lastError || new Error('All diagram generation models in cascade failed')
    }

    let rawSvg = response.text || ''
    // Strip markdown code fences if model accidentally emitted them
    rawSvg = rawSvg.trim().replace(/^```(?:xml|svg|html)?\s*/i, '').replace(/\s*```$/i, '').trim()

    // Validate SVG contains basic tags
    if (!rawSvg.includes('<svg') || !rawSvg.includes('</svg>')) {
      throw new Error('Model did not return a valid complete SVG element.')
    }

    const result = {
      title,
      svg: rawSvg,
      caption: `Authentic vector diagram for ${title}, rendered with textbook-grade precision.`,
      why_needed: whyNeeded || `Visually grounds the core principles and mathematical relations of ${title}.`,
      what_to_explain: whatToExplain || `Explain the key features, directional axes, and labeled callouts shown in the diagram.`,
      timestamp: Date.now(),
    }

    // Cache the result
    svgCache.set(cacheKey, result)
    if (svgCache.size > 100) {
      const oldestKey = svgCache.keys().next().value
      if (oldestKey) svgCache.delete(oldestKey)
    }

    return NextResponse.json(result)
  } catch (err: any) {
    console.error('[Diagram Generate API] Error generating SVG:', err)
    return NextResponse.json(
      { error: err?.message || 'Failed to generate scientific SVG diagram.' },
      { status: 500 }
    )
  }
}

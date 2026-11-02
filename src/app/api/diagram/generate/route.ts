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
    } = body

    const cacheKey = `${title.toLowerCase().trim()}|${subject.toLowerCase().trim()}|${classLevel}`
    const cached = svgCache.get(cacheKey)
    if (cached && Date.now() - cached.timestamp < 1000 * 60 * 60) {
      return NextResponse.json(cached)
    }

    const apiKey = process.env.GEMINI_API_KEY
    if (!apiKey) {
      return NextResponse.json({ error: 'GEMINI_API_KEY is not configured.' }, { status: 500 })
    }

    const ai = new GoogleGenAI({ apiKey })

    const systemPrompt = `You are a World-Class Academic Textbook Illustrator & Senior Vector Graphic Designer for elite scholastic platforms (Aristotle, Gauth, Desmos).
Your ONLY task is to generate an authentic, publication-grade, ultra-detailed vector SVG educational diagram for:
Topic: "${title}"
Subject / Discipline: "${subject}"
Grade Level: "${classLevel}"
Academic Context: "${context || prompt || title}"

CRITICAL VECTOR DESIGN SPECIFICATIONS (PREMIUM SCHOLASTIC BENCHMARK):
1. CANVAS & LUXURY THEME PALETTE:
   - Must use viewBox="0 0 540 280" and xmlns="http://www.w3.org/2000/svg".
   - Include shape-rendering="geometricPrecision" and text-rendering="geometricPrecision".
   - CLEAN LUXURY DARK SLATE/OBSIDIAN BACKDROP (NO MURKY GREEN):
     * Canvas backdrop: <rect x="8" y="8" width="524" height="264" rx="10" fill="#0A0F1D" stroke="#1E293B" stroke-width="1.5"/>
     * Inner cards / panels: fill="#111C33" or fill="#0F172A", stroke="#1E293B"
     * Subtle coordinate grid: stroke="#1E293B" stroke-width="0.5" opacity="0.4"
     * Header badge pill at top center: <rect x="140" y="16" width="260" height="22" rx="6" fill="#111C33" stroke="#1E293B"/> with <text fill="#38BDF8" font-size="11" font-weight="bold">
   - Accent & Feature Colors:
     * Cyan / Electric Sky: #38BDF8 (primary vectors, active layers, axes)
     * Vibrant Mint / Emerald: #34D399 (biological structures, positive vectors, focus)
     * Warm Chalk Amber: #FBBF24 (secondary layers, formulas, angles)
     * Coral Rose: #F43F5E or #FB7185 (transport proteins, nuclei, return paths)
     * Pure Slate White: #F8FAFC (crisp text labels, ticks)
     * Muted Gray: #94A3B8 (subtitles, secondary info, leader lines)
   - Fonts: 'JetBrains Mono', 'Segoe UI', system-ui, sans-serif

2. SMART CALLOUT & POINTER SYSTEM (CRITICAL - MUST BE APPLIED TO ALL SUBJECTS):
   - NEVER cram all labels on one side! Distribute labels intelligently (e.g. Left and Right sides, or Top and Bottom).
   - EXACT POINTER TARGET ACCURACY:
     * Every pointer must start with a small solid circle dot <circle cx="..." cy="..." r="2.5" fill="#38BDF8"/> located PRECISELY at the anatomical or mathematical feature it describes.
     * The leader line must connect cleanly: <polyline points="targetX,targetY elbowX,targetY labelX,labelY" fill="none" stroke="#64748B" stroke-width="1"/>
     * NEVER point to empty space, wrong layers, or incorrect coordinates!
   - NO TEXT CLUSTERING OR OVERFLOW:
     * Maintain AT LEAST 24px vertical separation between any two adjacent text lines.
     * Labels on the right side: anchor at x <= 420 (text-anchor="start") so they never clip off the 540 canvas.
     * Labels on the left side: anchor at x >= 120 (text-anchor="end").
   - Balanced vertical centering: Center the main illustration vertically (between y=55 and y=225) so the card feels full, balanced, and intentional without awkward bottom voids.

3. UNIVERSAL SUBJECT ADAPTABILITY:
   - BIOLOGY: Center the anatomical/cellular structure. Dual-sided leader lines pointing accurately to specific membranes, organelles, or layers. Labeled cross-sections with cellular textures.
   - PHYSICS & KINEMATICS (ARISTOTLE BENCHMARK):
     * For Motion Graphs & Kinematics: Draw a dual-tier diagram:
       - Top row: 4 mini coordinate line graphs (Distance-Time s vs t or Velocity-Time v vs t) side by side with axes, arrowheads, and emerald/cyan curves (#34D399 / #38BDF8):
         1. Stationary body: flat horizontal line
         2. Uniform motion: constant straight diagonal slope
         3. Accelerating non-uniform motion: upward curved parabola
         4. Decelerating non-uniform motion: downward curved line
         Each labeled clearly below the graph!
       - Bottom row: 1D horizontal coordinate axis with numbered ticks (1 to 8), Start dot (x_i), End diamond (x_f), actual path curved arc (orange dashed with arrow and distance/time), net displacement vector arrow (#38BDF8), and velocity calculation box (v̄ = Δx / Δt)!
     * For Optics: Principal axis, concave/convex dual curved lens, focal points F and 2F, object arrow, 3 distinct refracted rays, inverted image arrow, Gaussian formula.
     * For Mechanics & Forces: Incline plane with angle theta, block, normal force N perpendicular, mg downward, resolved components, friction vector, and Newton's equations.
     * For Circuits: Battery plates, switch, zigzag resistor, ammeter circle (A), voltmeter circle (V), and Ohm's law.
   - MATHEMATICS & COORDINATE GEOMETRY:
     * Balanced coordinate grid, labeled axes with ticks, quadrant badges, clean curve plots, plotted coordinates P(x, y) with dashed drop-lines to axes. For algebraic equations, plot actual lines and curves with their equations labeled directly beside them (like Desmos/Aristotle).
   - CHEMISTRY: Accurate apparatus, molecular geometry, or electron shells with clear atomic orbitals.

4. STRICT PROHIBITIONS:
   - NEVER use murky olive green (#13211B). Use deep obsidian navy (#0A0F1D / #111C33).
   - NEVER output generic placeholder boxes, corporate flowchart cards ("CONCEPTUAL BLUEPRINT", "ANAXLY VECTOR ENGINE", "1. GOVERNING PRINCIPLE").
   - NEVER wrap your output in markdown code fences (\`\`\`xml or \`\`\`svg). Output ONLY the raw <svg>...</svg> element.
   - Output must be 100% valid XML with closing </svg>.`

    const response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: [
        {
          role: 'user',
          parts: [
            {
              text: `Generate a publication-grade vector SVG diagram for: "${title}". Academic domain: ${domain}. Grade: ${classLevel}. Context: ${context}. Return ONLY the raw <svg viewBox="0 0 540 280" ...>...</svg> element.`,
            },
          ],
        },
      ],
      config: {
        systemInstruction: systemPrompt,
        temperature: 0.15,
        maxOutputTokens: 16384,
        thinkingConfig: {
          thinkingBudget: 1024,
        },
      },
    })

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

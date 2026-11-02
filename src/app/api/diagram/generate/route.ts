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

    const systemPrompt = `You are a World-Class Academic Textbook Illustrator & Vector Graphic Designer for elite scholastic platforms (Aristotle, Gauth, Desmos).
Your ONLY task is to generate an authentic, publication-grade, ultra-detailed vector SVG educational diagram for:
Topic: "${title}"
Subject / Discipline: "${subject}"
Grade Level: "${classLevel}"
Academic Context: "${context || prompt || title}"

CRITICAL VECTOR DESIGN SPECIFICATIONS (ARISTOTLE & GAUTH BENCHMARK):
1. CANVAS & GEOMETRY:
   - Must use viewBox="0 0 540 280" and xmlns="http://www.w3.org/2000/svg".
   - Include shape-rendering="geometricPrecision" and text-rendering="geometricPrecision".
   - Dark scholastic chalkboard backdrop: <rect x="8" y="8" width="524" height="264" rx="10" fill="#13211B" stroke="#233930" stroke-width="2"/>
   - Subtle chalk grid pattern or background texture.
   - Header badge at top: dark pill with title in bold cyan/sage (<text fill="#7EC8E3" font-size="11" font-weight="bold">).

2. DOMAIN-SPECIFIC ARTISTIC FIDELITY:
   - BIOLOGY (Cells, Cell Walls, Organelles, Tissues, Photosynthesis):
     * NEVER draw 4 flat horizontal colored stripes or a plain empty ellipse!
     * For Plant Cell Wall: Draw authentic layered architecture with Middle Lamella (pectin mesh, #68B084), Primary Cell Wall with cellulose microfibril criss-cross fibers (#7EC8E3), Secondary Cell Wall (thick layered cellulose, #FBBF24 / #F87171), and Plasma Membrane phospholipid bilayer (hydrophilic heads and hydrophobic tails). Include callout leader lines with labeled circular dots.
     * For Cells: Draw plasma membrane, cytoplasm with ribosomes/mitochondria, nucleus with nuclear envelope, nucleolus, and chromatin network.
   - PHYSICS & KINEMATICS (Motion, Vectors, Forces, Optics, Circuits):
     * For 1D / 2D Motion: Draw horizontal coordinate reference scale with origin O(0m), positions A and B, forward dashed vector arrow, return dashed vector arrow, and bottom bold solid net displacement vector with distance vs displacement calculation legend!
     * For Optics: Principal axis, concave/convex lens or mirror with dual curvature, focal points F and 2F, object arrow, at least 3 refracted rays (parallel through focus, through optical center, through focus emerging parallel), inverted image arrow, and Gaussian formula panel.
     * For Mechanics: Incline plane with angle theta, block, normal force N perpendicular to surface, weight W = mg downward, resolved components mg*sin(theta) and mg*cos(theta), friction arrow opposite to motion, and Newton's law solution panel.
     * For Circuits: Battery plates (+ and -), switch, zigzag resistor, ammeter circle (A) in series, voltmeter circle (V) in parallel, and Ohm's law formula.
   - MATHEMATICS & COORDINATE GEOMETRY:
     * Perpendicular axes X and Y with directional arrows, origin O(0,0), numbered ticks (-4 to +4), colored quadrant tinting, sign convention labels: Quadrant I (+, +), Quadrant II (-, +), Quadrant III (-, -), Quadrant IV (+, -), and plotted sample point (e.g. P(3, 2)) with dashed projection lines.
   - CHEMISTRY:
     * Accurate apparatus (beaker with liquid meniscus, test tube with stand, Bunsen burner flame, condenser), chemical reaction energy profiles, or Lewis dot structures.

3. PALETTE (Dark Scholastic / Zero Generic Orange):
   - Backgrounds: #13211B (felt), #0F1A15 (inner cards), #1B2E26 (accents).
   - Lines & Vectors: #7EC8E3 (Ice Blue), #4A90E2 (Royal Blue), #68B084 (Scholar Sage), #FBBF24 (Chalk Gold), #F87171 (Coral Red), #FFFFFF (White).
   - Fonts: 'JetBrains Mono', 'Segoe UI', system-ui, monospace.

4. STRICT PROHIBITIONS:
   - NEVER output generic placeholder boxes, corporate flowchart cards ("CONCEPTUAL BLUEPRINT", "ANAXLY VECTOR ENGINE", "1. GOVERNING PRINCIPLE").
   - NEVER wrap your output in markdown code fences (\`\`\`xml or \`\`\`svg). Output ONLY the raw <svg>...</svg> element.
   - Must be 100% valid, self-contained SVG XML with closing </svg>.`

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
        maxOutputTokens: 8192,
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

import { NextResponse } from 'next/server'
import { checkRateLimit, getClientIp } from '@/lib/rateLimit'
import { generateOrRefineDiagramWithTier2 } from '@/services/tier2DiagramRefiner'

// In-memory LRU-like cache for generated SVGs to conserve API tokens and render instantly
const svgCache = new Map<string, { svg: string; title: string; caption: string; why_needed: string; what_to_explain: string; refined_by_tier2: boolean; timestamp: number }>()

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
      whatToMake = '',
      visualType = 'diagram',
      animationType = '',
      interactiveMathFormula = '',
    } = body

    const cacheKey = `${title.toLowerCase().trim()}|${subject.toLowerCase().trim()}|${classLevel}|${visualType}|${Boolean(existingSvg)}`
    const cached = svgCache.get(cacheKey)
    if (!existingSvg && cached && Date.now() - cached.timestamp < 1000 * 60 * 60) {
      return NextResponse.json(cached)
    }

    const result = await generateOrRefineDiagramWithTier2({
      title,
      domain,
      subject,
      classLevel,
      context: context || prompt || title,
      existingSvg,
      refinementPrompt,
      whyNeeded,
      whatToExplain,
      whatToMake,
      visualType,
      animationType,
      interactiveMathFormula,
    })

    const payload = {
      title: result.title,
      svg: result.svg,
      caption: result.caption,
      why_needed: result.why_needed,
      what_to_explain: result.what_to_explain,
      what_to_make: result.what_to_make,
      visual_type: result.visual_type || visualType,
      interactive_math_formula: result.interactive_math_formula || interactiveMathFormula,
      refined_by_tier2: true,
      timestamp: Date.now(),
      modelUsed: result.modelUsed,
    }

    // Cache the result
    svgCache.set(cacheKey, payload)
    if (svgCache.size > 100) {
      const oldestKey = svgCache.keys().next().value
      if (oldestKey) svgCache.delete(oldestKey)
    }

    return NextResponse.json(payload)
  } catch (err: any) {
    console.error('[Diagram Generate API] Error generating SVG:', err)
    return NextResponse.json(
      { error: err?.message || 'Failed to generate scientific SVG diagram.' },
      { status: 500 }
    )
  }
}

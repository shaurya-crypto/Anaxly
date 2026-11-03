import { NextResponse } from 'next/server'
import { checkRateLimit, getClientIp } from '@/lib/rateLimit'
import { generateOrRefineDiagramWithTier2 } from '@/services/tier2DiagramRefiner'
import { createAdminClient } from '@/utils/supabase/admin'

// In-memory LRU cache for generated SVGs to conserve API tokens and render instantly
const svgCache = new Map<
  string,
  {
    svg: string
    title: string
    concept_title?: string
    diagram_title?: string
    caption: string
    why_needed: string
    what_to_explain: string
    what_to_make?: string
    visual_type?: string
    interactive_math_formula?: string
    refined_by_tier2: boolean
    tier2_refined_at?: string
    timestamp: number
    modelUsed?: string
  }
>()

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

    const body = await req.json().catch(() => ({}))
    let {
      title: rawTitle = '',
      domain = '',
      subject = '',
      classLevel = '',
      context = '',
      prompt = '',
      existingSvg = '',
      refinementPrompt = '',
      whyNeeded = '',
      whatToExplain = '',
      whatToMake = '',
      visualType = '',
      animationType = '',
      interactiveMathFormula = '',
      moduleId,
      conceptIndex,
      conceptTitle = '',
      isLiveClass = false,
      source = '',
    } = body

    // Dynamically resolve classLevel and subject from module/curriculum if not provided in the request
    if (moduleId && (!classLevel || !subject)) {
      try {
        const adminSupabase = createAdminClient()
        const { data: modInfo } = await adminSupabase
          .from('syllabus_modules')
          .select('id, class_level, curriculums(category, class_level)')
          .eq('id', moduleId)
          .single()

        if (modInfo) {
          const curr = Array.isArray(modInfo.curriculums) ? modInfo.curriculums[0] : modInfo.curriculums
          if (!classLevel) {
            classLevel = modInfo.class_level || curr?.class_level || ''
          }
          if (!subject) {
            subject = curr?.category || ''
          }
        }
      } catch (e) {
        console.warn('[Diagram Generate API] Warning resolving module metadata:', e)
      }
    }

    const title = (rawTitle && rawTitle !== 'Scientific Diagram' && rawTitle !== 'Educational Diagram')
      ? rawTitle
      : (conceptTitle || rawTitle || 'Scientific Diagram')

    const isLive = Boolean(isLiveClass || source === 'live_classroom')
    const cacheKey = `${(conceptTitle || title).toLowerCase().trim()}|${title.toLowerCase().trim()}|${(subject || domain).toLowerCase().trim()}|${classLevel.toLowerCase().trim()}|${visualType.toLowerCase().trim()}|${Boolean(existingSvg)}`
    const cached = svgCache.get(cacheKey)

    let result: any = null
    if (!existingSvg && cached && Date.now() - cached.timestamp < 1000 * 60 * 60) {
      result = cached
    } else {
      result = await generateOrRefineDiagramWithTier2({
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
        isLiveClass: isLive,
        source: isLive ? 'live_classroom' : source,
      })

      // Cache the freshly generated result
      svgCache.set(cacheKey, {
        svg: result.svg,
        title: result.title,
        concept_title: conceptTitle || title,
        diagram_title: result.title || title,
        caption: result.caption,
        why_needed: result.why_needed,
        what_to_explain: result.what_to_explain,
        what_to_make: result.what_to_make,
        visual_type: result.visual_type,
        interactive_math_formula: result.interactive_math_formula,
        refined_by_tier2: result.refined_by_tier2,
        tier2_refined_at: result.tier2_refined_at,
        timestamp: Date.now(),
        modelUsed: result.modelUsed,
      })
      if (svgCache.size > 100) {
        const oldestKey = svgCache.keys().next().value
        if (oldestKey) svgCache.delete(oldestKey)
      }
    }

    const cTitle = conceptTitle || title
    const dTitle = result.title || title
    const refinedAt = result.tier2_refined_at || new Date().toISOString()

    const fullVisualDetail = {
      concept_title: cTitle,
      diagram_title: dTitle,
      svg: result.svg,
      diagram_svg: result.svg,
      what_to_make: result.what_to_make || whatToMake || '',
      what_to_explain: result.what_to_explain || whatToExplain || '',
      why_needed: result.why_needed || whyNeeded || `Pedagogical visual grounding for ${cTitle}.`,
      visual_type: result.visual_type || visualType || 'diagram',
      interactive_math_formula: result.interactive_math_formula || interactiveMathFormula || '',
      refined_by_tier2: true,
      tier2_refined_at: refinedAt,
    }

    // Fully detailed persistence into syllabus_modules when moduleId is provided
    if (moduleId) {
      try {
        const adminSupabase = createAdminClient()
        const { data: mod, error: fetchErr } = await adminSupabase
          .from('syllabus_modules')
          .select('id, visual_lesson_plan')
          .eq('id', moduleId)
          .single()

        if (mod && !fetchErr) {
          let vPlan: any = mod.visual_lesson_plan
          if (typeof vPlan === 'string') {
            try {
              vPlan = JSON.parse(vPlan)
            } catch {
              vPlan = {}
            }
          }
          if (!vPlan || typeof vPlan !== 'object') {
            vPlan = {}
          }
          const conceptVisuals: any[] = Array.isArray(vPlan.concept_visuals) ? [...vPlan.concept_visuals] : []

          if (typeof conceptIndex === 'number' && conceptIndex >= 0 && conceptIndex < conceptVisuals.length) {
            conceptVisuals[conceptIndex] = {
              ...conceptVisuals[conceptIndex],
              ...fullVisualDetail,
            }
          } else {
            const matchIdx = conceptVisuals.findIndex((cv: any) => {
              const cvConcept = (cv.concept_title || '').toLowerCase().trim()
              const cvDiagram = (cv.diagram_title || '').toLowerCase().trim()
              const qC = cTitle.toLowerCase().trim()
              const qD = dTitle.toLowerCase().trim()
              return (
                (cvConcept && (cvConcept === qC || cvConcept.includes(qC) || qC.includes(cvConcept))) ||
                (cvDiagram && (cvDiagram === qD || cvDiagram.includes(qD) || qD.includes(cvDiagram)))
              )
            })

            if (matchIdx !== -1) {
              conceptVisuals[matchIdx] = {
                ...conceptVisuals[matchIdx],
                ...fullVisualDetail,
              }
            } else {
              conceptVisuals.push(fullVisualDetail)
            }
          }

          if (!vPlan.diagram_svg || conceptIndex === 0) {
            vPlan.diagram_svg = result.svg
          }
          vPlan.concept_visuals = conceptVisuals
          vPlan.refined_by_tier2 = true
          vPlan.tier2_refined_at = refinedAt

          const { error: updateErr } = await adminSupabase
            .from('syllabus_modules')
            .update({ visual_lesson_plan: vPlan })
            .eq('id', moduleId)

          if (updateErr) {
            console.warn('[Diagram Generate API] Supabase update warning:', updateErr.message)
          }
        }
      } catch (persistErr) {
        console.warn('[Diagram Generate API] Error persisting visual into database:', persistErr)
      }
    }

    const payload = {
      title: dTitle,
      concept_title: cTitle,
      diagram_title: dTitle,
      svg: result.svg,
      diagram_svg: result.svg,
      caption: result.caption,
      why_needed: fullVisualDetail.why_needed,
      what_to_explain: fullVisualDetail.what_to_explain,
      what_to_make: fullVisualDetail.what_to_make,
      visual_type: fullVisualDetail.visual_type,
      interactive_math_formula: fullVisualDetail.interactive_math_formula,
      refined_by_tier2: true,
      tier2_refined_at: refinedAt,
      timestamp: Date.now(),
      modelUsed: result.modelUsed,
      moduleId,
      conceptIndex,
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

import { NextResponse } from 'next/server'
import { createAdminClient } from '@/utils/supabase/admin'
import { generateOrRefineDiagramWithTier2 } from '@/services/tier2DiagramRefiner'

export const maxDuration = 300
export const dynamic = 'force-dynamic'

export async function POST(req: Request) {
  try {
    const body = await req.json().catch(() => ({}))
    const { curriculumId, moduleId, force = false } = body

    if (!curriculumId && !moduleId) {
      return NextResponse.json(
        { error: 'Please provide either curriculumId or moduleId to refine.' },
        { status: 400 }
      )
    }

    const adminSupabase = createAdminClient()

    let modulesToRefine: any[] = []
    let curriculumInfo: any = null

    if (moduleId) {
      const { data: mod, error: modErr } = await adminSupabase
        .from('syllabus_modules')
        .select('*')
        .eq('id', moduleId)
        .single()

      if (modErr || !mod) {
        return NextResponse.json({ error: `Module not found: ${modErr?.message}` }, { status: 404 })
      }
      modulesToRefine = [mod]
      if (mod.curriculum_id) {
        const { data: curr } = await adminSupabase
          .from('curriculums')
          .select('id, title, category, class_level, board')
          .eq('id', mod.curriculum_id)
          .single()
        curriculumInfo = curr
      }
    } else {
      const { data: curr, error: currErr } = await adminSupabase
        .from('curriculums')
        .select('id, title, category, class_level, board')
        .eq('id', curriculumId)
        .single()

      if (currErr || !curr) {
        return NextResponse.json({ error: `Curriculum not found: ${currErr?.message}` }, { status: 404 })
      }
      curriculumInfo = curr

      const { data: mods, error: modsErr } = await adminSupabase
        .from('syllabus_modules')
        .select('*')
        .eq('curriculum_id', curriculumId)
        .order('order_index', { ascending: true })

      if (modsErr || !mods || mods.length === 0) {
        return NextResponse.json({ error: 'No modules found for curriculum.' }, { status: 404 })
      }
      modulesToRefine = mods
    }

    const subject = curriculumInfo?.category || 'Science'
    const classLevel = curriculumInfo?.class_level || 'Class 9'
    const refinedSummary: any[] = []

    for (const mod of modulesToRefine) {
      const vPlan = mod.visual_lesson_plan || {}
      const isAlreadyRefined = vPlan.refined_by_tier2 === true

      if (isAlreadyRefined && !force) {
        refinedSummary.push({
          id: mod.id,
          title: mod.title,
          status: 'already_refined',
          diagramsCount: (vPlan.concept_visuals?.length || 0) + (vPlan.diagram_svg ? 1 : 0),
        })
        continue
      }

      console.log(`[Tier 2 Refinement] Refining visuals for module: "${mod.title}"...`)

      // 1. Refine main diagram_svg if present or generate if missing
      let refinedMainSvg = vPlan.diagram_svg || ''
      if (vPlan.diagram_svg && vPlan.diagram_svg.includes('<svg')) {
        try {
          const res = await generateOrRefineDiagramWithTier2({
            title: mod.title,
            subject,
            classLevel,
            context: mod.description || mod.title,
            existingSvg: vPlan.diagram_svg,
            whyNeeded: vPlan.diagram_idea || `Pedagogical vector grounding for ${mod.title}`,
            whatToExplain: vPlan.what_to_make || `Step-by-step vector explanation for ${mod.title}`,
            whatToMake: vPlan.what_to_make,
            visualType: vPlan.diagram_type || 'diagram',
          })
          refinedMainSvg = res.svg
        } catch (err: any) {
          console.warn(`[Tier 2 Refinement] Main SVG refinement failed for ${mod.title}:`, err?.message)
        }
      } else if (!refinedMainSvg || !refinedMainSvg.includes('<svg')) {
        try {
          const res = await generateOrRefineDiagramWithTier2({
            title: mod.title,
            subject,
            classLevel,
            context: mod.description || mod.title,
            whyNeeded: vPlan.diagram_idea || `Pedagogical vector grounding for ${mod.title}`,
            whatToExplain: vPlan.what_to_make || `Step-by-step vector explanation for ${mod.title}`,
            whatToMake: vPlan.what_to_make || vPlan.diagram_idea || mod.title,
            visualType: vPlan.diagram_type || 'diagram',
          })
          refinedMainSvg = res.svg
        } catch (err: any) {
          console.warn(`[Tier 2 Refinement] Main SVG synthesis failed for ${mod.title}:`, err?.message)
        }
      }

      // 2. Refine concept_visuals list (diagrams, animations, graphs, visualizations)
      const originalConceptVisuals = Array.isArray(vPlan.concept_visuals) ? vPlan.concept_visuals : []
      const refinedConceptVisuals: any[] = []

      for (const cv of originalConceptVisuals) {
        const initialSvg = cv.svg || cv.diagram_svg || ''
        const cvTitle = cv.diagram_title || cv.concept_title || mod.title
        const isGraph = cv.diagram_type === 'graph' || /graph|parabola|function|kinematic|plot/i.test(cvTitle)
        const isAnimation = cv.diagram_type === 'animation' || /flow|circuit|wave|current|cycle|oscillation|motion/i.test(cvTitle)
        const visualType = isGraph ? 'graph' : isAnimation ? 'animation' : (cv.diagram_type || 'diagram')

        if (initialSvg && initialSvg.includes('<svg')) {
          try {
            const res = await generateOrRefineDiagramWithTier2({
              title: cvTitle,
              subject,
              classLevel,
              context: cv.concept_title || mod.title,
              existingSvg: initialSvg,
              whyNeeded: cv.why_needed || `Pedagogical visual grounding`,
              whatToExplain: cv.what_to_explain || `Walk the student through labeled callouts`,
              whatToMake: cv.what_to_make,
              visualType,
              interactiveMathFormula: cv.interactive_math_formula,
            })
            refinedConceptVisuals.push({
              ...cv,
              svg: res.svg,
              diagram_svg: res.svg,
              visual_type: visualType,
              refined_by_tier2: true,
              tier2_refined_at: res.tier2_refined_at,
            })
          } catch (err: any) {
            console.warn(`[Tier 2 Refinement] Concept visual refinement failed for ${cvTitle}:`, err?.message)
            refinedConceptVisuals.push(cv)
          }
        } else {
          // Synthesize fresh publication-grade visual asset if missing
          try {
            const res = await generateOrRefineDiagramWithTier2({
              title: cvTitle,
              subject,
              classLevel,
              context: cv.concept_title || mod.title,
              whyNeeded: cv.why_needed || `Pedagogical visual grounding for ${cvTitle}`,
              whatToExplain: cv.what_to_explain || cv.what_to_make || `Walk the student through labeled callouts`,
              whatToMake: cv.what_to_make || cvTitle,
              visualType,
              interactiveMathFormula: cv.interactive_math_formula,
            })
            refinedConceptVisuals.push({
              ...cv,
              svg: res.svg,
              diagram_svg: res.svg,
              visual_type: visualType,
              refined_by_tier2: true,
              tier2_refined_at: res.tier2_refined_at,
            })
          } catch (err: any) {
            console.warn(`[Tier 2 Refinement] Concept visual synthesis failed for ${cvTitle}:`, err?.message)
            refinedConceptVisuals.push(cv)
          }
        }
      }

      // 3. Keep visual steps in vPlan.steps in sync with refined SVGs without altering non-visual curriculum content
      const updatedSteps = (vPlan.steps || []).map((step: any, idx: number) => {
        if (step.type === 'DIAGRAM' || step.type === 'GRAPH') {
          const matchingCv = refinedConceptVisuals[idx] || refinedConceptVisuals[0]
          const bestSvg = matchingCv?.svg || refinedMainSvg
          if (bestSvg) {
            return {
              ...step,
              content: {
                ...step.content,
                diagram: {
                  ...step.content?.diagram,
                  svg: bestSvg,
                },
              },
              boardDirective: {
                ...step.boardDirective,
                action: step.boardDirective?.action || 'render_svg_diagram',
                content: `${matchingCv?.diagram_title || step.title} | ${bestSvg} | ${matchingCv?.what_to_make || step.title}`,
              },
            }
          }
        }
        return step
      })

      // Refine ONLY visual_lesson_plan: preserve all text, definitions, exercises, and curriculum content intact
      const updatedVisualPlan = {
        ...vPlan,
        diagram_svg: refinedMainSvg,
        concept_visuals: refinedConceptVisuals,
        ...(updatedSteps.length > 0 ? { steps: updatedSteps } : {}),
        refined_by_tier2: true,
        tier2_refined_at: new Date().toISOString(),
      }

      // Update ONLY visual_lesson_plan in database - NEVER mutate chapter_notes, textbook_definitions, worked_examples, etc.
      const { error: updateErr } = await adminSupabase
        .from('syllabus_modules')
        .update({ visual_lesson_plan: updatedVisualPlan })
        .eq('id', mod.id)

      if (updateErr) {
        console.error(`[Tier 2 Refinement] Error updating module ${mod.id}:`, updateErr)
      }

      refinedSummary.push({
        id: mod.id,
        title: mod.title,
        status: updateErr ? 'update_error' : 'refined_successfully',
        diagramsCount: refinedConceptVisuals.length + (refinedMainSvg ? 1 : 0),
      })
    }

    return NextResponse.json({
      success: true,
      curriculumId: curriculumInfo?.id,
      chapterTitle: curriculumInfo?.title,
      board: curriculumInfo?.board,
      classLevel,
      category: subject,
      modulesCount: modulesToRefine.length,
      modulesRefined: refinedSummary,
    })
  } catch (err: any) {
    console.error('[Tier 2 Refine Chapter API] Error:', err)
    return NextResponse.json(
      { error: err?.message || 'Failed to refine chapter diagrams.' },
      { status: 500 }
    )
  }
}

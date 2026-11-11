import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@/utils/supabase/server'
import { calculateStudentProgress } from '@/lib/studentProgressService'

export const dynamic = 'force-dynamic'

/**
 * GET /api/student/progress?userId=<userId>
 * Returns student progress summary, completed chapters count, and saved chalkboard notes.
 * Cached with HTTP headers to prevent database load on frequent client navigations.
 */
export async function GET(req: NextRequest) {
  try {
    // Authenticate: student must be logged in to read progress
    const supabase = await createClient()
    const {
      data: { user },
    } = await supabase.auth.getUser()

    const searchParams = req.nextUrl.searchParams
    const requestedUserId = searchParams.get('userId')
    const targetUserId = requestedUserId || user?.id

    if (!targetUserId || !user) {
      return NextResponse.json({ error: 'Missing userId or unauthorized' }, { status: 401 })
    }

    // Tenant check: non-admin students can only query their own progress
    if (user.id !== targetUserId) {
      return NextResponse.json({ error: 'Unauthorized to view progress of other users' }, { status: 403 })
    }

    // Fetch user profile
    const { data: profile } = await supabase
      .from('profiles')
      .select('id, full_name, class_level, target_board, completed_chapters_count')
      .eq('id', targetUserId)
      .maybeSingle()

    // Fetch all published curriculums for the student's class
    let curriculumsQuery = supabase
      .from('curriculums')
      .select('id, title, description, category, difficulty_level, estimated_duration_minutes, is_published, class_level, board, order_index')
      .eq('is_published', true)

    if (profile?.class_level) {
      curriculumsQuery = curriculumsQuery.or(`class_level.eq.${profile.class_level},class_level.is.null`)
    }

    const { data: curriculumsData } = await curriculumsQuery.order('order_index', { ascending: true })
    const curriculums = curriculumsData || []

    const curriculumIds = curriculums.map((c: any) => c.id).filter(Boolean)

    // Fetch syllabus modules
    let modulesQuery = supabase
      .from('syllabus_modules')
      .select('id, curriculum_id, order_index, title, description, key_concepts, estimated_minutes, class_level, board')
      .order('order_index', { ascending: true })

    if (curriculumIds.length > 0) {
      modulesQuery = modulesQuery.in('curriculum_id', curriculumIds)
    }

    const { data: modulesData } = await modulesQuery
    const modules = modulesData || []

    // Fetch user progress records
    const { data: progressData } = await supabase
      .from('user_progress')
      .select('*')
      .eq('user_id', targetUserId)

    const progressRecords = progressData || []

    // Compute progress & chapter stats
    const progressSummary = calculateStudentProgress({
      userId: targetUserId,
      curriculums,
      modules,
      progressRecords,
    })

    return NextResponse.json(
      {
        success: true,
        summary: progressSummary,
        profile: {
          fullName: profile?.full_name || 'Student',
          classLevel: profile?.class_level,
          targetBoard: profile?.target_board,
          completedChaptersCount:
            profile?.completed_chapters_count ?? progressSummary.completedChaptersCount,
        },
      },
      {
        status: 200,
        headers: {
          'Cache-Control': 'private, max-age=30, stale-while-revalidate=60',
        },
      }
    )
  } catch (err: any) {
    console.error('[API Progress GET] Error fetching progress:', err)
    return NextResponse.json({ error: err.message || 'Internal Server Error' }, { status: 500 })
  }
}

/**
 * POST /api/student/progress
 * Saves debounced chalkboard notes, module completion, and updates chapter progress in student profile.
 * Supports standard JSON fetch and navigator.sendBeacon on page unload.
 */
export async function POST(req: NextRequest) {
  try {
    let body: any = {}

    // Support both application/json and text/plain (used by sendBeacon)
    const contentType = req.headers.get('content-type') || ''
    if (contentType.includes('application/json')) {
      body = await req.json()
    } else {
      const rawText = await req.text()
      try {
        body = JSON.parse(rawText)
      } catch {
        body = { rawText }
      }
    }

    const {
      userId,
      moduleId,
      notesText,
      roughText,
      fullSummary,
      visualProgress,
      status,
      currentConceptIndex,
      completedConcepts,
      lastCoveredConcept,
    } = body

    if (!userId || !moduleId) {
      return NextResponse.json({ error: 'Missing userId or moduleId' }, { status: 400 })
    }

    // Authenticate: user must be authenticated
    const supabase = await createClient()
    const {
      data: { user },
    } = await supabase.auth.getUser()

    if (!user) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 })
    }

    if (user.id !== userId) {
      return NextResponse.json({ error: 'Unauthorized user operation' }, { status: 403 })
    }

    const clientToUse = supabase

    const notesToPersist = (fullSummary || notesText || '').trim()
    const now = new Date().toISOString()

    const progressPayload: any = {
      user_id: userId,
      syllabus_module_id: moduleId,
    }

    if (notesToPersist) {
      progressPayload.chapter_notes = notesToPersist
    }

    if (status) {
      progressPayload.status = status
      if (status === 'completed') {
        progressPayload.completed_at = now
      }
    }

    if (typeof currentConceptIndex === 'number') {
      progressPayload.current_concept_index = currentConceptIndex
    }

    if (Array.isArray(completedConcepts)) {
      progressPayload.completed_concepts = completedConcepts
    }

    if (lastCoveredConcept) {
      progressPayload.last_covered_concept = lastCoveredConcept
    }

    if (visualProgress) {
      progressPayload.visual_progress = visualProgress
    }

    // Upsert into user_progress
    const { error: upsertErr } = await clientToUse
      .from('user_progress')
      .upsert(progressPayload, { onConflict: 'user_id,syllabus_module_id' })

    if (upsertErr) {
      // If visual_progress column or syntax issue, fallback without visual_progress
      if (upsertErr.code === '42703' && progressPayload.visual_progress) {
        delete progressPayload.visual_progress
        await clientToUse
          .from('user_progress')
          .upsert(progressPayload, { onConflict: 'user_id,syllabus_module_id' })
      } else {
        console.warn('[API Progress POST] Notice upserting user_progress:', upsertErr.message)
      }
    }

    // Check if this module completion completes the parent chapter
    let isChapterCompleted = false
    let completedChaptersCount = 0

    if (status === 'completed') {
      // 1. Find parent curriculum
      const { data: currentMod } = await clientToUse
        .from('syllabus_modules')
        .select('curriculum_id')
        .eq('id', moduleId)
        .single()

      if (currentMod?.curriculum_id) {
        const curriculumId = currentMod.curriculum_id

        // Fetch all sibling modules for this curriculum
        const { data: siblings } = await clientToUse
          .from('syllabus_modules')
          .select('id')
          .eq('curriculum_id', curriculumId)

        const siblingIds = (siblings || []).map((s: any) => s.id)

        if (siblingIds.length > 0) {
          // Fetch user progress for all sibling modules
          const { data: siblingProgress } = await clientToUse
            .from('user_progress')
            .select('syllabus_module_id, status, completed_at')
            .eq('user_id', userId)
            .in('syllabus_module_id', siblingIds)

          const completedSiblingIds = new Set(
            (siblingProgress || [])
              .filter((p: any) => p.status === 'completed' || !!p.completed_at)
              .map((p: any) => p.syllabus_module_id)
          )

          // Ensure current module is treated as completed
          completedSiblingIds.add(moduleId)

          if (completedSiblingIds.size >= siblingIds.length) {
            isChapterCompleted = true

            // Calculate total completed chapters for the student
            const { data: allUserCompletedProgress } = await clientToUse
              .from('user_progress')
              .select('syllabus_module_id, status, completed_at')
              .eq('user_id', userId)
              .or('status.eq.completed,completed_at.not.is.null')

            const allCompletedModuleIds = new Set(
              (allUserCompletedProgress || []).map((p: any) => p.syllabus_module_id)
            )
            allCompletedModuleIds.add(moduleId)

            // Fetch all modules grouped by curriculum to calculate total completed chapters
            const { data: allModules } = await clientToUse
              .from('syllabus_modules')
              .select('id, curriculum_id')

            const chaptersModuleCount = new Map<string, number>()
            const chaptersCompletedCount = new Map<string, number>()

            ;(allModules || []).forEach((m: any) => {
              chaptersModuleCount.set(
                m.curriculum_id,
                (chaptersModuleCount.get(m.curriculum_id) || 0) + 1
              )
              if (allCompletedModuleIds.has(m.id)) {
                chaptersCompletedCount.set(
                  m.curriculum_id,
                  (chaptersCompletedCount.get(m.curriculum_id) || 0) + 1
                )
              }
            })

            let totalDone = 0
            const completedChapterIdsList: string[] = []
            chaptersModuleCount.forEach((total, currId) => {
              const done = chaptersCompletedCount.get(currId) || 0
              if (total > 0 && done >= total) {
                totalDone += 1
                completedChapterIdsList.push(currId)
              }
            })

            completedChaptersCount = totalDone

            // Update student profile with completed chapters count (resilient to missing column)
            const { error: profileErr } = await clientToUse
              .from('profiles')
              .update({
                completed_chapters_count: totalDone,
                completed_chapter_ids: completedChapterIdsList,
                updated_at: now,
              })
              .eq('id', userId)

            if (profileErr && profileErr.code === '42703') {
              // Retry without completed_chapter_ids if that column is pending migration
              const { error: secondErr } = await clientToUse
                .from('profiles')
                .update({
                  completed_chapters_count: totalDone,
                  updated_at: now,
                })
                .eq('id', userId)

              if (secondErr && secondErr.code === '42703') {
                // If completed_chapters_count is also not migrated, update timestamp only
                await clientToUse
                  .from('profiles')
                  .update({ updated_at: now })
                  .eq('id', userId)
              }
            }
          }
        }
      }
    }

    return NextResponse.json({
      success: true,
      isChapterCompleted,
      completedChaptersCount,
    })
  } catch (err: any) {
    console.error('[API Progress POST] Error saving progress:', err)
    return NextResponse.json({ error: err.message || 'Internal Server Error' }, { status: 500 })
  }
}

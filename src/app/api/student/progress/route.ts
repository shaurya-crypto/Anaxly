import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@/utils/supabase/server'
import { calculateStudentProgress } from '@/lib/studentProgressService'
import {
  getCachedCurriculumModuleCounts,
  getCachedSyllabusModule,
  getCachedUserProfile,
  getCachedCurriculums,
  getCachedCurriculumModules,
  getCachedUserProgressList,
  getCachedSiblingModules,
  invalidateUserProgressCache,
  invalidateUserProfileCache,
} from '@/lib/cache/dataCache'
import { isSchemaError } from '@/lib/utils'

export const dynamic = 'force-dynamic'

/**
 * GET /api/student/progress?userId=<userId>
 * Returns student progress summary, completed chapters count, and saved chalkboard notes.
 * Uses multi-tier cache + HTTP headers to prevent database load on frequent client navigations.
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

    const profile = await getCachedUserProfile(supabase, targetUserId)
    const curriculums = await getCachedCurriculums(supabase, {
      classLevel: profile?.class_level,
      isPublished: true,
    })

    const curriculumIds = curriculums.map((c: any) => c.id).filter(Boolean)
    const [modules, progressRecords] = await Promise.all([
      curriculumIds.length > 0 ? getCachedCurriculumModules(supabase, curriculumIds) : Promise.resolve([]),
      getCachedUserProgressList(supabase, targetUserId),
    ])

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
      if (isSchemaError(upsertErr) && progressPayload.visual_progress) {
        delete progressPayload.visual_progress
        await clientToUse
          .from('user_progress')
          .upsert(progressPayload, { onConflict: 'user_id,syllabus_module_id' })
      } else {
        console.warn('[API Progress POST] Notice upserting user_progress:', upsertErr.message)
      }
    }

    // Invalidate per-user progress cache immediately on write
    invalidateUserProgressCache(userId, moduleId)
    if (status === 'completed') {
      invalidateUserProfileCache(userId)
    }

    // Check if this module completion completes the parent chapter
    let isChapterCompleted = false
    let completedChaptersCount = 0

    if (status === 'completed') {
      // 1. Find parent curriculum via cache
      const currentMod = await getCachedSyllabusModule(clientToUse, moduleId)

      if (currentMod?.curriculum_id) {
        const curriculumId = currentMod.curriculum_id

        // Fetch all sibling modules for this curriculum via cache
        const siblings = await getCachedSiblingModules(clientToUse, curriculumId)

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

            // Fetch all module counts grouped by curriculum to calculate total completed chapters (cached in memory)
            const chaptersModuleCount = await getCachedCurriculumModuleCounts(clientToUse)
            const chaptersCompletedCount = new Map<string, number>()

            // Targeted query: only query curriculums of completed modules rather than scanning entire table
            const completedList = Array.from(allCompletedModuleIds)
            if (completedList.length > 0) {
              const { data: completedModuleRows } = await clientToUse
                .from('syllabus_modules')
                .select('id, curriculum_id')
                .in('id', completedList)

              ;(completedModuleRows || []).forEach((m: any) => {
                if (m.curriculum_id) {
                  chaptersCompletedCount.set(
                    m.curriculum_id,
                    (chaptersCompletedCount.get(m.curriculum_id) || 0) + 1
                  )
                }
              })
            }

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

'use client'

import React, { useEffect } from 'react'
import { useParams, useRouter } from 'next/navigation'
import { createClient } from '@/utils/supabase/client'
import {
  getCachedUserProfile,
  getCachedUserProgressList,
  getCachedUserEnrollments,
  getCachedCurriculums,
  getCachedCurriculumModules,
} from '@/lib/cache/dataCache'

export const dynamic = 'force-dynamic'

export default function ClassRedirectPage() {
  const router = useRouter()
  const params = useParams()
  const userId = params.id as string

  useEffect(() => {
    const supabase = createClient()

    async function routeToActiveModule() {
      try {
        // 1-4. Parallel cached reads for profile, progress, and enrollments
        const [profile, allProgress, enrollments] = await Promise.all([
          getCachedUserProfile(supabase, userId),
          getCachedUserProgressList(supabase, userId),
          getCachedUserEnrollments(supabase, userId),
        ])

        const isUnlimitedUser = profile?.limit_type === 'unlimited'
        const maxAllowedModules = profile?.limit_type === 'modules' ? (profile?.max_modules ?? 5) : 1

        const completedList = (allProgress || []).filter((p: any) => p.status === 'completed')
        if (!isUnlimitedUser && completedList.length >= maxAllowedModules) {
          router.replace('/pricing')
          return
        }

        const inProgRec = (allProgress || []).find((p: any) => p.status === 'in_progress' && p.syllabus_module_id)
        if (inProgRec?.syllabus_module_id) {
          router.replace(`/dashboard/${userId}/class/${inProgRec.syllabus_module_id}`)
          return
        }

        const completedSet = new Set(completedList.map((p: any) => p.syllabus_module_id))
        const enrolledCurriculumIds = (enrollments || []).map((e: any) => e.curriculum_id).filter(Boolean)

        let candidateMods: any[] = []
        if (enrolledCurriculumIds.length > 0) {
          candidateMods = await getCachedCurriculumModules(supabase, enrolledCurriculumIds)
        } else {
          const currs = await getCachedCurriculums(supabase, {
            classLevel: profile?.class_level,
            isPublished: true,
          })
          const currIds = currs.map((c: any) => c.id).filter(Boolean)
          if (currIds.length > 0) {
            candidateMods = await getCachedCurriculumModules(supabase, currIds)
          }
        }

        if (candidateMods && candidateMods.length > 0) {
          const nextMod = candidateMods.find((m) => !completedSet.has(m.id))
          const targetModId = nextMod ? nextMod.id : candidateMods[0].id
          router.replace(`/dashboard/${userId}/class/${targetModId}`)
          return
        }

        // 5. Absolute fallback: any module in database
        const { data: anyMod } = await supabase
          .from('syllabus_modules')
          .select('id')
          .order('order_index', { ascending: true })
          .limit(1)

        if (anyMod && anyMod.length > 0) {
          router.replace(`/dashboard/${userId}/class/${anyMod[0].id}`)
        } else {
          router.replace(`/dashboard/${userId}`)
        }
      } catch (err) {
        console.error('Error routing to module class:', err)
        router.replace(`/dashboard/${userId}`)
      }
    }

    if (userId) {
      routeToActiveModule()
    }
  }, [userId, router])

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-[#0d1611] text-emerald-200">
      <div className="w-10 h-10 border-2 border-emerald-400 border-t-transparent rounded-full animate-spin mb-4" />
      <p className="font-serif text-lg text-emerald-100">Entering Spoken Classroom...</p>
      <p className="text-xs text-emerald-400/60 font-mono mt-1">Calibrating Green Chalkboard &amp; Neural Tutor</p>
    </div>
  )
}

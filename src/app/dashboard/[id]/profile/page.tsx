import React, { Suspense } from 'react'
import { createClient } from '@/utils/supabase/server'
import { redirect } from 'next/navigation'
import { StudentProfileView } from '@/components/profile/StudentProfileView'
import {
  getCachedUserProfile,
  getCachedCurriculums,
  getCachedCurriculumModules,
  getCachedUserProgressList,
} from '@/lib/cache/dataCache'

export const dynamic = 'force-dynamic'

export default async function StudentProfilePage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const resolvedParams = await params
  const supabase = await createClient()

  const {
    data: { user },
  } = await supabase.auth.getUser()

  if (!user || user.id !== resolvedParams.id) {
    redirect('/login')
  }

  // 1. Fetch cached user profile
  const profile = await getCachedUserProfile(supabase, user.id)

  if (!profile || !profile.onboarding_completed) {
    redirect('/onboarding')
  }

  // 2. Fetch cached published curriculums & user progress in parallel
  const [curriculums, progressRecords] = await Promise.all([
    getCachedCurriculums(supabase, { classLevel: profile?.class_level, isPublished: true }),
    getCachedUserProgressList(supabase, user.id),
  ])

  const curriculumIds = curriculums.map((c: any) => c.id).filter(Boolean)

  // 3. Fetch cached syllabus modules
  const modules = curriculumIds.length > 0
    ? await getCachedCurriculumModules(supabase, curriculumIds)
    : []

  return (
    <Suspense
      fallback={
        <div className="flex min-h-screen items-center justify-center bg-[#FBFBF9] font-serif text-[#555852]">
          Loading student profile and master notes...
        </div>
      }
    >
      <StudentProfileView
        user={{ id: user.id, email: user.email }}
        profile={profile}
        curriculums={curriculums}
        modules={modules}
        progressRecords={progressRecords}
      />
    </Suspense>
  )
}

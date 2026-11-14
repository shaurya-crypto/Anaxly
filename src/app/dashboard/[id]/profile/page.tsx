import React, { Suspense } from 'react'
import { createClient } from '@/utils/supabase/server'
import { redirect } from 'next/navigation'
import { StudentProfileView } from '@/components/profile/StudentProfileView'

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

  // 1. Fetch user profile
  const { data: profile } = await supabase
    .from('profiles')
    .select('*')
    .eq('id', user.id)
    .maybeSingle()

  if (!profile || !profile.onboarding_completed) {
    redirect('/onboarding')
  }

  // 2. Fetch published curriculums
  let curriculumsQuery = supabase
    .from('curriculums')
    .select('id, title, description, category, difficulty_level, estimated_duration_minutes, is_published, class_level, board, order_index')
    .eq('is_published', true)

  if (profile?.class_level) {
    curriculumsQuery = curriculumsQuery.or(`class_level.eq.${profile.class_level},class_level.is.null`)
  }

  const { data: curriculumsData } = await curriculumsQuery
    .order('order_index', { ascending: true })
    .order('created_at', { ascending: true })
  const curriculums = curriculumsData || []

  const curriculumIds = curriculums.map((c: any) => c.id).filter(Boolean)

  // 3. Fetch syllabus modules
  let modulesQuery = supabase
    .from('syllabus_modules')
    .select('id, curriculum_id, order_index, title, description, key_concepts, estimated_minutes, class_level, board, chapter_notes')
    .order('order_index', { ascending: true })

  if (curriculumIds.length > 0) {
    modulesQuery = modulesQuery.in('curriculum_id', curriculumIds)
  }

  const { data: modulesData } = await modulesQuery
  const modules = modulesData || []

  // 4. Fetch user progress records (including saved chalkboard notes)
  const { data: progressData } = await supabase
    .from('user_progress')
    .select('*')
    .eq('user_id', user.id)

  const progressRecords = progressData || []

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

import React, { Suspense } from 'react'
import { createClient } from '@/utils/supabase/server'
import { redirect } from 'next/navigation'
import { SettingsView } from '@/components/settings/SettingsView'
import { getStudentSubscription } from '@/lib/subscription/subscriptionService'
import { getCachedUserProfile, getCachedActiveStudyPlan } from '@/lib/cache/dataCache'

export const dynamic = 'force-dynamic'

export default async function SettingsPage({
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

  // Fetch cached student profile, study plan, and subscription in parallel
  const [profile, studyPlan, subscription] = await Promise.all([
    getCachedUserProfile(supabase, user.id),
    getCachedActiveStudyPlan(supabase, user.id),
    getStudentSubscription(user.id).catch(() => null),
  ])

  return (
    <Suspense fallback={<div className="min-h-screen bg-canvas flex items-center justify-center font-serif text-[#555852]">Loading settings...</div>}>
      <SettingsView
        user={{
          id: user.id,
          email: user.email,
          createdAt: user.created_at,
          lastSignIn: user.last_sign_in_at,
          provider: user.app_metadata?.provider,
        }}
        profile={profile || {}}
        studyPlan={studyPlan}
        subscription={subscription}
      />
    </Suspense>
  )
}

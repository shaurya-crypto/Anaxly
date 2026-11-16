'use client'

import { useEffect, useState } from 'react'
import { createClient } from '@/utils/supabase/client'

/**
 * Returns the signed-in user's id, or null while unknown / signed out.
 * Used by landing CTAs to show "Dashboard" to returning students instead of sign-up/sign-in.
 */
export function useAuthUserId(): string | null {
  const [userId, setUserId] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false
    try {
      const supabase = createClient()
      supabase.auth
        .getUser()
        .then(({ data }) => {
          if (!cancelled && data?.user?.id) setUserId(data.user.id)
        })
        .catch(() => {})
      const { data: sub } = supabase.auth.onAuthStateChange((_event, session) => {
        if (!cancelled) setUserId(session?.user?.id ?? null)
      })
      return () => {
        cancelled = true
        sub?.subscription?.unsubscribe()
      }
    } catch {
      // Offline / mock mode: treat as signed out
      return () => {
        cancelled = true
      }
    }
  }, [])

  return userId
}

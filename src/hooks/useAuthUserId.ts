'use client'

import { useEffect, useState } from 'react'

/**
 * Returns the signed-in user's id, or null while unknown / signed out.
 * Used by landing CTAs to show "Dashboard" to returning students instead of sign-up/sign-in.
 *
 * The Supabase client (~260 kB) is imported lazily once the browser is idle, so it
 * never sits on the landing page's critical path.
 */
export function useAuthUserId(): string | null {
  const [userId, setUserId] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false
    let unsubscribe: (() => void) | undefined

    const run = async () => {
      try {
        const { createClient } = await import('@/utils/supabase/client')
        if (cancelled) return
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
        unsubscribe = () => sub?.subscription?.unsubscribe()
        if (cancelled) unsubscribe()
      } catch {
        // Offline / mock mode: treat as signed out
      }
    }

    const w = window as Window & {
      requestIdleCallback?: (cb: () => void, opts?: { timeout: number }) => number
      cancelIdleCallback?: (id: number) => void
    }
    let idleId: number | undefined
    let timeoutId: ReturnType<typeof setTimeout> | undefined
    if (w.requestIdleCallback) idleId = w.requestIdleCallback(() => void run(), { timeout: 2500 })
    else timeoutId = setTimeout(() => void run(), 1200)

    return () => {
      cancelled = true
      if (idleId !== undefined) w.cancelIdleCallback?.(idleId)
      if (timeoutId !== undefined) clearTimeout(timeoutId)
      unsubscribe?.()
    }
  }, [])

  return userId
}

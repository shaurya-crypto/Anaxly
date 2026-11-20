'use client'

import React, { useEffect } from 'react'

/**
 * Lenis smooth wheel scrolling for the landing page. Native wheel scrolling jumps in
 * ~100 px steps, which makes the scroll-scrubbed hero look jerky; Lenis interpolates it.
 * Imported lazily so it never sits on the first-paint critical path.
 */
export function SmoothScroll({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return

    let rafId = 0
    let destroyed = false
    let lenis: { raf: (t: number) => void; destroy: () => void } | null = null

    import('lenis').then(({ default: Lenis }) => {
      if (destroyed) return
      lenis = new Lenis({
        // lerp gives a consistent glide regardless of wheel delta size
        lerp: 0.09,
        // let in-page nav links (#experience, #flow) glide instead of jumping
        anchors: { offset: -80 },
        orientation: 'vertical',
        gestureOrientation: 'vertical',
        smoothWheel: true,
        wheelMultiplier: 1.0,
        touchMultiplier: 1.5,
      })
      const raf = (time: number) => {
        lenis?.raf(time)
        rafId = requestAnimationFrame(raf)
      }
      rafId = requestAnimationFrame(raf)
    })

    return () => {
      destroyed = true
      cancelAnimationFrame(rafId)
      lenis?.destroy()
    }
  }, [])

  return <>{children}</>
}

'use client'

import { useEffect, useState } from 'react'
import dynamic from 'next/dynamic'

const Mascot = dynamic(() => import('./Mascot').then((m) => m.Mascot), { ssr: false })

/** Mounts the mascot only once the browser is idle so it never delays the first paint. */
export function MascotLazy() {
  const [ready, setReady] = useState(false)
  useEffect(() => {
    const w = window as any
    // Queue guidance events until the mascot mounts; it replays them on mount.
    w.__mascotQueue = w.__mascotQueue || []
    const capture = (e: Event) => w.__mascotQueue.push(e)
    window.addEventListener('companion-guide', capture)
    const stopCapture = () => window.removeEventListener('companion-guide', capture)
    if (w.requestIdleCallback) {
      const id = w.requestIdleCallback(() => { stopCapture(); setReady(true) }, { timeout: 2000 })
      return () => { stopCapture(); w.cancelIdleCallback?.(id) }
    }
    const t = setTimeout(() => { stopCapture(); setReady(true) }, 600)
    return () => { stopCapture(); clearTimeout(t) }
  }, [])
  return ready ? <Mascot /> : null
}

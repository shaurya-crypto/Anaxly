'use client'

import React from 'react'
import { motion, useScroll, useSpring } from 'motion/react'

/** Thin reading-progress rule pinned to the top of the landing page. */
export function ScrollProgress() {
  const { scrollYProgress } = useScroll()
  const scaleX = useSpring(scrollYProgress, { stiffness: 140, damping: 30, restDelta: 0.001 })

  return (
    <motion.div
      style={{ scaleX }}
      className="fixed inset-x-0 top-0 z-[60] h-[2px] origin-left bg-coral-primary/80 pointer-events-none"
      aria-hidden="true"
    />
  )
}

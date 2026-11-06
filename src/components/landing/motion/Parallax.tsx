'use client'

import React, { useRef } from 'react'
import { motion, useReducedMotion, useScroll, useSpring, useTransform } from 'motion/react'

interface ParallaxProps {
  children: React.ReactNode
  className?: string
  /** Max vertical travel in px across the element's pass through the viewport. */
  distance?: number
}

export function Parallax({ children, className = '', distance = 40 }: ParallaxProps) {
  const ref = useRef<HTMLDivElement>(null)
  const reduceMotion = useReducedMotion()
  const { scrollYProgress } = useScroll({ target: ref, offset: ['start end', 'end start'] })
  const rawY = useTransform(scrollYProgress, [0, 1], [distance, -distance])
  const y = useSpring(rawY, { stiffness: 120, damping: 30 })

  return (
    <motion.div ref={ref} style={reduceMotion ? undefined : { y }} className={className}>
      {children}
    </motion.div>
  )
}

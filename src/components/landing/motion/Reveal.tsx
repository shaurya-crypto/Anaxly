'use client'

import React from 'react'
import { motion, useReducedMotion, type Variants } from 'motion/react'

export const EASE_EDITORIAL = [0.22, 1, 0.36, 1] as const

const itemVariants: Variants = {
  hidden: { opacity: 0, y: 16, filter: 'blur(6px)' },
  visible: {
    opacity: 1,
    y: 0,
    filter: 'blur(0px)',
    transition: { duration: 0.8, ease: EASE_EDITORIAL },
  },
}

interface RevealProps {
  children: React.ReactNode
  className?: string
  delay?: number
}

/**
 * Fades, lifts and un-blurs its content once it enters the viewport.
 */
export function Reveal({ children, className = '', delay = 0 }: RevealProps) {
  const reduceMotion = useReducedMotion()
  if (reduceMotion) return <div className={className}>{children}</div>

  return (
    <motion.div
      className={className}
      variants={itemVariants}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, margin: '0px 0px -10% 0px' }}
      transition={{ delay }}
    >
      {children}
    </motion.div>
  )
}

/**
 * Staggers direct `RevealItem` children as the group enters the viewport.
 */
export function RevealStagger({ children, className = '' }: Omit<RevealProps, 'delay'>) {
  const reduceMotion = useReducedMotion()
  if (reduceMotion) return <div className={className}>{children}</div>

  return (
    <motion.div
      className={className}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, margin: '0px 0px -10% 0px' }}
      variants={{ hidden: {}, visible: { transition: { staggerChildren: 0.08 } } }}
    >
      {children}
    </motion.div>
  )
}

export function RevealItem({ children, className = '' }: Omit<RevealProps, 'delay'>) {
  return (
    <motion.div className={className} variants={itemVariants}>
      {children}
    </motion.div>
  )
}

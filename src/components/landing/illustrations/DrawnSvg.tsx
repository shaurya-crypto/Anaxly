'use client'

import React, { createContext, useContext, useRef } from 'react'
import { motion, useInView, useReducedMotion } from 'motion/react'

/** Seconds the whole illustration takes to sketch itself. */
const DRAW_DURATION = 1.8

const DrawState = createContext<boolean | null>(null)

interface DrawnSvgProps {
  children: React.ReactNode
  viewBox?: string
  className?: string
  strokeWidth?: number
}

/**
 * Ink-style SVG whose `InkPath` children sketch themselves once, in sequence,
 * when the illustration enters the viewport. Time-based (not scroll-linked)
 * so nothing is recomputed per scroll frame.
 */
export function DrawnSvg({
  children,
  viewBox = '0 0 200 200',
  className = '',
  strokeWidth = 1.6,
}: DrawnSvgProps) {
  const ref = useRef<SVGSVGElement>(null)
  const inView = useInView(ref, { once: true, margin: '0px 0px -15% 0px' })

  return (
    <DrawState.Provider value={inView}>
      <svg
        ref={ref}
        viewBox={viewBox}
        fill="none"
        stroke="currentColor"
        strokeWidth={strokeWidth}
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden="true"
        className={className}
      >
        {children}
      </svg>
    </DrawState.Provider>
  )
}

interface InkPathProps extends Omit<React.SVGProps<SVGPathElement>, 'ref' | 'style'> {
  d: string
  /** Slice of the parent's drawing timeline this stroke occupies. */
  range?: [number, number]
}

export function InkPath({ d, range = [0, 1], ...rest }: InkPathProps) {
  const inView = useContext(DrawState)
  const reduceMotion = useReducedMotion()

  if (reduceMotion || inView === null) return <path d={d} {...rest} />

  const [start, end] = range
  return (
    <motion.path
      d={d}
      initial={{ pathLength: 0, opacity: 0 }}
      animate={inView ? { pathLength: 1, opacity: 1 } : undefined}
      transition={{
        pathLength: {
          delay: start * DRAW_DURATION,
          duration: Math.max(0.2, (end - start) * DRAW_DURATION),
          ease: [0.65, 0, 0.35, 1],
        },
        opacity: { delay: start * DRAW_DURATION, duration: 0.01 },
      }}
      {...(rest as React.ComponentProps<typeof motion.path>)}
    />
  )
}

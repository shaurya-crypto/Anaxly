'use client'

import React, { createContext, useContext, useRef } from 'react'
import { motion, MotionValue, useReducedMotion, useScroll, useSpring, useTransform } from 'motion/react'

const DrawProgress = createContext<MotionValue<number> | null>(null)

interface DrawnSvgProps {
  children: React.ReactNode
  viewBox?: string
  className?: string
  strokeWidth?: number
}

/**
 * Ink-style SVG whose `InkPath` children draw themselves as the
 * illustration scrolls from the lower viewport into the centre.
 */
export function DrawnSvg({
  children,
  viewBox = '0 0 200 200',
  className = '',
  strokeWidth = 1.6,
}: DrawnSvgProps) {
  const ref = useRef<SVGSVGElement>(null)
  const { scrollYProgress } = useScroll({
    target: ref as unknown as React.RefObject<HTMLElement>,
    offset: ['start 90%', 'center 55%'],
  })
  const progress = useSpring(scrollYProgress, { stiffness: 90, damping: 24 })

  return (
    <DrawProgress.Provider value={progress}>
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
    </DrawProgress.Provider>
  )
}

interface InkPathProps extends Omit<React.SVGProps<SVGPathElement>, 'ref' | 'style'> {
  d: string
  /** Slice of the parent's progress this stroke draws over. */
  range?: [number, number]
}

export function InkPath({ d, range = [0, 1], ...rest }: InkPathProps) {
  const parent = useContext(DrawProgress)
  const reduceMotion = useReducedMotion()
  const fallback = useSpring(1)
  const pathLength = useTransform(parent ?? fallback, range, [0, 1])
  const opacity = useTransform(pathLength, [0, 0.02], [0, 1])

  if (reduceMotion || !parent) return <path d={d} {...rest} />

  return (
    <motion.path
      d={d}
      style={{ pathLength, opacity }}
      {...(rest as React.ComponentProps<typeof motion.path>)}
    />
  )
}

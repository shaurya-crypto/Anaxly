'use client'

import React, { useRef } from 'react'
import { useInView } from 'motion/react'

interface HandwritingProps {
  text: string
  className?: string
  /** Seconds between letters. */
  pace?: number
}

/**
 * Writes cursive text letter by letter like a pen on paper, then strokes an
 * ink underline beneath it. Pure CSS animations (transform/opacity only),
 * started once when the line scrolls into view, so there is no per-frame JS.
 */
export function Handwriting({ text, className = '', pace = 0.035 }: HandwritingProps) {
  const ref = useRef<HTMLParagraphElement>(null)
  const inView = useInView(ref, { once: true, margin: '0px 0px -15% 0px' })

  let charIndex = 0
  const words = text.split(' ')
  const total = text.replace(/ /g, '').length

  return (
    <p ref={ref} className={`handwriting ${inView ? 'is-writing' : ''} ${className}`} aria-label={text}>
      <span aria-hidden="true" className="relative inline-block">
        {words.map((word, w) => (
          <React.Fragment key={w}>
            <span className="inline-block whitespace-nowrap">
              {Array.from(word).map((ch) => {
                const delay = charIndex++ * pace
                return (
                  <span
                    key={charIndex}
                    className="handwriting-char"
                    style={{ animationDelay: `${delay}s` }}
                  >
                    {ch}
                  </span>
                )
              })}
            </span>
            {w < words.length - 1 && ' '}
          </React.Fragment>
        ))}
        <span
          className="handwriting-underline"
          style={{ animationDelay: `${total * pace + 0.1}s` }}
        />
      </span>
    </p>
  )
}

'use client'

import React from 'react'
import Image from 'next/image'
import { Laurel } from './illustrations'

interface SectionDividerProps {
  className?: string
}

export function SectionDivider({ className = '' }: SectionDividerProps) {
  return (
    <div
      className={`relative w-full h-20 sm:h-28 overflow-hidden pointer-events-none ${className}`}
      aria-hidden="true"
    >
      {/* Cloud & Paper Shade Dissolve Layer */}
      <div className="absolute inset-0 overflow-hidden opacity-30 mix-blend-multiply">
        <Image
          src="/landing_images/hero-clouds.jpg"
          alt="Atmospheric cloud transition wash"
          fill
          sizes="100vw"
          className="object-cover object-center scale-110"
        />
      </div>

      {/* Inward Diffused Chiaroscuro Edge Shadows */}
      <div className="absolute inset-0 shadow-[inset_0_24px_35px_-12px_rgba(23,24,23,0.14),inset_0_-24px_35px_-12px_rgba(23,24,23,0.14)]" />

      {/* Top and Bottom Ivory Feathering Fades */}
      <div className="absolute inset-0 bg-gradient-to-b from-canvas-ivory via-transparent to-canvas-ivory opacity-95" />

      {/* Laurel ornament drawn in ink as the divider scrolls past */}
      <div className="absolute inset-0 flex items-center justify-center">
        <Laurel className="h-9 w-36 sm:h-11 sm:w-44 text-ink-secondary/60" />
      </div>
    </div>
  )
}

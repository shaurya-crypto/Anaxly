'use client'

import React from 'react'
import Image from 'next/image'
import { Ornament } from './illustrations'

interface SectionDividerProps {
  className?: string
}

export function SectionDivider({ className = '' }: SectionDividerProps) {
  return (
    <div
      className={`relative h-24 sm:h-28 w-full overflow-hidden pointer-events-none ${className}`}
      aria-hidden="true"
    >
      {/* Background Cloud Atmosphere */}
      <div className="absolute inset-0">
        <Image
          src="/landing_images/hero-clouds.jpg"
          alt="Clouds divider atmosphere"
          fill
          sizes="100vw"
          className="object-cover object-center opacity-30 mix-blend-multiply"
        />
      </div>

      {/* Atmospheric Inner Shadow Shade */}
      <div className="absolute inset-0 shadow-[inset_0_20px_30px_-10px_rgba(23,24,23,0.1),inset_0_-20px_30px_-10px_rgba(23,24,23,0.1)]" />

      {/* Top and Bottom Ivory Feathering Fades */}
      <div className="absolute inset-0 bg-gradient-to-b from-canvas-ivory via-transparent to-canvas-ivory opacity-95" />

      {/* Ornament drawn in ink as the divider scrolls past */}
      <div className="absolute inset-0 flex items-center justify-center">
        <Ornament className="h-4 w-48 sm:w-64 text-ink-secondary/50" />
      </div>
    </div>
  )
}

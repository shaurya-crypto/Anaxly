'use client'

import React, { useState, useRef } from 'react'
import Image from 'next/image'
import { motion, useReducedMotion, useScroll, useTransform, useSpring } from 'motion/react'
import { ArtworkSlot } from '@/lib/landing-artwork'
import { EASE_EDITORIAL } from './motion/Reveal'

interface ArtworkFrameProps {
  artwork: ArtworkSlot
  aspectRatioClass?: string
  priority?: boolean
  className?: string
  showCaption?: boolean
  overlayGradient?: 'none' | 'bottom-fade' | 'subtle-vignette' | 'translucent-overlay'
}

/**
 * Editorial museum-grade framed artwork component.
 * Integrates archival paper textures, inner border lines, diffused peripheral shadows,
 * and clean academic metadata captions.
 */
export function ArtworkFrame({
  artwork,
  aspectRatioClass = 'aspect-[4/3]',
  priority = false,
  className = '',
  showCaption = true,
  overlayGradient = 'none',
}: ArtworkFrameProps) {
  const [hasError, setHasError] = useState(false)
  const [isLoaded, setIsLoaded] = useState(false)
  const containerRef = useRef<HTMLElement>(null)
  const reduceMotion = useReducedMotion()

  // Scroll dynamics: the painting drifts slowly inside its frame (parallax window)
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start end', 'end start'],
  })
  const rawY = useTransform(scrollYProgress, [0, 1], ['-6%', '6%'])
  const imageY = useSpring(rawY, { stiffness: 110, damping: 28 })

  return (
    <figure ref={containerRef} className={`group relative flex flex-col ${className}`}>
      <motion.div
        initial={reduceMotion ? false : { clipPath: 'inset(8% 8% 8% 8% round 24px)', opacity: 0.4 }}
        // Negative final inset so the ambient shadow halo is never clipped once revealed
        whileInView={{ clipPath: 'inset(-15% -15% -15% -15% round 0px)', opacity: 1 }}
        viewport={{ once: true, margin: '0px 0px -12% 0px' }}
        transition={{ duration: 1.1, ease: EASE_EDITORIAL }}
        className="relative w-full"
      >
        {/* Ambient shadow shade behind frame to merge softly with the paper canvas */}
        <div
          className="absolute -inset-4 sm:-inset-6 -z-10 rounded-3xl sm:rounded-[36px] bg-ink-primary/10 blur-2xl transition-opacity duration-700 group-hover:opacity-85 pointer-events-none"
          aria-hidden="true"
        />

        {/* Master Frame Container */}
        <div
          className={`relative w-full overflow-hidden rounded-2xl sm:rounded-3xl border border-border-strong/80 bg-canvas-ivory shadow-[0_12px_36px_-6px_rgba(23,24,23,0.12),0_4px_12px_rgba(23,24,23,0.06)] transition-all duration-500 ${aspectRatioClass}`}
        >
          {!hasError ? (
            <>
              <motion.div
                style={reduceMotion ? undefined : { y: imageY }}
                className="absolute -inset-y-[8%] inset-x-0"
              >
                <Image
                  src={artwork.src}
                  alt={artwork.alt}
                  fill
                  sizes="(max-width: 768px) 100vw, (max-width: 1200px) 75vw, 1200px"
                  priority={priority}
                  style={{ objectPosition: artwork.objectPosition || 'center center' }}
                  className={`object-cover transition-[transform,opacity] duration-700 ease-out group-hover:scale-[1.028] ${
                    isLoaded ? 'opacity-100' : 'opacity-0'
                  }`}
                  onLoad={() => setIsLoaded(true)}
                  onError={() => setHasError(true)}
                />
              </motion.div>

              {/* Edge shadow shade and subtle peripheral vignette to merge artwork softly into canvas */}
              <div
                className="pointer-events-none absolute inset-0 shadow-[inset_0_0_24px_rgba(23,24,23,0.12)] rounded-2xl sm:rounded-3xl"
                aria-hidden="true"
              />

              {/* Fine Inset Precision Border */}
              <div
                className="pointer-events-none absolute inset-2.5 sm:inset-3.5 rounded-xl sm:rounded-2xl border border-white/25 mix-blend-overlay"
                aria-hidden="true"
              />

              {overlayGradient === 'bottom-fade' && (
                <div
                  className="pointer-events-none absolute inset-0 rounded-2xl sm:rounded-3xl bg-gradient-to-t from-canvas-ivory via-transparent to-transparent opacity-85"
                  aria-hidden="true"
                />
              )}
            </>
          ) : (
            <div className="flex h-full w-full items-center justify-center p-6 text-center text-ink-muted">
              <span className="font-serif italic text-sm">{artwork.title}</span>
            </div>
          )}
        </div>
      </motion.div>

      {/* Academic Archival Museum Metadata Caption */}
      {showCaption && (
        <figcaption className="mt-3.5 flex flex-col sm:flex-row sm:items-baseline justify-between gap-1 text-[11px] leading-tight text-ink-muted">
          <div className="flex items-baseline gap-2">
            <span className="font-serif italic text-ink-primary font-medium">{artwork.title}</span>
            {artwork.artistNote && (
              <span className="font-sans text-ink-secondary/70">&mdash; {artwork.artistNote}</span>
            )}
          </div>
          {artwork.caption && (
            <div className="flex items-center gap-2 font-mono text-[10px]">
              <span className="truncate max-w-[280px]">{artwork.caption}</span>
            </div>
          )}
        </figcaption>
      )}
    </figure>
  )
}

'use client'

import React, { useState, useRef } from 'react'
import Image from 'next/image'
import { motion, useReducedMotion, useScroll, useTransform, useSpring } from 'motion/react'
import { ArtworkSlot } from '@/lib/landing-artwork'
import { EASE_EDITORIAL } from './motion/Reveal'

interface ArtworkFrameProps {
  artwork: ArtworkSlot
  className?: string
  priority?: boolean
  showCaption?: boolean
  aspectRatioClass?: string
  overlayGradient?: 'none' | 'bottom-fade' | 'subtle-vignette' | 'translucent-overlay'
  maskBottom?: boolean
}

export function ArtworkFrame({
  artwork,
  className = '',
  priority = false,
  showCaption = false,
  aspectRatioClass = 'aspect-[16/10]',
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
          className="absolute -inset-3 sm:-inset-4 rounded-3xl sm:rounded-[32px] bg-ink-primary/[0.07] blur-xl -z-10 pointer-events-none transition-all duration-500 group-hover:bg-ink-primary/[0.12] group-hover:blur-2xl"
          aria-hidden="true"
        />

        <div
          className={`relative w-full overflow-hidden rounded-2xl sm:rounded-3xl border border-border-strong/80 bg-surface-soft shadow-[0_24px_60px_-12px_rgba(23,24,23,0.18),0_10px_25px_-5px_rgba(23,24,23,0.10),0_0_40px_rgba(248,246,240,0.8)] transition-transform duration-500 ease-out group-hover:scale-[1.012] ${aspectRatioClass}`}
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
                className="pointer-events-none absolute inset-0 rounded-2xl sm:rounded-3xl shadow-[inset_0_0_45px_rgba(23,24,23,0.22),inset_0_0_90px_rgba(23,24,23,0.12)]"
                aria-hidden="true"
              />

              {/* Inward dark gradient wash for photographic and painterly chiaroscuro */}
              <div
                className="pointer-events-none absolute inset-0 rounded-2xl sm:rounded-3xl bg-[radial-gradient(ellipse_at_center,_transparent_60%,_rgba(23,24,23,0.16)_100%)]"
                aria-hidden="true"
              />

              {/* Bottom gradient fade for soft transition into ivory canvas */}
              {overlayGradient === 'bottom-fade' && (
                <div
                  className="pointer-events-none absolute inset-0 rounded-2xl sm:rounded-3xl bg-gradient-to-t from-canvas-ivory via-transparent to-transparent opacity-85"
                  aria-hidden="true"
                />
              )}

              {/* Subtle atmospheric vignette */}
              {overlayGradient === 'subtle-vignette' && (
                <div
                  className="pointer-events-none absolute inset-0 rounded-2xl sm:rounded-3xl bg-radial-vignette opacity-25"
                  aria-hidden="true"
                />
              )}

              {/* Translucent overlay for readable text overlays */}
              {overlayGradient === 'translucent-overlay' && (
                <div
                  className="pointer-events-none absolute inset-0 rounded-2xl sm:rounded-3xl bg-canvas-ivory/70 backdrop-blur-[2px]"
                  aria-hidden="true"
                />
              )}
            </>
          ) : (
            /* Graceful Ivory Fallback without broken image icon */
            <div
              className="flex h-full w-full flex-col items-center justify-center rounded-2xl sm:rounded-3xl bg-surface-soft p-6 text-center"
              aria-label={artwork.alt}
            >
              <div className="h-8 w-8 rounded-full border border-border-strong bg-canvas-ivory" />
              <p className="mt-3 font-serif text-lg italic text-ink-secondary">{artwork.title}</p>
              {artwork.caption && (
                <p className="mt-1 font-mono text-xs uppercase tracking-wider text-ink-muted">
                  {artwork.caption}
                </p>
              )}
            </div>
          )}
        </div>
      </motion.div>

      {showCaption && artwork.caption && (
        <figcaption className="mt-3 flex items-center justify-between px-1.5 text-xs text-ink-muted">
          <span className="font-mono text-[11px] tracking-wide text-ink-secondary">
            {artwork.title}
          </span>
          <span className="font-sans text-[11px] italic text-ink-muted">
            {artwork.artistNote || artwork.caption}
          </span>
        </figcaption>
      )}
    </figure>
  )
}


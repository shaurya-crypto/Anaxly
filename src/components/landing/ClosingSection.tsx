'use client'

import React, { useRef } from 'react'
import Link from 'next/link'
import Image from 'next/image'
import { motion, useReducedMotion, useScroll, useTransform, useSpring } from 'motion/react'
import { ArrowRight } from 'lucide-react'
import { RevealStagger, RevealItem } from './motion/Reveal'
import { Ornament } from './illustrations'
import { Handwriting } from './motion/Handwriting'

export function ClosingSection() {
  const boxRef = useRef<HTMLDivElement>(null)
  const reduceMotion = useReducedMotion()
  const { scrollYProgress } = useScroll({
    target: boxRef,
    offset: ['start end', 'center center'],
  })
  // The box settles to full size as it reaches the centre of the viewport
  const scale = useSpring(useTransform(scrollYProgress, [0, 1], [0.92, 1]), {
    stiffness: 120,
    damping: 30,
  })

  return (
    <section className="relative py-20 sm:py-28 lg:py-36 px-4 sm:px-6 lg:px-12">
      {/* Big Box Container with Generous Border Radius and Multi-Layered Diffused Shadow */}
      <div ref={boxRef} className="mx-auto max-w-7xl lg:max-w-[1360px]">
        <motion.div
          style={reduceMotion ? undefined : { scale }}
          className="group relative will-change-transform"
        >
          {/* Ambient shadow shade behind big box to merge seamlessly with paper background */}
          <div
            className="absolute -inset-4 sm:-inset-8 -z-10 rounded-[44px] bg-ink-primary/10 blur-3xl transition-opacity duration-700 pointer-events-none"
            aria-hidden="true"
          />

          <div className="relative overflow-hidden rounded-[32px] sm:rounded-[44px] border border-border-strong/90 bg-canvas-ivory px-6 py-20 sm:px-12 sm:py-28 md:py-36 text-center shadow-[0_24px_64px_-12px_rgba(23,24,23,0.18),0_8px_24px_rgba(23,24,23,0.08)]">
            {/* Atmospheric Cloud Texture Blending Inside Box */}
            <div className="absolute inset-0 z-0 overflow-hidden pointer-events-none">
              <Image
                src="/landing_images/hero-clouds.jpg"
                alt="Atmospheric clouds texture"
                fill
                sizes="100vw"
                className="object-cover object-center opacity-40 mix-blend-multiply"
              />
            </div>

            {/* Inner Precision Border Inset */}
            <div
              className="pointer-events-none absolute inset-3 sm:inset-5 rounded-[24px] sm:rounded-[36px] border border-white/40 mix-blend-overlay z-[2]"
              aria-hidden="true"
            />

            {/* Subtle Gradient Shade from Bottom */}
            <div
              className="absolute inset-0 z-[1] pointer-events-none bg-gradient-to-t from-canvas-ivory/80 via-transparent to-canvas-ivory/40"
              aria-hidden="true"
            />

            {/* Foreground Content Inside Big Box */}
            <RevealStagger className="relative z-10 mx-auto max-w-4xl flex flex-col items-center">
              <RevealItem>
                <Ornament className="mb-6 h-4 w-48 text-ink-secondary/60" />
              </RevealItem>
              <RevealItem>
                <h2 className="font-serif font-normal text-[clamp(2.5rem,5.5vw,4.75rem)] leading-[1.08] tracking-tight text-ink-primary animate-gold-glow">
                  Understand more.<br />
                  <span className="italic text-ink-secondary">Step into your classroom.</span>
                </h2>
              </RevealItem>

              {/* Cursive Handwriting Accent */}
              <RevealItem>
                <Handwriting
                  text="Your personal chalkboard tutor awaits."
                  pace={0.05}
                  className="font-cursive text-coral-primary text-xl sm:text-2xl mt-3 tracking-wide"
                />
              </RevealItem>

              <RevealItem>
                <p className="mx-auto mt-6 max-w-2xl text-base sm:text-lg leading-relaxed text-ink-secondary">
                  Experience a personal AI tutor that listens, sketches derivations on a live chalkboard,
                  and reasons alongside you at every step.
                </p>
              </RevealItem>

              <RevealItem className="w-full sm:w-auto">
                <div className="mt-11 flex flex-col sm:flex-row items-center justify-center gap-4 w-full sm:w-auto">
                  <Link
                    href="/onboarding"
                    className="inline-flex items-center justify-center gap-2.5 rounded-full bg-ink-primary px-8 py-4 font-mono text-sm uppercase tracking-wider text-surface-white shadow-md transition-all duration-300 hover:bg-ink-secondary hover:shadow-lg hover:-translate-y-0.5 active:translate-y-0"
                  >
                    <span>Begin Free Session</span>
                    <ArrowRight className="h-4 w-4" />
                  </Link>
                  <Link
                    href="/login"
                    className="inline-flex items-center justify-center gap-2 rounded-full border border-border-strong bg-surface-white/80 backdrop-blur-xs px-7 py-4 font-mono text-sm tracking-wider text-ink-primary transition-all duration-300 hover:bg-surface-white hover:border-ink-primary hover:shadow-sm"
                  >
                    <span>Existing student sign in</span>
                  </Link>
                </div>
              </RevealItem>
            </RevealStagger>
          </div>
        </motion.div>
      </div>
    </section>
  )
}

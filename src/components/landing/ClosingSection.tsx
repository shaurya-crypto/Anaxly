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
            className="absolute -inset-4 sm:-inset-6 rounded-[40px] sm:rounded-[48px] lg:rounded-[56px] bg-ink-primary/[0.08] blur-2xl -z-10 pointer-events-none transition-all duration-500 group-hover:bg-ink-primary/[0.14] group-hover:blur-3xl"
            aria-hidden="true"
          />

          <div className="relative overflow-hidden rounded-3xl sm:rounded-[40px] lg:rounded-[48px] border border-border-strong/80 bg-surface-soft shadow-[0_32px_90px_-20px_rgba(23,24,23,0.22),0_12px_35px_-8px_rgba(23,24,23,0.12),0_0_60px_rgba(248,246,240,0.85)] transition-transform duration-500 ease-out group-hover:scale-[1.01] py-28 sm:py-36 lg:py-44 min-h-[580px] sm:min-h-[660px] flex flex-col justify-center items-center px-6 sm:px-12 text-center">
            {/* Background Moving Classical Neoclassical Arches Image */}
            <div className="absolute inset-0 z-0 overflow-hidden pointer-events-none">
              <Image
                src="/landing_images/footer_final.jpg"
                alt="Three monumental neoclassical stone arches framing misty mountain summits and morning skies"
                fill
                sizes="(max-width: 1440px) 100vw, 1440px"
                className="object-cover object-center animate-kenburns scale-105 transition-transform duration-700 ease-out group-hover:scale-110"
              />
            </div>

            {/* Inward Edge Shadow Shading & Edge Chiaroscuro Feathering */}
            <div
              className="absolute inset-0 z-[1] pointer-events-none shadow-[inset_0_0_90px_rgba(23,24,23,0.32),inset_0_0_160px_rgba(23,24,23,0.16)]"
              aria-hidden="true"
            />

            {/* Atmospheric Soft Ivory Gradient Veils for High Contrast Readability */}
            <div
              className="absolute inset-0 z-[2] pointer-events-none bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-canvas-ivory/55 via-canvas-ivory/80 to-canvas-ivory/95"
              aria-hidden="true"
            />
            <div
              className="absolute inset-0 z-[2] pointer-events-none bg-gradient-to-b from-canvas-ivory/80 via-transparent to-canvas-ivory/90"
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
                  className="inline-flex items-center justify-center gap-2.5 rounded-full bg-coral-primary px-9 py-4 text-base font-medium text-surface-white shadow-md transition-all duration-300 hover:bg-coral-hover hover:shadow-[0_8px_30px_rgba(37,93,136,0.35)] active:scale-[0.98]"
                >
                  <span>Enter the classroom</span>
                  <ArrowRight className="h-4 w-4" />
                </Link>

                <Link
                  href="/login"
                  className="inline-flex items-center justify-center rounded-full border border-border-strong bg-surface-white/95 backdrop-blur-sm px-8 py-4 text-base font-medium text-ink-primary shadow-xs transition-colors duration-200 hover:bg-surface-soft hover:border-ink-muted"
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

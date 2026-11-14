'use client'

import React, { useRef } from 'react'
import { motion, useInView, useScroll, useSpring } from 'motion/react'
import { ArtworkFrame } from './ArtworkFrame'
import { Reveal } from './motion/Reveal'
import { Parallax } from './motion/Parallax'
import { Handwriting } from './motion/Handwriting'
import { ChalkDerivation, OrbitSketch, QuillNotes } from './illustrations'
import { getArtwork } from '@/lib/landing-artwork'

type Step = {
  num: string
  title: string
  description: string
  tag: string
  Illustration: React.ComponentType<{ className?: string }>
}

/** One stage of the ladder; its numeral lights up while it holds the viewport centre. */
function StepRow({ step, isLast }: { step: Step; isLast: boolean }) {
  const ref = useRef<HTMLDivElement>(null)
  const isActive = useInView(ref, { margin: '-45% 0px -45% 0px' })
  const { Illustration } = step

  return (
    <div ref={ref} className="group relative flex gap-6">
      {/* Numeral Marker */}
      <div className="flex flex-col items-center">
        <span
          className={`relative z-10 flex h-11 w-11 shrink-0 items-center justify-center rounded-xl border bg-surface-white font-mono text-sm font-semibold shadow-xs transition-colors duration-500 ${
            isActive
              ? 'border-coral-primary text-coral-primary'
              : 'border-border-strong text-ink-primary group-hover:border-coral-primary group-hover:text-coral-primary'
          }`}
        >
          {step.num}
        </span>
        {!isLast && <div className="my-2 h-full w-[1px]" />}
      </div>

      {/* Content */}
      <div className="flex-1 pb-4">
        <span className="font-mono text-[11px] uppercase tracking-wider text-botanical-primary">
          {step.tag}
        </span>
        <h3 className="mt-1 font-serif text-xl sm:text-2xl text-ink-primary">{step.title}</h3>
        <p className="mt-2 text-sm sm:text-base leading-relaxed text-ink-secondary">
          {step.description}
        </p>
      </div>

      <Illustration className="hidden sm:block h-20 w-20 shrink-0 self-center text-ink-primary/55" />
    </div>
  )
}

export function LearningFlow() {
  const learningArtwork = getArtwork('learningArtwork')
  const stepsRef = useRef<HTMLDivElement>(null)

  // The connecting ink line is drawn down the ladder as the steps scroll through centre
  const { scrollYProgress } = useScroll({ target: stepsRef, offset: ['start 60%', 'end 50%'] })
  const lineScale = useSpring(scrollYProgress, { stiffness: 100, damping: 28 })

  const steps: Step[] = [
    {
      num: '01',
      title: 'Ground in everyday physical intuition',
      description:
        'Every concept begins with a tangible, real-world hook. Before looking at equations, you explore the underlying intuition through guided questions.',
      tag: 'Intuitive Foundation',
      Illustration: OrbitSketch,
    },
    {
      num: '02',
      title: 'Voice dialogue with live derivations',
      description:
        'Engage in natural conversation. The tutor writes derivations live on the chalkboard, checking your comprehension every two to three sentences.',
      tag: 'Continuous Reasoning',
      Illustration: ChalkDerivation,
    },
    {
      num: '03',
      title: 'Permanent mastery through problem-solving',
      description:
        'Tackle rigorous numerical problems formatted with clear steps: Given, Formula, Substitution, and Boxed Answers. All chalkboard work becomes your permanent Master Notes.',
      tag: 'Lifelong Rigor',
      Illustration: QuillNotes,
    },
  ]

  return (
    <section id="flow" className="relative scroll-mt-20 py-20 lg:py-28">
      <div className="mx-auto max-w-7xl px-6 lg:px-12">
        <div className="grid grid-cols-1 gap-12 lg:grid-cols-12 lg:gap-16 lg:items-center">
          {/* Left Column: The 3 Steps with JetBrains Mono Numbers */}
          <div className="lg:col-span-6 flex flex-col">
            <Reveal>
              <p className="font-mono text-xs uppercase tracking-widest text-ink-muted">
                The Three Stages of Mastery
              </p>
              <h2 className="mt-2 font-serif text-3xl sm:text-4xl lg:text-5xl text-ink-primary">
                How true comprehension is built.
              </h2>

              {/* Cursive Handwriting Marginalia */}
              <Handwriting
                text="Mastery is not memorization — it is the dialogue between intuition and rigor."
                className="font-cursive text-coral-primary text-xl sm:text-2xl mt-2 tracking-wide"
              />

              <p className="mt-4 text-base text-ink-secondary leading-relaxed">
                Learning is not a sprint through pre-recorded video lectures. It is a disciplined,
                dialogue-driven progression that builds lifelong conceptual clarity from first principles.
              </p>
            </Reveal>

            {/* Disciplined Step List */}
            <div ref={stepsRef} className="relative mt-10 space-y-8">
              {/* Static guide rail + scroll-drawn coral ink line behind the numerals */}
              <div className="absolute left-[22px] top-11 bottom-16 w-px bg-border-subtle" aria-hidden="true" />
              <motion.div
                style={{ scaleY: lineScale }}
                className="absolute left-[22px] top-11 bottom-16 w-px origin-top bg-coral-primary/70"
                aria-hidden="true"
              />
              {steps.map((step, idx) => (
                <Reveal key={step.num}>
                  <StepRow step={step} isLast={idx === steps.length - 1} />
                </Reveal>
              ))}
            </div>
          </div>

          {/* Right Column: Classical Ascending Staircase Artwork */}
          <div className="lg:col-span-6 flex flex-col">
            <Parallax className="relative" distance={36}>
              {/* Decorative Archival Corner accents */}
              <div className="absolute -top-2.5 -left-2.5 h-4 w-4 border-t border-l border-border-strong pointer-events-none" />
              <div className="absolute -bottom-2.5 -right-2.5 h-4 w-4 border-b border-r border-border-strong pointer-events-none" />

              <ArtworkFrame
                artwork={learningArtwork}
                aspectRatioClass="aspect-[4/3] sm:aspect-[16/11]"
                priority={false}
                showCaption={true}
              />

              {/* Editorial marginalia block below artwork */}
              <div className="mt-5 border-l-2 border-border-strong/70 pl-4 py-1">
                <p className="text-xs leading-relaxed text-ink-secondary">
                  &ldquo;A student who understands the derivation never needs to memorize the formula.&rdquo;
                </p>
                <div className="mt-1 flex items-center gap-2 font-mono text-[10px] text-ink-muted">
                  <span>Plato&apos;s Academy Method</span>
                  <span>&bull;</span>
                  <span className="font-sans italic text-ink-muted">Classical Foundation of Rigor</span>
                </div>
              </div>
            </Parallax>
          </div>
        </div>
      </div>
    </section>
  )
}

'use client'

import React from 'react'
import { ArtworkFrame } from './ArtworkFrame'
import { Reveal } from './motion/Reveal'
import { ChalkDerivation, OrbitSketch, PrismSketch, SpeechDialogue } from './illustrations'
import { getArtwork } from '@/lib/landing-artwork'

export function ProductExperience() {
  const scholarArtwork = getArtwork('featureArtwork')
  const libraryArtwork = getArtwork('featureLibraryArtwork')

  const principles = [
    {
      num: '01',
      title: 'The Socratic Voice Cadence',
      Illustration: SpeechDialogue,
      body: (
        <>
          Unlike recorded video courses or generic chat windows, the tutor adheres strictly to a 2–3
          sentence rule: it never speaks continuously without engaging the student or checking understanding.
          Every fundamental law is introduced first through everyday physical intuition before formal
          mathematical statement.
        </>
      ),
    },
    {
      num: '02',
      title: 'Live Chalkboard as the Single Source of Truth',
      Illustration: ChalkDerivation,
      body: (
        <>
          As the lesson unfolds, the tutor writes derivations, given parameters, and calculation steps
          live on the green chalkboard. There is no separate post-session notes generation — the live chalkboard
          drawings and handwritten steps themselves are preserved directly as your permanent Master Notes.
        </>
      ),
    },
    {
      num: '03',
      title: 'First-Principles Derivation Over Rote Memorization',
      Illustration: OrbitSketch,
      body: (
        <>
          Formulas are never treated as arbitrary recipes. The tutor co-solves with you step-by-step:
          starting from observed physical constraints, isolating variables with algebraic rigor, and
          verifying the physical units of every final result.
        </>
      ),
    },
    {
      num: '04',
      title: '3D Spatial Clarity & Permanent Memory',
      Illustration: PrismSketch,
      body: (
        <>
          When abstract formulas need physical clarity, interactive 3D simulations appear alongside the
          chalkboard for optics, mechanics, and geometric reasoning. The tutor retains permanent memory
          of your cognitive strengths and conceptual hurdles, ensuring every session builds seamlessly forward.
        </>
      ),
    },
  ]

  return (
    <section id="experience" className="relative scroll-mt-20 py-20 lg:py-28">
      <div className="mx-auto max-w-7xl px-6 lg:px-12">
        {/* Section Header: Universal Product Storytelling */}
        <Reveal className="max-w-3xl">
          <p className="font-mono text-xs uppercase tracking-widest text-coral-primary font-medium">
            The Architecture of Inquiry
          </p>
          <h2 className="mt-2 font-serif text-3xl sm:text-4xl lg:text-5xl text-ink-primary">
            Four principles of genuine understanding.
          </h2>
          <p className="mt-4 text-base sm:text-lg leading-relaxed text-ink-secondary">
            Learning is not a monologue. Anaxly replaces passive video watching with active voice
            reasoning, live chalkboard derivations, and spatial physical clarity.
          </p>
        </Reveal>

        {/* Master Product Editorial Layout */}
        <div className="mt-14 grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-start">
          {/* Left Column: Big Editorial Image */}
          <div className="lg:col-span-6 flex flex-col space-y-8">
            <div className="relative">
              {/* Decorative Archival Corner accents */}
              <div className="absolute -top-2.5 -left-2.5 h-4 w-4 border-t border-l border-border-strong pointer-events-none" />
              <div className="absolute -bottom-2.5 -right-2.5 h-4 w-4 border-b border-r border-border-strong pointer-events-none" />

              <ArtworkFrame
                artwork={libraryArtwork}
                aspectRatioClass="aspect-[4/3] sm:aspect-[16/11]"
                priority={false}
                showCaption={true}
              />
            </div>

            {/* Editorial Caption Note */}
            <Reveal className="border-l-2 border-coral-primary/60 pl-4 py-1">
              <p className="font-serif italic text-base text-ink-primary">
                &ldquo;True learning begins when a student is prompted to articulate why, not merely recite what.&rdquo;
              </p>
              <p className="mt-1.5 font-mono text-[11px] text-ink-muted uppercase tracking-wider">
                The Socratic Principle of Education
              </p>
            </Reveal>

            {/* Second artwork + session cues fill the column alongside the principles */}
            <Reveal className="grid grid-cols-1 sm:grid-cols-5 gap-6 items-start">
              <div className="sm:col-span-3">
                <ArtworkFrame
                  artwork={scholarArtwork}
                  aspectRatioClass="aspect-[16/10]"
                  priority={false}
                  showCaption={false}
                />
              </div>
              <ul className="sm:col-span-2 divide-y divide-border-subtle border-y border-border-subtle">
                {[
                  ['2–3', 'sentences per turn, then a question back to you'],
                  ['Live', 'chalkboard steps become your Master Notes'],
                  ['Units', 'checked on every final answer'],
                ].map(([k, v]) => (
                  <li key={k} className="py-3">
                    <p className="font-serif text-xl text-ink-primary">{k}</p>
                    <p className="mt-0.5 text-xs leading-snug text-ink-muted">{v}</p>
                  </li>
                ))}
              </ul>
            </Reveal>
          </div>

          {/* Right Column: Clear, Deep Description of What It Is & Why It Is Best */}
          <div className="lg:col-span-6 flex flex-col divide-y divide-border-subtle border-t border-border-subtle">
            {principles.map(({ num, title, Illustration, body }) => (
              <Reveal key={num} className="group py-8 first:pt-7">
                <div className="grid grid-cols-[auto_1fr] gap-x-5 sm:gap-x-7">
                  {/* Editorial numeral */}
                  <span
                    aria-hidden="true"
                    className="font-serif italic text-4xl sm:text-5xl leading-none text-coral-primary opacity-70 tabular-nums transition-opacity duration-300 group-hover:opacity-100"
                  >
                    {num}
                  </span>
                  <div className="min-w-0">
                    <div className="flex items-start justify-between gap-5">
                      <div className="min-w-0">
                        <span className="font-mono text-[11px] uppercase tracking-[0.18em] text-ink-muted">
                          Principle {num}
                        </span>
                        <h3 className="mt-1 font-serif text-xl sm:text-2xl leading-snug text-ink-primary">{title}</h3>
                      </div>
                      {/* Hand-drawn ink illustration that sketches itself on scroll */}
                      <Illustration className="h-14 w-14 sm:h-16 sm:w-16 shrink-0 text-ink-primary/60 transition-colors duration-300 group-hover:text-ink-primary/85" />
                    </div>
                    <p className="mt-3 text-sm sm:text-[15px] leading-relaxed text-ink-secondary">{body}</p>
                  </div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}

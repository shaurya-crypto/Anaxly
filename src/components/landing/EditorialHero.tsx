'use client'

import React, { useRef, useEffect, useState, useCallback, useMemo } from 'react'
import { motion, useScroll, useTransform, MotionValue } from 'motion/react'
import { preload } from 'react-dom'

const TOTAL_FRAMES = 144

/**
 * Individual Word component with scroll-driven blur and illumination transition.
 * Transitions smoothly from soft blur + medium opacity to razor-sharp, glowing pure white.
 */
function BlurWord({
  word,
  progress,
  range,
}: {
  word: string
  progress: MotionValue<number>
  range: [number, number]
}) {
  const [start, end] = range
  // Words start softly visible (0.35 opacity) and bloom into 1.0 brilliant white
  const opacity = useTransform(progress, [start, end], [0.35, 1])
  const y = useTransform(progress, [start, end], [8, 0])

  return (
    <motion.span
      style={{ opacity, y }}
      className="inline-block mx-1 sm:mx-2 md:mx-2.5 will-change-transform select-none text-[#FFFFFF]"
    >
      {word}
    </motion.span>
  )
}

/**
 * Single-Sentence Word Blur Component.
 * Illuminates one word at a time on scroll with a monumental, bright white serif italic glow.
 * Normal, editorial, and perfectly legible with subtle calligraphic elegance.
 */
function WordBlurSentence({
  sentence,
  progress,
  revealRange,
  visibilityRange,
}: {
  sentence: string
  progress: MotionValue<number>
  revealRange: [number, number]
  visibilityRange: [number, number, number, number]
}) {
  const words = useMemo(() => sentence.split(' '), [sentence])
  const [revealStart, revealEnd] = revealRange
  const [visInStart, visInEnd, visOutStart, visOutEnd] = visibilityRange

  const containerOpacity = useTransform(
    progress,
    [visInStart, visInEnd, visOutStart, visOutEnd],
    [0, 1, 1, 0]
  )

  const containerY = useTransform(
    progress,
    [visInStart, visInEnd, visOutStart, visOutEnd],
    [28, 0, 0, -24]
  )

  const containerScale = useTransform(
    progress,
    [visInStart, visInEnd, visOutStart, visOutEnd],
    [0.96, 1, 1, 0.98]
  )

  const step = (revealEnd - revealStart) / words.length

  return (
    <motion.div
      style={{
        opacity: containerOpacity,
        y: containerY,
        scale: containerScale,
      }}
      className="absolute inset-0 flex items-center justify-center pointer-events-none px-6 sm:px-12"
    >
      <div className="relative max-w-3xl lg:max-w-4xl text-center py-6 px-4">
        {/* Subtle localized soft back-glow directly behind text for maximum contrast against bright video */}
        <div
          className="absolute inset-0 -inset-x-8 -z-10 rounded-full bg-black/30 blur-3xl pointer-events-none"
          aria-hidden="true"
        />

        <h2 className="font-serif font-normal not-italic text-[#FFFFFF] text-glow-cinematic text-xl sm:text-2xl md:text-3xl lg:text-4xl xl:text-[2.65rem] tracking-[-0.015em] leading-[1.32]">
          {words.map((word, idx) => {
            const wStart = revealStart + idx * step
            const wEnd = Math.min(revealEnd, wStart + step * 0.92)
            return (
              <BlurWord
                key={`${word}-${idx}`}
                word={word}
                progress={progress}
                range={[wStart, wEnd]}
              />
            )
          })}
        </h2>
      </div>
    </motion.div>
  )
}

export function EditorialHero() {
  const containerRef = useRef<HTMLDivElement>(null)
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const imagesRef = useRef<HTMLImageElement[]>([])
  const currentFrameRef = useRef<number>(1)
  const targetFrameRef = useRef<number>(1)
  const rafIdRef = useRef<number | null>(null)
  const ctxRef = useRef<CanvasRenderingContext2D | null>(null)
  const lastDrawnRef = useRef<HTMLImageElement | null>(null)
  const wakeRef = useRef<() => void>(() => {})
  // LCP: get the first hero frame into the <head> as a high-priority preload.
  preload('/hero-frames/frame_001.webp', { as: 'image', fetchPriority: 'high' })
  const [firstFrameLoaded, setFirstFrameLoaded] = useState(false)

  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start start', 'end end'],
  })

  // Dissolve the sticky stage into the paper canvas, and retire the scroll cue early
  const paperFadeOpacity = useTransform(scrollYProgress, [0.9, 1], [0, 1])
  const cueOpacity = useTransform(scrollYProgress, [0, 0.05], [1, 0])

  // Render a specific frame to canvas preserving cover aspect ratio
  const renderFrame = useCallback((frameIndex: number) => {
    const canvas = canvasRef.current
    if (!canvas) return
    // Cache the 2D context instead of looking it up every frame.
    if (!ctxRef.current) ctxRef.current = canvas.getContext('2d')
    const ctx = ctxRef.current
    if (!ctx) return

    const safeIndex = Math.min(TOTAL_FRAMES, Math.max(1, frameIndex))
    // Frames stream in progressively; draw the nearest one that's ready.
    const images = imagesRef.current
    const ready = (i: number) => {
      const im = images[i]
      return im && im.complete && im.naturalWidth > 0 ? im : null
    }
    let img: HTMLImageElement | null = null
    for (let d = 0; d < TOTAL_FRAMES && !img; d++) {
      img = ready(safeIndex - 1 - d) || ready(safeIndex - 1 + d)
    }
    if (!img) return
    // Same picture already on the canvas: skip the (expensive) full-screen redraw.
    if (img === lastDrawnRef.current) return
    lastDrawnRef.current = img

    const width = canvas.width
    const height = canvas.height
    // No clearRect: the cover-fit image always paints every pixel.

    const imgRatio = img.naturalWidth / img.naturalHeight
    const canvasRatio = width / height

    let drawWidth = width
    let drawHeight = height
    let offsetX = 0
    let offsetY = 0

    if (canvasRatio > imgRatio) {
      drawHeight = width / imgRatio
      offsetY = (height - drawHeight) / 2
    } else {
      drawWidth = height * imgRatio
      offsetX = (width - drawWidth) / 2
    }

    ctx.drawImage(img, offsetX, offsetY, drawWidth, drawHeight)
  }, [])

  // Resize canvas with devicePixelRatio
  const handleResize = useCallback(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const displayWidth = window.innerWidth
    const displayHeight = window.innerHeight
    // Frames are 1920×1080. A backing store larger than the cover-fit source adds
    // no detail, only pixels to push each frame, so cap the ratio at what the
    // source can actually fill (never below 1, so nothing gets softer than before).
    const coverScale = Math.max(displayWidth / 1920, displayHeight / 1080)
    const dpr = Math.max(1, Math.min(window.devicePixelRatio || 1, 2, 1 / coverScale))

    canvas.width = displayWidth * dpr
    canvas.height = displayHeight * dpr
    canvas.style.width = `${displayWidth}px`
    canvas.style.height = `${displayHeight}px`

    lastDrawnRef.current = null // resizing clears the canvas; force a redraw
    renderFrame(Math.round(currentFrameRef.current))
  }, [renderFrame])

  // Load frame 1 right away, then stream the rest in the background:
  // coarse keyframes first (so scrubbing works early), a few at a time,
  // only once the visitor starts scrolling. Phones / data-saver get every 2nd frame.
  useEffect(() => {
    const images: HTMLImageElement[] = new Array(TOTAL_FRAMES)
    imagesRef.current = images
    let cancelled = false

    const loadFrame = (idx: number) =>
      new Promise<void>((resolve) => {
        const img = new window.Image()
        img.decoding = 'async'
        img.onload = () => {
          // Decode off the main thread first, so drawing it later never stalls a scroll frame.
          const ready = () => {
            images[idx] = img
            resolve()
          }
          if (typeof img.decode === 'function') img.decode().then(ready, ready)
          else ready()
        }
        img.onerror = () => resolve()
        img.src = `/hero-frames/frame_${String(idx + 1).padStart(3, '0')}.webp`
      })

    const conn = (navigator as Navigator & { connection?: { saveData?: boolean } }).connection
    const lite = window.innerWidth < 768 || conn?.saveData === true
    const step = lite ? 2 : 1

    const order: number[] = []
    const seen = new Set<number>([0])
    for (const stride of [16, 8, 4, 2, 1]) {
      if (stride < step) break
      for (let i = 0; i < TOTAL_FRAMES; i += stride) {
        if (!seen.has(i)) {
          seen.add(i)
          order.push(i)
        }
      }
    }

    const streamRest = async () => {
      const CONCURRENCY = 4
      let cursor = 0
      const worker = async () => {
        while (!cancelled && cursor < order.length) {
          await loadFrame(order[cursor++])
        }
      }
      await Promise.all(Array.from({ length: CONCURRENCY }, worker))
    }

    loadFrame(0).then(() => {
      if (cancelled) return
      setFirstFrameLoaded(true)
      handleResize()
      // Don't fetch the remaining ~12 MB of frames until the visitor actually
      // starts scrolling (or interacts) — keeps the initial load light.
      const start = () => {
        window.removeEventListener('scroll', start)
        window.removeEventListener('wheel', start)
        window.removeEventListener('touchstart', start)
        window.removeEventListener('keydown', start)
        if (!cancelled) void streamRest()
      }
      const opts = { passive: true, once: true } as const
      window.addEventListener('scroll', start, opts)
      window.addEventListener('wheel', start, opts)
      window.addEventListener('touchstart', start, opts)
      window.addEventListener('keydown', start, { once: true })
    })

    window.addEventListener('resize', handleResize)
    return () => {
      cancelled = true
      window.removeEventListener('resize', handleResize)
    }
  }, [handleResize])

  // Lerp animation loop for smooth scrubbing. Same easing as before, but it only
  // runs while the frame is catching up to the scroll position, then goes idle
  // instead of burning a requestAnimationFrame callback forever.
  useEffect(() => {
    let isRunning = true
    let active = false

    const tick = () => {
      if (!isRunning) return

      const target = targetFrameRef.current
      const current = currentFrameRef.current
      const diff = target - current

      if (Math.abs(diff) > 0.01) {
        // Damping factor of 0.12 provides responsive yet buttery smooth gliding
        const next = current + diff * 0.12
        currentFrameRef.current = next
        renderFrame(Math.round(next))
        rafIdRef.current = requestAnimationFrame(tick)
      } else {
        active = false
        rafIdRef.current = null
      }
    }

    wakeRef.current = () => {
      if (active || !isRunning) return
      active = true
      rafIdRef.current = requestAnimationFrame(tick)
    }
    wakeRef.current()

    return () => {
      isRunning = false
      wakeRef.current = () => {}
      if (rafIdRef.current) cancelAnimationFrame(rafIdRef.current)
    }
  }, [renderFrame])

  // Update target frame smoothly from Lenis-backed scroll progress
  useEffect(() => {
    const unsubscribe = scrollYProgress.on('change', (progress) => {
      const clamped = Math.max(0, Math.min(1, progress))
      targetFrameRef.current = 1 + clamped * (TOTAL_FRAMES - 1)
      wakeRef.current()
    })

    return () => unsubscribe()
  }, [scrollYProgress])

  return (
    <div ref={containerRef} id="what-it-is" className="relative h-[250vh]">
      {/* Sticky Full-Viewport Stage with 100% Raw Video Clarity (No Dark or White Overlays) */}
      <div className="sticky top-0 h-screen w-full overflow-hidden flex items-center justify-center">
        {/* Hardware-Accelerated Canvas for Smooth Scrubbing */}
        <canvas
          ref={canvasRef}
          className={`absolute inset-0 z-0 pointer-events-none transition-opacity duration-700 ${
            firstFrameLoaded ? 'opacity-100' : 'opacity-0'
          }`}
        />

        {/* Fallback Poster before first frame decodes */}
        {!firstFrameLoaded && (
          // eslint-disable-next-line @next/next/no-img-element
          <img
            src="/hero-frames/frame_001.webp"
            alt=""
            fetchPriority="high"
            className="absolute inset-0 z-0 h-full w-full object-cover pointer-events-none"
          />
        )}

        {/* SCENE 1: Single Sentence Word-by-Word Blur Reveal */}
        <WordBlurSentence
          sentence="The new era of education begins in dialogue, not a lecture."
          progress={scrollYProgress}
          revealRange={[0.05, 0.38]}
          visibilityRange={[0.0, 0.05, 0.42, 0.49]}
        />

        {/* SCENE 2: Single Sentence Word-by-Word Blur Reveal */}
        <WordBlurSentence
          sentence="A personal tutor reasoning alongside you, deriving every law live on your chalkboard."
          progress={scrollYProgress}
          revealRange={[0.52, 0.85]}
          visibilityRange={[0.48, 0.53, 0.90, 0.98]}
        />

        {/* Scroll cue: a slow falling ink line */}
        <motion.div
          style={{ opacity: cueOpacity }}
          className="absolute bottom-8 left-1/2 z-10 -translate-x-1/2 flex flex-col items-center gap-2 pointer-events-none"
          aria-hidden="true"
        >
          <span className="font-mono text-xs uppercase tracking-[0.3em] text-white/80">Scroll</span>
          <span className="relative block h-10 w-px overflow-hidden bg-white/25">
            <span className="absolute inset-x-0 top-0 h-1/2 bg-white animate-scroll-cue" />
          </span>
        </motion.div>

        {/* Ivory dissolve into the next section */}
        <motion.div
          style={{ opacity: paperFadeOpacity }}
          className="absolute inset-x-0 bottom-0 z-10 h-2/5 bg-gradient-to-t from-canvas-ivory via-canvas-ivory/70 to-transparent pointer-events-none"
          aria-hidden="true"
        />
      </div>
    </div>
  )
}

'use client'

import React, { useEffect, useRef, useState, useCallback } from 'react'
import { usePathname } from 'next/navigation'
import { createAvatar, type AvatarController } from '@bible-strong/avatar-react'
import '@bible-strong/avatar-react/styles.css'
import avatarDefinition from '@/avatar.avatar.json'
import { X, Sparkles, AlertCircle, HelpCircle, Key, ArrowRight } from 'lucide-react'

// Available animations in cloudee.avatar.json:
// ['sleeping', 'waking', 'idle', 'listening', 'thinking', 'searching', 'working', 'excited', 'bored', 'suspicious', 'angry', 'drowsy', 'happy', 'curious', 'confused', 'surprised', 'proud', 'shy', 'sad', 'laughing', 'scared', 'playful', 'celebrate']
// Available expressions in cloudee.avatar.json:
// ['neutral', 'joyful-wide', 'attentive-left', 'curious-left', 'surprised-left', 'downward-gaze', 'wide-downward-gaze', 'playful-right', 'upward-side-glance', 'skeptical-left', 'skeptical-right', 'sleepy-squint', 'drowsy-closed', ...]

const SobiAvatar = createAvatar(avatarDefinition as any)

export interface CompanionGuideDetail {
  targetSelector?: string
  targetElementId?: string
  message: string
  animation?: 'idle' | 'listening' | 'working' | 'excited' | 'suspicious' | 'laughing' | 'celebrate' | 'happy' | 'thinking' | 'curious' | string
  expression?: string
  mood?: 'normal' | 'suspicious' | 'warning' | 'celebrate' | 'thinking'
  autoDismissMs?: number
}

// Global helper to guide the mascot to any element on any page
export function triggerCompanionGuidance(detail: CompanionGuideDetail) {
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent('companion-guide', { detail }))
  }
}

// ---------- Step-by-step guided tours (sign-up + first app walkthrough) ----------
export interface TourStep {
  selector: string
  message: string
  animation?: string
  expression?: string
}

interface TourDef {
  key: string
  match: (path: string) => boolean
  steps: TourStep[]
}

const TOURS: TourDef[] = [
  {
    key: 'signup',
    match: (p) => p.startsWith('/login'),
    steps: [
      { selector: '#google-signin-btn', message: "Hi, I'm Sobi! Fastest way in: tap Continue with Google and you're signed up in one click.", animation: 'excited', expression: 'joyful-wide' },
      { selector: '#email', message: 'Prefer email? Type your email address here. No password needed.', animation: 'listening', expression: 'attentive-left' },
      { selector: '#email-continue-btn', message: "Then tap Continue. I'll send a 6-digit code to your inbox.", animation: 'listening' },
      { selector: '#password-signin-toggle', message: 'Already have a password? Use this link to sign in with it instead.', animation: 'curious', expression: 'curious-left' },
    ],
  },
  {
    key: 'dashboard',
    match: (p) => /^\/dashboard\/[^/]+\/?$/.test(p),
    steps: [
      { selector: '#primary-resume-btn, #browse-curriculums-btn', message: 'Welcome aboard! This is where you start or resume your live class with your AI tutor.', animation: 'excited', expression: 'joyful-wide' },
      { selector: '#top-open-syllabus-btn, #hero-open-syllabus-btn', message: 'Open your syllabus to pick any chapter from your class.', animation: 'listening' },
      { selector: '#consistency-section', message: 'Your study rhythm lives here. Study a little each day to keep your streak going.', animation: 'happy' },
      { selector: '#open-quiz-btn', message: 'Test yourself with a quick mastery quiz after each lesson.', animation: 'curious', expression: 'curious-left' },
      { selector: '#enrolled-subjects-section', message: 'All your subjects are listed here. Tap one to jump in.', animation: 'listening' },
      { selector: '#deliberate-practice-section', message: "Practice your weak spots here. That's it, you're ready to learn!", animation: 'celebrate', expression: 'joyful-wide' },
    ],
  },
]

const tourDoneKey = (key: string) => `anaxly_tour_done_${key}`

export function startCompanionTour() {
  if (typeof window !== 'undefined') window.dispatchEvent(new CustomEvent('companion-tour-start'))
}

const DEFAULT_TIPS = [
  "Hi! I'm your AI learning companion. Click me anytime for study tips!",
  "Tip: You can start a live voice class any time.",
  "Keep your streak alive by reviewing one syllabus topic capsule today!",
  "Stuck on a problem? Your tutor can explain with questions, directly, or with visuals.",
]

export function Mascot() {
  const pathname = usePathname()
  const avatarRef = useRef<AvatarController>(null)
  const containerRef = useRef<HTMLDivElement>(null)
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(false)
  const [speechBubbleOpen, setSpeechBubbleOpen] = useState(false)
  const [currentMessage, setCurrentMessage] = useState(DEFAULT_TIPS[0])
  const [currentMood, setCurrentMood] = useState<'normal' | 'suspicious' | 'warning' | 'celebrate' | 'thinking'>('normal')
  const [tipIndex, setTipIndex] = useState(0)
  const [isSleeping, setIsSleeping] = useState(false)

  // Guided tour state
  const [tour, setTour] = useState<{ def: TourDef; steps: TourStep[]; index: number } | null>(null)
  const tourRef = useRef(tour)
  tourRef.current = tour
  const highlightedRef = useRef<HTMLElement | null>(null)

  // Floating coordinates when anchored next to a field or button
  const [anchorCoords, setAnchorCoords] = useState<{ x: number; y: number; side: 'right' | 'left' | 'top' } | null>(null)

  const inactivityTimerRef = useRef<NodeJS.Timeout | null>(null)
  const returnToIdleTimerRef = useRef<NodeJS.Timeout | null>(null)
  const autoDismissTimerRef = useRef<NodeJS.Timeout | null>(null)

  // 1. Detect prefers-reduced-motion
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)')
    setPrefersReducedMotion(mediaQuery.matches)

    const handleChange = (e: MediaQueryListEvent) => {
      setPrefersReducedMotion(e.matches)
    }

    mediaQuery.addEventListener('change', handleChange)
    return () => mediaQuery.removeEventListener('change', handleChange)
  }, [])

  // 2. Play animation safely
  const safePlay = useCallback((anim: string) => {
    if (prefersReducedMotion) return
    try {
      avatarRef.current?.play(anim as any)
    } catch (e) {
      console.warn('[Mascot] play error:', e)
    }
  }, [prefersReducedMotion])

  const safeExpression = useCallback((expr: string) => {
    if (prefersReducedMotion) return
    try {
      avatarRef.current?.setExpression(expr as any)
    } catch (e) {
      console.warn('[Mascot] setExpression error:', e)
    }
  }, [prefersReducedMotion])

  // 3. Reset to idle after reaction
  const resetToIdle = useCallback((delayMs = 3000) => {
    if (returnToIdleTimerRef.current) clearTimeout(returnToIdleTimerRef.current)
    returnToIdleTimerRef.current = setTimeout(() => {
      safePlay('idle')
      setIsSleeping(false)
      setCurrentMood('normal')
    }, delayMs)
  }, [safePlay])

  // Return to bottom-right resting dock
  const returnToDock = useCallback(() => {
    setAnchorCoords(null)
    setCurrentMood('normal')
    safePlay('idle')
    safeExpression('neutral')
    if (autoDismissTimerRef.current) clearTimeout(autoDismissTimerRef.current)
  }, [safePlay, safeExpression])

  // 4. Inactivity watchdog: 35s no movement -> drowsy/sleeping
  const handleUserActivity = useCallback(() => {
    if (isSleeping) {
      setIsSleeping(false)
      safePlay('idle')
    }

    if (inactivityTimerRef.current) clearTimeout(inactivityTimerRef.current)

    if (!prefersReducedMotion) {
      inactivityTimerRef.current = setTimeout(() => {
        setIsSleeping(true)
        safeExpression('drowsy-closed')
      }, 35000)
    }
  }, [isSleeping, prefersReducedMotion, safeExpression, safePlay])

  useEffect(() => {
    if (pathname?.includes('/class/') || pathname === '/') return
    const events = ['mousemove', 'keydown', 'scroll', 'touchstart']
    events.forEach((ev) => window.addEventListener(ev, handleUserActivity, { passive: true }))
    handleUserActivity()

    return () => {
      events.forEach((ev) => window.removeEventListener(ev, handleUserActivity))
      if (inactivityTimerRef.current) clearTimeout(inactivityTimerRef.current)
      if (returnToIdleTimerRef.current) clearTimeout(returnToIdleTimerRef.current)
      if (autoDismissTimerRef.current) clearTimeout(autoDismissTimerRef.current)
    }
  }, [handleUserActivity, pathname])

  // 5. Intelligent Guidance Event Listener (moves ball to anchor & delivers dialogue)
  useEffect(() => {
    if (pathname?.includes('/class/') || pathname === '/') return
    const handleCompanionGuide = (e: Event) => {
      if (tourRef.current) return // a guided tour owns the mascot right now
      const customEvent = e as CustomEvent<CompanionGuideDetail>
      const { targetSelector, targetElementId, message, animation, expression, mood = 'normal', autoDismissMs } = customEvent.detail

      setIsSleeping(false)
      setCurrentMessage(message)
      setCurrentMood(mood)
      setSpeechBubbleOpen(true)

      // Calculate anchor coordinates next to target element
      const selector = targetSelector || (targetElementId ? `#${targetElementId}` : undefined)
      if (selector) {
        const targetEl = document.querySelector(selector)
        if (targetEl) {
          const rect = targetEl.getBoundingClientRect()
          const viewportWidth = window.innerWidth
          const viewportHeight = window.innerHeight

          // Approximate footprint of the speech bubble plus the avatar ball
          const boxW = viewportWidth >= 640 ? 290 : 250
          const boxH = viewportWidth >= 768 ? 240 : 205
          const margin = 8

          // Everything the companion must not cover: controls and text blocks
          const blockers = Array.from(
            document.querySelectorAll<HTMLElement>(
              'a[href], button, input, select, textarea, [role="button"], h1, h2, h3, h4, p, li, label'
            )
          )
            .filter((el) => !containerRef.current?.contains(el))
            .map((el) => el.getBoundingClientRect())
            .filter((r) => r.width > 0 && r.height > 0 && r.bottom > 0 && r.top < viewportHeight)

          const isClear = (x: number, y: number) =>
            blockers.every((r) => x >= r.right || x + boxW <= r.left || y >= r.bottom || y + boxH <= r.top)

          const clampX = (x: number) => Math.min(viewportWidth - boxW - margin, Math.max(margin, x))
          const clampY = (y: number) => Math.min(viewportHeight - boxH - margin, Math.max(margin, y))

          const candidates: Array<{ x: number; y: number; side: 'right' | 'left' | 'top' }> = [
            { x: rect.right + 16, y: rect.top - 20, side: 'right' },
            { x: rect.left - boxW - 16, y: rect.top - 20, side: 'left' },
            { x: rect.left, y: rect.top - boxH - margin, side: 'top' },
            { x: rect.left, y: rect.bottom + margin, side: 'top' },
          ]

          const clear = candidates
            .map((c) => ({ ...c, x: clampX(c.x), y: clampY(c.y) }))
            // Clamping must not have pushed the box back over the target itself
            .filter(
              (c) =>
                c.x >= rect.right || c.x + boxW <= rect.left || c.y >= rect.bottom || c.y + boxH <= rect.top
            )
            .find((c) => isClear(c.x, c.y))

          // No clear spot next to the target: stay in the bottom-right dock
          setAnchorCoords(clear ?? null)
        }
      }

      // Execute requested animation and facial expression
      if (animation) {
        safePlay(animation)
      } else if (mood === 'suspicious' || mood === 'warning') {
        safePlay('suspicious')
      } else if (mood === 'celebrate') {
        safePlay('excited')
      } else {
        safePlay('listening')
      }

      if (expression) {
        safeExpression(expression)
      } else if (mood === 'suspicious') {
        safeExpression('suspicious-right')
      } else if (mood === 'warning') {
        safeExpression('skeptical-left')
      } else if (mood === 'celebrate') {
        safeExpression('joyful-wide')
      }

      // Optional auto-dismiss back to dock
      if (autoDismissTimerRef.current) clearTimeout(autoDismissTimerRef.current)
      if (autoDismissMs) {
        autoDismissTimerRef.current = setTimeout(() => {
          returnToDock()
        }, autoDismissMs)
      } else if (mood !== 'suspicious' && mood !== 'warning') {
        // Normal tips dismiss after 8 seconds
        autoDismissTimerRef.current = setTimeout(() => {
          setSpeechBubbleOpen(false)
          returnToDock()
        }, 9000)
      }
    }

    window.addEventListener('companion-guide', handleCompanionGuide)
    return () => window.removeEventListener('companion-guide', handleCompanionGuide)
  }, [safePlay, safeExpression, returnToDock, pathname])

  // 6. Global Reaction Listener (backward compatibility)
  useEffect(() => {
    if (pathname?.includes('/class/') || pathname === '/') return
    const handleGlobalReaction = (e: Event) => {
      const customEvent = e as CustomEvent<string>
      const reaction = customEvent.detail
      if (['idle', 'listening', 'working', 'excited', 'suspicious', 'laughing'].includes(reaction)) {
        safePlay(reaction as any)
        resetToIdle(3000)
      } else if (reaction === 'celebrate') {
        safePlay('excited')
        setSpeechBubbleOpen(true)
        resetToIdle(3000)
      } else if (reaction === 'confused' || reaction === 'error') {
        safeExpression('surprised-left')
        safePlay('suspicious')
        resetToIdle(3000)
      }
    }

    window.addEventListener('mascot-react', handleGlobalReaction)
    return () => window.removeEventListener('mascot-react', handleGlobalReaction)
  }, [safePlay, safeExpression, resetToIdle, pathname])

  // 7. Guided tour engine
  const clearHighlight = useCallback(() => {
    const el = highlightedRef.current
    if (el) {
      el.style.outline = el.dataset.tourPrevOutline || ''
      el.style.outlineOffset = el.dataset.tourPrevOffset || ''
      delete el.dataset.tourPrevOutline
      delete el.dataset.tourPrevOffset
    }
    highlightedRef.current = null
  }, [])

  const endTour = useCallback((markDone = true) => {
    const t = tourRef.current
    if (t && markDone) {
      try { localStorage.setItem(tourDoneKey(t.def.key), '1') } catch { }
    }
    clearHighlight()
    setTour(null)
    setSpeechBubbleOpen(false)
    returnToDock()
  }, [clearHighlight, returnToDock])

  const startTour = useCallback((def: TourDef) => {
    // Keep only steps whose target is actually on the page
    const steps = def.steps.filter((st) => document.querySelector(st.selector))
    if (steps.length === 0) return
    if (autoDismissTimerRef.current) clearTimeout(autoDismissTimerRef.current)
    setTour({ def, steps, index: 0 })
  }, [])

  // Show the current step: scroll, highlight, anchor the mascot next to the target
  useEffect(() => {
    if (!tour) return
    const step = tour.steps[tour.index]
    const target = document.querySelector<HTMLElement>(step.selector)
    clearHighlight()
    if (!target) {
      // Target vanished (e.g. user moved on to the code screen) -> end quietly
      endTour(false)
      return
    }
    target.scrollIntoView({ behavior: prefersReducedMotion ? 'auto' : 'smooth', block: 'center' })
    target.dataset.tourPrevOutline = target.style.outline
    target.dataset.tourPrevOffset = target.style.outlineOffset
    target.style.outline = '3px solid var(--accent-warm, #E07A5F)'
    target.style.outlineOffset = '4px'
    highlightedRef.current = target

    setIsSleeping(false)
    setCurrentMood(step.animation === 'celebrate' ? 'celebrate' : 'normal')
    setCurrentMessage(step.message)
    setSpeechBubbleOpen(true)
    safePlay(step.animation === 'celebrate' ? 'excited' : step.animation || 'listening')
    if (step.expression) safeExpression(step.expression)

    // Anchor after the smooth scroll settles
    const place = () => {
      const rect = target.getBoundingClientRect()
      const vw = window.innerWidth
      const vh = window.innerHeight
      const boxW = vw >= 640 ? 300 : 250
      const boxH = vw >= 768 ? 270 : 235
      const m = 8
      const clampX = (x: number) => Math.min(vw - boxW - m, Math.max(m, x))
      const clampY = (y: number) => Math.min(vh - boxH - m, Math.max(m, y))
      const hits = (r: { left: number; right: number; top: number; bottom: number }, x: number, y: number) =>
        !(x >= r.right || x + boxW <= r.left || y >= r.bottom || y + boxH <= r.top)
      // Other controls the bubble must not cover (e.g. "Open syllabus" next to "Resume capsule")
      const controls = Array.from(
        document.querySelectorAll<HTMLElement>('a[href], button, input, select, textarea, [role="button"]')
      )
        .filter((el) => !containerRef.current?.contains(el) && !target.contains(el))
        .map((el) => el.getBoundingClientRect())
        .filter((r) => r.width > 0 && r.height > 0 && r.bottom > 0 && r.top < vh)
      const cands: Array<{ x: number; y: number; side: 'right' | 'left' | 'top' }> = [
        { x: rect.right + 16, y: rect.top - 20, side: 'right' as const },
        { x: rect.left - boxW - 16, y: rect.top - 20, side: 'left' as const },
        { x: rect.left, y: rect.bottom + m, side: 'top' as const },
        { x: rect.left, y: rect.top - boxH - m, side: 'top' as const },
        { x: rect.right - boxW, y: rect.bottom + m, side: 'top' as const },
        { x: rect.right - boxW, y: rect.top - boxH - m, side: 'top' as const },
        // Last resorts: screen corners (bottom-right dock first)
        { x: vw - boxW - 20, y: vh - boxH - 20, side: 'top' as const },
        { x: vw - boxW - 20, y: 80, side: 'top' as const },
        { x: 20, y: vh - boxH - 20, side: 'top' as const },
      ]
        .map((c) => ({ ...c, x: clampX(c.x), y: clampY(c.y) }))
        // Small targets must stay visible; a large section may sit under the bubble
        .filter((c) => rect.height > vh * 0.4 || !hits(rect, c.x, c.y))
      // Prefer a spot clear of every control; otherwise dock bottom-right rather than cover one.
      // Phones rarely have room beside the target: stay docked.
      const clear = cands.find((c) => controls.every((r) => !hits(r, c.x, c.y)))
      setAnchorCoords(vw < 640 ? null : clear ?? null)
    }
    // Place once scrolling has settled (smooth scroll can outlast a fixed delay)
    let settleTimer: NodeJS.Timeout | null = null
    const onScroll = () => {
      if (settleTimer) clearTimeout(settleTimer)
      settleTimer = setTimeout(place, 150)
    }
    window.addEventListener('scroll', onScroll, { passive: true, capture: true })
    onScroll()
    const hardStop = setTimeout(place, 1500)
    return () => {
      window.removeEventListener('scroll', onScroll, { capture: true } as any)
      if (settleTimer) clearTimeout(settleTimer)
      clearTimeout(hardStop)
    }
  }, [tour, clearHighlight, endTour, safePlay, safeExpression, prefersReducedMotion])

  // Auto-start the tour on first visit to a page that has one; also listen for manual start
  useEffect(() => {
    if (!pathname) return
    // Navigating mid-tour: drop the old tour without marking it done
    if (tourRef.current) {
      clearHighlight()
      setTour(null)
      setAnchorCoords(null)
    }
    const def = TOURS.find((d) => d.match(pathname))
    let timer: NodeJS.Timeout | null = null
    if (def) {
      let done = false
      try { done = localStorage.getItem(tourDoneKey(def.key)) === '1' } catch { }
      if (!done) timer = setTimeout(() => startTour(def), 1600)
    }
    const onStart = () => {
      const d = TOURS.find((x) => x.match(window.location.pathname))
      if (d) startTour(d)
    }
    window.addEventListener('companion-tour-start', onStart)
    return () => {
      if (timer) clearTimeout(timer)
      window.removeEventListener('companion-tour-start', onStart)
    }
  }, [pathname, startTour, clearHighlight])

  useEffect(() => () => clearHighlight(), [clearHighlight])

  // Esc skips the tour
  useEffect(() => {
    if (!tour) return
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') endTour(true) }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [tour, endTour])

  const tourNext = () => {
    if (!tour) return
    if (tour.index >= tour.steps.length - 1) {
      endTour(true)
      safePlay('excited')
    } else setTour({ ...tour, index: tour.index + 1 })
  }
  const tourBack = () => {
    if (tour && tour.index > 0) setTour({ ...tour, index: tour.index - 1 })
  }
  const pageTour = pathname ? TOURS.find((d) => d.match(pathname)) : undefined

  // Click on mascot -> laughing + cycle speech tip
  const handleMascotClick = () => {
    if (tour) return
    safePlay('laughing')
    setTipIndex((prev) => (prev + 1) % DEFAULT_TIPS.length)
    setCurrentMessage(DEFAULT_TIPS[(tipIndex + 1) % DEFAULT_TIPS.length])
    setSpeechBubbleOpen(true)
    resetToIdle(2500)
  }

  // Hover on mascot -> excited
  const handleMascotMouseEnter = () => {
    if (!isSleeping && currentMood === 'normal') {
      safePlay('excited')
    }
  }

  const handleMascotMouseLeave = () => {
    if (!isSleeping && currentMood === 'normal') {
      safePlay('idle')
    }
  }

  // Positioning style: Docked at bottom-right or floating anchored near an element
  const containerStyle: React.CSSProperties = anchorCoords
    ? {
        position: 'fixed',
        left: `${anchorCoords.x}px`,
        top: `${anchorCoords.y}px`,
        zIndex: 50,
        transition: 'left 0.6s cubic-bezier(0.32, 0.72, 0, 1), top 0.6s cubic-bezier(0.32, 0.72, 0, 1)',
      }
    : {
        position: 'fixed',
        bottom: '1.25rem',
        right: '1.25rem',
        zIndex: 40,
        transition: 'all 0.6s cubic-bezier(0.32, 0.72, 0, 1)',
      }

  // Mood-based halos and themes
  const isSuspicious = currentMood === 'suspicious' || currentMood === 'warning'
  const isCelebrate = currentMood === 'celebrate'

  // Never render on landing page, login, onboarding, or in active classroom sessions
  if (
    pathname?.includes('/class/') ||
    pathname === '/' ||
    pathname?.startsWith('/onboarding')
  ) {
    return null
  }

  return (
    <aside
      ref={containerRef}
      style={containerStyle}
      aria-label="Anaxly Intelligent Companion"
      className={`${
        pathname?.startsWith('/login') ? 'hidden md:flex' : 'flex'
      } flex-col items-center md:items-start select-none pointer-events-none group`}
    >
      {/* Interactive Floating Speech Bubble with Apple-tier springs */}
      {speechBubbleOpen && (
        <div
          className={`pointer-events-auto mb-2 max-w-[240px] sm:max-w-[280px] p-3.5 rounded-2xl backdrop-blur-xl border shadow-[0_16px_36px_rgba(23,24,23,0.12)] text-xs text-[#171817] animate-in fade-in zoom-in-95 duration-300 relative ${
            isSuspicious
              ? 'bg-amber-50/95 border-amber-300 ring-2 ring-amber-400/20'
              : isCelebrate
              ? 'bg-emerald-50/95 border-emerald-300 ring-2 ring-emerald-400/20'
              : 'bg-white/95 border-[var(--border-subtle)]'
          }`}
        >
          {/* Dismiss button to dock mascot */}
          <button
            onClick={() => {
              if (tour) return endTour(true)
              setSpeechBubbleOpen(false)
              returnToDock()
            }}
            className="absolute top-2 right-2 text-[#7A7C75] hover:text-[#171817] p-1 rounded-full hover:bg-black/5 transition-colors cursor-pointer"
            aria-label="Close message"
          >
            <X className="w-3.5 h-3.5" />
          </button>

          <div className="flex items-start gap-2.5 pr-4">
            {isSuspicious ? (
              <AlertCircle className="w-4 h-4 text-sky-600 shrink-0 mt-0.5 animate-pulse" />
            ) : isCelebrate ? (
              <Sparkles className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
            ) : (
              <Sparkles className="w-4 h-4 text-[var(--accent-warm)] shrink-0 mt-0.5" />
            )}
            <p className="leading-relaxed font-medium text-[11px] sm:text-xs text-[#171817]">
              {currentMessage}
            </p>
          </div>

          {/* Action pills for forgot password / assistance */}
          {currentMood === 'warning' && (
            <div className="mt-2.5 pt-2 border-t border-sky-200 flex justify-end">
              <span className="text-[10px] text-sky-800 font-bold flex items-center gap-1">
                <Key className="w-3 h-3" /> Tap 'Forgot Password' above
              </span>
            </div>
          )}

          {/* Guided tour controls */}
          {tour ? (
            <div className="mt-3 pt-2.5 border-t border-[var(--border-subtle)] flex items-center justify-between gap-2">
              <span className="text-[10px] font-semibold text-[#7A7C75] tabular-nums">
                Step {tour.index + 1} of {tour.steps.length}
              </span>
              <div className="flex items-center gap-1.5">
                <button
                  onClick={() => endTour(true)}
                  className="text-[10px] font-medium text-[#7A7C75] hover:text-[#171817] px-2 py-1 rounded-full cursor-pointer"
                >
                  Skip
                </button>
                {tour.index > 0 && (
                  <button
                    onClick={tourBack}
                    className="text-[10px] font-semibold text-[#171817] border border-[var(--border-subtle)] px-2.5 py-1 rounded-full hover:bg-black/5 cursor-pointer"
                  >
                    Back
                  </button>
                )}
                <button
                  onClick={tourNext}
                  className="text-[10px] font-semibold text-white bg-[#171817] px-3 py-1 rounded-full hover:opacity-90 flex items-center gap-1 cursor-pointer"
                >
                  {tour.index >= tour.steps.length - 1 ? 'Got it' : 'Next'}
                  <ArrowRight className="w-3 h-3" />
                </button>
              </div>
            </div>
          ) : pageTour && currentMood === 'normal' ? (
            <div className="mt-2.5 pt-2 border-t border-[var(--border-subtle)] flex justify-end">
              <button
                onClick={() => startTour(pageTour)}
                className="text-[10px] font-semibold text-[#171817] flex items-center gap-1 hover:underline cursor-pointer"
              >
                <HelpCircle className="w-3 h-3" /> Show me around
              </button>
            </div>
          ) : null}

          {/* Pointer tail */}
          <div
            className={`w-3 h-3 border-r border-b transform rotate-45 absolute -bottom-1.5 ${
              anchorCoords?.side === 'left' ? 'right-6' : 'left-6'
            } ${
              isSuspicious
                ? 'bg-amber-50 border-amber-300'
                : isCelebrate
                ? 'bg-emerald-50 border-emerald-300'
                : 'bg-white border-[var(--border-subtle)]'
            }`}
          />
        </div>
      )}

      {/* Procedural Avatar Ball Container */}
      <div
        onClick={handleMascotClick}
        onMouseEnter={handleMascotMouseEnter}
        onMouseLeave={handleMascotMouseLeave}
        className={`pointer-events-auto cursor-pointer transition-all duration-300 hover:scale-105 active:scale-95 flex items-center justify-center relative w-[85px] h-[85px] sm:w-[110px] sm:h-[110px] rounded-full ${
          isSuspicious
            ? 'ring-4 ring-amber-400/70 shadow-[0_0_30px_rgba(245,158,11,0.45)] animate-pulse'
            : isCelebrate
            ? 'ring-4 ring-emerald-400/70 shadow-[0_0_30px_rgba(16,185,129,0.45)]'
            : 'filter drop-shadow-[0_10px_25px_rgba(23,24,23,0.1)]'
        }`}
        title="Sobi - Interactive AI Companion"
      >
        <SobiAvatar
          ref={avatarRef}
          size="100%"
          defaultAnimation={prefersReducedMotion ? undefined : 'idle'}
          defaultExpression={prefersReducedMotion ? 'neutral' : undefined}
          ariaLabel="Sobi Animated Companion"
          onAnimationEnd={(anim) => {
            if (anim === 'laughing' || anim === 'excited') {
              safePlay('idle')
            }
          }}
        />

        {/* Suspicious Warning Icon Badge */}
        {isSuspicious && (
          <span className="absolute -top-1 -right-1 bg-amber-500 text-white p-1 rounded-full shadow-sm animate-bounce">
            <AlertCircle className="w-3.5 h-3.5" />
          </span>
        )}

        {/* Sleeping Status Badge */}
        {isSleeping && (
          <span className="absolute top-1 right-2 bg-white/90 border border-[var(--border-subtle)] text-[10px] font-bold px-1.5 py-0.5 rounded-full text-[#7A7C75] shadow-xs animate-bounce">
            zZz
          </span>
        )}
      </div>
    </aside>
  )
}

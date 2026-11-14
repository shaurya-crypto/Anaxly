'use client'

import React, { useEffect, useState, useRef } from 'react'
import { motion, AnimatePresence } from 'motion/react'
import { Volume2 } from 'lucide-react'
import { cleanChalkboardTypography } from './chalkboardTypography'

export interface ActiveHighlight {
  text: string
  color?: string
  timestamp: number
}

interface LiveChalkSubtitleStreamerProps {
  latestTranscript?: string
  isTeacherSpeaking?: boolean
  activeHighlight?: ActiveHighlight | null
}

/**
 * Word-by-word floating chalk subtitle streamer for live spoken teaching.
 * Renders words as they are spoken in exact chalkboard hand-drawn font,
 * then smoothly fades out with optical physics blur.
 * Also highlights AI-targeted words with an animated golden/amber marker glow pill.
 */
export const LiveChalkSubtitleStreamer: React.FC<LiveChalkSubtitleStreamerProps> = ({
  latestTranscript = '',
  isTeacherSpeaking = false,
  activeHighlight = null,
}) => {
  const [displayedWords, setDisplayedWords] = useState<string[]>([])
  const [isVisible, setIsVisible] = useState(false)
  const fadeTimeoutRef = useRef<NodeJS.Timeout | null>(null)
  const lastTextRef = useRef<string>('')

  // Clean raw transcript from directives and tool calls, and format clean math typography
  const rawClean = latestTranscript
    .replace(/\[[A-Z_]+(?::\s*[^\]]+)?\]/gi, '')
    .replace(/(?:write_chalkboard|write_board|highlight_text|highlight_word|highlight_sentence|plot_mathematical_graph|draw_shape|render_svg_diagram)\s*\([^)]*\)/gi, '')
    .replace(/\s+/g, ' ')
    .trim()
  const clean = cleanChalkboardTypography(rawClean)

  useEffect(() => {
    if (!clean) return

    if (clean !== lastTextRef.current) {
      lastTextRef.current = clean
      const words = clean.split(/\s+/).filter(Boolean)

      // Keep most recent words for an uncluttered aesthetic
      const recentWords = words.slice(-16)
      setDisplayedWords(recentWords)
      setIsVisible(true)

      if (fadeTimeoutRef.current) {
        clearTimeout(fadeTimeoutRef.current)
      }

      // Smooth fade-out 2.8 seconds after speech completes
      fadeTimeoutRef.current = setTimeout(() => {
        setIsVisible(false)
      }, 2800)
    }
  }, [clean])

  useEffect(() => {
    if (!isTeacherSpeaking && isVisible) {
      if (fadeTimeoutRef.current) clearTimeout(fadeTimeoutRef.current)
      fadeTimeoutRef.current = setTimeout(() => {
        setIsVisible(false)
      }, 2200)
    }
  }, [isTeacherSpeaking, isVisible])

  useEffect(() => {
    return () => {
      if (fadeTimeoutRef.current) clearTimeout(fadeTimeoutRef.current)
    }
  }, [])

  // Check if a word matches active highlight
  const isWordHighlighted = (word: string): boolean => {
    if (!activeHighlight || !activeHighlight.text) return false
    const elapsed = Date.now() - activeHighlight.timestamp
    if (elapsed > 4500) return false

    const cleanWord = word.toLowerCase().replace(/[^a-z0-9]/g, '')
    if (!cleanWord || cleanWord.length < 2) return false

    const target = activeHighlight.text.toLowerCase()
    const targetWords = target.split(/\s+/).map((w) => w.replace(/[^a-z0-9]/g, '')).filter(Boolean)
    return targetWords.includes(cleanWord) || (cleanWord.length > 3 && target.includes(cleanWord))
  }

  return (
    <AnimatePresence>
      {isVisible && displayedWords.length > 0 && (
        <motion.div
          initial={{ opacity: 0, y: 12, scale: 0.96 }}
          animate={{ opacity: 1, y: 0, scale: 1 }}
          exit={{
            opacity: 0,
            y: -6,
            scale: 0.98,
            filter: 'blur(4px)',
            transition: { duration: 0.45, ease: [0.16, 1, 0.3, 1] },
          }}
          transition={{ duration: 0.28, ease: [0.16, 1, 0.3, 1] }}
          className="absolute bottom-12 left-1/2 -translate-x-1/2 z-25 max-w-[90vw] sm:max-w-[560px] pointer-events-none select-none"
        >
          <div className="px-4 py-2 rounded-2xl bg-white/94 backdrop-blur-xl border border-[#E5E3DB] shadow-[0_12px_32px_rgba(23,24,23,0.1)] flex items-center gap-2.5">
            <span className="p-1 rounded-lg bg-[#255D88]/10 text-[#255D88] shrink-0">
              <Volume2 className="w-3.5 h-3.5 animate-pulse" />
            </span>
            <div className="flex-1 font-chalk text-sm sm:text-base text-[#1F1C18] leading-relaxed flex flex-wrap items-center">
              {displayedWords.map((word, idx) => {
                const isHighlighted = isWordHighlighted(word)
                return isHighlighted ? (
                  <motion.span
                    key={`${word}-${idx}`}
                    initial={{ scale: 0.95 }}
                    animate={{ scale: [1, 1.1, 1] }}
                    transition={{ duration: 0.35, ease: 'easeOut' }}
                    className="inline-block mr-1 px-1.5 py-0.5 rounded-md bg-[#F59E0B]/20 text-[#B45309] font-bold border border-[#F59E0B]/40 shadow-xs"
                  >
                    {word}
                  </motion.span>
                ) : (
                  <motion.span
                    key={`${word}-${idx}`}
                    initial={{ opacity: 0, y: 3, filter: 'blur(2px)' }}
                    animate={{ opacity: 1, y: 0, filter: 'blur(0px)' }}
                    transition={{ duration: 0.18, ease: 'easeOut' }}
                    className="inline-block mr-1 text-[#1F1C18]"
                  >
                    {word}
                  </motion.span>
                )
              })}
              <span className="inline-block w-1.5 h-3.5 ml-0.5 rounded-full bg-[#255D88] animate-pulse align-middle" />
            </div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}

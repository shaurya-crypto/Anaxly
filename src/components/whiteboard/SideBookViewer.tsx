'use client'

import React, { useState, useEffect, useRef, useCallback } from 'react'
import {
  ChevronLeft,
  ChevronRight,
  X,
  BookOpen,
  ExternalLink,
  Layers,
  Sparkles,
} from 'lucide-react'

export interface SideBookViewerProps {
  /** Relative or absolute URL to textbook PDF (e.g. https://ncert.nic.in/textbook/pdf/jemh101.pdf) */
  pdfUrl: string
  /** Auto-scrolled page requested by tutor or lesson progression (1-based) */
  targetPage?: number
  /** Total pages in current chapter PDF */
  totalPages?: number
  /** Optional chapter or book title for minimal top bar */
  chapterTitle?: string
  /** Invoked when student manually navigates pages */
  onPageChange?: (page: number) => void
  /** Invoked when student closes the docked textbook viewer */
  onClose?: () => void
  /** Optional custom CSS classes */
  className?: string
}

export function SideBookViewer({
  pdfUrl,
  targetPage = 1,
  totalPages,
  chapterTitle,
  onPageChange,
  onClose,
  className = '',
}: SideBookViewerProps) {
  const [currentPage, setCurrentPage] = useState<number>(() => Math.max(1, targetPage || 1))
  const [inputVal, setInputVal] = useState<string>(() => String(Math.max(1, targetPage || 1)))
  const [showEmbed, setShowEmbed] = useState<boolean>(false)
  const iframeRef = useRef<HTMLIFrameElement | null>(null)

  // Clean base URL without existing hash
  const cleanPdfUrl = pdfUrl ? pdfUrl.split('#')[0] : ''

  // Identify official NCERT online URLs
  const isNcertUrl =
    cleanPdfUrl.startsWith('https://ncert.nic.in/') ||
    cleanPdfUrl.startsWith('http://ncert.nic.in/') ||
    cleanPdfUrl.includes('ncert.nic.in')

  // Sync internal state when parent updates targetPage (e.g. tutor jumps to new topic or question)
  useEffect(() => {
    if (typeof targetPage === 'number' && targetPage > 0) {
      const intPage = Math.round(targetPage)
      const clamped = Math.max(1, totalPages ? Math.min(intPage, totalPages) : intPage)
      if (clamped !== currentPage) {
        setCurrentPage(clamped)
        setInputVal(String(clamped))
        if (iframeRef.current && cleanPdfUrl) {
          const nextUrl = `${cleanPdfUrl}#page=${clamped}&view=FitH`
          try {
            iframeRef.current.contentWindow?.location.replace(nextUrl)
          } catch {
            iframeRef.current.src = nextUrl
          }
        }
      }
    }
  }, [targetPage, totalPages, cleanPdfUrl, currentPage])

  // Reload iframe cleanly when chapter/PDF URL changes mid-session
  useEffect(() => {
    if (cleanPdfUrl) {
      const intPage = Math.round(targetPage || 1)
      const clamped = Math.max(1, totalPages ? Math.min(intPage, totalPages) : intPage)
      setCurrentPage(clamped)
      setInputVal(String(clamped))
      if (iframeRef.current) {
        iframeRef.current.src = `${cleanPdfUrl}#page=${clamped}&view=FitH`
      }
    }
  }, [cleanPdfUrl])

  const navigateToPage = useCallback(
    (page: number) => {
      const intPage = Math.round(page)
      const clamped = Math.max(1, totalPages ? Math.min(intPage, totalPages) : intPage)
      setCurrentPage(clamped)
      setInputVal(String(clamped))
      onPageChange?.(clamped)

      if (iframeRef.current && cleanPdfUrl) {
        const nextUrl = `${cleanPdfUrl}#page=${clamped}&view=FitH`
        try {
          iframeRef.current.contentWindow?.location.replace(nextUrl)
        } catch {
          iframeRef.current.src = nextUrl
        }
      }
    },
    [cleanPdfUrl, totalPages, onPageChange]
  )

  const handlePrev = useCallback(() => {
    if (currentPage > 1) {
      navigateToPage(currentPage - 1)
    }
  }, [currentPage, navigateToPage])

  const handleNext = useCallback(() => {
    if (!totalPages || currentPage < totalPages) {
      navigateToPage(currentPage + 1)
    }
  }, [currentPage, totalPages, navigateToPage])

  const handleCommitPage = useCallback(() => {
    const parsed = parseInt(inputVal.trim(), 10)
    if (!isNaN(parsed) && parsed > 0) {
      navigateToPage(parsed)
    } else {
      setInputVal(String(currentPage))
    }
  }, [inputVal, currentPage, navigateToPage])

  const handleOpenCompanionWindow = useCallback(() => {
    if (!cleanPdfUrl) return
    const url = `${cleanPdfUrl}#page=${currentPage}`
    const width = 760
    const height = 920
    const left = typeof window !== 'undefined' ? Math.max(0, window.screen.width - width - 40) : 100
    const top = 40
    window.open(
      url,
      'textbook_companion',
      `width=${width},height=${height},left=${left},top=${top},menubar=no,status=no,toolbar=no`
    )
  }, [cleanPdfUrl, currentPage])

  if (!pdfUrl) {
    return null
  }

  const directOnlineUrl = cleanPdfUrl ? `${cleanPdfUrl}#page=${currentPage}` : '#'
  const exercisePage = totalPages ? Math.max(1, totalPages - 2) : 25

  return (
    <div
      className={`flex flex-col w-full h-full bg-[#0d1612] text-stone-200 select-none overflow-hidden ${className}`}
      data-testid="side-book-viewer"
    >
      {/* Ponytail Minimal Header: [ Title ]  [ < ] Page [ N ] / Total [ > ]  [ ↗ ] [ ✕ ] */}
      <div className="h-10 px-3 bg-[#0d1612] border-b border-emerald-950/80 flex items-center justify-between gap-2 shrink-0">
        {/* Left: Minimal Chapter Title */}
        <div className="flex items-center gap-1.5 min-w-0 pr-2">
          <BookOpen className="w-3.5 h-3.5 text-emerald-400 shrink-0" />
          <span className="text-xs font-serif text-emerald-100/90 tracking-wide font-medium truncate max-w-[120px] sm:max-w-[180px]">
            {chapterTitle || 'Textbook'}
          </span>
        </div>

        {/* Center: Minimal Page Controls [ < ] Page [ N ] / Total [ > ] */}
        <div className="flex items-center gap-1 text-xs">
          <button
            type="button"
            onClick={handlePrev}
            disabled={currentPage <= 1}
            className="w-7 h-7 flex items-center justify-center rounded hover:bg-emerald-900/40 text-stone-300 hover:text-white disabled:opacity-25 disabled:hover:bg-transparent cursor-pointer disabled:cursor-default transition-colors"
            title="Previous page"
            aria-label="Previous page"
          >
            <ChevronLeft className="w-4 h-4" />
          </button>

          <span className="text-stone-400 text-xs font-mono select-none">Page</span>
          <input
            type="text"
            inputMode="numeric"
            pattern="[0-9]*"
            value={inputVal}
            onChange={(e) => setInputVal(e.target.value.replace(/\D/g, ''))}
            onKeyDown={(e) => {
              if (e.key === 'Enter') {
                e.currentTarget.blur()
              }
            }}
            onBlur={handleCommitPage}
            className="w-10 h-6 px-1 text-center bg-[#16251e] border border-emerald-800/60 rounded text-xs font-mono text-white focus:outline-none focus:border-emerald-500"
            aria-label="Current page number"
          />
          {typeof totalPages === 'number' && totalPages > 0 && (
            <span className="text-stone-400 text-xs font-mono select-none">
              / {totalPages}
            </span>
          )}

          <button
            type="button"
            onClick={handleNext}
            disabled={Boolean(totalPages && currentPage >= totalPages)}
            className="w-7 h-7 flex items-center justify-center rounded hover:bg-emerald-900/40 text-stone-300 hover:text-white disabled:opacity-25 disabled:hover:bg-transparent cursor-pointer disabled:cursor-default transition-colors"
            title="Next page"
            aria-label="Next page"
          >
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>

        {/* Right: External Link & Close Button */}
        <div className="flex items-center gap-1 shrink-0">
          <a
            href={directOnlineUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="w-7 h-7 flex items-center justify-center rounded hover:bg-emerald-900/40 text-stone-400 hover:text-emerald-300 transition-colors"
            title="Open official NCERT PDF in new tab"
            aria-label="Open official NCERT PDF in new tab"
          >
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
          <button
            type="button"
            onClick={onClose}
            className="w-7 h-7 flex items-center justify-center rounded hover:bg-rose-950/40 text-stone-400 hover:text-rose-300 cursor-pointer transition-colors"
            title="Close textbook"
            aria-label="Close textbook"
          >
            <X className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Main Viewport */}
      {isNcertUrl && !showEmbed ? (
        <div className="flex-1 w-full h-full overflow-y-auto bg-gradient-to-b from-[#0d1612] via-[#09100d] to-[#0d1612] p-5 flex flex-col justify-between">
          <div className="space-y-4">
            {/* Top Indicator */}
            <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-emerald-950/80 border border-emerald-800/50 text-[11px] font-medium text-emerald-300">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
              Online NCERT Companion
            </div>

            {/* Chapter Heading */}
            <div>
              <h3 className="font-serif text-lg text-emerald-100 font-semibold tracking-tight">
                {chapterTitle || 'Textbook Chapter'}
              </h3>
              <p className="text-xs text-stone-400 mt-0.5">
                Standard Board Curriculum (CBSE, ICSE &amp; IB)
              </p>
            </div>

            {/* Current Active Page Card */}
            <div className="p-3 rounded-xl bg-[#14201a] border border-emerald-900/60 flex items-center justify-between">
              <div className="flex items-center gap-2">
                <BookOpen className="w-4 h-4 text-emerald-400" />
                <span className="text-xs font-mono text-emerald-200">
                  Target Page: <strong className="text-white text-sm font-semibold">{currentPage}</strong>
                  {totalPages ? ` / ${totalPages}` : ''}
                </span>
              </div>
              <span className="text-[10px] text-emerald-400/80 uppercase font-mono tracking-wider">
                Active
              </span>
            </div>

            {/* Primary Action Buttons */}
            <div className="space-y-2 pt-1">
              <a
                href={directOnlineUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="w-full flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-medium transition-all shadow-lg shadow-emerald-950/50 hover:shadow-emerald-900/60 cursor-pointer"
              >
                <BookOpen className="w-3.5 h-3.5" />
                <span>Open Page {currentPage} in New Tab</span>
                <ExternalLink className="w-3.5 h-3.5 opacity-80" />
              </a>

              <button
                type="button"
                onClick={handleOpenCompanionWindow}
                className="w-full flex items-center justify-center gap-2 px-4 py-2 rounded-xl bg-emerald-950/60 hover:bg-emerald-900/50 border border-emerald-800/60 text-emerald-200 text-xs font-medium transition-colors cursor-pointer"
              >
                <Layers className="w-3.5 h-3.5 text-emerald-400" />
                <span>Open in Side Companion Window</span>
              </button>
            </div>

            {/* Quick Section Jump Chips */}
            <div className="pt-2">
              <span className="text-[10px] uppercase font-mono tracking-wider text-stone-500 block mb-1.5">
                Quick Jump
              </span>
              <div className="flex flex-wrap gap-1.5">
                <button
                  type="button"
                  onClick={() => navigateToPage(1)}
                  className={`px-2.5 py-1 rounded-lg text-xs font-mono transition-colors ${
                    currentPage === 1
                      ? 'bg-emerald-700 text-white'
                      : 'bg-emerald-950/40 text-stone-400 hover:text-white hover:bg-emerald-900/40 border border-emerald-900/40'
                  }`}
                >
                  Pg 1: Cover
                </button>
                <button
                  type="button"
                  onClick={() => navigateToPage(currentPage)}
                  className="px-2.5 py-1 rounded-lg text-xs font-mono bg-emerald-950/80 text-emerald-300 border border-emerald-700/60"
                >
                  Pg {currentPage}: Active
                </button>
                <button
                  type="button"
                  onClick={() => navigateToPage(exercisePage)}
                  className={`px-2.5 py-1 rounded-lg text-xs font-mono transition-colors ${
                    currentPage === exercisePage
                      ? 'bg-emerald-700 text-white'
                      : 'bg-emerald-950/40 text-stone-400 hover:text-white hover:bg-emerald-900/40 border border-emerald-900/40'
                  }`}
                >
                  Pg {exercisePage}: Exercises
                </button>
              </div>
            </div>

            {/* Socratic Notice */}
            <div className="p-3 rounded-xl bg-emerald-950/30 border border-emerald-900/40 text-[11px] text-stone-300 leading-relaxed flex items-start gap-2">
              <Sparkles className="w-3.5 h-3.5 text-emerald-400 shrink-0 mt-0.5" />
              <span>
                <strong>Socratic Sync:</strong> When your tutor explains a diagram, worked example, or textbook citation, the page target updates automatically.
              </span>
            </div>
          </div>

          {/* Bottom Embed Toggle */}
          <div className="pt-4 border-t border-emerald-950/60 text-center">
            <button
              type="button"
              onClick={() => setShowEmbed(true)}
              className="text-[11px] text-emerald-400/70 hover:text-emerald-300 underline underline-offset-2 transition-colors cursor-pointer"
            >
              Try In-App Embedded View
            </button>
          </div>
        </div>
      ) : (
        <div className="flex-1 w-full h-full relative overflow-hidden bg-[#525659]">
          {isNcertUrl && (
            <div className="absolute top-2 right-2 z-10">
              <button
                type="button"
                onClick={() => setShowEmbed(false)}
                className="px-2 py-1 rounded bg-black/70 hover:bg-black/90 text-white text-[10px] font-mono shadow transition-colors cursor-pointer"
              >
                Back to Companion
              </button>
            </div>
          )}
          <iframe
            ref={iframeRef}
            src={`${cleanPdfUrl}#page=${currentPage}&view=FitH`}
            className="w-full h-full border-0"
            title={chapterTitle || 'Textbook Page'}
          />
        </div>
      )}
    </div>
  )
}

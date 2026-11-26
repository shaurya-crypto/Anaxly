'use client'

import React, { useState, useEffect, useRef, useCallback } from 'react'
import {
  ChevronLeft,
  ChevronRight,
  X,
  BookOpen,
  ExternalLink,
} from 'lucide-react'

export interface SideBookViewerProps {
  /** Relative same-origin proxy URL (e.g. /api/pdf-proxy?file=jemh101.pdf) or NCERT textbook URL */
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

function normalizeToSameOriginPdfUrl(rawUrl: string): string {
  if (!rawUrl) return ''
  const base = rawUrl.split('#')[0].trim()
  if (!base) return ''
  if (base.startsWith('/api/pdf-proxy')) {
    return base
  }
  const cleanName = (base.split('?')[0].split('/').pop() || '')
    .replace(/\s*\(\d+\)/g, '')
    .trim()
    .toLowerCase()
  if (cleanName.endsWith('.pdf')) {
    return `/api/pdf-proxy?file=${encodeURIComponent(cleanName)}`
  }
  return base
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
  const iframeRef = useRef<HTMLIFrameElement | null>(null)

  const cleanPdfUrl = normalizeToSameOriginPdfUrl(pdfUrl)

  // Sync internal state ONLY when parent updates targetPage or PDF URL (never re-trigger on local manual page turns!)
  useEffect(() => {
    if (typeof targetPage === 'number' && targetPage > 0) {
      const intPage = Math.round(targetPage)
      const clamped = Math.max(1, totalPages ? Math.min(intPage, totalPages) : intPage)
      setCurrentPage(clamped)
      setInputVal(String(clamped))
    }
  }, [targetPage, totalPages, cleanPdfUrl])

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

  if (!pdfUrl || !cleanPdfUrl) {
    return null
  }

  const directOpenUrl = `${cleanPdfUrl}#page=${currentPage}&view=FitH`

  return (
    <div
      className={`flex flex-col w-full h-full bg-[#0d1612] text-stone-200 select-none overflow-hidden ${className}`}
      data-testid="side-book-viewer"
    >
      {/* Minimal Header: [ Title ]  [ < ] Page [ N ] / Total [ > ]  [ External ] [ Close ] */}
      <div className="h-10 px-3 bg-[#0d1612] border-b border-emerald-950/80 flex items-center justify-between gap-2 shrink-0">
        <div className="flex items-center gap-1.5 min-w-0 pr-2">
          <BookOpen className="w-3.5 h-3.5 text-emerald-400 shrink-0" />
          <span className="text-xs font-serif text-emerald-100/90 tracking-wide font-medium truncate max-w-[120px] sm:max-w-[180px]">
            {chapterTitle || 'Textbook'}
          </span>
        </div>

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

        <div className="flex items-center gap-1 shrink-0">
          <a
            href={directOpenUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="w-7 h-7 flex items-center justify-center rounded hover:bg-emerald-900/40 text-stone-400 hover:text-emerald-300 transition-colors"
            title="Open PDF in full tab"
            aria-label="Open PDF in full tab"
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

      {/* Direct Same-Origin Embedded PDF Viewport (keyed by page so Chromium PDFium reliably scrolls on auto-jump) */}
      <div className="flex-1 w-full h-full relative overflow-hidden bg-[#525659]">
        <iframe
          key={`${cleanPdfUrl}::p${currentPage}`}
          ref={iframeRef}
          src={`${cleanPdfUrl}#page=${currentPage}&view=FitH`}
          className="w-full h-full border-0"
          title={chapterTitle || 'Textbook Page'}
        />
      </div>
    </div>
  )
}

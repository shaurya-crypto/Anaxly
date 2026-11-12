'use client'

import React, { useState, useEffect, useRef, useImperativeHandle, forwardRef, useCallback } from 'react'
import dynamic from 'next/dynamic'
import '@excalidraw/excalidraw/index.css'
import {
  FileText,
  Plus,
  Sparkles,
  ChevronLeft,
  ChevronRight,
  RotateCcw,
  BookOpen,
  Trash2,
  Eraser,
  X,
  ZoomIn,
  ZoomOut,
  Maximize2,
} from 'lucide-react'
import { evaluateMathExpression } from '@/lib/mathEvaluator'
import { isLegitimateGraphTopic } from '@/lib/graphGating'

// Dynamically import Excalidraw with SSR disabled
const Excalidraw = dynamic(
  async () => (await import('@excalidraw/excalidraw')).Excalidraw,
  {
    ssr: false,
    loading: () => (
      <div className="w-full h-full flex flex-col items-center justify-center bg-[#FFFFFF] text-[#171817] space-y-3 font-serif">
        <div className="w-8 h-8 border-2 border-[#52715D] border-t-transparent rounded-full animate-spin" />
        <p className="text-sm tracking-wide text-[#555852]">Preparing AI Whiteboard...</p>
      </div>
    ),
  }
)

export interface GreenChalkboardRef {
  highlightText: (text: string, color?: string) => Promise<boolean>
  drawText: (text: string, x?: number, y?: number, color?: string) => void
  drawTitle: (title: string, color?: string) => void
  drawStep: (stepText: string, color?: string) => void
  drawNote: (noteText: string, color?: string) => void
  drawQuestion: (questionText: string, color?: string) => void
  drawHighlightBox: (text: string, color?: string) => void
  drawFlowchart: (flowText: string, color?: string) => void
  drawRoughWork: (workText: string, color?: string) => void
  clearRough: () => void
  clearBoard: () => void
  resetBoard?: () => void
  setChalkColor: (colorNameOrHex: string) => void
  setBoardColor: (theme: 'green' | 'blackboard' | 'slate' | 'white') => void
  drawSvgDiagram: (title: string, svgMarkup: string, caption?: string, forceUpdate?: boolean) => void
  drawImage?: (urlOrDataUrl: string, title?: string, caption?: string) => void
  drawDiagramSkeleton?: (title: string) => void
  clearDiagramSkeleton?: (title?: string) => void
  drawGraph: (type?: string) => void
  drawNumericalSolution?: (solution: {
    problem?: string
    given?: string
    formula?: string
    substitution?: string
    calculation?: string
    answer: string
    unit?: string
  }) => void
  drawVideoCard?: (title: string, description?: string, url?: string, mimeType?: string) => void
  drawTable?: (tableStr: string) => void
  drawGeometry?: (geomStr: string) => void
  drawShape?: (shapeDef: any) => void
  drawStudentAnswer?: (answerText: string, isCorrect?: boolean, color?: string) => void
  drawAnswerVerdict?: (verdictText: string, isCorrect?: boolean, color?: string) => void
  drawExamQuestion?: (questionText: string, modelAnswer?: string, marks?: string, color?: string) => void
  addNewPage?: () => void
  goToPage: (pageIndex: number, title?: string) => void
  clearNotes: () => void
  rewriteNotes: (newNotes: string) => Promise<void>
  getBoardSummary: () => { notesText: string; roughText: string; fullSummary: string }
  getCompactBoardContext?: () => string
  handleAiDirective: (directive: string, transcriptId?: string) => void
  getActiveQuestion?: () => { text: string; y: number; height: number; pageIndex: number } | null
  getNextY?: () => number
  getCurrentPageIndex?: () => number
  restoreBoardState?: (pages: WhiteboardPage[], files?: Record<string, any>) => void
}

interface WhiteboardPage {
  id: number
  elements: any[]
  nextY: number
  roughY: number
}


export interface ActiveTypingItem {
  id: string
  actionLabel: string
  words: string[]
  visibleWordCount: number
  canvasX: number
  canvasY: number
  fontSize: number
  color: string
  bulletType?: 'dot' | 'step' | 'title' | 'box' | 'question' | 'none'
  bulletColor?: string
  isFadingOut: boolean
}

export interface WritingPositionInfo {
  nextY: number
  pageIndex: number
  lastAction?: string
  lastText?: string
  activeQuestion?: { text: string; y: number; height: number; pageIndex: number } | null
  scrollY?: number
}

interface GreenChalkboardProps {
  moduleId?: string
  moduleTitle: string
  classLevel?: string
  subject?: string
  keyConcepts?: string[]
  activeConceptIndex?: number
  onPageChange?: (pageIndex: number) => void
  onNoteRecorded?: (note: string) => void
  onConceptFocus?: (concept: string) => void
  onConceptDone?: (concept: string) => void
  onConceptGoto?: (target: number | string) => void
  onBoardContentChange?: (summary: { notesText: string; roughText: string; fullSummary: string }) => void
  onModuleComplete?: (summary?: string) => void
  onConfirmEndChapter?: (question: string) => void
  onStartQuiz?: () => void
  onWritingPositionChange?: (pos: WritingPositionInfo) => void
}

import {
  INK_PRIMARY,
  INK_SECONDARY,
  INK_MUTED,
  INK_BOTANICAL,
  INK_CORAL,
  INK_CORAL_SOFT,
  INK_BLUE,
  INK_AMBER,
  INK_PURPLE,
  INK_ROSE,
  INK_CYAN,
  INK_EMERALD,
  BORDER_SUBTLE,
  CANVAS_BG,
  resolveChalkColor,
} from './chalkboardColor'
export {
  INK_PRIMARY,
  INK_SECONDARY,
  INK_MUTED,
  INK_BOTANICAL,
  INK_CORAL,
  INK_CORAL_SOFT,
  INK_BLUE,
  INK_AMBER,
  INK_PURPLE,
  INK_ROSE,
  INK_CYAN,
  INK_EMERALD,
  BORDER_SUBTLE,
  CANVAS_BG,
  resolveChalkColor,
}

import {
  normalizeTitle,
  isRedundantConceptOrMasteredText,
} from './chalkboardFilter'
export { normalizeTitle, isRedundantConceptOrMasteredText }

import { wrapText, cleanChalkboardTypography } from './textWrapper'
export { wrapText, cleanChalkboardTypography }

import {
  sanitizeBase64DataUrl,
  isValidBase64DataUrl,
  svgToBase64DataUrl,
  validateSvgForExcalidraw,
  createFallbackImageSvg,
} from './chalkboardMediaUtils'
export {
  sanitizeBase64DataUrl,
  isValidBase64DataUrl,
  svgToBase64DataUrl,
  validateSvgForExcalidraw,
  createFallbackImageSvg,
}

const EXCALIDRAW_INITIAL_DATA = {
  appState: {
    viewBackgroundColor: 'transparent',
    currentItemStrokeColor: INK_PRIMARY,
    currentItemFontFamily: 1,
    currentItemRoughness: 0,
    zenModeEnabled: false,
    viewModeEnabled: true,
    gridModeEnabled: true,
    gridSize: 20,
    zoom: { value: 0.7 as any },
  },
}

const EXCALIDRAW_UI_OPTIONS = {
  canvasActions: {
    changeViewBackgroundColor: false,
    clearCanvas: false,
    loadScene: false,
    saveToActiveFile: false,
    toggleTheme: false,
    saveAsImage: false,
  },
  tools: {
    image: false,
  },
  welcomeScreen: false,
}

/**
 * Safely saves whiteboard data to localStorage with automatic LRU pruning of stale module data
 * to completely eliminate QuotaExceededError in the browser.
 */
function safeSaveWhiteboardStorage(key: string, data: any, isFilesStore = false): void {
  if (typeof window === 'undefined' || !key) return
  try {
    const jsonStr = JSON.stringify(data)
    // If files store is large (>250KB), do not store raw base64 files to localStorage to protect browser quota
    if (isFilesStore && jsonStr.length > 250 * 1024) {
      return
    }
    // Persist whiteboard state or files: localStorage.setItem(`${storageKey}_files`, jsonStr)
    localStorage.setItem(key, jsonStr)
  } catch (err: any) {
    if (err?.name === 'QuotaExceededError' || err?.code === 22) {
      try {
        const toRemove: string[] = []
        for (let i = 0; i < localStorage.length; i++) {
          const k = localStorage.key(i)
          if (!k) continue
          // Prune heavy file payloads from other modules
          if (k.includes('_files') && !k.startsWith(key)) {
            toRemove.push(k)
          }
          // Prune pages from other modules
          else if (k.startsWith('whiteboard_pages_') && !k.startsWith(key)) {
            toRemove.push(k)
          }
          // Prune notes from other modules
          else if (k.startsWith('ai_tutor_board_notes_')) {
            toRemove.push(k)
          }
        }
        for (const k of toRemove) localStorage.removeItem(k)

        // Retry saving current module state
        if (!isFilesStore) {
          localStorage.setItem(key, JSON.stringify(data))
        }
      } catch {}
    }
  }
}

export const GreenChalkboard = forwardRef<GreenChalkboardRef, GreenChalkboardProps>(
  (
    {
      moduleId,
      moduleTitle,
      classLevel = '',
      subject = '',
      keyConcepts = [],
      activeConceptIndex = 0,
      onPageChange,
      onNoteRecorded,
      onConceptFocus,
      onConceptDone,
      onConceptGoto,
      onBoardContentChange,
      onModuleComplete,
      onConfirmEndChapter,
      onStartQuiz,
      onWritingPositionChange,
    },
    ref
  ) => {
    const [excalidrawAPI, setExcalidrawAPI] = useState<any>(null)
    const excalidrawAPIRef = useRef<any>(null)

    // Stable API assignment callback: prevents infinite render loops by setting state strictly once
    const handleExcalidrawAPI = useCallback((api: any) => {
      if (!api || excalidrawAPIRef.current) return
      excalidrawAPIRef.current = api
      setExcalidrawAPI(api)
    }, [])

    const storageKey = moduleId ? `whiteboard_pages_${moduleId}` : `whiteboard_pages_${moduleTitle}`

    // Multi-page system state
    const [pages, setPages] = useState<WhiteboardPage[]>([
      { id: 1, elements: [], nextY: 140, roughY: 140 },
    ])
    const [currentPageIndex, setCurrentPageIndex] = useState<number>(0)
    const pagesRef = useRef<WhiteboardPage[]>([
      { id: 1, elements: [], nextY: 140, roughY: 140 },
    ])
    const currentPageIndexRef = useRef<number>(0)

    const boardElementsRef = useRef<any[]>([])
    const nextYRef = useRef(140)
    const roughYRef = useRef(140)
    const activeQuestionRef = useRef<{ text: string; y: number; height: number; pageIndex: number } | null>(null)
    const convertElementsRef = useRef<any>(null)
    const executedDirectivesRef = useRef<Set<string>>(new Set())
    const executedTextHistoryRef = useRef<Set<string>>(new Set())
    const persistTimeoutRef = useRef<NodeJS.Timeout | null>(null)
    const containerRef = useRef<HTMLDivElement>(null)
    // Narrow screens: smaller board zoom and fewer text columns so lines fit the board width
    const [boardZoom, setBoardZoom] = useState(0.7)
    const boardZoomRef = useRef(0.7)
    const wrapFactorRef = useRef(1)
    const cols = (n: number) => Math.max(24, Math.floor(n * wrapFactorRef.current))
    useEffect(() => {
      const el = containerRef.current
      if (!el) return
      const update = () => {
        const w = el.clientWidth
        if (!w) return
        const zoom = w < 600 ? 0.55 : 0.7
        // 840 canvas px fit the full column count; leave room for the 60px left margin
        const factor = Math.min(1, Math.max(0.3, (w / zoom - 80) / 840))
        boardZoomRef.current = zoom
        wrapFactorRef.current = factor
        setBoardZoom((prev) => (prev === zoom ? prev : zoom))
      }
      update()
      const ro = new ResizeObserver(update)
      ro.observe(el)
      return () => ro.disconnect()
    }, [])
    const operationQueueRef = useRef<Promise<any>>(Promise.resolve())
    const [activeChalkColor, setActiveChalkColor] = useState<string>(INK_PRIMARY)
    const activeChalkColorRef = useRef<string>(INK_PRIMARY)
    const lastDrawnStudentAnswerRef = useRef<{ text: string; time: number } | null>(null)
    const lastExecutedActionTimeRef = useRef<Map<string, number>>(new Map())

    // High-Resolution Interactive Image Lightbox
    const [lightboxImage, setLightboxImage] = useState<{
      url: string
      title: string
      caption?: string
    } | null>(null)
    const [lightboxZoom, setLightboxZoom] = useState<number>(1)
    const [lightboxPan, setLightboxPan] = useState<{ x: number; y: number }>({ x: 0, y: 0 })
    const [isDraggingLightbox, setIsDraggingLightbox] = useState<boolean>(false)
    const dragStartRef = useRef<{ startX: number; startY: number; initialPanX: number; initialPanY: number }>({
      startX: 0,
      startY: 0,
      initialPanX: 0,
      initialPanY: 0,
    })

    // Educational Video Demonstration Lightbox / Modal
    const [videoModal, setVideoModal] = useState<{
      url: string
      title: string
      description?: string
    } | null>(null)

    useEffect(() => {
      const handleKeyDown = (e: KeyboardEvent) => {
        if (e.key === 'Escape') {
          if (videoModal) {
            setVideoModal(null)
          }
          if (lightboxImage) {
            setLightboxImage(null)
            setLightboxZoom(1)
            setLightboxPan({ x: 0, y: 0 })
          }
        }
      }
      window.addEventListener('keydown', handleKeyDown)
      return () => window.removeEventListener('keydown', handleKeyDown)
    }, [lightboxImage, videoModal])

    const [activeTyping, setActiveTyping] = useState<ActiveTypingItem | null>(null)

    const playTypingEffect = async (
      actionLabel: string,
      text: string,
      color: string,
      canvasX: number,
      canvasY: number,
      fontSize = 16,
      bulletType: 'dot' | 'step' | 'title' | 'box' | 'question' | 'none' = 'none',
      bulletColor?: string
    ): Promise<void> => {
      if (typeof window === 'undefined') return
      if (window.matchMedia?.('(prefers-reduced-motion: reduce)')?.matches) return

      const cleanText = text.trim()
      const words = cleanText.split(/\s+/).filter(Boolean)
      if (words.length === 0) return

      const id = Math.random().toString(36).substring(7)
      setActiveTyping({
        id,
        actionLabel,
        words,
        visibleWordCount: 1,
        canvasX,
        canvasY,
        fontSize,
        color,
        bulletType,
        bulletColor,
        isFadingOut: false,
      })

      // Smooth, natural word-by-word pacing (60-80ms per word)
      const wordDelay = Math.max(45, Math.min(80, 850 / words.length))
      for (let i = 2; i <= words.length; i++) {
        await new Promise((r) => setTimeout(r, wordDelay))
        setActiveTyping((prev) => (prev && prev.id === id ? { ...prev, visibleWordCount: i } : prev))
      }

      // Brief hold to absorb the complete written phrase
      await new Promise((r) => setTimeout(r, 180))

      // Smooth fade-out into the permanent chalkboard canvas
      setActiveTyping((prev) => (prev && prev.id === id ? { ...prev, isFadingOut: true } : prev))
      await new Promise((r) => setTimeout(r, 280))

      setActiveTyping((prev) => (prev && prev.id === id ? null : prev))
    }


    const notifyPositionChange = (lastAction?: string, lastText?: string) => {
      const scrollY = excalidrawAPIRef.current?.getAppState?.()?.scrollY || 0
      onWritingPositionChange?.({
        nextY: nextYRef.current,
        pageIndex: currentPageIndexRef.current,
        lastAction,
        lastText,
        activeQuestion: activeQuestionRef.current,
        scrollY,
      })
    }

    const setChalkColor = (colorNameOrHex: string) => {
      const resolved = resolveChalkColor(colorNameOrHex, INK_PRIMARY)
      activeChalkColorRef.current = resolved
      setActiveChalkColor(resolved)
    }

    // Serialized execution queue for non-overlapping atomic whiteboard updates
    const enqueueOperation = <T,>(op: () => Promise<T>): Promise<T> => {
      return new Promise<T>((resolve, reject) => {
        operationQueueRef.current = operationQueueRef.current
          .then(async () => {
            try {
              const res = await op()
              resolve(res)
            } catch (err) {
              console.error('Queue op error:', err)
              reject(err)
            }
          })
          .catch((err) => {
            console.error('Operation queue chain error:', err)
          })
      })
    }

    // Synchronous helper to get current active elements without Excalidraw async race condition
    const getCurrentElements = (): any[] => {
      if (boardElementsRef.current && boardElementsRef.current.length > 0) {
        return boardElementsRef.current
      }
      return (excalidrawAPI?.getSceneElements() || []) as any[]
    }

    // Inspect board elements to guarantee zero duplicate writes on current page
    const isAlreadyOnBoard = (text: string): boolean => {
      if (!text || !text.trim()) return false
      const clean = text
        .toLowerCase()
        .replace(/^(note|step|breakdown|intuition|definition|q\d?|verdict|ans)[:\s\-]*/i, '')
        .replace(/[^a-z0-9]/g, '')
        .trim()
      if (clean.length < 5) return false

      const currentEls = getCurrentElements()
      for (const el of currentEls) {
        if (el.type === 'text' && el.text) {
          const elClean = el.text
            .toLowerCase()
            .replace(/^(note|step|breakdown|intuition|definition|q\d?|verdict|ans)[:\s\-]*/i, '')
            .replace(/[^a-z0-9]/g, '')
            .trim()
          if (elClean === clean) {
            return true
          }
        }
      }
      return false
    }

    const shouldSkipDuplicate = (action: string, content: string, windowMs = 15000): boolean => {
      if (!content || !content.trim()) return false
      const clean = content.toLowerCase().trim()
      const cleanNorm = clean.replace(/[^a-z0-9]/g, '')

      if (cleanNorm.length >= 8 && isAlreadyOnBoard(content)) {
        return true
      }

      const key = `${action}:${cleanNorm.slice(0, 80)}`
      const now = Date.now()
      const prev = lastExecutedActionTimeRef.current.get(key)
      if (prev && now - prev < windowMs) {
        return true
      }
      lastExecutedActionTimeRef.current.set(key, now)
      if (lastExecutedActionTimeRef.current.size > 200) {
        for (const [k, t] of lastExecutedActionTimeRef.current.entries()) {
          if (now - t > 120000) lastExecutedActionTimeRef.current.delete(k)
        }
      }
      return false
    }

    const isInitializedRef = useRef(false)
    const prevModuleIdRef = useRef(moduleId)

    // Calculate dynamic Y coordinate below existing elements on the left column to prevent collision/overlap
    const getDynamicNextY = (margin = 20): number => {
      const currentEls = getCurrentElements()
      const noteEls = currentEls.filter(
        (el: any) =>
          !el.id?.startsWith('header_') &&
          el.customData?.isRough !== true &&
          typeof el.y === 'number' &&
          (el.x === undefined || el.x < 620)
      )
      if (noteEls.length === 0) {
        return Math.max(nextYRef.current, 140)
      }
      const maxY = Math.max(
        ...noteEls.map((el: any) => {
          let h = el.height
          if (!h || h <= 0) {
            if (el.type === 'text' && el.text) {
              const lineCount = (el.text.split('\n') || []).length
              const fontSize = el.fontSize || 16
              h = lineCount * Math.round(fontSize * 1.35) + 8
            } else if (el.type === 'rectangle') {
              h = 60
            } else {
              h = 30
            }
          }
          return el.y + h
        }),
        nextYRef.current
      )
      return Math.max(maxY + margin, nextYRef.current)
    }

    // Centralized helper: synchronously updates page buffer, state, Excalidraw scene, and storage
    const updateCurrentPageElements = (elements: any[], nextY?: number) => {
      boardElementsRef.current = elements
      if (typeof nextY === 'number') {
        nextYRef.current = nextY
      }
      const pageIdx = currentPageIndexRef.current
      if (pagesRef.current[pageIdx]) {
        pagesRef.current[pageIdx].elements = elements
        pagesRef.current[pageIdx].nextY = nextYRef.current
        pagesRef.current[pageIdx].roughY = roughYRef.current
      }
      setPages([...pagesRef.current])
      excalidrawAPI?.updateScene({ elements })
      persistScene(elements)
      notifyPositionChange()
    }

    const checkIsRedundant = (text: string): boolean =>
      isRedundantConceptOrMasteredText(text, moduleTitle, keyConcepts)
    const isRedundant = checkIsRedundant

    useEffect(() => {
      const el = containerRef.current
      if (!el) return
      const preventZoom = (e: WheelEvent) => {
        if (e.ctrlKey || e.metaKey) {
          e.preventDefault()
        }
      }
      const preventGesture = (e: Event) => {
        e.preventDefault()
      }
      el.addEventListener('wheel', preventZoom, { passive: false })
      el.addEventListener('gesturestart', preventGesture, { passive: false })
      el.addEventListener('gesturechange', preventGesture, { passive: false })
      return () => {
        el.removeEventListener('wheel', preventZoom)
        el.removeEventListener('gesturestart', preventGesture)
        el.removeEventListener('gesturechange', preventGesture)
      }
    }, [])

    // Helper to build a clean page header with optional single-concept title
    const createHeaderSkeleton = (pageNum = 1, conceptTitle?: string): any[] => {
      // Keep the one-line header inside the board on narrow screens (20px font is ~11.5 canvas px per char)
      const boardW = containerRef.current?.clientWidth || 0
      const headerZoom = boardW && boardW < 600 ? 0.55 : 0.7
      const headerMaxChars = boardW ? Math.max(16, Math.floor((boardW / headerZoom - 130) / 11.5)) : 200
      const fitHeader = (t: string) => (t.length > headerMaxChars ? `${t.slice(0, headerMaxChars - 1).trimEnd()}…` : t)
      const items: any[] = [
        {
          id: `header_topic_p${pageNum}`,
          type: 'text',
          x: 60,
          y: 35,
          text: fitHeader(`TOPIC: ${moduleTitle.toUpperCase()}${pageNum > 1 ? ` (PAGE ${pageNum})` : ''}`),
          fontSize: 20,
          fontFamily: 1,
          strokeColor: INK_PRIMARY,
          customData: { isHeader: true },
        },
        {
          id: `header_meta_p${pageNum}`,
          type: 'text',
          x: 60,
          y: 68,
          text: [subject, classLevel, `Interactive Whiteboard • Page ${pageNum}`].filter(Boolean).join(' • '),
          fontSize: 12,
          fontFamily: 1,
          strokeColor: INK_MUTED,
          customData: { isHeader: true },
        },
        {
          id: `header_sep_h_p${pageNum}`,
          type: 'line',
          x: 60,
          y: 95,
          width: 760,
          height: 0,
          points: [[0, 0], [760, 0]],
          strokeColor: BORDER_SUBTLE,
          strokeStyle: 'dashed',
          customData: { isHeader: true },
        },
      ]

      if (conceptTitle) {
        const clean = conceptTitle
          .replace(/^focus:\s*/i, '')
          .replace(/^concept\s*\d*:\s*/i, '')
          .replace(/[\(\)\[\]\{\}\"]/g, '')
          .replace(/^'+|'+$/g, '')
          .replace(/\s+/g, ' ')
          .trim()
        if (clean && normalizeTitle(clean) !== normalizeTitle(moduleTitle)) {
          const startX = 60
          const startY = 140 + 12
          const titleText = `CONCEPT ${pageNum}: ${clean.toUpperCase()}`
          items.push(
            {
              id: `title_concept_p${pageNum}`,
              type: 'text',
              x: startX,
              y: startY,
              text: fitHeader(titleText),
              fontSize: 19,
              fontFamily: 1,
              strokeColor: INK_PRIMARY,
              customData: { isRough: false, isTitle: true },
            },
            {
              id: `title_underline_p${pageNum}`,
              type: 'line',
              x: startX,
              y: startY + 28,
              points: [[0, 0], [Math.min(titleText.length * 12, 380), 0]],
              strokeColor: INK_BOTANICAL,
              strokeWidth: 2,
              customData: { isRough: false, isTitle: true },
            }
          )
        }
      }

      return items
    }

    // Compile notes across ALL pages for comprehensive Master Notes
    const getBoardSummary = (): { notesText: string; roughText: string; fullSummary: string } => {
      // Sync current scene into current page in memory
      if (excalidrawAPI && pagesRef.current[currentPageIndexRef.current]) {
        pagesRef.current[currentPageIndexRef.current].elements = getCurrentElements()
      }

      const allNotes: string[] = []

      pagesRef.current.forEach((page, pIdx) => {
        const pageElements = page.elements || []
        const textElements = pageElements.filter(
          (el: any) => el.type === 'text' && !el.id?.startsWith('header_') && el.text
        )

        const pageNotes: string[] = []
        for (const el of textElements) {
          const text = (el.text || '').trim()
          if (!text) continue
          pageNotes.push(text)
        }

        if (pageNotes.length > 0) {
          allNotes.push(`--- PAGE ${pIdx + 1} ---`)
          allNotes.push(...pageNotes)
        }
      })

      const notesText = allNotes.join('\n')
      const roughText = ''

      const fullSummary = allNotes.length > 0
        ? `MASTER NOTES ON BOARD:\n${allNotes.map((n) => (n.startsWith('---') ? n : `• ${n}`)).join('\n')}`
        : 'MASTER NOTES: (Module header initialized)'

      return { notesText, roughText, fullSummary }
    }

    // Token-efficient snapshot of current chalkboard page for live AI context
    const getCompactBoardContext = (): string => {
      if (excalidrawAPI && pagesRef.current[currentPageIndexRef.current]) {
        pagesRef.current[currentPageIndexRef.current].elements = getCurrentElements()
      }

      const totalPages = pagesRef.current.length
      const curIdx = currentPageIndexRef.current
      const curPage = pagesRef.current[curIdx]
      if (!curPage) return 'CURRENT BOARD: Empty / Initialized'

      const lines: string[] = []
      lines.push(`CHALKBOARD SNAPSHOT (Page ${curIdx + 1} of ${totalPages}):`)

      if (curIdx > 0) {
        lines.push('PREVIOUS COMPLETED PAGES (DO NOT RE-TEACH):')
        for (let i = 0; i < curIdx; i++) {
          const p = pagesRef.current[i]
          const pEls = p?.elements || []
          const pTitleEl = pEls.find((el: any) => el.type === 'text' && (el.id?.startsWith('header_') || el.customData?.isTitle))
          const pDiag = pEls.find((el: any) => el.customData?.isSvgCard || el.customData?.diagramTitle)
          const pTitle = pTitleEl?.text?.replace(/\n/g, ' ') || `Concept ${i + 1}`
          const pDiagInfo = pDiag?.customData?.diagramTitle ? ` | Diagram: "${pDiag.customData.diagramTitle}"` : ''
          lines.push(`  * Page ${i + 1}: ${pTitle}${pDiagInfo} (Mastered)`)
        }
      }

      lines.push(`ACTIVE PAGE ${curIdx + 1} ON BOARD RIGHT NOW:`)
      const curElements = curPage.elements || []

      // 1. Visual Diagrams
      const diagrams = curElements.filter((el: any) => el.customData?.isSvgCard && el.customData?.diagramTitle)
      if (diagrams.length > 0) {
        const uniqueDiags = Array.from(new Set(diagrams.map((d: any) => d.customData.diagramTitle)))
        lines.push(`  - Drawn Diagram(s): ${uniqueDiags.map(d => `"${d}"`).join(', ')} (Already drawn - do not redraw!)`)
      }

      // 2. Cartesian Graphs
      const graphEls = curElements.filter((el: any) => el.text && (el.text.includes('Cartesian Graph') || el.text.startsWith('f(x) =') || el.text.startsWith('y =')))
      if (graphEls.length > 0) {
        lines.push(`  - Plotted Graph: "${graphEls[0].text.replace(/\n/g, ' ')}" (Already plotted)`)
      }

      // 3. Notes / Formulas
      const textEls = curElements.filter(
        (el: any) =>
          el.type === 'text' &&
          !el.id?.startsWith('header_') &&
          el.customData?.isRough !== true &&
          el.text &&
          !el.text.startsWith('0') && !el.text.match(/^[-+]?\d+$/)
      )

      const extractedNotes: string[] = []
      for (const el of textEls) {
        const raw = (el.text || '').trim()
        if (!raw || raw.startsWith('[DIAGRAM]:')) continue
        const clean = raw.replace(/\n+/g, ' | ')
        if (clean.length > 180) {
          extractedNotes.push(clean.slice(0, 180) + '...')
        } else {
          extractedNotes.push(clean)
        }
      }

      if (extractedNotes.length > 0) {
        lines.push('  - Notes Already on Board (Do not duplicate):')
        extractedNotes.slice(-10).forEach(n => lines.push(`    • ${n}`))
      } else {
        lines.push('  - Notes Already on Board: [Clean page - Ready for new notes]')
      }

      if (activeQuestionRef.current) {
        lines.push(`  - Active Question on Board: "${activeQuestionRef.current.text}"`)
      }

      return lines.join('\n')
    }

    // Sanitize raw SVG markup: parse via DOMParser, fix common Gemini output issues, return clean SVG or null
    const sanitizeSvg = (rawSvg: string): string | null => {
      if (typeof window === 'undefined' || typeof DOMParser === 'undefined') return rawSvg
      try {
        // Fix common malformed XML issues from Gemini Live output before parsing
        let fixed = rawSvg
        // Escape unescaped ampersands (not already part of &amp; &lt; &gt; &apos; &quot; &#...)
        fixed = fixed.replace(/&(?!amp;|lt;|gt;|apos;|quot;|#\d+;|#x[\da-fA-F]+;)/g, '&amp;')
        // Self-close unclosed void elements common in SVG (e.g. <path d="..." > -> <path d="..." />)
        fixed = fixed.replace(/<(path|circle|ellipse|rect|line|polygon|polyline|use|image|stop)\b([^>]*?)(?<!\/)>/gi,
          (match, tag, attrs) => {
            if (attrs.trim().endsWith('/')) return match
            return `<${tag}${attrs}/>`
          }
        )
        const parser = new DOMParser()
        const doc = parser.parseFromString(fixed, 'image/svg+xml')
        const parseError = doc.querySelector('parsererror')
        if (parseError) {
          // Last resort: try with text/html parser which is more forgiving
          const htmlDoc = parser.parseFromString(`<body>${fixed}</body>`, 'text/html')
          const svgEl = htmlDoc.querySelector('svg')
          if (svgEl) {
            if (!svgEl.hasAttribute('xmlns')) svgEl.setAttribute('xmlns', 'http://www.w3.org/2000/svg')
            return svgEl.outerHTML
          }
          return null
        }
        const svgEl = doc.querySelector('svg')
        if (!svgEl) return null
        if (!svgEl.hasAttribute('xmlns')) svgEl.setAttribute('xmlns', 'http://www.w3.org/2000/svg')
        // Ensure width/height are set (Excalidraw requires them)
        const vb = svgEl.getAttribute('viewBox')
        if (vb && (!svgEl.getAttribute('width') || !svgEl.getAttribute('height'))) {
          const parts = vb.trim().split(/[\s,]+/).map(Number)
          if (parts.length === 4 && parts[2] > 0 && parts[3] > 0) {
            if (!svgEl.getAttribute('width')) svgEl.setAttribute('width', String(parts[2]))
            if (!svgEl.getAttribute('height')) svgEl.setAttribute('height', String(parts[3]))
          }
        }
        return svgEl.outerHTML
      } catch {
        return null
      }
    }

    // Rasterize SVG string to PNG data URL via offscreen canvas (bulletproof fallback for Excalidraw)
    const rasterizeSvgToPng = (svgString: string, width: number, height: number): Promise<string> => {
      return new Promise((resolve, reject) => {
        if (typeof window === 'undefined') { reject(new Error('No window')); return }
        const blob = new Blob([svgString], { type: 'image/svg+xml;charset=utf-8' })
        const url = URL.createObjectURL(blob)
        const img = new Image()
        const timer = setTimeout(() => {
          URL.revokeObjectURL(url)
          reject(new Error('SVG rasterization timeout'))
        }, 2500)

        img.onload = () => {
          clearTimeout(timer)
          try {
            const canvas = document.createElement('canvas')
            canvas.width = Math.max(100, width * 2)  // 2x for sharpness
            canvas.height = Math.max(100, height * 2)
            const ctx = canvas.getContext('2d')
            if (!ctx) { reject(new Error('No canvas context')); URL.revokeObjectURL(url); return }
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height)
            const pngDataUrl = canvas.toDataURL('image/png')
            URL.revokeObjectURL(url)
            resolve(pngDataUrl)
          } catch (err) {
            URL.revokeObjectURL(url)
            reject(err)
          }
        }
        img.onerror = (err) => {
          clearTimeout(timer)
          URL.revokeObjectURL(url)
          reject(err)
        }
        img.src = url
      })
    }

    // Debounced persistence to localStorage
    const persistScene = (elements: readonly any[] | any[]) => {
      if (!storageKey || typeof window === 'undefined') return

      if (pagesRef.current[currentPageIndexRef.current] && elements && elements.length > 0) {
        pagesRef.current[currentPageIndexRef.current].elements = elements as any[]
        pagesRef.current[currentPageIndexRef.current].nextY = nextYRef.current
        pagesRef.current[currentPageIndexRef.current].roughY = roughYRef.current
      }

      if (persistTimeoutRef.current) clearTimeout(persistTimeoutRef.current)
      persistTimeoutRef.current = setTimeout(() => {
        try {
          safeSaveWhiteboardStorage(storageKey, pagesRef.current)
          if (excalidrawAPI?.getFiles) {
            const files = excalidrawAPI.getFiles()
            if (files && Object.keys(files).length > 0) {
              safeSaveWhiteboardStorage(`${storageKey}_files`, files, true)
            }
          }
          if (onBoardContentChange) {
            onBoardContentChange(getBoardSummary())
          }
        } catch (err) {
          console.warn('Failed to save whiteboard pages to localStorage:', err)
        }
      }, 400)
    }

    const persistSceneRef = useRef(persistScene)
    persistSceneRef.current = persistScene

    const lastElementCountRef = useRef<number>(0)
    const handleExcalidrawChange = useCallback((elements: readonly any[], appState?: any) => {
      if (elements && elements.length > 0) {
        boardElementsRef.current = elements as any[]
        if (elements.length !== lastElementCountRef.current) {
          lastElementCountRef.current = elements.length
          persistSceneRef.current(elements)
        }
      }
      if (appState?.selectedElementIds) {
        const selectedId = Object.keys(appState.selectedElementIds).find((id) => appState.selectedElementIds[id])
        if (selectedId) {
          const selectedEl = (elements || []).find((el: any) => el.id === selectedId)
          if (selectedEl?.customData?.isExpandableImage && (selectedEl.customData?.fullUrl || selectedEl.customData?.imageUrl)) {
            setLightboxImage({
              url: selectedEl.customData.fullUrl || selectedEl.customData.imageUrl,
              title: selectedEl.customData.title || selectedEl.customData.diagramTitle || 'Scientific Diagram',
              caption: selectedEl.customData.caption || '',
            })
            setLightboxZoom(1)
            setLightboxPan({ x: 0, y: 0 })
          } else if (selectedEl?.customData?.isPlayableVideo && selectedEl.customData?.videoUrl) {
            setVideoModal({
              url: selectedEl.customData.videoUrl,
              title: selectedEl.customData.title || 'Educational Demonstration',
              description: selectedEl.customData.description || '',
            })
          }
        }
      }
    }, [])

    const handleContainerClick = useCallback((e: React.MouseEvent<HTMLDivElement>) => {
      if (!excalidrawAPIRef.current || !containerRef.current) return
      try {
        const appState = excalidrawAPIRef.current.getAppState?.()
        if (!appState) return
        const zoom = appState.zoom?.value || boardZoomRef.current || 0.7
        const scrollX = appState.scrollX || 0
        const scrollY = appState.scrollY || 0
        const rect = containerRef.current.getBoundingClientRect()
        const canvasX = (e.clientX - rect.left) / zoom - scrollX
        const canvasY = (e.clientY - rect.top) / zoom - scrollY

        const currentEls = boardElementsRef.current || []
        for (let i = currentEls.length - 1; i >= 0; i--) {
          const el = currentEls[i]
          if (
            canvasX >= el.x &&
            canvasX <= el.x + el.width &&
            canvasY >= el.y &&
            canvasY <= el.y + el.height
          ) {
            if (el.customData?.isPlayableVideo && el.customData?.videoUrl) {
              setVideoModal({
                url: el.customData.videoUrl,
                title: el.customData.title || 'Educational Demonstration',
                description: el.customData.description || '',
              })
              return
            }
            if (el.customData?.isExpandableImage || el.customData?.fullUrl || el.customData?.isImageCard) {
              const fullUrl =
                el.customData?.fullUrl ||
                el.customData?.imageUrl ||
                (el.type === 'image' && excalidrawAPIRef.current.getFiles?.()?.[el.fileId]?.dataURL)
              if (fullUrl) {
                setLightboxImage({
                  url: fullUrl,
                  title: el.customData?.title || el.customData?.diagramTitle || 'Scientific Diagram',
                  caption: el.customData?.caption || '',
                })
                setLightboxZoom(1)
                setLightboxPan({ x: 0, y: 0 })
                return
              }
            }
          }
        }
      } catch (err) {
        console.warn('[handleContainerClick lightbox error]:', err)
      }
    }, [])

    // Push the responsive zoom into the canvas when the board width crosses the phone breakpoint
    useEffect(() => {
      if (!excalidrawAPI) return
      try {
        excalidrawAPI.updateScene({ appState: { zoom: { value: boardZoom }, gridModeEnabled: true } })
      } catch {}
    }, [boardZoom, excalidrawAPI])

    // Helper to lock zoom to exactly 70% (0.7) and prevent zooming out/in
    const enforceLockedZoom = useCallback((api: any) => {
      if (!api) return
      try {
        const state = api.getAppState()
        if (state && (!state.zoom || Math.abs(state.zoom.value - boardZoomRef.current) > 0.01)) {
          setTimeout(() => {
            try {
              api.updateScene({
                appState: {
                  zoom: { value: boardZoomRef.current },
                  gridModeEnabled: true,
                },
              })
            } catch (err) {}
          }, 50)
        }
      } catch (err) {}
    }, [])

    // Add new page when board fills or AI requests
    const addNewPage = async () => {
      if (!excalidrawAPI) return
      try {
        const convertFn =
          convertElementsRef.current ||
          (await import('@excalidraw/excalidraw')).convertToExcalidrawElements
        convertElementsRef.current = convertFn

        // 1. Save current page state
        if (pagesRef.current[currentPageIndexRef.current]) {
          pagesRef.current[currentPageIndexRef.current].elements = boardElementsRef.current
          pagesRef.current[currentPageIndexRef.current].nextY = nextYRef.current
          pagesRef.current[currentPageIndexRef.current].roughY = roughYRef.current
        }

        // 2. Create new page
        const newPageNum = pagesRef.current.length + 1
        const newConcept = keyConcepts && keyConcepts[newPageNum - 1] ? keyConcepts[newPageNum - 1] : undefined
        const initialSkeleton = createHeaderSkeleton(newPageNum, newConcept)
        const initialElements = convertFn(initialSkeleton)
        const hasConceptTitle = Boolean(newConcept)

        const newPage: WhiteboardPage = {
          id: newPageNum,
          elements: initialElements,
          nextY: hasConceptTitle ? 200 : 140,
          roughY: 140,
        }

        const updatedPages = [...pagesRef.current, newPage]
        const newIdx = updatedPages.length - 1

        pagesRef.current = updatedPages
        currentPageIndexRef.current = newIdx
        setPages(updatedPages)
        setCurrentPageIndex(newIdx)

        nextYRef.current = hasConceptTitle ? 200 : 140
        roughYRef.current = 140
        boardElementsRef.current = initialElements

        excalidrawAPI.updateScene({
          elements: initialElements,
          appState: {
            viewBackgroundColor: 'transparent',
            currentItemStrokeColor: INK_PRIMARY,
            currentItemFontFamily: 1,
            currentItemRoughness: 0,
            gridModeEnabled: true,
            zoom: { value: boardZoomRef.current },
            scrollX: 0,
            scrollY: 0,
          },
        })

        persistScene(initialElements)
        notifyPositionChange('add_new_page')
        onNoteRecorded?.(`--- New Whiteboard Page ${newPageNum} Created ---`)
      } catch (err) {
        console.error('addNewPage error:', err)
      }
    }

    // Switch or dynamically create pages up to targetIdx (0-indexed)
    const goToPage = async (targetIdx: number, conceptTitle?: string) => {
      if (!excalidrawAPI || targetIdx < 0) return

      return enqueueOperation(async () => {
        // Save current page state synchronously if elements exist
        if (pagesRef.current[currentPageIndexRef.current] && boardElementsRef.current && boardElementsRef.current.length > 0) {
          pagesRef.current[currentPageIndexRef.current].elements = boardElementsRef.current
          pagesRef.current[currentPageIndexRef.current].nextY = nextYRef.current
          pagesRef.current[currentPageIndexRef.current].roughY = roughYRef.current
        }

        // If targetIdx is beyond existing pages, create missing pages up to targetIdx
        if (targetIdx >= pagesRef.current.length) {
          try {
            const convertFn =
              convertElementsRef.current ||
              (await import('@excalidraw/excalidraw')).convertToExcalidrawElements
            convertElementsRef.current = convertFn

            const updatedPages = [...pagesRef.current]
            while (updatedPages.length <= targetIdx) {
              const newPageNum = updatedPages.length + 1
              const pageConcept =
                keyConcepts && keyConcepts[newPageNum - 1]
                  ? keyConcepts[newPageNum - 1]
                  : newPageNum - 1 === targetIdx
                  ? conceptTitle
                  : undefined
              const initialSkeleton = createHeaderSkeleton(newPageNum, pageConcept)
              const initialElements = convertFn(initialSkeleton)
              const hasConceptTitle = Boolean(pageConcept)
              updatedPages.push({
                id: newPageNum,
                elements: initialElements,
                nextY: hasConceptTitle ? 200 : 140,
                roughY: 140,
              })
            }
            pagesRef.current = updatedPages
            setPages(updatedPages)
          } catch (err) {
            console.error('goToPage create pages error:', err)
            return
          }
        }

        const targetPage = pagesRef.current[targetIdx]

        // Safety: If target page has 0 elements, regenerate header skeleton so it is NEVER blank!
        if (!targetPage.elements || targetPage.elements.length === 0) {
          try {
            const convertFn =
              convertElementsRef.current ||
              (await import('@excalidraw/excalidraw')).convertToExcalidrawElements
            convertElementsRef.current = convertFn
            const pageConcept =
              conceptTitle ||
              (keyConcepts && keyConcepts[targetIdx] ? keyConcepts[targetIdx] : undefined)
            const skeleton = createHeaderSkeleton(targetIdx + 1, pageConcept)
            targetPage.elements = convertFn(skeleton)
            targetPage.nextY = pageConcept ? 200 : 140
            targetPage.roughY = 140
          } catch (e) {
            console.error('Regenerate page skeleton error:', e)
          }
        }

        currentPageIndexRef.current = targetIdx
        setCurrentPageIndex(targetIdx)

        nextYRef.current = targetPage.nextY || 140
        roughYRef.current = targetPage.roughY || 140
        boardElementsRef.current = targetPage.elements || []

        excalidrawAPI.updateScene({
          elements: targetPage.elements || [],
          appState: {
            viewBackgroundColor: 'transparent',
            currentItemStrokeColor: INK_PRIMARY,
            currentItemFontFamily: 1,
            currentItemRoughness: 0,
            gridModeEnabled: true,
            zoom: { value: boardZoomRef.current },
            scrollX: 0,
            scrollY: 0,
          },
        })
        persistScene(targetPage.elements || [])

        // If the target page somehow lacks a title, add it once
        const targetHasTitle = (targetPage.elements || []).some(
          (el: any) =>
            el.customData?.isTitle === true ||
            (el.type === 'text' && !el.id?.startsWith('header_') && el.fontSize >= 18)
        )
        if (!targetHasTitle && (conceptTitle || keyConcepts?.[targetIdx])) {
          await drawTitle(conceptTitle || keyConcepts[targetIdx])
        }
        notifyPositionChange('go_to_page')
      })
    }

    // Switch between pages and notify parent to update concept tracking
    const switchPage = (targetIdx: number) => {
      goToPage(targetIdx)
      onPageChange?.(targetIdx)
      onConceptGoto?.(targetIdx + 1)
    }

    // 1-Concept-Per-Page invariant: The chalkboard canvas scrolls smoothly vertically.
    // We never auto-flip pages mid-concept so questions, student answers, and verdicts
    // remain permanently together on the concept's dedicated page.
    const checkAutoPageOverflow = async (_requiredHeight = 60) => {
      // Intentionally no-op: page flips are governed strictly by concept progression, not arbitrary pixel heights.
      return
    }

    // Initialize board: restore from localStorage or build initial page
    useEffect(() => {
      if (!excalidrawAPI) return

      if (prevModuleIdRef.current !== moduleId) {
        prevModuleIdRef.current = moduleId
        isInitializedRef.current = false
      }

      if (isInitializedRef.current) return
      isInitializedRef.current = true

      const initializeBoard = async () => {
        try {
          const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
          convertElementsRef.current = convertToExcalidrawElements

          // 1. Check if pages were previously saved
          let savedPages: WhiteboardPage[] | null = null
          try {
            if (typeof window !== 'undefined' && storageKey) {
              const raw = localStorage.getItem(storageKey)
              if (raw) {
                const parsed = JSON.parse(raw)
                if (Array.isArray(parsed) && parsed.length > 0) {
                  savedPages = parsed
                }
              }
            }
          } catch (e) {
            console.error('Error reading saved whiteboard pages:', e)
          }

          try {
            if (typeof window !== 'undefined' && storageKey) {
              const rawFiles = localStorage.getItem(`${storageKey}_files`)
              if (rawFiles && excalidrawAPI?.addFiles) {
                const parsedFiles = JSON.parse(rawFiles)
                const filesArr = Object.values(parsedFiles) as any[]
                const updatedFilesStore: Record<string, any> = {}

                for (const file of filesArr) {
                  if (!file || !file.id || !file.dataURL) continue
                  let currentFile = { ...file }
                  const isSvg =
                    currentFile.mimeType === 'image/svg+xml' ||
                    (typeof currentFile.dataURL === 'string' &&
                      currentFile.dataURL.startsWith('data:image/svg+xml'))

                  if (isSvg) {
                    let rawSvg: string | null = null
                    if (currentFile.dataURL.startsWith('data:image/svg+xml;utf8,')) {
                      try {
                        rawSvg = decodeURIComponent(currentFile.dataURL.slice('data:image/svg+xml;utf8,'.length))
                      } catch {}
                    } else if (currentFile.dataURL.startsWith('data:image/svg+xml;base64,')) {
                      try {
                        const b64 = currentFile.dataURL.slice('data:image/svg+xml;base64,'.length)
                        const binary = atob(b64)
                        const bytes = new Uint8Array(binary.length)
                        for (let i = 0; i < binary.length; i++) {
                          bytes[i] = binary.charCodeAt(i)
                        }
                        rawSvg = new TextDecoder().decode(bytes)
                      } catch {}
                    }

                    if (rawSvg) {
                      const clean = sanitizeSvg(rawSvg)
                      if (clean) {
                        currentFile = {
                          ...currentFile,
                          dataURL: svgToBase64DataUrl(clean),
                          mimeType: 'image/svg+xml',
                        }
                      }
                    }
                  }

                  // Sanitize dataURL to ensure valid base64
                  const cleanDataUrl = sanitizeBase64DataUrl(currentFile.dataURL)
                  if (!cleanDataUrl) {
                    const fallbackSvg = createFallbackImageSvg('Whiteboard Asset', typeof currentFile.dataURL === 'string' ? currentFile.dataURL : '')
                    currentFile.dataURL = svgToBase64DataUrl(fallbackSvg)
                    currentFile.mimeType = 'image/svg+xml'
                  } else {
                    currentFile.dataURL = cleanDataUrl
                  }

                  // Pre-validate SVG files before addFiles so Excalidraw never logs "Invalid SVG"
                  if (currentFile.mimeType === 'image/svg+xml') {
                    const { isValid, cleanSvg } = validateSvgForExcalidraw(currentFile.dataURL)
                    if (!isValid) {
                      try {
                        const pngUrl = await rasterizeSvgToPng(cleanSvg || createFallbackImageSvg('Whiteboard Asset'), 500, 260)
                        const cleanPng = sanitizeBase64DataUrl(pngUrl)
                        if (cleanPng) {
                          currentFile = {
                            ...currentFile,
                            dataURL: cleanPng,
                            mimeType: 'image/png',
                          }
                        } else {
                          const fallbackSvg = createFallbackImageSvg('Whiteboard Asset')
                          currentFile = {
                            ...currentFile,
                            dataURL: svgToBase64DataUrl(fallbackSvg),
                            mimeType: 'image/svg+xml',
                          }
                        }
                      } catch {
                        const fallbackSvg = createFallbackImageSvg('Whiteboard Asset')
                        currentFile = {
                          ...currentFile,
                          dataURL: svgToBase64DataUrl(fallbackSvg),
                          mimeType: 'image/svg+xml',
                        }
                      }
                    }
                  }

                  if (isValidBase64DataUrl(currentFile.dataURL)) {
                    try {
                      excalidrawAPI.addFiles([currentFile])
                      updatedFilesStore[currentFile.id] = currentFile
                    } catch (fileErr) {
                      console.warn(`File ${currentFile.id} failed addFiles:`, fileErr)
                    }
                  }                }

                // Resave cleaned files to localStorage so invalid SVGs are pruned
                try {
                  safeSaveWhiteboardStorage(`${storageKey}_files`, updatedFilesStore, true)
                } catch {}
              }
            }
          } catch (e) {
            console.warn('Error reading saved whiteboard files:', e)
          }

          const initialTargetIdx = typeof activeConceptIndex === 'number' && activeConceptIndex > 0 ? activeConceptIndex : 0
          const reachedPagesCount = Math.max(1, initialTargetIdx + 1)
          const hasValidElements =
            savedPages &&
            savedPages.length > 0 &&
            savedPages.some((p) => Array.isArray(p.elements) && p.elements.length > 0)

          if (hasValidElements && savedPages) {
            // Restore ALL saved pages across reload (never slice or truncate user notes)
            savedPages.forEach((p, idx) => {
              if (!p.elements || p.elements.length === 0) {
                const pageConcept = keyConcepts && keyConcepts[idx] ? keyConcepts[idx] : undefined
                const skeleton = createHeaderSkeleton(idx + 1, pageConcept)
                p.elements = convertElementsRef.current(skeleton)
                p.nextY = pageConcept ? 200 : 140
                p.roughY = 140
              }
            })
            pagesRef.current = savedPages
            setPages(savedPages)
            const targetPage = savedPages[initialTargetIdx] || savedPages[0]
            currentPageIndexRef.current = initialTargetIdx < savedPages.length ? initialTargetIdx : 0
            setCurrentPageIndex(currentPageIndexRef.current)
            boardElementsRef.current = targetPage.elements || []
            nextYRef.current = targetPage.nextY || 140
            roughYRef.current = targetPage.roughY || 140

            excalidrawAPI.updateScene({
              elements: targetPage.elements || [],
              appState: {
                viewBackgroundColor: 'transparent',
                currentItemStrokeColor: INK_PRIMARY,
                currentItemFontFamily: 1,
                currentItemRoughness: 0,
                gridModeEnabled: true,
                zoom: { value: boardZoomRef.current },
                scrollX: 0,
                scrollY: 0,
              },
            })
            return
          }

          // 2. Otherwise create initial fresh page skeleton only for reached concepts
          const initialPages: WhiteboardPage[] = []
          for (let p = 1; p <= reachedPagesCount; p++) {
            const conceptForPage = keyConcepts && keyConcepts[p - 1] ? keyConcepts[p - 1] : undefined
            const initialSkeleton = createHeaderSkeleton(p, conceptForPage)
            const initialElements = convertToExcalidrawElements(initialSkeleton)
            const hasConceptTitle = Boolean(conceptForPage)
            initialPages.push({
              id: p,
              elements: initialElements,
              nextY: hasConceptTitle ? 200 : 140,
              roughY: 140,
            })
          }

          pagesRef.current = initialPages
          setPages(initialPages)
          const chosenPage = initialPages[initialTargetIdx] || initialPages[0]
          currentPageIndexRef.current = initialTargetIdx < initialPages.length ? initialTargetIdx : 0
          setCurrentPageIndex(currentPageIndexRef.current)
          boardElementsRef.current = chosenPage.elements
          nextYRef.current = chosenPage.nextY
          roughYRef.current = chosenPage.roughY

          excalidrawAPI.updateScene({
            elements: chosenPage.elements,
            appState: {
              viewBackgroundColor: 'transparent',
              currentItemStrokeColor: INK_PRIMARY,
              currentItemFontFamily: 1,
              currentItemRoughness: 0,
              gridModeEnabled: true,
              zoom: { value: boardZoomRef.current },
              scrollX: 0,
              scrollY: 0,
            },
          })
          persistScene(chosenPage.elements)
        } catch (e) {
          console.error('Failed to initialize whiteboard:', e)
        }
      }

      initializeBoard()
    }, [excalidrawAPI, moduleId, moduleTitle])

    // Draw text in permanent notes column (left side)
    const drawText = async (text: string, x = 60, customY?: number, color?: string) => {
      if (!excalidrawAPI || !text?.trim()) return
      const clean = cleanChalkboardTypography(text.trim())
      if (checkIsRedundant(clean)) return
      if (executedTextHistoryRef.current.has(clean.toLowerCase())) return
      executedTextHistoryRef.current.add(clean.toLowerCase())

      const lines = wrapText(clean, cols(62))
      const lineHeight = 24
      const totalH = Math.max(30, lines.length * lineHeight)

      await checkAutoPageOverflow(totalH + 16)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const y = customY !== undefined ? customY : getDynamicNextY(15)
        const chosenColor = resolveChalkColor(color, activeChalkColorRef.current)

        const newElements = convertToExcalidrawElements([
          {
            type: 'text',
            x,
            y,
            text: lines.join('\n'),
            fontSize: 18,
            fontFamily: 1,
            strokeColor: chosenColor,
            customData: { isRough: false },
          },
        ])

        const currentElements = getCurrentElements()
        const merged = [...currentElements, ...newElements]
        updateCurrentPageElements(merged, y + totalH + 12)
        notifyPositionChange('draw_text', clean)
        onNoteRecorded?.(clean)
      } catch (err) {
        console.error('drawText error:', err)
      }
    }

    // Draw Section Title with Botanical Accent Underline (rendered once per page)
    const drawTitle = async (title: any, color?: string) => {
      if (!excalidrawAPI) return
      const raw = typeof title === 'string' ? title : (title?.content || title?.text || title?.title || (title ? JSON.stringify(title) : ''))
      if (!raw?.trim()) return
      const rawClean = raw
        .replace(/^focus:\s*/i, '')
        .replace(/^concept\s*\d*:\s*/i, '')
        .replace(/[\(\)\[\]\{\}\"]/g, '')
        .replace(/^'+|'+$/g, '')
        .replace(/\s+/g, ' ')
        .trim()
      const clean = cleanChalkboardTypography(rawClean)
      if (!clean) return

      // Invariant: Never write Mastered or Concept Done as a title
      if (checkIsRedundant(clean) || /^(concept\s*\d*\s*)?(done|mastered|completed)\b[:\-]?/i.test(clean) || /\b(mastered)\b/i.test(clean)) {
        return
      }

      // Skip if identical to module title
      if (normalizeTitle(clean) === normalizeTitle(moduleTitle)) {
        return
      }

      // Check if current page already has a concept title or topic headline (synchronous check)
      const currentEls = getCurrentElements()
      const hasTitleOnCurrentPage = currentEls.some(
        (el: any) =>
          el.customData?.isTitle === true ||
          (el.type === 'text' && !el.id?.startsWith('header_') && el.fontSize >= 18)
      )
      if (hasTitleOnCurrentPage) {
        return
      }

      await checkAutoPageOverflow(65)
      try {
        const convertFn =
          convertElementsRef.current ||
          (await import('@excalidraw/excalidraw')).convertToExcalidrawElements
        convertElementsRef.current = convertFn

        const startX = 60
        const startY = getDynamicNextY(16)
        nextYRef.current = Math.max(nextYRef.current, startY + 54)
        const titleText = `CONCEPT ${currentPageIndexRef.current + 1}: ${clean.toUpperCase()}`
        const titleColor = resolveChalkColor(color, INK_PRIMARY)
        const underlineColor = color ? titleColor : INK_BOTANICAL

        await playTypingEffect('Topic', titleText, titleColor, startX, startY, 19, 'none')

        const elements = convertFn([
          {
            type: 'text',
            x: startX,
            y: startY,
            text: titleText,
            fontSize: 19,
            fontFamily: 1,
            strokeColor: titleColor,
            customData: { isRough: false, isTitle: true },
          },
          {
            type: 'line',
            x: startX,
            y: startY + 28,
            points: [[0, 0], [Math.min(titleText.length * 12, 380), 0]],
            strokeColor: underlineColor,
            strokeWidth: 2,
            customData: { isRough: false, isTitle: true },
          },
        ])

        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, startY + 48)
        onNoteRecorded?.(`### ${clean}`)
      } catch (err) {
        console.error('drawTitle error:', err)
      }
    }

    // Draw Note with botanical indicator
    const drawNote = async (noteText: any, color?: string) => {
      if (!excalidrawAPI) return
      const raw = typeof noteText === 'string' ? noteText : (noteText?.content || noteText?.text || noteText?.note || (noteText ? JSON.stringify(noteText) : ''))
      if (!raw?.trim()) return
      const clean = cleanChalkboardTypography(raw.trim())
      if (checkIsRedundant(clean)) return
      if (shouldSkipDuplicate('draw_note', clean)) return

      const lines = wrapText(clean, cols(64))
      const lineHeight = 22
      const totalH = Math.max(28, lines.length * lineHeight)

      await checkAutoPageOverflow(totalH + 16)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const startY = getDynamicNextY(12)
        nextYRef.current = Math.max(nextYRef.current, startY + totalH + 16)
        const noteColor = resolveChalkColor(color, activeChalkColorRef.current)
        const bulletColor = color ? noteColor : INK_BOTANICAL

        await playTypingEffect('Note', clean, noteColor, startX, startY, 16, 'dot', bulletColor)

        const elements = convertToExcalidrawElements([
          {
            type: 'ellipse',
            x: startX,
            y: startY + 6,
            width: 8,
            height: 8,
            strokeColor: bulletColor,
            backgroundColor: bulletColor,
            fillStyle: 'solid',
            customData: { isRough: false },
          },
          {
            type: 'text',
            x: startX + 16,
            y: startY,
            text: lines.join('\n'),
            fontSize: 16,
            fontFamily: 1,
            strokeColor: noteColor,
            customData: { isRough: false },
          },
        ])

        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, startY + totalH + 12)
        notifyPositionChange('draw_note', clean)
        onNoteRecorded?.(`• ${clean}`)
      } catch (err) {
        console.error('drawNote error:', err)
      }
    }

    // Draw Step / Derivation Line
    const drawStep = async (stepText: any, color?: string) => {
      if (!excalidrawAPI) return
      const raw = typeof stepText === 'string' ? stepText : (stepText?.content || stepText?.text || stepText?.step || (stepText ? JSON.stringify(stepText) : ''))
      if (!raw?.trim()) return
      const clean = cleanChalkboardTypography(raw.trim())
      if (checkIsRedundant(clean)) return
      if (shouldSkipDuplicate('draw_step', clean)) return
      const lines = wrapText(clean, cols(60))
      const lineHeight = 21
      const totalH = Math.max(26, lines.length * lineHeight)

      await checkAutoPageOverflow(totalH + 16)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const startY = getDynamicNextY(12)
        nextYRef.current = Math.max(nextYRef.current, startY + totalH + 16)
        const stepColor = resolveChalkColor(color, INK_SECONDARY)

        await playTypingEffect('Step', clean, stepColor, startX, startY, 15, 'step')

        const elements = convertToExcalidrawElements([
          {
            type: 'text',
            x: startX,
            y: startY,
            text: lines.map((l, i) => (i === 0 ? `->  ${l}` : `    ${l}`)).join('\n'),
            fontSize: 15,
            fontFamily: 1,
            strokeColor: stepColor,
            customData: { isRough: false },
          },
        ])

        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, startY + totalH + 12)
        executedTextHistoryRef.current.add(clean.toLowerCase().replace(/[^a-z0-9]/g, ''))
        notifyPositionChange('draw_step', clean)
        onNoteRecorded?.(`  -> ${clean}`)
      } catch (err) {
        console.error('drawStep error:', err)
      }
    }

    // Draw Highlight Box / Governed Law / Formula in Coral Accent
    const drawHighlightBox = async (text: any, color?: string) => {
      if (!excalidrawAPI) return
      const raw = typeof text === 'string' ? text : (text?.content || text?.text || text?.box || (text ? JSON.stringify(text) : ''))
      if (!raw?.trim()) return
      const clean = cleanChalkboardTypography(raw.trim())
      if (checkIsRedundant(clean)) return
      if (shouldSkipDuplicate('draw_highlight_box', clean)) return
      const lines = wrapText(clean, cols(60))
      const boxWidth = 740
      const lineHeight = 22
      const textHeight = Math.max(1, lines.length) * lineHeight
      const boxHeight = Math.max(54, 16 + textHeight + 16)

      await checkAutoPageOverflow(boxHeight + 20)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const startY = getDynamicNextY(16)
        nextYRef.current = Math.max(nextYRef.current, startY + boxHeight + 20)
        const boxStroke = resolveChalkColor(color, INK_CORAL)
        const boxBg = boxStroke === INK_CORAL ? INK_CORAL_SOFT : '#F8F6F0'

        const elements = convertToExcalidrawElements([
          {
            type: 'rectangle',
            x: startX,
            y: startY,
            width: boxWidth,
            height: boxHeight,
            strokeColor: boxStroke,
            backgroundColor: boxBg,
            fillStyle: 'solid',
            strokeWidth: 1.5,
            roundness: { type: 3 },
            customData: { isRough: false },
          },
          {
            type: 'text',
            x: startX + 16,
            y: startY + 14,
            text: lines.join('\n'),
            fontSize: 16,
            fontFamily: 1,
            strokeColor: INK_PRIMARY,
            customData: { isRough: false },
          },
        ])

        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, startY + boxHeight + 14)
        executedTextHistoryRef.current.add(clean.toLowerCase().replace(/[^a-z0-9]/g, ''))
        notifyPositionChange('draw_highlight_box', clean)
        onNoteRecorded?.(`**[Key Principle]**: ${clean}`)
      } catch (err) {
        console.error('drawHighlightBox error:', err)
      }
    }

    // Draw Exam / Checkpoint Question Callout (Full Width, Crisp Layout)
    const drawQuestion = async (questionText: any, color?: string) => {
      if (!excalidrawAPI) return
      const raw = typeof questionText === 'string' ? questionText : (questionText?.content || questionText?.text || questionText?.question || (questionText ? JSON.stringify(questionText) : ''))
      if (!raw?.trim()) return
      const clean = cleanChalkboardTypography(raw.trim())
      if (shouldSkipDuplicate('draw_question', clean)) return
      const lines = wrapText(clean, cols(64))
      const lineHeight = 22
      const paddingTop = 28
      const textHeight = Math.max(1, lines.length) * lineHeight
      const paddingBottom = 20
      const qHeight = Math.max(68, paddingTop + textHeight + paddingBottom)

      await checkAutoPageOverflow(qHeight + 20)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const startY = getDynamicNextY(16)
        nextYRef.current = Math.max(nextYRef.current, startY + qHeight + 20)
        const qStroke = resolveChalkColor(color, INK_CORAL)

        const elements = convertToExcalidrawElements([
          {
            type: 'rectangle',
            x: startX,
            y: startY,
            width: 740,
            height: qHeight,
            strokeColor: qStroke,
            backgroundColor: '#FFF8F6',
            fillStyle: 'solid',
            strokeWidth: 1.5,
            roundness: { type: 3 },
            customData: { isRough: false },
          },
          {
            type: 'text',
            x: startX + 16,
            y: startY + 8,
            text: 'CHECKPOINT QUESTION:',
            fontSize: 11,
            fontFamily: 1,
            strokeColor: qStroke,
            customData: { isRough: false },
          },
          {
            type: 'text',
            x: startX + 16,
            y: startY + 28,
            text: lines.join('\n'),
            fontSize: 15,
            fontFamily: 1,
            strokeColor: INK_PRIMARY,
            customData: { isRough: false },
          },
        ])

        activeQuestionRef.current = {
          text: clean,
          y: startY,
          height: qHeight,
          pageIndex: currentPageIndexRef.current,
        }

        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, startY + qHeight + 14)
        executedTextHistoryRef.current.add(clean.toLowerCase().replace(/[^a-z0-9]/g, ''))
        notifyPositionChange('draw_question', clean)
        onNoteRecorded?.(`? **Question**: ${clean}`)
      } catch (err) {
        console.error('drawQuestion error:', err)
      }
    }

    // Draw Student's Spoken Answer on Whiteboard
    const drawStudentAnswer = async (answerText: string, isCorrect?: boolean, color?: string) => {
      if (!excalidrawAPI || !answerText?.trim()) return
      const clean = cleanChalkboardTypography(answerText.trim())

      // Deduplicate recent identical or redundant student responses within 30 seconds
      const cleanLower = clean.toLowerCase().replace(/^(?:student(?:'s)?\s*answer:?\s*)+/i, '').trim()
      if (lastDrawnStudentAnswerRef.current) {
        const prevLower = lastDrawnStudentAnswerRef.current.text.toLowerCase().replace(/^(?:student(?:'s)?\s*answer:?\s*)+/i, '').trim()
        const isRecent = Date.now() - lastDrawnStudentAnswerRef.current.time < 30000
        if (isRecent && (cleanLower === prevLower || cleanLower.includes(prevLower) || prevLower.includes(cleanLower))) {
          console.log('[Chalkboard] Skipping duplicate student answer render:', clean)
          return
        }
      }
      lastDrawnStudentAnswerRef.current = { text: clean, time: Date.now() }

      const lines = wrapText(`"${clean}"`, cols(64))
      const lineHeight = 20
      const paddingTop = 26
      const textHeight = Math.max(1, lines.length) * lineHeight
      const paddingBottom = 18
      const boxHeight = Math.max(64, paddingTop + textHeight + paddingBottom)

      await checkAutoPageOverflow(boxHeight + 18)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const startY = getDynamicNextY(14)
        nextYRef.current = Math.max(nextYRef.current, startY + boxHeight + 18)
        const ansStroke = resolveChalkColor(color, INK_BLUE)

        const elements = convertToExcalidrawElements([
          {
            type: 'rectangle',
            x: startX,
            y: startY,
            width: 740,
            height: boxHeight,
            strokeColor: ansStroke,
            backgroundColor: '#F0F7FF',
            fillStyle: 'solid',
            strokeWidth: 1.5,
            roundness: { type: 3 },
            customData: { isRough: false },
          },
          {
            type: 'text',
            x: startX + 16,
            y: startY + 8,
            text: "STUDENT'S RESPONSE:",
            fontSize: 11,
            fontFamily: 1,
            strokeColor: ansStroke,
            customData: { isRough: false },
          },
          {
            type: 'text',
            x: startX + 16,
            y: startY + 26,
            text: lines.join('\n'),
            fontSize: 14,
            fontFamily: 1,
            strokeColor: INK_PRIMARY,
            customData: { isRough: false },
          },
        ])

        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, startY + boxHeight + 14)
        notifyPositionChange('draw_student_answer', clean)
        onNoteRecorded?.(`**Student**: "${clean}"`)
      } catch (err) {
        console.error('drawStudentAnswer error:', err)
      }
    }

    // Draw Answer Verdict / Correction on Whiteboard
    const drawAnswerVerdict = async (verdictText: string, isCorrect?: boolean, color?: string) => {
      if (!excalidrawAPI || !verdictText?.trim()) return
      const clean = cleanChalkboardTypography(verdictText.trim())
      const looksCorrect =
        isCorrect === true ||
        /^(correct|spot on|perfect|exactly|well done|excellent|right|yes)\b/i.test(clean) ||
        /\b(correct|spot on|perfect|well done)\b/i.test(clean)
      const lines = wrapText(clean, cols(64))
      const lineHeight = 20
      const paddingTop = 26
      const textHeight = Math.max(1, lines.length) * lineHeight
      const paddingBottom = 18
      const boxHeight = Math.max(64, paddingTop + textHeight + paddingBottom)

      await checkAutoPageOverflow(boxHeight + 18)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const startY = getDynamicNextY(14)
        nextYRef.current = Math.max(nextYRef.current, startY + boxHeight + 18)
        const vStroke = resolveChalkColor(
          color,
          looksCorrect ? INK_BOTANICAL : INK_CORAL
        )
        const vBg = looksCorrect ? '#F0FDF4' : '#FFF1F2'

        const elements = convertToExcalidrawElements([
          {
            type: 'rectangle',
            x: startX,
            y: startY,
            width: 740,
            height: boxHeight,
            strokeColor: vStroke,
            backgroundColor: vBg,
            fillStyle: 'solid',
            strokeWidth: 1.5,
            roundness: { type: 3 },
            customData: { isRough: false },
          },
          {
            type: 'text',
            x: startX + 16,
            y: startY + 8,
            text: looksCorrect ? 'VERDICT: CORRECT & COMPLETE' : 'MODEL CORRECTION & REFINED ANSWER:',
            fontSize: 11,
            fontFamily: 1,
            strokeColor: vStroke,
            customData: { isRough: false },
          },
          {
            type: 'text',
            x: startX + 16,
            y: startY + 26,
            text: lines.join('\n'),
            fontSize: 14,
            fontFamily: 1,
            strokeColor: INK_PRIMARY,
            customData: { isRough: false },
          },
        ])

        // Question resolved
        activeQuestionRef.current = null

        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, startY + boxHeight + 14)
        notifyPositionChange('draw_answer_verdict', clean)
        onNoteRecorded?.(`**Verdict**: ${clean}`)
      } catch (err) {
        console.error('drawAnswerVerdict error:', err)
      }
    }

    // Draw Exam Question & Model Answer on Whiteboard
    const drawExamQuestion = async (
      question: string,
      modelAnswer?: string,
      marks?: string,
      color?: string
    ) => {
      if (!excalidrawAPI || !question?.trim()) return
      if (shouldSkipDuplicate('draw_exam_question', question)) return

      // Support "question | model answer" in single string if modelAnswer omitted
      let qText = cleanChalkboardTypography(question.trim())
      let aText = cleanChalkboardTypography((modelAnswer || '').trim())
      if (!aText && qText.includes('|')) {
        const parts = qText.split('|').map((s) => s.trim())
        qText = cleanChalkboardTypography(parts[0])
        aText = cleanChalkboardTypography(parts.slice(1).join(' | ').replace(/^answer:\s*/i, ''))
      }

      const qLines = wrapText(qText, cols(60))
      const qLineHeight = 22
      const qTextHeight = qLines.length * qLineHeight
      let aLines: string[] = []
      let aTextHeight = 0
      if (aText) {
        aLines = wrapText(aText, cols(58))
        aTextHeight = aLines.length * 20
      }

      const cardHeight = 28 + qTextHeight + (aText ? 12 + 24 + aTextHeight : 0) + 24
      await checkAutoPageOverflow(cardHeight + 20)

      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const startY = getDynamicNextY(16)
        const exStroke = resolveChalkColor(color, INK_AMBER)

        const skeletons: any[] = [
          {
            type: 'rectangle',
            x: startX,
            y: startY,
            width: 740,
            height: cardHeight,
            strokeColor: exStroke,
            backgroundColor: '#FDFCF7',
            fillStyle: 'solid',
            strokeWidth: 2,
            roundness: { type: 3 },
            customData: { isRough: false },
          },
          {
            type: 'text',
            x: startX + 16,
            y: startY + 10,
            text: `BOARD EXAM QUESTION ${marks ? `[${marks}]` : '[Typical Board Pattern]'}:`,
            fontSize: 11,
            fontFamily: 1,
            strokeColor: exStroke,
            customData: { isRough: false },
          },
          {
            type: 'text',
            x: startX + 16,
            y: startY + 28,
            text: `Q: ${qLines.join('\n   ')}`,
            fontSize: 15,
            fontFamily: 1,
            strokeColor: INK_PRIMARY,
            customData: { isRough: false },
          },
        ]

        let curY = startY + 28 + qTextHeight + 12

        if (aText) {
          skeletons.push(
            {
              type: 'line',
              x: startX + 16,
              y: curY,
              points: [[0, 0], [708, 0]],
              strokeColor: BORDER_SUBTLE,
              strokeWidth: 1,
              strokeStyle: 'dashed',
              customData: { isRough: false },
            },
            {
              type: 'text',
              x: startX + 16,
              y: curY + 6,
              text: 'TOPPER MODEL ANSWER:',
              fontSize: 11,
              fontFamily: 1,
              strokeColor: INK_BOTANICAL,
              customData: { isRough: false },
            },
            {
              type: 'text',
              x: startX + 16,
              y: curY + 24,
              text: `Ans: ${aLines.join('\n     ')}`,
              fontSize: 14,
              fontFamily: 1,
              strokeColor: INK_PRIMARY,
              customData: { isRough: false },
            }
          )
        }

        const elements = convertToExcalidrawElements(skeletons)
        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, startY + cardHeight + 16)
        executedTextHistoryRef.current.add(qText.toLowerCase().replace(/[^a-z0-9]/g, ''))
        notifyPositionChange('draw_exam_question', qText)
        onNoteRecorded?.(`**Exam Question**: ${qText}\n**Model Answer**: ${aText}`)
      } catch (err) {
        console.error('drawExamQuestion error:', err)
      }
    }

    // Helper parser for custom shapes with dynamic sizing
    const parseShapeInput = (input: any): {
      shape: string
      width: number
      height: number
      radius?: number
      label?: string
      color?: string
      fillColor?: string
    } => {
      if (typeof input === 'object' && input !== null) {
        const shape = String(input.shape || input.type || 'rectangle').toLowerCase().trim()
        const width = Number(input.width || input.w || input.dimension1 || input.length || 260)
        const height = Number(input.height || input.h || input.dimension2 || 140)
        const radius = input.radius !== undefined ? Number(input.radius) : undefined
        return {
          shape,
          width,
          height,
          radius,
          label: input.label || input.title || input.text || '',
          color: input.color,
          fillColor: input.fillColor || input.fill || input.bg,
        }
      }

      const str = String(input || '').trim()
      if (str.startsWith('{') && str.endsWith('}')) {
        try {
          const parsed = JSON.parse(str)
          return parseShapeInput(parsed)
        } catch {}
      }

      let shape = 'rectangle'
      let width = 260
      let height = 140
      let radius: number | undefined
      let label = ''
      let color: string | undefined
      let fillColor: string | undefined

      const lower = str.toLowerCase()
      if (lower.includes('circle')) shape = 'circle'
      else if (lower.includes('right_triangle') || lower.includes('right triangle')) shape = 'right_triangle'
      else if (lower.includes('triangle')) shape = 'triangle'
      else if (lower.includes('ellipse')) shape = 'ellipse'
      else if (lower.includes('cylinder')) shape = 'cylinder'
      else if (lower.includes('cube') || lower.includes('cuboid') || lower.includes('box')) shape = 'cube'
      else if (lower.includes('square')) shape = 'square'
      else if (lower.includes('polygon')) shape = 'polygon'
      else if (lower.includes('arrow') || lower.includes('line')) shape = 'arrow'
      else if (lower.includes('rectangle')) shape = 'rectangle'

      const wMatch = str.match(/\b(?:width|w|length|len)[:=]\s*(\d+(?:\.\d+)?)/i)
      if (wMatch) width = parseFloat(wMatch[1])

      const hMatch = str.match(/\b(?:height|h|breadth|b)[:=]\s*(\d+(?:\.\d+)?)/i)
      if (hMatch) height = parseFloat(hMatch[1])

      const rMatch = str.match(/\b(?:radius|rad|r)[:=]\s*(\d+(?:\.\d+)?)/i)
      if (rMatch) radius = parseFloat(rMatch[1])

      const labelMatch = str.match(/\b(?:label|title|text)[:=]\s*(?:"([^"]+)"|'([^']+)'|([^|;\n]+))/i)
      if (labelMatch) label = (labelMatch[1] || labelMatch[2] || labelMatch[3] || '').trim()

      const colMatch = str.match(/\b(?:color|stroke)[:=]\s*([a-zA-Z#0-9]+)/i)
      if (colMatch) color = colMatch[1].trim()

      const fillMatch = str.match(/\b(?:fill|fillColor|bg)[:=]\s*([a-zA-Z#0-9]+)/i)
      if (fillMatch) fillColor = fillMatch[1].trim()

      if (!label && str.includes('|')) {
        const parts = str.split('|').map((p) => p.trim())
        if (parts.length > 1 && !parts[1].includes(':') && !parts[1].includes('=')) {
          label = parts[1]
        }
      }

      return { shape, width, height, radius, label, color, fillColor }
    }

    // Draw Geometric Shape with Complete Size, Dimension & Label Control
    const drawShape = async (shapeInput: any) => {
      if (!excalidrawAPI) return
      const { shape, width, height, radius, label, color, fillColor } = parseShapeInput(shapeInput)
      const stroke = resolveChalkColor(color, INK_BOTANICAL)
      const bg = fillColor || (stroke === INK_CORAL ? INK_CORAL_SOFT : '#F0F6F2')

      const startX = 70
      let w = Math.min(Math.max(width, 40), 720)
      let h = Math.min(Math.max(height, 30), 450)
      if (shape === 'square') {
        w = Math.min(w, h)
        h = w
      }

      await checkAutoPageOverflow(h + (label ? 60 : 30))

      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startY = getDynamicNextY(16)
        const skeletons: any[] = []

        if (shape === 'rectangle' || shape === 'square' || shape === 'box') {
          skeletons.push({
            type: 'rectangle',
            x: startX,
            y: startY,
            width: w,
            height: h,
            strokeColor: stroke,
            backgroundColor: bg,
            fillStyle: 'solid',
            strokeWidth: 2,
            roundness: { type: 3 },
            customData: { isRough: false },
          })

          skeletons.push({
            type: 'text',
            x: startX + Math.max(Math.floor(w / 2) - 35, 10),
            y: startY - 18,
            text: `w: ${w}px`,
            fontSize: 12,
            fontFamily: 1,
            strokeColor: INK_MUTED,
            customData: { isRough: false },
          })

          skeletons.push({
            type: 'text',
            x: startX + w + 8,
            y: startY + Math.floor(h / 2) - 8,
            text: `h: ${h}px`,
            fontSize: 12,
            fontFamily: 1,
            strokeColor: INK_MUTED,
            customData: { isRough: false },
          })
        } else if (shape === 'circle') {
          const r = radius ? radius : Math.floor(Math.min(w, h) / 2)
          const diam = r * 2
          skeletons.push(
            {
              type: 'ellipse',
              x: startX,
              y: startY,
              width: diam,
              height: diam,
              strokeColor: stroke,
              backgroundColor: bg,
              fillStyle: 'solid',
              strokeWidth: 2,
              customData: { isRough: false },
            },
            {
              type: 'ellipse',
              x: startX + r - 3,
              y: startY + r - 3,
              width: 6,
              height: 6,
              strokeColor: stroke,
              backgroundColor: stroke,
              fillStyle: 'solid',
              customData: { isRough: false },
            },
            {
              type: 'line',
              x: startX + r,
              y: startY + r,
              points: [[0, 0], [r, 0]],
              strokeColor: INK_CORAL,
              strokeWidth: 2,
              customData: { isRough: false },
            },
            {
              type: 'text',
              x: startX + r + Math.floor(r / 2) - 8,
              y: startY + r - 16,
              text: `r: ${r}`,
              fontSize: 12,
              fontFamily: 1,
              strokeColor: INK_CORAL,
              customData: { isRough: false },
            }
          )
          w = diam
          h = diam
        } else if (shape === 'ellipse') {
          skeletons.push({
            type: 'ellipse',
            x: startX,
            y: startY,
            width: w,
            height: h,
            strokeColor: stroke,
            backgroundColor: bg,
            fillStyle: 'solid',
            strokeWidth: 2,
            customData: { isRough: false },
          })
        } else if (shape === 'triangle' || shape === 'right_triangle') {
          const isRight = shape === 'right_triangle'
          const pts = isRight
            ? [[0, 0], [w, 0], [0, -h], [0, 0]]
            : [[0, 0], [w, 0], [Math.floor(w / 2), -h], [0, 0]]

          skeletons.push(
            {
              type: 'line',
              x: startX,
              y: startY + h,
              points: pts,
              strokeColor: stroke,
              strokeWidth: 2,
              backgroundColor: bg,
              fillStyle: 'solid',
              customData: { isRough: false },
            },
            {
              type: 'text',
              x: startX - 14,
              y: startY + h + 2,
              text: 'A',
              fontSize: 13,
              fontFamily: 1,
              strokeColor: INK_CORAL,
              customData: { isRough: false },
            },
            {
              type: 'text',
              x: startX + w + 4,
              y: startY + h + 2,
              text: 'B',
              fontSize: 13,
              fontFamily: 1,
              strokeColor: INK_CORAL,
              customData: { isRough: false },
            },
            {
              type: 'text',
              x: isRight ? startX - 14 : startX + Math.floor(w / 2) - 6,
              y: startY - 14,
              text: 'C',
              fontSize: 13,
              fontFamily: 1,
              strokeColor: INK_CORAL,
              customData: { isRough: false },
            }
          )
        } else if (shape === 'cylinder') {
          const r = radius ? radius : Math.floor(w / 4)
          const cylW = r * 2
          const topH = Math.max(Math.floor(r * 0.6), 18)
          skeletons.push(
            {
              type: 'ellipse',
              x: startX,
              y: startY + h - topH,
              width: cylW,
              height: topH * 2,
              strokeColor: stroke,
              backgroundColor: bg,
              fillStyle: 'solid',
              strokeWidth: 2,
              customData: { isRough: false },
            },
            {
              type: 'line',
              x: startX,
              y: startY + topH,
              points: [[0, 0], [0, h - topH]],
              strokeColor: stroke,
              strokeWidth: 2,
              customData: { isRough: false },
            },
            {
              type: 'line',
              x: startX + cylW,
              y: startY + topH,
              points: [[0, 0], [0, h - topH]],
              strokeColor: stroke,
              strokeWidth: 2,
              customData: { isRough: false },
            },
            {
              type: 'ellipse',
              x: startX,
              y: startY,
              width: cylW,
              height: topH * 2,
              strokeColor: stroke,
              backgroundColor: bg,
              fillStyle: 'solid',
              strokeWidth: 2,
              customData: { isRough: false },
            },
            {
              type: 'text',
              x: startX + cylW + 12,
              y: startY + Math.floor(h / 2),
              text: `Height = ${h}px`,
              fontSize: 12,
              fontFamily: 1,
              strokeColor: INK_MUTED,
              customData: { isRough: false },
            }
          )
          w = cylW
        } else if (shape === 'cube' || shape === 'cuboid') {
          const offset = 24
          skeletons.push(
            {
              type: 'rectangle',
              x: startX + offset,
              y: startY,
              width: w,
              height: h,
              strokeColor: BORDER_SUBTLE,
              strokeWidth: 1.5,
              strokeStyle: 'dashed',
              customData: { isRough: false },
            },
            {
              type: 'rectangle',
              x: startX,
              y: startY + offset,
              width: w,
              height: h,
              strokeColor: stroke,
              backgroundColor: bg,
              fillStyle: 'solid',
              strokeWidth: 2,
              roundness: { type: 3 },
              customData: { isRough: false },
            },
            {
              type: 'line',
              x: startX,
              y: startY + offset,
              points: [[0, 0], [offset, -offset]],
              strokeColor: stroke,
              strokeWidth: 1.5,
              customData: { isRough: false },
            },
            {
              type: 'line',
              x: startX + w,
              y: startY + offset,
              points: [[0, 0], [offset, -offset]],
              strokeColor: stroke,
              strokeWidth: 1.5,
              customData: { isRough: false },
            },
            {
              type: 'line',
              x: startX + w,
              y: startY + offset + h,
              points: [[0, 0], [offset, -offset]],
              strokeColor: stroke,
              strokeWidth: 1.5,
              customData: { isRough: false },
            }
          )
        } else if (shape === 'arrow' || shape === 'line') {
          skeletons.push({
            type: 'arrow',
            x: startX,
            y: startY + 15,
            points: [[0, 0], [w, 0]],
            strokeColor: stroke,
            strokeWidth: 3,
            customData: { isRough: false },
          })
          h = 30
        }

        if (label) {
          skeletons.push({
            type: 'text',
            x: startX,
            y: startY + h + 14,
            text: label,
            fontSize: 15,
            fontFamily: 1,
            strokeColor: INK_PRIMARY,
            customData: { isRough: false },
          })
        }

        const elements = convertToExcalidrawElements(skeletons)
        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, startY + h + (label ? 42 : 24))
        onNoteRecorded?.(`[Shape: ${shape}] ${label || `${w}x${h}`}`)
      } catch (err) {
        console.error('drawShape error:', err)
      }
    }

    // Universal Topic-Adaptive Flowchart on Board (Multi-Level Trees, Branching Decisions, Multi-Row Wrapping & Cycles)
    const drawFlowchart = async (flowText: string, color?: string) => {
      if (!excalidrawAPI || !flowText?.trim()) return
      if (shouldSkipDuplicate('draw_flowchart', flowText)) return
      const rawText = flowText.trim()
      const isCycle = rawText.toLowerCase().startsWith('cycle:') || rawText.toLowerCase().includes('[cycle]')
      const cleanText = rawText.replace(/^cycle:\s*/i, '').replace(/\[cycle\]/gi, '').trim()
      if (!cleanText) return

      const hasMultiStatements = cleanText.includes(';') || cleanText.includes('\n')
      const hasBranches = cleanText.includes('|') && (cleanText.includes('->') || cleanText.includes('=>'))

      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const flowColor = resolveChalkColor(color, INK_BOTANICAL)
        const skeletons: any[] = []

        if (hasMultiStatements || hasBranches) {
          // --- HIERARCHICAL BRANCHING TREE FLOWCHART ---
          // Format e.g. "Root -> Branch A | Branch B; Branch A -> Sub 1 | Sub 2"
          const statements = cleanText.split(/;|\n/).map((s) => s.trim()).filter(Boolean)
          const parentChildMap: Map<string, string[]> = new Map()
          const allNodes = new Set<string>()
          const nonRootNodes = new Set<string>()

          statements.forEach((stmt) => {
            const parts = stmt.split(/->|=>/).map((s) => s.trim())
            if (parts.length >= 2) {
              const parent = parts[0]
              const children = parts[1].split('|').map((c) => c.trim()).filter(Boolean)
              allNodes.add(parent)
              if (!parentChildMap.has(parent)) {
                parentChildMap.set(parent, [])
              }
              children.forEach((c) => {
                allNodes.add(c)
                nonRootNodes.add(c)
                parentChildMap.get(parent)!.push(c)
              })
            }
          })

          // Determine root nodes
          let roots = Array.from(allNodes).filter((n) => !nonRootNodes.has(n))
          if (roots.length === 0 && allNodes.size > 0) {
            roots = [Array.from(allNodes)[0]]
          }

          // Build levels
          const levels: string[][] = []
          const visited = new Set<string>()
          let currentLevel = [...roots]

          while (currentLevel.length > 0 && levels.length < 5) {
            levels.push(currentLevel)
            currentLevel.forEach((n) => visited.add(n))
            const nextLevel: string[] = []
            currentLevel.forEach((parent) => {
              const children = parentChildMap.get(parent) || []
              children.forEach((child) => {
                if (!visited.has(child) && !nextLevel.includes(child)) {
                  nextLevel.push(child)
                }
              })
            })
            currentLevel = nextLevel
          }

          // Fallback if some nodes were not placed
          allNodes.forEach((n) => {
            if (!visited.has(n)) {
              if (levels.length > 0) levels[levels.length - 1].push(n)
              else levels.push([n])
            }
          })

          const boxH = 38
          const levelGap = 42
          const estimatedHeight = Math.max(90, levels.length * (boxH + levelGap) + 20)
          await checkAutoPageOverflow(estimatedHeight)

          const startY = getDynamicNextY(16)
          const nodePositions: Map<string, { x: number; y: number; w: number; h: number }> = new Map()
          const canvasWidth = 720
          const startX = 60

          levels.forEach((lvlNodes, lvlIdx) => {
            const rowY = startY + lvlIdx * (boxH + levelGap)
            const count = lvlNodes.length
            const slotWidth = (canvasWidth - startX) / Math.max(1, count)

            lvlNodes.forEach((nodeLabel, nodeIdx) => {
              const w = Math.min(Math.max(110, nodeLabel.length * 8 + 20), slotWidth - 16)
              const boxX = startX + nodeIdx * slotWidth + (slotWidth - w) / 2
              nodePositions.set(nodeLabel, { x: boxX, y: rowY, w, h: boxH })

              // Node box
              skeletons.push(
                {
                  type: 'rectangle',
                  x: boxX,
                  y: rowY,
                  width: w,
                  height: boxH,
                  strokeColor: flowColor,
                  backgroundColor: lvlIdx === 0 ? '#E8F3EC' : '#F4F9F6',
                  fillStyle: 'solid',
                  strokeWidth: lvlIdx === 0 ? 2 : 1.5,
                  roundness: { type: 3 },
                  customData: { isRough: false },
                },
                {
                  type: 'text',
                  x: boxX + 8,
                  y: rowY + 10,
                  text: nodeLabel,
                  fontSize: lvlIdx === 0 ? 13 : 12,
                  fontFamily: 1,
                  strokeColor: INK_PRIMARY,
                  customData: { isRough: false },
                }
              )
            })
          })

          // Draw connecting arrows from parents to children
          parentChildMap.forEach((children, parent) => {
            const pPos = nodePositions.get(parent)
            if (!pPos) return
            children.forEach((child) => {
              const cPos = nodePositions.get(child)
              if (!cPos) return
              const pCenterX = pPos.x + pPos.w / 2
              const pBottomY = pPos.y + pPos.h
              const cCenterX = cPos.x + cPos.w / 2
              const cTopY = cPos.y

              skeletons.push({
                type: 'arrow',
                x: pCenterX,
                y: pBottomY,
                points: [
                  [0, 0],
                  [0, 16],
                  [cCenterX - pCenterX, 16],
                  [cCenterX - pCenterX, cTopY - pBottomY],
                ],
                strokeColor: flowColor,
                strokeWidth: 1.8,
                customData: { isRough: false },
              })
            })
          })

          // If cycle, draw loopback arrow from last level back to root
          if (isCycle && levels.length > 1) {
            const lastLvl = levels[levels.length - 1]
            const firstRoot = roots[0]
            const lastPos = nodePositions.get(lastLvl[lastLvl.length - 1])
            const rootPos = nodePositions.get(firstRoot)
            if (lastPos && rootPos) {
              skeletons.push({
                type: 'arrow',
                x: lastPos.x + lastPos.w / 2,
                y: lastPos.y + lastPos.h,
                points: [
                  [0, 0],
                  [0, 18],
                  [rootPos.x - lastPos.x, 18],
                  [rootPos.x - lastPos.x, -(lastPos.y - rootPos.y)],
                ],
                strokeColor: flowColor,
                strokeWidth: 1.5,
                strokeStyle: 'dashed',
                customData: { isRough: false },
              })
            }
          }

          const elements = convertToExcalidrawElements(skeletons)
          const current = getCurrentElements()
          const merged = [...current, ...elements]
          updateCurrentPageElements(merged, startY + estimatedHeight)
          onNoteRecorded?.(`[Hierarchy Flowchart]: ${statements.join(' | ')}`)
        } else {
          // --- LINEAR PIPELINE FLOWCHART WITH MULTI-ROW WRAPPING ---
          const steps = cleanText.split(/->|=>/).map((s) => s.trim()).filter(Boolean)
          if (steps.length === 0) return

          const maxBoxesPerRow = 3
          const numRows = Math.ceil(steps.length / maxBoxesPerRow)
          const estimatedHeight = Math.max(70, numRows * 76 + 20)
          await checkAutoPageOverflow(estimatedHeight)

          const startY = getDynamicNextY(16)
          nextYRef.current = Math.max(nextYRef.current, startY + 180)
          const rowPositions: { x: number; y: number; w: number; h: number }[] = []

          steps.forEach((st, i) => {
            const rowIdx = Math.floor(i / maxBoxesPerRow)
            const colIdx = i % maxBoxesPerRow
            const w = Math.min(210, Math.max(120, st.length * 8.5 + 24))
            const h = 36
            const boxX = 60 + colIdx * (210 + 28)
            const boxY = startY + rowIdx * (h + 38)

            rowPositions.push({ x: boxX, y: boxY, w, h })

            skeletons.push(
              {
                type: 'rectangle',
                x: boxX,
                y: boxY,
                width: w,
                height: h,
                strokeColor: flowColor,
                backgroundColor: '#F0F6F2',
                fillStyle: 'solid',
                strokeWidth: 1.5,
                roundness: { type: 3 },
                customData: { isRough: false },
              },
              {
                type: 'text',
                x: boxX + 10,
                y: boxY + 10,
                text: st,
                fontSize: 13,
                fontFamily: 1,
                strokeColor: INK_PRIMARY,
                customData: { isRough: false },
              }
            )

            // Connecting arrow to next step
            if (i < steps.length - 1) {
              const nextRowIdx = Math.floor((i + 1) / maxBoxesPerRow)
              if (nextRowIdx === rowIdx) {
                // Horizontal arrow to next box in same row
                skeletons.push({
                  type: 'arrow',
                  x: boxX + w,
                  y: boxY + Math.floor(h / 2),
                  points: [[0, 0], [22, 0]],
                  strokeColor: flowColor,
                  strokeWidth: 2,
                  customData: { isRough: false },
                })
              } else {
                // Row wrap: downward connector arrow to next row
                skeletons.push({
                  type: 'arrow',
                  x: boxX + Math.floor(w / 2),
                  y: boxY + h,
                  points: [
                    [0, 0],
                    [0, 20],
                    [-colIdx * (210 + 28), 20],
                    [-colIdx * (210 + 28), 38],
                  ],
                  strokeColor: flowColor,
                  strokeWidth: 2,
                  customData: { isRough: false },
                })
              }
            }
          })

          // If cycle, draw curved return arrow from last step back to first step
          if (isCycle && rowPositions.length > 1) {
            const lastPos = rowPositions[rowPositions.length - 1]
            const firstPos = rowPositions[0]
            skeletons.push({
              type: 'arrow',
              x: lastPos.x + Math.floor(lastPos.w / 2),
              y: lastPos.y + lastPos.h,
              points: [
                [0, 0],
                [0, 18],
                [firstPos.x - lastPos.x, 18],
                [firstPos.x - lastPos.x, -(lastPos.y - firstPos.y)],
              ],
              strokeColor: flowColor,
              strokeWidth: 1.5,
              strokeStyle: 'dashed',
              customData: { isRough: false },
            })
          }

          const elements = convertToExcalidrawElements(skeletons)
          const current = getCurrentElements()
          const merged = [...current, ...elements]
          updateCurrentPageElements(merged, startY + estimatedHeight)
          onNoteRecorded?.(`[Flow${isCycle ? ' Cycle' : ''}]: ${steps.join(' -> ')}`)
        }
      } catch (err) {
        console.error('drawFlowchart error:', err)
      }
    }

    // Universal Responsive & Auto-Wrapping Whiteboard Table Renderer
    const drawTable = async (tableStr: string) => {
      if (!excalidrawAPI || !tableStr?.trim()) return
      if (shouldSkipDuplicate('draw_table', tableStr)) return
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const totalTableWidth = 720

        // 1. Robust multiformat row parser: handles '||', '\n', and markdown table syntax
        const rawLines = tableStr.includes('||')
          ? tableStr.split('||')
          : tableStr.split(/\r?\n/)

        const rows: string[][] = []
        for (const line of rawLines) {
          const trimmed = line.trim()
          if (!trimmed) continue
          // Skip markdown divider rows like |---|---| or |:---:|
          if (/^\|?[\s\-:]+(\|[\s\-:]+)+\|?$/.test(trimmed)) continue

          // Remove leading and trailing pipe if present
          const cleanLine = trimmed.replace(/^\|/, '').replace(/\|$/, '')
          const cells = cleanLine.split('|').map((c) => c.trim())
          if (cells.some((c) => c.length > 0)) {
            rows.push(cells)
          }
        }

        if (rows.length === 0) return

        const numCols = Math.max(...rows.map((r) => r.length), 1)
        const colWidth = Math.floor(totalTableWidth / numCols)
        // Approximate chars per line based on column width (average character is ~7.5px in Excalidraw font 1)
        const maxCharsPerCellLine = Math.max(12, Math.floor((colWidth - 20) / 7.8))

        // 2. Measure and pre-wrap all cells, computing dynamic row heights
        const wrappedRows: { cellText: string; lines: string[] }[][] = []
        const rowHeights: number[] = []

        rows.forEach((row, rowIdx) => {
          let maxLinesInRow = 1
          const wrappedCells: { cellText: string; lines: string[] }[] = []

          // Pad row to have numCols
          for (let colIdx = 0; colIdx < numCols; colIdx++) {
            const rawCell = row[colIdx] || ''
            const lines = rawCell ? wrapText(rawCell, maxCharsPerCellLine) : ['-']
            if (lines.length > maxLinesInRow) {
              maxLinesInRow = lines.length
            }
            wrappedCells.push({ cellText: rawCell, lines })
          }

          wrappedRows.push(wrappedCells)
          // Line height: 16px per line + 14px vertical padding
          const dynamicHeight = Math.max(34, 14 + maxLinesInRow * 16)
          rowHeights.push(dynamicHeight)
        })

        const totalTableHeight = rowHeights.reduce((a, b) => a + b, 0)
        await checkAutoPageOverflow(totalTableHeight + 24)
        const startY = getDynamicNextY(16)
        nextYRef.current = Math.max(nextYRef.current, startY + totalTableHeight + 24)

        const skeletons: any[] = []
        let currentY = startY

        wrappedRows.forEach((row, rowIdx) => {
          const isHeader = rowIdx === 0
          const currentRowHeight = rowHeights[rowIdx]

          row.forEach((cellData, colIdx) => {
            const x = startX + colIdx * colWidth

            // Cell background box
            skeletons.push({
              type: 'rectangle',
              x,
              y: currentY,
              width: colWidth,
              height: currentRowHeight,
              strokeColor: isHeader ? INK_BOTANICAL : '#D5D2C8',
              backgroundColor: isHeader ? '#EBF2ED' : rowIdx % 2 === 1 ? '#FFFFFF' : '#FAF9F6',
              fillStyle: 'solid',
              strokeWidth: isHeader ? 1.5 : 1,
              customData: { isRough: false },
            })

            // Wrapped cell text
            skeletons.push({
              type: 'text',
              x: x + 10,
              y: currentY + 8,
              text: cellData.lines.join('\n'),
              fontSize: isHeader ? 12 : 11,
              fontFamily: 1,
              strokeColor: isHeader ? INK_PRIMARY : '#2E302D',
              customData: { isRough: false },
            })
          })

          currentY += currentRowHeight
        })

        const elements = convertToExcalidrawElements(skeletons)
        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, currentY + 20)
        onNoteRecorded?.(`[Table]: ${rows[0]?.join(' | ')}`)
      } catch (err) {
        console.error('drawTable error:', err)
      }
    }

    // Universal 2D Geometry & Shapes on Whiteboard (Mathematics, Physics, Engineering)
    const drawGeometry = async (geomStr: string) => {
      if (!excalidrawAPI || !geomStr?.trim()) return
      return drawShape(geomStr)
    }

    // Draw Working Calculations in unified board flow
    const drawRoughWork = async (workText: any, color?: string) => {
      if (!excalidrawAPI) return
      const raw = typeof workText === 'string' ? workText : (workText?.content || workText?.text || workText?.work || (workText ? JSON.stringify(workText) : ''))
      if (!raw?.trim()) return
      const clean = cleanChalkboardTypography(raw.trim())
      await checkAutoPageOverflow(46)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const startY = getDynamicNextY(12)
        const roughColor = resolveChalkColor(color, INK_AMBER)

        const elements = convertToExcalidrawElements([
          {
            id: `work_${Date.now()}_${Math.random().toString(36).substr(2, 4)}`,
            type: 'text',
            x: startX,
            y: startY,
            text: `[Working]: ${clean}`,
            fontSize: 14,
            fontFamily: 1,
            strokeColor: roughColor,
            customData: { isRough: false },
          },
        ])

        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, startY + 36)
        onNoteRecorded?.(`  [Working]: ${clean}`)
      } catch (err) {
        console.error('drawRoughWork error:', err)
      }
    }

    // Clear Working / Scratch calculations
    const clearRough = async () => {
      if (!excalidrawAPI) return
      try {
        const current = getCurrentElements()
        const filtered = current.filter(
          (el: any) => !el.id?.startsWith('work_') && !el.id?.startsWith('rough_')
        )
        updateCurrentPageElements(filtered, nextYRef.current)
      } catch (err) {
        console.error('clearRough error:', err)
      }
    }

    // Live AI Chalk Highlighter: Highlight Word / Sentence on Whiteboard
    const highlightText = async (text: string, color?: string): Promise<boolean> => {
      if (!excalidrawAPI) return false
      const raw = typeof text === 'string' ? text : (text as any)?.text || ''
      if (!raw?.trim()) return false
      const clean = raw.trim()
      const searchTarget = clean.toLowerCase()

      try {
        const elements = getCurrentElements()
        const matchingTextElements = elements.filter((el: any) => {
          if (el.isDeleted || el.type !== 'text') return false
          const elText = (el.text || '').toLowerCase()
          return elText.includes(searchTarget)
        })

        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const markerColor = resolveChalkColor(color, INK_AMBER)

        if (matchingTextElements.length > 0) {
          const newHighlighters: any[] = []
          for (const match of matchingTextElements.slice(0, 3)) {
            const hId = `hl_${Date.now()}_${Math.random().toString(36).substr(2, 4)}`
            const padX = 6
            const padY = 4
            const width = Math.min((match.width || 200) + padX * 2, 780)
            const height = (match.height || 24) + padY * 2

            newHighlighters.push({
              id: hId,
              type: 'rectangle',
              x: match.x - padX,
              y: match.y - padY,
              width: width,
              height: height,
              strokeColor: 'transparent',
              backgroundColor: markerColor === INK_AMBER ? '#FEF3C7' : `${markerColor}33`,
              fillStyle: 'solid',
              strokeWidth: 1,
              strokeStyle: 'solid',
              roughness: 0,
              opacity: 45,
              roundness: { type: 3 },
              customData: { isHighlight: true, targetText: clean },
            })
          }

          if (newHighlighters.length > 0) {
            const excalElements = convertToExcalidrawElements(newHighlighters)
            const updated = [...elements, ...excalElements]
            updateCurrentPageElements(updated, nextYRef.current)

            // Auto-clear highlight after 6 seconds so it behaves as an active optical pointer
            setTimeout(() => {
              try {
                const current = getCurrentElements()
                const filtered = current.filter((el: any) => !el.id?.startsWith('hl_'))
                updateCurrentPageElements(filtered, nextYRef.current)
              } catch (_) {}
            }, 6000)
            return true
          }
        } else {
          // If the term is not yet on the board, draw an elegant key term badge so the student sees the focused term
          await checkAutoPageOverflow(46)
          const startX = 60
          const startY = getDynamicNextY(12)
          const badgeElements = convertToExcalidrawElements([
            {
              id: `hl_badge_${Date.now()}`,
              type: 'rectangle',
              x: startX,
              y: startY,
              width: Math.min(Math.max(clean.length * 10 + 40, 180), 720),
              height: 32,
              strokeColor: markerColor,
              backgroundColor: '#FEF3C7',
              fillStyle: 'solid',
              strokeWidth: 1.5,
              roughness: 1,
              opacity: 90,
              roundness: { type: 3 },
              customData: { isHighlight: true },
            },
            {
              id: `hl_badgetxt_${Date.now()}`,
              type: 'text',
              x: startX + 14,
              y: startY + 7,
              text: `* Focus: ${clean}`,
              fontSize: 14,
              fontFamily: 1,
              strokeColor: markerColor === INK_AMBER ? '#92400E' : markerColor,
              customData: { isHighlight: true },
            },
          ])
          const updated = [...elements, ...badgeElements]
          updateCurrentPageElements(updated, startY + 40)
          return true
        }
      } catch (err) {
        console.warn('[GreenChalkboard] Error highlighting text:', err)
      }
      return false
    }

    // Clear Notes on current page
    const clearNotes = async () => {
      if (!excalidrawAPI) return
      try {
        const current = getCurrentElements()
        const filtered = current.filter(
          (el: any) => el.customData?.isHeader === true
        )
        updateCurrentPageElements(filtered, 140)
      } catch (err) {
        console.error('clearNotes error:', err)
      }
    }

    // Reset entire board to clean state (clears localStorage and resets to clean Page 1)
    const resetBoard = async () => {
      if (!excalidrawAPI) return
      try {
        if (typeof window !== 'undefined' && storageKey) {
          localStorage.removeItem(storageKey)
          localStorage.removeItem(`${storageKey}_files`)
        }
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const firstConcept = keyConcepts && keyConcepts[0] ? keyConcepts[0] : undefined
        const initialSkeleton = createHeaderSkeleton(1, firstConcept)
        const initialElements = convertToExcalidrawElements(initialSkeleton)
        const freshPages: WhiteboardPage[] = [
          {
            id: 1,
            elements: initialElements,
            nextY: firstConcept ? 200 : 140,
            roughY: 140,
          },
        ]
        pagesRef.current = freshPages
        setPages(freshPages)
        currentPageIndexRef.current = 0
        setCurrentPageIndex(0)
        boardElementsRef.current = initialElements
        nextYRef.current = firstConcept ? 200 : 140
        roughYRef.current = 140
        executedTextHistoryRef.current.clear()
        lastExecutedActionTimeRef.current.clear()
        activeQuestionRef.current = null

        excalidrawAPI.updateScene({
          elements: initialElements,
          appState: {
            viewBackgroundColor: 'transparent',
            currentItemStrokeColor: INK_PRIMARY,
            currentItemFontFamily: 1,
            currentItemRoughness: 0,
            gridModeEnabled: true,
            zoom: { value: boardZoomRef.current },
            scrollX: 0,
            scrollY: 0,
          },
        })
      } catch (err) {
        console.error('resetBoard error:', err)
      }
    }

    // Clear entire board (resets to Page 1 clean state)
    const clearBoard = async () => {
      await resetBoard()
    }

    // Rewrite notes cleanly on board
    const rewriteNotes = async (newNotes: string) => {
      if (!excalidrawAPI || !newNotes?.trim()) return
      await clearNotes()
      const lines = newNotes.split('\n').filter((l) => l.trim().length > 0)
      for (const line of lines) {
        const t = line.trim()
        if (t.startsWith('###')) {
          await drawTitle(t.replace(/^###\s*/, ''))
        } else if (t.startsWith('•') || t.startsWith('*') || t.startsWith('-')) {
          await drawNote(t.replace(/^[•*-]\s*/, ''))
        } else if (t.startsWith('->')) {
          await drawStep(t.replace(/^->\s*/, ''))
        } else if (t.startsWith('**[') || t.toLowerCase().includes('formula')) {
          await drawHighlightBox(t)
        } else {
          await drawText(t)
        }
      }
    }

    // -------------------------------------------------------------------------
    // Safe math evaluator for dynamic Cartesian formulas (y = f(x)) is imported from @/lib/mathEvaluator
    // -------------------------------------------------------------------------

    // Dynamic Mathematical & Scientific Graph Plotter (Cartesian Coordinates, Arbitrary Formulas, Custom Domain/Range, Discrete Points)
    const drawGraph = async (query = 'linear') => {
      if (!excalidrawAPI) return
      const q = (query || '').trim()
      if (q && !isLegitimateGraphTopic(q, subject || '')) {
        console.log(`[GreenChalkboard] Denied Cartesian graph for non-mathematical query "${q}" in subject "${subject}". Routing to SVG diagram.`)
        await drawSvgDiagram(q, '', 'Visual conceptual diagram')
        return
      }
      await checkAutoPageOverflow(230)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 75
        const startY = getDynamicNextY(18)
        nextYRef.current = Math.max(nextYRef.current, startY + 240 + 20)
        const q = (query || '').trim()
        const lowerQ = q.toLowerCase()

        // 1. Parse parameters & options from query
        let formula = ''
        let domain: [number, number] = [-5, 5]
        let range: [number, number] | null = null
        let titleText = 'Cartesian Graph'
        let yLabel = 'Y'
        let xLabel = 'X'
        let calloutText = ''
        const discretePoints: [number, number][] = []
        let hasExplicitDomain = false

        // Extract pipe or comma parameters: domain=[-5,5], points=[(1,2),(3,4)], etc.
        const pipeParts = q.split('|').map((s) => s.trim())
        const mainPart = pipeParts[0] || 'linear'

        pipeParts.forEach((part) => {
          const l = part.toLowerCase()
          if (l.includes('domain=') || l.includes('x=[')) {
            const m = part.match(/\[\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\]/)
            if (m) {
              domain = [parseFloat(m[1]), parseFloat(m[2])]
              hasExplicitDomain = true
            }
          } else if (l.includes('range=') || l.includes('y=[')) {
            const m = part.match(/\[\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\]/)
            if (m) range = [parseFloat(m[1]), parseFloat(m[2])]
          } else if (l.includes('points=')) {
            const matches = part.matchAll(/\(\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\)/g)
            for (const match of matches) {
              discretePoints.push([parseFloat(match[1]), parseFloat(match[2])])
            }
          } else if (l.startsWith('title=')) {
            titleText = part.split('=')[1]?.trim() || titleText
          } else if (l.startsWith('xlabel=')) {
            xLabel = part.split('=')[1]?.trim() || xLabel
          } else if (l.startsWith('ylabel=')) {
            yLabel = part.split('=')[1]?.trim() || yLabel
          } else if (l.startsWith('callout=')) {
            calloutText = part.split('=')[1]?.trim() || calloutText
          } else if (l.startsWith('formula=')) {
            formula = part.split('=')[1]?.trim() || formula
          }
        })

        // Check if mainPart is a mathematical formula or scientific preset
        const isParamDirective = /^(points|domain|range|title|xlabel|ylabel|callout|formula)=/i.test(mainPart)
        const isMathFormula =
          !isParamDirective &&
          (mainPart.includes('=') ||
            mainPart.includes('x') ||
            mainPart.includes('sin') ||
            mainPart.includes('cos') ||
            mainPart.includes('tan') ||
            mainPart.includes('exp') ||
            mainPart.includes('log') ||
            mainPart.includes('ln') ||
            mainPart.includes('^'))

        if (formula) {
          if (titleText === 'Cartesian Graph') titleText = `Function Plot: ${formula}`
        } else if (isMathFormula && !mainPart.includes('v-t') && !mainPart.includes('velocity')) {
          formula = mainPart
          titleText = titleText === 'Cartesian Graph' ? `Function Plot: ${mainPart}` : titleText
        } else if (lowerQ.includes('velocity') || lowerQ.includes('speed') || lowerQ.includes('v-t') || lowerQ.includes('vt')) {
          titleText = 'Velocity-Time Graph (v-t): Slope = Acceleration (a)'
          yLabel = 'v (m/s)'
          xLabel = 't (s)'
          calloutText = 'Slope = a = (v - u)/t | Area = Displacement (s)'
          if (!hasExplicitDomain) domain = [0, 10]
          formula = '1.5x + 2' // Linear acceleration exemplar
        } else if (lowerQ.includes('distance') || lowerQ.includes('displacement') || lowerQ.includes('s-t') || lowerQ.includes('st')) {
          titleText = 'Distance-Time Graph (s-t): Slope = Speed (v)'
          yLabel = 's (m)'
          xLabel = 't (s)'
          calloutText = 'Slope = Speed v = Delta_s / Delta_t'
          if (!hasExplicitDomain) domain = [0, 10]
          formula = '2.5x'
        } else if (lowerQ.includes('ohm') || lowerQ.includes('v-i') || lowerQ.includes('vi') || lowerQ.includes('resistan')) {
          titleText = "Ohm's Law V vs I Characteristic (Slope = Resistance R)"
          yLabel = 'V (Volts)'
          xLabel = 'I (Amperes)'
          calloutText = 'Slope = Delta_V / Delta_I = Resistance R'
          if (!hasExplicitDomain) domain = [0, 5]
          formula = '4x' // R = 4 Ohm exemplar
        } else if (lowerQ.includes('boyle') || lowerQ.includes('p-v') || lowerQ.includes('pv') || lowerQ.includes('isotherm')) {
          titleText = "Boyle's Law Isothermal Curve: P proportional to 1/V"
          yLabel = 'P (Pa)'
          xLabel = 'V (m^3)'
          calloutText = 'P * V = Constant (Isothermal)'
          if (!hasExplicitDomain) domain = [1, 10]
          formula = '20 / x'
        } else if (lowerQ.includes('wave') || lowerQ.includes('sine') || lowerQ.includes('harmonic')) {
          titleText = 'Transverse Harmonic Wave: y = A * sin(kx)'
          yLabel = 'y (m)'
          xLabel = 'x (m)'
          calloutText = 'Wavelength Lambda | Amplitude A'
          if (!hasExplicitDomain) domain = [-3.14, 3.14]
          formula = '2 * sin(x)'
        } else if (lowerQ.includes('decay') || lowerQ.includes('radio') || lowerQ.includes('exponen')) {
          titleText = 'Exponential Decay: N = N0 * e^(-lambda * t)'
          yLabel = 'N'
          xLabel = 't'
          calloutText = 'Half-life t_1/2 = ln(2) / lambda'
          if (!hasExplicitDomain) domain = [0, 5]
          formula = '10 * e^(-0.6x)'
        } else if (lowerQ.includes('quad') || lowerQ.includes('para')) {
          titleText = 'Quadratic Parabola: y = ax^2 + bx + c'
          if (!hasExplicitDomain) domain = [-4, 4]
          formula = 'x^2 - 4'
          calloutText = 'Vertex & Axis of Symmetry'
        } else if (discretePoints.length > 0) {
          if (titleText === 'Cartesian Graph') titleText = 'Discrete Points Plot'
        } else {
          // Standard linear default
          titleText = 'Linear Graph: y = mx + c'
          if (!hasExplicitDomain) domain = [-5, 5]
          formula = 'x + 1'
          calloutText = 'Slope m = Delta_y / Delta_x'
        }

        // Auto-fit domain if discrete points given without explicit domain
        if (!hasExplicitDomain && discretePoints.length > 0 && !formula) {
          const ptXs = discretePoints.map((p) => p[0])
          const minX = Math.min(...ptXs)
          const maxX = Math.max(...ptXs)
          const pad = (maxX - minX) * 0.2 || 1
          domain = [Math.floor(minX - pad), Math.ceil(maxX + pad)]
        }

        // 2. Evaluate formula over domain to compute coordinates
        const graphWidth = 240
        const graphHeight = 130
        const numSamples = 35
        const [xMin, xMax] = domain
        const xStep = (xMax - xMin) / (numSamples - 1)

        const sampled: { x: number; y: number }[] = []
        if (formula) {
          for (let i = 0; i < numSamples; i++) {
            const xVal = xMin + i * xStep
            const yVal = evaluateMathExpression(formula, xVal)
            if (yVal !== null && !isNaN(yVal) && isFinite(yVal)) {
              sampled.push({ x: xVal, y: yVal })
            }
          }
        }

        // Add discrete points if any
        discretePoints.forEach(([px, py]) => {
          sampled.push({ x: px, y: py })
        })

        // Sort sampled points strictly by x to ensure monotonic plotting without zig-zags
        sampled.sort((a, b) => a.x - b.x)

        // Determine range [yMin, yMax]
        let [yMin, yMax] = range || [-10, 10]
        if (!range && sampled.length > 0) {
          const yVals = sampled.map((p) => p.y)
          const minY = Math.min(...yVals)
          const maxY = Math.max(...yVals)
          const padding = (maxY - minY) * 0.15 || 2
          yMin = Math.floor(minY - padding)
          yMax = Math.ceil(maxY + padding)
          if (yMin === yMax) {
            yMin -= 5
            yMax += 5
          }
        }

        // Coordinate projection helper: converts mathematical (x, y) to pixel offset relative to origin box
        const toPixels = (x: number, y: number): [number, number] => {
          const clampedX = Math.max(xMin, Math.min(xMax, x))
          const clampedY = Math.max(yMin, Math.min(yMax, y))
          const px = ((clampedX - xMin) / (xMax - xMin)) * graphWidth
          const py = -((clampedY - yMin) / (yMax - yMin)) * graphHeight
          return [px, py]
        }

        // Calculate origin position on screen
        const originX = startX + 35
        const originY = startY + 155
        const [axisZeroX, axisZeroY] = toPixels(
          xMin <= 0 && xMax >= 0 ? 0 : xMin,
          yMin <= 0 && yMax >= 0 ? 0 : yMin
        )

        // Curve point offsets relative to (originX, originY)
        const curvePoints: [number, number][] = sampled
          .filter((p) => p.y >= yMin && p.y <= yMax)
          .map((p) => toPixels(p.x, p.y))

        const elementsSkeleton: any[] = [
          // Title Banner
          {
            type: 'text',
            x: startX,
            y: startY,
            text: titleText,
            fontSize: 16,
            fontFamily: 1,
            strokeColor: INK_PRIMARY,
            customData: { isRough: false },
          },
          // Cartesian Y-Axis
          {
            type: 'arrow',
            x: originX + axisZeroX,
            y: originY,
            points: [
              [0, 10],
              [0, -graphHeight - 20],
            ],
            strokeColor: INK_PRIMARY,
            strokeWidth: 2,
            customData: { isRough: false },
          },
          // Cartesian X-Axis
          {
            type: 'arrow',
            x: originX,
            y: originY + axisZeroY,
            points: [
              [-10, 0],
              [graphWidth + 25, 0],
            ],
            strokeColor: INK_PRIMARY,
            strokeWidth: 2,
            customData: { isRough: false },
          },
          // Axis Labels
          {
            type: 'text',
            x: originX + axisZeroX - 12,
            y: originY - graphHeight - 32,
            text: yLabel,
            fontSize: 13,
            fontFamily: 1,
            strokeColor: INK_BOTANICAL,
            customData: { isRough: false },
          },
          {
            type: 'text',
            x: originX + graphWidth + 30,
            y: originY + axisZeroY - 6,
            text: xLabel,
            fontSize: 13,
            fontFamily: 1,
            strokeColor: INK_BOTANICAL,
            customData: { isRough: false },
          },
        ]

        // Coordinate Origin Marker "0" (only when origin [0, 0] is within viewable domain & range)
        const originInView = xMin <= 0 && xMax >= 0 && yMin <= 0 && yMax >= 0
        if (originInView) {
          elementsSkeleton.push({
            type: 'text',
            x: originX + axisZeroX - 18,
            y: originY + axisZeroY + 6,
            text: '0',
            fontSize: 11,
            fontFamily: 1,
            strokeColor: INK_MUTED,
            customData: { isRough: false },
          })
        }

        // Add domain ticks on X-axis (xmin, xmax)
        const [xMinPx] = toPixels(xMin, yMin <= 0 && yMax >= 0 ? 0 : yMin)
        const [xMaxPx] = toPixels(xMax, yMin <= 0 && yMax >= 0 ? 0 : yMin)
        if (!originInView || Math.abs(xMin) > 0.001) {
          elementsSkeleton.push({
            type: 'text',
            x: originX + xMinPx - 6,
            y: originY + axisZeroY + 6,
            text: `${xMin}`,
            fontSize: 10,
            fontFamily: 1,
            strokeColor: INK_MUTED,
            customData: { isRough: false },
          })
        }
        if (!originInView || Math.abs(xMax) > 0.001) {
          elementsSkeleton.push({
            type: 'text',
            x: originX + xMaxPx - 6,
            y: originY + axisZeroY + 6,
            text: `${xMax}`,
            fontSize: 10,
            fontFamily: 1,
            strokeColor: INK_MUTED,
            customData: { isRough: false },
          })
        }

        // Plotted Function Curve / Line (only if curvePoints has >= 2 points)
        if (curvePoints.length > 1) {
          elementsSkeleton.push({
            type: 'line',
            x: originX,
            y: originY,
            points: curvePoints,
            strokeColor: INK_CORAL,
            strokeWidth: 2.5,
            customData: { isRough: false },
          })
        }

        // Add Discrete Points Markers if provided
        discretePoints.forEach(([dx, dy]) => {
          const [ptX, ptY] = toPixels(dx, dy)
          elementsSkeleton.push(
            {
              type: 'ellipse',
              x: originX + ptX - 4,
              y: originY + ptY - 4,
              width: 8,
              height: 8,
              strokeColor: INK_CORAL,
              backgroundColor: INK_CORAL,
              fillStyle: 'solid',
              customData: { isRough: false },
            },
            {
              type: 'text',
              x: originX + ptX + 6,
              y: originY + ptY - 14,
              text: `(${dx}, ${dy})`,
              fontSize: 11,
              fontFamily: 1,
              strokeColor: INK_PRIMARY,
              customData: { isRough: false },
            }
          )
        })

        // Callout Note / Principle Badge
        if (calloutText) {
          elementsSkeleton.push({
            type: 'text',
            x: originX + graphWidth + 20,
            y: originY - graphHeight / 2 - 15,
            text: calloutText,
            fontSize: 13,
            fontFamily: 1,
            strokeColor: INK_BOTANICAL,
            customData: { isRough: false },
          })
        }

        const elements = convertToExcalidrawElements(elementsSkeleton)
        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, originY + 35)
        onNoteRecorded?.(`**Graph**: ${titleText} [${xLabel} vs ${yLabel}]`)
      } catch (err) {
        console.error('drawGraph error:', err)
      }
    }

    // Step-by-Step Problem Solving on Whiteboard (Given -> Formula -> Substitution -> Calculation in Rough -> Boxed Answer)
    const drawNumericalSolution = async (solution: {
      problem?: string
      given?: string
      formula?: string
      substitution?: string
      calculation?: string
      answer: string
      unit?: string
    }) => {
      if (!excalidrawAPI) return
      await checkAutoPageOverflow(170)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const startY = getDynamicNextY(16)
        const elements: any[] = []

        let curY = startY

        // 1. Problem / Numerical Statement
        if (solution.problem) {
          const problemText = cleanChalkboardTypography(solution.problem)
          elements.push({
            type: 'text',
            x: startX,
            y: curY,
            text: `Problem: ${problemText}`,
            fontSize: 15,
            fontFamily: 1,
            strokeColor: INK_PRIMARY,
            customData: { isRough: false },
          })
          curY += 28
        }

        // 2. Given Parameters
        if (solution.given) {
          const givenText = cleanChalkboardTypography(solution.given)
          elements.push({
            type: 'text',
            x: startX + 10,
            y: curY,
            text: `• Given: ${givenText}`,
            fontSize: 14,
            fontFamily: 1,
            strokeColor: INK_SECONDARY,
            customData: { isRough: false },
          })
          curY += 24
        }

        // 3. Formula / Governing Law
        if (solution.formula) {
          const formulaText = cleanChalkboardTypography(solution.formula)
          elements.push({
            type: 'text',
            x: startX + 10,
            y: curY,
            text: `Formula: ${formulaText}`,
            fontSize: 15,
            fontFamily: 1,
            strokeColor: INK_BOTANICAL,
            customData: { isRough: false },
          })
          curY += 26
        }

        // 4. Substitution Step
        if (solution.substitution) {
          const subText = cleanChalkboardTypography(solution.substitution)
          elements.push({
            type: 'text',
            x: startX + 10,
            y: curY,
            text: `-> Substitution: ${subText}`,
            fontSize: 14,
            fontFamily: 1,
            strokeColor: INK_SECONDARY,
            customData: { isRough: false },
          })
          curY += 30
        }

        // 5. Boxed Final Answer with SI Units
        const cleanAns = cleanChalkboardTypography(solution.answer)
        const cleanUnit = solution.unit ? cleanChalkboardTypography(solution.unit) : ''
        const ansText = `Answer: ${cleanAns}${cleanUnit ? ' ' + cleanUnit : ''}`
        const boxWidth = Math.min(Math.max(ansText.length * 11 + 32, 240), 400)
        elements.push(
          {
            type: 'rectangle',
            x: startX + 10,
            y: curY,
            width: boxWidth,
            height: 40,
            strokeColor: INK_CORAL,
            backgroundColor: INK_CORAL_SOFT,
            fillStyle: 'solid',
            strokeWidth: 2,
            roundness: { type: 3 },
            customData: { isRough: false },
          },
          {
            type: 'text',
            x: startX + 22,
            y: curY + 10,
            text: ansText,
            fontSize: 15,
            fontFamily: 1,
            strokeColor: INK_PRIMARY,
            customData: { isRough: false },
          }
        )
        curY += 50

        const current = getCurrentElements()
        const converted = convertToExcalidrawElements(elements)
        const merged = [...current, ...converted]
        updateCurrentPageElements(merged, curY + 15)

        // 6. Scratchpad / Calculation in Right Rough Margin
        if (solution.calculation) {
          await drawRoughWork(`Calculation:\n${cleanChalkboardTypography(solution.calculation)}`)
        }

        onNoteRecorded?.(`**Solved Numerical**: ${solution.problem || solution.formula || ansText}`)
      } catch (err) {
        console.error('drawNumericalSolution error:', err)
      }
    }

    // Draw Chalkboard Skeleton Loading Box while SVG diagram is generating
    const drawDiagramSkeleton = async (title: string) => {
      if (!excalidrawAPI) return
      const cleanTitle = (title || '').trim() || 'Visualizing Illustration'
      const normTitle = cleanTitle.toLowerCase().replace(/[^a-z0-9]/g, '')

      const current = getCurrentElements()
      // Avoid duplicate skeletons for the same concept/diagram
      const alreadyHasSkeleton = current.some(
        (el: any) =>
          el.customData?.isDiagramSkeleton &&
          (el.customData?.normTitle === normTitle || !normTitle)
      )
      if (alreadyHasSkeleton) return

      await checkAutoPageOverflow(270)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const startY = getDynamicNextY(20)
        const cardWidth = 532
        const cardHeight = 250
        const innerW = 496
        const innerH = 150

        const skeletonElements = convertToExcalidrawElements([
          // 1. Outer container box with dashed chalk outline and subtle scholastic tint
          {
            type: 'rectangle',
            x: startX,
            y: startY,
            width: cardWidth,
            height: cardHeight,
            strokeColor: '#52715D',
            backgroundColor: '#F8FAF9',
            fillStyle: 'solid',
            strokeWidth: 1.5,
            strokeStyle: 'dashed',
            roundness: { type: 3 },
            customData: { isRough: false, isDiagramSkeleton: true, normTitle, skeletonTitle: cleanTitle },
          },
          // 2. Header title
          {
            type: 'text',
            x: startX + 18,
            y: startY + 14,
            text: `Visualizing: ${cleanTitle}...`,
            fontSize: 14,
            fontFamily: 1,
            strokeColor: INK_BOTANICAL,
            customData: { isRough: false, isDiagramSkeleton: true, normTitle, skeletonTitle: cleanTitle },
          },
          // 3. Inner illustration placeholder frame with dashed boundary
          {
            type: 'rectangle',
            x: startX + 18,
            y: startY + 44,
            width: innerW,
            height: innerH,
            strokeColor: '#CBD5E1',
            backgroundColor: '#F1F5F9',
            fillStyle: 'solid',
            strokeWidth: 1,
            strokeStyle: 'dashed',
            roundness: { type: 2 },
            customData: { isRough: false, isDiagramSkeleton: true, normTitle, skeletonTitle: cleanTitle },
          },
          // 4. Scholastic status / shimmer label centered in the inner frame
          {
            type: 'text',
            x: startX + 84,
            y: startY + 105,
            text: `Synthesizing scientific vector illustration...`,
            fontSize: 13,
            fontFamily: 1,
            strokeColor: INK_MUTED,
            customData: { isRough: false, isDiagramSkeleton: true, normTitle, skeletonTitle: cleanTitle },
          },
          // 5. Educational sub-caption placeholder
          {
            type: 'text',
            x: startX + 18,
            y: startY + 212,
            text: `The precision illustration will appear on this board space automatically.`,
            fontSize: 11,
            fontFamily: 1,
            strokeColor: INK_SECONDARY,
            customData: { isRough: false, isDiagramSkeleton: true, normTitle, skeletonTitle: cleanTitle },
          },
        ])

        const merged = [...current, ...skeletonElements]
        updateCurrentPageElements(merged, startY + cardHeight + 20)
      } catch (err) {
        console.error('drawDiagramSkeleton error:', err)
      }
    }

    // Clear any active skeleton loading boxes
    const clearDiagramSkeleton = async (title?: string) => {
      if (!excalidrawAPI) return
      try {
        const current = getCurrentElements()
        const normTitle = title ? title.toLowerCase().replace(/[^a-z0-9]/g, '') : null
        const filtered = current.filter((el: any) => {
          if (!el.customData?.isDiagramSkeleton) return true
          if (!normTitle) return false
          const sTitle = el.customData?.normTitle || ''
          if (sTitle === normTitle) return false
          if (sTitle && (normTitle.includes(sTitle) || sTitle.includes(normTitle))) return false
          return true
        })
        if (filtered.length !== current.length) {
          updateCurrentPageElements(filtered, nextYRef.current)
        }
      } catch (err) {
        console.error('clearDiagramSkeleton error:', err)
      }
    }

    // Draw Dynamic Vector SVG Diagram Card directly on Whiteboard
    const drawSvgDiagram = async (title: string, svgMarkup: string, caption = '', forceUpdate = false) => {
      if (!excalidrawAPI || (!title?.trim() && !svgMarkup?.trim())) return
      const currentEls = getCurrentElements()
      const hasAnySkeleton = currentEls.some((el: any) => el.customData?.isDiagramSkeleton)
      if (hasAnySkeleton) {
        forceUpdate = true
      }
      if (!forceUpdate && shouldSkipDuplicate('draw_svg_diagram', `${title}:${caption || ''}`)) return

      await checkAutoPageOverflow(260)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const startY = getDynamicNextY(20)
        nextYRef.current = Math.max(nextYRef.current, startY + 280 + 24)

        // Clean markdown code blocks, script tags, and whitespace
        let cleanSvg = (svgMarkup || '').trim().replace(/^```(?:xml|svg|html)?\s*/i, '').replace(/\s*```$/i, '').trim()
        cleanSvg = cleanSvg.replace(/<script[\s\S]*?<\/script>/gi, '')

        let resolvedTitle = (title || '').trim() || 'Scientific Diagram'
        let resolvedCaption = caption

        // If SVG markup is missing or does not contain an <svg tag, skip rendering fake/irrelevant diagrams
        if (!cleanSvg.toLowerCase().includes('<svg')) {
          console.warn(`[GreenChalkboard] drawSvgDiagram called without valid SVG for "${resolvedTitle}". Skipping diagram render.`)
          return
        }

        // Sanitize SVG via DOMParser to catch malformed XML from Gemini Live output
        const sanitized = sanitizeSvg(cleanSvg)
        if (sanitized) {
          cleanSvg = sanitized
        } else {
          console.warn(`[GreenChalkboard] SVG for "${resolvedTitle}" is malformed. Skipping diagram render.`)
          return
        }

        // Determine dimensions from viewBox or width/height
        let svgWidth = 500
        let svgHeight = 260
        const viewBoxMatch = cleanSvg.match(/viewBox\s*=\s*["']([^"']+)["']/i)
        if (viewBoxMatch) {
          const parts = viewBoxMatch[1].trim().split(/[\s,]+/).map(Number)
          if (parts.length === 4 && parts[2] > 0 && parts[3] > 0) {
            const vbW = parts[2]
            const vbH = parts[3]
            const aspect = vbH / vbW
            svgWidth = Math.min(520, Math.max(300, vbW))
            svgHeight = Math.round(svgWidth * aspect)
          }
        } else {
          const wMatch = cleanSvg.match(/width\s*=\s*["']?(\d+)/i)
          const hMatch = cleanSvg.match(/height\s*=\s*["']?(\d+)/i)
          if (wMatch && hMatch) {
            const parsedW = parseInt(wMatch[1], 10)
            const parsedH = parseInt(hMatch[1], 10)
            if (parsedW > 0 && parsedH > 0) {
              const aspect = parsedH / parsedW
              svgWidth = Math.min(520, Math.max(300, parsedW))
              svgHeight = Math.round(svgWidth * aspect)
            }
          }
        }

        // Clamp height for whiteboard balance
        if (svgHeight > 340) {
          const ratio = 340 / svgHeight
          svgHeight = 340
          svgWidth = Math.round(svgWidth * ratio)
        }
        if (svgHeight < 140) svgHeight = 160

        const fileId = `svg_${Date.now()}_${Math.random().toString(36).substring(2, 8)}` as any
        const dataURL = svgToBase64DataUrl(cleanSvg)
        let resolvedDataURL = sanitizeBase64DataUrl(dataURL) || dataURL
        let fileMimeType = 'image/svg+xml'

        // Pre-validate SVG to prevent Excalidraw internal console.error("Invalid SVG")
        const svgValidation = validateSvgForExcalidraw(resolvedDataURL)
        if (!svgValidation.isValid) {
          try {
            const pngDataUrl = await rasterizeSvgToPng(cleanSvg, svgWidth, svgHeight)
            const cleanPng = sanitizeBase64DataUrl(pngDataUrl)
            if (cleanPng) {
              resolvedDataURL = cleanPng
              fileMimeType = 'image/png'
            }
          } catch (rasterErr) {
            console.warn('[drawSvgDiagram] SVG rasterization fallback error:', rasterErr)
          }
        }

        let fileObj: any = {
          id: fileId,
          dataURL: resolvedDataURL,
          mimeType: fileMimeType,
          created: Date.now(),
        }

        if (excalidrawAPI?.addFiles) {
          try {
            if (isValidBase64DataUrl(fileObj.dataURL)) {
              excalidrawAPI.addFiles([fileObj])
            }
          } catch (svgErr) {
            console.warn('[drawSvgDiagram] excalidrawAPI.addFiles warning:', svgErr)
          }
        }

        // Persist SVG file to localStorage so it survives page reload
        if (typeof window !== 'undefined' && storageKey) {
          try {
            const rawFiles = localStorage.getItem(`${storageKey}_files`)
            const existingFiles = rawFiles ? JSON.parse(rawFiles) : {}
            existingFiles[fileId] = fileObj
            safeSaveWhiteboardStorage(`${storageKey}_files`, existingFiles, true)
          } catch (e) {
            console.warn('Error saving whiteboard file to localStorage:', e)
          }
        }

        const cardWidth = Math.max(svgWidth + 32, 440)
        // Wraps SVG captions at base column width: wrapText(caption.trim(), 55) adapted via cols(55)
        const captionLines = caption?.trim()
          ? wrapText(caption.trim(), cols(55))
          : resolvedCaption?.trim()
          ? wrapText(resolvedCaption.trim(), cols(55))
          : []
        const captionHeight = captionLines.length * 18
        const cardHeight = svgHeight + 56 + (captionLines.length > 0 ? captionHeight + 12 : 0) + 16

        const normTitle = resolvedTitle.toLowerCase().replace(/[^a-z0-9]/g, '')
        const rawNormTitle = (title || '').toLowerCase().replace(/[^a-z0-9]/g, '')

        let skeletonStartX: number | null = null
        let skeletonStartY: number | null = null

        const current = getCurrentElements()

        // 1. Check for matching skeleton on current page
        const isSkeletonMatch = (el: any) => {
          if (!el.customData?.isDiagramSkeleton) return false
          const sTitle = el.customData?.normTitle || ''
          if (!sTitle) return true
          if (sTitle === normTitle || sTitle === rawNormTitle) return true
          if (normTitle && (normTitle.includes(sTitle) || sTitle.includes(normTitle))) return true
          if (rawNormTitle && (rawNormTitle.includes(sTitle) || sTitle.includes(rawNormTitle))) return true
          return false
        }

        const matchingSkeletons = current.filter(isSkeletonMatch)
        const hasMatchingSkeleton = matchingSkeletons.length > 0 || current.some((el: any) => el.customData?.isDiagramSkeleton)

        // 2. Or if forceUpdate, check for existing SVG diagram card for this title
        const isExistingSvgMatch = (el: any) => {
          if (!el.customData?.isSvgCard) return false
          const cTitle = el.customData?.normTitle || ''
          if (!cTitle) return false
          if (cTitle === normTitle || cTitle === rawNormTitle) return true
          if (normTitle && (normTitle.includes(cTitle) || cTitle.includes(normTitle))) return true
          if (rawNormTitle && (rawNormTitle.includes(cTitle) || cTitle.includes(rawNormTitle))) return true
          return false
        }
        const hasExistingSvgCard = forceUpdate && current.some(isExistingSvgMatch)

        let filteredElements = current

        if (hasMatchingSkeleton) {
          const targetSkeletons = matchingSkeletons.length > 0
            ? matchingSkeletons
            : current.filter((el: any) => el.customData?.isDiagramSkeleton)
          const firstSkel = targetSkeletons[0]
          if (firstSkel) {
            skeletonStartX = firstSkel.x
            skeletonStartY = firstSkel.y
          }
          filteredElements = current.filter((el: any) => !targetSkeletons.includes(el))
        } else if (hasExistingSvgCard) {
          const matchingCards = current.filter(isExistingSvgMatch)
          const firstCard = matchingCards[0]
          if (firstCard) {
            skeletonStartX = firstCard.x
            skeletonStartY = firstCard.y
          }
          filteredElements = current.filter((el: any) => !matchingCards.includes(el))
        }

        const targetStartX = skeletonStartX !== null ? skeletonStartX : startX
        const targetStartY = skeletonStartY !== null ? skeletonStartY : startY

        const skeletons: any[] = [
          // Background card container
          {
            type: 'rectangle',
            x: targetStartX,
            y: targetStartY,
            width: cardWidth,
            height: cardHeight,
            strokeColor: '#CBD5E1',
            backgroundColor: '#FFFFFF',
            fillStyle: 'solid',
            strokeWidth: 1.5,
            roundness: { type: 3 },
            customData: { isRough: false, isSvgCard: true, normTitle, diagramTitle: resolvedTitle },
          },
          // Header / Title
          {
            type: 'text',
            x: targetStartX + 16,
            y: targetStartY + 12,
            text: `[DIAGRAM]: ${resolvedTitle.toUpperCase()}`,
            fontSize: 14,
            fontFamily: 1,
            strokeColor: '#0F172A',
            customData: { isRough: false, isSvgCard: true, normTitle, diagramTitle: resolvedTitle },
          },
          // SVG Image Element
          {
            type: 'image',
            x: targetStartX + 16,
            y: targetStartY + 44,
            width: svgWidth,
            height: svgHeight,
            fileId,
            status: 'saved',
            customData: { isRough: false, isSvgCard: true, normTitle, diagramTitle: resolvedTitle },
          },
        ]

        if (captionLines.length > 0) {
          skeletons.push({
            type: 'text',
            x: targetStartX + 16,
            y: targetStartY + 44 + svgHeight + 12,
            text: captionLines.join('\n'),
            fontSize: 12,
            fontFamily: 1,
            strokeColor: INK_SECONDARY,
            customData: { isRough: false, isSvgCard: true, normTitle, diagramTitle: resolvedTitle },
          })
        }

        const elements = convertToExcalidrawElements(skeletons)
        const merged = [...filteredElements, ...elements]
        const nextYTarget = Math.max(nextYRef.current, targetStartY + cardHeight + 20)
        updateCurrentPageElements(merged, nextYTarget)
        onNoteRecorded?.(`[Diagram]: ${title}${caption ? ` - ${caption}` : ''}`)
      } catch (err) {
        console.error('drawSvgDiagram error:', err)
      }
    }

    // Draw Educational Image Card directly on Whiteboard
    const drawImage = async (urlOrDataUrl: string, title = 'Educational Image', caption = '') => {
      if (!excalidrawAPI || !urlOrDataUrl?.trim()) return
      const cleanUrl = urlOrDataUrl.trim()
      const resolvedTitle = (title || '').trim() || 'Educational Image'
      const resolvedCaption = (caption || '').trim()

      if (shouldSkipDuplicate('draw_image', `${resolvedTitle}:${cleanUrl}`)) return

      await checkAutoPageOverflow(320)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 60
        const startY = getDynamicNextY(20)

        let finalDataURL = ''
        let fileMimeType = 'image/jpeg'
        const lowerUrl = cleanUrl.toLowerCase()
        if (lowerUrl.endsWith('.png')) fileMimeType = 'image/png'
        else if (lowerUrl.endsWith('.webp')) fileMimeType = 'image/webp'
        else if (lowerUrl.endsWith('.svg')) fileMimeType = 'image/svg+xml'

        let imgWidth = 480
        let imgHeight = 280

        // Step 1: Detect raw SVG markup (including comments, doctypes, or xml declarations)
        const isRawSvg = (lowerUrl.includes('<svg') && lowerUrl.includes('</svg>')) ||
          /^\s*(?:<\?xml|<!DOCTYPE|<!--|<svg)/i.test(cleanUrl)

        if (isRawSvg) {
          const sanitized = sanitizeSvg(cleanUrl) || cleanUrl
          finalDataURL = svgToBase64DataUrl(sanitized)
          fileMimeType = 'image/svg+xml'
        }
        // Step 2: Detect unencoded / utf-8 SVG data URI (data:image/svg+xml,... without base64)
        else if (lowerUrl.startsWith('data:image/svg+xml') && !lowerUrl.includes(';base64,')) {
          const commaIdx = cleanUrl.indexOf(',')
          let rawPayload = commaIdx !== -1 ? cleanUrl.slice(commaIdx + 1) : cleanUrl
          try {
            rawPayload = decodeURIComponent(rawPayload)
          } catch {}
          const sanitized = sanitizeSvg(rawPayload) || rawPayload
          finalDataURL = svgToBase64DataUrl(sanitized)
          fileMimeType = 'image/svg+xml'
        }
        // Step 3: Base64 data URL
        else if (cleanUrl.startsWith('data:')) {
          const sanitized = sanitizeBase64DataUrl(cleanUrl)
          if (sanitized) {
            finalDataURL = sanitized
            const mimeMatch = sanitized.match(/^data:([^;,]+)/i)
            if (mimeMatch?.[1]) fileMimeType = mimeMatch[1].toLowerCase().trim()
          }
        }
        // Step 4: Remote HTTP / HTTPS URL
        else if (cleanUrl.startsWith('http://') || cleanUrl.startsWith('https://')) {
          let isExplicit404 = false
          // Attempt A: Server proxy with base64 dataUrl=true
          try {
            const proxyRes = await fetch(`/api/diagram/proxy?dataUrl=true&url=${encodeURIComponent(cleanUrl)}`)
            if (proxyRes.ok) {
              const proxyData = await proxyRes.json()
              if (proxyData.success && proxyData.dataURL) {
                const sanitized = sanitizeBase64DataUrl(proxyData.dataURL)
                if (sanitized) {
                  finalDataURL = sanitized
                  if (proxyData.contentType) fileMimeType = proxyData.contentType.split(';')[0].trim().toLowerCase()
                }
              }
            } else if (proxyRes.status === 404) {
              isExplicit404 = true
            }
          } catch (proxyErr) {
            console.warn('[drawImage] Server proxy fallback:', proxyErr)
          }

          // Attempt B: Direct CORS fetch if proxy didn't produce valid base64 data URL
          if (!isExplicit404 && !finalDataURL) {
            try {
              const resp = await fetch(cleanUrl, { mode: 'cors' })
              if (resp.ok) {
                const blob = await resp.blob()
                if (blob.type) fileMimeType = blob.type.split(';')[0].trim().toLowerCase()
                const b64 = await new Promise<string>((res, rej) => {
                  const reader = new FileReader()
                  reader.onloadend = () => res(reader.result as string)
                  reader.onerror = rej
                  reader.readAsDataURL(blob)
                })
                const sanitized = sanitizeBase64DataUrl(b64)
                if (sanitized) {
                  finalDataURL = sanitized
                }
              }
            } catch (fetchErr) {
              console.warn('[drawImage] Direct fetch fallback:', fetchErr)
            }
          }

          // Attempt C: Canvas capture via Image element with crossOrigin='anonymous'
          if (!finalDataURL && typeof window !== 'undefined') {
            try {
              const canvasB64 = await new Promise<string>((resolve, reject) => {
                const img = new window.Image()
                img.crossOrigin = 'anonymous'
                img.onload = () => {
                  try {
                    const canvas = document.createElement('canvas')
                    canvas.width = img.naturalWidth || 480
                    canvas.height = img.naturalHeight || 280
                    const ctx = canvas.getContext('2d')
                    if (!ctx) return reject(new Error('No canvas context'))
                    ctx.drawImage(img, 0, 0)
                    resolve(canvas.toDataURL('image/png'))
                  } catch (err) {
                    reject(err)
                  }
                }
                img.onerror = reject
                setTimeout(() => reject(new Error('Canvas image load timeout')), 1500)
                img.src = cleanUrl
              })
              const sanitized = sanitizeBase64DataUrl(canvasB64)
              if (sanitized) {
                finalDataURL = sanitized
                fileMimeType = 'image/png'
              }
            } catch {}
          }
        }
        // Step 5: Relative / local URL
        else if (cleanUrl.startsWith('/') || !cleanUrl.includes('://')) {
          try {
            const resp = await fetch(cleanUrl)
            if (resp.ok) {
              const blob = await resp.blob()
              if (blob.type) fileMimeType = blob.type.split(';')[0].trim().toLowerCase()
              const b64 = await new Promise<string>((res, rej) => {
                const reader = new FileReader()
                reader.onloadend = () => res(reader.result as string)
                reader.onerror = rej
                reader.readAsDataURL(blob)
              })
              const sanitized = sanitizeBase64DataUrl(b64)
              if (sanitized) {
                finalDataURL = sanitized
              }
            }
          } catch (relErr) {
            console.warn('[drawImage] Relative fetch error:', relErr)
          }
        }

        // Step 6: Fallback guard for non-base64 or failed sources
        const sanitizedFinal = sanitizeBase64DataUrl(finalDataURL)
        if (!sanitizedFinal) {
          console.warn('[drawImage] Using vector card fallback for non-base64 source:', cleanUrl.slice(0, 60))
          const fallbackSvg = createFallbackImageSvg(resolvedTitle, cleanUrl)
          finalDataURL = svgToBase64DataUrl(fallbackSvg)
          fileMimeType = 'image/svg+xml'
        } else {
          finalDataURL = sanitizedFinal
        }

        // Step 7: SVG Validation & PNG Rasterization guard for Excalidraw
        if (fileMimeType === 'image/svg+xml') {
          const { isValid, cleanSvg } = validateSvgForExcalidraw(finalDataURL)
          if (!isValid) {
            try {
              const pngDataUrl = await rasterizeSvgToPng(cleanSvg || cleanUrl, imgWidth, imgHeight)
              const cleanPng = sanitizeBase64DataUrl(pngDataUrl)
              if (cleanPng) {
                finalDataURL = cleanPng
                fileMimeType = 'image/png'
              } else {
                const fallbackSvg = createFallbackImageSvg(resolvedTitle, cleanUrl)
                finalDataURL = svgToBase64DataUrl(fallbackSvg)
              }
            } catch (rasterErr) {
              console.warn('[drawImage] SVG rasterization fallback error:', rasterErr)
              const fallbackSvg = createFallbackImageSvg(resolvedTitle, cleanUrl)
              finalDataURL = svgToBase64DataUrl(fallbackSvg)
            }
          }
        }

        if (typeof window !== 'undefined') {
          try {
            const probeImg = new window.Image()
            probeImg.src = finalDataURL
            await new Promise((resolve) => {
              probeImg.onload = resolve
              probeImg.onerror = resolve
              setTimeout(resolve, 600)
            })
            if (probeImg.naturalWidth && probeImg.naturalHeight) {
              const aspect = probeImg.naturalHeight / probeImg.naturalWidth
              imgWidth = Math.min(500, Math.max(300, probeImg.naturalWidth))
              imgHeight = Math.round(imgWidth * aspect)
            }
          } catch {}
        }

        if (imgHeight > 340) {
          const ratio = 340 / imgHeight
          imgHeight = 340
          imgWidth = Math.round(imgWidth * ratio)
        }
        if (imgHeight < 160) imgHeight = 160

        const fileId = `img_${Date.now()}_${Math.random().toString(36).substring(2, 8)}` as any
        const safeDataURL = sanitizeBase64DataUrl(finalDataURL) || svgToBase64DataUrl(createFallbackImageSvg(resolvedTitle, cleanUrl))
        const fileObj: any = {
          id: fileId,
          dataURL: safeDataURL,
          mimeType: fileMimeType,
          created: Date.now(),
        }

        if (excalidrawAPI?.addFiles) {
          try {
            if (isValidBase64DataUrl(fileObj.dataURL)) {
              excalidrawAPI.addFiles([fileObj])
            } else {
              console.warn('[drawImage] Skipping addFiles: invalid base64 dataURL avoided')
            }
          } catch (fileErr) {
            console.warn('[drawImage] excalidrawAPI.addFiles warning:', fileErr)
          }
        }

        if (typeof window !== 'undefined' && storageKey) {
          try {
            const rawFiles = localStorage.getItem(`${storageKey}_files`)
            const existingFiles = rawFiles ? JSON.parse(rawFiles) : {}
            existingFiles[fileId] = fileObj
            safeSaveWhiteboardStorage(`${storageKey}_files`, existingFiles, true)
          } catch (e) {
            console.warn('Error saving whiteboard file to localStorage:', e)
          }
        }

        const cardWidth = Math.max(imgWidth + 32, 440)
        const captionLines = resolvedCaption
          ? wrapText(resolvedCaption, cols(55))
          : []
        const captionHeight = captionLines.length * 18
        const zoomHintHeight = 22
        const cardHeight = imgHeight + 56 + (captionLines.length > 0 ? captionHeight + 10 : 0) + zoomHintHeight + 16

        const current = getCurrentElements()
        const customPayload = {
          isRough: false,
          isImageCard: true,
          isExpandableImage: true,
          fullUrl: cleanUrl,
          imageUrl: finalDataURL,
          title: resolvedTitle,
          caption: resolvedCaption,
        }

        const elementsToInsert: any[] = [
          {
            type: 'rectangle',
            x: startX,
            y: startY,
            width: cardWidth,
            height: cardHeight,
            strokeColor: '#CBD5E1',
            backgroundColor: '#FFFFFF',
            fillStyle: 'solid',
            strokeWidth: 1.5,
            roundness: { type: 3 },
            customData: customPayload,
          },
          {
            type: 'text',
            x: startX + 16,
            y: startY + 12,
            text: `[IMAGE]: ${resolvedTitle.toUpperCase()}`,
            fontSize: 14,
            fontFamily: 1,
            strokeColor: '#0F172A',
            customData: customPayload,
          },
          {
            type: 'image',
            x: startX + 16,
            y: startY + 44,
            width: imgWidth,
            height: imgHeight,
            fileId,
            status: 'saved',
            customData: customPayload,
          },
        ]

        let nextOffsetY = startY + 44 + imgHeight + 10
        if (captionLines.length > 0) {
          elementsToInsert.push({
            type: 'text',
            x: startX + 16,
            y: nextOffsetY,
            text: captionLines.join('\n'),
            fontSize: 12,
            fontFamily: 1,
            strokeColor: INK_SECONDARY,
            customData: customPayload,
          })
          nextOffsetY += captionHeight + 6
        }

        elementsToInsert.push({
          type: 'text',
          x: startX + 16,
          y: nextOffsetY,
          text: '[TAP/CLICK TO EXPAND HIGH-RES VIEW]',
          fontSize: 11,
          fontFamily: 1,
          strokeColor: '#52715D',
          customData: customPayload,
        })

        const elements = convertToExcalidrawElements(elementsToInsert)
        const merged = [...current, ...elements]
        const nextYTarget = Math.max(nextYRef.current, startY + cardHeight + 20)
        updateCurrentPageElements(merged, nextYTarget)
        onNoteRecorded?.(`[Image]: ${resolvedTitle}${resolvedCaption ? ` - ${resolvedCaption}` : ''}`)
      } catch (err) {
        console.error('drawImage error:', err)
      }
    }

    // Draw Video Demonstration Card directly on Whiteboard
    const drawVideoCard = async (title: string, description = '', url = '', mimeType = 'video/mp4') => {
      if (!excalidrawAPI || !title?.trim()) return

      // Dynamic video lookup if no URL provided
      let resolvedUrl = (url || '').trim()
      let resolvedMime = mimeType
      if (!resolvedUrl) {
        try {
          const res = await fetch(`/api/diagram/search-video?query=${encodeURIComponent(title)}&limit=1`)
          if (res.ok) {
            const data = await res.json()
            if (data.videos?.[0]?.url) {
              resolvedUrl = data.videos[0].url
              if (data.videos[0].mimeType) resolvedMime = data.videos[0].mimeType
            }
          }
        } catch (vidLookupErr) {
          console.warn('[drawVideoCard] Dynamic video discovery fallback warning:', vidLookupErr)
        }
      }

      await checkAutoPageOverflow(140)
      try {
        const { convertToExcalidrawElements } = await import('@excalidraw/excalidraw')
        const startX = 70
        const startY = getDynamicNextY(16)
        const customPayload = {
          isRough: false,
          isPlayableVideo: true,
          videoUrl: resolvedUrl,
          title: title.trim(),
          description: description?.trim() || '',
          mimeType: resolvedMime,
        }

        const elements = convertToExcalidrawElements([
          {
            type: 'rectangle',
            x: startX,
            y: startY,
            width: 420,
            height: 105,
            strokeColor: INK_CORAL,
            backgroundColor: '#FFF8F6',
            fillStyle: 'solid',
            strokeWidth: 1.5,
            roundness: { type: 3 },
            customData: customPayload,
          },
          {
            type: 'text',
            x: startX + 14,
            y: startY + 12,
            text: `[DEMONSTRATION VIDEO]: ${title.toUpperCase()}`,
            fontSize: 13,
            fontFamily: 1,
            strokeColor: INK_CORAL,
            customData: customPayload,
          },
          {
            type: 'text',
            x: startX + 14,
            y: startY + 38,
            text: description || `Visual experimental proof demonstration on ${title}.`,
            fontSize: 13,
            fontFamily: 1,
            strokeColor: INK_PRIMARY,
            customData: customPayload,
          },
          {
            type: 'text',
            x: startX + 14,
            y: startY + 74,
            text: url ? '[TAP/CLICK TO WATCH VIDEO DEMONSTRATION]' : '[LIVE EXPERIMENTAL DEMONSTRATION]',
            fontSize: 11,
            fontFamily: 1,
            strokeColor: url ? INK_CORAL : INK_MUTED,
            customData: customPayload,
          },
        ])

        const current = getCurrentElements()
        const merged = [...current, ...elements]
        updateCurrentPageElements(merged, startY + 125)
        onNoteRecorded?.(`[Video Demo]: ${title}`)
      } catch (err) {
        console.error('drawVideoCard error:', err)
      }
    }

    // Parse AI Directives like [BOARD_TITLE: ...], [DIAGRAM: ...], [IMAGE: ...], etc.
    const handleAiDirective = (rawText: string, transcriptId = 'global') => {
      if (!rawText) return

      // Match pseudo-code: write_chalkboard(action="...", content="...", color="...")
      const codeRegex = /write_chalkboard\s*\(\s*(?:action\s*=\s*)?["']?([a-zA-Z0-9_\-]+)["']?\s*(?:,\s*(?:content\s*=\s*)?(?:["']([^"']*)["']|([^"',\)]*)))?(?:,\s*(?:color\s*=\s*)?["']?([a-zA-Z0-9_#]+)["']?)?\s*\)/gi;
      const codeMatches = Array.from(rawText.matchAll(codeRegex));
      for (const cm of codeMatches) {
        const action = cm[1]?.toLowerCase();
        const content = (cm[2] ?? cm[3] ?? '').trim();
        const color = cm[4]?.trim();
        if (!action) continue;
        const signature = `CODE:${action}:${normalizeTitle(content)}`;
        if (executedDirectivesRef.current.has(signature)) continue;
        executedDirectivesRef.current.add(signature);

        enqueueOperation(async () => {
          if (action === 'draw_note' || action === 'note') {
            if (content && !checkIsRedundant(content)) await drawNote(content, color);
          } else if (action === 'draw_step' || action === 'step') {
            if (content && !checkIsRedundant(content)) await drawStep(content, color);
          } else if (action === 'draw_highlight_box' || action === 'highlight_box') {
            if (content && !checkIsRedundant(content)) await drawHighlightBox(content, color);
          } else if (action === 'draw_title' || action === 'title') {
            if (content && !checkIsRedundant(content)) await drawTitle(content, color);
          } else if (action === 'set_color' || action === 'color') {
            setChalkColor(content || color || '');
          } else if (action === 'draw_question' || action === 'question') {
            if (content) await drawQuestion(content, color);
          } else if (action === 'draw_student_answer' || action === 'student_answer') {
            if (content) await drawStudentAnswer(content, undefined, color);
          } else if (action === 'draw_answer_verdict' || action === 'answer_verdict') {
            if (content) await drawAnswerVerdict(content, undefined, color);
          } else if (action === 'draw_exam_question' || action === 'exam_question') {
            if (content) await drawExamQuestion(content, undefined, undefined, color);
          } else if (action === 'draw_shape' || action === 'shape' || action === 'draw_rectangle' || action === 'draw_circle' || action === 'draw_triangle') {
            if (content) await drawShape(content);
          } else if (action === 'draw_table' || action === 'table') {
            if (content) await drawTable(content);
          } else if (action === 'draw_graph' || action === 'graph') {
            if (content) await drawGraph(content);
          } else if (action === 'draw_geometry' || action === 'geometry') {
            if (content) await drawGeometry(content);
          } else if (action === 'draw_image' || action === 'image') {
            const anyContent = content as any;
            if (typeof anyContent === 'object' && anyContent !== null) {
              const url = anyContent.url || anyContent.image_url || anyContent.fullUrl;
              if (url) {
                await drawImage(url, anyContent.title, anyContent.caption);
              } else if (anyContent.query || anyContent.title) {
                try {
                  const res = await fetch(`/api/diagram/search-image?q=${encodeURIComponent(anyContent.query || anyContent.title)}`);
                  const data = await res.json();
                  const first = data.images?.[0];
                  if (first?.url) {
                    await drawImage(first.url, anyContent.title || first.title, anyContent.caption || first.description);
                  } else {
                    await drawSvgDiagram(anyContent.title || 'Scientific Diagram', '', anyContent.caption || '');
                  }
                } catch {
                  await drawSvgDiagram(anyContent.title || 'Scientific Diagram', '', anyContent.caption || '');
                }
              }
            } else if (typeof content === 'string') {
              const trimmed = content.trim();
              if (trimmed.startsWith('{') && trimmed.endsWith('}')) {
                try {
                  const parsed = JSON.parse(trimmed);
                  const url = parsed.url || parsed.image_url || parsed.fullUrl;
                  if (url) {
                    await drawImage(url, parsed.title, parsed.caption);
                  } else {
                    const res = await fetch(`/api/diagram/search-image?q=${encodeURIComponent(parsed.query || parsed.title || trimmed)}`);
                    const data = await res.json();
                    const first = data.images?.[0];
                    if (first?.url) await drawImage(first.url, parsed.title || first.title, parsed.caption || first.description);
                    else await drawSvgDiagram(parsed.title || 'Scientific Diagram', '', parsed.caption || '');
                  }
                } catch {
                  await drawSvgDiagram('Scientific Diagram', '', trimmed);
                }
              } else {
                const parts = trimmed.split('|').map((s) => s.trim());
                if (parts[0]?.startsWith('http') || parts[0]?.startsWith('data:')) {
                  await drawImage(parts[0], parts[1], parts[2]);
                } else if (parts[1]?.startsWith('http') || parts[1]?.startsWith('data:')) {
                  await drawImage(parts[1], parts[0], parts[2]);
                } else {
                  try {
                    const res = await fetch(`/api/diagram/search-image?q=${encodeURIComponent(parts[0] || trimmed)}`);
                    const data = await res.json();
                    const first = data.images?.[0];
                    if (first?.url) {
                      await drawImage(first.url, parts[0] || first.title, parts[1] || first.description);
                    } else {
                      await drawSvgDiagram(parts[0] || 'Scientific Diagram', '', parts[1] || '');
                    }
                  } catch {
                    await drawSvgDiagram(parts[0] || 'Scientific Diagram', '', parts[1] || '');
                  }
                }
              }
            }
          } else if (action === 'draw_video' || action === 'video') {
            let vidUrl = '';
            let vidTitle = 'Demonstration';
            let vidDesc = '';
            const rawContent: any = content;
            if (typeof rawContent === 'object' && rawContent !== null) {
              vidUrl = rawContent.url || rawContent.video_url || '';
              vidTitle = rawContent.title || 'Demonstration';
              vidDesc = rawContent.description || rawContent.caption || '';
            } else if (typeof rawContent === 'string') {
              const trimmed = rawContent.trim();
              if (trimmed.startsWith('{') && trimmed.endsWith('}')) {
                try {
                  const parsed = JSON.parse(trimmed);
                  vidUrl = parsed.url || parsed.video_url || '';
                  vidTitle = parsed.title || 'Demonstration';
                  vidDesc = parsed.description || parsed.caption || '';
                } catch {}
              } else {
                const parts = trimmed.split('|').map((s) => s.trim());
                if (parts[0]?.startsWith('http')) {
                  vidUrl = parts[0];
                  vidTitle = parts[1] || 'Demonstration';
                  vidDesc = parts[2] || '';
                } else if (parts[1]?.startsWith('http')) {
                  vidTitle = parts[0];
                  vidUrl = parts[1];
                  vidDesc = parts[2] || '';
                } else {
                  vidTitle = parts[0];
                  vidDesc = parts[1] || '';
                }
              }
            }
            if (vidUrl) {
              await drawVideoCard(vidTitle, vidDesc, vidUrl);
            } else {
              try {
                const r = await fetch('/api/diagram/search-video', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({ query: vidTitle }),
                });
                const data = await r.json();
                const first = data.videos?.[0];
                if (first?.url) {
                  await drawVideoCard(first.title || vidTitle, vidDesc || first.description, first.url, first.mimeType);
                } else {
                  await drawVideoCard(vidTitle, vidDesc);
                }
              } catch {
                await drawVideoCard(vidTitle, vidDesc);
              }
            }
          } else if (action === 'draw_numerical' || action === 'numerical' || action === 'worked_example' || action === 'solve') {
            if (typeof content === 'object') await drawNumericalSolution(content);
            else {
              const parts = (content || '').split('|').map((s) => s.trim());
              const solutionData: any = { answer: '' };
              parts.forEach((p) => {
                const lower = p.toLowerCase();
                if (lower.startsWith('problem:')) solutionData.problem = p.substring(8).trim();
                else if (lower.startsWith('given:')) solutionData.given = p.substring(6).trim();
                else if (lower.startsWith('formula:')) solutionData.formula = p.substring(8).trim();
                else if (lower.startsWith('substitution:') || lower.startsWith('sub:')) solutionData.substitution = p.split(':')[1]?.trim();
                else if (lower.startsWith('calculation:') || lower.startsWith('rough:')) solutionData.calculation = p.split(':')[1]?.trim();
                else if (lower.startsWith('answer:') || lower.startsWith('final:')) solutionData.answer = p.split(':')[1]?.trim();
                else if (lower.startsWith('unit:') || lower.startsWith('units:')) solutionData.unit = p.split(':')[1]?.trim();
                else if (!solutionData.problem) solutionData.problem = p;
                else if (!solutionData.answer) solutionData.answer = p;
              });
              await drawNumericalSolution(solutionData);
            }
          } else if (action === 'render_svg_diagram' || action === 'draw_svg' || action === 'draw_svg_diagram') {
            if (content) {
              const trimmed = content.trim();
              if (trimmed.includes('|') && trimmed.includes('<svg')) {
                const parts = trimmed.split('|').map((s) => s.trim());
                await drawSvgDiagram(parts[0] || 'Educational Diagram', parts[1] || '', parts[2]);
              } else if (trimmed.includes('<svg')) {
                await drawSvgDiagram('Educational Diagram', trimmed);
              } else {
                await drawSvgDiagram(trimmed, '');
              }
            }
          } else if (action === 'highlight_text' || action === 'highlight_word' || action === 'highlight_sentence' || action === 'highlight') {
            if (content) await highlightText(content, color);
          } else if (action === 'draw_flowchart' || action === 'flowchart') {
            if (content) await drawFlowchart(content, color);
          } else if (action === 'draw_rough_work' || action === 'rough_work' || action === 'rough') {
            if (content) await drawStep(content, color);
          } else if (action === 'new_page') {
            await addNewPage();
          } else if (action === 'clear_rough') {
            clearRough();
          } else if (action === 'clear_notes') {
            await clearNotes();
          } else if (action === 'concept_done') {
            onConceptDone?.(content);
          } else if (action === 'concept_focus') {
            onConceptFocus?.(content);
          } else if (action === 'concept_goto') {
            onConceptGoto?.(content);
          } else if (action === 'start_quiz' || action === 'open_quiz') {
            onStartQuiz?.();
          } else if (action === 'chapter_summary') {
            await drawTitle('Chapter Synthesis Summary', color);
            await drawNote(content, color);
            onNoteRecorded?.(`#### Chapter Summary:\n${content}`);
            onModuleComplete?.(content);
          }
        });
      }

      // Match pseudo-code: render_svg_diagram(title="...", svg="...", caption="...") or JSON format
      const svgToolRegex = /render_svg_diagram\s*\(([\s\S]*?)\)/gi;
      const svgMatches = Array.from(rawText.matchAll(svgToolRegex));
      for (const sm of svgMatches) {
        const body = sm[1]?.trim();
        if (!body) continue;
        let title = 'Educational Diagram';
        let svg = '';
        let caption = '';
        if (body.startsWith('{')) {
          try {
            const parsed = JSON.parse(body);
            title = parsed.title || title;
            svg = parsed.svg || '';
            caption = parsed.caption || '';
          } catch {}
        } else {
          const explicitTitle = body.match(/\btitle\s*=\s*["']([^"']*)["']/i);
          const explicitSvg = body.match(/\bsvg\s*=\s*["']([\s\S]*?)["'](?:\s*,\s*[a-zA-Z_]+\s*=|\s*$)/i);
          const explicitCaption = body.match(/\bcaption\s*=\s*["']([^"']*)["']/i);
          const explicitWhat = body.match(/\bwhat\s*=\s*["']([^"']*)["']/i);
          if (explicitSvg) {
            title = explicitTitle ? explicitTitle[1] : 'Educational Diagram';
            svg = explicitSvg[1];
            caption = explicitCaption ? explicitCaption[1] : (explicitWhat ? explicitWhat[1] : '');
          } else {
            const posMatch = body.match(/["']([^"']*)["']\s*,\s*["']([\s\S]*?)["'](?:\s*,\s*["']([^"']*)["'])?/);
            if (posMatch) {
              title = posMatch[1];
              svg = posMatch[2];
              caption = posMatch[3] || (explicitWhat ? explicitWhat[1] : '');
            }
          }
        }
        if (svg) {
          const signature = `SVG:${normalizeTitle(title)}:${svg.slice(0, 40)}`;
          if (!executedDirectivesRef.current.has(signature)) {
            executedDirectivesRef.current.add(signature);
            enqueueOperation(async () => {
              await drawSvgDiagram(title, svg, caption);
            });
          }
        }
      }

      const directiveRegex = /\[([A-Z_]+)(?::\s*([^\]]+))?\]/gi;
      const matches = Array.from(rawText.matchAll(directiveRegex))

      for (const match of matches) {
        const fullTag = match[0]
        const tagType = match[1]?.toUpperCase()
        const payload = match[2]?.trim() || ''
        const signature = `${tagType}:${normalizeTitle(payload)}`

        // Prevent repeated execution of the exact same directive
        if (executedDirectivesRef.current.has(signature)) {
          continue
        }
        executedDirectivesRef.current.add(signature)

        enqueueOperation(async () => {
          // 1. Board & Page Operations
          if (tagType === 'NEW_PAGE' || tagType === 'PAGE_NEW' || tagType === 'NEXT_PAGE') {
            await addNewPage()
          } else if (tagType === 'CLEAR_ROUGH') {
            clearRough()
          } else if (tagType === 'CLEAR_NOTES') {
            await clearNotes()
          } else if (tagType === 'REWRITE_NOTES') {
            if (payload) await rewriteNotes(payload)
            else await clearNotes()
          } else if (tagType === 'CLEAR_BOARD' || tagType === 'ERASE_BOARD') {
            await clearBoard()
          }
          // 2. Titles & Notes (Avoid duplicating module title and clean raw parentheses)
          else if (tagType === 'BOARD_TITLE' || tagType === 'TITLE') {
            const cleanPayload = payload.replace(/^[\s\(\[\{]+|[\s\)\]\}]+$/g, '').trim()
            if (cleanPayload && !checkIsRedundant(cleanPayload)) {
              const [titleText, color] = cleanPayload.includes('|') ? cleanPayload.split('|').map((s) => s.trim()) : [cleanPayload, undefined]
              await drawTitle(titleText, color)
            }
          } else if (
            tagType === 'BOARD_NOTE' ||
            tagType === 'NOTE' ||
            tagType === 'WRITE_BOARD' ||
            tagType === 'WRITE_CHALKBOARD' ||
            tagType === 'CHALKBOARD' ||
            tagType === 'BOARD' ||
            tagType === 'DRAW_NOTE' ||
            tagType === 'TEXT'
          ) {
            if (payload && !checkIsRedundant(payload)) {
              const [noteText, color] = payload.includes('|') ? payload.split('|').map((s) => s.trim()) : [payload, undefined]
              await drawNote(noteText, color)
            }
          } else if (tagType === 'BOARD_STEP' || tagType === 'STEP') {
            if (payload && !checkIsRedundant(payload)) {
              const [stepText, color] = payload.includes('|') ? payload.split('|').map((s) => s.trim()) : [payload, undefined]
              await drawStep(stepText, color)
            }
          } else if (tagType === 'HIGHLIGHT_BOX') {
            if (payload && !checkIsRedundant(payload)) {
              const [boxText, color] = payload.includes('|') ? payload.split('|').map((s) => s.trim()) : [payload, undefined]
              await drawHighlightBox(boxText, color)
            }
          } else if (tagType === 'FLOWCHART') {
            if (payload) {
              const [flowText, color] = payload.includes('|') && !payload.includes('->') ? payload.split('|').map((s) => s.trim()) : [payload, undefined]
              await drawFlowchart(flowText, color)
            }
          } else if (tagType === 'HIGHLIGHT' || tagType === 'HIGHLIGHT_WORD' || tagType === 'HIGHLIGHT_SENTENCE' || tagType === 'FOCUS_WORD') {
            if (payload) {
              const [hlText, color] = payload.includes('|') ? payload.split('|').map((s) => s.trim()) : [payload, undefined]
              await highlightText(hlText, color)
            }
          } else if (tagType === 'ROUGH_WORK' || tagType === 'ROUGH') {
            if (payload) {
              const [roughText, color] = payload.includes('|') ? payload.split('|').map((s) => s.trim()) : [payload, undefined]
              await drawStep(roughText, color)
            }
          } else if (tagType === 'SET_COLOR' || tagType === 'CHALK_COLOR' || tagType === 'COLOR') {
            if (payload) setChalkColor(payload)
          }
          // 2b. Math & Science Step-by-Step Problem Solving Directives
          else if (
            tagType === 'NUMERICAL' ||
            tagType === 'WORKED_EXAMPLE' ||
            tagType === 'SOLVE' ||
            tagType === 'MATH_SOLVE' ||
            tagType === 'BOARD_NUMERICAL'
          ) {
            if (payload) {
              const parts = payload.split('|').map((s) => s.trim())
              const solutionData: any = { answer: '' }
              parts.forEach((p) => {
                const lower = p.toLowerCase()
                if (lower.startsWith('problem:')) solutionData.problem = p.substring(8).trim()
                else if (lower.startsWith('given:')) solutionData.given = p.substring(6).trim()
                else if (lower.startsWith('formula:')) solutionData.formula = p.substring(8).trim()
                else if (lower.startsWith('substitution:') || lower.startsWith('sub:')) solutionData.substitution = p.split(':')[1]?.trim()
                else if (lower.startsWith('calculation:') || lower.startsWith('rough:')) solutionData.calculation = p.split(':')[1]?.trim()
                else if (lower.startsWith('answer:') || lower.startsWith('final:')) solutionData.answer = p.split(':')[1]?.trim()
                else if (lower.startsWith('unit:') || lower.startsWith('units:')) solutionData.unit = p.split(':')[1]?.trim()
                else if (!solutionData.problem) solutionData.problem = p
                else if (!solutionData.answer) solutionData.answer = p
              })
              await drawNumericalSolution(solutionData)
            }
          } else if (tagType === 'GIVEN' || tagType === 'BOARD_GIVEN') {
            if (payload) await drawStep(`Given: ${payload}`)
          } else if (tagType === 'FORMULA' || tagType === 'BOARD_FORMULA') {
            if (payload) await drawHighlightBox(`Formula: ${payload}`, INK_BOTANICAL)
          } else if (tagType === 'SUBSTITUTION' || tagType === 'SUBSTITUTE') {
            if (payload) await drawStep(`Substitution: ${payload}`)
          } else if (tagType === 'CALCULATION') {
            if (payload) await drawRoughWork(payload)
          } else if (tagType === 'FINAL_ANSWER' || tagType === 'BOXED_ANSWER') {
            if (payload) await drawHighlightBox(`Answer: ${payload}`, INK_CORAL)
          }
          // 2c. Universal Tables & Geometry
          else if (tagType === 'TABLE' || tagType === 'COMPARISON_TABLE') {
            if (payload) await drawTable(payload)
          } else if (tagType === 'GEOMETRY' || tagType === 'SHAPE' || tagType === 'POLYGON' || tagType === 'DRAW_SHAPE') {
            if (payload) await drawShape(payload)
          } else if (tagType === 'QUESTION' || tagType === 'CHECKPOINT_QUESTION') {
            if (payload) await drawQuestion(payload)
          } else if (tagType === 'STUDENT_ANSWER' || tagType === 'STUDENT_RESPONSE') {
            if (payload) await drawStudentAnswer(payload)
          } else if (tagType === 'VERDICT' || tagType === 'ANSWER_VERDICT' || tagType === 'CORRECTION') {
            if (payload) await drawAnswerVerdict(payload)
          } else if (tagType === 'EXAM_QUESTION' || tagType === 'BOARD_QUESTION') {
            if (payload) await drawExamQuestion(payload)
          } else if (tagType === 'TIMELINE') {
            if (payload) await drawFlowchart(payload)
          }
          // 3. Universal Diagrams, SVG & Graphs (Any Subject)
          else if (tagType === 'SVG' || tagType === 'SVG_DIAGRAM' || tagType === 'RENDER_SVG' || tagType === 'RENDER_SVG_DIAGRAM') {
            if (payload.includes('|') && payload.includes('<svg')) {
              const parts = payload.split('|').map((s) => s.trim())
              const title = parts[0] || 'Educational Diagram'
              const svg = parts[1] || ''
              const caption = parts[2] || ''
              if (svg) await drawSvgDiagram(title, svg, caption)
            } else if (payload.includes('<svg')) {
              await drawSvgDiagram('Educational Diagram', payload)
            }
          } else if (tagType === 'GRAPH' || tagType === 'DRAW_GRAPH') {
            await drawGraph(payload)
          } else if (tagType === 'DIAGRAM' || tagType === 'DRAW_DIAGRAM') {
            const diag = payload.toLowerCase()
            if (payload.includes('<svg') && payload.includes('</svg>')) {
              const titleMatch = payload.match(/title\s*=\s*["']([^"']+)["']/i)
              const title = titleMatch ? titleMatch[1] : 'Educational Diagram'
              const svgMatch = payload.match(/<svg[\s\S]*?<\/svg>/i)
              if (svgMatch) await drawSvgDiagram(title, svgMatch[0])
            } else if (diag.includes('triangle') || diag.includes('circle') || diag.includes('geometry') || diag.includes('polygon') || diag.includes('angle')) {
              await drawGeometry(payload)
            } else if (diag.includes('table') || diag.includes('compare') || diag.includes('vs')) {
              if (payload.includes('|')) await drawTable(payload)
              else await drawFlowchart(payload)
            } else if (diag.includes('timeline') || diag.includes('flow')) {
              await drawFlowchart(payload)
            } else if (
              isLegitimateGraphTopic(diag, subject || '') &&
              (diag.includes('graph') || diag.includes('ohm') || diag.includes('linear') || diag.includes('velocity') || diag.includes('speed') || diag.includes('distance') || diag.includes('wave') || diag.includes('parabola') || diag.includes('quad') || diag.includes('boyle') || diag.includes('curve') || diag.includes('plot') || diag.includes('='))
            ) {
              await drawGraph(diag)
            } else {
              // Universal dynamic vector SVG diagram for any syllabus subject
              await drawSvgDiagram(payload || 'Scientific Diagram', '', '')
            }
          }
          // 4. Board Videos & Dynamic Vector Diagrams
          else if (tagType === 'IMAGE' || tagType === 'DRAW_IMAGE') {
            const parts = payload.split('|').map((s) => s.trim())
            if (parts[0]?.startsWith('http') || parts[0]?.startsWith('data:')) {
              await drawImage(parts[0], parts[1], parts[2])
            } else if (parts[1]?.startsWith('http') || parts[1]?.startsWith('data:')) {
              await drawImage(parts[1], parts[0], parts[2])
            } else {
              try {
                const res = await fetch(`/api/diagram/search-image?q=${encodeURIComponent(parts[0] || payload)}&limit=3`)
                const data = await res.json()
                const candidateImages: any[] = data.images || []
                let loaded = false
                for (const img of candidateImages) {
                  if (!img?.url) continue
                  try {
                    const check = await fetch(`/api/diagram/proxy?dataUrl=true&url=${encodeURIComponent(img.url)}`)
                    if (check.ok) {
                      const pData = await check.json()
                      if (pData.success && pData.dataURL) {
                        await drawImage(pData.dataURL, parts[0] || img.title, parts[1] || img.description)
                        loaded = true
                        break
                      }
                    }
                  } catch {}
                }
                if (!loaded) {
                  await drawSvgDiagram(parts[0] || 'Scientific Diagram', '', parts[1] || '')
                }
              } catch {
                await drawSvgDiagram(parts[0] || 'Scientific Diagram', '', parts[1] || '')
              }
            }
          } else if (tagType === 'VIDEO' || tagType === 'DRAW_VIDEO') {
            const [vidTitle, vidDesc] = payload.split('|').map((s) => s.trim())
            await drawVideoCard(vidTitle || 'Visual Demonstration', vidDesc || '')
          }
          // 5. Questions and Progress
          else if (tagType === 'BOARD_QUESTION' || tagType === 'QUESTION') {
            if (payload) {
              await drawQuestion(payload)
            }
          } else if (tagType === 'CONFIRM_END_CHAPTER') {
            if (payload) {
              await drawQuestion(payload)
              onConfirmEndChapter?.(payload)
            }
          } else if (tagType === 'START_QUIZ' || tagType === 'OPEN_QUIZ') {
            onStartQuiz?.()
          } else if (tagType === 'CHAPTER_SUMMARY') {
            if (payload) {
              await drawTitle('Chapter Synthesis Summary')
              await drawNote(payload)
              onNoteRecorded?.(`#### Chapter Summary:\n${payload}`)
              onModuleComplete?.(payload)
            }
          } else if (tagType === 'MODULE_DONE' || tagType === 'LESSON_COMPLETE') {
            // Invariant: Do NOT write "Capsule Completed Successfully" on the board
            onModuleComplete?.(payload || 'Lesson finished')
          } else if (tagType === 'CONCEPT_FOCUS' || tagType === 'FOCUS') {
            const cleanPayload = (payload || '')
              .replace(/^focus:\s*/i, '')
              .replace(/^concept\s*\d*:\s*/i, '')
              .replace(/^[\s\(\[\{]+|[\s\)\]\}]+$/g, '')
              .trim()
            if (cleanPayload) {
              onConceptFocus?.(cleanPayload)
            }
          } else if (tagType === 'CONCEPT_DONE' || tagType === 'CONCEPT_MASTERED' || tagType === 'MASTERED') {
            const cleanPayload = (payload || '').trim()
            // Invariant: Do NOT write "Mastered: ..." or "Concept Done" on the board.
            onConceptDone?.(cleanPayload)
          } else if (tagType === 'CONCEPT_GOTO' || tagType === 'GOTO_CONCEPT') {
            if (payload) onConceptGoto?.(payload)
          } else if (tagType === 'RESET_MODULE_PROGRESS' || tagType === 'TEACH_FROM_START') {
            onConceptGoto?.(1)
          } else if (tagType === 'BOARD') {
            if (payload) await drawText(payload)
          }
        })
      }
    }

    const restoreBoardState = (savedPages: WhiteboardPage[], files?: Record<string, any>) => {
      if (!savedPages || !Array.isArray(savedPages) || savedPages.length === 0) return
      try {
        if (files && excalidrawAPI?.addFiles) {
          const filesArr: any[] = []
          for (const f of Object.values(files) as any[]) {
            if (!f || !f.id) continue
            const cleanDataUrl = sanitizeBase64DataUrl(f.dataURL)
            if (!cleanDataUrl) continue
            f.dataURL = cleanDataUrl
            if (f.mimeType === 'image/svg+xml') {
              const { isValid } = validateSvgForExcalidraw(cleanDataUrl)
              if (!isValid) {
                const fallbackSvg = createFallbackImageSvg('Whiteboard Asset')
                f.dataURL = svgToBase64DataUrl(fallbackSvg)
              }
            }
            filesArr.push(f)
          }
          if (filesArr.length > 0) {
            try {
              excalidrawAPI.addFiles(filesArr)
            } catch (fileErr) {
              console.warn('[restoreBoardState] excalidrawAPI.addFiles warning:', fileErr)
            }
          }
        }
        pagesRef.current = savedPages
        setPages(savedPages)
        const targetPage = savedPages[currentPageIndexRef.current] || savedPages[0]
        boardElementsRef.current = targetPage.elements || []
        nextYRef.current = targetPage.nextY || 140
        roughYRef.current = targetPage.roughY || 140

        if (excalidrawAPI) {
          excalidrawAPI.updateScene({
            elements: targetPage.elements || [],
            appState: {
              viewBackgroundColor: 'transparent',
              currentItemStrokeColor: INK_PRIMARY,
              currentItemFontFamily: 1,
              currentItemRoughness: 0,
              gridModeEnabled: true,
              zoom: { value: boardZoomRef.current },
              scrollX: 0,
              scrollY: 0,
            },
          })
        }

        if (storageKey && typeof window !== 'undefined') {
          safeSaveWhiteboardStorage(storageKey, savedPages)
          if (files) {
            safeSaveWhiteboardStorage(`${storageKey}_files`, files, true)
          }
        }
      } catch (err) {
        console.warn('[GreenChalkboard] Error restoring board state:', err)
      }
    }

    // Expose imperative API
    useImperativeHandle(ref, () => ({
      highlightText: (text: string, color?: string) => enqueueOperation(async () => highlightText(text, color)),
      drawText: (text: string, x?: number, y?: number, color?: string) => enqueueOperation(async () => drawText(text, x, y, color)),
      drawTitle: (title: string, color?: string) => enqueueOperation(async () => drawTitle(title, color)),
      drawStep: (stepText: any, color?: string) => enqueueOperation(async () => drawStep(stepText, color)),
      drawNote: (noteText: any, color?: string) => enqueueOperation(async () => drawNote(noteText, color)),
      drawQuestion: (questionText: string, color?: string) => enqueueOperation(async () => drawQuestion(questionText, color)),
      drawHighlightBox: (text: string, color?: string) => enqueueOperation(async () => drawHighlightBox(text, color)),
      drawFlowchart: (flowText: string, color?: string) => enqueueOperation(async () => drawFlowchart(flowText, color)),
      drawRoughWork: (workText: string, color?: string) => enqueueOperation(async () => drawRoughWork(workText, color)),
      clearRough,
      clearNotes,
      rewriteNotes,
      clearBoard,
      resetBoard,
      setChalkColor: (colorNameOrHex: string) => setChalkColor(colorNameOrHex),
      setBoardColor: () => {},
      drawSvgDiagram: (title: string, svgMarkup: string, caption?: string, forceUpdate?: boolean) => enqueueOperation(async () => drawSvgDiagram(title, svgMarkup, caption, forceUpdate)),
      drawImage: (urlOrDataUrl: string, title?: string, caption?: string) => enqueueOperation(async () => drawImage(urlOrDataUrl, title, caption)),
      drawDiagramSkeleton,
      clearDiagramSkeleton,
      drawGraph: (type?: string) => enqueueOperation(async () => drawGraph(type)),
      drawNumericalSolution: (solution: any) => enqueueOperation(async () => drawNumericalSolution(solution)),
      drawVideoCard: (title: string, description?: string, url?: string, mimeType?: string) => enqueueOperation(async () => drawVideoCard(title, description, url, mimeType)),
      drawTable: (tableStr: string) => enqueueOperation(async () => drawTable(tableStr)),
      drawGeometry: (geomStr: string) => enqueueOperation(async () => drawGeometry(geomStr)),
      drawShape: (shapeDef: any) => enqueueOperation(async () => drawShape(shapeDef)),
      drawStudentAnswer: (answerText: string, isCorrect?: boolean, color?: string) => enqueueOperation(async () => drawStudentAnswer(answerText, isCorrect, color)),
      drawAnswerVerdict: (verdictText: string, isCorrect?: boolean, color?: string) => enqueueOperation(async () => drawAnswerVerdict(verdictText, isCorrect, color)),
      drawExamQuestion: (questionText: string, modelAnswer?: string, marks?: string, color?: string) => enqueueOperation(async () => drawExamQuestion(questionText, modelAnswer, marks, color)),
      addNewPage,
      goToPage,
      getBoardSummary,
      getCompactBoardContext,
      handleAiDirective,
      getActiveQuestion: () => activeQuestionRef.current,
      getNextY: () => nextYRef.current,
      getCurrentPageIndex: () => currentPageIndexRef.current,
      restoreBoardState,
    }))

    return (
      <div className="whiteboard-container relative w-full h-full flex flex-col rounded-2xl overflow-hidden border border-[#E5E3DB] shadow-[0_10px_30px_-10px_rgba(23,24,23,0.06)]" style={{ backgroundColor: "#F8F6F0", backgroundImage: "url('/landing_images/bg.jpg')", backgroundRepeat: "repeat", backgroundSize: "1000px auto" }}>
        {/* Excalidraw Light Engine - 100% Uninterrupted Vertical Height */}
        <div
          ref={containerRef}
          onClick={handleContainerClick}
          onClickCapture={handleContainerClick}
          className="relative flex-1 w-full h-full bg-transparent" style={{ backgroundColor: "transparent" }}
        >
          <Excalidraw
            excalidrawAPI={handleExcalidrawAPI}
            onChange={handleExcalidrawChange}
            theme="light"
            viewModeEnabled={true}
            gridModeEnabled={true}
            initialData={EXCALIDRAW_INITIAL_DATA}
            UIOptions={EXCALIDRAW_UI_OPTIONS}
          />

          {/* Exact Board-Font Word-by-Word Typing & Smooth Fade-Out Chalk Overlay */}
          {activeTyping && (
            <div
              key={activeTyping.id}
              style={{
                position: 'absolute',
                left: `${((activeTyping.canvasX || 60) + (excalidrawAPIRef.current?.getAppState?.()?.scrollX || 0)) * boardZoom}px`,
                top: `${((activeTyping.canvasY || 100) + (excalidrawAPIRef.current?.getAppState?.()?.scrollY || 0)) * boardZoom}px`,
                transform: `scale(${boardZoom})`,
                transformOrigin: 'top left',
                zIndex: 25,
                maxWidth: `min(840px, ${Math.max(160, ((containerRef.current?.clientWidth || 840) - ((activeTyping.canvasX || 60) + (excalidrawAPIRef.current?.getAppState?.()?.scrollX || 0)) * boardZoom - 12) / boardZoom)}px)`,
                pointerEvents: 'none',
                fontFamily: 'Excalifont, Virgil, Xiaolai, "Segoe UI Emoji", sans-serif',
                fontSize: `${activeTyping.fontSize}px`,
                lineHeight: 1.38,
                color: activeTyping.color,
                opacity: activeTyping.isFadingOut ? 0 : 1,
                transition: 'opacity 0.28s cubic-bezier(0.16, 1, 0.3, 1)',
              }}
              className="select-none flex items-start"
            >
              {/* Optional Dot Bullet matching board ellipse */}
              {activeTyping.bulletType === 'dot' && (
                <span
                  style={{
                    display: 'inline-block',
                    width: '8px',
                    height: '8px',
                    borderRadius: '50%',
                    backgroundColor: activeTyping.bulletColor || activeTyping.color,
                    marginTop: '8px',
                    marginRight: '12px',
                    flexShrink: 0,
                  }}
                />
              )}

              {/* Optional Step Arrow matching board derivation */}
              {activeTyping.bulletType === 'step' && (
                <span
                  style={{
                    display: 'inline-block',
                    marginRight: '8px',
                    color: activeTyping.color,
                    fontWeight: 'bold',
                  }}
                >
                  -&gt;
                </span>
              )}

              {/* Words typed word-by-word with exact board font & size */}
              <div className="flex-1 whitespace-pre-wrap leading-relaxed">
                {activeTyping.words.slice(0, activeTyping.visibleWordCount).map((word, wIdx) => (
                  <span
                    key={`${activeTyping.id}-${wIdx}`}
                    style={{
                      display: 'inline-block',
                      marginRight: '0.28em',
                      animation: 'chalkWordFadeIn 0.18s cubic-bezier(0.16, 1, 0.3, 1) forwards',
                    }}
                  >
                    {word}
                  </span>
                ))}

                {/* Chalk typing cursor / blinking caret */}
                {!activeTyping.isFadingOut && (
                  <span
                    style={{
                      display: 'inline-block',
                      width: '2px',
                      height: `${activeTyping.fontSize * 0.9}px`,
                      marginLeft: '2px',
                      backgroundColor: activeTyping.color,
                      verticalAlign: 'middle',
                    }}
                    className="animate-pulse"
                  />
                )}
              </div>
            </div>
          )}
        </div>

        {/* Floating Top-Right Whiteboard Controls: Clear Board Action */}
        <div className="absolute top-3 right-3 z-30 flex items-center gap-2 pointer-events-auto">
          <button
            type="button"
            onClick={() => {
              if (typeof window !== 'undefined' && window.confirm('Clear all notes and drawings from the whiteboard?')) {
                clearBoard()
              }
            }}
            className="group flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-[#E5E3DB] bg-white/95 backdrop-blur-md text-[#555852] hover:text-[#DC2626] hover:border-[#DC2626]/40 hover:bg-[#FEF2F2] transition-all shadow-xs hover:shadow-sm cursor-pointer active:scale-95 text-xs font-mono select-none"
            title="Clear all board notes & drawings"
            aria-label="Clear all board"
          >
            <Trash2 className="w-3.5 h-3.5 text-[#7A7C75] group-hover:text-[#DC2626] transition-colors" />
            <span className="hidden sm:inline font-medium">Clear Board</span>
          </button>
        </div>

        {/* Minimalist Bottom Bar: Multi-Page Navigation, Chalk Swatches, and Page Counter */}
        <div className="relative z-20 py-1.5 px-3 bg-[#F8F6F0] border-t border-[#E5E3DB] flex flex-wrap items-center justify-between gap-2 text-[11px] font-mono text-[#7A7C75] select-none">
          {/* Multi-Page Navigation Bar */}
          <div className="flex items-center gap-1.5 bg-white px-2 py-0.5 rounded-lg border border-[#E5E3DB] shadow-xs">
            <span className="hidden sm:inline text-[10px] text-[#7A7C75] font-mono mr-0.5">Pages:</span>
            <div className="flex items-center gap-1">
              {pages.map((p, idx) => (
                <button
                  key={p.id}
                  onClick={() => switchPage(idx)}
                  className={`px-2 py-0.5 text-[10px] font-mono rounded-md transition-all cursor-pointer ${
                    currentPageIndex === idx
                      ? 'bg-[#52715D] text-white font-bold shadow-xs'
                      : 'text-[#555852] hover:bg-[#F8F6F0]'
                  }`}
                  title={`View Page ${idx + 1}`}
                >
                  {idx + 1}
                </button>
              ))}
            </div>

            <button
              onClick={addNewPage}
              className="p-0.5 rounded text-[#52715D] hover:bg-[#E8F0EA] transition-colors cursor-pointer ml-0.5"
              title="Add New Whiteboard Page"
            >
              <Plus className="w-3 h-3" />
            </button>
          </div>

          {/* Multi-Color Chalk Palette */}
          <div className="flex items-center gap-1.5 bg-white px-2 py-1 rounded-lg border border-[#E5E3DB] shadow-xs">
            <span className="hidden sm:inline text-[10px] text-[#7A7C75] font-mono mr-0.5">Chalk:</span>
            {[
              { name: 'Charcoal', value: INK_PRIMARY, title: 'Charcoal / Primary Ink' },
              { name: 'Botanical', value: INK_BOTANICAL, title: 'Botanical Green' },
              { name: 'Coral', value: INK_CORAL, title: 'Coral / Red' },
              { name: 'Amber', value: INK_AMBER, title: 'Amber / Gold' },
              { name: 'Blue', value: INK_BLUE, title: 'Ocean Blue' },
              { name: 'Purple', value: INK_PURPLE, title: 'Amethyst Purple' },
            ].map((swatch) => (
              <button
                key={swatch.name}
                type="button"
                onClick={() => setChalkColor(swatch.value)}
                className={`w-3 h-3 rounded-full transition-all cursor-pointer border ${
                  activeChalkColor === swatch.value
                    ? 'scale-125 ring-2 ring-[#52715D] ring-offset-1 border-white shadow-xs'
                    : 'border-black/10 hover:scale-115'
                }`}
                style={{ backgroundColor: swatch.value }}
                title={swatch.title}
                aria-label={swatch.title}
              />
            ))}
          </div>

          {/* Page Counter, Clear Button & Status */}
          <div className="flex items-center gap-2 sm:gap-3">
                        <span className="text-[#52715D] font-bold text-[11px]">{currentPageIndex + 1}/{pages.length}</span>
          </div>
        </div>

        {/* Full-Screen Scientific Visual Lightbox Modal */}
        {lightboxImage && (
          <div
            className="fixed inset-0 z-[100] flex flex-col bg-black/85 backdrop-blur-md animate-fadeIn"
            onClick={(e) => {
              if (e.target === e.currentTarget) {
                setLightboxImage(null)
                setLightboxZoom(1)
                setLightboxPan({ x: 0, y: 0 })
              }
            }}
          >
            {/* Lightbox Header Bar */}
            <div className="flex items-center justify-between px-6 py-4 bg-black/40 border-b border-white/10 text-white">
              <div className="flex items-center gap-3">
                <span className="px-2.5 py-1 rounded bg-[#52715D] text-xs font-semibold uppercase tracking-wider text-white">
                  High-Res Visual
                </span>
                <h3 className="text-base font-serif font-medium text-white/95">
                  {lightboxImage.title}
                </h3>
              </div>
              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={() => setLightboxZoom((prev) => Math.max(0.5, prev - 0.25))}
                  className="p-2 rounded-lg bg-white/10 hover:bg-white/20 text-white transition-colors cursor-pointer"
                  title="Zoom Out"
                >
                  <ZoomOut className="w-4 h-4" />
                </button>
                <span className="text-xs font-mono text-white/70 px-1 min-w-[3rem] text-center">
                  {Math.round(lightboxZoom * 100)}%
                </span>
                <button
                  type="button"
                  onClick={() => setLightboxZoom((prev) => Math.min(4, prev + 0.25))}
                  className="p-2 rounded-lg bg-white/10 hover:bg-white/20 text-white transition-colors cursor-pointer"
                  title="Zoom In"
                >
                  <ZoomIn className="w-4 h-4" />
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setLightboxZoom(1)
                    setLightboxPan({ x: 0, y: 0 })
                  }}
                  className="p-2 rounded-lg bg-white/10 hover:bg-white/20 text-white transition-colors cursor-pointer"
                  title="Reset Zoom"
                >
                  <Maximize2 className="w-4 h-4" />
                </button>
                <div className="h-4 w-px bg-white/20 mx-1" />
                <button
                  type="button"
                  onClick={() => {
                    setLightboxImage(null)
                    setLightboxZoom(1)
                    setLightboxPan({ x: 0, y: 0 })
                  }}
                  className="p-2 rounded-lg bg-white/10 hover:bg-red-500/80 text-white transition-colors cursor-pointer"
                  title="Close (Esc)"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>
            </div>

            {/* Lightbox Interactive Image Stage */}
            <div
              className="flex-1 w-full h-full overflow-hidden flex items-center justify-center p-4 cursor-grab active:cursor-grabbing select-none"
              onMouseDown={(e) => {
                setIsDraggingLightbox(true)
                dragStartRef.current = {
                  startX: e.clientX,
                  startY: e.clientY,
                  initialPanX: lightboxPan.x,
                  initialPanY: lightboxPan.y,
                }
              }}
              onMouseMove={(e) => {
                if (!isDraggingLightbox) return
                const dx = e.clientX - dragStartRef.current.startX
                const dy = e.clientY - dragStartRef.current.startY
                setLightboxPan({
                  x: dragStartRef.current.initialPanX + dx,
                  y: dragStartRef.current.initialPanY + dy,
                })
              }}
              onMouseUp={() => setIsDraggingLightbox(false)}
              onMouseLeave={() => setIsDraggingLightbox(false)}
              onWheel={(e) => {
                if (e.cancelable) e.preventDefault()
                const delta = e.deltaY < 0 ? 0.15 : -0.15
                setLightboxZoom((prev) => Math.min(4, Math.max(0.5, prev + delta)))
              }}
            >
              <div
                style={{
                  transform: `translate(${lightboxPan.x}px, ${lightboxPan.y}px) scale(${lightboxZoom})`,
                  transition: isDraggingLightbox ? 'none' : 'transform 0.15s cubic-bezier(0.16, 1, 0.3, 1)',
                }}
                className="max-w-[90vw] max-h-[80vh] flex items-center justify-center"
              >
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={lightboxImage.url}
                  alt={lightboxImage.title}
                  referrerPolicy="no-referrer"
                  onError={(e) => {
                    const target = e.currentTarget
                    if (!target.src.includes('/api/diagram/proxy')) {
                      target.src = `/api/diagram/proxy?url=${encodeURIComponent(lightboxImage.url)}`
                    }
                  }}
                  className="max-w-[85vw] max-h-[75vh] object-contain rounded-lg shadow-2xl border border-white/10 pointer-events-none"
                />
              </div>
            </div>

            {/* Lightbox Footer Note */}
            {lightboxImage.caption && (
              <div className="px-6 py-3 bg-black/60 border-t border-white/10 text-center">
                <p className="text-sm font-sans text-white/80 max-w-3xl mx-auto">
                  {lightboxImage.caption}
                </p>
              </div>
            )}
          </div>
        )}

        {/* Educational Demonstration Video Modal */}
        {videoModal && (
          <div
            className="fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex flex-col items-center justify-center p-4 animate-in fade-in duration-200"
            onClick={() => setVideoModal(null)}
          >
            <div
              className="relative max-w-4xl w-full bg-[#1A1A1A] rounded-2xl overflow-hidden border border-white/10 shadow-2xl flex flex-col"
              onClick={(e) => e.stopPropagation()}
            >
              {/* Video Modal Header */}
              <div className="flex items-center justify-between px-6 py-4 border-b border-white/10 bg-[#141414]">
                <div>
                  <span className="text-xs uppercase tracking-widest text-emerald-400 font-mono font-semibold">[DEMONSTRATION VIDEO]</span>
                  <h3 className="text-base font-serif font-bold text-white mt-0.5">{videoModal.title}</h3>
                </div>
                <button
                  type="button"
                  onClick={() => setVideoModal(null)}
                  className="p-2 rounded-lg bg-white/10 hover:bg-red-500/80 text-white transition-colors cursor-pointer"
                  title="Close (Esc)"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              {/* Video Player */}
              <div className="w-full bg-black flex items-center justify-center aspect-video max-h-[65vh]">
                {(() => {
                  const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/
                  const match = videoModal.url.match(regExp)
                  const ytId = match && match[2].length === 11 ? match[2] : null
                  if (ytId) {
                    return (
                      <iframe
                        src={`https://www.youtube.com/embed/${ytId}?autoplay=1&rel=0`}
                        title={videoModal.title}
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowFullScreen
                        className="w-full h-full border-0"
                      />
                    )
                  }
                  return (
                    <video
                      src={videoModal.url}
                      controls
                      autoPlay
                      playsInline
                      {...({ referrerPolicy: 'no-referrer' } as any)}
                      className="w-full h-full object-contain"
                      onError={(e) => {
                        const target = e.currentTarget
                        if (!target.src.includes('/api/diagram/proxy')) {
                          target.src = `/api/diagram/proxy?url=${encodeURIComponent(videoModal.url)}`
                        }
                      }}
                    />
                  )
                })()}
              </div>

              {/* Video Modal Footer */}
              {videoModal.description && (
                <div className="px-6 py-3 bg-[#141414] border-t border-white/10 text-center">
                  <p className="text-sm font-sans text-white/80 max-w-3xl mx-auto">
                    {videoModal.description}
                  </p>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    )
  }
)

GreenChalkboard.displayName = 'GreenChalkboard'

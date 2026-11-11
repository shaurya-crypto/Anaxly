'use client'

import React, { forwardRef, useState, useEffect, useCallback, useRef } from 'react'
import { GreenChalkboard, GreenChalkboardRef, WritingPositionInfo } from './GreenChalkboard'
import { SobiCompanion } from './SobiCompanion'
import { LiveChalkSubtitleStreamer, ActiveHighlight } from './LiveChalkSubtitleStreamer'
import { VisualizationViewport } from './VisualizationViewport'
import { MafsGraphCanvas, MafsGraphCanvasProps, GraphDisplayMode } from './MafsGraphCanvas'
import { VisualizationSceneType } from './scenes/sceneTypes'
import { resolveSceneType } from './scenes/sceneRegistry'
import { VisualLessonManifest, LessonStep } from '@/types/lessonManifest'
import { motion } from 'motion/react'
import {
  Box,
  Minimize2,
  X,
  Activity,
  Sparkles,
} from 'lucide-react'

// Whiteboard Workspace forwards all chalkboard directives to GreenChalkboard, including set_color and raw SVG when trimmed.includes('<svg')

export interface WhiteboardWorkspaceProps {
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
  activeSceneType?: VisualizationSceneType | string | null
  activeSceneParams?: Record<string, any>
  activeSceneTitle?: string
  onCloseScene?: () => void
  lessonManifest?: VisualLessonManifest | null
  initialStepIndex?: number
  onStepChange?: (stepIndex: number, step: LessonStep) => void
  onSaveProgress?: (stepIndex: number, completedStepIds: string[]) => void
  latestTranscript?: string
  isTeacherSpeaking?: boolean
  isListening?: boolean
  onSubmitStudentAnswer?: (answer: string) => void
  onVoiceStudentAnswer?: (answer: string) => void
  activeGraph?: MafsGraphCanvasProps | null
  onCloseGraph?: () => void
  generatingDiagramTitle?: string | null
  activeHighlight?: ActiveHighlight | null
}

export const WhiteboardWorkspace = forwardRef<GreenChalkboardRef, WhiteboardWorkspaceProps>(
  (
    {
      moduleId,
      moduleTitle,
      classLevel,
      subject,
      keyConcepts,
      activeConceptIndex,
      onPageChange,
      onNoteRecorded,
      onConceptFocus,
      onConceptDone,
      onConceptGoto,
      onBoardContentChange,
      onModuleComplete,
      onConfirmEndChapter,
      onStartQuiz,
      activeSceneType = null,
      activeSceneParams = {},
      activeSceneTitle,
      onCloseScene,
      lessonManifest = null,
      initialStepIndex = 0,
      onStepChange,
      onSaveProgress,
      latestTranscript = '',
      isTeacherSpeaking = false,
      isListening = true,
      onSubmitStudentAnswer,
      onVoiceStudentAnswer,
      activeGraph = null,
      onCloseGraph,
      generatingDiagramTitle = null,
      activeHighlight = null,
    },
    ref
  ) => {
    // Resolved canonical scene type via alias resolver
    const resolvedScene = activeSceneType ? resolveSceneType(activeSceneType) : null

    // Sobi Whiteboard Companion writing position tracking
    const [writingPosition, setWritingPosition] = useState<WritingPositionInfo | null>(null)

    // Workspace container ref for bounds tracking
    const workspaceContainerRef = useRef<HTMLDivElement | null>(null)

    // In-Board Mathematical Vector Graph Display Mode:
    // 'docked' (split side-panel on right) | 'floating' (moveable draggable box) | 'maximized' | 'minimized'
    const [graphMode, setGraphMode] = useState<GraphDisplayMode>('docked')

    // Automatically expand and dock the graph panel when a new graph is triggered by tutor
    useEffect(() => {
      if (activeGraph) {
        setGraphMode((prev) => (prev === 'minimized' ? 'docked' : prev))
      }
    }, [activeGraph?.formula, activeGraph?.title])

    const handleWritingPositionChange = useCallback((pos: WritingPositionInfo) => {
      setWritingPosition((prev) => {
        if (
          prev &&
          prev.nextY === pos.nextY &&
          prev.pageIndex === pos.pageIndex &&
          prev.lastAction === pos.lastAction &&
          prev.lastText === pos.lastText
        ) {
          return prev
        }
        return pos
      })
    }, [])

    // 3D Scene In-Whiteboard Display Mode:
    // 'box_in_board' (embedded container box right on the whiteboard) | 'minimized'
    const [sceneBoxMode, setSceneBoxMode] = useState<'box_in_board' | 'minimized'>('box_in_board')

    // When an active scene is summoned, pop open the in-board box
    useEffect(() => {
      if (activeSceneType) {
        setSceneBoxMode((prev) => (prev === 'minimized' ? 'box_in_board' : prev))
      }
    }, [activeSceneType])

    // Format active params summary string for badge
    const paramSummary = Object.entries(activeSceneParams || {})
      .filter(([k]) => !['color', 'wireframe'].includes(k))
      .slice(0, 3)
      .map(([k, v]) => `${k}: ${v}`)
      .join(' · ')

    const hasDockedGraph = Boolean(activeGraph && graphMode === 'docked')

    return (
      <div 
        ref={workspaceContainerRef} 
        className="relative w-full h-full flex flex-row overflow-hidden bg-[#13211B]"
      >
        {/* Main Digital Chalkboard Canvas (Expands to full width or shares row with docked graph) */}
        <div className="relative flex-1 h-full min-w-0 overflow-hidden flex flex-col">
          {/* Whiteboard Visual Progress Box */}
          {generatingDiagramTitle && (
            <div className="absolute top-4 sm:top-6 left-1/2 -translate-x-1/2 z-30 pointer-events-none animate-in fade-in slide-in-from-top-4 duration-300">
              <div className="flex items-center gap-3 px-4 py-2.5 rounded-xl bg-[#0c1612]/95 backdrop-blur-md border border-emerald-500/40 shadow-xl ring-1 ring-white/10">
                <div className="relative flex items-center justify-center w-7 h-7 rounded-lg bg-emerald-950/90 border border-emerald-500/50 text-emerald-400 shrink-0">
                  <Sparkles className="w-3.5 h-3.5 animate-spin [animation-duration:3s]" />
                  <span className="absolute -top-0.5 -right-0.5 w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
                </div>
                <p className="text-xs text-white/95 font-medium truncate max-w-[280px] sm:max-w-[420px]">
                  Generating visualization: <span className="text-emerald-300 font-semibold">{generatingDiagramTitle}</span>...
                </p>
                {/* Indeterminate shimmer pulse bar */}
                <div className="w-14 h-1.5 bg-emerald-950/80 rounded-full overflow-hidden shrink-0 border border-emerald-800/40">
                  <div className="w-full h-full bg-gradient-to-r from-emerald-500 via-teal-200 to-emerald-500 animate-scholastic-shimmer rounded-full" />
                </div>
              </div>
            </div>
          )}

          <GreenChalkboard
            ref={ref}
            moduleId={moduleId}
            moduleTitle={moduleTitle}
            classLevel={classLevel}
            subject={subject}
            keyConcepts={keyConcepts}
            activeConceptIndex={activeConceptIndex}
            onPageChange={onPageChange}
            onNoteRecorded={onNoteRecorded}
            onConceptFocus={onConceptFocus}
            onConceptDone={onConceptDone}
            onConceptGoto={onConceptGoto}
            onBoardContentChange={onBoardContentChange}
            onModuleComplete={onModuleComplete}
            onConfirmEndChapter={onConfirmEndChapter}
            onStartQuiz={onStartQuiz}
            onWritingPositionChange={handleWritingPositionChange}
          />

          {/* Sobi Whiteboard Companion: Glides alongside writing and points to questions */}
          <SobiCompanion
            writingPosition={writingPosition}
            latestTranscript={latestTranscript}
            isTeacherSpeaking={isTeacherSpeaking}
            isListening={isListening}
            activeConceptTitle={
              keyConcepts && typeof activeConceptIndex === 'number'
                ? keyConcepts[activeConceptIndex] || moduleTitle
                : moduleTitle
            }
            onSubmitAnswer={(ans) => {
              if (onSubmitStudentAnswer) {
                onSubmitStudentAnswer(ans)
              } else if (ref && typeof ref !== 'function' && ref.current) {
                ref.current.drawStudentAnswer?.(ans)
              }
            }}
            onVoiceAnswer={(ans) => {
              if (onVoiceStudentAnswer) {
                onVoiceStudentAnswer(ans)
              } else if (ref && typeof ref !== 'function' && ref.current) {
                ref.current.drawStudentAnswer?.(ans)
              }
            }}
          />

          {/* Live Word-by-Word Chalk Subtitle Streamer with Smooth Fade-out */}
          <LiveChalkSubtitleStreamer
            latestTranscript={latestTranscript}
            isTeacherSpeaking={isTeacherSpeaking}
            activeHighlight={activeHighlight}
          />

          {/* In-Whiteboard 3D Simulation Box (Rendered directly inside whiteboard area) */}
          {resolvedScene && sceneBoxMode === 'box_in_board' && (
            <div className="absolute bottom-4 right-4 z-30 w-[92vw] max-w-[480px] h-[370px] sm:h-[410px] rounded-2xl border-2 border-[#52715D]/80 shadow-[0_20px_50px_rgba(0,0,0,0.35)] bg-[#0c1310] flex flex-col overflow-hidden animate-in fade-in slide-in-from-bottom-6 duration-300">
              {/* Embedded Box Top Controls Bar */}
              <div className="px-3.5 py-2 bg-[#122319] border-b border-emerald-900/60 flex items-center justify-between gap-2 select-none">
                <div className="flex items-center gap-2 min-w-0">
                  <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse shrink-0" />
                  <span className="text-xs font-semibold text-emerald-100 truncate">
                    {activeSceneTitle || 'In-Board 3D Simulation'}
                  </span>
                  {paramSummary && (
                    <span className="hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-emerald-950/80 text-emerald-300 border border-emerald-800/40 truncate max-w-[160px]">
                      {paramSummary}
                    </span>
                  )}
                </div>

                <div className="flex items-center gap-1 shrink-0">
                  {/* Minimize toggle */}
                  <button
                    onClick={() => setSceneBoxMode('minimized')}
                    className="p-1 rounded text-emerald-300 hover:text-white hover:bg-emerald-900/50 transition-colors cursor-pointer"
                    title="Minimize simulation box"
                  >
                    <Minimize2 className="w-3.5 h-3.5" />
                  </button>
                  {/* Close button */}
                  <button
                    onClick={() => onCloseScene?.()}
                    className="p-1 rounded text-emerald-300 hover:text-rose-400 hover:bg-rose-950/40 transition-colors cursor-pointer"
                    title="Close simulation"
                  >
                    <X className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>

              {/* Live 3D WebGL Canvas inside the box */}
              <div className="flex-1 w-full h-full relative overflow-hidden">
                <VisualizationViewport
                  sceneType={resolvedScene}
                  initialParams={activeSceneParams}
                  title={activeSceneTitle}
                  onClose={onCloseScene}
                />
              </div>
            </div>
          )}

          {/* Minimized Simulation Floating Pill */}
          {resolvedScene && sceneBoxMode === 'minimized' && (
            <button
              onClick={() => setSceneBoxMode('box_in_board')}
              className="absolute bottom-4 right-4 z-30 flex items-center gap-2 px-3.5 py-2 rounded-xl bg-[#122319] border border-emerald-500/60 shadow-xl text-emerald-100 hover:bg-[#1a3324] transition-all cursor-pointer group animate-in fade-in"
            >
              <Box className="w-4 h-4 text-emerald-400 group-hover:rotate-12 transition-transform" />
              <span className="text-xs font-semibold">
                3D Simulation Active {paramSummary ? `(${paramSummary})` : ''}
              </span>
              <span className="text-[10px] px-1.5 py-0.5 rounded bg-emerald-900 text-emerald-200">Expand</span>
            </button>
          )}
        </div>

        {/* MODE A: Docked Side-Panel Inside the Chalkboard (Right 45% of workspace) */}
        {hasDockedGraph && activeGraph && (
          <div className="relative w-full sm:w-[460px] md:w-[480px] lg:w-[520px] h-full shrink-0 border-l-2 border-[#E2E8F0] bg-[#FFFFFF] shadow-2xl flex flex-col z-20 animate-in slide-in-from-right duration-300">
            <MafsGraphCanvas
              formula={activeGraph.formula}
              domain={activeGraph.domain}
              range={activeGraph.range}
              title={activeGraph.title}
              callout={activeGraph.callout}
              points={activeGraph.points}
              displayMode="docked"
              onModeChange={setGraphMode}
              onClose={onCloseGraph}
            />
          </div>
        )}

        {/* MODE B: Moveable Floating Window (Draggable by student anywhere over the board) */}
        {activeGraph && graphMode === 'floating' && (
          <motion.div
            drag
            dragMomentum={false}
            dragElastic={0.05}
            className="absolute top-12 right-6 z-30 w-[92vw] max-w-[500px] h-[450px] shadow-[0_25px_60px_rgba(15,23,42,0.18)] cursor-default animate-in fade-in zoom-in-95 duration-200"
          >
            <MafsGraphCanvas
              formula={activeGraph.formula}
              domain={activeGraph.domain}
              range={activeGraph.range}
              title={activeGraph.title}
              callout={activeGraph.callout}
              points={activeGraph.points}
              displayMode="floating"
              onModeChange={setGraphMode}
              onClose={onCloseGraph}
            />
          </motion.div>
        )}

        {/* MODE C: Maximized Full-Chalkboard Graph Viewport */}
        {activeGraph && graphMode === 'maximized' && (
          <div className="absolute inset-2 z-40 rounded-2xl overflow-hidden shadow-[0_25px_70px_rgba(15,23,42,0.22)] animate-in fade-in zoom-in-95 duration-200">
            <MafsGraphCanvas
              formula={activeGraph.formula}
              domain={activeGraph.domain}
              range={activeGraph.range}
              title={activeGraph.title}
              callout={activeGraph.callout}
              points={activeGraph.points}
              displayMode="maximized"
              onModeChange={setGraphMode}
              onClose={onCloseGraph}
            />
          </div>
        )}

        {/* MODE D: Minimized Floating Pill in Top-Right */}
        {activeGraph && graphMode === 'minimized' && (
          <button
            onClick={() => setGraphMode('docked')}
            className="absolute top-14 right-4 z-30 flex items-center gap-2 px-3.5 py-2 rounded-xl bg-[#FFFFFF] border border-[#CBD5E1] shadow-xl text-[#0F172A] hover:bg-[#F8FAFC] transition-all cursor-pointer group animate-in fade-in"
            title="Expand mathematical graph"
          >
            <Activity className="w-4 h-4 text-[#2563EB] group-hover:rotate-12 transition-transform" />
            <span className="text-xs font-semibold font-mono">
              Graph: y = {activeGraph.formula}
            </span>
            <span className="text-[10px] px-1.5 py-0.5 rounded-md bg-[#EFF6FF] text-[#2563EB] border border-[#BFDBFE] font-mono font-bold">
              Expand
            </span>
          </button>
        )}
      </div>
    )
  }
)

WhiteboardWorkspace.displayName = 'WhiteboardWorkspace'

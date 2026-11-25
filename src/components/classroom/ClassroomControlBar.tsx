'use client'

import React, { useEffect, useRef, useState } from 'react'
import {
  Mic,
  MicOff,
  Video,
  VideoOff,
  Pause,
  Play,
  Captions,
  CaptionsOff,
  BookOpen,
  MessageSquare,
  Layers,
  MoreVertical,
  PhoneOff,
  ChevronRight,
  Settings2,
  NotebookPen,
  ClipboardCheck,
  CheckCircle2,
} from 'lucide-react'

export interface ClassroomControlBarProps {
  isMuted: boolean
  userVolumeRef?: React.RefObject<number>
  onToggleMute: () => void
  isCameraOn: boolean
  onToggleCamera: () => void
  isPaused: boolean
  onTogglePause: () => void
  captionsOn: boolean
  onToggleCaptions: () => void
  hasBook: boolean
  isBookOpen: boolean
  onToggleBook: () => void
  activePanel: 'chat' | 'concepts' | null
  onTogglePanel: (panel: 'chat' | 'concepts') => void
  conceptProgress?: string
  onNextConcept: () => void
  onEndCall: () => void
  onOpenSettings: () => void
  onOpenNotes?: () => void
  onOpenQuiz: () => void
  onMarkComplete?: () => void
  elapsed: string
  title: string
}

function RoundButton({
  label,
  shortcut,
  active = true,
  danger = false,
  pressed,
  onClick,
  children,
  className = '',
}: {
  label: string
  shortcut?: string
  active?: boolean
  danger?: boolean
  pressed?: boolean
  onClick: () => void
  children: React.ReactNode
  className?: string
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label={label}
      aria-pressed={pressed}
      title={shortcut ? `${label} (${shortcut})` : label}
      className={`group relative flex h-11 w-11 shrink-0 items-center justify-center rounded-full transition-colors active:scale-95 cursor-pointer focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white/70 ${
        danger
          ? 'bg-[#EA4335] text-white hover:bg-[#d33426]'
          : active
          ? 'bg-[#3C4043] text-white hover:bg-[#4a4e51]'
          : 'bg-[#EA4335] text-white hover:bg-[#d33426]'
      } ${className}`}
    >
      {children}
      <span className="pointer-events-none absolute -top-9 hidden whitespace-nowrap rounded-md bg-[#3C4043] px-2 py-1 text-[11px] text-white opacity-0 shadow transition-opacity group-hover:opacity-100 md:block">
        {shortcut ? `${label} · ${shortcut}` : label}
      </span>
    </button>
  )
}

export function ClassroomControlBar(props: ClassroomControlBarProps) {
  const {
    isMuted,
    userVolumeRef,
    onToggleMute,
    isCameraOn,
    onToggleCamera,
    isPaused,
    onTogglePause,
    captionsOn,
    onToggleCaptions,
    hasBook,
    isBookOpen,
    onToggleBook,
    activePanel,
    onTogglePanel,
    conceptProgress,
    onNextConcept,
    onEndCall,
    onOpenSettings,
    onOpenNotes,
    onOpenQuiz,
    onMarkComplete,
    elapsed,
    title,
  } = props
  const [menuOpen, setMenuOpen] = useState(false)
  const rippleRef = useRef<HTMLSpanElement | null>(null)
  const menuRef = useRef<HTMLDivElement | null>(null)

  // Mic volume ripple, read from a ref so the bar does not re-render per frame.
  useEffect(() => {
    let id = 0
    const tick = () => {
      const vol = userVolumeRef?.current ?? 0
      const el = rippleRef.current
      if (el) {
        if (!isMuted && vol > 0.04) {
          el.style.opacity = `${Math.min(1, vol * 2.5)}`
          el.style.transform = `scale(${1 + Math.min(vol, 1) * 0.35})`
        } else {
          el.style.opacity = '0'
        }
      }
      id = requestAnimationFrame(tick)
    }
    id = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(id)
  }, [isMuted, userVolumeRef])

  // Meet-style shortcuts: Ctrl/Cmd+D mic, Ctrl/Cmd+E camera.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (!(e.ctrlKey || e.metaKey)) return
      const k = e.key.toLowerCase()
      if (k === 'd') {
        e.preventDefault()
        onToggleMute()
      } else if (k === 'e') {
        e.preventDefault()
        onToggleCamera()
      }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [onToggleMute, onToggleCamera])

  useEffect(() => {
    if (!menuOpen) return
    const onDown = (e: MouseEvent) => {
      if (!menuRef.current?.contains(e.target as Node)) setMenuOpen(false)
    }
    window.addEventListener('mousedown', onDown)
    return () => window.removeEventListener('mousedown', onDown)
  }, [menuOpen])

  const menuItem = (label: string, Icon: React.ElementType, onClick: () => void, mobileOnly = false) => (
    <button
      type="button"
      onClick={() => {
        setMenuOpen(false)
        onClick()
      }}
      className={`${mobileOnly ? 'md:hidden ' : ''}flex w-full items-center gap-3 rounded-lg px-3 py-2.5 text-left text-sm text-[#E8EAED] hover:bg-white/10 cursor-pointer`}
    >
      <Icon className="h-4 w-4 shrink-0 text-[#9AA0A6]" />
      {label}
    </button>
  )

  return (
    <div className="relative flex h-[72px] shrink-0 items-center justify-between gap-2 bg-[#202124] px-3 sm:px-5">
      {/* Left: clock + title (desktop) */}
      <div className="hidden min-w-0 flex-1 items-center gap-3 text-sm text-[#E8EAED] lg:flex">
        <span className="tabular-nums">{elapsed}</span>
        <span className="h-4 w-px bg-white/20" />
        <span className="truncate">{title}</span>
      </div>

      {/* Center: main controls */}
      <div className="flex flex-1 items-center justify-center gap-2 sm:gap-3 lg:flex-none">
        <RoundButton
          label={isMuted ? 'Turn on microphone' : 'Turn off microphone'}
          shortcut="Ctrl+D"
          active={!isMuted}
          pressed={!isMuted}
          onClick={onToggleMute}
        >
          <span
            ref={rippleRef}
            className="pointer-events-none absolute inset-0 rounded-full ring-2 ring-[#8AB4F8] transition-transform duration-75"
            style={{ opacity: 0 }}
          />
          {isMuted ? <MicOff className="h-5 w-5" /> : <Mic className="h-5 w-5" />}
        </RoundButton>
        <RoundButton
          label={isCameraOn ? 'Turn off camera' : 'Turn on camera'}
          shortcut="Ctrl+E"
          active={isCameraOn}
          pressed={isCameraOn}
          onClick={onToggleCamera}
        >
          {isCameraOn ? <Video className="h-5 w-5" /> : <VideoOff className="h-5 w-5" />}
        </RoundButton>
        <RoundButton
          label={isPaused ? 'Resume lesson' : 'Pause lesson'}
          onClick={onTogglePause}
          className="hidden sm:flex"
        >
          {isPaused ? <Play className="h-5 w-5" /> : <Pause className="h-5 w-5" />}
        </RoundButton>
        <RoundButton
          label={captionsOn ? 'Turn off captions' : 'Turn on captions'}
          pressed={captionsOn}
          onClick={onToggleCaptions}
          className={`hidden sm:flex ${captionsOn ? '!bg-[#8AB4F8] !text-[#202124]' : ''}`}
        >
          {captionsOn ? <Captions className="h-5 w-5" /> : <CaptionsOff className="h-5 w-5" />}
        </RoundButton>
        {hasBook && (
          <RoundButton
            label={isBookOpen ? 'Hide textbook' : 'Open textbook'}
            pressed={isBookOpen}
            onClick={onToggleBook}
            className={`hidden sm:flex ${isBookOpen ? '!bg-[#8AB4F8] !text-[#202124]' : ''}`}
          >
            <BookOpen className="h-5 w-5" />
          </RoundButton>
        )}
        <button
          type="button"
          onClick={onNextConcept}
          title="Mark current concept as understood and move to the next"
          className="hidden h-11 items-center gap-1.5 rounded-full bg-[#3C4043] px-4 text-sm font-medium text-white hover:bg-[#4a4e51] active:scale-95 cursor-pointer md:flex"
        >
          <CheckCircle2 className="h-4 w-4 text-[#81C995]" />
          Understood
          <ChevronRight className="h-4 w-4 opacity-70" />
        </button>
        <div ref={menuRef} className="relative">
          <RoundButton label="More options" onClick={() => setMenuOpen((o) => !o)} pressed={menuOpen}>
            <MoreVertical className="h-5 w-5" />
          </RoundButton>
          {menuOpen && (
            <div className="absolute bottom-14 left-1/2 z-50 w-60 -translate-x-1/2 rounded-xl bg-[#2D2E31] p-1.5 shadow-2xl ring-1 ring-white/10">
              {menuItem(isPaused ? 'Resume lesson' : 'Pause lesson', isPaused ? Play : Pause, onTogglePause, true)}
              {menuItem(captionsOn ? 'Turn off captions' : 'Turn on captions', Captions, onToggleCaptions, true)}
              {hasBook && menuItem(isBookOpen ? 'Hide textbook' : 'Open textbook', BookOpen, onToggleBook, true)}
              {menuItem('Understood · next concept', CheckCircle2, onNextConcept, true)}
              {menuItem('Concepts', Layers, () => onTogglePanel('concepts'), true)}
              {menuItem('Chat with tutor', MessageSquare, () => onTogglePanel('chat'), true)}
              {onOpenNotes && menuItem('Chapter notes', NotebookPen, onOpenNotes)}
              {menuItem('Take mastery quiz', ClipboardCheck, onOpenQuiz)}
              {onMarkComplete && menuItem('Mark chapter complete', CheckCircle2, onMarkComplete)}
              {menuItem('Avatar & voice settings', Settings2, onOpenSettings)}
            </div>
          )}
        </div>
        <button
          type="button"
          onClick={onEndCall}
          aria-label="Leave class"
          title="Leave class"
          className="flex h-11 w-14 items-center justify-center rounded-full bg-[#EA4335] text-white hover:bg-[#d33426] active:scale-95 cursor-pointer"
        >
          <PhoneOff className="h-5 w-5" />
        </button>
      </div>

      {/* Right: panels (desktop) */}
      <div className="hidden flex-1 items-center justify-end gap-1 md:flex">
        <button
          type="button"
          onClick={() => onTogglePanel('concepts')}
          aria-pressed={activePanel === 'concepts'}
          title="Concepts"
          className={`flex h-11 items-center gap-1.5 rounded-full px-3 text-sm cursor-pointer ${
            activePanel === 'concepts' ? 'bg-[#8AB4F8]/20 text-[#8AB4F8]' : 'text-[#E8EAED] hover:bg-white/10'
          }`}
        >
          <Layers className="h-5 w-5" />
          {conceptProgress && <span className="tabular-nums">{conceptProgress}</span>}
        </button>
        <button
          type="button"
          onClick={() => onTogglePanel('chat')}
          aria-pressed={activePanel === 'chat'}
          title="Chat with tutor"
          className={`flex h-11 w-11 items-center justify-center rounded-full cursor-pointer ${
            activePanel === 'chat' ? 'bg-[#8AB4F8]/20 text-[#8AB4F8]' : 'text-[#E8EAED] hover:bg-white/10'
          }`}
        >
          <MessageSquare className="h-5 w-5" />
        </button>
      </div>
    </div>
  )
}

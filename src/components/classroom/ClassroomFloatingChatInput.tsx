'use client'

import React, { useState, useRef, useCallback } from 'react'
import { Sparkles, ArrowUp, ChevronDown, MessageSquare } from 'lucide-react'

export interface ClassroomFloatingChatInputProps {
  onSendMessage: (message: string) => void
  disabled?: boolean
  isTeacherSpeaking?: boolean
  className?: string
}

const QUICK_PROMPT_CHIPS = [
  { label: '💡 Give an example', prompt: 'Can you explain this with a concrete everyday example?' },
  { label: '❓ Why does this work?', prompt: 'Why does this underlying mechanism/formula hold true?' },
  { label: '✍️ Solve step-by-step', prompt: 'Can you solve a step-by-step numerical on the board for this?' },
  { label: '🔄 Explain again', prompt: 'Could you please explain that concept again simply step-by-step?' },
]

export function ClassroomFloatingChatInput({
  onSendMessage,
  disabled = false,
  isTeacherSpeaking = false,
  className = '',
}: ClassroomFloatingChatInputProps) {
  const [message, setMessage] = useState('')
  const [isMinimized, setIsMinimized] = useState(false)
  const [showChips, setShowChips] = useState(false)
  const inputRef = useRef<HTMLInputElement>(null)

  const handleSend = useCallback(
    (textToSend?: string) => {
      const text = (textToSend || message).trim()
      if (!text || disabled) return
      onSendMessage(text)
      setMessage('')
      setShowChips(false)
    },
    [message, disabled, onSendMessage]
  )

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    handleSend()
  }

  // Minimized floating trigger pill
  if (isMinimized) {
    return (
      <div className={`fixed bottom-12 sm:bottom-14 left-1/2 -translate-x-1/2 z-30 pointer-events-auto ${className}`}>
        <button
          type="button"
          onClick={() => {
            setIsMinimized(false)
            setTimeout(() => inputRef.current?.focus(), 80)
          }}
          className="flex items-center gap-2 px-4 py-2 rounded-full bg-white/95 border border-[#E5E3DB] shadow-[0_8px_25px_rgba(0,0,0,0.12)] text-xs font-semibold text-[var(--ink-primary)] hover:border-[var(--accent-sage)] hover:bg-white transition-all cursor-pointer backdrop-blur-md active:scale-95 group"
          title="Open text chat with AI tutor"
        >
          <MessageSquare className="w-3.5 h-3.5 text-[var(--accent-sage)] group-hover:scale-110 transition-transform" />
          <span>Ask Tutor (Type Message)</span>
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
        </button>
      </div>
    )
  }

  return (
    <div
      className={`fixed bottom-12 sm:bottom-14 left-1/2 -translate-x-1/2 z-30 w-[94vw] sm:w-[480px] md:w-[540px] max-w-2xl pointer-events-auto animate-in fade-in slide-in-from-bottom-3 duration-200 ${className}`}
      onKeyDown={(e) => e.stopPropagation()}
    >
      <div className="flex flex-col gap-1.5 w-full">
        {/* Quick Socratic Prompt Chips */}
        {showChips && (
          <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar px-1 py-0.5 animate-in fade-in slide-in-from-bottom-2 duration-150">
            {QUICK_PROMPT_CHIPS.map((chip) => (
              <button
                key={chip.label}
                type="button"
                onClick={() => handleSend(chip.prompt)}
                disabled={disabled}
                className="px-2.5 py-1 rounded-full bg-white/95 border border-stone-200 hover:border-[var(--accent-sage)] text-[11px] font-medium text-[var(--ink-secondary)] hover:text-[var(--ink-primary)] transition-all shadow-2xs whitespace-nowrap cursor-pointer hover:bg-stone-50 disabled:opacity-50"
              >
                {chip.label}
              </button>
            ))}
          </div>
        )}

        {/* Floating Chat Input Bar */}
        <form
          onSubmit={handleSubmit}
          className="flex items-center gap-2 bg-white/95 backdrop-blur-md border border-[#E5E3DB] shadow-[0_10px_35px_rgba(0,0,0,0.12)] rounded-2xl p-1.5 sm:p-2 transition-all focus-within:border-[var(--accent-sage)] focus-within:ring-2 focus-within:ring-[var(--accent-sage)]/20"
        >
          <button
            type="button"
            onClick={() => setShowChips((prev) => !prev)}
            className={`w-8 h-8 rounded-xl flex items-center justify-center shrink-0 transition-colors cursor-pointer ${
              showChips
                ? 'bg-[var(--accent-sage)] text-white'
                : 'bg-[var(--accent-sage-soft)] text-[var(--accent-sage)] hover:brightness-95'
            }`}
            title="Toggle quick suggested questions (AI speaks reply)"
          >
            <Sparkles className="w-4 h-4" />
          </button>

          <input
            ref={inputRef}
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onFocus={() => {
              if (!showChips && !message) setShowChips(true)
            }}
            placeholder={
              isTeacherSpeaking
                ? 'Type to ask tutor... (AI will pause and reply in voice)'
                : 'Ask a doubt or question... (AI replies in voice)'
            }
            disabled={disabled}
            className="flex-1 bg-transparent border-0 text-xs sm:text-sm text-[var(--ink-primary)] placeholder:text-stone-400 focus:outline-none focus:ring-0 px-1.5 py-1 min-w-0"
          />

          {/* Send Button */}
          <button
            type="submit"
            disabled={disabled || !message.trim()}
            aria-label="Send message to AI tutor"
            title="Send message (AI replies in voice)"
            className="w-8 h-8 rounded-xl bg-[var(--accent-sage)] hover:brightness-105 active:scale-95 text-white flex items-center justify-center transition-all cursor-pointer disabled:opacity-30 disabled:cursor-not-allowed shrink-0 shadow-xs"
          >
            <ArrowUp className="w-4 h-4 stroke-[2.5]" />
          </button>

          {/* Minimize Button */}
          <button
            type="button"
            onClick={() => setIsMinimized(true)}
            className="p-1 rounded-lg text-stone-400 hover:text-stone-600 hover:bg-stone-100 transition-colors cursor-pointer shrink-0"
            title="Minimize chat input"
          >
            <ChevronDown className="w-4 h-4" />
          </button>
        </form>
      </div>
    </div>
  )
}

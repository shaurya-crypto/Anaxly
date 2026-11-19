'use client'

import React, { useState, useEffect } from 'react'
import { SlidersHorizontal } from 'lucide-react'

export interface ClassroomSpeedControlProps {
  onSpeedChange: (speed: number) => void
  initialSpeed?: number
  className?: string
}

export function ClassroomSpeedControl({
  onSpeedChange,
  initialSpeed = 1.0,
  className = '',
}: ClassroomSpeedControlProps) {
  const [speed, setSpeed] = useState<number>(initialSpeed)
  const [isOpen, setIsOpen] = useState(false)

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const saved = localStorage.getItem('anaxly_tutor_speed')
      if (saved) {
        const val = parseFloat(saved)
        if (!isNaN(val) && val >= 0.75 && val <= 1.3) {
          setSpeed(val)
          onSpeedChange(val)
        }
      }
    }
  }, [onSpeedChange])

  const handleSpeedUpdate = (newSpeed: number) => {
    const clamped = Math.max(0.75, Math.min(1.3, Math.round(newSpeed * 100) / 100))
    setSpeed(clamped)
    onSpeedChange(clamped)
    if (typeof window !== 'undefined') {
      localStorage.setItem('anaxly_tutor_speed', clamped.toString())
    }
  }

  const speedPresets = [0.75, 0.85, 1.0, 1.15, 1.25]

  return (
    <div className={`relative z-20 select-none ${className}`}>
      <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/90 backdrop-blur-md border border-[var(--border-subtle)] shadow-xs transition-all">
        <button
          type="button"
          onClick={() => setIsOpen((prev) => !prev)}
          className="flex items-center gap-1.5 text-xs font-medium text-[var(--ink-secondary)] hover:text-[var(--ink-primary)] transition-colors cursor-pointer"
          title="Adjust tutor voice speed"
          aria-label="Adjust tutor voice speed"
        >
          <SlidersHorizontal className="w-3.5 h-3.5 text-[var(--accent-primary)]" />
          <span className="font-mono text-xs font-semibold tabular-nums text-[var(--ink-primary)]">
            Speed: {speed.toFixed(2).replace(/\.00$/, '.0').replace(/(\.\d)0$/, '$1')}x
          </span>
        </button>

        {isOpen && (
          <div className="flex items-center gap-2 pl-2 border-l border-[var(--border-subtle)] animate-in fade-in slide-in-from-right-1 duration-150">
            <input
              type="range"
              min="0.75"
              max="1.3"
              step="0.05"
              value={speed}
              onChange={(e) => handleSpeedUpdate(parseFloat(e.target.value))}
              aria-label="Voice playback speed slider"
              className="w-20 h-1 bg-[var(--border-strong)] rounded-lg appearance-none cursor-pointer accent-[var(--accent-primary)]"
            />
            <div className="hidden sm:flex items-center gap-1">
              {speedPresets.map((preset) => (
                <button
                  key={preset}
                  type="button"
                  onClick={() => handleSpeedUpdate(preset)}
                  className={`px-1.5 py-0.5 rounded text-xs font-mono transition-colors cursor-pointer ${
                    Math.abs(speed - preset) < 0.03
                      ? 'bg-[var(--accent-primary)] text-white font-bold'
                      : 'text-[var(--ink-muted)] hover:text-[var(--ink-primary)] hover:bg-black/5'
                  }`}
                >
                  {preset}x
                </button>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

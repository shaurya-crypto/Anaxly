'use client'

import React, { useRef, useState, useEffect } from 'react'

export interface ClassroomConnectingAnimationProps {
  stageText?: string
  connectionState?: string
  className?: string
}

const STAGES = [
  'Getting your tutor ready…',
  'Loading Authentic Board Curriculum...',
  'Preparing Vector Chalkboard & Geometric Engine...',
  'Faculty Connected — Entering Classroom Stage',
]

export function ClassroomConnectingAnimation({
  stageText,
  connectionState,
  className = '',
}: ClassroomConnectingAnimationProps) {
  const containerRef = useRef<HTMLDivElement>(null)
  const [pointer, setPointer] = useState({ x: 0, y: 0 })
  const [spring, setSpring] = useState({ x: 0, y: 0 })
  const [currentStep, setCurrentStep] = useState(0)

  // Step progression timer
  useEffect(() => {
    if (connectionState === 'CONNECTED') {
      setCurrentStep(3)
      return
    }
    const interval = setInterval(() => {
      setCurrentStep((prev) => (prev < 2 ? prev + 1 : prev))
    }, 1200)
    return () => clearInterval(interval)
  }, [connectionState])

  // Mouse move handler for spring tilt
  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!containerRef.current) return
    const rect = containerRef.current.getBoundingClientRect()
    const rawX = (e.clientX - rect.left) / rect.width - 0.5
    const rawY = (e.clientY - rect.top) / rect.height - 0.5
    setPointer({ x: rawX * 18, y: rawY * 18 })
  }

  const handleMouseLeave = () => {
    setPointer({ x: 0, y: 0 })
  }

  // Smooth spring physics interpolation
  useEffect(() => {
    let animId: number
    const tick = () => {
      setSpring((prev) => ({
        x: prev.x + (pointer.x - prev.x) * 0.1,
        y: prev.y + (pointer.y - prev.y) * 0.1,
      }))
      animId = requestAnimationFrame(tick)
    }
    animId = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(animId)
  }, [pointer])

  const activeMessage = stageText || (connectionState === 'CONNECTED' ? STAGES[3] : STAGES[currentStep])

  return (
    <div
      ref={containerRef}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      className={`relative w-full h-full flex flex-col items-center justify-center p-6 bg-[#FAF8F4] select-none cursor-crosshair overflow-hidden ${className}`}
      aria-label="Classroom Connecting Stage"
    >
      {/* 30° Axonometric Hairline Vector Graphic */}
      <div
        className="w-full max-w-md flex flex-col items-center transition-transform duration-75 ease-out"
        style={{
          transform: `perspective(900px) rotateX(${-spring.y * 0.3}deg) rotateY(${spring.x * 0.35}deg)`,
        }}
      >
        <svg
          viewBox="0 0 600 320"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="w-full h-auto max-h-[220px] drop-shadow-xs"
        >
          <defs>
            <linearGradient id="hl-tablet-fill" x1="0" y1="0" x2="600" y2="320" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#FFFFFF" />
              <stop offset="100%" stopColor="#F4F1EA" />
            </linearGradient>
            <radialGradient id="hl-blue-pulse" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stopColor="#255D88" stopOpacity="0.25" />
              <stop offset="100%" stopColor="#1F3852" stopOpacity="0" />
            </radialGradient>
          </defs>

          {/* 30° Axonometric Grid Lines */}
          <g stroke="#E2E6EA" strokeWidth="1" strokeDasharray="3 4">
            <line x1="80" y1="160" x2="520" y2="160" />
            <line x1="120" y1="200" x2="480" y2="200" />
            <line x1="160" y1="240" x2="440" y2="240" />
            <path d="M 150 250 L 300 163 L 450 250" />
            <path d="M 210 250 L 300 198 L 390 250" />
          </g>

          {/* Subtle Ambient Radial Pulse */}
          <circle
            cx={300 + spring.x * 1.5}
            cy={165 + spring.y * 1.5}
            r="90"
            fill="url(#hl-blue-pulse)"
          />

          {/* Isometric Chalkboard Tablet (30° axonometric prism) */}
          <g transform={`translate(${spring.x * 0.5}, ${spring.y * 0.5})`}>
            {/* Tablet Shadow */}
            <path
              d="M 170 215 L 300 270 L 430 215 L 300 160 Z"
              fill="#E8E4D9"
              opacity="0.8"
            />
            {/* Tablet Body */}
            <path
              d="M 170 205 L 300 260 L 430 205 L 300 150 Z"
              fill="url(#hl-tablet-fill)"
              stroke="#CBD5E1"
              strokeWidth="1.5"
            />
            {/* Tablet Screen Face */}
            <path
              d="M 195 200 L 300 245 L 405 200 L 300 155 Z"
              fill="#13211B"
              stroke="#233930"
              strokeWidth="1"
            />
            {/* Chalkboard Hairline Accent Mark */}
            <path
              d="M 240 195 L 300 220 L 360 195"
              stroke="#68B084"
              strokeWidth="1.2"
              strokeLinecap="round"
              strokeDasharray="2 3"
            />
          </g>

          {/* Floating Drafting Compass & Vector Calibrator */}
          <g transform={`translate(${300 + spring.x * 1.2}, ${120 + spring.y * 1.2})`}>
            {/* Central Compass Hinge */}
            <circle cx="0" cy="0" r="5.5" fill="#1F3852" stroke="#255D88" strokeWidth="1.5" />
            {/* Compass Left Leg */}
            <line
              x1="-3"
              y1="4"
              x2="-24"
              y2="44"
              stroke="#1F3852"
              strokeWidth="2"
              strokeLinecap="round"
            />
            {/* Needle Point */}
            <circle cx="-24" cy="44" r="1.5" fill="#3B7CAE" />

            {/* Compass Right Leg with drafting lead */}
            <line
              x1="3"
              y1="4"
              x2="24"
              y2="44"
              stroke="#1F3852"
              strokeWidth="2"
              strokeLinecap="round"
            />
            {/* Drafting lead */}
            <circle cx="24" cy="44" r="2" fill="#255D88" />

            {/* Subtle rotating calibrator arc */}
            <path
              d="M -16 28 A 20 20 0 0 1 16 28"
              stroke="#3B7CAE"
              strokeWidth="1"
              strokeDasharray="2 2"
              fill="none"
            />
          </g>

          {/* Calibrating Laser Guides */}
          <line
            x1={276 + spring.x * 1.2}
            y1={164 + spring.y * 1.2}
            x2={300 + spring.x * 0.5}
            y2={195 + spring.y * 0.5}
            stroke="#255D88"
            strokeWidth="0.8"
            strokeDasharray="2 3"
            opacity="0.6"
          />
          <line
            x1={324 + spring.x * 1.2}
            y1={164 + spring.y * 1.2}
            x2={340 + spring.x * 0.5}
            y2={190 + spring.y * 0.5}
            stroke="#3B7CAE"
            strokeWidth="0.8"
            strokeDasharray="2 3"
            opacity="0.6"
          />
        </svg>

        {/* Dynamic Status Progress Indicator */}
        <div className="mt-4 flex flex-col items-center gap-2 text-center max-w-sm">
          {/* Progress Notches */}
          <div className="flex items-center gap-1.5">
            {[0, 1, 2, 3].map((step) => (
              <span
                key={step}
                className={`h-1.5 rounded-full transition-all duration-300 ${
                  step === currentStep
                    ? 'w-7 bg-[#1F3852]'
                    : step < currentStep
                    ? 'w-3 bg-[#255D88]'
                    : 'w-2 bg-[#CBD5E1]'
                }`}
              />
            ))}
          </div>

          <p className="text-xs sm:text-sm font-medium text-[#1F3852] animate-pulse">
            {activeMessage}
          </p>
          <span className="text-xs font-mono text-[#64748B]">
            Anaxly · Classes 6–12
          </span>
        </div>
      </div>
    </div>
  )
}

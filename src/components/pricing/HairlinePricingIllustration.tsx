'use client'

import React, { useRef, useState, useEffect } from 'react'

/**
 * Hairline Scholastic Socratic Illustration
 * Built adhering to @lucasmarkes/hairline geometric principles:
 * - Single-stroke axonometric projection (30° isometric angle)
 * - Rounded solids and precise geometric drafting instruments
 * - Responsive pointer tilt and dynamic focal anchor
 */
export function HairlineHeroIllustration() {
  const containerRef = useRef<HTMLDivElement>(null)
  const [pointer, setPointer] = useState({ x: 0, y: 0, active: false })
  const [spring, setSpring] = useState({ x: 0, y: 0 })

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!containerRef.current) return
    const rect = containerRef.current.getBoundingClientRect()
    const rawX = (e.clientX - rect.left) / rect.width - 0.5
    const rawY = (e.clientY - rect.top) / rect.height - 0.5
    setPointer({ x: rawX * 24, y: rawY * 24, active: true })
  }

  const handleMouseLeave = () => {
    setPointer({ x: 0, y: 0, active: false })
  }

  // Smooth spring physics interpolation
  useEffect(() => {
    let animId: number
    const tick = () => {
      setSpring((prev) => ({
        x: prev.x + (pointer.x - prev.x) * 0.12,
        y: prev.y + (pointer.y - prev.y) * 0.12,
      }))
      animId = requestAnimationFrame(tick)
    }
    animId = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(animId)
  }, [pointer])

  return (
    <div
      ref={containerRef}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      className="relative mx-auto w-full max-w-xl py-1 select-none cursor-crosshair"
      aria-label="Interactive Hairline scholastic illustration"
    >
      <div
        className="w-full flex justify-center items-center transition-transform duration-75 ease-out"
        style={{
          transform: `perspective(1000px) rotateX(${-spring.y * 0.35}deg) rotateY(${spring.x * 0.45}deg)`,
        }}
      >
        <svg
          viewBox="0 0 860 340"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="w-full h-auto max-h-[170px] sm:max-h-[190px] drop-shadow-xs"
        >
          <defs>
            <linearGradient id="hl-canvas-fade" x1="0" y1="0" x2="860" y2="340" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#FBF9F4" stopOpacity="0.8" />
              <stop offset="100%" stopColor="#F5F1E6" stopOpacity="0.4" />
            </linearGradient>
            <radialGradient id="hl-focus-glow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stopColor="#10B981" stopOpacity="0.18" />
              <stop offset="100%" stopColor="#10B981" stopOpacity="0" />
            </radialGradient>
          </defs>

          {/* Background drafting grid in 30° axonometry */}
          <g stroke="#E8E4D9" strokeWidth="1" opacity="0.75">
            {/* Isometric Horizontal Racks */}
            <line x1="120" y1="180" x2="740" y2="180" strokeDasharray="3 5" />
            <line x1="160" y1="220" x2="700" y2="220" strokeDasharray="3 5" />
            <line x1="200" y1="260" x2="660" y2="260" strokeDasharray="3 5" />

            {/* Diagonal Grid 30° / 150° */}
            <path d="M 220 280 L 430 158 L 640 280" />
            <path d="M 280 280 L 430 193 L 580 280" />
            <path d="M 340 280 L 430 228 L 520 280" />
          </g>

          {/* Focal Glow Anchor following pointer */}
          <circle
            cx={430 + spring.x * 3}
            cy={180 + spring.y * 3}
            r="110"
            fill="url(#hl-focus-glow)"
          />

          {/* 1. CENTRAL ELEMENT: Axonometric Digital Chalkboard Tablet */}
          <g id="hl-board">
            {/* Board Base Shadow */}
            <path
              d="M 240 230 L 430 310 L 620 230 L 430 150 Z"
              fill="#EFECE3"
              stroke="#D6D1C1"
              strokeWidth="1.25"
            />
            {/* Floating Display Slab */}
            <path
              d="M 240 222 L 430 302 L 620 222 L 430 142 Z"
              fill="#FAF8F3"
              stroke="#2D2A26"
              strokeWidth="1.75"
              strokeLinejoin="round"
            />
            {/* Bevel Edge */}
            <path d="M 240 222 L 240 230 L 430 310 L 430 302 Z" fill="#E4E0D2" stroke="#2D2A26" strokeWidth="1.25" />
            <path d="M 430 302 L 430 310 L 620 230 L 620 222 Z" fill="#DAD5C5" stroke="#2D2A26" strokeWidth="1.25" />

            {/* Coordinate Grid on Board Surface */}
            <g stroke="#3D5A46" strokeWidth="1.2" opacity="0.85">
              {/* Board Axes */}
              <line x1="310" y1="210" x2="550" y2="210" strokeDasharray="2 3" />
              <line x1="430" y1="165" x2="430" y2="280" strokeDasharray="2 3" />

              {/* Dynamic S-Curve / Harmonic Waveform on Board */}
              <path
                d={`M 320 225 Q 380 ${180 + spring.y * 0.5}, 430 210 T 540 ${195 - spring.y * 0.5}`}
                fill="none"
                stroke="#047857"
                strokeWidth="2"
                strokeLinecap="round"
              />

              {/* Peak Tangent Vectors */}
              <circle cx="375" cy="195" r="3.5" fill="#047857" />
              <line x1="355" y1="195" x2="395" y2="195" stroke="#047857" strokeWidth="1.5" />
              <circle cx="485" cy="225" r="3.5" fill="#047857" />
              <line x1="465" y1="225" x2="505" y2="225" stroke="#047857" strokeWidth="1.5" />
            </g>
          </g>

          {/* 2. LEFT ELEMENT: Scholastic Drafting Compass */}
          <g id="hl-compass" transform={`translate(${spring.x * 0.4}, ${spring.y * 0.3})`}>
            {/* Compass Shadow */}
            <ellipse cx="190" cy="245" rx="35" ry="12" fill="#E6E2D4" opacity="0.6" />

            {/* Compass Pivot Hinge */}
            <circle cx="190" cy="90" r="9" fill="#FAF8F3" stroke="#2D2A26" strokeWidth="1.75" />
            <circle cx="190" cy="90" r="3" fill="#2D2A26" />
            {/* Knurled Adjustment Thumbwheel */}
            <line x1="175" y1="135" x2="205" y2="135" stroke="#2D2A26" strokeWidth="2.5" strokeLinecap="round" />
            <circle cx="190" cy="135" r="4.5" fill="#FAF8F3" stroke="#2D2A26" strokeWidth="1.5" />

            {/* Left Leg with Needle Tip */}
            <polyline
              points="183,95 168,170 152,240"
              fill="none"
              stroke="#2D2A26"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
            {/* Needle point */}
            <line x1="152" y1="240" x2="150" y2="248" stroke="#2D2A26" strokeWidth="1.5" />

            {/* Right Leg with Graphite Lead Holder */}
            <polyline
              points="197,95 212,170 228,235"
              fill="none"
              stroke="#2D2A26"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
            {/* Lead sleeve & tip */}
            <rect
              x="224"
              y="235"
              width="8"
              height="10"
              rx="1.5"
              fill="#EAE5D6"
              stroke="#2D2A26"
              strokeWidth="1.5"
              transform="rotate(25 228 240)"
            />

            {/* Arc traced on paper */}
            <path
              d="M 152 248 A 45 18 0 0 1 236 244"
              fill="none"
              stroke="#B45309"
              strokeWidth="1.5"
              strokeDasharray="4 3"
            />
          </g>

          {/* 3. RIGHT ELEMENT: Real-Time Socratic Aperture & Optical Lens */}
          <g id="hl-aperture" transform={`translate(${-spring.x * 0.4}, ${spring.y * 0.3})`}>
            {/* Base Pedestal */}
            <ellipse cx="670" cy="245" rx="38" ry="14" fill="#E6E2D4" opacity="0.6" />
            <ellipse cx="670" cy="240" rx="36" ry="12" fill="#FAF8F3" stroke="#2D2A26" strokeWidth="1.5" />

            {/* Optical Ring Stand */}
            <line x1="670" y1="240" x2="670" y2="165" stroke="#2D2A26" strokeWidth="2.5" strokeLinecap="round" />
            <circle cx="670" cy="195" r="4" fill="#2D2A26" />

            {/* Floating Iris / Avatar Eye Ring in 3D Axonometry */}
            <g transform="translate(670, 130)">
              {/* Outer Housing Ring */}
              <ellipse cx="0" cy="0" rx="42" ry="42" fill="#FAF8F3" stroke="#2D2A26" strokeWidth="2" />
              <ellipse cx="0" cy="0" rx="34" ry="34" fill="#FAF8F3" stroke="#2D2A26" strokeWidth="1.25" strokeDasharray="3 3" />
              {/* Inner Lens Element */}
              <ellipse cx="0" cy="0" rx="20" ry="20" fill="#E6F4EA" stroke="#047857" strokeWidth="1.75" />
              <circle cx="-4" cy="-4" r="5" fill="#047857" opacity="0.9" />
              <circle cx="5" cy="5" r="2.5" fill="#047857" opacity="0.5" />

              {/* Radiating Socratic Wavefronts */}
              <path
                d="M 44 -15 A 48 48 0 0 1 44 15"
                fill="none"
                stroke="#047857"
                strokeWidth="1.5"
                strokeLinecap="round"
                opacity="0.8"
              />
              <path
                d="M 52 -24 A 58 58 0 0 1 52 24"
                fill="none"
                stroke="#047857"
                strokeWidth="1.5"
                strokeLinecap="round"
                opacity="0.5"
              />
              <path
                d="M 60 -32 A 68 68 0 0 1 60 32"
                fill="none"
                stroke="#047857"
                strokeWidth="1.5"
                strokeLinecap="round"
                opacity="0.3"
              />
            </g>
          </g>

          {/* 4. UPPER FLOATING LABELS & GEOMETRIC ANCHORS */}
          <g id="hl-details" stroke="#2D2A26" strokeWidth="1">
            {/* Top Right Astrolabe Ring */}
            <circle cx="760" cy="65" r="18" fill="none" stroke="#D5D0C2" strokeWidth="1.25" />
            <circle cx="760" cy="65" r="12" fill="none" stroke="#A8A29E" strokeWidth="1" strokeDasharray="2 2" />
            <line x1="742" y1="65" x2="778" y2="65" stroke="#A8A29E" />
            <line x1="760" y1="47" x2="760" y2="83" stroke="#A8A29E" />

            {/* Top Left Precision Ruler */}
            <g transform="translate(100, 50) rotate(-15)">
              <rect x="0" y="0" width="110" height="18" rx="2" fill="#FAF8F3" stroke="#2D2A26" strokeWidth="1.5" />
              {/* Tick Marks */}
              <line x1="15" y1="0" x2="15" y2="9" stroke="#2D2A26" strokeWidth="1.2" />
              <line x1="30" y1="0" x2="30" y2="12" stroke="#2D2A26" strokeWidth="1.5" />
              <line x1="45" y1="0" x2="45" y2="9" stroke="#2D2A26" strokeWidth="1.2" />
              <line x1="60" y1="0" x2="60" y2="12" stroke="#2D2A26" strokeWidth="1.5" />
              <line x1="75" y1="0" x2="75" y2="9" stroke="#2D2A26" strokeWidth="1.2" />
              <line x1="90" y1="0" x2="90" y2="12" stroke="#2D2A26" strokeWidth="1.5" />
              <line x1="105" y1="0" x2="105" y2="9" stroke="#2D2A26" strokeWidth="1.2" />
            </g>
          </g>
        </svg>
      </div>
    </div>
  )
}

/**
 * Miniature Hairline Crests for Individual Pricing Cards
 */
export function HairlineFreeCrest() {
  return (
    <svg viewBox="0 0 48 48" fill="none" className="w-10 h-10 text-stone-900" stroke="currentColor">
      {/* Drafting Compass & Arc */}
      <circle cx="24" cy="10" r="4" strokeWidth="1.5" fill="#FAF8F3" />
      <polyline points="21,14 16,36" strokeWidth="1.75" strokeLinecap="round" />
      <polyline points="27,14 32,36" strokeWidth="1.75" strokeLinecap="round" />
      <line x1="18" y1="24" x2="30" y2="24" strokeWidth="1.5" />
      <path d="M 12 38 A 20 8 0 0 0 36 38" strokeWidth="1.25" strokeDasharray="2 2" stroke="#059669" />
    </svg>
  )
}

export function HairlineScholarCrest() {
  return (
    <svg viewBox="0 0 48 48" fill="none" className="w-10 h-10 text-blue-900" stroke="currentColor">
      {/* Open Parchment Codex & Fountain Pen */}
      <path d="M 8 16 C 14 13, 20 16, 24 18 C 28 16, 34 13, 40 16 L 40 36 C 34 33, 28 36, 24 38 C 20 36, 14 33, 8 36 Z" strokeWidth="1.75" fill="#FAF8F3" strokeLinejoin="round" />
      <line x1="24" y1="18" x2="24" y2="38" strokeWidth="1.5" />
      {/* Ruled lines on pages */}
      <line x1="12" y1="22" x2="20" y2="24" strokeWidth="1" stroke="#2563EB" />
      <line x1="12" y1="27" x2="20" y2="29" strokeWidth="1" stroke="#2563EB" />
      <line x1="28" y1="24" x2="36" y2="22" strokeWidth="1" stroke="#2563EB" />
      <line x1="28" y1="29" x2="36" y2="27" strokeWidth="1" stroke="#2563EB" />
    </svg>
  )
}

export function HairlineTopperCrest() {
  return (
    <svg viewBox="0 0 48 48" fill="none" className="w-10 h-10 text-emerald-950" stroke="currentColor">
      {/* Photorealistic Iris & Radiating Wavefront */}
      <circle cx="22" cy="24" r="16" strokeWidth="1.75" fill="#FAF8F3" />
      <circle cx="22" cy="24" r="9" strokeWidth="1.5" stroke="#047857" fill="#ECFDF5" />
      <circle cx="20" cy="22" r="3.5" fill="#047857" />
      {/* Socratic Signal Arcs */}
      <path d="M 39 16 A 14 14 0 0 1 39 32" strokeWidth="1.75" stroke="#059669" strokeLinecap="round" />
      <path d="M 44 11 A 20 20 0 0 1 44 37" strokeWidth="1.5" stroke="#059669" strokeLinecap="round" opacity="0.6" />
    </svg>
  )
}

export function HairlineMasteryCrest() {
  return (
    <svg viewBox="0 0 48 48" fill="none" className="w-10 h-10 text-stone-950" stroke="currentColor">
      {/* Astrolabe Armillary Sphere & Vision Aperture */}
      <circle cx="24" cy="24" r="18" strokeWidth="1.75" fill="#FAF8F3" />
      <ellipse cx="24" cy="24" rx="18" ry="7" strokeWidth="1.5" stroke="#4F46E5" />
      <ellipse cx="24" cy="24" rx="7" ry="18" strokeWidth="1.5" stroke="#4F46E5" />
      <circle cx="24" cy="24" r="4.5" fill="#312E81" />
      <line x1="24" y1="3" x2="24" y2="45" strokeWidth="1.25" strokeDasharray="2 2" />
    </svg>
  )
}

'use client'

import React from 'react'
import { DrawnSvg, InkPath } from './DrawnSvg'

type IllustrationProps = { className?: string }

const accent = 'text-coral-primary'

/** Two overlapping speech bubbles: the Socratic back-and-forth. */
export function SpeechDialogue({ className = '' }: IllustrationProps) {
  return (
    <DrawnSvg className={className}>
      <InkPath range={[0, 0.5]} d="M30 50 C30 34 44 26 80 26 C116 26 130 34 130 56 C130 78 116 86 84 86 L60 86 L42 104 L46 84 C34 80 30 70 30 50 Z" />
      <InkPath range={[0.15, 0.4]} d="M52 50 L108 50 M52 64 L94 64" />
      <InkPath
        range={[0.35, 0.85]}
        className={accent}
        d="M170 120 C170 104 156 96 122 96 C88 96 74 104 74 126 C74 148 88 156 118 156 L142 156 L160 174 L156 154 C166 150 170 140 170 120 Z"
      />
      <InkPath range={[0.6, 0.95]} className={accent} d="M96 120 L150 120 M96 134 L132 134" />
      <InkPath range={[0.85, 1]} d="M150 40 C156 30 166 30 168 38 C170 46 160 48 160 56 M160 66 L160 67" />
    </DrawnSvg>
  )
}

/** A chalk slate with a derivation sketch and a boxed result. */
export function ChalkDerivation({ className = '' }: IllustrationProps) {
  return (
    <DrawnSvg className={className}>
      <InkPath range={[0, 0.35]} d="M20 36 L180 36 L180 150 L20 150 Z" />
      <InkPath range={[0.05, 0.35]} d="M70 150 L60 176 M130 150 L140 176" />
      {/* F = m a */}
      <InkPath range={[0.3, 0.5]} d="M38 58 L38 82 M38 58 L54 58 M38 70 L50 70 M64 66 L76 66 M64 74 L76 74 M86 82 L86 66 C86 60 96 60 96 66 L96 82 M96 66 C96 60 106 60 106 66 L106 82 M128 66 C116 62 114 82 126 82 C130 82 132 78 132 74 L132 66 L132 82" />
      {/* arrow */}
      <InkPath range={[0.5, 0.62]} className={accent} d="M60 96 C70 104 70 108 62 116 M62 116 L58 108 M62 116 L70 114" />
      {/* a = F / m, boxed */}
      <InkPath range={[0.62, 0.82]} d="M92 120 C80 116 78 134 90 134 C94 134 96 130 96 126 L96 118 L96 134 M106 124 L118 124 M106 130 L118 130 M130 110 L130 126 M130 110 L140 110 M130 118 L138 118 M126 129 L146 129 M132 134 L132 144 M132 136 C132 132 138 132 138 136 L138 144 M138 136 C138 132 144 132 144 136 L144 144" />
      <InkPath range={[0.82, 1]} className={accent} d="M74 104 L158 104 L158 150 L74 150" />
    </DrawnSvg>
  )
}

/** A sun, an elliptical orbit, and a travelling planet: everyday intuition. */
export function OrbitSketch({ className = '' }: IllustrationProps) {
  return (
    <DrawnSvg className={className}>
      <InkPath range={[0, 0.45]} d="M20 100 C20 60 60 40 100 40 C150 40 180 70 180 100 C180 130 150 160 100 160 C60 160 20 140 20 100 Z" />
      <InkPath range={[0.2, 0.45]} className={accent} d="M88 100 A12 12 0 1 0 112 100 A12 12 0 1 0 88 100 Z" />
      <InkPath range={[0.35, 0.55]} className={accent} d="M100 76 L100 70 M100 124 L100 130 M76 100 L70 100 M124 100 L130 100 M83 83 L79 79 M117 117 L121 121 M117 83 L121 79 M83 117 L79 121" />
      <InkPath range={[0.55, 0.75]} d="M160 64 A8 8 0 1 0 176 64 A8 8 0 1 0 160 64 Z" />
      <InkPath range={[0.7, 0.9]} strokeDasharray="4 5" d="M112 94 L160 68" />
      <InkPath range={[0.8, 1]} d="M178 82 C186 92 186 104 180 114 M180 114 L176 106 M180 114 L186 110" />
    </DrawnSvg>
  )
}

/** A prism splitting a ray into three: spatial clarity. */
export function PrismSketch({ className = '' }: IllustrationProps) {
  return (
    <DrawnSvg className={className}>
      <InkPath range={[0, 0.4]} d="M100 40 L150 140 L50 140 Z" />
      <InkPath range={[0.15, 0.4]} d="M100 40 L112 126 L150 140 M112 126 L50 140" strokeOpacity={0.45} />
      <InkPath range={[0.4, 0.6]} d="M10 110 L76 92" />
      <InkPath range={[0.6, 0.85]} d="M124 96 L192 74" />
      <InkPath range={[0.65, 0.9]} className={accent} d="M124 100 L192 104" />
      <InkPath range={[0.7, 0.95]} d="M124 104 L190 134" strokeOpacity={0.6} />
      <InkPath range={[0.85, 1]} d="M40 170 L160 170" strokeOpacity={0.4} />
    </DrawnSvg>
  )
}

/** A quill over a ruled page: preserved master notes. */
export function QuillNotes({ className = '' }: IllustrationProps) {
  return (
    <DrawnSvg className={className}>
      <InkPath range={[0, 0.35]} d="M36 30 L136 30 L150 44 L150 176 L36 176 Z M136 30 L136 44 L150 44" />
      <InkPath range={[0.2, 0.55]} d="M52 62 L132 62 M52 82 L120 82 M52 102 L128 102 M52 122 L100 122" strokeOpacity={0.55} />
      <InkPath range={[0.45, 0.6]} className={accent} d="M52 144 L96 144 L96 160 L52 160 Z" />
      <InkPath range={[0.5, 0.85]} d="M186 16 C150 30 124 70 112 128 C130 96 156 72 186 16 Z" />
      <InkPath range={[0.75, 0.95]} d="M186 16 C168 50 140 90 112 128" strokeOpacity={0.6} />
      <InkPath range={[0.9, 1]} className={accent} d="M112 128 L106 142" />
    </DrawnSvg>
  )
}

/** A fine rule drawn outward from a small centred diamond: section ornament. */
export function Ornament({ className = '' }: IllustrationProps) {
  return (
    <DrawnSvg viewBox="0 0 240 24" className={className} strokeWidth={1.1}>
      <InkPath range={[0, 0.35]} className={accent} d="M120 4 L128 12 L120 20 L112 12 Z" />
      <InkPath range={[0.3, 1]} d="M104 12 L20 12" />
      <InkPath range={[0.3, 1]} d="M136 12 L220 12" />
      <InkPath range={[0.75, 1]} d="M10 12 L11 12 M229 12 L230 12" strokeWidth={2.4} />
    </DrawnSvg>
  )
}

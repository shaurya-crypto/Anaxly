// Tiny event helper split out of Mascot.tsx so pages can nudge the mascot
// without bundling the avatar library + animation JSON.

export interface CompanionGuideDetail {
  targetSelector?: string
  targetElementId?: string
  message: string
  animation?: 'idle' | 'listening' | 'working' | 'excited' | 'suspicious' | 'laughing' | 'celebrate' | 'happy' | 'thinking' | 'curious' | string
  expression?: string
  mood?: 'normal' | 'suspicious' | 'warning' | 'celebrate' | 'thinking'
  autoDismissMs?: number
}

// Global helper to guide the mascot to any element on any page
export function triggerCompanionGuidance(detail: CompanionGuideDetail) {
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent('companion-guide', { detail }))
  }
}


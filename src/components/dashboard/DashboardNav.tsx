'use client'

import React from 'react'
import { cn } from '@/lib/utils'

export interface NavItem {
  id: string
  label: string
  /** Material Symbols icon name. */
  icon: string
  onSelect: () => void
  /** Shows a small status dot, e.g. the tutor is available. */
  badge?: string
}

interface DashboardNavProps {
  items: NavItem[]
  activeId: string
  ariaLabel: string
  className?: string
}

/** Single navigation list shared by the desktop sidebar and the mobile drawer. */
export function DashboardNav({ items, activeId, ariaLabel, className }: DashboardNavProps) {
  return (
    <nav aria-label={ariaLabel} className={cn('space-y-1', className)}>
      {items.map((item) => {
        const active = item.id === activeId
        return (
          <button
            key={item.id}
            type="button"
            onClick={item.onSelect}
            aria-current={active ? 'page' : undefined}
            className={cn(
              'flex min-h-11 w-full cursor-pointer items-center gap-3 rounded-lg px-3 py-2 text-left text-sm font-medium transition-colors',
              'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm focus-visible:ring-offset-2 focus-visible:ring-offset-canvas',
              active
                ? 'bg-accent-primary text-on-primary shadow-xs'
                : 'text-ink-secondary hover:bg-canvas-soft hover:text-ink-primary'
            )}
          >
            <span
              aria-hidden="true"
              className="material-symbols-outlined text-xl"
              style={{ fontVariationSettings: active ? '"FILL" 1' : '"FILL" 0' }}
            >
              {item.icon}
            </span>
            <span className="flex-1">{item.label}</span>
            {item.badge && (
              <span className="inline-flex items-center">
                <span className="h-2 w-2 rounded-full bg-accent-sage" aria-hidden="true" />
                <span className="sr-only">{item.badge}</span>
              </span>
            )}
          </button>
        )
      })}
    </nav>
  )
}

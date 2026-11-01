'use client'

import React, { useMemo, useState } from 'react'

interface ActivityRecord {
  completed_at?: string | null
}

interface DailyActivityChartProps {
  records: ActivityRecord[]
  days?: number
}

const dayKey = (d: Date) => `${d.getFullYear()}-${d.getMonth()}-${d.getDate()}`
const shortDate = (d: Date) => new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric' }).format(d)

/** Lessons completed per day, derived from existing progress records. Plain SVG, no chart library. */
export function DailyActivityChart({ records, days = 14 }: DailyActivityChartProps) {
  const [activeIndex, setActiveIndex] = useState<number | null>(null)

  const buckets = useMemo(() => {
    const today = new Date()
    const list = Array.from({ length: days }, (_, i) => {
      const date = new Date(today.getFullYear(), today.getMonth(), today.getDate() - (days - 1 - i))
      return { date, key: dayKey(date), count: 0 }
    })
    const index = new Map(list.map((b, i) => [b.key, i]))
    records.forEach((r) => {
      if (!r.completed_at) return
      const i = index.get(dayKey(new Date(r.completed_at)))
      if (i !== undefined) list[i].count += 1
    })
    return list
  }, [records, days])

  const total = buckets.reduce((sum, b) => sum + b.count, 0)
  const max = Math.max(1, ...buckets.map((b) => b.count))
  const shown = activeIndex === null ? null : buckets[activeIndex]

  const W = 320
  const H = 120
  const padTop = 8
  const padBottom = 4
  const slot = W / days
  const barW = slot * 0.62
  const plotH = H - padTop - padBottom

  return (
    <div className="space-y-3">
      <div className="flex min-h-5 items-baseline justify-between gap-2 text-sm">
        <span className="font-medium text-ink-primary">
          {shown ? `${shortDate(shown.date)}` : 'Last 14 days'}
        </span>
        <span className="tabular-nums text-ink-secondary" aria-live="polite">
          {shown
            ? `${shown.count} ${shown.count === 1 ? 'lesson' : 'lessons'}`
            : `${total} ${total === 1 ? 'lesson' : 'lessons'} completed`}
        </span>
      </div>

      <svg
        viewBox={`0 0 ${W} ${H}`}
        className="h-28 w-full"
        role="img"
        aria-label={`Lessons completed per day over the last ${days} days: ${total} in total.`}
        onMouseLeave={() => setActiveIndex(null)}
      >
        <line x1="0" x2={W} y1={H - padBottom} y2={H - padBottom} stroke="var(--border-subtle)" strokeWidth="1" />
        <line x1="0" x2={W} y1={padTop} y2={padTop} stroke="var(--border-subtle)" strokeWidth="1" strokeDasharray="3 4" />
        {buckets.map((b, i) => {
          const h = b.count === 0 ? 2 : Math.max(6, (b.count / max) * plotH)
          const x = i * slot + (slot - barW) / 2
          const isToday = i === days - 1
          return (
            <g key={b.key} onMouseEnter={() => setActiveIndex(i)}>
              <rect x={i * slot} y={0} width={slot} height={H} fill="transparent" />
              <rect
                x={x}
                y={H - padBottom - h}
                width={barW}
                height={h}
                rx="3"
                fill={b.count === 0 ? 'var(--border-strong)' : isToday ? 'var(--accent-primary)' : 'var(--accent-ochre)'}
                opacity={activeIndex === null || activeIndex === i ? 1 : 0.55}
              >
                <title>{`${shortDate(b.date)}: ${b.count} ${b.count === 1 ? 'lesson' : 'lessons'}`}</title>
              </rect>
            </g>
          )
        })}
      </svg>

      <div className="flex justify-between text-xs text-ink-muted">
        <span>{shortDate(buckets[0].date)}</span>
        <span>{shortDate(buckets[Math.floor(days / 2)].date)}</span>
        <span>Today</span>
      </div>

      {total === 0 && (
        <p className="text-sm text-ink-secondary">No lessons completed yet. Finish a capsule to start your chart.</p>
      )}
    </div>
  )
}

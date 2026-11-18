'use client'

import React, { useMemo, useState } from 'react'
import Link from 'next/link'

interface HistoryModule {
  id: string
  title: string
  curriculum_id?: string | null
  estimated_minutes?: number | null
}

interface HistoryProgress {
  syllabus_module_id: string
  status: string
  score?: number | null
  started_at?: string | null
  completed_at?: string | null
  chapter_notes?: string | null
}

interface HistoryCurriculum {
  id: string
  title: string
}

interface HistoryPanelProps {
  userId: string
  modules: HistoryModule[]
  progressRecords: HistoryProgress[]
  curriculums: HistoryCurriculum[]
  memories: { id: string; content?: string; memory_text?: string; created_at: string }[]
}

type Filter = 'all' | 'completed' | 'in_progress'

function dayLabel(d: Date) {
  const today = new Date()
  const y = new Date(today)
  y.setDate(today.getDate() - 1)
  if (d.toDateString() === today.toDateString()) return 'Today'
  if (d.toDateString() === y.toDateString()) return 'Yesterday'
  return d.toLocaleDateString(undefined, { weekday: 'long', day: 'numeric', month: 'long' })
}

/** Timeline of past lessons built from the student's progress records. */
export function HistoryPanel({ userId, modules, progressRecords, curriculums, memories }: HistoryPanelProps) {
  const [filter, setFilter] = useState<Filter>('all')

  const entries = useMemo(() => {
    const modById = new Map(modules.map((m) => [m.id, m]))
    const curById = new Map(curriculums.map((c) => [c.id, c.title]))
    return progressRecords
      .map((p) => {
        const mod = modById.get(p.syllabus_module_id)
        const when = p.completed_at || p.started_at
        if (!mod || !when) return null
        return {
          id: p.syllabus_module_id,
          title: mod.title,
          subject: (mod.curriculum_id && curById.get(mod.curriculum_id)) || '',
          minutes: mod.estimated_minutes || null,
          status: p.status === 'completed' || p.completed_at ? 'completed' : 'in_progress',
          score: p.score ?? null,
          hasNotes: !!p.chapter_notes,
          date: new Date(when),
        }
      })
      .filter((e): e is NonNullable<typeof e> => !!e)
      .sort((a, b) => b.date.getTime() - a.date.getTime())
  }, [modules, progressRecords, curriculums])

  const shown = entries.filter((e) => filter === 'all' || e.status === filter)
  const groups = shown.reduce<Record<string, typeof shown>>((acc, e) => {
    const k = dayLabel(e.date)
    ;(acc[k] ||= []).push(e)
    return acc
  }, {})

  const completed = entries.filter((e) => e.status === 'completed')
  const avgScore = completed.filter((e) => e.score !== null).length
    ? Math.round(completed.reduce((s, e) => s + (e.score || 0), 0) / completed.filter((e) => e.score !== null).length)
    : null

  return (
    <div className="space-y-8">
      <div className="grid grid-cols-3 gap-3">
        {[
          ['Lessons started', entries.length],
          ['Completed', completed.length],
          ['Average score', avgScore !== null ? `${avgScore}%` : '—'],
        ].map(([label, value]) => (
          <div key={label as string} className="rounded-2xl border border-border-subtle bg-surface p-4 shadow-xs">
            <p className="font-editorial text-3xl text-ink-primary">{value}</p>
            <p className="mt-1 text-xs text-ink-muted">{label}</p>
          </div>
        ))}
      </div>

      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="inline-flex rounded-xl border border-border-subtle bg-canvas-soft p-1">
          {(
            [
              ['all', 'All'],
              ['completed', 'Completed'],
              ['in_progress', 'In progress'],
            ] as [Filter, string][]
          ).map(([id, label]) => (
            <button
              key={id}
              type="button"
              onClick={() => setFilter(id)}
              className={`cursor-pointer rounded-lg px-3 py-1.5 text-xs font-medium transition-all ${
                filter === id ? 'bg-surface text-ink-primary shadow-xs' : 'text-ink-muted hover:text-ink-primary'
              }`}
            >
              {label}
            </button>
          ))}
        </div>
        <Link href={`/dashboard/${userId}/profile`} className="text-sm font-medium text-accent-warm hover:underline">
          All saved notes →
        </Link>
      </div>

      {shown.length === 0 ? (
        <div className="rounded-2xl border border-dashed border-border-subtle bg-surface py-16 text-center">
          <span className="material-symbols-outlined text-4xl text-ink-hairline">history</span>
          <p className="mt-2 text-sm text-ink-secondary">No lessons here yet.</p>
          <Link href={`/dashboard/${userId}/learn`} className="mt-3 inline-block text-sm font-medium text-accent-warm hover:underline">
            Start a lesson
          </Link>
        </div>
      ) : (
        <div className="space-y-8">
          {Object.entries(groups).map(([day, items]) => (
            <div key={day}>
              <p className="mb-3 text-xs font-semibold uppercase tracking-[0.14em] text-ink-muted">{day}</p>
              <ol className="relative space-y-3 border-l border-border-subtle pl-6">
                {items.map((e) => (
                  <li key={e.id} className="relative">
                    <span
                      className={`absolute -left-[31px] top-5 h-3 w-3 rounded-full ring-4 ring-canvas ${
                        e.status === 'completed' ? 'bg-accent-sage' : 'bg-accent-warm'
                      }`}
                    />
                    <div className="group flex flex-col gap-3 rounded-2xl border border-border-subtle bg-surface p-4 shadow-xs transition-all hover:-translate-y-0.5 hover:shadow-md sm:flex-row sm:items-center">
                      <div className="min-w-0 flex-1">
                        <p className="truncate text-sm font-semibold text-ink-primary">{e.title}</p>
                        <p className="mt-0.5 text-xs text-ink-muted">
                          {[e.subject, e.date.toLocaleTimeString(undefined, { hour: 'numeric', minute: '2-digit' }), e.minutes ? `${e.minutes} min` : null]
                            .filter(Boolean)
                            .join(' · ')}
                        </p>
                      </div>
                      <div className="flex items-center gap-2">
                        {e.score !== null && (
                          <span className="rounded-full bg-canvas-soft px-2.5 py-1 font-mono text-xs text-ink-secondary">{e.score}%</span>
                        )}
                        <span
                          className={`rounded-full px-2.5 py-1 text-xs font-medium ${
                            e.status === 'completed' ? 'bg-emerald-50 text-emerald-700' : 'bg-accent-warm-soft text-accent-warm'
                          }`}
                        >
                          {e.status === 'completed' ? 'Completed' : 'In progress'}
                        </span>
                        <Link
                          href={`/dashboard/${userId}/class/${e.id}`}
                          className="rounded-lg border border-border-subtle px-3 py-1.5 text-xs font-medium text-ink-primary transition-colors hover:bg-canvas-soft"
                        >
                          {e.status === 'completed' ? 'Review' : 'Resume'}
                        </Link>
                      </div>
                    </div>
                  </li>
                ))}
              </ol>
            </div>
          ))}
        </div>
      )}

      {memories.length > 0 && (
        <section>
          <h3 className="mb-3 font-editorial text-xl text-ink-primary">What your tutor remembers</h3>
          <div className="grid gap-3 sm:grid-cols-2">
            {memories.slice(0, 8).map((m) => (
              <div key={m.id} className="rounded-xl border border-border-subtle bg-surface p-3.5 text-sm text-ink-secondary">
                {m.content || m.memory_text}
                <p className="mt-1.5 text-[11px] text-ink-muted">{new Date(m.created_at).toLocaleDateString()}</p>
              </div>
            ))}
          </div>
        </section>
      )}
    </div>
  )
}

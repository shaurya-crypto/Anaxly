'use client'

import React from 'react'
import Link from 'next/link'
import { AlertCircle, ArrowRight, RotateCcw } from 'lucide-react'

interface Module {
  id: string
  curriculum_id: string
  order_index: number
  title: string
  description?: string | null
  key_concepts?: string[] | null
  estimated_minutes?: number | null
}

interface ProgressRecord {
  id: string
  syllabus_module_id: string
  status: 'not_started' | 'in_progress' | 'completed' | 'needs_review'
  score?: number | null
  completed_at?: string | null
}

interface WeakConceptsReviewCardProps {
  userId: string
  modules: Module[]
  progressRecords: ProgressRecord[]
  onModuleClick?: (e: React.MouseEvent, moduleId?: string) => void
}

export function WeakConceptsReviewCard({
  userId,
  modules,
  progressRecords,
  onModuleClick,
}: WeakConceptsReviewCardProps) {
  const progressMap = new Map<string, ProgressRecord>()
  progressRecords.forEach((p) => progressMap.set(p.syllabus_module_id, p))

  // 1. Identify modules needing review: status is 'needs_review' or score < 70
  const reviewNeededModules = modules.filter((m) => {
    const p = progressMap.get(m.id)
    if (!p) return false
    if (p.status === 'needs_review') return true
    if (typeof p.score === 'number' && p.score < 70) return true
    return false
  })

  // 2. Fallback: completed modules for spaced repetition if no explicitly flagged weak modules
  const candidateModules =
    reviewNeededModules.length > 0
      ? reviewNeededModules
      : modules.filter((m) => progressMap.get(m.id)?.status === 'completed').slice(0, 3)

  if (candidateModules.length === 0) {
    return null
  }

  const isExplicitWeakness = reviewNeededModules.length > 0

  return (
    <section className="bg-surface rounded-3xl border border-border-subtle p-7 md:p-8 shadow-soft space-y-5 w-full">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-border-subtle/80 pb-4">
        <div className="flex items-center gap-3">
          <div
            className={`w-9 h-9 rounded-xl border flex items-center justify-center shrink-0 ${
              isExplicitWeakness
                ? 'bg-amber-500/10 border-amber-500/25 text-amber-700'
                : 'bg-secondary/10 border-secondary/20 text-secondary'
            }`}
          >
            {isExplicitWeakness ? (
              <AlertCircle className="w-4 h-4 text-amber-700" />
            ) : (
              <RotateCcw className="w-4 h-4 text-secondary" />
            )}
          </div>
          <div>
            <h3 className="font-editorial text-2xl text-ink-primary leading-tight">
              {isExplicitWeakness ? 'Topics to revise' : 'Quick revision'}
            </h3>
            <p className="text-xs text-ink-secondary mt-0.5 leading-relaxed">
              {isExplicitWeakness
                ? 'Based on your quiz scores.'
                : 'Go over lessons you finished a while ago.'}
            </p>
          </div>
        </div>

      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {candidateModules.slice(0, 3).map((mod) => {
          const prog = progressMap.get(mod.id)
          const score = prog?.score
          const keyConcepts = mod.key_concepts || []

          return (
            <div
              key={mod.id}
              className="bg-canvas rounded-2xl border border-border-subtle p-4 flex flex-col justify-between space-y-3 hover:border-ink-muted transition-all"
            >
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-xs text-ink-muted font-medium">
                    Lesson {mod.order_index}
                  </span>
                  {typeof score === 'number' ? (
                    <span
                      className={`text-xs tabular-nums ${score < 70 ? 'text-amber-700' : 'text-ink-muted'}`}
                    >
                      Quiz {score}%
                    </span>
                  ) : (
                    <span className="text-xs font-semibold text-ink-muted">
                      Revise
                    </span>
                  )}
                </div>

                <h4 className="text-sm text-ink-primary font-semibold line-clamp-1">
                  {mod.title}
                </h4>

                {keyConcepts.length > 0 && (
                  <p className="truncate pt-1 text-xs text-ink-secondary">{keyConcepts.slice(0, 2).join(', ')}</p>
                )}
              </div>

              <Link
                href={`/dashboard/${userId}/class/${mod.id}`}
                onClick={(e) => onModuleClick?.(e, mod.id)}
                className="w-full inline-flex items-center justify-center gap-1.5 bg-surface hover:bg-canvas-soft text-ink-primary border border-border-subtle text-xs font-medium py-2 rounded-xl transition-all shadow-xs hover:border-ink-muted cursor-pointer"
              >
                <span>Revise</span>
                <ArrowRight className="w-3.5 h-3.5 text-primary" />
              </Link>
            </div>
          )
        })}
      </div>
    </section>
  )
}

'use client'

import React, { useState } from 'react'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import {
  Target,
  AlertTriangle,
  CheckCircle2,
  TrendingUp,
  Settings,
  ArrowRight,
} from 'lucide-react'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogFooter,
} from '@/components/ui/dialog'
import { Button } from '@/components/ui/button'
import { Label } from '@/components/ui/label'
import { Input } from '@/components/ui/input'
import { updateStudyPlanAction } from '@/app/dashboard/actions'

export interface StudyPlanData {
  id: string
  user_id: string
  target_exam_date: string
  daily_study_minutes: number
  target_curriculum_ids?: string[] | null
  plan_metadata?: Record<string, any> | null
  is_active: boolean
  created_at: string
  updated_at: string
}

interface StudyPlannerCardProps {
  userId: string
  studyPlan: StudyPlanData | null
  totalModulesCount: number
  completedModulesCount: number
  nextModuleId?: string | null
  onPlanUpdated?: () => void
  onModuleClick?: (e: React.MouseEvent, moduleId?: string) => void
}

export function StudyPlannerCard({
  userId,
  studyPlan,
  totalModulesCount,
  completedModulesCount,
  nextModuleId,
  onPlanUpdated,
  onModuleClick,
}: StudyPlannerCardProps) {
  const router = useRouter()
  const [modalOpen, setModalOpen] = useState(false)
  const [isSubmitting, setIsSubmitting] = useState(false)

  // Default target date: 60 days from now if not set
  const defaultTargetDate = (() => {
    if (studyPlan?.target_exam_date) return studyPlan.target_exam_date
    const d = new Date()
    d.setDate(d.getDate() + 60)
    return d.toISOString().split('T')[0]
  })()

  const [targetDateInput, setTargetDateInput] = useState(defaultTargetDate)
  const [dailyMinutesInput, setDailyMinutesInput] = useState(
    studyPlan?.daily_study_minutes || 45
  )

  // Live calculations
  const targetDate = studyPlan?.target_exam_date || defaultTargetDate
  const dailyStudyMinutes = studyPlan?.daily_study_minutes || 45

  const now = new Date()
  const examDate = new Date(targetDate)
  const diffTime = examDate.getTime() - now.getTime()
  const daysRemaining = Math.max(1, Math.ceil(diffTime / (1000 * 60 * 60 * 24)))

  const remainingCapsules = Math.max(0, totalModulesCount - completedModulesCount)
  const estimatedMinutesPerCapsule = 15
  const totalMinutesNeeded = remainingCapsules * estimatedMinutesPerCapsule
  const totalMinutesAvailable = daysRemaining * dailyStudyMinutes

  const dailyCapsuleCapacity = Math.max(1, Math.floor(dailyStudyMinutes / estimatedMinutesPerCapsule))
  const requiredCapsulesPerDay = Math.ceil(remainingCapsules / daysRemaining)
  const requiredMinutesPerDay = requiredCapsulesPerDay * estimatedMinutesPerCapsule

  const isOnTrack = totalMinutesAvailable >= totalMinutesNeeded
  const bufferDays = isOnTrack
    ? Math.max(0, Math.floor((totalMinutesAvailable - totalMinutesNeeded) / dailyStudyMinutes))
    : 0

  const percentComplete =
    totalModulesCount > 0
      ? Math.round((completedModulesCount / totalModulesCount) * 100)
      : 0

  const handleSavePlan = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsSubmitting(true)
    try {
      const res = await updateStudyPlanAction({
        targetExamDate: targetDateInput,
        dailyStudyMinutes: dailyMinutesInput,
      })
      if (res?.success) {
        setModalOpen(false)
        router.refresh()
        onPlanUpdated?.()
      }
    } catch (err) {
      console.error('Failed to update study plan:', err)
    } finally {
      setIsSubmitting(false)
    }
  }

  // Pre-calculated options for daily minutes
  const studyTimeOptions = [
    { minutes: 15, label: '15 min/day (1 capsule)', desc: 'Light pace' },
    { minutes: 30, label: '30 min/day (2 capsules)', desc: 'Steady cadence' },
    { minutes: 45, label: '45 min/day (3 capsules)', desc: 'Standard exam prep' },
    { minutes: 60, label: '60 min/day (4 capsules)', desc: 'Accelerated study' },
    { minutes: 90, label: '90 min/day (6 capsules)', desc: 'Intensive revision' },
  ]

  return (
    <section className="bg-surface rounded-3xl border border-border-subtle p-7 md:p-8 shadow-soft space-y-6 w-full">
      {/* Header Row */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-border-subtle/80 pb-5">
        <div className="flex items-center gap-3.5">
          <div className="w-10 h-10 rounded-xl bg-primary/10 border border-primary/20 flex items-center justify-center text-primary flex-shrink-0">
            <Target className="w-5 h-5 text-primary" />
          </div>
          <div>
            <div className="flex items-center gap-2.5">
              <h3 className="font-editorial text-2xl text-ink-primary leading-tight tracking-tight">
                Adaptive Exam Study Planner
              </h3>
              <span className="hidden sm:inline-flex px-2.5 py-0.5 rounded-full text-xs font-mono font-medium bg-primary/10 text-primary border border-primary/20">
                15-Min Dynamic Balancing
              </span>
            </div>
            <p className="text-sm text-ink-secondary mt-1 leading-relaxed">
              Dynamic syllabus distribution balancing remaining capsules against target exam countdown.
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2.5 self-start sm:self-center">
          <button
            type="button"
            onClick={() => setModalOpen(true)}
            className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-border-subtle bg-surface hover:bg-canvas-soft text-ink-primary text-xs font-medium transition-colors cursor-pointer shadow-xs"
          >
            <Settings className="w-3.5 h-3.5 text-ink-muted" />
            <span>Customize Schedule</span>
          </button>
        </div>
      </div>

      {/* Grid of Key Metrics */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Metric 1: Exam Countdown */}
        <div className="p-4 bg-canvas rounded-2xl border border-border-subtle flex flex-col justify-between">
          <span className="text-xs text-ink-muted font-medium block">
            Exam Countdown
          </span>
          <div className="mt-3">
            <div className="flex items-baseline gap-1.5">
              <span className="text-2xl font-semibold tabular-nums text-ink-primary tracking-tight leading-none">
                {daysRemaining}
              </span>
              <span className="text-xs font-mono text-primary font-medium">
                Days Left
              </span>
            </div>
            <p className="text-xs font-mono text-ink-secondary mt-1.5 leading-tight truncate">
              Target: {new Date(targetDate).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}
            </p>
          </div>
        </div>

        {/* Metric 2: Remaining Capsules */}
        <div className="p-4 bg-canvas rounded-2xl border border-border-subtle flex flex-col justify-between">
          <span className="text-xs text-ink-muted font-medium block">
            Remaining Capsules
          </span>
          <div className="mt-3">
            <div className="flex items-baseline gap-1.5">
              <span className="text-2xl font-semibold tabular-nums text-ink-primary tracking-tight leading-none">
                {remainingCapsules}
              </span>
              <span className="text-xs font-mono text-ink-muted font-medium">
                / {totalModulesCount} total
              </span>
            </div>
            <div className="w-full h-1.5 rounded-full bg-border-subtle overflow-hidden mt-2">
              <div
                className="h-full bg-secondary rounded-full transition-all duration-500 ease-out"
                style={{ width: `${percentComplete}%` }}
              />
            </div>
          </div>
        </div>

        {/* Metric 3: Daily Target Pace */}
        <div className="p-4 bg-canvas rounded-2xl border border-border-subtle flex flex-col justify-between">
          <span className="text-xs text-ink-muted font-medium block">
            Daily Study Budget
          </span>
          <div className="mt-3">
            <div className="flex items-baseline gap-1.5">
              <span className="text-2xl font-semibold tabular-nums text-ink-primary tracking-tight leading-none">
                {dailyStudyMinutes}
              </span>
              <span className="text-xs font-mono text-ink-muted font-medium">
                min/day
              </span>
            </div>
            <p className="text-xs text-secondary mt-1.5 leading-tight font-medium">
              {dailyCapsuleCapacity} capsule{dailyCapsuleCapacity > 1 ? 's' : ''} per session
            </p>
          </div>
        </div>

        {/* Metric 4: Feasibility Status */}
        <div className="p-4 bg-canvas rounded-2xl border border-border-subtle flex flex-col justify-between">
          <span className="text-xs text-ink-muted font-medium block">
            Pacing Health
          </span>
          <div className="mt-3">
            <div className="flex items-center gap-1.5">
              {isOnTrack ? (
                <>
                  <CheckCircle2 className="w-5 h-5 text-accent-sage shrink-0" />
                  <span className="text-sm font-semibold text-accent-sage">
                    On Schedule
                  </span>
                </>
              ) : (
                <>
                  <AlertTriangle className="w-5 h-5 text-amber-600 shrink-0" />
                  <span className="text-sm font-semibold text-amber-700">
                    Pacing Warning
                  </span>
                </>
              )}
            </div>
            <p className="text-xs text-ink-secondary mt-1.5 leading-tight">
              {isOnTrack
                ? `${bufferDays} buffer days before exam`
                : `Need ${requiredMinutesPerDay} min/day to finish`}
            </p>
          </div>
        </div>
      </div>

      {/* Adaptive Rebalancing Callout Banner */}
      <div
        className={`p-4 rounded-2xl border transition-all ${
          isOnTrack
            ? 'bg-accent-sage-soft/70 border-accent-sage-border text-ink-primary'
            : 'bg-amber-50 border-amber-200 text-amber-950'
        }`}
      >
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-start gap-3">
            {isOnTrack ? (
              <TrendingUp className="w-5 h-5 text-accent-sage shrink-0 mt-0.5" />
            ) : (
              <AlertTriangle className="w-5 h-5 text-amber-600 shrink-0 mt-0.5" />
            )}
            <div>
              <h4 className="text-sm font-semibold text-ink-primary">
                {isOnTrack ? 'Cadence Health: Optimal' : 'Adaptive Rebalance Alert: Time Deficit Detected'}
              </h4>
              <p className="text-xs text-ink-secondary mt-0.5 leading-relaxed">
                {isOnTrack
                  ? `At your current pace of ${dailyStudyMinutes} min/day (${dailyCapsuleCapacity} capsule${
                      dailyCapsuleCapacity > 1 ? 's' : ''
                    }), you will finish the ${remainingCapsules} remaining capsules comfortably ${bufferDays} days prior to exam day.`
                  : `You have ${remainingCapsules} capsules remaining (${totalMinutesNeeded} min) across ${daysRemaining} days. At ${dailyStudyMinutes} min/day, you will complete only ${Math.floor(
                      totalMinutesAvailable / estimatedMinutesPerCapsule
                    )} capsules. Recommended target: Increase to ${requiredMinutesPerDay} min/day (${requiredCapsulesPerDay} capsules/day) or prioritize weak concepts.`}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2 shrink-0">
            {nextModuleId && (
              <Link
                href={`/dashboard/${userId}/class/${nextModuleId}`}
                onClick={(e) => onModuleClick?.(e, nextModuleId)}
                className="inline-flex items-center gap-1.5 bg-primary hover:bg-accent-primary-hover text-white text-xs font-medium px-4 py-2 rounded-xl transition-colors shadow-xs"
              >
                <span>Start Today's Capsule</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </Link>
            )}
          </div>
        </div>
      </div>

      {/* Customize Schedule Dialog */}
      <Dialog open={modalOpen} onOpenChange={setModalOpen}>
        <DialogContent className="sm:max-w-[480px] bg-surface border border-border-subtle rounded-2xl p-6 text-ink-primary shadow-xl">
          <DialogHeader>
            <DialogTitle className="font-editorial text-2xl text-ink-primary">
              Customize Study Schedule
            </DialogTitle>
            <DialogDescription className="text-xs text-ink-secondary">
              Set your target exam date and daily study budget. The adaptive engine will recalculate daily capsule goals.
            </DialogDescription>
          </DialogHeader>

          <form onSubmit={handleSavePlan} className="space-y-4 pt-2">
            <div className="space-y-1.5">
              <Label htmlFor="exam-date" className="text-xs font-semibold text-ink-primary">
                Target Examination Date
              </Label>
              <Input
                id="exam-date"
                type="date"
                autoComplete="off"
                value={targetDateInput}
                onChange={(e) => setTargetDateInput(e.target.value)}
                min={new Date().toISOString().split('T')[0]}
                className="bg-canvas border-border-subtle rounded-xl text-xs h-10"
                required
              />
            </div>

            <div className="space-y-1.5">
              <Label className="text-xs font-semibold text-ink-primary">
                Daily Study Budget (Minutes)
              </Label>
              <div className="grid grid-cols-1 gap-2">
                {studyTimeOptions.map((opt) => (
                  <button
                    key={opt.minutes}
                    type="button"
                    onClick={() => setDailyMinutesInput(opt.minutes)}
                    className={`flex items-center justify-between p-3 rounded-xl border text-xs text-left transition-all cursor-pointer ${
                      dailyMinutesInput === opt.minutes
                        ? 'bg-accent-primary-soft border-primary text-primary font-semibold'
                        : 'bg-canvas border-border-subtle text-ink-secondary hover:border-ink-muted'
                    }`}
                  >
                    <div>
                      <p className="font-medium text-ink-primary">{opt.label}</p>
                      <p className="text-[11px] text-ink-muted">{opt.desc}</p>
                    </div>
                    {dailyMinutesInput === opt.minutes && (
                      <CheckCircle2 className="w-4 h-4 text-primary shrink-0" />
                    )}
                  </button>
                ))}
              </div>
            </div>

            <DialogFooter className="pt-3 border-t border-border-subtle/80 flex items-center justify-end gap-2">
              <Button
                type="button"
                variant="ghost"
                onClick={() => setModalOpen(false)}
                className="text-xs rounded-xl"
              >
                Cancel
              </Button>
              <Button
                type="submit"
                disabled={isSubmitting}
                className="bg-primary hover:bg-accent-hover text-white text-xs rounded-xl px-5"
              >
                {isSubmitting ? 'Saving...' : 'Save & Rebalance'}
              </Button>
            </DialogFooter>
          </form>
        </DialogContent>
      </Dialog>
    </section>
  )
}

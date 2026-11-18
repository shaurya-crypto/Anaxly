'use client'

import React, { useState, useEffect, useMemo } from 'react'
import Link from 'next/link'
import { useRouter, useSearchParams } from 'next/navigation'
import {
  User, Sparkles, Check, RotateCcw, LogOut, ArrowLeft, Shield, Video, VideoOff, CheckCircle2, AlertCircle,
  Target, CreditCard, Volume2, GraduationCap, Bell, Palette, Keyboard, Search, Mail, Loader2, KeyRound,
  Eye, EyeOff, NotebookPen, Users, MonitorSmartphone, CalendarClock, ExternalLink, Lock, Download, Trash2, AlertTriangle,
} from 'lucide-react'
import {
  updateAccountAction,
  updateTeachingStyleAction,
  updateGeneralSettingsAction,
  updatePasswordAction,
  updateAvatarPreferenceAction,
  updateStudyPlanAction,
  signOutAction,
  signOutEverywhereAction,
  switchAccountAction,
  exportMyDataAction,
} from '@/app/dashboard/actions'
import { VOICE_OPTIONS } from '@/lib/voiceAndLanguageConfig'
import { Subscription, SUBSCRIPTION_PLANS } from '@/lib/types/subscription'


export interface PrebuiltAvatar {
  id: string
  name: string
  title: string
  subject: string
  description: string
  image: string
  badge: string
  recommendedBoard: string
  engine: string
}

export const PREBUILT_AVATARS: PrebuiltAvatar[] = [
  {
    id: '80459b57-2d66-4ca7-8682-59e1c649bc53',
    name: 'Prof. Vikram Raman',
    title: 'Senior Academician & Physics Specialist',
    subject: 'Physics, Mechanics & Advanced Numericals',
    description:
      'Rigorous 6-stage Socratic problem solving, comprehensive board numerical breakdowns (Given -> Formula -> Substitution -> Boxed Answer), and clear physical intuition.',
    image: '/avatars/80459b57-2d66-4ca7-8682-59e1c649bc53.jpg',
    badge: 'Primary Default',
    recommendedBoard: 'CBSE & ICSE Classes 9-12',
    engine: 'Simli Ultra-Fast WebRTC',
  },
  {
    id: 'a6d08e06-038a-4b32-84ae-b02e0f0f1140',
    name: 'Prof. Marcus Chen',
    title: 'Senior Mathematics & Applied Science Fellow',
    subject: 'Mathematics, Coordinate Geometry & Calculus',
    description:
      'First-principles proofs, geometric interpretation of limits and derivatives, trigonometric identities, and algebraic symmetry.',
    image: '/avatars/a6d08e06-038a-4b32-84ae-b02e0f0f1140.jpg',
    badge: 'Available Free',
    recommendedBoard: 'CBSE & IB Mathematics',
    engine: 'Simli Ultra-Fast WebRTC',
  },
  {
    id: '20cfe7d7-cfd7-43ee-9301-72a7c7056eaf',
    name: 'Dr. Elena Rostova',
    title: 'Atomic Chemistry & Thermodynamics Fellow',
    subject: 'Chemistry, Stoichiometry & Chemical Bonding',
    description:
      'Deep experimental intuition, precise definitions of chemical phenomena, stoichiometry, reaction mechanisms, and foundational atomic theory.',
    image: '/avatars/20cfe7d7-cfd7-43ee-9301-72a7c7056eaf.jpg',
    badge: 'Available Free',
    recommendedBoard: 'ICSE & IB Chemistry',
    engine: 'Simli Ultra-Fast WebRTC',
  },
  {
    id: 'd9c96b08-b2ca-48ef-b458-5c4471d9fe09',
    name: 'Prof. Sarah Jenkins',
    title: 'Life Sciences & Cellular Biology Mentor',
    subject: 'Biology, Physiological Cycles & Biochemistry',
    description:
      'Dynamic physical visualization of biological cycles, genetics, cellular respiration, and organ system interaction with clinical precision.',
    image: '/avatars/d9c96b08-b2ca-48ef-b458-5c4471d9fe09.jpg',
    badge: 'Available Free',
    recommendedBoard: 'CBSE & ICSE Classes 9-12',
    engine: 'Simli Ultra-Fast WebRTC',
  },
]



export const BOARD_OPTIONS = [
  {
    id: 'CBSE',
    name: 'CBSE (Central Board of Secondary Education)',
    desc: 'NCERT standard, step-by-step derivations, 50% NEP-2020 competency questions, no calculators.',
  },
  {
    id: 'ICSE',
    name: 'ICSE / ISC (Council for the Indian School Certificate)',
    desc: 'Verbatim textbook definitions, dual-column rough work margin, Selina Concise & Morning Star alignment.',
  },
  {
    id: 'IB',
    name: 'IB (International Baccalaureate - Coming Soon)',
    desc: 'Coming Soon - Statement of Inquiry (SOI), official IB command terms, measurement uncertainty.',
    disabled: true,
  },
]

export const CLASS_LEVEL_OPTIONS = [
  { id: 'class_6', label: 'Class 6' },
  { id: 'class_7', label: 'Class 7' },
  { id: 'class_8', label: 'Class 8' },
  { id: 'class_9', label: 'Class 9' },
  { id: 'class_10', label: 'Class 10' },
  { id: 'class_11', label: 'Class 11' },
  { id: 'class_12', label: 'Class 12' },
]

// ---------------------------------------------------------------------------
// Local (device) preferences — things the server profile has no column for.
// ---------------------------------------------------------------------------
export const LOCAL_PREFS_KEY = 'anaxly_prefs'

export interface LocalPrefs {
  speechRate: string
  autoListen: boolean
  captions: boolean
  soundEffects: boolean
  noteDensity: string
  hintLevel: string
  language: string
  reminders: boolean
  reminderTime: string
  streakAlerts: boolean
  weeklyReport: boolean
  productNews: boolean
  textSize: 'sm' | 'md' | 'lg'
  reduceMotion: boolean
  highContrast: boolean
  dyslexiaFont: boolean
  mascot: boolean
}

const DEFAULT_PREFS: LocalPrefs = {
  speechRate: '1.0',
  autoListen: true,
  captions: true,
  soundEffects: true,
  noteDensity: 'topper_detailed',
  hintLevel: 'balanced',
  language: 'en-IN',
  reminders: false,
  reminderTime: '18:00',
  streakAlerts: true,
  weeklyReport: true,
  productNews: false,
  textSize: 'md',
  reduceMotion: false,
  highContrast: false,
  dyslexiaFont: false,
  mascot: true,
}

export function readLocalPrefs(): LocalPrefs {
  try {
    const raw = localStorage.getItem(LOCAL_PREFS_KEY)
    return raw ? { ...DEFAULT_PREFS, ...JSON.parse(raw) } : DEFAULT_PREFS
  } catch {
    return DEFAULT_PREFS
  }
}

function applyAppearance(p: LocalPrefs) {
  const root = document.documentElement
  root.style.fontSize = p.textSize === 'sm' ? '15px' : p.textSize === 'lg' ? '17.5px' : ''
  root.classList.toggle('reduce-motion', p.reduceMotion)
  root.classList.toggle('high-contrast', p.highContrast)
  root.classList.toggle('dyslexia-font', p.dyslexiaFont)
}

interface SettingsViewProps {
  user: { id: string; email?: string; createdAt?: string; lastSignIn?: string; provider?: string }
  profile: any
  studyPlan?: { target_exam_date?: string | null; daily_study_minutes?: number | null } | null
  subscription?: Subscription | null
}

type TabType =
  | 'account'
  | 'avatars'
  | 'audio'
  | 'teaching'
  | 'goals'
  | 'notifications'
  | 'appearance'
  | 'billing'
  | 'privacy'
  | 'shortcuts'

const TABS: { id: TabType; label: string; icon: React.ElementType; group: string; desc: string }[] = [
  { id: 'account', label: 'Account', icon: User, group: 'You', desc: 'Name, class, board, password and sessions.' },
  { id: 'goals', label: 'Study goals', icon: Target, group: 'You', desc: 'Exam date and daily study target.' },
  { id: 'billing', label: 'Billing & plan', icon: CreditCard, group: 'You', desc: 'Your plan, usage and entitlements.' },
  { id: 'avatars', label: 'Tutor avatar', icon: Sparkles, group: 'Classroom', desc: 'Choose who teaches you live.' },
  { id: 'audio', label: 'Voice & audio', icon: Volume2, group: 'Classroom', desc: 'Voice, speed, listening and captions.' },
  { id: 'teaching', label: 'Teaching style', icon: GraduationCap, group: 'Classroom', desc: 'Method, pacing, hints and notes.' },
  { id: 'notifications', label: 'Notifications', icon: Bell, group: 'App', desc: 'Reminders, streaks and reports.' },
  { id: 'appearance', label: 'Appearance', icon: Palette, group: 'App', desc: 'Text size, motion and accessibility.' },
  { id: 'shortcuts', label: 'Shortcuts', icon: Keyboard, group: 'App', desc: 'Keyboard shortcuts in the classroom.' },
  { id: 'privacy', label: 'Privacy & data', icon: Shield, group: 'App', desc: 'Export data, clear cache, danger zone.' },
]

// ---------------------------------------------------------------------------
// Small UI primitives
// ---------------------------------------------------------------------------
function Section({ title, desc, children, action }: { title: string; desc?: string; children: React.ReactNode; action?: React.ReactNode }) {
  return (
    <section className="rounded-2xl border border-border-subtle bg-surface shadow-xs transition-shadow hover:shadow-sm">
      <div className="flex items-start justify-between gap-4 border-b border-border-subtle px-5 py-4 sm:px-6">
        <div>
          <h3 className="font-editorial text-lg text-ink-primary">{title}</h3>
          {desc && <p className="mt-0.5 text-xs text-ink-muted">{desc}</p>}
        </div>
        {action}
      </div>
      <div className="divide-y divide-border-subtle">{children}</div>
    </section>
  )
}

function Row({ label, desc, children }: { label: string; desc?: string; children: React.ReactNode }) {
  return (
    <div className="flex flex-col gap-3 px-5 py-4 sm:flex-row sm:items-center sm:justify-between sm:px-6">
      <div className="min-w-0 sm:max-w-[60%]">
        <p className="text-sm font-medium text-ink-primary">{label}</p>
        {desc && <p className="mt-0.5 text-xs leading-relaxed text-ink-muted">{desc}</p>}
      </div>
      <div className="shrink-0">{children}</div>
    </div>
  )
}

function Toggle({ checked, onChange, label }: { checked: boolean; onChange: (v: boolean) => void; label: string }) {
  return (
    <button
      type="button"
      role="switch"
      aria-checked={checked}
      aria-label={label}
      onClick={() => onChange(!checked)}
      className={`relative inline-flex h-6 w-11 cursor-pointer items-center rounded-full transition-colors duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm focus-visible:ring-offset-2 ${
        checked ? 'bg-accent-warm' : 'bg-surface-container-highest'
      }`}
    >
      <span
        className={`inline-block h-5 w-5 rounded-full bg-white shadow-sm transition-transform duration-200 ${
          checked ? 'translate-x-[22px]' : 'translate-x-0.5'
        }`}
      />
    </button>
  )
}

function Segmented<T extends string>({ value, onChange, options }: { value: T; onChange: (v: T) => void; options: { id: T; label: string }[] }) {
  return (
    <div className="inline-flex rounded-xl border border-border-subtle bg-canvas-soft p-1">
      {options.map((o) => (
        <button
          key={o.id}
          type="button"
          onClick={() => onChange(o.id)}
          className={`cursor-pointer rounded-lg px-3 py-1.5 text-xs font-medium transition-all ${
            value === o.id ? 'bg-surface text-ink-primary shadow-xs' : 'text-ink-muted hover:text-ink-primary'
          }`}
        >
          {o.label}
        </button>
      ))}
    </div>
  )
}

function ChoiceCard({ active, onClick, title, desc, badge }: { active: boolean; onClick: () => void; title: string; desc: string; badge?: string }) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={`group relative w-full cursor-pointer rounded-xl border p-4 text-left transition-all ${
        active
          ? 'border-accent-warm bg-accent-warm-soft ring-1 ring-accent-warm/30'
          : 'border-border-subtle bg-surface hover:-translate-y-0.5 hover:border-accent-warm-border hover:shadow-sm'
      }`}
    >
      <div className="flex items-center justify-between gap-2">
        <span className="text-sm font-semibold text-ink-primary">{title}</span>
        {badge && <span className="rounded-full bg-accent-warm/10 px-2 py-0.5 text-[10px] font-semibold text-accent-warm">{badge}</span>}
        <span
          className={`flex h-5 w-5 shrink-0 items-center justify-center rounded-full border transition-colors ${
            active ? 'border-accent-warm bg-accent-warm text-white' : 'border-border-subtle'
          }`}
        >
          {active && <Check className="h-3 w-3" />}
        </span>
      </div>
      <p className="mt-1.5 text-xs leading-relaxed text-ink-muted">{desc}</p>
    </button>
  )
}

const inputClass =
  'w-full rounded-xl border border-border-subtle bg-surface px-3.5 py-2.5 text-sm text-ink-primary transition-shadow placeholder:text-ink-hairline focus:border-accent-warm focus:outline-none focus:ring-4 focus:ring-accent-warm/10 disabled:cursor-not-allowed disabled:bg-canvas-soft disabled:text-ink-muted'
const primaryBtn =
  'inline-flex cursor-pointer items-center gap-2 rounded-xl bg-accent-warm px-4 py-2 text-sm font-medium text-white shadow-xs transition-all hover:bg-accent-warm-hover active:scale-[0.98] disabled:cursor-not-allowed disabled:opacity-50'
const ghostBtn =
  'inline-flex cursor-pointer items-center gap-2 rounded-xl border border-border-subtle bg-surface px-3.5 py-2 text-sm font-medium text-ink-primary transition-colors hover:bg-canvas-soft disabled:opacity-50'

function passwordStrength(pw: string) {
  let s = 0
  if (pw.length >= 8) s++
  if (/[A-Z]/.test(pw) && /[a-z]/.test(pw)) s++
  if (/\d/.test(pw)) s++
  if (/[^A-Za-z0-9]/.test(pw)) s++
  return s
}

// ---------------------------------------------------------------------------
// Main view
// ---------------------------------------------------------------------------
export function SettingsView({ user, profile, studyPlan = null, subscription = null }: SettingsViewProps) {
  const router = useRouter()
  const searchParams = useSearchParams()
  const paramTab = searchParams.get('tab') as TabType | null
  const [activeTab, setActiveTab] = useState<TabType>(
    paramTab && TABS.some((t) => t.id === paramTab) ? paramTab : 'account'
  )
  const [query, setQuery] = useState('')
  const [toast, setToast] = useState<{ type: 'success' | 'error'; message: string } | null>(null)
  const [busy, setBusy] = useState<string | null>(null)

  // Server-backed
  const [selectedAvatarId, setSelectedAvatarId] = useState<string>(profile?.selected_avatar_id || PREBUILT_AVATARS[0].id)
  const [fullName, setFullName] = useState<string>(profile?.full_name || '')
  const [classLevel, setClassLevel] = useState<string>(profile?.class_level || 'Class 10')
  const [targetBoard, setTargetBoard] = useState<string>(profile?.target_board || 'CBSE')
  const [newPassword, setNewPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [showPw, setShowPw] = useState(false)
  const [preferredVoice, setPreferredVoice] = useState<string>(profile?.preferred_teacher_voice || 'Leda')
  const [learningStyle, setLearningStyle] = useState<string>(profile?.learning_style || 'socratic')
  const [preferredPacing, setPreferredPacing] = useState<string>(profile?.preferred_pacing || 'normal')
  const [examDate, setExamDate] = useState<string>(studyPlan?.target_exam_date?.slice(0, 10) || '')
  const [dailyMinutes, setDailyMinutes] = useState<number>(studyPlan?.daily_study_minutes || 45)
  const [deleteConfirm, setDeleteConfirm] = useState('')

  // Device-local
  const [prefs, setPrefs] = useState<LocalPrefs>(DEFAULT_PREFS)
  useEffect(() => {
    const p = readLocalPrefs()
    setPrefs(p)
    applyAppearance(p)
    try {
      const storedFaceId = localStorage.getItem('ai_tutor_selected_face_id')
      if (storedFaceId && storedFaceId.length > 5) setSelectedAvatarId(storedFaceId)
    } catch {}
  }, [])

  const setPref = <K extends keyof LocalPrefs>(key: K, value: LocalPrefs[K]) => {
    setPrefs((prev) => {
      const next = { ...prev, [key]: value }
      try {
        localStorage.setItem(LOCAL_PREFS_KEY, JSON.stringify(next))
      } catch {}
      applyAppearance(next)
      return next
    })
    flash('success', 'Saved on this device')
  }

  useEffect(() => {
    if (paramTab && TABS.some((t) => t.id === paramTab)) setActiveTab(paramTab)
  }, [paramTab])

  const flash = (type: 'success' | 'error', message: string) => {
    setToast({ type, message })
    window.clearTimeout((flash as any)._t)
    ;(flash as any)._t = window.setTimeout(() => setToast(null), 2600)
  }

  const go = (tab: TabType) => {
    setActiveTab(tab)
    router.replace(`/dashboard/${user.id}/settings?tab=${tab}`, { scroll: false })
  }

  const run = async (key: string, fn: () => Promise<{ error?: string } | any>, ok: string) => {
    setBusy(key)
    try {
      const res = await fn()
      if (res?.error) flash('error', res.error)
      else flash('success', ok)
      return res
    } catch (e: any) {
      flash('error', e?.message || 'Something went wrong')
    } finally {
      setBusy(null)
    }
  }

  // Plan / usage
  const tier = subscription?.plan_tier || profile?.subscription_tier || 'free'
  const plan = SUBSCRIPTION_PLANS[tier as keyof typeof SUBSCRIPTION_PLANS] || SUBSCRIPTION_PLANS.free
  const classesLimit = subscription?.monthly_classes_limit ?? plan.monthlyClassesLimit
  const classesUsed = subscription?.monthly_classes_used ?? 0
  const usagePct = classesLimit > 0 ? Math.min(100, Math.round((classesUsed / classesLimit) * 100)) : 0

  const activeAvatar = PREBUILT_AVATARS.find((a) => a.id === selectedAvatarId) || PREBUILT_AVATARS[0]
  const strength = passwordStrength(newPassword)
  const daysToExam = examDate ? Math.ceil((new Date(examDate).getTime() - Date.now()) / 86400000) : null

  const filteredTabs = useMemo(() => {
    const q = query.trim().toLowerCase()
    if (!q) return TABS
    return TABS.filter((t) => (t.label + ' ' + t.desc).toLowerCase().includes(q))
  }, [query])
  const groups = Array.from(new Set(filteredTabs.map((t) => t.group)))
  const current = TABS.find((t) => t.id === activeTab)!

  const handleSelectAvatar = async (avatar: PrebuiltAvatar) => {
    setSelectedAvatarId(avatar.id)
    try {
      localStorage.setItem('ai_tutor_selected_face_id', avatar.id)
      localStorage.setItem('ai_tutor_avatar_preview', avatar.image)
      localStorage.removeItem('ai_tutor_avatar_config')
    } catch {}
    await run('avatar', () => updateAvatarPreferenceAction({ avatarId: avatar.id, avatarUrl: avatar.image }), `${avatar.name} is now your tutor`)
  }

  const handleExport = async () => {
    const res = await run('export', () => exportMyDataAction(), 'Your data export is downloading')
    if (res?.data) {
      const blob = new Blob([JSON.stringify(res.data, null, 2)], { type: 'application/json' })
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `anaxly-data-${new Date().toISOString().slice(0, 10)}.json`
      a.click()
      URL.revokeObjectURL(url)
    }
  }

  const clearLocalCache = () => {
    try {
      const keep = new Set([LOCAL_PREFS_KEY, 'ai_tutor_selected_face_id', 'ai_tutor_avatar_preview'])
      Object.keys(localStorage)
        .filter((k) => !keep.has(k) && (k.startsWith('whiteboard_pages_') || k.startsWith('completed_concepts_') || k.startsWith('ai_tutor_')))
        .forEach((k) => localStorage.removeItem(k))
      flash('success', 'Cleared cached whiteboards and lesson data on this device')
    } catch {
      flash('error', 'Could not access browser storage')
    }
  }

  const requestNotifications = async () => {
    if (!('Notification' in window)) return flash('error', 'This browser does not support notifications')
    const perm = await Notification.requestPermission()
    if (perm === 'granted') setPref('reminders', true)
    else flash('error', 'Notifications are blocked in your browser settings')
  }

  const memberSince = user.createdAt ? new Date(user.createdAt).toLocaleDateString(undefined, { month: 'long', year: 'numeric' }) : null

  return (
    <div className="min-h-screen bg-canvas text-ink-primary">
      {/* Header */}
      <header className="sticky top-0 z-30 border-b border-border-subtle bg-canvas/85 backdrop-blur-xl">
        <div className="mx-auto flex max-w-7xl items-center justify-between gap-3 px-4 py-3 sm:px-8">
          <div className="flex min-w-0 items-center gap-3">
            <Link
              href={`/dashboard/${user.id}`}
              className="inline-flex h-10 w-10 items-center justify-center rounded-xl border border-border-subtle bg-surface text-ink-secondary transition-colors hover:bg-canvas-soft hover:text-ink-primary"
              aria-label="Back to dashboard"
            >
              <ArrowLeft className="h-4 w-4" />
            </Link>
            <div className="min-w-0">
              <p className="text-xs text-ink-muted">Dashboard / Settings</p>
              <h1 className="truncate font-editorial text-2xl leading-tight">Settings</h1>
            </div>
          </div>
          <Link href={`/dashboard/${user.id}`} className={primaryBtn}>
            <Sparkles className="h-4 w-4" />
            <span className="hidden sm:inline">Open classroom</span>
          </Link>
        </div>
      </header>

      <div className="mx-auto flex max-w-7xl flex-col gap-6 px-4 py-6 sm:px-8 md:flex-row md:py-10">
        {/* Sidebar */}
        <aside className="w-full shrink-0 md:sticky md:top-24 md:h-fit md:w-64">
          {/* Identity */}
          <div className="mb-4 overflow-hidden rounded-2xl border border-border-subtle bg-surface shadow-xs">
            <div className="h-14 bg-gradient-to-r from-accent-warm via-accent-primary to-accent-sage opacity-90" />
            <div className="-mt-7 px-4 pb-4">
              <div className="flex h-14 w-14 items-center justify-center rounded-full border-4 border-surface bg-accent-warm-soft font-editorial text-xl text-accent-warm">
                {(fullName || 'S').charAt(0).toUpperCase()}
              </div>
              <p className="mt-2 truncate text-sm font-semibold">{fullName || 'Student'}</p>
              <p className="truncate text-xs text-ink-muted">{user.email}</p>
              <div className="mt-2 flex flex-wrap gap-1.5 text-[10px] font-semibold uppercase tracking-wider">
                <span className="rounded-full bg-accent-warm-soft px-2 py-0.5 text-accent-warm">{plan.name}</span>
                <span className="rounded-full bg-canvas-soft px-2 py-0.5 text-ink-secondary">{targetBoard}</span>
                <span className="rounded-full bg-canvas-soft px-2 py-0.5 text-ink-secondary">{classLevel.replace('_', ' ')}</span>
              </div>
            </div>
          </div>

          <div className="relative mb-3">
            <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-ink-muted" />
            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search settings"
              className={`${inputClass} pl-9`}
            />
          </div>

          <nav className="flex gap-1 overflow-x-auto pb-1 md:flex-col md:overflow-visible">
            {groups.map((g) => (
              <div key={g} className="contents md:block md:pb-3">
                <p className="hidden px-3 pb-1 pt-2 text-[10px] font-semibold uppercase tracking-[0.14em] text-ink-hairline md:block">{g}</p>
                {filteredTabs
                  .filter((t) => t.group === g)
                  .map((t) => {
                    const active = t.id === activeTab
                    const Icon = t.icon
                    return (
                      <button
                        key={t.id}
                        type="button"
                        onClick={() => go(t.id)}
                        className={`relative flex w-full shrink-0 cursor-pointer items-center gap-3 whitespace-nowrap rounded-xl px-3 py-2 text-left text-sm font-medium transition-all ${
                          active ? 'bg-surface text-ink-primary shadow-xs ring-1 ring-border-subtle' : 'text-ink-secondary hover:bg-canvas-soft hover:text-ink-primary'
                        }`}
                      >
                        {active && <span className="absolute left-0 top-2 bottom-2 hidden w-1 rounded-full bg-accent-warm md:block" />}
                        <Icon className={`h-4 w-4 ${active ? 'text-accent-warm' : 'text-ink-muted'}`} />
                        <span>{t.label}</span>
                      </button>
                    )
                  })}
                {g === 'You' && (
                  <Link
                    href={`/dashboard/${user.id}/profile`}
                    className="flex w-full shrink-0 items-center gap-3 whitespace-nowrap rounded-xl px-3 py-2 text-left text-sm font-medium text-ink-secondary transition-all hover:bg-canvas-soft hover:text-ink-primary"
                  >
                    <NotebookPen className="h-4 w-4 text-ink-muted" />
                    <span className="flex-1">Profile &amp; notes</span>
                    <ExternalLink className="hidden h-3.5 w-3.5 text-ink-hairline md:block" />
                  </Link>
                )}
              </div>
            ))}
            {filteredTabs.length === 0 && <p className="px-3 py-2 text-xs text-ink-muted">No settings match “{query}”.</p>}
          </nav>

          <form action={signOutAction} className="mt-4 hidden md:block">
            <button type="submit" className="flex w-full cursor-pointer items-center gap-3 rounded-xl px-3 py-2 text-sm font-medium text-red-700 transition-colors hover:bg-red-50">
              <LogOut className="h-4 w-4" /> Sign out
            </button>
          </form>
        </aside>

        {/* Content */}
        <main key={activeTab} className="min-w-0 flex-1 animate-in fade-in-0 slide-in-from-bottom-2 duration-300">
          <div className="mb-6">
            <h2 className="font-editorial text-3xl">{current.label}</h2>
            <p className="mt-1 text-sm text-ink-muted">{current.desc}</p>
          </div>

          <div className="space-y-6">
            {/* ACCOUNT */}
            {activeTab === 'account' && (
              <>
                <Section title="Student profile" desc="How the tutor addresses you and which syllabus it follows.">
                  <form
                    onSubmit={(e) => {
                      e.preventDefault()
                      run('account', () => updateAccountAction({ fullName, classLevel, targetBoard }), 'Profile updated')
                    }}
                    className="space-y-4 px-5 py-5 sm:px-6"
                  >
                    <div className="grid gap-4 sm:grid-cols-2">
                      <label className="space-y-1.5">
                        <span className="text-xs font-medium text-ink-secondary">Full name</span>
                        <input className={inputClass} value={fullName} onChange={(e) => setFullName(e.target.value)} required placeholder="e.g. Aarav Sharma" />
                      </label>
                      <label className="space-y-1.5">
                        <span className="text-xs font-medium text-ink-secondary">Email</span>
                        <div className="relative">
                          <Mail className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-ink-muted" />
                          <input className={`${inputClass} pl-9`} value={user.email || ''} disabled />
                        </div>
                      </label>
                    </div>
                    <div className="space-y-1.5">
                      <span className="text-xs font-medium text-ink-secondary">Board</span>
                      <div className="grid gap-2 sm:grid-cols-3">
                        {BOARD_OPTIONS.map((b: any) => (
                          <button
                            key={b.id}
                            type="button"
                            disabled={b.disabled}
                            onClick={() => setTargetBoard(b.id)}
                            className={`cursor-pointer rounded-xl border px-3 py-2.5 text-left transition-all disabled:cursor-not-allowed disabled:opacity-50 ${
                              targetBoard === b.id ? 'border-accent-warm bg-accent-warm-soft ring-1 ring-accent-warm/30' : 'border-border-subtle hover:bg-canvas-soft'
                            }`}
                          >
                            <p className="text-sm font-semibold">{b.id}</p>
                            <p className="text-[11px] text-ink-muted">{b.disabled ? 'Coming soon' : b.name.split('(')[1]?.replace(')', '') || ''}</p>
                          </button>
                        ))}
                      </div>
                    </div>
                    <div className="space-y-1.5">
                      <span className="text-xs font-medium text-ink-secondary">Class</span>
                      <div className="flex flex-wrap gap-2">
                        {CLASS_LEVEL_OPTIONS.map((c) => (
                          <button
                            key={c.id}
                            type="button"
                            onClick={() => setClassLevel(c.label)}
                            className={`cursor-pointer rounded-full border px-3.5 py-1.5 text-xs font-medium transition-all ${
                              classLevel === c.label ? 'border-accent-warm bg-accent-warm text-white' : 'border-border-subtle bg-surface hover:border-accent-warm-border'
                            }`}
                          >
                            {c.label}
                          </button>
                        ))}
                      </div>
                    </div>
                    <div className="flex justify-end">
                      <button type="submit" disabled={busy === 'account'} className={primaryBtn}>
                        {busy === 'account' ? <Loader2 className="h-4 w-4 animate-spin" /> : <Check className="h-4 w-4" />} Save profile
                      </button>
                    </div>
                  </form>
                </Section>

                <Section title="Password" desc="Use at least 8 characters with a mix of letters, numbers and symbols.">
                  <form
                    onSubmit={(e) => {
                      e.preventDefault()
                      if (newPassword.length < 6) return flash('error', 'Password must be at least 6 characters')
                      if (newPassword !== confirmPassword) return flash('error', 'Passwords do not match')
                      run('pw', () => updatePasswordAction({ newPassword }), 'Password changed').then(() => {
                        setNewPassword('')
                        setConfirmPassword('')
                      })
                    }}
                    className="space-y-4 px-5 py-5 sm:px-6"
                  >
                    <div className="grid gap-4 sm:grid-cols-2">
                      <div className="relative">
                        <input type={showPw ? 'text' : 'password'} className={inputClass} placeholder="New password" value={newPassword} onChange={(e) => setNewPassword(e.target.value)} />
                        <button type="button" onClick={() => setShowPw(!showPw)} className="absolute right-3 top-1/2 -translate-y-1/2 cursor-pointer text-ink-muted hover:text-ink-primary" aria-label="Toggle password visibility">
                          {showPw ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                        </button>
                      </div>
                      <input type={showPw ? 'text' : 'password'} className={inputClass} placeholder="Confirm password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} />
                    </div>
                    {newPassword && (
                      <div className="flex items-center gap-3">
                        <div className="flex flex-1 gap-1">
                          {[0, 1, 2, 3].map((i) => (
                            <div
                              key={i}
                              className={`h-1.5 flex-1 rounded-full transition-colors ${
                                i < strength ? (strength <= 1 ? 'bg-red-500' : strength === 2 ? 'bg-amber-500' : 'bg-emerald-500') : 'bg-border-subtle'
                              }`}
                            />
                          ))}
                        </div>
                        <span className="text-xs text-ink-muted">{['Too weak', 'Weak', 'Okay', 'Strong', 'Excellent'][strength]}</span>
                      </div>
                    )}
                    <div className="flex justify-end">
                      <button type="submit" disabled={!newPassword || busy === 'pw'} className={primaryBtn}>
                        {busy === 'pw' ? <Loader2 className="h-4 w-4 animate-spin" /> : <KeyRound className="h-4 w-4" />} Update password
                      </button>
                    </div>
                  </form>
                </Section>

                <Section title="Sessions & sign-in">
                  <Row label="This device" desc={`Signed in${user.provider ? ` with ${user.provider}` : ''}${user.lastSignIn ? ` · last sign-in ${new Date(user.lastSignIn).toLocaleString()}` : ''}`}>
                    <span className="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 px-2.5 py-1 text-xs font-medium text-emerald-700">
                      <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-emerald-500" /> Active now
                    </span>
                  </Row>
                  {memberSince && (
                    <Row label="Member since" desc="Thanks for learning with Anaxly.">
                      <span className="text-sm text-ink-secondary">{memberSince}</span>
                    </Row>
                  )}
                  <Row label="Switch account" desc="Sign out here and pick a different account.">
                    <form action={switchAccountAction}>
                      <button className={ghostBtn}>
                        <Users className="h-4 w-4" /> Switch
                      </button>
                    </form>
                  </Row>
                  <Row label="Sign out of all devices" desc="Ends every session, including phones and other browsers.">
                    <form action={signOutEverywhereAction}>
                      <button className={`${ghostBtn} border-red-200 text-red-700 hover:bg-red-50`}>
                        <MonitorSmartphone className="h-4 w-4" /> Sign out everywhere
                      </button>
                    </form>
                  </Row>
                </Section>
              </>
            )}

            {/* GOALS */}
            {activeTab === 'goals' && (
              <Section title="Exam target" desc="Your study planner and dashboard use this to pace your chapters.">
                <form
                  onSubmit={(e) => {
                    e.preventDefault()
                    if (!examDate) return flash('error', 'Pick your exam date first')
                    run('goals', () => updateStudyPlanAction({ targetExamDate: examDate, dailyStudyMinutes: dailyMinutes }), 'Study goals saved')
                  }}
                  className="space-y-6 px-5 py-5 sm:px-6"
                >
                  <div className="grid gap-4 sm:grid-cols-2">
                    <label className="space-y-1.5">
                      <span className="text-xs font-medium text-ink-secondary">Exam date</span>
                      <input type="date" className={inputClass} value={examDate} onChange={(e) => setExamDate(e.target.value)} />
                    </label>
                    <div className="flex items-center gap-3 rounded-xl border border-border-subtle bg-canvas-soft p-4">
                      <CalendarClock className="h-8 w-8 text-accent-warm" />
                      <div>
                        <p className="font-editorial text-2xl leading-none">{daysToExam !== null ? Math.max(0, daysToExam) : '—'}</p>
                        <p className="text-xs text-ink-muted">days until your exam</p>
                      </div>
                    </div>
                  </div>
                  <div className="space-y-2">
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-medium text-ink-secondary">Daily study target</span>
                      <span className="font-mono text-sm font-semibold text-accent-warm">{dailyMinutes} min</span>
                    </div>
                    <input type="range" min={15} max={180} step={15} value={dailyMinutes} onChange={(e) => setDailyMinutes(Number(e.target.value))} className="w-full cursor-pointer accent-[var(--accent-warm)]" />
                    <div className="flex justify-between text-[10px] text-ink-muted">
                      <span>15 min</span>
                      <span>1.5 h</span>
                      <span>3 h</span>
                    </div>
                    <p className="text-xs text-ink-muted">≈ {Math.round((dailyMinutes * 7) / 60 * 10) / 10} hours per week{daysToExam && daysToExam > 0 ? ` · ${Math.round((dailyMinutes * daysToExam) / 60)} hours before your exam` : ''}.</p>
                  </div>
                  <div className="flex justify-end">
                    <button type="submit" disabled={busy === 'goals'} className={primaryBtn}>
                      {busy === 'goals' ? <Loader2 className="h-4 w-4 animate-spin" /> : <Target className="h-4 w-4" />} Save goals
                    </button>
                  </div>
                </form>
              </Section>
            )}

            {/* BILLING */}
            {activeTab === 'billing' && (
              <>
                <div className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-accent-primary via-accent-warm to-accent-sage p-6 text-white shadow-md">
                  <div className="absolute -right-10 -top-10 h-40 w-40 rounded-full bg-white/10 blur-2xl" />
                  <p className="text-xs uppercase tracking-[0.18em] text-white/70">Current plan</p>
                  <div className="mt-1 flex flex-wrap items-end justify-between gap-4">
                    <div>
                      <h3 className="font-editorial text-4xl">{plan.name}</h3>
                      <p className="mt-1 text-sm text-white/80">
                        {subscription?.status ? `${subscription.status} · ` : ''}
                        {subscription?.current_period_end ? `renews ${new Date(subscription.current_period_end).toLocaleDateString()}` : 'No active billing cycle'}
                      </p>
                    </div>
                    <Link href="/pricing" className="inline-flex items-center gap-2 rounded-xl bg-white px-4 py-2 text-sm font-semibold text-accent-primary transition-transform hover:scale-[1.02]">
                      {tier === 'free' ? 'Upgrade' : 'Change plan'} <ExternalLink className="h-4 w-4" />
                    </Link>
                  </div>
                  <div className="mt-6">
                    <div className="flex justify-between text-xs text-white/80">
                      <span>Live classes this month</span>
                      <span className="font-mono">
                        {classesUsed} / {classesLimit}
                      </span>
                    </div>
                    <div className="mt-1.5 h-2 overflow-hidden rounded-full bg-white/20">
                      <div className="h-full rounded-full bg-white transition-all duration-700" style={{ width: `${usagePct}%` }} />
                    </div>
                  </div>
                </div>
                <Section title="What's included">
                  <div className="grid gap-px bg-border-subtle sm:grid-cols-2">
                    {[
                      ['AI video avatar', subscription?.is_avatar_enabled ?? profile?.is_avatar_enabled !== false],
                      ['Mock exams', !!subscription?.has_mock_exam_access],
                      ['Camera scratchpad', !!subscription?.has_camera_scratchpad],
                      ['Unwatermarked notes', !!subscription?.has_unwatermarked_notes],
                      ['Parent WhatsApp reports', !!subscription?.has_parent_whatsapp_reports],
                      ['Morning blitz', !!subscription?.has_morning_blitz],
                    ].map(([label, on]) => (
                      <div key={label as string} className="flex items-center justify-between bg-surface px-5 py-3.5 text-sm">
                        <span className={on ? 'text-ink-primary' : 'text-ink-muted'}>{label as string}</span>
                        {on ? <CheckCircle2 className="h-4 w-4 text-emerald-600" /> : <Lock className="h-4 w-4 text-ink-hairline" />}
                      </div>
                    ))}
                  </div>
                </Section>
                <p className="text-xs text-ink-muted">
                  Need a higher limit or an invoice? Email{' '}
                  <a className="font-medium text-accent-warm hover:underline" href="mailto:shauryaprabhakar097@gmail.com">
                    shauryaprabhakar097@gmail.com
                  </a>
                  .
                </p>
              </>
            )}

            {/* AVATARS */}
            {activeTab === 'avatars' && (
              <>
                <div className="flex flex-col items-center gap-6 rounded-2xl border border-border-subtle bg-surface p-6 shadow-xs sm:flex-row">
                  <div className="relative h-32 w-32 shrink-0">
                    <div className="absolute inset-0 animate-pulse rounded-full bg-accent-warm/20 blur-xl" />
                    <img
                      src={activeAvatar.image}
                      alt={activeAvatar.name}
                      className="relative h-full w-full rounded-full border-4 border-surface object-cover shadow-lg"
                      onError={(e) => {
                        ;(e.currentTarget as HTMLImageElement).src = `https://app.simli.com/characters/trinity2/${activeAvatar.id}.jpg`
                      }}
                    />
                  </div>
                  <div className="text-center sm:text-left">
                    <span className="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 px-2.5 py-0.5 text-[11px] font-medium text-emerald-700">
                      <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-emerald-500" /> Your live tutor
                    </span>
                    <h3 className="mt-2 font-editorial text-2xl">{activeAvatar.name}</h3>
                    <p className="text-xs text-ink-muted">{activeAvatar.title}</p>
                    <p className="mt-2 text-sm leading-relaxed text-ink-secondary">{activeAvatar.description}</p>
                  </div>
                </div>
                <div className="grid gap-4 md:grid-cols-2">
                  {PREBUILT_AVATARS.map((a) => {
                    const sel = a.id === selectedAvatarId
                    return (
                      <button
                        key={a.id}
                        type="button"
                        disabled={sel || busy === 'avatar'}
                        onClick={() => handleSelectAvatar(a)}
                        className={`group flex cursor-pointer gap-4 rounded-2xl border p-4 text-left transition-all disabled:cursor-default ${
                          sel ? 'border-accent-warm bg-accent-warm-soft ring-1 ring-accent-warm/30' : 'border-border-subtle bg-surface hover:-translate-y-0.5 hover:shadow-md'
                        }`}
                      >
                        <img src={a.image} alt="" className="h-16 w-16 shrink-0 rounded-full object-cover transition-transform group-hover:scale-105" />
                        <div className="min-w-0 flex-1">
                          <div className="flex items-center justify-between gap-2">
                            <p className="truncate text-sm font-semibold">{a.name}</p>
                            <span className={`shrink-0 rounded-full px-2 py-0.5 text-[10px] font-semibold ${sel ? 'bg-accent-warm text-white' : 'bg-canvas-soft text-ink-muted'}`}>
                              {sel ? 'Active' : a.badge}
                            </span>
                          </div>
                          <p className="truncate text-xs text-ink-muted">{a.subject}</p>
                          <p className="mt-1 line-clamp-2 text-xs text-ink-secondary">{a.description}</p>
                        </div>
                      </button>
                    )
                  })}
                </div>
                <Section title="Video avatar">
                  <Row label="Face-to-face video" desc={profile?.is_avatar_enabled !== false ? 'Your tutor appears on video in live classes.' : 'Audio-only mode is set by your administrator.'}>
                    {profile?.is_avatar_enabled !== false ? <Video className="h-5 w-5 text-emerald-600" /> : <VideoOff className="h-5 w-5 text-ink-muted" />}
                  </Row>
                  <Row label="Reset tutor" desc="Go back to the default tutor.">
                    <button type="button" onClick={() => handleSelectAvatar(PREBUILT_AVATARS[0])} className={ghostBtn}>
                      <RotateCcw className="h-4 w-4" /> Reset
                    </button>
                  </Row>
                </Section>
              </>
            )}

            {/* AUDIO */}
            {activeTab === 'audio' && (
              <>
                <Section
                  title="Tutor voice"
                  desc="Saved to your account and used in every live class."
                  action={
                    <button
                      type="button"
                      disabled={busy === 'voice'}
                      onClick={() => run('voice', () => updateGeneralSettingsAction({ preferredTeacherVoice: preferredVoice }), 'Voice saved')}
                      className={primaryBtn}
                    >
                      {busy === 'voice' ? <Loader2 className="h-4 w-4 animate-spin" /> : <Check className="h-4 w-4" />} Save
                    </button>
                  }
                >
                  <div className="grid gap-3 px-5 py-5 sm:grid-cols-2 sm:px-6">
                    {VOICE_OPTIONS.map((v) => (
                      <ChoiceCard
                        key={v.id}
                        active={preferredVoice === v.id}
                        onClick={() => setPreferredVoice(v.id)}
                        title={`${v.name} · ${v.gender}`}
                        desc={v.desc}
                        badge={v.isRecommended ? 'Recommended' : undefined}
                      />
                    ))}
                  </div>
                </Section>
                <Section title="Listening & playback" desc="Stored on this device.">
                  <Row label="Speaking speed">
                    <Segmented value={prefs.speechRate} onChange={(v) => setPref('speechRate', v)} options={[{ id: '0.9', label: '0.9×' }, { id: '1.0', label: '1×' }, { id: '1.15', label: '1.15×' }, { id: '1.3', label: '1.3×' }]} />
                  </Row>
                  <Row label="Lesson language" desc="Language the tutor leans towards when explaining.">
                    <Segmented value={prefs.language} onChange={(v) => setPref('language', v)} options={[{ id: 'en-IN', label: 'English' }, { id: 'hinglish', label: 'Hinglish' }, { id: 'hi-IN', label: 'Hindi' }]} />
                  </Row>
                  <Row label="Auto-listen" desc="Detects when you start speaking and pauses the tutor.">
                    <Toggle label="Auto-listen" checked={prefs.autoListen} onChange={(v) => setPref('autoListen', v)} />
                  </Row>
                  <Row label="Live captions" desc="Show a transcript of what the tutor says.">
                    <Toggle label="Live captions" checked={prefs.captions} onChange={(v) => setPref('captions', v)} />
                  </Row>
                  <Row label="Sound effects" desc="Subtle chimes for correct answers and page turns.">
                    <Toggle label="Sound effects" checked={prefs.soundEffects} onChange={(v) => setPref('soundEffects', v)} />
                  </Row>
                </Section>
              </>
            )}

            {/* TEACHING */}
            {activeTab === 'teaching' && (
              <>
                <Section
                  title="Teaching method"
                  desc="Saved to your account."
                  action={
                    <button
                      type="button"
                      disabled={busy === 'teach'}
                      onClick={() => run('teach', () => updateTeachingStyleAction({ learningStyle, preferredPacing }), 'Teaching style saved')}
                      className={primaryBtn}
                    >
                      {busy === 'teach' ? <Loader2 className="h-4 w-4 animate-spin" /> : <Check className="h-4 w-4" />} Save
                    </button>
                  }
                >
                  <div className="grid gap-3 px-5 py-5 sm:px-6">
                    <ChoiceCard active={learningStyle === 'socratic'} onClick={() => setLearningStyle('socratic')} title="Socratic" badge="Recommended" desc="Intuition → formula → example → worked numerical → check understanding → board question. The tutor keeps asking you questions." />
                    <ChoiceCard active={learningStyle === 'direct'} onClick={() => setLearningStyle('direct')} title="Direct" desc="Concise statements and quick worked numericals. Best for fast revision." />
                    <ChoiceCard active={learningStyle === 'visual'} onClick={() => setLearningStyle('visual')} title="Visual" desc="Graphs, diagrams and analogies first, then the numericals." />
                  </div>
                  <Row label="Pacing" desc="How fast the tutor moves between concepts.">
                    <Segmented value={preferredPacing} onChange={setPreferredPacing} options={[{ id: 'slow', label: 'Relaxed' }, { id: 'normal', label: 'Normal' }, { id: 'fast', label: 'Fast' }]} />
                  </Row>
                </Section>
                <Section title="Notes & hints" desc="Stored on this device.">
                  <Row label="Chalkboard notes" desc="Full worked layout or key points only.">
                    <Segmented value={prefs.noteDensity} onChange={(v) => setPref('noteDensity', v)} options={[{ id: 'topper_detailed', label: 'Detailed' }, { id: 'summary_keypoints', label: 'Key points' }]} />
                  </Row>
                  <Row label="Hints" desc="How much help you get before the answer is revealed.">
                    <Segmented value={prefs.hintLevel} onChange={(v) => setPref('hintLevel', v)} options={[{ id: 'minimal', label: 'Minimal' }, { id: 'balanced', label: 'Balanced' }, { id: 'generous', label: 'Generous' }]} />
                  </Row>
                  <Row label="Sobi companion" desc="Show the mascot with tips around the app.">
                    <Toggle label="Sobi companion" checked={prefs.mascot} onChange={(v) => setPref('mascot', v)} />
                  </Row>
                </Section>
              </>
            )}

            {/* NOTIFICATIONS */}
            {activeTab === 'notifications' && (
              <Section title="Reminders" desc="Stored on this device.">
                <Row label="Daily study reminder" desc="A browser notification at your chosen time.">
                  <div className="flex items-center gap-3">
                    {prefs.reminders && <input type="time" value={prefs.reminderTime} onChange={(e) => setPref('reminderTime', e.target.value)} className={`${inputClass} w-32 py-1.5`} />}
                    <Toggle label="Daily study reminder" checked={prefs.reminders} onChange={(v) => (v ? requestNotifications() : setPref('reminders', false))} />
                  </div>
                </Row>
                <Row label="Streak alerts" desc="Nudge me before I lose my streak.">
                  <Toggle label="Streak alerts" checked={prefs.streakAlerts} onChange={(v) => setPref('streakAlerts', v)} />
                </Row>
                <Row label="Weekly progress report" desc="Summary of chapters, minutes and weak concepts.">
                  <Toggle label="Weekly report" checked={prefs.weeklyReport} onChange={(v) => setPref('weeklyReport', v)} />
                </Row>
                <Row label="Product updates" desc="New chapters, features and tips.">
                  <Toggle label="Product updates" checked={prefs.productNews} onChange={(v) => setPref('productNews', v)} />
                </Row>
              </Section>
            )}

            {/* APPEARANCE */}
            {activeTab === 'appearance' && (
              <Section title="Display & accessibility" desc="Stored on this device and applied instantly.">
                <Row label="Text size">
                  <Segmented value={prefs.textSize} onChange={(v) => setPref('textSize', v)} options={[{ id: 'sm', label: 'Small' }, { id: 'md', label: 'Default' }, { id: 'lg', label: 'Large' }]} />
                </Row>
                <Row label="Reduce motion" desc="Turn off most animations and transitions.">
                  <Toggle label="Reduce motion" checked={prefs.reduceMotion} onChange={(v) => setPref('reduceMotion', v)} />
                </Row>
                <Row label="High contrast" desc="Darker text and stronger borders.">
                  <Toggle label="High contrast" checked={prefs.highContrast} onChange={(v) => setPref('highContrast', v)} />
                </Row>
                <Row label="Dyslexia-friendly font" desc="Wider letter spacing for easier reading.">
                  <Toggle label="Dyslexia-friendly font" checked={prefs.dyslexiaFont} onChange={(v) => setPref('dyslexiaFont', v)} />
                </Row>
              </Section>
            )}

            {/* SHORTCUTS */}
            {activeTab === 'shortcuts' && (
              <Section title="Keyboard shortcuts">
                {[
                  ['Space', 'Hold to talk / interrupt the tutor'],
                  ['M', 'Mute or unmute microphone'],
                  ['N', 'Open chapter notes'],
                  ['← / →', 'Previous / next whiteboard page'],
                  ['Esc', 'Close dialogs'],
                ].map(([k, d]) => (
                  <Row key={k} label={d}>
                    <kbd className="rounded-lg border border-border-subtle bg-canvas-soft px-2.5 py-1 font-mono text-xs shadow-xs">{k}</kbd>
                  </Row>
                ))}
              </Section>
            )}

            {/* PRIVACY */}
            {activeTab === 'privacy' && (
              <>
                <Section title="Your data">
                  <Row label="Download my data" desc="Profile, progress, study plans and enrollments as JSON.">
                    <button type="button" onClick={handleExport} disabled={busy === 'export'} className={ghostBtn}>
                      {busy === 'export' ? <Loader2 className="h-4 w-4 animate-spin" /> : <Download className="h-4 w-4" />} Export
                    </button>
                  </Row>
                  <Row label="Clear cached lessons" desc="Removes saved whiteboards and lesson cache from this browser. Your account progress is kept.">
                    <button type="button" onClick={clearLocalCache} className={ghostBtn}>
                      <Trash2 className="h-4 w-4" /> Clear cache
                    </button>
                  </Row>
                  <Row label="Legal" desc="How we handle your data.">
                    <div className="flex gap-3 text-sm">
                      <Link href="/privacy" className="text-accent-warm hover:underline">Privacy</Link>
                      <Link href="/terms" className="text-accent-warm hover:underline">Terms</Link>
                    </div>
                  </Row>
                </Section>
                <section className="rounded-2xl border border-red-200 bg-red-50/40 p-5 sm:p-6">
                  <div className="flex items-start gap-3">
                    <AlertTriangle className="mt-0.5 h-5 w-5 text-red-600" />
                    <div className="flex-1">
                      <h3 className="font-editorial text-lg text-red-900">Delete account</h3>
                      <p className="mt-1 text-xs text-red-800/80">This permanently removes your profile, notes and progress. Type DELETE to request deletion.</p>
                      <div className="mt-3 flex flex-col gap-2 sm:flex-row">
                        <input value={deleteConfirm} onChange={(e) => setDeleteConfirm(e.target.value)} placeholder="DELETE" className={`${inputClass} sm:max-w-[12rem]`} />
                        <a
                          href={deleteConfirm === 'DELETE' ? `mailto:shauryaprabhakar097@gmail.com?subject=Account%20deletion%20request&body=Please%20delete%20my%20Anaxly%20account%20(${encodeURIComponent(user.email || user.id)}).` : undefined}
                          aria-disabled={deleteConfirm !== 'DELETE'}
                          className={`inline-flex items-center justify-center gap-2 rounded-xl px-4 py-2 text-sm font-medium text-white transition-colors ${
                            deleteConfirm === 'DELETE' ? 'cursor-pointer bg-red-600 hover:bg-red-700' : 'pointer-events-none bg-red-300'
                          }`}
                        >
                          <Trash2 className="h-4 w-4" /> Request deletion
                        </a>
                      </div>
                    </div>
                  </div>
                </section>
              </>
            )}
          </div>
        </main>
      </div>

      {/* Toast */}
      <div aria-live="polite" className="pointer-events-none fixed bottom-6 left-1/2 z-50 -translate-x-1/2">
        {toast && (
          <div
            className={`flex animate-in items-center gap-2 rounded-full px-4 py-2.5 text-sm font-medium shadow-lg fade-in-0 slide-in-from-bottom-4 ${
              toast.type === 'success' ? 'bg-ink-primary text-white' : 'bg-red-600 text-white'
            }`}
          >
            {toast.type === 'success' ? <CheckCircle2 className="h-4 w-4" /> : <AlertCircle className="h-4 w-4" />}
            {toast.message}
          </div>
        )}
      </div>
    </div>
  )
}

'use client'

import React, { useState, useEffect } from 'react'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogFooter,
} from '@/components/ui/dialog'
import { Label } from '@/components/ui/label'
import { signOutAction, updatePreferencesAction, enrollCurriculumAction } from '@/app/dashboard/actions'
import { triggerCompanionGuidance } from '@/components/mascot/Mascot'
import { MasteryQuizModal } from '@/components/quiz/MasteryQuizModal'
import { PricingNoticeModal } from './PricingNoticeModal'
import { StudyPlannerCard, StudyPlanData } from './StudyPlannerCard'
import { WeakConceptsReviewCard } from './WeakConceptsReviewCard'
import { VOICE_OPTIONS } from '@/lib/voiceAndLanguageConfig'
import { DashboardNav, NavItem } from './DashboardNav'
import { DailyActivityChart } from './DailyActivityChart'
import { DashCard, StatTile, SectionHeader } from './primitives'

interface Module {
  id: string
  curriculum_id: string
  order_index: number
  title: string
  description?: string | null
  ai_system_prompt_context?: string | null
  key_concepts?: string[] | null
  success_criteria?: string | null
  estimated_minutes?: number | null
  subtopics?: string[] | Array<{ title?: string; duration?: string; key_formula?: string }> | null
  board?: string | null
  class_level?: string | null
  chapter_notes?: string | null
}

interface ProgressRecord {
  id: string
  syllabus_module_id: string
  user_id: string
  status: 'not_started' | 'in_progress' | 'completed' | 'needs_review'
  score?: number | null
  started_at?: string | null
  completed_at?: string | null
}

interface Curriculum {
  id: string
  title: string
  description?: string | null
  category?: string | null
  difficulty_level?: string | null
  estimated_duration_minutes?: number | null
  is_published?: boolean
  class_level?: string | null
  board?: string | null
  order_index?: number | null
}

interface MemoryItem {
  id: string
  content?: string
  memory_text?: string
  importance_score?: number | null
  created_at: string
}

interface Profile {
  id: string
  full_name?: string | null
  avatar_url?: string | null
  current_streak?: number | null
  longest_streak?: number | null
  total_classes_taken?: number | null
  total_learning_minutes?: number | null
  learning_style?: string | null
  preferred_pacing?: string | null
  preferred_teacher_voice?: string | null
  weak_subjects?: string[] | null
  strong_subjects?: string[] | null
  learning_level?: string | null
  class_level?: string | null
  last_class_date?: string | null
  limit_type?: 'unlimited' | 'modules' | 'requests' | string | null
  max_modules?: number | null
  used_modules?: number | null
  max_requests?: number | null
  used_requests?: number | null
}

interface StitchDashboardViewProps {
  user: {
    id: string
    email?: string
  }
  profile: Profile
  primaryCurriculum: Curriculum | null
  enrolledCurriculums: Curriculum[]
  allCurriculums?: Curriculum[]
  modules: Module[]
  progressRecords: ProgressRecord[]
  memories: MemoryItem[]
  studyPlan?: StudyPlanData | null
}



export function StitchDashboardView({
  user,
  profile,
  primaryCurriculum,
  enrolledCurriculums = [],
  allCurriculums = [],
  modules = [],
  progressRecords = [],
  memories = [],
  studyPlan = null,
}: StitchDashboardViewProps) {
  const router = useRouter()
  const [activeNav, setActiveNav] = useState('home')
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const [liveModalOpen, setLiveModalOpen] = useState(false)
  const [preferencesOpen, setPreferencesOpen] = useState(false)
  const [notesDialogOpen, setNotesDialogOpen] = useState(false)
  const [pricingModalOpen, setPricingModalOpen] = useState(false)
  const [coursesDialogOpen, setCoursesDialogOpen] = useState(false)
  const [isStartingSession, setIsStartingSession] = useState(false)
  const [quizModalOpen, setQuizModalOpen] = useState(false)
  const [syllabusModalOpen, setSyllabusModalOpen] = useState(false)
  const [selectedSyllabusCurriculumId, setSelectedSyllabusCurriculumId] = useState<string | null>(null)
  const [selectedSyllabusCategory, setSelectedSyllabusCategory] = useState<string | null>(null)

  // Discipline chips derived from actual enrolled curriculums (or all published)
  const availableDisciplines = enrolledCurriculums.length > 0 
    ? enrolledCurriculums.map((c) => c.title)
    : allCurriculums.length > 0
    ? allCurriculums.map((c) => c.title)
    : ['General Studies']

  const [selectedDiscipline, setSelectedDiscipline] = useState(availableDisciplines[0] || 'General Studies')

  // Preferences form state
  const [selectedVoice, setSelectedVoice] = useState(profile.preferred_teacher_voice || 'Leda')
  const [selectedStyle, setSelectedStyle] = useState(profile.learning_style || 'socratic')
  const [selectedPacing, setSelectedPacing] = useState(profile.preferred_pacing || 'standard')
  const [selectedClass, setSelectedClass] = useState(profile.class_level || 'Class 10')
  const [savingPrefs, setSavingPrefs] = useState(false)

  // Student Identity: Strictly from DB, no fake constants
  const studentName = profile.full_name || user.email?.split('@')[0] || 'Student'
  const studentAvatar = profile.avatar_url || null
  const studentTrack = profile.class_level || (profile.learning_level 
    ? `${profile.learning_level.charAt(0).toUpperCase() + profile.learning_level.slice(1)} Track`
    : 'Scholar')

  // Dynamic Date
  const todayFormatted = new Intl.DateTimeFormat('en-US', {
    weekday: 'long',
    month: 'long',
    day: 'numeric',
  }).format(new Date())

  // Quick dates for 14-day chart
  const now = new Date()
  const date7DaysAgo = new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric' }).format(new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000))
  const date14DaysAgo = new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric' }).format(new Date(now.getTime() - 14 * 24 * 60 * 60 * 1000))
  const todayShort = new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric' }).format(now)

  // Live Progress Map
  const progressMap = new Map<string, ProgressRecord>()
  progressRecords.forEach((p) => progressMap.set(p.syllabus_module_id, p))

  // 1 Free Module Quota Calculation
  const isUnlimitedUser = profile?.limit_type === 'unlimited'
  const maxAllowedModules = profile?.limit_type === 'modules' ? (profile?.max_modules ?? 5) : 1
  const completedCapsulesCount = progressRecords.filter((p) => p.status === 'completed' || !!p.completed_at).length
  const isFreeQuotaExhausted = !isUnlimitedUser && completedCapsulesCount >= maxAllowedModules

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const urlParams = new URLSearchParams(window.location.search)
      if (urlParams.get('pricing_notice') === 'true' || urlParams.get('limit_reached') === 'true') {
        setPricingModalOpen(true)
      }
    }
  }, [])

  const handleModuleClick = (e: React.MouseEvent, targetModId?: string) => {
    if (isFreeQuotaExhausted) {
      if (targetModId && isModuleComplete(targetModId)) {
        return
      }
      e.preventDefault()
      setPricingModalOpen(true)
    }
  }

  // Helper to reliably check module completion (respects status === 'completed' or completed_at != null)
  const isModuleComplete = (modId: string) => {
    const p = progressMap.get(modId)
    return p?.status === 'completed' || !!p?.completed_at
  }

  const isModuleInProgress = (modId: string) => {
    const p = progressMap.get(modId)
    return p?.status === 'in_progress' && !p?.completed_at
  }

  // Find Primary Active Course & Active Module
  // Dynamic resolution:
  // 1. If primaryCurriculum has unfinished modules, keep it active
  // 2. If primaryCurriculum is 100% completed, check other enrolled curriculums for pending modules
  // 3. If all enrolled are completed, advance to next chapter in allCurriculums
  // 4. Fallback to primaryCurriculum or first enrolled curriculum
  const activeCourse = (() => {
    if (primaryCurriculum) {
      const pMods = modules.filter((m) => m.curriculum_id === primaryCurriculum.id)
      const allDone = pMods.length > 0 && pMods.every((m) => isModuleComplete(m.id))
      if (!allDone) return primaryCurriculum
    }
    for (const curr of enrolledCurriculums) {
      const cMods = modules.filter((m) => m.curriculum_id === curr.id)
      const allDone = cMods.length > 0 && cMods.every((m) => isModuleComplete(m.id))
      if (!allDone) return curr
    }
    for (const curr of allCurriculums) {
      const cMods = modules.filter((m) => m.curriculum_id === curr.id)
      const allDone = cMods.length > 0 && cMods.every((m) => isModuleComplete(m.id))
      if (!allDone && cMods.length > 0) return curr
    }
    return primaryCurriculum || enrolledCurriculums[0] || allCurriculums[0] || null
  })()

  const activeCourseModules = activeCourse
    ? modules.filter((m) => m.curriculum_id === activeCourse.id).sort((a, b) => a.order_index - b.order_index)
    : []

  const inProgressModule = activeCourseModules.find((m) => isModuleInProgress(m.id))
  const nextUncompletedModule = activeCourseModules.find((m) => !isModuleComplete(m.id) && !isModuleInProgress(m.id))

  // If all completed, activeModule is the last module (for review), otherwise the next module
  const activeModule =
    inProgressModule ||
    nextUncompletedModule ||
    activeCourseModules[activeCourseModules.length - 1] ||
    null

  const activeModuleIndex = activeModule ? activeCourseModules.findIndex((m) => m.id === activeModule.id) + 1 : 0
  const activeModuleTotal = activeCourseModules.length

  // Universe of curriculums available to the student (deduplicated by id)
  const allAvailableCurriculums = (() => {
    const map = new Map<string, Curriculum>()
    allCurriculums.forEach((c) => map.set(c.id, c))
    enrolledCurriculums.forEach((c) => map.set(c.id, c))
    return Array.from(map.values()).sort((a, b) => (a.order_index ?? 0) - (b.order_index ?? 0))
  })()

  // Distinct subjects / disciplines
  const syllabusSubjects = Array.from(
    new Set(allAvailableCurriculums.map((c) => c.category || 'General').filter(Boolean))
  )

  // Chapter PYQs State
  const defaultChapterId = activeCourse?.id || (allCurriculums.length > 0 ? allCurriculums[0].id : null)
  const [selectedPyqChapterId, setSelectedPyqChapterId] = useState<string | null>(defaultChapterId)
  const [chapterPyqsData, setChapterPyqsData] = useState<any | null>(null)
  const [isLoadingPyqs, setIsLoadingPyqs] = useState(false)
  const [pyqMarkFilter, setPyqMarkFilter] = useState<'all' | '1' | '2' | '3' | '5'>('all')

  useEffect(() => {
    if (!selectedPyqChapterId) return
    let isCancelled = false
    setIsLoadingPyqs(true)
    fetch(`/api/curriculum/pyq?curriculumId=${selectedPyqChapterId}`)
      .then((res) => res.json())
      .then((json) => {
        if (!isCancelled) {
          if (json.success && Array.isArray(json.pyqs) && json.pyqs.length > 0) {
            setChapterPyqsData(json.pyqs[0])
          } else {
            setChapterPyqsData(null)
          }
        }
      })
      .catch((err) => {
        console.error('Failed to load dashboard PYQs:', err)
        if (!isCancelled) setChapterPyqsData(null)
      })
      .finally(() => {
        if (!isCancelled) setIsLoadingPyqs(false)
      })
    return () => {
      isCancelled = true
    }
  }, [selectedPyqChapterId])

  // Current active subject in syllabus modal
  const activeSyllabusCategory = selectedSyllabusCategory 
    || (activeCourse?.category || syllabusSubjects[0] || 'General')

  // Chapters in the active subject
  const currentSubjectChapters = allAvailableCurriculums
    .filter((c) => (c.category || 'General') === activeSyllabusCategory)
    .sort((a, b) => (a.order_index ?? 0) - (b.order_index ?? 0))

  // Current active chapter in syllabus modal
  const activeSyllabusChapter = (selectedSyllabusCurriculumId
    ? currentSubjectChapters.find((c) => c.id === selectedSyllabusCurriculumId)
    : null) || currentSubjectChapters[0] || activeCourse || allAvailableCurriculums[0] || null

  // Divided capsules for the active chapter
  const activeChapterCapsules = activeSyllabusChapter
    ? modules
        .filter((m) => m.curriculum_id === activeSyllabusChapter.id)
        .sort((a, b) => (a.order_index ?? 0) - (b.order_index ?? 0))
    : []

  // Calculations for Active Course
  const activeCompletedCount = activeCourseModules.filter((m) => isModuleComplete(m.id)).length
  const isAllCourseCompleted = activeCourseModules.length > 0 && activeCompletedCount === activeCourseModules.length
  const activePercentComplete = activeCourseModules.length > 0 
    ? Math.round((activeCompletedCount / activeCourseModules.length) * 100) 
    : 0

  // Overall Stats across all courses: strictly live DB numbers
  const totalCompletedModules = progressRecords.filter((p) => p.status === 'completed' || !!p.completed_at).length
  const overallPercentComplete = modules.length > 0
    ? Math.round((totalCompletedModules / modules.length) * 100)
    : 0

  const studyHours = profile.total_learning_minutes && profile.total_learning_minutes > 0
    ? (profile.total_learning_minutes / 60).toFixed(1)
    : '0'

  const currentStreak = profile.current_streak || 0
  const totalMasteryLessons = profile.total_classes_taken ?? totalCompletedModules ?? 0

  // Weekly Cadence (Mon = 0, Sun = 6)
  const currentDayIndex = (new Date().getDay() + 6) % 7
  const weekDays = ['M', 'T', 'W', 'T', 'F', 'S', 'S']

  // Auto-guide companion to primary resume action on dashboard mount (strictly zero emojis)
  useEffect(() => {
    const timer = setTimeout(() => {
      if (activeCourse && activeModule) {
        const actionLabel = isModuleInProgress(activeModule.id) ? 'resume' : 'start'
        triggerCompanionGuidance({
          targetElementId: 'primary-resume-btn',
          expression: 'attentive-left',
          animation: 'listening',
          message: `Ready, ${studentName}? Let's ${actionLabel} "${activeModule.title}"! Tap here to begin our live session.`,
        })
      } else {
        triggerCompanionGuidance({
          targetElementId: 'browse-curriculums-btn',
          expression: 'curious-left',
          animation: 'listening',
          message: `Welcome, ${studentName}! Choose a chapter from your class syllabus to start learning.`,
        })
      }
    }, 1000)

    return () => clearTimeout(timer)
  }, [activeCourse?.id, activeModule?.id, studentName])

  // Pre-calculate enrolled subject card stats from real database records
  const subjectCards = enrolledCurriculums.map((curr, idx) => {
    const cModules = modules.filter((m) => m.curriculum_id === curr.id).sort((a, b) => a.order_index - b.order_index)
    const cCompleted = cModules.filter((m) => isModuleComplete(m.id)).length
    const cTotal = cModules.length
    const cPercent = cTotal > 0 ? Math.round((cCompleted / cTotal) * 100) : 0

    const inProgModule = cModules.find((m) => isModuleInProgress(m.id))
    const nextMod = inProgModule || cModules.find((m) => !isModuleComplete(m.id)) || cModules[0]

    let iconName = 'biotech'
    let statusLabel = cPercent === 100 ? 'Completed' : cPercent > 0 ? 'In Progress' : 'Not Started'
    let statusColor = cPercent > 0 ? 'text-secondary' : 'text-ink-muted'
    let progressBg = 'bg-secondary'
    let unitLabel = nextMod ? `Unit ${nextMod.order_index}: ${nextMod.title.split(':')[0]}` : (curr.category || 'Academic Track')

    if (curr.title.toLowerCase().includes('chem')) {
      iconName = 'science'
      progressBg = 'bg-primary'
    } else if (curr.title.toLowerCase().includes('calc') || curr.title.toLowerCase().includes('math')) {
      iconName = 'functions'
      progressBg = 'bg-ink-primary'
    }

    return {
      curriculum: curr,
      iconName,
      statusLabel,
      statusColor,
      progressBg,
      completedCount: cCompleted,
      totalCount: cTotal,
      percent: cPercent,
      activeTopicTitle: nextMod ? nextMod.title : 'Overview & Fundamentals',
      nextModuleId: nextMod ? nextMod.id : null,
      unitLabel,
    }
  })

  // Handlers
  const handleSavePreferences = async (e: React.FormEvent) => {
    e.preventDefault()
    setSavingPrefs(true)
    const formData = new FormData()
    formData.append('learning_style', selectedStyle)
    formData.append('preferred_pacing', selectedPacing)
    formData.append('preferred_teacher_voice', selectedVoice)
    formData.append('class_level', selectedClass)
    await updatePreferencesAction(formData)
    setSavingPrefs(false)
    setPreferencesOpen(false)
  }

  const handleStartSession = () => {
    if (isFreeQuotaExhausted && (!activeModule?.id || !isModuleComplete(activeModule.id))) {
      setLiveModalOpen(false)
      setPricingModalOpen(true)
      return
    }
    setIsStartingSession(true)
    setTimeout(() => {
      setLiveModalOpen(false)
      if (activeModule?.id) {
        router.push(`/dashboard/${user.id}/class/${activeModule.id}`)
      } else {
        router.push(`/dashboard/${user.id}/class`)
      }
    }, 800)
  }

  // Navigation config shared by the desktop sidebar and the mobile drawer
  const scrollToSection = (id: string) => {
    const el = document.getElementById(id)
    if (el) el.scrollIntoView({ behavior: 'smooth' })
  }
  const navItems: NavItem[] = [
    { id: 'home', label: 'Home', icon: 'home', onSelect: () => setActiveNav('home') },
    {
      id: 'syllabus',
      label: 'Syllabus',
      icon: 'menu_book',
      onSelect: () => {
        setActiveNav('syllabus')
        setSyllabusModalOpen(true)
      },
    },
    {
      id: 'learn',
      label: 'Learn',
      icon: 'auto_stories',
      onSelect: () => {
        setActiveNav('learn')
        scrollToSection('enrolled-subjects-section')
      },
    },
    {
      id: 'practice',
      label: 'Practice',
      icon: 'edit_note',
      onSelect: () => {
        setActiveNav('practice')
        scrollToSection('deliberate-practice-section')
      },
    },
    { id: 'live', label: 'Live Tutor', icon: 'psychology', badge: 'Tutor available', onSelect: () => setLiveModalOpen(true) },
    {
      id: 'progress',
      label: 'Progress',
      icon: 'insights',
      onSelect: () => {
        setActiveNav('progress')
        scrollToSection('consistency-section')
      },
    },
    { id: 'history', label: 'History', icon: 'schedule', onSelect: () => setLiveModalOpen(true) },
  ]

  const hour = new Date().getHours()
  const greeting = hour < 12 ? 'Good morning' : hour < 18 ? 'Good afternoon' : 'Good evening'
  const firstName = studentName.split(' ')[0]

  const iconButtonClass =
    'inline-flex h-10 w-10 cursor-pointer items-center justify-center rounded-lg border border-border-subtle bg-surface text-ink-secondary transition-colors hover:bg-canvas-soft hover:text-ink-primary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm'
  const headerTextButtonClass =
    'inline-flex h-10 min-w-10 cursor-pointer items-center justify-center gap-2 whitespace-nowrap rounded-lg border border-border-subtle bg-surface px-0 text-sm font-medium text-ink-primary transition-colors hover:bg-canvas-soft focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm lg:px-3.5'
  const textButtonClass =
    'inline-flex h-10 cursor-pointer items-center gap-2 whitespace-nowrap rounded-lg border border-border-subtle bg-surface px-3.5 text-sm font-medium text-ink-primary transition-colors hover:bg-canvas-soft focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm'

  return (
    <div className="min-h-full font-body-md text-body-md text-ink-primary bg-canvas botanical-pattern antialiased selection:bg-primary selection:text-white">
      
      {/* ========================================================================= */}
      {/* 1. SIDE NAVIGATION (Desktop Fixed Shell: w-64)                           */}
      {/* ========================================================================= */}
      <aside className="fixed left-0 top-0 z-40 hidden h-screen w-64 flex-col justify-between border-r border-border-subtle bg-canvas p-5 md:flex">
        {/* Top Area: Brand & Navigation */}
        <div className="space-y-8">
          <Link
            href={`/dashboard/${user.id}`}
            className="group flex items-center gap-3 rounded-lg px-1 pt-1 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm"
          >
            <div className="flex h-10 w-10 items-center justify-center rounded-lg border border-border-subtle bg-surface text-secondary shadow-xs transition-transform group-hover:scale-105">
              <span aria-hidden="true" className="material-symbols-outlined text-2xl text-secondary">eco</span>
            </div>
            <div>
              <p className="font-editorial text-2xl leading-none text-ink-primary">Anaxly</p>
              <p className="mt-1 text-xs text-ink-muted">Scholar's Edition</p>
            </div>
          </Link>

          <DashboardNav items={navItems} activeId={activeNav} ariaLabel="Main navigation" />

          <button
            type="button"
            onClick={() => setLiveModalOpen(true)}
            className="flex min-h-11 w-full cursor-pointer items-center justify-center gap-2 rounded-lg bg-primary px-4 py-2.5 text-sm font-semibold text-white shadow-xs transition-colors hover:bg-accent-hover focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm focus-visible:ring-offset-2 focus-visible:ring-offset-canvas"
          >
            <span aria-hidden="true" className="material-symbols-outlined text-lg">mic</span>
            <span>Start session</span>
          </button>
        </div>

{/* Bottom Dock: Student Profile Card & Settings */}
        <div className="space-y-3 pt-6 border-t border-border-subtle">
          <div className="p-2.5 bg-surface rounded-xl border border-border-subtle flex items-center gap-3">
            <div className="relative w-9 h-9 rounded-full bg-surface-container-high border border-border-subtle overflow-hidden flex-shrink-0 flex items-center justify-center">
              {studentAvatar ? (
                <img
                  className="w-full h-full object-cover"
                  alt={studentName}
                  src={studentAvatar}
                />
              ) : (
                <span className="font-semibold text-ink-primary text-sm font-label-md">
                  {studentName.charAt(0).toUpperCase()}
                </span>
              )}
            </div>
            <div className="min-w-0 flex-1">
              <p className="font-label-md text-label-md text-ink-primary truncate font-semibold">
                {studentName}
              </p>
              <p className="font-label-micro text-label-micro text-ink-muted truncate">
                {studentTrack}
              </p>
            </div>
          </div>

          <nav className="space-y-0.5">
            <Link
              href={`/dashboard/${user.id}/settings?tab=account`}
              className="w-full flex items-center gap-3 text-ink-secondary font-label-md text-label-md pl-3 py-2 rounded-lg hover:text-ink-primary hover:bg-surface-container-low/40 transition-colors text-left cursor-pointer"
            >
              <span className="material-symbols-outlined text-lg">person</span>
              <span>Profile</span>
            </Link>
            <Link
              href={`/dashboard/${user.id}/settings?tab=avatars`}
              className="w-full flex items-center gap-3 text-ink-secondary font-label-md text-label-md pl-3 py-2 rounded-lg hover:text-ink-primary hover:bg-surface-container-low/40 transition-colors text-left cursor-pointer"
            >
              <span className="material-symbols-outlined text-lg">settings</span>
              <span>Settings</span>
            </Link>
          </nav>
        </div>
      </aside>

      {/* ========================================================================= */}
      {/* 2. MAIN WORKSPACE & TOP BAR                                               */}
      {/* ========================================================================= */}
      <div className="md:pl-64 flex flex-col min-h-screen">
        
        {/* Top Sticky Bar */}
        <header className="sticky top-0 z-30 flex w-full items-center justify-between gap-3 border-b border-border-subtle bg-canvas/90 px-4 py-3 backdrop-blur-md sm:px-6 md:px-8">
          <div className="flex min-w-0 items-center gap-2">
            <button
              type="button"
              className={`${iconButtonClass} md:hidden`}
              onClick={() => setMobileMenuOpen(true)}
              aria-label="Open navigation menu"
            >
              <span aria-hidden="true" className="material-symbols-outlined">menu</span>
            </button>
            <div className="min-w-0">
              <p className="truncate text-sm text-ink-muted" suppressHydrationWarning>{todayFormatted}</p>
              <h1 className="truncate font-editorial text-2xl leading-tight text-ink-primary" suppressHydrationWarning>
                {greeting}, {firstName}
              </h1>
            </div>
          </div>

          <div className="flex shrink-0 items-center gap-2">
            <button
              id="top-open-syllabus-btn"
              type="button"
              onClick={() => setSyllabusModalOpen(true)}
              className={`${headerTextButtonClass} hidden sm:inline-flex`}
            >
              <span aria-hidden="true" className="material-symbols-outlined text-lg text-secondary">menu_book</span>
              <span className="sr-only lg:not-sr-only">Open syllabus</span>
            </button>

            <Link
              href={`/dashboard/${user.id}/class?mode=focus`}
              onClick={(e) => handleModuleClick(e, activeModule?.id)}
              className={`${headerTextButtonClass} hidden sm:inline-flex`}
            >
              <span aria-hidden="true" className="material-symbols-outlined text-lg text-primary">timer</span>
              <span className="hidden lg:inline">Quick focus</span>
              <span className="sr-only lg:hidden">Quick focus</span>
            </Link>

            <button
              type="button"
              onClick={() => scrollToSection('consistency-section')}
              className={`${iconButtonClass} hidden sm:inline-flex`}
              aria-label="Jump to study calendar"
            >
              <span aria-hidden="true" className="material-symbols-outlined text-xl">calendar_today</span>
            </button>

            <div className="relative">
              <button
                type="button"
                onClick={() => setLiveModalOpen(true)}
                className={iconButtonClass}
                aria-label={memories.length > 0 ? 'Notifications, new items' : 'Notifications'}
              >
                <span aria-hidden="true" className="material-symbols-outlined text-xl">notifications</span>
              </button>
              {memories.length > 0 && (
                <span aria-hidden="true" className="absolute right-1.5 top-1.5 h-2 w-2 rounded-full bg-primary ring-2 ring-canvas" />
              )}
            </div>

            <div className="mx-1 hidden h-6 w-px bg-border-subtle sm:block" />

            <button
              type="button"
              onClick={() => setPreferencesOpen(true)}
              className="flex cursor-pointer items-center gap-2.5 rounded-lg p-1 text-left transition-colors hover:bg-canvas-soft focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm"
              aria-label={`Open preferences for ${studentName}`}
            >
              <div className="flex h-9 w-9 items-center justify-center overflow-hidden rounded-full border border-border-subtle bg-surface">
                {studentAvatar ? (
                  <img className="h-full w-full object-cover" alt="" src={studentAvatar} />
                ) : (
                  <span className="text-sm font-semibold text-ink-primary">{studentName.charAt(0).toUpperCase()}</span>
                )}
              </div>
              <span className="hidden whitespace-nowrap text-sm font-medium text-ink-primary xl:inline-block">{studentName}</span>
            </button>
          </div>
        </header>

{/* ======================================================================= */}
        {/* DASHBOARD CORE CANVAS (DISCOVER → LEARN → PRACTICE → REVIEW LOOP)       */}
        {/* ======================================================================= */}
        <main className="flex-1 px-6 sm:px-10 lg:px-12 py-8 max-w-[1536px] w-full mx-auto space-y-10">
          
          {/* SECTION 1: CONTINUE LEARNING (primary focus of the page) */}
          <section aria-labelledby="continue-heading">
            {activeCourse ? (
              <DashCard tone="primary" size="lg" className="relative overflow-hidden md:p-10">
                <div className="grid grid-cols-1 items-center gap-8 lg:grid-cols-12">
                  <div className="space-y-6 lg:col-span-8">
                    <div className="flex flex-wrap items-center gap-2">
                      <span id="continue-heading" className="text-sm font-medium text-white/80">
                        Continue learning
                      </span>
                      <span className="rounded-full bg-white/10 px-3 py-0.5 text-xs font-medium text-white ring-1 ring-white/25">
                        {activeCourse.title}
                      </span>
                      {isAllCourseCompleted && (
                        <span className="rounded-full bg-accent-sage px-3 py-0.5 text-xs font-medium text-white">
                          Chapter completed
                        </span>
                      )}
                    </div>

                    <div className="space-y-3">
                      <h2 className="font-editorial text-4xl leading-[1.1] text-white md:text-5xl">
                        {activeModule?.title || activeCourse.title}
                      </h2>
                      <p className="max-w-prose text-base leading-relaxed text-white/80">
                        {activeModule?.description
                          ? activeModule.description
                          : activeCourse.description || 'Pick up where you left off.'}
                      </p>
                      <p className="flex items-center gap-1.5 text-sm text-white/70">
                        <span aria-hidden="true" className="material-symbols-outlined text-base">schedule</span>
                        {activeModule?.estimated_minutes ? `${activeModule.estimated_minutes} min remaining` : '15 min remaining'}
                      </p>
                    </div>

                    <div className="flex flex-wrap items-center gap-3">
                      <Link
                        id="primary-resume-btn"
                        className="inline-flex min-h-12 items-center gap-2.5 rounded-lg bg-white px-6 py-3 text-base font-semibold text-accent-primary shadow-xs transition-colors hover:bg-accent-primary-soft focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-offset-2 focus-visible:ring-offset-accent-primary"
                        href={activeModule?.id ? `/dashboard/${user.id}/class/${activeModule.id}` : `/dashboard/${user.id}/class`}
                        onClick={(e) => handleModuleClick(e, activeModule?.id)}
                      >
                        <span aria-hidden="true" className="material-symbols-outlined text-xl" style={{ fontVariationSettings: '"FILL" 1' }}>
                          play_arrow
                        </span>
                        <span>
                          {isAllCourseCompleted
                            ? 'Review chapter'
                            : isModuleInProgress(activeModule?.id || '')
                            ? 'Resume capsule'
                            : 'Start capsule'}
                        </span>
                      </Link>

                      <button
                        id="hero-open-syllabus-btn"
                        type="button"
                        onClick={() => {
                          if (activeCourse) {
                            setSelectedSyllabusCategory(activeCourse.category || 'General')
                            setSelectedSyllabusCurriculumId(activeCourse.id)
                          }
                          setSyllabusModalOpen(true)
                        }}
                        className="inline-flex min-h-12 cursor-pointer items-center gap-2 rounded-lg px-4 py-3 text-sm font-medium text-white ring-1 ring-white/30 transition-colors hover:bg-white/10 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white"
                      >
                        <span aria-hidden="true" className="material-symbols-outlined text-lg">menu_book</span>
                        <span>Open syllabus</span>
                      </button>

                      <button
                        type="button"
                        onClick={() => setNotesDialogOpen(true)}
                        className="inline-flex min-h-12 cursor-pointer items-center gap-1.5 rounded-lg px-1 py-3 text-sm font-medium text-white/90 sm:px-3 underline-offset-4 transition-colors hover:text-white hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white"
                      >
                        <span>Chapter notes</span>
                        <span aria-hidden="true" className="material-symbols-outlined text-base">arrow_forward</span>
                      </button>
                    </div>
                  </div>

                  {/* Progress ring */}
                  <div className="flex items-center gap-5 lg:col-span-4 lg:justify-end">
                    <div
                      className="relative h-32 w-32 shrink-0"
                      role="img"
                      aria-label={`${activePercentComplete}% of ${activeCourse.title} complete`}
                    >
                      <svg viewBox="0 0 120 120" className="h-full w-full -rotate-90">
                        <circle cx="60" cy="60" r="52" fill="none" stroke="rgba(255,255,255,0.18)" strokeWidth="10" />
                        <circle
                          cx="60"
                          cy="60"
                          r="52"
                          fill="none"
                          stroke="#FFFFFF"
                          strokeWidth="10"
                          strokeLinecap="round"
                          strokeDasharray={2 * Math.PI * 52}
                          strokeDashoffset={2 * Math.PI * 52 * (1 - Math.min(100, Math.max(0, activePercentComplete)) / 100)}
                          className="transition-all duration-500 ease-out"
                        />
                      </svg>
                      <div className="absolute inset-0 flex flex-col items-center justify-center">
                        <span className="text-3xl font-semibold tabular-nums leading-none text-white">{activePercentComplete}%</span>
                        <span className="mt-1 text-xs text-white/70">complete</span>
                      </div>
                    </div>
                    <p className="text-sm leading-snug text-white/80 lg:hidden xl:block">
                      {activeModuleIndex > 0 ? `Capsule ${activeModuleIndex} of ${activeModuleTotal}` : activeCourse.title}
                    </p>
                  </div>
                </div>
              </DashCard>
            ) : (
              <DashCard size="lg" className="space-y-5 md:p-10">
                <div className="flex h-12 w-12 items-center justify-center rounded-lg border border-border-subtle bg-canvas-soft text-secondary">
                  <span aria-hidden="true" className="material-symbols-outlined text-2xl">school</span>
                </div>
                <div className="space-y-2">
                  <h2 id="continue-heading" className="font-editorial text-4xl leading-tight text-ink-primary">
                    Choose a course to begin
                  </h2>
                  <p className="max-w-prose text-base text-ink-secondary">
                    You have not enrolled in a curriculum yet. Browse the published courses or open the syllabus to get started.
                  </p>
                </div>
                <div className="flex flex-wrap items-center gap-3">
                  <button
                    id="browse-curriculums-btn"
                    type="button"
                    onClick={() => setCoursesDialogOpen(true)}
                    className="inline-flex min-h-12 cursor-pointer items-center gap-2 rounded-lg bg-primary px-6 py-3 font-semibold text-white shadow-xs transition-colors hover:bg-accent-hover focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm focus-visible:ring-offset-2"
                  >
                    <span aria-hidden="true" className="material-symbols-outlined text-lg">add</span>
                    <span>Browse courses</span>
                  </button>
                  <button
                    type="button"
                    onClick={() => setSyllabusModalOpen(true)}
                    className={`${textButtonClass} min-h-12`}
                  >
                    <span aria-hidden="true" className="material-symbols-outlined text-lg text-secondary">menu_book</span>
                    <span>Open syllabus</span>
                  </button>
                </div>
              </DashCard>
            )}
          </section>

          {/* SECTION 2: STUDY RHYTHM (stats, activity chart, weekly streak) */}
          <section id="consistency-section" aria-labelledby="rhythm-heading" className="space-y-5">
            <SectionHeader
              title={<span id="rhythm-heading">Your study rhythm</span>}
              description="How consistently you have studied over the last two weeks."
            />

            <div className="grid grid-cols-1 gap-5 lg:grid-cols-12">
              <DashCard size="md" className="lg:col-span-5">
                <DailyActivityChart records={progressRecords} />
              </DashCard>

              <div className="grid grid-cols-2 gap-4 lg:col-span-7">
                <StatTile
                  label="Day streak"
                  value={currentStreak}
                  unit={currentStreak === 1 ? 'day' : 'days'}
                  hint={currentStreak > 0 ? 'Keep it going today' : 'Start your streak today'}
                />
                <StatTile
                  label="Hours studied"
                  value={studyHours}
                  unit="hrs"
                  hint={Number(studyHours) > 0 ? 'Across all sessions' : 'No study time recorded yet'}
                />
                <StatTile
                  role="button"
                  tabIndex={0}
                  onClick={() => setSyllabusModalOpen(true)}
                  onKeyDown={(e: React.KeyboardEvent) => {
                    if (e.key === 'Enter' || e.key === ' ') {
                      e.preventDefault()
                      setSyllabusModalOpen(true)
                    }
                  }}
                  className="cursor-pointer transition-colors hover:border-ink-muted focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm"
                  aria-label={`Syllabus covered: ${overallPercentComplete}%. Open the syllabus.`}
                  label="Syllabus covered"
                  value={`${overallPercentComplete}%`}
                  icon={<span aria-hidden="true" className="material-symbols-outlined text-lg text-ink-muted">menu_book</span>}
                  hint={
                    <span className="mt-1 block h-1.5 w-full overflow-hidden rounded-full bg-border-subtle">
                      <span
                        className="block h-full rounded-full bg-secondary transition-all duration-500 ease-out"
                        style={{ width: `${overallPercentComplete}%` }}
                      />
                    </span>
                  }
                />
                <StatTile
                  label="Lessons mastered"
                  value={totalMasteryLessons}
                  hint={totalMasteryLessons > 0 ? 'Verified by mastery checks' : 'Complete a capsule to begin'}
                />
              </div>
            </div>

            {/* Weekly streak: derived from currentStreak and today's weekday */}
            <DashCard tone="soft" size="sm" className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
              <div className="flex flex-wrap items-center gap-x-4 gap-y-2">
                <span className="text-sm font-medium text-ink-primary">This week</span>
                <ul className="flex items-center gap-1.5" aria-label="Study days this week">
                  {weekDays.map((day, idx) => {
                    const isToday = idx === currentDayIndex
                    const isChecked = currentStreak > 0 && idx < currentStreak && idx <= currentDayIndex
                    const base = 'flex h-9 w-9 items-center justify-center rounded-full text-xs font-semibold'
                    const state = isChecked || (isToday && currentStreak > 0)
                      ? 'bg-accent-primary text-on-primary'
                      : 'border border-dashed border-border-strong text-ink-muted'
                    return (
                      <li
                        key={idx}
                        className={`${base} ${state} ${isToday ? 'ring-2 ring-accent-warm ring-offset-2 ring-offset-canvas-soft' : ''}`}
                        aria-label={`${day}${isToday ? ' (today)' : ''}: ${isChecked || (isToday && currentStreak > 0) ? 'studied' : 'not studied'}`}
                      >
                        {isChecked || (isToday && currentStreak > 0) ? (
                          <span aria-hidden="true" className="material-symbols-outlined text-base leading-none">check</span>
                        ) : (
                          <span aria-hidden="true">{day}</span>
                        )}
                      </li>
                    )
                  })}
                </ul>
              </div>
              <p className="flex items-center gap-2 text-sm text-ink-secondary">
                <span aria-hidden="true" className="material-symbols-outlined text-lg text-accent-sage">verified</span>
                <span>
                  {currentStreak > 0 ? 'On track for your exams' : 'Complete a study session to start your week'}
                </span>
              </p>
            </DashCard>
          </section>

{/* SECTION 2B: DYNAMIC ADAPTIVE EXAM STUDY PLANNER */}
          <StudyPlannerCard
            userId={user.id}
            studyPlan={studyPlan}
            totalModulesCount={modules.length}
            completedModulesCount={totalCompletedModules}
            nextModuleId={activeModule?.id || null}
            onModuleClick={handleModuleClick}
          />

          {/* SECTION 3: TODAY'S STRUCTURED LEARNING PLAN */}
          <section className="grid grid-cols-1 lg:grid-cols-12 gap-8">
            <div className="lg:col-span-12 space-y-4">
              <div className="flex items-baseline justify-between">
                <div>
                  <h3 className="font-editorial text-2xl text-ink-primary leading-tight">
                    Today's Learning Plan
                  </h3>
                  <p className="text-sm text-ink-secondary mt-0.5">
                    Prioritized tasks to maintain academic cadence.
                  </p>
                </div>
                <span className="text-xs font-mono text-ink-muted font-medium">
                  {activeModule ? '3 of 3 Pending' : '0 Pending'}
                </span>
              </div>

              {activeModule ? (
                <div className="space-y-3.5">
                  {/* Task 1: Lesson */}
                  <div className="group bg-surface rounded-2xl border border-border-subtle p-5 md:p-6 transition-all hover:border-ink-muted flex flex-col sm:flex-row sm:items-center justify-between gap-4 shadow-soft">
                    <div className="flex items-start gap-4">
                      <div className="w-10 h-10 rounded-xl bg-surface-container-low border border-border-subtle flex items-center justify-center text-primary flex-shrink-0 mt-0.5">
                        <span className="material-symbols-outlined text-xl">menu_book</span>
                      </div>
                      <div>
                        <div className="flex items-center gap-2">
                          <span className="text-xs font-medium text-primary uppercase tracking-wide">
                            Lesson
                          </span>
                          <span className="text-ink-muted text-xs">
                            • Est. {activeModule.estimated_minutes || 20} min
                          </span>
                        </div>
                        <h4 className="text-base font-semibold text-ink-primary mt-0.5 group-hover:text-primary transition-colors">
                          Complete {activeModule.title}
                        </h4>
                        <p className="text-sm text-ink-secondary mt-0.5 leading-relaxed">
                          {activeModule.description || 'Core instructional module review with Anaxly.'}
                        </p>
                      </div>
                    </div>
                    <Link
                      href={activeModule?.id ? `/dashboard/${user.id}/class/${activeModule.id}` : `/dashboard/${user.id}/class`}
                      onClick={(e) => handleModuleClick(e, activeModule?.id)}
                      className="sm:self-center flex-shrink-0 px-5 py-2.5 rounded-xl bg-primary hover:bg-accent-hover text-white font-medium text-sm transition-colors text-center shadow-xs"
                    >
                      Continue
                    </Link>
                  </div>

                  {/* Task 2: Practice & 10 MCQs Mastery */}
                  <div className="group bg-surface rounded-2xl border border-border-subtle p-5 md:p-6 transition-all hover:border-ink-muted flex flex-col sm:flex-row sm:items-center justify-between gap-4 shadow-soft">
                    <div className="flex items-start gap-4">
                      <div className="w-10 h-10 rounded-xl bg-surface-container-low border border-border-subtle flex items-center justify-center text-secondary flex-shrink-0 mt-0.5">
                        <span className="material-symbols-outlined text-xl">psychology_alt</span>
                      </div>
                      <div>
                        <div className="flex items-center gap-2">
                          <span className="text-xs font-medium text-secondary uppercase tracking-wide">
                            Mastery Evaluation
                          </span>
                          <span className="text-ink-muted text-xs">• 10 Gemini MCQs • Advances Syllabus Progress</span>
                        </div>
                        <h4 className="text-base font-semibold text-ink-primary mt-0.5 group-hover:text-secondary transition-colors">
                          10 Mastery Questions: {activeModule.title}
                        </h4>
                        <p className="text-sm text-ink-secondary mt-0.5 leading-relaxed">
                          Direct test on core textbook formulas and principles. Scoring 70%+ completes this capsule and unlocks the next section.
                        </p>
                      </div>
                    </div>
                    <button
                      id="open-quiz-btn"
                      onClick={() => setQuizModalOpen(true)}
                      className="sm:self-center flex-shrink-0 px-6 py-2.5 rounded-xl bg-secondary/10 hover:bg-secondary/20 text-secondary text-sm font-semibold transition-colors text-center cursor-pointer border border-secondary/20 shadow-xs active:scale-95"
                    >
                      Take 10 MCQs
                    </button>
                  </div>

                  {/* Task 3: Review */}
                  <div className="group bg-surface rounded-2xl border border-border-subtle p-5 md:p-6 transition-all hover:border-ink-muted flex flex-col sm:flex-row sm:items-center justify-between gap-4 shadow-soft">
                    <div className="flex items-start gap-4">
                      <div className="w-10 h-10 rounded-xl bg-surface-container-low border border-border-subtle flex items-center justify-center text-ink-secondary flex-shrink-0 mt-0.5">
                        <span className="material-symbols-outlined text-xl">history_edu</span>
                      </div>
                      <div>
                        <div className="flex items-center gap-2">
                          <span className="text-xs font-medium text-ink-muted uppercase tracking-wide">
                            Review
                          </span>
                          <span className="text-ink-muted text-xs">• 5 min flash review</span>
                        </div>
                        <h4 className="text-base font-semibold text-ink-primary mt-0.5">
                          {(() => {
                            const memorySnippet = (memories[0]?.memory_text || memories[0]?.content || '').trim()
                            return memorySnippet
                              ? `Spaced Repetition: ${memorySnippet.slice(0, 42)}...`
                              : `Spaced Repetition: ${activeCourse.title} Concepts`
                          })()}
                        </h4>
                        <p className="text-sm text-ink-secondary mt-0.5 leading-relaxed">
                          Keep key concepts from your recent sessions fresh with a quick review.
                        </p>
                      </div>
                    </div>
                    <Link
                      href={`/dashboard/${user.id}/class?mode=review`}
                      onClick={(e) => handleModuleClick(e)}
                      className="sm:self-center flex-shrink-0 px-5 py-2.5 rounded-xl border border-border-subtle bg-surface hover:bg-canvas-soft text-ink-primary text-sm font-medium transition-colors text-center shadow-xs"
                    >
                      Quick Review
                    </Link>
                  </div>
                </div>
              ) : (
                <div className="p-8 text-center bg-surface rounded-2xl border border-border-subtle shadow-soft space-y-3">
                  <span className="material-symbols-outlined text-3xl text-ink-muted">playlist_add_check</span>
                  <p className="font-editorial text-xl text-ink-primary">No Pending Tasks</p>
                  <p className="text-sm text-ink-secondary max-w-sm mx-auto">
                    Enroll in a curriculum to generate a personalized daily deliberate practice plan.
                  </p>
                  <button
                    onClick={() => setCoursesDialogOpen(true)}
                    className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-primary text-white font-medium text-sm hover:bg-accent-hover cursor-pointer shadow-xs"
                  >
                    <span>Browse Courses</span>
                  </button>
                </div>
              )}
            </div>
          </section>

          {/* SECTION 3B: WEAK-CONCEPT REVISION SPOTLIGHT */}
          <WeakConceptsReviewCard
            userId={user.id}
            modules={modules}
            progressRecords={progressRecords}
            onModuleClick={handleModuleClick}
          />

          {/* SECTION 4: ENROLLED SUBJECTS & SCHOLAR TRACKS */}
          <section id="enrolled-subjects-section" className="space-y-5">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="font-editorial text-2xl text-ink-primary leading-tight">
                  Enrolled Subjects
                </h3>
                <p className="text-sm text-ink-secondary mt-0.5">
                  Curriculum status across your active academic courses.
                </p>
              </div>
              <div className="flex items-center gap-3">
                <button
                  onClick={() => setSyllabusModalOpen(true)}
                  className="text-xs text-ink-secondary hover:text-ink-primary font-medium inline-flex items-center gap-1.5 cursor-pointer transition-colors"
                >
                  <span className="material-symbols-outlined text-base text-secondary">menu_book</span>
                  <span>Open Syllabus</span>
                </button>
                <button
                  onClick={() => setCoursesDialogOpen(true)}
                  className="text-xs text-primary hover:text-accent-hover font-semibold inline-flex items-center gap-1 cursor-pointer"
                >
                  <span>Manage Courses</span>
                  <span className="material-symbols-outlined text-base">chevron_right</span>
                </button>
              </div>
            </div>

            {subjectCards.length > 0 ? (
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {subjectCards.map((card, idx) => (
                  <div
                    key={card.curriculum.id || idx}
                    className="bg-surface rounded-2xl border border-border-subtle p-6 shadow-soft flex flex-col justify-between hover:border-ink-muted transition-colors"
                  >
                    <div className="space-y-4">
                      <div className="flex items-center justify-between">
                        <span className="w-9 h-9 rounded-xl bg-surface-container-low border border-border-subtle flex items-center justify-center text-secondary">
                          <span className="material-symbols-outlined text-xl">{card.iconName}</span>
                        </span>
                        <span className={`text-xs ${card.statusColor} font-semibold`}>
                          {card.statusLabel}
                        </span>
                      </div>

                      <div>
                        <h4 className="text-base font-semibold text-ink-primary">
                          {card.curriculum.title}
                        </h4>
                        <p className="text-xs text-ink-secondary mt-1 leading-relaxed">
                          {card.completedCount} of {card.totalCount} chapters completed · Active topic: {card.activeTopicTitle.split(':')[0]}.
                        </p>
                      </div>

                      {/* Progress bar */}
                      <div className="space-y-1.5 pt-2">
                        <div className="flex justify-between text-xs text-ink-muted">
                          <span>Syllabus Completed</span>
                          <span className="text-ink-primary font-medium">{card.percent}%</span>
                        </div>
                        <div className="w-full h-1.5 rounded-full bg-border-subtle overflow-hidden">
                          <div
                            className={`h-full ${card.progressBg} rounded-full transition-all duration-500`}
                            style={{ width: `${card.percent}%` }}
                          />
                        </div>
                      </div>
                    </div>

                    <div className="pt-6 mt-4 border-t border-border-subtle flex items-center justify-between">
                      <button
                        onClick={() => {
                          setSelectedSyllabusCategory(card.curriculum.category || 'General')
                          setSelectedSyllabusCurriculumId(card.curriculum.id)
                          setSyllabusModalOpen(true)
                        }}
                        className="text-xs text-ink-secondary hover:text-ink-primary font-medium inline-flex items-center gap-1.5 cursor-pointer transition-colors"
                      >
                        <span className="material-symbols-outlined text-base text-secondary">menu_book</span>
                        <span>Open Syllabus</span>
                      </button>
                      <Link
                        className="text-xs text-ink-primary hover:text-primary font-medium inline-flex items-center gap-1"
                        href={card.nextModuleId ? `/dashboard/${user.id}/class/${card.nextModuleId}` : `/dashboard/${user.id}/class`}
                        onClick={(e) => handleModuleClick(e, card.nextModuleId || activeModule?.id)}
                      >
                        <span>Enter Subject</span>
                        <span className="material-symbols-outlined text-sm">arrow_forward</span>
                      </Link>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="p-8 text-center bg-surface rounded-2xl border border-border-subtle space-y-3">
                <span className="material-symbols-outlined text-3xl text-ink-muted">menu_book</span>
                <p className="font-headline-sm text-ink-primary">No Enrolled Subjects</p>
                <p className="font-body-md text-ink-secondary text-sm max-w-sm mx-auto">
                  You are not currently enrolled in any subjects. Enroll now to track syllabus mastery and deliberate practice blocks.
                </p>
                <button
                  onClick={() => setCoursesDialogOpen(true)}
                  className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-primary text-white font-semibold font-label-md text-sm hover:bg-accent-hover cursor-pointer"
                >
                  <span className="material-symbols-outlined text-sm">add</span>
                  <span>Browse Available Subjects</span>
                </button>
              </div>
            )}
          </section>

          {/* SECTION 5: DELIBERATE PRACTICE & PAST YEAR QUESTIONS (PYQ) HUB */}
          <section id="deliberate-practice-section" className="grid grid-cols-1 lg:grid-cols-12 gap-8 pb-12">
            <div className="lg:col-span-5 bg-surface rounded-3xl border border-border-subtle p-7 md:p-8 shadow-soft flex flex-col justify-between">
              <div className="space-y-5">
                <div className="flex items-center justify-between">
                  <span className="text-xs text-ink-muted font-medium">
                    Practice Diagnostic
                  </span>
                  <span className="material-symbols-outlined text-ink-muted text-xl">tune</span>
                </div>
                <div>
                  <h4 className="font-editorial text-2xl text-ink-primary leading-tight">
                    Deliberate Question Bank
                  </h4>
                  <p className="text-sm text-ink-secondary mt-1.5 leading-relaxed">
                    Target high-yield exam question types calibrated dynamically to your weaker diagnostic areas.
                  </p>
                </div>

                {/* Subject Toggle Chips */}
                <div className="space-y-2 pt-1">
                  <span className="text-xs text-ink-muted font-medium">
                    Select Discipline
                  </span>
                  <div className="flex flex-wrap gap-2">
                    {availableDisciplines.map((discipline) => {
                      const isSelected = selectedDiscipline === discipline
                      return (
                        <button
                          key={discipline}
                          onClick={() => setSelectedDiscipline(discipline)}
                          className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-colors cursor-pointer ${
                            isSelected
                              ? 'bg-ink-primary text-white'
                              : 'border border-border-subtle bg-canvas hover:bg-surface text-ink-secondary'
                          }`}
                        >
                          {discipline}
                        </button>
                      )
                    })}
                  </div>
                </div>
              </div>

              <div className="pt-6 mt-6 border-t border-border-subtle">
                <Link
                  href={`/dashboard/${user.id}/class?mode=diagnostic&discipline=${encodeURIComponent(selectedDiscipline)}`}
                  onClick={(e) => handleModuleClick(e)}
                  className="w-full flex items-center justify-center gap-2 border border-border-subtle bg-surface hover:bg-canvas-soft text-ink-primary py-2.5 rounded-xl text-sm font-medium transition-colors text-center shadow-xs"
                >
                  <span className="material-symbols-outlined text-lg">edit_document</span>
                  <span>Launch Custom 15-Question Set</span>
                </Link>
              </div>
            </div>

            {/* Chapter Past Year Questions (PYQ) Practice Hub */}
            <div className="lg:col-span-7 bg-surface rounded-3xl border border-border-subtle p-7 md:p-8 shadow-soft flex flex-col justify-between space-y-5">
              <div>
                <div className="flex items-center justify-between">
                  <span className="text-xs font-medium text-secondary flex items-center gap-1.5">
                    <span className="w-2 h-2 rounded-full bg-secondary" />
                    <span>Board Exam PYQ Practice Hub</span>
                  </span>
                  {chapterPyqsData && (
                    <span className="text-xs font-mono text-ink-muted bg-surface-container-low px-2.5 py-1 rounded-full border border-border-subtle">
                      {chapterPyqsData.practice_set?.length || 0} Questions
                    </span>
                  )}
                </div>

                <div className="mt-3 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                  <div>
                    <h4 className="font-editorial text-2xl text-ink-primary leading-tight">
                      Chapter Previous Year Questions
                    </h4>
                    <p className="text-xs text-ink-secondary mt-1 leading-relaxed">
                      Authentic board examination problems with step-by-step chalkboard derivations.
                    </p>
                  </div>

                  {/* Chapter Selector Dropdown */}
                  {allCurriculums.length > 0 && (
                    <select
                      value={selectedPyqChapterId || ''}
                      onChange={(e) => setSelectedPyqChapterId(e.target.value)}
                      className="h-9 px-3 rounded-xl bg-canvas border border-border-subtle text-xs text-ink-primary focus:outline-none focus:border-secondary font-sans cursor-pointer max-w-[210px] truncate"
                    >
                      {allCurriculums.map((c) => (
                        <option key={c.id} value={c.id}>
                          {c.title}
                        </option>
                      ))}
                    </select>
                  )}
                </div>

                {/* Mark Allocation Filter Chips */}
                <div className="flex flex-wrap items-center gap-2 mt-4">
                  <span className="text-xs text-ink-muted font-medium">Filter:</span>
                  {(['all', '1', '2', '3', '5'] as const).map((m) => (
                    <button
                      key={m}
                      onClick={() => setPyqMarkFilter(m)}
                      className={`px-2.5 py-1 rounded-lg text-xs font-mono transition-colors cursor-pointer ${
                        pyqMarkFilter === m
                          ? 'bg-secondary text-white font-bold'
                          : 'bg-canvas text-ink-secondary border border-border-subtle hover:text-ink-primary'
                      }`}
                    >
                      {m === 'all' ? 'All Marks' : `${m} Mark${m !== '1' ? 's' : ''}`}
                    </button>
                  ))}
                </div>
              </div>

              {/* Questions List */}
              <div className="space-y-3 min-h-[220px] max-h-[340px] overflow-y-auto pr-1">
                {isLoadingPyqs ? (
                  <div className="py-12 text-center text-xs font-mono text-ink-muted">
                    Loading authentic board exam questions...
                  </div>
                ) : chapterPyqsData && chapterPyqsData.practice_set?.length > 0 ? (
                  (() => {
                    const filteredQuestions = chapterPyqsData.practice_set.filter((q: any) =>
                      pyqMarkFilter === 'all' ? true : String(q.marks) === pyqMarkFilter
                    )

                    if (filteredQuestions.length === 0) {
                      return (
                        <div className="py-8 text-center text-xs font-mono text-ink-muted">
                          No {pyqMarkFilter}-mark questions in this practice set.
                        </div>
                      )
                    }

                    const matchingModule = modules.find((m) => m.curriculum_id === selectedPyqChapterId) || activeModule

                    return filteredQuestions.map((q: any, idx: number) => (
                      <div
                        key={q.id || idx}
                        className="p-4 rounded-2xl bg-canvas border border-border-subtle space-y-2 hover:border-secondary/40 transition-colors"
                      >
                        <div className="flex items-center justify-between gap-2">
                          <span className="px-2 py-0.5 rounded bg-surface text-secondary text-[11px] font-mono border border-secondary/20 font-bold">
                            {q.year || 'Board Exam'}
                          </span>
                          <span className="px-2 py-0.5 rounded bg-surface text-ink-primary text-[11px] font-mono border border-border-subtle">
                            {q.marks || 1} Mark{(q.marks || 1) > 1 ? 's' : ''}
                          </span>
                        </div>

                        <p className="text-xs text-ink-primary font-medium leading-relaxed">
                          {q.question}
                        </p>

                        <div className="pt-2 flex items-center justify-between border-t border-border-subtle/60 text-xs">
                          <span className="text-[11px] font-mono text-ink-muted">
                            {q.topic || 'Core Concept'}
                          </span>
                          {matchingModule && (
                            <Link
                              href={`/dashboard/${user.id}/class/${matchingModule.id}?pyqQuestion=${encodeURIComponent(q.question)}`}
                              onClick={(e) => handleModuleClick(e, matchingModule.id)}
                              className="text-xs font-medium text-secondary hover:underline flex items-center gap-1"
                            >
                              <span>Solve on Chalkboard</span>
                              <span className="material-symbols-outlined text-sm">arrow_forward</span>
                            </Link>
                          )}
                        </div>
                      </div>
                    ))
                  })()
                ) : (
                  <div className="py-12 text-center rounded-2xl bg-canvas border border-border-subtle text-xs text-ink-muted font-mono">
                    No past year questions uploaded for this chapter yet. Upload question papers in Admin Studio!
                  </div>
                )}
              </div>
            </div>
          </section>
        </main>

        {/* Quiet Editorial Footer */}
        <footer className="border-t border-border-subtle bg-canvas px-6 md:px-10 py-8 text-center text-ink-muted font-label-micro text-label-micro max-w-7xl mx-auto w-full flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <span className="material-symbols-outlined text-secondary text-lg">eco</span>
            <span>Anaxly Scholar's Edition · Classical Intelligence</span>
          </div>
          <div>
            <span>Curriculum aligned with CBSE, ICSE, and IB standards</span>
          </div>
        </footer>
      </div>

      {/* ========================================================================= */}
      {/* 3. MODAL: LIVE AI TUTOR SOCRATIC DIALOGUE PREVIEW                         */}
      {/* ========================================================================= */}
      {liveModalOpen && (
        <div className="fixed inset-0 z-50 bg-ink-primary/30 backdrop-blur-xs flex items-center justify-center p-4 animate-in fade-in duration-200">
          <div className="bg-surface rounded-3xl border border-border-subtle max-w-lg w-full p-8 shadow-card relative">
            {/* Close button */}
            <button
              className="absolute top-6 right-6 p-2 rounded-full text-ink-muted hover:text-ink-primary hover:bg-canvas transition-colors cursor-pointer"
              onClick={() => setLiveModalOpen(false)}
            >
              <span className="material-symbols-outlined text-xl">close</span>
            </button>

            {/* Modal Header */}
            <div className="space-y-3">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-secondary/10 border border-secondary/20 text-secondary text-xs font-mono font-medium">
                <span className="w-2 h-2 rounded-full bg-secondary animate-pulse" />
                <span>Connecting to Neural Tutor Core</span>
              </div>
              <h3 className="font-editorial text-2xl text-ink-primary leading-tight">
                {activeCourse ? `Ready to explore ${activeModule?.title || activeCourse.title}?` : 'Ready to begin your study session?'}
              </h3>
              <p className="text-sm text-ink-secondary leading-relaxed">
                {(() => {
                  const memorySnippet = (memories[0]?.memory_text || memories[0]?.content || '').trim()
                  if (memorySnippet) {
                    return `Anaxly has synthesized your recent sessions: "${memorySnippet.slice(0, 110)}..."`
                  }
                  if (activeModule?.description) {
                    return `Beginning with ${activeModule.title}. Reviewing foundational concepts and interactive socratic problems.`
                  }
                  return 'Anaxly is ready for interactive dialogue, concept clarification, and deliberate practice.'
                })()}
              </p>
            </div>

            {/* Audio wave animation placeholder simulation */}
            <div className="my-6 p-6 rounded-2xl bg-canvas border border-border-subtle flex flex-col items-center justify-center space-y-3 text-center">
              <div className="flex items-center justify-center gap-1.5 h-10">
                <span className="w-1.5 h-4 bg-secondary rounded-full animate-bounce" style={{ animationDelay: '0.1s' }} />
                <span className="w-1.5 h-8 bg-secondary rounded-full animate-bounce" style={{ animationDelay: '0.2s' }} />
                <span className="w-1.5 h-10 bg-primary rounded-full animate-bounce" style={{ animationDelay: '0.3s' }} />
                <span className="w-1.5 h-6 bg-secondary rounded-full animate-bounce" style={{ animationDelay: '0.4s' }} />
                <span className="w-1.5 h-3 bg-secondary rounded-full animate-bounce" style={{ animationDelay: '0.5s' }} />
              </div>
              <span className="text-xs font-mono text-ink-muted uppercase tracking-wider">
                Microphone calibrated &amp; clear
              </span>
            </div>

            {/* Action buttons */}
            <div className="flex items-center gap-3 pt-2">
              <button
                className="flex-1 py-2.5 px-4 rounded-xl border border-border-subtle text-ink-primary text-sm font-medium hover:bg-canvas-soft transition-colors cursor-pointer shadow-xs"
                onClick={() => setLiveModalOpen(false)}
              >
                Cancel
              </button>
              <button
                disabled={isStartingSession}
                onClick={handleStartSession}
                className="flex-1 py-2.5 px-4 rounded-xl bg-primary hover:bg-accent-hover text-white text-sm font-semibold transition-colors flex items-center justify-center gap-2 shadow-xs cursor-pointer"
              >
                <span className="material-symbols-outlined text-lg">mic</span>
                <span>{isStartingSession ? 'Connecting...' : 'Begin Conversation'}</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* 4. MODAL: CHAPTER NOTES DIALOG                                            */}
      {/* ========================================================================= */}
      <Dialog open={notesDialogOpen} onOpenChange={setNotesDialogOpen}>
        <DialogContent className="max-w-xl bg-surface border-border-subtle rounded-3xl p-7 text-ink-primary shadow-2xl">
          <DialogHeader>
            <DialogTitle className="font-headline-md text-2xl text-ink-primary">
              {activeModule?.title || 'Chapter Notes'}
            </DialogTitle>
            <DialogDescription className="font-body-md text-ink-secondary">
              Summary and foundational concepts for the current module.
            </DialogDescription>
          </DialogHeader>

          <div className="space-y-4 my-2">
            <div className="p-4 rounded-2xl bg-canvas border border-border-subtle space-y-2 max-h-60 overflow-y-auto">
              <span className="font-label-micro text-xs uppercase tracking-wider text-ink-muted">
                Core Topic Overview & Master Notes
              </span>
              <p className="font-body-md text-ink-primary text-sm whitespace-pre-line">
                {activeModule?.chapter_notes || activeModule?.description || 'Foundational concepts and principles for this chapter.'}
              </p>
            </div>

            {activeModule?.key_concepts && activeModule.key_concepts.length > 0 && (
              <div className="space-y-2">
                <span className="font-label-micro text-xs uppercase tracking-wider text-ink-muted">
                  Key Concepts
                </span>
                <div className="flex flex-wrap gap-2">
                  {activeModule.key_concepts.map((concept, idx) => (
                    <span
                      key={idx}
                      className="px-3 py-1 rounded-lg bg-surface-container-low border border-border-subtle text-xs font-label-md text-ink-primary"
                    >
                      {concept}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </div>

          <DialogFooter className="flex gap-2">
            <button
              onClick={() => setNotesDialogOpen(false)}
              className="px-4 py-2 rounded-xl border border-border-subtle text-ink-primary font-label-md hover:bg-canvas cursor-pointer"
            >
              Close
            </button>
            <Link
              href={activeModule?.id ? `/dashboard/${user.id}/class/${activeModule.id}` : `/dashboard/${user.id}/class`}
              onClick={(e) => {
                handleModuleClick(e, activeModule?.id)
                if (isFreeQuotaExhausted && (!activeModule?.id || !isModuleComplete(activeModule.id))) {
                  setNotesDialogOpen(false)
                }
              }}
              className="px-5 py-2 rounded-xl bg-primary text-white font-semibold font-label-md hover:bg-accent-hover text-center"
            >
              Open Live Session
            </Link>
          </DialogFooter>
        </DialogContent>
      </Dialog>

      {/* ========================================================================= */}
      {/* 5. MODAL: SETTINGS & PREFERENCES DIALOG                                  */}
      {/* ========================================================================= */}
      <Dialog open={preferencesOpen} onOpenChange={setPreferencesOpen}>
        <DialogContent className="max-w-md bg-surface border-border-subtle rounded-3xl p-7 text-ink-primary shadow-2xl">
          <DialogHeader>
            <DialogTitle className="font-headline-md text-2xl text-ink-primary">
              Student Preferences
            </DialogTitle>
            <DialogDescription className="font-body-md text-ink-secondary text-sm">
              Tune your Anaxly voice, pedagogical model, and pacing.
            </DialogDescription>
          </DialogHeader>

          <form onSubmit={handleSavePreferences} className="space-y-4 my-2">
            {/* Preferred Voice */}
            <div className="space-y-1.5">
              <Label className="font-label-micro text-xs uppercase text-ink-muted">
                Tutor Voice
              </Label>
              <select
                value={selectedVoice}
                onChange={(e) => setSelectedVoice(e.target.value)}
                className="w-full p-2.5 rounded-xl border border-border-subtle bg-surface text-ink-primary text-sm focus:outline-hidden focus:ring-2 focus:ring-primary/20"
              >
                {VOICE_OPTIONS.map((v) => (
                  <option key={v.id} value={v.id}>
                    {v.name} — {v.desc}
                  </option>
                ))}
              </select>
            </div>

            {/* Learning Style */}
            <div className="space-y-1.5">
              <Label className="font-label-micro text-xs uppercase text-ink-muted">
                Pedagogical Style
              </Label>
              <select
                value={selectedStyle}
                onChange={(e) => setSelectedStyle(e.target.value)}
                className="w-full p-2.5 rounded-xl border border-border-subtle bg-surface text-ink-primary text-sm focus:outline-hidden focus:ring-2 focus:ring-primary/20"
              >
                <option value="socratic">Socratic (Questions &amp; Guided Discovery)</option>
                <option value="direct">Direct (Concise &amp; Factual)</option>
                <option value="visual">Visual (Diagrams &amp; Analogies)</option>
                <option value="storytelling">Storytelling (Contextual Narrative)</option>
              </select>
            </div>

            {/* Pacing */}
            <div className="space-y-1.5">
              <Label className="font-label-micro text-xs uppercase text-ink-muted">
                Instruction Pacing
              </Label>
              <select
                value={selectedPacing}
                onChange={(e) => setSelectedPacing(e.target.value)}
                className="w-full p-2.5 rounded-xl border border-border-subtle bg-surface text-ink-primary text-sm focus:outline-hidden focus:ring-2 focus:ring-primary/20"
              >
                <option value="slow_and_thorough">Slow &amp; Thorough</option>
                <option value="standard">Standard</option>
                <option value="fast_and_high_level">Fast &amp; High-Level</option>
              </select>
            </div>

            {/* Class / Grade Level */}
            <div className="space-y-1.5">
              <Label className="font-label-micro text-xs uppercase text-ink-muted">
                Class / Academic Grade
              </Label>
              <select
                value={selectedClass}
                onChange={(e) => setSelectedClass(e.target.value)}
                className="w-full p-2.5 rounded-xl border border-border-subtle bg-surface text-ink-primary text-sm focus:outline-hidden focus:ring-2 focus:ring-primary/20"
              >
                <option value="Class 6">Class 6</option>
                <option value="Class 7">Class 7</option>
                <option value="Class 8">Class 8</option>
                <option value="Class 9">Class 9</option>
                <option value="Class 10">Class 10</option>
                <option value="Class 11">Class 11</option>
                <option value="Class 12">Class 12</option>
              </select>
            </div>

            <div className="pt-3 border-t border-border-subtle flex items-center justify-between">
              <button
                type="button"
                onClick={() => signOutAction()}
                className="text-xs font-label-micro text-primary hover:underline cursor-pointer"
              >
                Sign Out
              </button>

              <div className="flex gap-2">
                <button
                  type="button"
                  onClick={() => setPreferencesOpen(false)}
                  className="px-4 py-2 rounded-xl border border-border-subtle text-ink-primary font-label-md text-sm hover:bg-canvas cursor-pointer"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={savingPrefs}
                  className="px-5 py-2 rounded-xl bg-primary text-white font-semibold font-label-md text-sm hover:bg-accent-hover cursor-pointer"
                >
                  {savingPrefs ? 'Saving...' : 'Save Settings'}
                </button>
              </div>
            </div>
          </form>
        </DialogContent>
      </Dialog>

      {/* ========================================================================= */}
      {/* 6. MODAL: MANAGE COURSES DIALOG                                           */}
      {/* ========================================================================= */}
      <Dialog open={coursesDialogOpen} onOpenChange={setCoursesDialogOpen}>
        <DialogContent className="max-w-lg bg-surface border-border-subtle rounded-3xl p-7 text-ink-primary shadow-2xl">
          <DialogHeader>
            <DialogTitle className="font-headline-md text-2xl text-ink-primary">
              All Available Curriculums
            </DialogTitle>
            <DialogDescription className="font-body-md text-ink-secondary text-sm">
              Enroll in syllabus courses and rigorous academic tracks.
            </DialogDescription>
          </DialogHeader>

          <div className="space-y-3 my-3 max-h-80 overflow-y-auto pr-1">
            {allCurriculums.map((curr) => {
              const isEnrolled = enrolledCurriculums.some((e) => e.id === curr.id)
              return (
                <div
                  key={curr.id}
                  className="p-4 rounded-2xl bg-canvas border border-border-subtle flex items-center justify-between gap-3"
                >
                  <div>
                    <h5 className="font-label-md font-semibold text-ink-primary">
                      {curr.title}
                    </h5>
                    <p className="font-label-micro text-ink-muted text-xs mt-0.5">
                      {curr.category} • {curr.difficulty_level || 'advanced'}
                    </p>
                  </div>
                  {isEnrolled ? (
                    <span className="px-3 py-1 rounded-lg bg-secondary/10 text-secondary text-xs font-semibold">
                      Enrolled
                    </span>
                  ) : (
                    <button
                      onClick={async () => {
                        await enrollCurriculumAction(curr.id)
                        setCoursesDialogOpen(false)
                      }}
                      className="px-3.5 py-1.5 rounded-lg bg-primary text-white font-semibold text-xs font-medium hover:bg-accent-hover cursor-pointer"
                    >
                      Enroll
                    </button>
                  )}
                </div>
              )
            })}
          </div>

          <DialogFooter>
            <button
              onClick={() => setCoursesDialogOpen(false)}
              className="px-4 py-2 rounded-xl border border-border-subtle text-ink-primary font-label-md text-sm hover:bg-canvas cursor-pointer"
            >
              Done
            </button>
          </DialogFooter>
        </DialogContent>
      </Dialog>

      {/* ========================================================================= */}
      {/* 6B. MODAL: SYLLABUS & DIVIDED CAPSULES DIALOG                             */}
      {/* ========================================================================= */}
      <Dialog open={syllabusModalOpen} onOpenChange={setSyllabusModalOpen}>
        <DialogContent className="max-w-4xl w-[95vw] md:w-full bg-surface border border-border-subtle rounded-3xl p-0 overflow-hidden shadow-2xl flex flex-col max-h-[90vh] text-ink-primary">
          {/* Modal Header */}
          <div className="p-6 md:p-7 border-b border-border-subtle bg-surface/95 backdrop-blur-md">
            <div className="flex flex-wrap items-center gap-2 mb-2.5">
              <span className="px-2.5 py-0.5 rounded-md bg-secondary/10 border border-secondary/20 text-secondary font-label-micro text-xs font-bold uppercase tracking-wider">
                {activeSyllabusChapter?.board || 'CBSE'} Board
              </span>
              <span className="px-2.5 py-0.5 rounded-md bg-surface-container-low border border-border-subtle text-ink-primary font-label-micro text-xs font-semibold">
                {activeSyllabusChapter?.class_level || profile.class_level || 'Class 9'}
              </span>
              <span className="px-2.5 py-0.5 rounded-md bg-primary/10 border border-primary/20 text-primary font-label-micro text-xs font-semibold">
                {activeSyllabusCategory}
              </span>
            </div>

            <DialogTitle className="font-headline-md text-2xl md:text-3xl text-ink-primary tracking-tight">
              Official Syllabus &amp; Divided Capsules
            </DialogTitle>
            <DialogDescription className="font-body-md text-ink-secondary text-sm mt-1">
              Hierarchical curriculum mapped from class &amp; subject to sequential chapters and divided 15-minute concept capsules.
            </DialogDescription>

            {/* Subject Selector Tabs */}
            {syllabusSubjects.length > 1 && (
              <div className="flex items-center gap-2 mt-4 pt-3 border-t border-border-subtle/60 overflow-x-auto no-scrollbar">
                <span className="font-label-micro text-xs uppercase text-ink-muted shrink-0 mr-1">
                  Subject:
                </span>
                {syllabusSubjects.map((sub) => {
                  const isSelected = activeSyllabusCategory === sub
                  return (
                    <button
                      key={sub}
                      onClick={() => {
                        setSelectedSyllabusCategory(sub)
                        const firstCh = allAvailableCurriculums.find((c) => (c.category || 'General') === sub)
                        if (firstCh) setSelectedSyllabusCurriculumId(firstCh.id)
                      }}
                      className={`px-3.5 py-1.5 rounded-xl font-label-micro text-xs font-medium transition-all shrink-0 cursor-pointer ${
                        isSelected
                          ? 'bg-ink-primary text-white shadow-xs'
                          : 'border border-border-subtle bg-canvas hover:bg-surface-container-low text-ink-secondary'
                      }`}
                    >
                      {sub}
                    </button>
                  )
                })}
              </div>
            )}
          </div>

          {/* Modal Body: Scrollable */}
          <div className="flex-1 overflow-y-auto p-6 md:p-7 space-y-6">
            {/* Chapters Navigator */}
            {currentSubjectChapters.length > 0 ? (
              <div className="space-y-2.5">
                <div className="flex items-center justify-between">
                  <span className="font-label-micro text-xs uppercase tracking-wider text-ink-muted">
                    Syllabus Chapters ({currentSubjectChapters.length})
                  </span>
                  <span className="font-label-micro text-xs text-ink-muted">
                    Select chapter to view divided capsules
                  </span>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                  {currentSubjectChapters.map((ch, idx) => {
                    const isSelected = activeSyllabusChapter?.id === ch.id
                    const chModules = modules.filter((m) => m.curriculum_id === ch.id)
                    const chDone = chModules.filter((m) => isModuleComplete(m.id)).length
                    const chPercent = chModules.length > 0 ? Math.round((chDone / chModules.length) * 100) : 0

                    return (
                      <button
                        key={ch.id}
                        onClick={() => setSelectedSyllabusCurriculumId(ch.id)}
                        className={`p-3.5 rounded-2xl border text-left transition-all cursor-pointer flex flex-col justify-between ${
                          isSelected
                            ? 'border-primary bg-primary/5 ring-1 ring-primary shadow-xs'
                            : 'border-border-subtle bg-canvas hover:bg-surface-container-low'
                        }`}
                      >
                        <div className="space-y-1">
                          <div className="flex items-center justify-between">
                            <span className="font-label-micro text-xs text-primary font-bold">
                              Chapter {ch.order_index ?? idx + 1}
                            </span>
                            <span className="font-label-micro text-[11px] text-ink-muted">
                              {chModules.length} Capsules
                            </span>
                          </div>
                          <p className="font-label-md text-sm font-semibold text-ink-primary line-clamp-1">
                            {ch.title.replace(/^Class\s+\d+\s+[^:]+:\s*/i, '')}
                          </p>
                        </div>

                        <div className="mt-2.5 pt-2 border-t border-border-subtle/50 flex items-center justify-between">
                          <span className="font-label-micro text-[11px] text-ink-muted">
                            {chPercent}% Complete
                          </span>
                          <span className={`w-2 h-2 rounded-full ${chPercent === 100 ? 'bg-secondary' : chPercent > 0 ? 'bg-primary' : 'bg-surface-container-high'}`} />
                        </div>
                      </button>
                    )
                  })}
                </div>
              </div>
            ) : (
              <div className="p-6 text-center rounded-2xl bg-canvas border border-border-subtle">
                <p className="font-body-md text-sm text-ink-secondary">
                  No chapters available for this subject yet.
                </p>
              </div>
            )}

            {/* Active Chapter Written Syllabus Summary Card */}
            {activeSyllabusChapter && (
              <div className="p-5 md:p-6 rounded-2xl bg-canvas border border-border-subtle space-y-3">
                <div className="flex flex-wrap items-start justify-between gap-3">
                  <div>
                    <span className="font-label-micro text-xs text-primary uppercase tracking-wider font-semibold">
                      Chapter {activeSyllabusChapter.order_index ?? 1} Syllabus
                    </span>
                    <h3 className="font-headline-md text-xl font-bold text-ink-primary mt-0.5">
                      {activeSyllabusChapter.title}
                    </h3>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className="px-3 py-1 rounded-lg bg-surface border border-border-subtle text-ink-primary font-label-micro text-xs">
                      {activeChapterCapsules.length} Capsules
                    </span>
                    <span className="px-3 py-1 rounded-lg bg-surface border border-border-subtle text-ink-primary font-label-micro text-xs">
                      {activeSyllabusChapter.estimated_duration_minutes || activeChapterCapsules.length * 15} mins
                    </span>
                    <span className="px-3 py-1 rounded-lg bg-surface border border-border-subtle text-secondary font-label-micro text-xs font-semibold capitalize">
                      {activeSyllabusChapter.difficulty_level || 'Intermediate'}
                    </span>
                  </div>
                </div>

                <div className="pt-2 border-t border-border-subtle/60">
                  <span className="font-label-micro text-xs text-ink-muted uppercase block mb-1">
                    Written Syllabus Scope
                  </span>
                  <p className="font-body-md text-sm text-ink-primary leading-relaxed">
                    {activeSyllabusChapter.description || 'Comprehensive conceptual and practical study module calibrated to curriculum specifications.'}
                  </p>
                </div>
              </div>
            )}

            {/* Divided Capsules List */}
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <h4 className="font-headline-sm text-lg text-ink-primary">
                    Divided Capsules ({activeChapterCapsules.length})
                  </h4>
                  <p className="font-body-md text-xs text-ink-secondary">
                    Sequential 15-minute deliberate learning units with subtopics and key formulas.
                  </p>
                </div>
              </div>

              {activeChapterCapsules.length > 0 ? (
                <div className="space-y-3.5">
                  {activeChapterCapsules.map((mod, modIdx) => {
                    const prog = progressMap.get(mod.id)
                    const isDone = isModuleComplete(mod.id)
                    const isInProg = isModuleInProgress(mod.id)
                    const status = isDone ? 'completed' : isInProg ? 'in_progress' : (prog?.status || 'not_started')

                    // Safely extract subtopics array
                    const rawSubtopics = mod.subtopics
                    let subtopicsList: Array<{ title: string; formula?: string }> = []
                    if (Array.isArray(rawSubtopics)) {
                      subtopicsList = rawSubtopics.map((item: any) => {
                        if (typeof item === 'string') {
                          return { title: item }
                        } else if (item && typeof item === 'object') {
                          return {
                            title: item.title || item.name || String(item),
                            formula: item.key_formula || item.formula || undefined,
                          }
                        }
                        return { title: String(item) }
                      })
                    } else if (typeof rawSubtopics === 'string') {
                      try {
                        const parsed = JSON.parse(rawSubtopics)
                        if (Array.isArray(parsed)) {
                          subtopicsList = parsed.map((item: any) =>
                            typeof item === 'string' ? { title: item } : { title: item.title || String(item), formula: item.key_formula }
                          )
                        }
                      } catch {
                        subtopicsList = [{ title: rawSubtopics }]
                      }
                    }

                    return (
                      <div
                        key={mod.id}
                        className={`p-5 rounded-2xl border transition-all ${
                          isInProg
                            ? 'bg-surface border-primary/40 ring-1 ring-primary/20 shadow-xs'
                            : isDone
                            ? 'bg-surface/90 border-border-subtle'
                            : 'bg-surface border-border-subtle hover:border-ink-muted'
                        }`}
                      >
                        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 pb-3 border-b border-border-subtle/50">
                          <div className="flex items-center gap-2.5">
                            <span className="px-2.5 py-1 rounded-lg bg-surface-container-low border border-border-subtle font-label-micro text-xs font-bold text-ink-primary">
                              Capsule {mod.order_index ?? modIdx + 1}
                            </span>
                            <span className="flex items-center gap-1 font-label-micro text-xs text-ink-muted">
                              <span className="material-symbols-outlined text-sm">timer</span>
                              <span>{mod.estimated_minutes || 15} mins</span>
                            </span>
                          </div>

                          <div className="flex items-center gap-2">
                            {isDone ? (
                              <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-secondary/10 text-secondary text-xs font-semibold">
                                <span className="material-symbols-outlined text-xs">check_circle</span>
                                <span>Completed</span>
                              </span>
                            ) : isInProg ? (
                              <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-primary/10 text-primary text-xs font-semibold">
                                <span className="material-symbols-outlined text-xs">play_circle</span>
                                <span>In Progress</span>
                              </span>
                            ) : (
                              <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-surface-container-low text-ink-muted text-xs font-medium">
                                <span className="material-symbols-outlined text-xs">radio_button_unchecked</span>
                                <span>Ready to Start</span>
                              </span>
                            )}
                          </div>
                        </div>

                        {/* Title & Description */}
                        <div className="mt-3 space-y-1.5">
                          <h5 className="font-headline-sm text-base md:text-lg font-semibold text-ink-primary">
                            {mod.title}
                          </h5>
                          {mod.description && (
                            <p className="font-body-md text-xs md:text-sm text-ink-secondary">
                              {mod.description}
                            </p>
                          )}
                        </div>

                        {/* Subtopics breakdown */}
                        {subtopicsList.length > 0 && (
                          <div className="mt-3.5 pt-3 border-t border-border-subtle/40 space-y-2">
                            <span className="font-label-micro text-[11px] uppercase tracking-wider text-ink-muted block">
                              Capsule Subtopics &amp; Problem Areas:
                            </span>
                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                              {subtopicsList.map((sub, sIdx) => (
                                <div
                                  key={sIdx}
                                  className="flex items-start gap-2 p-2 rounded-xl bg-canvas border border-border-subtle/60 text-xs"
                                >
                                  <span className="material-symbols-outlined text-sm text-secondary shrink-0 mt-0.5">
                                    arrow_right
                                  </span>
                                  <div className="min-w-0 flex-1">
                                    <span className="font-body-md text-ink-primary font-medium">
                                      {sub.title}
                                    </span>
                                    {sub.formula && (
                                      <span className="block font-mono text-[11px] text-primary font-semibold mt-0.5">
                                        Formula: {sub.formula}
                                      </span>
                                    )}
                                  </div>
                                </div>
                              ))}
                            </div>
                          </div>
                        )}

                        {/* Key Concepts */}
                        {mod.key_concepts && mod.key_concepts.length > 0 && (
                          <div className="mt-3 flex flex-wrap items-center gap-1.5">
                            <span className="font-label-micro text-[11px] text-ink-muted mr-1">
                              Key Concepts:
                            </span>
                            {mod.key_concepts.map((concept, cIdx) => (
                              <span
                                key={cIdx}
                                className="px-2 py-0.5 rounded-md bg-surface-container-low border border-border-subtle text-[11px] font-label-micro text-ink-primary"
                              >
                                {concept}
                              </span>
                            ))}
                          </div>
                        )}

                        {/* Launch Action */}
                        <div className="mt-4 pt-3 border-t border-border-subtle/50 flex justify-end">
                          <Link
                            href={`/dashboard/${user.id}/class/${mod.id}`}
                            onClick={(e) => {
                              handleModuleClick(e, mod.id)
                              setSyllabusModalOpen(false)
                            }}
                            className={`inline-flex items-center gap-2 px-4 py-2 rounded-xl font-label-md text-xs font-semibold transition-all ${
                              isInProg
                                ? 'bg-primary hover:bg-accent-hover text-white font-semibold shadow-xs'
                                : isDone
                                ? 'border border-border-subtle hover:bg-canvas text-ink-primary'
                                : 'bg-primary hover:bg-accent-hover text-white font-semibold shadow-xs'
                            }`}
                          >
                            <span className="material-symbols-outlined text-sm">
                              {isDone ? 'replay' : 'play_arrow'}
                            </span>
                            <span>
                              {isInProg ? 'Resume Capsule' : isDone ? 'Review in Spoken Class' : 'Start Capsule (15m)'}
                            </span>
                          </Link>
                        </div>
                      </div>
                    )
                  })}
                </div>
              ) : (
                <div className="p-6 text-center rounded-2xl bg-canvas border border-border-subtle">
                  <p className="font-body-md text-sm text-ink-secondary">
                    No divided capsules found for this chapter.
                  </p>
                </div>
              )}
            </div>
          </div>

          {/* Modal Footer */}
          <div className="p-4 md:p-5 border-t border-border-subtle bg-surface flex items-center justify-between">
            <span className="font-label-micro text-xs text-ink-muted hidden sm:inline-block">
              {activeSyllabusChapter?.board || 'CBSE'} • {activeSyllabusChapter?.class_level || profile.class_level || 'Class 9'} • {activeSyllabusCategory}
            </span>
            <button
              onClick={() => setSyllabusModalOpen(false)}
              className="px-5 py-2 rounded-xl border border-border-subtle text-ink-primary font-label-md text-sm hover:bg-canvas cursor-pointer ml-auto"
            >
              Close Syllabus
            </button>
          </div>
        </DialogContent>
      </Dialog>

      {/* ========================================================================= */}
      {/* 7. MOBILE DRAWER                                                          */}
      {/* ========================================================================= */}
      {mobileMenuOpen && (
        <div
          className="fixed inset-0 bg-ink-primary/20 backdrop-blur-xs z-50 md:hidden"
          onClick={() => setMobileMenuOpen(false)}
        />
      )}

      <aside
        className={`fixed left-0 top-0 bottom-0 w-72 bg-canvas z-50 border-r border-border-subtle p-6 flex flex-col justify-between transform transition-transform duration-300 md:hidden ${
          mobileMenuOpen ? 'translate-x-0' : '-translate-x-full'
        }`}
      >
        <div className="space-y-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <span className="material-symbols-outlined text-secondary text-2xl">eco</span>
              <span className="font-editorial text-2xl leading-none text-ink-primary">Anaxly</span>
            </div>
            <button
              className="inline-flex h-10 w-10 cursor-pointer items-center justify-center rounded-lg text-ink-muted hover:text-ink-primary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm"
              onClick={() => setMobileMenuOpen(false)}
              aria-label="Close menu"
            >
              <span className="material-symbols-outlined">close</span>
            </button>
          </div>

          <DashboardNav
            ariaLabel="Mobile navigation"
            activeId={activeNav}
            items={navItems.map((item) => ({
              ...item,
              onSelect: () => {
                item.onSelect()
                setMobileMenuOpen(false)
              },
            }))}
          />
          <Link
            href={`/dashboard/${user.id}/settings?tab=avatars`}
            onClick={() => setMobileMenuOpen(false)}
            className="flex min-h-11 w-full items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium text-ink-secondary transition-colors hover:bg-canvas-soft hover:text-ink-primary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm"
          >
            <span aria-hidden="true" className="material-symbols-outlined text-xl">settings</span>
            <span>Settings &amp; avatars</span>
          </Link>
        </div>

        <div className="border-t border-border-subtle pt-4">
          <div className="flex items-center gap-3 p-2 bg-surface rounded-xl border border-border-subtle">
            <div className="w-8 h-8 rounded-full bg-surface-container-high overflow-hidden flex items-center justify-center">
              {studentAvatar ? (
                <img
                  className="w-full h-full object-cover"
                  alt={studentName}
                  src={studentAvatar}
                />
              ) : (
                <span className="font-semibold text-ink-primary text-xs font-label-md">
                  {studentName.charAt(0).toUpperCase()}
                </span>
              )}
            </div>
            <div>
              <p className="font-label-md text-label-md text-ink-primary font-medium">
                {studentName}
              </p>
              <p className="font-label-micro text-label-micro text-ink-muted">
                {studentTrack}
              </p>
            </div>
          </div>
        </div>
      </aside>

      {/* 10-Question Mastery Evaluation Modal */}
      {activeModule && (
        <MasteryQuizModal
          isOpen={quizModalOpen}
          onClose={() => setQuizModalOpen(false)}
          moduleId={activeModule.id}
          moduleTitle={activeModule.title}
          onCompleteSuccess={() => {
            router.refresh()
          }}
        />
      )}

    </div>
  )
}

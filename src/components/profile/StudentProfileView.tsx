'use client'

import React, { useState, useEffect, useMemo } from 'react'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import {
  BookOpen,
  CheckCircle2,
  Clock,
  Flame,
  Award,
  Sparkles,
  Download,
  Copy,
  Check,
  Search,
  ArrowLeft,
  ExternalLink,
  Layers,
  FileText,
  RefreshCw,
  ChevronRight,
  GraduationCap,
  SlidersHorizontal,
} from 'lucide-react'
import {
  calculateStudentProgress,
  getCachedStudentProgress,
  setCachedStudentProgress,
  getAllCachedBoardNotesForUser,
  StudentProgressSummary,
  SavedBoardNote,
  Curriculum,
  SyllabusModule,
  UserProgressRecord,
} from '@/lib/studentProgressService'

interface StudentProfileViewProps {
  user: {
    id: string
    email?: string
  }
  profile: {
    id: string
    full_name?: string | null
    class_level?: string | null
    target_board?: string | null
    current_streak?: number | null
    longest_streak?: number | null
    total_classes_taken?: number | null
    total_learning_minutes?: number | null
    learning_style?: string | null
    preferred_pacing?: string | null
    preferred_teacher_voice?: string | null
    completed_chapters_count?: number | null
    avatar_url?: string | null
  }
  curriculums: Curriculum[]
  modules: SyllabusModule[]
  progressRecords: UserProgressRecord[]
}

export function StudentProfileView({
  user,
  profile,
  curriculums = [],
  modules = [],
  progressRecords = [],
}: StudentProfileViewProps) {
  const router = useRouter()
  const [activeTab, setActiveTab] = useState<'progress' | 'notes'>('progress')
  const [selectedSubject, setSelectedSubject] = useState<string>('All')
  const [searchQuery, setSearchQuery] = useState<string>('')
  const [copiedNoteId, setCopiedNoteId] = useState<string | null>(null)
  const [isRefreshing, setIsRefreshing] = useState<boolean>(false)
  const [expandedNoteId, setExpandedNoteId] = useState<string | null>(null)

  // Compute live progress data
  const computedProgress = useMemo(() => {
    return calculateStudentProgress({
      userId: user.id,
      curriculums,
      modules,
      progressRecords,
    })
  }, [user.id, curriculums, modules, progressRecords])

  const [progressSummary, setProgressSummary] = useState<StudentProgressSummary>(() => {
    // Check client-side cache first for instant 0ms mount
    const cached = getCachedStudentProgress(user.id)
    if (cached && Date.now() - cached.timestamp < 3 * 60 * 1000) {
      return cached
    }
    return computedProgress
  })

  // Synchronize with computed progress and update client cache
  useEffect(() => {
    setProgressSummary((prev) => {
      if (prev && prev.completedChaptersCount > computedProgress.completedChaptersCount) {
        return {
          ...computedProgress,
          completedChaptersCount: prev.completedChaptersCount,
          completedChapters:
            prev.completedChapters.length >= computedProgress.completedChapters.length
              ? prev.completedChapters
              : computedProgress.completedChapters,
        }
      }
      return computedProgress
    })
    setCachedStudentProgress(user.id, computedProgress)
  }, [computedProgress, user.id])

  // Support direct deep-linking via query parameters (e.g. ?tab=notes&search=...)
  useEffect(() => {
    if (typeof window !== 'undefined') {
      try {
        const sp = new URLSearchParams(window.location.search)
        const tabParam = sp.get('tab')
        const searchParam = sp.get('search') || sp.get('q')
        const subjectParam = sp.get('subject')
        if (tabParam === 'notes' || searchParam) {
          setActiveTab('notes')
        }
        if (searchParam) {
          setSearchQuery(searchParam)
        }
        if (subjectParam) {
          setSelectedSubject(subjectParam)
        }
      } catch {}
    }
  }, [])

  // Merge any locally cached board notes that haven't synced yet
  const allNotes = useMemo(() => {
    const serverNotes = progressSummary.savedNotes || []
    const localCached = getAllCachedBoardNotesForUser(user.id)

    const map = new Map<string, SavedBoardNote>()
    serverNotes.forEach((n) => map.set(n.moduleId, n))

    localCached.forEach((l) => {
      const existing = map.get(l.moduleId)
      if (existing) {
        if (l.fullSummary && l.fullSummary.length > existing.fullSummary.length) {
          map.set(l.moduleId, {
            ...existing,
            fullSummary: l.fullSummary,
            notesText: l.notesText,
            roughText: l.roughText,
            savedAt: l.updatedAt || existing.savedAt,
          })
        }
      } else {
        const mod = modules.find((m) => m.id === l.moduleId)
        const curr = mod ? curriculums.find((c) => c.id === mod.curriculum_id) : null
        map.set(l.moduleId, {
          moduleId: l.moduleId,
          moduleTitle: mod?.title || 'Classroom Lesson',
          moduleOrder: mod?.order_index || 1,
          chapterId: curr?.id || '',
          chapterTitle: curr?.title || 'Academic Chapter',
          category: curr?.category || 'General',
          classLevel: curr?.class_level || profile.class_level,
          board: curr?.board || profile.target_board,
          notesText: l.notesText,
          roughText: l.roughText,
          fullSummary: l.fullSummary,
          savedAt: l.updatedAt || new Date().toISOString(),
          hasDiagrams: l.fullSummary.includes('[DIAGRAM:'),
          hasFormulas: l.fullSummary.includes('=') || l.fullSummary.toLowerCase().includes('formula'),
          hasRoughWork: !!(l.roughText && l.roughText.length > 0) || l.fullSummary.includes('ROUGH WORK'),
          visualDataAvailable: !!(l.visualProgress?.whiteboard_pages?.length),
        })
      }
    })

    return Array.from(map.values())
  }, [progressSummary.savedNotes, user.id, modules, curriculums, profile])

  // Extract unique subjects/categories for filtering
  const subjects = useMemo(() => {
    const set = new Set<string>()
    curriculums.forEach((c) => {
      if (c.category) set.add(c.category)
    })
    return ['All', ...Array.from(set).sort()]
  }, [curriculums])

  // Filtered notes based on subject and search query
  const filteredNotes = useMemo(() => {
    return allNotes.filter((note) => {
      const matchesSubject = selectedSubject === 'All' || note.category === selectedSubject
      const matchesQuery =
        !searchQuery ||
        note.moduleTitle.toLowerCase().includes(searchQuery.toLowerCase()) ||
        note.chapterTitle.toLowerCase().includes(searchQuery.toLowerCase()) ||
        note.fullSummary.toLowerCase().includes(searchQuery.toLowerCase())
      return matchesSubject && matchesQuery
    })
  }, [allNotes, selectedSubject, searchQuery])

  // Filtered chapters for progress view
  const completedChapters = progressSummary.completedChapters || []
  const inProgressChapters = progressSummary.inProgressChapters || []
  const totalChaptersCount = progressSummary.totalChaptersCount || curriculums.length
  const completedChaptersCount = Math.max(
    completedChapters.length,
    progressSummary.completedChaptersCount || 0,
    typeof profile.completed_chapters_count === 'number' ? profile.completed_chapters_count : 0
  )

  const studyHours = profile.total_learning_minutes
    ? (profile.total_learning_minutes / 60).toFixed(1)
    : '0.0'

  const handleCopyNote = async (noteId: string, content: string) => {
    try {
      await navigator.clipboard.writeText(content)
      setCopiedNoteId(noteId)
      setTimeout(() => setCopiedNoteId(null), 2500)
    } catch (err) {
      console.error('Failed to copy note:', err)
    }
  }

  const handleDownloadNote = (note: SavedBoardNote) => {
    const filename = `${note.chapterTitle}_${note.moduleTitle}_Master_Notes.md`.replace(/[\s/\\?%*:|"<>]/g, '_')
    const header = `# ${note.chapterTitle}\n## ${note.moduleTitle}\n**Subject**: ${note.category} | **Class**: ${note.classLevel || 'Standard'}\n**Board Notes Single Source of Truth** | **Generated**: ${new Date(note.savedAt).toLocaleDateString()}\n\n---\n\n`
    const blob = new Blob([header + note.fullSummary], { type: 'text/markdown;charset=utf-8' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = filename
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
  }

  const handleSyncWithCloud = async () => {
    setIsRefreshing(true)
    try {
      const res = await fetch(`/api/student/progress?userId=${user.id}`, {
        cache: 'no-store',
      })
      if (res.ok) {
        const json = await res.json()
        if (json.summary) {
          setProgressSummary(json.summary)
          setCachedStudentProgress(user.id, json.summary)
        }
      }
    } catch (err) {
      console.warn('Sync failed:', err)
    } finally {
      setIsRefreshing(false)
    }
  }

  return (
    <div className="min-h-screen bg-[#FBFBF9] text-[#1E231B] selection:bg-[#E2EBE0] selection:text-[#183B28]">
      {/* Top Navigation Bar */}
      <header className="sticky top-0 z-30 border-b border-[#E7E9E3] bg-[#FBFBF9]/90 backdrop-blur-md">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 sm:px-6 lg:px-8">
          <div className="flex items-center gap-3">
            <Link
              href={`/dashboard/${user.id}`}
              className="inline-flex h-9 w-9 items-center justify-center rounded-lg border border-[#E7E9E3] bg-white text-[#555852] transition hover:bg-[#F2F4F0] hover:text-[#1E231B]"
              aria-label="Back to Dashboard"
            >
              <ArrowLeft className="h-4 w-4" />
            </Link>
            <div>
              <h1 className="font-serif text-lg font-semibold tracking-tight text-[#1E231B]">
                Student Profile &amp; Master Notes
              </h1>
              <p className="text-xs text-[#6B7066]">
                Academic dossier &amp; Chalkboard Notes Single Source of Truth
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={handleSyncWithCloud}
              disabled={isRefreshing}
              className="inline-flex items-center gap-1.5 rounded-lg border border-[#E7E9E3] bg-white px-3 py-1.5 text-xs font-medium text-[#555852] transition hover:bg-[#F2F4F0] hover:text-[#1E231B] disabled:opacity-50"
            >
              <RefreshCw className={`h-3.5 w-3.5 ${isRefreshing ? 'animate-spin text-[#183B28]' : ''}`} />
              <span>{isRefreshing ? 'Syncing...' : 'Sync Cloud'}</span>
            </button>
            <Link
              href={`/dashboard/${user.id}/settings`}
              className="inline-flex items-center gap-1.5 rounded-lg border border-[#E7E9E3] bg-white px-3 py-1.5 text-xs font-medium text-[#555852] transition hover:bg-[#F2F4F0] hover:text-[#1E231B]"
            >
              <SlidersHorizontal className="h-3.5 w-3.5" />
              <span>Settings</span>
            </Link>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-7xl space-y-8 px-4 py-6 sm:px-6 lg:px-8">
        {/* Student Profile Header Card */}
        <section className="rounded-3xl border border-[#E7E9E3] bg-white p-6 shadow-sm sm:p-8">
          <div className="flex flex-col gap-6 md:flex-row md:items-center md:justify-between">
            <div className="flex items-start gap-4">
              <div className="relative flex h-16 w-16 shrink-0 items-center justify-center rounded-2xl bg-gradient-to-br from-[#183B28] to-[#2E5E43] font-serif text-2xl font-bold text-white shadow-md">
                {profile.full_name?.charAt(0) || user.email?.charAt(0)?.toUpperCase() || 'S'}
                <div className="absolute -bottom-1 -right-1 rounded-full bg-[#E5A93C] p-1 text-white shadow-xs">
                  <Award className="h-3.5 w-3.5" />
                </div>
              </div>

              <div className="space-y-1">
                <div className="flex flex-wrap items-center gap-2">
                  <h2 className="font-serif text-2xl font-semibold tracking-tight text-[#1E231B]">
                    {profile.full_name || 'Enrolled Student'}
                  </h2>
                  <span className="rounded-full bg-[#EAF0E8] px-2.5 py-0.5 text-xs font-medium text-[#183B28]">
                    {profile.target_board || 'CBSE'} Board
                  </span>
                  <span className="rounded-full bg-[#F2F4F0] px-2.5 py-0.5 text-xs font-medium text-[#555852]">
                    {profile.class_level?.replace('_', ' ').toUpperCase() || 'CLASS 10'}
                  </span>
                </div>
                <p className="text-sm text-[#6B7066]">
                  {user.email} &bull; Socratic Cadence Learner &bull; Mentor: {profile.preferred_teacher_voice || 'Prof. Vikram Raman'}
                </p>
              </div>
            </div>

            {/* Quick Metrics Badges */}
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
              <div className="rounded-2xl border border-[#E7E9E3] bg-[#FBFBF9] p-3 text-center">
                <div className="flex items-center justify-center gap-1 text-xs font-medium text-[#6B7066]">
                  <Flame className="h-3.5 w-3.5 text-[#E5A93C]" />
                  <span>Streak</span>
                </div>
                <div className="mt-1 font-serif text-xl font-bold text-[#1E231B]">
                  {profile.current_streak || 1} <span className="text-xs font-normal text-[#6B7066]">days</span>
                </div>
              </div>

              <div className="rounded-2xl border border-[#E7E9E3] bg-[#FBFBF9] p-3 text-center">
                <div className="flex items-center justify-center gap-1 text-xs font-medium text-[#6B7066]">
                  <Clock className="h-3.5 w-3.5 text-[#2E5E43]" />
                  <span>Study Time</span>
                </div>
                <div className="mt-1 font-serif text-xl font-bold text-[#1E231B]">
                  {studyHours} <span className="text-xs font-normal text-[#6B7066]">hrs</span>
                </div>
              </div>

              <div className="rounded-2xl border border-[#E7E9E3] bg-[#EAF0E8] p-3 text-center">
                <div className="flex items-center justify-center gap-1 text-xs font-medium text-[#183B28]">
                  <CheckCircle2 className="h-3.5 w-3.5 text-[#183B28]" />
                  <span>Chapters Done</span>
                </div>
                <div className="mt-1 font-serif text-xl font-bold text-[#183B28]">
                  {completedChaptersCount} <span className="text-xs font-normal text-[#183B28]/80">/ {totalChaptersCount}</span>
                </div>
              </div>

              <div className="rounded-2xl border border-[#E7E9E3] bg-[#FBFBF9] p-3 text-center">
                <div className="flex items-center justify-center gap-1 text-xs font-medium text-[#6B7066]">
                  <FileText className="h-3.5 w-3.5 text-[#555852]" />
                  <span>Board Notes</span>
                </div>
                <div className="mt-1 font-serif text-xl font-bold text-[#1E231B]">
                  {allNotes.length} <span className="text-xs font-normal text-[#6B7066]">saved</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Navigation Tabs: Chapter Progress vs Chalkboard Master Notes */}
        <div className="flex border-b border-[#E7E9E3]">
          <button
            type="button"
            onClick={() => setActiveTab('progress')}
            className={`flex items-center gap-2 border-b-2 px-5 py-3 text-sm font-medium transition ${
              activeTab === 'progress'
                ? 'border-[#183B28] text-[#183B28]'
                : 'border-transparent text-[#6B7066] hover:border-[#E7E9E3] hover:text-[#1E231B]'
            }`}
          >
            <GraduationCap className="h-4 w-4" />
            <span>Chapter Mastery Progress</span>
            <span className="rounded-full bg-[#EAF0E8] px-2 py-0.5 text-xs text-[#183B28]">
              {completedChaptersCount} Done
            </span>
          </button>

          <button
            type="button"
            onClick={() => setActiveTab('notes')}
            className={`flex items-center gap-2 border-b-2 px-5 py-3 text-sm font-medium transition ${
              activeTab === 'notes'
                ? 'border-[#183B28] text-[#183B28]'
                : 'border-transparent text-[#6B7066] hover:border-[#E7E9E3] hover:text-[#1E231B]'
            }`}
          >
            <BookOpen className="h-4 w-4" />
            <span>Master Board Notes Vault</span>
            <span className="rounded-full bg-[#F2F4F0] px-2 py-0.5 text-xs text-[#555852]">
              {allNotes.length} Notes
            </span>
          </button>
        </div>

        {/* TAB 1: CHAPTER PROGRESS OVERVIEW */}
        {activeTab === 'progress' && (
          <div className="space-y-6">
            {/* Progress Hero Banner */}
            <div className="flex flex-col gap-6 rounded-3xl border border-[#E7E9E3] bg-white p-6 shadow-sm sm:flex-row sm:items-center sm:justify-between sm:p-8">
              <div className="space-y-2">
                <span className="inline-flex items-center gap-1.5 rounded-full bg-[#EAF0E8] px-3 py-1 text-xs font-semibold uppercase tracking-wider text-[#183B28]">
                  <Sparkles className="h-3 w-3" />
                  Syllabus Mastery Cadence
                </span>
                <h3 className="font-serif text-2xl font-semibold tracking-tight text-[#1E231B]">
                  {completedChaptersCount > 0
                    ? `You have mastered ${completedChaptersCount} of ${totalChaptersCount} chapters`
                    : `Begin your first chapter to start building topper notes`}
                </h3>
                <p className="max-w-xl text-sm leading-relaxed text-[#6B7066]">
                  Every chapter synthesizes 5 to 8 dedicated capsules with live chalkboard notes, worked numerical proofs, and authentic board-exam questions.
                </p>
              </div>

              {/* Circular or linear progress meter */}
              <div className="flex items-center gap-4 rounded-2xl border border-[#E7E9E3] bg-[#FBFBF9] p-4 sm:flex-col sm:p-6">
                <div className="text-center">
                  <div className="font-serif text-3xl font-bold text-[#183B28]">
                    {totalChaptersCount > 0 ? Math.round((completedChaptersCount / totalChaptersCount) * 100) : 0}%
                  </div>
                  <div className="text-xs uppercase tracking-wider text-[#6B7066]">Curriculum Complete</div>
                </div>
                <div className="h-2 w-32 overflow-hidden rounded-full bg-[#E7E9E3]">
                  <div
                    className="h-full bg-[#183B28] transition-all duration-700 ease-out"
                    style={{
                      width: `${totalChaptersCount > 0 ? Math.min(100, Math.round((completedChaptersCount / totalChaptersCount) * 100)) : 0}%`,
                    }}
                  />
                </div>
              </div>
            </div>

            {/* Completed Chapters Section */}
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <h4 className="font-serif text-lg font-semibold text-[#1E231B]">
                    Completed Chapters ({completedChapters.length})
                  </h4>
                  <p className="text-xs text-[#6B7066]">
                    Fully completed chapters with all capsules and live chalkboard notes recorded
                  </p>
                </div>
              </div>

              {completedChapters.length > 0 ? (
                <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                  {completedChapters.map((chap) => (
                    <div
                      key={chap.id}
                      className="flex flex-col justify-between rounded-2xl border border-[#C5D6C0] bg-[#F4F8F3] p-5 shadow-xs transition hover:shadow-md"
                    >
                      <div className="space-y-3">
                        <div className="flex items-center justify-between">
                          <span className="rounded-md bg-[#EAF0E8] px-2 py-0.5 text-xs font-semibold text-[#183B28]">
                            {chap.category}
                          </span>
                          <span className="inline-flex items-center gap-1 text-xs font-medium text-[#183B28]">
                            <CheckCircle2 className="h-3.5 w-3.5 text-[#183B28]" />
                            Mastered
                          </span>
                        </div>
                        <div>
                          <h5 className="font-serif text-base font-semibold text-[#1E231B]">
                            {chap.title}
                          </h5>
                          <p className="mt-1 text-xs text-[#555852]">
                            {chap.completedModules} of {chap.totalModules} capsules completed
                          </p>
                        </div>
                      </div>

                      <div className="mt-4 flex items-center justify-between border-t border-[#D9E5D6] pt-3 text-xs">
                        <span className="text-[#6B7066]">
                          {chap.completedAt
                            ? `Done ${new Date(chap.completedAt).toLocaleDateString()}`
                            : 'Completed'}
                        </span>
                        <button
                          type="button"
                          onClick={() => {
                            setSelectedSubject(chap.category || 'All')
                            setSearchQuery(chap.title)
                            setActiveTab('notes')
                          }}
                          className="inline-flex items-center gap-1 font-medium text-[#183B28] hover:underline"
                        >
                          <span>View Notes</span>
                          <ChevronRight className="h-3.5 w-3.5" />
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="rounded-2xl border border-dashed border-[#E7E9E3] bg-white p-8 text-center text-[#6B7066]">
                  <GraduationCap className="mx-auto h-8 w-8 text-[#A0A59B]" />
                  <p className="mt-2 font-serif text-sm font-semibold text-[#1E231B]">
                    No chapters completed yet
                  </p>
                  <p className="mt-1 text-xs">
                    Complete all modules in a chapter during live class sessions to mark it mastered.
                  </p>
                  <Link
                    href={`/dashboard/${user.id}/class`}
                    className="mt-4 inline-flex items-center gap-2 rounded-xl bg-[#183B28] px-4 py-2 text-xs font-medium text-white shadow-xs hover:bg-[#235037]"
                  >
                    <span>Start First Class</span>
                    <ChevronRight className="h-3.5 w-3.5" />
                  </Link>
                </div>
              )}
            </div>

            {/* In-Progress Chapters Section */}
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <h4 className="font-serif text-lg font-semibold text-[#1E231B]">
                    Chapters In Progress ({inProgressChapters.length})
                  </h4>
                  <p className="text-xs text-[#6B7066]">
                    Active chapters currently underway
                  </p>
                </div>
              </div>

              {inProgressChapters.length > 0 ? (
                <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                  {inProgressChapters.map((chap) => (
                    <div
                      key={chap.id}
                      className="flex flex-col justify-between rounded-2xl border border-[#E7E9E3] bg-white p-5 shadow-xs transition hover:shadow-md"
                    >
                      <div className="space-y-3">
                        <div className="flex items-center justify-between">
                          <span className="rounded-md bg-[#F2F4F0] px-2 py-0.5 text-xs font-semibold text-[#555852]">
                            {chap.category}
                          </span>
                          <span className="text-xs font-bold text-[#183B28]">
                            {chap.percentComplete}%
                          </span>
                        </div>
                        <div>
                          <h5 className="font-serif text-base font-semibold text-[#1E231B]">
                            {chap.title}
                          </h5>
                          <p className="mt-1 text-xs text-[#6B7066]">
                            Current: {chap.activeModuleTitle || 'Active capsule'}
                          </p>
                        </div>
                        {/* Progress bar */}
                        <div className="h-1.5 w-full overflow-hidden rounded-full bg-[#E7E9E3]">
                          <div
                            className="h-full bg-[#183B28] transition-all duration-500 ease-out"
                            style={{ width: `${chap.percentComplete}%` }}
                          />
                        </div>
                      </div>

                      <div className="mt-4 flex items-center justify-between border-t border-[#F2F4F0] pt-3 text-xs">
                        <span className="text-[#6B7066]">
                          {chap.completedModules} of {chap.totalModules} capsules
                        </span>
                        <Link
                          href={chap.activeModuleId ? `/dashboard/${user.id}/class/${chap.activeModuleId}` : `/dashboard/${user.id}/class`}
                          className="inline-flex items-center gap-1 font-medium text-[#183B28] hover:underline"
                        >
                          <span>Resume</span>
                          <ChevronRight className="h-3.5 w-3.5" />
                        </Link>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="rounded-2xl border border-dashed border-[#E7E9E3] bg-white p-6 text-center text-xs text-[#6B7066]">
                  No chapters currently in progress. Start an enrolled chapter from your syllabus!
                </div>
              )}
            </div>
          </div>
        )}

        {/* TAB 2: MASTER CHALKBOARD NOTES VAULT (INVARIANT 3 SINGLE SOURCE OF TRUTH) */}
        {activeTab === 'notes' && (
          <div className="space-y-6">
            {/* Filter and Search Bar */}
            <div className="flex flex-col gap-4 rounded-2xl border border-[#E7E9E3] bg-white p-4 sm:flex-row sm:items-center sm:justify-between">
              {/* Subject Category Chips */}
              <div className="flex flex-wrap items-center gap-1.5 overflow-x-auto">
                {subjects.map((sub) => (
                  <button
                    key={sub}
                    type="button"
                    onClick={() => setSelectedSubject(sub)}
                    className={`rounded-lg px-3 py-1.5 text-xs font-medium transition ${
                      selectedSubject === sub
                        ? 'bg-[#183B28] text-white'
                        : 'bg-[#F2F4F0] text-[#555852] hover:bg-[#E7E9E3] hover:text-[#1E231B]'
                    }`}
                  >
                    {sub}
                  </button>
                ))}
              </div>

              {/* Search input */}
              <div className="relative w-full sm:w-72">
                <Search className="absolute left-3 top-1/2 h-3.5 w-3.5 -translate-y-1/2 text-[#A0A59B]" />
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder="Search laws, formulas, notes..."
                  className="w-full rounded-xl border border-[#E7E9E3] bg-[#FBFBF9] py-1.5 pl-9 pr-3 text-xs text-[#1E231B] placeholder-[#A0A59B] focus:border-[#183B28] focus:outline-none"
                />
              </div>
            </div>

            {/* Notes List */}
            {filteredNotes.length > 0 ? (
              <div className="space-y-4">
                {filteredNotes.map((note) => {
                  const isExpanded = expandedNoteId === note.moduleId
                  const isCopied = copiedNoteId === note.moduleId

                  return (
                    <article
                      key={note.moduleId}
                      className="rounded-3xl border border-[#E7E9E3] bg-white p-6 shadow-sm transition hover:border-[#CCD5C8]"
                    >
                      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
                        <div className="space-y-1.5">
                          <div className="flex flex-wrap items-center gap-2">
                            <span className="rounded-md bg-[#EAF0E8] px-2 py-0.5 text-xs font-semibold text-[#183B28]">
                              {note.category}
                            </span>
                            <span className="text-xs font-medium text-[#6B7066]">
                              {note.chapterTitle} &bull; Capsule {note.moduleOrder}
                            </span>
                            {note.hasDiagrams && (
                              <span className="rounded-md bg-[#F4F8F3] px-2 py-0.5 text-[11px] font-medium text-[#2E5E43]">
                                📐 Diagrams Included
                              </span>
                            )}
                            {note.hasFormulas && (
                              <span className="rounded-md bg-[#FFF8EE] px-2 py-0.5 text-[11px] font-medium text-[#B8771A]">
                                ∑ Formulas Included
                              </span>
                            )}
                            {note.hasRoughWork && (
                              <span className="rounded-md bg-[#F2F4F0] px-2 py-0.5 text-[11px] font-medium text-[#555852]">
                                📝 Rough Work Margin
                              </span>
                            )}
                          </div>
                          <h4 className="font-serif text-xl font-semibold tracking-tight text-[#1E231B]">
                            {note.moduleTitle}
                          </h4>
                          <p className="text-xs text-[#6B7066]">
                            Live Chalkboard Notes Single Source of Truth &bull; Saved on {new Date(note.savedAt).toLocaleDateString()}
                          </p>
                        </div>

                        {/* Actions */}
                        <div className="flex items-center gap-2 self-end sm:self-auto">
                          <button
                            type="button"
                            onClick={() => handleCopyNote(note.moduleId, note.fullSummary)}
                            className="inline-flex items-center gap-1 rounded-lg border border-[#E7E9E3] bg-white px-2.5 py-1.5 text-xs font-medium text-[#555852] transition hover:bg-[#F2F4F0] hover:text-[#1E231B]"
                            title="Copy Master Notes"
                          >
                            {isCopied ? (
                              <>
                                <Check className="h-3.5 w-3.5 text-[#183B28]" />
                                <span className="text-[#183B28]">Copied</span>
                              </>
                            ) : (
                              <>
                                <Copy className="h-3.5 w-3.5" />
                                <span>Copy</span>
                              </>
                            )}
                          </button>

                          <button
                            type="button"
                            onClick={() => handleDownloadNote(note)}
                            className="inline-flex items-center gap-1 rounded-lg border border-[#E7E9E3] bg-white px-2.5 py-1.5 text-xs font-medium text-[#555852] transition hover:bg-[#F2F4F0] hover:text-[#1E231B]"
                            title="Download Markdown"
                          >
                            <Download className="h-3.5 w-3.5" />
                            <span>Download</span>
                          </button>

                          <Link
                            href={`/dashboard/${user.id}/class/${note.moduleId}`}
                            className="inline-flex items-center gap-1 rounded-lg bg-[#183B28] px-3 py-1.5 text-xs font-medium text-white transition hover:bg-[#235037]"
                          >
                            <span>Open Board</span>
                            <ExternalLink className="h-3 w-3" />
                          </Link>
                        </div>
                      </div>

                      {/* Chalkboard Slate Notes Preview */}
                      <div className="mt-4 overflow-hidden rounded-2xl border border-[#1A3324] bg-[#0E2016] p-4 text-[#D8EADB] shadow-inner font-mono text-xs sm:p-5">
                        <div className="mb-2 flex items-center justify-between border-b border-[#1E3B2A] pb-2 text-[11px] text-[#86A88E]">
                          <span className="flex items-center gap-1.5 font-sans uppercase tracking-wider">
                            <span className="h-2 w-2 rounded-full bg-[#48B36E]" />
                            Live Chalkboard Inscription
                          </span>
                          <button
                            type="button"
                            onClick={() => setExpandedNoteId(isExpanded ? null : note.moduleId)}
                            className="text-[11px] text-[#A7C8AF] underline hover:text-white"
                          >
                            {isExpanded ? 'Collapse' : 'Expand full board notes'}
                          </button>
                        </div>

                        <div className={`overflow-y-auto whitespace-pre-wrap leading-relaxed ${isExpanded ? 'max-h-[600px]' : 'max-h-48'}`}>
                          {note.fullSummary}
                        </div>
                      </div>
                    </article>
                  )
                })}
              </div>
            ) : (
              <div className="rounded-3xl border border-dashed border-[#E7E9E3] bg-white p-12 text-center text-[#6B7066]">
                <BookOpen className="mx-auto h-10 w-10 text-[#A0A59B]" />
                <h4 className="mt-3 font-serif text-base font-semibold text-[#1E231B]">
                  No Chalkboard Notes Found
                </h4>
                <p className="mt-1 max-w-sm mx-auto text-xs">
                  {searchQuery
                    ? `No notes match "${searchQuery}". Try a different keyword or subject.`
                    : 'Notes written on the green chalkboard by the AI tutor will automatically save here as your single source of truth.'}
                </p>
                <Link
                  href={`/dashboard/${user.id}/class`}
                  className="mt-4 inline-flex items-center gap-2 rounded-xl bg-[#183B28] px-4 py-2 text-xs font-medium text-white shadow-xs hover:bg-[#235037]"
                >
                  <span>Start a Class to Generate Notes</span>
                  <ChevronRight className="h-3.5 w-3.5" />
                </Link>
              </div>
            )}
          </div>
        )}
      </main>
    </div>
  )
}

/**
 * Student Progress and Board Notes Caching Service
 *
 * Implements client-side caching (in-memory + sessionStorage/localStorage)
 * to avoid unnecessary Supabase DB reads and writes across dashboard navigation
 * and live classroom sessions.
 *
 * Invariant 3: Live chalkboard is the single source of truth for Master Notes.
 */

export interface Curriculum {
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

export interface SyllabusModule {
  id: string
  curriculum_id: string
  order_index: number
  title: string
  description?: string | null
  key_concepts?: string[] | null
  success_criteria?: string | null
  estimated_minutes?: number | null
  subtopics?: any
  board?: string | null
  class_level?: string | null
  chapter_notes?: string | null
}

export interface UserProgressRecord {
  id?: string
  syllabus_module_id: string
  user_id: string
  status: 'not_started' | 'in_progress' | 'completed' | 'needs_review'
  score?: number | null
  started_at?: string | null
  completed_at?: string | null
  chapter_notes?: string | null
  visual_progress?: any
  current_concept_index?: number
  completed_concepts?: string[]
  last_covered_concept?: string | null
  updated_at?: string | null
}

export interface CompletedChapter {
  id: string
  title: string
  category: string
  class_level?: string | null
  board?: string | null
  order_index?: number | null
  totalModules: number
  completedModules: number
  completedAt?: string | null
  notesCount: number
}

export interface InProgressChapter {
  id: string
  title: string
  category: string
  class_level?: string | null
  board?: string | null
  order_index?: number | null
  totalModules: number
  completedModules: number
  percentComplete: number
  activeModuleTitle?: string
  activeModuleId?: string
}

export interface SavedBoardNote {
  moduleId: string
  moduleTitle: string
  moduleOrder: number
  chapterId: string
  chapterTitle: string
  category: string
  classLevel?: string | null
  board?: string | null
  notesText: string
  roughText?: string
  fullSummary: string
  savedAt: string
  hasDiagrams: boolean
  hasFormulas: boolean
  hasRoughWork: boolean
  visualDataAvailable: boolean
}

export interface StudentProgressSummary {
  userId: string
  timestamp: number
  totalChaptersCount: number
  completedChaptersCount: number
  completedChapterIds: string[]
  completedChapters: CompletedChapter[]
  inProgressChapters: InProgressChapter[]
  notStartedChaptersCount: number
  totalModulesCount: number
  completedModulesCount: number
  inProgressModulesCount: number
  overallPercentComplete: number
  savedNotes: SavedBoardNote[]
  savedNotesCount: number
}

export interface BoardNotesCacheItem {
  userId: string
  moduleId: string
  notesText: string
  roughText?: string
  fullSummary: string
  visualProgress?: any
  updatedAt: string
  isDirty?: boolean
}

// In-memory cache for ultra-fast instant lookups during SPA session
const inMemoryProgressCache = new Map<string, { data: StudentProgressSummary; expiresAt: number }>()
const inMemoryNotesCache = new Map<string, BoardNotesCacheItem>()

// Default Cache TTL: 3 minutes for general navigation, updated immediately on writes
const CACHE_TTL_MS = 3 * 60 * 1000

/**
 * Calculates complete student progress across curriculums, modules, and progress records.
 * Pure logic function that runs on both client and server.
 */
export function calculateStudentProgress(params: {
  userId: string
  curriculums: Curriculum[]
  modules: SyllabusModule[]
  progressRecords: UserProgressRecord[]
}): StudentProgressSummary {
  const { userId, curriculums = [], modules = [], progressRecords = [] } = params

  const progressMap = new Map<string, UserProgressRecord>()
  progressRecords.forEach((p) => {
    if (p.syllabus_module_id) {
      progressMap.set(p.syllabus_module_id, p)
    }
  })

  // Map modules by curriculum
  const modulesByCurriculum = new Map<string, SyllabusModule[]>()
  modules.forEach((mod) => {
    const list = modulesByCurriculum.get(mod.curriculum_id) || []
    list.push(mod)
    modulesByCurriculum.set(mod.curriculum_id, list)
  })

  const completedChapters: CompletedChapter[] = []
  const inProgressChapters: InProgressChapter[] = []
  let notStartedChaptersCount = 0

  curriculums.forEach((curr) => {
    const currMods = (modulesByCurriculum.get(curr.id) || []).sort(
      (a, b) => a.order_index - b.order_index
    )
    const totalCount = currMods.length

    if (totalCount === 0) {
      return
    }

    let completedInCurr = 0
    let inProgressInCurr = 0
    let lastCompletedAt: string | null = null
    let notesInCurr = 0
    let firstIncompleteMod: SyllabusModule | null = null

    for (const mod of currMods) {
      const rec = progressMap.get(mod.id)
      const isDone = rec?.status === 'completed' || !!rec?.completed_at
      const isInProg = rec?.status === 'in_progress' && !isDone

      if (isDone) {
        completedInCurr += 1
        if (rec?.completed_at) {
          if (!lastCompletedAt || new Date(rec.completed_at) > new Date(lastCompletedAt)) {
            lastCompletedAt = rec.completed_at
          }
        }
      } else if (isInProg) {
        inProgressInCurr += 1
      }

      if (!isDone && !firstIncompleteMod) {
        firstIncompleteMod = mod
      }

      if (rec?.chapter_notes && rec.chapter_notes.trim().length > 10) {
        notesInCurr += 1
      }
    }

    if (completedInCurr === totalCount && totalCount > 0) {
      completedChapters.push({
        id: curr.id,
        title: curr.title,
        category: curr.category || 'General',
        class_level: curr.class_level,
        board: curr.board,
        order_index: curr.order_index,
        totalModules: totalCount,
        completedModules: completedInCurr,
        completedAt: lastCompletedAt,
        notesCount: notesInCurr,
      })
    } else if (completedInCurr > 0 || inProgressInCurr > 0) {
      const percent = Math.round((completedInCurr / totalCount) * 100)
      inProgressChapters.push({
        id: curr.id,
        title: curr.title,
        category: curr.category || 'General',
        class_level: curr.class_level,
        board: curr.board,
        order_index: curr.order_index,
        totalModules: totalCount,
        completedModules: completedInCurr,
        percentComplete: percent,
        activeModuleTitle: firstIncompleteMod?.title || currMods[0]?.title,
        activeModuleId: firstIncompleteMod?.id || currMods[0]?.id,
      })
    } else {
      notStartedChaptersCount += 1
    }
  })

  // Extract saved board notes from user progress records
  const savedNotes: SavedBoardNote[] = []
  const curriculumMap = new Map<string, Curriculum>()
  curriculums.forEach((c) => curriculumMap.set(c.id, c))

  const moduleMap = new Map<string, SyllabusModule>()
  modules.forEach((m) => moduleMap.set(m.id, m))

  progressRecords.forEach((p) => {
    const rawNotes = (p.chapter_notes || '').trim()
    if (!rawNotes || rawNotes.length < 5) return

    const mod = moduleMap.get(p.syllabus_module_id)
    const curr = mod ? curriculumMap.get(mod.curriculum_id) : null

    // Determine metadata from notes content
    const hasDiagrams =
      rawNotes.includes('[DIAGRAM:') ||
      rawNotes.includes('Diagram:') ||
      rawNotes.toLowerCase().includes('drawn diagram') ||
      !!(p.visual_progress?.whiteboard_pages?.length)
    const hasFormulas =
      rawNotes.includes('=') ||
      rawNotes.includes('\\') ||
      rawNotes.toLowerCase().includes('formula') ||
      rawNotes.includes('• Formula:')
    const hasRoughWork =
      rawNotes.includes('[ROUGH_WORK') ||
      rawNotes.includes('ROUGH WORK') ||
      rawNotes.toLowerCase().includes('scratch')

    savedNotes.push({
      moduleId: p.syllabus_module_id,
      moduleTitle: mod?.title || 'Classroom Lesson',
      moduleOrder: mod?.order_index || 1,
      chapterId: curr?.id || '',
      chapterTitle: curr?.title || 'Academic Chapter',
      category: curr?.category || 'General',
      classLevel: curr?.class_level || mod?.class_level,
      board: curr?.board || mod?.board,
      notesText: rawNotes,
      roughText: '',
      fullSummary: rawNotes,
      savedAt: p.updated_at || p.completed_at || new Date().toISOString(),
      hasDiagrams,
      hasFormulas,
      hasRoughWork,
      visualDataAvailable: !!(p.visual_progress?.whiteboard_pages?.length),
    })
  })

  // Sort notes by chapter and module order
  savedNotes.sort((a, b) => {
    if (a.chapterTitle !== b.chapterTitle) {
      return a.chapterTitle.localeCompare(b.chapterTitle)
    }
    return a.moduleOrder - b.moduleOrder
  })

  const totalModulesCount = modules.length
  const completedModulesCount = progressRecords.filter(
    (p) => p.status === 'completed' || !!p.completed_at
  ).length
  const inProgressModulesCount = progressRecords.filter(
    (p) => p.status === 'in_progress' && !p.completed_at
  ).length
  const overallPercentComplete =
    totalModulesCount > 0 ? Math.round((completedModulesCount / totalModulesCount) * 100) : 0

  return {
    userId,
    timestamp: Date.now(),
    totalChaptersCount: curriculums.length,
    completedChaptersCount: completedChapters.length,
    completedChapterIds: completedChapters.map((c) => c.id),
    completedChapters,
    inProgressChapters,
    notStartedChaptersCount,
    totalModulesCount,
    completedModulesCount,
    inProgressModulesCount,
    overallPercentComplete,
    savedNotes,
    savedNotesCount: savedNotes.length,
  }
}

/**
 * Client-Side Cache Getter: returns cached student progress if still within TTL.
 * Checks in-memory cache first, then sessionStorage / localStorage.
 */
export function getCachedStudentProgress(userId: string): StudentProgressSummary | null {
  if (!userId) return null

  // 1. In-memory check
  const mem = inMemoryProgressCache.get(userId)
  if (mem && Date.now() < mem.expiresAt) {
    return mem.data
  }

  // 2. Storage check
  if (typeof window !== 'undefined') {
    try {
      const storageKey = `ai_tutor_progress_cache_${userId}`
      const raw = sessionStorage.getItem(storageKey) || localStorage.getItem(storageKey)
      if (raw) {
        const parsed = JSON.parse(raw) as StudentProgressSummary
        if (parsed && Date.now() - parsed.timestamp < CACHE_TTL_MS) {
          inMemoryProgressCache.set(userId, {
            data: parsed,
            expiresAt: Date.now() + (CACHE_TTL_MS - (Date.now() - parsed.timestamp)),
          })
          return parsed
        }
      }
    } catch (err) {
      console.warn('Failed reading student progress cache from storage:', err)
    }
  }

  return null
}

/**
 * Client-Side Cache Setter: persists progress summary to memory and storage.
 */
export function setCachedStudentProgress(userId: string, data: StudentProgressSummary): void {
  if (!userId || !data) return

  // Update in-memory
  inMemoryProgressCache.set(userId, {
    data,
    expiresAt: Date.now() + CACHE_TTL_MS,
  })

  // Update web storage
  if (typeof window !== 'undefined') {
    try {
      const storageKey = `ai_tutor_progress_cache_${userId}`
      const json = JSON.stringify(data)
      sessionStorage.setItem(storageKey, json)
      localStorage.setItem(storageKey, json)
    } catch (err) {
      console.warn('Failed writing student progress cache to storage:', err)
    }
  }
}

/**
 * Invalidate cached progress for a student (e.g. after capsule completion or save).
 */
export function invalidateStudentProgressCache(userId: string): void {
  if (!userId) return
  inMemoryProgressCache.delete(userId)
  if (typeof window !== 'undefined') {
    try {
      const storageKey = `ai_tutor_progress_cache_${userId}`
      sessionStorage.removeItem(storageKey)
      localStorage.removeItem(storageKey)
    } catch {}
  }
}

/**
 * Cache individual board notes for a module (text, rough work, full summary, visual state).
 */
/**
 * Safely evicts older cached board notes and whiteboard keys when localStorage quota is exceeded.
 */
function pruneStaleLocalStorageKeys(currentModuleId?: string): void {
  if (typeof window === 'undefined') return
  try {
    const keysToRemove: string[] = []
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i)
      if (!key) continue
      // Prune old whiteboard file payloads from other modules (largest consumers of quota)
      if (key.includes('_files') && (!currentModuleId || !key.includes(currentModuleId))) {
        keysToRemove.push(key)
      }
      // Prune old whiteboard pages from other modules
      else if (key.startsWith('whiteboard_pages_') && (!currentModuleId || !key.includes(currentModuleId))) {
        keysToRemove.push(key)
      }
      // Prune older notes entries
      else if (key.startsWith('ai_tutor_board_notes_') && (!currentModuleId || !key.includes(currentModuleId))) {
        keysToRemove.push(key)
      }
    }
    for (const k of keysToRemove) {
      localStorage.removeItem(k)
    }
  } catch {}
}

export function setCachedBoardNotes(item: BoardNotesCacheItem): void {
  if (!item.userId || !item.moduleId) return

  const key = `${item.userId}_${item.moduleId}`
  inMemoryNotesCache.set(key, item)

  if (typeof window !== 'undefined') {
    const storageKey = `ai_tutor_board_notes_${item.userId}_${item.moduleId}`
    try {
      localStorage.setItem(storageKey, JSON.stringify(item))
    } catch (err: any) {
      if (err?.name === 'QuotaExceededError' || err?.code === 22) {
        // Prune older entries from other modules and retry once
        pruneStaleLocalStorageKeys(item.moduleId)
        try {
          localStorage.setItem(storageKey, JSON.stringify(item))
        } catch {
          // In-memory cache retains full state safely; suppress further console noise
        }
      }
    }
  }
}

/**
 * Retrieve cached board notes for a module.
 */
export function getCachedBoardNotes(
  userId: string,
  moduleId: string
): BoardNotesCacheItem | null {
  if (!userId || !moduleId) return null

  const key = `${userId}_${moduleId}`
  const mem = inMemoryNotesCache.get(key)
  if (mem) return mem

  if (typeof window !== 'undefined') {
    try {
      const storageKey = `ai_tutor_board_notes_${userId}_${moduleId}`
      const raw = localStorage.getItem(storageKey)
      if (raw) {
        const parsed = JSON.parse(raw) as BoardNotesCacheItem
        inMemoryNotesCache.set(key, parsed)
        return parsed
      }
    } catch (err) {
      console.warn('Failed retrieving board notes from localStorage:', err)
    }
  }

  return null
}

/**
 * Retrieve all locally cached board notes for a user across all modules.
 */
export function getAllCachedBoardNotesForUser(userId: string): BoardNotesCacheItem[] {
  if (!userId || typeof window === 'undefined') return []

  const notes: BoardNotesCacheItem[] = []
  const prefix = `ai_tutor_board_notes_${userId}_`

  try {
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i)
      if (key && key.startsWith(prefix)) {
        const raw = localStorage.getItem(key)
        if (raw) {
          try {
            notes.push(JSON.parse(raw))
          } catch {}
        }
      }
    }
  } catch (err) {
    console.warn('Failed retrieving all cached board notes:', err)
  }

  return notes
}

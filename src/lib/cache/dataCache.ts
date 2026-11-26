/**
 * Data Cache Subsystem: Multi-Tier Caching with Global Store & In-Flight Request Coalescing
 * Eliminates duplicate Supabase PostgreSQL queries across API routes, Server Components,
 * Server Actions, and browser sessions while invalidating immediately on writes.
 */

import { SupabaseClient } from '@supabase/supabase-js'

interface CacheEntry<T> {
  data: T
  expiresAt: number
}

interface StoreOptions {
  ttlMs?: number
  prefix?: string
  persistToSessionStorage?: boolean
}

export class InMemoryTTLStore {
  private store = new Map<string, CacheEntry<any>>()
  private inflight = new Map<string, Promise<any>>()
  private defaultTtlMs: number
  private prefix: string
  private persistToSessionStorage: boolean

  constructor(defaultTtlMs: number = 10 * 60 * 1000, prefixOrOpts: string | StoreOptions = 'ai_tutor_cache_') {
    if (typeof prefixOrOpts === 'string') {
      this.defaultTtlMs = defaultTtlMs
      this.prefix = prefixOrOpts
      this.persistToSessionStorage = true
    } else {
      this.defaultTtlMs = prefixOrOpts.ttlMs ?? defaultTtlMs
      this.prefix = prefixOrOpts.prefix ?? 'ai_tutor_cache_'
      this.persistToSessionStorage = prefixOrOpts.persistToSessionStorage !== false
    }
  }

  public get<T>(key: string): T | null {
    const entry = this.store.get(key)
    if (entry) {
      if (Date.now() > entry.expiresAt) {
        this.store.delete(key)
      } else {
        return entry.data as T
      }
    }

    if (this.persistToSessionStorage && typeof window !== 'undefined' && window.sessionStorage) {
      try {
        const raw = window.sessionStorage.getItem(this.prefix + key)
        if (raw) {
          const parsed: CacheEntry<T> = JSON.parse(raw)
          if (Date.now() > parsed.expiresAt) {
            window.sessionStorage.removeItem(this.prefix + key)
          } else {
            this.store.set(key, parsed)
            return parsed.data
          }
        }
      } catch {
        // Fallback silently if sessionStorage is unavailable
      }
    }

    return null
  }

  public set<T>(key: string, data: T, ttlMs?: number): void {
    const ttl = ttlMs ?? this.defaultTtlMs
    const entry: CacheEntry<T> = {
      data,
      expiresAt: Date.now() + ttl,
    }
    this.store.set(key, entry)

    if (this.persistToSessionStorage && typeof window !== 'undefined' && window.sessionStorage) {
      try {
        window.sessionStorage.setItem(this.prefix + key, JSON.stringify(entry))
      } catch {
        // Quota exceeded or private browsing guard
      }
    }
  }

  public delete(key: string): void {
    this.store.delete(key)
    this.inflight.delete(key)
    if (this.persistToSessionStorage && typeof window !== 'undefined' && window.sessionStorage) {
      try {
        window.sessionStorage.removeItem(this.prefix + key)
      } catch {}
    }
  }

  public invalidateByPrefix(prefix: string): void {
    for (const k of Array.from(this.store.keys())) {
      if (k.startsWith(prefix)) this.store.delete(k)
    }
    for (const k of Array.from(this.inflight.keys())) {
      if (k.startsWith(prefix)) this.inflight.delete(k)
    }
    if (this.persistToSessionStorage && typeof window !== 'undefined' && window.sessionStorage) {
      try {
        const toRemove: string[] = []
        const fullPrefix = this.prefix + prefix
        for (let i = 0; i < window.sessionStorage.length; i++) {
          const k = window.sessionStorage.key(i)
          if (k && k.startsWith(fullPrefix)) toRemove.push(k)
        }
        toRemove.forEach((k) => window.sessionStorage.removeItem(k))
      } catch {}
    }
  }

  public clear(): void {
    this.store.clear()
    this.inflight.clear()
    if (this.persistToSessionStorage && typeof window !== 'undefined' && window.sessionStorage) {
      try {
        const keysToRemove: string[] = []
        for (let i = 0; i < window.sessionStorage.length; i++) {
          const k = window.sessionStorage.key(i)
          if (k && k.startsWith(this.prefix)) {
            keysToRemove.push(k)
          }
        }
        keysToRemove.forEach((k) => window.sessionStorage.removeItem(k))
      } catch {}
    }
  }

  public async getOrSet<T>(
    key: string,
    fetcher: () => Promise<T>,
    ttlMs?: number
  ): Promise<T> {
    const existing = this.get<T>(key)
    if (existing !== null && existing !== undefined) {
      return existing
    }

    const pending = this.inflight.get(key)
    if (pending) {
      return pending as Promise<T>
    }

    const promise = fetcher()
      .then((fresh) => {
        if (fresh !== null && fresh !== undefined) {
          this.set(key, fresh, ttlMs)
        }
        return fresh
      })
      .finally(() => {
        this.inflight.delete(key)
      })

    this.inflight.set(key, promise)
    return promise
  }
}

interface GlobalDataCaches {
  curriculum: InMemoryTTLStore
  module: InMemoryTTLStore
  sibling: InMemoryTTLStore
  counts: InMemoryTTLStore
  nextChapter: InMemoryTTLStore
  curriculumModules: InMemoryTTLStore
  pyq: InMemoryTTLStore
  adminCurriculums: InMemoryTTLStore
  profile: InMemoryTTLStore
  userProgress: InMemoryTTLStore
  enrollments: InMemoryTTLStore
  userMemories: InMemoryTTLStore
  studyPlan: InMemoryTTLStore
  subscription: InMemoryTTLStore
}

function getGlobalCaches(): GlobalDataCaches {
  const g = globalThis as any
  if (!g.__aiTutorDataCaches) {
    g.__aiTutorDataCaches = {
      curriculum: new InMemoryTTLStore(15 * 60 * 1000, { prefix: 'ai_tutor_curr_' }),
      module: new InMemoryTTLStore(15 * 60 * 1000, { prefix: 'ai_tutor_mod_' }),
      sibling: new InMemoryTTLStore(15 * 60 * 1000, { prefix: 'ai_tutor_sib_' }),
      counts: new InMemoryTTLStore(30 * 60 * 1000, { prefix: 'ai_tutor_cnt_' }),
      nextChapter: new InMemoryTTLStore(30 * 60 * 1000, { prefix: 'ai_tutor_next_' }),
      curriculumModules: new InMemoryTTLStore(15 * 60 * 1000, { prefix: 'ai_tutor_cmods_' }),
      pyq: new InMemoryTTLStore(10 * 60 * 1000, { prefix: 'ai_tutor_pyq_' }),
      adminCurriculums: new InMemoryTTLStore(10 * 60 * 1000, { persistToSessionStorage: false }),
      profile: new InMemoryTTLStore(2 * 60 * 1000, { persistToSessionStorage: false }),
      userProgress: new InMemoryTTLStore(2 * 60 * 1000, { persistToSessionStorage: false }),
      enrollments: new InMemoryTTLStore(3 * 60 * 1000, { persistToSessionStorage: false }),
      userMemories: new InMemoryTTLStore(5 * 60 * 1000, { persistToSessionStorage: false }),
      studyPlan: new InMemoryTTLStore(5 * 60 * 1000, { persistToSessionStorage: false }),
      subscription: new InMemoryTTLStore(3 * 60 * 1000, { persistToSessionStorage: false }),
    } satisfies GlobalDataCaches
  }
  return g.__aiTutorDataCaches as GlobalDataCaches
}

const caches = getGlobalCaches()

// 1. Exported Stores (Shared via globalThis across routes/HMR)
export const curriculumCacheStore = caches.curriculum
export const moduleCacheStore = caches.module
export const siblingCacheStore = caches.sibling
export const countsCacheStore = caches.counts
export const nextChapterCacheStore = caches.nextChapter
export const curriculumModulesCacheStore = caches.curriculumModules
export const pyqCacheStore = caches.pyq
export const adminCurriculumsCacheStore = caches.adminCurriculums
export const profileCacheStore = caches.profile
export const userProgressCacheStore = caches.userProgress
export const enrollmentsCacheStore = caches.enrollments
export const userMemoriesCacheStore = caches.userMemories
export const studyPlanCacheStore = caches.studyPlan
export const subscriptionCacheStore = caches.subscription

// 2. Catalog Cached Fetchers

export async function getCachedSyllabusModule(
  supabase: SupabaseClient<any, any, any>,
  moduleId: string
): Promise<any | null> {
  if (!moduleId) return null
  const cacheKey = `module_${moduleId}`
  return moduleCacheStore.getOrSet(cacheKey, async () => {
    const { data, error } = await supabase
      .from('syllabus_modules')
      .select('*, curriculums(*)')
      .eq('id', moduleId)
      .maybeSingle()

    if (error) {
      console.warn(`[DataCache] Failed fetching module ${moduleId}:`, error.message)
      return null
    }
    return data
  })
}

export async function getCachedSiblingModules(
  supabase: SupabaseClient<any, any, any>,
  curriculumId: string
): Promise<any[]> {
  if (!curriculumId) return []
  const cacheKey = `siblings_${curriculumId}`
  return siblingCacheStore.getOrSet(cacheKey, async () => {
    const { data, error } = await supabase
      .from('syllabus_modules')
      .select('id, title, order_index, estimated_minutes, description')
      .eq('curriculum_id', curriculumId)
      .order('order_index', { ascending: true })

    if (error) {
      console.warn(`[DataCache] Failed fetching siblings for ${curriculumId}:`, error.message)
      return []
    }
    return data || []
  })
}

export async function getCachedCurriculumModules(
  supabase: SupabaseClient<any, any, any>,
  curriculumIds: string[]
): Promise<any[]> {
  if (!curriculumIds || curriculumIds.length === 0) return []
  const sortedKey = [...curriculumIds].sort().join('_')
  const cacheKey = `curr_modules_${sortedKey}`

  return curriculumModulesCacheStore.getOrSet(cacheKey, async () => {
    const { data, error } = await supabase
      .from('syllabus_modules')
      .select('id, curriculum_id, order_index, title, description, estimated_minutes, key_concepts, success_criteria, class_level, board, subtopics, chapter_notes, curriculums(*)')
      .in('curriculum_id', curriculumIds)
      .order('order_index', { ascending: true })

    if (error) {
      console.warn('[DataCache] Failed fetching modules for curriculums:', error.message)
      return []
    }
    return data || []
  })
}

export async function getCachedCurriculums(
  supabase: SupabaseClient<any, any, any>,
  filters?: { classLevel?: string | null; board?: string | null; isPublished?: boolean }
): Promise<any[]> {
  const isPub = filters?.isPublished !== false
  const cacheKey = `curriculums_${filters?.classLevel || 'all'}_${filters?.board || 'all'}_${isPub}`

  return curriculumCacheStore.getOrSet(cacheKey, async () => {
    let q = supabase.from('curriculums').select('*').eq('is_published', isPub)

    if (filters?.classLevel) {
      q = q.or(`class_level.eq.${filters.classLevel},class_level.is.null`)
    }
    if (filters?.board) {
      q = q.eq('board', filters.board)
    }

    const { data, error } = await q
      .order('order_index', { ascending: true })
      .order('created_at', { ascending: true })

    if (error) {
      console.warn('[DataCache] Failed fetching curriculums:', error.message)
      return []
    }
    return data || []
  })
}

export async function getCachedCurriculumModuleCounts(
  supabase: SupabaseClient<any, any, any>,
  targetCurriculumIds?: string[]
): Promise<Map<string, number>> {
  const isTargeted = Array.isArray(targetCurriculumIds) && targetCurriculumIds.length > 0
  const cacheKey = isTargeted
    ? `counts_${targetCurriculumIds!.sort().join('_')}`
    : 'counts_all_curriculums'

  const countsMapObj = await countsCacheStore.getOrSet(cacheKey, async () => {
    let query = supabase.from('syllabus_modules').select('id, curriculum_id')
    if (isTargeted) {
      query = query.in('curriculum_id', targetCurriculumIds!)
    }

    const { data, error } = await query
    if (error) {
      console.warn('[DataCache] Failed fetching module counts:', error.message)
      return {}
    }

    const counts: Record<string, number> = {}
    ;(data || []).forEach((row: any) => {
      if (row.curriculum_id) {
        counts[row.curriculum_id] = (counts[row.curriculum_id] || 0) + 1
      }
    })
    return counts
  })

  const result = new Map<string, number>()
  Object.entries(countsMapObj || {}).forEach(([k, v]) => result.set(k, v))
  return result
}

export async function getCachedNextChapterInfo(
  supabase: SupabaseClient<any, any, any>,
  params: {
    classLevel?: string
    category?: string
    currentOrderIndex?: number
    board?: string
  }
): Promise<{
  chapterId: string
  chapterTitle: string
  firstModuleId: string
  firstModuleTitle: string
  orderIndex: number
} | null> {
  const { classLevel, category, currentOrderIndex = 1, board } = params
  if (!classLevel || !category) return null

  const cacheKey = `next_chapter_${classLevel}_${category}_${board || 'all'}_${currentOrderIndex}`

  return nextChapterCacheStore.getOrSet(cacheKey, async () => {
    let nextQuery = supabase
      .from('curriculums')
      .select('id, title, order_index, category, class_level, board')
      .eq('class_level', classLevel)
      .eq('category', category)
      .gt('order_index', currentOrderIndex)

    if (board) {
      nextQuery = nextQuery.eq('board', board)
    }

    const { data: nextChapters, error: currErr } = await nextQuery
      .order('order_index', { ascending: true })
      .limit(1)

    if (currErr || !nextChapters || nextChapters.length === 0) {
      return null
    }

    const nextChapter = nextChapters[0]
    const { data: nextModules, error: modErr } = await supabase
      .from('syllabus_modules')
      .select('id, title, order_index, description')
      .eq('curriculum_id', nextChapter.id)
      .order('order_index', { ascending: true })
      .limit(1)

    if (modErr || !nextModules || nextModules.length === 0) {
      return null
    }

    return {
      chapterId: nextChapter.id,
      chapterTitle: nextChapter.title,
      firstModuleId: nextModules[0].id,
      firstModuleTitle: nextModules[0].title,
      orderIndex: nextChapter.order_index,
    }
  })
}

export async function getCachedChapterPyqs(
  supabase: SupabaseClient<any, any, any>,
  filters?: { curriculumId?: string | null; board?: string | null; classLevel?: string | null; category?: string | null }
): Promise<any[]> {
  const cacheKey = `pyq_${filters?.curriculumId || 'all'}_${filters?.board || 'all'}_${filters?.classLevel || 'all'}_${filters?.category || 'all'}`
  return pyqCacheStore.getOrSet(cacheKey, async () => {
    let query = supabase.from('chapter_pyqs').select('*')
    if (filters?.curriculumId) query = query.eq('curriculum_id', filters.curriculumId)
    if (filters?.board) query = query.eq('board', filters.board)
    if (filters?.classLevel) query = query.eq('class_level', filters.classLevel)
    if (filters?.category) query = query.eq('category', filters.category)

    const { data, error } = await query.order('created_at', { ascending: false })
    if (error) {
      console.warn('[DataCache] Failed fetching chapter PYQs:', error.message)
      throw new Error(error.message)
    }
    return data || []
  })
}

// 3. Per-User Cached Fetchers (In-memory TTL + strict invalidation on writes)

export async function getCachedUserProfile(
  supabase: SupabaseClient<any, any, any>,
  userId: string
): Promise<any | null> {
  if (!userId) return null
  return profileCacheStore.getOrSet(`profile_${userId}`, async () => {
    const { data, error } = await supabase
      .from('profiles')
      .select('*')
      .eq('id', userId)
      .maybeSingle()

    if (error) {
      console.warn(`[DataCache] Failed fetching profile ${userId}:`, error.message)
      return null
    }
    return data
  })
}

export async function getCachedUserProgressList(
  supabase: SupabaseClient<any, any, any>,
  userId: string
): Promise<any[]> {
  if (!userId) return []
  return userProgressCacheStore.getOrSet(`progress_list_${userId}`, async () => {
    const { data, error } = await supabase
      .from('user_progress')
      .select('*')
      .eq('user_id', userId)

    if (error) {
      console.warn(`[DataCache] Failed fetching progress list for ${userId}:`, error.message)
      return []
    }
    return data || []
  })
}

export async function getCachedModuleProgress(
  supabase: SupabaseClient<any, any, any>,
  userId: string,
  moduleId: string
): Promise<any | null> {
  if (!userId || !moduleId) return null

  const existingList = userProgressCacheStore.get<any[]>(`progress_list_${userId}`)
  if (Array.isArray(existingList)) {
    const match = existingList.find((r) => r.syllabus_module_id === moduleId)
    if (match) return match
  }

  return userProgressCacheStore.getOrSet(`progress_${userId}_${moduleId}`, async () => {
    const res = await supabase
      .from('user_progress')
      .select(
        'status, chapter_notes, current_concept_index, completed_concepts, last_covered_concept, visual_progress, is_paused, completed_at'
      )
      .eq('user_id', userId)
      .eq('syllabus_module_id', moduleId)
      .maybeSingle()

    if (res.error && res.error.code === '42703') {
      const fallback = await supabase
        .from('user_progress')
        .select(
          'status, chapter_notes, current_concept_index, completed_concepts, last_covered_concept, completed_at'
        )
        .eq('user_id', userId)
        .eq('syllabus_module_id', moduleId)
        .maybeSingle()
      return fallback.data || null
    }
    return res.data || null
  })
}

export async function getCachedUserEnrollments(
  supabase: SupabaseClient<any, any, any>,
  userId: string
): Promise<any[]> {
  if (!userId) return []
  return enrollmentsCacheStore.getOrSet(`enrollments_${userId}`, async () => {
    const { data, error } = await supabase
      .from('enrollments')
      .select('id, status, enrolled_at, curriculum_id, curriculums (*)')
      .eq('user_id', userId)
      .eq('status', 'active')
      .order('enrolled_at', { ascending: true })

    if (error) {
      console.warn(`[DataCache] Failed fetching enrollments for ${userId}:`, error.message)
      return []
    }
    return data || []
  })
}

export async function getCachedUserMemories(
  supabase: SupabaseClient<any, any, any>,
  userId: string,
  limit: number = 10
): Promise<any[]> {
  if (!userId) return []
  return userMemoriesCacheStore.getOrSet(`memories_${userId}_${limit}`, async () => {
    const { data, error } = await supabase
      .from('ai_user_memories')
      .select('*')
      .eq('user_id', userId)
      .order('importance_score', { ascending: false })
      .limit(limit)

    if (error) {
      console.warn(`[DataCache] Failed fetching memories for ${userId}:`, error.message)
      return []
    }
    return data || []
  })
}

export async function getCachedActiveStudyPlan(
  supabase: SupabaseClient<any, any, any>,
  userId: string
): Promise<any | null> {
  if (!userId) return null
  return studyPlanCacheStore.getOrSet(`study_plan_${userId}`, async () => {
    const { data, error } = await supabase
      .from('student_study_plans')
      .select('*')
      .eq('user_id', userId)
      .eq('is_active', true)
      .maybeSingle()

    if (error) {
      console.warn(`[DataCache] Failed fetching study plan for ${userId}:`, error.message)
      return null
    }
    return data || null
  })
}

// 4. Cache Invalidators

export function invalidateCurriculumCache(): void {
  curriculumCacheStore.clear()
  curriculumModulesCacheStore.clear()
  adminCurriculumsCacheStore.clear()
  countsCacheStore.clear()
  nextChapterCacheStore.clear()
}

export function invalidateModuleCache(moduleId?: string, curriculumId?: string): void {
  if (moduleId) {
    moduleCacheStore.delete(`module_${moduleId}`)
  } else {
    moduleCacheStore.clear()
  }
  if (curriculumId) {
    siblingCacheStore.delete(`siblings_${curriculumId}`)
    countsCacheStore.delete(`counts_all_curriculums`)
  }
  curriculumModulesCacheStore.clear()
  adminCurriculumsCacheStore.clear()
}

export function invalidatePyqCache(): void {
  pyqCacheStore.clear()
}

export function invalidateUserProfileCache(userId?: string): void {
  if (!userId) return
  profileCacheStore.delete(`profile_${userId}`)
}

export function invalidateUserProgressCache(userId?: string, moduleId?: string): void {
  if (!userId) return
  userProgressCacheStore.delete(`progress_list_${userId}`)
  if (moduleId) {
    userProgressCacheStore.delete(`progress_${userId}_${moduleId}`)
  } else {
    userProgressCacheStore.invalidateByPrefix(`progress_${userId}_`)
  }
}

export function invalidateUserEnrollmentsCache(userId?: string): void {
  if (!userId) return
  enrollmentsCacheStore.delete(`enrollments_${userId}`)
}

export function invalidateUserMemoriesCache(userId?: string): void {
  if (!userId) return
  userMemoriesCacheStore.invalidateByPrefix(`memories_${userId}_`)
}

export function invalidateStudyPlanCache(userId?: string): void {
  if (!userId) return
  studyPlanCacheStore.delete(`study_plan_${userId}`)
}

export function invalidateSubscriptionCache(userId?: string): void {
  if (!userId) return
  subscriptionCacheStore.delete(`sub_${userId}`)
}

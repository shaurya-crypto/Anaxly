/**
 * SessionStateManager
 * Provides instantaneous client-side persistence for live classroom sessions.
 * Caches active concept index, pedagogical stage, and chalkboard state in localStorage
 * to ensure seamless F5/refresh resumption without restarting from Concept 0.
 *
 * User Invariant: Save in local first for instant resume, background-sync to Supabase DB,
 * and prune expired sessions to prevent local out-of-memory.
 */

export interface ClassroomSessionState {
  moduleId: string;
  currentConceptIndex: number;
  currentStage: string;
  completedConcepts: string[];
  lastCoveredConcept?: string;
  chalkboardPageIndex: number;
  chapterNotes?: string;
  updatedAt: number;
}

const STORAGE_PREFIX = 'anaxly_classroom_session_';
const SESSION_TTL_MS = 2 * 60 * 60 * 1000; // 2 hours for instant resume validity
const PRUNE_TTL_MS = 24 * 60 * 60 * 1000; // 24 hours for total eviction

export function saveSessionState(
  moduleId: string,
  state: Partial<ClassroomSessionState>
): void {
  if (typeof window === 'undefined' || !moduleId) return;
  try {
    const existing = loadSessionState(moduleId);
    const merged: ClassroomSessionState = {
      moduleId,
      currentConceptIndex: state.currentConceptIndex ?? existing?.currentConceptIndex ?? 0,
      currentStage: state.currentStage ?? existing?.currentStage ?? 'REAL_LIFE_INTUITION',
      completedConcepts: state.completedConcepts ?? existing?.completedConcepts ?? [],
      lastCoveredConcept: state.lastCoveredConcept ?? existing?.lastCoveredConcept,
      chalkboardPageIndex: state.chalkboardPageIndex ?? existing?.chalkboardPageIndex ?? 0,
      chapterNotes: state.chapterNotes ?? existing?.chapterNotes,
      updatedAt: Date.now(),
    };
    localStorage.setItem(`${STORAGE_PREFIX}${moduleId}`, JSON.stringify(merged));
  } catch (err) {
    console.warn('[SessionStateManager] Failed to save session state to localStorage:', err);
  }
}

export function loadSessionState(moduleId: string): ClassroomSessionState | null {
  if (typeof window === 'undefined' || !moduleId) return null;
  try {
    const raw = localStorage.getItem(`${STORAGE_PREFIX}${moduleId}`);
    if (!raw) return null;
    const parsed: ClassroomSessionState = JSON.parse(raw);
    if (!parsed || typeof parsed !== 'object') return null;

    // Reject stale sessions older than 2 hours
    if (Date.now() - (parsed.updatedAt || 0) > SESSION_TTL_MS) {
      localStorage.removeItem(`${STORAGE_PREFIX}${moduleId}`);
      return null;
    }
    return parsed;
  } catch {
    return null;
  }
}

export function clearSessionState(moduleId: string): void {
  if (typeof window === 'undefined' || !moduleId) return;
  try {
    localStorage.removeItem(`${STORAGE_PREFIX}${moduleId}`);
  } catch {}
}

export function pruneExpiredSessions(): void {
  if (typeof window === 'undefined') return;
  try {
    const now = Date.now();
    const toRemove: string[] = [];
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (key && key.startsWith(STORAGE_PREFIX)) {
        try {
          const val = localStorage.getItem(key);
          if (val) {
            const parsed = JSON.parse(val);
            if (!parsed?.updatedAt || now - parsed.updatedAt > PRUNE_TTL_MS) {
              toRemove.push(key);
            }
          }
        } catch {
          toRemove.push(key);
        }
      }
    }
    for (const k of toRemove) {
      localStorage.removeItem(k);
    }
  } catch {}
}

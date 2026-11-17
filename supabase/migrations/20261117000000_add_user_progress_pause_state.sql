-- Migration: Add is_paused to user_progress table and ensure preferred_teacher_voice on profiles
-- Supports explicit pause/resume session state persistence in database without overloading local storage.

ALTER TABLE public.user_progress
  ADD COLUMN IF NOT EXISTS is_paused boolean DEFAULT false;

ALTER TABLE public.profiles
  ADD COLUMN IF NOT EXISTS preferred_teacher_voice text DEFAULT 'Charon';

-- Add index on is_paused for fast session restoration queries
CREATE INDEX IF NOT EXISTS idx_user_progress_is_paused ON public.user_progress (user_id, is_paused);

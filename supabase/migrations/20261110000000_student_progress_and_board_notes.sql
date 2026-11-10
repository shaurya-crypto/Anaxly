-- Migration: 20261110000000_student_progress_and_board_notes.sql
-- Description: Add completed_chapters_count and completed_chapter_ids to profiles table for zero-DB-load caching

ALTER TABLE public.profiles
ADD COLUMN IF NOT EXISTS completed_chapters_count integer DEFAULT 0,
ADD COLUMN IF NOT EXISTS completed_chapter_ids text[] DEFAULT ARRAY[]::text[];

-- Fast index for retrieving user progress by status
CREATE INDEX IF NOT EXISTS idx_user_progress_status_user ON public.user_progress (user_id, status);

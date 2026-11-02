-- Migration: 20261102000000_database_cleanup_and_performance_optimization.sql
-- Description: Drop duplicate indexes, add missing foreign key covering indexes,
-- purge legacy dangerous/redundant permissive RLS policies, and optimize auth.uid() subqueries.

-- ==============================================================================
-- 1. DROP DUPLICATE INDEXES
-- ==============================================================================
-- Table curriculums had two identical compound indexes on (board, class_level, category, order_index)
DROP INDEX IF EXISTS public.idx_curriculums_board_class_cat_order;

-- Table syllabus_modules had two identical compound indexes on (curriculum_id, order_index)
DROP INDEX IF EXISTS public.idx_syllabus_modules_curr_order;


-- ==============================================================================
-- 2. ADD MISSING FOREIGN KEY COVERING INDEXES
-- ==============================================================================
CREATE INDEX IF NOT EXISTS idx_enrollments_curriculum_id 
  ON public.enrollments (curriculum_id);

CREATE INDEX IF NOT EXISTS idx_user_progress_module_id 
  ON public.user_progress (syllabus_module_id);

CREATE INDEX IF NOT EXISTS idx_study_session_logs_module_id 
  ON public.study_session_logs (syllabus_module_id);


-- ==============================================================================
-- 3. PURGE DUPLICATE & UNSAFE LEGACY PERMISSIVE RLS POLICIES
-- ==============================================================================

-- A. CURRICULUMS
DROP POLICY IF EXISTS "Allow all on curriculums" ON public.curriculums;
DROP POLICY IF EXISTS "Allow anon delete curriculums" ON public.curriculums;
DROP POLICY IF EXISTS "Public curriculums viewable by all" ON public.curriculums;
DROP POLICY IF EXISTS "Anyone can view published curriculums" ON public.curriculums;

CREATE POLICY "Anyone can view published curriculums" ON public.curriculums
  FOR SELECT TO public
  USING (is_published = true);

DROP POLICY IF EXISTS "Service role manages curriculums" ON public.curriculums;
CREATE POLICY "Service role manages curriculums" ON public.curriculums
  FOR ALL TO service_role
  USING (true)
  WITH CHECK (true);

-- B. SYLLABUS MODULES
DROP POLICY IF EXISTS "Allow all on syllabus_modules" ON public.syllabus_modules;
DROP POLICY IF EXISTS "Allow anon delete syllabus_modules" ON public.syllabus_modules;
DROP POLICY IF EXISTS "Public modules viewable by all" ON public.syllabus_modules;
DROP POLICY IF EXISTS "Anyone can view modules of published curriculums" ON public.syllabus_modules;

CREATE POLICY "Anyone can view modules of published curriculums" ON public.syllabus_modules
  FOR SELECT TO public
  USING (true);

DROP POLICY IF EXISTS "Service role manages syllabus modules" ON public.syllabus_modules;
CREATE POLICY "Service role manages syllabus modules" ON public.syllabus_modules
  FOR ALL TO service_role
  USING (true)
  WITH CHECK (true);

-- C. ENROLLMENTS
DROP POLICY IF EXISTS "Allow all on enrollments" ON public.enrollments;
DROP POLICY IF EXISTS "Allow anon delete enrollments" ON public.enrollments;
DROP POLICY IF EXISTS "Users can view their own enrollments" ON public.enrollments;
DROP POLICY IF EXISTS "Users can insert their own enrollments" ON public.enrollments;

CREATE POLICY "Users can view their own enrollments" ON public.enrollments
  FOR SELECT TO public
  USING ((SELECT auth.uid()) = user_id OR auth.role() = 'anon');

CREATE POLICY "Users can insert their own enrollments" ON public.enrollments
  FOR INSERT TO public
  WITH CHECK ((SELECT auth.uid()) = user_id OR auth.role() = 'anon');

CREATE POLICY "Users can update their own enrollments" ON public.enrollments
  FOR UPDATE TO public
  USING ((SELECT auth.uid()) = user_id OR auth.role() = 'anon');

CREATE POLICY "Users can delete their own enrollments" ON public.enrollments
  FOR DELETE TO public
  USING ((SELECT auth.uid()) = user_id OR auth.role() = 'anon');

-- D. USER PROGRESS
DROP POLICY IF EXISTS "Allow all on user_progress" ON public.user_progress;
DROP POLICY IF EXISTS "Users can view their own progress" ON public.user_progress;
DROP POLICY IF EXISTS "Users can manage their own progress" ON public.user_progress;

CREATE POLICY "Users can view their own progress" ON public.user_progress
  FOR SELECT TO public
  USING ((SELECT auth.uid()) = user_id OR auth.role() = 'anon');

CREATE POLICY "Users can insert their own progress" ON public.user_progress
  FOR INSERT TO public
  WITH CHECK ((SELECT auth.uid()) = user_id OR auth.role() = 'anon');

CREATE POLICY "Users can update their own progress" ON public.user_progress
  FOR UPDATE TO public
  USING ((SELECT auth.uid()) = user_id OR auth.role() = 'anon');

CREATE POLICY "Users can delete their own progress" ON public.user_progress
  FOR DELETE TO public
  USING ((SELECT auth.uid()) = user_id OR auth.role() = 'anon');

-- E. PROFILES
DROP POLICY IF EXISTS "Allow anon update profiles" ON public.profiles;
DROP POLICY IF EXISTS "Allow delete profiles" ON public.profiles;
DROP POLICY IF EXISTS "Allow view profiles" ON public.profiles;
DROP POLICY IF EXISTS "Users can view their own profile." ON public.profiles;
DROP POLICY IF EXISTS "Users can update their own profile." ON public.profiles;
DROP POLICY IF EXISTS "Users can insert their own profile." ON public.profiles;

CREATE POLICY "Users can view their own profile." ON public.profiles
  FOR SELECT TO public
  USING ((SELECT auth.uid()) = id OR auth.role() = 'anon');

CREATE POLICY "Users can insert their own profile." ON public.profiles
  FOR INSERT TO authenticated
  WITH CHECK ((SELECT auth.uid()) = id);

CREATE POLICY "Users can update their own profile." ON public.profiles
  FOR UPDATE TO public
  USING ((SELECT auth.uid()) = id OR auth.role() = 'anon');

-- F. AI USER MEMORIES
DROP POLICY IF EXISTS "Users can view their own memories" ON public.ai_user_memories;
DROP POLICY IF EXISTS "Users can manage their own memories" ON public.ai_user_memories;

CREATE POLICY "Users can manage their own memories" ON public.ai_user_memories
  FOR ALL TO public
  USING ((SELECT auth.uid()) = user_id OR auth.role() = 'anon')
  WITH CHECK ((SELECT auth.uid()) = user_id OR auth.role() = 'anon');

-- G. STUDENT STUDY PLANS & SESSION LOGS
DROP POLICY IF EXISTS "Users can view own study plans" ON public.student_study_plans;
DROP POLICY IF EXISTS "Users can create own study plans" ON public.student_study_plans;
DROP POLICY IF EXISTS "Users can update own study plans" ON public.student_study_plans;
DROP POLICY IF EXISTS "Users can delete own study plans" ON public.student_study_plans;

CREATE POLICY "Users can view own study plans" ON public.student_study_plans
  FOR SELECT TO public USING ((SELECT auth.uid()) = user_id);

CREATE POLICY "Users can create own study plans" ON public.student_study_plans
  FOR INSERT TO public WITH CHECK ((SELECT auth.uid()) = user_id);

CREATE POLICY "Users can update own study plans" ON public.student_study_plans
  FOR UPDATE TO public USING ((SELECT auth.uid()) = user_id);

CREATE POLICY "Users can delete own study plans" ON public.student_study_plans
  FOR DELETE TO public USING ((SELECT auth.uid()) = user_id);

DROP POLICY IF EXISTS "Users can view own study session logs" ON public.study_session_logs;
DROP POLICY IF EXISTS "Users can create own study session logs" ON public.study_session_logs;
DROP POLICY IF EXISTS "Users can update own study session logs" ON public.study_session_logs;
DROP POLICY IF EXISTS "Users can delete own study session logs" ON public.study_session_logs;

CREATE POLICY "Users can view own study session logs" ON public.study_session_logs
  FOR SELECT TO public USING ((SELECT auth.uid()) = user_id);

CREATE POLICY "Users can create own study session logs" ON public.study_session_logs
  FOR INSERT TO public WITH CHECK ((SELECT auth.uid()) = user_id);

CREATE POLICY "Users can update own study session logs" ON public.study_session_logs
  FOR UPDATE TO public USING ((SELECT auth.uid()) = user_id);

CREATE POLICY "Users can delete own study session logs" ON public.study_session_logs
  FOR DELETE TO public USING ((SELECT auth.uid()) = user_id);

-- ==============================================================================
-- 4. FUNCTION SECURITY DEFINER SEARCH PATH FIX
-- ==============================================================================
ALTER FUNCTION public.handle_new_user() SET search_path = public, auth;

-- ==============================================================================
-- Production Security Hardening & Row Level Security Remediation
-- Migration: 20261114000000_fix_security_and_rls_policies.sql
-- ==============================================================================

-- 1. PROFILES RLS: Remove anonymous vulnerability, restrict strictly to authenticated owner
DROP POLICY IF EXISTS "Users can view their own profile." ON public.profiles;
DROP POLICY IF EXISTS "Users can update their own profile." ON public.profiles;
DROP POLICY IF EXISTS "Users can insert their own profile." ON public.profiles;
DROP POLICY IF EXISTS "Allow anon update profiles" ON public.profiles;
DROP POLICY IF EXISTS "Allow delete profiles" ON public.profiles;
DROP POLICY IF EXISTS "Allow view profiles" ON public.profiles;

CREATE POLICY "Users can view their own profile." ON public.profiles
  FOR SELECT TO authenticated
  USING ((SELECT auth.uid()) = id);

CREATE POLICY "Users can insert their own profile." ON public.profiles
  FOR INSERT TO authenticated
  WITH CHECK ((SELECT auth.uid()) = id);

CREATE POLICY "Users can update their own profile." ON public.profiles
  FOR UPDATE TO authenticated
  USING ((SELECT auth.uid()) = id)
  WITH CHECK ((SELECT auth.uid()) = id);

-- 2. USER PROGRESS RLS: Remove anonymous access, restrict to authenticated owner
DROP POLICY IF EXISTS "Users can view their own progress" ON public.user_progress;
DROP POLICY IF EXISTS "Users can insert their own progress" ON public.user_progress;
DROP POLICY IF EXISTS "Users can update their own progress" ON public.user_progress;
DROP POLICY IF EXISTS "Users can delete their own progress" ON public.user_progress;

CREATE POLICY "Users can view their own progress" ON public.user_progress
  FOR SELECT TO authenticated
  USING ((SELECT auth.uid()) = user_id);

CREATE POLICY "Users can insert their own progress" ON public.user_progress
  FOR INSERT TO authenticated
  WITH CHECK ((SELECT auth.uid()) = user_id);

CREATE POLICY "Users can update their own progress" ON public.user_progress
  FOR UPDATE TO authenticated
  USING ((SELECT auth.uid()) = user_id)
  WITH CHECK ((SELECT auth.uid()) = user_id);

CREATE POLICY "Users can delete their own progress" ON public.user_progress
  FOR DELETE TO authenticated
  USING ((SELECT auth.uid()) = user_id);

-- 3. AI USER MEMORIES RLS: Remove anonymous access
DROP POLICY IF EXISTS "Users can view their own memories" ON public.ai_user_memories;
DROP POLICY IF EXISTS "Users can manage their own memories" ON public.ai_user_memories;

CREATE POLICY "Users can view their own memories" ON public.ai_user_memories
  FOR SELECT TO authenticated
  USING ((SELECT auth.uid()) = user_id);

CREATE POLICY "Users can manage their own memories" ON public.ai_user_memories
  FOR ALL TO authenticated
  USING ((SELECT auth.uid()) = user_id)
  WITH CHECK ((SELECT auth.uid()) = user_id);

-- 4. RPC SECURITY DEFINER HARDENING: Revoke PUBLIC access to subscription and admin RPCs
DO $$
BEGIN
  -- Revoke set_user_subscription from PUBLIC
  IF EXISTS (SELECT 1 FROM pg_proc WHERE proname = 'set_user_subscription') THEN
    REVOKE EXECUTE ON FUNCTION public.set_user_subscription FROM PUBLIC;
    GRANT EXECUTE ON FUNCTION public.set_user_subscription TO service_role;
  END IF;

  -- Revoke admin_get_students from PUBLIC
  IF EXISTS (SELECT 1 FROM pg_proc WHERE proname = 'admin_get_students') THEN
    REVOKE EXECUTE ON FUNCTION public.admin_get_students FROM PUBLIC;
    GRANT EXECUTE ON FUNCTION public.admin_get_students TO service_role;
  END IF;

  -- Revoke admin_update_student_quota from PUBLIC
  IF EXISTS (SELECT 1 FROM pg_proc WHERE proname = 'admin_update_student_quota') THEN
    REVOKE EXECUTE ON FUNCTION public.admin_update_student_quota FROM PUBLIC;
    GRANT EXECUTE ON FUNCTION public.admin_update_student_quota TO service_role;
  END IF;
END $$;

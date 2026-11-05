-- Migration: 20261105000000_phase6_student_subscriptions_and_entitlements.sql
-- Description: Phase 6 Enterprise Subscription Architecture & Entitlements Engine.
-- Provides canonical public.subscriptions and public.payment_orders tables,
-- automated profile sync triggers, and atomic tier management procedures.

-- ==============================================================================
-- 1. SUBSCRIPTIONS TABLE
-- ==============================================================================
CREATE TABLE IF NOT EXISTS public.subscriptions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  plan_tier text NOT NULL DEFAULT 'free' CHECK (plan_tier IN ('free', 'scholar', 'topper', 'mastery')),
  billing_cycle text NOT NULL DEFAULT 'monthly' CHECK (billing_cycle IN ('monthly', 'annual')),
  status text NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'trialing', 'past_due', 'canceled', 'expired')),
  current_period_start timestamptz NOT NULL DEFAULT now(),
  current_period_end timestamptz NOT NULL DEFAULT (now() + interval '30 days'),
  cancel_at_period_end boolean NOT NULL DEFAULT false,
  
  -- Entitlements & Quotas
  monthly_classes_limit integer NOT NULL DEFAULT 3,
  monthly_classes_used integer NOT NULL DEFAULT 0,
  total_term_classes_limit integer NOT NULL DEFAULT 30,
  total_term_classes_used integer NOT NULL DEFAULT 0,
  is_avatar_enabled boolean NOT NULL DEFAULT false,
  allowed_boards text[] NOT NULL DEFAULT ARRAY['CBSE']::text[],
  pyq_access_level text NOT NULL DEFAULT 'preview' CHECK (pyq_access_level IN ('preview', 'chapter_30', '10_year', 'predicted')),
  has_mock_exam_access boolean NOT NULL DEFAULT false,
  has_camera_scratchpad boolean NOT NULL DEFAULT false,
  has_parent_whatsapp_reports boolean NOT NULL DEFAULT false,
  has_unwatermarked_notes boolean NOT NULL DEFAULT false,
  has_morning_blitz boolean NOT NULL DEFAULT false,

  -- Payment & Gateway References
  razorpay_customer_id text,
  razorpay_subscription_id text,
  razorpay_payment_id text,
  razorpay_order_id text,

  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT subscriptions_user_id_key UNIQUE (user_id)
);

-- ==============================================================================
-- 2. PAYMENT ORDERS AUDIT TABLE
-- ==============================================================================
CREATE TABLE IF NOT EXISTS public.payment_orders (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  order_id text NOT NULL UNIQUE,
  payment_id text,
  plan_tier text NOT NULL CHECK (plan_tier IN ('free', 'scholar', 'topper', 'mastery')),
  billing_cycle text NOT NULL CHECK (billing_cycle IN ('monthly', 'annual')),
  amount integer NOT NULL, -- in INR paise
  currency text NOT NULL DEFAULT 'INR',
  status text NOT NULL DEFAULT 'created' CHECK (status IN ('created', 'attempted', 'paid', 'failed', 'refunded')),
  receipt text,
  metadata jsonb DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

-- ==============================================================================
-- 3. PERFORMANCE INDEXES (agency-database-optimizer)
-- ==============================================================================
CREATE UNIQUE INDEX IF NOT EXISTS idx_subscriptions_user_id ON public.subscriptions (user_id);
CREATE INDEX IF NOT EXISTS idx_subscriptions_plan_status ON public.subscriptions (plan_tier, status);
CREATE INDEX IF NOT EXISTS idx_payment_orders_user_id ON public.payment_orders (user_id);
CREATE INDEX IF NOT EXISTS idx_payment_orders_status ON public.payment_orders (status);

-- ==============================================================================
-- 4. ROW LEVEL SECURITY (RLS)
-- ==============================================================================
ALTER TABLE public.subscriptions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.payment_orders ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can view own subscription" ON public.subscriptions;
CREATE POLICY "Users can view own subscription" ON public.subscriptions
  FOR SELECT TO public
  USING ((SELECT auth.uid()) = user_id);

DROP POLICY IF EXISTS "Service role manages subscriptions" ON public.subscriptions;
CREATE POLICY "Service role manages subscriptions" ON public.subscriptions
  FOR ALL TO service_role
  USING (true)
  WITH CHECK (true);

DROP POLICY IF EXISTS "Users can view own payment orders" ON public.payment_orders;
CREATE POLICY "Users can view own payment orders" ON public.payment_orders
  FOR SELECT TO public
  USING ((SELECT auth.uid()) = user_id);

DROP POLICY IF EXISTS "Service role manages payment orders" ON public.payment_orders;
CREATE POLICY "Service role manages payment orders" ON public.payment_orders
  FOR ALL TO service_role
  USING (true)
  WITH CHECK (true);

-- ==============================================================================
-- 5. ENTITLEMENT CALCULATION HELPER
-- ==============================================================================
CREATE OR REPLACE FUNCTION public.apply_subscription_tier_entitlements(
  p_plan_tier text,
  p_target_board text DEFAULT 'CBSE'
)
RETURNS TABLE (
  monthly_classes_limit integer,
  total_term_classes_limit integer,
  is_avatar_enabled boolean,
  allowed_boards text[],
  pyq_access_level text,
  has_mock_exam_access boolean,
  has_camera_scratchpad boolean,
  has_parent_whatsapp_reports boolean,
  has_unwatermarked_notes boolean,
  has_morning_blitz boolean
) LANGUAGE plpgsql AS $$
BEGIN
  IF p_plan_tier = 'scholar' THEN
    RETURN QUERY SELECT
      8,
      80,
      false,
      ARRAY[COALESCE(p_target_board, 'CBSE')]::text[],
      'chapter_30'::text,
      false,
      false,
      false,
      true,
      false;
  ELSIF p_plan_tier = 'topper' THEN
    RETURN QUERY SELECT
      15,
      150,
      true,
      ARRAY[COALESCE(p_target_board, 'CBSE')]::text[],
      '10_year'::text,
      false,
      false,
      false,
      true,
      true;
  ELSIF p_plan_tier = 'mastery' THEN
    RETURN QUERY SELECT
      24,
      240,
      true,
      ARRAY['CBSE', 'ICSE', 'IB']::text[],
      'predicted'::text,
      true,
      true,
      true,
      true,
      true;
  ELSE -- 'free'
    RETURN QUERY SELECT
      3,
      30,
      false,
      ARRAY[COALESCE(p_target_board, 'CBSE')]::text[],
      'preview'::text,
      false,
      false,
      false,
      false,
      false;
  END IF;
END;
$$;

-- ==============================================================================
-- 6. BI-DIRECTIONAL PROFILE SYNC TRIGGER
-- ==============================================================================
CREATE OR REPLACE FUNCTION public.handle_subscription_updated()
RETURNS TRIGGER LANGUAGE plpgsql SECURITY DEFINER AS $$
BEGIN
  UPDATE public.profiles
  SET
    subscription_tier = NEW.plan_tier,
    is_avatar_enabled = NEW.is_avatar_enabled,
    monthly_avatar_capsules_limit = CASE WHEN NEW.is_avatar_enabled THEN NEW.monthly_classes_limit ELSE 0 END,
    updated_at = now()
  WHERE id = NEW.user_id;

  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS tr_subscriptions_sync_profiles ON public.subscriptions;
CREATE TRIGGER tr_subscriptions_sync_profiles
  AFTER INSERT OR UPDATE OF plan_tier, is_avatar_enabled, monthly_classes_limit
  ON public.subscriptions
  FOR EACH ROW
  EXECUTE FUNCTION public.handle_subscription_updated();

-- ==============================================================================
-- 7. ATOMIC USER SUBSCRIPTION SETTER PROCEDURE
-- ==============================================================================
CREATE OR REPLACE FUNCTION public.set_user_subscription(
  p_user_id uuid,
  p_plan_tier text,
  p_billing_cycle text DEFAULT 'monthly',
  p_razorpay_payment_id text DEFAULT NULL,
  p_razorpay_order_id text DEFAULT NULL,
  p_razorpay_subscription_id text DEFAULT NULL
)
RETURNS public.subscriptions LANGUAGE plpgsql SECURITY DEFINER AS $$
DECLARE
  v_target_board text := 'CBSE';
  v_sub public.subscriptions;
  v_interval interval;
  v_ent RECORD;
BEGIN
  -- Validate inputs
  IF p_plan_tier NOT IN ('free', 'scholar', 'topper', 'mastery') THEN
    RAISE EXCEPTION 'Invalid plan tier: %', p_plan_tier;
  END IF;

  IF p_billing_cycle NOT IN ('monthly', 'annual') THEN
    RAISE EXCEPTION 'Invalid billing cycle: %', p_billing_cycle;
  END IF;

  -- Get student target_board from profiles
  SELECT COALESCE(target_board, 'CBSE') INTO v_target_board
  FROM public.profiles
  WHERE id = p_user_id;

  -- Determine cycle duration
  IF p_billing_cycle = 'annual' THEN
    v_interval := interval '365 days';
  ELSE
    v_interval := interval '30 days';
  END IF;

  -- Calculate entitlements
  SELECT * INTO v_ent FROM public.apply_subscription_tier_entitlements(p_plan_tier, v_target_board);

  -- Upsert subscription
  INSERT INTO public.subscriptions (
    user_id,
    plan_tier,
    billing_cycle,
    status,
    current_period_start,
    current_period_end,
    cancel_at_period_end,
    monthly_classes_limit,
    monthly_classes_used,
    total_term_classes_limit,
    is_avatar_enabled,
    allowed_boards,
    pyq_access_level,
    has_mock_exam_access,
    has_camera_scratchpad,
    has_parent_whatsapp_reports,
    has_unwatermarked_notes,
    has_morning_blitz,
    razorpay_payment_id,
    razorpay_order_id,
    razorpay_subscription_id,
    updated_at
  ) VALUES (
    p_user_id,
    p_plan_tier,
    p_billing_cycle,
    'active',
    now(),
    now() + v_interval,
    false,
    v_ent.monthly_classes_limit,
    0,
    v_ent.total_term_classes_limit,
    v_ent.is_avatar_enabled,
    v_ent.allowed_boards,
    v_ent.pyq_access_level,
    v_ent.has_mock_exam_access,
    v_ent.has_camera_scratchpad,
    v_ent.has_parent_whatsapp_reports,
    v_ent.has_unwatermarked_notes,
    v_ent.has_morning_blitz,
    p_razorpay_payment_id,
    p_razorpay_order_id,
    p_razorpay_subscription_id,
    now()
  )
  ON CONFLICT (user_id) DO UPDATE SET
    plan_tier = EXCLUDED.plan_tier,
    billing_cycle = EXCLUDED.billing_cycle,
    status = 'active',
    current_period_start = now(),
    current_period_end = now() + v_interval,
    cancel_at_period_end = false,
    monthly_classes_limit = EXCLUDED.monthly_classes_limit,
    total_term_classes_limit = EXCLUDED.total_term_classes_limit,
    is_avatar_enabled = EXCLUDED.is_avatar_enabled,
    allowed_boards = EXCLUDED.allowed_boards,
    pyq_access_level = EXCLUDED.pyq_access_level,
    has_mock_exam_access = EXCLUDED.has_mock_exam_access,
    has_camera_scratchpad = EXCLUDED.has_camera_scratchpad,
    has_parent_whatsapp_reports = EXCLUDED.has_parent_whatsapp_reports,
    has_unwatermarked_notes = EXCLUDED.has_unwatermarked_notes,
    has_morning_blitz = EXCLUDED.has_morning_blitz,
    razorpay_payment_id = COALESCE(EXCLUDED.razorpay_payment_id, public.subscriptions.razorpay_payment_id),
    razorpay_order_id = COALESCE(EXCLUDED.razorpay_order_id, public.subscriptions.razorpay_order_id),
    razorpay_subscription_id = COALESCE(EXCLUDED.razorpay_subscription_id, public.subscriptions.razorpay_subscription_id),
    updated_at = now()
  RETURNING * INTO v_sub;

  RETURN v_sub;
END;
$$;

-- ==============================================================================
-- 8. BACKFILL EXISTING PROFILES
-- ==============================================================================
INSERT INTO public.subscriptions (
  user_id,
  plan_tier,
  billing_cycle,
  status,
  monthly_classes_limit,
  total_term_classes_limit,
  is_avatar_enabled,
  allowed_boards,
  pyq_access_level
)
SELECT
  p.id,
  COALESCE(p.subscription_tier, 'free'),
  'monthly',
  'active',
  CASE
    WHEN p.subscription_tier = 'mastery' THEN 24
    WHEN p.subscription_tier = 'topper' THEN 15
    WHEN p.subscription_tier = 'scholar' THEN 8
    ELSE 3
  END,
  CASE
    WHEN p.subscription_tier = 'mastery' THEN 240
    WHEN p.subscription_tier = 'topper' THEN 150
    WHEN p.subscription_tier = 'scholar' THEN 80
    ELSE 30
  END,
  CASE
    WHEN p.subscription_tier IN ('topper', 'mastery') THEN true
    ELSE false
  END,
  CASE
    WHEN p.subscription_tier = 'mastery' THEN ARRAY['CBSE', 'ICSE', 'IB']::text[]
    ELSE ARRAY[COALESCE(p.target_board, 'CBSE')]::text[]
  END,
  CASE
    WHEN p.subscription_tier = 'mastery' THEN 'predicted'
    WHEN p.subscription_tier = 'topper' THEN '10_year'
    WHEN p.subscription_tier = 'scholar' THEN 'chapter_30'
    ELSE 'preview'
  END
FROM public.profiles p
ON CONFLICT (user_id) DO NOTHING;

/**
 * Anaxly Enterprise Subscription & Entitlements Type System
 * Phase 6 Canonical Schema Definitions
 */

export type SubscriptionTier = 'free' | 'scholar' | 'topper' | 'mastery'
export type BillingCycle = 'monthly' | 'annual'
export type SubscriptionStatus = 'active' | 'trialing' | 'past_due' | 'canceled' | 'expired'
export type PyqAccessLevel = 'preview' | 'chapter_30' | '10_year' | 'predicted'

export interface Subscription {
  id: string
  user_id: string
  plan_tier: SubscriptionTier
  billing_cycle: BillingCycle
  status: SubscriptionStatus
  current_period_start: string
  current_period_end: string
  cancel_at_period_end: boolean

  // Entitlements & Live Class Quotas
  monthly_classes_limit: number
  monthly_classes_used: number
  total_term_classes_limit: number
  total_term_classes_used: number
  is_avatar_enabled: boolean
  allowed_boards: string[]
  pyq_access_level: PyqAccessLevel
  has_mock_exam_access: boolean
  has_camera_scratchpad: boolean
  has_parent_whatsapp_reports: boolean
  has_unwatermarked_notes: boolean
  has_morning_blitz: boolean

  // Gateway IDs
  razorpay_customer_id?: string | null
  razorpay_subscription_id?: string | null
  razorpay_payment_id?: string | null
  razorpay_order_id?: string | null

  created_at: string
  updated_at: string
}

export interface PaymentOrder {
  id: string
  user_id: string
  order_id: string
  payment_id?: string | null
  plan_tier: SubscriptionTier
  billing_cycle: BillingCycle
  amount: number // in paise
  currency: string
  status: 'created' | 'attempted' | 'paid' | 'failed' | 'refunded'
  receipt?: string | null
  metadata?: Record<string, any>
  created_at: string
  updated_at: string
}

export interface PlanConfig {
  id: SubscriptionTier
  name: string
  badge?: string
  monthlyPrice: number
  annualPrice: number // per month billed annually
  monthlyClassesLimit: number
  totalTermClassesLimit: number
  isAvatarEnabled: boolean
  avatarType: 'none' | '100%_face_to_face'
  boards: 'single_board' | 'all_boards'
  pyqLevel: PyqAccessLevel
  features: string[]
}

export const SUBSCRIPTION_PLANS: Record<SubscriptionTier, PlanConfig> = {
  free: {
    id: 'free',
    name: 'Chalkboard Free',
    monthlyPrice: 0,
    annualPrice: 0,
    monthlyClassesLimit: 3,
    totalTermClassesLimit: 30,
    isAvatarEnabled: false,
    avatarType: 'none',
    boards: 'single_board',
    pyqLevel: 'preview',
    features: [
      'Interactive Digital Chalkboard & Derivations (100% Free)',
      'Dynamic Science Diagrams & Math Graphs (100% Free)',
      '3 Live Socratic Classes / month (~1 hour total)',
      '3 Quick Last-Minute Summaries / month',
      'CBSE, ICSE & IB Core Curriculum standards',
    ],
  },
  scholar: {
    id: 'scholar',
    name: 'Scholar',
    badge: 'Syllabus Completion',
    monthlyPrice: 499,
    annualPrice: 399,
    monthlyClassesLimit: 8,
    totalTermClassesLimit: 80,
    isAvatarEnabled: false,
    avatarType: 'none',
    boards: 'single_board',
    pyqLevel: 'chapter_30',
    features: [
      'Interactive Chalkboard & Math Graphs (100% Free)',
      '8 Live Socratic Classes / month (80 classes over term)',
      'Guaranteed School Syllabus Coverage (Maths & Science)',
      'Unlimited Quick Last-Minute Summaries & Flashcards',
      'Downloadable Unwatermarked Clean PDF Master Notes',
    ],
  },
  topper: {
    id: 'topper',
    name: 'Topper Pro',
    badge: 'Most Popular',
    monthlyPrice: 1099,
    annualPrice: 899,
    monthlyClassesLimit: 15,
    totalTermClassesLimit: 150,
    isAvatarEnabled: true,
    avatarType: '100%_face_to_face',
    boards: 'single_board',
    pyqLevel: '10_year',
    features: [
      'Real-Time Face-to-Face AI Video Teacher (100% of All Classes)',
      '15 Live Socratic Classes / month (150 classes over term)',
      '10-Year Authentic Board Exam Question Bank with Marking',
      '10-Minute Morning Exam Blitz Sprint Mode',
      'Guaranteed School Syllabus Completion',
    ],
  },
  mastery: {
    id: 'mastery',
    name: 'Mastery Infinity',
    badge: 'Comprehensive Multi-Board',
    monthlyPrice: 1799,
    annualPrice: 1499,
    monthlyClassesLimit: 24,
    totalTermClassesLimit: 240,
    isAvatarEnabled: true,
    avatarType: '100%_face_to_face',
    boards: 'all_boards',
    pyqLevel: 'predicted',
    features: [
      'Real-Time Face-to-Face AI Video Teacher (100% of All Classes)',
      '24 Live Socratic Classes / month (240 classes over term)',
      'Multi-Board Access (CBSE NCERT, ICSE Selina & IB DP/MYP)',
      'Timed Full Board Mock Exams with Handwriting & Rubric Grading',
      'Parent WhatsApp Weekly Academic Progress Card',
    ],
  },
}

/**
 * Calculates remaining monthly classes for a student
 */
export function getClassesRemaining(sub: Subscription | null | undefined): number {
  if (!sub) return 0
  return Math.max(0, sub.monthly_classes_limit - sub.monthly_classes_used)
}

/**
 * Validates whether the student has quota to launch a live Socratic session
 */
export function canStartLiveClass(sub: Subscription | null | undefined): boolean {
  if (!sub) return false
  return sub.status === 'active' && sub.monthly_classes_used < sub.monthly_classes_limit
}

/**
 * Validates whether the student's active plan includes the Real-Time AI Video Avatar
 */
export function isAvatarSupported(sub: Subscription | null | undefined): boolean {
  if (!sub) return false
  return Boolean(sub.is_avatar_enabled)
}

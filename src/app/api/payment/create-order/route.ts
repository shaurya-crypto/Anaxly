import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@/utils/supabase/server'
import { createSubscriptionRazorpayOrder } from '@/lib/subscription/subscriptionService'
import { SubscriptionTier, BillingCycle } from '@/lib/types/subscription'

export async function POST(req: NextRequest) {
  try {
    const supabase = await createClient()
    const {
      data: { user },
      error: authError,
    } = await supabase.auth.getUser()

    if (authError || !user) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 })
    }

    const body = await req.json()
    const { planTier, billingCycle } = body as {
      planTier: SubscriptionTier
      billingCycle: BillingCycle
    }

    if (!planTier || !['scholar', 'topper', 'mastery'].includes(planTier)) {
      return NextResponse.json({ error: 'Invalid paid plan tier' }, { status: 400 })
    }

    const cycle: BillingCycle = billingCycle === 'annual' ? 'annual' : 'monthly'

    const order = await createSubscriptionRazorpayOrder(user.id, planTier, cycle)

    return NextResponse.json(order)
  } catch (err: any) {
    console.error('Error creating Razorpay order:', err)
    return NextResponse.json(
      { error: err.message || 'Failed to create payment order' },
      { status: 500 }
    )
  }
}

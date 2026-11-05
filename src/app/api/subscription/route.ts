import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@/utils/supabase/server'
import { getStudentSubscription, updateSubscriptionPlan } from '@/lib/subscription/subscriptionService'
import { SubscriptionTier } from '@/lib/types/subscription'

export async function GET() {
  try {
    const supabase = await createClient()
    const {
      data: { user },
      error: authError,
    } = await supabase.auth.getUser()

    if (authError || !user) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 })
    }

    const sub = await getStudentSubscription(user.id)
    return NextResponse.json({ subscription: sub })
  } catch (err: any) {
    return NextResponse.json({ error: err.message }, { status: 500 })
  }
}

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
    const { planTier } = body as { planTier: SubscriptionTier }

    if (planTier === 'free') {
      const updatedSub = await updateSubscriptionPlan(user.id, 'free', 'monthly')
      return NextResponse.json({ success: true, subscription: updatedSub })
    }

    return NextResponse.json(
      { error: 'Paid plans must be activated via payment verification' },
      { status: 400 }
    )
  } catch (err: any) {
    return NextResponse.json({ error: err.message }, { status: 500 })
  }
}

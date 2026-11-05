import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@/utils/supabase/server'
import { verifyAndActivateRazorpayPayment } from '@/lib/subscription/subscriptionService'

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
    const { razorpay_order_id, razorpay_payment_id, razorpay_signature } = body

    if (!razorpay_order_id || !razorpay_payment_id || !razorpay_signature) {
      return NextResponse.json(
        { error: 'Missing required Razorpay payment verification fields' },
        { status: 400 }
      )
    }

    const result = await verifyAndActivateRazorpayPayment(
      user.id,
      razorpay_order_id,
      razorpay_payment_id,
      razorpay_signature
    )

    if (!result.success) {
      return NextResponse.json({ error: result.error || 'Payment verification failed' }, { status: 400 })
    }

    return NextResponse.json({
      success: true,
      subscription: result.subscription,
    })
  } catch (err: any) {
    console.error('Error verifying Razorpay payment:', err)
    return NextResponse.json(
      { error: err.message || 'Server error verifying payment' },
      { status: 500 }
    )
  }
}

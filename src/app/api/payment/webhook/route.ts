import { NextRequest, NextResponse } from 'next/server'
import crypto from 'crypto'
import { createClient } from '@/utils/supabase/server'
import { updateSubscriptionPlan } from '@/lib/subscription/subscriptionService'
import { SubscriptionTier, BillingCycle } from '@/lib/types/subscription'

/**
 * Razorpay Webhook Handler
 * Production-grade asynchronous event processor.
 * Listens for 'payment.captured' and 'order.paid' to guarantee subscription activation.
 */
export async function POST(req: NextRequest) {
  try {
    const rawBody = await req.text()
    const signature = req.headers.get('x-razorpay-signature')

    const webhookSecret = process.env.RAZORPAY_WEBHOOK_SECRET || process.env.RAZORPAY_KEY_SECRET

    if (!webhookSecret) {
      console.error('[Razorpay Webhook] Missing RAZORPAY_WEBHOOK_SECRET or RAZORPAY_KEY_SECRET')
      return NextResponse.json({ error: 'Server configuration error' }, { status: 500 })
    }

    if (!signature) {
      console.warn('[Razorpay Webhook] Missing x-razorpay-signature header')
      return NextResponse.json({ error: 'Signature missing' }, { status: 400 })
    }

    // Cryptographic validation of webhook payload
    const expectedSignature = crypto
      .createHmac('sha256', webhookSecret)
      .update(rawBody)
      .digest('hex')

    if (expectedSignature !== signature) {
      console.error('[Razorpay Webhook] Invalid webhook signature')
      return NextResponse.json({ error: 'Invalid signature' }, { status: 400 })
    }

    const event = JSON.parse(rawBody)
    console.log(`[Razorpay Webhook] Received verified event: ${event.event}`)

    const supabase = await createClient()

    if (event.event === 'order.paid' || event.event === 'payment.captured') {
      const paymentEntity = event.payload.payment?.entity || {}
      const orderEntity = event.payload.order?.entity || {}

      const orderId = paymentEntity.order_id || orderEntity.id
      const paymentId = paymentEntity.id

      if (!orderId) {
        console.warn('[Razorpay Webhook] Event missing order_id')
        return NextResponse.json({ received: true })
      }

      // 1. Fetch pending order from database
      const { data: orderRecord, error: orderError } = await supabase
        .from('payment_orders')
        .select('*')
        .eq('order_id', orderId)
        .maybeSingle()

      if (orderError || !orderRecord) {
        console.warn(`[Razorpay Webhook] No payment_order found for order_id: ${orderId}`)
        return NextResponse.json({ received: true })
      }

      // 2. Idempotent check: if already paid, skip re-processing
      if (orderRecord.status === 'paid') {
        console.log(`[Razorpay Webhook] Order ${orderId} already processed as paid. Skipping.`)
        return NextResponse.json({ received: true, status: 'already_processed' })
      }

      // 3. Mark payment_order as paid
      await supabase
        .from('payment_orders')
        .update({
          payment_id: paymentId,
          status: 'paid',
          updated_at: new Date().toISOString(),
          metadata: {
            ...(orderRecord.metadata || {}),
            webhookVerifiedAt: new Date().toISOString(),
            webhookEvent: event.event,
          },
        })
        .eq('order_id', orderId)

      // 4. Activate/upgrade user's subscription
      await updateSubscriptionPlan(
        orderRecord.user_id,
        orderRecord.plan_tier as SubscriptionTier,
        orderRecord.billing_cycle as BillingCycle,
        {
          paymentId,
          orderId,
        }
      )

      console.log(`[Razorpay Webhook] Successfully activated ${orderRecord.plan_tier} for user ${orderRecord.user_id}`)
    }

    return NextResponse.json({ received: true })
  } catch (err: any) {
    console.error('[Razorpay Webhook] Processing error:', err)
    return NextResponse.json({ error: err.message || 'Webhook internal error' }, { status: 500 })
  }
}

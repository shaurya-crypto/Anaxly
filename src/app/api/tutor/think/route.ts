import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@/utils/supabase/server'
import { checkRateLimit, getClientIp } from '@/lib/rateLimit'
import { runPedagogicalThinkEngine, TutorThinkInputSchema } from '@/lib/tutor/thinkEngine'

export const dynamic = 'force-dynamic'
export const runtime = 'nodejs'

export async function POST(req: NextRequest) {
  try {
    const ip = getClientIp(req)
    const ipLimit = checkRateLimit({
      key: `tutor_think_ip:${ip}`,
      maxRequests: 60,
      windowMs: 60 * 1000,
    })
    if (!ipLimit.success) {
      return NextResponse.json(
        { error: 'Too many tutor reasoning requests. Please pause briefly.' },
        { status: 429 }
      )
    }

    const supabase = await createClient()
    const {
      data: { user },
      error: authError,
    } = await supabase.auth.getUser()

    if (authError || !user) {
      return NextResponse.json(
        { error: 'Unauthorized: Student session required.' },
        { status: 401 }
      )
    }

    const userLimit = checkRateLimit({
      key: `tutor_think_user:${user.id}`,
      maxRequests: 30,
      windowMs: 60 * 1000,
    })
    if (!userLimit.success) {
      return NextResponse.json(
        { error: 'Tutor think rate limit exceeded. Please wait a moment.' },
        { status: 429 }
      )
    }

    const body = await req.json()
    const parsed = TutorThinkInputSchema.safeParse(body)
    if (!parsed.success) {
      return NextResponse.json(
        { error: 'Invalid think payload', details: parsed.error.flatten() },
        { status: 400 }
      )
    }

    const plan = await runPedagogicalThinkEngine(parsed.data)
    return NextResponse.json({ success: true, ...plan })
  } catch (err: any) {
    console.error('[/api/tutor/think] Error:', err)
    return NextResponse.json(
      { error: err?.message || 'Failed to compute pedagogical teaching move.' },
      { status: 500 }
    )
  }
}

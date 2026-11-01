import { NextResponse } from 'next/server'
import { cookies } from 'next/headers'
import { verifyAdminToken } from '@/lib/adminAuth'
import { createAdminClient } from '@/utils/supabase/admin'

export const dynamic = 'force-dynamic'

// GET /api/admin/users: Fetch all student accounts with usage quotas & avatar settings
export async function GET() {
  try {
    const cookieStore = await cookies()
    const adminSession = cookieStore.get('admin_session')

    if (!adminSession?.value || !verifyAdminToken(adminSession.value)) {
      return NextResponse.json({ error: 'Unauthorized admin session' }, { status: 401 })
    }

    const supabase = createAdminClient()

    let usersList: any[] = []

    // 1. Attempt direct SELECT (succeeds if real SUPABASE_SERVICE_ROLE_KEY is present)
    const { data: users, error } = await supabase
      .from('profiles')
      .select(`
        id,
        email,
        full_name,
        class_level,
        target_board,
        is_avatar_enabled,
        limit_type,
        max_requests,
        used_requests,
        max_modules,
        used_modules,
        total_classes_taken,
        created_at,
        last_active_date
      `)
      .order('created_at', { ascending: false })

    if (!error && Array.isArray(users) && users.length > 0) {
      usersList = users
    } else {
      // 2. Fallback to SECURITY DEFINER RPC (bypasses RLS when service_role key is not configured)
      const adminSecret =
        process.env.ADMIN_SESSION_SECRET ||
        process.env.ADMIN_PORTAL_PASSWORD ||
        'admin_hmac_secret_key_cbse_curriculum_2026'

      const { data: rpcUsers, error: rpcErr } = await supabase.rpc('admin_get_students', {
        p_secret: adminSecret,
      })

      if (rpcErr) {
        console.error('[Admin Users API] RPC error fetching profiles:', rpcErr)
        if (error) {
          return NextResponse.json({ error: error.message || rpcErr.message }, { status: 500 })
        }
      } else if (Array.isArray(rpcUsers)) {
        usersList = rpcUsers
      }
    }

    return NextResponse.json({
      success: true,
      users: usersList,
    })
  } catch (err: any) {
    console.error('[Admin Users API] Unexpected error in GET:', err)
    return NextResponse.json({ error: err?.message || 'Internal server error' }, { status: 500 })
  }
}

// PATCH /api/admin/users: Update quota limits and avatar preferences for a specific student
export async function PATCH(req: Request) {
  try {
    const cookieStore = await cookies()
    const adminSession = cookieStore.get('admin_session')

    if (!adminSession?.value || !verifyAdminToken(adminSession.value)) {
      return NextResponse.json({ error: 'Unauthorized admin session' }, { status: 401 })
    }

    const body = await req.json()
    const {
      userId,
      is_avatar_enabled,
      limit_type,
      max_requests,
      used_requests,
      max_modules,
      used_modules,
    } = body

    if (!userId) {
      return NextResponse.json({ error: 'Missing required field: userId' }, { status: 400 })
    }

    const updates: Record<string, any> = {}

    if (typeof is_avatar_enabled === 'boolean') {
      updates.is_avatar_enabled = is_avatar_enabled
    }

    if (limit_type && ['requests', 'modules', 'unlimited'].includes(limit_type)) {
      updates.limit_type = limit_type
    }

    if (typeof max_requests === 'number' && !isNaN(max_requests)) {
      updates.max_requests = Math.max(1, Math.floor(max_requests))
    }

    if (typeof used_requests === 'number' && !isNaN(used_requests)) {
      updates.used_requests = Math.max(0, Math.floor(used_requests))
    }

    if (typeof max_modules === 'number' && !isNaN(max_modules)) {
      updates.max_modules = Math.max(1, Math.floor(max_modules))
    }

    if (typeof used_modules === 'number' && !isNaN(used_modules)) {
      updates.used_modules = Math.max(0, Math.floor(used_modules))
    }

    const supabase = createAdminClient()
    const adminSecret =
      process.env.ADMIN_SESSION_SECRET ||
      process.env.ADMIN_PORTAL_PASSWORD ||
      'admin_hmac_secret_key_cbse_curriculum_2026'

    let updatedProfile: any = null

    // 1. Attempt direct update if real service role key is configured
    const rawServiceKey = process.env.SUPABASE_SERVICE_ROLE_KEY
    const hasRealServiceKey = Boolean(
      rawServiceKey &&
      rawServiceKey.trim().length > 0 &&
      !rawServiceKey.startsWith('your_') &&
      rawServiceKey !== 'placeholder'
    )

    if (hasRealServiceKey) {
      const { data, error } = await supabase
        .from('profiles')
        .update(updates)
        .eq('id', userId)
        .select(`
          id,
          email,
          full_name,
          class_level,
          target_board,
          is_avatar_enabled,
          limit_type,
          max_requests,
          used_requests,
          max_modules,
          used_modules,
          total_classes_taken,
          created_at,
          last_active_date
        `)
        .single()

      if (!error && data) {
        updatedProfile = data
      }
    }

    // 2. Fallback to SECURITY DEFINER RPC if direct update didn't run or was blocked by RLS
    if (!updatedProfile) {
      const { error: rpcErr } = await supabase.rpc('admin_update_student_quota', {
        target_user_id: userId,
        new_is_avatar_enabled: typeof updates.is_avatar_enabled === 'boolean' ? updates.is_avatar_enabled : null,
        new_limit_type: updates.limit_type ?? null,
        new_max_requests: updates.max_requests ?? null,
        new_used_requests: updates.used_requests ?? null,
        new_max_modules: updates.max_modules ?? null,
        new_used_modules: updates.used_modules ?? null,
        p_secret: adminSecret,
      })

      if (rpcErr) {
        console.error('[Admin Users API] RPC error updating profile:', rpcErr)
        return NextResponse.json({ error: rpcErr.message }, { status: 500 })
      }

      // Fetch the updated profile via RPC
      const { data: refreshedUsers } = await supabase.rpc('admin_get_students', {
        p_secret: adminSecret,
      })
      updatedProfile = (refreshedUsers || []).find((u: any) => u.id === userId)
    }

    return NextResponse.json({
      success: true,
      user: updatedProfile,
    })
  } catch (err: any) {
    console.error('[Admin Users API] Unexpected error in PATCH:', err)
    return NextResponse.json({ error: err?.message || 'Internal server error' }, { status: 500 })
  }
}

import { notFound } from 'next/navigation'
import { StitchDashboardView } from '@/components/dashboard/StitchDashboardView'
import { mockDashboardProps } from '@/dev-preview/mockDashboardData'

// Development-only preview of the dashboard UI with mock data (no Supabase).
// Returns 404 in production or unless ENABLE_DEV_PREVIEW=true is set locally.
export const dynamic = 'force-dynamic'

export default function DashboardDevPreviewPage() {
  if (process.env.NODE_ENV === 'production' || process.env.ENABLE_DEV_PREVIEW !== 'true') {
    notFound()
  }

  return <StitchDashboardView {...mockDashboardProps} />
}

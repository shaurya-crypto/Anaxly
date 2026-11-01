import { notFound } from 'next/navigation'
import { StitchDashboardView } from '@/components/dashboard/StitchDashboardView'
import { mockDashboardProps } from '@/dev-preview/mockDashboardData'

// Development-only preview of the dashboard UI with mock data (no Supabase).
// Returns 404 in production or unless ENABLE_DEV_PREVIEW=true is set locally.
export const dynamic = 'force-dynamic'

const daysAgoIso = (n: number) => new Date(Date.now() - n * 86_400_000).toISOString()

// ?dataset= switches which of the mock progress records are shown, to exercise
// the empty, partial and edge-case states of the Home activity chart.
function progressFor(dataset: string | undefined) {
  const all = mockDashboardProps.progressRecords
  switch (dataset) {
    case 'empty':
      return []
    case 'partial':
      return all.slice(0, 3)
    case 'edge':
      return [
        ...all,
        // Completed outside the 14-day window: must not appear in the chart
        { ...all[0], id: 'edge-old', completed_at: daysAgoIso(20) },
        // Completed but with no timestamp: cannot be placed on a day
        { ...all[0], id: 'edge-undated', status: 'completed' as const, completed_at: null },
      ]
    default:
      return all
  }
}

export default async function DashboardDevPreviewPage({
  searchParams,
}: {
  searchParams: Promise<{ dataset?: string }>
}) {
  if (process.env.NODE_ENV === 'production' || process.env.ENABLE_DEV_PREVIEW !== 'true') {
    notFound()
  }

  const { dataset } = await searchParams

  return <StitchDashboardView {...mockDashboardProps} progressRecords={progressFor(dataset)} />
}

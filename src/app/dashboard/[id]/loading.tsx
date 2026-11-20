// Shown instantly on navigation while the dashboard's server data loads,
// so clicks feel responsive instead of the page appearing frozen.
export default function DashboardLoading() {
  return (
    <div className="min-h-[100dvh] w-full bg-canvas p-6 md:p-10" aria-busy="true" aria-live="polite">
      <span className="sr-only">Loading…</span>
      <div className="mx-auto max-w-6xl animate-pulse space-y-6">
        <div className="h-8 w-48 rounded-lg bg-black/5" />
        <div className="grid grid-cols-1 gap-4 md:grid-cols-3">
          <div className="h-28 rounded-2xl bg-black/5" />
          <div className="h-28 rounded-2xl bg-black/5" />
          <div className="h-28 rounded-2xl bg-black/5" />
        </div>
        <div className="h-64 rounded-2xl bg-black/5" />
        <div className="h-40 rounded-2xl bg-black/5" />
      </div>
    </div>
  )
}

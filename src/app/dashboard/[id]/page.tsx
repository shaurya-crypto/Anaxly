import { DashboardRoute } from "@/components/dashboard/DashboardRoute";

export const dynamic = "force-dynamic";

export default function DashboardPage({ params }: { params: Promise<{ id: string }> }) {
  return <DashboardRoute params={params} view="home" />;
}

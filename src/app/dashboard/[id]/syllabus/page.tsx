import { DashboardRoute } from "@/components/dashboard/DashboardRoute";

export const dynamic = "force-dynamic";

export default function SyllabusPage({ params }: { params: Promise<{ id: string }> }) {
  return <DashboardRoute params={params} view="syllabus" />;
}

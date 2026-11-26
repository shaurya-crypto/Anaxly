import React from "react";
import { createClient } from "@/utils/supabase/server";
import { redirect } from "next/navigation";
import { StitchDashboardView, DashboardViewId } from "@/components/dashboard/StitchDashboardView";
import { getStudentSubscription } from "@/lib/subscription/subscriptionService";
import {
  getCachedCurriculums,
  getCachedCurriculumModules,
  getCachedUserProfile,
  getCachedUserEnrollments,
  getCachedUserProgressList,
  getCachedUserMemories,
  getCachedActiveStudyPlan,
  invalidateUserProfileCache,
  invalidateUserEnrollmentsCache,
} from "@/lib/cache/dataCache";

/** Loads everything the dashboard shell needs and renders the requested view. */
export async function DashboardRoute({
  params,
  view = "home",
}: {
  params: Promise<{ id: string }>;
  view?: DashboardViewId;
}) {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  const resolvedParams = await params;

  if (!user || user.id !== resolvedParams.id) {
    redirect("/login");
  }

  // Subscription lookup is independent of the profile, so start it in parallel.
  const subscriptionPromise = getStudentSubscription(user.id).catch(() => null);

  // 1. Fetch cached user profile
  let profile = await getCachedUserProfile(supabase, user.id);

  if (!profile) {
    // Self-heal: auto-create the missing profile row in public.profiles
    const { data: newProfile } = await supabase
      .from("profiles")
      .upsert({
        id: user.id,
        email: user.email!,
        full_name: (user.user_metadata?.full_name as string) || null,
        class_level: (user.user_metadata?.class_level as string) || null,
        onboarding_completed: false,
      })
      .select("*")
      .single();

    profile = newProfile;
    invalidateUserProfileCache(user.id);
  }

  // Redirect to onboarding if not yet completed
  if (!profile || !profile.onboarding_completed) {
    redirect("/onboarding");
  }

  // 1b. Fetch active subscription & live class entitlements
  const subscription = await subscriptionPromise;

  // 1c. Daily Active Streak Engine: Automatically increments/maintains active streak on web visit
  const todayStr = new Date().toISOString().split("T")[0];
  let currentStreak = profile.current_streak || 0;
  let streakUpdated = false;

  if (!profile.last_active_date) {
    currentStreak = Math.max(1, currentStreak);
    streakUpdated = true;
  } else if (profile.last_active_date !== todayStr) {
    const lastActive = new Date(profile.last_active_date);
    const today = new Date(todayStr);
    const diffDays = Math.round((today.getTime() - lastActive.getTime()) / (1000 * 60 * 60 * 24));

    if (diffDays === 1) {
      // Visited on consecutive day: increment streak!
      currentStreak += 1;
      streakUpdated = true;
    } else if (diffDays > 1) {
      // Streak reset to 1
      currentStreak = 1;
      streakUpdated = true;
    }
  } else if (currentStreak === 0) {
    currentStreak = 1;
    streakUpdated = true;
  }

  // Streak write runs alongside the reads below instead of blocking them.
  let streakWrite: PromiseLike<unknown> = Promise.resolve();
  if (streakUpdated) {
    profile.current_streak = currentStreak;
    profile.last_active_date = todayStr;
    invalidateUserProfileCache(user.id);
    streakWrite = supabase
      .from("profiles")
      .update({
        current_streak: currentStreak,
        last_active_date: todayStr,
        updated_at: new Date().toISOString(),
      })
      .eq("id", user.id);
  }

  // 2-3 + 5. Independent cached reads in parallel
  const [
    enrollmentsData,
    allCurriculums,
    [progressData, memoriesData, studyPlan],
  ] = await Promise.all([
    getCachedUserEnrollments(supabase, user.id),
    getCachedCurriculums(supabase, {
      classLevel: profile?.class_level,
      board: profile?.board,
      isPublished: true,
    }),
    Promise.all([
      getCachedUserProgressList(supabase, user.id),
      getCachedUserMemories(supabase, user.id, 10),
      getCachedActiveStudyPlan(supabase, user.id),
    ]),
    streakWrite,
  ]);

  const enrollments = enrollmentsData || [];

  // Extract enrolled curriculums
  const enrolledCurriculums = enrollments
    .map((e) => (Array.isArray(e.curriculums) ? e.curriculums[0] : e.curriculums))
    .filter(Boolean);

  // 4. Fetch syllabus modules (using high-speed dataCache)
  const enrolledCurriculumIds = enrolledCurriculums.map((c: any) => c.id).filter(Boolean);
  const allCurriculumIds = allCurriculums.map((c: any) => c.id).filter(Boolean);
  const targetCurriculumIds = Array.from(new Set([...enrolledCurriculumIds, ...allCurriculumIds]));

  let allModules: any[] = [];
  if (targetCurriculumIds.length > 0) {
    allModules = await getCachedCurriculumModules(supabase, targetCurriculumIds);
  } else {
    let fallbackModulesQuery = supabase
      .from("syllabus_modules")
      .select("id, curriculum_id, order_index, title, description, estimated_minutes, key_concepts, success_criteria, class_level, board, subtopics, chapter_notes, curriculums(*)")
      .order("order_index", { ascending: true });
    if (profile?.class_level) {
      fallbackModulesQuery = fallbackModulesQuery.or(`class_level.eq.${profile.class_level},class_level.is.null`);
    }
    const { data: modulesData } = await fallbackModulesQuery;
    allModules = modulesData || [];
  }

  const userProgress = progressData || [];
  const userMemories = (memoriesData || []).map((m: any) => ({
    ...m,
    memory_text: m.memory_text || m.content || "",
  }));

  // 7. Dynamic Active Curriculum Resolution:
  const progressMap = new Map<string, any>();
  userProgress.forEach((p: any) => progressMap.set(p.syllabus_module_id, p));

  const isModuleDone = (mId: string) => {
    const p = progressMap.get(mId);
    return p?.status === 'completed' || !!p?.completed_at;
  };
  const isModuleInProgress = (mId: string) => {
    const p = progressMap.get(mId);
    return p?.status === 'in_progress' && !p?.completed_at;
  };

  let primaryCurriculum = null;

  // 1. Check for in-progress module across enrolled curriculums
  for (const curr of enrolledCurriculums) {
    const cMods = allModules.filter((m: any) => m.curriculum_id === curr.id);
    const hasInProgress = cMods.some((m: any) => isModuleInProgress(m.id));
    if (hasInProgress) {
      primaryCurriculum = curr;
      break;
    }
  }

  // 2. Check for curriculum with unfinished modules across enrolled curriculums
  if (!primaryCurriculum) {
    for (const curr of enrolledCurriculums) {
      const cMods = allModules.filter((m: any) => m.curriculum_id === curr.id);
      const isUnfinished = cMods.length > 0 && cMods.some((m: any) => !isModuleDone(m.id));
      if (isUnfinished) {
        primaryCurriculum = curr;
        break;
      }
    }
  }

  // 3. If all enrolled curriculums are 100% completed, pick next syllabus chapter in allCurriculums
  if (!primaryCurriculum) {
    for (const curr of allCurriculums) {
      const cMods = allModules.filter((m: any) => m.curriculum_id === curr.id);
      const isUnfinished = cMods.length > 0 && cMods.some((m: any) => !isModuleDone(m.id));
      if (isUnfinished) {
        primaryCurriculum = curr;
        await supabase
          .from('enrollments')
          .upsert({
            user_id: user.id,
            curriculum_id: curr.id,
            status: 'active',
            enrolled_at: new Date().toISOString()
          }, { onConflict: 'user_id,curriculum_id' });
        invalidateUserEnrollmentsCache(user.id);
        if (!enrolledCurriculums.some((c: any) => c.id === curr.id)) {
          enrolledCurriculums.push(curr);
        }
        break;
      }
    }
  }

  // 4. Fallback to first enrolled or first published curriculum
  if (!primaryCurriculum) {
    primaryCurriculum = enrolledCurriculums[0] || allCurriculums[0] || null;
  }

  return (
    <StitchDashboardView
      user={{ id: user.id, email: user.email }}
      profile={profile}
      subscription={subscription}
      primaryCurriculum={primaryCurriculum}
      enrolledCurriculums={enrolledCurriculums}
      allCurriculums={allCurriculums}
      modules={allModules}
      progressRecords={userProgress}
      memories={userMemories}
      studyPlan={studyPlan}
      view={view}
    />
  );
}

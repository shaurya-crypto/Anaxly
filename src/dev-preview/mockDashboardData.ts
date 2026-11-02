/**
 * Static, fake data for the development-only dashboard preview
 * (/dev-preview/dashboard). Contains no real user data.
 */

const USER_ID = 'preview-user'

const daysAgo = (n: number) => new Date(Date.now() - n * 86_400_000).toISOString()
const daysAhead = (n: number) => new Date(Date.now() + n * 86_400_000).toISOString().split('T')[0]

const curriculums = [
  { id: 'cur-math', title: 'Mathematics: Quadratic Equations', description: 'Roots, discriminant, and word problems.', category: 'Mathematics', difficulty_level: 'intermediate', estimated_duration_minutes: 240, is_published: true, class_level: 'Class 10', board: 'CBSE', order_index: 1 },
  { id: 'cur-sci', title: 'Science: Light, Reflection and Refraction', description: 'Mirrors, lenses, and the laws of refraction.', category: 'Science', difficulty_level: 'intermediate', estimated_duration_minutes: 200, is_published: true, class_level: 'Class 10', board: 'CBSE', order_index: 2 },
  { id: 'cur-phy', title: 'Physics: Electricity', description: 'Current, resistance, and Ohm\'s law.', category: 'Science', difficulty_level: 'advanced', estimated_duration_minutes: 220, is_published: true, class_level: 'Class 10', board: 'CBSE', order_index: 3 },
  { id: 'cur-eng', title: 'English: Letter and Essay Writing', description: 'Formal letters, essays, and reports.', category: 'English', difficulty_level: 'beginner', estimated_duration_minutes: 150, is_published: true, class_level: 'Class 10', board: 'CBSE', order_index: 4 },
]

const moduleTitles: Record<string, string[]> = {
  'cur-math': ['Standard form of a quadratic', 'Factorisation method', 'Completing the square', 'Quadratic formula', 'Nature of roots', 'Word problems'],
  'cur-sci': ['Laws of reflection', 'Spherical mirrors', 'Refraction of light', 'Lens formula', 'Power of a lens'],
  'cur-phy': ['Electric current', 'Ohm\'s law', 'Series and parallel circuits'],
  'cur-eng': ['Formal letters', 'Essay structure'],
}

const modules = Object.entries(moduleTitles).flatMap(([curriculumId, titles]) =>
  titles.map((title, i) => ({
    id: `${curriculumId}-m${i + 1}`,
    curriculum_id: curriculumId,
    order_index: i + 1,
    title,
    description: `Understand ${title.toLowerCase()} with guided practice.`,
    key_concepts: ['Definition', 'Worked example', 'Common mistakes'],
    success_criteria: 'Solve 4 of 5 practice questions correctly.',
    estimated_minutes: 30 + i * 5,
    class_level: 'Class 10',
    board: 'CBSE',
  }))
)

const statusFor = (index: number): 'completed' | 'in_progress' | 'needs_review' | 'not_started' =>
  index < 5 ? 'completed' : index === 5 ? 'in_progress' : index === 7 ? 'needs_review' : index < 9 ? 'completed' : 'not_started'

const progressRecords = modules.slice(0, 10).map((m, i) => {
  const status = statusFor(i)
  return {
    id: `prog-${i + 1}`,
    syllabus_module_id: m.id,
    user_id: USER_ID,
    status,
    score: status === 'completed' ? 72 + ((i * 7) % 26) : status === 'needs_review' ? 48 : null,
    started_at: daysAgo(14 - i),
    completed_at: status === 'completed' ? daysAgo([13, 12, 12, 9, 8, 6, 5, 4, 1, 0][i]) : null,
  }
})

export const mockDashboardProps = {
  user: { id: USER_ID, email: 'student@example.test' },
  profile: {
    id: USER_ID,
    full_name: 'Aarav Sharma',
    avatar_url: null,
    current_streak: 6,
    longest_streak: 12,
    total_classes_taken: 18,
    total_learning_minutes: 645,
    learning_style: 'socratic',
    preferred_pacing: 'standard',
    preferred_teacher_voice: 'Leda',
    weak_subjects: ['Nature of roots', 'Lens formula'],
    strong_subjects: ['Factorisation method', 'Laws of reflection'],
    learning_level: 'intermediate',
    class_level: 'Class 10',
    last_class_date: daysAgo(1).split('T')[0],
  },
  primaryCurriculum: curriculums[0],
  enrolledCurriculums: curriculums.slice(0, 2),
  allCurriculums: curriculums,
  modules,
  progressRecords,
  memories: [
    { id: 'mem-1', memory_text: 'Prefers worked examples before the formal definition.', importance_score: 9, created_at: daysAgo(3) },
    { id: 'mem-2', memory_text: 'Confuses the sign of the discriminant when roots are equal.', importance_score: 8, created_at: daysAgo(5) },
    { id: 'mem-3', memory_text: 'Studies best in 25-minute sessions.', importance_score: 6, created_at: daysAgo(9) },
  ],
  studyPlan: {
    id: 'plan-1',
    user_id: USER_ID,
    target_exam_date: daysAhead(45),
    daily_study_minutes: 60,
    target_curriculum_ids: ['cur-math', 'cur-sci'],
    plan_metadata: null,
    is_active: true,
    created_at: daysAgo(10),
    updated_at: daysAgo(2),
  },
}

'use client'

import React, { useEffect, useState, useRef, useCallback } from 'react'
import { useParams, useRouter } from 'next/navigation'
import { useGeminiLive } from '@/hooks/useGeminiLive'
import { ClassroomAvatar } from '@/components/classroom/ClassroomAvatar'
import { LiveAvatarConfig } from '@/services/geminiWebSocket'
import type { SimliAvatarController } from '@/services/simliAvatarService'
import dynamicImport from 'next/dynamic'
import type { GreenChalkboardRef } from '@/components/whiteboard/GreenChalkboard'

const WhiteboardWorkspace = dynamicImport(
  () => import('@/components/whiteboard/WhiteboardWorkspace').then((mod) => mod.WhiteboardWorkspace),
  {
    ssr: false,
    loading: () => (
      <div className="w-full h-full flex flex-col items-center justify-center bg-[#FFFFFF] text-[var(--ink-primary)] space-y-3 font-serif">
        <div className="w-8 h-8 border-2 border-[var(--accent-primary)] border-t-transparent rounded-full animate-spin" />
        <p className="text-sm tracking-wide text-[var(--ink-secondary)]">Preparing AI Classroom Stage...</p>
      </div>
    ),
  }
)
import { VisualizationSceneType } from '@/components/whiteboard/scenes/sceneTypes'
import { resolveSceneType, parseSceneParams } from '@/components/whiteboard/scenes/sceneRegistry'
import { getLanguageVoiceConfig } from '@/lib/voiceAndLanguageConfig'
import { isLegitimateGraphTopic, isValidGraphPayload, GraphFormulaItem, GraphSegmentItem, GraphPointItem } from '@/lib/graphGating'
import { saveSessionState, loadSessionState, clearSessionState, pruneExpiredSessions } from '@/lib/sessionStateManager'
import { isSchemaError } from '@/lib/utils'
import type { MafsGraphCanvasProps } from '@/components/whiteboard/MafsGraphCanvas'
import { VisualLessonManifest, LessonStep } from '@/types/lessonManifest'
import {
  generateVisualLessonPlanForCapsule,
  inferConceptVisualDirective,
} from '@/services/visualLessonPlanGenerator'
import { VisualEventQueue, parseVisualEventFromDirective } from '@/services/visualEventProtocol'
import { ChapterNotesModal } from '@/components/classroom/ChapterNotesModal'
import { ClassroomConnectingAnimation } from '@/components/classroom/ClassroomConnectingAnimation'
import { resolveBookForChapter, resolveTargetPageForLesson, extractChapterNumber } from '@/lib/textbookResolver'
import { ClassroomControlBar } from '@/components/classroom/ClassroomControlBar'
import { SelfViewTile } from '@/components/classroom/SelfViewTile'
import { useCameraPreview } from '@/hooks/useCameraPreview'
import { ErrorModal } from '@/components/ErrorModal'
import { MasteryQuizModal } from '@/components/quiz/MasteryQuizModal'
import {
  Mic,
  Play,
  ArrowLeft,
  BookOpen,
  CheckCircle2,
  Sparkles,
  Layers,
  Check,
  RotateCcw,
  AlertCircle,
  X,
  ChevronRight,
} from 'lucide-react'
import { Button } from '@/components/ui/button'
import { DashCard } from '@/components/dashboard/primitives'
import { createClient } from '@/utils/supabase/client'
import { triggerCompanionGuidance } from '@/components/mascot/companionEvents'
import {
  setCachedBoardNotes,
  getCachedBoardNotes,
  invalidateStudentProgressCache,
} from '@/lib/studentProgressService'
import {
  getCachedSyllabusModule,
  getCachedSiblingModules,
  getCachedNextChapterInfo,
  getCachedCurriculumModuleCounts,
  getCachedUserProfile,
  getCachedUserProgressList,
  getCachedModuleProgress,
  getCachedUserMemories,
  invalidateUserProgressCache,
  invalidateUserProfileCache,
  invalidateUserEnrollmentsCache,
} from '@/lib/cache/dataCache'

export const dynamic = 'force-dynamic'

function getPedagogyArchitectureDirective(classLevel: string, subject: string, board: string = 'CBSE', chapterOrTopic: string = ''): string {
  const context = `${subject || ''} ${chapterOrTopic || ''}`.toLowerCase()
  const cl = (classLevel || '').toLowerCase()
  const isG9 = cl.includes('9') || cl.includes('ix')
  const isG10 = cl.includes('10') || cl.includes(' x') || cl === 'x' || cl.includes('tenth')
  const isG11 = cl.includes('11') || cl.includes('xi') || cl.includes('eleventh')
  const isG12 = cl.includes('12') || cl.includes('xii') || cl.includes('twelfth')

  const isMath = context.includes('math') || context.includes('algebra') || context.includes('calculus') || context.includes('geometry') || context.includes('arithmetic')
  const isScience = context.includes('science')
  const isPhysics = context.includes('physic')
  const isChemistry = context.includes('chem')
  const isBiology = context.includes('bio') || context.includes('life') || context.includes('botan') || context.includes('zoolog') || context.includes('cell')

  const isOrganicChem = isChemistry && (
    context.includes('organic') || context.includes('hydrocarbon') || context.includes('iupac') ||
    context.includes('isomer') || context.includes('haloalkane') || context.includes('aldehyde') ||
    context.includes('ketone') || context.includes('amine') || context.includes('alcohol') ||
    context.includes('phenol') || context.includes('ether') || context.includes('benzene') ||
    context.includes('polymer') || context.includes('biomolecule') || context.includes('goc') ||
    context.includes('mechanism')
  )
  const isInorganicChem = isChemistry && !isOrganicChem && (
    context.includes('inorganic') || context.includes('periodic') || context.includes('bonding') ||
    context.includes('block') || context.includes('metal') || context.includes('coordination') ||
    context.includes('p-block') || context.includes('d-block') || context.includes('s-block') ||
    context.includes('f-block') || context.includes('hydrogen') || context.includes('metallurgy') ||
    context.includes('periodicity')
  )
  const isPhysicalChem = isChemistry && !isOrganicChem && !isInorganicChem

  const COMMON_PRINCIPLES = `
- COMMON PEDAGOGICAL PRINCIPLES (ALL GRADES & SUBJECTS):
  * ADAPT TO STUDENT: Dynamically adjust pacing, depth, and hints to the student's live understanding and learning pace.
  * INTERACTIVE 2-WAY DIALOGUE: Maintain an engaging conversation; never lecture in long uninterrupted monologues.
  * SIMPLE HINGLISH/ENGLISH: Use colloquial, everyday phrasing ("samjhe," "dekho," "bilkul," "chalo") with zero academic pretension.
  * SPACED REVISION: Anchor new ideas by regularly referencing previously mastered concepts ("Remember when we saw...").
  * EXAM READINESS: Structure answers around board-exam criteria (${board || 'CBSE'}), highlighting common student pitfalls and scoring keywords.
  * SUPPORTIVE MENTOR TONE: Real teacher warmth, empathy, celebrating correct insights ("Shabash!", "Exactly right!"), patient and diagnostic with mistakes.`

  // 1. Grade 9 Mathematics (Cricket, Mobile Data, Discounts, 1 Model + 4-5 Varied Practice, 9-10 Questions/Capsule)
  if (isG9 && isMath) {
    return `[GRADE 9 MATHEMATICS PEDAGOGICAL DIRECTIVE - USER GUIDE INVARIANT]:
- REAL-LIFE ANCHORS FIRST: Ground every abstract concept in tangible daily life (cricket bowling speed & run rate, mobile data recharge packs, market discounts & profit/loss, pizza slices for fractions, playground boundaries for perimeter/area).
- MICRO-PACING & QUESTION DEPTH: Fewer concepts per capsule, extreme question-solving depth. Never rush abstract algebraic theory.
- 1 EASY MODEL EXAMPLE + 4-5 VARIED PRACTICE QUESTIONS: Immediately after explaining the concept intuition and formula, solve 1 simple, clear model exemplar on the chalkboard. Then actively present 4 to 5 varied practice problems with progressive difficulty (direct formula -> variable reversal -> word problem -> multi-step challenge). Target 9-10 questions per capsule across concepts.
- INTERACTIVE STEP-BY-STEP CHECKPOINTS: Check in after each algebraic step. Ask guiding Socratic questions; do not lecture in long continuous theoretical monologues.${COMMON_PRINCIPLES}`
  }

  // 2. Grade 9 Science ('Picture this' visualization, Home/Outside phenomena, Depth over brevity, 2-3 conceptual 'why' questions)
  if (isG9 && (isScience || isPhysics || isChemistry || isBiology)) {
    return `[GRADE 9 SCIENCE PEDAGOGICAL DIRECTIVE - USER GUIDE INVARIANT]:
- 'PICTURE THIS' SENSORY VISUALIZATION HOOK: Every concept MUST start with a vivid sensory mental picture before formal laws (e.g., 'Picture this: you are standing inside a moving bus that suddenly slams on the brakes...', 'Picture this: a pan of water boiling on a stove as steam bubbles burst...').
- DAILY HOME & OUTDOOR PHENOMENA: Connect directly to everyday home/outdoor observations (boiling water, moving bus, bicycle inertia, sound echo in an empty hall, bicycle brakes, rust on iron gates).
- DEPTH OVER BREVITY: Explain the living physical/molecular mechanism under the hood. Avoid superficial dictionary definitions.
- 2-3 SHORT CONCEPTUAL 'WHY' QUESTIONS FIRST: Before jumping into formulas or NCERT numericals, pose 2-3 quick diagnostic conceptual questions ('Why did your body lean forward?', 'What happens if we double the mass?') to ignite critical reasoning.${COMMON_PRINCIPLES}`
  }

  // 3. Grade 10 Mathematics (Moderate pace, 50/50 Concept-Question, Concept-First via Questions, Board Spectrum, Whiteboard layout)
  if (isG10 && isMath) {
    return `[GRADE 10 MATHEMATICS PEDAGOGICAL DIRECTIVE - USER GUIDE INVARIANT]:
- 50/50 CONCEPT-QUESTION CADENCE: Equal time for conceptual clarity and rigorous board-exam problem solving.
- CONCEPT-FIRST VIA QUESTIONS (PROBLEM-FIRST INDUCTION): Introduce concepts through an authentic problem hook or practical dilemma first (present the puzzle before stating the formula/theorem), creating intellectual hunger to learn the method!
- FULL BOARD EXAM SPECTRUM: Cover all standard board question formats: 1-mark objective/MCQs, 2-mark short answers, 3-mark analytical/proofs, and 4-5 mark case-based / competency-based questions.
- AUTHENTIC TOPPER WHITEBOARD LAYOUT: Meticulous step-by-step layout (Given -> To Prove / Formula -> Substitution -> Step-by-Step Calculation -> [ROUGH_WORK] Margin -> Boxed Final Answer with SI Units or 'Hence Proved!').
- COORDINATE GEOMETRY DISTANCE FORMULA MANDATE: Whenever distance between two points (x₁, y₁) and (x₂, y₂) is involved, ALWAYS write the full authentic Distance Formula with square root first: write_chalkboard(action="draw_step", content="Distance Formula: d = √[(x₂ - x₁)² + (y₂ - y₁)²]", color="blue"). Show complete substitution under the square root: d = √[(7 - 2)² + (3 - 3)²] = √[5² + 0] = √25 = 5 units. Box final answer: write_chalkboard(action="draw_step", content="Boxed Answer: [ d = 5 units ]", color="botanical"). NEVER use lazy 1D shortcuts like |x2 - x1| without first writing the authentic square root distance formula!
- PROACTIVE CARTESIAN GRAPHING: Whenever teaching points, lines, segments, distances, or coordinate geometry, PROACTIVELY CALL plot_mathematical_graph(...) to plot points A and B, draw segment AB, and label distance AB. Never say "imagine in your head" when you can plot it!${COMMON_PRINCIPLES}`
  }

  // 4. Grade 10 Science (Conceptual imagination without ratta, student's own words, depth over quantity, Assertion-Reason & Case-based)
  if (isG10 && (isScience || isPhysics || isChemistry || isBiology)) {
    return `[GRADE 10 SCIENCE PEDAGOGICAL DIRECTIVE - USER GUIDE INVARIANT]:
- CONCEPTUAL IMAGINATION WITHOUT ROTE MEMORIZATION (ZERO RATTA): Strictly eliminate rote recitation. Train students to reason from first principles and articulate scientific phenomena in their own natural words.
- DEPTH OVER QUANTITY: Prioritize deep mastery of core mechanisms over superficial coverage of many topics.
- ASSERTION-REASONING MASTERY: Explicitly train students on CBSE/ICSE Assertion-Reason questions (Assertion (A), Reason (R) — evaluating both truth values and whether R is the correct explanation of A).
- CASE-BASED & EXPERIMENTAL QUESTIONS: Present experimental setups (circuits, test tubes, ray diagrams) and guide analytical deduction.${COMMON_PRINCIPLES}`
  }

  // 5. Grade 11 Mathematics (Transition gap bridging, prerequisite checks, question-first, explicit proofs, visual plots)
  if (isG11 && isMath) {
    return `[GRADE 11 MATHEMATICS PEDAGOGICAL DIRECTIVE - USER GUIDE INVARIANT]:
- TRANSITION GAP BRIDGING & PREREQUISITE CHECKS: The Class 10 to 11 transition is steep. Always verify foundational prerequisites first (quadratic roots, trigonometry identities, algebraic factorization) before diving into limits, calculus, conic sections, or complex numbers.
- QUESTION-FIRST INDUCTION: Pose an intriguing boundary dilemma or limit paradox before formal theorem statement.
- EXPLICIT PROOF & REASONING STEPS: State axioms and theorems rigorously; never skip intermediate algebraic or geometric proof steps.
- PURE VECTOR MATHEMATICAL GRAPHS: Compulsory visual plotting via plot_mathematical_graph (domain, range, asymptotes, roots, intercepts, extrema, comparative function curves).${COMMON_PRINCIPLES}`
  }

  // 6. Grade 11 Physical Chemistry (Math-heavy, high questions, Given + Formula + Units first)
  if (isG11 && isPhysicalChem) {
    return `[GRADE 11 PHYSICAL CHEMISTRY PEDAGOGICAL DIRECTIVE - USER GUIDE INVARIANT]:
- QUANTITATIVE & MATH-HEAVY: Numerical-intensive precision (mole concept, thermodynamics, equilibrium, chemical kinetics).
- HIGH PRACTICE QUESTION VOLUME: Drill authentic numerical problems with varied setups.
- GIVEN + FORMULA + UNITS FIRST: Board topper discipline — extract Given quantities with SI units, execute explicit unit conversions (atm to Pa, L to m³, kJ to J), state formula, show substitution, calculate, and box final answer.${COMMON_PRINCIPLES}`
  }

  // 7. Grade 11 Inorganic Chemistry (Deep concepts, why/how trends, tables & mnemonics, more homework)
  if (isG11 && isInorganicChem) {
    return `[GRADE 11 INORGANIC CHEMISTRY PEDAGOGICAL DIRECTIVE - USER GUIDE INVARIANT]:
- DEEP CONCEPTUAL REASONING: Explain WHY and HOW trends occur (effective nuclear charge Z_eff, shielding/screening effect, electronic configuration stability, inert pair effect, lattice vs hydration enthalpy).
- STRUCTURED TABLES & MNEMONICS: Use chalkboard tables (draw_table) for periodic trends and memorable mnemonics for memorizing group elements, oxidation states, and anomalous behaviors.
- FREQUENT RECALL & CHECKPOINTS: Regular quick retention checks to solidify chemical facts.${COMMON_PRINCIPLES}`
  }

  // 8. Grade 11 Organic Chemistry (Reaction mechanisms, electron movement, IUPAC, isomerism, reaction chains)
  if (isG11 && isOrganicChem) {
    return `[GRADE 11 ORGANIC CHEMISTRY PEDAGOGICAL DIRECTIVE - USER GUIDE INVARIANT]:
- MECHANISTIC ARROW-PUSHING: Teach reaction mechanisms with explicit curved arrow notation showing electron pair movement.
- CORE FOUNDATIONS: Electrophiles, nucleophiles, carbocation/carbanion stability, inductive (+I, -I), resonance (+R, -R), and hyperconjugation effects.
- IUPAC NOMENCLATURE & ISOMERISM: Rigorous rule-based naming and structural/stereoisomerism.
- MULTI-STEP REACTION CHAINS & CONVERSIONS: Lay out organic synthetic pathways from compound A to compound B via reagents on the chalkboard.${COMMON_PRINCIPLES}`
  }

  // 9. Grade 11 Physics & Biology (Real phenomenon -> concept -> derivation -> numerical; biology flowcharts)
  if (isG11 && isPhysics) {
    return `[GRADE 11 PHYSICS PEDAGOGICAL DIRECTIVE - USER GUIDE INVARIANT]:
- REAL PHENOMENON HOOK -> CONCEPT -> DERIVATION -> NUMERICAL: Begin with a tangible physical phenomenon, formulate the governing law, derive step-by-step without skipping steps, and solve authentic board numericals.
- MANDATORY MATHEMATICAL GRAPHING: Compulsory plotting via plot_mathematical_graph for kinematics (s-t, v-t, a-t), SHM, thermodynamics (P-V), and vector resolutions.${COMMON_PRINCIPLES}`
  }

  if (isG11 && isBiology) {
    return `[GRADE 11 BIOLOGY PEDAGOGICAL DIRECTIVE - USER GUIDE INVARIANT]:
- PHYSIOLOGICAL PHENOMENON -> CELLULAR MECHANISM -> FLOWCHART: Begin with a living biological hook, explain cellular/molecular mechanisms, and synthesize multi-step processes via structured flowcharts (draw_flowchart) for cycles (Krebs cycle, Calvin cycle, cardiac cycle, nephron counter-current mechanism) and high-res diagrams.${COMMON_PRINCIPLES}`
  }

  // Grade 12 Fallbacks
  if (isG12 && isMath) {
    return `[GRADE 12 MATHEMATICS PEDAGOGICAL DIRECTIVE]:
- Advanced calculus, differential equations, vectors, and 3D geometry with complete proof rigor, coordinate visual plots via plot_mathematical_graph, and board exemplar questions.${COMMON_PRINCIPLES}`
  }
  if (isG12 && isPhysics) {
    return `[GRADE 12 PHYSICS PEDAGOGICAL DIRECTIVE]:
- Electromagnetism, optics ray paths, wave optics, modern physics derivations, and board-exam numericals with Given + Formula + Units layout.${COMMON_PRINCIPLES}`
  }
  if (isG12 && isChemistry) {
    return `[GRADE 12 CHEMISTRY PEDAGOGICAL DIRECTIVE]:
- Solutions, electrochemistry, chemical kinetics numericals; d- and f-block trends; coordination chemistry; haloalkanes, aldehydes, ketones, amines mechanisms and organic synthesis chains.${COMMON_PRINCIPLES}`
  }
  if (isG12 && isBiology) {
    return `[GRADE 12 BIOLOGY PEDAGOGICAL DIRECTIVE]:
- Genetics, molecular basis of inheritance, biotechnology processes, physiology, and ecology with structured flowcharts (draw_flowchart) and labeled diagrams.${COMMON_PRINCIPLES}`
  }

  // Fallbacks for generic subjects
  if (isMath) {
    return `Focus on mathematical concepts, theorems, axioms, step-by-step proofs, and fully worked exemplar & exercise solutions.${COMMON_PRINCIPLES}`
  }
  if (isPhysics || isChemistry || isScience) {
    return `Focus on physical intuition, natural laws/equations, units/dimensions, and scratch math in [ROUGH_WORK: ...].${COMMON_PRINCIPLES}`
  }
  if (isBiology) {
    return `Focus on biological mechanisms, anatomical structures, cellular pathways, and visual schematics ([FLOWCHART: ...] or [DIAGRAM: ...]).${COMMON_PRINCIPLES}`
  }
  if (context.includes('hist') || context.includes('civic') || context.includes('politi') || context.includes('geograph') || context.includes('econ') || context.includes('social')) {
    return `Focus on chronological timelines, cause-and-effect, pivotal events, geographical processes, and structured analytical arguments.${COMMON_PRINCIPLES}`
  }
  if (context.includes('comp') || context.includes('code') || context.includes('program') || context.includes('data')) {
    return `Focus on algorithmic logic, data structures, step-by-step execution traces, and clean syntax.${COMMON_PRINCIPLES}`
  }
  if (context.includes('lang') || context.includes('eng') || context.includes('lit') || context.includes('gramm') || context.includes('hindi') || context.includes('french')) {
    return `Focus on grammatical principles, thematic analysis, textual evidence, and model sentence exemplars.${COMMON_PRINCIPLES}`
  }
  return `Focus on clear conceptual understanding, precise principles, and interactive Socratic guidance.${COMMON_PRINCIPLES}`
}

function getSubjectPedagogyDirective(subject: string, classLevel: string = '', board: string = 'CBSE', chapterOrTopic: string = ''): string {
  if (classLevel) {
    return getPedagogyArchitectureDirective(classLevel, subject, board, chapterOrTopic)
  }
  const s = (subject || '').toLowerCase()
  if (s.includes('math') || s.includes('algebra') || s.includes('calculus') || s.includes('geometry')) {
    return 'Focus on mathematical concepts, theorems, axioms, step-by-step proofs, and fully worked exemplar & exercise solutions.'
  }
  if (s.includes('physic') || s.includes('chem') || s.includes('science')) {
    return 'Focus on physical intuition, natural laws/equations, units/dimensions, and scratch math in [ROUGH_WORK: ...].'
  }
  if (s.includes('bio') || s.includes('life') || s.includes('environ') || s.includes('botan') || s.includes('zoolog')) {
    return 'Focus on biological mechanisms, anatomical structures, cellular pathways, and visual schematics ([FLOWCHART: ...] or [DIAGRAM: ...]).'
  }
  if (s.includes('hist') || s.includes('civic') || s.includes('politi') || s.includes('geograph') || s.includes('econ') || s.includes('social')) {
    return 'Focus on chronological timelines, cause-and-effect, pivotal events, geographical processes, and structured analytical arguments.'
  }
  if (s.includes('comp') || s.includes('code') || s.includes('program') || s.includes('data')) {
    return 'Focus on algorithmic logic, data structures, step-by-step execution traces, and clean syntax.'
  }
  if (s.includes('lang') || s.includes('eng') || s.includes('lit') || s.includes('gramm') || s.includes('hindi') || s.includes('french')) {
    return 'Focus on grammatical principles, thematic analysis, textual evidence, and model sentence exemplars.'
  }
  return 'Focus on clear conceptual understanding, precise definitions, and interactive Socratic guidance.'
}

function parseKeyConcepts(raw: any): string[] {
  const sanitize = (s: string) =>
    String(s || '')
      .replace(/^[\s\(\[\{\"\']+|[\s\)\]\}\"\']+$/g, '')
      .replace(/^concept\s*\d*[:\-\s]*/i, '')
      .replace(/^\d+[\.\:\)\-]\s*/, '')
      .replace(/^focus:\s*/i, '')
      .replace(/\s+/g, ' ')
      .trim()

  if (Array.isArray(raw)) return raw.map(sanitize).filter(Boolean)
  if (typeof raw === 'string' && raw.trim()) {
    const trimmed = raw.trim()
    if (trimmed.startsWith('[')) {
      try {
        const parsed = JSON.parse(trimmed)
        if (Array.isArray(parsed)) return parsed.map(sanitize).filter(Boolean)
      } catch {}
    }
    const splitItems = trimmed.split(/\n|,|•|;/).map(sanitize).filter(Boolean)
    if (splitItems.length > 1) return splitItems
    return [sanitize(trimmed)].filter(Boolean)
  }
  return []
}

/**
 * Distills lengthy module descriptions or activity titles into crisp, 2-4 word queries
 * tailored for high-accuracy Wikimedia Commons and scientific image search.
 */
function extractConciseSearchKeyword(raw: string): string {
  if (!raw || !raw.trim()) return ''
  let clean = raw.trim().replace(/^["']|["']$/g, '')

  // 1. Strip leading curriculum prefixes like "Activity 2.1: ", "Concept 3: ", "Module 1 - "
  clean = clean
    .replace(/^(?:Activity|Concept|Module|Experiment|Lab|Chapter|Section|Exercise)\s*[\d\.]*\s*[:\-\)]?\s*/i, '')
    .trim()

  // 2. Colon prefix/subtitle handling: ALWAYS isolate the core concept title BEFORE the colon
  if (clean.includes(':')) {
    const parts = clean.split(':').map((s) => s.trim()).filter(Boolean)
    const part0 = parts[0]?.replace(/[\(\)\[\]\{\}]/g, ' ').replace(/\s+/g, ' ').trim() || ''
    const part1 = parts[1]?.replace(/[\(\)\[\]\{\}]/g, ' ').replace(/\s+/g, ' ').trim() || ''

    const isPart0Generic = /^(?:part|step|subpart|case|fig|figure|section|table|row|col|overview|introduction)\s*[\d\w\.]*$/i.test(part0)
    if (part0.length >= 3 && part0.length <= 60 && !isPart0Generic) {
      clean = part0
    } else if (part1.length >= 3 && part1.length <= 60 && part1.split(' ').length <= 7) {
      clean = part1
    } else if (part0.length >= 3) {
      clean = part0.slice(0, 60).trim()
    }
  }

  // 3. Parenthetical handling on the isolated title ONLY (e.g. "Activity (Onion Peel)" -> "Onion Peel cells microscope")
  const parenMatch = clean.match(/\(([^\)]+)\)/)
  if (parenMatch && parenMatch[1]) {
    const inside = parenMatch[1]
      .replace(/^(activity|module|step|exp|experiment)\s*[\d\.]*/i, '')
      .replace(/['"]/g, '')
      .trim()
    if (/peel|mount|cell|tissue|specimen|stomata/i.test(inside)) {
      return `${inside.replace(/mount|mounts/i, 'cells')} microscope`
    }
    if (/if and only if/i.test(inside)) {
      clean = 'Biconditional statement if and only if'
    } else if (clean.startsWith('Activity') && inside.length >= 3) {
      clean = inside
    }
  }

  // Clean remaining parenthetical marks
  clean = clean.replace(/[\(\)\[\]\{\}'"]/g, ' ').replace(/\s+/g, ' ').trim()

  // 4. Fine-grained Academic Mathematics & Logic mappings
  if (/converse/i.test(clean) && /baudhayana|pythagor/i.test(clean)) {
    return 'Converse of Pythagoras theorem right triangle proof'
  }
  if (/baudhayana|pythagor/i.test(clean)) {
    return 'Baudhayana Pythagoras theorem right triangle proof'
  }
  if (/converse/i.test(clean)) {
    return 'Converse of conditional statement logic'
  }
  if (/biconditional|if and only if/i.test(clean)) {
    return 'Biconditional statement if and only if logic'
  }
  if (/counterexample/i.test(clean)) {
    return 'Mathematical counterexample logic diagram'
  }
  if (/truth\s*value|independence\s*of\s*truth/i.test(clean)) {
    return 'Conditional statement converse truth values'
  }
  if (/truth\s*table/i.test(clean)) {
    return 'Truth Table logic proposition'
  }
  if (/proposition|statement.*truth/i.test(clean)) {
    return 'Propositional logic statement truth'
  }

  // Geometry & Algebra mappings
  if (/quadrilateral|parallelogram/i.test(clean)) return 'Parallelogram properties geometry diagram'
  if (/linear\s*equation/i.test(clean)) return 'Linear equation coordinate graph diagram'
  if (/surface\s*area|volume.*(cylinder|cone|sphere)/i.test(clean)) return 'Surface area and volume geometry formula'
  if (/histogram|frequency\s*polygon/i.test(clean)) return 'Histogram frequency polygon statistics diagram'
  if (/algorithm|flowchart/i.test(clean)) return 'Algorithm flowchart diagram'

  // Science mappings
  if (/onion\s*peel/i.test(clean)) return 'Onion peel cells microscope'
  if (/human\s*cheek.*methylene|cheek.*methylene/i.test(clean)) return 'Human Cheek Cells Methylene Blue Stain'
  if (/human\s*cheek|cheek\s*cell/i.test(clean)) return 'Human cheek cells microscope'
  if (/robert\s*hooke|cork\s*cell/i.test(clean)) return 'Robert Hooke Micrographia cork cells 1665'
  if (/plant\s*cell\s*wall/i.test(clean)) return 'Plant cell wall ultrastructure diagram'
  if (/plant\s*cell/i.test(clean)) return 'Plant cell anatomy diagram'
  if (/animal\s*cell/i.test(clean)) return 'Animal cell anatomy diagram'
  if (/chloroplast/i.test(clean)) return 'Chloroplast structure diagram'
  if (/mitochondri[ao]/i.test(clean)) return 'Mitochondria structure diagram'
  if (/nucleus/i.test(clean)) return 'Cell nucleus structure diagram'
  if (/stomata/i.test(clean)) return 'Leaf stomata guard cells microscope'
  if (/xylem/i.test(clean)) return 'Xylem tissue microscope'
  if (/phloem/i.test(clean)) return 'Phloem tissue microscope'
  if (/osmosis/i.test(clean)) return 'Osmosis experiment diagram'
  if (/diffusion/i.test(clean)) return 'Diffusion experiment diagram'

  // 5. If short enough or already a detailed academic query, keep as is
  if (clean.length <= 140 && clean.split(' ').length <= 16) return clean

  // 6. Filter out filler words to get top keywords
  const words = clean
    .replace(/^Activity\s*[\d\.]+\s*[:\-\(]?/i, '')
    .replace(/[\(\)\[\]\{\}:,;]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .split(' ')
    .filter(
      (w) =>
        !/^(stripping|observing|mounting|with|and|the|of|in|to|a|an|is|are|for|by|from|into|large|small|regular|inner|outer|buccal)$/i.test(
          w
        )
    )
  return words.slice(0, 16).join(' ') || clean.slice(0, 140)
}

function tokenizeForMatch(text: string): string[] {
  return String(text || '')
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, ' ')
    .split(/\s+/)
    .filter(
      (w) =>
        w.length >= 3 &&
        ![
          'the', 'and', 'for', 'with', 'into', 'from', 'using', 'concept',
          'between', 'two', 'points', 'same', 'line', 'any', 'three', 'formula',
        ].includes(w)
    )
}

function scoreConceptVisualMatch(cv: any, targetConcept: string): number {
  if (!cv || !targetConcept) return 0
  const tLower = targetConcept.toLowerCase().trim()
  const cvC = String(cv.concept_title || '').toLowerCase().trim()
  const cvD = String(cv.diagram_title || '').toLowerCase().trim()
  if (!cvC && !cvD) return 0
  if (cvC && (cvC === tLower || cvC.includes(tLower) || tLower.includes(cvC))) return 100
  if (cvD && (cvD === tLower || cvD.includes(tLower) || tLower.includes(cvD))) return 80
  const targetTokens = tokenizeForMatch(targetConcept)
  const hayTokens = new Set(tokenizeForMatch(`${cvC} ${cvD}`))
  if (targetTokens.length === 0) return 0
  let hits = 0
  for (const tok of targetTokens) {
    if (hayTokens.has(tok)) hits++
  }
  return hits > 0 ? Math.round((hits / targetTokens.length) * 60) : 0
}

function findMatchingConceptVisual(
  conceptVisualsList: any[],
  conceptName: string,
  keyConcepts: string[],
  conceptIdx: number
): any | undefined {
  if (!Array.isArray(conceptVisualsList) || conceptVisualsList.length === 0) return undefined

  let bestCv: any = undefined
  let bestScore = 0
  for (const cv of conceptVisualsList) {
    const score = scoreConceptVisualMatch(cv, conceptName)
    if (score > bestScore) {
      bestScore = score
      bestCv = cv
    }
  }
  if (bestCv && bestScore >= 30) {
    return bestCv
  }

  // Only fall back by numeric index if that visual does NOT strongly belong to a DIFFERENT concept
  const indexed = conceptVisualsList[conceptIdx]
  if (indexed) {
    const indexedTargetScore = scoreConceptVisualMatch(indexed, conceptName)
    const ownsOtherConcept = keyConcepts.some((other, oIdx) => {
      if (oIdx === conceptIdx) return false
      return scoreConceptVisualMatch(indexed, other) > indexedTargetScore + 20
    })
    if (!ownsOtherConcept) {
      return indexed
    }
  }
  return undefined
}

function findMatchingWorkedExample(
  workedExamples: any[],
  conceptName: string,
  keyConcepts: string[],
  conceptIdx: number
): any | undefined {
  if (!Array.isArray(workedExamples) || workedExamples.length === 0) return undefined
  const targetTokens = tokenizeForMatch(conceptName)
  let bestEx: any = undefined
  let bestScore = 0
  for (const ex of workedExamples) {
    const hay = `${ex?.problem || ''} ${ex?.formula || ''} ${ex?.given || ''} ${ex?.calculation || ''}`.toLowerCase()
    let hits = 0
    for (const tok of targetTokens) {
      if (hay.includes(tok)) hits++
    }
    const score = targetTokens.length > 0 ? hits / targetTokens.length : 0
    if (score > bestScore) {
      bestScore = score
      bestEx = ex
    }
  }
  if (bestEx && bestScore >= 0.4) return bestEx

  const indexed = workedExamples[conceptIdx]
  if (indexed) {
    const hay = `${indexed?.problem || ''} ${indexed?.formula || ''}`.toLowerCase()
    const matchesOther = keyConcepts.some((other, oIdx) => {
      if (oIdx === conceptIdx) return false
      const toks = tokenizeForMatch(other)
      return toks.length >= 2 && toks.every((t) => hay.includes(t))
    })
    if (!matchesOther) return indexed
  }
  return undefined
}

/**
 * High-density concept micro-dossier engine.
 * Strips verbose token waste by 70-85% while packing 100% textbook facts,
 * SI units, governing equations, and 2-3 authentic board-exam questions per concept.
 */
function buildConceptMicroDossiers(
  keyConcepts: string[],
  activeModule: any,
  resolvedBoard: string,
  resolvedClassLevel: string,
  resolvedSubject: string,
  chapterName: string,
  workedExamples: any[],
  misconceptions: string[]
): string {
  if (!keyConcepts || keyConcepts.length === 0) return ''

  const visualPlan = activeModule?.visual_lesson_plan || {}
  const textbookDefs: any[] = visualPlan?.textbook_definitions || activeModule?.textbook_definitions || []
  const textbookExamples: any[] = visualPlan?.textbook_examples || activeModule?.textbook_examples || []
  const textbookExercises: any[] = visualPlan?.textbook_exercises || activeModule?.textbook_exercises || []
  const subtopics: string[] = activeModule?.subtopics?.length ? activeModule.subtopics : (visualPlan?.subtopics || [])
  const chapterFlowchart = visualPlan?.chapter_flowchart || activeModule?.chapter_flowchart || ''
  const diagramType = visualPlan?.diagram_type || activeModule?.diagram_type || 'vector_svg_diagram'
  const whatToMake = visualPlan?.what_to_make || visualPlan?.diagram_description || activeModule?.what_to_make || ''

  // Format module-level subtopics overview so tutor knows every subtopic that must be covered
  const subtopicsHeader = subtopics.length > 0
    ? `MANDATORY EXAMINATION SUBTOPICS TO COVER IN THIS CAPSULE (Must cover 100% of these):\n${subtopics.map((st, i) => `  ${i + 1}. ${st}`).join('\n')}\n\n`
    : ''

  // Format chapter flowchart if available
  const flowchartSection = chapterFlowchart
    ? `CHAPTER FLOWCHART (MANDATORY ON STEP 1):\nCall write_chalkboard(action="draw_flowchart", content="${chapterFlowchart}") to establish the visual architectural map on the chalkboard!\n\n`
    : ''

  // Format textbook exercises overview if available
  const exercisesOverview = textbookExercises.length > 0
    ? `\nAUTHENTIC TEXTBOOK EXERCISES (In-Text & Chapter-End):\n${textbookExercises.map((ex: any) => {
        const qList = (ex.questions || []).map((q: any) => `  - [${q.q_num || 'Q'}] (${q.question_type || 'Exercise'}): ${q.question}${q.solution_method ? ` | Method: ${q.solution_method}` : ''}`).join('\n')
        return `${ex.exercise_number || 'Exercise Set'}:\n${qList}`
      }).join('\n')}\n`
    : ''

  const conceptBlocks = keyConcepts.map((rawConcept, idx) => {
    const conceptName = rawConcept.replace(/^[\s\(\[\{]+|[\s\)\]\}]+$/g, '').trim()
    const ex1 = findMatchingWorkedExample(workedExamples, conceptName, keyConcepts, idx)
    const misc = misconceptions[idx] || misconceptions[0]

    const isMathSubject = /math|algebra|geometry|calculus|trigonometry|statistics|probability/i.test(
      String(resolvedSubject || chapterName || '')
    )

    // 1. Match all definitions / core theorems that mention or match conceptName
    const matchingDefs = Array.isArray(textbookDefs)
      ? textbookDefs.filter(
          (d: any) =>
            (d.concept || '').toLowerCase().includes(conceptName.toLowerCase()) ||
            conceptName.toLowerCase().includes((d.concept || '').toLowerCase())
        )
      : []
    const defToUse = matchingDefs.length > 0 ? matchingDefs : (textbookDefs[idx] ? [textbookDefs[idx]] : [])
    const defLabel = isMathSubject ? 'Core Mathematical Concept / Property' : 'Verbatim Textbook Definition'
    const defStr = defToUse.length > 0
      ? defToUse.map((d: any) => `\n   * ${defLabel}: "${d.definition}" ${d.si_units ? `[SI Unit: ${d.si_units}]` : ''}`).join('')
      : ''

    // 2. Match all textbook illustrative examples for this concept
    const matchingExamples = Array.isArray(textbookExamples)
      ? textbookExamples.filter(
          (e: any) =>
            (e.title || '').toLowerCase().includes(conceptName.toLowerCase()) ||
            conceptName.toLowerCase().includes((e.title || '').toLowerCase()) ||
            (e.scenario || '').toLowerCase().includes(conceptName.toLowerCase())
        )
      : []
    const exToUse = matchingExamples.length > 0 ? matchingExamples : (textbookExamples[idx] ? [textbookExamples[idx]] : [])
    const exStr = exToUse.length > 0
      ? `\n   * Textbook Real-Life Scenarios / Concrete Illustrations:\n` +
        exToUse.map((e: any) => `     - "${e.title}": ${e.scenario}`).join('\n')
      : ''

    // 3. Match relevant exercises for this concept (keyword overlap + proportional partition fallback; zero truncation)
    const conceptTokens = conceptName
      .toLowerCase()
      .replace(/[^a-z0-9\s]/g, ' ')
      .split(/\s+/)
      .filter((w) => w.length >= 3 && !['the', 'and', 'for', 'with', 'into', 'from', 'using', 'concept'].includes(w))
    const allExQuestions = textbookExercises.flatMap((ex: any) =>
      (ex.questions || []).map((q: any) => ({ ...q, exercise_number: ex.exercise_number, exercise_title: ex.exercise_title }))
    )
    const directMatchedExercises = allExQuestions.filter((q: any) => {
      const hay = `${q.question || ''} ${q.solution_method || ''} ${q.exercise_title || ''}`.toLowerCase()
      if (hay.includes(conceptName.toLowerCase())) return true
      return conceptTokens.some((tok) => hay.includes(tok))
    })
    const perConceptSlice = allExQuestions.length > 0 && keyConcepts.length > 0
      ? Math.max(1, Math.ceil(allExQuestions.length / keyConcepts.length))
      : 0
    const matchingExercises = directMatchedExercises.length > 0
      ? directMatchedExercises
      : allExQuestions.slice(idx * perConceptSlice, (idx + 1) * perConceptSlice)
    const exerciseStr = matchingExercises.length > 0
      ? `\n   * Linked Textbook In-Text / Board Exercises (Solve ALL of these with Exercise & Question numbers written clearly on board):\n` +
        matchingExercises.map((q: any) => `     - [Exercise ${q.exercise_number || '1'} • Q.${q.q_num || '1'}]: ${q.question}${q.solution_method ? ` (Solve: ${q.solution_method})` : ''}`).join('\n')
      : ''

    // 4. Model problem
    const q1 = ex1?.problem
      ? `Model Problem: ${ex1.problem} (Given: ${ex1.given || ''}, Formula: ${ex1.formula || ''}, Ans: ${ex1.finalAnswer || ''} ${ex1.unit || ''})`
      : `Q: State the law/definition for ${conceptName}. | Ans: Standard ${resolvedBoard} formulation.`

    // 5. Prepared 4-6 questions for socratic gating
    const conceptQuestionsList = Array.isArray(visualPlan?.concept_questions)
      ? visualPlan.concept_questions
      : Array.isArray(activeModule?.concept_questions)
      ? activeModule.concept_questions
      : []
    const matchingQuestions =
      conceptQuestionsList.find(
        (cq: any) =>
          cq.concept_index === idx ||
          (cq.concept_title || '').toLowerCase().includes(conceptName.toLowerCase()) ||
          conceptName.toLowerCase().includes((cq.concept_title || '').toLowerCase())
      ) || conceptQuestionsList[idx]
    const rawQuestions = matchingQuestions?.questions?.length
      ? matchingQuestions.questions
      : (conceptQuestionsList.length > 0 && conceptQuestionsList[0]?.question ? conceptQuestionsList : [])
    const qListStr = rawQuestions.length > 0
      ? `\n   * Prepared Board Exam Checkpoint Questions for Socratic Gating (MUST ASK & SOLVE EACH):\n` +
        rawQuestions
          .map(
            (q: any, qIdx: number) => {
              const ans = q.ideal_answer || (q.options && q.correct_option_index !== undefined ? q.options[q.correct_option_index] : '') || q.explanation || ''
              const hint = q.socratic_hint || q.explanation || ''
              return `     - [Q${qIdx + 1} (${q.type || 'Checkpoint'})]: "${q.question}" [WAIT FOR STUDENT TO ANSWER — DO NOT ANSWER FOR THEM]`
            }
          )
          .join('\n')
      : ''

    // 6. Visual directive
    const conceptVisualsList = Array.isArray(visualPlan?.concept_visuals)
      ? visualPlan.concept_visuals
      : Array.isArray(activeModule?.concept_visuals)
      ? activeModule.concept_visuals
      : []
    const matchedCv = findMatchingConceptVisual(conceptVisualsList, conceptName, keyConcepts, idx)

    const hasExistingSvg = Boolean(matchedCv && (matchedCv.svg || matchedCv.diagram_svg))
    const isLegitGraph = isLegitimateGraphTopic(conceptName, resolvedSubject)
    const hasValidMathFormula = Boolean(
      matchedCv?.interactive_math_formula &&
      matchedCv.interactive_math_formula !== 'formula' &&
      matchedCv.interactive_math_formula !== 'linear' &&
      matchedCv.interactive_math_formula.trim() !== 'x'
    )
    const isGraph = Boolean(matchedCv && hasValidMathFormula && isLegitGraph)
    const isFlowchart = Boolean(matchedCv && matchedCv.diagram_type === 'draw_flowchart')
    const isImage = Boolean(matchedCv && (matchedCv.diagram_type === 'image' || matchedCv.image_url || matchedCv.image_search_query))

    let visualDirective = ''
    if (matchedCv && (hasExistingSvg || isGraph || isFlowchart || isImage)) {
      const isAnim = matchedCv.visual_type === 'animation' || /wave|current|flow|circuit|motion/i.test(matchedCv.diagram_title || '')
      const imgUrl = matchedCv.image_url || ''
      const searchQuery = matchedCv.image_search_query || matchedCv.diagram_title || conceptName
      const actionCue = isGraph && matchedCv.interactive_math_formula
        ? `plot_mathematical_graph(formula="${matchedCv.interactive_math_formula}", title="${matchedCv.diagram_title || conceptName}")`
        : isFlowchart
        ? `write_chalkboard(action="draw_flowchart", content="${matchedCv.what_to_make || conceptName}")`
        : isImage
        ? (imgUrl
            ? `write_chalkboard(action="draw_image", content="${imgUrl} | ${matchedCv.diagram_title || conceptName} | ${(matchedCv.what_to_make || conceptName).slice(0, 100)}")`
            : `search_and_show_image(query="${searchQuery}", title="${matchedCv.diagram_title || conceptName}")`)
        : `render_svg_diagram("${matchedCv.diagram_title || matchedCv.concept_title || conceptName}", caption="${matchedCv.what_to_explain || matchedCv.what_to_make || conceptName}")`

      visualDirective = `\n   * Pedagogical Visual Blueprint (${matchedCv.refined_by_tier2 ? 'Tier 2 Publication Grade' : isImage ? 'Authentic Scientific Micrograph/Image' : 'Tier 1 Blueprint'}):
     - Diagram Title: "${matchedCv.diagram_title || matchedCv.concept_title || conceptName}"
     - Visual Type: ${isGraph ? 'Interactive Coordinate Graph' : isAnim ? 'Animated Vector Visual' : isImage ? 'Authentic Micrograph / High-Res Scientific Visual' : (matchedCv.diagram_type || diagramType)}
     - Why Needed: ${matchedCv.why_needed || 'Pedagogical grounding of core principles and formulas'}
     - What to Explain Step-by-Step: ${matchedCv.what_to_explain || matchedCv.what_to_make || whatToMake || 'Point out key components, labels, and physical intuition to the student'}
     - Action Cue: Call ${actionCue}${matchedCv.interactive_math_formula ? `\n     - Interactive Coordinate Function: ${matchedCv.interactive_math_formula}` : ''}${isImage ? `\n     - Hesitation Recovery: If student hesitates, call search_and_show_image(query="${searchQuery}", title="${matchedCv.diagram_title || conceptName}")` : ''}
     - Timing Cue: ${matchedCv.timing_and_cue || 'Step 1 (Intuition) or Step 2 (Definition)'}`
    } else if (idx === 0 && chapterFlowchart) {
      visualDirective = `\n   * Mandatory Chapter Flowchart (Step 1):\n     - Action Cue: Call write_chalkboard(action="draw_flowchart", content="${chapterFlowchart}")`
    } else if (idx === 0 && whatToMake && (visualPlan?.diagram_svg || activeModule?.diagram_svg)) {
      visualDirective = `\n   * Capsule Visual:\n     - Action Cue: Call render_svg_diagram(title="${conceptName}", caption="${whatToMake.slice(0, 140)}")`
    } else {
      // Dynamic Visual Cue when diagram is missing for this concept
      const whatSpec = (matchedCv?.what_to_make || whatToMake || `Publication-grade scientific vector diagram illustrating ${conceptName} with precise components, axes, vectors, callout pointer dots, and SI unit annotations`).slice(0, 180)
      visualDirective = `\n   * Missing Diagram for Concept #${idx + 1}: Call render_svg_diagram(title="${conceptName}", what="${whatSpec}") to generate an on-demand vector diagram.`
    }

    return `Concept ${idx + 1} "${conceptName}":\n   * Core: ${q1}${defStr}${exStr}${exerciseStr}${misc ? ` [Caution: ${misc}]` : ''}${qListStr}${visualDirective}`
  }).join('\n\n')

  return `${subtopicsHeader}${flowchartSection}${conceptBlocks}${exercisesOverview}`
}

/**
 * Single-Concept Micro-Dossier Engine.
 * Gating invariant: Provides 100% textbook facts, SI units, governing equations,
 * and 4-6 authentic board-exam questions for ONLY the single active concept being taught.
 */
function buildDetailedEducationalQueries(
  conceptTitle: string,
  moduleTitle: string,
  cv?: any,
  subject: string = 'Science'
): { image_search_query: string; video_search_query: string } {
  const existingImg = (cv?.image_search_query || cv?.image_query || '').trim()
  const existingVid = (cv?.video_search_query || cv?.video_query || '').trim()

  const rawConceptTitle = conceptTitle || cv?.concept_title || ''
  const rawDiagramTitle = cv?.diagram_title || ''
  const rawWhatToMake = cv?.what_to_make || ''

  const cleanMathAndLatex = (str: string) =>
    str
      .replace(/\$[^$]*\$/g, '')
      .replace(/\\text\{([^}]+)\}/g, '$1')
      .replace(/\\\w+/g, '')
      .replace(/[\(\)\[\]\{\}]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim()

  const cleanPrefixes = (str: string) =>
    str
      .replace(/^(?:Vector diagram illustrating|Textbook diagram illustrating|Textbook diagram showing|Diagram illustrating|Diagram showing|Textbook diagram of|Diagram of|Schematic diagram of|Textbook anatomical diagram of|Interactive coordinate canvas plotting)\s*/i, '')
      .replace(/\s*(?:with precise mathematical labels and parameters|with precise components, axes, vectors|with clear labels and annotations|clearly on the chalkboard)\s*$/i, '')
      .trim()

  let baseConcept = rawConceptTitle.includes(':') 
    ? rawConceptTitle.split(':')[0].trim() 
    : (rawDiagramTitle || rawConceptTitle)
  baseConcept = cleanMathAndLatex(baseConcept).replace(/Illustrated$/i, '').trim()

  let baseDiagram = cleanMathAndLatex(rawDiagramTitle).replace(/Illustrated$/i, '').trim()
  let cleanedWhatToMake = cleanPrefixes(cleanMathAndLatex(rawWhatToMake))

  const lowerMod = (moduleTitle || '').toLowerCase()
  const lowerConcept = (rawConceptTitle + ' ' + rawDiagramTitle + ' ' + rawWhatToMake).toLowerCase()

  const isMath = lowerMod.includes('math') || lowerMod.includes('linear equation') || lowerMod.includes('hcf') || lowerMod.includes('lcm') || lowerMod.includes('polynomial') || lowerMod.includes('quadratic') || lowerMod.includes('triangle') || lowerMod.includes('circle') || lowerMod.includes('coordinate') || lowerMod.includes('arithmetic') || lowerMod.includes('statistics') || lowerMod.includes('probability') || lowerMod.includes('surface area') || lowerMod.includes('volume') || lowerMod.includes('trigonometr')

  const isCircuit = lowerConcept.includes('circuit') || (lowerConcept.includes('current') && (lowerConcept.includes('ammeter') || lowerConcept.includes('resistor') || lowerConcept.includes('switch')))

  let imgQuery = existingImg
  let vidQuery = existingVid

  // Video Search: Mandate "animated short video showing animation to understand" across all classes and subjects
  if (vidQuery && !/animated short video|animation to understand/i.test(vidQuery)) {
    vidQuery = `animated short video showing animation to understand ${vidQuery}`
  }

  // Image Search: Ensure textbook diagram with labeled parts
  if (imgQuery && !/diagram|labeled|labelled/i.test(imgQuery)) {
    imgQuery = `${imgQuery} textbook diagram with labeled parts`
  }

  if (!imgQuery || !vidQuery) {
    if (isCircuit) {
      let circuitDetails = cleanedWhatToMake || baseDiagram
      if (/circuit diagram with/i.test(circuitDetails)) {
        imgQuery = imgQuery || `${circuitDetails}, ammeter, voltmeter, switch, and current direction arrows`
      } else {
        imgQuery = imgQuery || `electric circuit diagram of ${baseDiagram} with battery, ammeter, resistors, switch, and current direction arrows`
      }
      vidQuery = vidQuery || `animated short video showing animation to understand ${baseDiagram} electric circuit connection and current flow`
    } else if (isMath) {
      const mathTopic = baseDiagram || baseConcept
      imgQuery = imgQuery || `${subject || 'Mathematics'} ${mathTopic} step by step textbook diagram with labeled points coordinates and geometric proof`
      vidQuery = vidQuery || `animated short video showing animation to understand ${mathTopic} concept mathematics`
    } else {
      let descriptiveCore = cleanedWhatToMake
      if (!descriptiveCore || descriptiveCore.length < 10) {
        descriptiveCore = baseDiagram || baseConcept
      }
      imgQuery = imgQuery || `${descriptiveCore} textbook educational diagram with labeled parts and clear annotations`
      vidQuery = vidQuery || `animated short video showing animation to understand ${baseDiagram || baseConcept}`
    }
  }

  imgQuery = imgQuery.replace(/\s+/g, ' ').replace(/\.{2,}/g, '.').trim()
  vidQuery = vidQuery.replace(/\s+/g, ' ').replace(/\.{2,}/g, '.').trim()

  return {
    image_search_query: imgQuery,
    video_search_query: vidQuery
  }
}

function buildSingleConceptMicroDossier(
  conceptIdx: number,
  keyConcepts: string[],
  activeModule: any,
  resolvedBoard: string,
  resolvedClassLevel: string,
  resolvedSubject: string,
  chapterName: string,
  workedExamples: any[],
  misconceptions: string[],
  chapterNumber?: number | string
): string {
  if (!keyConcepts || keyConcepts.length === 0 || conceptIdx < 0 || conceptIdx >= keyConcepts.length) {
    return ''
  }

  const rawConcept = keyConcepts[conceptIdx]
  const conceptName = rawConcept.replace(/^[\s\(\[\{]+|[\s\)\]\}]+$/g, '').trim()
  const visualPlan = activeModule?.visual_lesson_plan || {}
  const textbookDefs: any[] = visualPlan?.textbook_definitions || activeModule?.textbook_definitions || []
  const textbookExamples: any[] = visualPlan?.textbook_examples || activeModule?.textbook_examples || []
  const textbookExercises: any[] = visualPlan?.textbook_exercises || activeModule?.textbook_exercises || []
  const subtopics: string[] = activeModule?.subtopics?.length ? activeModule.subtopics : (visualPlan?.subtopics || [])
  const diagramType = visualPlan?.diagram_type || activeModule?.diagram_type || 'vector_svg_diagram'
  const whatToMake = visualPlan?.what_to_make || visualPlan?.diagram_description || activeModule?.what_to_make || ''
  const resolvedChNum = chapterNumber || extractChapterNumber(String(chapterName || activeModule?.title || '')) || 1

  // Subtopics matching this concept strictly by token overlap (never blind index to unrelated subtopic)
  const conceptStemTokens = tokenizeForMatch(conceptName)
  const matchingSubtopics = subtopics.filter((st: string) => {
    const sLow = st.toLowerCase()
    if (sLow.includes(conceptName.toLowerCase()) || conceptName.toLowerCase().includes(sLow)) return true
    return conceptStemTokens.some((tok) => sLow.includes(tok))
  })
  const subtopicsStr = matchingSubtopics.length > 0
    ? `\n   * Key Examination Subtopics for this Concept:\n` + matchingSubtopics.map((st) => `     - ${st}`).join('\n')
    : ''

  const isMathSubject = /math|algebra|geometry|calculus|trigonometry|statistics|probability/i.test(
    String(resolvedSubject || chapterName || '')
  )

  // Definitions / Core Concepts
  const matchingDefs = Array.isArray(textbookDefs)
    ? textbookDefs.filter(
        (d: any) =>
          (d.concept || '').toLowerCase().includes(conceptName.toLowerCase()) ||
          conceptName.toLowerCase().includes((d.concept || '').toLowerCase())
      )
    : []
  const defToUse = matchingDefs.length > 0 ? matchingDefs : (textbookDefs[conceptIdx] ? [textbookDefs[conceptIdx]] : [])
  const defLabel = isMathSubject ? 'Core Mathematical Concept / Property' : 'Verbatim Textbook Definition'
  const defStr = defToUse.length > 0
    ? defToUse.map((d: any) => `\n   * ${defLabel}: "${d.definition}" ${d.si_units ? `[SI Unit: ${d.si_units}]` : ''}`).join('')
    : ''

  // Concrete Scenarios
  const matchingExamples = Array.isArray(textbookExamples)
    ? textbookExamples.filter(
        (e: any) =>
          (e.title || '').toLowerCase().includes(conceptName.toLowerCase()) ||
          conceptName.toLowerCase().includes((e.title || '').toLowerCase()) ||
          (e.scenario || '').toLowerCase().includes(conceptName.toLowerCase())
      )
    : []
  const exToUse = matchingExamples.length > 0 ? matchingExamples : (textbookExamples[conceptIdx] ? [textbookExamples[conceptIdx]] : [])
  const exStr = exToUse.length > 0
    ? `\n   * Textbook Real-Life Scenarios / Concrete Illustrations:\n` +
      exToUse.map((e: any) => `     - "${e.title}": ${e.scenario}`).join('\n')
    : ''

  // Exercises (keyword overlap + proportional partition fallback; zero truncation; explicit Exercise X.Y • Q.N tags)
  const conceptTokens = conceptName
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, ' ')
    .split(/\s+/)
    .filter((w) => w.length >= 3 && !['the', 'and', 'for', 'with', 'into', 'from', 'using', 'concept'].includes(w))
  const allExQuestions = textbookExercises.flatMap((ex: any) =>
    (ex.questions || []).map((q: any) => ({ ...q, exercise_number: ex.exercise_number, exercise_title: ex.exercise_title }))
  )
  const directMatchedExercises = allExQuestions.filter((q: any) => {
    const hay = `${q.question || ''} ${q.solution_method || ''} ${q.exercise_title || ''}`.toLowerCase()
    if (hay.includes(conceptName.toLowerCase())) return true
    return conceptTokens.some((tok) => hay.includes(tok))
  })
  const perConceptSlice = allExQuestions.length > 0 && keyConcepts.length > 0
    ? Math.max(1, Math.ceil(allExQuestions.length / keyConcepts.length))
    : 0
  const matchingExercises = directMatchedExercises.length > 0
    ? directMatchedExercises
    : allExQuestions.slice(conceptIdx * perConceptSlice, (conceptIdx + 1) * perConceptSlice)
  const exerciseStr = matchingExercises.length > 0
    ? `\n   * Linked Textbook In-Text / Board Exercises (MUST solve on board showing Exercise X.Y • Q.N clearly; never advance past taught concepts without completing these):\n` +
      matchingExercises.map((q: any) => {
        const figExCue = (q.figure_id || q.image_url)
          ? ` [TEXTBOOK FIGURE: Direct student to Side Book Viewer: "Look at ${q.figure_id || 'the diagram'} in your textbook in the side viewer" — DO NOT draw or extract book images onto the chalkboard; the chalkboard is strictly reserved for live math steps, formulas, and pure vector graphs.]`
          : ''
        return `     - [Exercise ${q.exercise_number || '1'} • Q.${q.q_num || '1'}]: ${q.question}${figExCue}${q.solution_method ? ` (Solve: ${q.solution_method})` : ''}`
      }).join('\n')
    : ''

  // Model problem matched strictly to this active concept (never inject unrelated formulas from other concepts)
  const ex1 = findMatchingWorkedExample(workedExamples, conceptName, keyConcepts, conceptIdx)
  const figPrompt = (ex1?.figure_id || ex1?.image_url)
    ? ` [TEXTBOOK FIGURE: Direct student to Side Book Viewer: "Look at ${ex1.figure_id || 'the diagram'} in your textbook in the side viewer" — DO NOT draw or extract book images onto the chalkboard; the chalkboard is strictly reserved for live math steps, formulas, and pure vector graphs.]`
    : ''
  const q1 = ex1?.problem
    ? `Model Problem: "${ex1.problem}"${figPrompt} (Given: ${ex1.given || ''}, Formula: ${ex1.formula || ''}, Substitution: ${ex1.substitution || ''}, Ans: ${ex1.finalAnswer || ''} ${ex1.unit || ''})`
    : `Practice Focus: Teach ONLY "${conceptName}" cleanly with your own freshly generated everyday analogy and worked example tailored to ${resolvedClassLevel} ${resolvedBoard}. Do NOT invent exercise numbers outside Chapter ${resolvedChNum}.`

  // Misconception matched strictly if relevant
  const misc = misconceptions.find((m) =>
    conceptStemTokens.some((tok) => String(m || '').toLowerCase().includes(tok))
  ) || ''
  const miscStr = misc ? `\n   * Common Student Pitfall / Caution: "${misc}"` : ''

  // Prepared 4-6 questions for socratic gating
  const conceptQuestionsList = Array.isArray(visualPlan?.concept_questions)
    ? visualPlan.concept_questions
    : Array.isArray(activeModule?.concept_questions)
    ? activeModule.concept_questions
    : []
  const matchingQuestions =
    conceptQuestionsList.find(
      (cq: any) =>
        cq.concept_index === conceptIdx ||
        (cq.concept_title || '').toLowerCase().includes(conceptName.toLowerCase()) ||
        conceptName.toLowerCase().includes((cq.concept_title || '').toLowerCase())
    ) || conceptQuestionsList[conceptIdx]
  const rawQuestions = matchingQuestions?.questions?.length
    ? matchingQuestions.questions
    : (conceptQuestionsList.length > 0 && conceptQuestionsList[0]?.question ? conceptQuestionsList : [])
  const qListStr = rawQuestions.length > 0
    ? `\n   * Prepared Authentic Board Exam Questions for Gating (MUST ASK & SOLVE EACH):\n` +
      rawQuestions
        .map(
          (q: any, qIdx: number) => {
            const ans = q.ideal_answer || (q.options && q.correct_option_index !== undefined ? q.options[q.correct_option_index] : '') || q.explanation || ''
            const hint = q.socratic_hint || q.explanation || ''
            const figCue = (q.figure_id || q.image_url)
              ? ` [TEXTBOOK FIGURE: Direct student to Side Book Viewer: "Look at ${q.figure_id || 'the diagram'} in your textbook in the side viewer" — DO NOT draw or extract book images onto the chalkboard; the chalkboard is strictly reserved for live math steps, formulas, and pure vector graphs.]`
              : ''
            return `     - [Q${qIdx + 1} (${q.type || 'Checkpoint'})]: "${q.question}"${figCue} [WAIT FOR STUDENT TO ANSWER — DO NOT ANSWER FOR THEM]`
          }
        )
        .join('\n')
    : ''

  // Visual Directive matched strictly for this single concept
  const conceptVisualsList = Array.isArray(visualPlan?.concept_visuals)
    ? visualPlan.concept_visuals
    : Array.isArray(activeModule?.concept_visuals)
    ? activeModule.concept_visuals
    : []
  const matchedCv = findMatchingConceptVisual(conceptVisualsList, conceptName, keyConcepts, conceptIdx)

  const isLegitimateGraph = isLegitimateGraphTopic(conceptName, resolvedSubject)
  const hasValidMathFormula = Boolean(
    matchedCv?.interactive_math_formula &&
    matchedCv.interactive_math_formula !== 'formula' &&
    matchedCv.interactive_math_formula !== 'linear' &&
    matchedCv.interactive_math_formula.trim() !== 'x'
  )
  const isGraph = Boolean(
    matchedCv &&
    hasValidMathFormula &&
    isLegitimateGraph
  )
  const isFlowchart = Boolean(matchedCv && matchedCv.diagram_type === 'draw_flowchart')
  const diagramTitle = matchedCv?.diagram_title || matchedCv?.concept_title || conceptName
  const whatSpec = matchedCv?.what_to_make || whatToMake || `Publication-grade scientific vector diagram illustrating ${conceptName} with precise components, axes, vectors, callout pointer dots, and SI unit annotations`

  const { image_search_query: fullImgQuery, video_search_query: fullVidQuery } = buildDetailedEducationalQueries(
    conceptName,
    chapterName || activeModule?.title || '',
    matchedCv,
    resolvedSubject
  )

  let visualDirective = ''
  if (isGraph && matchedCv?.interactive_math_formula) {
    visualDirective = `\n   * MATHEMATICAL/KINEMATIC GRAPH: When plotting coordinate functions or kinematics, call plot_mathematical_graph(formula="${matchedCv.interactive_math_formula}", title="${diagramTitle}") with actual key points or bounded stopping segments! NEVER output a line passing from origin without points or stopping segments. If a diagram is needed, use render_svg_diagram or search_and_show_image.`
  } else if (isFlowchart) {
    visualDirective = `\n   * MANDATORY FLOWCHART: Call write_chalkboard(action="draw_flowchart", content="${matchedCv?.what_to_make || conceptName}") on Step 1!`
  } else {
    // Image-First visual flow: start with ONE clean diagram (or plotted graph when quantitative); unlock video / extra visuals ONLY on confusion, doubt, or request
    visualDirective = `\n   * IMAGE-FIRST CONCEPT VISUALS (NO UNPROMPTED VIDEO AT STARTUP):
     1. Call search_and_show_image(query="${fullImgQuery}", title="${diagramTitle}", caption="Visual illustration")${isLegitimateGraphTopic(conceptName, resolvedSubject) ? ` OR plot_mathematical_graph(..., title="${diagramTitle}")` : ''} ON YOUR VERY FIRST TURN so the student immediately sees ONE clean visual on the board.
     2. Do NOT call search_and_show_video on Turn 1 unless the student asks for a video or gets stuck/confused later.
     3. ONLY if the student expresses confusion ("I didn't understand", "samajh nahi aaya"), asks to explain again, or asks for a video/more visuals, IMMEDIATELY unlock search_and_show_video(query="${fullVidQuery}", title="${diagramTitle}", description="Demonstration video") or extra diagrams/graphs/shapes to explain simply!
   * MANDATORY GRAPH & SHAPE CALL (WHEN EXPLAINING OR SOLVING):
     - If this concept or any question/worked-example involves coordinate geometry, circles, triangles, functions, kinematics (s-t, v-t, a-t), Ohm's law (V-I), thermodynamics (P-V), statistics (bar graphs, histograms), vectors, or bounded line segments: CALL plot_mathematical_graph(...) or write_chalkboard(action="draw_shape", ...) to visualize it interactively!
   * VECTOR SVG FALLBACK: If an authentic web image is unavailable, call render_svg_diagram(title="${diagramTitle}", what="${whatSpec.slice(0, 160)}").`
  }

  return `========================================================================================
CURRENT ACTIVE CONCEPT: Concept ${conceptIdx + 1} of ${keyConcepts.length}: "${conceptName}"
========================================================================================
${subtopicsStr}${defStr}${exStr}${exerciseStr}
   * ${q1}${miscStr}${qListStr}
${visualDirective}
`
}

/**
 * Natural language detector for spoken concept transitions by the AI tutor.
 * Detects phrases like: "Moving on to Concept 2", "Let's move to Concept 3",
 * "Now moving to Concept 2", "Moving on to cellulose", "Let's talk about cellulose", etc.
 */
function detectSpokenConceptTransition(
  text: string,
  keyConcepts: string[]
): { targetIdx: number; conceptTitle: string } | null {
  if (!text || keyConcepts.length === 0) return null

  // 1. Direct number match: e.g. "moving on to concept 2", "let's talk about concept 2", "now on to concept 2", "advance to concept 2"
  const numMatch = text.match(
    /(?:moving\s+(?:on\s+)?to|let['’]?s\s+(?:move\s+(?:on\s+)?to|talk\s+about|discuss|begin|start|advance\s+to|proceed\s+to|go\s+to)|now\s+(?:moving\s+to|on\s+to|for|let['’]?s\s+look\s+at)|turn(?:ing)?\s+(?:our\s+attention\s+)?to|next\s+(?:is|up\s+is|concept\s+is)|welcome\s+to|starting|onto|in|advance\s+to|proceed\s+to)\s+concept\s*#?\s*(\d+)/i
  ) || text.match(/\bconcept\s*#?\s*(\d+)\s*(?:is\s+next|next)\b/i)
  if (numMatch && numMatch[1]) {
    const num = parseInt(numMatch[1], 10)
    if (num >= 1 && num <= keyConcepts.length) {
      return { targetIdx: num - 1, conceptTitle: keyConcepts[num - 1] }
    }
  }

  // 2. Ordinal word match: e.g. "moving on to the second concept", "second concept"
  const ordinals: Record<string, number> = {
    first: 1,
    second: 2,
    third: 3,
    fourth: 4,
    fifth: 5,
    sixth: 6,
    seventh: 7,
    eighth: 8,
    ninth: 9,
    tenth: 10,
  }
  const ordinalMatch = text.match(
    /(?:moving\s+(?:on\s+)?to|let['’]?s\s+(?:move\s+(?:on\s+)?to|advance\s+to|proceed\s+to)|now\s+moving\s+to|next\s+is)\s+(?:the\s+)?([a-z]+)\s+concept/i
  )
  if (ordinalMatch && ordinalMatch[1]) {
    const word = ordinalMatch[1].toLowerCase()
    if (ordinals[word] && ordinals[word] <= keyConcepts.length) {
      const idx = ordinals[word] - 1
      return { targetIdx: idx, conceptTitle: keyConcepts[idx] }
    }
  }

  // 3. Keyword / topic title match: e.g. "moving on to cellulose", "let's talk about cellulose"
  for (let i = 0; i < keyConcepts.length; i++) {
    const c = keyConcepts[i]
    // Filter significant topic words (length >= 4)
    const words = c
      .toLowerCase()
      .replace(/[^a-z0-9\s]/g, ' ')
      .split(/\s+/)
      .filter((w) => w.length >= 4 && !['what', 'with', 'from', 'this', 'that', 'about', 'basic', 'types', 'cell'].includes(w))
    for (const word of words) {
      const isUnique = !keyConcepts.some((other, oIdx) => oIdx !== i && other.toLowerCase().includes(word))
      if (isUnique) {
        const pattern = new RegExp(
          `(?:moving\\s+(?:on\\s+)?to|let['’]?s\\s+(?:move\\s+to|talk\\s+about|discuss|advance\\s+to)|now\\s+(?:on\\s+to|for)|turn(?:ing)?\\s+to|next\\s+up\\s+is)\\s+${word}`,
          'i'
        )
        if (pattern.test(text)) {
          return { targetIdx: i, conceptTitle: keyConcepts[i] }
        }
      }
    }
  }

  return null
}

/**
 * Natural language detector for spoken concept completion by the AI tutor.
 * Detects phrases like: "We have finished Concept 1", "Concept 1 is complete",
 * "That concludes Concept 1", "That covers Concept 1", "That wraps up this concept", etc.
 */
function detectSpokenConceptCompletion(
  text: string,
  keyConcepts: string[],
  currentIdx: number
): { conceptIdx: number; conceptTitle: string } | null {
  if (!text || keyConcepts.length === 0) return null

  // 1. Direct number completion: e.g. "concept 1 is complete", "we have finished concept 1", "that concludes concept 1"
  const compMatch = text.match(
    /(?:(?:we\s+have\s+|we've\s+)?(?:completed|finished|concluded|covered|wrapped\s+up)|that\s+(?:completes|concludes|covers|wraps\s+up))\s+(?:the\s+)?concept\s*#?\s*(\d+)/i
  ) || text.match(/\bconcept\s*#?\s*(\d+)\s*(?:is|has\s+been)\s*(?:completed|done|finished|mastered)/i)

  if (compMatch && compMatch[1]) {
    const num = parseInt(compMatch[1], 10)
    if (num >= 1 && num <= keyConcepts.length) {
      return { conceptIdx: num - 1, conceptTitle: keyConcepts[num - 1] }
    }
  }

  // 2. Generic "this concept is complete" / "that concludes this concept"
  const thisConceptMatch = text.match(
    /(?:(?:we\s+have\s+|we've\s+)?(?:completed|finished|concluded|wrapped\s+up)|that\s+(?:completes|concludes|wraps\s+up))\s+(?:this\s+concept|this\s+topic)/i
  )
  if (thisConceptMatch && currentIdx >= 0 && currentIdx < keyConcepts.length) {
    return { conceptIdx: currentIdx, conceptTitle: keyConcepts[currentIdx] }
  }

  return null
}

export default function ModuleClassroomPage() {
  const router = useRouter()
  const params = useParams()
  const userId = params.id as string
  const moduleId = params.moduleId as string

  const {
    connectionState,
    isMuted,
    errorMessage,
    transcripts,
    teacherVolume,
    userVolume,
    teacherVolumeRef,
    userVolumeRef,
    selectedVoice,
    setSelectedVoice,
    latestVideoFrame,
    videoMimeType,
    activeHighlight,
    startClass,
    toggleMute,
    setTeacherAudioMuted,
    pauseClass,
    resumeClass,
    endCall,
    resetToIdle,
    sendBoardContext,
    sendTextMessage,
    setAwaitingStudentAnswer,
    pedagogicalStateManager,
  } = useGeminiLive()

  const transcriptsRef = useRef(transcripts)
  transcriptsRef.current = transcripts
  const isMutedRef = useRef(isMuted)
  isMutedRef.current = isMuted
  const hasUserRespondedSinceQuestionRef = useRef<boolean>(true)

  const leaveTo = (path: string) => {
    endCall()
    router.refresh()
    if (!path || path.includes('undefined') || path.includes('null')) {
      router.push(`/dashboard/${userId}`)
      return
    }
    router.push(path)
  }

  const [selectedPyqQuestion, setSelectedPyqQuestion] = useState<string | null>(null)

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const searchParams = new URLSearchParams(window.location.search)
      const q = searchParams.get('pyqQuestion')
      if (q) setSelectedPyqQuestion(decodeURIComponent(q))
    }
  }, [])

  // User Quota & Avatar configuration
  const [isAvatarEnabled, setIsAvatarEnabled] = useState<boolean>(true)
  const [userQuota, setUserQuota] = useState<{
    limit_type: 'requests' | 'modules' | 'unlimited'
    max_requests: number
    used_requests: number
    max_modules: number
    used_modules: number
  }>({
    limit_type: 'unlimited',
    max_requests: 100,
    used_requests: 0,
    max_modules: 5,
    used_modules: 0,
  })

  // Google Gemini 3.8 Live Avatar configuration state
  const [avatarConfig, setAvatarConfig] = useState<LiveAvatarConfig | null>(null)
  const simliControllerRef = useRef<SimliAvatarController | null>(null)
  const saveNotesToSupabaseRef = useRef<((notes: string, forcedStatus?: 'in_progress' | 'completed') => Promise<void>) | null>(null)

  useEffect(() => {
    if (typeof window !== 'undefined') {
      try {
        const saved = localStorage.getItem('ai_tutor_avatar_config')
        if (saved) {
          setAvatarConfig(JSON.parse(saved))
        }
      } catch {}
    }
  }, [])

  const handleCustomAvatarChange = useCallback((cfg: LiveAvatarConfig | null) => {
    setAvatarConfig((prev) => {
      if (prev === cfg) return prev
      if (!prev && !cfg) return prev
      if (
        prev &&
        cfg &&
        prev.avatarName === cfg.avatarName &&
        prev.customizedAvatar?.imageData === cfg.customizedAvatar?.imageData
      ) {
        return prev
      }
      return cfg
    })
  }, [])

  const handleSimliControllerReady = useCallback((ctrl: SimliAvatarController | null) => {
    simliControllerRef.current = ctrl
  }, [])

  const handleSimliActiveChange = useCallback(
    (active: boolean) => {
      setTeacherAudioMuted(active)
    },
    [setTeacherAudioMuted]
  )

  const handleBoardContentChange = useCallback(
    (summary: { notesText: string; roughText: string; fullSummary: string }) => {
      const fullNotesContent = (summary.fullSummary || summary.notesText || '').trim()
      setLatestBoardSummary((prev) => (prev === summary.fullSummary ? prev : summary.fullSummary))

      // Sync compact board context to live AI tutor (safely buffered if tutor is currently speaking)
      const compactContext = chalkboardRef.current?.getCompactBoardContext?.()
      if (compactContext) {
        sendBoardContext(compactContext)
      }

      if (!fullNotesContent || fullNotesContent === lastSentBoardNotesRef.current) return
      lastSentBoardNotesRef.current = fullNotesContent
      setChapterNotes(fullNotesContent)

      // 1. Instant client-side cache write (0ms, zero DB load)
      if (userId && moduleId) {
        setCachedBoardNotes({
          userId,
          moduleId,
          notesText: summary.notesText,
          roughText: summary.roughText,
          fullSummary: summary.fullSummary,
          updatedAt: new Date().toISOString(),
          isDirty: true,
        })
      }

      // 2. Batch and debounce saves with 4-second idle window to persist chalkboard notes promptly
      setNotesSaveStatus('saving')
      if (saveTimeoutRef.current) {
        clearTimeout(saveTimeoutRef.current)
      }
      saveTimeoutRef.current = setTimeout(() => {
        saveNotesToSupabaseRef.current?.(fullNotesContent)
      }, 4000)
    },
    [userId, moduleId]
  )

  // Interactive page flip barrier: prevents premature page flips until student replies to checkpoint question
  const isAwaitingStudentAnswerRef = useRef<boolean>(false)
  const [isAwaitingStudentAnswer, setIsAwaitingStudentAnswer] = useState<boolean>(false)

  // Verdict review barrier: locks whiteboard on current page until student confirms understanding
  const isReviewingVerdictRef = useRef<boolean>(false)
  const [isReviewingVerdict, setIsReviewingVerdict] = useState<boolean>(false)
  const lastVerdictStatusRef = useRef<'correct' | 'incorrect' | 'neutral'>('neutral')

  // Mafs.dev high-precision dynamic mathematical & scientific graph state
  const [activeGraph, setActiveGraph] = useState<MafsGraphCanvasProps | null>(null)

  // Docked Textbook SideBookViewer State (Clean Zero-Bloat Ponytail UI)
  const [isBookOpen, setIsBookOpen] = useState<boolean>(false)
  const [bookPdfUrl, setBookPdfUrl] = useState<string | null>(null)
  const [bookCurrentPage, setBookCurrentPage] = useState<number>(1)
  const [bookTotalPages, setBookTotalPages] = useState<number | undefined>(undefined)
  const [bookChapterTitle, setBookChapterTitle] = useState<string | undefined>(undefined)
  const bookTotalPagesRef = useRef<number | undefined>(undefined)
  const bookPdfUrlRef = useRef<string | null>(null)
  bookTotalPagesRef.current = bookTotalPages
  bookPdfUrlRef.current = bookPdfUrl

  // Whiteboard on-demand diagram generation progress tracker
  const [generatingDiagramTitle, setGeneratingDiagramTitle] = useState<string | null>(null)

  // Background pre-fetched scientific images cache for instant concept mounting
  const [prefetchedImages, setPrefetchedImages] = useState<Record<number, { url: string; title: string; caption?: string }>>({})
  const prefetchedImagesRef = useRef<Record<number, { url: string; title: string; caption?: string }>>({})
  prefetchedImagesRef.current = prefetchedImages
  const [verifiedAssetsDirectives, setVerifiedAssetsDirectives] = useState<string>('')
  const handleConceptDoneRef = useRef<(conceptName?: string) => void>(() => {})

  // Helper to detect if student statement is an EXPLICIT command to advance to the next concept/page
  const isExplicitNextConceptIntent = (text: string): boolean => {
    if (!text) return false
    const clean = text.toLowerCase().trim().replace(/[.,!?;:'"()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim()
    if (!clean) return false

    // Explicit single-phrase advancement commands
    const explicitCommands = new Set([
      'next', 'next concept', 'next page', 'next topic', 'next question', 'next one',
      'move', 'move on', 'move ahead', 'move forward', 'move to next', 'move to next concept', 'move to the next concept',
      'advance', 'advance to next', 'advance to next concept', 'go to next', 'go to next concept', 'skip to next concept',
      'continue', 'proceed', 'lets proceed', "let's proceed", 'lets continue', "let's continue",
      'ready for next', 'ready to move', 'ready to move on',
      'understood next', 'understood next concept', 'understood move on', 'understood move ahead',
      'yes next', 'done next', 'yes understood next', 'all clear next', 'samajh gaya next',
      'aage badho', 'aage chalo', 'chalo aage', 'aage badho agle concept pe',
      'agle concept pe chalo', 'agle concept pe aao', 'agle topic pe chalo', 'agle pe chalo',
      'move to next page', 'turn the page',
    ])
    if (explicitCommands.has(clean)) return true

    // Must explicitly contain "next concept", "next page", "move to next", etc.
    const explicitPatterns = [
      /\b(?:move|go|advance|proceed|step|skip)\s*(?:on\s*|ahead\s*|forward\s*)?(?:to\s*)?(?:the\s*)?next\s*(?:concept|page|topic|question)?\b/i,
      /\bnext\s*(?:concept|page|topic|question|one)\b/i,
      /\b(?:ready|prepared)\s*(?:for|to\s*move\s*to)\s*(?:the\s*)?next\s*(?:concept|page|topic)?\b/i,
      /\b(?:aage|agle|agle\s*wale)\s*(?:concept|topic|page)?\s*(?:pe|par)?\s*(?:chalo|badho|aao|continue)\b/i,
      /\b(?:understood|samajh\s*aaya|samajh\s*aa\s*gaya)\b.*\b(?:next|aage|move)\b/i,
    ]
    return explicitPatterns.some((p) => p.test(clean))
  }

  // Helper to detect if student statement is confirming understanding or requesting next concept
  const isConfirmationOrNextIntent = (text: string): boolean => {
    if (!text) return false
    const clean = text.toLowerCase().trim().replace(/[.,!?;:'"()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim()
    if (!clean) return false

    // If student mentions doubt, question, or asks to repeat/re-explain, NEVER treat as confirmation!
    if (isStudentQuestionOrDoubt(clean) || isRepeatIntent(clean) || isDontUnderstandIntent(clean)) {
      return false
    }

    const exactAffirmations = new Set([
      'yes', 'yeah', 'yep', 'yup', 'sure', 'ok', 'okay', 'alright', 'fine', 'correct',
      'understood', 'i understood', 'i understand', 'yes understood', 'yes i understood',
      'got it', 'i got it', 'yes got it', 'clear', 'all clear', 'it is clear', 'its clear',
      'crystal clear', 'doubts clear', 'no doubts', 'no doubt', 'zero doubts',
      'ready', 'i am ready', 'im ready', 'ready for next', 'ready to move on',
      'next', 'next concept', 'next page', 'move on', 'move to next', 'move to next concept',
      'move to the next concept', 'advance', 'advance to next', 'advance to next concept',
      'continue', 'proceed', 'go to next', 'go to next concept',
      'haan', 'haanji', 'samajh gaya', 'samajh aa gaya', 'theek hai', 'bilkul', 'aage badho',
      'done', 'concept done',
    ])

    if (exactAffirmations.has(clean)) return true

    // If student provides an explanatory answer starting with yes (e.g. "yes because velocity is zero")
    if (/\b(?:because|since|due to|as\s+\w+|when\s+\w+|where\s+\w+)\b/i.test(clean) && !/\b(?:next|advance|move\s*on|understood|clear|no\s*doubts?)\b/i.test(clean)) {
      return false
    }

    const patterns = [
      /\b(?:move|go|advance|proceed|step)\s*(?:on\s*)?(?:to\s*)?(?:the\s*)?next\b/i,
      /\bnext\s*(?:concept|page|topic|chapter|lesson|question)\b/i,
      /\b(?:i\s*)?(?:have\s*)?understood\b/i,
      /\b(?:i\s*)?(?:got\s*it|understand)\b/i,
      /\b(?:it\s*is|its|everything\s*is)?\s*(?:crystal\s*)?clear\b/i,
      /\b(?:no|zero|without\s*any)\s*doubts?\b/i,
      /\b(?:ready|prepared)\s*(?:for|to\s*move\s*to)\s*(?:the\s*)?next\b/i,
      /\b(?:samajh\s*gaya|samajh\s*aa\s*gaya|aage\s*chalo|aage\s*badho)\b/i,
      /^(?:yes|yeah|yep|yup|sure|ok|okay)(?:\s+(?:sir|teacher|ma'?am|sobi|tutor|please|now))?$/i,
      /^(?:yes|yeah|yep|yup|sure|ok|okay),?\s*(?:please\s*)?(?:move|continue|proceed|next|advance|understood|clear|i\s*understood|all\s*clear)/i,
      /(?:understood|clear|got\s*it)[\s\w]*\b(?:move|next|advance|continue|proceed)\b/i,
    ]

    return patterns.some((p) => p.test(clean))
  }

  // Helper to detect if student statement is asking a question or expressing doubt/confusion
  const isStudentQuestionOrDoubt = (text: string): boolean => {
    if (!text) return false
    const clean = text.toLowerCase().trim().replace(/[.,!;:()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim()
    if (!clean) return false
    if (text.includes('?')) return true

    const questionPatterns = [
      /\b(?:why|what|how|when|where|who|which)\b/i,
      /\b(?:can|could|will|would)\s+(?:you|we)\b/i,
      /\b(?:is|are|does|do|did|was|were)\s+(?:it|this|that|there)\b/i,
      /\b(?:explain|repeat|clarify|elaborate)\b/i,
      /\b(?:doubt|doubts|douth|douts|dought|daoubt|daot|shanka|confusion|confused|unclear)\b/i,
      /\b(?:not\s*sure|don't\s*get|didn't\s*get|did\s*not\s*get|don't\s*understand|didn't\s*understand)\b/i,
      /\b(?:help\s*me|once\s*more|one\s*more\s*time|again)\b/i,
      /\b(?:kya|kyun|kyu|kaise|kab|kahan|kaun)\b/i,
      /\b(?:samajh\s*nahi\s*aaya|samajh\s*na\s*aaya|dobara|phir\s*se|batao|samjha\s*do|samjhao)\b/i,
      /\b(?:wait|hold\s*on|what\s*if)\b/i,
      /\b(?:explain\s*(?:the\s*)?(?:whole|entire|full|all|complete)?\s*concept\s*again)\b/i,
      /\b(?:explain\s*(?:it\s*|this\s*)?again|teach\s*(?:it\s*|this\s*)?again)\b/i,
      /\b(?:pura\s*concept\s*samjhao|pura\s*samjhao|dobara\s*samjhao|phir\s*se\s*samjhao)\b/i,
      /\b(?:teach\s*(?:this|it|again)|shuru\s*se\s*samjhao|start\s*(?:from\s*)?again)\b/i,
      /\b(?:i\s*have\s*a\s*(?:doubt|douth|question)|have\s*(?:a\s*)?(?:doubt|douth)|ek\s*doubt)\b/i,
    ]
    return questionPatterns.some((p) => p.test(clean))
  }

  // Conversational Intent Classifiers (Student-Controlled Teaching & Pedagogy)
  const isSolveItIntent = (text: string): boolean => {
    if (!text) return false
    const clean = text.toLowerCase().trim().replace(/[.,!?:;()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim()
    const patterns = [
      /\b(?:solve\s*it|solve\s*this|please\s*solve|can\s*you\s*solve|solve\s*karo|solve\s*kar\s*do|aap\s*solve\s*karo|solve\s*karein)\b/i,
      /\b(?:hal\s*kijiye|hal\s*karo|hal\s*kar\s*do|hal\s*karein)\b/i,
      /\b(?:solution\s*please|show\s*(?:the\s*)?solution|give\s*(?:me\s*)?(?:the\s*)?solution|iska\s*solution\s*batao)\b/i,
      /\b(?:answer\s*bata\s*do|answer\s*batao|tell\s*(?:me\s*)?(?:the\s*)?answer|show\s*answer)\b/i,
      /^(?:solve|solution)$/i,
    ]
    return patterns.some((p) => p.test(clean))
  }

  const isGiveHintIntent = (text: string): boolean => {
    if (!text) return false
    const clean = text.toLowerCase().trim().replace(/[.,!?:;()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim()
    const patterns = [
      /\b(?:give\s*(?:me\s*)?(?:a\s*)?hint|hint\s*please|can\s*i\s*get\s*a\s*hint|need\s*a\s*hint|any\s*hint)\b/i,
      /\b(?:kuch\s*hint\s*do|hint\s*do|thoda\s*hint\s*do|hint\s*chahiye|clue\s*please|give\s*a\s*clue)\b/i,
      /\b(?:help\s*me\s*start|how\s*to\s*start|where\s*to\s*start)\b/i,
      /^hint$/i,
    ]
    return patterns.some((p) => p.test(clean))
  }

  const isExplainStepByStepIntent = (text: string): boolean => {
    if (!text) return false
    const clean = text.toLowerCase().trim().replace(/[.,!?:;()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim()
    const patterns = [
      /\b(?:explain\s*step\s*by\s*step|step\s*by\s*step\s*explain|explain\s*(?:this|it|in\s*detail))\b/i,
      /\b(?:detail\s*me\s*samjha\s*do|step\s*by\s*step\s*batao|pura\s*explain\s*karo|samjhao)\b/i,
      /\b(?:can\s*you\s*explain|please\s*explain|samjha\s*do|kaise\s*aaya|how\s*did\s*this\s*come)\b/i,
      /\b(?:why\s*does\s*this\s*happen|reason\s*behind\s*this|underlying\s*reason|explain\s*clearly)\b/i,
      /^explain$/i,
    ]
    return patterns.some((p) => p.test(clean))
  }

  const isNeedTimeIntent = (text: string): boolean => {
    if (!text) return false
    const clean = text.toLowerCase().trim().replace(/[.,!?:;()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim()
    const patterns = [
      /\b(?:give\s*me\s*(?:some\s*)?time|give\s*me\s*(?:a\s*)?(?:minute|sec|second|moment)|need\s*(?:some\s*)?time)\b/i,
      /\b(?:wait|wait\s*a\s*minute|wait\s*a\s*sec|wait\s*a\s*second|hold\s*on|just\s*a\s*(?:minute|sec|second))\b/i,
      /\b(?:thoda\s*time\s*do|ek\s*minute|ruko|ruk\s*jao|thoda\s*wait\s*karo|sochne\s*do)\b/i,
      /\b(?:let\s*me\s*(?:think|calculate|try|solve)|i\s*am\s*(?:thinking|calculating|solving|trying))\b/i,
      /\b(?:soch\s*raha\s*hoon|calculate\s*kar\s*raha\s*hoon|solve\s*kar\s*raha\s*hoon)\b/i,
    ]
    return patterns.some((p) => p.test(clean))
  }

  const isRepeatIntent = (text: string): boolean => {
    if (!text) return false
    const clean = text.toLowerCase().trim().replace(/[.,!?:;()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim()
    const patterns = [
      /\b(?:repeat\s*that|can\s*you\s*repeat|please\s*repeat|say\s*that\s*again)\b/i,
      /\b(?:phir\s*se\s*bolo|dobara\s*bolo|ek\s*baar\s*phir|pardon)\b/i,
      /\b(?:explain\s*(?:the\s*)?(?:whole|entire|full|all|complete)?\s*concept\s*again)\b/i,
      /\b(?:explain\s*(?:it\s*|this\s*)?again|teach\s*(?:it\s*|this\s*)?again)\b/i,
      /\b(?:dobara\s*samjhao|phir\s*se\s*samjhao|pura\s*concept\s*samjhao|pura\s*samjhao|shuru\s*se\s*samjhao)\b/i,
      /\b(?:start\s*(?:from\s*the\s*)?beginning|from\s*scratch)\b/i,
      /\b(?:one\s*more\s*time|once\s*again)\b/i,
      /^repeat$/i,
    ]
    return patterns.some((p) => p.test(clean))
  }

  const isDontUnderstandIntent = (text: string): boolean => {
    if (!text) return false
    const clean = text.toLowerCase().trim().replace(/[.,!?:;()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim()
    const patterns = [
      /\b(?:i\s*don'?t\s*understand|i\s*do\s*not\s*understand|didn'?t\s*get\s*it|not\s*getting\s*it|don'?t\s*understand)\b/i,
      /\b(?:samajh\s*nahi\s*aaya|samajh\s*na\s*aaya|kuch\s*samajh\s*nahi\s*aaya|nahi\s*samjha)\b/i,
      /\b(?:totally\s*confused|i\s*am\s*confused|it\s*is\s*confusing|not\s*clear)\b/i,
      /\b(?:i\s*am\s*stuck|stuck\s*here|fasi\s*gaya|atke\s*hue\s*hai)\b/i,
    ]
    return patterns.some((p) => p.test(clean))
  }

  const isPauseIntent = (text: string): boolean => {
    if (!text) return false
    const clean = text.toLowerCase().trim().replace(/[.,!?:;()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim()
    const patterns = [
      /^(?:pause|pause\s*lesson|pause\s*capsule|pause\s*class|stop\s*for\s*now)$/i,
      /\b(?:pause\s*(?:the\s*)?(?:class|lesson|capsule|here|please)|please\s*pause|can\s*we\s*pause)\b/i,
      /\b(?:pause\s*karo|roko|thoda\s*pause\s*karo|class\s*pause\s*karo|ruk\s*jao)\b/i,
    ]
    return patterns.some((p) => p.test(clean))
  }

  const isResumeIntent = (text: string): boolean => {
    if (!text) return false
    const clean = text.toLowerCase().trim().replace(/[.,!?:;()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim()
    const patterns = [
      /^(?:resume|resume\s*lesson|resume\s*capsule|resume\s*class|continue\s*lesson|continue)$/i,
      /\b(?:resume\s*karo|shuru\s*karo|aage\s*shuru\s*karo|chalu\s*karo|aage\s*badho)\b/i,
      /\b(?:let'?s\s*continue|continue\s*(?:the\s*)?(?:class|lesson|capsule)|please\s*resume)\b/i,
    ]
    return patterns.some((p) => p.test(clean))
  }

  // Check and increment request quota
  const checkAndRecordRequestQuota = useCallback(async (): Promise<boolean> => {
    if (userQuota.limit_type !== 'requests') return true
    if (userQuota.used_requests >= userQuota.max_requests) {
      router.push('/pricing')
      return false
    }

    try {
      const res = await fetch('/api/user/quota', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action: 'record_request' }),
      })
      const data = await res.json()
      if (data?.allowed === false) {
        router.push('/pricing')
        return false
      }
      if (typeof data?.used_requests === 'number') {
        setUserQuota((prev) => ({ ...prev, used_requests: data.used_requests }))
      }
      return true
    } catch {
      return true
    }
  }, [userQuota, router])

  const handlePauseClassRef = useRef<(() => void) | null>(null)
  const handleStartClassRef = useRef<(() => void) | null>(null)

  const handleStudentSubmitAnswer = async (answer: string) => {
    if (!answer?.trim()) return
    hasUserRespondedSinceQuestionRef.current = true
    setAwaitingStudentAnswer(false)
    const allowed = await checkAndRecordRequestQuota()
    if (!allowed) return

    const cleanAnswer = answer.trim()

    // 1. Pause intent
    if (isPauseIntent(cleanAnswer)) {
      handlePauseClassRef.current?.()
      return
    }

    // 2. Resume intent
    if (isResumeIntent(cleanAnswer)) {
      if (isPaused) {
        setIsPaused(false)
        handleStartClassRef.current?.()
      }
      return
    }

    // 0. Active Doubt / Question / Repeat Intent Fast-Paths MUST run BEFORE confirmation checks!
    if (isRepeatIntent(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      studentHasActiveDoubtRef.current = true
      lastVerdictStatusRef.current = 'neutral'
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Explanation Requested: ${cleanAnswer}`, 'coral')
      unlockConfusionVisualsForConcept(currentConceptIndexRef.current, cleanAnswer)
      sendTextMessage(
        `[STUDENT REQUEST - EXPLAIN WHOLE CONCEPT AGAIN / REPEAT]: The student requested: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. The student did not understand or wants it explained simply. Drop heavy jargon and teach in the simplest everyday language with a relatable daily-life analogy!
2. USE VISUAL TOOLS: Open or draw a visual on the board (plot_mathematical_graph, write_chalkboard draw_shape/draw_note, search_and_show_image, or search_and_show_video) while you explain step-by-step in 2 to 3 crisp sentences at a time.
3. STRICT LOCK: Stay on the CURRENT concept and current chalkboard page. DO NOT advance or call concept_completed!
4. HARD STOP: Ask if this simpler explanation makes sense and wait for the student's response!`,
        cleanAnswer
      )
      return
    }

    // Explicit next concept fast-path (must run BEFORE generic question-word checks unless user has an unresolved doubt/repeat)
    const hasExplicitDoubtInSubmit =
      isRepeatIntent(cleanAnswer) ||
      isDontUnderstandIntent(cleanAnswer) ||
      /\b(?:doubt|douth|douts|dought|daoubt|confus|unclear|samajh\s*nahi)\b/i.test(cleanAnswer)
    if (isExplicitNextConceptIntent(cleanAnswer) && !hasExplicitDoubtInSubmit) {
      hasConfirmedUnderstandingRef.current = true
      studentHasActiveDoubtRef.current = false
      doubtClearedAtMsgCountRef.current = transcriptsRef.current.length
      lastVerdictStatusRef.current = 'correct'
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)

      chalkboardRef.current?.drawStudentAnswer?.(cleanAnswer, undefined, 'blue')
      chalkboardRef.current?.drawAnswerVerdict?.('Advancing to next concept...', true, 'botanical')

      handleConceptDoneRef.current?.('EXPLICIT_USER_ADVANCE')
      return
    }

    if (isStudentQuestionOrDoubt(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      studentHasActiveDoubtRef.current = true
      lastVerdictStatusRef.current = 'neutral'
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Student Query: ${cleanAnswer}`, 'coral')
      unlockConfusionVisualsForConcept(currentConceptIndexRef.current, cleanAnswer)
      sendTextMessage(
        `[STUDENT QUESTION / DOUBT ON CURRENT CONCEPT]: The student asked: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Answer the student's question directly in simple, everyday language with a relatable example.
2. WRITE OR VISUALIZE AS YOU EXPLAIN: Use write_chalkboard, draw_shape, plot_mathematical_graph, search_and_show_image, or search_and_show_video so the student sees the answer on the board as you speak.
3. STRICT LOCK: DO NOT evaluate this as a test answer, and DO NOT call concept_completed or advance to the next concept.
4. Keep helping on the CURRENT concept until the student's doubt is completely cleared.`,
        cleanAnswer
      )
      return
    }

    if (isConfirmationOrNextIntent(cleanAnswer)) {
      studentHasActiveDoubtRef.current = false
      hasConfirmedUnderstandingRef.current = true
      doubtClearedAtMsgCountRef.current = transcriptsRef.current.length
    }

    // 3. Solve It fast-path: Student requests full solution
    if (isSolveItIntent(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Student: Please solve this step-by-step`, 'coral')
      sendTextMessage(
        `[STUDENT REQUEST - SOLVE COMPLETELY]: The student requested: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Do NOT evaluate this as a test answer or penalize them.
2. Provide the COMPLETE, rigorous, step-by-step solution on the chalkboard right now following the authentic board-exam layout (write ONE OR MAX 2 STEPS PER LINE):
   - State Given quantities with explicit units: write_chalkboard(action="draw_step", content="Given: <values with SI units>", color="amber").
   - State Formula / Theorem used: write_chalkboard(action="draw_step", content="Formula: <equation>", color="blue").
   - Detailed substitution & calculations (1 or max 2 steps per line): write_chalkboard(action="draw_step", content="Step 1: <substitution>\nStep 2: <calculation>", color="white").
   - Boxed Final Answer with SI units: write_chalkboard(action="draw_step", content="Boxed Answer: [ <numerical result> <SI unit> ]", color="botanical").
3. Speak out loud in rich pedagogical depth (5 to 6 articulate sentences) explaining WHY each step was taken. Do NOT skip any calculations or reasoning steps!
4. Check understanding: "Did you follow each step of this solution, or do you have any questions on this step?" HARD STOP: Wait for student response!`,
        cleanAnswer
      )
      return
    }

    // 4. Hint fast-path: Student requests a hint
    if (isGiveHintIntent(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      isAwaitingStudentAnswerRef.current = true
      setIsAwaitingStudentAnswer(true)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Hint requested`, 'amber')
      sendTextMessage(
        `[STUDENT REQUEST - HINT ONLY (ZERO ANSWER REVEAL)]: The student requested a hint: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Provide ONE targeted, gentle Socratic hint or guiding clue.
2. STRICT LOCK: DO NOT reveal the final answer, formula substitution, or complete solution!
3. Point out a key given value on the board, a relatable physical analogy, or ask a leading question that helps them take the next step.
4. HARD STOP: Wait silently for the student to attempt the question.`,
        cleanAnswer
      )
      return
    }

    // 5. Need more time / Wait fast-path
    if (isNeedTimeIntent(cleanAnswer)) {
      sendTextMessage(
        `[STUDENT REQUEST - MORE TIME TO THINK]: The student said: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Warmly acknowledge: e.g., "Take your time! Work through it on your notebook and let me know whenever you are ready."
2. HARD STOP: IMMEDIATELY STOP SPEAKING and remain completely silent. Do NOT reveal the answer, do NOT rush them, and do NOT speak until the student responds.`,
        cleanAnswer
      )
      return
    }

    // 6. Step-by-step explanation fast-path
    if (isExplainStepByStepIntent(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Explanation requested: ${cleanAnswer}`, 'blue')
      sendTextMessage(
        `[STUDENT REQUEST - STEP-BY-STEP EXPLANATION]: The student requested: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Explain the underlying physical intuition, governing mechanism, and step-by-step reasoning behind this concept or problem.
2. Speak conversationally in 5 to 6 rich, articulate sentences with deep clarity. Break complex steps down. Explain WHY something happens, not just what happens.
3. Write key transitions on the chalkboard as you explain.
4. Then ask if the explanation makes sense. HARD STOP: Wait for student response!`,
        cleanAnswer
      )
      return
    }

    // 7. Struggle / Don't understand fast-path
    if (isDontUnderstandIntent(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      studentHasActiveDoubtRef.current = true
      lastVerdictStatusRef.current = 'neutral'
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Student Query: Need simpler visual explanation`, 'coral')
      unlockConfusionVisualsForConcept(currentConceptIndexRef.current, cleanAnswer)
      sendTextMessage(
        `[STUDENT STRUGGLE - CONCEPT NOT CLEAR]: The student stated: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Be warm and reassuring ("No worries at all! Let me make this super simple with an everyday example").
2. DO NOT repeat textbook wording or ask about "definitions". Use the easiest everyday language and a relatable real-life example.
3. USE YOUR VISUAL TOOLS RIGHT NOW: Plot on the graph (plot_mathematical_graph), draw shapes (draw_shape), show a clarifying image/video (search_and_show_image / search_and_show_video), or write simple step-by-step notes as you speak!
4. STRICT LOCK: Stay on the current concept! HARD STOP: Ask if this simpler visual angle makes sense and wait for the student!`,
        cleanAnswer
      )
      return
    }

    // 8. Repeat fast-path
    if (isRepeatIntent(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      studentHasActiveDoubtRef.current = true
      unlockConfusionVisualsForConcept(currentConceptIndexRef.current, cleanAnswer)
      sendTextMessage(
        `[STUDENT REQUEST - REPEAT]: The student requested: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Patiently re-explain using simpler everyday words and a relatable example in 2 to 3 crisp sentences while writing/drawing on the board.
2. HARD STOP: Check if it is clear now and wait for student response!`,
        cleanAnswer
      )
      return
    }

    // 9. Question / Doubt fast-path: Address student doubt without evaluating as a test answer or advancing
    if (isStudentQuestionOrDoubt(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      studentHasActiveDoubtRef.current = true
      lastVerdictStatusRef.current = 'neutral'
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Student Query: ${cleanAnswer}`, 'coral')
      unlockConfusionVisualsForConcept(currentConceptIndexRef.current, cleanAnswer)
      sendTextMessage(
        `[STUDENT QUESTION / DOUBT ON CURRENT CONCEPT]: The student asked: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Address the student's question/doubt immediately in clear, simple language while writing/visualizing on the chalkboard.
2. STRICT LOCK: DO NOT evaluate this as a test answer, and DO NOT call concept_completed or advance to the next concept.
3. Keep answering on the CURRENT concept until the student's doubt is completely cleared.`,
        cleanAnswer
      )
      return
    }

    // Socratic Answer Handling: ALWAYS draw student answer and send for evaluation
    isAwaitingStudentAnswerRef.current = false
    setIsAwaitingStudentAnswer(false)
    isReviewingVerdictRef.current = true
    setIsReviewingVerdict(true)
    lastVerdictStatusRef.current = 'neutral'

    chalkboardRef.current?.drawStudentAnswer?.(cleanAnswer, undefined, 'blue')
    sendTextMessage(
      `Student response: "${cleanAnswer}". (Student's input is displayed on the whiteboard).
[MANDATORY SOCRATIC INSTRUCTION]:
1. Evaluate my response warmly out loud. Explain whether it is correct, partially correct, or an affirmation. Speak in complete, articulate, well-formed sentences with proper teacherly depth (do NOT stop abruptly after just one short sentence!).
2. If this was a check-for-understanding confirmation (e.g. "yes", "understood", "samajh gaya", "ok"), acknowledge warmly and proceed directly to the NEXT STAGE of this concept (e.g. formulate the formal law with SI units, solve the step-by-step board numerical, or pose the Stage 5/6 checkpoint question). When the Stage 5/6 checkpoint question has been evaluated, proceed smoothly to concept completion.
3. If this was an answer to a question or numerical:
   - Write the verdict and model answer on this current whiteboard page using write_chalkboard(action="draw_answer_verdict", content="Verdict: <Correct / Needs Review> - <Reason>").
   - If incorrect or hesitant, break down the step and co-solve with me in [ROUGH_WORK].
4. HARD STOP: Deliver complete, well-formed teacherly explanations. Ask if I followed or have any doubts before proceeding.
5. ADVANCEMENT GATING: Call concept_completed(conceptName="...") or write_chalkboard(action="concept_done") ONLY after the Stage 5/6 checkpoint question has been solved and verified, or if the student explicitly commands moving to the next concept. DO NOT advance to the next concept or page yet! Remain on this current concept page so I can review the chalkboard notes. NEVER skip concepts.`,
      cleanAnswer
    )
  }

  const handleStudentVoiceAnswer = async (answer: string) => {
    if (!answer?.trim()) return
    hasUserRespondedSinceQuestionRef.current = true
    setAwaitingStudentAnswer(false)
    const allowed = await checkAndRecordRequestQuota()
    if (!allowed) return

    const cleanAnswer = answer.trim()

    // 1. Pause intent
    if (isPauseIntent(cleanAnswer)) {
      handlePauseClassRef.current?.()
      return
    }

    // 2. Resume intent
    if (isResumeIntent(cleanAnswer)) {
      if (isPaused) {
        setIsPaused(false)
        handleStartClassRef.current?.()
      }
      return
    }

    // 0. Active Doubt / Question / Repeat Intent Fast-Paths MUST run BEFORE confirmation checks!
    if (isRepeatIntent(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      studentHasActiveDoubtRef.current = true
      lastVerdictStatusRef.current = 'neutral'
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Explanation Requested: ${cleanAnswer}`, 'coral')
      unlockConfusionVisualsForConcept(currentConceptIndexRef.current, cleanAnswer)
      sendTextMessage(
        `[STUDENT REQUEST - EXPLAIN WHOLE CONCEPT AGAIN / REPEAT]: The student requested: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Drop jargon and re-explain from scratch in the simplest everyday words with a relatable student-life example!
2. USE VISUAL TOOLS: Plot on the graph, draw shapes/steps, or use video/follow-up image as you explain.
3. STRICT LOCK: Stay on the CURRENT concept and current chalkboard page. DO NOT advance or call concept_completed!
4. HARD STOP: Check if it makes sense now and wait for the student's response!`
      )
      return
    }

    // Explicit next concept fast-path (must run BEFORE generic question-word checks unless user has an unresolved doubt/repeat)
    const hasExplicitDoubtInVoice =
      isRepeatIntent(cleanAnswer) ||
      isDontUnderstandIntent(cleanAnswer) ||
      /\b(?:doubt|douth|douts|dought|daoubt|confus|unclear|samajh\s*nahi)\b/i.test(cleanAnswer)
    if (isExplicitNextConceptIntent(cleanAnswer) && !hasExplicitDoubtInVoice) {
      hasConfirmedUnderstandingRef.current = true
      studentHasActiveDoubtRef.current = false
      doubtClearedAtMsgCountRef.current = transcriptsRef.current.length
      lastVerdictStatusRef.current = 'correct'
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)

      chalkboardRef.current?.drawStudentAnswer?.(cleanAnswer, undefined, 'blue')
      chalkboardRef.current?.drawAnswerVerdict?.('Advancing to next concept...', true, 'botanical')

      handleConceptDoneRef.current?.('EXPLICIT_USER_ADVANCE')
      return
    }

    if (isStudentQuestionOrDoubt(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      studentHasActiveDoubtRef.current = true
      lastVerdictStatusRef.current = 'neutral'
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Student Query: ${cleanAnswer}`, 'coral')
      unlockConfusionVisualsForConcept(currentConceptIndexRef.current, cleanAnswer)
      sendTextMessage(
        `[STUDENT QUESTION / DOUBT ON CURRENT CONCEPT]: The student asked: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Answer clearly in simple everyday language while writing/visualizing on the chalkboard (write_chalkboard, draw_shape, plot_mathematical_graph, search_and_show_image, or search_and_show_video).
2. STRICT LOCK: DO NOT evaluate this as a test answer, and DO NOT call concept_completed or advance to the next concept.
3. Keep answering on the CURRENT concept until the student's doubt is completely cleared.`
      )
      return
    }

    if (isConfirmationOrNextIntent(cleanAnswer)) {
      studentHasActiveDoubtRef.current = false
      hasConfirmedUnderstandingRef.current = true
      doubtClearedAtMsgCountRef.current = transcriptsRef.current.length
    }

    // 3. Solve It fast-path
    if (isSolveItIntent(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Student: Please solve this step-by-step`, 'coral')
      sendTextMessage(
        `[STUDENT REQUEST - SOLVE COMPLETELY]: The student requested: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Do NOT evaluate this as a test answer or penalize them.
2. Provide the COMPLETE, rigorous, step-by-step solution on the chalkboard right now following the authentic board-exam layout (write ONE OR MAX 2 STEPS PER LINE):
   - State Given quantities with explicit units: write_chalkboard(action="draw_step", content="Given: <values with SI units>", color="amber").
   - State Formula / Theorem used: write_chalkboard(action="draw_step", content="Formula: <equation>", color="blue").
   - Detailed substitution & calculations (1 or max 2 steps per line): write_chalkboard(action="draw_step", content="Step 1: <substitution>\nStep 2: <calculation>", color="white").
   - Boxed Final Answer with SI units: write_chalkboard(action="draw_step", content="Boxed Answer: [ <numerical result> <SI unit> ]", color="botanical").
3. Speak out loud in rich pedagogical depth (5 to 6 articulate sentences) explaining WHY each step was taken. Do NOT skip any calculations or reasoning steps!
4. Check understanding: "Did you follow each step of this solution, or do you have any questions on this step?" HARD STOP: Wait for student response!`
      )
      return
    }

    // 4. Hint fast-path
    if (isGiveHintIntent(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      isAwaitingStudentAnswerRef.current = true
      setIsAwaitingStudentAnswer(true)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Hint requested`, 'amber')
      sendTextMessage(
        `[STUDENT REQUEST - HINT ONLY (ZERO ANSWER REVEAL)]: The student requested a hint: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Provide ONE targeted, gentle Socratic hint or guiding clue.
2. STRICT LOCK: DO NOT reveal the final answer, formula substitution, or complete solution!
3. Point out a key given value on the board, a relatable physical analogy, or ask a leading question that helps them take the next step.
4. HARD STOP: Wait silently for the student to attempt the question.`
      )
      return
    }

    // 5. Need more time / Wait fast-path
    if (isNeedTimeIntent(cleanAnswer)) {
      sendTextMessage(
        `[STUDENT REQUEST - MORE TIME TO THINK]: The student said: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Warmly acknowledge: e.g., "Take your time! Work through it on your notebook and let me know whenever you are ready."
2. HARD STOP: IMMEDIATELY STOP SPEAKING and remain completely silent. Do NOT reveal the answer, do NOT rush them, and do NOT speak until the student responds.`
      )
      return
    }

    // 6. Step-by-step explanation fast-path
    if (isExplainStepByStepIntent(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Explanation requested: ${cleanAnswer}`, 'blue')
      sendTextMessage(
        `[STUDENT REQUEST - STEP-BY-STEP EXPLANATION]: The student requested: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Explain the underlying physical intuition, governing mechanism, and step-by-step reasoning behind this concept or problem.
2. Speak conversationally in 5 to 6 rich, articulate sentences with deep clarity. Break complex steps down. Explain WHY something happens, not just what happens.
3. Write key transitions on the chalkboard as you explain.
4. Then ask if the explanation makes sense. HARD STOP: Wait for student response!`
      )
      return
    }

    // 7. Struggle / Don't understand fast-path
    if (isDontUnderstandIntent(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      studentHasActiveDoubtRef.current = true
      lastVerdictStatusRef.current = 'neutral'
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Student Query: Need simpler visual explanation`, 'coral')
      unlockConfusionVisualsForConcept(currentConceptIndexRef.current, cleanAnswer)
      sendTextMessage(
        `[STUDENT STRUGGLE - CONCEPT NOT CLEAR]: The student stated: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Be warm and patient. Explain in the easiest everyday words with a relatable real-life student example (never repeat jargon or talk about "definitions").
2. USE VISUAL TOOLS NOW: Open or plot on the graph (plot_mathematical_graph), draw shapes (draw_shape), show a clarifying video/image, or write simple step-by-step notes on the board!
3. HARD STOP: Ask if this simpler angle makes sense and wait for student response!`
      )
      return
    }

    // 8. Repeat fast-path
    if (isRepeatIntent(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      studentHasActiveDoubtRef.current = true
      unlockConfusionVisualsForConcept(currentConceptIndexRef.current, cleanAnswer)
      sendTextMessage(
        `[STUDENT REQUEST - REPEAT]: The student requested: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Patiently re-explain in simple everyday words using a relatable analogy and visual board notes in 2 to 3 crisp sentences.
2. HARD STOP: Check if it is clear now and wait for student response!`
      )
      return
    }

    // 9. Question / Doubt fast-path: Address student doubt without evaluating as a test answer or advancing
    if (isStudentQuestionOrDoubt(cleanAnswer)) {
      hasConfirmedUnderstandingRef.current = false
      studentHasActiveDoubtRef.current = true
      lastVerdictStatusRef.current = 'neutral'
      isAwaitingStudentAnswerRef.current = false
      setIsAwaitingStudentAnswer(false)
      isReviewingVerdictRef.current = false
      setIsReviewingVerdict(false)

      chalkboardRef.current?.drawNote?.(`Student Query: ${cleanAnswer}`, 'coral')
      unlockConfusionVisualsForConcept(currentConceptIndexRef.current, cleanAnswer)
      sendTextMessage(
        `[STUDENT QUESTION / DOUBT ON CURRENT CONCEPT]: The student asked: "${cleanAnswer}".
CRITICAL DIRECTIVE:
1. Answer clearly in simple everyday language while writing/visualizing on the chalkboard.
2. STRICT LOCK: DO NOT evaluate this as a test answer, and DO NOT call concept_completed or advance to the next concept.
3. Keep answering on the CURRENT concept until the student's doubt is completely cleared.`
      )
      return
    }

    isAwaitingStudentAnswerRef.current = false
    setIsAwaitingStudentAnswer(false)
    isReviewingVerdictRef.current = true
    setIsReviewingVerdict(true)
    lastVerdictStatusRef.current = 'neutral'

    chalkboardRef.current?.drawStudentAnswer?.(cleanAnswer, undefined, 'blue')
    sendTextMessage(
      `Student response: "${cleanAnswer}". (Student's input is displayed on the whiteboard).
[MANDATORY SOCRATIC INSTRUCTION]:
1. Evaluate my response warmly out loud. Explain whether it is correct, partially correct, or an affirmation. Speak in complete, articulate, well-formed sentences with proper teacherly depth (do NOT stop abruptly after just one short sentence!).
2. If this was a check-for-understanding confirmation (e.g. "yes", "understood", "samajh gaya", "ok"), acknowledge warmly and proceed directly to the NEXT STAGE of this concept (e.g. formulate the formal law with SI units, solve the step-by-step board numerical, or pose the Stage 5/6 checkpoint question). When the Stage 5/6 checkpoint question has been evaluated, proceed smoothly to concept completion.
3. If this was an answer to a question or numerical:
   - Write the verdict and model answer on this current whiteboard page using write_chalkboard(action="draw_answer_verdict", content="Verdict: <Correct / Needs Review> - <Reason>").
   - If incorrect or hesitant, break down the step and co-solve with me in [ROUGH_WORK].
4. HARD STOP: Deliver complete, well-formed teacherly explanations. Ask if I followed or have any doubts before proceeding.
5. ADVANCEMENT GATING: Call concept_completed(conceptName="...") or write_chalkboard(action="concept_done") ONLY after the Stage 5/6 checkpoint question has been solved and verified, or if the student explicitly commands moving to the next concept. DO NOT advance to the next concept or page yet! Remain on this current concept page so I can review the chalkboard notes. NEVER skip concepts.`
    )
  }

  const [activeModule, setActiveModule] = useState<any>(null)
  const [userMemories, setUserMemories] = useState<any[]>([])

  // Background pre-fetching of high-resolution educational images for all module concepts & pre-flight asset verification
  useEffect(() => {
    if (!activeModule) return
    const vPlan = (activeModule.visual_lesson_plan as any) || {}
    const conceptVisuals: any[] = Array.isArray(vPlan.concept_visuals)
      ? vPlan.concept_visuals
      : Array.isArray(activeModule.concept_visuals)
      ? activeModule.concept_visuals
      : []
    const keyConceptsList = parseKeyConcepts(activeModule.key_concepts)

    const moduleStorageKey = `prefetched_imgs_${activeModule.id}`
    let localCached: Record<number, any> = {}
    if (typeof window !== 'undefined') {
      try {
        const raw = localStorage.getItem(moduleStorageKey)
        if (raw) localCached = JSON.parse(raw)
      } catch {}
    }

    // Filter out any stale, low-quality slide decks or blog URLs that were previously cached in localStorage
    Object.keys(localCached).forEach((k) => {
      const item = localCached[Number(k)]
      if (
        item?.url &&
        (item.url.includes('slideserve') ||
          item.url.includes('slideshare') ||
          item.url.includes('slideplayer') ||
          item.url.includes('factmyth') ||
          item.url.includes('Alpha'))
      ) {
        delete localCached[Number(k)]
      }
    })

    if (Object.keys(localCached).length > 0) {
      setPrefetchedImages(localCached)
    }

    // 1. Run Pre-flight Asset Verification & dynamic repair route
    fetch('/api/diagram/verify-assets', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ moduleId: activeModule.id }),
    })
      .then((r) => r.json())
      .then((data) => {
        if (data.success && data.aiDirectives) {
          setVerifiedAssetsDirectives(data.aiDirectives)
        }
        if (data.success && Array.isArray(data.verifiedImages)) {
          data.verifiedImages.forEach((vImg: any, idx: number) => {
            if (vImg.url && vImg.verified) {
              localCached[idx] = {
                url: vImg.url,
                title: vImg.title || keyConceptsList[idx] || 'Diagram',
                caption: vImg.description || '',
              }
            }
          })
          setPrefetchedImages({ ...localCached })
          if (typeof window !== 'undefined') {
            try {
              localStorage.setItem(moduleStorageKey, JSON.stringify(localCached))
            } catch {}
          }
        }
      })
      .catch((err) => console.warn('[verify-assets check error]:', err))

    // 2. Also ensure every concept without verified cached URL initiates image lookup
    const prefetchPromises = keyConceptsList.map(async (concept, idx) => {
      if (localCached[idx]?.url) return

      const cv = conceptVisuals[idx] || {}
      const rawSearchQuery = cv.image_search_query || cv.image_query || cv.diagram_title || concept
      const searchQuery = extractConciseSearchKeyword(rawSearchQuery) || rawSearchQuery
      if (!searchQuery) return

      try {
        const res = await fetch(`/api/diagram/search-image?q=${encodeURIComponent(searchQuery)}&limit=3`)
        if (res.ok) {
          const data = await res.json()
          const candidateImages: any[] = data.images || []
          for (const img of candidateImages) {
            if (!img?.url) continue
            try {
              const check = await fetch(`/api/diagram/proxy?dataUrl=true&url=${encodeURIComponent(img.url)}`)
              if (check.ok) {
                const pData = await check.json()
                if (pData.success && pData.dataURL) {
                  localCached[idx] = {
                    url: pData.dataURL,
                    title: cv.diagram_title || img.title || concept,
                    caption: cv.what_to_make || img.description || '',
                  }
                  break
                }
              }
            } catch {}
          }
        }
      } catch (err) {
        console.warn(`[Prefetch Image Error for concept ${idx}]:`, err)
      }
    })

    Promise.allSettled(prefetchPromises).then(() => {
      setPrefetchedImages({ ...localCached })
      if (typeof window !== 'undefined') {
        try {
          localStorage.setItem(moduleStorageKey, JSON.stringify(localCached))
        } catch {}
      }
    })
  }, [activeModule])
  const [activeCurriculum, setActiveCurriculum] = useState<any>(null)
  const [siblingModules, setSiblingModules] = useState<any[]>([])
  const [nextChapterInfo, setNextChapterInfo] = useState<{
    chapterId: string
    chapterTitle: string
    firstModuleId: string
    firstModuleTitle: string
    orderIndex: number
  } | null>(null)
  const [moduleCompletedSuccess, setModuleCompletedSuccess] = useState(false)
  const [isLoadingLesson, setIsLoadingLesson] = useState(true)
  const [quizOpen, setQuizOpen] = useState(false)
  const [conceptsOpen, setConceptsOpen] = useState(false)
  // Meet-style classroom UI state
  const camera = useCameraPreview()
  const [captionsOn, setCaptionsOn] = useState(true)
  const [sidePanel, setSidePanel] = useState<'chat' | 'concepts' | null>(null)
  const [chatDraft, setChatDraft] = useState('')
  const [elapsedSec, setElapsedSec] = useState(0)
  const [preferredVoice, setPreferredVoice] = useState<string>('Charon')
  const sessionActiveVoiceRef = useRef<string | null>(null)
  const [isPaused, setIsPaused] = useState<boolean>(false)
  const isPausedRef = useRef<boolean>(false)
  useEffect(() => {
    isPausedRef.current = isPaused
  }, [isPaused])

  // Persist student's voice preference to Supabase profiles table
  const persistVoicePreferenceToDb = useCallback(async (voice: string) => {
    if (!userId || !voice) return
    try {
      const supabase = createClient()
      await supabase
        .from('profiles')
        .update({ preferred_teacher_voice: voice, updated_at: new Date().toISOString() })
        .eq('id', userId)
    } catch (err) {
      console.warn('[Classroom] Notice saving voice preference to DB:', err)
    }
  }, [userId])

  const [isCompletedBefore, setIsCompletedBefore] = useState(false)
  const [studentProfileClassLevel, setStudentProfileClassLevel] = useState<string>('')
  const [studentName, setStudentName] = useState<string>('')
  const [studentPreferredLanguage, setStudentPreferredLanguage] = useState<string>('English')
  const [studentStudyMedium, setStudentStudyMedium] = useState<string>('English')
  const [studentTargetBoard, setStudentTargetBoard] = useState<string>('CBSE')
  const [studentLearningPace, setStudentLearningPace] = useState<string>('steady_and_balanced')
  const [studentLearningStyle, setStudentLearningStyle] = useState<string>('socratic')
  const [studentCareerAspiration, setStudentCareerAspiration] = useState<string>('')
  const [studentFavoriteSubject, setStudentFavoriteSubject] = useState<string>('Physics')
  const [studentWeakSubjects, setStudentWeakSubjects] = useState<string[]>([])
  const [studentStrongSubjects, setStudentStrongSubjects] = useState<string[]>([])
  const [endChapterConfirmPrompt, setEndChapterConfirmPrompt] = useState<string | null>(null)

  // Interactive 3D Visualization Stage state
  const [activeSceneType, setActiveSceneType] = useState<VisualizationSceneType | null>(null)
  const [activeSceneParams, setActiveSceneParams] = useState<Record<string, any>>({})
  const [activeSceneTitle, setActiveSceneTitle] = useState<string | undefined>(undefined)

  // Multimedia Lesson Manifest & Position State
  const [lessonManifest, setLessonManifest] = useState<VisualLessonManifest | null>(null)
  const [activeVisualStepIndex, setActiveVisualStepIndex] = useState<number>(0)

  // Concept-level progress tracking & automatic session resumption
  const [currentConceptIndex, setCurrentConceptIndex] = useState<number>(0)
  const currentConceptIndexRef = useRef<number>(0)
  useEffect(() => {
    currentConceptIndexRef.current = currentConceptIndex
  }, [currentConceptIndex])
  const [completedConcepts, setCompletedConcepts] = useState<string[]>([])
  const completedConceptsRef = useRef<string[]>([])
  useEffect(() => {
    completedConceptsRef.current = completedConcepts
  }, [completedConcepts])
  const [lastCoveredConcept, setLastCoveredConcept] = useState<string>('')

  // Chapter Notes state, AI optimization & auto-save to Supabase
  const [chapterNotes, setChapterNotes] = useState<string>('')
  const [notesModalOpen, setNotesModalOpen] = useState(false)
  const [notesSaveStatus, setNotesSaveStatus] = useState<'saved' | 'saving' | 'idle'>('idle')
  const [latestBoardSummary, setLatestBoardSummary] = useState<string>('')
  const saveTimeoutRef = useRef<NodeJS.Timeout | null>(null)
  const boardSyncTimeoutRef = useRef<NodeJS.Timeout | null>(null)
  const lastSentBoardNotesRef = useRef<string>('')
  const isMarkingCompleteRef = useRef<boolean>(false)

  const chalkboardRef = useRef<GreenChalkboardRef | null>(null)
  const executedSceneDirectivesRef = useRef<Set<string>>(new Set())
  const renderedVisualConceptsRef = useRef<Set<number>>(new Set())
  const imagesRenderedPerConceptRef = useRef<Map<number, number>>(new Map())
  const videosUnlockedPerConceptRef = useRef<Set<number>>(new Set())
  const askedOrSolvedExercisesPerConceptRef = useRef<Map<number, number>>(new Map())
  const hasEverConnectedRef = useRef<boolean>(false)
  if (
    connectionState === 'CONNECTED' ||
    connectionState === 'LISTENING' ||
    connectionState === 'TEACHER_SPEAKING'
  ) {
    hasEverConnectedRef.current = true
  }
  const lastPageJumpTimeRef = useRef<number>(0)
  const lastTargetIdxRef = useRef<number>(-1)
  const lastConceptDoneTimeRef = useRef<number>(0)
  const hasSessionStartedRef = useRef<boolean>(false)
  const isUserTerminatedRef = useRef<boolean>(false)
  const reconnectAttemptsRef = useRef<number>(0)
  const hasConfirmedUnderstandingRef = useRef<boolean>(false)
  const studentHasActiveDoubtRef = useRef<boolean>(false)
  const doubtClearedAtMsgCountRef = useRef<number>(0)
  const [isReconnecting, setIsReconnecting] = useState<boolean>(false)
  const reconnectAttemptTimerRef = useRef<NodeJS.Timeout | null>(null)

  // Exact database values (no hardcoded mocks)
  const resolvedClassLevel =
    activeModule?.class_level ||
    (Array.isArray(activeModule?.curriculums)
      ? activeModule?.curriculums[0]?.class_level
      : activeModule?.curriculums?.class_level) ||
    activeCurriculum?.class_level ||
    studentProfileClassLevel ||
    ''

  const resolvedSubject =
    (Array.isArray(activeModule?.curriculums)
      ? activeModule?.curriculums[0]?.category
      : activeModule?.curriculums?.category) ||
    activeCurriculum?.category ||
    'Science'

  const resolvedBoard =
    activeModule?.board ||
    (Array.isArray(activeModule?.curriculums)
      ? activeModule?.curriculums[0]?.board
      : activeModule?.curriculums?.board) ||
    activeCurriculum?.board ||
    'CBSE'

  const resolvedTitle = activeModule?.title || ''

  // Guard to ensure loadModuleContext runs strictly once per module navigation
  const hasLoadedModuleContextRef = useRef<string | null>(null)

  // 1. Fetch exact module context, student profile, concept tracking & existing notes
  useEffect(() => {
    if (!userId || !moduleId) return
    const contextKey = `${userId}_${moduleId}`
    if (hasLoadedModuleContextRef.current === contextKey) return
    hasLoadedModuleContextRef.current = contextKey

    const supabase = createClient()

    async function loadModuleContext() {
      setIsLoadingLesson(true)
      try {
        // Security Invariant: Validate active authenticated user matches route userId
        const { data: authData } = await supabase.auth.getUser()
        if (!authData?.user || authData.user.id !== userId) {
          console.warn('[Classroom Guard] IDOR mismatch: current user is not authorized for this classroom URL.')
          router.replace('/login')
          return
        }

        // Fetch cached student profile & progress list
        const [profile, cachedAllProgress] = await Promise.all([
          getCachedUserProfile(supabase, userId),
          getCachedUserProgressList(supabase, userId),
        ])

        // Dynamic Quota Check (respecting unlimited & module limits configured by admin):
        const isUnlimitedUser = profile?.limit_type === 'unlimited'
        const maxAllowedModules = profile?.limit_type === 'modules' ? (profile?.max_modules ?? 5) : 1

        if (!isUnlimitedUser) {
          const completedList = (cachedAllProgress || []).filter((p: any) => p.status === 'completed' || !!p.completed_at)
          if (completedList.length >= maxAllowedModules && !completedList.some((p: any) => p.syllabus_module_id === moduleId)) {
            console.warn('[Classroom Guard] User module quota reached. Redirecting to pricing notice.')
            router.replace(`/dashboard/${userId}?pricing_notice=true`)
            return
          }
        }

        if (profile?.target_board) setStudentTargetBoard(profile.target_board)
        if (profile?.preferred_language) setStudentPreferredLanguage(profile.preferred_language)
        if (profile?.study_medium) setStudentStudyMedium(profile.study_medium)
        if (profile?.learning_pace) setStudentLearningPace(profile.learning_pace)
        if (profile?.learning_style) setStudentLearningStyle(profile.learning_style)
        if (profile?.career_aspiration) setStudentCareerAspiration(profile.career_aspiration)
        if (profile?.favorite_subject) setStudentFavoriteSubject(profile.favorite_subject)
        if (Array.isArray(profile?.strong_subjects)) setStudentStrongSubjects(profile.strong_subjects)
        if (Array.isArray(profile?.weak_subjects) && profile.weak_subjects.length > 0) {
          setStudentWeakSubjects(profile.weak_subjects)
        } else if (profile?.weak_area) {
          setStudentWeakSubjects([profile.weak_area])
        }

        if (typeof profile?.is_avatar_enabled === 'boolean') {
          setIsAvatarEnabled(profile.is_avatar_enabled)
        }
        if (profile?.limit_type) {
          setUserQuota({
            limit_type: profile.limit_type || 'unlimited',
            max_requests: profile.max_requests || 100,
            used_requests: profile.used_requests || 0,
            max_modules: profile.max_modules || 5,
            used_modules: profile.used_modules || 0,
          })
        }

        // Module Quota Guard: Enforce limit if student is under 'modules' policy
        if (profile?.limit_type === 'modules') {
          try {
            const quotaCheckRes = await fetch('/api/user/quota', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ action: 'record_module', moduleId }),
            })
            const quotaData = await quotaCheckRes.json()
            if (quotaData?.allowed === false) {
              router.replace('/pricing')
              return
            } else if (quotaData?.used_modules) {
              setUserQuota((prev) => ({ ...prev, used_modules: quotaData.used_modules }))
            }
          } catch (e) {
            console.warn('[Classroom] Failed to check module quota:', e)
          }
        }

        let foundName = ''
        if (profile?.full_name?.trim()) {
          foundName = profile.full_name.trim()
        } else {
          const meta = authData?.user?.user_metadata
          foundName = (meta?.full_name || meta?.name || authData?.user?.email?.split('@')[0] || '').trim()
        }
        if (foundName) {
          setStudentName(foundName)
        }
        if (profile?.class_level) {
          setStudentProfileClassLevel(profile.class_level)
        }
        if (profile?.preferred_teacher_voice) {
          setPreferredVoice(profile.preferred_teacher_voice)
          setSelectedVoice(profile.preferred_teacher_voice as any)
        }

        // Fetch exact syllabus module from high-speed dataCache or Supabase
        const mod = await getCachedSyllabusModule(supabase, moduleId)

        if (!mod) {
          console.warn('[Classroom] Module not found or relocated:', moduleId, '-> Redirecting to active module resolver')
          router.replace(`/dashboard/${userId}/class`)
          return
        } else {
          setActiveModule(mod)
          const curr = Array.isArray(mod.curriculums) ? mod.curriculums[0] : mod.curriculums
          setActiveCurriculum(curr)

          // Resolve authentic textbook PDF for this chapter
          const resolvedBook = resolveBookForChapter({
            classLevel: resolvedClassLevel || curr?.class_level || mod.class_level,
            category: resolvedSubject || curr?.category,
            chapterTitle: curr?.title || mod.title,
            chapterOrderIndex: curr?.order_index || mod.order_index,
            notesSourceFilename: curr?.notes_source_filename,
          })
          if (resolvedBook) {
            setBookPdfUrl(resolvedBook.pdfUrl)
            setBookTotalPages(resolvedBook.totalPages)
            bookTotalPagesRef.current = resolvedBook.totalPages
            bookPdfUrlRef.current = resolvedBook.pdfUrl
            setBookChapterTitle(curr?.title || `Chapter ${resolvedBook.chapterNumber} Textbook`)
            const modConcepts = parseKeyConcepts(mod.key_concepts)
            const initialConceptName = modConcepts[currentConceptIndexRef.current || 0] || mod.title
            const initialPage = resolveTargetPageForLesson({
              conceptName: initialConceptName,
              capsuleTitle: mod.title,
              chapterNumber: curr?.order_index || mod.order_index,
              classLevel: resolvedClassLevel || curr?.class_level || mod.class_level,
              subject: resolvedSubject || curr?.category || mod.subject,
              pdfPath: resolvedBook.pdfUrl,
              conceptIndex: currentConceptIndexRef.current || 0,
              totalConcepts: modConcepts.length || 1,
              moduleIndex: typeof mod.order_index === 'number' ? mod.order_index - 1 : 0,
              totalModules: 6,
              totalPages: resolvedBook.totalPages,
            })
            setBookCurrentPage(initialPage)
          }

          // Load or generate structured visual lesson plan
          if (mod.visual_lesson_plan && typeof mod.visual_lesson_plan === 'object' && Array.isArray(mod.visual_lesson_plan.steps)) {
            setLessonManifest(mod.visual_lesson_plan)
          } else {
            const generatedPlan = generateVisualLessonPlanForCapsule(
              {
                moduleId: mod.id,
                order_index: mod.order_index,
                title: mod.title,
                description: mod.description,
                subtopics: mod.subtopics || [],
                key_concepts: mod.key_concepts || [],
                worked_examples: mod.worked_examples || [],
                common_misconceptions: mod.common_misconceptions || [],
                board: resolvedBoard,
                class_level: resolvedClassLevel,
                category: resolvedSubject,
              },
              {
                textbookName: `${resolvedBoard} Official Curriculum`,
              }
            )
            const mergedPlan = {
              ...generatedPlan,
              ...(mod.visual_lesson_plan || {}),
              steps: mod.visual_lesson_plan?.steps || generatedPlan.steps,
            }
            setLessonManifest(mergedPlan)
          }

          // Fetch all sibling modules in this curriculum for flexible progression (from cache)
          if (mod.curriculum_id) {
            const sibs = await getCachedSiblingModules(supabase, mod.curriculum_id)
            setSiblingModules(sibs || [])
            if (resolvedBook && sibs && sibs.length > 0) {
              const modConcepts = parseKeyConcepts(mod.key_concepts)
              const initialConceptName = modConcepts[currentConceptIndexRef.current || 0] || mod.title
              const pageWithSibs = resolveTargetPageForLesson({
                conceptName: initialConceptName,
                capsuleTitle: mod.title,
                chapterNumber: curr?.order_index || mod.order_index,
                classLevel: resolvedClassLevel || curr?.class_level || mod.class_level,
                subject: resolvedSubject || curr?.category || mod.subject,
                pdfPath: resolvedBook.pdfUrl,
                conceptIndex: currentConceptIndexRef.current || 0,
                totalConcepts: modConcepts.length || 1,
                moduleIndex: typeof mod.order_index === 'number' ? mod.order_index - 1 : 0,
                totalModules: sibs.length,
                totalPages: resolvedBook.totalPages,
              })
              setBookCurrentPage(pageWithSibs)
            }
          }

          // Fetch next chapter in the same class and category (ordered sequentially from cache)
          if (curr && curr.class_level && curr.category) {
            const nextInfo = await getCachedNextChapterInfo(supabase, {
              classLevel: curr.class_level,
              category: curr.category,
              currentOrderIndex: typeof curr.order_index === 'number' ? curr.order_index : 1,
              board: curr.board,
            })
            if (nextInfo) {
              setNextChapterInfo(nextInfo)
            }
          }
        }

        // Check Free Completed Module Quota (only for free tier non-unlimited users, via cached progress)
        const isFreeTierUser = !isUnlimitedUser && (profile?.subscription_tier === 'free' || !profile?.subscription_tier)
        if (isFreeTierUser) {
          const otherCompleted = (cachedAllProgress || []).filter(
            (c: any) => c.status === 'completed' && c.syllabus_module_id !== moduleId
          )
          if (otherCompleted.length >= maxAllowedModules) {
            console.warn('[Classroom Guard] User module quota reached. Redirecting to /pricing.')
            router.replace('/pricing')
            return
          }
        }

        // 1. Instant local session restoration
        let hasRestoredCachedSession = false
        let cachedSessionSnapshot: any = null
        if (moduleId) {
          pruneExpiredSessions()
          const cachedSession = loadSessionState(moduleId)
          if (cachedSession) {
            cachedSessionSnapshot = cachedSession
            hasRestoredCachedSession = true
            if (typeof cachedSession.currentConceptIndex === 'number') {
              currentConceptIndexRef.current = cachedSession.currentConceptIndex
              setCurrentConceptIndex(cachedSession.currentConceptIndex)
            }
            if (Array.isArray(cachedSession.completedConcepts) && cachedSession.completedConcepts.length > 0) {
              completedConceptsRef.current = cachedSession.completedConcepts
              setCompletedConcepts(cachedSession.completedConcepts)
            }
            if (cachedSession.lastCoveredConcept) {
              setLastCoveredConcept(cachedSession.lastCoveredConcept)
            }
            if (cachedSession.currentStage) {
              pedagogicalStateManager?.setStage?.(cachedSession.currentStage as any)
            }
            if (typeof cachedSession.chalkboardPageIndex === 'number') {
              setTimeout(() => {
                chalkboardRef.current?.goToPage?.(cachedSession.chalkboardPageIndex)
              }, 400)
            }
            setIsPaused(true)
          }
        }

        // Fetch cached top AI student memories & module progress in parallel
        const [mems, progress] = await Promise.all([
          userId ? getCachedUserMemories(supabase, userId, 5).catch(() => []) : Promise.resolve([]),
          getCachedModuleProgress(supabase, userId, moduleId),
        ])
        if (mems && mems.length > 0) {
          const mapped = mems.map((m: any) => ({ ...m, memory_text: m.content || m.memory_text || '', category: m.memory_type || m.category || '' }))
          setUserMemories(mapped)
        }

        if (progress) {
          if (typeof progress.current_concept_index === 'number') {
            const currentCached = currentConceptIndexRef.current
            if (!hasRestoredCachedSession || progress.current_concept_index > currentCached) {
              currentConceptIndexRef.current = progress.current_concept_index
              setCurrentConceptIndex(progress.current_concept_index)
            }
          }
          if (progress.is_paused || progress.visual_progress?.isPaused) {
            setIsPaused(true)
          }
          if (Array.isArray(progress.completed_concepts)) {
            const dbLoaded = parseKeyConcepts(progress.completed_concepts)
            const keepAheadLocal =
              hasRestoredCachedSession &&
              typeof cachedSessionSnapshot?.currentConceptIndex === 'number' &&
              cachedSessionSnapshot.currentConceptIndex >= (progress.current_concept_index ?? 0)
            const mergedCompleted = keepAheadLocal
              ? Array.from(new Set([...dbLoaded, ...(completedConceptsRef.current || [])]))
              : dbLoaded
            completedConceptsRef.current = mergedCompleted
            setCompletedConcepts(mergedCompleted)
          }
          if (progress.last_covered_concept) {
            setLastCoveredConcept((prev) => (prev === progress.last_covered_concept ? prev : progress.last_covered_concept))
          }
          const cachedLocalNotes = getCachedBoardNotes(userId, moduleId)
          const hasFreshLocalNotes = cachedLocalNotes?.fullSummary && cachedLocalNotes.fullSummary.trim().length > 10

          if (progress.chapter_notes && !hasFreshLocalNotes) {
            setChapterNotes((prev) => (prev === progress.chapter_notes ? prev : progress.chapter_notes))
          }

          // Restore whiteboard state from DB if localStorage is empty or sync from cloud
          if (typeof window !== 'undefined' && moduleId) {
            const localRaw = localStorage.getItem(`whiteboard_pages_${moduleId}`)
            const hasLocalPages = localRaw && localRaw.length > 50

            if (progress.visual_progress?.whiteboard_pages && Array.isArray(progress.visual_progress.whiteboard_pages)) {
              try {
                localStorage.setItem(`whiteboard_pages_${moduleId}`, JSON.stringify(progress.visual_progress.whiteboard_pages))
                if (progress.visual_progress.whiteboard_files) {
                  localStorage.setItem(`whiteboard_pages_${moduleId}_files`, JSON.stringify(progress.visual_progress.whiteboard_files))
                }
              } catch {}
              if (!hasLocalPages) {
                setTimeout(() => {
                  chalkboardRef.current?.restoreBoardState?.(
                    progress.visual_progress.whiteboard_pages,
                    progress.visual_progress.whiteboard_files
                  )
                }, 300)
              }
            } else if (!hasLocalPages && progress.chapter_notes) {
              setTimeout(() => {
                if (chalkboardRef.current && progress.chapter_notes) {
                  chalkboardRef.current.rewriteNotes?.(progress.chapter_notes)
                }
              }, 800)
            }
          }
          if (progress.status === 'completed' || progress.completed_at) {
            setIsCompletedBefore(true)
            setModuleCompletedSuccess(true)
          }
          if (progress.visual_progress && typeof progress.visual_progress.currentStepIndex === 'number') {
            setActiveVisualStepIndex((prev) => (prev === progress.visual_progress.currentStepIndex ? prev : progress.visual_progress.currentStepIndex))
          }
        }
      } catch (err) {
        console.error('Error loading module context:', err)
      } finally {
        setIsLoadingLesson(false)
      }
    }

    if (userId && moduleId) {
      // Restore from instant local cache if present
      const cachedNotes = getCachedBoardNotes(userId, moduleId)
      if (cachedNotes?.fullSummary) {
        setChapterNotes(cachedNotes.fullSummary)
        setLatestBoardSummary(cachedNotes.fullSummary)
        lastSentBoardNotesRef.current = cachedNotes.fullSummary
      }

      loadModuleContext().then(() => {
        setTimeout(() => {
          autoTriggerVisualForConcept(currentConceptIndexRef.current)
          triggerBackgroundSvgPregeneration(currentConceptIndexRef.current)
        }, 1000)
      })
    }
  }, [userId, moduleId])

  // 1c. Zero-loss page unload handler: flush any unsaved chalkboard notes on tab close or route transition
  useEffect(() => {
    const handleUnload = () => {
      if (!userId || !moduleId) return
      const cached = getCachedBoardNotes(userId, moduleId)
      if (cached && cached.isDirty && cached.fullSummary) {
        const payload = JSON.stringify({
          userId,
          moduleId,
          notesText: cached.notesText,
          roughText: cached.roughText,
          fullSummary: cached.fullSummary,
          status: isCompletedBefore || moduleCompletedSuccess ? 'completed' : 'in_progress',
        })

        // Mark clean locally so duplicate unload events don't re-fire
        setCachedBoardNotes({
          ...cached,
          isDirty: false,
        })

        let sent = false
        if (typeof navigator !== 'undefined' && navigator.sendBeacon) {
          try {
            const blob = new Blob([payload], { type: 'application/json' })
            sent = navigator.sendBeacon('/api/student/progress', blob)
          } catch {}
        }
        if (!sent && typeof fetch !== 'undefined') {
          try {
            fetch('/api/student/progress', {
              method: 'POST',
              body: payload,
              headers: { 'Content-Type': 'application/json' },
              keepalive: true,
            }).catch(() => {})
          } catch {}
        }
      }
    }

    window.addEventListener('beforeunload', handleUnload)
    window.addEventListener('pagehide', handleUnload)
    return () => {
      window.removeEventListener('beforeunload', handleUnload)
      window.removeEventListener('pagehide', handleUnload)
    }
  }, [userId, moduleId, isCompletedBefore, moduleCompletedSuccess])

  // 2. Synchronize AI spoken directives to Green Chalkboard and 3D Simulation Viewport
  useEffect(() => {
    if (transcripts.length === 0) return

    const latest = transcripts[transcripts.length - 1]
    if (latest && latest.sender === 'teacher') {
      if (chalkboardRef.current) {
        // Pass transcript ID so GreenChalkboard executes each tag once as streaming chunks arrive
        chalkboardRef.current.handleAiDirective(latest.text, latest.id)
      }

      // Directives execution tracking to prevent repeated triggers during text streaming
      const transcriptId = latest.id || 'turn'

      // Check for [SCENE: <sceneType> | <parameters>]
      const sceneMatches = Array.from(latest.text.matchAll(/\[SCENE:\s*([a-zA-Z0-9_\-]+)(?:\s*\|\s*([^\]]+))?\]/gi))
      for (const sm of sceneMatches) {
        const tag = sm[0]
        const key = `${transcriptId}:${tag}`
        if (!executedSceneDirectivesRef.current.has(key)) {
          executedSceneDirectivesRef.current.add(key)
          const rawType = sm[1].trim()
          const resolvedType = resolveSceneType(rawType)
          const rawParams = sm[2] || ''
          const parsedParams = parseSceneParams(rawParams)
          setActiveSceneType(resolvedType)
          setActiveSceneParams(parsedParams)
        }
      }

      // Check for [UPDATE_SCENE: <parameters>] to dynamically alter values/shapes in active 3D scene
      const updateMatches = Array.from(latest.text.matchAll(/\[UPDATE_SCENE:\s*([^\]]+)\]/gi))
      for (const um of updateMatches) {
        const tag = um[0]
        const key = `${transcriptId}:${tag}`
        if (!executedSceneDirectivesRef.current.has(key)) {
          executedSceneDirectivesRef.current.add(key)
          const updateParams = parseSceneParams(um[1])
          setActiveSceneParams((prev) => ({ ...prev, ...updateParams }))
        }
      }

      // Check for [CLOSE_SCENE]
      if (latest.text.includes('[CLOSE_SCENE]')) {
        const key = `${transcriptId}:[CLOSE_SCENE]`
        if (!executedSceneDirectivesRef.current.has(key)) {
          executedSceneDirectivesRef.current.add(key)
          setActiveSceneType(null)
        }
      }

      // Check for visual events (via parseVisualEventFromDirective)
      const parsedVisualEvent = parseVisualEventFromDirective(latest.text, latest.id)
      if (parsedVisualEvent) {
        const visualKey = `${transcriptId}:visual:${parsedVisualEvent.action}:${JSON.stringify(parsedVisualEvent.parameters)}`
        if (!executedSceneDirectivesRef.current.has(visualKey)) {
          executedSceneDirectivesRef.current.add(visualKey)
          handleVisualAction(parsedVisualEvent.action, parsedVisualEvent.parameters)
        }
      }

      // Check for question directives that require student response (sets awaiting answer guard)
      const questionRegex = /\[(?:QUESTION|CHECKPOINT_QUESTION|BOARD_QUESTION)(?::\s*([^\]]*))?\]|write_chalkboard\s*\(\s*(?:action\s*=\s*)?["']?(?:draw_question|question)["']?/gi
      const questionMatches = Array.from(latest.text.matchAll(questionRegex))
      for (const qm of questionMatches) {
        const tag = qm[0]
        const key = `${transcriptId}:${tag}`
        if (!executedSceneDirectivesRef.current.has(key)) {
          executedSceneDirectivesRef.current.add(key)
          isAwaitingStudentAnswerRef.current = true
          setIsAwaitingStudentAnswer(true)
          hasUserRespondedSinceQuestionRef.current = false
          setAwaitingStudentAnswer(true)
        }
      }

      // Check for answer verdict directives that resolve question & enter verdict review state
      const verdictRegex = /\[(?:VERDICT|ANSWER_VERDICT|CORRECTION)(?::\s*([^\]]*))?\]|write_chalkboard\s*\(\s*(?:action\s*=\s*)?["']?(?:draw_answer_verdict|answer_verdict|verdict)["']?/gi
      const verdictMatches = Array.from(latest.text.matchAll(verdictRegex))
      for (const vm of verdictMatches) {
        const tag = vm[0]
        const key = `${transcriptId}:${tag}`
        if (!executedSceneDirectivesRef.current.has(key)) {
          executedSceneDirectivesRef.current.add(key)
          isAwaitingStudentAnswerRef.current = false
          setIsAwaitingStudentAnswer(false)
          setAwaitingStudentAnswer(false)
          isReviewingVerdictRef.current = true
          setIsReviewingVerdict(true)
        }
      }

      // Directives and tool calls like concept_completed handled via onChalkboardToolCall
      // Transcript matching for [CONCEPT_DONE] is intentionally omitted to avoid premature advancement from verbal mentions.
    } else if (latest && latest.sender === 'user') {
      const userText = (latest.text || '').trim().toLowerCase()
      if (
        userText.startsWith('[') ||
        userText.startsWith('[transition') ||
        userText.startsWith('[session') ||
        userText.startsWith('[student question') ||
        userText.startsWith('[student requested')
      ) {
        return // Never parse internal system transition prompts as student commands!
      }

      if (!/[a-zA-Z0-9\u0900-\u097F]{2,}|\d/.test(userText)) {
        return // Ignore spurious background-noise punctuation or single-char ASR artifacts
      }

      // Student genuinely spoke or typed a response -> unlock wait-for-student gate cleanly
      hasUserRespondedSinceQuestionRef.current = true
      setAwaitingStudentAnswer(false)
      if (/\b(?:solve|batao|solution|explain|help|hint|don'?t know|samajh nahi)\b/i.test(userText)) {
        isAwaitingStudentAnswerRef.current = false
        setIsAwaitingStudentAnswer(false)
      }

      const transcriptId = latest.id || `user_${latest.timestamp || Date.now()}`

      if (isPauseIntent(userText)) {
        const pauseKey = `${transcriptId}:pause`
        if (!executedSceneDirectivesRef.current.has(pauseKey)) {
          executedSceneDirectivesRef.current.add(pauseKey)
          handlePauseClassRef.current?.()
          return
        }
      }

      if (isResumeIntent(userText) && isPaused) {
        const resumeKey = `${transcriptId}:resume`
        if (!executedSceneDirectivesRef.current.has(resumeKey)) {
          executedSceneDirectivesRef.current.add(resumeKey)
          setIsPaused(false)
          handleStartClassRef.current?.()
          return
        }
      }

      const hasDoubtKeyword = /\b(?:doubt|douth|douts|dought|daoubt|daot|shanka|confus|unclear|samajh\s*nahi)\b/i.test(userText)
      const isPureNextCommand =
        isExplicitNextConceptIntent(userText) &&
        !isRepeatIntent(userText) &&
        !isDontUnderstandIntent(userText) &&
        !hasDoubtKeyword

      if (!isPureNextCommand && (isStudentQuestionOrDoubt(userText) || isRepeatIntent(userText) || isDontUnderstandIntent(userText))) {
        hasConfirmedUnderstandingRef.current = false
        studentHasActiveDoubtRef.current = true
        lastVerdictStatusRef.current = 'neutral'
        const doubtVisualKey = `${transcriptId}:doubt_visual`
        if (!executedSceneDirectivesRef.current.has(doubtVisualKey)) {
          executedSceneDirectivesRef.current.add(doubtVisualKey)
          unlockConfusionVisualsForConcept(currentConceptIndexRef.current, userText)
        }
      } else if (isPureNextCommand || isConfirmationOrNextIntent(userText)) {
        studentHasActiveDoubtRef.current = false
        hasConfirmedUnderstandingRef.current = true
        doubtClearedAtMsgCountRef.current = transcriptsRef.current.length
      }

      const userKey = `${transcriptId}:user_ack`

      if (!executedSceneDirectivesRef.current.has(userKey)) {
        if (isPureNextCommand) {
          executedSceneDirectivesRef.current.add(userKey)
          hasConfirmedUnderstandingRef.current = true
          studentHasActiveDoubtRef.current = false
          doubtClearedAtMsgCountRef.current = transcriptsRef.current.length
          lastVerdictStatusRef.current = 'correct'
          isReviewingVerdictRef.current = false
          setIsReviewingVerdict(false)
          isAwaitingStudentAnswerRef.current = false
          setIsAwaitingStudentAnswer(false)
          handleConceptDoneRef.current?.('EXPLICIT_USER_ADVANCE')
          sendTextMessage(
            `[STUDENT REQUESTED NEXT CONCEPT]: Student requested: "${userText}". Transitioning to the next concept page now. Introduce the new concept warmly with an everyday physical intuition hook.`
          )
        }
      }
    }
  }, [transcripts, lessonManifest, activeModule])

  // Automatically sync docked textbook page whenever active concept changes or module finishes loading
  useEffect(() => {
    const totalPgs = bookTotalPagesRef.current || bookTotalPages
    if (!activeModule || !totalPgs) return
    const keyConceptsList = parseKeyConcepts(activeModule?.key_concepts)
    const currConceptTitle = keyConceptsList[currentConceptIndex] || activeModule?.title
    const target = resolveTargetPageForLesson({
      conceptName: currConceptTitle,
      capsuleTitle: activeModule?.title,
      chapterNumber: activeCurriculum?.order_index || activeModule?.order_index,
      classLevel: resolvedClassLevel || activeCurriculum?.class_level || activeModule?.class_level,
      subject: resolvedSubject || activeCurriculum?.category || activeModule?.subject,
      pdfPath: bookPdfUrlRef.current || bookPdfUrl || undefined,
      conceptIndex: currentConceptIndex,
      totalConcepts: Math.max(1, keyConceptsList.length),
      moduleIndex: typeof activeModule?.order_index === 'number' ? activeModule.order_index - 1 : 0,
      totalModules: Math.max(1, siblingModules.length),
      totalPages: totalPgs,
    })
    if (target && target >= 1 && target <= totalPgs) {
      setBookCurrentPage(target)
    }
  }, [currentConceptIndex, activeModule?.id, bookTotalPages, siblingModules.length])

  // Auto-scroll docked textbook when tutor directs student to a page, exercise, or topic in live speech
  useEffect(() => {
    if (transcripts.length === 0) return
    const lastTr = transcripts[transcripts.length - 1]
    if (lastTr && lastTr.sender === 'teacher' && lastTr.text) {
      const totalPgs = bookTotalPagesRef.current || bookTotalPages
      if (totalPgs) {
        const text = lastTr.text
        if (/\b(?:page|pg\.?|exercise|ex\.?|example|fig(?:ure)?\.?)\b/i.test(text)) {
          const keyConceptsList = parseKeyConcepts(activeModule?.key_concepts)
          const currConceptTitle = keyConceptsList[currentConceptIndexRef.current || 0] || activeModule?.title
          const target = resolveTargetPageForLesson({
            content: text,
            conceptName: currConceptTitle,
            capsuleTitle: activeModule?.title,
            chapterNumber: activeCurriculum?.order_index || activeModule?.order_index,
            classLevel: resolvedClassLevel || activeCurriculum?.class_level || activeModule?.class_level,
            subject: resolvedSubject || activeCurriculum?.category || activeModule?.subject,
            pdfPath: bookPdfUrlRef.current || bookPdfUrl || undefined,
            totalPages: totalPgs,
            moduleIndex: typeof activeModule?.order_index === 'number' ? activeModule.order_index - 1 : 0,
            totalModules: Math.max(1, siblingModules.length),
            conceptIndex: currentConceptIndexRef.current || 0,
            totalConcepts: keyConceptsList.length || 1,
          })
          if (target && target >= 1 && target <= totalPgs && target !== bookCurrentPage) {
            setBookCurrentPage(target)
          }
        }
      }
    }
  }, [transcripts])

  // Helper to auto-save visual timeline progress
  const saveVisualProgressToSupabase = async (stepIndex: number, completedStepIds: string[]) => {
    setActiveVisualStepIndex(stepIndex)
    if (!userId || !moduleId) return
    try {
      const supabase = createClient()
      const { error } = await supabase.from('user_progress').upsert(
        {
          user_id: userId,
          syllabus_module_id: moduleId,
          visual_progress: {
            currentStepIndex: stepIndex,
            completedStepIds,
            lastActiveAt: new Date().toISOString(),
          },
        },
        { onConflict: 'user_id,syllabus_module_id' }
      )
      if (error && error.code !== '42703') {
        console.warn('Notice saving visual progress:', error.message)
      }
    } catch (err: any) {
      if (err?.code !== '42703') {
        console.warn('Notice auto-saving visual progress:', err)
      }
    }
  }

  // Helper to handle visual stage actions from Gemini Live
  const handleVisualAction = (action: string, params: Record<string, any>) => {
    // 1. Dispatch through non-blocking event queue
    VisualEventQueue.getInstance().dispatchEvent(
      action as any,
      params,
      typeof params.stepIndex === 'number' ? params.stepIndex : undefined
    )

    // 2. Synchronize classroom state
    if (action === 'SHOW_SCENE') {
      const rawSceneName = (params.sceneType || params.scene || params.value || '').toLowerCase()
      if (rawSceneName) {
        const resolved = resolveSceneType(rawSceneName)
        setActiveSceneType(resolved)
        const extraParams = { ...params }
        delete (extraParams as any).sceneType
        delete (extraParams as any).scene
        delete (extraParams as any).value
        const sceneParams = params.parameters || params.params || extraParams
        setActiveSceneParams(sceneParams)
      }
    } else if (action === 'UPDATE_SCENE') {
      setActiveSceneParams((prev) => ({ ...prev, ...(params.parameters || params.params || params || {}) }))
    } else if (action === 'CLOSE_SCENE') {
      setActiveSceneType(null)
    } else if (action === 'SHOW_MEDIA') {
      const stepIdx = typeof params.stepIndex === 'number' ? params.stepIndex : params.step
      if (typeof stepIdx === 'number' && lessonManifest && stepIdx >= 0 && stepIdx < lessonManifest.steps.length) {
        setActiveVisualStepIndex(stepIdx)
        const step = lessonManifest.steps[stepIdx]
        if (step.type === 'VIDEO' && step.content.video) {
          chalkboardRef.current?.drawVideoCard?.(step.title, step.content.video.description)
        } else if (step.type === 'GRAPH') {
          const gExpr = step.content.graph?.expression || (activeModule?.visual_lesson_plan as any)?.interactive_math_formula || 'x^2 - 3x - 4'
          const cleanFormula = gExpr.replace(/^(?:y|f\(x\))\s*=\s*/i, '').trim()
          const domain = step.content.graph?.domain || [-4, 6]
          const range = step.content.graph?.range || [-8, 8]
          setActiveGraph({
            formula: cleanFormula,
            domain: [Number(domain[0]), Number(domain[1])],
            range: [Number(range[0]), Number(range[1])],
            title: step.content.graph?.title || step.title || 'Mathematical Graph',
          })
          chalkboardRef.current?.drawGraph(step.content.graph?.title || 'linear')
        } else if (step.type === 'DIAGRAM') {
          chalkboardRef.current?.handleAiDirective(`[DIAGRAM: ${step.title}]`)
        } else {
          chalkboardRef.current?.drawFlowchart?.(`${step.title} -> Core Concept Formulation -> Board Application`)
        }
      } else if (params.title) {
        chalkboardRef.current?.drawFlowchart?.(`${params.title} -> Socratic Progression`)
      }
    } else if (action === 'UPDATE_GRAPH') {
      const stepIdx = typeof params.stepIndex === 'number' ? params.stepIndex : params.step
      if (typeof stepIdx === 'number' && lessonManifest && stepIdx >= 0 && stepIdx < lessonManifest.steps.length) {
        setActiveVisualStepIndex(stepIdx)
      }
      chalkboardRef.current?.drawGraph(params.type || params.title || 'linear')
    } else if (action === 'REVEAL_DIAGRAM_STEP') {
      // Dispatched via VisualEventQueue
    } else if (action === 'PLAY_ANIMATION' || action === 'PAUSE_MEDIA') {
      // Dispatched via VisualEventQueue
    } else if (action === 'ASK_CHECK') {
      if (lessonManifest) {
        const checkIdx = lessonManifest.steps.findIndex((s) => s.type === 'QUICK_CHECK')
        if (checkIdx !== -1) setActiveVisualStepIndex(checkIdx)
      }
    } else if (action === 'HIGHLIGHT_BOARD') {
      if (params.text) {
        chalkboardRef.current?.drawHighlightBox(params.text, params.color)
      }
    } else if (action === 'SAVE_LESSON_POSITION') {
      const stepIdx = typeof params.stepIndex === 'number' ? params.stepIndex : activeVisualStepIndex
      saveVisualProgressToSupabase(stepIdx, [])
    }
  }

  const pregenerationQueueRef = useRef<Set<number>>(new Set())
  const inFlightPregenerationRef = useRef<Map<number, Promise<any>>>(new Map())

  // Background SVG Pre-Generation: Disabled per user requirement.
  // Pre-seeded vector diagrams and verified online images take full precedence without background LLM spam.
  const triggerBackgroundSvgPregeneration = useCallback(
    (_activeConceptIdx: number) => {
      // No-op to eliminate background 30s timeouts and 503 high demand spikes
    },
    []
  )

  // Unlock video demonstration and follow-up visual support ONLY when student is confused, asks doubt/repeat, or explicitly requests video
  const unlockConfusionVisualsForConcept = (conceptIdx: number, _reasonText?: string) => {
    if (typeof window === 'undefined') return
    if (videosUnlockedPerConceptRef.current.has(conceptIdx)) return
    videosUnlockedPerConceptRef.current.add(conceptIdx)

    const keyConceptsList: string[] = parseKeyConcepts(activeModule?.key_concepts)
    const targetConcept = keyConceptsList[conceptIdx] || activeModule?.title || ''
    if (!targetConcept) return

    const customPlan = activeModule?.visual_lesson_plan
    const conceptVisuals: any[] = Array.isArray(customPlan?.concept_visuals)
      ? customPlan.concept_visuals
      : Array.isArray(activeModule?.concept_visuals)
      ? activeModule.concept_visuals
      : []
    const matchedConceptVisual =
      conceptVisuals[conceptIdx] ||
      conceptVisuals.find((cv: any) =>
        cv.concept_title?.toLowerCase().includes(targetConcept.toLowerCase()) ||
        targetConcept.toLowerCase().includes(cv.concept_title?.toLowerCase()) ||
        cv.diagram_title?.toLowerCase().includes(targetConcept.toLowerCase())
      )

    const { video_search_query: vidQuery } = buildDetailedEducationalQueries(
      targetConcept,
      activeCurriculum?.title || resolvedTitle,
      matchedConceptVisual,
      resolvedSubject
    )
    if (vidQuery) {
      fetch('/api/diagram/search-video', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: vidQuery }),
      })
        .then((r) => (r.ok ? r.json() : null))
        .then((vData) => {
          const firstVid = vData?.videos?.[0]
          if (firstVid && chalkboardRef.current) {
            chalkboardRef.current.drawVideoCard?.(
              firstVid.title || targetConcept,
              firstVid.description || 'Visual demonstration',
              firstVid.url,
              firstVid.mimeType || 'video/mp4'
            )
          }
        })
        .catch(() => {})
    }
  }

  // 2b. Automatically trigger and guarantee Image-First visualization for the active concept
  const autoTriggerVisualForConcept = (conceptIdx: number, force: boolean = false) => {
    if (!force && renderedVisualConceptsRef.current.has(conceptIdx)) return
    renderedVisualConceptsRef.current.add(conceptIdx)

    const keyConceptsList: string[] = parseKeyConcepts(activeModule?.key_concepts)
    const targetConcept = keyConceptsList[conceptIdx] || activeModule?.title || ''
    if (!targetConcept) return

    if (chalkboardRef.current) {

      // 1. Check if module has a concept-specific custom visual matching active concept title (never blind index to wrong concept)
      const customPlan = activeModule?.visual_lesson_plan
      const conceptVisuals: any[] = Array.isArray(customPlan?.concept_visuals)
        ? customPlan.concept_visuals
        : Array.isArray(activeModule?.concept_visuals)
        ? activeModule.concept_visuals
        : []
      const matchedConceptVisual = findMatchingConceptVisual(
        conceptVisuals,
        targetConcept,
        keyConceptsList,
        conceptIdx
      )

      const conceptSvg = matchedConceptVisual?.svg || matchedConceptVisual?.diagram_svg || customPlan?.steps?.[conceptIdx]?.content?.diagram?.svg
      const conceptTitle = matchedConceptVisual?.diagram_title || matchedConceptVisual?.concept_title || targetConcept
      const conceptCaption = matchedConceptVisual?.what_to_make || targetConcept
      const isLegitGraph = isLegitimateGraphTopic(targetConcept, resolvedSubject)
      const isGraph = Boolean(
        matchedConceptVisual &&
        (matchedConceptVisual.diagram_type === 'graph' || matchedConceptVisual.interactive_math_formula) &&
        isLegitGraph
      )
      const isFlowchart = Boolean(matchedConceptVisual && matchedConceptVisual.diagram_type === 'draw_flowchart')

      // Image-First visual guarantee: even when a concept is graph-eligible, ALWAYS launch 1 clean authentic image first at concept start
      const prefetchedImg = prefetchedImagesRef.current[conceptIdx]
      const conceptImageUrl = matchedConceptVisual?.image_url || matchedConceptVisual?.url || prefetchedImg?.url
      const existingImgCount = imagesRenderedPerConceptRef.current.get(conceptIdx) || 0
      if (conceptImageUrl && existingImgCount === 0) {
        const imageTitle = matchedConceptVisual?.diagram_title || prefetchedImg?.title || conceptTitle
        const imageCaption = matchedConceptVisual?.what_to_make || prefetchedImg?.caption || conceptCaption
        imagesRenderedPerConceptRef.current.set(conceptIdx, 1)
        chalkboardRef.current.drawImage?.(conceptImageUrl, imageTitle, imageCaption)
        triggerBackgroundSvgPregeneration(conceptIdx)
        return
      }

      if (existingImgCount === 0 && !conceptSvg && !isFlowchart) {
        const { image_search_query: startImgQuery } = buildDetailedEducationalQueries(
          targetConcept,
          activeCurriculum?.title || resolvedTitle,
          matchedConceptVisual,
          resolvedSubject
        )
        if (startImgQuery) {
          imagesRenderedPerConceptRef.current.set(conceptIdx, 1)
          fetch('/api/diagram/search-image', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: startImgQuery, limit: 4 }),
          })
            .then((r) => (r.ok ? r.json() : null))
            .then(async (data) => {
              const candidateImages: any[] = data?.images || []
              for (const img of candidateImages) {
                if (!img?.url) continue
                try {
                  const check = await fetch(`/api/diagram/proxy?dataUrl=true&url=${encodeURIComponent(img.url)}`)
                  if (check.ok) {
                    const pData = await check.json()
                    if (pData?.success && pData?.dataURL) {
                      chalkboardRef.current?.drawImage?.(pData.dataURL, conceptTitle, conceptCaption)
                      return
                    }
                  }
                } catch {}
              }
              triggerBackgroundSvgPregeneration(conceptIdx)
            })
            .catch(() => triggerBackgroundSvgPregeneration(conceptIdx))
          return
        }
      }

      if (isGraph) {
        // Do NOT auto-popup graph before initial image; tutor opens MafsGraphCanvas dynamically via plot_mathematical_graph.
        triggerBackgroundSvgPregeneration(conceptIdx)
        return
      }

      if (isFlowchart) {
        chalkboardRef.current.drawFlowchart?.(matchedConceptVisual?.what_to_make || targetConcept)
        triggerBackgroundSvgPregeneration(conceptIdx)
        return
      }

      if (conceptSvg && typeof conceptSvg === 'string' && conceptSvg.includes('<svg')) {
        chalkboardRef.current.drawSvgDiagram?.(conceptTitle, conceptSvg, conceptCaption)
        // Also trigger background pregeneration for next concepts
        triggerBackgroundSvgPregeneration(conceptIdx)
        return
      }

      // If no concept-specific visual exists, but a top-level capsule SVG was provided, ONLY use it for Concept 0 (the first concept), NEVER duplicate it on subsequent concepts!
      const defaultCapsuleSvg = customPlan?.diagram_svg || customPlan?.svg || activeModule?.diagram_svg
      if (conceptIdx === 0 && defaultCapsuleSvg && typeof defaultCapsuleSvg === 'string' && defaultCapsuleSvg.includes('<svg')) {
        chalkboardRef.current.drawSvgDiagram?.(customPlan?.diagram_idea || targetConcept, defaultCapsuleSvg, customPlan?.what_to_make || targetConcept)
        triggerBackgroundSvgPregeneration(conceptIdx)
        return
      }

      const applyDirectiveFallback = (targetConceptName: string, captionText: string) => {
        if (!chalkboardRef.current) return
        const directive = inferConceptVisualDirective(
          targetConceptName,
          resolvedSubject,
          activeCurriculum?.title || resolvedTitle
        )

        if (directive.toolCallAction === 'execute_visual_action' && directive.sceneType) {
          const resolved = resolveSceneType(directive.sceneType)
          setActiveSceneType(resolved)
          setActiveSceneParams(directive.sceneParams || {})
        }

        if (directive.chalkboardAction === 'draw_diagram' && directive.chalkboardContent) {
          chalkboardRef.current.handleAiDirective(`[DIAGRAM: ${directive.chalkboardContent}]`)
        } else if (directive.chalkboardAction === 'draw_graph' && directive.chalkboardContent) {
          if (isLegitimateGraphTopic(targetConceptName, resolvedSubject)) {
            setActiveGraph({
              formula: directive.chalkboardContent,
              title: targetConceptName,
            })
          } else {
            chalkboardRef.current.drawSvgDiagram?.(targetConceptName, '', captionText)
          }
        } else if (directive.chalkboardAction === 'draw_geometry' && directive.chalkboardContent) {
          chalkboardRef.current.drawGeometry?.(directive.chalkboardContent)
        } else if (directive.chalkboardAction === 'draw_flowchart' && directive.chalkboardContent) {
          chalkboardRef.current.drawFlowchart(directive.chalkboardContent)
        } else if (directive.chalkboardAction === 'draw_table' && directive.chalkboardContent) {
          chalkboardRef.current.drawTable?.(directive.chalkboardContent)
        } else if (
          (directive.chalkboardAction === 'draw_numerical' || directive.chalkboardAction === 'numerical') &&
          directive.chalkboardContent
        ) {
          chalkboardRef.current.handleAiDirective(`[NUMERICAL: ${directive.chalkboardContent}]`)
        } else if (
          (directive.chalkboardAction === 'render_svg_diagram' || directive.chalkboardAction === 'draw_svg') &&
          directive.chalkboardContent
        ) {
          const rawContent = directive.chalkboardContent.trim()
          if (rawContent.includes('|') && rawContent.includes('<svg')) {
            const firstPipe = rawContent.indexOf('|')
            const lastPipe = rawContent.lastIndexOf('|')
            if (firstPipe !== -1 && lastPipe !== -1 && lastPipe > firstPipe) {
              const title = rawContent.substring(0, firstPipe).trim()
              const svg = rawContent.substring(firstPipe + 1, lastPipe).trim()
              const caption = rawContent.substring(lastPipe + 1).trim()
              chalkboardRef.current.drawSvgDiagram?.(
                title || targetConceptName,
                svg || '',
                caption || ''
              )
            } else {
              chalkboardRef.current.drawSvgDiagram?.(targetConceptName, rawContent, captionText)
            }
          } else if (rawContent.includes('<svg')) {
            chalkboardRef.current.drawSvgDiagram?.(targetConceptName, rawContent, captionText)
          }
        }
      }

      // 2. Image-First policy: only fetch & render clean educational image on concept start (video unlocked on doubt/confusion/request)
      // 2b. Search online authentic scientific images via /api/diagram/search-image
      if (typeof window !== 'undefined') {
        const handleSuccessData = (data: any) => {
          if (data?.svg && chalkboardRef.current) {
            chalkboardRef.current.drawSvgDiagram?.(
              data.diagram_title || data.concept_title || targetConcept,
              data.svg,
              data.caption || data.what_to_explain || targetConcept,
              true
            )

          } else {
            chalkboardRef.current?.clearDiagramSkeleton?.(targetConcept)
          }
        }

        const handleFailure = (err: any) => {
          console.warn('[Classroom] Notice fetching generated diagram:', err)
          chalkboardRef.current?.clearDiagramSkeleton?.(targetConcept)
        }

        const runFastDiagramGeneration = () => {
          chalkboardRef.current?.drawDiagramSkeleton?.(targetConcept)
          setGeneratingDiagramTitle(targetConcept)

          const genController = new AbortController()
          const genTimer = setTimeout(() => genController.abort(), 25000)

          fetch('/api/diagram/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            signal: genController.signal,
            body: JSON.stringify({
              title: targetConcept,
              conceptTitle: targetConcept,
              conceptIndex: conceptIdx,
              moduleId,
              subject: resolvedSubject,
              classLevel: resolvedClassLevel,
              context: activeCurriculum?.title || resolvedTitle,
              animationType: 'moving_points_and_pulsing_glow',
              isLiveClass: true,
              source: 'live_classroom',
            }),
          })
            .then((res) => {
              clearTimeout(genTimer)
              return res.ok ? res.json() : null
            })
            .then(handleSuccessData)
            .catch(handleFailure)
            .finally(() => {
              clearTimeout(genTimer)
              setGeneratingDiagramTitle(null)
            })
        }

        const rawSearchQuery =
          matchedConceptVisual?.image_search_query ||
          matchedConceptVisual?.image_query ||
          matchedConceptVisual?.diagram_title ||
          targetConcept

        const searchQuery = extractConciseSearchKeyword(rawSearchQuery) || rawSearchQuery

        fetch(`/api/diagram/search-image?q=${encodeURIComponent(searchQuery)}&limit=3`)
          .then((res) => (res.ok ? res.json() : null))
          .then(async (data) => {
            const candidateImages: any[] = data?.images || []
            if (candidateImages.length > 0 && chalkboardRef.current) {
              for (const img of candidateImages) {
                if (!img?.url) continue
                try {
                  const check = await fetch(`/api/diagram/proxy?dataUrl=true&url=${encodeURIComponent(img.url)}`)
                  if (check.ok) {
                    const proxyData = await check.json()
                    if (proxyData.success && proxyData.dataURL) {
                      prefetchedImagesRef.current[conceptIdx] = {
                        url: proxyData.dataURL,
                        title: matchedConceptVisual?.diagram_title || img.title || targetConcept,
                        caption: matchedConceptVisual?.what_to_make || img.description || conceptCaption,
                      }
                      if ((imagesRenderedPerConceptRef.current.get(conceptIdx) || 0) === 0) {
                        imagesRenderedPerConceptRef.current.set(conceptIdx, 1)
                        chalkboardRef.current.drawImage?.(
                          proxyData.dataURL,
                          matchedConceptVisual?.diagram_title || img.title || targetConcept,
                          matchedConceptVisual?.what_to_make || img.description || conceptCaption
                        )
                      }
                      return
                    }
                  }
                } catch {
                  // Try next candidate image
                }
              }
            }

            // Online search yielded no accessible image -> Run Live Class Fast Diagram Generation
            runFastDiagramGeneration()
          })
          .catch((err) => {
            console.warn('[Classroom] Online search error before diagram generation:', err)
            runFastDiagramGeneration()
          })
      }

      // Proactively trigger background SVG pre-generation for subsequent concepts N+1, N+2...
      triggerBackgroundSvgPregeneration(conceptIdx)
    }
  }

  // 3. Auto-save notes to Supabase user_progress.chapter_notes and visual_progress.whiteboard_pages
  const saveNotesToSupabase = async (
    notesToSave?: string,
    forcedStatus?: 'in_progress' | 'completed',
    pausedOverride?: boolean
  ) => {
    saveNotesToSupabaseRef.current = (notes, status) => saveNotesToSupabase(notes, status)
    if (!userId || !moduleId) return
    setNotesSaveStatus('saving')
    try {
      const supabase = createClient()

      let whiteboardData: any = null
      let whiteboardFiles: any = null
      if (typeof window !== 'undefined') {
        try {
          const raw = localStorage.getItem(`whiteboard_pages_${moduleId}`)
          if (raw) whiteboardData = JSON.parse(raw)
          const rawFiles = localStorage.getItem(`whiteboard_pages_${moduleId}_files`)
          if (rawFiles) whiteboardFiles = JSON.parse(rawFiles)
        } catch {}
      }

      const statusToSet = forcedStatus || (isCompletedBefore || moduleCompletedSuccess ? 'completed' : 'in_progress')
      const currentIdxToSave = currentConceptIndexRef.current
      const completedToSave = completedConceptsRef.current
      const isPausedVal = typeof pausedOverride === 'boolean' ? pausedOverride : (isPausedRef.current || isPaused)

      const effectiveNotes = (typeof notesToSave === 'string' && notesToSave.trim())
        ? notesToSave
        : (chalkboardRef.current?.getBoardSummary()?.fullSummary || latestBoardSummary || chapterNotes || '').trim()

      const payload: any = {
        user_id: userId,
        syllabus_module_id: moduleId,
        chapter_notes: effectiveNotes,
        current_concept_index: currentIdxToSave,
        completed_concepts: completedToSave,
        last_covered_concept: lastCoveredConcept,
        status: statusToSet,
        is_paused: isPausedVal,
      }

      if (statusToSet === 'completed') {
        payload.completed_at = new Date().toISOString()
      }

      payload.visual_progress = {
        currentStepIndex: activeVisualStepIndex,
        completedStepIds: [],
        whiteboard_pages: whiteboardData || [],
        whiteboard_files: whiteboardFiles || {},
        lastActiveAt: new Date().toISOString(),
        isPaused: isPausedVal,
      }

      const { error } = await supabase
        .from('user_progress')
        .upsert(payload, { onConflict: 'user_id,syllabus_module_id' })

      if (error) {
        if (isSchemaError(error)) {
          // Graceful fallback if is_paused or visual_progress column is not yet applied on remote table
          const fallback = { ...payload }
          delete fallback.is_paused
          delete fallback.visual_progress
          await supabase.from('user_progress').upsert(fallback, { onConflict: 'user_id,syllabus_module_id' })
        } else {
          console.warn('Notice saving notes to Supabase:', error.message)
        }
      }

      // Mark clean in client-side cache & invalidate server/session progress cache
      invalidateUserProgressCache(userId, moduleId)
      invalidateStudentProgressCache(userId)
      if (effectiveNotes) {
        setCachedBoardNotes({
          userId,
          moduleId,
          notesText: effectiveNotes,
          fullSummary: effectiveNotes,
          updatedAt: new Date().toISOString(),
          isDirty: false,
        })
      }

      setNotesSaveStatus('saved')
    } catch (err) {
      console.error('Error auto-saving chapter notes:', err)
      setNotesSaveStatus('idle')
    }
  }
  saveNotesToSupabaseRef.current = saveNotesToSupabase
  useEffect(() => {
    saveNotesToSupabaseRef.current = saveNotesToSupabase
  })

  // 4. Handle note recorded from chalkboard directives
  const handleNoteRecorded = (note: string) => {
    if (!note || !note.trim()) return

    setChapterNotes((prev) => {
      const trimmed = note.trim()
      if (prev.includes(trimmed)) return prev

      const formatted = prev ? `${prev}\n\n${trimmed}` : trimmed

      // Immediate local cache write (0ms, 0 DB load)
      if (userId && moduleId) {
        setCachedBoardNotes({
          userId,
          moduleId,
          notesText: formatted,
          fullSummary: formatted,
          updatedAt: new Date().toISOString(),
          isDirty: true,
        })
      }

      // Debounce auto-save to cloud with 12s idle debounce
      if (saveTimeoutRef.current) {
        clearTimeout(saveTimeoutRef.current)
      }
      setNotesSaveStatus('saving')
      saveTimeoutRef.current = setTimeout(() => {
        saveNotesToSupabase(formatted)
      }, 12000)

      return formatted
    })
  }

  // 5. Automatic Module Completion & Progression Engine
  const markModuleAsCompleted = async (summaryNote?: string) => {
    if (!userId || !moduleId || isMarkingCompleteRef.current) return
    isMarkingCompleteRef.current = true

    // Flush any pending debounced save
    if (saveTimeoutRef.current) {
      clearTimeout(saveTimeoutRef.current)
      saveTimeoutRef.current = null
    }

    try {
      const supabase = createClient()
      const now = new Date().toISOString()
      const todayStr = now.split('T')[0]
      const keyConcepts: string[] = parseKeyConcepts(activeModule?.key_concepts)

      // Invariant 3: Live chalkboard is single source of truth for notes.
      const boardSummary =
        chalkboardRef.current?.getBoardSummary()?.fullSummary ||
        latestBoardSummary ||
        summaryNote ||
        chapterNotes

      const finalNotes = (boardSummary || '').trim()

      // 1. Update user_progress to completed
      await supabase
        .from('user_progress')
        .upsert(
          {
            user_id: userId,
            syllabus_module_id: moduleId,
            status: 'completed',
            completed_at: now,
            current_concept_index: keyConcepts.length,
            completed_concepts: keyConcepts.length > 0 ? keyConcepts : completedConcepts,
            last_covered_concept:
              keyConcepts[keyConcepts.length - 1] || activeModule?.title || 'Synthesis',
            ...(finalNotes ? { chapter_notes: finalNotes } : {}),
          },
          { onConflict: 'user_id,syllabus_module_id' }
        )

      // Also persist to local cache immediately
      if (finalNotes) {
        setCachedBoardNotes({
          userId,
          moduleId,
          notesText: finalNotes,
          fullSummary: finalNotes,
          updatedAt: now,
          isDirty: false,
        })
        setChapterNotes(finalNotes)
      }

      // 1b. Check if this module completion completes all sibling capsules in this chapter
      const siblingIds = (siblingModules || []).map((m: any) => m.id)
      let chapterWasCompleted = false

      if (siblingIds.length > 0) {
        const { data: siblingProgress } = await supabase
          .from('user_progress')
          .select('syllabus_module_id, status, completed_at')
          .eq('user_id', userId)
          .in('syllabus_module_id', siblingIds)

        const completedSiblingIds = new Set(
          (siblingProgress || [])
            .filter((p: any) => p.status === 'completed' || !!p.completed_at)
            .map((p: any) => p.syllabus_module_id)
        )
        completedSiblingIds.add(moduleId)

        if (completedSiblingIds.size >= siblingIds.length) {
          chapterWasCompleted = true
        }
      }

      // Automatically unlock next capsule or next chapter's first capsule
      const nextMod = siblingModules.find(
        (m) => m.order_index > (activeModule?.order_index || 0)
      )

      if (nextMod) {
        await supabase
          .from('user_progress')
          .upsert(
            {
              user_id: userId,
              syllabus_module_id: nextMod.id,
              status: 'in_progress',
              started_at: now,
            },
            { onConflict: 'user_id,syllabus_module_id' }
          )
      } else if (chapterWasCompleted && nextChapterInfo?.firstModuleId) {
        // Unlock first capsule of next chapter
        await supabase
          .from('user_progress')
          .upsert(
            {
              user_id: userId,
              syllabus_module_id: nextChapterInfo.firstModuleId,
              status: 'in_progress',
              started_at: now,
            },
            { onConflict: 'user_id,syllabus_module_id' }
          )

        // Ensure student is active in the next chapter's curriculum
        if (nextChapterInfo.chapterId) {
          await supabase
            .from('enrollments')
            .upsert(
              {
                user_id: userId,
                curriculum_id: nextChapterInfo.chapterId,
                status: 'active',
                enrolled_at: now,
              },
              { onConflict: 'user_id,curriculum_id' }
            )
        }
      }

      // 2. Fetch and increment profiles learning minutes, classes taken, and completed chapters
      if (!isCompletedBefore) {
        const { data: prof } = await supabase
          .from('profiles')
          .select('total_classes_taken, total_learning_minutes, current_streak, last_active_date, completed_chapters_count')
          .eq('id', userId)
          .single()

        const currentClasses = prof?.total_classes_taken || 0
        const currentMinutes = prof?.total_learning_minutes || 0
        const estimatedMins = activeModule?.estimated_minutes || 15

        const profileUpdate: Record<string, any> = {
          total_classes_taken: currentClasses + 1,
          total_learning_minutes: currentMinutes + estimatedMins,
          last_active_date: todayStr,
          updated_at: now,
        }

        if (chapterWasCompleted) {
          // Recalculate true completed chapters across all curriculums (using high-speed dataCache)
          const { data: allUserProgress } = await supabase
            .from('user_progress')
            .select('syllabus_module_id, status, completed_at')
            .eq('user_id', userId)
            .or('status.eq.completed,completed_at.not.is.null')

          const allDone = new Set((allUserProgress || []).map((p: any) => p.syllabus_module_id))
          allDone.add(moduleId)

          const cCounts = await getCachedCurriculumModuleCounts(supabase)
          const doneModuleIds = Array.from(allDone)
          const cDoneCounts = new Map<string, number>()

          if (doneModuleIds.length > 0) {
            const { data: userDoneMods } = await supabase
              .from('syllabus_modules')
              .select('id, curriculum_id')
              .in('id', doneModuleIds)

            ;(userDoneMods || []).forEach((m: any) => {
              if (m.curriculum_id) {
                cDoneCounts.set(m.curriculum_id, (cDoneCounts.get(m.curriculum_id) || 0) + 1)
              }
            })
          }

          let calculatedDone = 0
          const doneChapterIds: string[] = []
          cCounts.forEach((total, cId) => {
            const done = cDoneCounts.get(cId) || 0
            if (total > 0 && done >= total) {
              calculatedDone += 1
              doneChapterIds.push(cId)
            }
          })

          profileUpdate.completed_chapters_count = calculatedDone
          profileUpdate.completed_chapter_ids = doneChapterIds
        }

        const { error: profErr } = await supabase
          .from('profiles')
          .update(profileUpdate)
          .eq('id', userId)

        if (profErr && profErr.code === '42703') {
          delete profileUpdate.completed_chapter_ids
          const { error: secondErr } = await supabase.from('profiles').update(profileUpdate).eq('id', userId)
          if (secondErr && secondErr.code === '42703') {
            delete profileUpdate.completed_chapters_count
            await supabase.from('profiles').update(profileUpdate).eq('id', userId)
          }
        }
      }

      setIsCompletedBefore(true)
      setModuleCompletedSuccess(true)
      setNotesSaveStatus('saved')

      // Invalidate all student progress, profile & enrollment caches so dashboard and profile load fresh data
      invalidateUserProgressCache(userId, moduleId)
      invalidateUserProfileCache(userId)
      invalidateUserEnrollmentsCache(userId)
      invalidateStudentProgressCache(userId)

      // 3. Companion guidance celebration (strictly zero emojis)
      triggerCompanionGuidance({
        animation: 'excited',
        expression: 'joyful-wide',
        mood: 'celebrate',
        message: nextMod
          ? `Outstanding work! You completed "${activeModule?.title || 'this lesson'}". Ready for "${nextMod.title}"?`
          : `Great work! You have finished every lesson in this chapter.`,
        autoDismissMs: 12000,
      })
    } catch (err) {
      console.error('Error marking module as completed:', err)
    } finally {
      setTimeout(() => {
        isMarkingCompleteRef.current = false
      }, 5000)
    }
  }

  // Helper to trigger automatic module progression to next capsule, next chapter, or quiz
  const triggerModuleCompletionAndAdvance = () => {
    let nextMod: any = null
    if (siblingModules.length > 0 && activeModule?.id) {
      const currIdx = siblingModules.findIndex((m) => m.id === activeModule.id)
      if (currIdx >= 0 && currIdx < siblingModules.length - 1) {
        nextMod = siblingModules[currIdx + 1]
      }
    }
    if (!nextMod && siblingModules.length > 0) {
      nextMod = siblingModules.find(
        (m) => (m.order_index ?? 0) > (activeModule?.order_index ?? 0)
      )
    }

    if (nextMod) {
      triggerCompanionGuidance({
        animation: 'excited',
        expression: 'joyful-wide',
        mood: 'celebrate',
        message: `Outstanding work! You completed "${activeModule?.title || 'this lesson'}". Advancing to "${nextMod.title}" in 3 seconds...`,
        autoDismissMs: 6000,
      })
      setTimeout(() => {
        leaveTo(`/dashboard/${userId}/class/${nextMod.id}`)
      }, 3000)
    } else if (nextChapterInfo?.firstModuleId) {
      triggerCompanionGuidance({
        animation: 'excited',
        expression: 'joyful-wide',
        mood: 'celebrate',
        message: `Outstanding work! You completed this chapter. Advancing to Chapter: "${nextChapterInfo.chapterTitle}" in 3 seconds...`,
        autoDismissMs: 6000,
      })
      setTimeout(() => {
        leaveTo(`/dashboard/${userId}/class/${nextChapterInfo.firstModuleId}`)
      }, 3000)
    } else {
      triggerCompanionGuidance({
        animation: 'excited',
        expression: 'joyful-wide',
        mood: 'celebrate',
        message: `Great work! You have finished every lesson. Starting your quiz now.`,
        autoDismissMs: 5000,
      })
      setTimeout(() => {
        endCall()
        setQuizOpen(true)
      }, 2000)
    }
  }

  // Helper to advance to next concept: switches/creates whiteboard page, triggers visual, saves progress, and feeds single concept micro-dossier to tutor
  const advanceToNextConcept = async (nextIdx: number, completedList: string[]) => {
    const keyConcepts: string[] = parseKeyConcepts(activeModule?.key_concepts)
    if (keyConcepts.length === 0) return

    if (nextIdx >= keyConcepts.length) {
      const allDone = Array.from(new Set([...completedList, ...keyConcepts]))
      completedConceptsRef.current = allDone
      setCompletedConcepts(allDone)
      if (userId && moduleId) {
        saveVisualProgressToSupabase(keyConcepts.length - 1, allDone)
      }
      markModuleAsCompleted()
      triggerModuleCompletionAndAdvance()
      return
    }

    const nextConceptTitle = keyConcepts[nextIdx] || activeModule?.title || 'Concept'

    lastVerdictStatusRef.current = 'neutral'
    isReviewingVerdictRef.current = false
    setIsReviewingVerdict(false)
    isAwaitingStudentAnswerRef.current = false
    setIsAwaitingStudentAnswer(false)
    hasConfirmedUnderstandingRef.current = false
    studentHasActiveDoubtRef.current = false
    doubtClearedAtMsgCountRef.current = transcriptsRef.current.length

    currentConceptIndexRef.current = nextIdx
    setCurrentConceptIndex(nextIdx)
    setLastCoveredConcept(nextConceptTitle)
    setIsCompletedBefore(false)
    setModuleCompletedSuccess(false)

    const totalPgs = bookTotalPagesRef.current || bookTotalPages
    if (totalPgs) {
      const targetPg = resolveTargetPageForLesson({
        conceptName: nextConceptTitle,
        capsuleTitle: activeModule?.title,
        chapterNumber: activeCurriculum?.order_index || activeModule?.order_index,
        classLevel: resolvedClassLevel || activeCurriculum?.class_level || activeModule?.class_level,
        subject: resolvedSubject || activeCurriculum?.category || activeModule?.subject,
        pdfPath: bookPdfUrlRef.current || bookPdfUrl || undefined,
        conceptIndex: nextIdx,
        totalConcepts: keyConcepts.length,
        moduleIndex: typeof activeModule?.order_index === 'number' ? activeModule.order_index - 1 : 0,
        totalModules: Math.max(1, siblingModules.length),
        totalPages: totalPgs,
      })
      setBookCurrentPage(targetPg)
    }

    const norm = (s: string) =>
      String(s || '')
        .toLowerCase()
        .replace(/^[\s\(\[\{\"\']+|[\s\)\]\}\"\']+$/g, '')
        .replace(/^concept\s*\d*[:\-\s]*/i, '')
        .replace(/^\d+[\.\:\)\-]\s*/, '')
        .replace(/[^a-z0-9]/g, '')

    // Guarantee all concepts prior to nextIdx are permanently marked completed
    const priorConcepts = keyConcepts.slice(0, nextIdx)
    const updated = Array.from(new Set([...completedList, ...priorConcepts]))
    completedConceptsRef.current = updated
    setCompletedConcepts(updated)

    // Graph lifecycle cleanup: dismiss active graph when transitioning concepts
    setActiveGraph(null)

    // Reset pedagogical state for new concept
    pedagogicalStateManager?.resetStages?.()

    // Persist instant session state locally first
    if (moduleId) {
      saveSessionState(moduleId, {
        currentConceptIndex: nextIdx,
        completedConcepts: updated,
        currentStage: 'REAL_LIFE_INTUITION',
        chalkboardPageIndex: nextIdx,
        lastCoveredConcept: nextConceptTitle,
      })
    }

    // Whiteboard 1-Concept-Per-Page: Switch to concept's dedicated page (creates clean new page with header if needed)
    await chalkboardRef.current?.goToPage?.(nextIdx, nextConceptTitle)

    // Auto-generate & render visual diagram for this concept proactively
    autoTriggerVisualForConcept(nextIdx, true)
    triggerBackgroundSvgPregeneration(nextIdx)

    // Update Supabase user_progress and invalidate caches immediately
    if (userId && moduleId) {
      const latestNotesForConcept = (chalkboardRef.current?.getBoardSummary()?.fullSummary || latestBoardSummary || chapterNotes || '').trim()
      invalidateUserProgressCache(userId, moduleId)
      invalidateStudentProgressCache(userId)
      const supabase = createClient()
      await supabase
        .from('user_progress')
        .upsert(
          {
            user_id: userId,
            syllabus_module_id: moduleId,
            current_concept_index: nextIdx,
            completed_concepts: updated,
            last_covered_concept: nextConceptTitle,
            status: 'in_progress',
            ...(latestNotesForConcept ? { chapter_notes: latestNotesForConcept } : {}),
          },
          { onConflict: 'user_id,syllabus_module_id' }
        )
        .then(() => {})
    }

    const newPercent =
      keyConcepts.length > 0 ? Math.round((updated.length / keyConcepts.length) * 100) : 0

    // Companion guidance (strictly zero emojis)
    triggerCompanionGuidance({
      animation: 'working',
      expression: 'attentive-left',
      mood: 'thinking',
      message: `Advancing to Concept ${nextIdx + 1}: "${nextConceptTitle}" on Page ${nextIdx + 1}. Progress is ${newPercent}%.`,
      autoDismissMs: 5000,
    })

    // Parse worked examples and misconceptions for single concept micro-dossier
    const rawWorkedExamples = activeModule?.worked_examples
    let parsedWorkedExamples: any[] = []
    if (Array.isArray(rawWorkedExamples)) {
      parsedWorkedExamples = rawWorkedExamples
    } else if (typeof rawWorkedExamples === 'string') {
      try {
        const p = JSON.parse(rawWorkedExamples)
        if (Array.isArray(p)) parsedWorkedExamples = p
      } catch {
        parsedWorkedExamples = []
      }
    }

    const rawMisconceptions = activeModule?.common_misconceptions
    let parsedMisconceptions: string[] = []
    if (Array.isArray(rawMisconceptions)) {
      parsedMisconceptions = rawMisconceptions
    } else if (typeof rawMisconceptions === 'string') {
      try {
        const p = JSON.parse(rawMisconceptions)
        if (Array.isArray(p)) parsedMisconceptions = p
      } catch {
        parsedMisconceptions = []
      }
    }

    const chapterName = activeCurriculum?.title || resolvedTitle || 'Chapter'

    const nextDossier = buildSingleConceptMicroDossier(
      nextIdx,
      keyConcepts,
      activeModule,
      resolvedBoard,
      resolvedClassLevel,
      resolvedSubject,
      chapterName,
      parsedWorkedExamples,
      parsedMisconceptions
    )

    const isNextLegitGraph = isLegitimateGraphTopic(nextConceptTitle, resolvedSubject)
    const nextVisualCue = isNextLegitGraph
      ? `search_and_show_image(query="<full detailed 10-25 word educational search query for ${nextConceptTitle} specifying exact components, apparatus, or anatomical structures>", title="${nextConceptTitle}", caption="Visual illustration") or plot_mathematical_graph(formula="...", title="${nextConceptTitle}") with worked derivations`
      : `search_and_show_image(query="<full detailed 10-25 word educational search query for ${nextConceptTitle} specifying exact components, apparatus, or anatomical structures>", title="${nextConceptTitle}", caption="Visual illustration")`

    const isNextMath = (resolvedSubject || '').toLowerCase().includes('math')
    // Notify Gemini Live with single concept micro-dossier and instructions
    sendTextMessage(
      `[TEACHING STATE: Active Concept ${nextIdx + 1} of ${keyConcepts.length} ("${nextConceptTitle}")]
[TRANSITION TO NEXT CONCEPT - PAGE ${nextIdx + 1}]:
We are now teaching Concept ${nextIdx + 1} of ${keyConcepts.length}: "${nextConceptTitle}".
The chalkboard is ready on Page ${nextIdx + 1} with the topic title written in chalk.

PEDAGOGICAL GUIDANCE:
1. FOCUS EXCLUSIVELY on "${nextConceptTitle}". Teach conversationally in crisp 2 to 3 sentence micro-turns using the simplest everyday words and relatable student analogies.
2. WRITE AS YOU SPEAK (NEVER explain silently without writing/visualizing!): call write_chalkboard(action="draw_note", content="<core ${isNextMath ? 'concept or formula' : 'law or mechanism'}>", color="white") or plot_mathematical_graph / draw_shape / draw_flowchart / render_svg_diagram right alongside your voice.
3. VISUAL FREEDOM (IMAGE-FIRST, VIDEO ON CONFUSION/REQUEST): Show clean educational visuals via search_and_show_image or plot_mathematical_graph first. Whenever the student asks doubts, struggles, or requests more visuals, also call search_and_show_video and render_svg_diagram freely!
4. ${isNextMath ? 'NEVER ask "did you understand the definition?" in Maths — ask "Did you follow that concept / method?"' : 'Check understanding after finishing your explanation.'} Pose ONE checkpoint question with write_chalkboard(action="draw_question", content="<question>") (and show Exercise X.Y • Q.N clearly for textbook problems).
5. HARD STOP: Wait for the student's response before solving or moving forward.

${nextDossier}`
    )
  }

  // 6. Rewind / Concept Jump Navigation (Bidirectional sync with Supabase and UI)
  const handleConceptGoto = async (target: number | string) => {
    const keyConcepts: string[] = parseKeyConcepts(activeModule?.key_concepts)
    if (keyConcepts.length === 0) return

    let targetIdx = 0

    if (typeof target === 'number') {
      targetIdx = Math.max(0, Math.min(target - 1, Math.max(0, keyConcepts.length - 1)))
    } else {
      const lower = String(target || '').toLowerCase().trim()
      if (lower === 'start' || lower === 'beginning' || lower === 'first') {
        targetIdx = 0
      } else {
        const found = keyConcepts.findIndex(
          (c) => c.toLowerCase().includes(lower) || lower.includes(c.toLowerCase())
        )
        if (found >= 0) {
          targetIdx = found
        } else {
          const conceptNumMatch = lower.match(/\bconcept\s*#?\s*(\d+)\b/i)
          if (conceptNumMatch && conceptNumMatch[1]) {
            const num = parseInt(conceptNumMatch[1], 10)
            if (!isNaN(num) && num > 0) {
              targetIdx = Math.max(0, Math.min(num - 1, Math.max(0, keyConcepts.length - 1)))
            }
          }
        }
      }
    }

    const targetConceptName = keyConcepts[targetIdx] || activeModule?.title || 'Concept'

    lastVerdictStatusRef.current = 'neutral'
    isReviewingVerdictRef.current = false
    setIsReviewingVerdict(false)
    isAwaitingStudentAnswerRef.current = false
    setIsAwaitingStudentAnswer(false)
    hasConfirmedUnderstandingRef.current = false
    studentHasActiveDoubtRef.current = false
    doubtClearedAtMsgCountRef.current = transcriptsRef.current.length

    currentConceptIndexRef.current = targetIdx
    setCurrentConceptIndex(targetIdx)
    setLastCoveredConcept(targetConceptName)
    setIsCompletedBefore(false)
    setModuleCompletedSuccess(false)

    const totalPgs = bookTotalPagesRef.current || bookTotalPages
    if (totalPgs) {
      const targetPg = resolveTargetPageForLesson({
        conceptName: targetConceptName,
        capsuleTitle: activeModule?.title,
        chapterNumber: activeCurriculum?.order_index || activeModule?.order_index,
        classLevel: resolvedClassLevel || activeCurriculum?.class_level || activeModule?.class_level,
        subject: resolvedSubject || activeCurriculum?.category || activeModule?.subject,
        pdfPath: bookPdfUrlRef.current || bookPdfUrl || undefined,
        conceptIndex: targetIdx,
        totalConcepts: keyConcepts.length,
        moduleIndex: typeof activeModule?.order_index === 'number' ? activeModule.order_index - 1 : 0,
        totalModules: Math.max(1, siblingModules.length),
        totalPages: totalPgs,
      })
      setBookCurrentPage(targetPg)
    }

    // Whiteboard 1-Concept-Per-Page: Switch to concept's dedicated page
    chalkboardRef.current?.goToPage?.(targetIdx, targetConceptName)
    // Auto-generate & render visual diagram for this concept
    autoTriggerVisualForConcept(targetIdx)

    try {
      invalidateUserProgressCache(userId, moduleId)
      invalidateStudentProgressCache(userId)
      const supabase = createClient()
      await supabase
        .from('user_progress')
        .upsert(
          {
            user_id: userId,
            syllabus_module_id: moduleId,
            current_concept_index: targetIdx,
            completed_concepts: completedConceptsRef.current,
            last_covered_concept: targetConceptName,
            status: 'in_progress',
            completed_at: null,
          },
          { onConflict: 'user_id,syllabus_module_id' }
        )

      const newPercent =
        keyConcepts.length > 0 ? Math.round((completedConceptsRef.current.length / keyConcepts.length) * 100) : 0

      triggerCompanionGuidance({
        animation: 'listening',
        expression: 'neutral',
        mood: 'thinking',
        message: targetIdx === 0
          ? `Rewound to start. Teaching Concept 1: "${targetConceptName}".`
          : `Jumped to Concept ${targetIdx + 1}: "${targetConceptName}". Progress is ${newPercent}%.`,
        autoDismissMs: 5000,
      })

      sendTextMessage(
        `[JUMP TO CONCEPT ${targetIdx + 1} - PAGE ${targetIdx + 1}]:
The student navigated directly to Concept ${targetIdx + 1} of ${keyConcepts.length}: "${targetConceptName}".
The whiteboard has switched to Page ${targetIdx + 1} with the header "CONCEPT ${targetIdx + 1}: ${targetConceptName}".

CRITICAL INSTRUCTIONS:
1. FOCUS EXCLUSIVELY on this single concept: "${targetConceptName}". Do NOT repeat previous concepts.
2. Introduce "${targetConceptName}" with an engaging real-life physical intuition hook (2-3 sentences max) and write on the board: write_chalkboard(action="draw_note", content="Intuition: <hook>", color="botanical").
3. HARD STOP: Ask if the student understood the intuition, and wait for their response.`
      )
    } catch (err) {
      console.error('Failed to rewind concept in database:', err)
    }
  }

  // 7. Concept Tracking Callbacks: auto-save progress and resume state
  const handleConceptFocus = (conceptName: string | number) => {
    const keyConcepts: string[] = parseKeyConcepts(activeModule?.key_concepts)
    if (keyConcepts.length === 0) return

    let targetIdx = -1

    if (typeof conceptName === 'number') {
      targetIdx = Math.max(0, Math.min(conceptName - 1, keyConcepts.length - 1))
    } else {
      const raw = String(conceptName || '').trim()
      // STRICT: Must explicitly state "concept <num>", e.g. "Concept 2" or "Concept #2".
      // NEVER match arbitrary standalone numbers like "4 m/s", "Step 4", "Example 4"!
      const numMatch = raw.match(/\bconcept\s*#?\s*(\d+)\b/i)
      if (numMatch && numMatch[1]) {
        const parsedNum = parseInt(numMatch[1], 10)
        if (parsedNum >= 1 && parsedNum <= keyConcepts.length) {
          targetIdx = parsedNum - 1
        }
      }

      if (targetIdx === -1) {
        const norm = (s: string) =>
          String(s || '')
            .toLowerCase()
            .replace(/^[\s\(\[\{\"\']+|[\s\)\]\}\"\']+$/g, '')
            .replace(/^concept\s*\d*[:\-\s]*/i, '')
            .replace(/^\d+[\.\:\)\-]\s*/, '')
            .replace(/[^a-z0-9]/g, '')

        const targetNorm = norm(raw)
        // Only match if targetNorm has substantial length (at least 4 chars) to prevent accidental partial substring match
        if (targetNorm && targetNorm.length >= 4) {
          const matchedIdx = keyConcepts.findIndex((c) => {
            const cNorm = norm(c)
            return cNorm === targetNorm || (cNorm.length >= 6 && targetNorm.length >= 6 && (cNorm.includes(targetNorm) || targetNorm.includes(cNorm)))
          })
          if (matchedIdx >= 0) {
            targetIdx = matchedIdx
          }
        }
      }

      // CRITICAL: If no valid concept was matched, DO NOT jump or advance!
      if (targetIdx === -1) {
        return
      }
    }

    // Concept focus: visual indicator and guidance only. NEVER jump or advance concepts automatically!
    const targetConceptName = keyConcepts[targetIdx] || ''
    if (targetConceptName && targetIdx !== currentConceptIndexRef.current) {
      triggerCompanionGuidance({
        animation: 'listening',
        expression: 'attentive-left',
        mood: 'thinking',
        message: `Currently focusing on Concept ${currentConceptIndexRef.current + 1}: "${keyConcepts[currentConceptIndexRef.current]}". We will proceed to "${targetConceptName}" once current concept is mastered.`,
        autoDismissMs: 4000,
      })
    }
  }

  const handleConceptDone = (conceptName?: string): { status: string; reason?: string } => {
    handleConceptDoneRef.current = handleConceptDone
    isReviewingVerdictRef.current = false
    setIsReviewingVerdict(false)

    const keyConcepts: string[] = parseKeyConcepts(activeModule?.key_concepts)
    if (keyConcepts.length === 0) return { status: 'skipped', reason: 'No key concepts loaded.' }

    // Sequential progression: complete the current active concept
    const currentIdx = currentConceptIndexRef.current
    let matchedIdx = currentIdx

    const isExplicitUserCommand =
      conceptName === 'EXPLICIT_USER_ADVANCE' ||
      isExplicitNextConceptIntent(conceptName || '')

    if (!isExplicitUserCommand) {
      // Guard 0: Never self-advance or nudge if student is awaiting answer with no response yet or mic is muted
      if (isAwaitingStudentAnswerRef.current && !hasUserRespondedSinceQuestionRef.current) {
        console.warn(`[Classroom Answer Gate] Blocked concept_completed for Concept ${currentIdx + 1}: waiting for student response to posted question.`)
        return {
          status: 'blocked_waiting_for_student',
          reason: 'Wait silently for the student to answer the active question before completing this concept.',
        }
      }

      // Guard 1: Active student doubt or repeat/re-explain request
      if (studentHasActiveDoubtRef.current) {
        console.warn(`[Classroom Socratic Guard] Blocked concept_completed for Concept ${currentIdx + 1} ("${keyConcepts[currentIdx]}"). Student has an active doubt or re-explanation request.`)
        if (!isMutedRef.current) {
          sendTextMessage(
            `[PEDAGOGICAL DOUBT GUARD]: You called concept_completed, but the student has an active doubt or asked to explain the concept again!
CRITICAL INVARIANT:
1. You MUST NOT advance to the next concept or teach upcoming concepts on the current page.
2. Address their doubt thoroughly with clarity and patience on Concept ${currentIdx + 1} first.
3. Only after the student confirms their doubt is cleared or solves the checkpoint can you call concept_completed.`
          )
        }
        return {
          status: 'blocked_active_doubt',
          reason: 'Student has an active doubt on the current concept. Resolve it first and confirm understanding before advancing.',
        }
      }

      // Guard 2: Inspect student transcripts AFTER the last cleared doubt / confirmation
      const recentStudentTranscripts = transcriptsRef.current
        .slice(doubtClearedAtMsgCountRef.current)
        .filter((t) => t.sender === 'user')
        .slice(-3)
      const hasUnresolvedRecentDoubt = recentStudentTranscripts.some((t) =>
        (isStudentQuestionOrDoubt(t.text) && !isExplicitNextConceptIntent(t.text)) ||
        isRepeatIntent(t.text) ||
        isDontUnderstandIntent(t.text)
      )
      if (hasUnresolvedRecentDoubt && !hasConfirmedUnderstandingRef.current && lastVerdictStatusRef.current !== 'correct') {
        studentHasActiveDoubtRef.current = true
        console.warn(`[Classroom Socratic Guard] Blocked concept_completed: recent student transcript contains doubt/question.`)
        if (!isMutedRef.current) {
          sendTextMessage(
            `[PEDAGOGICAL DOUBT GUARD]: The student recently asked a question or expressed doubt on Concept ${currentIdx + 1}. Answer their doubt on the current chalkboard first before calling concept_completed!`
          )
        }
        return {
          status: 'blocked_active_doubt',
          reason: 'Recent student message contains an unresolved question or doubt on this concept.',
        }
      }

      // Guard 3: Ensure linked textbook exercises/questions for this concept were actually asked/solved on board
      const rawExercises = activeModule?.textbook_exercises
      const textbookExercises: any[] = Array.isArray(rawExercises) ? rawExercises : []
      const allExQuestions = textbookExercises.flatMap((ex: any) =>
        (ex.questions || []).map((q: any) => ({ ...q, exercise_number: ex.exercise_number, exercise_title: ex.exercise_title }))
      )
      const conceptNameStr = keyConcepts[currentIdx] || ''
      const conceptTokens = conceptNameStr
        .toLowerCase()
        .replace(/[^a-z0-9\s]/g, ' ')
        .split(/\s+/)
        .filter((w) => w.length >= 3 && !['the', 'and', 'for', 'with', 'into', 'from', 'using', 'concept'].includes(w))
      const directMatchedEx = allExQuestions.filter((q: any) => {
        const hay = `${q.question || ''} ${q.solution_method || ''} ${q.exercise_title || ''}`.toLowerCase()
        return hay.includes(conceptNameStr.toLowerCase()) || conceptTokens.some((tok) => hay.includes(tok))
      })
      const perSlice = allExQuestions.length > 0 && keyConcepts.length > 0
        ? Math.max(1, Math.ceil(allExQuestions.length / keyConcepts.length))
        : 0
      const linkedExercisesCount = directMatchedEx.length > 0
        ? directMatchedEx.length
        : allExQuestions.slice(currentIdx * perSlice, (currentIdx + 1) * perSlice).length
      const solvedOrAskedCount = askedOrSolvedExercisesPerConceptRef.current.get(currentIdx) || 0

      if (linkedExercisesCount > 0 && solvedOrAskedCount === 0 && !hasConfirmedUnderstandingRef.current) {
        console.warn(`[Classroom Exercise Guard] Blocked concept_completed for Concept ${currentIdx + 1}: linked textbook exercises not yet posed/solved on board.`)
        if (!isMutedRef.current) {
          sendTextMessage(
            `[EXERCISE COMPLETENESS GUARD]: Concept ${currentIdx + 1} ("${conceptNameStr}") has linked textbook exercise problems that have not been asked or solved on the chalkboard yet. Write and pose the Exercise question clearly with Exercise X.Y • Q.N via write_chalkboard(action="draw_question", ...), let the student attempt it, and solve it step-by-step via draw_numerical before calling concept_completed!`
          )
        }
        return {
          status: 'blocked_missing_exercise',
          reason: 'Pose and walk through an active chapter exercise question before completing this concept.',
        }
      }

      // Programmatic Socratic Stage 1-4 Gating:
      // Verify that the chalkboard has actually posed a checkpoint question or evaluated student answer on this page
      const currentBoard = chalkboardRef.current?.getCompactBoardContext?.(currentIdx) || ''
      const hasCheckpointQuestion =
        currentBoard.includes('Active Question on Board') ||
        currentBoard.includes('Checkpoint Question') ||
        currentBoard.includes('CHECKPOINT QUESTION') ||
        currentBoard.includes('Question:') ||
        currentBoard.includes('Stage 5') ||
        currentBoard.includes('Stage 6') ||
        currentBoard.includes('Verdict:') ||
        currentBoard.includes('Student:') ||
        lastVerdictStatusRef.current === 'correct' ||
        hasConfirmedUnderstandingRef.current

      if (!hasCheckpointQuestion && !hasConfirmedUnderstandingRef.current) {
        const isCurrMath = (resolvedSubject || '').toLowerCase().includes('math')
        console.warn(`[Classroom Socratic Guard] Blocked premature concept completion for Concept ${currentIdx + 1} ("${keyConcepts[currentIdx]}"). Has not reached Stage 5/6 checkpoint question.`)
        if (!isMutedRef.current) {
          sendTextMessage(
            `[PEDAGOGICAL CADENCE GUARD]: You called concept_completed before completing Concept ${currentIdx + 1}: "${keyConcepts[currentIdx]}".
CRITICAL DIRECTIVE:
1. You CANNOT advance or skip concepts during Stages 1 to 4!
2. Teach in concise 2 to 3 sentence conversational micro-turns while writing on the board (${isCurrMath ? 'core theorem/method and worked example/exercise' : 'formal scientific law/mechanism and worked numerical'}), then pose ONE focused checkpoint question with write_chalkboard(action="draw_question", ...).
3. Only after evaluating my answer can you call concept_completed.`
          )
        }
        return {
          status: 'blocked_premature_stage',
          reason: 'Complete the current concept explanation and checkpoint question on this page first.',
        }
      }

      // Mandatory Pedagogical Understanding Checkpoint Guard:
      if (!hasConfirmedUnderstandingRef.current && lastVerdictStatusRef.current !== 'correct') {
        console.warn(`[Classroom Socratic Guard] Blocked concept_completed for Concept ${currentIdx + 1} ("${keyConcepts[currentIdx]}"). Student has not confirmed understanding yet.`)
        if (!isMutedRef.current) {
          sendTextMessage(
            `[PEDAGOGICAL CHECKPOINT GUARD]: You called concept_completed before verifying student understanding for Concept ${currentIdx + 1}: "${keyConcepts[currentIdx]}".
MANDATORY INVARIANT:
1. After explaining or solving a problem, you MUST explicitly ask: "Did you understand this concept, or should we solve another problem together?" (or in Hindi/Hinglish: "Kya yeh concept samajh aaya, ya koi doubt hai?").
2. HARD STOP: You MUST stop speaking completely and wait for the student's confirmation.
3. You are strictly forbidden from calling concept_completed until the student explicitly answers and confirms they understood!`
          )
        }
        return {
          status: 'blocked_unconfirmed',
          reason: 'Wait for the student to confirm understanding or get a correct checkpoint verdict before advancing.',
        }
      }
    }

    // Debounce guard ONLY after passing all guards so blocked attempts never poison valid advancement
    const now = Date.now()
    if (now - lastConceptDoneTimeRef.current < 3000) {
      return { status: 'deduplicated', reason: 'Concept transition already in progress.' }
    }
    lastConceptDoneTimeRef.current = now

    if (conceptName?.trim() && !isConfirmationOrNextIntent(conceptName) && conceptName !== 'EXPLICIT_USER_ADVANCE') {
      // STRICT: Must explicitly state "concept <num>", e.g. "Concept 2"
      // NEVER match arbitrary standalone numbers like "4", "40", "Question 4"!
      const numMatch = String(conceptName).match(/\bconcept\s*#?\s*(\d+)\b/i)
      if (numMatch && numMatch[1]) {
        const parsed = parseInt(numMatch[1], 10)
        if (parsed >= 1 && parsed <= keyConcepts.length) {
          // Never allow jumping ahead: cap at current concept index
          matchedIdx = Math.min(parsed - 1, currentIdx)
        }
      } else {
        const norm = (s: string) =>
          String(s || '')
            .toLowerCase()
            .replace(/^[\s\(\[\{\"\']+|[\s\)\]\}\"\']+$/g, '')
            .replace(/^concept\s*\d*[:\-\s]*/i, '')
            .replace(/^\d+[\.\:\)\-]\s*/, '')
            .replace(/[^a-z0-9]/g, '')

        const targetNorm = norm(conceptName)
        if (targetNorm && targetNorm.length >= 4) {
          const found = keyConcepts.findIndex((c) => {
            const cNorm = norm(c)
            return cNorm === targetNorm || (cNorm.length >= 6 && targetNorm.length >= 6 && (cNorm.includes(targetNorm) || targetNorm.includes(cNorm)))
          })
          if (found >= 0) {
            matchedIdx = Math.min(found, currentIdx)
          }
        }
      }
    }

    const canonicalConcept = keyConcepts[currentIdx] || keyConcepts[matchedIdx]
    const priorConcepts = keyConcepts.slice(0, currentIdx + 1)
    let updated = Array.from(new Set([...completedConceptsRef.current, ...priorConcepts, ...(canonicalConcept ? [canonicalConcept] : [])]))
    completedConceptsRef.current = updated
    setCompletedConcepts(updated)

    // STRICT SEQUENTIAL STEP: Advance strictly by +1 from CURRENT concept
    const nextIdx = currentIdx + 1
    if (nextIdx < keyConcepts.length) {
      // advanceToNextConcept updates currentConceptIndexRef, localStorage, chalkboard page, and DB atomically
      void advanceToNextConcept(nextIdx, updated)
    } else {
      if (userId && moduleId && canonicalConcept) {
        const latestBoardNotes = (chalkboardRef.current?.getBoardSummary()?.fullSummary || latestBoardSummary || chapterNotes || '').trim()
        invalidateUserProgressCache(userId, moduleId)
        invalidateStudentProgressCache(userId)
        const supabase = createClient()
        supabase
          .from('user_progress')
          .upsert(
            {
              user_id: userId,
              syllabus_module_id: moduleId,
              completed_concepts: updated,
              current_concept_index: currentIdx,
              last_covered_concept: canonicalConcept,
              status: 'completed',
              ...(latestBoardNotes ? { chapter_notes: latestBoardNotes } : {}),
            },
            { onConflict: 'user_id,syllabus_module_id' }
          )
          .then(() => {})
      }

      // Verify all concepts are actually completed before ending the module
      const allCompleted = keyConcepts.every((k) =>
        updated.some((u) => {
          const uNorm = u.toLowerCase().replace(/[^a-z0-9]/g, '')
          const kNorm = k.toLowerCase().replace(/[^a-z0-9]/g, '')
          return uNorm === kNorm || uNorm.includes(kNorm) || kNorm.includes(uNorm)
        })
      )
      if (allCompleted && updated.length >= keyConcepts.length) {
        if (moduleId) clearSessionState(moduleId)
        markModuleAsCompleted()
        triggerModuleCompletionAndAdvance()
      } else {
        // If some earlier concepts were missed, navigate to the first uncompleted concept
        const uncompletedIdx = keyConcepts.findIndex((k) =>
          !updated.some((u) => {
            const uNorm = u.toLowerCase().replace(/[^a-z0-9]/g, '')
            const kNorm = k.toLowerCase().replace(/[^a-z0-9]/g, '')
            return uNorm === kNorm || uNorm.includes(kNorm) || kNorm.includes(uNorm)
          })
        )
        if (uncompletedIdx >= 0) {
          void advanceToNextConcept(uncompletedIdx, updated)
        }
      }
    }

    return { status: 'ok' }
  }
  handleConceptDoneRef.current = handleConceptDone

  const isCallActive =
    connectionState === 'CONNECTED' ||
    connectionState === 'LISTENING' ||
    connectionState === 'TEACHER_SPEAKING' ||
    connectionState === 'MUTED' ||
    connectionState === 'CONNECTING'
  // Meet-style elapsed-time counter for the control bar
  useEffect(() => {
    if (!isCallActive) return
    const t = setInterval(() => setElapsedSec((s) => s + 1), 1000)
    return () => clearInterval(t)
  }, [isCallActive])

  const handlePauseClass = () => {
    console.log('[Classroom] Student paused lesson. Preserving exact position in DB and halting audio.')
    setIsPaused(true)
    isPausedRef.current = true
    setIsReconnecting(false)
    if (reconnectAttemptTimerRef.current) {
      clearTimeout(reconnectAttemptTimerRef.current)
      reconnectAttemptTimerRef.current = null
    }
    const currentNotes = (chalkboardRef.current?.getBoardSummary()?.fullSummary || latestBoardSummary || chapterNotes || '').trim()
    // Persist paused state and progress strictly in Supabase DB
    saveNotesToSupabase(currentNotes, 'in_progress', true)
    pauseClass()
  }

  // Start Spoken Lesson: continuous teaching flow, explanation-first, worked-demonstrations second, strict chalkboard directives
  const handleStartClass = async () => {
    if (!activeModule) return

    handleStartClassRef.current = handleStartClass
    handlePauseClassRef.current = handlePauseClass

    const wasPausedSession = isPaused || isPausedRef.current
    setIsPaused(false)
    isPausedRef.current = false
    const currentNotes = (chalkboardRef.current?.getBoardSummary()?.fullSummary || latestBoardSummary || chapterNotes || '').trim()
    // Clear pause flag in DB
    saveNotesToSupabase(currentNotes, 'in_progress', false)

    isUserTerminatedRef.current = false
    reconnectAttemptsRef.current = 0
    hasSessionStartedRef.current = true
    setIsReconnecting(false)

    // Voice locking: lock chosen voice for this session and persist to profiles in DB
    const lockedVoice = sessionActiveVoiceRef.current || preferredVoice || 'Charon'
    sessionActiveVoiceRef.current = lockedVoice
    persistVoicePreferenceToDb(lockedVoice)

    lastVerdictStatusRef.current = 'neutral'
    isReviewingVerdictRef.current = false
    setIsReviewingVerdict(false)
    isAwaitingStudentAnswerRef.current = false
    setIsAwaitingStudentAnswer(false)
    hasConfirmedUnderstandingRef.current = false

    const keyConcepts: string[] = parseKeyConcepts(activeModule?.key_concepts)
    const rawCurrent = keyConcepts[currentConceptIndex] || activeModule.title || ''
    const currentConcept = rawCurrent.replace(/^[\s\(\[\{]+|[\s\)\]\}]+$/g, '').trim()
    const rawFirst = keyConcepts[0] || resolvedTitle || ''
    const firstConcept = rawFirst.replace(/^[\s\(\[\{]+|[\s\)\]\}]+$/g, '').trim()
    const norm = (s: string) =>
      String(s || '')
        .toLowerCase()
        .replace(/^[\s\(\[\{\"\']+|[\s\)\]\}\"\']+$/g, '')
        .replace(/^concept\s*\d*[:\-\s]*/i, '')
        .replace(/^\d+[\.\:\)\-]\s*/, '')
        .replace(/[^a-z0-9]/g, '')

    const currentCompletedCount = keyConcepts.filter((k) =>
      completedConcepts.some((c) => {
        const cNorm = norm(c)
        const kNorm = norm(k)
        return cNorm === kNorm || cNorm.includes(kNorm) || kNorm.includes(cNorm)
      })
    ).length

    const isCompletedModule =
      isCompletedBefore ||
      moduleCompletedSuccess ||
      (keyConcepts.length > 0 && currentCompletedCount >= keyConcepts.length)
    const nextConcept = keyConcepts[currentConceptIndex + 1] || 'Chapter Synthesis Summary'

    const boardSummaryObj = chalkboardRef.current?.getBoardSummary()
    const currentBoard = boardSummaryObj?.fullSummary || latestBoardSummary || ''
    const chapterName = activeCurriculum?.title || resolvedTitle || 'Chapter'
    const subjectDirective = getSubjectPedagogyDirective(resolvedSubject, resolvedClassLevel, resolvedBoard, resolvedTitle + ' ' + (chapterName || ''))

    const isLastCapsuleOfChapter = !nextSiblingModule

    const rawWorkedExamples = activeModule.worked_examples
    let parsedWorkedExamples: any[] = []
    if (Array.isArray(rawWorkedExamples)) {
      parsedWorkedExamples = rawWorkedExamples
    } else if (typeof rawWorkedExamples === 'string') {
      try {
        const p = JSON.parse(rawWorkedExamples)
        if (Array.isArray(p)) parsedWorkedExamples = p
      } catch {
        parsedWorkedExamples = []
      }
    }

    const workedExamplesText =
      parsedWorkedExamples.length > 0
        ? parsedWorkedExamples
            .map(
              (ex: any, i: number) => {
                const figCue = (ex.figure_id || ex.image_url) ? ` | [TEXTBOOK FIGURE: Direct student to Side Book Viewer: "Look at ${ex.figure_id || 'the diagram'} in your textbook in the side viewer" — DO NOT draw book image on board; chalkboard is reserved for live math, formulas, and vector graphs]` : ''
                return `#${i + 1}: "${ex.problem || ''}" | Given: ${ex.given || ''} | Formula: ${ex.formula || ''} | Sub: ${ex.substitution || ''} | Calc: ${ex.calculation || ''} | Ans: ${ex.finalAnswer || ''} ${ex.unit || ''}${figCue}`.trim()
              }
            )
            .join('\n')
        : ''

    const rawMisconceptions = activeModule.common_misconceptions
    let parsedMisconceptions: string[] = []
    if (Array.isArray(rawMisconceptions)) {
      parsedMisconceptions = rawMisconceptions
    } else if (typeof rawMisconceptions === 'string') {
      try {
        const p = JSON.parse(rawMisconceptions)
        if (Array.isArray(p)) parsedMisconceptions = p
      } catch {
        parsedMisconceptions = []
      }
    }

    const misconceptionsText =
      parsedMisconceptions.length > 0
        ? parsedMisconceptions.map((m: string, i: number) => `${i + 1}. ${m}`).join(' | ')
        : ''

    const capsuleNotesText = (activeModule.chapter_notes || '').trim()
    const aiContextText = (activeModule.ai_system_prompt_context || '').trim()

    const isMath = (resolvedSubject || '').toLowerCase().includes('math')
    const totalSiblingCount = siblingModules.length || 1
    const moduleOrderIndex = typeof activeModule?.order_index === 'number' ? activeModule.order_index : 1
    const isFoundationalHalf = moduleOrderIndex <= Math.max(1, Math.ceil(totalSiblingCount / 2))

    const mathProgressionText = isMath
      ? isFoundationalHalf
        ? `Math Pedagogy (#${moduleOrderIndex}/${totalSiblingCount} "${chapterName}"): Ground conceptual foundations, axioms, coordinate properties, theorems, and proofs on the chalkboard with geometrical intuition (never use "definition" phrasing in Maths).`
        : `Math Pedagogy (#${moduleOrderIndex}/${totalSiblingCount} "${chapterName}"): Solve authentic board exam questions & textbook numericals step-by-step on whiteboard showing Exercise X.Y • Q.N clearly with 1 or max 2 steps per line (Given -> Formula -> Substitution -> Calculation -> Boxed Answer).`
      : ''

    const firstVisual = inferConceptVisualDirective(firstConcept, resolvedSubject, chapterName)
    const currentVisual = inferConceptVisualDirective(currentConcept, resolvedSubject, chapterName)

    const customPlan = activeModule?.visual_lesson_plan
    const conceptVisuals: any[] = Array.isArray(customPlan?.concept_visuals)
      ? customPlan.concept_visuals
      : Array.isArray(activeModule?.concept_visuals)
      ? activeModule.concept_visuals
      : []

    const formatVisualEntry = (cv: any, conceptName: string, subLabel: string) => {
      const vTitle = cv?.diagram_title || cv?.concept_title || conceptName
      const timing = cv?.timing_and_cue || 'Step 1 (Intuition) or Step 2 (Definition) or during problem solving'
      const why = cv?.why_needed || 'Visual grounding of core principles'
      const explain = cv?.what_to_explain || cv?.what_to_make || ''

      const isLegitGraph = isLegitimateGraphTopic(conceptName, resolvedSubject) || isLegitimateGraphTopic(vTitle, resolvedSubject)
      if (isLegitGraph && cv?.interactive_math_formula) {
        return `    - Visual [${subLabel}]: Interactive Mathematical/Kinematic Graph (Requires Worked Math)\n      * Tool Call Cue: plot_mathematical_graph(formula="${cv.interactive_math_formula}", title="${vTitle}")\n      * Timing: ${timing}\n      * Focus: ${explain || why}\n      * Requirement: Accompany with worked chalkboard calculations (draw_step, draw_rough_work).`
      }

      if (cv?.diagram_type === 'draw_flowchart') {
        return `    - Visual [${subLabel}]: Process Flowchart\n      * Tool Call Cue: write_chalkboard(action="draw_flowchart", content="${cv?.what_to_make || conceptName}")\n      * Timing: ${timing}`
      }

      if (cv?.diagram_type === 'draw_shape') {
        return `    - Visual [${subLabel}]: Geometric Shape Primitive\n      * Tool Call Cue: draw_shape(shape="${cv?.what_to_make || 'rectangle'}", label="${vTitle}")\n      * Timing: ${timing}`
      }

      // Image-First Authentic Educational Diagram - strictly dynamic, zero hardcoded URLs
      const { image_search_query: fullImgQ, video_search_query: fullVidQ } = buildDetailedEducationalQueries(
        conceptName,
        activeModule?.title || '',
        cv,
        resolvedSubject
      )
      return `    - Visual [${subLabel}]: Image-First Educational Visual (Video on Doubt/Request Only)\n      * Image Search Cue: search_and_show_image(query="${fullImgQ}", title="${vTitle}", caption="${explain || why}")\n      * Confusion/Request Video Cue (ONLY if student didn't understand or asks for video): search_and_show_video(query="${fullVidQ}", title="${vTitle}")\n      * Vector SVG Fallback: render_svg_diagram(title="${vTitle}", what="${explain || why}") if online diagram is unavailable or for bespoke vector illustration\n      * Proactive Visual: Start with ONE clean image (or graph) first; unlock video & extra diagrams/shapes when student asks doubts or gets confused\n      * Timing: ${timing}`

      const hasSvg = Boolean(cv?.svg || cv?.diagram_svg)
      if (!cv || (!hasSvg && !cv?.interactive_math_formula && cv?.diagram_type !== 'draw_flowchart' && cv?.diagram_type !== 'draw_shape' && cv?.diagram_type !== 'image')) {
        const whatSpec = cv?.what_to_make || `Publication-grade scientific vector diagram illustrating ${conceptName}`
        return `    - Visual [${subLabel}]: On-Demand Bespoke Vector Generation\n      * Tool Call Cue: render_svg_diagram(title="${conceptName}", what="${whatSpec}")\n      * Timing: ${timing}\n      * Notice: Digital chalkboard will display a live progress card and generate this diagram on-demand.`
      }

      const isAnimated = cv?.visual_type === 'animation' || /wave|current|flow|circuit|motion/i.test(vTitle)
      return `    - Visual [${subLabel}]: ${isAnimated ? 'Animated Vector Visualization' : 'Tier 2 Publication-Grade Vector SVG'}\n      * Tool Call Cue: render_svg_diagram(title="${vTitle}", caption="${explain || why}")\n      * Timing: ${timing}\n      * Why Needed: ${why}`
    }

    // Strict Single-Concept Isolation: build visual roadmap ONLY for the currently active concept (zero future concept leakage!)
    const activeMatchedCv = findMatchingConceptVisual(
      conceptVisuals,
      currentConcept,
      keyConcepts,
      currentConceptIndex
    )
    const activeConceptVisualRoadmap = `  * Active Concept #${currentConceptIndex + 1} "${currentConcept}":\n` + formatVisualEntry(activeMatchedCv || null, currentConcept, 'Primary Visual')

    const visualRoadmap =
      `VISUAL FREEDOM DIRECTIVE (CURRENT CONCEPT ONLY): You are NOT limited to 1 or 2 graphs or visuals for "${currentConcept}". Actively use search_and_show_image (clean educational images on concept entry and examples), search_and_show_video (animated conceptual videos whenever helpful on doubt, struggle, or student request), plot_mathematical_graph (curves, bar graphs, pie charts, line graphs, color fills), render_svg_diagram (vector diagrams), and step-by-step chalkboard calculations whenever helpful.\n` +
      activeConceptVisualRoadmap

    const studentFirstName = studentName ? studentName.split(' ')[0].trim() : ''

    // 1. Spoken Language Directive (Language of Talking & Verbal Guidance)
    let spokenLanguageDirective = ''
    if (studentPreferredLanguage === 'Hindi') {
      spokenLanguageDirective = `PRIMARY SPOKEN TALKING LANGUAGE: Pure Conversational Hindi (हिंदी).
MANDATORY SPOKEN REQUIREMENT: You MUST speak and teach strictly in Hindi (हिंदी).
- Explain all everyday intuitions, step-by-step solutions, questions, and conversational guidance in clear, encouraging, respectful Hindi.
- Retain accurate scientific formulas and standard symbols while conducting all speech in Hindi.
- Check understanding in Hindi: "श्यामपट्ट पर लिखे नोट्स और हल को देखिए। क्या यह संकल्पना आपको अच्छे से समझ आई?"`
    } else if (studentPreferredLanguage === 'Hinglish') {
      spokenLanguageDirective = `PRIMARY SPOKEN TALKING LANGUAGE: Authentic Conversational Hinglish (Indian School Bilingual Voice).
MANDATORY SPOKEN REQUIREMENT: You MUST speak, converse, and teach strictly in natural, conversational Hinglish.
- Blending Style: Use English for standard curriculum terms and formulas (e.g. Velocity, Acceleration, Force, Chemical Equation, Photosynthesis, Quadratic, etc.), but use warm, natural Hindi words for ALL conversation, intuition, explanations, and questions (e.g., "Pehle iska real-life logic samajhte hain", "Imagine karo jab aap cricket ball ko throw karte ho...", "${isMath ? 'Ab whiteboard par core concept aur formula likhte hain: [write step]. Iska simple matlab yeh hai ki...' : 'Ab whiteboard par formal law dekh lete hain: [read law]. Iska simple matlab yeh hai ki...'}", "Ab is problem ko ek-ek step karke solve karte hain: Pehle given values likhte hain, fir formula lagayenge...", "Whiteboard ke notes aur step dekho. Yeh ${isMath ? 'concept' : 'law'} achhe se samajh aaya, ya ek aur example se samjhaun?", "Chalo ab ek authentic ${resolvedBoard} question try karo! Batao iska kya answer aayega?", "Shabash! Bilkul sahi answer!").
- Tone: Friendly, energetic Indian school exam topper / mentor (Bhaiya/Didi) tone.
- CRITICAL: Never lecture in continuous formal English. Speak primarily in lively Hinglish as requested by the student!`
    } else if (studentPreferredLanguage === 'Spanish') {
      spokenLanguageDirective = 'PRIMARY SPOKEN TALKING LANGUAGE: Spanish (Español).\nMANDATORY SPOKEN REQUIREMENT: You MUST speak, converse, and deliver all spoken intuitions, definitions, and explanations in fluent Spanish.'
    } else if (studentPreferredLanguage === 'French') {
      spokenLanguageDirective = 'PRIMARY SPOKEN TALKING LANGUAGE: French (Français).\nMANDATORY SPOKEN REQUIREMENT: You MUST speak, converse, and deliver all spoken explanations in fluent French.'
    } else if (studentPreferredLanguage === 'German') {
      spokenLanguageDirective = 'PRIMARY SPOKEN TALKING LANGUAGE: German (Deutsch).\nMANDATORY SPOKEN REQUIREMENT: You MUST speak, converse, and deliver all spoken explanations in fluent German.'
    } else {
      spokenLanguageDirective = 'PRIMARY SPOKEN TALKING LANGUAGE: English.\nMANDATORY SPOKEN REQUIREMENT: You MUST speak, converse, and teach verbally in clear, articulate, and encouraging academic English.'
    }

    // 2. Study Medium Directive (Language of Whiteboard Notes & Formal Instruction)
    let studyMediumDirective = ''
    if (studentStudyMedium === 'Hindi') {
      studyMediumDirective = 'STUDY MEDIUM (WHITEBOARD NOTES & FORMAL TEACHING): Hindi Medium (हिंदी माध्यम).\nMANDATORY WHITEBOARD REQUIREMENT: You MUST write structured chalkboard notes, formulas, definitions, and derivations primarily in formal Hindi (हिंदी), while preserving standard international scientific symbols, SI units, and mathematical variables (e.g. F = ma, v = u + at, SI unit: N).'
    } else if (studentStudyMedium === 'Hinglish') {
      studyMediumDirective = 'STUDY MEDIUM (WHITEBOARD NOTES & FORMAL TEACHING): Bilingual / Hinglish.\nMANDATORY WHITEBOARD REQUIREMENT: Write core chalkboard notes, formulas, and derivations in clean English notation, supplemented with brief Hinglish explanations for maximum conceptual clarity.'
    } else if (studentStudyMedium === 'Other') {
      studyMediumDirective = 'STUDY MEDIUM (WHITEBOARD NOTES & FORMAL TEACHING): Universal Academic Notation.\nMANDATORY WHITEBOARD REQUIREMENT: Write clean, precise chalkboard notes using standard mathematical and scientific notation.'
    } else {
      studyMediumDirective = 'STUDY MEDIUM (WHITEBOARD NOTES & FORMAL TEACHING): English Medium.\nMANDATORY WHITEBOARD REQUIREMENT: All chalkboard notes, formal definitions, formulas, derivations, and board-exam steps MUST be written in crisp, topper-standard academic English.'
    }

    // Pedagogical Dossier (strictly excluding age and non-teaching metadata)
    const paceDirective = studentLearningPace === 'fast_and_curious'
      ? 'Pacing: Fast & Curious (Move briskly, present high-level intuition, and challenge with rigorous problems quickly).'
      : studentLearningPace === 'slow_deep_intuitive'
      ? 'Pacing: Deep & Intuitive (Slow down, ground every concept with relatable daily analogies before symbols, and verify understanding thoroughly).'
      : 'Pacing: Steady & Balanced (Maintain standard pace, balancing conceptual intuition with step-by-step worked examples).'

    const styleDirective = studentLearningStyle === 'socratic'
      ? 'Teaching Style: Socratic Guidance (Guide the student with thoughtful questions so they deduce conclusions themselves).'
      : studentLearningStyle === 'visual'
      ? 'Teaching Style: Visual & Intuitive (Prioritize dynamic chalkboard diagrams, coordinate plots, and physical schematic sketches).'
      : studentLearningStyle === 'board_numerical'
      ? 'Teaching Style: Step-by-Step Derivations (Meticulously lay out formulas, substitutions, and rough work on the chalkboard).'
      : 'Teaching Style: Real-Life Analogies (Ground abstract equations in daily physical objects and memorable narratives).'

    const careerHook = studentCareerAspiration
      ? `Student Career Dream: Aspires to become ${studentCareerAspiration}. When appropriate, naturally reference real-world applications in ${studentCareerAspiration} to inspire and motivate!`
      : ''

    const favoriteHook = studentFavoriteSubject
      ? `Favorite Subject: Loves ${studentFavoriteSubject}. Use creative analogies, concepts, or problem-solving intuition from ${studentFavoriteSubject} to make learning fun and engaging!`
      : ''

    const weakAreaHook = studentWeakSubjects && studentWeakSubjects.length > 0
      ? `Focus & Struggle Areas: ${studentWeakSubjects.join(', ')}. Pay special attention here! Break down steps with extra patience and clarity; do not rush through these topics.`
      : ''

    const langVoiceConfig = getLanguageVoiceConfig(studentPreferredLanguage)

    const pedagogicalDossier = `
STUDENT PERSONALIZATION & PEDAGOGICAL DOSSIER:
- Name: ${studentFirstName || 'Student'}
- Grade / Class: ${resolvedClassLevel || 'Class 10'}
- Board Curriculum: ${resolvedBoard || studentTargetBoard || 'CBSE'}
- Spoken Conversation Language (Talking): ${studentPreferredLanguage}
- Voice Persona: ${preferredVoice} (${langVoiceConfig.recommendedVoices.includes(preferredVoice as any) ? 'Recommended Persona' : 'Selected Persona'})
- Speech Inflection & Cadence: ${langVoiceConfig.accentPromptInstruction}
- Supported Language Parameters: ["en-IN", "hi-IN"] (Primary: ${langVoiceConfig.primaryLanguageCode})
- Medium of Study (Whiteboard Notes & Formal Instruction): ${studentStudyMedium} Medium
- ${spokenLanguageDirective}
- ${studyMediumDirective}
- ${paceDirective}
- ${styleDirective}
${careerHook ? `- ${careerHook}\n` : ''}${favoriteHook ? `- ${favoriteHook}\n` : ''}${weakAreaHook ? `- ${weakAreaHook}\n` : ''}${userMemories && userMemories.length > 0 ? `- Long-Term Student Learning Context: ${userMemories.map((m: any) => m.memory_text || m.content).filter(Boolean).join('; ')}\n` : ''}`

    // Grounded RAG: Ensure the chalkboard has navigated to the active concept's page and synchronized
    await chalkboardRef.current?.goToPage?.(currentConceptIndex, currentConcept)

    const boardCompactContext = chalkboardRef.current?.getCompactBoardContext?.(currentConceptIndex) || chalkboardRef.current?.getBoardSummary()?.notesText || chapterNotes || ''
    const hasExistingContent = Boolean(
      boardCompactContext.trim() &&
      !boardCompactContext.includes('[Clean page - Ready for new notes]') &&
      (boardCompactContext.includes('Notes Already on Board') ||
       boardCompactContext.includes('Drawn Diagram') ||
       boardCompactContext.includes('Plotted Graph') ||
       boardCompactContext.includes('Geometric Figure') ||
       boardCompactContext.includes('Completed Pedagogical Stages'))
    )
    const hasPendingQuestion = Boolean(
      boardCompactContext.includes('Active Question on Board') ||
      boardCompactContext.includes('Stage 5 (Checkpoint Question)')
    )
    const isResumed = !isCompletedModule && (
      currentConceptIndex > 0 ||
      currentCompletedCount > 0 ||
      wasPausedSession ||
      hasExistingContent
    )
    const boardContinuationNote = boardCompactContext.trim()
      ? `\n========================================================================================\nCURRENT DIGITAL CHALKBOARD STATE (DO NOT RE-WRITE OR DUPLICATE):\n========================================================================================\n${boardCompactContext.trim()}\nCONTINUATION MANDATE: The items above are ALREADY VISIBLE on the student's chalkboard right now. Continue directly from where you left off. DO NOT re-write, duplicate, or re-draw any note or diagram already present on the board. Live diagram tools (render_svg_diagram, plot_mathematical_graph, draw_shape) remain fully active for all new concepts!\n`
      : ''

    const langGreeting = studentPreferredLanguage === 'Hindi'
      ? `Namaste ${studentFirstName || 'विद्यार्थी'}! Aaj ham ${resolvedTitle} start karenge. `
      : studentPreferredLanguage === 'Hinglish'
      ? `Hello ${studentFirstName || 'yaar'}! Welcome to today's class on ${resolvedTitle}! Aaj hum ${firstConcept} seekhenge Lets GO.`
      : studentPreferredLanguage === 'Spanish'
      ? `¡Hola ${studentFirstName || 'allí'}! Bienvenido a la clase de hoy sobre ${resolvedTitle}.`
      : studentPreferredLanguage === 'French'
      ? `Bonjour ${studentFirstName || ''}! Bienvenue au cours d'aujourd'hui sur ${resolvedTitle}.`
      : studentPreferredLanguage === 'German'
      ? `Hallo ${studentFirstName || ''}! Willkommen zur heutigen Stunde über ${resolvedTitle}.`
      : `Hello ${studentFirstName || 'there'}! Welcome to today's class on ${resolvedTitle}! Let us dive right in.`

    const isResumedLegitGraph = isLegitimateGraphTopic(currentConcept, resolvedSubject)
    const resumedVisualTool = isResumedLegitGraph
      ? `search_and_show_image(query="<full detailed 10-25 word educational search query for ${currentConcept} specifying exact components, apparatus, or anatomical structures>", title="${currentConcept}", caption="Visual illustration") or plot_mathematical_graph(formula="...", title="${currentConcept}") with worked derivations`
      : `search_and_show_image(query="<full detailed 10-25 word educational search query for ${currentConcept} specifying exact components, apparatus, or anatomical structures>", title="${currentConcept}", caption="Visual illustration")`

    const kickoffPrompt = selectedPyqQuestion
      ? `[SESSION START - BOARD EXAM PYQ PRACTICE]: Speak FIRST immediately in ${studentPreferredLanguage}! Warmly greet me by my name ("${langGreeting}"). State that today we are tackling an authentic Board Exam Past Year Question on ${resolvedTitle}: "${selectedPyqQuestion}". Introduce the problem clearly in 2 to 3 crisp conversational sentences. YOU MUST CALL write_chalkboard(action="draw_question", content="Board PYQ: ${selectedPyqQuestion}", color="amber") RIGHT NOW IN THIS TURN! Then ask me what our given values or strategy should be in ${studentPreferredLanguage}. HARD STOP: Wait for my answer! (Stop speaking immediately if I speak or ask something).`
      : isCompletedModule
      ? `[SESSION START]: Speak FIRST immediately in ${studentPreferredLanguage}! Warmly greet me by my name ("${langGreeting}"). State that I have completed this capsule in 2 to 3 warm, encouraging sentences reviewing what we mastered, and ask if I would like a quick review of any concept or if I am ready for the quiz in ${studentPreferredLanguage}. HARD STOP: Wait for my answer. (Stop speaking immediately if I speak or ask something).`
      : isResumed && hasPendingQuestion
      ? `[SESSION START - RESUMING ACTIVE QUESTION ON CONCEPT ${currentConceptIndex + 1}: "${currentConcept}"]: Speak FIRST immediately in ${studentPreferredLanguage}! Warmly greet me by my name ("${langGreeting}"). State that we are resuming right at our checkpoint question on the board: [see CURRENT DIGITAL CHALKBOARD STATE above]. DO NOT re-write notes, DO NOT repeat past explanations, and NEVER reveal or solve the question automatically! Remind me of the question briefly in 2 to 3 encouraging sentences, and ask if I would like a hint or need more time to work it out. HARD STOP: Wait silently for my response! (Stop speaking immediately if I speak or ask something).`
      : isResumed && hasExistingContent
      ? `[SESSION START - RESUMING CONCEPT ${currentConceptIndex + 1}: "${currentConcept}"]: Speak FIRST immediately in ${studentPreferredLanguage}! Warmly greet me by my name ("${langGreeting}"). State that we are resuming Concept ${currentConceptIndex + 1}: "${currentConcept}". Existing chalkboard notes and visuals are ALREADY visible on the board: [see CURRENT DIGITAL CHALKBOARD STATE above]. Acknowledge what is already on the board in 2 to 3 clear conversational sentences. DO NOT re-write or duplicate existing notes or diagrams. Continue directly with the NEXT pedagogical step (${isMath ? 'theorem, worked example, or board numerical' : 'formal law, worked example, or board numerical'}). Write on the board as you speak, then ask a checkpoint question. HARD STOP: Wait for my response! (Stop speaking immediately if I speak or ask something).`
      : isResumed
      ? `[SESSION START]: Speak FIRST immediately in ${studentPreferredLanguage}! Warmly greet me by my name ("${langGreeting}"). State that we are resuming Concept ${currentConceptIndex + 1}: "${currentConcept}". Explain the intuition in 2 to 3 crisp, simple everyday sentences as you write ONE short intuitive note via write_chalkboard(action="draw_note", content="Intuition: <everyday hook>", color="botanical") AND ${resumedVisualTool} RIGHT NOW IN THIS TURN! Do NOT wait for the student to ask for a diagram. Then ask: "Did you follow this intuition?" HARD STOP: Wait for my response! (Stop speaking immediately if I speak or ask something).`
      : `[SESSION START]: Speak FIRST immediately in ${studentPreferredLanguage}! Warmly greet me by my name ("${langGreeting}"). Introduce Concept 1: "${firstConcept}" with a simple, relatable everyday real-life hook. Speak in 2 to 3 crisp, warm sentences—teach like an approachable mentor (no textbook jargon). YOU MUST CALL write_chalkboard(action="draw_note", content="Intuition: <everyday hook>", color="botanical") AND search_and_show_image(query="<full detailed 10-25 word educational search query for ${firstConcept} specifying exact components, apparatus parts, anatomical structures, or system elements>", title="${firstConcept}", caption="Visual illustration")${isLegitimateGraphTopic(firstConcept, resolvedSubject) ? ` (or plot_mathematical_graph if quantitative)` : ''} RIGHT NOW IN THIS FIRST TURN! Image-First rule: show ONE clean image/graph first; do NOT call search_and_show_video yet unless the student asks for a video or gets confused later. Complete your explanation, then ask: "${isMath ? 'Did you follow this concept so far?' : 'Did you catch this intuition?'}" HARD STOP: Stop speaking and wait for my answer! (Stop speaking immediately if I speak or ask something).`

    const activeChapterNumber =
      activeCurriculum?.order_index ||
      extractChapterNumber(String(chapterName || activeModule?.title || '')) ||
      1

    const singleConceptDossier = buildSingleConceptMicroDossier(
      currentConceptIndex,
      keyConcepts,
      activeModule,
      resolvedBoard,
      resolvedClassLevel,
      resolvedSubject,
      chapterName,
      parsedWorkedExamples,
      parsedMisconceptions,
      activeChapterNumber
    )

    const nextConceptIdx = currentConceptIndex + 1
    const nextConceptName = keyConcepts[nextConceptIdx]
    // STRICT SINGLE-CONCEPT ENFORCEMENT: Never inject upcoming concept data into active prompt
    const nextConceptLockedDossier = ''

    const activeBookPdfUrl = bookPdfUrlRef.current || bookPdfUrl || ''
    const activeBookTotalPages = bookTotalPagesRef.current || bookTotalPages || 30
    const activeTargetPage = resolveTargetPageForLesson({
      conceptName: currentConcept,
      capsuleTitle: activeModule?.title,
      chapterNumber: activeCurriculum?.order_index || activeModule?.order_index,
      classLevel: resolvedClassLevel || activeCurriculum?.class_level || activeModule?.class_level,
      subject: resolvedSubject || activeCurriculum?.category || activeModule?.subject,
      pdfPath: activeBookPdfUrl,
      totalPages: activeBookTotalPages,
      moduleIndex: typeof activeModule?.order_index === 'number' ? activeModule.order_index - 1 : 0,
      totalModules: Math.max(1, siblingModules.length),
      conceptIndex: currentConceptIndex,
      totalConcepts: keyConcepts.length,
    }) || bookCurrentPage || 1

    const lessonPrompt = `ROLE: Senior Academic Topper Tutor & Master Faculty Mentor (1-on-1 spoken class with live interactive chalkboard).
${pedagogicalDossier}
STUDENT: ${studentFirstName ? studentFirstName + ' | ' : ''}${resolvedClassLevel || 'Class 9'} (${resolvedBoard || 'CBSE'}) | Subject: ${resolvedSubject} | Capsule: "${resolvedTitle}"${
  isLastCapsuleOfChapter && nextChapterInfo
    ? ` | Final Capsule (Next: #${nextChapterInfo.orderIndex} "${nextChapterInfo.chapterTitle}")`
    : ''
}
${boardContinuationNote}${
  selectedPyqQuestion
    ? `\n========================================================================================\nCURRENT BOARD EXAM PYQ PRACTICE FOCUS:\n========================================================================================\nThe student is solving this authentic Board Exam question: "${selectedPyqQuestion}".\n1. Lay out problem on board: write_chalkboard(action="draw_question", content="Board PYQ: ${selectedPyqQuestion}", color="amber").\n2. Solve step-by-step with the student using the Trio Combo (Given -> Formula -> Substitution -> Scratchpad in [ROUGH_WORK] -> Boxed Answer).\n`
    : ''
}

========================================================================================
GRADE & SUBJECT PEDAGOGICAL ARCHITECTURE SPECIFICATION:
========================================================================================
${subjectDirective}

========================================================================================
TEXTBOOK SIDE VIEWER SYNCHRONIZATION:
========================================================================================
- Active Chapter PDF: "${activeBookPdfUrl}" (Side Book Viewer currently at Page ${activeTargetPage} of ${activeBookTotalPages}).
- When referencing a textbook figure, example, or exercise, direct the student to that exact page ("Look at Figure X on Page ${activeTargetPage} in your textbook").

========================================================================================
HOW TO TEACH LIKE A REAL HUMAN MENTOR (Classes 9-12):
========================================================================================
1. Short Conversational Turns (2-3 Sentences + Live Board Action):
   - Speak warmly and plainly in ${studentPreferredLanguage}, like a caring senior mentor. Skip textbook monologues.
   - Keep each turn to 2 or 3 crisp sentences while writing or plotting on the board. Never explain purely verbally without writing or visualizing.
   - Start every new concept with write_chalkboard(action="draw_title", content="<Topic Title>", color="cream").
2. Adaptive Problem Solving & Diagnostic Co-Pilot (plan_teaching_move):
   - Whenever the student is confused, makes a mistake, raises a doubt, or works on an advanced Class 10-12 proof/numerical, call plan_teaching_move(questionOrTopic="...", studentMessage="...") to get a mathjs-verified teaching move (everyday analogy, tiny-number test, prerequisite bridge, or graph spec).
   - ${isMath
     ? `Mathematics: Teach intuition, theorems, and solving methods dynamically. NEVER ask "did you understand the definition?" in Mathematics; ask "Did you follow this concept / method?". ACTIVE TEXTBOOK CHAPTER IS CHAPTER ${activeChapterNumber} ("${chapterName}"): ONLY reference Exercise ${activeChapterNumber}.1, ${activeChapterNumber}.2, etc. when matching chapter problems — NEVER invent Exercise numbers from other chapters (such as Exercise 2.1, 3.1, 7.1, 10.1)! For self-generated practice questions, label as "Practice Problem • Q.N".`
     : `Science: Start with a daily real-life hook, explain the mechanism, state the exact law with SI units, and solve Chapter ${activeChapterNumber} board numericals step-by-step.`}
   - Interactive Step-by-Step Writing (DO NOT DUMP ALL STEPS AT ONCE): Write 1 line/step per spoken micro-turn via write_chalkboard(draw_step) instead of dumping Given -> Formula -> Substitution -> Calculation -> Boxed Answer in one big blob! Always show intermediate square-root arithmetic (e.g. d = √[(4 - 1)² + (6 - 2)²] -> next turn = √[3² + 4²] = √[9 + 16] = √25 -> Boxed Answer: [ d = 5 units ]). Use Unicode math (x², x₁, x₂, y₁, y₂, θ, √, ×, ÷, ±) and NEVER output raw *, **, ^, or //. For 2D distance, always write d = √[(x₂ - x₁)² + (y₂ - y₁)²].
3. Visuals (Image-First, Full Interactive Graphs & Confusion Escalation):
   - Start each visual concept with 1 clean authentic image via search_and_show_image (or plot_mathematical_graph if quantitative). Do NOT launch search_and_show_video at initial startup.
   - Use plot_mathematical_graph dynamically for coordinate geometry, circles, polygons, segments, vectors, curves, kinematics (v-t, s-t), Ohm's law (V-I), statistical bar graphs, pie charts (pies), line graphs (lineSeries), and shaded color fills (shadedRegions / fillColor). Use draw_shape for 2D/3D solids, draw_table for comparisons, and draw_flowchart for cycles or hierarchies.
   - If the student asks a doubt or says they did not understand, simplify immediately with everyday student examples AND unlock search_and_show_video, extra diagrams, or interactive graphs until it clicks.
4. Checkpoint Questions, Hard Stop & Doubt Lock:
   - Write every question on the board via write_chalkboard(action="draw_question", content="Practice Problem • Q.1: <Question>" or "Exercise ${activeChapterNumber}.1 • Q.1: <Question>", color="amber"), then STOP speaking immediately and wait silently for the student's answer or explicit request to solve ("solve it"). NEVER call draw_step("Given: ..."), draw_numerical, or Verdict after posing a question before the student responds!
   - Whenever the student speaks or raises a doubt, stop immediately, listen, and never call concept_completed or switch pages until their doubt is resolved.
   - Advance ONLY after the student confirms understanding after checkpoint/exercises or asks for the next concept. Call conclude_and_open_quiz(summary="...") only after all capsule concepts are complete.

${verifiedAssetsDirectives ? `\n========================================================================================\n${verifiedAssetsDirectives}\n` : ''}

========================================================================================
CURRENT ACTIVE CONCEPT DOSSIER (SINGLE-CONCEPT GATED PROGRESSION):
========================================================================================
${singleConceptDossier}${nextConceptLockedDossier}

CRITICAL SINGLE-CONCEPT PROGRESSION:
- You are teaching Concept ${currentConceptIndex + 1} of ${keyConcepts.length}: "${currentConcept}".
- ABSOLUTE PROHIBITION ON FUTURE CONCEPTS: Never teach, introduce, or preview upcoming concepts until Concept ${currentConceptIndex + 1} is 100% completed and confirmed by the student.
${visualRoadmap ? `\n========================================================================================\nVISUAL ROADMAP (MANDATORY UNIQUE CONCEPT VISUALS):\n========================================================================================\n${visualRoadmap}\n` : ''}${mathProgressionText ? `- ${mathProgressionText}\n` : ''}${aiContextText ? `\n========================================================================================\nAUTHENTIC TEXTBOOK TEACHING DIRECTIVES & CURRICULUM BLUEPRINT:\n========================================================================================\n${aiContextText}\n` : ''}
RULES: Strictly ZERO emojis on board. Whiteboard is single source of truth for notes. Warm, intellectually rigorous topper tone.`

    // Whiteboard 1-Concept-Per-Page: Ensure active concept page is active with proper title
    chalkboardRef.current?.goToPage?.(currentConceptIndex, currentConcept)
    setTimeout(() => {
      autoTriggerVisualForConcept(currentConceptIndexRef.current)
    }, 500)

    startClass(
      lockedVoice as any,
      lessonPrompt,
      kickoffPrompt,
      (action, content, color) => {
        if (action === 'close_graph') {
          setActiveGraph(null);
          return;
        }
        const isVisualAction = [
          'draw_graph', 'graph',
          'draw_geometry', 'geometry', 'draw_table', 'table',
          'draw_shape', 'shape', 'draw_rectangle', 'draw_circle', 'draw_triangle',
          'draw_flowchart', 'draw_numerical', 'numerical', 'solve', 'worked_example',
          'render_svg_diagram', 'draw_svg', 'draw_svg_diagram',
          'draw_video', 'video',
        ].includes(action)
        if (isVisualAction) {
          renderedVisualConceptsRef.current.add(currentConceptIndexRef.current)
        }
        if (chalkboardRef.current) {
          // Normalize action and unwrap nested content if action is write_chalkboard or write_board
          if (
            action === 'write_chalkboard' ||
            action === 'write_board' ||
            action === 'chalkboard' ||
            action === 'whiteboard' ||
            action === 'board'
          ) {
            if (typeof content === 'object' && content !== null) {
              const innerAction = content.action || (content.note ? 'draw_note' : content.step ? 'draw_step' : content.title ? 'draw_title' : content.question ? 'draw_question' : 'draw_note')
              const innerContent = content.content ?? content.text ?? content.note ?? content.step ?? content.title ?? content.question ?? ''
              color = content.color || color
              action = innerAction
              content = innerContent
            } else if (typeof content === 'string') {
              const trimmed = content.trim()
              if (trimmed.startsWith('{') && trimmed.endsWith('}')) {
                try {
                  const parsed = JSON.parse(trimmed)
                  const innerAction = parsed.action || (parsed.note ? 'draw_note' : parsed.step ? 'draw_step' : parsed.title ? 'draw_title' : parsed.question ? 'draw_question' : 'draw_note')
                  const innerContent = parsed.content ?? parsed.text ?? parsed.note ?? parsed.step ?? parsed.title ?? parsed.question ?? ''
                  color = parsed.color || color
                  action = innerAction
                  content = innerContent
                } catch {}
              } else {
                action = 'draw_note'
              }
            }
          }

          // Convert content to string for text-based chalkboard drawing
          const stringContent = typeof content === 'string' ? content : (content?.content || content?.text || content?.note || (content ? JSON.stringify(content) : ''))

          // Auto-scroll docked textbook when tutor teaches a topic, question, or diagram
          const totalPgs = bookTotalPagesRef.current || bookTotalPages
          if (totalPgs && stringContent) {
            const activeConcepts = parseKeyConcepts(activeModule?.key_concepts)
            const activeConceptName = activeConcepts[currentConceptIndexRef.current || 0] || activeModule?.title
            const resolvedTargetPage = resolveTargetPageForLesson({
              content: stringContent,
              conceptName: activeConceptName,
              capsuleTitle: activeModule?.title,
              chapterNumber: activeCurriculum?.order_index || activeModule?.order_index,
              classLevel: resolvedClassLevel || activeCurriculum?.class_level || activeModule?.class_level,
              subject: resolvedSubject || activeCurriculum?.category || activeModule?.subject,
              pdfPath: bookPdfUrlRef.current || bookPdfUrl || undefined,
              totalPages: totalPgs,
              moduleIndex: typeof activeModule?.order_index === 'number' ? activeModule.order_index - 1 : 0,
              totalModules: Math.max(1, siblingModules.length),
              conceptIndex: currentConceptIndexRef.current || 0,
              totalConcepts: activeConcepts.length || 1,
            })
            if (resolvedTargetPage && resolvedTargetPage >= 1 && resolvedTargetPage <= totalPgs) {
              setBookCurrentPage(resolvedTargetPage)
            }
            if (
              action === 'draw_image' &&
              (stringContent.includes('extracted_diagrams') || stringContent.includes('BOOK FIGURE'))
            ) {
              setIsBookOpen(true)
            }
          }

          const executeLiveDiagramGeneration = (
            targetConceptTitle: string,
            explicitCaption?: string,
            explicitWhat?: string,
            matchedVisual?: any
          ) => {
            const matched = matchedVisual
            const vPlan = (activeModule?.visual_lesson_plan as any) || {}
            const isGraph =
              isLegitimateGraphTopic(targetConceptTitle, resolvedSubject) &&
              (matchedVisual?.diagram_type === 'graph' || /graph|parabola|function|kinematic/i.test(targetConceptTitle))
            const isAnim =
              matchedVisual?.visual_type === 'animation' || /wave|current|flow|circuit|motion/i.test(targetConceptTitle)
            const resolvedVisualType = isGraph ? 'graph' : isAnim ? 'animation' : matchedVisual?.diagram_type || 'diagram'

            chalkboardRef.current?.drawDiagramSkeleton?.(targetConceptTitle)
            setGeneratingDiagramTitle(targetConceptTitle)

            const genController = new AbortController()
            const genTimer = setTimeout(() => genController.abort(), 25000)

            fetch('/api/diagram/generate', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              signal: genController.signal,
              body: JSON.stringify({
                title: targetConceptTitle,
                subject: resolvedSubject,
                classLevel: resolvedClassLevel,
                context: targetConceptTitle,
                existingSvg: matchedVisual?.svg || matchedVisual?.diagram_svg || '',
                whyNeeded: matchedVisual?.why_needed || '',
                whatToExplain: matchedVisual?.what_to_explain || explicitCaption || '',
                whatToMake: explicitWhat || matched?.what_to_make || '',
                refinementPrompt: explicitCaption || '',
                visualType: resolvedVisualType,
                interactiveMathFormula: matchedVisual?.interactive_math_formula || '',
                moduleId: activeModule?.id,
                conceptIndex: currentConceptIndexRef.current,
                conceptTitle: targetConceptTitle,
                animationType: 'moving_points_and_pulsing_glow',
                isLiveClass: true,
                source: 'live_classroom',
              }),
            })
              .then((res) => {
                clearTimeout(genTimer)
                return res.ok ? res.json() : null
              })
              .then((data) => {
                setGeneratingDiagramTitle(null)
                if (data?.svg && data.svg.includes('<svg')) {
                  chalkboardRef.current?.drawSvgDiagram?.(
                    data.title || targetConceptTitle,
                    data.svg,
                    data.caption || explicitCaption || data.what_to_explain,
                    true
                  )
                  if (activeModule?.id) {
                    if (!vPlan.concept_visuals) vPlan.concept_visuals = []
                    if (matchedVisual) {
                      matchedVisual.svg = data.svg
                      matchedVisual.diagram_svg = data.svg
                      matchedVisual.refined_by_tier2 = true
                      matchedVisual.tier2_refined_at = data.tier2_refined_at || new Date().toISOString()
                    } else {
                      vPlan.concept_visuals.push({
                        concept_title: targetConceptTitle,
                        diagram_title: data.title || targetConceptTitle,
                        svg: data.svg,
                        diagram_svg: data.svg,
                        what_to_make: data.what_to_make || explicitWhat || '',
                        what_to_explain: data.what_to_explain || '',
                        why_needed: data.why_needed || '',
                        visual_type: data.visual_type || 'diagram',
                        interactive_math_formula: data.interactive_math_formula || '',
                        refined_by_tier2: true,
                        tier2_refined_at: data.tier2_refined_at || new Date().toISOString(),
                      })
                    }
                  }
                } else {
                  console.warn('[Classroom] Live diagram generation returned empty SVG. Clearing skeleton.')
                  chalkboardRef.current?.clearDiagramSkeleton?.(targetConceptTitle)
                }
              })
              .catch((err) => {
                setGeneratingDiagramTitle(null)
                chalkboardRef.current?.clearDiagramSkeleton?.(targetConceptTitle)
                console.warn('[Classroom] Live diagram generation failed:', err)
              })
          }

          if (action === 'set_color' || action === 'chalk_color') {
            chalkboardRef.current.setChalkColor(color || stringContent)
          }
          else if (action === 'draw_title' || action === 'title' || action === 'board_title') {
            chalkboardRef.current.drawTitle(stringContent, color)
            handleNoteRecorded(`### ${stringContent}`)
          }
          else if (action === 'draw_note' || action === 'note' || action === 'text' || action === 'draw_text' || action === 'board_note') {
            chalkboardRef.current.drawNote(stringContent, color)
            handleNoteRecorded(`• ${stringContent}`)
          }
          else if (action === 'draw_step' || action === 'step' || action === 'board_step') {
            if (isAwaitingStudentAnswerRef.current && !hasUserRespondedSinceQuestionRef.current) {
              return { status: 'blocked_waiting_for_student', reason: 'STOP! Wait for the student to reply or ask you to solve before writing Given/Formula/solution steps.' }
            }
            chalkboardRef.current.drawStep(stringContent, color)
            handleNoteRecorded(`- Step: ${stringContent}`)
          }
          else if (action === 'draw_highlight_box' || action === 'highlight_box' || action === 'highlight' || action === 'box') {
            chalkboardRef.current.drawHighlightBox(stringContent, color)
            handleNoteRecorded(`**Core Formulation:** ${stringContent}`)
          }
          else if (action === 'highlight_text' || action === 'highlight_word' || action === 'highlight_sentence') {
            chalkboardRef.current.highlightText?.(stringContent, color)
          }
          else if (action === 'clear_notes') chalkboardRef.current.clearNotes()
          else if (action === 'rewrite_notes') chalkboardRef.current.rewriteNotes(stringContent)
          else if (action === 'draw_question' || action === 'question') {
            isAwaitingStudentAnswerRef.current = true
            setIsAwaitingStudentAnswer(true)
            hasUserRespondedSinceQuestionRef.current = false
            setAwaitingStudentAnswer(true)
            const cIdx = currentConceptIndexRef.current
            askedOrSolvedExercisesPerConceptRef.current.set(
              cIdx,
              (askedOrSolvedExercisesPerConceptRef.current.get(cIdx) || 0) + 1
            )
            chalkboardRef.current.drawQuestion(stringContent, color)
            handleNoteRecorded(`**Checkpoint Question:** ${stringContent}`)
          }
          else if (action === 'draw_student_answer' || action === 'student_answer') {
            chalkboardRef.current.drawStudentAnswer?.(stringContent, undefined, color)
          }
          else if (action === 'draw_answer_verdict' || action === 'answer_verdict' || action === 'verdict') {
            if (isAwaitingStudentAnswerRef.current && !hasUserRespondedSinceQuestionRef.current) {
              return { status: 'blocked_waiting_for_student', reason: 'Wait for student answer before giving verdict.' }
            }
            const isIncorrect = /\b(incorrect|wrong|needs review|needs correction|not quite|try again|mistake|error)\b/i.test(stringContent)
            const isCorrect = /\b(correct|spot on|perfect|right|excellent|well done)\b/i.test(stringContent)
            if (isIncorrect) {
              lastVerdictStatusRef.current = 'incorrect'
            } else if (isCorrect) {
              lastVerdictStatusRef.current = 'correct'
              studentHasActiveDoubtRef.current = false
              doubtClearedAtMsgCountRef.current = transcriptsRef.current.length
            }
            chalkboardRef.current.drawAnswerVerdict?.(stringContent, !isIncorrect, color)
            isAwaitingStudentAnswerRef.current = false
            setIsAwaitingStudentAnswer(false)
            setAwaitingStudentAnswer(false)
            isReviewingVerdictRef.current = true
            setIsReviewingVerdict(true)
          }
          else if (action === 'draw_exam_question' || action === 'exam_question') {
            isAwaitingStudentAnswerRef.current = true
            setIsAwaitingStudentAnswer(true)
            hasUserRespondedSinceQuestionRef.current = false
            setAwaitingStudentAnswer(true)
            const cIdx = currentConceptIndexRef.current
            askedOrSolvedExercisesPerConceptRef.current.set(
              cIdx,
              (askedOrSolvedExercisesPerConceptRef.current.get(cIdx) || 0) + 1
            )
            chalkboardRef.current.drawExamQuestion?.(stringContent, undefined, undefined, color)
          }
          else if (
            action === 'draw_shape' || action === 'shape' ||
            action === 'draw_rectangle' || action === 'draw_circle' ||
            action === 'draw_triangle' || action === 'draw_square' ||
            action === 'draw_cylinder' || action === 'draw_cube' ||
            action === 'draw_ellipse' || action === 'draw_line' ||
            action === 'draw_arrow'
          ) {
            chalkboardRef.current.drawShape?.(content)
          }
          else if (action === 'draw_flowchart') chalkboardRef.current.drawFlowchart(content, color)
          else if (action === 'draw_table' || action === 'table') chalkboardRef.current.drawTable?.(content)
          else if (action === 'draw_geometry' || action === 'geometry') chalkboardRef.current.drawGeometry?.(content)
          else if (action === 'draw_graph' || action === 'graph' || action === 'plot_mathematical_graph') {
            let formula: string | undefined = undefined
            let formulas: Array<string | GraphFormulaItem> | undefined = undefined
            let segments: any = undefined
            let domain: [number, number] | undefined = undefined
            let range: [number, number] | undefined = undefined
            let title = 'Graph'
            let callout = ''
            let points: any = undefined
            let bars: any = undefined
            let vectors: any = undefined
            let polygons: any = undefined
            let circles: any = undefined
            let texts: any = undefined
            let pies: any = undefined
            let lineSeries: any = undefined
            let shadedRegions: any = undefined

            if (typeof content === 'object' && content !== null) {
              formula = typeof content.formula === 'string' ? content.formula : undefined
              if (Array.isArray(content.formulas)) {
                formulas = content.formulas
              }
              if (Array.isArray(content.segments)) {
                segments = content.segments
              }
              if (content.points) {
                points = content.points
              }
              if (content.bars) {
                bars = content.bars
              }
              if (content.vectors) {
                vectors = content.vectors
              }
              if (content.polygons) {
                polygons = content.polygons
              }
              if (content.circles) {
                circles = content.circles
              }
              if (content.texts) {
                texts = content.texts
              }
              if (content.pies || content.slices) {
                pies = content.pies || content.slices
              }
              if (content.lineSeries || content.lines) {
                lineSeries = content.lineSeries || content.lines
              }
              if (content.shadedRegions || content.fills) {
                shadedRegions = content.shadedRegions || content.fills
              }
              title = content.title || (formula ? `Graph: y = ${formula}` : (formulas && formulas.length > 0 ? 'Comparative Graphs' : (segments && segments.length > 0 ? 'Coordinate Segments' : (pies ? 'Pie Chart Distribution' : (lineSeries ? 'Line Graph' : (bars ? 'Statistical Bar Graph' : (vectors ? 'Physics Vector Diagram' : (circles ? 'Geometric Circle' : 'Mathematical Graph'))))))))
              callout = content.callout || ''
              if (content.domain) {
                if (Array.isArray(content.domain)) domain = [Number(content.domain[0]), Number(content.domain[1])]
                else if (typeof content.domain === 'string') {
                  const m = content.domain.match(/\[\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\]/)
                  if (m) domain = [parseFloat(m[1]), parseFloat(m[2])]
                }
              }
              if (content.range) {
                if (Array.isArray(content.range)) range = [Number(content.range[0]), Number(content.range[1])]
                else if (typeof content.range === 'string') {
                  const m = content.range.match(/\[\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\]/)
                  if (m) range = [parseFloat(m[1]), parseFloat(m[2])]
                }
              }
            } else if (typeof content === 'string') {
              const pipeParts = (content || '').split('|').map((s: string) => s.trim())
              pipeParts.forEach((p: string) => {
                if (p.startsWith('formula=')) formula = p.substring(8).trim()
                else if (p.startsWith('formulas=')) {
                  const rawFormulas = p.substring(9).trim()
                  try {
                    const parsed = JSON.parse(rawFormulas)
                    if (Array.isArray(parsed)) formulas = parsed
                  } catch {
                    formulas = rawFormulas.split(/[;,]/).map((s) => s.trim()).filter(Boolean)
                  }
                }
                else if (p.startsWith('segments=')) {
                  const rawSegments = p.substring(9).trim()
                  try {
                    const parsed = JSON.parse(rawSegments)
                    if (Array.isArray(parsed)) segments = parsed
                  } catch {
                    segments = rawSegments
                  }
                }
                else if (p.startsWith('bars=')) {
                  const rawBars = p.substring(5).trim()
                  try { bars = JSON.parse(rawBars) } catch { bars = rawBars }
                }
                else if (p.startsWith('vectors=')) {
                  const rawVectors = p.substring(8).trim()
                  try { vectors = JSON.parse(rawVectors) } catch { vectors = rawVectors }
                }
                else if (p.startsWith('polygons=')) {
                  const rawPolygons = p.substring(9).trim()
                  try { polygons = JSON.parse(rawPolygons) } catch { polygons = rawPolygons }
                }
                else if (p.startsWith('circles=')) {
                  const rawCircles = p.substring(8).trim()
                  try { circles = JSON.parse(rawCircles) } catch { circles = rawCircles }
                }
                else if (p.startsWith('texts=')) {
                  const rawTexts = p.substring(6).trim()
                  try { texts = JSON.parse(rawTexts) } catch { texts = rawTexts }
                }
                else if (p.startsWith('pies=') || p.startsWith('slices=')) {
                  const rawPies = p.substring(p.indexOf('=') + 1).trim()
                  try { pies = JSON.parse(rawPies) } catch { pies = rawPies }
                }
                else if (p.startsWith('lineSeries=') || p.startsWith('lines=')) {
                  const rawSeries = p.substring(p.indexOf('=') + 1).trim()
                  try { lineSeries = JSON.parse(rawSeries) } catch { lineSeries = rawSeries }
                }
                else if (p.startsWith('shadedRegions=') || p.startsWith('fills=')) {
                  const rawShaded = p.substring(p.indexOf('=') + 1).trim()
                  try { shadedRegions = JSON.parse(rawShaded) } catch { shadedRegions = rawShaded }
                }
                else if (p.startsWith('title=')) title = p.substring(6).trim()
                else if (p.startsWith('callout=')) callout = p.substring(8).trim()
                else if (p.startsWith('points=')) {
                  const rawPoints = p.substring(7).trim()
                  try {
                    points = JSON.parse(rawPoints)
                  } catch {
                    points = rawPoints
                  }
                }
                else if (p.startsWith('domain=')) {
                  const m = p.match(/\[\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\]/)
                  if (m) domain = [parseFloat(m[1]), parseFloat(m[2])]
                } else if (p.startsWith('range=')) {
                  const m = p.match(/\[\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\]/)
                  if (m) range = [parseFloat(m[1]), parseFloat(m[2])]
                } else if (!formula && (p.includes('x') || p.includes('^') || p.includes('sin') || p.includes('cos'))) {
                  formula = p
                }
              })
            }

            const candidatePayload = { formula, formulas, segments, points, bars, vectors, polygons, circles, texts, pies, lineSeries, shadedRegions, domain, range, title, callout }
            const isAllowedGraph = isLegitimateGraphTopic(title || formula || '', resolvedSubject, candidatePayload)
            if (!isAllowedGraph) {
              console.log(`[Classroom Graph Gating] Denied graph plot for non-mathematical topic "${title || formula}" in subject ${resolvedSubject}. Rendering search-engine diagram instead.`)
              const searchKw = extractConciseSearchKeyword(title || formula || '') || title || 'Scientific Diagram'
              fetch('/api/diagram/search-image', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: searchKw, limit: 3 }),
              })
                .then((r) => (r.ok ? r.json() : null))
                .then(async (data) => {
                  const candidateImages: any[] = data?.images || []
                  for (const img of candidateImages) {
                    if (!img?.url) continue
                    try {
                      const check = await fetch(`/api/diagram/proxy?dataUrl=true&url=${encodeURIComponent(img.url)}`)
                      if (check.ok) {
                        const pData = await check.json()
                        if (pData?.success && pData?.dataURL) {
                          chalkboardRef.current?.drawImage?.(
                            pData.dataURL,
                            title || img.title || 'Scientific Diagram',
                            'Visual conceptual diagram'
                          )
                          return
                        }
                      }
                    } catch {}
                  }
                  executeLiveDiagramGeneration(title || 'Scientific Diagram', 'Visual conceptual diagram')
                })
                .catch(() => executeLiveDiagramGeneration(title || 'Scientific Diagram', 'Visual conceptual diagram'))
              return { status: 'denied', reason: `Graph topic "${title || formula}" in ${resolvedSubject} routed to conceptual diagram.` }
            }

            if (!isValidGraphPayload(candidatePayload)) {
              console.warn('[Classroom Graph Gating] Rejected meaningless or empty graph payload (no substantive functions/points/segments):', candidatePayload)
              return { status: 'rejected', reason: 'Empty or meaningless graph payload; include explicit formula, points, segments, circles, or polygons.' }
            }

            // Launch interactive MafsGraphCanvas directly (never draw duplicate static Excalidraw axes)
            setActiveGraph(candidatePayload)
            return { status: 'ok' }
          }
          else if (action === 'draw_numerical' || action === 'numerical' || action === 'worked_example' || action === 'solve') {
            if (isAwaitingStudentAnswerRef.current && !hasUserRespondedSinceQuestionRef.current) {
              return { status: 'blocked_waiting_for_student', reason: 'STOP! Wait for the student to reply or ask you to solve before writing the numerical solution.' }
            }
            const cIdx = currentConceptIndexRef.current
            askedOrSolvedExercisesPerConceptRef.current.set(
              cIdx,
              (askedOrSolvedExercisesPerConceptRef.current.get(cIdx) || 0) + 1
            )
            let numericalData: any = content
            if (typeof numericalData === 'object' && numericalData !== null) {
              if (numericalData.content && !numericalData.answer && !numericalData.problem) {
                numericalData = numericalData.content
              }
            }
            if (typeof numericalData === 'string') {
              try {
                const parsed = JSON.parse(numericalData)
                if (parsed && typeof parsed === 'object') numericalData = parsed
              } catch {}
            }
            if (typeof numericalData === 'object' && numericalData !== null) {
              chalkboardRef.current.drawNumericalSolution?.(numericalData)
            } else {
              chalkboardRef.current.handleAiDirective(`[NUMERICAL: ${numericalData}]`)
            }
          }
          else if (action === 'draw_video' || action === 'video') {
            let vidUrl = ''
            let vidTitle = 'Demonstration Video'
            let vidDesc = ''
            let vidMime = 'video/mp4'
            if (typeof content === 'object' && content !== null) {
              vidUrl = content.url || content.video_url || ''
              vidTitle = content.title || 'Demonstration Video'
              vidDesc = content.description || content.caption || ''
              vidMime = content.mimeType || content.mime_type || 'video/mp4'
            } else if (typeof content === 'string') {
              const trimmed = content.trim()
              if (trimmed.startsWith('{') && trimmed.endsWith('}')) {
                try {
                  const parsed = JSON.parse(trimmed)
                  vidUrl = parsed.url || parsed.video_url || ''
                  vidTitle = parsed.title || 'Demonstration Video'
                  vidDesc = parsed.description || parsed.caption || ''
                  vidMime = parsed.mimeType || parsed.mime_type || 'video/mp4'
                } catch {}
              } else {
                const parts = trimmed.split('|').map((s: string) => s.trim())
                if (parts[0]?.startsWith('http')) {
                  vidUrl = parts[0]
                  vidTitle = parts[1] || 'Demonstration Video'
                  vidDesc = parts[2] || ''
                } else if (parts[1]?.startsWith('http')) {
                  vidTitle = parts[0]
                  vidUrl = parts[1]
                  vidDesc = parts[2] || ''
                } else {
                  vidTitle = parts[0]
                  vidDesc = parts[1] || ''
                }
              }
            }

            if (vidUrl) {
              chalkboardRef.current?.drawVideoCard?.(vidTitle, vidDesc, vidUrl, vidMime)
            } else {
              fetch('/api/diagram/search-video', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: vidTitle }),
              })
                .then((r) => r.json())
                .then((data) => {
                  const first = data.videos?.[0]
                  if (first?.url) {
                    chalkboardRef.current?.drawVideoCard?.(first.title || vidTitle, vidDesc || first.description, first.url, first.mimeType || 'video/mp4')
                  } else {
                    chalkboardRef.current?.drawVideoCard?.(vidTitle, vidDesc)
                  }
                })
                .catch(() => chalkboardRef.current?.drawVideoCard?.(vidTitle, vidDesc))
            }
          }
          else if (action === 'draw_image' || action === 'image') {
            const currConceptIdx = currentConceptIndexRef.current
            const existingImgCount = imagesRenderedPerConceptRef.current.get(currConceptIdx) || 0
            const recentStudentTranscripts = transcriptsRef.current.filter((t) => t.sender === 'user').slice(-3)
            const isExplicitStudentImageRequest = recentStudentTranscripts.some((t) =>
              /\b(image|picture|diagram|photo|figure|dikhaiye|chitra|draw|more|another|repeat|again|samajh)\b/i.test(t.text)
            )
            const isConfusionOrFollowUp = Boolean(studentHasActiveDoubtRef.current) || isExplicitStudentImageRequest

            if ((existingImgCount >= 1 && !isConfusionOrFollowUp) || existingImgCount >= 3) {
              console.log(`[Classroom Visual Guard] Concept ${currConceptIdx + 1} already has ${existingImgCount} educational image(s). Skipped duplicate.`)
              return { status: 'skipped', reason: 'Image already displayed on chalkboard.' }
            }
            imagesRenderedPerConceptRef.current.set(currConceptIdx, existingImgCount + 1)

            let imgUrl = ''
            let imgTitle = 'Educational Visual'
            let imgCaption = ''
            if (typeof content === 'object' && content !== null) {
              imgUrl = content.url || content.image_url || content.fullUrl || ''
              imgTitle = content.title || 'Educational Visual'
              imgCaption = content.caption || ''
            } else if (typeof content === 'string') {
              const trimmed = content.trim()
              if (trimmed.startsWith('{') && trimmed.endsWith('}')) {
                try {
                  const parsed = JSON.parse(trimmed)
                  imgUrl = parsed.url || parsed.image_url || parsed.fullUrl || ''
                  imgTitle = parsed.title || 'Educational Visual'
                  imgCaption = parsed.caption || ''
                } catch {}
              } else {
                const parts = trimmed.split('|').map((s: string) => s.trim())
                if (parts[0]?.startsWith('http') || parts[0]?.startsWith('data:')) {
                  imgUrl = parts[0]
                  imgTitle = parts[1] || 'Educational Visual'
                  imgCaption = parts[2] || ''
                } else if (parts[1]?.startsWith('http') || parts[1]?.startsWith('data:')) {
                  imgTitle = parts[0]
                  imgUrl = parts[1]
                  imgCaption = parts[2] || ''
                } else {
                  imgTitle = parts[0]
                  imgCaption = parts[1] || ''
                }
              }
            }

            if (imgUrl) {
              chalkboardRef.current?.drawImage?.(imgUrl, imgTitle, imgCaption)
            } else {
              fetch('/api/diagram/search-image', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: extractConciseSearchKeyword(imgTitle) || imgTitle }),
              })
                .then((r) => r.json())
                .then(async (data) => {
                  const candidateImages: any[] = data.images || []
                  for (const img of candidateImages) {
                    if (!img?.url) continue
                    try {
                      const check = await fetch(`/api/diagram/proxy?dataUrl=true&url=${encodeURIComponent(img.url)}`)
                      if (check.ok) {
                        const pData = await check.json()
                        if (pData.success && pData.dataURL) {
                          chalkboardRef.current?.drawImage?.(pData.dataURL, imgTitle || img.title, imgCaption || img.description)
                          return
                        }
                      }
                    } catch {}
                  }
                  // If online image search found no authentic relevant image, generate an authentic vector diagram
                  executeLiveDiagramGeneration(imgTitle, imgCaption)
                })
                .catch(() => executeLiveDiagramGeneration(imgTitle, imgCaption))
            }
          }
          else if (
            action === 'draw_diagram' ||
            action === 'diagram' ||
            action === 'render_svg_diagram' ||
            action === 'draw_svg' ||
            action === 'draw_svg_diagram'
          ) {
            const supabase = createClient()
            const vPlan = (activeModule?.visual_lesson_plan as any) || {}
            const conceptVisuals: any[] = Array.isArray(vPlan.concept_visuals) ? vPlan.concept_visuals : []
            const moduleDefaultSvg = vPlan.diagram_svg || ''

            let queryTitle = 'Educational Diagram'
            let explicitSvg = ''
            let explicitCaption = ''
            let explicitWhat = ''

            if (typeof content === 'object' && content !== null) {
              queryTitle = content.title || 'Educational Diagram'
              explicitSvg = content.svg || ''
              explicitCaption = content.caption || ''
              explicitWhat = content.what || ''
            } else if (typeof content === 'string') {
              const trimmed = content.trim()
              if (trimmed.includes('|') && trimmed.includes('<svg')) {
                const parts = trimmed.split('|').map((s: string) => s.trim())
                queryTitle = parts[0] || 'Educational Diagram'
                explicitSvg = parts[1] || ''
                explicitCaption = parts[2] || ''
              } else if (trimmed.includes('<svg')) {
                explicitSvg = trimmed
              } else if (trimmed.includes('|')) {
                const parts = trimmed.split('|').map((s: string) => s.trim())
                queryTitle = parts[0] || 'Educational Diagram'
                explicitCaption = parts[1] || ''
                explicitWhat = parts[2] || ''
              } else {
                queryTitle = trimmed || 'Educational Diagram'
              }
            }

            const activeConceptName = keyConcepts[currentConceptIndexRef.current] || currentConcept || ''
            const targetConceptTitle =
              queryTitle && queryTitle !== 'Educational Diagram' && queryTitle !== 'Scientific Diagram'
                ? queryTitle
                : (activeConceptName || 'Scientific Diagram')

            // If valid SVG markup was explicitly supplied, draw immediately
            if (explicitSvg && explicitSvg.toLowerCase().includes('<svg')) {
              chalkboardRef.current?.drawSvgDiagram?.(queryTitle, explicitSvg, explicitCaption)
              return
            }

            // 1. Search for pre-authored concept visual in activeModule
            const qLower = queryTitle.toLowerCase().trim()
            let matched = conceptVisuals.find((cv: any) => {
              const cTitle = (cv.concept_title || '').toLowerCase()
              const dTitle = (cv.diagram_title || '').toLowerCase()
              return (
                (cTitle && (cTitle.includes(qLower) || qLower.includes(cTitle))) ||
                (dTitle && (dTitle.includes(qLower) || qLower.includes(dTitle)))
              )
            })

            // Only fall back by index when the requested query is generic; never force an unrelated caption/SVG onto a specific topic
            const isGenericDiagramQuery = !qLower || qLower === 'educational diagram' || qLower === 'scientific diagram' || qLower === 'diagram'
            if (!matched && isGenericDiagramQuery && conceptVisuals[currentConceptIndexRef.current]) {
              const currCv = conceptVisuals[currentConceptIndexRef.current]
              if (currCv?.svg || currCv?.diagram_svg) {
                matched = currCv
              }
            }



            if (matched && (matched.svg || matched.diagram_svg)) {
              // 1a. Draw immediate diagram without blocking student
              chalkboardRef.current?.drawSvgDiagram?.(
                matched.diagram_title || matched.concept_title || queryTitle,
                matched.svg || matched.diagram_svg,
                explicitCaption || matched.diagram_title || matched.concept_title
              )
              return
            }

            // Check default module SVG only if topic matches capsule title
            if (moduleDefaultSvg && activeModule?.title?.toLowerCase().includes(qLower)) {
              chalkboardRef.current?.drawSvgDiagram?.(queryTitle, moduleDefaultSvg, explicitCaption || queryTitle)
              return
            }

            // MANDATE: Search Engine First before falling back to bespoke LLM agent generation
            const searchKw = extractConciseSearchKeyword(targetConceptTitle) || targetConceptTitle
            fetch('/api/diagram/search-image', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ query: searchKw, limit: 3 }),
            })
              .then((r) => (r.ok ? r.json() : null))
              .then(async (data) => {
                const candidateImages: any[] = data?.images || []
                for (const img of candidateImages) {
                  if (!img?.url) continue
                  try {
                    const check = await fetch(`/api/diagram/proxy?dataUrl=true&url=${encodeURIComponent(img.url)}`)
                    if (check.ok) {
                      const pData = await check.json()
                      if (pData?.success && pData?.dataURL) {
                        chalkboardRef.current?.drawImage?.(
                          pData.dataURL,
                          targetConceptTitle || img.title,
                          explicitCaption || ''
                        )
                        return
                      }
                    }
                  } catch {}
                }
                // Online search yielded no usable image -> fall back to bespoke agent SVG generator
                executeLiveDiagramGeneration(targetConceptTitle, explicitCaption, explicitWhat, matched)
              })
              .catch(() => {
                // Online search network error -> fall back to bespoke agent SVG generator
                executeLiveDiagramGeneration(targetConceptTitle, explicitCaption, explicitWhat, matched)
              })
          }
          else if (action === 'new_page') {
            console.warn('[Classroom] Ignored AI action: new_page. Chalkboard uses 1 dedicated page per concept with vertical scrolling.')
          }
          else if (action === 'clear_board' || action === 'erase_board') {
            setActiveGraph(null)
            chalkboardRef.current?.clearBoard()
          }
          else if (action === 'start_quiz' || action === 'open_quiz') {
            markModuleAsCompleted(typeof content === 'string' ? content : undefined)
            setIsCompletedBefore(true)
            setModuleCompletedSuccess(true)
            setEndChapterConfirmPrompt(null)
            handleOpenQuiz()
          }
          else if (action === 'chapter_summary') {
            chalkboardRef.current.drawTitle('Chapter Synthesis Summary', color)
            chalkboardRef.current.drawNote(content, color)
            handleNoteRecorded(`#### Chapter Summary:\n${content}`)
            const keyConcepts: string[] = parseKeyConcepts(activeModule?.key_concepts)
            if (completedConceptsRef.current.length >= keyConcepts.length && keyConcepts.length > 0) {
              markModuleAsCompleted(content)
            }
          }
          else if (action === 'concept_focus') {
            isReviewingVerdictRef.current = false
            setIsReviewingVerdict(false)
            isAwaitingStudentAnswerRef.current = false
            setIsAwaitingStudentAnswer(false)
            const cleanContent = content.replace(/^[\s\(\[\{]+|[\s\)\]\}]+$/g, '').trim()
            if (cleanContent) {
              handleConceptFocus(cleanContent)
            }
          } else if (action === 'concept_done') {
            return handleConceptDone(content)
          } else if (action === 'concept_goto' || action === 'goto_concept') {
            handleConceptGoto(content)
          } else {
            const dirPayload = color ? `${content} | ${color}` : content
            chalkboardRef.current.handleAiDirective(`[${action.toUpperCase()}: ${dirPayload}]`)
          }
        }
      },
      (action, params) => {
        renderedVisualConceptsRef.current.add(currentConceptIndexRef.current)
        handleVisualAction(action, params)
      },
      avatarConfig || undefined,
      (pcm16, sampleRate) => {
        simliControllerRef.current?.sendAudioChunk(pcm16, sampleRate)
      },
      () => {
        simliControllerRef.current?.clearBuffer()
        chalkboardRef.current?.stopWritingQueue?.()
      },
      {
        preferredLanguage: studentPreferredLanguage,
        supportedLanguages: langVoiceConfig.supportedLanguageCodes || ['en-IN', 'hi-IN'],
        languageCode: langVoiceConfig.primaryLanguageCode || 'en-IN',
      },
      () => {
        const currentSummary = chalkboardRef.current?.getBoardSummary?.();
        const compactContext = chalkboardRef.current?.getCompactBoardContext?.();
        return (
          compactContext ||
          currentSummary?.fullSummary ||
          currentSummary?.notesText ||
          chapterNotes ||
          'Digital chalkboard is active and ready.'
        );
      },
      (highlightText, target, color) => {
        if (target === 'chalkboard' || target === 'both' || !target) {
          chalkboardRef.current?.highlightText?.(highlightText, color)
        }
      },
      async ({ questionOrTopic, studentMessage, struggleCount }) => {
        try {
          const boardState =
            chalkboardRef.current?.getCompactBoardContext?.(currentConceptIndexRef.current) ||
            chalkboardRef.current?.getBoardSummary?.()?.notesText ||
            ''
          const res = await fetch('/api/tutor/think', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              questionOrTopic,
              studentMessage,
              classLevel: resolvedClassLevel || activeCurriculum?.class_level || 10,
              subject: resolvedSubject || activeCurriculum?.category || 'Mathematics',
              board: resolvedBoard || 'CBSE',
              chapterNumber: activeCurriculum?.order_index || activeModule?.order_index || undefined,
              boardState,
              struggleCount,
            }),
          })
          if (!res.ok) {
            return { result: 'fallback', status: res.status }
          }
          const plan = await res.json()
          if (plan?.visualGraphSpec && isLegitimateGraphTopic(plan.visualGraphSpec.title || questionOrTopic, resolvedSubject, plan.visualGraphSpec)) {
            setActiveGraph({
              ...plan.visualGraphSpec,
              title: plan.visualGraphSpec.title || questionOrTopic,
            })
            renderedVisualConceptsRef.current.add(currentConceptIndexRef.current)
          }
          return plan
        } catch (err: any) {
          return { result: 'fallback', error: err?.message || 'think_request_failed' }
        }
      }
    )
  }

  // Auto-reconnect session when unexpectedly dropped during an active class, preserving chalkboard and concept index
  useEffect(() => {
    if (
      !isUserTerminatedRef.current &&
      hasSessionStartedRef.current &&
      (connectionState === 'DISCONNECTED' || connectionState === 'ERROR')
    ) {
      if (reconnectAttemptsRef.current >= 3) {
        console.warn('[Classroom Auto-Reconnect] Maximum reconnect attempts (3) reached. Pausing auto-reconnect.')
        setIsReconnecting(false)
        return
      }
      setIsReconnecting(true)
      if (reconnectAttemptTimerRef.current) clearTimeout(reconnectAttemptTimerRef.current)
      reconnectAttemptTimerRef.current = setTimeout(() => {
        if (
          !isUserTerminatedRef.current &&
          hasSessionStartedRef.current &&
          (connectionState === 'DISCONNECTED' || connectionState === 'ERROR')
        ) {
          reconnectAttemptsRef.current += 1
          console.log(`[Classroom Auto-Reconnect] Attempting to reconnect session preserving board context and concept index... (Attempt ${reconnectAttemptsRef.current}/3)`)
          handleStartClass()
        }
      }, 1500)
    } else if (connectionState === 'CONNECTED' || connectionState === 'LISTENING' || connectionState === 'TEACHER_SPEAKING') {
      setIsReconnecting(false)
      reconnectAttemptsRef.current = 0
    }
    return () => {
      if (reconnectAttemptTimerRef.current) clearTimeout(reconnectAttemptTimerRef.current)
    }
  }, [connectionState])

  const handleEndClass = () => {
    isUserTerminatedRef.current = true
    hasSessionStartedRef.current = false
    setIsReconnecting(false)
    if (reconnectAttemptTimerRef.current) {
      clearTimeout(reconnectAttemptTimerRef.current)
      reconnectAttemptTimerRef.current = null
    }
    saveNotesToSupabase(chapterNotes, undefined)
    endCall()
    if (isCompletedBefore || moduleCompletedSuccess) {
      setQuizOpen(true)
    }
  }

  const handleOpenQuiz = () => {
    markModuleAsCompleted()
    setIsCompletedBefore(true)
    setModuleCompletedSuccess(true)
    isUserTerminatedRef.current = true
    hasSessionStartedRef.current = false
    setIsReconnecting(false)
    if (reconnectAttemptTimerRef.current) {
      clearTimeout(reconnectAttemptTimerRef.current)
      reconnectAttemptTimerRef.current = null
    }
    endCall()
    setQuizOpen(true)
  }

  const handleBackToDashboard = () => {
    isUserTerminatedRef.current = true
    hasSessionStartedRef.current = false
    setIsReconnecting(false)
    if (reconnectAttemptTimerRef.current) {
      clearTimeout(reconnectAttemptTimerRef.current)
      reconnectAttemptTimerRef.current = null
    }
    endCall()
    router.refresh()
    router.push(`/dashboard/${userId}`)
  }

  const handleGoToSettings = () => {
    isUserTerminatedRef.current = true
    hasSessionStartedRef.current = false
    setIsReconnecting(false)
    if (reconnectAttemptTimerRef.current) {
      clearTimeout(reconnectAttemptTimerRef.current)
      reconnectAttemptTimerRef.current = null
    }
    endCall()
    router.push(`/dashboard/${userId}/settings?tab=avatars`)
  }

  const latestTranscript =
    transcripts.length > 0 ? transcripts[transcripts.length - 1] : null

  const keyConceptsList: string[] = parseKeyConcepts(activeModule?.key_concepts)
  const nextSiblingModule = siblingModules.find(
    (m) => m.order_index > (activeModule?.order_index || 0)
  )

  const normConcept = (s: string) =>
    String(s || '')
      .toLowerCase()
      .replace(/^[\s\(\[\{\"\']+|[\s\)\]\}\"\']+$/g, '')
      .replace(/^concept\s*\d*[:\-\s]*/i, '')
      .replace(/^\d+[\.\:\)\-]\s*/, '')
      .replace(/[^a-z0-9]/g, '')

  const completedCount = keyConceptsList.filter((k) =>
    completedConcepts.some((c) => {
      const cNorm = normConcept(c)
      const kNorm = normConcept(k)
      return cNorm === kNorm || cNorm.includes(kNorm) || kNorm.includes(cNorm)
    })
  ).length

  const progressPercent =
    keyConceptsList.length > 0
      ? Math.min(100, Math.round((completedCount / keyConceptsList.length) * 100))
      : isCompletedBefore
      ? 100
      : 0

  const isCompleted = isCompletedBefore || moduleCompletedSuccess
  const statusLabel =
    connectionState === 'TEACHER_SPEAKING'
      ? 'Speaking'
      : connectionState === 'LISTENING'
      ? isMuted
        ? 'Muted'
        : 'Listening'
      : connectionState === 'CONNECTING'
      ? 'Connecting…'
      : 'Ready'
  const statusDot =
    connectionState === 'TEACHER_SPEAKING'
      ? 'bg-amber-500 animate-pulse'
      : connectionState === 'LISTENING'
      ? isMuted
        ? 'bg-stone-400'
        : 'bg-[var(--accent-primary)]'
      : connectionState === 'CONNECTING'
      ? 'bg-amber-400 animate-pulse'
      : 'bg-stone-300'

  const conceptList = (
    <div className="space-y-1">
      {keyConceptsList.map((concept: string, idx: number) => {
        const kNorm = normConcept(concept)
        const isDone = completedConcepts.some((c) => {
          const cNorm = normConcept(c)
          return cNorm === kNorm || cNorm.includes(kNorm) || kNorm.includes(cNorm)
        })
        const isCurrent = idx === currentConceptIndex && !isDone
        return (
          <button
            key={idx}
            type="button"
            onClick={() => {
              handleConceptGoto(idx + 1)
              setConceptsOpen(false)
            }}
            className={`w-full min-h-10 flex items-center gap-2.5 px-3 py-2 rounded-xl text-left text-[13px] leading-snug transition-colors cursor-pointer ${
              isCurrent
                ? 'bg-[var(--accent-warm-soft)] text-[var(--ink-primary)] font-medium'
                : 'text-[var(--ink-secondary)] hover:bg-[var(--canvas-soft)]'
            }`}
          >
            {isDone ? (
              <CheckCircle2 className="w-4 h-4 text-[var(--accent-primary)] shrink-0" />
            ) : (
              <span
                className={`w-2 h-2 mx-1 rounded-full shrink-0 ${
                  isCurrent ? 'bg-[var(--accent-warm)]' : 'bg-[var(--border-strong)]'
                }`}
              />
            )}
            <span className="min-w-0 break-words">{concept}</span>
          </button>
        )
      })}
    </div>
  )

  const elapsedLabel = `${String(Math.floor(elapsedSec / 60)).padStart(2, '0')}:${String(elapsedSec % 60).padStart(2, '0')}`
  const teacherCaption = [...transcripts].reverse().find((t) => t.sender === 'teacher')?.text || ''
  const inSession = isCallActive || isPaused
  const togglePanel = (panel: 'chat' | 'concepts') => {
    if (typeof window !== 'undefined' && window.innerWidth < 768 && panel === 'concepts') {
      setConceptsOpen(true)
      return
    }
    setSidePanel((p) => (p === panel ? null : panel))
  }
  const sendChat = () => {
    const text = chatDraft.trim()
    if (!text) return
    handleStudentSubmitAnswer(text)
    setChatDraft('')
  }

  return (
    <main className="relative w-full h-[100dvh] flex flex-col overflow-hidden bg-[#202124] text-[#E8EAED]">
      {/* Top bar */}
      <header className="flex h-12 shrink-0 items-center gap-2 px-2 sm:px-4">
        <button
          type="button"
          onClick={handleBackToDashboard}
          aria-label="Back to dashboard"
          title="Back to dashboard"
          className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full text-[#E8EAED] hover:bg-white/10 cursor-pointer"
        >
          <ArrowLeft className="h-5 w-5" />
        </button>
        <h1 className="min-w-0 flex-1 truncate text-sm font-medium sm:text-base">{resolvedTitle}</h1>
        <span className="flex shrink-0 items-center gap-1.5 rounded-full bg-white/10 px-2.5 py-1 text-xs">
          <span className={`h-1.5 w-1.5 rounded-full ${statusDot}`} />
          {statusLabel}
          {inSession && <span className="tabular-nums text-[#9AA0A6] lg:hidden">· {elapsedLabel}</span>}
        </span>
        {keyConceptsList.length > 0 && (
          <span className="hidden shrink-0 text-xs text-[#9AA0A6] sm:inline">
            Concept {Math.min(currentConceptIndex + 1, keyConceptsList.length)} of {keyConceptsList.length} · {progressPercent}%
          </span>
        )}
      </header>

      <div className="flex min-h-0 flex-1 gap-2 px-2 sm:gap-3 sm:px-3">
        {/* Stage: the board is the shared screen */}
        <section className="relative flex min-h-0 min-w-0 flex-1 flex-col overflow-hidden rounded-xl bg-[#FAF8F4] text-[var(--ink-primary)]">
          {/* Hairline 30° Axonometric Connecting Stage (initial mount only; keep board visible during silent background reconnects) */}
          {(isLoadingLesson || (connectionState === 'CONNECTING' && !hasEverConnectedRef.current)) && (
            <div className="absolute inset-0 z-50 flex items-center justify-center bg-[#FAF8F4] transition-opacity duration-300">
              <ClassroomConnectingAnimation
                connectionState={connectionState}
                stageText={isLoadingLesson ? 'Loading Authentic Board Curriculum...' : undefined}
              />
            </div>
          )}

          {!isCallActive && hasSessionStartedRef.current && (
            <div className="absolute top-4 left-1/2 -translate-x-1/2 z-40 flex items-center gap-3 px-4 py-2 rounded-full bg-[#1F3852] text-white shadow-lg border border-white/20 text-xs sm:text-sm">
              <span className={`w-2 h-2 rounded-full ${isPaused ? 'bg-amber-400' : 'bg-amber-400 animate-ping'}`} />
              <span className="font-medium">
                {isPaused
                  ? 'Lesson Paused · Progress Saved'
                  : isReconnecting
                  ? 'Reconnecting to Faculty...'
                  : 'Voice Connection Paused'}
              </span>
              <button
                type="button"
                onClick={() => {
                  reconnectAttemptsRef.current = 0
                  isUserTerminatedRef.current = false
                  handleStartClass()
                }}
                className="px-3 py-1 bg-white text-[#1F3852] font-semibold rounded-full hover:bg-white/90 transition-colors cursor-pointer text-xs"
              >
                {isPaused ? 'Resume lesson' : 'Reconnect Voice'}
              </button>
            </div>
          )}

          {!isCallActive && !hasSessionStartedRef.current && (
            <div className="absolute inset-0 z-30 flex items-center justify-center overflow-y-auto bg-[#FAF8F4] p-3 sm:p-6">
              <DashCard tone="primary" size="lg" className="w-full max-w-2xl space-y-5 p-5 sm:p-8">
                <div className="flex flex-wrap items-center gap-2">
                  <span className="text-sm font-medium text-white/80">
                    {isCompleted ? 'Review' : isPaused || currentConceptIndex > 0 || completedConcepts.length > 0 ? 'Continue learning' : 'Start learning'}
                  </span>
                  {resolvedSubject && (
                    <span className="rounded-full bg-white/10 px-3 py-0.5 text-xs font-medium text-white ring-1 ring-white/25">
                      {resolvedSubject}
                    </span>
                  )}
                </div>

                <div className="space-y-2.5">
                  <h2 className="font-editorial text-3xl leading-[1.1] text-white sm:text-4xl">{resolvedTitle}</h2>
                  {activeModule?.description && (
                    <p className="line-clamp-3 text-sm leading-relaxed text-white/80 sm:text-base">
                      {activeModule.description}
                    </p>
                  )}
                  <p className="text-sm text-white/70">
                    {keyConceptsList.length > 0 ? `${keyConceptsList.length} concepts · ` : ''}
                    {activeModule?.estimated_minutes || 15} min
                  </p>
                </div>

                <div className="flex flex-wrap items-center gap-3">
                  <button
                    id="start-module-spoken-class-btn"
                    type="button"
                    onClick={() => {
                      setIsPaused(false)
                      handleStartClass()
                    }}
                    disabled={isLoadingLesson}
                    className="inline-flex min-h-12 w-full sm:w-auto items-center justify-center gap-2.5 rounded-lg bg-white px-6 py-3 text-base font-semibold text-accent-primary shadow-xs transition-colors hover:bg-accent-primary-soft disabled:opacity-60 cursor-pointer focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-offset-2 focus-visible:ring-offset-accent-primary"
                  >
                    <Play className="w-5 h-5 fill-current" />
                    {isCompleted
                      ? 'Review chapter'
                      : isPaused || currentConceptIndex > 0 || completedConcepts.length > 0
                      ? 'Resume lesson'
                      : 'Start lesson'}
                  </button>
                  {keyConceptsList.length > 0 && (
                    <button
                      type="button"
                      onClick={() => setConceptsOpen(true)}
                      className="md:hidden inline-flex min-h-12 w-full sm:w-auto items-center justify-center gap-2 rounded-lg px-4 py-3 text-sm font-medium text-white ring-1 ring-white/30 hover:bg-white/10 cursor-pointer"
                    >
                      <Layers className="w-4 h-4" />
                      Concepts
                    </button>
                  )}
                </div>
              </DashCard>
            </div>
          )}
          <WhiteboardWorkspace
            ref={chalkboardRef}
            moduleId={moduleId}
            moduleTitle={resolvedTitle}
            classLevel={resolvedClassLevel}
            subject={resolvedSubject}
            keyConcepts={keyConceptsList}
            activeConceptIndex={currentConceptIndex}
            onPageChange={(pageIdx) => {
              setActiveGraph(null)
              isReviewingVerdictRef.current = false
              setIsReviewingVerdict(false)
              currentConceptIndexRef.current = pageIdx
              setCurrentConceptIndex(pageIdx)
              const targetConceptTitle = keyConceptsList[pageIdx] || `Concept ${pageIdx + 1}`
              setLastCoveredConcept(targetConceptTitle)
              const totalPgs = bookTotalPagesRef.current || bookTotalPages
              if (totalPgs) {
                const targetPg = resolveTargetPageForLesson({
                  conceptName: targetConceptTitle,
                  capsuleTitle: activeModule?.title,
                  chapterNumber: activeCurriculum?.order_index || activeModule?.order_index,
                  classLevel: resolvedClassLevel || activeCurriculum?.class_level || activeModule?.class_level,
                  subject: resolvedSubject || activeCurriculum?.category || activeModule?.subject,
                  pdfPath: bookPdfUrlRef.current || bookPdfUrl || undefined,
                  conceptIndex: pageIdx,
                  totalConcepts: keyConceptsList.length,
                  moduleIndex: typeof activeModule?.order_index === 'number' ? activeModule.order_index - 1 : 0,
                  totalModules: Math.max(1, siblingModules.length),
                  totalPages: totalPgs,
                })
                setBookCurrentPage(targetPg)
              }
              if (moduleId) {
                saveSessionState(moduleId, {
                  currentConceptIndex: pageIdx,
                  chalkboardPageIndex: pageIdx,
                  lastCoveredConcept: targetConceptTitle,
                })
              }
              const updatedContext = chalkboardRef.current?.getCompactBoardContext?.(pageIdx)
              if (updatedContext && connectionState !== 'DISCONNECTED' && connectionState !== 'ERROR') {
                sendBoardContext(updatedContext)
              }
            }}
            activeSceneType={activeSceneType}
            activeSceneParams={activeSceneParams}
            activeSceneTitle={activeSceneTitle}
            onCloseScene={() => setActiveSceneType(null)}
            activeGraph={activeGraph}
            onCloseGraph={() => setActiveGraph(null)}
            onOpenGraphRequest={(payload) => setActiveGraph(payload)}
            lessonManifest={lessonManifest}
            initialStepIndex={activeVisualStepIndex}
            onStepChange={(stepIdx) => setActiveVisualStepIndex(stepIdx)}
            onSaveProgress={(stepIdx, completedIds) => saveVisualProgressToSupabase(stepIdx, completedIds)}
            onNoteRecorded={handleNoteRecorded}
            onConceptFocus={handleConceptFocus}
            onConceptDone={handleConceptDone}
            onConceptGoto={handleConceptGoto}
            onBoardContentChange={handleBoardContentChange}
            onModuleComplete={(summary) => {
              markModuleAsCompleted(summary ? `#### Chapter Summary:\n${summary}` : undefined)
            }}
            onConfirmEndChapter={(question) => {
              setEndChapterConfirmPrompt(question)
            }}
            onStartQuiz={() => {
              setEndChapterConfirmPrompt(null)
              markModuleAsCompleted()
              handleOpenQuiz()
            }}
            latestTranscript={transcripts[transcripts.length - 1]?.text || ''}
            isTeacherSpeaking={connectionState === 'TEACHER_SPEAKING'}
            isListening={connectionState === 'LISTENING'}
            onSubmitStudentAnswer={handleStudentSubmitAnswer}
            onVoiceStudentAnswer={handleStudentVoiceAnswer}
            generatingDiagramTitle={generatingDiagramTitle}
            activeHighlight={activeHighlight}
            isBookOpen={isBookOpen}
            bookPdfUrl={bookPdfUrl}
            bookCurrentPage={bookCurrentPage}
            bookTotalPages={bookTotalPages}
            bookChapterTitle={bookChapterTitle}
            onCloseBook={() => setIsBookOpen(false)}
            onBookPageChange={(page) => setBookCurrentPage(page)}
          />

          {/* Live captions */}
          {captionsOn && isCallActive && teacherCaption && (
            <div className="pointer-events-none absolute inset-x-0 bottom-3 z-40 flex justify-center px-3">
              <p className="max-w-3xl rounded-lg bg-black/75 px-4 py-2 text-center text-sm leading-snug text-white line-clamp-2 sm:text-base">
                {teacherCaption.slice(-220)}
              </p>
            </div>
          )}

          {/* Mobile: floating tiles over the board */}
          {inSession && (
            <div className="absolute right-2 top-2 z-40 flex flex-col gap-2 md:hidden">
              <div className="flex h-24 w-20 items-center justify-center overflow-hidden rounded-xl bg-[#3C4043] shadow-lg">
                <ClassroomAvatar
                  state={connectionState}
                  teacherVolumeRef={teacherVolumeRef}
                  userVolumeRef={userVolumeRef}
                  isMuted={isMuted}
                  latestTranscript={latestTranscript}
                  latestVideoFrame={latestVideoFrame}
                  videoMimeType={videoMimeType}
                  onCustomAvatarChange={handleCustomAvatarChange}
                  onSimliControllerReady={handleSimliControllerReady}
                  onSimliActiveChange={handleSimliActiveChange}
                  isAvatarEnabled={isAvatarEnabled}
                  className="h-14 w-14"
                />
              </div>
              {camera.isOn && (
                <SelfViewTile stream={camera.stream} isMuted={isMuted} name="You" className="h-24 w-20 shadow-lg" />
              )}
            </div>
          )}
        </section>

        {/* Participant tiles (desktop) & completion bottom sheet (mobile) */}
        <aside className="contents md:flex md:w-[220px] md:shrink-0 md:flex-col md:gap-3 md:overflow-y-auto lg:w-[260px]">
          <div className="relative hidden aspect-[4/3] shrink-0 items-center justify-center overflow-hidden rounded-xl bg-[#3C4043] md:flex">
            <ClassroomAvatar
              state={connectionState}
              teacherVolumeRef={teacherVolumeRef}
              userVolumeRef={userVolumeRef}
              isMuted={isMuted}
              latestTranscript={latestTranscript}
              latestVideoFrame={latestVideoFrame}
              videoMimeType={videoMimeType}
              onCustomAvatarChange={handleCustomAvatarChange}
              onSimliControllerReady={handleSimliControllerReady}
              onSimliActiveChange={handleSimliActiveChange}
              isAvatarEnabled={isAvatarEnabled}
              className="h-24 w-24 lg:h-28 lg:w-28"
            />
            <div className="absolute bottom-2 left-2 rounded-md bg-black/50 px-2 py-0.5 text-xs text-white">
              Tutor{connectionState === 'TEACHER_SPEAKING' ? ' · speaking' : ''}
            </div>
          </div>
          <SelfViewTile
            stream={camera.stream}
            isMuted={isMuted}
            name={studentName ? studentName.split(' ')[0] : 'You'}
            error={camera.error}
            className="hidden aspect-[4/3] shrink-0 md:block"
          />
          <div className="contents text-[var(--ink-primary)] md:block">
          {/* Completed state: next steps (bottom sheet on mobile) */}
          {isCompleted && (
            <div className={`fixed inset-x-2 ${inSession ? 'bottom-20' : 'bottom-2'} z-40 max-h-[60dvh] overflow-y-auto md:static md:z-auto md:max-h-none p-3 rounded-2xl bg-white md:bg-[var(--accent-primary-soft)] border border-[var(--accent-primary-border)] shadow-lg md:shadow-none space-y-2`}>
              <div className="flex items-center gap-1.5 text-[var(--accent-primary)] font-semibold text-sm">
                <CheckCircle2 className="w-4 h-4 shrink-0" />
                Completed
              </div>

              {chapterNotes.trim() && (
                <div className="flex gap-2">
                  <Button
                    id="apply-clean-notes-btn"
                    onClick={() => chapterNotes && chalkboardRef.current?.rewriteNotes(chapterNotes)}
                    className="flex-1 h-9 bg-white hover:bg-stone-50 border border-[var(--border-subtle)] text-[var(--ink-primary)] rounded-xl text-xs cursor-pointer"
                  >
                    <RotateCcw className="w-3.5 h-3.5 mr-1" />
                    Notes to board
                  </Button>
                  <Button
                    id="view-clean-notes-modal-btn"
                    onClick={() => setNotesModalOpen(true)}
                    className="flex-1 h-9 bg-white hover:bg-stone-50 border border-[var(--border-subtle)] text-[var(--ink-primary)] rounded-xl text-xs cursor-pointer"
                  >
                    <BookOpen className="w-3.5 h-3.5 mr-1" />
                    View notes
                  </Button>
                </div>
              )}

              {nextSiblingModule?.id ? (
                <Button
                  id="go-to-next-capsule-btn"
                  onClick={() => leaveTo(`/dashboard/${userId}/class/${nextSiblingModule.id}`)}
                  className="w-full h-10 bg-[var(--accent-primary)] hover:bg-[var(--accent-primary-hover)] text-white rounded-xl text-sm cursor-pointer"
                >
                  <span className="truncate">Next: {nextSiblingModule.title}</span>
                  <ArrowLeft className="w-4 h-4 rotate-180 ml-1.5 shrink-0" />
                </Button>
              ) : nextChapterInfo?.firstModuleId ? (
                <Button
                  id="go-to-next-chapter-btn"
                  onClick={() => leaveTo(`/dashboard/${userId}/class/${nextChapterInfo.firstModuleId}`)}
                  className="w-full h-10 bg-[var(--accent-primary)] hover:bg-[var(--accent-primary-hover)] text-white rounded-xl text-sm cursor-pointer"
                >
                  <span className="truncate">Next chapter: {nextChapterInfo.chapterTitle}</span>
                  <ArrowLeft className="w-4 h-4 rotate-180 ml-1.5 shrink-0" />
                </Button>
              ) : null}

              <Button
                id="return-to-dashboard-btn"
                variant="outline"
                onClick={() => leaveTo(`/dashboard/${userId}`)}
                className="w-full h-9 bg-white border-[var(--border-subtle)] text-[var(--ink-secondary)] rounded-xl text-xs cursor-pointer"
              >
                Back to dashboard
              </Button>
            </div>
          )}

          {/* End-of-chapter confirmation */}
          {isCompleted && endChapterConfirmPrompt && (
            <div className={`fixed inset-x-2 ${inSession ? 'bottom-20' : 'bottom-2'} z-50 md:static md:z-auto p-3 rounded-2xl bg-white border border-[var(--accent-primary)]/50 shadow-lg md:shadow-none space-y-2.5`}>
              <p className="text-sm text-[var(--ink-primary)] leading-snug">{endChapterConfirmPrompt}</p>
              <div className="flex gap-2">
                <Button
                  id="confirm-end-yes-btn"
                  onClick={() => {
                    setEndChapterConfirmPrompt(null)
                    markModuleAsCompleted()
                    handleOpenQuiz()
                  }}
                  className="flex-1 h-10 bg-[var(--accent-primary)] hover:bg-[var(--accent-primary-hover)] text-white rounded-xl text-xs cursor-pointer"
                >
                  Take quiz
                </Button>
                <Button
                  id="confirm-end-no-btn"
                  variant="outline"
                  onClick={() => {
                    setEndChapterConfirmPrompt(null)
                    triggerCompanionGuidance({
                      animation: 'listening',
                      expression: 'attentive-left',
                      mood: 'thinking',
                      message: 'What is your doubt? Speak and your tutor will explain it on the board.',
                      autoDismissMs: 10000,
                    })
                  }}
                  className="flex-1 h-10 bg-white border-[var(--border-subtle)] text-[var(--ink-secondary)] rounded-xl text-xs cursor-pointer"
                >
                  I have doubts
                </Button>
              </div>
            </div>
          )}

          </div>
        </aside>

        {/* Side panel: concepts / chat */}
        {sidePanel && (
          <aside className="fixed inset-0 z-50 flex flex-col bg-white text-[var(--ink-primary)] md:static md:z-auto md:w-[320px] md:shrink-0 md:rounded-xl">
            <div className="flex items-center justify-between px-4 py-3">
              <span className="text-base font-medium">
                {sidePanel === 'chat' ? 'Chat with tutor' : `Concepts · ${progressPercent}%`}
              </span>
              <button
                type="button"
                onClick={() => setSidePanel(null)}
                aria-label="Close panel"
                className="flex h-9 w-9 items-center justify-center rounded-full hover:bg-stone-100 cursor-pointer"
              >
                <X className="h-5 w-5" />
              </button>
            </div>
            {sidePanel === 'concepts' ? (
              <div className="min-h-0 flex-1 overflow-y-auto px-3 pb-3">
                <div className="mx-1 mb-2 h-1 overflow-hidden rounded-full bg-stone-200">
                  <div
                    className="h-full bg-[var(--accent-primary)] transition-all duration-500"
                    style={{ width: `${progressPercent}%` }}
                  />
                </div>
                {conceptList}
                <button
                  type="button"
                  onClick={() => handleConceptGoto(1)}
                  className="mt-2 px-3 text-xs text-[var(--accent-primary)] hover:underline cursor-pointer"
                >
                  Restart from first concept
                </button>
              </div>
            ) : (
              <>
                <div className="flex min-h-0 flex-1 flex-col-reverse overflow-y-auto px-4 pb-3">
                  <div className="space-y-3">
                    {transcripts.length === 0 && (
                      <p className="pt-6 text-center text-sm text-[var(--ink-secondary)]">
                        Type a question and your tutor will answer it out loud and on the board.
                      </p>
                    )}
                    {transcripts.slice(-60).map((t) => (
                      <div key={t.id} className={t.sender === 'user' ? 'text-right' : ''}>
                        <p className="text-[11px] font-medium text-[var(--ink-secondary)]">
                          {t.sender === 'user' ? 'You' : 'Tutor'}
                        </p>
                        <p
                          className={`inline-block max-w-[90%] rounded-2xl px-3 py-2 text-left text-sm leading-snug ${
                            t.sender === 'user' ? 'bg-[var(--accent-primary)] text-white' : 'bg-stone-100'
                          }`}
                        >
                          {t.text}
                        </p>
                      </div>
                    ))}
                  </div>
                </div>
                <form
                  onSubmit={(e) => {
                    e.preventDefault()
                    sendChat()
                  }}
                  className="m-3 flex items-center gap-2 rounded-full bg-stone-100 py-1 pl-4 pr-1"
                >
                  <input
                    value={chatDraft}
                    onChange={(e) => setChatDraft(e.target.value)}
                    placeholder={isCallActive ? 'Ask your tutor…' : 'Start the lesson to chat'}
                    disabled={!isCallActive}
                    className="min-w-0 flex-1 bg-transparent text-sm outline-none placeholder:text-stone-400"
                  />
                  <button
                    type="submit"
                    disabled={!isCallActive || !chatDraft.trim()}
                    aria-label="Send"
                    className="flex h-9 w-9 items-center justify-center rounded-full bg-[var(--accent-primary)] text-white disabled:opacity-40 cursor-pointer"
                  >
                    <ChevronRight className="h-5 w-5" />
                  </button>
                </form>
              </>
            )}
          </aside>
        )}
      </div>

      {/* Bottom control bar */}
      {inSession ? (
        <ClassroomControlBar
          isMuted={isMuted}
          userVolumeRef={userVolumeRef}
          onToggleMute={toggleMute}
          isCameraOn={camera.isOn}
          onToggleCamera={camera.toggle}
          isPaused={isPaused}
          onTogglePause={isPaused ? handleStartClass : handlePauseClass}
          captionsOn={captionsOn}
          onToggleCaptions={() => setCaptionsOn((c) => !c)}
          hasBook={!!bookPdfUrl}
          isBookOpen={isBookOpen}
          onToggleBook={() => setIsBookOpen((p) => !p)}
          activePanel={sidePanel}
          onTogglePanel={togglePanel}
          conceptProgress={
            keyConceptsList.length > 0
              ? `${Math.min(currentConceptIndex + 1, keyConceptsList.length)}/${keyConceptsList.length}`
              : undefined
          }
          onNextConcept={() => {
            lastVerdictStatusRef.current = 'correct'
            handleConceptDone('EXPLICIT_USER_ADVANCE')
          }}
          onEndCall={() => {
            camera.stop()
            handleEndClass()
          }}
          onOpenSettings={handleGoToSettings}
          onOpenNotes={chapterNotes.trim() ? () => setNotesModalOpen(true) : undefined}
          onOpenQuiz={handleOpenQuiz}
          onMarkComplete={!isCompleted ? () => markModuleAsCompleted() : undefined}
          elapsed={elapsedLabel}
          title={resolvedTitle}
        />
      ) : (
        <div className="h-3 shrink-0" />
      )}

      {/* Mobile concepts sheet */}
      {conceptsOpen && (
        <div className="md:hidden fixed inset-0 z-50 flex items-end bg-black/40" onClick={() => setConceptsOpen(false)}>
          <div
            className="w-full max-h-[70dvh] overflow-y-auto rounded-t-3xl bg-white p-4 pb-6"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between pb-2">
              <span className="text-sm font-medium text-[var(--ink-primary)]">
                Concepts · {progressPercent}%
              </span>
              <button
                type="button"
                onClick={() => setConceptsOpen(false)}
                aria-label="Close"
                className="w-9 h-9 flex items-center justify-center rounded-full hover:bg-stone-100 cursor-pointer"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
            {conceptList}
            {!isCompleted && (
              <button
                type="button"
                onClick={() => {
                  markModuleAsCompleted()
                  setConceptsOpen(false)
                }}
                className="mt-3 w-full h-10 rounded-xl border border-[var(--border-subtle)] text-xs text-[var(--ink-secondary)] cursor-pointer"
              >
                Mark complete
              </button>
            )}
          </div>
        </div>
      )}

      {/* Chapter Notes Modal */}
      <ChapterNotesModal
        isOpen={notesModalOpen}
        onClose={() => setNotesModalOpen(false)}
        moduleTitle={resolvedTitle}
        classLevel={resolvedClassLevel}
        subject={resolvedSubject}
        chapterNotes={chapterNotes}
        notesSaveStatus={notesSaveStatus}
      />

      {/* 10-Question Mastery Evaluation Modal (Available anytime!) */}
      {activeModule && (
        <MasteryQuizModal
          isOpen={quizOpen}
          onClose={() => setQuizOpen(false)}
          moduleId={activeModule.id}
          moduleTitle={activeModule.title}
          onCompleteSuccess={() => {
            markModuleAsCompleted()
          }}
        />
      )}

      {/* Error Modal */}
      {errorMessage && <ErrorModal message={errorMessage} onRetry={resetToIdle} />}
    </main>
  )
}

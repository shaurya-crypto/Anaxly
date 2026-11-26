import { z } from 'zod'
import { GoogleGenAI } from '@google/genai'
import { evaluate, derivative as mathDerivative } from 'mathjs'
import { resilientGenerateContent, resilientJsonParse } from '@/lib/geminiResilientGenerate'
import {
  hybridRetrieveTextbookChunks,
  lookupConceptPrerequisites,
  normalizeClassLevelInt,
  canonicalSubjectForRag,
} from '@/lib/rag/textbookRag'

export const TEACHING_MOVES = [
  'INTUITION_ANALOGY',
  'TINY_NUMBER_TEST',
  'ANIMATED_VISUAL_GRAPH',
  'PREREQUISITE_REPAIR',
  'STEP_BY_STEP_COACH',
] as const

export type TeachingMoveType = (typeof TEACHING_MOVES)[number]

export const TutorThinkInputSchema = z.object({
  questionOrTopic: z.string().min(1).max(1000),
  studentMessage: z.string().min(1).max(2000),
  classLevel: z.union([z.number(), z.string()]).default(10),
  subject: z.string().default('Mathematics'),
  board: z.string().default('CBSE'),
  chapterNumber: z.number().int().positive().optional(),
  boardState: z.string().max(4000).optional(),
  struggleCount: z.number().int().min(0).max(20).optional(),
})

export type TutorThinkInput = z.infer<typeof TutorThinkInputSchema>

export interface VerifiedMathCheck {
  expression: string
  claimedValue?: string
  evaluatedValue: string
  verified: boolean
}

export interface TutorThinkOutput {
  teachingMove: TeachingMoveType
  diagnosis: string
  spokenGuidance: string
  everydayAnalogy: string
  chalkboardSteps: Array<{
    action: 'draw_note' | 'draw_step' | 'draw_highlight_box' | 'draw_question'
    content: string
    color: string
  }>
  visualGraphSpec?: {
    title: string
    formula?: string
    formulas?: string[]
    points?: Array<{ x: number; y: number; label?: string }>
    segments?: Array<{ start: [number, number]; end: [number, number]; label?: string }>
    circles?: Array<{ center: [number, number]; radius: number; label?: string }>
    polygons?: Array<{ points: Array<[number, number]>; label?: string }>
    vectors?: Array<{ tail: [number, number]; tip: [number, number]; label?: string }>
    callout?: string
  } | null
  shapeSpec?: {
    shape: string
    label?: string
    values?: Record<string, string>
  } | null
  prerequisiteBridge?: {
    prerequisiteKey: string
    prerequisiteClassLevel: number | null
    bridgeNote: string
  } | null
  verifiedMath: VerifiedMathCheck[]
  followUpCheckQuestion: string
  ragSources: Array<{
    sectionTitle: string
    pageNumber: number | null
    chunkType: string
    source: string
  }>
  modelUsed: string
}

/**
 * Deterministically evaluates and verifies mathematical expressions/derivatives with mathjs
 * so the live voice tutor never speaks unverified arithmetic or derivative mistakes.
 */
export function verifyMathWithMathJs(
  checks: Array<{ expression: string; expected?: string | number }>
): VerifiedMathCheck[] {
  const results: VerifiedMathCheck[] = []
  for (const item of checks.slice(0, 6)) {
    const rawExpr = String(item.expression || '').trim()
    if (!rawExpr) continue
    try {
      let evaluated: any
      const derivMatch = rawExpr.match(/^d\/d([a-zA-Z])\s*\((.+)\)$/)
      if (derivMatch) {
        evaluated = mathDerivative(derivMatch[2], derivMatch[1]).toString()
      } else {
        evaluated = evaluate(rawExpr)
      }
      const evalStr =
        typeof evaluated === 'number'
          ? Number.isInteger(evaluated)
            ? String(evaluated)
            : Number(evaluated.toFixed(4)).toString()
          : String(evaluated)

      let verified = true
      if (item.expected !== undefined && item.expected !== null && String(item.expected).trim() !== '') {
        try {
          const expEval = evaluate(String(item.expected))
          if (typeof expEval === 'number' && typeof evaluated === 'number') {
            verified = Math.abs(expEval - evaluated) < 1e-4
          } else {
            verified = evalStr.replace(/\s+/g, '') === String(item.expected).replace(/\s+/g, '')
          }
        } catch {
          verified = evalStr.replace(/\s+/g, '') === String(item.expected).replace(/\s+/g, '')
        }
      }

      results.push({
        expression: rawExpr,
        claimedValue: item.expected !== undefined ? String(item.expected) : undefined,
        evaluatedValue: evalStr,
        verified,
      })
    } catch {
      results.push({
        expression: rawExpr,
        claimedValue: item.expected !== undefined ? String(item.expected) : undefined,
        evaluatedValue: 'unparsed',
        verified: false,
      })
    }
  }
  return results
}

export function selectFallbackTeachingMove(input: TutorThinkInput): TeachingMoveType {
  const msg = input.studentMessage.toLowerCase()
  const sub = canonicalSubjectForRag(input.subject, normalizeClassLevelInt(input.classLevel)).toLowerCase()
  if (/graph|plot|draw|line|circle|curve|slope|vector|shape|visual/i.test(msg)) {
    return 'ANIMATED_VISUAL_GRAPH'
  }
  if (/basic|forgot|why|where did|formula come from|previous|class 9|class 10/i.test(msg)) {
    return 'PREREQUISITE_REPAIR'
  }
  if ((input.struggleCount ?? 0) >= 2 || /didn't understand|samajh nahi|confused|hard|again/i.test(msg)) {
    return sub === 'mathematics' || sub === 'physics' ? 'TINY_NUMBER_TEST' : 'INTUITION_ANALOGY'
  }
  return 'STEP_BY_STEP_COACH'
}

export async function runPedagogicalThinkEngine(
  rawInput: TutorThinkInput,
  options?: { apiKey?: string; skipLlm?: boolean }
): Promise<TutorThinkOutput> {
  const input = TutorThinkInputSchema.parse(rawInput)
  const classInt = normalizeClassLevelInt(input.classLevel)
  const subjectNorm = canonicalSubjectForRag(input.subject, classInt)
  const isMath = subjectNorm.toLowerCase() === 'mathematics'

  const combinedQuery = `${input.questionOrTopic} ${input.studentMessage}`.trim()

  const [ragChunks, prerequisites] = await Promise.all([
    hybridRetrieveTextbookChunks({
      query: combinedQuery,
      classLevel: classInt,
      subject: subjectNorm,
      chapterNumber: input.chapterNumber,
      limit: 4,
    }),
    lookupConceptPrerequisites({
      query: combinedQuery,
      classLevel: classInt,
      subject: subjectNorm,
    }),
  ])

  const ragSources = ragChunks.map((c) => ({
    sectionTitle: c.sectionTitle,
    pageNumber: c.pageNumber,
    chunkType: c.chunkType,
    source: c.source,
  }))

  const primaryPrereq = prerequisites[0] || null
  const fallbackMove = selectFallbackTeachingMove(input)

  const apiKey = options?.apiKey ?? process.env.GEMINI_API_KEY
  if (options?.skipLlm || !apiKey) {
    return {
      teachingMove: fallbackMove,
      diagnosis: 'Student needs a smaller, concrete step before continuing the formal solution.',
      spokenGuidance: isMath
        ? `Let us pause the heavy symbols and test ${input.questionOrTopic} with simple whole numbers first. Watch what happens on the board as we trace one small step together.`
        : `Let us step back from the textbook wording and connect ${input.questionOrTopic} to something you see every day. I am putting a clean visual step on the board now.`,
      everydayAnalogy:
        'Think of it like measuring two landmarks on a school ground or tracking speed on a bike ride.',
      chalkboardSteps: [
        {
          action: 'draw_note',
          content: primaryPrereq
            ? `Quick Link: ${primaryPrereq.bridgeNote}`
            : `Core Idea: Break ${input.questionOrTopic} into one small test case first.`,
          color: 'botanical',
        },
      ],
      visualGraphSpec: null,
      shapeSpec: null,
      prerequisiteBridge: primaryPrereq
        ? {
            prerequisiteKey: primaryPrereq.prerequisiteKey,
            prerequisiteClassLevel: primaryPrereq.prerequisiteClassLevel,
            bridgeNote: primaryPrereq.bridgeNote,
          }
        : null,
      verifiedMath: [],
      followUpCheckQuestion: isMath
        ? 'Did you follow how this smaller step works?'
        : 'Does this everyday picture make sense so far?',
      ragSources,
      modelUsed: 'deterministic-fallback',
    }
  }

  const ragContext =
    ragChunks.length > 0
      ? ragChunks
          .map(
            (c, i) =>
              `[Chunk ${i + 1} | ${c.chunkType} | Pg ${c.pageNumber ?? '?'} | ${c.sectionTitle}]: ${c.content.slice(0, 450)}`
          )
          .join('\n')
      : 'No chunk excerpts matched; use verified Class 9-12 NCERT/ICSE/IB subject accuracy.'

  const prereqContext =
    prerequisites.length > 0
      ? prerequisites
          .map(
            (p) =>
              `- ${p.prerequisiteKey} (Class ${p.prerequisiteClassLevel ?? '?'}): ${p.bridgeNote}`
          )
          .join('\n')
      : 'None needed unless student missed an earlier-grade algebraic/geometric link.'

  const systemPrompt = `You are a master diagnostic tutor co-pilot (HeyAristotle / Gauth caliber) advising a live voice tutor for Class ${classInt} ${subjectNorm} (${input.board}).
Return ONLY valid JSON matching the exact schema below.

PEDAGOGICAL RULES:
1. Choose ONE diagnostic teachingMove from: INTUITION_ANALOGY, TINY_NUMBER_TEST, ANIMATED_VISUAL_GRAPH, PREREQUISITE_REPAIR, STEP_BY_STEP_COACH.
2. Keep spokenGuidance to 2-3 short, natural, human sentences (no textbook stiffness, no robotic filler).
3. ${isMath ? 'MATHEMATICS RULE: NEVER mention "definition" or ask "Did you understand the definition?". Focus on concept, theorem, intuition, and solving method; ask "Did you follow this concept?"' : 'Connect physical/chemical/biological mechanism to an everyday real-world experience first.'}
4. If the topic involves coordinates, lines, curves, circles, triangles, vectors, kinematics (v-t, s-t), Ohm law (V-I), or P-V curves, populate visualGraphSpec with exact non-empty coordinates/formula/circles/polygons. NEVER output formula="x" without purpose.
5. Put any numeric evaluations or derivatives you rely on into mathChecks: [{"expression": "...", "expected": "..."}] using standard mathjs syntax (e.g. "sqrt((7-2)^2 + (3-3)^2)" or "d/dx(x^3 + 2*x)").
6. Use Unicode math symbols in chalkboardSteps (x², √, ×, ÷, θ, Δ) — NO raw *, **, or ^ in display text.

JSON SCHEMA:
{
  "teachingMove": "INTUITION_ANALOGY | TINY_NUMBER_TEST | ANIMATED_VISUAL_GRAPH | PREREQUISITE_REPAIR | STEP_BY_STEP_COACH",
  "diagnosis": "1-sentence diagnosis of student confusion or error",
  "spokenGuidance": "2-3 natural conversational sentences for the voice tutor to say now",
  "everydayAnalogy": "1 crisp student-relatable real-world analogy",
  "chalkboardSteps": [
    { "action": "draw_note | draw_step | draw_highlight_box | draw_question", "content": "...", "color": "botanical | blue | amber | white | coral" }
  ],
  "visualGraphSpec": null or {
    "title": "...",
    "formula": "optional",
    "formulas": ["optional"],
    "points": [{"x": 0, "y": 0, "label": "O(0, 0)"}],
    "segments": [{"start": [0, 0], "end": [3, 4], "label": "d = 5"}],
    "circles": [{"center": [0, 0], "radius": 5, "label": "r = 5"}],
    "polygons": [{"points": [[0, 0], [3, 0], [0, 4]], "label": "Right Triangle"}],
    "vectors": [{"tail": [0, 0], "tip": [3, 4], "label": "v"}],
    "callout": "..."
  },
  "shapeSpec": null or { "shape": "triangle | circle | cone | cylinder | parallelogram | number_line | angle_arc", "label": "...", "values": {} },
  "mathChecks": [{ "expression": "...", "expected": "..." }],
  "followUpCheckQuestion": "1 short focused checkpoint question"
}`

  const userPrompt = `TOPIC/QUESTION: ${input.questionOrTopic}
STUDENT MESSAGE/ATTEMPT: ${input.studentMessage}
STRUGGLE COUNT: ${input.struggleCount ?? 0}
CURRENT CHALKBOARD: ${input.boardState ? input.boardState.slice(0, 1200) : 'Empty/Fresh'}

GROUNDED TEXTBOOK CHUNKS:
${ragContext}

PREREQUISITE LINKS:
${prereqContext}`

  const ai = new GoogleGenAI({ apiKey })
  const { text, modelUsed } = await resilientGenerateContent(ai, {
    contents: userPrompt,
    preferredModels: ['gemini-3.8-flash', 'gemini-3.5-flash', 'gemini-2.5-flash'],
    maxRounds: 1,
    timeoutMs: 12000,
    label: 'TutorThinkCoPilot',
    config: {
      systemInstruction: systemPrompt,
      responseMimeType: 'application/json',
      temperature: 0.35,
      maxOutputTokens: 2048,
      thinkingConfig: { thinkingBudget: 512 },
    },
  })

  const parsed = resilientJsonParse<any>(text, 'TutorThinkCoPilot')
  const move: TeachingMoveType = TEACHING_MOVES.includes(parsed?.teachingMove)
    ? parsed.teachingMove
    : fallbackMove

  const verifiedMath = Array.isArray(parsed?.mathChecks)
    ? verifyMathWithMathJs(parsed.mathChecks)
    : []

  const rawSteps = Array.isArray(parsed?.chalkboardSteps) ? parsed.chalkboardSteps.slice(0, 4) : []
  const chalkboardSteps = rawSteps
    .filter((s: any) => s && typeof s.content === 'string' && s.content.trim())
    .map((s: any) => ({
      action: (['draw_note', 'draw_step', 'draw_highlight_box', 'draw_question'].includes(s.action)
        ? s.action
        : 'draw_note') as 'draw_note' | 'draw_step' | 'draw_highlight_box' | 'draw_question',
      content: String(s.content).trim(),
      color: String(s.color || 'botanical'),
    }))

  let followUp = String(parsed?.followUpCheckQuestion || '').trim()
  if (isMath && /\bdefinition\b/i.test(followUp)) {
    followUp = 'Did you follow how this concept works?'
  }
  if (!followUp) {
    followUp = isMath ? 'Did you follow that concept so far?' : 'Does that step make sense?'
  }

  return {
    teachingMove: move,
    diagnosis: String(parsed?.diagnosis || 'Clarifying core concept with concrete intuition.'),
    spokenGuidance: String(parsed?.spokenGuidance || ''),
    everydayAnalogy: String(parsed?.everydayAnalogy || ''),
    chalkboardSteps,
    visualGraphSpec: parsed?.visualGraphSpec && typeof parsed.visualGraphSpec === 'object' ? parsed.visualGraphSpec : null,
    shapeSpec: parsed?.shapeSpec && typeof parsed.shapeSpec === 'object' ? parsed.shapeSpec : null,
    prerequisiteBridge: primaryPrereq
      ? {
          prerequisiteKey: primaryPrereq.prerequisiteKey,
          prerequisiteClassLevel: primaryPrereq.prerequisiteClassLevel,
          bridgeNote: primaryPrereq.bridgeNote,
        }
      : null,
    verifiedMath,
    followUpCheckQuestion: followUp,
    ragSources,
    modelUsed,
  }
}

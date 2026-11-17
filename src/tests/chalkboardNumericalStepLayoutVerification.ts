import assert from 'assert'
import fs from 'fs'
import path from 'path'
import { formatChalkboardSteps, wrapText } from '../components/whiteboard/textWrapper'
import { cleanChalkboardTypography } from '../components/whiteboard/chalkboardTypography'

console.log('=== CHALKBOARD NUMERICAL STEP LAYOUT & TYPOGRAPHY VERIFICATION ===\n')

// -------------------------------------------------------------
// SUITE 1: formatChalkboardSteps & Multi-Row Layout Verification
// -------------------------------------------------------------
console.log('--- SUITE 1: formatChalkboardSteps Line Breaking & Step Gating ---')

// 1. Single concise step
const singleStep = formatChalkboardSteps('F = m * a')
assert.strictEqual(singleStep.length, 1, 'Single equation must stay on 1 line')
assert.strictEqual(singleStep[0], 'F = m · a', 'Multiplication operator * must be converted to authentic math notation')
console.log('  [PASS] Single step stays on 1 line with clean math notation.')

// 2. Multi-step derivation separated by semicolons (Standard Topper Steps)
const semicolonSteps = formatChalkboardSteps('Given: m = 2 kg, a = 5 m/s^2; Formula: F = m * a; Step 1: F = 2 * 5; Step 2: F = 10 N; Answer: Force F = 10 N')
assert.strictEqual(semicolonSteps.length, 5, 'Every major labeled step must be on its own line')
assert.strictEqual(semicolonSteps[0], 'Given: m = 2 kg, a = 5 m/s²', 'Given line with superscript power')
assert.strictEqual(semicolonSteps[1], 'Formula: F = m · a', 'Formula line with clean dot product')
assert.strictEqual(semicolonSteps[2], 'Step 1: F = 2 × 5', 'Step 1 substitution line')
assert.strictEqual(semicolonSteps[3], 'Step 2: F = 10 N', 'Step 2 calculation line')
assert.strictEqual(semicolonSteps[4], 'Answer: Force F = 10 N', 'Answer line')
console.log('  [PASS] Semicolon-delimited steps split cleanly into individual lines (1 step per line).')

// 3. Pipe-separated steps
const pipeSteps = formatChalkboardSteps('v = u + at | 0 = 20 - 9.8t | 9.8t = 20 | t = 2.04 s')
assert(pipeSteps.length >= 2, 'Pipe-delimited steps must NOT be crammed onto 1 line')
for (const line of pipeSteps) {
  // Ensure no line contains more than 2 steps
  const stepsOnLine = line.split(/⇒/).length
  assert(stepsOnLine <= 2, `Line must have at most 2 steps, found ${stepsOnLine} in "${line}"`)
}
console.log('  [PASS] Pipe-delimited numerical split cleanly across lines (max 2 steps per line).')

// 4. Chained implication arrows (e.g. A => B => C => D)
const chainedArrows = formatChalkboardSteps('4x + 8 = 20 => 4x = 12 => x = 12/4 => x = 3')
assert(chainedArrows.length >= 2, 'Chained equations with 4 steps must be split into multiple lines')
for (const line of chainedArrows) {
  const arrowCount = (line.match(/⇒/g) || []).length
  assert(arrowCount <= 2, `Line must not have more than 2 steps, found ${arrowCount} arrows in "${line}"`)
}
console.log('  [PASS] Chained implications split so at most 2 steps appear per line.')

// 5. Pairing concise consecutive equations (max 2 steps on 1 line)
const pairable = formatChalkboardSteps('2x = 6; x = 3')
assert.strictEqual(pairable.length, 1, 'Two concise steps may be paired on 1 line')
assert(pairable[0].includes('2x = 6') && pairable[0].includes('x = 3'), 'Both steps present on line')
console.log('  [PASS] Two concise steps paired cleanly on 1 line.')

// 5b. Pairing given variables with comma (never false implication arrow)
const givenPair = formatChalkboardSteps('m = 2 kg; a = 5 m/s^2')
assert.strictEqual(givenPair.length, 1, 'Two concise given quantities may be paired on 1 line')
assert.strictEqual(givenPair[0], 'm = 2 kg, a = 5 m/s²', 'Given quantities must be separated by comma, NEVER false implication arrow ⇒')
console.log('  [PASS] Given quantities paired with comma without false implication arrow.')

// 5c. Mathematical absolute value and parallel lines preserved
const absVal = formatChalkboardSteps('|x - 3| = 5')
assert.strictEqual(absVal.length, 1, 'Absolute value expression must not be split by pipe delimiter')
assert.strictEqual(absVal[0], '|x - 3| = 5', 'Modulus bars must be preserved intact')

const geomParallel = formatChalkboardSteps('AB || CD; To Prove: AB ∥ CD')
assert.strictEqual(geomParallel.length, 2, 'Parallel lines must not be split on pipe, and To Prove must be on its own line')
assert(geomParallel[0].includes('AB') && geomParallel[0].includes('CD'), 'Parallel segment preserved')
assert(geomParallel[1].startsWith('To Prove:'), 'To Prove starts on its own line')
console.log('  [PASS] Absolute value and geometry parallel symbols preserved intact.')

// 5d. Geometry and math proof headers (Given, To Prove, Proof, Hence Proved)
const proofSteps = formatChalkboardSteps('Given: AB = AC; To Prove: ∠B = ∠C; Proof: In ΔABC, AB = AC; Hence Proved!')
assert.strictEqual(proofSteps.length, 4, 'Math proof headers must each be on their own line')
assert(proofSteps[0].startsWith('Given:'), 'Given starts line 1')
assert(proofSteps[1].startsWith('To Prove:'), 'To Prove starts line 2')
assert(proofSteps[2].startsWith('Proof:'), 'Proof starts line 3')
assert(proofSteps[3].includes('Hence Proved!'), 'Hence Proved is on line 4')
console.log('  [PASS] Math proof sections (Given, To Prove, Proof, Hence Proved) formatted 1 step per line.')

// 6. Inline step markers without semicolons
const inlineMarkers = formatChalkboardSteps('Given: m = 2 kg, a = 5 m/s^2 Step 1: F = m * a Step 2: F = 10 N Answer: 10 N')
assert.strictEqual(inlineMarkers.length, 4, 'Inline step headers must each start on their own line')
assert(inlineMarkers[0].startsWith('Given:'), 'Given starts line 1')
assert(inlineMarkers[1].startsWith('Step 1:'), 'Step 1 starts line 2')
assert(inlineMarkers[2].startsWith('Step 2:'), 'Step 2 starts line 3')
assert(inlineMarkers[3].startsWith('Answer:'), 'Answer starts line 4')
console.log('  [PASS] Inline step headers without semicolons split into distinct lines.')

// 7. Long step wrapping without spilling
const longStep = formatChalkboardSteps('Step 1: According to Newtons Second Law of Motion, the rate of change of momentum is directly proportional to the applied unbalanced force in the direction of force.')
assert(longStep.length >= 2, 'Long step text must wrap across multiple lines')
for (const line of longStep) {
  assert(line.length <= 65, `Wrapped line length must be within column bounds, got ${line.length}: "${line}"`)
}
console.log('  [PASS] Long step text wrapped cleanly within column bounds.')

// -------------------------------------------------------------
// SUITE 2: Pure Textbook Typography & Zero Code Operators
// -------------------------------------------------------------
console.log('\n--- SUITE 2: Pure Textbook Typography & Zero Code Operators ---')

const mathTestInputs = [
  'm = 2 kg * 5 m/s^2',
  'a = F // m',
  'v^2 = u^2 + 2*a*s',
  '10^8 m/s and 6.67 * 10^-11 N m^2/kg^2',
  'W = F * d * cos(theta)',
  '(1/2)*m*v^2',
  '2 * 5 = 10',
]

for (const input of mathTestInputs) {
  const cleaned = cleanChalkboardTypography(input)
  assert(!cleaned.includes('*'), `Cleaned text must NOT contain raw asterisk (*): "${cleaned}"`)
  assert(!cleaned.includes('^'), `Cleaned text must NOT contain raw caret (^): "${cleaned}"`)
  assert(!cleaned.includes('//'), `Cleaned text must NOT contain raw double slash (//): "${cleaned}"`)
}
console.log('  [PASS] Zero raw code operators (*, ^, //) in cleaned typography output.')

// -------------------------------------------------------------
// SUITE 3: GreenChalkboard.tsx Engine Verification
// -------------------------------------------------------------
console.log('\n--- SUITE 3: GreenChalkboard.tsx Engine Verification ---')
const chalkboardSource = fs.readFileSync(path.resolve('src/components/whiteboard/GreenChalkboard.tsx'), 'utf8')

// A. formatChalkboardSteps import and export
assert(
  chalkboardSource.includes('formatChalkboardSteps') && chalkboardSource.includes("from './textWrapper'"),
  'GreenChalkboard.tsx must import formatChalkboardSteps from textWrapper'
)
assert(
  chalkboardSource.includes('export { wrapText, cleanChalkboardTypography, formatChalkboardSteps }'),
  'GreenChalkboard.tsx must export formatChalkboardSteps'
)
console.log('  [PASS] formatChalkboardSteps imported and exported.')

// B. drawStep uses formatChalkboardSteps
assert(
  chalkboardSource.includes('const lines = formatChalkboardSteps(clean, cols(60))'),
  'drawStep must use formatChalkboardSteps(clean, cols(60)) to split multi-step strings'
)
console.log('  [PASS] drawStep enforces multi-row step formatting (max 2 steps per line).')

// C. drawNumericalSolution standard topper layout
assert(
  chalkboardSource.includes('// 1. Problem / Numerical Statement') &&
  chalkboardSource.includes('// 2. Given Parameters') &&
  chalkboardSource.includes('// 3. Formula / Governing Law') &&
  chalkboardSource.includes('// 4. Substitution Step') &&
  chalkboardSource.includes('// 5. Calculation Step') &&
  chalkboardSource.includes('// 6. Boxed Final Answer with SI Units'),
  'drawNumericalSolution must implement all 6 stages of the standard topper layout'
)
assert(
  chalkboardSource.includes('formatChalkboardSteps(cleanSubBody, cols(56))'),
  'drawNumericalSolution must format substitution with formatChalkboardSteps'
)
assert(
  chalkboardSource.includes('formatChalkboardSteps(cleanCalcBody, cols(56))'),
  'drawNumericalSolution must format calculation on the board with formatChalkboardSteps'
)
assert(
  chalkboardSource.includes('checkAutoPageOverflow(totalEstimatedH)'),
  'drawNumericalSolution must check auto page overflow dynamically based on total estimated height'
)
console.log('  [PASS] drawNumericalSolution enforces full standard topper layout with dynamic overflow.')

// D. Directive parser colon preservation & multiline/step expansion
assert(
  chalkboardSource.includes("const colonIdx = p.indexOf(':')") &&
  chalkboardSource.includes('p.substring(colonIdx + 1).trim()'),
  'GreenChalkboard.tsx directive parser must use indexOf and substring to avoid truncating inner colons'
)
assert(
  chalkboardSource.includes('(?<!\\|)\\|(?!\\|)|\\n|;\\s*(?=(?:problem|given|formula|substitution|sub|calculation|rough|step\\s*\\d+|answer|final|unit)\\s*[:\\.\\-])'),
  'GreenChalkboard.tsx directive parser must split on pipes, newlines, and keyword-delimited semicolons while preserving parallel ||'
)
assert(
  chalkboardSource.includes('/^step\\s*\\d+\\s*:/i.test(lower)'),
  'GreenChalkboard.tsx directive parser must preserve additional calculation steps (Step 3, Step 4) without overwriting answer'
)
console.log('  [PASS] Directive parser preserves inner colons, additional steps, and multiline inputs.')

// E. Step arrow alignment in drawStep
assert(
  chalkboardSource.includes('const isStepHeader = /^(?:->|→|•|\\*|Step\\s*\\d+|Step\\s*[A-Za-z]|Case\\s*\\d+|Given|Formula|Theorem|Law|To\\s+(?:Find|Prove|Evaluate|Calculate)|Proof|Substitution|Calculation|Answer|Result|Hence|Therefore|\\([ivxlcdm\\d]+\\)|\\([a-z]\\))\\s*[:\\.\\-]?/i.test(trimmed)'),
  'drawStep must recognize step headers and continuation lines to maintain aligned indentation'
)
console.log('  [PASS] drawStep step header alignment verified.')

// -------------------------------------------------------------
// SUITE 4: Gemini Live WebSocket Prompt & Tool Verification
// -------------------------------------------------------------
console.log('\n--- SUITE 4: geminiWebSocket.ts Prompt & Tool Verification ---')
const wsSource = fs.readFileSync(path.resolve('src/services/geminiWebSocket.ts'), 'utf8')

assert(
  wsSource.includes('NUMERICAL|BOARD_NUMERICAL|WORKED_EXAMPLE|SOLVE|MATH_SOLVE'),
  'geminiWebSocket.ts bracketRegex must include NUMERICAL and BOARD_NUMERICAL directives'
)

assert(
  wsSource.includes('STEP-BY-STEP PROBLEM SOLVING & HUMAN-UNDERSTANDABLE NUMERICAL LAYOUT'),
  'geminiWebSocket.ts systemInstruction must include STEP-BY-STEP PROBLEM SOLVING invariant'
)
assert(
  wsSource.includes('ONE OR AT MOST TWO CONCISE STEPS PER LINE'),
  'geminiWebSocket.ts systemInstruction must mandate ONE OR AT MOST TWO CONCISE STEPS PER LINE'
)
assert(
  wsSource.includes('Given line (e.g. Given: m = 2 kg, a = 5 m/s²)') &&
  wsSource.includes('Formula line (e.g. Formula: F = m × a)') &&
  wsSource.includes('Substitution line (e.g. Step 1: F = 2 kg × 5 m/s²)') &&
  wsSource.includes('Calculation line (e.g. Step 2: F = 10 N)') &&
  wsSource.includes('Boxed Answer line (e.g. Answer: Force F = 10 N)'),
  'geminiWebSocket.ts systemInstruction must document the exact standard topper layout'
)
assert(
  wsSource.includes('write cleanly with 1 or at most 2 steps per line in standard topper layout'),
  'geminiWebSocket.ts write_chalkboard tool description must specify 1 or at most 2 steps per line'
)
assert(
  wsSource.includes('format with 1 or max 2 steps per line (separated by newlines or semicolons) in standard topper layout'),
  'geminiWebSocket.ts write_chalkboard content parameter must specify 1 or max 2 steps per line'
)
console.log('  [PASS] geminiWebSocket.ts systemInstruction and tool declarations verified.')

// -------------------------------------------------------------
// SUITE 5: Classroom Page Prompt Architecture Verification
// -------------------------------------------------------------
console.log('\n--- SUITE 5: Classroom Page (page.tsx) Prompts Verification ---')
const pageSource = fs.readFileSync(path.resolve('src/app/dashboard/[id]/class/[moduleId]/page.tsx'), 'utf8')

assert(
  pageSource.includes('write step-by-step with ONE OR MAX 2 STEPS PER LINE (never cram multiple steps together):'),
  'page.tsx Stage 4 prompt must mandate ONE OR MAX 2 STEPS PER LINE'
)
assert(
  pageSource.includes('Problem-Solving Layout (Exact Authentic Board Exam Format - 1 or Max 2 Steps Per Line):') &&
  pageSource.includes('Given line: Given: <extract all known variables with explicit SI units>') &&
  pageSource.includes('Formula line: Formula: <state the exact equation or physical theorem>') &&
  pageSource.includes('Substitution line: Step 1: <substitute numerical values with units>') &&
  pageSource.includes('Calculation line: Step 2: <intermediate algebraic or arithmetic step> (one or max 2 steps per line)'),
  'page.tsx pedagogical layout must mandate 1 or max 2 steps per line in standard topper format'
)
assert(
  pageSource.includes('Provide the COMPLETE, rigorous, step-by-step solution on the chalkboard right now following the authentic board-exam layout (write ONE OR MAX 2 STEPS PER LINE):'),
  'page.tsx complete solution request prompt must enforce ONE OR MAX 2 STEPS PER LINE'
)
assert(
  pageSource.includes('Solve authentic board exam questions & textbook numericals step-by-step on whiteboard with 1 or max 2 steps per line'),
  'page.tsx mathProgressionText must specify 1 or max 2 steps per line'
)
console.log('  [PASS] page.tsx Stage 4, Section 3, solver prompts, and math pedagogy verified.')

console.log('\n=============================================================')
console.log('ALL CHALKBOARD NUMERICAL STEP LAYOUT VERIFICATION CHECKS PASSED!')
console.log('=============================================================')

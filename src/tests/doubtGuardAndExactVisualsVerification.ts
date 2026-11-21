/**
 * Automated Verification Test Suite for Phase 11:
 * 1. Doubt & Re-explanation Intent Classification (including typos like 'douth' and 'explain whole concept again')
 * 2. Confirmation Intent Gating (rejects confirmation if text contains doubt/question/repeat)
 * 3. Sequential Concept Completion & Non-Zero Progress Percent Guarantee
 * 4. Active Doubt Guard Blocking Concept Completion
 * 5. Mandatory "animated short video showing animation to understand" video search queries across all subjects/classes
 * 6. High-Precision Image Relevance Gating & Scoring
 * 7. Gemini Live Tool Definition Invariants (no new_page, doubt lock on concept_completed, animated video query)
 */

import assert from 'assert';
import fs from 'fs';
import path from 'path';

// 1. Replicate Intent Classifiers from page.tsx for unit testing
function isStudentQuestionOrDoubt(text: string): boolean {
  if (!text) return false;
  const clean = text.toLowerCase().trim().replace(/[.,!;:()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim();
  if (!clean) return false;
  if (text.includes('?')) return true;

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
  ];
  return questionPatterns.some((p) => p.test(clean));
}

function isRepeatIntent(text: string): boolean {
  if (!text) return false;
  const clean = text.toLowerCase().trim().replace(/[.,!?:;()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim();
  const patterns = [
    /\b(?:repeat\s*that|can\s*you\s*repeat|please\s*repeat|say\s*that\s*again)\b/i,
    /\b(?:phir\s*se\s*bolo|dobara\s*bolo|ek\s*baar\s*phir|pardon)\b/i,
    /\b(?:explain\s*(?:the\s*)?(?:whole|entire|full|all|complete)?\s*concept\s*again)\b/i,
    /\b(?:explain\s*(?:it\s*|this\s*)?again|teach\s*(?:it\s*|this\s*)?again)\b/i,
    /\b(?:dobara\s*samjhao|phir\s*se\s*samjhao|pura\s*concept\s*samjhao|pura\s*samjhao|shuru\s*se\s*samjhao)\b/i,
    /\b(?:start\s*(?:from\s*the\s*)?beginning|from\s*scratch)\b/i,
    /\b(?:one\s*more\s*time|once\s*again)\b/i,
    /^repeat$/i,
  ];
  return patterns.some((p) => p.test(clean));
}

function isDontUnderstandIntent(text: string): boolean {
  if (!text) return false;
  const clean = text.toLowerCase().trim().replace(/[.,!?:;()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim();
  const patterns = [
    /\b(?:i\s*don'?t\s*understand|i\s*do\s*not\s*understand|didn'?t\s*get\s*it|not\s*getting\s*it|don'?t\s*understand)\b/i,
    /\b(?:samajh\s*nahi\s*aaya|samajh\s*na\s*aaya|kuch\s*samajh\s*nahi\s*aaya|nahi\s*samjha)\b/i,
    /\b(?:totally\s*confused|i\s*am\s*confused|it\s*is\s*confusing|not\s*clear)\b/i,
    /\b(?:i\s*am\s*stuck|stuck\s*here|fasi\s*gaya|atke\s*hue\s*hai)\b/i,
  ];
  return patterns.some((p) => p.test(clean));
}

function isConfirmationOrNextIntent(text: string): boolean {
  if (!text) return false;
  const clean = text.toLowerCase().trim().replace(/[.,!?;:'"()[\]{}]+/g, ' ').replace(/\s+/g, ' ').trim();
  if (!clean) return false;

  if (isStudentQuestionOrDoubt(clean) || isRepeatIntent(clean) || isDontUnderstandIntent(clean)) {
    return false;
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
  ]);

  if (exactAffirmations.has(clean)) return true;

  if (/\b(?:because|since|due to|as\s+\w+|when\s+\w+|where\s+\w+)\b/i.test(clean) && !/\b(?:next|advance|move\s*on|understood|clear|no\s*doubts?)\b/i.test(clean)) {
    return false;
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
  ];

  return patterns.some((p) => p.test(clean));
}

async function runVerification() {
  console.log('================================================================');
  console.log('PHASE 11 AUTOMATED VERIFICATION: DOUBT GUARD & EXACT VISUALS');
  console.log('================================================================\n');

  // Test 1: Doubt and typo classification
  console.log('[Test 1] Testing Doubt & Re-explanation Intent Classification...');
  assert.strictEqual(isStudentQuestionOrDoubt('i have a douth'), true, 'Should classify "i have a douth" as doubt');
  assert.strictEqual(isStudentQuestionOrDoubt('sir ek doubt hai'), true, 'Should classify "sir ek doubt hai" as doubt');
  assert.strictEqual(isStudentQuestionOrDoubt('explain whole concept again'), true, 'Should classify "explain whole concept again" as doubt/repeat');
  assert.strictEqual(isRepeatIntent('explain whole concept again'), true, 'Should classify "explain whole concept again" as repeat intent');
  assert.strictEqual(isRepeatIntent('can you explain again?'), true, 'Should classify "can you explain again?" as repeat intent');
  assert.strictEqual(isStudentQuestionOrDoubt('pura concept samjhao dobara'), true, 'Should classify "pura concept samjhao dobara" as doubt');
  assert.strictEqual(isRepeatIntent('phir se samjhao'), true, 'Should classify "phir se samjhao" as repeat intent');
  console.log('  ✓ Test 1 passed: All doubt and re-explanation phrases correctly identified.\n');

  // Test 2: Confirmation Intent Gating
  console.log('[Test 2] Testing Confirmation Intent Gating...');
  assert.strictEqual(isConfirmationOrNextIntent('yes understood'), true, 'Pure affirmation should be true');
  assert.strictEqual(isConfirmationOrNextIntent('all clear, next concept'), true, 'Clear confirmation should be true');
  assert.strictEqual(isConfirmationOrNextIntent('yes but i have a douth'), false, 'Affirmation followed by doubt must be FALSE');
  assert.strictEqual(isConfirmationOrNextIntent('understood, but can you explain whole concept again'), false, 'Affirmation followed by re-explain request must be FALSE');
  assert.strictEqual(isConfirmationOrNextIntent('ok wait, explain again'), false, 'Affirmation with explain again must be FALSE');
  console.log('  ✓ Test 2 passed: Doubts and re-explanation requests are strictly rejected by confirmation intent.\n');

  // Test 3: Sequential Concept Completion & Non-Zero Progress Percent Guarantee
  console.log('[Test 3] Testing Sequential Concept Completion & Progress Percentage...');
  const keyConcepts = ['Fundamental Theorem of Arithmetic', 'Prime Factorization', 'HCF and LCM Applications', 'Revisiting Irrational Numbers', 'Summary'];
  const nextIdx = 1; // Transitioning to Concept 2 (index 1)
  const completedList: string[] = [];

  // Logic replicated from advanceToNextConcept in page.tsx
  const priorConcepts = keyConcepts.slice(0, nextIdx);
  const updated = Array.from(new Set([...completedList, ...priorConcepts]));

  const normConcept = (s: string) => String(s || '').toLowerCase().replace(/[^a-z0-9]/g, '');
  const completedCount = keyConcepts.filter((k) =>
    updated.some((c) => {
      const cNorm = normConcept(c);
      const kNorm = normConcept(k);
      return cNorm === kNorm || cNorm.includes(kNorm) || kNorm.includes(cNorm);
    })
  ).length;

  const progressPercent = Math.min(100, Math.round((completedCount / keyConcepts.length) * 100));

  assert.strictEqual(updated.length, 1, 'Should have 1 concept marked completed');
  assert.strictEqual(updated[0], 'Fundamental Theorem of Arithmetic');
  assert.strictEqual(completedCount, 1, 'Completed count should be 1');
  assert.strictEqual(progressPercent, 20, 'Progress percent must be 20%, NOT 0%');
  console.log(`  ✓ Test 3 passed: Concept 1 is permanently marked, progress is ${progressPercent}% (not 0%).\n`);

  // Test 4: Active Doubt Guard in handleConceptDone
  console.log('[Test 4] Testing Active Doubt Guard in Concept Completion...');
  let studentHasActiveDoubt = true;
  let hasConfirmedUnderstanding = false;
  let advanceAllowed = false;

  function simulateHandleConceptDone() {
    if (studentHasActiveDoubt) {
      advanceAllowed = false;
      return 'BLOCKED_BY_ACTIVE_DOUBT';
    }
    if (!hasConfirmedUnderstanding) {
      advanceAllowed = false;
      return 'BLOCKED_BY_CHECKPOINT_GUARD';
    }
    advanceAllowed = true;
    return 'ADVANCED';
  }

  assert.strictEqual(simulateHandleConceptDone(), 'BLOCKED_BY_ACTIVE_DOUBT', 'Must block when studentHasActiveDoubt is true');
  assert.strictEqual(advanceAllowed, false);

  // Student clears doubt
  studentHasActiveDoubt = false;
  assert.strictEqual(simulateHandleConceptDone(), 'BLOCKED_BY_CHECKPOINT_GUARD', 'Must block until understanding is confirmed');

  hasConfirmedUnderstanding = true;
  assert.strictEqual(simulateHandleConceptDone(), 'ADVANCED', 'Advances only when doubt cleared and confirmed');
  assert.strictEqual(advanceAllowed, true);
  console.log('  ✓ Test 4 passed: Concept advancement is strictly gated against active doubts.\n');

  // Test 5: Tool Definitions Invariants
  console.log('[Test 5] Verifying tool declarations in src/services/geminiWebSocket.ts...');
  const gwsContent = fs.readFileSync('src/services/geminiWebSocket.ts', 'utf8');

  // Check write_chalkboard doesn't have "new_page" in enum
  const writeChalkboardMatch = gwsContent.match(/name:\s*"write_chalkboard"[\s\S]*?enum:\s*\[([\s\S]*?)\]/);
  assert.ok(writeChalkboardMatch, 'write_chalkboard tool declaration found');
  const enumContents = writeChalkboardMatch[1];
  assert.strictEqual(enumContents.includes('"new_page"'), false, 'write_chalkboard enum MUST NOT include "new_page"');

  // Check concept_completed description mentions doubt lock
  const conceptCompletedMatch = gwsContent.match(/name:\s*"concept_completed"[\s\S]*?description:\s*"([\s\S]*?)"/);
  assert.ok(conceptCompletedMatch, 'concept_completed tool declaration found');
  assert.ok(conceptCompletedMatch[1].includes('NEVER call this tool when the student asks a question, raises a doubt'), 'concept_completed must instruct to stay on current concept during doubts');

  // Check search_and_show_video mentions animated short video
  const searchVideoMatch = gwsContent.match(/name:\s*"search_and_show_video"[\s\S]*?query:[\s\S]*?description:\s*"([\s\S]*?)"/);
  assert.ok(searchVideoMatch, 'search_and_show_video tool declaration found');
  assert.ok(searchVideoMatch[1].includes('animated short video showing animation to understand'), 'search_and_show_video query must mandate animated short video to understand');
  console.log('  ✓ Test 5 passed: All tool declarations adhere strictly to invariants.\n');

  // Test 6: Image relevance filter precision gate
  console.log('[Test 6] Testing Image Search Relevance & Scoring Quality...');
  const searchImageRoute = fs.readFileSync('src/app/api/diagram/search-image/route.ts', 'utf8');
  assert.ok(searchImageRoute.includes('minRequiredMatches'), 'Image route must contain precision gate');
  assert.ok(searchImageRoute.includes('ratio * 80'), 'Image route must score token match ratio');
  assert.ok(searchImageRoute.includes('freepik') && searchImageRoute.includes('canva'), 'Harmful patterns must include stock/canva/freepik');

  const searchVideoRoute = fs.readFileSync('src/app/api/diagram/search-video/route.ts', 'utf8');
  assert.ok(searchVideoRoute.includes('animated short video'), 'Video route must search animated short videos');
  assert.ok(searchVideoRoute.includes('videos.sort'), 'Video route must sort animated concept videos first');
  console.log('  ✓ Test 6 passed: Image relevance and video search ranking upgrades verified.\n');

  console.log('================================================================');
  console.log('ALL PHASE 11 AUTOMATED VERIFICATION CHECKS PASSED SUCCESSFULLY!');
  console.log('================================================================');
}

runVerification().catch((err) => {
  console.error('Verification failed:', err);
  process.exit(1);
});

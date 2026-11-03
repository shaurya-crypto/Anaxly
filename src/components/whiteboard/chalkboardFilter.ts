// Botanical Chalkboard Concept & Redundancy Filter

export const normalizeTitle = (t: string): string =>
  (t || '')
    .replace(/^focus:\s*/i, '')
    .replace(/^concept\s*\d*:\s*/i, '')
    .replace(/[\(\)\[\]\{\}\"\']/g, '')
    .replace(/\s+/g, ' ')
    .trim()
    .toLowerCase()

export const isRedundantConceptOrMasteredText = (
  text: string,
  moduleTitle = '',
  keyConcepts: string[] = []
): boolean => {
  if (!text) return true
  const trimmed = text.trim()

  // 1. Invariant: Never write Mastered or Concept Done on chalkboard
  if (/^(concept\s*\d*\s*)?(done|mastered|completed)\b/i.test(trimmed)) return true
  if (/\b(mastered|completed\s+successfully)\b/i.test(trimmed)) return true

  // 2. Invariant: Never write repeated Concept Title / Focus / Key Concept alone
  if (/^(key\s+concepts?|focus)\b[:\-]?$/i.test(trimmed)) return true
  if (/^concept\s*\d+\b[:\-]?$/i.test(trimmed)) return true
  
  const conceptHeaderMatch = trimmed.match(/^(?:key\s+concepts?|concept\s*\d*|focus|topic)\s*[:\-]\s*(.*)$/i)
  if (conceptHeaderMatch) {
    const remainder = conceptHeaderMatch[1]?.trim()
    // If empty after header prefix, drop
    if (!remainder) return true
    // If remainder is literally just the title of the module or a key concept (< 50 chars), drop
    if (remainder.length < 50) {
      const normRemainder = normalizeTitle(remainder)
      if (moduleTitle) {
        const normMod = normalizeTitle(moduleTitle)
        if (normRemainder === normMod || normMod.includes(normRemainder) || normRemainder.includes(normMod)) {
          return true
        }
      }
      if (keyConcepts && keyConcepts.length > 0) {
        const isMatch = keyConcepts.some((c) => {
          const normC = normalizeTitle(c)
          return normRemainder === normC || normC.includes(normRemainder) || normRemainder.includes(normC)
        })
        if (isMatch) return true
      }
      // Also if remainder is short without sentence punctuation or equation symbols, it's just a topic heading
      if (remainder.split(/\s+/).length <= 4 && !/[.!?=><+\-*\/]/.test(remainder)) {
        return true
      }
    }
    // If remainder contains real explanatory content, DO NOT drop
  }

  // 3. Exact match with any key concept or module title (short text only)
  if (trimmed.length < 50) {
    const norm = normalizeTitle(trimmed)
    if (moduleTitle && norm === normalizeTitle(moduleTitle)) return true
    if (keyConcepts && keyConcepts.some((c) => normalizeTitle(c) === norm)) return true
  }

  return false
}

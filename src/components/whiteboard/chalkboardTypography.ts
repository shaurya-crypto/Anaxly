/**
 * chalkboardTypography.ts - Master Scientific and Mathematical Typography Engine for Live Chalkboard
 * Eliminates raw programming markers (*, **, //, ^) and formats clean Unicode mathematics,
 * Greek symbols, vectors, exponents, subscripts, and scientific units for both chalkboard notes
 * and live subtitle streaming.
 */

const SUPERSCRIPT_MAP: Record<string, string> = {
  '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
  '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
  '+': '⁺', '-': '⁻', '=': '⁼', '(': '⁽', ')': '⁾',
  'n': 'ⁿ', 'i': 'ⁱ', 't': 'ᵗ', 'x': 'ˣ', 'y': 'ʸ', 'k': 'ᵏ',
  'm': 'ᵐ', 'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ',
  'r': 'ʳ', 's': 'ˢ', 'v': 'ᵛ', 'o': 'ᵒ', 'p': 'ᵖ', 'T': 'ᵀ',
}

const SUBSCRIPT_MAP: Record<string, string> = {
  '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
  '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
  '+': '₊', '-': '₋', '=': '₌', '(': '₍', ')': '₎',
  'a': 'ₐ', 'e': 'ₑ', 'h': 'ₕ', 'i': 'ᵢ', 'j': 'ⱼ',
  'k': 'ₖ', 'l': 'ₗ', 'm': 'ₘ', 'n': 'ₙ', 'o': 'ₒ',
  'p': 'ₚ', 'r': 'ᵣ', 's': 'ₛ', 't': 'ₜ', 'u': 'ᵤ',
  'v': 'ᵥ', 'x': 'ₓ', 'y': 'ᵧ', 'c': '꜀',
}

export function toSuperscript(str: string): string {
  return str.split('').map((ch) => SUPERSCRIPT_MAP[ch] || ch).join('')
}

export function toSubscript(str: string): string {
  return str.split('').map((ch) => SUBSCRIPT_MAP[ch] || ch).join('')
}

/**
 * Transforms raw text from AI or textbook into clean, publication-grade chalkboard typography.
 * Strips raw markdown asterisks, converts ^ exponents to Unicode powers, cleans up division/multiplication,
 * renders vectors with combining arrows, and translates LaTeX Greek symbols into clean Unicode glyphs.
 */
export function cleanChalkboardTypography(text: string): string {
  if (!text || typeof text !== 'string') return text || ''
  let out = text

  // 1. Preserve URLs so their slashes, underscores, and characters are never altered
  const urls: string[] = []
  out = out.replace(/(https?:\/\/[^\s\)]+)/gi, (match) => {
    urls.push(match)
    return `###URLHOLDER${urls.length - 1}###`
  })

  // 2. Remove markdown code backticks: `F = ma` -> F = ma
  out = out.replace(/`([^`]+)`/g, '$1')

  // 3. LaTeX Greek and mathematical replacements
  const latexReplacements: [RegExp, string][] = [
    [/\\theta/gi, 'θ'],
    [/\\alpha/gi, 'α'],
    [/\\beta/gi, 'β'],
    [/\\gamma/gi, 'γ'],
    [/\\Delta/g, 'Δ'],
    [/\\delta/g, 'δ'],
    [/\\epsilon/gi, 'ε'],
    [/\\eta/gi, 'η'],
    [/\\lambda/gi, 'λ'],
    [/\\Lambda/g, 'Λ'],
    [/\\mu/gi, 'μ'],
    [/\\nu/gi, 'ν'],
    [/\\pi/gi, 'π'],
    [/\\Pi/g, 'Π'],
    [/\\rho/gi, 'ρ'],
    [/\\sigma/gi, 'σ'],
    [/\\Sigma/g, 'Σ'],
    [/\\tau/gi, 'τ'],
    [/\\phi/gi, 'φ'],
    [/\\Phi/g, 'Φ'],
    [/\\omega/gi, 'ω'],
    [/\\Omega/g, 'Ω'],
    [/\\int/gi, '∫'],
    [/\\iint/gi, '∬'],
    [/\\oint/gi, '∮'],
    [/\\sum/gi, '∑'],
    [/\\prod/gi, '∏'],
    [/\\angle/gi, '∠'],
    [/\\perp/gi, '⊥'],
    [/\\parallel/gi, '∥'],
    [/\\degree|\\circ/gi, '°'],
    [/\\infty/gi, '∞'],
    [/\\propto/gi, '∝'],
    [/\\partial/gi, '∂'],
    [/\\nabla/gi, '∇'],
    [/\\approx/gi, '≈'],
    [/\\le(?!a)|\\leq/gi, '≤'],
    [/\\ge(?!a)|\\geq/gi, '≥'],
    [/\\ne(?!w)|\\neq/gi, '≠'],
    [/\\pm/gi, '±'],
    [/\\mp/gi, '∓'],
    [/\\times/gi, '×'],
    [/\\cdot/gi, '·'],
    [/\\div/gi, '÷'],
    [/\\hat\{i\}|\\hat\s+i/gi, 'î'],
    [/\\hat\{j\}|\\hat\s+j/gi, 'ĵ'],
    [/\\hat\{k\}|\\hat\s+k/gi, 'k̂'],
    [/\\vec\{([A-Za-z])\}/g, '$1\u20D7'],
    [/\\vec\s+([A-Za-z])/g, '$1\u20D7'],
    [/\\sqrt\{([^}]+)\}/g, '√($1)'],
    [/\\sqrt\s*([0-9a-zA-Z]+)/g, '√$1'],
    [/sqrt\(([^)]+)\)/gi, '√($1)'],
    [/\\frac\{([^}]+)\}\{([^}]+)\}/g, '($1)/($2)'],
  ]

  for (const [regex, rep] of latexReplacements) {
    out = out.replace(regex, rep)
  }

  // 4. Bullet lists at the start of a line or paragraph: * Item -> • Item
  out = out.replace(/(^|\n)\s*\*\s+/g, '$1• ')

  // 5. Degree syntax: ^o, ^\circ, ^deg -> °
  out = out.replace(/\^(?:o|deg|\circ)/gi, '°')

  // 6. Exponent / Power conversions:
  // Parenthesized exponents: ^( -11 ) or ^(2)
  out = out.replace(/\^\(([\+\-]?[0-9a-zA-Z\+\-\*\/]+)\)/g, (_match, p1) => toSuperscript(p1))

  // Signed/unsigned numeric or variable exponents: ^2, ^-11, ^3, ^n, ^-1, ^-2
  out = out.replace(/\^([\+\-]?[0-9]+|[a-zA-Z])(?=[^0-9a-zA-Z]|$)/g, (_match, p1) => toSuperscript(p1))

  // 7. Subscript conversions:
  // e.g. v_0, m_1, m_2, r_1, F_{net}, a_c, lambda_0
  out = out.replace(/_\{([0-9a-zA-Z\+\-]+)\}/g, (_match, p1) => toSubscript(p1))
  out = out.replace(/(?<=[a-zA-Z\u20D7α-ωΑ-Ω])_([0-9a-zA-Z]{1,3})(?=[^0-9a-zA-Z]|$)/g, (_match, p1) => {
    return toSubscript(p1)
  })

  // 8. Double slashes: // -> ÷ (with clean spacing)
  out = out.replace(/\s*\/\/\s*/g, ' ÷ ')

  // 9. Markdown Bold / Italic removal: ***bold italic*** -> bold italic, **bold** -> bold, *italic* -> italic
  out = out.replace(/\*\*\*([^*]+)\*\*\*/g, '$1')
  out = out.replace(/\*\*([^*]+)\*\*/g, '$1')

  // 10. Asterisks / Multiplications:
  // Number * Number -> Number × Number (e.g. 5 * 10 -> 5 × 10, 6.67 * 10⁻¹¹ -> 6.67 × 10⁻¹¹)
  out = out.replace(/([0-9\.\)\]])\s*\*\s*([0-9\(\[\+\-])/g, '$1 × $2')
  // Variable * Variable -> Variable · Variable (e.g. m * a -> m · a, u * t -> u · t)
  out = out.replace(/([a-zA-Z\u20D7α-ωΑ-Ω⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉])\s*\*\s*([a-zA-Z\u20D7α-ωΑ-Ω⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉])/g, '$1 · $2')
  // Number or ) * Variable (e.g. 2 * a * s -> 2 · a · s, (½)*a -> (½) · a)
  out = out.replace(/([0-9\)])\s*\*\s*([a-zA-Z\u20D7α-ωΑ-Ω])/g, '$1 · $2')
  out = out.replace(/([a-zA-Z\u20D7α-ωΑ-Ω])\s*\*\s*([0-9\()])/g, '$1 · $2')
  // Isolated * with spaces: " * " -> " × "
  out = out.replace(/\s+\*\s+/g, ' × ')
  // Standalone asterisks remaining from markdown italics
  out = out.replace(/(^|\s)\*([a-zA-Z0-9\s]+)\*(\s|$)/g, '$1$2$3')
  // Guarantee zero stray raw asterisks on chalkboard
  out = out.replace(/\*/g, '·')

  // 11. Common math symbols & comparisons:
  out = out.replace(/<=\s*/g, '≤ ')
  out = out.replace(/>=\s*/g, '≥ ')
  out = out.replace(/!=\s*/g, '≠ ')
  out = out.replace(/~=\s*/g, '≈ ')
  out = out.replace(/\+\/\-/g, '±')
  out = out.replace(/->\s*/g, '→ ')
  out = out.replace(/=>\s*/g, '⇒ ')
  out = out.replace(/<->\s*/g, '↔ ')
  out = out.replace(/<=>/g, '⇌ ')

  // 12. Standalone common fractions: (1/2) -> ½, 1/2 -> ½, 1/4 -> ¼, 3/4 -> ¾, 1/3 -> ⅓, 2/3 -> ⅔
  out = out.replace(/(^|[\s\(\+\-\=])1\/2(?=[\s\)\+\-\*·×]|$)/g, '$1½')
  out = out.replace(/(^|[\s\(\+\-\=])1\/4(?=[\s\)\+\-\*·×]|$)/g, '$1¼')
  out = out.replace(/(^|[\s\(\+\-\=])3\/4(?=[\s\)\+\-\*·×]|$)/g, '$1¾')
  out = out.replace(/(^|[\s\(\+\-\=])1\/3(?=[\s\)\+\-\*·×]|$)/g, '$1⅓')
  out = out.replace(/(^|[\s\(\+\-\=])2\/3(?=[\s\)\+\-\*·×]|$)/g, '$1⅔')

  // Guarantee zero stray raw carets on chalkboard
  out = out.replace(/\^([0-9a-zA-Z]+)/g, (_match, p1) => toSuperscript(p1))
  out = out.replace(/\^/g, '')

  // 13. Restore URLs
  urls.forEach((url, i) => {
    out = out.split(`###URLHOLDER${i}###`).join(url)
  })

  return out
}

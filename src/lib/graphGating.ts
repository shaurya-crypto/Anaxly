/**
 * Dynamic Graph Gating, Parsing & Payload Validation for Mathematics and Physics.
 *
 * User Mandates:
 * 1. "dont be fixed let the tutor call itself without any fixed thing" — do NOT restrict graph
 *    opening with a rigid keyword list; allow the AI tutor to dynamically invoke graphing whenever needed.
 * 2. "should also work with physics" — graphing capabilities and tool calls must support Physics
 *    as well as Mathematics whenever a graph is helpful.
 * 3. Under NO circumstances should Cartesian coordinate graphs open for non-STEM or non-mathematical
 *    topics (such as biology cell walls, histology, chemistry bonding, literature, history)
 *    where vector SVG diagrams or flowcharts are the proper visual medium.
 * 4. Strictly reject meaningless default graphs (e.g. y = x line passing through origin with no
 *    diagram, points, segments, or mathematical context).
 * 5. Robust multi-format parsing for formulas, bounded segments with stopping points, and key points
 *    across JSON objects, tuples, string arrays, and coordinate representations.
 */

export interface GraphFormulaItem {
  formula: string
  color?: string
  label?: string
  domain?: [number, number]
}

export interface GraphSegmentItem {
  start: [number, number]
  end: [number, number]
  label?: string
  color?: string
  dashed?: boolean
}

export interface GraphPointItem {
  x: number
  y: number
  label?: string
  color?: string
  callout?: string
}

export interface GraphPayload {
  formula?: string | string[] | GraphFormulaItem[]
  formulas?: Array<string | GraphFormulaItem>
  segments?: Array<GraphSegmentItem | string | [number, number][] | any>
  points?: Array<[number, number] | GraphPointItem | string> | string
  domain?: [number, number]
  range?: [number, number]
  title?: string
  callout?: string
}

/**
 * Robustly parses key coordinate points from any format:
 * - Array of objects: { x, y, label, color, callout }
 * - Array of coordinate tuples: [x, y]
 * - Array of JSON strings: '{"x": 0, "y": 0, "label": "Origin"}'
 * - Array of coordinate strings: '(0, 0)', '(2, 4)'
 * - Single JSON string: '[{"x": 0, "y": 0}, {"x": 2, "y": 4}]'
 * - Single coordinate tuple string: "(0, -4), (2, 0), (-2, 0)"
 */
export function parseGraphPoints(raw: any): GraphPointItem[] {
  if (!raw) return []
  const result: GraphPointItem[] = []

  const parseSinglePoint = (p: any) => {
    if (!p) return
    if (typeof p === 'string') {
      const trimmed = p.trim()
      if (trimmed.startsWith('{')) {
        try {
          const parsed = JSON.parse(trimmed)
          if (parsed && typeof parsed === 'object') parseSinglePoint(parsed)
          return
        } catch {}
      }
      const tupleMatch = trimmed.match(/\(\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\)/)
      if (tupleMatch) {
        const x = parseFloat(tupleMatch[1])
        const y = parseFloat(tupleMatch[2])
        if (!isNaN(x) && !isNaN(y)) {
          result.push({ x, y })
        }
      }
      return
    }

    if (Array.isArray(p) && p.length >= 2) {
      const x = Number(p[0])
      const y = Number(p[1])
      if (!isNaN(x) && !isNaN(y)) {
        result.push({ x, y })
      }
      return
    }

    if (typeof p === 'object' && 'x' in p && 'y' in p) {
      const x = Number(p.x)
      const y = Number(p.y)
      if (!isNaN(x) && !isNaN(y)) {
        result.push({
          x,
          y,
          label: typeof p.label === 'string' ? p.label : undefined,
          color: typeof p.color === 'string' ? p.color : undefined,
          callout: typeof p.callout === 'string' ? p.callout : undefined,
        })
      }
    }
  }

  if (Array.isArray(raw)) {
    raw.forEach(parseSinglePoint)
    return result
  }

  if (typeof raw === 'string') {
    const trimmed = raw.trim()
    if (trimmed.startsWith('[')) {
      try {
        const parsed = JSON.parse(trimmed)
        if (Array.isArray(parsed)) {
          parsed.forEach(parseSinglePoint)
          return result
        }
      } catch {}
    }

    // Fallback coordinate tuple regex across entire string
    const matches = trimmed.matchAll(/\(\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\)/g)
    for (const m of matches) {
      const px = parseFloat(m[1])
      const py = parseFloat(m[2])
      if (!isNaN(px) && !isNaN(py)) {
        result.push({ x: px, y: py })
      }
    }
    return result
  }

  if (typeof raw === 'object') {
    parseSinglePoint(raw)
  }

  return result
}

/**
 * Robustly parses line segments with start & end stopping points from any format:
 * - Array of objects: { start: [x,y] | {x,y}, end: [x,y] | {x,y}, label, color, dashed }
 * - Array of JSON strings: '{"start": [0,0], "end": [4,8], "label": "OA"}'
 * - Array of point tuples: [[x1, y1], [x2, y2]]
 * - Array of transition strings: '(0, 0) -> (4, 8)' or '[0,0] to [4,8]'
 * - Single JSON string of array of segments
 */
export function parseGraphSegments(raw: any): GraphSegmentItem[] {
  if (!raw) return []
  const result: GraphSegmentItem[] = []

  const extractCoords = (pt: any): [number, number] | null => {
    if (!pt) return null
    if (Array.isArray(pt) && pt.length >= 2) {
      const x = Number(pt[0])
      const y = Number(pt[1])
      return !isNaN(x) && !isNaN(y) ? [x, y] : null
    }
    if (typeof pt === 'object' && 'x' in pt && 'y' in pt) {
      const x = Number(pt.x)
      const y = Number(pt.y)
      return !isNaN(x) && !isNaN(y) ? [x, y] : null
    }
    if (typeof pt === 'string') {
      const m = pt.match(/\(?\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\)?/)
      if (m) {
        const x = parseFloat(m[1])
        const y = parseFloat(m[2])
        return !isNaN(x) && !isNaN(y) ? [x, y] : null
      }
    }
    return null
  }

  const parseSingleSegment = (s: any) => {
    if (!s) return

    // 1. String segment item
    if (typeof s === 'string') {
      const trimmed = s.trim()
      if (trimmed.startsWith('{')) {
        try {
          const parsed = JSON.parse(trimmed)
          if (parsed && typeof parsed === 'object') parseSingleSegment(parsed)
          return
        } catch {}
      }

      // Check transition format like "(0, 0) -> (4, 8)" or "[0, 0] to [4, 8]"
      const matches = Array.from(trimmed.matchAll(/(?:\(|\[)\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*(?:\)|\])/g))
      if (matches.length >= 2) {
        const x1 = parseFloat(matches[0][1])
        const y1 = parseFloat(matches[0][2])
        const x2 = parseFloat(matches[1][1])
        const y2 = parseFloat(matches[1][2])
        if (!isNaN(x1) && !isNaN(y1) && !isNaN(x2) && !isNaN(y2)) {
          result.push({
            start: [x1, y1],
            end: [x2, y2],
          })
          return
        }
      }
      return
    }

    // 2. Object with start and end
    if (typeof s === 'object' && s !== null && ('start' in s || 'end' in s)) {
      const start = extractCoords(s.start)
      const end = extractCoords(s.end)
      if (start && end) {
        result.push({
          start,
          end,
          label: typeof s.label === 'string' ? s.label : undefined,
          color: typeof s.color === 'string' ? s.color : undefined,
          dashed: Boolean(s.dashed),
        })
        return
      }
    }

    // 3. Raw tuple of points [[x1, y1], [x2, y2]]
    if (Array.isArray(s) && s.length >= 2) {
      const start = extractCoords(s[0])
      const end = extractCoords(s[1])
      if (start && end) {
        result.push({
          start,
          end,
        })
      }
    }
  }

  if (Array.isArray(raw)) {
    raw.forEach(parseSingleSegment)
    return result
  }

  if (typeof raw === 'string') {
    const trimmed = raw.trim()
    if (trimmed.startsWith('[')) {
      try {
        const parsed = JSON.parse(trimmed)
        if (Array.isArray(parsed)) {
          parsed.forEach(parseSingleSegment)
          return result
        }
      } catch {}
    }

    // Split on pipe or newline if multiple segments represented as strings
    if (trimmed.includes('|') || trimmed.includes('\n') || trimmed.includes(';')) {
      const parts = trimmed.split(/[|\n;]+/).map((p) => p.trim()).filter(Boolean)
      parts.forEach(parseSingleSegment)
      return result
    }

    parseSingleSegment(trimmed)
    return result
  }

  if (typeof raw === 'object') {
    parseSingleSegment(raw)
  }

  return result
}

/**
 * Robustly parses mathematical formulas:
 * - Array of strings: ['2x + 1', '-x + 4']
 * - Array of objects: [{ formula: '2x + 1', label: 'L1', domain: [0, 5] }]
 * - Array of JSON strings: '{"formula": "2x + 1"}'
 * - Multi-formula string: "2x + 1, -x + 4" or "y = 2x + 1; y = -x + 4"
 */
export function parseGraphFormulas(formula?: any, formulas?: any): GraphFormulaItem[] {
  const result: GraphFormulaItem[] = []

  const addFormulaItem = (item: any) => {
    if (!item) return
    if (typeof item === 'string') {
      const trimmed = item.trim()
      if (!trimmed) return
      if (trimmed.startsWith('{')) {
        try {
          const parsed = JSON.parse(trimmed)
          if (parsed && typeof parsed === 'object') {
            addFormulaItem(parsed)
            return
          }
        } catch {}
      }
      result.push({ formula: trimmed })
      return
    }

    if (typeof item === 'object' && item !== null && item.formula) {
      const fStr = typeof item.formula === 'string' ? item.formula.trim() : ''
      if (fStr) {
        let domain: [number, number] | undefined = undefined
        if (Array.isArray(item.domain) && item.domain.length >= 2) {
          const d0 = Number(item.domain[0])
          const d1 = Number(item.domain[1])
          if (!isNaN(d0) && !isNaN(d1)) domain = [d0, d1]
        }
        result.push({
          formula: fStr,
          color: typeof item.color === 'string' ? item.color : undefined,
          label: typeof item.label === 'string' ? item.label : undefined,
          domain,
        })
      }
    }
  }

  if (Array.isArray(formulas)) {
    formulas.forEach(addFormulaItem)
  }

  if (Array.isArray(formula)) {
    formula.forEach(addFormulaItem)
  } else if (typeof formula === 'string' && formula.trim()) {
    let parts: string[] = []
    if (formula.includes(';') || formula.includes('|') || formula.includes('\n')) {
      parts = formula.split(/[;|\n]+/).map((s) => s.trim()).filter(Boolean)
    } else if (formula.includes('and') || formula.includes('&')) {
      parts = formula.split(/\s*(?:and|&)\s*/i).map((s) => s.trim()).filter(Boolean)
    } else if (/y\s*=.*y\s*=/i.test(formula)) {
      parts = formula.split(/,\s*(?=y\s*=)/i).map((s) => s.trim()).filter(Boolean)
    } else if (formula.includes(',') && !formula.includes('(')) {
      parts = formula.split(',').map((s) => s.trim()).filter(Boolean)
    } else {
      parts = [formula.trim()]
    }

    parts.forEach(addFormulaItem)
  }

  return result
}

/**
 * Validates whether a graph payload has substantive mathematical purpose.
 * Rejects empty graphs, placeholder 'x' or 'linear' formulas with no segments or points,
 * or payloads with neither valid formulas nor segments.
 */
export function isValidGraphPayload(payload?: GraphPayload | null): boolean {
  if (!payload || typeof payload !== 'object') return false

  // 1. If segments are present and non-empty with valid start/end coordinates, it's valid
  const parsedSegments = parseGraphSegments(payload.segments)
  if (parsedSegments.length > 0) {
    return true
  }

  // 2. Check points
  const parsedPoints = parseGraphPoints(payload.points)
  const hasPoints = parsedPoints.length > 0

  // 3. Collect all formulas
  const parsedFormulas = parseGraphFormulas(payload.formula, payload.formulas)
  const cleanFormulas = parsedFormulas.map((f) => f.formula.trim()).filter((f) => f.length > 0)

  // If no formulas and no segments and no points, reject
  if (cleanFormulas.length === 0 && !hasPoints) {
    return false
  }

  // Check if the only formula is a meaningless default line y = x or 'linear'
  const isMeaninglessLine = (f: string) => {
    const normalized = f.toLowerCase().replace(/\s+/g, '').replace(/^(?:y|f\(x\))=/, '')
    return normalized === 'x' || normalized === 'linear' || normalized === '+x' || normalized === '1*x' || normalized === 'y=x'
  }

  const allAreMeaningless = cleanFormulas.length > 0 && cleanFormulas.every(isMeaninglessLine)

  // If the formulas are solely meaningless y = x lines AND there are no points or segments, reject!
  if (allAreMeaningless && !hasPoints) {
    return false
  }

  // If there are points, even with a line through origin or no formula, it's a valid coordinate plot
  if (hasPoints) {
    return true
  }

  return cleanFormulas.length > 0
}

export function isLegitimateGraphTopic(topic: string, subject: string): boolean {
  const s = (subject || '').toLowerCase().trim();
  const t = (topic || '').toLowerCase().trim();

  // 1. Non-mathematical and non-physics subjects are unconditionally barred from graphing
  const nonStemSubjects = [
    'bio', 'life', 'botan', 'zool', 'histol', 'anatom',
    'cell', 'environ', 'hist', 'civic', 'geog', 'politi',
    'social', 'eng', 'lit', 'lang', 'hindi', 'french', 'german', 'chem'
  ];
  if (nonStemSubjects.some((sub) => s.includes(sub))) {
    return false;
  }

  // 2. Disallow topics containing purely non-mathematical, biological, or chemical keywords
  const strictlyNonMathKeywords = [
    'cell', 'wall', 'tissue', 'histolog', 'organ', 'plant', 'animal',
    'cellulose', 'pectin', 'lignin', 'photosynth', 'digest', 'xylem',
    'phloem', 'parenchyma', 'collenchyma', 'sclerenchyma', 'epithel',
    'covalent', 'ionic', 'bonding', 'reaction', 'periodic table',
    'valency', 'compound', 'acid', 'base', 'salt', 'metal', 'nonmetal',
    'respiration', 'circulat', 'neuron', 'nephron', 'dna', 'rna',
    'chromosome', 'mitosis', 'meiosis', 'endocrine', 'hormone',
    'ecosystem', 'trophic', 'atom', 'molecule', 'redox', 'electrolysis'
  ];
  if (strictlyNonMathKeywords.some((kw) => t.includes(kw))) {
    return false;
  }

  // 3. Geometric diagram topics belong to SVG diagram / geometry tool, not Cartesian coordinate graph
  const geometricDiagramKeywords = [
    'triangle', 'circle', 'cylinder', 'cone', 'sphere', 'cube', 'polygon',
    'cuboid', 'geometry', 'angle', 'ray', 'optics', 'lens', 'mirror',
    'circuit', 'resistor', 'apparatus'
  ];
  if (geometricDiagramKeywords.some((kw) => t.includes(kw)) && !t.includes('coordinate') && !t.includes('graph')) {
    return false;
  }

  // 4. Subject must be Mathematics or Physics / Quantitative Science
  const isMathSubject = s.includes('math') || s.includes('algebra') || s.includes('calculus') || s.includes('geometry') || s.includes('stat') || s.includes('arithmetic');
  const isPhysicsSubject = s.includes('physic') || s.includes('science') || s.includes('mechanic');
  if (!isMathSubject && !isPhysicsSubject) {
    return false;
  }

  // Allow dynamic graph calls for both Mathematics and Physics topics without rigid keyword allowlists
  return true;
}

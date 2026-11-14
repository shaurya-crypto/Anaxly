/**
 * Strict Purpose-Driven Graph Gating.
 * Invariant: Mafs interactive Cartesian graphs MUST ONLY open when the topic actually
 * requires graphing a mathematical or kinematic function/curve (e.g. quadratic roots,
 * calculus derivatives, kinematics v-t or s-t curves) and with actual mathematical work.
 * Under NO circumstances should graphs trigger for non-mathematical topics (such as biology,
 * histology, chemical bonding, tissue structures) where vector SVG diagrams or flowcharts
 * are the proper visual medium.
 */
export function isLegitimateGraphTopic(topic: string, subject: string): boolean {
  const s = (subject || '').toLowerCase().trim()
  const t = (topic || '').toLowerCase().trim()

  // 1. Non-mathematical subjects are unconditionally barred from graphing
  const nonMathSubjects = [
    'bio', 'life', 'botan', 'zool', 'histol', 'anatom',
    'cell', 'environ', 'hist', 'civic', 'geog', 'politi',
    'social', 'eng', 'lit', 'lang', 'hindi', 'french', 'german', 'chem'
  ]
  if (nonMathSubjects.some((sub) => s.includes(sub))) {
    return false
  }

  // 2. Disallow topics containing non-mathematical or biological/chemical keywords regardless of subject
  const strictlyNonMathKeywords = [
    'cell', 'wall', 'tissue', 'histolog', 'organ', 'plant', 'animal',
    'cellulose', 'pectin', 'lignin', 'photosynth', 'digest', 'xylem',
    'phloem', 'parenchyma', 'collenchyma', 'sclerenchyma', 'epithel',
    'covalent', 'ionic', 'bonding', 'reaction', 'periodic table',
    'valency', 'compound', 'acid', 'base', 'salt', 'metal', 'nonmetal',
    'respiration', 'circulat', 'neuron', 'nephron', 'dna', 'rna',
    'chromosome', 'mitosis', 'meiosis', 'endocrine', 'hormone',
    'ecosystem', 'trophic', 'atom', 'molecule', 'redox', 'electrolysis'
  ]
  if (strictlyNonMathKeywords.some((kw) => t.includes(kw))) {
    return false
  }

  // 3. Subject must be Mathematics or Physics / Mechanics
  const isMathSubject = s.includes('math') || s.includes('algebra') || s.includes('calculus') || s.includes('geometry') || s.includes('stat') || s.includes('arithmetic')
  const isPhysicsSubject = s.includes('physic') || s.includes('science') || s.includes('mechanic')
  if (!isMathSubject && !isPhysicsSubject) {
    return false
  }

  // If the subject is Mathematics (and passed non-math keyword check), all genuine mathematical concepts/curves are legitimate
  if (isMathSubject) {
    return true
  }

  // 4. Positive verification for Physics / Science: Must be genuine mathematical curve or kinematics
  const validMathGraphPatterns = [
    /quadrat/i,
    /parabola/i,
    /polynomial/i,
    /calculus/i,
    /derivative/i,
    /integral/i,
    /tangent\s+curve/i,
    /trigonomet/i,
    /sine\s+(?:curve|wave|graph)/i,
    /cosine\s+(?:curve|wave|graph)/i,
    /linear\s+(?:equation|function|graph)/i,
    /coordinate\s+geometry/i,
    /cartesian/i,
    /kinematic/i,
    /velocity[\s\-]time/i,
    /displacement[\s\-]time/i,
    /distance[\s\-]time/i,
    /acceleration[\s\-]time/i,
    /speed[\s\-]time/i,
    /position[\s\-]time/i,
    /\bv\-t\b/i,
    /\bs\-t\b/i,
    /\ba\-t\b/i,
    /function\s+plot/i,
    /roots\s+of/i,
    /ohm['’]?s\s+law/i,
    /v[\s\-]i\s+(?:graph|curve|characteristic)/i,
    /straight\s+line/i,
    /slope/i,
    /y\s*=\s*/i,
    /f\(x\)/i,
    /\bx\^2\b/i,
    /\bsin\(/i,
    /\bcos\(/i,
    /\btan\(/i,
  ]

  return validMathGraphPatterns.some((pattern) => pattern.test(t))
}

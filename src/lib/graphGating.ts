/**
 * Dynamic Graph Gating for Mathematics and Physics.
 *
 * User Mandates:
 * 1. "dont be fixed let the tutor call itself without any fixed thing" — do NOT restrict graph
 *    opening with a rigid keyword list; allow the AI tutor to dynamically invoke graphing whenever needed.
 * 2. "should also work with physics" — graphing capabilities and tool calls must support Physics
 *    as well as Mathematics whenever a graph is helpful.
 * 3. Under NO circumstances should Cartesian coordinate graphs open for non-STEM or non-mathematical
 *    topics (such as biology cell walls, histology, chemistry bonding, literature, history)
 *    where vector SVG diagrams or flowcharts are the proper visual medium.
 */
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

  // 3. Subject must be Mathematics or Physics / Quantitative Science
  const isMathSubject = s.includes('math') || s.includes('algebra') || s.includes('calculus') || s.includes('geometry') || s.includes('stat') || s.includes('arithmetic');
  const isPhysicsSubject = s.includes('physic') || s.includes('science') || s.includes('mechanic');
  if (!isMathSubject && !isPhysicsSubject) {
    return false;
  }

  // Allow dynamic graph calls for both Mathematics and Physics topics without rigid keyword allowlists
  return true;
}

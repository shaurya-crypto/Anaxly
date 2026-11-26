-- ==============================================================================
-- Phase 4: Hybrid Textbook RAG (pgvector + FTS) & Prerequisite Knowledge Graph
-- Classes 9-12 (CBSE, ICSE, IB) — Mathematics, Science, Physics, Chemistry, Biology
-- ==============================================================================

CREATE EXTENSION IF NOT EXISTS vector;

-- 1. Chunked Textbook Repository (Dense pgvector + Sparse FTS)
CREATE TABLE IF NOT EXISTS public.book_chunks (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  class_level integer NOT NULL CHECK (class_level BETWEEN 9 AND 12),
  subject text NOT NULL,
  chapter_number integer NOT NULL CHECK (chapter_number >= 1),
  book_code text NOT NULL DEFAULT '',
  section_title text NOT NULL DEFAULT '',
  chunk_type text NOT NULL CHECK (
    chunk_type IN ('intuition', 'theorem', 'proof', 'example', 'exercise', 'solution', 'summary')
  ),
  page_number integer,
  content text NOT NULL,
  content_hash text NOT NULL,
  tsv tsvector GENERATED ALWAYS AS (
    to_tsvector('english', coalesce(section_title, '') || ' ' || content)
  ) STORED,
  embedding vector(768),
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_book_chunks_content_hash
  ON public.book_chunks (content_hash);

CREATE INDEX IF NOT EXISTS idx_book_chunks_scope
  ON public.book_chunks (class_level, lower(subject), chapter_number, chunk_type);

CREATE INDEX IF NOT EXISTS idx_book_chunks_tsv_gin
  ON public.book_chunks USING gin (tsv);

CREATE INDEX IF NOT EXISTS idx_book_chunks_embedding_hnsw
  ON public.book_chunks USING hnsw (embedding vector_cosine_ops)
  WITH (m = 16, ef_construction = 64);

-- 2. Concept Prerequisite Knowledge Graph (Cross-Grade & Within-Grade Bridges)
CREATE TABLE IF NOT EXISTS public.concept_prerequisites (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  concept_key text NOT NULL,
  prerequisite_key text NOT NULL,
  class_level integer NOT NULL CHECK (class_level BETWEEN 9 AND 12),
  subject text NOT NULL,
  prerequisite_class_level integer CHECK (prerequisite_class_level BETWEEN 6 AND 12),
  bridge_note text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_concept_prerequisites_unique
  ON public.concept_prerequisites (lower(concept_key), lower(prerequisite_key), class_level, lower(subject));

CREATE INDEX IF NOT EXISTS idx_concept_prerequisites_lookup
  ON public.concept_prerequisites (class_level, lower(subject), lower(concept_key));

-- 3. Row Level Security
ALTER TABLE public.book_chunks ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.concept_prerequisites ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Authenticated users can read book_chunks" ON public.book_chunks;
CREATE POLICY "Authenticated users can read book_chunks" ON public.book_chunks
  FOR SELECT TO authenticated, anon
  USING (true);

DROP POLICY IF EXISTS "Service role manages book_chunks" ON public.book_chunks;
CREATE POLICY "Service role manages book_chunks" ON public.book_chunks
  FOR ALL TO service_role
  USING (true)
  WITH CHECK (true);

DROP POLICY IF EXISTS "Authenticated users can read concept_prerequisites" ON public.concept_prerequisites;
CREATE POLICY "Authenticated users can read concept_prerequisites" ON public.concept_prerequisites
  FOR SELECT TO authenticated, anon
  USING (true);

DROP POLICY IF EXISTS "Service role manages concept_prerequisites" ON public.concept_prerequisites;
CREATE POLICY "Service role manages concept_prerequisites" ON public.concept_prerequisites
  FOR ALL TO service_role
  USING (true)
  WITH CHECK (true);

-- 4. Hybrid Dense + Sparse Reciprocal Rank Fusion (RRF) Search RPC
CREATE OR REPLACE FUNCTION public.hybrid_search_book_chunks(
  p_query_text text,
  p_query_embedding vector(768),
  p_class_level integer,
  p_subject text,
  p_chapter_number integer DEFAULT NULL,
  p_chunk_type text DEFAULT NULL,
  p_match_count integer DEFAULT 6
)
RETURNS TABLE (
  id uuid,
  class_level integer,
  subject text,
  chapter_number integer,
  book_code text,
  section_title text,
  chunk_type text,
  page_number integer,
  content text,
  metadata jsonb,
  rrf_score double precision
)
LANGUAGE sql
STABLE
AS $$
  WITH scoped AS (
    SELECT bc.*
    FROM public.book_chunks bc
    WHERE bc.class_level = p_class_level
      AND lower(bc.subject) = lower(p_subject)
      AND (p_chapter_number IS NULL OR bc.chapter_number = p_chapter_number)
      AND (p_chunk_type IS NULL OR bc.chunk_type = p_chunk_type)
  ),
  dense AS (
    SELECT
      s.id,
      row_number() OVER (ORDER BY s.embedding <=> p_query_embedding ASC) AS r
    FROM scoped s
    WHERE p_query_embedding IS NOT NULL AND s.embedding IS NOT NULL
    ORDER BY s.embedding <=> p_query_embedding ASC
    LIMIT GREATEST(p_match_count * 4, 20)
  ),
  sparse AS (
    SELECT
      s.id,
      row_number() OVER (ORDER BY ts_rank_cd(s.tsv, websearch_to_tsquery('english', p_query_text)) DESC) AS r
    FROM scoped s
    WHERE coalesce(trim(p_query_text), '') <> ''
      AND s.tsv @@ websearch_to_tsquery('english', p_query_text)
    ORDER BY ts_rank_cd(s.tsv, websearch_to_tsquery('english', p_query_text)) DESC
    LIMIT GREATEST(p_match_count * 4, 20)
  ),
  combined AS (
    SELECT
      coalesce(d.id, sp.id) AS id,
      coalesce(1.0 / (60.0 + d.r), 0.0) + coalesce(1.0 / (60.0 + sp.r), 0.0) AS score
    FROM dense d
    FULL OUTER JOIN sparse sp ON d.id = sp.id
  )
  SELECT
    s.id,
    s.class_level,
    s.subject,
    s.chapter_number,
    s.book_code,
    s.section_title,
    s.chunk_type,
    s.page_number,
    s.content,
    s.metadata,
    c.score AS rrf_score
  FROM combined c
  JOIN scoped s ON s.id = c.id
  ORDER BY c.score DESC
  LIMIT GREATEST(p_match_count, 1);
$$;

-- 5. Seed Prerequisite Links Across Classes 9-12
INSERT INTO public.concept_prerequisites (concept_key, prerequisite_key, class_level, subject, prerequisite_class_level, bridge_note)
VALUES
  -- Class 9
  ('linear_equations_two_variables', 'cartesian_coordinate_plane', 9, 'Mathematics', 9, 'Every solution (x, y) of ax + by + c = 0 plots as one point on the 2D coordinate grid; two solutions fix the whole straight line.'),
  ('newtons_second_law', 'rate_of_change_of_momentum', 9, 'Science', 9, 'Force measures how quickly momentum (m*v) changes each second: doubling mass or speed change doubles the push needed.'),
  -- Class 10
  ('distance_formula', 'pythagoras_theorem', 10, 'Mathematics', 9, 'The segment joining (x₁, y₁) and (x₂, y₂) is the hypotenuse of a right triangle: d = √[(x₂ - x₁)² + (y₂ - y₁)²].'),
  ('circle_through_two_points', 'perpendicular_bisector_locus', 10, 'Mathematics', 9, 'Any point equidistant from A and B lies on the perpendicular bisector of AB; the smallest circle through A and B has center at the midpoint of AB and diameter AB.'),
  ('quadratic_roots_discriminant', 'factorisation_and_parabola_x_intercepts', 10, 'Mathematics', 9, 'Roots of ax^2 + bx + c = 0 are the x-values where the parabola y = ax^2 + bx + c crosses the x-axis; b^2 - 4ac tells whether it crosses twice, touches once, or stays above/below.'),
  ('trigonometric_ratios', 'similar_right_triangles', 10, 'Mathematics', 10, 'sin(theta), cos(theta), and tan(theta) stay constant for a given acute angle because all right triangles sharing that angle are similar.'),
  ('ohms_law_vi_graph', 'linear_proportionality_slope', 10, 'Science', 9, 'On a V-I graph, constant resistance R means V = I*R is a straight line through the origin whose slope V/I equals resistance R.'),
  ('mirror_lens_formula', 'sign_convention_cartesian_axes', 10, 'Science', 10, 'Treat the pole or optical center like the origin (0, 0) on an x-y grid: light travels left-to-right, so left is negative and right is positive.'),
  -- Class 11
  ('instantaneous_velocity_derivative', 'average_slope_secant_to_tangent', 11, 'Physics', 10, 'Average velocity over a time interval is the slope of a chord on the x-t graph; shrinking delta-t to zero turns the chord into the tangent slope dx/dt.'),
  ('projectile_motion', 'independent_x_y_components', 11, 'Physics', 11, 'Horizontal motion has zero acceleration (constant u*cos(theta)), while vertical motion is free fall under gravity g; only time t links the two.'),
  ('limits_and_derivatives', 'algebraic_factorisation_and_slope', 11, 'Mathematics', 10, 'When direct substitution gives 0/0, factor and cancel the common (x - a) factor first to reveal the true limiting value near x = a.'),
  ('chemical_equilibrium_kc', 'reversible_rate_balance', 11, 'Chemistry', 11, 'At equilibrium, forward and reverse reaction rates become equal so concentrations stay steady without the reaction stopping.'),
  ('photosynthesis_light_dark_reactions', 'chloroplast_thylakoid_stroma_structure', 11, 'Biology', 11, 'Light reactions on thylakoid membranes make ATP and NADPH; the Calvin cycle in the stroma spends them to fix CO2 into sugar.'),
  -- Class 12
  ('integration_by_parts', 'product_rule_and_antiderivatives', 12, 'Mathematics', 11, 'Integration by parts simply reverses the derivative product rule d(u*v) = u*dv + v*du, trading an integral of u*dv for u*v minus the integral of v*du.'),
  ('definite_integral_area', 'riemann_sum_and_ftc', 12, 'Mathematics', 11, 'Area under y = f(x) from a to b is the accumulation of thin vertical strips f(x)*dx, evaluated cleanly as F(b) - F(a).'),
  ('gauss_law_electrostatics', 'vector_dot_product_and_flux', 12, 'Physics', 11, 'Electric flux E dot dA = E*dA*cos(theta) counts field lines piercing a closed surface; by symmetry on a Gaussian sphere or cylinder, E pulls out of the integral.'),
  ('faraday_law_emi', 'magnetic_flux_time_derivative', 12, 'Physics', 12, 'Induced EMF equals -d(Phi_B)/dt: a changing magnetic field, area, or angle theta drives current, and the minus sign (Lenz law) opposes that change.'),
  ('first_order_kinetics_half_life', 'natural_logarithm_exponential_decay', 12, 'Chemistry', 11, 'When rate is proportional to remaining concentration [A], [A] decays exponentially as [A]0 * e^(-kt), giving a constant half-life t_1/2 = 0.693/k.'),
  ('lac_operon_gene_regulation', 'transcription_promoter_operator_dna', 12, 'Biology', 12, 'RNA polymerase must pass the operator region to transcribe z, y, a genes; lactose binds and removes the repressor blocker so transcription turns on.')
ON CONFLICT (lower(concept_key), lower(prerequisite_key), class_level, lower(subject)) DO NOTHING;

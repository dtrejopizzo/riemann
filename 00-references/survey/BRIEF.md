# Brief for the  literature survey (row D)

## Target (row D)
Weil positivity on the declared carrier: λ_A(T) ≥ 0 for the window form 𝔞_T on the primitive
space P_T = {F ∈ L²(−T,T): ∫F e^{t/2} = ∫F e^{−t/2} = 0}, for every T > 0. The form is
archimedean term (Γ_ℝ Lévy kernel) minus the prime comb Σ v_n c_F(log n), v_n = 2Λ(n)/√n,
c_F the autocorrelation of F. Definitions: 04-papers/46-row-d-sign-radial-intersection-form/main.tex.
Known: certified to ½log5 (Paper 46), Liu (unrefereed) to 17/16.

## What we already know (read before searching)
- 05-meta-and-planning/ROUTES-TRIED-INDEX/README.md: closed families, phases 194–198, the
  six-clause "Specification of the sign carrier", AUDIT tags.
- Literature already covered: 05_LITERATURE.md (L01–L68) and 05b_LITERATURE_EXTENSION.md (L69–L85),
  SURVEY_MODERN_UNTRIED.md.
- Everything tried ends as: comb-generic (also holds for Beurling / Λ with small primes deleted /
  cΛ), a dual certificate (thm:Z, def:PD), or a reformulation of the positivity (REF-D).

## What is missing (the object we are hunting)
An object or theorem that:
1. reads the actual values of the prime comb (fails for Beurling systems, for Λ with small primes
   deleted, for cΛ with c ≠ 1);
2. couples the small primes (n < e^{2T}) with the global functional equation, not through the
   factor ζ(½+iτ), and not place by place;
3. is not linear in Λ, not a cone condition on log ζ, not coefficientwise integrality, not a sup of
   linear forms (dual certificate), not an exact identity;
4. carries a built-in positivity verifiable without assuming the target.
The only Λ-specific datum found: Π(T) = Σ v_n c_{h*}(log n), the comb paired against the (even)
minimizer h*, which is a near-kernel (λ ≤ 2.5e−22 at T = 1).

## Hunt for "someone already built it"
Look especially for results built for other purposes that might be exactly this missing step:
positivity theorems involving Λ or primes plus the functional equation; Fourier-interpolation /
uniqueness results with zeros or primes; extremal problems with prime-supported constraints;
operator / Hilbert-space constructions (de Branges, canonical systems, Sonine spaces, prolate)
with positivity; semilocal trace formulas; Beurling systems that do or do not satisfy RH-type
positivity and why; anything with "Weil positivity", "explicit formula" + "positive definite".

## Rules
- Use WebSearch / WebFetch (arXiv listing and API, e.g. export.arxiv.org/api/query, Google Scholar,
  MathOverflow, journal pages, author home pages, Zenodo, HAL, theses). Scan abstracts broadly
  (target ≥ 200 distinct items per survey track), read the most relevant ~15–25 in depth (full text when
  available).
- Do NOT edit repo files except your own output file in 00-references/survey/.
- For each relevant item: citation + link, what it proves (label PROVED/CONDITIONAL/CLAIMED/
  HEURISTIC, refereed or not), its positivity mechanism, which of the 4 "missing object" properties
  it has, whether it is already in our index (cite L-number or entry), and a verdict:
  NEW-CANDIDATE / KNOWN / IRRELEVANT. Be honest; do not inflate.
- Output: one markdown file with (a) list of all scanned items (compact table), (b) deep-read notes,
  (c) a ranked "possible missing-object" section with concrete first theorem we could attempt.

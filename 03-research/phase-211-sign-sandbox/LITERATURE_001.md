# Literature sweep, phase 211 (new items only, beyond L01–L110)

Scope: WebSearch/WebFetch over arXiv, Zenodo, GitHub, HAL-adjacent sources, 2024–2026, targeting
the specific problem of window positivity for a_T(F) as defined in the phase-211 brief. The index
files 05_LITERATURE.md, 05b_LITERATURE_EXTENSION.md and AUDIT_ZENODO_FRONTIER.md were read first.
Everything already carrying an L-number (Zhu, Liu, Mori I–IX, Guo Chen, Ziad, Senke, the
jose-paul-b repository, Suzuki's screw-function family, Connes–Consani–Moscovici prolate papers,
the Mehennaoui/Lemke/Eberwein items already flagged, etc.) is **not** repeated here even when it
resurfaced in search results; only genuinely new items are reported. Per the index convention,
nothing below is treated as a solution, only as a possible tool, benchmark, or falsifier.

## 1. New certification / new method beyond ½log15

Nothing supersedes Mori's ½log15 ≈ 1.354 (zenodo 23281236, already CITED and audited in
AUDIT_ZENODO_FRONTIER.md). No new window record, and no new *method* of certification (beyond the
already-known Liu bounded-comparison + Schur + Legendre-projection template), was found. One
adjacent but distinct new item:

**Mehennaoui, "Evenness from Simplicity in the Truncated Weil Quadratic Form and Conditional
Spectral Criteria for the Riemann Hypothesis"** (Zenodo 23441946, and a companion "Evenness from
Simplicity and Finite Hermitian Determinant Criteria in the Truncated Weil Framework", Zenodo
23442026; University of Skikda, posted 17 Oct 2026).
- What is proved: Theorem A (unconditional) — for the truncated Weil quadratic form QW_λ^N, if the
  lowest eigenvalue ε_N is simple, then (under an imposed reflection symmetry) the ground state is
  even. Theorems B and C are explicitly conditional (simplicity propagating to N → ∞; regularized
  determinants having only real zeros and converging to Ξ). The author states in the text that no
  unconditional proof of RH is claimed, only a structural reduction.
- Label: preprint, unrefereed, no arXiv id (Zenodo only); asymptotic statements with no explicit
  numerical range of λ.
- Tool value for the problem: low. It is a simplicity-implies-evenness lemma for the *truncated*
  (Connes–van Suijlekom-style) form, not for a_T(F)/W_T on the window directly, and it supplies no
  sign; it only says that *if* the lowest eigenvalue is simple, the ground state has a definite
  parity. Could in principle be cross-checked against the existing even/odd parity splitting
  already used in Theorems A/B/SC of the corpus (phase 155), but it does not shorten any gap there.

**GenusCore, "weil-ground-state-simple-even"** (GitHub repository plus certificate data and a
paper; Arb/FLINT interval-arithmetic computer-assisted proof).
- What is proved: for every window half-width L ∈ (0, 1.19], the lowest eigenvalue of the localized
  Weil quadratic form (for ζ) is simple with an even eigenfunction. Method: a Lipschitz argument
  for small L plus 31 certified grid windows for L ∈ [0.05, 1.19] joined by min-max monotonicity.
- Label: NUMÉRICO, explicitly unrefereed; the repository's own README states the result brings RH
  "no closer in any quantified sense," flags AI-assisted production (Claude via Claude Code),
  flags a corrected Gauss–Legendre off-by-one bug, and states that windows past L = 1 have had no
  review round at all.
- Tool value: low–medium as an independent, non-overlapping data point for the parity/simplicity
  question used as a standing hypothesis in the CCM/CvS program (L06/L39/L09 already in the
  index); it does **not** give the sign of W_T itself and does not reach or exceed the certified
  window-positivity frontier (½log15), since simplicity+evenness of the ground state is a strictly
  weaker statement than nonnegativity of the whole form.
- These two items (Mehennaoui and GenusCore) are new instances of the same move already recorded
  generically in the index (unrefereed, AI-assisted Zenodo/GitHub claims around the truncated Weil
  form): no new mechanism, so no new L-row is warranted beyond this note; record as "seen, no
  action" rather than opening a new route.

## 2. Sign-definite (not mean-square) estimates for smoothed Chebyshev sums, or Toeplitz positivity indexed by log(m/k)

No new 2024–2026 item found. Searches on "Toeplitz matrix positivity log(m/k)", "Hankel total
positivity primes", "Chebyshev sum smoothed vanishing moments sign definite" returned only generic
total-positivity combinatorics (Narayana interpolations, array-signal-processing Hankel/Toeplitz
constructions) with no prime-indexed or Λ(n)-weighted content, plus already-covered items
(S-E route to Chebyshev bounds, arXiv 2604.21946, which is a magnitude/order estimate for
Σ√(log p/p), not a sign-definite statement and not new to the target problem — it does not touch
vanishing-moment weights at scale √x). Nothing to report as new in this category.

## 3. Λ(n) coupled to the functional equation other than through ζ(½+it)

Two new 2026 preprints on twisted second moments were found, both using Voronoi + Poisson
summation, but neither couples Λ(n) to the functional equation outside the usual ζ(½+it) route,
and neither produces a sign statement:
- "The second moment of twisted modular L-functions and Dirichlet L-functions at the central
  point" (arXiv 2608.25812): moment asymptotics via Voronoi/Poisson, ordinary mean-square result,
  no positivity content for the window problem.
- "Reciprocity for the Short Twisted Second Moment of the Riemann Zeta Function" (arXiv 2608.14852):
  reciprocity formula for a twisted short second moment on the critical line, extends Khan's
  reciprocity; again a mean-value identity, not a sign-definite statement, and it still reads ζ at
  ½+it.
Neither is a tool for the a_T(F) problem beyond what reciprocity/Voronoi techniques already
contribute generically (and those are already covered via the Voronoi/explicit-formula family in
the index). No approximate functional equation for ζ'/ζ specifically, and no "Dirichlet polynomial
mean value against digamma weight" paper, was found in 2024–2026.

## 4. Positivity-preserving structures: Beurling primes with functional equation, Bochner on ℚ_{>0}^×, Kreĭn extension with prime atoms

- Beurling generalized primes + functional equation + positivity, 2024–2026: nothing beyond what
  is already in the index (Diamond–Montgomery–Vorhauer family, covered). Current arXiv hits
  (Carlson-type zero density, Riemann–von Mangoldt formula for Beurling primes, functional
  independence of Beurling zeta functions) are all classical analytic-number-theory results about
  Beurling systems, with no functional-equation-plus-positivity statement and nothing new since the
  last sweep.
- "Positive definite functions on the multiplicative group of positive rationals" / Bochner on
  ℚ_{>0}^×: no literature at all was found treating ℚ_{>0}^× (as a discrete group ≅ ⊕_p ℤ) directly
  as the Bochner/Pontryagin domain in connection with Λ(n) or the Weil form. The only adjacent
  material is the standard quantum-group/Coxeter-group generalizations of Bochner's theorem
  (arXiv 1210.5231, 1704.06845), which are structural generalizations with no arithmetic content;
  not a tool.
- Kreĭn extension problem with prime-indexed atoms: no new paper found connecting Kreĭn's classical
  extension theorem (continuous PD functions on (−a,a) extend to ℝ) to a prime-indexed discrete
  atomic measure. The only material is the generic classical theory (Krein 1940s; the
  multi-dimensional failure of extension for n>1 cubes), already generically covered by L20. This
  is a genuine gap: nobody has posed the window problem as a Krein extension problem with atoms at
  log p specifically; it remains unexplored, not merely covered-and-rejected.

## 5. De Branges spaces and the Weil form on finite intervals, 2024–2026

No item beyond what is already indexed (Suzuki's de Branges/Hilbert-space-from-the-Weil-distribution
paper, arXiv 2301.00421, already L38/covered; the Lemke private-communication construction and its
arXiv 2609.04908 descendant, already covered per L57's correction). One tangential new preprint:
"On the construction of de Branges spaces for dynamical systems associated with finite Jacobi
matrices" (arXiv 2505.20905) — this is a finite-Jacobi-matrix de Branges construction with no
arithmetic content (no primes, no ζ); it is a generic linear-algebra tool for building de Branges
spaces from finite matrices, conceivably reusable as machinery for a finite-N truncation but with
no bearing on the sign problem itself. Not worth an index row; noted here as "exists, no bearing."

## Summary of what is genuinely new since L01–L110

Only two new non-duplicate items exist, both low-value for the sign problem: Mehennaoui's
evenness-from-simplicity reduction for the truncated form (Zenodo 23441946/23442026, conditional,
unrefereed) and GenusCore's Arb-certified simple-even-ground-state result up to L = 1.19 (unrefereed,
explicitly self-described as bringing RH "no closer"). Neither reaches, challenges, or offers a new
mechanism toward the certified frontier (Mori's ½log15). Every other search category (sign-definite
smoothed Chebyshev/Toeplitz positivity, Λ(n) coupled to the functional equation outside ζ(½+it),
Bochner on ℚ_{>0}^×, Kreĭn extension with prime atoms, de Branges spaces on finite intervals) turned
up nothing new worth recording as a tool; "nothing new" is the honest answer for categories 2–5. The
clearest open gap surfaced by this sweep is category 4's Kreĭn-extension-with-prime-atoms framing,
which appears never to have been attempted in the literature at all (not closed, simply absent).

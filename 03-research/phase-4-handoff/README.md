# Phase 4 — Handoff: a faithful Kreĭn-space realization of the Weil quadratic form

The phase asks whether the Weil positivity criterion can be given a rigorous operator-theoretic
realization on the classical band-limited (Paley–Wiener) test class, and whether that realization
opens any route to the sign of the associated operator's spectral bottom. It builds a semibounded
operator $\mathcal T$ representing the Weil functional, identifies its structure as a Kreĭn-space
(indefinite-metric) problem via an exact identity $\mathfrak t = E^*JE$, and proves a no-go result
on zero-side attacks.

## Results
- Semibounded realization of $\mathcal T$ on $PW_d$ with finite spectral bottom (theorem B-2):
  PROVED unconditionally except for one isolated hypothesis (H), a uniform short-interval
  zero-density statement strictly weaker than the Riemann Hypothesis.
- Exact identity $\mathfrak t = E^*JE$ with $J$ a genuine Kreĭn fundamental symmetry: PROVED.
- Sharpened angular-operator reformulation ($\|K\|<\infty \iff$ B-2) unifying B-2 and the sign
  question on one axis: PROVED, with the factor-4 slack of B-2 removed.
- No-go theorem: the zero-side expression for $K$ and the arithmetic side of the explicit formula
  are the same functional, so no zero-position-free, sign-agnostic bound on $\|K\|$ can reach the
  needed threshold: PROVED (structural, not a temporary gap).
- Comparison to Connes–Consani's archimedean angular operator and to the de Branges completion:
  the construction is identified as the same abstract framework, not new ground: CITED/ARGUED.

## Documents
- `PAPER-A.md` — self-contained write-up of the full construction and the no-go theorem.
- `B2-THEOREM.md` — the semibounded realization theorem and its supporting lemmas.
- `B3-KREIN-STRUCTURE.md` — the Kreĭn/angular-operator identification and audit of the identity.
- `PHASE4-WORK-PROGRAM.md` — work program stating the single open question (faithfulness, not the sign) and decomposing it for further attack.
- `RH-ENDGAME.md` — candid statement of what the machinery does and does not reach.
- `proofs/` — day-by-day proof log and audits (Days 10–22) of the lemmas used in B2 (closability, semiboundedness, quadrature, Plancherel–Pólya, coercivity), plus LaTeX sources.

## Relation to other phases
`phase-5-structural` (Route B, milestones M1–M5) builds directly on this phase's Kreĭn template and
no-go theorem, comparing it to the Connes–Consani and de Branges frameworks.

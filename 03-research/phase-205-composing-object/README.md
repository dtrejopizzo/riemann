# Phase 205 — The object that composes E and F

## Goal
Build the object: assemble the skeleton and then advance piece by piece, starting from the sign already established.

## Architecture of the sign (the PROVED part; phase 204)
1. **Counting, not a bound.** The even archimedean form has ≍ 4T negative directions (lem:archcount, Theorem A∞); the
   even form with comb and without pole never drops below one (cor:H1minus). Even positivity in the window T ⟺ the comb
   exactly cancels all but one of those directions.
2. **Exact residual inertia.** n₋(𝔄_ev) = 1 (pole) + one hyperbolic pair per quadruple of zeros off the line
   (H1PLUS_001, PROVED); verified in ζ (1), Epstein T=2 (2), DH (0). Even positivity ⟺ n₋ = 1 ∧ q_ev < −½ (prop:WT),
   with q monotone on intervals of constant inertia (Lemma WT-R).
3. **Where the sign is not.** Not in anything linear in the comb; not in the symbol on the line; not in the escape
   quotient; not in imported positivities; not in functionals of the minimizer; not in the exterior via Möbius (→ 1/ζ);
   not in polynomial scales (Prop S). Every proof uses E (Dirichlet series over ℕ) and F (FE, conductor 1) IN THE SAME
   SIGN STEP, composed and not chained (rem:conjunctions, Φ200′). Never done before.
4. **Falsifiers the object must respect in the identity:** Epstein x²+5y² (quadratic Euler defect Λ_cosh;
   hyperbolic pair), DH (no pole, no Euler), a_P (partial Euler, broken FE), cΛ c≠1, Beurling (no FE), quartets
   (FE without E-series). Certified battery: 12 witnesses.
5. **Reference datum:** Mori extremal μ=15 (W_T(g*) = 4.978e−70; g* of one sign; f* = Möbius⁻¹ g* changes
   sign; resonances μ(n); staircase; ℓ* upper bound).

## Specification of the object (what it must satisfy)
S-A: input (F ∈ P_T even, exact comb Λ); output: a NONLINEAR sign step in the comb that uses E and F at once.
S-B: in ζ it reproduces the cancellation of ≍4T − 1 directions (counting); in Epstein it leaves a hyperbolic pair; in
DH the pole does not exist; in a_P, F is broken; in Beurling, E is broken — all IN THE IDENTITY, not numerically.
S-C: it is not the zero form (P4), it is not the minimizer (Theorem X), it does not go through norms (R-K1), it is not
data (C-data).
S-D: each piece of the skeleton is PROVED, CITED, or has an OPEN lemma with an exact statement and a death criterion.

## Protocol
Skeleton → skeleton audit → pieces one by one (numerical verification in Mori/Epstein/DH) → index in the same phase.

## Status
- SKELETON_001 → AUDIT (P3 = lem:polarelim rewritten; Φ_E = −𝓕_T; L205.★ REF-D withdrawn) → SKELETON_002: no sign
  node; P1.c NO-GO (pole failure at high frequencies); P1.c′ OPEN (upper bound of A∞ in P_T + control of 𝓕_T = M1).
- Pieces PROVED: P2a (comb matrix in Dirichlet sines), coefficients c_k of χ_ev, A∞(t₀′) ≈ 3.90T.
- **No node exists in the corpus that composes E and F (Def O1.2) with an identified abstract falsifier.**

## Other files in this folder

- `AUDIT_205_SKELETON_001.md` — Skeleton review (phase 205).
- `BIBLIO_CHECK_001.md` — Bibliographic verification, phases 200–205 and Paper 46.
- `INTEGRATION_205_001.md` — Integration into Paper 46, phase 205.
- `REVIEW_STATE.md` — State of the audits of this phase.
- `RFIN_TRACT_001.md` — Tractability review: the finite reformulation "n₋(𝔄_N(T)) = 1 ∀T" (phase 205, part R-fin).
- `INTEGRATION_205_001_check.py` — script.

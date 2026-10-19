# Phase 191 — design specifications for a statement T*

A design-only round (no construction, no numerics beyond cited record
values) that tries to write down a precise statement T*, stronger than the
row-D target λ_A(T) > 0 for all T, provable by induction through the prime
contacts T_j = ½log n_j, or isolated at a single selected frequency. Each
candidate formalization is checked against the admissibility clauses of the
SHAPE theorem and the crossword before any attempt is made.

## Results
- SPEC A (exact induction through contacts): the inductive step is an exact
  restatement of the target at the next contact, entering only through the
  resolvent of the frozen window; it would have to decide a sign of size
  doubly-exponentially small in T, while every available power-saving input
  is at best exponentially small — clause (γ) fails by a doubly-exponential
  factor — and no step uses ℤ-integrality (clause θ). **NOT ADMISSIBLE**
  (the base cases T*_1..T*_4 up to ½log5 are **PROVED/CITED** independently
  of the induction design).
- SPEC B (missing estimate at a selected frequency / integer resolution):
  exactly three consistent formalizations exist. The single-frequency form
  T*₁(γ) is an exact limit equality with no power-saving slack and is, in
  content, a half-plane summability statement (Hardy-Riesz), so it fails
  clauses (λ) and (κ). The pointwise-mesh form is false for ζ (the symbol is
  negative on a nonempty set). The correlated-mesh form T*₂ is an exact
  restatement of row D itself. **NOT ADMISSIBLE** for T*₁, T*₂ (REF-D).
- The remaining variant, T*₃(η) on a smooth-cutoff family (problem (S)), is
  genuinely new in form (supplies prime-divisibility and ℤ-integrality
  content) but collapses to row D itself (REF-D) for small cutoff parameter
  η, and is otherwise an unproved necessary condition that does not close
  D. **OPEN** (bounded by NUMERICAL estimates of the threshold η₀≈0.3-0.4).
- No sign of λ_A(T) is certified by either specification.

## Documents
- `SPEC_A_EXACT_INDUCTION.md` — formal design of the induction-through-
  contacts statement, base cases, and the clause-by-clause failure analysis.
- `SPEC_B_SELECTED_FREQUENCY.md` — the three nested formalizations T*₁, T*₂,
  T*₃(η) of a selected-frequency estimate, with a full clause-compliance
  table (A1-A17, B1-B8) against the SHAPE theorem's admissible region.

## Relation to other phases
Builds directly on the SHAPE theorem and crossword (phase 190), on the
λ_A(T) machinery and margin/ceiling theorems of Paper 47, and on the
routes-tried index; both specifications close as design dead ends except
for the single open residual T*₃(η), handed off as a target for later
phases (190/EXP_005's bulk/edge split is named as the unfinished next step).

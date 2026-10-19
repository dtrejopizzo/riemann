# Phase 118 — The exact threshold inequality

Phase 117 eliminated the Gamma–Tate source route for the row-(d) threshold condition and redirected
effort to proving the exact inequality S_E − Z_E*Z_E − b_E*A_0†b_E ≥ 0 (equivalently ‖Θ_N‖≤1) directly,
in the output-defect metric where it has constant one. This phase derives exactly what the operator A_T
is, verifies that identity to high precision, and tries several structural routes to close it.

## Results
- Exact identity derived and verified: for primitive F supported in I_T, ⟨A_T F,F⟩ equals a sum over the nontrivial zeros of ζ of ĥ(γ_ρ) with h(τ)=F̂(τ)F̂(−τ); three features that looked like design choices (the archimedean constant m₀, restriction to the primitive space, and the prime-sum truncation) are each shown forced rather than chosen. PROVED, verified numerically to relative agreement 5.4e-11–1.6e-9 at several T values.
- Consequence drawn from this identity: the target inequality, taken over all T, is classified as unreachable by any purely operator-theoretic reformulation (factorization, Schur complement, defect operators, scattering), since none of these adds arithmetic input; the phase closes this specific target rather than continuing to pursue it. NO-GO (route closed as posed).
- Independent cross-check of the balanced factorization (X*X=R, Y*Y=L, X*X−Y*Y=A) to ~1e-12 at 19 prime-power thresholds, via a code path sharing nothing with the main assembly beyond the mesh. NUMERICAL (verification).
- Structural candidates for the scattering operator are killed by measurement: Toeplitz-in-log-n and Hankel-in-log-n structures refuted (R²≤0.16); block-diagonal-over-places excluded; no explicit factor Ψ found with I−Φ*Φ=Ψ*Ψ; a heuristic that the archimedean channel carries the positivity load is refuted (its share falls, 0.70→0.59→0.44, with threshold). NO-GO (each structural candidate).
- The existing log-2 certificate is reproduced and diagnosed: all precision/tail-quadrature budgets have large headroom, so the limiting factor is the genuine smallness of a Feshbach gap (h=0.0012) near one direction, not numerics; extending further requires unfinished cross-coupling analytic work previously attempted and retracted elsewhere. CONFIRMED (reproduction) / OPEN (extension).
- λ_min(A_0) measured to shrink toward 0 under refinement (to 5.4e-8 at refine 512), confirming an earlier "no spectral gap" finding. NUMERICAL.
- Left open and carried forward: an unresolved 2%–8% discrepancy between two independent computations of the same quantity for piecewise-constant test functions, suspected to be a truncation bug in the cross-validation script, not yet checked; and whether λ_min converges to a positive limit or to zero. OPEN.

## Documents
- `PHASE_118_CLOSURE.md` — the closure note summarized above.
- `LAUNCH.md`, `RESUME.md`, `SPEC.md`, `PROOF_ARCHITECTURE.md` — phase setup, resumption notes, specification, and the architecture document recording the unresolved two-route discrepancy.
- `W3_SCATTERING.md` — the independent balanced-factorization cross-check and structural-candidate refutations.
- `W4_CERTIFIED_RANGE.md` — reproduction and diagnosis of the existing log-2 certificate.
- `scripts/`, `vendor/` — supporting computation and third-party code used for the verifications above.

## Relation to other phases
Continues phase 117 (redirected target after its Gamma–Tate source-route no-go); continues in `phase-119-what-a-finite-compression-certifies/`, which inherits the unresolved two-route discrepancy and the open λ_min question as items to settle first.

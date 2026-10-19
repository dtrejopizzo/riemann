# Phase 23 — two-scale structure and spectral compatibility of the defect

Continuing phase 22's Hypothesis D (a finite nonzero number of off-line zero
orbits), the phase computes the exact effect of such a defect at two scales
— the prime-counting scale x and the critical-line height scale t — and
tests whether that effect is compatible with the unconditional prime number
theorem and with the Gaussian-multiplicative-chaos (GMC) model of ζ
fluctuations, in the hope of finding a contradiction that would force the
defect to vanish. No numerics; only Hadamard-product computations, the
Korobov-Vinogradov prime number theorem, and structure-function estimates.

## Results
- Proposition 23-A.1: exact closed-form contribution δ_j log|ζ(1/2+it)| of
  an off-line orbit to the log-modulus of ζ on the critical line, derived
  directly from the Hadamard product. **PROVED**.
- The resulting depression has depth O(log log γ_j) at t = γ_j, while the
  GMC model predicts fluctuations of size O((log log γ_j)^{1/2}); although
  the ratio diverges, this is shown to be an unusual-but-not-impossible GMC
  tail event, not a contradiction. **Negative result**: GMC is compatible
  with Hypothesis D.
- Proposition 23-B.1 (lower bound) and 23-B.2 (unconditional upper bound,
  via Korobov-Vinogradov) on the structure function S_2(τ,T) of ψ
  fluctuations; Theorem 23-B.3 shows the two bounds are always compatible
  whenever b_j < 1/2, which holds automatically for any off-line zero — so
  no contradiction is produced. **PROVED compatible (negative for the
  program)**.
- Theorem 23-C.1 (Fundamental Obstacle Theorem): excluding Hypothesis D (or
  proving Exclusion Conjecture EX / RH) from the phases 21-23 toolbox
  requires one of three further inputs — (F1) an unconditional PNT error
  bound stronger than any b_j (essentially equivalent to RH), (F2) a
  property of the Euler product incompatible with poles of -ζ'/ζ inside the
  strip (the content of the still-open "Wall W4-RSRP"), or (F3) a GMC
  property incompatible with the computed depression. None of the three is
  available from the current toolbox. **PROVED** (as a precise statement of
  what is missing).
- Overall: the spectral/structure-function strategy for excluding a finite
  defect is closed negatively; all five methods tried (explicit
  formula+Paley-Wiener, three invariant candidates, GMC, structure
  function, Korobov-Vinogradov restriction) reach exactly the boundary
  Re(s)=1 and no further. **NO-GO** for this strategy as a whole.

## Documents
- `00-setup.md` — recap of phase 22's findings and the two-scale question.
- `01-exact-hadamard-effect.md` — exact Hadamard-product computation of the
  off-line orbit's effect on log|ζ(1/2+it)| (Proposition 23-A.1).
- `02-structure-function-analysis.md` — lower/upper bound analysis of the
  structure function S_2(τ,T) and the compatibility theorem 23-B.3.
- `03-barrier-formulation.md` — the Fundamental Obstacle Theorem (23-C.1),
  frank evaluation of the three remaining routes (F1/F2/F3), and the
  summary table for phases 22-23.

## Relation to other phases
Direct continuation of phase 22 (Hypothesis D, Exclusion Conjecture EX);
closes the spectral direction and proposes a successor phase 24 on the
analytic uniqueness of the Euler product as the only unexhausted route
(Wall W4-RSRP, route F2).

# Phase 3 — The Structural Assault on the Uniform Inequality

This phase states the single inequality to which prior programs reduced the problem — the localized Weil quadratic form $Q(T_0,\sigma,J) = M_{\mathrm{zeros}} - M_{\mathrm{arith}}$ on a Hermite–Gauss basis, and the "uniform positivity limit" (LB): $\lambda_{\min}(Q_\infty(f)) \ge 0$ for every admissible test function — and asks whether a structural reason forces (LB) to hold. It specifies a numerical validation engine (reference zero sets for $\zeta$, a Dirichlet L-function, the Davenport–Heilbronn RH-violator, a cusp-form L-function, and a de Bruijn–Newman-type deformation family) and lays out two candidate structural routes: a Connes trace/reflection-positivity compression, and a de Branges canonical-system monotonicity/chain condition.

## Results
- (LB), the uniform positivity limit, is identified explicitly as being equivalent to RH; no reduction in this phase removes that equivalence. (stated explicitly, not a new result)
- Forced negativity under an off-critical zero, and truncation-error control of the prime cutoff ($\eta(X)\le Ae^{-\alpha(\log X)^2}$): carried over from prior work as already unconditional. (PROVED, inherited, not re-derived here)
- Two candidate structural routes (Connes trace compression; de Branges chain/monotonicity condition) are set up as dictionaries to be verified, with a function-field analogy (intersection-form positivity) offered only as orientation toward the Connes route. (OPEN — framework only, no result proved)
- A numerical engine specification (five controls: $\zeta$, $L(\chi_4\bmod5)$, Davenport–Heilbronn $L_{DH}$, the Ramanujan $\Delta$ L-function, and a $\zeta_\delta$ real-part-deformation family) with validation gates and reference output values ($\lambda_{\min}$ magnitudes, locality, $\delta^2$ scaling) for testing the two structural conjectures. (NUMERICAL, specification/validation data only, no conjecture tested to completion here)

## Documents
- `phase3-plan.md`: states the uniform-inequality target (LB), the two structural flanks (Connes, de Branges), the function-field orientation, and a staged realistic/strong/dream outcome plan.
- `engine-spec.md`: specification of the numerical validation engine — reference zero sets, the five controls, the localized Weil quadratic form $Q$, and reference engine outputs for validating implementations.

## Relation to other phases
This phase states the frontier inequality that the later CCM-based phases (29 onward) approach from a different, operator-theoretic direction; it is explicitly flagged as the only phase that "could, in principle, touch RH," with the frank acknowledgment that (LB) itself already is RH.

# Paper 31 — A curvature criterion for the Riemann Hypothesis and the unification of four analytic frameworks

The paper derives an explicit Hadamard curvature formula for the completed zeta function on the critical line, C(γ) = ∂²_σ log|ξ(σ+iγ)| at σ = 1/2, written as a sum over all non-trivial zeros, and proves that RH holds if and only if C(γ) > 0 for every γ not an ordinate of a zero, equivalently ξ(1/2+it) lies in the Laguerre–Pólya class. It then uses this criterion to place four frameworks proposed as proof strategies in one picture: de Bruijn–Newman heat flow and Kreĭn monotonicity, APS spectral flow, a K-theoretic obstruction class, and a transversal energy functional. The curvature splits into an analytic sector computable from the functional equation and a zeta sector, and the remaining difficulty is located in a lower bound for the zeta sector.

## Main results

- `thm:curvature` (curvature formula) — PROVED.
- `thm:rh-curvature` (curvature criterion: RH ⟺ C(γ) > 0 off the ordinates; equivalently membership in the Laguerre–Pólya class) — PROVED.
- `thm:lp` (unification of the four frameworks through the criterion) — PROVED as a reformulation.
- `thm:sectors` (sector decomposition into analytic and zeta parts) — PROVED.
- `prop:wall`, `thm:wall`: RH is equivalent to G_ζ(t) > −G_ana(t) for t > t*; this lower bound is OPEN.
- Supporting computations of the sectors — NUMERICAL, illustrative only.

## Files

- `main.tex` — LaTeX source.
- `main.pdf` — compiled paper.

## Relation to other papers

The curvature formula is used again in the colligation route of Paper 35.

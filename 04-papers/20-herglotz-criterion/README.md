# A Herglotz positivity criterion for the Riemann hypothesis

This expository paper studies the known criterion that the Riemann hypothesis holds if and only if Re ξ′/ξ(s) > 0 for Re s > ½, where ξ is the completed zeta function. It gives short proofs of the criterion, of an elementary identity on the critical line, and of the Nevanlinna-function form of the criterion, with a few numerical evaluations.

## Contents
- Proposition 2.1 (`prop:crit`): RH ⟺ Re ξ′/ξ > 0 on σ > ½, proved via the Hadamard sum and the pole of ξ′/ξ at an off-line zero.
- Theorem 3.1 (`thm:boundary`): Re ξ′/ξ(½+iτ) = 0 whenever ξ(½+iτ) ≠ 0 (elementary, from the functional equation).
- Corollary 3.2 (`cor:min`): σ ↦ log|ξ(σ+iτ)| is stationary at σ = ½ for such τ; under RH it has a strict local minimum there.
- Proposition 4.1 (`prop:minprinciple`): positivity holds iff ξ has no zero in σ > ½; a minimum-principle argument is noted as heuristic only.
- Section 5: with s = ½ − iz, m(z) = i ξ′/ξ(½−iz) is a Nevanlinna function iff the criterion holds; under RH its operator realization is built from the zeros and gives no independent route to RH.
- Appendix A: numerical evaluations at a few points (numerical, not a verification beyond those points).

## Known and new
The criterion is due to Hinkkanen (1997) and Lagarias (1999); the monotonicity form is in Sondow–Dumitrescu (2010). Nothing in the paper goes beyond the known equivalence.

## Files
- [main.tex](main.tex) — LaTeX source.
- [herglotz-criterion.pdf](herglotz-criterion.pdf) — compiled paper (4 pages).
- The Python (mpmath) code for the numerics is given as listings in Appendix A; there are no separate script files.

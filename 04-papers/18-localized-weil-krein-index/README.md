# The localized Weil form on even test functions: off-line Lorentzian blocks and obstructions to positive-kernel realizations

The paper studies the symmetric bilinear form Q(f,g) = Σ_ρ φ_f(ρ) φ_g(ρ) on even real test functions f ∈ C_c^∞(ℝ), where φ_f(s) = ∫ f(u) e^{(s−1/2)u} du and ρ runs over the nontrivial zeros of ζ. Q(f,f) is the zero side of Weil's explicit formula at f∗f, so the Riemann Hypothesis implies Q ≥ 0. The paper describes where negative directions of Q can come from and which kinds of spaces cannot carry them.

## Results
- Lemma 2.3: the series defining Q converges absolutely; φ_f(1−s) = φ_f(s), φ_f(s̄) = conj φ_f(s).
- Theorem 3.1: Q splits into nonnegative squares f̂(γ)² over on-line zeros and one Lorentzian block 4μ(u² − v²), u + iv = f̂(γ − ib), per off-line quartet.
- Proposition 4.1, Theorem 4.2: the modular-surface resonance weights R_ρ = Λ(ρ−1)/(2Λ'(ρ)) = (ρ/(ρ−2)) ξ(ρ−1)/(2ξ'(ρ)), Λ(s) = π^{−s/2}Γ(s/2)ζ(s), for simple zeros, with a Stirling asymptotic; |R_ρ| is computed numerically (0.51–0.69 for the first fifteen zeros, 1.04 at the 300th). The Cauchy-type resonance pairings are sign-definite for every configuration of simple zeros in the strip.
- Theorems 5.1–5.3, Corollary 5.4: positive-kernel forms are semidefinite; Cauchy Gram forms with parameters on one side of a line are definite; continuous non-degenerate families of Hermitian forms on ℂ^N have constant index.
- Theorems 6.2–6.3, Lemma 6.4, Proposition 6.7: evaluation functionals at points with disjoint orbits {±z, ±z̄} are independent on even real functions; signature of bilinear evaluation forms.
- Corollary 6.5: with m < ∞ off-line quartets, the off-line part of Q has signature (m, m) and the negative index satisfies κ_V ≤ m. Equality is left open.
- Remark 6.6: E_ξ(z) = ξ(1/2 + iz) satisfies E_ξ^# = E_ξ, so H(E_ξ) = {0}.
- Theorem 8.4: a realization of Q satisfying the three de Branges axioms is a space H(E) (Kaltenbäck–Woracek) whose negative index is at least κ_V.
- Proposition 9.2, Theorem 9.5: the zero set is invariant under s ↦ s̄, s ↦ 1−s unconditionally; RH is the pointwise condition 1 − ρ̄ = ρ. Remarks 9.4 and 9.6 are explicitly heuristic.

Open: κ_V = m, finiteness of m, existence of a realization satisfying the de Branges axioms, and the location of the zeros of its structure function.

## Known and new
Weil's explicit formula and criterion, the Moore–Aronszajn theorem, de Branges' theory and its Pontryagin-space extension by Kaltenbäck and Woracek are classical and are cited. The quartet decomposition on even real test functions, the independence lemma on that space, the bound κ_V ≤ m and the obstruction statements as formulated here are the contribution of the paper; they are elementary.

## Files
- [main.tex](main.tex) — LaTeX source.
- [localized-weil-krein-index.pdf](localized-weil-krein-index.pdf) — compiled paper (13 pages).
- [scripts/resonance_weights.py](scripts/resonance_weights.py) — computes |R_ρ| for the zeros listed in Proposition 4.1 (requires mpmath).

## Relation to other papers
Papers 7, 8 and 11 of the series treat related forms (a Hermite–Gauss Gram matrix of the Weil form, a Kreĭn-space formulation of its zero side, and the negative index of the full Weil form on functions of bounded support).

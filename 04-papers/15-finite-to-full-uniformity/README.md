# Eventual versus uniform positivity in scale-dependent hierarchies

The paper separates "eventually positive at each order" from "uniformly positive at all orders" for positivity hierarchies that depend on a scale parameter, and studies how the Hodge–Riemann gap of a convergent family of forms behaves in the limit. The Jensen-polynomial hierarchy of the Riemann ξ-function is discussed heuristically; no statement about the Riemann hypothesis is proved.

## What the paper proves or observes
- Theorem 3.1: elementary observations — eventual and uniform positivity coincide for scale-free hierarchies; a bounded threshold gives uniform positivity beyond a single scale.
- Proposition 6.1: scale-dependent hierarchies with bounded threshold exist (elementary example).
- Lemma 8.2, Proposition 11.1: continuity of the HR gap under convergence of forms and primitive projections, with an explicit rate (standard perturbation argument); Corollary 8.3 notes that positivity holds at every level regardless of the limit.
- Examples 9.1–9.2: weak convergence of discrete measures gives unbounded threshold T_0(N)=N; a mixed measure has positive definite Hankel forms at every level but a gap ≍ 1/m (the 1/m decay is proved by a two-sided eigenvalue bound and illustrated numerically).
- Example 9.3: the lemma does not apply as stated to uniform matroids, whose Chow rings grow with m.
- Section 6: for measures on [-1,1] the smallest Hankel eigenvalue tends to 0 with the order (short proof; Hilbert-matrix values computed).
- Remarks 5.1, 7.1 and Section 10: heuristic discussion of the ξ Jensen hierarchy; no RH-related result.

## Known and new
The perturbation lemma is standard; the Turán inequalities (Csordas–Norfolk–Varga) and the eventual hyperbolicity of Jensen polynomials (Griffin–Ono–Rolen–Zagier) are cited. What is new is only the organization of the quantifier distinction and the examples.

## Files
- [main.tex](main.tex) — LaTeX source.
- [finite-to-full-uniformity.pdf](finite-to-full-uniformity.pdf) — compiled paper (8 pages).
- [code.py](code.py) — toy families of forms constructed to have the stated gaps (Appendix A).
- [code2.py](code2.py) — smallest Hankel eigenvalues of the mixed measure ν_m (Appendix B).

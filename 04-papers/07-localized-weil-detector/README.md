# The localized Weil form on a Hermite–Gauss basis: the effect of an off-line zero pair and the truncation of the prime sum

The paper considers the Gram matrix of Weil's quadratic form on J Hermite–Gauss functions of width σ centred at height T₀, written as the zero side minus the arithmetic side of the explicit formula. It studies how this matrix responds when a zero pair is moved off the critical line by hand, and how fast the prime sum converges when it is cut at X.

## Results

- **Lemma 3.1, Theorem 3.2 (proved).** Replacing a double point 1/2 + iγ of the zero configuration (γ arbitrary) by the pair 1/2 ± δ + iγ changes the zero-side matrix by δ²A(γ) + R, with A = −(ΦΦᵀ)'' of rank ≤ 3, ‖R‖ ≤ C(γ,δ)δ⁴ explicit, and least eigenvalue −a(γ) < 0 (indefinite in all computed cases) with an explicit lower bound for a(γ). Weyl's inequality turns this into bounds for the least eigenvalue of the perturbed matrix.
- **Theorem 4.2 (proved).** The operator norm of the prime-sum tail beyond X is at most an explicit integral, which is exp(−σ²(log X)²/4 + (log X)/2 + O(log log X)); hence ≤ A_tr exp(−α(log X)²) for every α < σ²/4. Only the Chebyshev bound ψ(x) < 1.03883x (Rosser–Schoenfeld) is used.
- **Theorem 5.1 (proved).** For the model configuration (zero side of ζ plus the change P_δ produced by splitting a double point at 1/2 ± iγ into the four points 1/2 ± δ ± iγ, a formal signed configuration; arithmetic side of ζ), the truncated matrix has a negative eigenvalue for X ≥ X_min, given explicitly, when δ is below an explicit threshold (C_* δ² ≤ (1−κ)a_*/2).
- **Proposition 6.1, Corollary 6.2 (proved).** For a fixed basis the limit X → ∞ is controlled unconditionally; under RH the zero-side matrix is positive semidefinite for every basis.
- **Numerical.** Proposition 3.4 checks the expansion of Lemma 3.1 on 80 parameter cases; Proposition 4.3 compares the tail bound with the computed tail; Remark 2.1 checks the explicit formula on the basis; Table 1 gives cutoffs X_min.

For ζ itself the truncated matrix is the prime tail and tends to 0 whether or not RH holds: nothing in the paper bears on RH.

## Known and new

The explicit formula and Weil's criterion are classical (Weil 1952; Bombieri 2000), as is the Gaussian decay of the prime sum for Gaussian test functions. The new content is the explicit second-order perturbation formula on the Hermite–Gauss basis, the explicit tail majorant, and the resulting cutoff for the model configuration.

## Files

- [main.tex](main.tex) — source
- [localized-weil-detector.pdf](localized-weil-detector.pdf) — the paper (8 pages)
- [numerics.py](numerics.py) — script for all numerical statements (numpy, scipy, mpmath); `python3 numerics.py [output_dir]`
- [results/zero_side.txt](results/zero_side.txt) — output for Lemma 3.1, Remark 3.3, Proposition 3.4, Theorem 3.2(iii)
- [results/prime_side.txt](results/prime_side.txt) — output for Remark 2.1, Theorem 4.2, Proposition 4.3, Table 1

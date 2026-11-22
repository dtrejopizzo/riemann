# Paper 39 — Cofinal Weil Quotients: Exact Transport, Fixed-Cutoff Summability, and the Global Branch Obstruction

## What the paper studies

The finite self-adjoint operators of Connes–Consani–Moscovici (CCM) are built from principal Fourier restrictions of the semilocal Weil form at a physical cutoff L = 2 log λ: the restriction is shifted by its least Ritz value and quotiented by the resulting one-dimensional radical. Suzuki studies a related continuous localized operator. The paper examines the two limits N → ∞ (L fixed) and L → ∞, and then rewrites the complete Weil form, without cutoff, in a ground-state coordinate given by Riemann's full positive kernel K (with K̂ = Ξ). No conclusion about RH is claimed.

## Results proved unconditionally (given the simple-even and nonzero-overlap hypotheses that define the CCM quotients)

- Canonical isometric connection between successive quotients (Theorem 3.2). Exact transport defect: two rank-one channels of opposite parity (Theorem 4.1) plus a Loewner/double-operator-integral metric correction (Theorem 5.1).
- Exact second-resolvent increment (Proposition 6.1) and the Cauchy-transform formula Tr(s−D_N)^{-2} = Σ(s−2πk/L)^{-2} − (log C_N)'' (Theorem 7.1). Consecutive scalar criterion (Theorem 7.3).
- Compact-form counterexample: abstract Galerkin compactness alone cannot prove consecutive (gap–drop) summability (Proposition 9.1).
- Affine-free ground/model criterion, valid on compact subsets of 0 < |Im z| < 1/2 away from the zeros of Ξ (Theorem 11.1). Affine rigidity and divisor rigidity of the logarithmic curvature (Theorems 12.1, 12.2).
- Residual/overlap criterion and bilateral parity detection: failure of RH gives fixed compactly supported negative tests in both parity sectors (Theorems 13.1, 13.2).
- Moving co-Poisson radical: an exact zero-side identity, rewritten through the paper's explicit source form with primes, prime powers, Gamma and pole kept together (Theorem 15.1). Frame–residual conservation (Theorem 16.1).
- Translated Montgomery–Vaughan mean square on Fourier blocks (Theorem 18.1). Centered prime–Gamma square with κ_N = 4λ + o(λ) and unique minimum at t = 0 (Theorem 19.1, Corollary 19.2).
- Exact PNT-discrepancy compensation and the quadratic completion QW_L = E_* − c_* I − A_Δ with E_* ≥ 0 and c_* > 0 (Theorems 20.1, 20.2).
- Nonlocal Picone identity (Theorem 21.1) and a positive one-atom countermodel (Proposition 21.2): generic jump positivity cannot give the branch sign.
- Smooth truncations of K are operator quasimodes with super-exponentially small residual (Theorem 22.1). This gives only the residual input for q_L^K. It does not address Gate SPG.
- Doob–variance identity QW(Kr,Kr) = E_K(r) − ½ Var_{μ_K}(r) (Theorem 23.1). Restatement of the classical Weil criterion as the spectral floor inf σ(L_K | H_{0,+}) ≥ ½ (Corollary 23.2). A family of modes lying exactly at ½ (Proposition 23.3).
- Every von Mangoldt atom is load-bearing at the sharp constant (Theorem 24.1). The same holds for the nondivisible theta channel and the central crossing region (§24). Exact theta–divisor lift (Proposition 24.2).

- Using the compactness and core properties (C_L) proved by CCM (§7): cofinal summability at fixed L (Theorem 7.4), the selected continuum transform (Corollary 7.5), identification of the fixed-L sum (Theorem 7.6), the uniform Weyl bound (Theorem 8.1), and the corollary that the new-mode shell is not independent (Corollary 8.2).
- The sup bound (14.4) in §14, from CCM (7.8) and the proof of Lemma 7.3.

## Open

- Gate SPG (Problem 17.1), the signed branch selector for the moving vector.
- The all-source sharp gate (Problem 24.3). By Corollary 23.2 it is equivalent to RH.
- Consecutive summability, and the global curvature limit L → ∞.

## Known versus new

The finite Weil matrices, the radical quotient and the rank-one perturbation are taken from CCM (§5 of that paper). The continuous viewpoint comes from Suzuki, the mean-square input from Montgomery–Vaughan, and the Weil criterion from Weil. The Doob–variance identity is a ground-state normalization of Weil's criterion, not a new criterion; analytic equivalents of RH of a related kind are due to Sun. The transport, defect, summability, rigidity, compensation and atomwise statements listed above are new in this paper.

## Numerical content

None. The finite identities of §§4–7 are exact matrix identities that can be checked by direct computation (§10). No theorem depends on numerics.

## Files

- `main.tex` — LaTeX source.
- `cofinal-weil-summability.pdf` — compiled paper, 39 pages.

# `scripts/r6a` — round 6a (P8): nodal criterion for the even Schur complement

Inherits `scripts/r3a/arch_core.py` (symbol `m`, Lévy density `K`, Legendre basis, `Cmat`,
`gamma_matrix`, `pole_matrix`, von Mangoldt weights). Nothing in `r3a`…`r5a` is modified.

| script | what it does | output | time |
|---|---|---|---|
| `r6a_01_nodal.py` | even archimedean eigenvectors `e₁…e₁₅` of `A_∞\|P_T` at `T = log 2` (`N = 18` and `N = 36`) and `T = 0.65`; their **nodes**; the exact one-sided overlaps `J_n(i,j) = ∫_{log n−T}^{T} e_i(z−log n)e_j(z)dz` (Lemma N) for `n = 2,3`; a **node-only sign predictor** (largest nodal cell of the common refinement); cross-check of `−Σ v_n J_n` against the `π_ij` matrix computed from `Cmat`; even spectrum at `N = 60` for the growth law | `r6a_01.json` | ≈ 150 s |
| `r6a_02_rule.py` | accuracy of the node-only rule stratified by `\|J\|`, mass fraction predicted correctly; the **arena bound** `N*(T) ≥ #{k : m((2k+3)π/2T) ≤ 𝖠_T}` from the proved ceiling | `r6a_02.json` | < 2 s |

All numbers are `DIAGNOSTIC` (double-precision Galerkin). The statements proved in
`R155_044` (Chebyshev-system node bound, the log-convexity obstruction to total positivity,
the ceiling `λ_{2k+1} ≤ m((2k+3)π/2T)`, the arena bound) do not depend on these runs.

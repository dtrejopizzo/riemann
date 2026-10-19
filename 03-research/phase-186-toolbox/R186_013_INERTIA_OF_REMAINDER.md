# R186.013 — Inertia of the semilocal Sonin remainder in the window 𝒫_T (S = {∞,2})

Sources: R186_009/011/012, R186_017/099 (term (D3) 2log(1/λ)‖h‖²), R183_030 (window form, basis ξ, h = ½ξ − ξ′), R183_026, CC 2006.13771 (43), (83)–(85).
Scripts (NUMERICAL, scratchpad d9ffd571…): `cvl.py` (cv.py with variable λ and the correction of the c_K term from R186_007 #2), `epsgridl.py`/`egfast.py` (ε at nodes a ∈ (0, log 3], graded toward log 2), `r186_013.py` (Galerkin on 𝒫_T, M = 16/28/40, L²(h) metric, primitive Tate restriction).

## Status

| # | Statement | Label |
|---|---|---|
| 0 | Convention: E_S(h) = W_{∞,2}(h) (form of R183_030 with the prime 2), C_ε(h) := ∫_ℝ c_h(a) ε(e^{\|a\|}) da. Chain at level λ: Son_S^{(λ)} = E_S + 2log(1/λ)‖h‖² + C_{ε^{(λ)}} (D3, R186_017/099); exact with no extra term only at λ = 1 (CC (43)/(85)) | CITED (R186_017/099, CC) |
| 1 | **Archimedean control at λ = 1 (CC exact).** ε_∞'(1⁺) ≈ 22.4 (CC: ≈ 23). Son_∞ = W_∞ + C_{ε_∞} ≥ 0 on 𝒫_T: min = +0.175, +0.047, +0.014 at T = 0.35, 0.45, ½log3 (stable in M). n₋(−C_{ε_∞}\|𝒫_T) = 0, 0, **1** (eigenvalue −0.035): CC's unique direction appears before ½log3 | NUMERICAL |
| 2 | **Archimedean control at λ = ½ without (D3)**: min(W_∞ + C_ε) = −0.075 < 0 at ½log3 ⇒ the chain without the term 2log2‖h‖² is false at λ = ½; with (D3) the minimum is +1.31 > 0. Confirms R186_017/099 independently | NUMERICAL |
| 3 | **λ = 1, S = {∞,2}: ε_S is not computable with this Galerkin method.** A_S^{(λ=1)} has two eigenvalues approaching ±1 as K grows: (K=6) −1.016, 0.979; (K=8) −1.0008, 0.9933; (K=10) 0.998, −0.9953. The weights λ_n²/(1−λ_n²) are ~10²–10³ and change sign under truncation (λ = −1.0008 gives weight −273). Numerical ε_S^{(1)} ≈ −5…−12 in the window, with no +β₁log peak at log 2 as predicted by L2_S: **not converged**, discarded as data | NUMERICAL (negative for the computation) |
| 3′ | Structural consequence: the gap G of R186_009 (λ₁² < 1) is **marginal or fails** at λ = 1 for S = {∞,2}. If ‖A_S^{(1)}‖ = 1 (supremum not attained, or eigenvalue ±1), Π_S ceases to be a Riesz projection with a gap, and L2_S/(M) at λ = 1 are left without a foundation | OPEN (new, decisive question) |
| 4 | **λ = ½ (with D3): count of the log-singular remainder.** n₋(−C_{ε_S^{(½)}}\|𝒫_T), M = 16/28/40: T = 0.35: 1/1/2; T = 0.45: 4/7/10; T = ½log3: 4/9/12. Grows with M once 2T > log 2 (eigenvalues −7e-3 … −1e-4). Archimedean λ = ½: 0 at all three T | NUMERICAL |
| 5 | n₋(−C_{ε_S}\|𝒫_T) = ∞ for ½log2 < T ≤ ½log3 (λ = ½): the peak β₁log(1/\|a−log2\|) generates an anti-diagonal block between J₁ = (−T, T−log2) and J₂ = (−T+log2, T) (disjoint for T < log 2) with singular values ≍ 1/n, while the diagonal part (a ≈ 0, symbol ~ s^{−2}) decays ≍ 1/n²; [[D₁,B],[B*,D₂]] with σ_n(B) ≫ √(d_n d_n′) has infinitely many negative eigenvalues | ARGUED |
| 6 | Correction: "n₋(−C_ε) < ∞ by compactness" is **false** as a piece of reasoning: compactness only gives #{eigenvalues < −δ} < ∞ ∀δ > 0. The valid bound is n₋(E_S\|𝒫_T) ≤ n_{−δ}(remainder) + (directions of Son below δ), not n₋(E_S) ≤ n₋(remainder) finite | PROVED (elementary) |
| 7 | n₋(E_S\|𝒫_T) ≤ n₋(remainder) where remainder := E_S − Son_S (Son_S ≥ 0) | PROVED (trivial; with n₋(remainder) = ∞ for λ = ½ since it includes −2log2·I: no content) |
| 8 | **Sharp test** (h* = minimizer of E_S on 𝒫_{½log3}, E_S(h*) = 9.54e-4‖h*‖², reproduces the certified gap 9.5e-4): λ = ½: ∫c_{h*}ε_S = −0.1425, Son(h*) = 9.5e-4 + 1.386 − 0.1425 = +1.245 > 0 ✓ (slack, not sharp). λ = 1 (not converged): ∫c_{h*}ε_S = +0.597 ≥ −9.5e-4 ✓, but the data are invalid by (3). min Son over all of 𝒫_T > 0 at both levels | NUMERICAL |
| 9 | Pointwise symbol check ρ_S = θ + ε̂_S ≥ 0: not a window statement (only σ̌ on (−2T,2T) counts, R183_022 §1); ε̂ truncated to the window: archimedean λ = 1 gives 3.01 at s = 0 < 6.35 = −θ(0). The correct check is min Son\|𝒫_T ≥ 0, done in (1),(2),(8) | PROVED (reading) / NUMERICAL |
| 10 | T ∈ (½log3, ½log5]: E_S with S = {∞,2} is **not** the window form (missing Λ(3)/√3 c_h(log3) and Λ(4)); S ⊇ {2,3} is needed, whose ε_S is only ARGUED (R186_012 S3). It is not extended | — |

## Verdict

1. At the CC level (λ = 1) the archimedean accounting closes: Son_∞ ≥ 0 on 𝒫_T and the remainder has exactly CC's single negative direction (n₋ = 1 at ½log3), which Son_∞ absorbs with margin 0.014.
2. At level λ = 1 the semilocal {∞,2} version **cannot currently be computed nor, for now, grounded**: A_S^{(1)} has eigenvalues numerically stuck to ±1, so that the Halmos gap (R186_009 G) and with it L2_S/(M) at λ = 1 are in doubt. This is the main finding and a precise OPEN question: is ‖PF_SP‖ < 1 at λ = 1?
3. At λ = ½ (where the gap is clear, λ₁ ≈ 0.986) the chain with (D3) is consistent with the certified window (min Son > 0, the test at h* passes with slack); the log-singular remainder has n₋ growing with resolution (ARGUED = ∞) once 2T > log 2, against 0 for the archimedean case. The positive part of the semilocal Sonin space thus absorbs infinitely many small directions (|μ| ≲ 7e-3) plus the constant 2log2. Within the window this is free (E_S ≥ 0 by thm:C); for all T it is exactly the density requirement of R183_031/R185_008, with no progress.

## Audit notes

- The normalization of W_∞ in r183_030 is validated because minE = 9.54e-4 at ½log3 reproduces the certified gap and ε_∞'(1⁺) ≈ 22.4 reproduces CC's ≈ 23 at λ = 1.
- The identification "u-model with P = (0,λ], kernel 2cos2πux" ↔ "CC with [−λ,λ]" rests on (1)–(2); if the λ dictionary were different, (2) would detect it as a failure at λ = 1, which does not occur.
- (3) may be a truncation artifact (R186_007 #2: the c_K term of norm ½); the correction G_K = Σc_k − c_{−1} + c_K was applied and the phenomenon persists (K = 6, 8, 10). It was not proved that ‖A_S^{(1)}‖ = 1.
- The counts in (4) depend on M and on the quality of quadrature near the singularity; the ~25% drift of ε_S in K (R186_011) changes values but not the growth pattern in M; the claim n₋ = ∞ is ARGUED, not NUMERICAL.
- The test (8) at λ = ½ is not sharp: the constant 2log2 ≈ 1.39 dominates. It is not presented as a fine confirmation.

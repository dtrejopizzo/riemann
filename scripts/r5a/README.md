# scripts/r5a — round 5a of phase 155 (`R155_039`)

All `DIAGNOSTIC` unless the report says otherwise; double precision, Galerkin, no interval
arithmetic. They reuse `scripts/r3a/arch_core.py` verbatim. Total runtime ≈ 4 min.

| script | what it does | runtime | output |
|---|---|---|---|
| `r5a_01_bs.py` | Birman–Schwinger for (H1): `M_±` in the Legendre/spherical-Bessel symbol representation, `τ₀`, `∫₀^{τ₀}(−m)`, `c(T) = C₀ + Ktail(2T)` and its zero, `λ_min(M₊)`, `tr M₋`, `tr(M₊^{−1}M₋)`, Prop NC for comparison; cross-checks `M₊ − M₋` against `arch_core.gamma_matrix` (rel. `1.1·10⁻²`, quadrature level) | ≈ 150 s | `r5a_01.json` |
| `r5a_02_nodal.py` | even archimedean eigenfunctions at `log 2, 0.62, 0.65`; nodes of `F*` and `e₃`; per-prime atoms of `π₁₁, π₁₃, π₃₃`; verifies Lemma N pointwise against the matrix entries | ≈ 100 s | `r5a_02.json` |
| `r5a_03_scan.py` | scans `I(a) = ⟨Re(R_Tτ_aR_T)F*,e₃⟩` over `a ∈ (0,2T)`, locates its zeros, and tests whether `{log 2, log 3}` straddle one | ≈ 150 s | `r5a_03.json` |
| `r5a_04_lower.py` | checks `φ(τ₀²) = −C₀` to `1.2·10⁻¹⁰` and tabulates Theorem J's lower bound `⌈2Tτ₀/π⌉ − 1` against the computed counts | < 1 s | `r5a_04.json` |

Caveat: `λ_min(M₊)` and every `n₋` here are Galerkin values, hence **upper** bounds on the truth;
they are used only to *refute* the Birman–Schwinger route (a large BS bound at `N = 18` can only
grow as the true `λ_min(M₊)` falls). Theorem J and Lemma N are proved independently of them.

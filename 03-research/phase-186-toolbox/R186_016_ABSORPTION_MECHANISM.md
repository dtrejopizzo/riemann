# R186.016 — Absorption mechanism: attempt at Theorem A and chain consistency test

Chain from R186.009/010/012/014 (+ revisions 095–098). S = {∞,2}, λ = ½ unless stated otherwise. Scripts (scratchpad, not versioned): `r186_013.py` (inertia + test at h*), `r186_016.py` (family W + tC), with Legendre basis from `r183_030_inertia.py` (h = ξ/2 − ξ′, L²(h) metric, a Tate constraint `cp`), grids `epsgrid_A_3000_8.npz` (ε_∞, λ=½), `epsgridL0.5_S_4000_10.npz` (ε_S, λ=½), `epsgridL1_A_3000_8.npz` (ε_∞, λ=1), all at |a| ≤ 1.0981 = 2·½log3.

## Status

| # | Statement | Label |
|---|---|---|
| F1 | ∫_{−δ}^{δ} log(δ/\|t\|) e^{−ist} dt = 2 Si(δs)/s (value 2δ at s = 0, ~ π/\|s\| at high frequency) | PROVED |
| F2 | Singular part of κ̂_S (symmetrized): Σ_j β_j · 2cos(s j log2) · 2Si(δ_j s)/s + (transform of a bounded function), δ_j ≍ 2^{−j}; at s = 0 its total mass is Σ 4β_jδ_j = 4b Σ 2^{−j/2}(1−2^{−j}) ≈ 1.35 (δ_j = 2^{−j}); only j = 1 is visible in the window T ≤ ½log3: 4β₁·½ = 0.255 | PROVED (F1 + L2_S); numerical value NUMERICAL |
| SI | Symbol identity ρ_S = m − √2log2 cos(s log2) + ε̂_S as an identity of forms in 𝒫_T | PROVED **only modulo the normalization dictionary** (MAJOR-1 of R186.098, not written); see C1 |
| **C1** | **Consistency test Son_S ≥ 0 in the window normalization: FAILS.** With W from r183_030 (symbol m in the convention (1/2π)∫\|ĥ\|²) and C = ∫c_h ε: min eig (W + C) in 𝒫_{½log3} = **−0.150** (S, λ=½), **−0.073** (∞, λ=½), +0.014 (∞, λ=1). Son_S := E_S + ∫c_hε_S is a trace ≥ 0: it cannot be negative | NUMERICAL (stable at M = 16, 20, 24) |
| C2 | 2π discrepancy: R183_026 Prop 2.1 uses σ_Son = m/2π + ε̂, while the window uses symbol m with the same (1/2π)∫\|ĥ\|². One of the two conventions is off by 2π, or (84) is missing a λ-dependent term | OPEN (flagged; it is exactly MAJOR-1 of R186.098) |
| C3 | ε̂_∞ truncated to \|a\| < 2T (the only thing the window sees), λ=½: 1.64 (s=0), 0.36 (s=2), −0.80 (s=4), −0.03 (6.29), −0.20 (10); ε̂_S truncated: 2.30, 0.45, −1.20, 0.00, −0.23. κ̂_S,trunc(0) = 0.67 | NUMERICAL |
| C4 | Pointwise test ρ_S(0) = m(0) − √2log2 + ε̂_S(0): with ε̂ truncated gives −5.37 − 0.98 + 2.30 < 0; inconclusive (the window does not see the pointwise symbol, only the form) — the significant test is C1 | NUMERICAL / inconclusive |
| A(i) | **n₋(−C_{ε_S}\|𝒫_T) ≤ 1 with a low-frequency eigenvector: NO-GO in this form.** Archimedean (λ=½): n₋(−C_{ε_∞}) = 0 at T = ½log2·…·½log3 (−C_{ε_∞} ≥ 0, spectrum in [2e-4, 0.17]): the archimedean remainder is **positive** in the L²(h) metric (the negative CC direction lives in the ξ metric, R183_026). Semilocal: n₋ = 4 (M=16) → 7 (M=24) at T = ½log3, eigenvalues ≥ −0.007, increasing with M: oscillating modes of κ_S (F2), not a low prolate mode | NUMERICAL; Weyl useless (gap of −C_{ε_∞} ≈ 2e-4) |
| A(ii) | Absorption in v_T and reproduction of the 9.5e-4 certificate | **NOT REPRODUCED**: at h* (certified minimizer, E_S(h*) = 1.0e-3): ∫c_{h*}ε_S = −0.142, so Son_S(h*) = −0.141 < 0 in the convention E = Son − ∫cε; the balance is two orders larger than the gap and with an impossible sign | NUMERICAL |

**Verdict.** There is no sign contact. The chain E_S = Son_S − ∫c_hε_S, implemented in the window normalization (that of the ½log3 certificate), **violates Son_S ≥ 0** in 𝒫_{½log3} by 0.15 (and the pure archimedean one by 0.07 at λ=½), which is incompatible with Son_S being a positive trace. Before any absorption theorem can be stated, the CC dictionary (84) ↔ window Weil form must be written (2π factor from C2 and a possible log λ term / λ-dependence: the minimum changes from −0.073 to +0.014 when going from λ=½ to λ=1 without changing W, which shows that the W side of (84) must depend on λ, or that the window is not the W form of (84)). Theorem A, as formulated, is NO-GO: the archimedean remainder has no negative direction in L²(h), and the semilocal negatives are high-frequency (dyadic oscillation of κ_S), not rank one.

## 1. Transforms (PROVED)

F1: 2∫_0^δ log(δ/t)cos(st)dt = 2Si(δs)/s (integration by parts: ∫_0^δ log(δ/t)cos(st)dt = (1/s)∫_0^δ sin(st)/t dt). At ρ = e^x, near x = j log2, |ρ − 2^j| = 2^j|x − jlog2|(1+O(x−jlog2)), so β_j log⁺(1/|ρ−2^j|) = β_j log(δ_j/|x−jlog2|) + O(1) for |x − jlog2| < δ_j = 2^{−j}. Symmetrizing x ↦ |x| produces the factor 2cos(s j log2) (F2). Consequence: the symbol of −C_{κ_S} is −Σ_j 4β_j cos(sjlog2)Si(δ_js)/s + O_{L¹}: it oscillates with the dyadic frequencies and decays like π/|s|; it has infinitely many sign changes, so −C_{κ_S} restricted to L²(I_T) is indefinite with negative eigenvalues accumulating at 0 (compatible with HS: yes; "finite negative index" only holds when counting eigenvalues < −δ).

Comparison with the prime comb in θ: −√2log2·cos(s log2) (coefficient 0.98, no decay) versus −4β₁cos(s log2)Si(s/2)/s (≤ 0.255 at s = 0, ~0.40/|s| afterward): same phase, different structure; the logarithmic mass cannot pay for the comb at high frequency, and at s = 0 it pays at most 0.255 + (bounded part) versus 0.98. Therefore the payment for the comb in Son_S, if it exists, is made by the bounded part of κ_S (the Neumann terms m ≥ 1 and the regular part of G₀), not the singularities — NUMERICAL: κ̂_S,trunc(0) = 0.67 < 0.98.

## 2. Inertia (NUMERICAL)

Outputs of r186_013 (λ=½, L²(h) metric, cp constraint):

| grid | T | M | n₋(E_S) | min E_S | n₋(−C_ε) | min(W+C) | ∫c_{h*}ε |
|---|---|---|---|---|---|---|---|
| ε_S | 0.3466 | 24 | 0 | 0.549 | 1 (−1e-4) | +0.486 | −0.062 |
| ε_S | 0.45 | 24 | 0 | 0.068 | 6 (≥ −0.0065) | −0.034 | −0.101 |
| ε_S | 0.5493 | 24 | 0 | 9.9e-4 | 7 (≥ −0.0069) | −0.150 | −0.142 |
| ε_∞ | 0.5493 | 24 | 0 | 0.085 | 0 | −0.074 | −0.157 |
| ε_∞ (λ=1) | 0.5493 | 16 | 0 | 0.085 | 1 (−0.032) | +0.014 | −0.039 |

min E_S at ½log3 = 9.9e-4 reproduces the certificate (consistency of the W side). The Son side does not.

## 3. What would make the window-by-window argument analytic

Necessary statement (OPEN): **(D) dictionary**: there exists a constant c_λ and a form L_λ (log λ term) such that for h ∈ 𝒫_T, Tr ϑ(h*h̃)Π_S(λ) = E_S^{win}(h) + c_λ∫c_h ε_S + L_λ(h), with E_S^{win} the certificate's form. Given (D): **(Abs)** for all h ∈ 𝒫_T, c_λ∫c_hε_S + L_λ(h) ≤ Tr ϑ(h*h̃)Π_S(λ) with an explicit gap. Without (D), any "Theorem A" compares quantities in different normalizations. With (D), the analytic route would be: estimate Tr ϑΠ_S from below using the Halmos data (Π_S = Q₁Q₂Q₁ − Σλ_n²|ζ_n⟩⟨ζ_n|, R186.009 D) — a trace lower bound that does not go through E_S (to avoid circularity) — and the ε term via F2 + an L^p bound on the bounded part.

## Audit notes

1. C1 is the central finding: check whether W from r183_030 is exactly W_S of (84)_S (2π factor; does it include the pole/ log π / log λ term?). If the error is in R183_026 Prop 2.1 (m/2π), that proposition and its consequence "ε̂ > 0 at |s| < 6.29" must be re-audited.
2. The ε grids are truncated to |a| ≤ 1.098; the form in 𝒫_{½log3} only sees that range, so C1 does not depend on the tail.
3. The growth of n₋(−C_{ε_S}) with M may be resolution of the log singularity at a = log2 (400-node quadrature); it does not affect C1 (min(W+C) stable to 1e-3 between M = 16, 20, 24).
4. Son_S(v) was not computed from the Halmos spectral data (s2.py) — that is the independent check that decides C1 vs. grid error; it remains pending.

## For Paper 46

Nothing citable as progress. The only usable items: F1/F2 (structure of the symbol of the logarithmic part, dyadic oscillation with π/|s| decay) and the warning that the identity E_S = Son_S − ∫c_hε_S is not verifiable without the normalization dictionary. Do not mention "absorption" or "sign contact".

## Note (R186_017)

* C1 RESOLVED: the term 2·log(1/λ)·‖h‖² (scaling law (Λ)) was missing; with it Son_S(h*) = +1.245. The C1 conclusion and the "2π error" are withdrawn. The chain E_S = Son_S − ∫c_hε_S as it stood only holds at λ=1; at the λ level: Son_S^{(λ)} = E_S + 2log(1/λ)‖h‖² + ∫c_hε_S^{(λ)}.

## Note (R186_099)

* Withdraw A(i) ("−C_{ε_∞} ≥ 0, n₋=0"): only at λ=½ and due to the term 2log2‖h‖²; at λ=1, n₋ = 1 (−0.032) at ½log3, consistent with CC/R183_026. A(ii) is superseded by R186_017 (Son_S(h*) = +1.245 at λ=½). The absorption question reopens at λ=1.

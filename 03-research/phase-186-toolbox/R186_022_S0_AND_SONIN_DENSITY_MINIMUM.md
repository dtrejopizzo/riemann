# R186_022 — s₀ and the "Sonin density minimum": the wave-packet-at-s* hypothesis does not survive

Script: scratchpad `r022.py` (uses `r021_vec_24.npy`, `g1_A_5_8_1_0.npz`, M = 24).

## Status

- **NO-GO (NUMERICAL)** for the hypothesis "s₀ = window wave packet at a fixed minimum/zero s* ≈ 7 of a Sonin density ρ_∞ ≥ 0".
- **PROVED (elementary)**: in 𝒫_T only |a| < 2T of ε enters C(h) = ∫c_h ε, so the compression P_T ρ(D) P_T does not determine a unique symbol; the natural representative is ρ_T(s) := m(s) + ε̂_T(s), ε̂_T(s) = ∫_{|a|<2T} ε(e^{|a|}) e^{isa} da. Son_∞(h) = (1/2π)∫ρ_T|ĥ|² exactly.
- **NUMERICAL**: ρ_T **is not ≥ 0**. At T = ½log3: ρ_T(0) = −2.360 (m(0) = −5.372, ε̂_T(0) = +3.012); ρ_T(4) = −0.277, ρ_T(5) = −0.199, ρ_T(10) = −0.110; zeros of ρ_T in [0,20]: 0.63, 3.05, 5.82, 8.66, 11.14 (truncation oscillation). The positivity of Son_∞|𝒫_T is a property of the **compressed operator**, not of a pointwise symbol. Hence "λ_min ≈ min_s ρ_∞(s)" is meaningless with ρ_T, and the global density ρ_∞ (ε over all a) is not computable from the record (ε only up to log 3) — **OPEN**, and moreover irrelevant to 𝒫_T.
- **NUMERICAL (real structure of s₀)**: broad spectrum (|ŝ₀|² appreciable for s ∈ [3,12]), with a peak that **drifts with T** as ≈ 4/T:

| T | peak s | peak·T | RMS freq. | Son_∞ | E_∞ | C_∞ | Son⁺ / Son⁻ | Re c_{s₀}(log 2) | cos(peak·log 2) |
|---|---|---|---|---|---|---|---|---|---|
| ½log2 | 11.05 | 3.83 | 11.92 | 0.161 | 0.530 | −0.369 | 0.204 / −0.043 | 0 | +0.19 |
| 0.40 | 9.80 | 3.92 | 10.53 | 0.081 | 0.410 | −0.329 | 0.118 / −0.038 | +0.088 | +0.87 |
| 0.45 | 8.91 | 4.01 | 9.51 | 0.042 | 0.313 | −0.271 | 0.087 / −0.045 | +0.162 | +0.99 |
| 0.50 | 8.19 | 4.10 | 8.71 | 0.023 | 0.229 | −0.206 | 0.074 / −0.051 | +0.180 | +0.82 |
| ½log3 | 7.60 | 4.18 | 8.07 | 0.0127 | 0.153 | −0.140 | 0.066 / −0.054 | +0.145 | +0.53 |

 (Son_∞ by spectral quadrature 0.0127 vs 0.0140 matrix-based in R186_021: quadrature agreement; E_∞, C_∞ match R186_021 to 3 digits.)
- Conclusion: s₀ is a **geometric window mode** (≈ third even mode, frequency ∝ 1/T), not a packet anchored at an arithmetic-archimedean frequency. Its small Sonin value comes from **cancellation** between regions ρ_T > 0 and ρ_T < 0 (Son⁺ ≈ 0.066, Son⁻ ≈ −0.054 at ½log3), not from a spectral gap.
- Requested numbers (with the "natural" s* = peak of |ŝ₀|² at ½log3): s* ≈ 7.60; ρ_{T}(s*) ≈ +0.13 (ρ_T(7) = +0.176, ρ_T(8) = +0.104; not zero); m(s*) ≈ +0.19 (m(7) = +0.107, zero of m at s_m ≈ 6.29); cos(s* log 2) = +0.527 (cos(7 log 2) = +0.139). Re c_{s₀}(log 2) = +0.145 > 0 confirmed (the positive autocorrelation at log 2 is what makes the prime 2 eat into E_∞(s₀)).
- **Predictive CONJECTURE of item 3: withdrawn** (it presupposes ρ_∞(s*) = 0 at a fixed s*; the data show drift ∝ 1/T). What does survive (NUMERICAL): on [½log2, ½log3] the peak of s₀ crosses the region s ∈ [7.6, 11] where cos(s log 2) > 0, and the cost of the prime 2 at s₀ is maximal near T ≈ 0.45–0.50 (cos ≈ 0.99–0.82), which explains the turn in C/Son from R186_021.

## Audit notes

1. Is ε̂_T the correct symbol? Any extension of ε outside |a| < 2T gives the same form on 𝒫_T; the non-positivity claim is only about ρ_T. There may exist an extension with symbol ≥ 0 (e.g. CC's global ε, if R183_021 Thm 3.1 is correct); that would not rescue the hypothesis, because the peak of s₀ drifts with T.
2. Dependence on M = 24 and on the `g1_A_5_8_1_0` grid: check with M = 20, 28 (`r021_vec_{20,28}.npy`).
3. Normalization: s₀ unit-normalized in L²(h), h = ½ξ − ξ′; spectral mass 0.9995 (tail outside [0,40] negligible).
4. Prime-term convention: E_S − E_∞ = −2Λ(2)/√2 · c(log 2) in `build`; with c = 0.145 this gives −0.142, consistent with ΔC − ΔSon ≈ 0.15 from R186_017.

## For Paper 47

Do not integrate as a theorem. As an observation (NUMERICAL): the fragile direction of the archimedean Sonin form on 𝒫_T is a window mode of frequency ≈ 4/T, whose autocorrelation at log 2 is positive for T ∈ [0.40, ½log3]; the truncated symbol m + ε̂_T changes sign, so any positivity argument for Son via a pointwise symbol is ruled out in the window (NO-GO for that class of method).

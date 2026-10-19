# MORI15_EXTREMAL_001 — Mori's certified bottom at μ = 15 in the coordinates of the exterior form (NUMÉRICO)

Phase 199.
**Everything quantitative in this memo is NUMÉRICO** (ball arithmetic, 400–720 bits, on Mori's released matrices); no new
certification. Zero data (mpmath `zetazero`) is used in §5 **only as a consistency check** of the computed vector, never as
an input to any construction or claim.

**Outcome in one line.** The bottom eigenvector of Mori's μ = 15 compressed form is a smooth super-Gaussian bump of width
σ ≈ 0.21 (even sector; x·bump in the odd sector), whose Möbius inverse f* = E⁻¹g* is **Fourier-self-dual**
(f̂* = f* on the band to the numerical floor): f* = 1.106 ψ₀ − 1.822 ψ₄ + 3.3·10⁻⁵ ψ₈ + … lies in span{ψ_{4j}} (Guo's
F_{λ,m}-type class), the anti-self-dual prolates ψ₂, ψ₆, … carry nothing (|a_{4j+2}| ≤ 6·10⁻³⁸). The O(1) cancellation
is Γ_ℝ (−5.372) + Lévy (+3.916) + pole (+1.519) − primes (0.063) = 0 in the even sector and Γ_ℝ-Lévy (−0.304) + pole
(−0.035) + [−primes] (+0.340) = 0 in the odd sector (there the prime 2 is the positive carrier). The leakage of f* is
ℓ ≈ (4.4–8.5)·10⁻⁷⁰, 81 % of it a₄²(1−λ₄); W_T(g*) = 4.763·10⁻⁷⁰ = 4.08·(1−λ₄) = (0.56–1.09)·ℓ. In the zero picture (check
only) the vector is tuned so that Fg* vanishes at every zero below t* ≈ 185 and the whole value of W_T sits on the zeros
above t*, where |Fg*(γ)| equals the generic level of a rough floor component (Legendre modes j ≥ 240, energy ≈ 3·10⁻⁷¹).
No sign is obtained; no new theorem. Two corrections to earlier memos (K_001 §1, PATTERN κ) and one new structural datum
(self-duality) are recorded. (★★) OPEN; row D OPEN.

## 0. Corpus / index check and why this is not a retry
- Index read: README l.449 (PATTERN_001, κ-band), l.450 (MECH_001, Möbius bijection Prop 3.1), l.452 (A_001 half-line
  identity), l.459 (K_001: repair of ψ₀ along ψ₂, index-4 reading), l.465 (T_001 sectors), U_001 (𝔉_μ-sectors on the
  carrier), AUDIT_ZENODO_FRONTIER §B1 (Mori VIII: conventions, matrices, margins), BB_001 (Identity 1), B_001
  Lemma 3.1 (ã / R_Λ split), D_001 Thm 2.1, H_001 Thm H.4 (W⁻), Q_001 (Q.2).
- Why new: no entry examines the certified extremal vector itself. All previous evaluations of the exterior form were on
  model data (deep bumps, prolates without constraints, radical vectors). This memo evaluates every piece of the framework on
  the actual bottom vector of Mori's 1664-mode form. It claims no sign and launches no construction.

## 1. Sources, conventions, what was computed
- Mori VIII code v1.6.2 (`prolate-weil-bounds/certificate-VIII`, SHA-pinned) and data (zenodo 23281176), restored and
  verified in the scratchpad (AUDIT §B1-run). Matrices used: `m15n1664p3328q224_p{0,1}_{A,J}.json.gz` (Arb balls, 3328
  bits; midpoints extracted to 200 digits). Per parity d = 832 Legendre modes φ_j = √((2j+1)/2L) P_j(x/L), L = T = ½log 15.
- Mori's form Q(f) = (1/π)∫₀^∞ a(t)|Ff|² dt + 2(∫f cosh ½x)² − 2(∫f sinh ½x)² − 2Σ_{n<15}Λ(n)n^{−½}c_f(log n),
  a(t) = Re ψ(¼+it/2) − log π, c_f(u) = ∫f(x)f(x+u)dx: this is **W_T with the pole term**, T = ½log15 (AUDIT §0). In his
  blocks A = γI − C_p (γ = 74/16, C_p the prime comb) and J = (arch_Ω − γ·band) + pole + U; so **A + J = Q compressed to
  the Legendre span up to the tail (1/π)∫_Ω^∞(a−γ)|F|² (Ω = 736, PSD, ≈ +2·10⁻⁷¹ on g*, §3) and the rank-one U
  (≈ 10⁻⁸⁰⁰)**. Checked: vᵀAv = γ − Σ_n 2Λ(n)n^{−½}c_{g*}(log n) and vᵀJv = arch_Ω(g*) − γ + pole(g*) both to 50 digits
  by independent quadrature (§3), which fixes the normalisation.
- Scripts (`MORI15_EXTREMAL_001_*.py`, run with python-flint 0.9.0 / mpmath 1.3.0 in the scratchpad venv; paths point to
  the scratchpad): `extract_mid` (midpoints), `eigvec` (subspace inverse iteration in arb, 720 bits, midpoint recentering),
  `pieces` (all pieces of Q on v*, 420 bits, 1700-node Gauss–Legendre, t-panels as Mori's), `prolate_mobius` /
  `prolate_M28` (Möbius inverse, prolates at c = 30π by the Legendre tridiagonal, minimal gauge in a polynomial family,
  exterior datum), `zeros_check(_hi)` (Fg* at zeros, check only), `shape_np` / `anatomy_np` (double-precision shape and
  Lévy split). Derived data in `MORI15_EXTREMAL_001_data/` (eigenvectors to 120 digits, pieces, prolate output, zero logs).
- Numerical pitfalls met and fixed (recorded for reuse): the Legendre three-term recurrence must be run on exact midpoints
  (ball radii grow like 2.4ⁿ near |x| = 1 and give radius 10⁴⁷⁸ at n = 1663 otherwise); the gauge part of f is two-sided
  (no factor 2); the gauge polynomial family must be large enough (M = 16 leaves a 10⁻³³ floor, M = 28 reaches the
  Galerkin floor 10⁻³⁸).

## 2. Task 1 — bottom eigenvectors and Rayleigh quotients
Subspace inverse iteration (6 vectors, 10 iterations) on G = (A+J) symmetrised, parity by parity.

| sector | λ₁ (Galerkin, A+J) | λ₂ | λ₃ | λ₄ | λ₅ | λ₆ | certified Schur margin (Mori Table 2) |
|---|---|---|---|---|---|---|---|
| even | **4.76346613556556·10⁻⁷⁰** | 3.5915·10⁻⁶² | 6.1427·10⁻⁵⁵ | 2.8756·10⁻⁴⁸ | 2.7034·10⁻⁴² | 1.9392·10⁻³⁶ | 2.3979·10⁻⁷⁰ |
| odd | **6.10904110104·10⁻⁶⁶** | 1.5285·10⁻⁵⁸ | 1.8376·10⁻⁵¹ | 2.6808·10⁻⁴⁵ | 3.0547·10⁻³⁹ | 6.8377·10⁻³⁴ | 3.9458·10⁻⁶⁶ |

Residual ‖Gv − λv‖ = 2.7·10⁻¹⁴⁸ (even). The Galerkin bottom is an upper bound for the true bottom of the compressed
form; the certified margin (a Schur complement of the bounded-comparison transfer) is below it by a factor 1.99 (even) and
1.55 (odd). Successive eigenvalues are separated by 10⁶–10⁸, not by the prolate ratios 64c²/((k+1)(k+2)) ≈ 2·10⁴.

**Shape of g* (even), ‖g*‖ = 1.** A single super-Gaussian bump: g*(0) = −1.59846, ∫g* = −0.86677, ⟨x²⟩ = 0.043507
(σ = 0.2086), g*/g*(0) = 0.0557 at x = 0.5, 2.1·10⁻⁶ at 0.9, 6.9·10⁻¹⁷ at 1.3 (faster than Gaussian in the tail), no sign
change. Edge: g*(T) = −1.4208·10⁻³⁴, g*(T−10⁻³) = −1.7·10⁻³³, g*(T−0.05) = −1.3·10⁻²³ (a tiny boundary layer, not a
monotone decay). Legendre amplitudes |v_j|: 0.527 (j=0), 0.145 (10), 1.4·10⁻⁴ (20), 1.9·10⁻⁷ (40), 7.7·10⁻¹² (60),
4.6·10⁻¹⁹ (100), 1.5·10⁻²⁸ (160), 2.1·10⁻³³ (200), then a **flat floor ≈ 10⁻³⁷ for j ≥ 240** (energy in modes ≥ 300:
2.6·10⁻⁷¹; ≥ 600: 4.5·10⁻⁷²). Fourier side: Fg*(t) = −0.867, −0.497, −0.0758, −4.6·10⁻⁴, +1.9·10⁻³, 1.1·10⁻⁴, 8.9·10⁻⁸,
−1.7·10⁻¹³, 1.4·10⁻²⁴ at t = 0, 5, 10, 14, 16, 20, 30, 50, 100; spectral energy per panel (1/π)∫|F|²: 0.119 [0,½],
0.117 [½,1], 0.216 [1,2], 0.321 [2,4], 0.214 [4,8], 0.0129 [8,16], 1.4·10⁻⁶ [16,32], 3.5·10⁻¹⁶ [32,64], 1.0·10⁻³² [64,128],
6.4·10⁻⁶⁰ [128,192], **9.8·10⁻⁷¹ [192,256], 4.1·10⁻⁷¹ [256,320], 2.2·10⁻⁷¹, 1.0·10⁻⁷¹, 6.3·10⁻⁷², 6.4·10⁻⁷², 3.3·10⁻⁷²,
2.2·10⁻⁷², 1.0·10⁻⁷² [704,736]**, 2.3·10⁻⁷² [736,800], 5.4·10⁻⁷² [800,1000], 6.0·10⁻⁷² [1000,1500], 4.2·10⁻⁷² [1500,2000]
(beyond 2000 the 1700-node x-quadrature no longer resolves cos(xt); not used). So 99.99994 % of the energy is below t = 16
and a rough floor of total energy ≈ 3·10⁻⁷¹ sits above t ≈ 180.

**Shape of g* (odd).** g ≈ x·(bump): |g| peaks at |x| = 0.234 (1.380), no interior zero, |g| < 10⁻⁴ for |x| > 0.8;
∫g sinh(x/2) = −0.1327873; g(T) = −1.5·10⁻³²; mode floor ≈ 10⁻³⁵ for j ≥ 240 (energy in modes ≥ 301: 2.1·10⁻⁶⁷).

**Möbius inverse (A Prop 3.1 / MECH Prop 3.1, PROVED) applied to g*.** f₁(u) = Σ_{m≤λ/u} μ(m)(mu)^{−½} g*(log mu) on
[1/λ, λ], λ = √15 = 3.873: f₁ = 1.5257 at u = 1/λ⁺, 2.122 at 1.5/λ, 1.701 at 2/λ, −0.780 at 3/λ, −0.722 at 5/λ, −8.5·10⁻⁴ at
8/λ, −2.3·10⁻⁷ at 10/λ, −8.9·10⁻¹³ at 12/λ, −6.0·10⁻²² at 14/λ, −4.6·10⁻³⁴ at 14.99/λ. So **f* lives on u ≲ 1.5 ≪ λ**; it is
O(1) at the gauge boundary 1/λ = 0.258 (so the gauge is not optional: with φ = 0 the jump at 1/λ gives leak = 0.0645).
Jumps at u = λ/m are μ(m)g*(T)/√λ = 7.2·10⁻³⁵. ‖f₁‖²_{[1/λ,λ]} = 2.12193, ∫_{1/λ}^λ f₁ = −0.152217. Minimal-leak gauge
φ = Σβ_i q_i(λu) (even normalised Legendre on [−1/λ,1/λ], constraints f(0) = 0, ∫f = 0; M = 28): β = (0.83373, 0.67679,
−0.06598, 0.00245, −5.4·10⁻⁵, 8.3·10⁻⁷, −9.8·10⁻⁹, …, 3·10⁻³⁴, then ±1.46·10⁻³⁸ floor). ‖f*‖² = 4.54272.

**Exterior datum ρ*(ω) = r*(λω), ω > 1** (direct 400-bit Fourier integral of f*, cross-checked against the prolate series
at ω = 1, 1.05, 1.2, 1.5: agreement to 12 digits): ρ*(1) = −7.215·10⁻³⁵, ρ*(1.002) = −9.0·10⁻³⁶, zero crossings at ω =
1.004, 1.008, 1.012, 1.018, 1.026, 1.034, 1.044, 1.056, 1.068, 1.080, 1.092, 1.106, 1.122, 1.138, 1.154, 1.172, 1.192,
1.212, 1.232, 1.252, …; |ρ*| ≤ 7.2·10⁻³⁵ on [1,1.2], ≤ 1.2·10⁻³⁵ on [1.2,1.5], ≈ 8·10⁻³⁶ on [1.5,4]. The zero spacing follows
the Langer phase c√(ω²−1) of K.2 (predicted spacing π√(ω²−1)/(cω) = 0.0102 at ω = 1.05, 0.0184 at 1.2; measured 0.012,
0.020): **ρ* is the analytic continuation of the dominant prolate ψ₄ beyond the band edge**, amplitude ~10⁻³⁵, i.e. the
square root of the leakage scale. (Values of ρ* below ≈ 10⁻³⁸ are at the Galerkin floor and not meaningful.)

## 3. Task 3 — the pieces of W_T on g* (even sector; 50-digit arb unless marked)
| piece | value | comment |
|---|---|---|
| ‖g*‖² | 1 | |
| A = ∫g e^{x/2} = B = ∫g e^{−x/2} | −0.871492550533 | A = B exactly (even) |
| pole 2AB | **+1.518998531269** | |
| Γ_ℝ constant b_∞‖g‖², b_∞ = ψ(¼) − log π | **−5.372183419** | |
| Lévy energy ∫₀^∞[c(0)−c(v)]·2ν(v)dv, ν = e^{−v/2}/(1−e^{−2v}) | **+3.916389** (interior [0,2L] 2.882673 + exterior 1.033716; double) | |
| archimedean total (1/π)∫₀^Ω a|F|² (= vᵀJv − pole + γ, 50 digits) | **−1.455794761161863487215** | tail (Ω,2000]: +9.3·10⁻⁷¹, beyond: ≈ +4·10⁻⁷¹ (jump-tail estimate) |
| prime comb Σ_n 2Λ(n)n^{−½}c(log n) (= γ − vᵀAv, 50 digits) | **0.063203770107594605** | |
|  n = 2 | 0.0625809102 (c = 0.0638412551) | 99.0 % |
|  n = 3 | 6.2177132·10⁻⁴ (c = 4.9013630·10⁻⁴) | 1.0 % |
|  n = 4 | 1.08473·10⁻⁶ (c = 1.56493·10⁻⁶) | |
|  n = 5 | 3.85162·10⁻⁹ (c = 2.67562·10⁻⁹) | |
|  n = 7 | 2.15397·10⁻¹⁵ (c = 1.46432·10⁻¹⁵) | |
|  n = 8 | 2.17327·10⁻¹⁹ | |
|  n = 9 | 4.84496·10⁻²³ | |
|  n = 11 | 1.24909·10⁻³¹ (c = 8.6383·10⁻³²) | the two contacts new at μ = 15 (11, 13) |
|  n = 13 | 2.21420·10⁻⁴³ (c = 1.5563·10⁻⁴³) | are 10³⁹ and 10²⁷ above W_T, and 10⁻³² below the n = 2 term |
| ∫e^{−|u|/2}c(u)du = (1/2π)∫|F|²/(¼+t²) | 0.669994480662 | ≥ 0 (B_001 Lemma 3.1) |
| Chebyshev main 2∫₁^μ t^{−½}c(log t)dt = pole − previous | 0.849004050608 | |
| R_Λ = primes − Chebyshev main | **−0.785800280500** | Chebyshev remainder form |
| ã-form (1/2π)∫ã|F|², ã = Re ψ(5/4+it/2) − log π | **−0.785800280500** | Q = ã-form − R_Λ (B_001) ✓ |
| **Q = vᵀ(A+J)v** | **4.7634661355655572499·10⁻⁷⁰** | vᵀAv = 4.56179622989240539491 = −vᵀJv to 10⁻⁷⁰ |

All c_{g*}(log n) are **positive** (Gaussian-like autocorrelation of a bump): every prime contact enters with the negative
sign, hierarchically (n = 2 carries 99 %). Near-coincidence lags: c(log 16/15) = 0.9747, c(log 5/4) = 0.7637, c(log 4/3)
= 0.6376, c(log 3/2) = 0.4052, c(log 5/3) = 0.2342, c(log 2) = 0.0638, c(log 5/2) = 0.0064, c(log 7/2) = 3.0·10⁻⁵,
c(log 3) = 4.9·10⁻⁴ — a smooth function of the lag, **no arithmetic structure at the lags log(m/n)** (NUMÉRICO).

Odd sector (50 digits): ∫g sinh(x/2) = −0.132787275547, pole = −0.035264921095, prime comb = **−0.339646593129**
(n = 2: −0.325954265 with c(log 2) = −0.332518803; n = 3: −0.013636227; n = 4: −5.57·10⁻⁵; 5: −3.73·10⁻⁷; 7: −5.5·10⁻¹³; 8:
−8.4·10⁻¹⁷; 9: −2.7·10⁻²⁰; 11: −1.5·10⁻²⁸; 13: −5.6·10⁻⁴⁰), arch_Ω = −0.304381672034, ∫e^{−|u|/2}c = 0.0773263497,
Chebyshev main = −0.1125912707, R_Λ = −0.2270553224, Q = 6.109041101·10⁻⁶⁶.

**Anatomy, and the deep-mode numbers (J_001: −5.372 + 2.264 + 2 + 1.154 = 0.046).** On the even extremal the same four
labels read: Γ_ℝ **−5.3722** + Lévy **+3.9164** + (pole − Chebyshev main = ∫e^{−|u|/2}c) **+0.6700** + (−R_Λ, Chebyshev
remainder) **+0.7858** = 0 (to 10⁻⁵ in double; exactly 4.8·10⁻⁷⁰ in arb). Same signs as J.3's deep mode, different weights
(the Lévy energy of a bump replaces 2.264, the residue-1 cancellation leaves 0.670 instead of 2, the Chebyshev-bias term
is +0.786 instead of Mertens' 2γ = 1.154). The sign-carrying piece is not the pole alone: pole (+1.519) + Lévy (+3.916)
against Γ_ℝ (−5.372), with the comb a 1 % correction. In the odd sector the balance is different: Γ_ℝ+Lévy (−0.304) +
pole (−0.035) + [−comb] (+0.340) = 0 — **the prime 2 is the positive carrier** (c(log 2) < 0 for the x·bump profile).
Reading (ARGUED): the even extremal is a bump whose spectrum (width ≈ 1/σ ≈ 5) sits where a(t) < 0 (|t| < τ₀ = 6.29, R.3);
narrowing it costs the log t growth of a, widening it costs the comb (c(log 2) ↑); the width is set by τ₀ and the comb
only forbids the wide bumps. D_001's Son/𝔅/K_s pieces were not computed (Son needs CC's Π_{1,1} trace; 𝔅 = ‖G‖²
requires ∫g = 0, which fails: ∫g* = −0.867): OPEN here.

## 4. Task 2 — prolate decomposition, leakage, κ
Prolates ψ_k of [−λ,λ] with c = 2πμ = 30π, computed from the Legendre tridiagonal (300 even modes, inverse iteration,
400 bits; λ_k from μ_k = √2β₀/ψ_k(0)). 1−λ₀ = 9.40069·10⁻⁸¹, 1−λ₂ = 2.60802·10⁻⁷⁵, **1−λ₄ = 1.166825·10⁻⁷⁰**, 1−λ₆ =
2.01858·10⁻⁶⁶, 1−λ₈ = 1.80665·10⁻⁶², 1−λ₁₀ = 9.7058·10⁻⁵⁹, 1−λ₁₂ = 3.4257·10⁻⁵⁵ (Fuchs: 9.44·10⁻⁸¹, 1.27·10⁻⁷⁰; the
asymptotic formula is 8 % high at index 4).

**Coefficients of f* (minimal gauge, M = 28), ‖f*‖² = 4.54272:**
a₀ = +1.106365, a₄ = −1.821723, a₈ = +3.3400·10⁻⁵, a₁₂ = −2.4993·10⁻⁹, a₁₆ = +2.3141·10⁻¹², a₂₀ = +2.7388·10⁻¹⁶, a₂₄ =
−2.8832·10⁻¹⁸, a₂₈ = +2.5129·10⁻²¹, a₃₂ = +1.0532·10⁻²³, a₃₆ = −3.576·10⁻²⁶, a₄₀ = −7.14·10⁻²⁹, a₄₄ = +2.06·10⁻³⁰, a₄₈ =
7.1·10⁻³³, …; **every a_{4j+2} (k = 2, 6, 10, …, 58) is ≤ 6.3·10⁻³⁸** (the Galerkin floor). Self-dual mass Σ_{k≡0(4)}a_k² =
4.54272 = ‖f*‖²; anti-self-dual mass 2.3·10⁻⁷¹.

**Self-duality (new, NUMÉRICO).** Since ψ̂_k = (−i)^k√λ_k ψ_k (Slepian–Pollak, CITED) with the standard transform (the 𝔉 of
T_001 Lemma 1.1, self-dual scale λ — **not** U_001's edge-scaled 𝔉_μ), the band part of f̂* equals Σa_k(−1)^{k/2}√λ_k ψ_k;
with a_{4j+2} = 0 this is f* up to O(1−λ_k) ≤ 10⁻⁷⁰ per coefficient. So f̂* = f* + r* with r* the out-of-band datum:
**the extremal is as self-dual as a compactly supported function can be**, and f(0) = 0 ⇒ f̂(0) = 0 automatically; the two
admissibility constraints collapse to one. T Lemma 1.1 then gives Φ_{f̂*} = Φ_{f*}∘R (no polar term), consistent with g*
even. In U_001's language f*_− (standard 𝔉) is at the floor, ‖f_−‖²/‖f‖² ≈ 5·10⁻⁷²; U_001's "f_− ≠ 0 by Paley–Wiener" is
true but f_− is numerically invisible on the extremal.

**Correction to K_001 §1 (K.1b).** The minimal-leak admissible repair of ψ₀ is **not** ψ₀ + αψ₂ (α = −√2): ψ₂ is
anti-self-dual and would break f̂(0) = 0 as f(0) = 0 is imposed. The extremal repairs along **ψ₄**: a₄/a₀ = −1.6466, i.e.
ψ₄(0)/ψ₀(0) = 0.6073 (Hermite limit h₄(0)/h₀(0) = 3/(2√6) = 0.6124), fixed by f(0) = 0 alone. K.4's reading "defect index
4" is confirmed and explained: index 4 is the first self-dual index after ψ₀.

**Leakage.** ℓ = Σa_k²(1−λ_k) + (energy beyond the 81 prolates, weight 1): terms a₄²(1−λ₄) = **3.872·10⁻⁷⁰** (81 %), a₈²:
2.02·10⁻⁷¹, a₂₄²: 9.6·10⁻⁷², a₁₆²: 8.1·10⁻⁷², a₃₂²: 3.1·10⁻⁷², a₁₂²: 2.1·10⁻⁷², a₄₄²: 1.9·10⁻⁷², a₃₆²: 1.8·10⁻⁷², a₂₈²:
1.7·10⁻⁷², a₀²: 1.15·10⁻⁸⁰; Σ_{k≤44} = 4.361·10⁻⁷⁰; floor modes 46–160: +4.3·10⁻⁷¹; beyond: +3.7·10⁻⁷⁰ (floor, upper
bound of this gauge family). So **4.4·10⁻⁷⁰ ≲ ℓ(g*) ≤ 8.45·10⁻⁷⁰** (the lower value is the structured part; the floor
3.7·10⁻⁷⁰ is at the Galerkin resolution and may or may not be physical). Hence
  **κ_emp = W_T(g*)/ℓ(g*) ∈ [0.56, 1.09]**,  W_T(g*)/(1−λ₄) = **4.0824**, W_T/(1−λ₀) = 5.07·10¹⁰, W_T/(1−λ₂) = 1.83·10⁵.
With Fuchs' 1−λ₄ the ratio is 3.75 (PATTERN's κ ≈ 4.6 used Mori V's Galerkin value and Fuchs; the exact prolate defect
moves κ to ≈ 4.1 at μ = 15). The κ-band conjecture is consistent with the data; the natural normalisation is **W_T ≈ 1.2 ×
a₄²(1−λ₄)** with a₄² = 3.32 fixed by f(0) = 0 and ‖g‖ = 1 (NUMÉRICO at μ = 15 only).

## 5. Task 4 — where the e^{4πμ}-size pieces cancel (check with zero data; interpretation ARGUED)
Fg*(γ_n) at the ordinates (70-digit zeros for n ≤ 30, 45-digit for 31–419; the values are far above the zero-location
error): n = 1: −1.14·10⁻⁶⁸, 2: 4.2·10⁻⁶⁷, 3: −3.8·10⁻⁶⁶, 10: 1.3·10⁻⁵⁹, 30: 6.4·10⁻⁴⁸, 50: 1.2·10⁻⁴⁰, 60: 3.3·10⁻³⁸, 70:
8.4·10⁻³⁷, 80: −4.8·10⁻³⁷, 100: 1.5·10⁻³⁶, then a plateau (0.3–1.5)·10⁻³⁶ up to n = 419 (γ = 705). Compared with the
envelope |Fg*(t)| between zeros (1.4·10⁻²⁴ at t = 100; ≈ 1.2·10⁻³⁶ rms on [192,256] from the panel energies): **below
t* ≈ 185 the vector is tuned (|Fg*(γ)| is 10⁻⁴⁴…10⁻¹² of the local envelope); above t* it is not (|Fg*(γ)| ≈ envelope)**.
Partial sums Σ_{n≤N} 2|Fg*(γ_n)|²: 7.5·10⁻⁷² (N = 70), 1.30·10⁻⁷⁰ (80), 1.84·10⁻⁷⁰ (100), 2.40·10⁻⁷⁰ (120), 2.80·10⁻⁷⁰
(150), 3.26·10⁻⁷⁰ (200), 3.67·10⁻⁷⁰ (300), 3.92·10⁻⁷⁰ (419); tail beyond γ = 705 estimated ≈ 1·10⁻⁷⁰; total ≈ 4.9·10⁻⁷⁰
against Q_true(g*) = 4.763·10⁻⁷⁰ + tail(Ω,∞) ≈ 4.8·10⁻⁷⁰ — consistent. Odd sector: tuned to n ≈ 60, plateau ≈ 10⁻³⁴,
partial sums 2.0·10⁻⁷⁰ (60), 1.7·10⁻⁶⁷ (70), 1.85·10⁻⁶⁶ (80), 4.2·10⁻⁶⁶ (200), 5.04·10⁻⁶⁶ (384) vs Q = 6.11·10⁻⁶⁶.

**The mechanism as it appears in the data (ARGUED from NUMÉRICO facts):**
1. The smooth, self-dual part (prolate indices ≤ 44, Legendre modes ≤ 200) makes the O(1) pieces cancel exactly
   (§3) and is tuned so that its transform vanishes at every zero below t*; its own contribution to W_T is nil.
2. The residual is a rough floor component (Legendre j ≥ 240, energy ≈ 3·10⁻⁷¹, spectrum above t ≈ 180), which the form
   sees generically: Σ_{γ>t*}2|F(γ)|² ≈ (1/π)∫_{t*}^∞ log(t/2π)|F|²dt, the archimedean energy of the floor (≈ 7·10⁻⁷⁰ above
   192, the comb and the tuned part bring it to 4.8·10⁻⁷⁰). In exterior coordinates the same residual is the out-of-band
   datum r* (ℓ ≈ (4–8)·10⁻⁷⁰), dominated by the continuation of ψ₄, and W_T(g*) = 𝒲_ext[Z r*] = (0.56–1.09)·‖r*‖².
3. t* ≈ 185 is **not** τ_env = 2πe^{A_T} ≈ 1.3·10⁵ (A_T = 9.94 at μ = 15) and not Ω; it is where the super-exponential
   decay of the smooth spectrum meets the floor. What fixes the floor level (hence the bottom) is not identified here.
4. Identity 1 of BB_001 (Π = Arch − λ) is the split of §3: Arch + pole = 0.0632038 = prime pairing + 4.8·10⁻⁷⁰.
5. Edge value: J = g*(T) = −1.42·10⁻³⁴ and J²·Σ_{γ>0}|ρ|⁻² = J²·0.0230957 = 4.66·10⁻⁷⁰ agree with Q to 2 %. This is
   recorded as an **unexplained numerical coincidence**: the plateau magnitudes are of the order 2J|sin Tγ|/γ but do not
   match it zero by zero (the model sum over γ > 185 gives 2.0·10⁻⁷⁰ against 3.9·10⁻⁷⁰ measured), and |g*| is 10⁻³³ at
   T − 10⁻³, so "the jump J" is a boundary layer, not a clean jump. Do not build on it.
6. Kernel questions: v* is **not** tested against W⁻ (H_001) or H_ζ (Q.2) — not computed, OPEN. v* is nearly
   **self-dual** (§4), and Φ_{f*} is in the radical of W by construction (Guo Lemma 4.4, CITED), as for every admissible f.

## 6. Labels, corrections, residual
- NUMÉRICO (this memo): §2 eigenvalues/vectors, §3 pieces (50 digits, two independent routes agree), §4 prolate
  coefficients/leakage/κ_emp, §5 zero sums (check only). Reproducible from the shipped scripts and data.
- PROVED (classical, used): Möbius bijection (MECH Prop 3.1), Slepian–Pollak ψ̂_k = (−i)^k√λ_kψ_k (CITED), B_001 Lemma 3.1.
- ARGUED: the mechanism reading §5.1–3; the width-selection reading in §3.
- **Corrections recorded:** K_001 K.1b (repair along ψ₄, not ψ₂; self-dual sector forced); PATTERN κ at μ = 15 is 4.08 with
  the exact 1−λ₄ (not 4.63); AUDIT_5 constraint 16 "no window datum lies in 𝒮": true, but the extremal window datum is
  self-dual up to its out-of-band part (f̂* − f* = r*), which is the quantitative form of the 𝒮-vs-PW gap on the extremal.
- OPEN: what fixes the floor level/t*; Son/𝔅/K_s on g*; W⁻ and H_ζ on v*; whether the floor part of ℓ is physical.
- No sign claimed. (★★) OPEN. Row D OPEN.
- **Do not retry:** "ψ₀ + αψ₂" as extremal model (K.1b); reading the comb contacts 11, 13 as carriers of the μ = 15
  cancellation (they are 10⁻³²–10⁻⁴⁴ of the n = 2 term, though 10²⁷–10³⁹ above W_T); searching arithmetic structure in
  c_{g*}(log m/n) (smooth Gaussian autocorrelation).

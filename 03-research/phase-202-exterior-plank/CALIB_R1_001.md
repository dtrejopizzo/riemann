# CALIB_R1_001 — Numerical calibrator, phase 202, round 1 (NUMERICAL)

Everything that follows is **NUMERICAL**. No extremals or
new windows were sought. The phase was closed by criterion (a) in round 2 (BUILD_R2_001). This memo delivers what
was already computed. Data and scripts: `CALIB_001_data/`.

## 0. Conventions and precision
- **Datum.** r* = 𝓕f*|_{(λ,∞)} of the Mori extremal μ = 15, with ρ(ω) = r*(λω)·10³⁵.
  - Minimum-leak gauge M = 28.
  - It is the true f*, without Galerkin compression. That is why the target is **W_T(g*) = 4.978e−70** and not W* = 4.763e−70.
  - ρ was taken from F0_TEST_001 (arb 400/256 bits, stable to 30 digits).
- **Units.** Quadratic quantities in 10⁻⁷⁰.
- **Grid.** y = log s with s = ω, Δy = 1.5e−5, cutoff X = 240 (nω ≤ X); control with X = 48.
- **Precision.** In exterior coordinates there is no cancellation: everything is O(ℓ*), so double precision suffices.
  - Precision is limited by the cutoff X: around 1% against the 1/X extrapolation.
  - Quadrature contributes less than 10⁻⁴.
- **Pairs.**
  - Ψ_n(y) = √(λs)·ρ(ns).
  - P(m,n) = λ∫₁ρ(ms)ρ(ns)ds = K(m,n) from BUILD (2.1).
  - I(m,n) = √(mn)·P(m,n).
  - bil(a@m, b@n) = 𝒜(Ψ_a,m, Ψ_b,n) + A_aB_b + A_bB_a − (log m + log n)⟨a_m, b_n⟩.
  - Entry (1,n) of 𝒲 = 2·bil(ρ@1, ρ@n).
  - **This is the EXTERIOR_DATUM convention (`Xbil`, verified in the code): the R_n are entries of 𝒲, not of ⟨·,·⟩, and do not carry a separate vector v** (ρ already contains μ). This confirms the convention fixed in the audit.
- **ρ_pro.** Projection of f* onto the 81 prolates c = 30π, with the a_k from the gauge.
  - Computed with √λ Σ_t C_t·2(−1)^t j_{2t}(30πω), in arb at 640 bits; radius ≤ 1e−99.
  - ρ_pro(1) = −7.2222 = ρ(1) to 9 digits.
  - pro04 = a₀ψ₀ + a₂ψ₄ (edge −9.588, as in EXTERIOR).
  - Δr_out = ρ − ρ_pro, neglecting Δr_in (≤ 1e−4 relative).

## 1. Reconstruction (request 1)
| X | 𝒜 | 2AB | ⟨Zr*,Z_log r*⟩ | (★★)-LHS |
|---|---|---|---|---|
| 240 | 6.5294 | 0.0007 | 0.73392 | **5.0623** |

- A = −0.0581, B = −0.00616, ‖Ψ̌‖² = 1.612. Reproduces step3 of F0_TEST.
- The 1/X extrapolation (F0_TEST) gives 5.03, against W_T(g*) = 4.978: agreement of around 1%.
- Control: Σ_d Λ(d)⟨Zr, D_dZr⟩ = 0.73364 (difference of 4e−4 from interpolation).

## 2. Ratio classes for ⟨Zr*, Z_log r*⟩ (request 2)
- **Formula.** For q = a/b coprime: Σ_k L(kb)/k · λ∫_k ρ(at)ρ(bt)dt. All pairs with max ≤ 240 were taken, Simpson with dω ≤ 0.002.
- **Totals.** The sum over classes gives 0.73392, equal to the direct computation.
- **Sign of each class:**
  - diagonal 1/1: **+5.60**;
  - 1/2: −4.28; 1/3: −3.14; 1/5: −2.18; 1/7: −1.29; 3/4: −1.01;
  - 2/3: +1.97; 2/5: +1.33; 3/5: +1.09; 1/6: +0.82; 3/7: +0.78; 2/7: +0.77; 1/4: +0.67; 1/10: +0.56.
- **Cancellation.** The value 0.73 comes from O(5) classes cancelling. Reaching 99% requires **128 classes**: there is no concentration.
- **Files.**
  - Table I(m,n) for m,n ≤ 36: `calib_r1_X240.json` (pairs.I).
  - Q_j per class: `classes_Q_X240.json`.
  - Summary: `classes_summary.json`.

**Contribution to 𝒲 per class (P1).** Pairs m,n ≤ 36; the sum gives 5.131 against 5.062 for the total.

| class | 𝔅 (archim.) | pole | comb | total |
|---|---|---|---|---|
| 1/1 | +30.31 | 0.000 | −10.50 | +19.80 |
| 1/2 | −17.21 | 0 | +8.08 | −9.12 |
| 1/3 | −11.23 | 0 | +5.90 | −5.33 |
| 1/4 | +2.25 | 0 | −1.36 | +0.89 |
| 1/5 | −6.63 | 0 | +4.05 | −2.58 |
| 1/6 | +2.44 | 0 | −1.52 | +0.92 |
| 1/7 | −3.59 | 0 | +2.38 | −1.21 |
| 2/3 | +5.15 | 0 | −3.81 | +1.34 |

- **Where the sign μ(n) comes from.** In the integer classes the sign μ(n) is carried by the 𝔅 (archimedean) part, in 6/6 cases. The comb partially compensates it with opposite sign. This is consistent with Lemma M of BUILD_R2.

**Entries (1,n)/X₁₁, with X₁₁ = 15.63:**

| n | total | 𝔅 | comb | README |
|---|---|---|---|---|
| 2 | **−0.487** | −0.605 | +0.117 | −0.479 |
| 3 | −0.299 | −0.429 | +0.131 | −0.295 |
| 4 | +0.057 | — | — | +0.062 |
| 5 | −0.155 | — | — | −0.148 |
| 6 | +0.054 | — | — | — |
| 7 | −0.075 | — | — | — |

- The README values are reproduced.
- With X = 48: −0.482 / −0.291 / +0.059 / −0.148.

## 3. Angles and cross block (requests 3, P2, P3)
- **cos∠(r*, D_n r*), n = 2…10.**
  - L², normalized by Cauchy–Schwarz: −0.575, −0.551, +0.189, −0.578, +0.262, −0.446, −0.150, +0.060, +0.264.
  - 𝒜 metric, formal because 𝒜 is indefinite in general (here 𝒜[r], 𝒜[D_n r] > 0): −0.548, −0.527, +0.158, −0.540, +0.242, −0.413, …
- **Normalized by ‖r‖².** With that normalization, n = 2 gives −0.446.
- **TEST_2X2 thresholds.** All |cos| stay below 0.6 (the maximum is 0.578, at n = 5) and far from 0.95. **None is 0.644**: that TEST_2X2 number is a different normalization, of coupling and not of angle.
- **cos(Zr*, D_n Z_log r*).** Ranges from 0.05 to 0.17 in absolute value, with mixed signs.
- **Cross block (n = 2):**
  - 2bil(pro04@1, Δr@2)/X₁₁ = **−0.213**, and in the reverse direction −0.004.
  - With pro_all: −0.238 against 0.000.
  - cos⟨ρ_pro, D₂Δr_out⟩ = −0.36 (pro04) and −0.43 (pro_all).
  - **The −0.481 from EXTERIOR is NOT reproduced in r*.** That value was from the vector p = g*₅₀, which is a different datum. The directionality is confirmed: the reverse block is ≈ 0.
  - In r*, the remainder of (1,2) is Δr×Δr = −0.29 (pro04).
- **Layer masses θ_n (n = 2, 3, 5):**
  - r*: 0.397, 0.515, 0.680;
  - ρ_pro: 0.696, 0.863, 0.934;
  - **Δr_out: 1.1e−4, 0.056, 0.343** (has no mass in [λ, 2λ)).
- **Lemma X1.0.** Gives |cos₂| ≤ √(1 − 0.397) = 0.78 for r*, which is not reached.

## 4. Other combs on the same r* (requests 4/P6, convention A)
- **Convention A.** Z_log^X r = Σ_d Λ_X(d) D_d Zr, i.e. weight (Λ_X∗1)(n). 𝒜 and 2AB from ζ are kept.
- **Comb data.** Exact Λ_Q from file `lambdaQ_exact.json`; b_n from DH with the CERT_DH recursion.

| comb | ⟨Zr,Z^X_log r⟩ | LHS (★★) |
|---|---|---|
| ζ | 0.7339 | 5.062 |
| Epstein | 0.6889 | 5.152 |
| DH | −0.0934 | 6.717 |

- **Finding.** In exterior coordinates no comb gives O(1) against 1e−70. The 70-digit cancellation is already inside r*: r* is O(ℓ*), so every LHS is O(ℓ*) for any comb.
- **Epstein classes.** Follow those of ζ: 1/1 +4.37, 1/2 −3.55, 1/3 −3.49, 2/3 +2.14, 1/6 +1.56 (ζ: +0.82).
- **DH classes.** There is no structure: the diagonal comes out −0.38 and the dominant class is 1/6 (+0.43). 205 classes are needed for 99%.

## 5. Not computed (stopped by phase closure)
- **P4 (𝒥(m′), 𝓡/𝓓).** σ̃ = σ_g(λ·) was computed (`sigma_tilde.npy`, double precision, noise floor ≈ 1e−13 for ω ≳ 5), but not integrated.
  - **Scale datum.** σ̃(1) = −3.3e−3 and σ̃(0.1) = 1.24. The lattice lines are between 10³² and 10³⁵ times r*. 𝒥(m′) is O(1) in absolute units, so 𝓡/𝓓 is a ratio between quantities that cancel to about 70 digits with the gauge.
- **P5 (‖Zσ_g‖).** Not computed; would be limited by the double-precision noise floor.
- **P6 (μ_X, convention B: weights a_X log n in Z).** Not computed.
- **P7 (a_P).** Not computed.
- **Coincident/non-coincident separation within P1.** Not computed: would require 70-digit precision on the lattice lines.

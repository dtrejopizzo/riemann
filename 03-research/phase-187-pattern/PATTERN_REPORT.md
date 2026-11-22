# PATTERN_REPORT — pattern of T ↦ λ_A(T) over the non-contiguous windows of phase 187

Data: `DATA_100_WINDOWS.csv` (campaign in progress; this report uses the
46 converged windows available at closing, T ∈ [0.3366, 1.075]). Reproducible script: `r187_pattern.py`
(numpy/scipy only; prints all the tables here). Falsifier: `r187_mm.py` → `DATA_MM_FALSIFIER.csv`, `windows_mm/`.
Constraints: `CONSTRAINTS_FOR_PATTERN.md` (§1–§6).
**Global label: NUMERICAL (fits) / CONJECTURE (laws). No result touches the sign or the grid.**
Notation: y := −ln λ_A, d := −log₁₀ λ_A, N := N(T*) from the data, N_s := e^{2T}(2T−1) + 7/8 (smooth RvM).

**Sign status in the data:** the 46 rows all have n₋ = 0 and λ_A > 0 (none with nneg > 0 or λ_A ≤ 0); minimum
precision margin 31.0 digits; all converged (relvar < 10⁻²; λ_A is a variational upper bound with error ≲ 1–3%,
i.e. ±0.01 in d: that is the noise level of everything that follows).

## 0. Verification of the preliminary observation

s(T) := d′(T)/e^{2T} (centered differences between consecutive windows): 6.5–7.1 at T ≈ 0.55, 9.1–9.7 at 0.69, 9.1–9.2 at
0.80, 9.6–10.1 at 0.97; mean 9.31 ± 0.65 for T > 0.6 (range 7.8–10.5). **Verified as a description**, with a caveat: law (c)
of §1 gives s(T) = (2c₁ − |c₂|e^{−2T})/ln 10 ≈ 11.3 − 10.7·e^{−2T}, which rises slowly (7.6 at 0.55, 9.8 at 1.0, 10.7 at 1.5)
toward 11.3: "nearly constant" is correct in this range, not a limit. Continuity at the boundaries: y does not jump at any
½log n (table §1.3), although N_Sh jumps ×1.2–×1.8.

## 1. Candidate laws for y = −ln λ_A (protocol §6: form fixed beforehand, fit on 0.55 ≤ T ≤ 0.85, prediction at T > 0.85)

Fit windows: 17; held out: 17 (T = 0.87 … 1.075). Error reported in d (digits) and relative in y.

| law | #par | parameters (fit ≤ 0.85) | fit rms (dig) | out-of-sample error: mean ± sd, max (dig) | relative error in y: 0.87 → 1.075 |
|---|---|---|---|---|---|
| a0: 2π²N/lnN (Zhu, fixed c) | 0 | — | 15.7 | +10.9 ± 0.9, max 12.4 | +0.81 → +0.37 |
| a1: c·N/lnN (N from data) | 1 | c = 7.27 | 2.58 | −9.8 ± 2.9, max 14.2 | −0.33 → −0.50 |
| a2: c·N_s/lnN_s | 1 | c = 7.18 | 2.82 | −9.9 ± 2.9, max 14.6 | −0.34 → −0.51 |
| b: c·x/ln x + d, x = e^{2T}(2T−1) | 2 | c = −13.3, d = 62.2 | 1.50 | −15.7 ± 6.6, max 26.7 | −0.32 → −0.93 |
| **c: c₁e^{2T} + c₂T + c₃** | 3 | 13.69, −30.34, −17.57 | **0.03** | **+0.24 ± 0.12, max 0.51** | +0.004 → +0.018 |
| d1: a·N lnN + d | 2 | 2.87, 9.36 | 0.98 | +2.8 ± 2.7, max 8.2 | −0.04 → +0.29 |
| d2: a·N_s lnN_s + d | 2 | 3.40, 8.19 | 0.35 | +6.0 ± 3.4, max 12.5 | +0.07 → +0.44 |
| g: a·N_s + d | 2 | 6.97, −0.90 | 0.09 | +1.7 ± 0.9, max 3.4 | +0.02 → +0.12 |
| g1: a·N + d (N from data) | 2 | 5.94, 1.70 | 0.89 | −0.8 ± 0.9, max 2.6 | −0.07 → +0.01 |
| f: a·e^{bT} + d (free rate) | 3 | 4.36, b = 2.73, −12.73 | 0.03 | +0.57 ± 0.35, max 1.30 | +0.006 → +0.045 |
| h: a·T·e^{2T} + d | 2 | 8.24, −6.72 | 0.03 | +0.64 ± 0.37, max 1.39 | +0.008 → +0.048 |

Reading:
- **(a) Zhu, fixed c = 2π², N/ln N:** overestimates by 10–12 digits over the whole range (λ_W ≠ λ_A, CONSTRAINTS §4 (iv)): it does not apply to λ_A.
  With free c (a1, a2) the fit is already poor (rms 2.6–2.8) and the prediction fails by 5–14 digits and worsens with T: the
  N/ln N form is **pre-asymptotic** here (ln N ∈ [0, 2.3] and N_s < 1 below T = 0.52). (b) with denominator ln x gets c < 0: excluded.
- **(d) a·N ln N:** +2 … +11 digits out of sample, increasing: excluded. **(g) linear in N_s:** +1.6 ± 0.8, max 3: excluded
  as an exact law (the "nat per zero" is not constant: ℓ₁/N_s drops 6.47 → 6.10 between 0.85 and 1.06).
- **(c) y = c₁e^{2T} + c₂T + c₃:** rms 0.03 dig in the fit, **out-of-sample error +0.23 ± 0.11 dig (max 0.43) over
  17 windows**, relative +0.4% → +1.6%. It is the only law with error < 0.5 dig; but the relative error **grows** with T
  (Zhu's criterion §6.3: it is not certified two-sided). (f) with free rate gives b = 2.7 (fit) / 2.4 (whole range): rate 2
  is not fixed by the data (c₂ < 0 and b > 2 compensate); (h) a·Te^{2T} + d: +0.6 ± 0.3.
- Fit over the whole range T ≥ 0.55 of (c): **y ≈ 12.98·e^{2T} − 24.55·T − 18.70** (rms 0.034 dig, max residual 0.07).
  Asymptotically (c) ≡ 6.5·N_s/T ≈ 13·N_s/ln N_s: the same *form* as Zhu's Conj. 12.1 with constant ≈ 13 ≈ 0.66·2π² instead
  of 2π², but that identification is extrapolation: in the measured range N/ln N does not describe the data.

### 1.1 Per-window prediction of (c) (fit ≤ 0.85): predicted − observed digits
| T | 0.87 | 0.89 | 0.90 | 0.92 | 0.94 | 0.955 | 0.963 | 0.973 | 0.983 | 0.995 | 1.015 | 1.030 | 1.040 | 1.050 | 1.060 | 1.075 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| d obs | 14.71 | 15.76 | 16.33 | 17.62 | 18.77 | 19.78 | 20.32 | 20.98 | 21.62 | 22.48 | 23.99 | 25.11 | 25.87 | 26.71 | 27.49 | 28.73 |
| (c) − obs | +0.06 | +0.14 | +0.14 | +0.05 | +0.17 | +0.15 | +0.15 | +0.18 | +0.25 | +0.27 | +0.27 | +0.33 | +0.35 | +0.34 | +0.43 | +0.51 |
The error grows monotonically (+0.03 dig per 0.01 T at the end): (c) with the parameters fit ≤ 0.85 overestimates d; the
refit over the whole range lowers c₁ to 12.98 (the "−24.6 T" absorbs the difference). It is not a closed law, it is an excellent interpolation.

### 1.2 Structured residuals
Residual of (c) (whole range) against log N_Sh: corr = −0.005; residual at the 6 prime entries (0.559, 0.703, 0.815,
0.983, 1.050): |res| ≤ 0.07 dig, the same as between primes. **No visible fold in the residual.**

### 1.3 Folds at the ½log n boundaries (triples T_b ± 0.01)
CONDITIONAL[(REG)] prediction (CONSTRAINTS 1.11–1.12, R186_036 Lemma 2, even sector): Δ(dλ_A/dT) = −2v_n h*(T_b)²,
hence Δ(dy/dT) = +2v_n·h*(T_b)²/λ_A. h*(T_b) is read from the Legendre coefficients (`windows/T_*.json`, P_k(1) = 1).

| boundary | n, v_n | left/right slope of y | measured Δ | curvature y″h (expected if y is smooth) | Δ − y″h | h*(T_b)²/λ_A | predicted Δ |
|---|---|---|---|---|---|---|---|
| ½log2 | 2, 0.980 | 5.2 / 9.2 | +4.0 | +1.0 (law c; actual is larger: s(T) rises 1.2→3.7 here) | ≈ +3 | 0.37 | +0.7 |
| ½log3 | 3, 1.269 | 44.5 / 45.3 | +0.8 | +1.6 | −0.8 | 2.23 | +5.7 |
| log2 | 4, 0.693 | 88.2 / 84.9 | −3.3 | +2.1 | −5.4 | 4.35 | +6.0 |
| ½log5 | 5, 1.440 | 105.3 / 106.1 | +0.7 | +2.6 | −1.9 | 5.52 | +15.9 |
| ½log7 | 7, 1.471 | 153.0 / 147.6 | −5.5 | +3.6 | −9.1 | 6.27 | +18.4 |
| ½log8 | 8, 0.490 | 180.4 / 193.2 | +12.8 | +4.2 | +8.6 | 9.34 | +9.1 |
| ½log9 | (triple incomplete at closing) | | | | | | | |

Noise of Δ: the convergence error of λ_A (1–3%) gives ±0.01–0.03 in y per window ⇒ ±2–5 in Δ. **Result: the predicted
fold (+6 … +18) does not appear at ½log3, log2, ½log5, ½log7 (measured 0 ± 3, with opposite sign in two cases); only at ½log8
is the measured value (+8.6 ± 5) compatible with the prediction (+9.1).** New NUMERICAL datum: the minimizer has a boundary
layer: |h*(t)|² drops from O(1) at t = 0.9T to h*(T)² ≈ (2…9)·λ_A at the boundary (½log5: 2.6e-5 → 1.75e-11), so the
theoretical fold is an O(1) fraction of the slope (15% at ½log5) and should be visible; it is not. Reading: either (REG) fails at the
boundary (the minimizer readjusts its boundary layer at zero first-order cost), or the Galerkin boundary value is not the true one.
In any case, **𝒱 from CONSTRAINTS 1.11 is not an observable measurable at this resolution; the prime entry is invisible
in y(T) at the 0.05-dig level.**

## 2. Patterns in the observables

### 2.1 K_δ against N(T*) (40 windows with N ≥ 1)
| threshold | mean(K−N) | sd | min/max | #{|K−N| ≤ 1} | corr(K, N) | corr(K, N_Sh) | line K = αN + β |
|---|---|---|---|---|---|---|---|
| K_{10⁻²} | +0.45 | 0.74 | −1 / 2 | 39/40 | 0.991 | 0.957 | — |
| K_{10⁻³} | −0.10 | 0.77 | −1 / 1 | **40/40** | 0.988 | 0.959 | 1.18·N − 0.91 |
| K_{10⁻⁴} | −0.55 | 0.59 | −2 / 1 | 39/40 | 0.989 | 0.968 | — |
| K_{e⁻¹} | +1.73 | 0.95 | −1 / 3 | 14/40 | 0.986 | 0.957 | 1.24·N + 0.65 |

Confirms CONSTRAINTS 2.1 across 40 windows: K_{10⁻³} = N(T*) + c, c ∈ {−1, 0, 1}, without exception; K_{e⁻¹} = N + 2…3. The
10⁻³ threshold is the most stable (sd 0.77 and centered). Warning: the fitted slope is 1.18 > 1; if it persists, K − N will grow ≈ 0.18·N and
the "±1" rule will fail toward N ≈ 12–15 (T ≈ 1.15–1.3): **discriminating test for the high-T rows** (prediction: K₃(T=1.3) = 19 ± 1
with the line, 17 ± 1 with "N ± 1"). K does not track N_Sh (lower corr and N_Sh jumps without a K jump).

### 2.2 Ladder ℓ_j = −ln(1 − β_j)
- Exact identity verified: y − ℓ₁ = −ln Pos(h*) ∈ [1.08, 1.51] (piecewise constant over prime stretches: 1.40 → 1.50 → 1.09 → 1.27 → 1.08).
- ℓ₁ ≈ 6.25·N_s − 0.13 (rms 0.83 nat): "≈ 6 nats per zero," but ℓ₁/N_s is not constant (5.1 → 6.47 → 6.10), and the residual
  0.83 nat ≫ 0.03 noise: the linear-in-N(T*) law is only approximate (it is law (g), excluded out of sample).
- Steps ℓ_j − ℓ_{j+1}: **not constant in j or in T**: first step 4.0 (0.61) → 6.7 (1.06), second 3.6 → 7.4; step j decreases
  with j (at T = 1.06: 6.5, 7.4, 6.2, 6.0, 5.3 …) down to j ≈ K_e and then drops to ≪ 1. Mean step over j ≤ K_e: 2.8 → 5.7.
  ℓ_j is approximately linear in j with slope ≈ 5–7 only within the head (j ≤ K_e). "Σ steps = ℓ₁" is tautological
  and is not a law: neither the steps nor their number (K_e ≈ 1.24N + 0.65) follow a closed formula in this range.

### 2.3 Parity and peak of the minimizer
- h* even in all 46 windows (even mass = 1.000000); second eigenvector odd in all of them (even mass 0.0000): the even/odd
  alternation of CONSTRAINTS 2.6 confirmed in the head (u₁, u₂).
- Peak of |ĥ*|²: 10.35 (0.357) → 7.53 (½log3) → 6.90 (½log5) → 6.65 (1.04); peak·T = 3.7 → 6.9 (not constant: the 1/T law excluded);
  peak/T* decreases 0.5 → 0.13 (does not track the zeros ≤ T*). Fits for T ≥ 0.5: a + b/T² (6.33 + 0.37/T², rms 0.011) ≈ a + b/T
  (5.63 + 1.04/T, rms 0.022): limit 5.6–6.3, indistinguishable at the ±0.3 resolution (CONSTRAINTS 2.7); below γ₁/2 = 7.07
  from T ≈ 0.70 on. No law with content.

### 2.4 N_Sh against λ_A
N_Sh jumps at every prime entry (×1.72 at ½log3⁺, ×1.20 at log2⁺, ×1.79 at ½log5⁺, ×1.57 at ½log7⁺, ×1.19 at ½log8⁺) and
N_Sh/N(T*) oscillates in [1.7, 3.1]; the local slope s(T) of y across those boundaries is 6.4, 9.0, 9.0, 9.0, 10.3 (no
jump); corr(log N_Sh, residual of (c)) = −0.005. **Insensitivity of λ_A to prime entries confirmed** (R186 rounds
18–19): y(T) is a smooth function of T whose only apparent parameter is e^{2T} (∝ T*), not the negative set.

## 3. Extrapolation with constraints

### 3.1 Admissibility (§6 step 1 and 6)
- Data: y increasing over the 44 consecutive pairs (monotonicity 1.1 ✓), no jumps (1.3 ✓); λ_A ≤ 𝓑(T,k*) in all windows
  (𝓑 > 1 for T < 1.43: vacuous) and λ_A ≤ 4·10⁹Te^{−15.449T} at T ≥ 1 (10^{+2.8…+2.5}: vacuous). Certified values 1.8: 9.46e-4 ∈
  [8.86e-5, 9.5e-4] at ½log3 ✓, 3.18e-12 ∈ [2.5e-12, 3.9e-12] at ½log5 ✓ (3.86e-12 in R186_039 with smaller M: consistent, Galerkin decreases in M).
- Law (c): non-increasing in λ (c₁ > 0 dominates; dy/dT = 26e^{2T} − 24.6 > 0 for T > 0), continuous, −ln L ~ 13e^{2T} ≥ e^{(2−ε)T}
  (Thm M (b) ✓ with ε = 0), below 𝓑 and below the closed bound for all T ≥ 1. Does not violate thm:margin at any T. No convexity imposed.

### 3.2 Prediction (fit of (c) over the whole range; band = spread among the three laws with rms ≤ 0.15: c, f, h)
| T | N_s(T*) | −log₁₀ λ_A by (c) | band [f, h] | −log₁₀ 𝓑(T,k*) (must be ≤) | −log₁₀ closed bound | Thm M: e^{2T}/ln10 |
|---|---|---|---|---|---|---|
| 1.2 | 16.3 | 41 | 42–43 | −1.5 | −1.6 | 4.8 |
| 1.5 | 41.0 | 89 | 94–101 | 0.5 | 0.3 | 8.7 |
| 2.0 | 164.7 | 278 | 336–371 | 3.7 | 3.5 | 23.7 |
| 3.0 | 2018 | 2233 | 3913–4138 | 10.2 | 10.0 | 175 |
Out-of-sample error of (c) at ΔT = 0.2 from the fit: 0.4 dig (1.6%); extrapolating the growth of the relative error
(≈ +0.6%/0.1 T) the honest band at 1.2 is ±3%, at 1.5 ±7%, at 2.0 ±15% **if the form is correct**; the spread in form
(f, h vs c) is already 2% at 1.2, 13% at 1.5, 33% at 2.0 and 85% at 3.0: **the form is not determined beyond T ≈ 1.3.**
The high-T rows of the campaign (1.3–1.75) are the only test: prediction of (c) at T = 1.5: d = 89 ± 6 (vs 94–101 from f/h).
New rows arriving during the analysis (1.05, 1.06, 1.075): predicted by (c) (fit ≤ 0.85) with +0.34, +0.43, +0.51 dig;
K₃ = 10, 10, 10 with N(T*) = 10, 10, 11 (±1 rule ✓); even parity; nneg = 0 in all of them (**no contact with the sign**).

### 3.3 Test against f_t (§3.1, §6 step 4)
With T_fit = 0.85, N₀ = e^{2T_fit} = 5.47. **Statement:** f_t with this N₀ (Thm F, R163_901) has W^{f_t}_T = W^ζ_T for
T ≤ T₁ = ½log λ₁ > T_fit, so it satisfies exactly the same fit (c) and the same table §1; out of sample
λ_A^{f_t} = λ_A^ζ + θ|t|C(T) with a sign decided by the perturbation. By construction the law does not distinguish ζ from f_t in the
measured range, and **no finite range [0, T_max] would**: for every T_max there is an f_t with T₁ > T_max. The §3.2 extrapolation is a
statement about the family {ζ, f_t}, not about ζ; only a proved two-sided law (CONSTRAINTS §3.2) would escape.

### 3.4 Test against M_m (§3.3, §6 step 5): M_1 = quartet ½ ± δ ± iγ₁, same code (`r187_mm.py`)
Form: 𝔞^M_T = 𝔞_T + ∫_{−2T}^{2T} c_F(u)·4cos(γ₁u)cosh(δu)du (= quartet sum by lem:roughEF; R163_801 Thm 5);
symbol σ^M = σ_T + β̂ (closed form, verified against quadrature). Everything else (Galerkin, 𝒫_T, pencil, K, parity, peak) identical.

| δ | T | λ_A^{M} | λ_A^{ζ} | n₋ | K₂/K₃/K₄/K_e (M) | (ζ) | parity h* (M/ζ) | peak (M/ζ) | ℓ₁,ℓ₂,ℓ₃ (M) | (ζ) | N_Sh (M/ζ) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 10⁻³ | ½log3 | 9.480e-4 | 9.457e-4 | 0 | 1/0/0/2 | 1/0/0/2 | even/even | 7.53/7.53 | 5.9, 2.6, 0.3 | 5.5, 2.1, 0.0 | 3.20/2.41 |
| 10⁻³ | 0.61 | 3.550e-5 | 3.551e-5 | 0 | 2/1/1/3 | 2/1/0/3 | even/even | 7.31/7.31 | 9.5, 5.6, 1.7 | 8.8, 4.8, 1.2 | 4.51/4.52 |
| 10⁻³ | 0.67 | 6.124e-7 | 6.311e-7 | 0 | 2/2/1/4 | 2/2/1/4 | even/even | 7.16/7.15 | 13.4, 9.2, 4.3 | 12.9, 8.5, 3.7 | 5.09/4.96 |
| 10⁻⁶ | ½log5 | 3.162e-12 | 3.176e-12 | 0 | 5/4/4/6 | 5/4/4/6 | even/even | 6.90/6.90 | 25.8, 20.6, 14.6 | 25.0, 19.6, 13.7 | 11.66/7.05 |
| 0.1 | ½log3 | 5.774e-4 | 9.457e-4 | 0 | 1/0/0/2 | 1/0/0/2 | even/even | 7.53/7.53 | 6.4, 2.7, 0.3 | 5.5, 2.1, 0.0 | 3.20/2.41 |
| 0.1 | log2 | **−1.52e-3** | 9.86e-8 | **2** | 3/3/2/4 | 3/2/2/4 | even/even | 10.3/7.10 | —, —, 7.5 | 14.7, 10.0, 5.1 | 5.19/5.13 |
| 0.3 | log2 | **−2.85e-2** | 9.86e-8 | **2** | 3/3/2/4 | 3/2/2/4 | even/even | 10.6/7.10 | —, —, 8.2 | 14.7, 10.0, 5.1 | 5.21/5.13 |
| 0.1 | ½log5 | **−4.97e-3** | 3.18e-12 | **2** | 5/4/4/6 | 5/4/4/6 | odd/even | 11.1/6.90 | —, —, 16.6 | 25.0, 19.6, 13.7 | 11.66/7.05 |
| 0.3 | ½log5 | **−4.77e-2** | 3.18e-12 | **2** | 5/4/4/6 | 5/4/4/6 | even/even | 17.3/6.90 | —, —, 13.0 | 25.0, 19.6, 13.7 | 11.63/7.05 |
(Runs with δ = 10⁻³ at log 2 and 0.72 and with δ = 10⁻⁶ at 0.85, 0.90 were still in progress at closing; added to `DATA_MM_FALSIFIER.csv` on completion.)

Reading:
- **Before its contact, M_1 reproduces the ENTIRE ζ pattern:** λ_A^{M} = λ_A^{ζ} to within 0.2–3% (δ = 10⁻³ up to 0.67; δ = 10⁻⁶ at ½log5
  to within 0.4%), same K_δ (= N(T*) ± 1, which does **not** count the quartet: N^{M}(T*) = N + 2 and K does not change), same parity, same
  peak, ladder equal to within ±0.9 nat. Hence law (c), the count K ≈ N(T*), the ladder, the parity and the peak are **class
  properties** (§3.3): M_1 satisfies them and has λ_A^{M} < 0 from T_c(δ) on: T_c(0.1) ∈ (0.55, 0.69), T_c(10⁻³) ∈ (0.67, 0.72] due to
  the shift −C·δ² (C ≈ 4·10⁻² at ½log3: 9.5e-4 − 5.8e-4 = 3.7e-4 at δ = 0.1; 2e-8 at 0.67 at δ = 10⁻³ ✓ scales as δ²).
- Upon crossing the contact, M_1 **preserves** K_δ = N(T*) ± 1 and even parity (n₋ = 2, λ < 0): not even the count detects the sign.
- λ_A is insensitive to the negative set here too: N_Sh(M_1) = 11.66 vs 7.05 at ½log5 with λ identical to 4·10⁻³.
- **Conclusion of the test: no law or observable in this report implies positivity** (class blindness W3/F3 verified
  with the same code). The only ζ/M_1 difference is the −Cδ² term that the law does not model: detecting it would require
  λ_A at relative precision < Cδ²/λ_A, impossible by extrapolation.

## 4. Honest conclusion (three lines)
1. **There is indeed a clean law in the measured range:** y = −ln λ_A ≈ 13.0·e^{2T} − 24.6·T − 18.7 (rms 0.03 dig, out-of-
   sample error 0.2–0.4 dig over 17 windows), i.e. d′(T)/e^{2T} → 11.3 slowly; it is the asymptotic form c·N(T*)/ln N(T*)
   of Zhu with c ≈ 13 ≠ 2π² (λ_A ≠ λ_W), but N/ln N does **not** describe the data at T ≤ 1.1; K_{10⁻³} = N(T*) ± 1 in 40/40 windows.
2. **What the law implies:** a description of λ_A(T) with error ≈ 1% in y up to T ≈ 1.1 and a falsifiable prediction for
   the high-T rows (d(1.5) = 89 ± 6; K₃(1.3) = 17–19); the prime folds predicted by 1.11–1.12 are not observed (NUMERICAL,
   against the CONDITIONAL formula of R186_036 Lemma 2 at 4 of 5 boundaries).
3. **What it does not imply:** anything about the sign for all T: the law is "leading term + O(1) relative error" (W-det),
   f_t shares it by construction, and M_1 shares it up to its contact (class blindness); label for all of this NUMERICAL/
   CONJECTURE; **no contact with the sign: row D OPEN.** No grid symbol changes; neither Paper 46 nor the crossword has been touched.

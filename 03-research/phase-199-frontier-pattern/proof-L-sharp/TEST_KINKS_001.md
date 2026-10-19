# TEST_KINKS_001 — is Δr_out a sum of Möbius-kink tails? (NUMÉRICO on existing data)

Phase 199, numerical analyst.
No new certification. Data reused: EXTERIOR_DATUM_001 exterior run
(`ed1/exterior_decomp_v2_OMX48_NP900.json`: ρ_p, ρ_pro04, ρ_pro8+, inner residual; M = 28 Tate-constrained min-leak gauge,
ω ∈ [1,48], Δω = 0.002), p = g*_50 Legendre vector (`rc/pvecs.pkl`), g* (MORI15 `p0_eig.json`). Units ρ: 10⁻³⁵; forms: W*.
Scripts: `TEST_KINKS_001_jets.py` (mpmath dps 130), `TEST_KINKS_001_analysis.py`, `TEST_KINKS_001_resum.py` (double, X-matrix =
EXTERIOR_DATUM_001_analysis.py). Data: `TEST_KINKS_001_data/{jets,analysis,resum}.json`, `analysis.log`.

**Hypothesis tested (HH_001):** Δr_out = Σ_m μ(m)K_m (+ smooth), K_m the Fourier tail of the jet jump of f = E⁻¹g at u = λ/m.

## Verdict: NO (jumps exact; jet-tail model fails by orders of magnitude; resummed kinks too small by ≈ 40×)

## 1. Edge jet and jumps (task 1)
| | g(T) | g′(T) | g″(T) | g′/g | g″/g |
|---|---|---|---|---|---|
| p = g*_50 | −1.16575e−34 | −5.92065e−31 | −7.55881e−25 | 5078.8 | 6.48e9 |
| g* | −1.42077e−34 | −9.66891e−31 | −7.95158e−25 | 6805.4 | 5.60e9 |
h(v) = v^{−½}g(log v): for p, h(λ) = −5.92355e−35, h′(λ) = −7.76708e−32, h″(λ) = −2.56058e−26 (h′/h = 1311 in u-units,
h″/h = 4.32e8 ≫ (h′/h)² = 1.7e6). g*: h(λ) = −7.21939e−35, h′(λ) = −1.26846e−31, h″(λ) = −2.69363e−26.
**Jumps (black-box one-sided 8-point polynomial fits of f₁ at λ/m ± k·10⁻¹⁴, dps 130):** for every squarefree m ∈ {1,2,3,5,6,7,
10,11,13,14} the ratios (J₀,J₁,J₂)/(μ(m)h, μ(m)m h′, μ(m)m²h″)(λ) = 1 to ≥ 15 digits. For m = 4,8,9,12 (μ = 0):
|J₀|/|h| ≤ 2·10⁻⁸³, |J₁|/|h′| ≤ 1.1·10⁻⁵⁹, |J₂|/|h″| ≤ 5·10⁻⁶³ (FD noise). AA_001 D.2 confirmed (NUMÉRICO; it is PROVED).

## 2. Kink tails vs Δr (task 2)
K_m(ω) = 2[J₀ sin(ku₀)/k + J₁ cos(ku₀)/k² − J₂ sin(ku₀)/k³], k = 2πλω, u₀ = λ/m (integration by parts of 2∫₀^λ f cos ku).
Relative L² error ‖Δr_out − Σ_{m≥2}μ(m)K_m‖/‖Δr_out‖ (corr in brackets):
| model | (1,2) | (2,4) | (4,8) | (8,48) |
|---|---|---|---|---|
| order 0 | 17.7 (−0.09) | 2.06 (−0.06) | 1.86 (−0.06) | 1.32 (−0.04) |
| order ≤ 1 | 5.5·10³ (0.11) | 317 (0.02) | 162 (−0.01) | 30 (−0.06) |
| order ≤ 2 | ~10⁸ | ~2·10⁷ | ~6·10⁶ | ~5·10⁵ |
| exp. resummation 2Re[J₀e^{iku₀}/(m h′/h + ik)] | 1.007 (−0.03) | 1.001 (−0.04) | 1.002 (−0.05) | 1.007 (−0.08) |
Against Δr (incl. pro8+): order 0 → 3.75 / 2.04 / 1.84 / 1.32. rms Δr_out: 0.050 / 0.203 / 0.143 / 0.064.
**Reason (structural, NUMÉRICO):** the order ratio is m(h′/h)/k = 54m/ω (= 108 at m = 2, ω = 1; 7.9 at m = 7, ω = 48) and the
second order is ~(h″/h)m²/k² ≈ 7·10⁵m²/ω²: the jet series is divergent everywhere on ω ≤ 48 (asymptotic regime needs ω ≫ 54m).
The steep end of h (Legendre endpoint growth, width ~1/1311 in u) is not a kink at the frequencies of the exterior form.
The resummed (exponential-ramp) kinks are bounded, but rms ≈ 0.0045 vs 0.14–0.20: ≈ 40× too small, uncorrelated.

## 3. Cross-dilation terms (task 3; W* units, as EXTERIOR_DATUM's −0.481/−0.30/−0.15)
| r | X₁₁ | (1,2)/X₁₁ | (1,3)/X₁₁ | (1,5)/X₁₁ |
|---|---|---|---|---|
| p (measured) | 2.718 | −0.350 | −0.240 | −0.126 |
| pro04 + Δr_out | 2.600 | −0.304 | −0.220 | −0.114 |
| pro04 + ΣμK order 0 | 3.299 | −0.082 | −0.039 | −0.009 |
| pro04 + ΣμK order ≤ 1 | 5.7·10⁴ | −0.152 | +0.007 | +0.008 |
| pro04 + ΣμK order ≤ 2 | 6.3·10¹⁴ | −0.043 | +0.002 | −0.005 |
Directional (pro04 @ dilate 1 × piece @ dilate n, W*): Δr_out: **−0.481 / −0.296 / −0.197** (n = 2/3/5; reproduces
EXTERIOR_DATUM); ΣμK order 0: **+0.016 / +0.015 / +0.030** (wrong sign, 30× small); order ≤ 1: +4.09 / +0.10 / −0.68;
order ≤ 2: ~10⁴ (meaningless).

## 4. Residual (task 4)
Δr_out − ΣμK(order 0): rms 0.88 / 0.42 / 0.27 / 0.085 on (1,2)/(2,4)/(4,8)/(8,48) — larger than Δr_out itself in every
window; i.e. Δr_out is essentially all residual. Size: Δr_out ≈ 0.03·|h(λ)| (consistent with "O(h(λ)), no 33-digit
cancellation"), localized at ω ∈ (2,8) (rms 0.20/0.14 vs 0.05 in (1,2)), but it is **non-local** content of the cells
μ(m)h(mu)1_{[1/λ,λ/m)} (bulk of the steep end, not the jump jet). The band-dilation structure of EXTERIOR_DATUM §3
(line m ↔ c/m) survives; its profile σ is not the jet tail of the jump.

## 5. Labels / records
NUMÉRICO: §1–§4 (μ = 15, one vector). Jump identity: PROVED (AA_001 D.2), numerically confirmed to 15 digits.
**NO-GO (NUMÉRICO, for the jet-tail class):** "Δr_out = Σμ(m)K_m with K_m the finite-order jet tail (orders 0–2) of the
Möbius jumps", and its exponential resummation. **Do not retry** local jump/kink asymptotics of E⁻¹g at u = λ/m on ω ≤ 48
(divergent, ratio 54m/ω). Open: the line profile σ_g as a non-local cell transform. Row D OPEN.

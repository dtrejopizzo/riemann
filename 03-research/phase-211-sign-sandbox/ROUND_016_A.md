# Round 016 A — The band-restricted packet reduction: exact identity, error bounds, envelope margins at T = 1–3, λ_A(1.5) at 150 digits

Notation of ROUND_012_A §3, ROUND_013_B, ROUND_015_C: N = e^{2T}, v_n = 2Λ(n)/√n (n < N), ℓ_n = log n,
m(t) = Re ψ(¼ + it/2) − log π, Ω_lo = 2πN(1 + δ), δ = 0.1. Sine basis e_k(x) = sin(a_k(x + T))/√T on [−T, T], a_k = kπ/2T.
A_τ f(x) = ½Σ_n v_n cos(τℓ_n)[f(x + ℓ_n) + f(x − ℓ_n)]·1_{[−T,T]} (f extended by 0). Free form on L²[−T, T]:
Q_T(f) = (1/2π)∫ m(ξ)|f̂(ξ)|² dξ − Σ_n v_n c_f(ℓ_n), c_f(u) = ∫ f(x)f(x + u)dx; W_T = Q_T on P_T = {∫ f e^{±x/2} = 0}.

## 0. Corpus check

Index rows read: P211-12A (Proposition 3.1, unrestricted sup), P211-13B, P211-15C (the unrestricted sup is attained by
frequency-τ oscillations, where the packet identification fails; band-limited envelope margin +0.46…+0.72 at T ≈ 1.5).
This memo is the correction requested there: same object (A_τ), new hypothesis (envelopes in a band |ξ| ≤ ητ, η < ½),
which removes exactly the recorded failure (the dropped 2τ cross term is O(1) only for envelopes oscillating at ≈ τ).
Not a new route; no index row is retried.

## 1. The band-restricted packet reduction

**Definition 1.0.** For τ > 0 and η ∈ (0, ½) let K_η(τ) = {k ≥ 1 : a_k ≤ ητ} (so |K_η| ≤ 2Tητ/π),
V_η(τ) = span{e_k : k ∈ K_η(τ)} ⊂ L²[−T, T], Π_η the orthogonal projection onto V_η, and
A_τ^{(η)} = Π_η A_τ Π_η restricted to V_η (a symmetric |K_η| × |K_η| matrix, the leading block of the sine-Galerkin
matrix of A_τ; its entries are the exact closed forms of tools/A_tau_lmax.py). Every β ∈ V_η is real-analytic on
(−T, T), vanishes at ±T together with all its even derivatives, and satisfies ‖β′‖² = Σ a_k² b_k² ≤ (ητ)²‖β‖²
(b_k = ⟨β, e_k⟩, since ⟨e_j′, e_k′⟩ = a_k² δ_jk).

**Theorem 1.1 (exact packet identity). PROVED.** For every real β ∈ L²[−T, T] with ∫|m||β̂|² < ∞ and f = β·cos(τx),
  Q_T(f) = ½[m(τ)‖β‖² − ⟨A_τβ, β⟩] + ½[D_τ(β) + X_τ(β) − R_τ(β)],
where M_τ(ξ) = ½(m(τ + ξ) + m(τ − ξ)) and
  D_τ(β) = (1/2π)∫(M_τ(ξ) − m(τ))|β̂(ξ)|² dξ                 (curvature of the archimedean symbol across the band),
  X_τ(β) = (1/2π) Re∫ m(ξ) β̂(ξ − τ) \overline{β̂(ξ + τ)} dξ      (archimedean ±τ interference),
  R_τ(β) = Σ_n v_n ∫ β(x)β(x + ℓ_n) cos(τ(2x + ℓ_n)) dx         (comb 2τ term).
For β ∈ V_η, ⟨A_τβ, β⟩ = ⟨A_τ^{(η)}β, β⟩.
*Proof.* f̂(ξ) = ½(β̂(ξ − τ) + β̂(ξ + τ)), so |f̂|² = ¼|β̂(ξ − τ)|² + ¼|β̂(ξ + τ)|² + ½Re β̂(ξ − τ)\overline{β̂(ξ + τ)}.
Substituting ζ = ξ ∓ τ in the first two terms and using m(−t) = m(t),
(1/2π)∫m(ξ)(¼|β̂(ξ − τ)|² + ¼|β̂(ξ + τ)|²) = ½(1/2π)∫M_τ(ζ)|β̂(ζ)|² = ½m(τ)‖β‖² + ½D_τ(β) by Plancherel; the third term
gives ½X_τ(β). For the comb, cos(τx)cos(τ(x + u)) = ½cos(τu) + ½cos(τ(2x + u)), hence
c_f(u) = ½cos(τu)c_β(u) + ½∫β(x)β(x + u)cos(τ(2x + u))dx, and Σ_n v_n c_f(ℓ_n) = ½Σ_n v_n cos(τℓ_n)c_β(ℓ_n) + ½R_τ(β).
Finally ⟨A_τβ, β⟩ = ½Σ_n v_n cos(τℓ_n)[∫β(x)β(x + ℓ_n) + ∫β(x)β(x − ℓ_n)] = Σ_n v_n cos(τℓ_n)c_β(ℓ_n). ∎

Theorem 1.1 is an identity, not an approximation: the reduction of ROUND_012_A Prop. 3.1 is exactly the statement that
D + X − R is negligible, and ROUND_015_C showed it is not for the unrestricted maximisers (their β̂ sits at |ξ| ≈ τ, where
X and R are O(1)). The band restriction controls all three terms through the following leakage lemma.

**Lemma 1.2 (leakage of V_η). PROVED.** Let β ∈ V_η(τ). Then
(a) ê_k(ξ) = T^{−1/2} e^{iξT} a_k(1 − (−1)^k e^{−2iξT})/(a_k² − ξ²), so |ê_k(ξ)| ≤ 2a_k/(√T|a_k² − ξ²|);
(b) |β̂(ξ)|² ≤ (8/π) η³τ³ ‖β‖² / (ξ² − η²τ²)² for |ξ| > ητ;
(c) for η < θ ≤ 1: (1/2π)∫_{|ξ|>θτ} |β̂|² ≤ L(η, θ)‖β‖², L(η, θ) = (8/3π²)(η/θ)³(1 − η²/θ²)^{−2}. Write L₁ = L(η, 1).
*Proof.* (a) ∫_0^{2T} sin(a y)e^{−sy}dy = (a − e^{−2Ts}(s sin 2aT + a cos 2aT))/(s² + a²) with s = iξ, 2a_kT = kπ, and
x = y − T. (b) By (a) and Cauchy–Schwarz, |β̂(ξ)| ≤ (2/√T)‖β‖(Σ_{k∈K_η} a_k²/(ξ² − a_k²)²)^{1/2}
≤ (2/√T)‖β‖|K_η|^{1/2} ητ/(ξ² − η²τ²); insert |K_η| ≤ 2Tητ/π. (c) For |ξ| ≥ θτ, ξ² − η²τ² ≥ ξ²(1 − η²/θ²); integrate (b):
(1/2π)·2·(8/π)η³τ³(1 − η²/θ²)^{−2}∫_{θτ}^∞ ξ^{−4}dξ = (8/3π²)(η/θ)³(1 − η²/θ²)^{−2}. ∎
The bound (b) is attained in order by envelopes concentrated in a layer of width ≈ 1/(ητ) at ±T (b_k ∝ ±a_k): the
leakage is a boundary effect (β′(±T) ≠ 0), not a bulk one. Values: L₁ = 5.45·10⁻⁴ (η = ⅛), 4.80·10⁻³ (¼), 1.92·10⁻² (⅜).

**Lemma 1.3 (the archimedean symbol).** (i) PROVED: m is even and increasing on [0, ∞); m(0) = ψ(¼) − log π = −5.37218.
*Proof.* d/dt Re ψ(¼ + it/2) = −½ Im ψ′(¼ + it/2) and Im ψ′(a + iy) = Σ_{k≥0} Im (a + k + iy)^{−2}
= −Σ 2(a + k)y/((a + k)² + y²)² < 0 for y > 0. ∎
(ii) CITED (Stirling's series for ψ in Re z > 0) with NUMERICAL check: m(t) = log(t/2π) + r(t), r(t) = −1/(24t²) + O(t⁻⁴),
and |r(t)| ≤ 1/(20t²) for t ≥ 10 (t²r(t) = −0.04174, −0.04168, −0.041667 at t = 10, 50, 1000). (iii) |m(s)| ≤ 5.38 + log(1 + s)
for s ≥ 0 (from (i), (ii), and m(s) ≤ log(1 + s) on [0, 10] checked at 30 digits). Status of (iii): CITED + NUMERICAL.

**Proposition 1.4 (curvature term). PROVED (given Lemma 1.3(ii)).** For β ∈ V_η, η < θ< 1, (1 − θ)τ ≥ 10:
  D_τ(β) ≥ −‖β‖² [ η²/(2(1 − θ²)) + 1/(10(1 − θ)²τ²) + ½(m(τ) − m(0)) L(η, θ) ] =: −‖β‖² d(η, θ, τ).
*Proof.* For |ξ| ≤ θτ, τ ± ξ ≥ (1 − θ)τ ≥ 10, and Lemma 1.3(ii) gives
M_τ(ξ) − m(τ) = ½log(1 − ξ²/τ²) + ½(r(τ + ξ) + r(τ − ξ)) − r(τ) ≥ −ξ²/(2τ²(1 − θ²)) − 1/(10(1 − θ)²τ²), using
log(1 − s) ≥ −s/(1 − s) for s ≤ θ². Integrating, (1/2π)∫ξ²|β̂|² = ‖β′‖² ≤ η²τ²‖β‖². For |ξ| > θτ,
M_τ(ξ) ≥ ½(m(τ) + m(0)) by Lemma 1.3(i) (m(τ + |ξ|) ≥ m(τ), m(|τ − |ξ||) ≥ m(0)); the mass there is ≤ L(η, θ)‖β‖². ∎
The in-band part −½log(1 − ξ²/τ²) is the genuine price of the band: the symbol is concave across the band, so a band
of half-width ητ loses ≈ ⟨ξ²⟩/2τ² ≤ η²/2 of the margin. It does not vanish as τ → ∞; it is O(η²).

**Proposition 1.5 (cross terms). PROVED (X uses Lemma 1.3(iii)).** For β ∈ V_η:
  |X_τ(β)| ≤ √(2L₁)(5.72 + log τ)‖β‖²,   |R_τ(β)| ≤ 2√L₁ (Σ_{n<N} v_n)‖β‖².
*Proof.* R: with p_n(x) = β(x)β(x + ℓ_n), ∫p_n(x)e^{2iτx}dx = (1/2π)∫β̂(ξ)\widehat{β(·+ℓ_n)}(−2τ − ξ)dξ and
|\widehat{β(·+ℓ)}| = |β̂|. For every ξ, |ξ| ≥ τ or |2τ + ξ| ≥ τ; on each of the two regions apply Cauchy–Schwarz with
the factor living at frequency ≥ τ, whose L²-mass is ≤ L₁‖β‖² by Lemma 1.2(c): |∫p_n e^{2iτx}| ≤ 2√L₁‖β‖². Sum over n.
X: the integrand is symmetric under ξ → −ξ (β real, m even), so |X| ≤ 2·(1/2π)∫_{ξ≥0}|m(ξ)||β̂(ξ − τ)||β̂(ξ + τ)|
≤ 2‖β‖((1/2π)∫_{ζ≥τ} m(ζ − τ)²|β̂(ζ)|²dζ)^{1/2}. By Lemma 1.3(iii), m(ζ − τ)² ≤ (5.38 + 1/τ + log ζ)²; by Lemma 1.2(b),
|β̂(ζ)|² ≤ (8/π)η³τ³‖β‖²/(ζ²(1 − η²))²; and ∫_τ^∞(c + log ζ)²ζ^{−4}dζ ≤ (c + log τ + ⅓)²/(3τ³). Collecting,
(1/2π)∫… ≤ ½L₁(5.72 + log τ)²‖β‖². ∎

**Theorem 1.6 (band-restricted packet reduction). PROVED.** For β ∈ V_η(τ), η < θ < 1, (1 − θ)τ ≥ 10, f = β cos(τx):
  Q_T(f) ≥ ½‖β‖² [ m(τ) − ⟨A_τ^{(η)}β, β⟩/‖β‖² − E(η, θ, τ, T) ],
  E = d(η, θ, τ) + √(2L₁)(5.72 + log τ) + 2√L₁ Σ_{n<N} v_n,
and symmetrically Q_T(f) ≤ ½‖β‖²[m(τ) − ⟨A_τ^{(η)}β, β⟩/‖β‖² + |X|/‖β‖² + |R|/‖β‖² + D⁺], D⁺ ≤ 1/(10(1 − θ)²τ²)
+ (1/2π)∫_{|ξ|>θτ}(M_τ − m(τ))₊|β̂|²/‖β‖² (the last term is finite: M_τ grows like log|ξ| and |β̂|² ≲ ξ^{−4}).
Consequently the correct high-block condition is
  (HB_η)  λ_max(A_τ^{(η)}) ≤ m(τ) − κ − E(η, θ, τ, T) for all τ ≥ Ω_lo,
which gives Q_T(β cos τx) ≥ (κ/2)‖β‖² for all β ∈ V_η(τ). *Proof.* Theorem 1.1 with Propositions 1.4, 1.5; the
Rayleigh quotient of A_τ^{(η)} on V_η is ≤ λ_max(A_τ^{(η)}). ∎
**Transfer to W_T (P_T).** For β ∈ V_η, by Lemma 1.2(a) with s = −(½ ± iτ) in place of iξ, |⟨f, e^{±x/2}⟩| ≤
2e^{T/2}‖β‖(2η³/π)^{1/2}τ^{−1/2}/(1 − η² − 1/(4τ²)) (PROVED, same Cauchy–Schwarz), which is O(e^{−T/2}η^{3/2}‖β‖) at
τ ≥ Ω_lo; hence ‖P_T f − f‖²/‖f‖² = O(e^{−2T}η³). That Q_T(P_T f) − Q_T(f) is of the same order is ARGUED (it needs a
form bound for Q_T against the two exponentials restricted to the window; not written out). Measured: ≤ 10⁻⁴ (§2.3).

**How large is E?** The curvature part d is honest and small: optimised over θ, d = 0.022–0.025 (η = ⅛), 0.12–0.14 (¼),
0.37–0.45 (⅜) on T ∈ [1, 3] at τ = Ω_lo. The cross-term bounds are worst-case boundary-leakage bounds and are not small:
√(2L₁)(5.72 + log τ) = 0.32/0.39/0.45 (η = ⅛; T = 1/2/3), 0.95/1.14/1.34 (¼); 2√L₁Σv_n = 0.27/1.14/3.51 (⅛), 0.81/3.38/10.4 (¼)
(Σv_n = 5.85, 24.38, 75.19 at T = 1, 2, 3). The R bound grows like Σv_n ≍ e^T, so **Theorem 1.6 as proved does not
certify (HB_η) from the measured margins** at any T ≥ 1; the measured X, R (§2.3) are 10³–10⁴ times smaller than the
bounds. The obstruction is identified: Cauchy–Schwarz charges every comb term with the full boundary-layer leakage mass
L₁ (attained only by envelopes living in a 1/(ητ)-layer at ±T), while R_τ is an oscillatory sum Σ v_n e^{iτℓ_n}(…).
A sharp cross-term lemma (OPEN) must either exploit that the comb shift moves the boundary layer off the window
(β(x + ℓ_n) vanishes in the layer at x = T − ℓ_n only if β does) or replace V_η by an envelope class with β′(±T) = 0
to higher order (then (b) improves to η^{2j+1} with j vanishing orders — still a constant, not o(1)); only smooth
compactly supported envelope classes give genuinely o(1) cross terms.

## 2. Envelope margins m(τ) − λ_max(A_τ^{(η)}) at T = 1–3 (NUMERICAL)

Method. A_τ^{(η)} is the leading K × K block, K = ⌊2Tητ/π⌋, of the exact sine-Galerkin matrix of A_τ
(tools/A_tau_lmax.py closed forms). Because A_τ^{(η)} is the compression to the finite space V_η(τ), there is no basis
truncation: the issue of ROUND_015_C (Nb·π/2T < τ) does not arise, the space resolves exactly the band |ξ| ≤ ητ by
construction (K = 5–20 at T = 1–1.5, 62–673 at T = 2–3 for η = ⅛, up to 1346 for η = ¼ at T = 3). Convergence is
therefore a question of the τ-scan only: grid step, then bounded Brent polish of the grid minimum (|polish − grid| ≤ 0.02
in all runs), cross-checked by a 0.02-step rescan around the T = 3 minimiser (identical to 5 digits), and by a direct
evaluation of Q_T and W_T on the top eigenvector (§2.3). Scripts: scratchpad band.py / fine.py / direct_band.py
(same closed forms as tools/A_tau_lmax.py; not added to tools/).

### 2.1 Minimum margin

| T | τ-range scanned (step) | η = ⅛: min (τ − Ω_lo) | η = ¼ | η = ⅜ |
|---|---|---|---|---|
| 1.0 | [Ω_lo, 3Ω_lo] (0.02) | **0.888** (11.9) | 0.780 (3.43) | 0.624 (3.36) |
| 1.5 | [Ω_lo, 3Ω_lo] (0.03) | 0.544 (32.8) | **0.468** (1.60) | 0.429 (1.60) |
| 2.0 | [Ω_lo, 3Ω_lo] (0.06) η = ⅛; [Ω_lo, Ω_lo + 300] η = ¼ | **0.280** (39.5) | 0.275 (39.5) | 0.348 on [Ω_lo, Ω_lo + 25] |
| 2.5 | [Ω_lo, Ω_lo + 400] (0.08) η = ⅛; [Ω_lo, Ω_lo + 25] others | **0.256** (243.0) | 0.279 (window) | 0.276 (window) |
| 3.0 | [Ω_lo, Ω_lo + 300] (0.25) + fine rescan η = ⅛; single cell η = ¼ | **0.114** (30.9, τ = 2819.236) | 0.114 (same cell) | not computed (build > 15 min) |

(Ω_lo = 51.07, 138.82, 377.36, 1025.76, 2788.30.) At the far end the margin is large (η = ⅛: 1.78/1.65/1.66 at 1.5Ω_lo for
T = 1/1.5/2; 0.68 at 1.2Ω_lo for T = 3): the minimum sits in the first ≈ 5% of the high range for T ≤ 2 and T = 3, but at
τ − Ω_lo = 243 (≈ 1.24Ω_lo) for T = 2.5, so a scan of only [Ω_lo, Ω_lo + 20] (as in ROUND_015_C) misses the minimum
(T = 2: 0.349 on the short window vs 0.280 on the full range). The T = 2.5 and T = 3 values are minima over partial
ranges: upper bounds for the true minimum over [Ω_lo, 3Ω_lo].

**Dependence on η.** Weak once T ≥ 2: at the minimising cell the top envelope already lies in |ξ| ≤ τ/8 (η = ⅛ and ¼ agree
to 0.005 at T = 2 and to 0.0002 at T = 3). At T ≤ 1.5 a larger band lowers the margin by 0.1–0.26 (bands contain more of
the oscillating directions). ROUND_013_B's T ≥ 2 values (0.273/0.255/0.114 at Nb = 400) are, in hindsight, band-restricted
values with η ≈ Nb·π/(2Tτ) ≈ 0.11–0.8: they coincide with the η = ⅛ column at T = 3 (0.114).

**Trend.** min margin (η = ⅛): 0.888, 0.544, 0.280, ≤ 0.256, ≤ 0.114 at T = 1, 1.5, 2, 2.5, 3: positive, decreasing,
roughly linearly ≈ −0.37 per unit T from T = 1 to 3, with the T = 2 → 2.5 step small and T = 2.5 → 3 large (partial ranges;
location jumps between cells). Linear extrapolation gives a zero crossing near T ≈ 3.3; this is a NUMERICAL warning, not a
result: the measured margin is O(0.1) at T = 3 and falling.

### 2.2 cΛ budget

c* = min_τ m(τ)/λ_max(A_τ^{(η)}) (the condition for cΛ is λ_max ≤ m/c, since A scales linearly):
T = 1: 1.627 / 1.531 / 1.406 (η = ⅛/¼/⅜); T = 1.5: 1.197 / 1.178 / 1.160; **T = 2: 1.072 (η = ⅛), 1.071 (¼); T = 3: ≤ 1.022
(η = ⅛, over [Ω_lo, Ω_lo + 300]), 1.051 over the short window [Ω_lo, Ω_lo + 20] (¼)**. The budget tends to 1 as T grows.

### 2.3 Direct check of the reduction (Theorem 1.1 error terms measured)

Q_T and W_T (after the P_T projection) evaluated directly on f = β* cos(τx), β* the top eigenvector of A_τ^{(η)}, FFT
quadrature with 2^15–2^18 points (zero padding ×16), exact comb:

| (T, τ, η) | m − λ_max | Q_T(f)/‖f‖² | W_T(P_T f)/‖·‖² | D + X (arch) | −R (comb) | ‖P_Tf − f‖²/‖f‖² |
|---|---|---|---|---|---|---|
| (1.5, 140.42, ⅛) | 0.9154 | 0.9123 | 0.9123 | −0.0031 | 0.0000 | 1.1·10⁻⁶ |
| (1.5, 140.42, ¼) | 0.4684 | 0.4434 | 0.4434 | −0.0256 | −0.0006 | 8.6·10⁻⁶ |
| (1.5, 140.42, ⅜) | 0.4287 | 0.4025 | 0.4026 | −0.0264 | −0.0002 | 1.2·10⁻⁵ |
| (2.0, 416.86, ⅛) | 0.2797 | 0.2796 | 0.2796 | −0.0000 | −0.0000 | 2.2·10⁻⁹ |
| (2.0, 416.86, ¼) | 0.2749 | 0.2756 | 0.2756 | −0.0001 | −0.0008 | 8.7·10⁻⁹ |
| (2.5, 1046.66, ⅛) | 0.3411 | 0.3416 | 0.3416 | −0.0002 | −0.0008 | 9·10⁻¹⁰ |
| (2.5, 1028.78, ⅜) | 0.2760 | 0.2599 | 0.2599 | −0.0279 | −0.0117 (2^15 grid) | 2.5·10⁻⁸ |
| (3.0, 2819.24, ⅛) | 0.1140 | 0.1158 | 0.1158 | −0.0000 | −0.0018 | 5·10⁻¹¹ |

(error columns are (2·arch − m‖β‖²)/‖β‖² and −(2·comb − λ‖β‖²)/‖β‖², i.e. D + X and −R of Theorem 1.1 per ‖β‖²; the
comb column at 2^15 points carries a linear-interpolation error ≈ 10⁻²: at (2.5, 1046.66, ⅛) it drops from −0.0110 to
−0.0008 at 2^17 points.) The reduction is accurate to ≤ 0.002 for η = ⅛ and to ≤ 0.03 for η = ⅜, the larger error being
the curvature term D (Proposition 1.4: ≈ −⟨ξ²⟩/2τ²), as predicted; X and R are ≤ 2·10⁻³, against worst-case bounds
of order 1–10 (§1). The projection to P_T changes nothing at the fourth digit. No negative direct value.

## 3. λ_A(1.5) at high precision (NUMERICAL)

tools/galerkin_mp.py, T = 1.5, true Λ comb; Galerkin minimum of Arch − Π on P_T (both sectors); the bottom vector is even
in every run.

| N | dps | nodes | Galerkin λ_A | other sector | est. Arch entry error |
|---|---|---|---|---|---|
| 60 | 150 | 30 | 1.285·10⁻⁵¹ | 2.32·10⁻⁴⁹ | 4.7·10⁻⁷⁶ |
| 80 | 80 | 30 | 4.2095043·10⁻⁶¹ | 1.46·10⁻⁵⁸ | 2.2·10⁻⁷⁴ |
| 80 | 150 | 30 | 4.2095043·10⁻⁶¹ (identical) | 1.46·10⁻⁵⁸ | 2.2·10⁻⁷⁴ |
| 100 | 80 | 30 | 9.692·10⁻⁶⁹ | 3.68·10⁻⁶⁶ | 2.6·10⁻⁷³ |
| 120 | 150 | 40 | 1.047·10⁻⁷⁴ | 8.69·10⁻⁷² | 9.0·10⁻¹⁰⁷ |
| 140 | 150 | 40 | 1.911·10⁻⁷⁹ | 1.41·10⁻⁷⁶ | 4.8·10⁻¹⁰⁶ |
| 160 | 150 | 40 | 5.085·10⁻⁸³ | 8.00·10⁻⁸⁰ | 1.8·10⁻¹⁰⁵ |

Sign: every Galerkin value is **positive** and exceeds the matrix error by ≥ 12 orders (dps 80 and 150 agree to 8 digits at
N = 80, so precision is not the limit; the dps-30 negatives of ROUND_015_C were quadrature noise). Magnitude: a Galerkin
minimum is an upper bound for λ_A (Rayleigh–Ritz, up to the matrix error), so these runs give 0 < Galerkin value and
**λ_A(1.5) ≤ 5.1·10⁻⁸³** (NUMERICAL); they do not give a lower bound, and the true sign of λ_A(1.5) is not decided by an
upper bound. Convergence: log₁₀ = −50.9, −60.4, −68.0, −74.0, −78.7, −82.3; successive drops per 20 modes 9.5, 7.6, 6.0,
4.7, 3.6 decay with ratio ≈ 0.77–0.79, a geometric extrapolation gives a limit near 10⁻⁹⁵ (±5 orders). The law
−ln λ_A ≈ 4πe^{2T} = 252.4 predicts 10⁻¹⁰⁹·⁶. The Galerkin sequence has not converged at N = 160 and is still 27 orders
above the law; it is compatible with the law only if the drops decay more slowly than geometric. Resolving 10⁻¹¹⁰ needs
N well above 160 (build time ≈ 5 min at N = 160, dps 150; the eigen-solve dominates beyond). Status: **λ_A(1.5) unresolved
in magnitude; all Galerkin evidence positive, upper bound 5.1·10⁻⁸³.**

## Falsifier note

No sign step is made: Theorem 1.6 is an exact reduction plus error bounds, valid for every comb (v_n arbitrary real
weights, any finite set of ℓ_n < 2T; Propositions 1.4–1.5 use only Σ|v_n| — for signed weights replace Σv_n by Σ|v_n|).
It therefore holds verbatim for (a) cΛ, (b) a_P, (c) Beurling systems, (d) finite weight modifications, as it must
(it is a structural identity, not a positivity argument). The condition (HB_η) is what distinguishes them, and
numerically (a) is rejected only for c > c*(T) (c* = 1.07 at T = 2, ≤ 1.022 at T = 3): (HB_η) is a necessary condition
whose budget shrinks to 1 with T; it is not itself a proof of anything. (b)–(d) not run.

## Result

PROVED piece + NUMERICAL. (1) Exact packet identity (Theorem 1.1) and band-restricted reduction (Theorem 1.6): for
envelopes in V_η, Q_T(β cos τx) ≥ ½‖β‖²[m(τ) − ⟨A_τ^{(η)}β,β⟩/‖β‖² − E], with explicit E = curvature + leakage terms;
the correct high-block condition is (HB_η) λ_max(A_τ^{(η)}) ≤ m(τ) − κ − E. (2) NUMERICAL: the band-restricted margin
is positive at every T ∈ {1, 1.5, 2, 2.5, 3} and every η tested, minimum 0.888/0.544/0.280/≤0.256/≤0.114 (η = ⅛),
η-insensitive for T ≥ 2, decreasing with T; direct W_T on the extremal envelopes agrees to ≤ 0.002 (η = ⅛). (3) λ_A(1.5):
all Galerkin values positive and above the error floor, ≤ 5.1·10⁻⁸³ at N = 160; not converged; magnitude unresolved.

## What was proved

Theorem 1.1 (exact identity with three explicit error functionals), Lemma 1.2 (closed-form ê_k and leakage of V_η),
Lemma 1.3(i) (monotonicity of m), Proposition 1.4 (curvature term ≥ −η²/2(1 − θ²) − … ; uses the cited Stirling bound),
Proposition 1.5 (cross-term bounds), Theorem 1.6 (band-restricted reduction and condition (HB_η)); bound on the P_T
correction (the transfer of the inequality from Q_T to W_T is ARGUED).

## What failed and why

The proved error E is not small: the cross-term bounds (2√L₁Σv_n ≍ e^T, √(2L₁)log τ) exceed the measured margins at every
T ≥ 1 (e.g. T = 2, η = ⅛: E ≥ 0.02 + 0.39 + 1.14 against margin 0.28), so Theorem 1.6 does not certify (HB_η) from the
numbers. Cause: Cauchy–Schwarz charges each comb term with the full leakage mass L₁ of the boundary layer at ±T (Lemma 1.2
is attained by envelopes with β′(±T) ≍ (ητ)^{3/2}‖β‖), while the measured X, R are ≤ 2·10⁻³. The margin itself decreases
with T (0.114 at T = 3 on a partial range) and c* → 1.

## Next concrete step

(i) Sharp cross-term lemma: bound R_τ(β) = Re Σ v_n e^{iτℓ_n}∫β(x)β(x + ℓ_n)e^{2iτx}dx by integrating by parts against the
2τ phase with the boundary terms β′(±T)β(±T ∓ ℓ_n) written out, aiming at |R| ≤ C(η)Σv_n/τ^{1/2} + (boundary-layer term
in which β(±T ∓ ℓ_n) is small); or replace V_η by the class β = χ·γ with a fixed smooth cutoff χ (o(1) leakage).
(ii) Complete the τ-range at T = 2.5, 3 (full [Ω_lo, 3Ω_lo]) and add T = 3.5 for η = ⅛ to decide whether the margin
crosses zero (projected ≈ 3.3); this needs a matrix-free top-eigenvalue routine (K ≈ 2000 at T = 3.5).
(iii) λ_A(1.5): N = 200–240 at dps 150 to test geometric vs slower decay of the Galerkin sequence.

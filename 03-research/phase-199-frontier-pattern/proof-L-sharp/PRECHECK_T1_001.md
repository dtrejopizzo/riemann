# PRECHECK_T1_001 — exact Λ-free exterior form on prolate tails, μ = 10, 15, 20, 30 (NUMÉRICO pre-check of M3 / T1)

Phase 199, numerical analyst. No equivalence of any kind is
invoked. **No zero data is used anywhere**: the exterior form is evaluated from its definition, using only the
archimedean symbol, the pole and the weights log n (a_n ≡ 1).
NO-GO / NUMÉRICO. Everything quantitative below is NUMÉRICO.

**Outcome in one line.**
- On the out-of-band tail of ψ₄ (c = 2πμ), the exact exterior form satisfies W_ext/(1−λ₄) = 0.976, 0.984, 0.972, 0.970 × ½D₄(μ)
  for μ = 10, 15, 20, 30.
- So M3's leading order is confirmed to 2–3 %, the sign is positive in every case, and the gauge projection Π changes
  nothing (relative change ≤ 2·10⁻⁹).
- The ratio does **not** visibly tend to 1 on 10 ≤ μ ≤ 30. It stays flat at ≈ 0.97–0.98. That residual is far smaller than
  the c^{−½} log c allowance.
- On the core vector (f(0) = f̂(0) = f(λ) = 0 in span{ψ₀,ψ₄,ψ₈,ψ₁₂}), the weight 𝔴_μ evaluated on the vector's **own** mass
  matches the value to within −9 … +7 %. D₄ (the Langer mass of ψ₄) is the wrong mass for this vector: against it the ratio
  is 0.69–0.82.
- The f* check at μ = 15 gives W_ext[Z r_{f*}] = 9.6·10⁻⁷⁰, against W_T(g*) = 4.76·10⁻⁷⁰. The non-core (edge) defect is
  therefore −4.9·10⁻⁷⁰ = **−51 %** of the chirp value. This is the lower end of AUDIT_L_SHARP_7's predicted −51…−78 %.
- The route lives: (M3) is not falsified at leading order. No sign theorem is claimed, and row D stays OPEN.
  **[ corrección AUDIT_8: "route lives" = no-falsificación únicamente. El zero-test que certifica el
  pipeline es parcial (no ejercita los Li₁/Li₂/L_s de la cola); sólo el chequeo de fuerza bruta (10⁻⁴, ψ₄, μ=10)
  cubre esa ruta. "M3 confirmed at leading order" es justo sólo en el sentido log μ; el término de orden siguiente
  no está modelado.]**

## 0. Corpus / index check, and why this is not a retry
- **Read:** SYNTHESIS_MECHANISM_001 (§3.3 M3, §6 T1 and pre-check), AUDIT_L_SHARP_7 (§4–§5: Π, the edge −51…−78 %, T1
  ill-posed as stated), A_001 (Thm 1.1, Rem 1.1(ii),(iv)), E_001 (Thm E.2, Cor E.3, the killing-term correction §1),
  U_001 (U.2: ℓ = λ‖Πρ‖², 𝒢̄ = (𝒮(1,1)⁺)^⊥), MORI15_EXTREMAL_001 (a_k, 1−λ_k), W_001 (caustic), and ROUTES-TRIED-INDEX
  l.467–471.
- **Why it is new.** No entry evaluates the exact exterior form 𝒲_ext on a prolate continuation. Previous evaluations used
  deep bumps (E.5, J.3), endpoint data (S.3–S.4), radical vectors (TEST_CG) or the window form (MORI15). This memo is the
  pre-check that SYNTHESIS §6 and AUDIT_7 §5 asked for. It launches no construction.

## 1. What was computed (exact definitions, ρ-units)
Setting:
- λ = √μ, c = 2πμ. Prolates ψ_k live on [−1,1] at bandwidth c, with ψ^λ(x) = λ^{−½}ψ_k(x/λ) ([−λ,λ]-normalised).
- f̂ uses e^{−2πixξ}. Then ρ(t) := r(λt) = f̂(λt) for t > 1, and for ψ_k this is ρ_k = λ^{½}μ_kψ_k(t), where ψ_k(t) is the
  analytic continuation of ψ_k beyond the interval.

Exterior form (A_001 Thm 1.1 + E_001 Cor E.3, translation to s = x − a as in U_001 §2):
  W_ext = λ·𝔔[ρ],  𝔔[ρ] = 𝒜[φ] − 2⟨φ, φ_log⟩ + 2A·B,
  φ(s) = e^{s/2}Σ_{n≥1}ρ(ne^s), φ_log(s) = e^{s/2}Σ_{n≥2}(log n)ρ(ne^s), s > 0,
  𝒜[φ] = (1/2π)∫Θ_∞(τ)|Fφ(τ)|²dτ, Θ_∞(τ) = Re ψ(¼+iτ/2) − log π,
  A = ∫φe^{−s/2}, B = ∫φe^{s/2}.
- 𝒜 is the complete archimedean form of the zero-extended φ, so it includes E_001's killing term. It is Mori's a(t), with
  pole 2AB.
- The leakages are ‖r‖² = 2λ∫_1^∞ρ² (two-sided) and ℓ = 2λ∫_1^∞|Πρ|².

Numerical pipeline (scripts in `PRECHECK_T1_001_scripts/`):
1. **Prolates (mp, 112–234 digits).** Normalised-Legendre tridiagonal with Rayleigh-quotient iteration, giving χ_k,
   μ_k = √2 d₀/ψ_k(0), λ_k = μμ_k², ψ_k(0) and ψ_k(1). At μ = 15: 1−λ₀ = 9.40069·10⁻⁸¹ and 1−λ₄ = 1.166825·10⁻⁷⁰, both
   equal to MORI15.
2. **Continuation y_k = ψ_k/ψ_k(1) on (1, 4c].**
   - Start: Frobenius series at the regular singular point t = 1 (mp).
   - Then DOP853 at rtol 10⁻¹³, on a grid uniform in the Langer phase c√(t²−1). This grid is needed: a uniform t-grid
     misses the √(t−1) oscillation and gave a 10 % leak error.
   - Beyond 4c: the exact asymptotic series y = Re[Be^{ict}Σβ_m t^{−m−1}] (recurrence from the ODE). B is fitted at 4c and
     is stable to 4·10⁻¹².
   - Checked against the direct Bessel–Legendre integral at 1.0005 and 1.01 to 10⁻⁸.
3. **Leak verification (replaces the Nyström check).** 2λ_kψ_k(1)²∫_1^∞y_k² = 1−λ_k to 6·10⁻⁵ relative (ψ₄, μ = 15). The
   leak2 column below equals 1−λ_k to ≤ 9·10⁻⁵ for all μ.
4. **Dilate sums.**
   - Split ρ = Re[b₀e^{ict}]/t + Re[b₁e^{ict}]/t² + ρ_rest.
   - The first two pieces are summed over **all** n in closed form: Li₁, Li₂ for φ, and L_s(z) = Σ log n zⁿ/nˢ (s = 1, 2)
     for φ_log. These come from the ζ/ζ′ series of Li_s(e^{−w}), verified against mpmath to 10⁻⁹.
   - ρ_rest is summed directly for n ≤ 4c/v, with a geometric b₂-remainder.
   - Spot-checked against brute-force sums to n = 4·10⁶ (agreement ≤ 10⁻⁴, ψ₄, μ = 10).
5. **Forms.**
   - Midpoint grid in s: v = m/μ is a resonance, and v = 1 is one of them.
   - 𝒜 by FFT up to Q = max(2·10⁵, 10cV), Nyquist ≥ 4Q.
   - Analytic 1/τ² tail from the jumps and log-singularities: the sawtooth jumps at cv ∈ 2πℤ, of size π|Im b₀|v^{−½}, plus
     the ends.
   - Parseval check to ≤ 7·10⁻⁵. Halving h and doubling Q changes 𝔔 by ≤ 10⁻⁸ relative.
   - Truncation in s ≤ log V, with V = 25 … 800, extrapolated (increments halve per doubling of V).
6. **Pipeline zero-test (exact).** For a pure gauge datum (ψ(y) = y²(1−y²)³(1−by²), ∫ψ = 0, so Ef ≡ 0 on the window and
   W_T = 0, which by Thm 1.1 forces 𝒲_ext = 0):
   - arch = −4.0495·10⁻⁴, prime = −5.52·10⁻⁶, pole = +4.1045·10⁻⁴;
   - **sum = −1.4·10⁻⁸** (3·10⁻⁵ of the pieces).
   This fixes every convention (Θ_∞, the factor 2 in the collapsed prime term, 2AB, the killing term).
   **[ corrección AUDIT_8: este zero-test es PARCIAL. El dato de gauge puro tiene c = 2π (baja frecuencia)
   y b ≡ 0, de modo que el camino de forma cerrada Li₁/Li₂/L_s usado en cada chirp prolato no se ejerce aquí. El
   dato también está truncado en t ≤ 3000, descartando la cola j_j(2πt) ~ 1/t. El valor −1.4·10⁻⁸ valida Θ_∞, el
   factor 2 y 2AB; no valida la suma de la cola de alta frecuencia. Esa ruta sólo la cubre el chequeo de fuerza
   bruta (10⁻⁴, ψ₄, μ = 10). Etiqueta: validación PARCIAL (NUMÉRICO).]**
7. **Canonical projection Π (U.2).**
   - 𝒢̄ = closure{(1−P₁)ψ̂ : ψ ∈ L²_even(−1,1), ∫ψ = 0}, with basis ψ̂_j ∝ j_j(2πt), j = 2 … 80, and Gram condition 34.
   - ‖(1−Π)ρ‖²/‖ρ‖² ≤ 2·10⁻⁹ for every tail computed (≤ 10⁻¹⁵ on core vectors). The value is stable in J = 20/40/80.
   - So ℓ = ‖r‖² to 9 digits and **W_ext/ℓ = W_ext/‖r‖²**. Gauge-like (low-Mellin) components are absent from these
     chirps. AUDIT_7 §4.3's caveat therefore does not bite here.

## 2. Results
Notation:
- κ := W_ext/‖r‖² = 𝔔/(2∫_1^∞ρ²), and = W_ext/ℓ;
- P := ∫𝔴_μρ²/(2∫ρ²), the leading-order M3 value on the vector's own mass;
- ½D₄, with D₄ = ∫𝔴_μ m₄ and m₄ = (2/π)dω/(ω√(ω²−1)).
Extrapolated values are marked ∞; their uncertainty is about ±0.005 in κ.

**2.1 ψ₄ tail (the requested r = ψ̂₄|_{(λ,∞)}).**

| μ | κ (V=100) | κ (V=800) | κ (∞) | P | ½D₄ | κ/½D₄ | κ/P | ½log 2μ | 1−λ₄ | W_ext (V=800 or max) |
|---|---|---|---|---|---|---|---|---|---|---|
| 10 | 2.146 | 2.177 | 2.183 | 2.224 | 2.238 | **0.976** | 0.982 | 1.498 | 3.48934·10⁻⁴⁴ | 7.60·10⁻⁴⁴ |
| 15 | 2.447 | 2.480 | 2.486 | 2.514 | 2.526 | **0.984** | 0.989 | 1.701 | 1.166825·10⁻⁷⁰ | 2.894·10⁻⁷⁰ |
| 20 | 2.613 | 2.648 | 2.654 | 2.720 | 2.730 | **0.972** | 0.975 | 1.844 | 2.24502·10⁻⁹⁷ | 5.945·10⁻⁹⁷ |
| 30 | 2.885 | (V=400) 2.916 | 2.927 | 3.010 | 3.018 | **0.970** | 0.972 | 2.047 | 3.78427·10⁻¹⁵¹ | 1.104·10⁻¹⁵⁰ |

V-sequence 𝔔/∫ρ² at μ = 15: 4.713, 4.829, 4.894, 4.930, 4.951, 4.961 (V = 25 … 800).

**2.2 ψ₀ tail (comparison).** At V = 100, κ = 2.269 (10), 2.430 (15), 2.786 (20), 3.100 (30). The extrapolated values are
≈ 2.31, 2.47, 2.83, 3.15, which is **κ/½D₄ ≈ 1.03, 0.98, 1.035, 1.04**. ψ₀ sits slightly above the prediction and ψ₄
slightly below; both are within 4 %.

**2.3 Core vector** f ∈ span{ψ₀,ψ₄,ψ₈,ψ₁₂} with f(0) = f̂(0) = f(λ) = 0 (AUDIT_7's restatement of T1).
- Coefficients at μ = 15: (0.5191, −0.8547, 6.95·10⁻⁵, −4.1·10⁻¹²). The 1/t amplitude b₀ is 10⁻¹⁴ relative (f(λ) = 0 ✓),
  and f̂(0) = 10⁻²⁰¹.
- The 3-mode version, which imposes only f(0) = f(λ) = 0, agrees to 10⁻⁴.
- V-converged to 10⁻⁵.

| μ | κ | P (own mass) | κ/P | ½D₄ | κ/½D₄ | ½log 2μ | ‖r‖² | W_ext |
|---|---|---|---|---|---|---|---|---|
| 10 | 1.549 | 1.703 | **0.910** | 2.238 | 0.692 | 1.498 | 5.209·10⁻⁴⁴ | 8.07·10⁻⁴⁴ |
| 15 | 2.064 | 1.934 | **1.067** | 2.526 | 0.817 | 1.701 | 1.725·10⁻⁷⁰ | 3.56·10⁻⁷⁰ |
| 20 | 1.943 | 2.098 | **0.926** | 2.730 | 0.712 | 1.844 | 3.305·10⁻⁹⁷ | 6.42·10⁻⁹⁷ |
| 30 | 2.216 | 2.330 | **0.951** | 3.018 | 0.734 | 2.047 | 5.548·10⁻¹⁵¹ | 1.23·10⁻¹⁵⁰ |

κ > ½log 2μ in all four cases: this is M3's leading lower bound, B.0 of BRIDGE_001. The deviation from P is ±10 %,
non-monotone in μ, which is the size of SYNTHESIS's resonant (1,n) corrections (O(c^{−½}) ≈ 10 %). The core tail is
dominated by the ψ₈ continuation, because the condition f(λ) = 0 is met by a₈ψ₈(1) ≈ −a₄ψ₄(1). Its mass is shifted away from
m₄, so D₄ is not the right comparator for T1 as written. P is.

**2.4 f* consistency check (μ = 15).**
- f*₂ = 1.106365ψ₀ − 1.821723ψ₄:
  - ‖r‖² = 3.8725·10⁻⁷⁰ (= a₄²(1−λ₄) + a₀²(1−λ₀) ✓);
  - **W_ext[Z r_{f*₂}] = 9.606·10⁻⁷⁰** (V = 800; ∞: ≈ 9.63·10⁻⁷⁰), so κ = 2.486.
- With a₈ and a₁₂ added (f*₄), W_ext = 9.375·10⁻⁷⁰ at V = 100, against 9.476·10⁻⁷⁰ for f*₂ at V = 100: a 1 % effect.
- Mori's window value is W_T(g*) = 4.763·10⁻⁷⁰. The identity W_T = 𝒲_ext **does not hold here, and is not expected to**:
  f*(λ) ≠ 0 (J = g*(T) ≠ 0), so A_001 Thm 1.1 does not apply. Rem 1.1(iv) adds the β-block.
- The pipeline therefore reproduces the defect, not 4.76·10⁻⁷⁰: **W_T(g*) − 𝒲_ext[Z r_{f*}] = −4.87·10⁻⁷⁰ = −50.6 % of
  the chirp value**.
- This is exactly AUDIT_7 §4.4's lower end (−51 %, which assumed leak ≈ a₄²(1−λ₄)). So the (chirp, edge) block must carry
  −51 % at μ = 15. The edge channel is leading order, as AUDIT_7 said.
- The pipeline cannot split this defect further into Guo's 2f(λ)⟨h_p,XΨ_v⟩ + f(λ)²W_T(h_p), because p_λ is not
  implemented. **Edge value at μ = 15: −4.9·10⁻⁷⁰ in aggregate** (non-core defect).
- The pipeline's exactness is certified separately by the zero-test (§1.6), where Thm 1.1 does apply.

**2.5 The weight 𝔴_μ** (dense grid, ω ∈ (1, 10⁵]).

| μ | min 𝔴 | argmin | log 2μ | 𝔴(1.05) | 𝔴(1.5) | 𝔴(2) | 𝔴(3) | 𝔴(10) |
|---|---|---|---|---|---|---|---|---|
| 10 | 2.9957323 | 1.414229 | 2.9957323 | 3.539 | 3.002 | 4.016 | 4.918 | 8.119 |
| 15 | 3.4011974 | 1.414229 | 3.4011974 | 3.945 | 3.407 | 4.624 | 5.661 | 9.306 |
| 20 | 3.6888795 | 1.414229 | 3.6888795 | 4.232 | 3.695 | 5.056 | 6.189 | 10.149 |
| 30 | 4.0943446 | 1.414229 | 4.0943446 | 4.638 | 4.101 | 5.664 | 6.932 | 11.337 |

The minimum is log 2μ at ω = √2, which is the caustic τ = 2c. That point is tautological by AUDIT_7 §4.2 and proved
by BRIDGE B.0. D₄ = 4.4754, 5.0513, 5.4599, 6.0358, reproducing SYNTHESIS's table.

## 3. Verdict
1. **Sign.** W_ext > 0 on every tail computed: ψ₀, ψ₄, the core vector, and f*₂ / f*₄, for μ = 10, 15, 20, 30. The ratio
   is O(1)·log μ, between ½log 2μ and ½D₄. There is no polynomial loss.
2. **Leading order of M3.** κ(ψ₄)/½D₄ = 0.976, 0.984, 0.972, 0.970, and κ/P = 0.98–0.99 on ψ₄ and 0.91–1.07 on the core.
   The diagonal-dilate weight 𝔴_μ predicts the exact Λ-free form to 2–3 % on pure prolate chirps and to ±10 % on the core
   vector.
   - The ratio does **not** visibly → 1 on 10 ≤ μ ≤ 30. It is flat at ≈ 0.97–0.98 for ψ₄ and ≈ 1.03 for ψ₀.
   - That residual is about 5 % of the c^{−½}log c allowance at μ = 30.
   - Whether it decays like 1/log μ or tends to a constant ≠ 1 is not decidable at this range. Status: ARGUED → supported
     NUMÉRICO at leading order, with an unresolved 2–3 % offset.
3. **Gauge.** Π is irrelevant for chirps (≤ 2·10⁻⁹). So W_ext/ℓ = W_ext/‖r‖², and the gauge objection (AUDIT_7 §4.3,
   constraint 19a) does not affect this test.
4. **The MORI15 mismatch is the edge.** The pure chirp gives κ ≈ 2.49 at μ = 15. The certified extremal gives 1.23 because
   f*(λ) ≠ 0 adds −4.9·10⁻⁷⁰ (−51 %). The route therefore continues only through S3 (the 2×2 chirp/edge block), as AUDIT_7
   concluded. T1 must be restated with P (own mass), or with the core vector's Langer mass, in place of D₄.

**Labels.** All of §2 is NUMÉRICO. The zero-test, the leak identity and the Π-smallness are pipeline validations, not
theorems. M3 stays ARGUED, now with numerical support at leading order. T1, S1–S5, L′♯ and (★★) are OPEN. No sign is
claimed. Row D is OPEN.

**Do not retry.**
- The unprojected-vs-projected question on prolate chirps: settled, Π is negligible.
- Using the f* exterior form as a check of W_T: it is off-core, and the defect is the edge.

**Next.** Three steps follow from this memo:
- (i) S3: implement Guo's p_λ and split the −4.9·10⁻⁷⁰ into a cross term and an edge term;
- (ii) run μ = 50 and 80 to decide whether the 2–3 % offset decays;
- (iii) restate T1 with P.

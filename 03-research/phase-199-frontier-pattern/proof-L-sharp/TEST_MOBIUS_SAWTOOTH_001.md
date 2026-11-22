# TEST_MOBIUS_SAWTOOTH_001: is the κ-sawtooth of Mori V a Möbius sign pattern?

Phase 199 analyst memo. Labels follow the standard PROVED/CITED/CONDITIONAL/OPEN/NO-GO/NUMÉRICO convention.

**Status:** NUMÉRICO, using existing published data only. Nothing was certified and no Galerkin runs were made.

Script: `TEST_MOBIUS_SAWTOOTH_001.py` (mpmath + sympy, runs in under 1 s).

## Corpus check
- PATTERN_001 §2 is where the sawtooth was first observed.
- FF_001 and GG_001 give the Möbius tail c_N and D_μ = ζM_μ − 1.
- Lemma M (AUDIT_198) applies.
- ROUTES-TRIED-INDEX has no prior arithmetic test of Mori's table. Mori V §7 itself says the arithmetic explanation was "not tested".
- This memo is a data test, not a construction route.

## 1. Available data (task 1)
- **Mori V Table 1** is the only source of λ^Gal_min for μ ∈ [7, 20]. It gives the ratio κ = λ_min/(1 − λ₄(2πμ)) for the **even part only**, at the integers μ = 7, 11, …, 20.
  - The table has **no values at μ = 8, 9, 10**.
  - It has **no odd parity**.
  - It has **no non-integer μ**.
- **Precision of the values:**
  - The tabulated ratio has 3 significant digits. The stored λ has 8 digits.
  - Precision was checked only at μ = 17 and μ = 20.
  - μ = 18 and μ = 19 come from a single N each, so convergence in N is unverified there.
  - Every N/(ac) is between 2.67 and 5.6, which is at or above Mori's empirical threshold of 2.3. Under-resolution overestimates κ, for example 7.83 at μ = 20 with N = 350.
- **Only absolute value in hand:** λ(20) = 1.09899e−96. Mori's raw runs (`outputs/numerics-V/runs`) are not in the scratchpad copy, and `code.zip` is corrupt.
- **Other sources do not fit:**
  - Mori VI, VII and VIII give certified Schur margins (2.40e−70 / 3.95e−66 at μ = 15), which are a different quantity.
  - Paper 46 (μ = 5) gives the primitive form λ_A, which is not comparable.
- **Reconstruction check:** λ = κ·(1 − λ₄) was rebuilt using Fuchs × Mori's smooth correction factor 0.89 → 0.94. At μ = 20 it gives 1.103e−96, against the actual 1.099e−96.

## 2. Increments (task 2)
The contact m enters the window for μ > m, so the step μ = m → m + 1 is the one that adds m.

Columns:
- Δκ₄ = increment in Mori's ratio.
- Δlog for the three normalizations: 1 − λ₄, 1 − λ₂ (via Fuchs n = 2), and μ^{9/2}e^{−4πμ}.

| m | μ(m) | Λ(m) ≠ 0 | Δκ₄ | Δlog κ₄ | Δlog κ₂ | Δlog κ_scale |
|---|---|---|---|---|---|---|
| 11 | −1 | yes | −0.61 | −0.138 | +0.042 | −0.132 |
| 12 | 0 | no | +0.83 | +0.184 | +0.350 | +0.190 |
| 13 | −1 | yes | −0.39 | −0.082 | +0.072 | −0.076 |
| 14 | +1 | no | +0.08 | +0.017 | +0.162 | +0.024 |
| 15 | +1 | no | −0.14 | −0.031 | +0.104 | −0.025 |
| 16 | 0 | yes (2⁴) | +0.21 | +0.046 | +0.173 | +0.052 |
| 17 | −1 | yes | −0.32 | −0.071 | +0.050 | −0.065 |
| 18 | 0 | no | +0.96 | +0.198 | +0.312 | +0.204 |
| 19 | −1 | yes | −0.44 | −0.086 | +0.023 | −0.080 |

The steps for m = 8, 9, 10 cannot be tested because the table has no values at μ = 8, 9, 10.

**Scoring for the Möbius reading** (normalization 1 − λ₄, which behaves the same as μ^{9/2}e^{−4πμ}):

| class | expected | observed | hits |
|---|---|---|---|
| primes (μ(m) = −1) | Δ < 0 | 4/4 negative, effect −7% to −14% | 4/4 |
| μ(m) = +1 | Δ > 0 | 14 gives +1.7%; 15 gives −3.1% | 1/2 |
| μ(m) = 0 | Δ ≈ 0 | 12: +18%, 16: +5%, 18: +20% | 0/3 |

The μ(m) = 0 steps are the **largest** jumps in the whole table, the opposite of what the Möbius reading predicts.

**A competing von Mangoldt / contact reading fits better:**
- Steps where a prime power enters (11, 13, 16, 17, 19) go down in 4 of 5 cases. The exception is 16 = 2⁴, at +5%.
- Steps where no contact enters (12, 14, 15, 18) go up in 3 of 4 cases. The exception is 15, at −3%, which is within the 3-digit and convergence noise.
- An even simpler description: κ is high at every μ that is prime (11, 13, 17, 19), whatever happens at the step.

**The sign depends on the normalization:**
- With 1 − λ₂, every Δ is positive. The extra factor c² dominates.
- So a "positive jump" is not intrinsic. It exists only relative to a chosen smooth drift.
- By Lemma M, λ itself never increases. Here λ falls by about 5–6 orders of magnitude per unit μ, and every step is consistent with that.

## 3. Resolution needed and its cost (task 3)
- **The data are too coarse.** With only integer μ, a jump at μ = m cannot be separated from the smooth drift over (m, m + 1). Telling them apart needs λ_min at μ = m ± 0.05 and m ± 0.1 for m = 10, 11, 14, 15, about 15 values in total.
- **Double precision cannot resolve this.** λ_min ≈ 1e−48 to 1e−70, while the matrix entries are O(1), so the bottom eigenvalue sits below roundoff by 30 to 55 orders of magnitude.
- **Precision required:** about 18μ bits for the margin plus guard bits. Mori used 680–1300 bits with N = 300–570.
- **Mori's measured cost:** hours per run on 4 vCPUs. The README says the largest run takes about 50 minutes.
- **Estimated cost for this test:** at μ ≈ 10–15, N ≈ 300–370, about 700 bits, roughly 0.5–2 h per value, so about 10–25 h for 15 values. That is far above the 10-minute budget, so **the runs were not made**.
- **A cheaper relative Galerkin in mpmath** may be possible: a shift-and-invert approach in a fixed prolate-adapted basis with small N (≈ 100). It still needs ≥ 18μ bits, because the cancellation is in the form itself, not in the solver. It might bring the cost down to ~10 min per value, but that is unverified.
- **Cheapest decisive alternative: the jump at the contact itself.** At μ = m, the window form changes only by the term Λ(m)m^{−1/2}·(shift at log m). That shift's support enters at the window edge, so the first-order jump is 0 at μ = m. The Λ effect therefore shows up as a change of slope, not as a discontinuity. Coefficients for 14 and 15 are exactly 0, since Λ = 0 there.
- **This means the Möbius hypothesis has no mechanism at m = 14, 15 inside the window form.** The c_N of FF/GG live on the exterior datum and act at N ≥ μ. They do not add an integer-indexed term to the window form.

## 4. Verdict
**CONTRADICTED (NUMÉRICO)** on the data available.
- **Primes:** the 4/4 negative steps are real, but they are also predicted by the contact (Λ) reading.
- **μ(m) = +1:** the predicted positive jumps are not present (1/2, and the one hit is within noise).
- **μ(m) = 0:** the predicted absence of a jump fails worst. 12 → 13 and 18 → 19 are the largest jumps in the table.
- **Pattern that survives:** the data are compatible with the reading already in PATTERN_001. κ is lowered when a prime-power contact enters, with 16 as an exception, and drifts upward elsewhere. That drift is an artefact of normalizing by the 1 − λ₄ scale.
- **Limits:** this is n = 9 steps, from 3-digit even-parity data with unchecked convergence at μ = 18 and 19. A test at sub-integer resolution would cost about 10–25 h of Mori Galerkin.

Nothing here bears on the sign. Row D OPEN.

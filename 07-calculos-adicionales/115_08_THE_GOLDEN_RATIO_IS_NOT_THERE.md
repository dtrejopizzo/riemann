# 115.08 — The golden ratio in σ: an audit, and what the data do say

`115_04` produces the universal constant σ = e^{-(log 2)²}. Its value,
0.6185031378…, resembles 1/φ = 0.6180339887…. This note audits that
resemblance with measurements rather than impressions. Script:
`115_08_golden_ratio_audit.py`; full output in `115_08_resultados.txt`.
The two drawings of panels F and G, separately and enlarged, are in `115_09_*`;
the anatomy of the rays is in `115_10_*`.

**Incidental correction.** `115_04` wrote σ = 0.618505…; the correct value is
**0.618503**137801575983…. Corrected in the text.

## Result

σ ≠ 1/φ, and the difference is structural, not a matter of precision.

| | value |
|---|---|
| σ = e^{-(log 2)²} | 0.618503137801576 |
| 1/φ | 0.618033988749895 |
| relative separation | 7.59 × 10⁻⁴ (0.076 %) |

σ = 1/φ would mean (log 2)² = log φ, i.e. 0.480453014 = 0.481211825.
These are different numbers: they agree to 3 significant digits and differ in the 4th.

## The three measurements (`fig1`)

**A — where the 2 comes from.** The 2 in (log 2)² is not a universal constant:
it comes from `cor:cotangentRRdimension` counting **binary digits**,
r(m) ≈ log m / log 2. With a base-b code the construction gives
σ_b = e^{-(log b)²}. The golden value is reached at b\* = e^{√(log φ)} =
**2.0010946**, not at b = 2. The "appearance" of the golden ratio is exactly the
numerical fact log 2 ≈ √(log φ), and nothing more.

**B — calibrating the near-coincidence.** Within 7.6 × 10⁻⁴ of σ lie 3
constants from a catalogue of 2,201 simple combinations of π, e, φ, √2, ln 2,
γ, ζ(3), and 5 from a catalogue of 4,115 quadratics (p+q√d)/s of height ≤ 12.
Moreover, **e^{-γ/ζ(3)} = 0.618665854 is three times closer to σ than 1/φ**.
At this precision the golden ratio is not a distinguished neighbour; it is one
among eight, and wins only because it is the familiar one.

**C — the deciding test.** The theorem of `115_04` is
h⁰_t − h²_t = N_t·log(1/σ), and its content is that this equals
(log 2)²N_t = t²ab **with no spurious factor**. With σ = 1/φ the ratio
log φ/(log 2)² = 1.001579…, a spurious factor of 0.158 % at every t; since
N_t ~ t²ab/(log 2)², the absolute error grows like t² and diverges. The covolume
leaves no choice: σ is forced by `eq:finiteRRmetric`, and what it forces is not φ.

## In the primes or the zeros? (`fig2`)

**D2 is the important panel, and for a while it seems to support the golden
hypothesis.** On **100,118 zeros** of ζ up to height γ = 75,000, computed by
Riemann–Siegel with the C₀ correction, on segments where N = ⌊√(t/2π)⌋ is
constant (checks: 100,118 found against N(T) = 100,117.7 theoretical; error
1 × 10⁻⁴ against `mpmath` at γ₁₀₀ and γ₁₀₀₀), the statistic r (ratio of
consecutive spacings, independent of unfolding) gives

* measured, whole sample: **0.6109 ± 0.0007**
* asymptotic GUE: 0.5996 → at 15.8 σ
* 1/φ: 0.6180 → at 9.9 σ

With the small sample (22,491 zeros up to γ = 20,000) the same computation gave
0.6133 ± 0.0015, at 3.2 σ from 1/φ and 9.2 σ from GUE: there the golden ratio
seemed to win. With 100,000 zeros the advantage disappears: the global value is
neither constant, because **it depends on height**.

Splitting the sample into 12 bands and plotting ⟨r⟩ against 1/log(γ/2π), the
natural scale of the finite-height arithmetic corrections (Bogomolny–Keating),
the value **decreases monotonically** and the linear fit extrapolates to
infinite height at

> ⟨r⟩_∞ = **0.5965 ± 0.0026** → GUE at 1.2 σ, **1/φ excluded at 8.2 σ**.

Check with a quadratic term in 1/L, in case of curvature:
⟨r⟩_∞ = 0.5992 ± 0.0273, χ²/dof 0.15 (linear) against 0.16 (quadratic); the
linear fit suffices and the result does not move.

The excess over GUE decays like 1/log(height). φ is not a limit: it is a
transient value that the sample crosses around γ ~ 10³.

**E — φ against the primes.** Weyl sum |N⁻¹ Σ_{p≤p_N} e(αp)| over 148,933
primes: α = φ gives 0.00118, α = √2 gives 0.00143, both following N^{-1/2} (pure
noise). A genuine resonance looks like α = 1/2, which gives 0.99999. φ is generic
with respect to the primes.

**F, G, H — the drawings.** The primes in polar coordinates (p, p rad) **do**
form arms and rays, and so does the sunflower (√n, n·2π/φ²) (13, 21, 34). It is
the same mechanism, continued fractions, with two different numbers: the arms of
the primes are counted by the denominators of 2π (6, 44, 710), those of the
sunflower by those of φ (Fibonacci). Panel H measures the cause: q²|α − p/q|
drops to 0.007 at 710/113 for 2π, while φ sits at the Hurwitz floor
1/√5 = 0.447, being the worst approximable number. The primes speak of 2π; φ
appears where one puts it.

## Classification

* σ ≈ 1/φ: **NEAR-COINCIDENCE**, 0.076 %, with at least 7 competitors equally
  close and one (e^{-γ/ζ(3)}) closer. **No identity.**
* σ = 1/φ as a hypothesis: **REFUTED**; it breaks the exact equality of `115_04`
  by a spurious factor of 0.158 %.
* φ in the spacing statistics of the zeros: **REFUTED** at 8.2 σ after
  extrapolating in height, on 100,118 zeros up to γ = 75,000. The apparent
  agreement at γ ≲ 10⁴ is the finite-height arithmetic correction, and it
  dissolves as the sample grows.
* φ in the distribution of primes: **NEGATIVE**; generic in Weyl sums.
* What remains: the 2 in (log 2)² is the **2 of the binary code**. If one ever
  needs to understand where that constant comes from, the right question is why
  the coding of `perfectCotangentObject` is binary, not why σ resembles 1/φ.

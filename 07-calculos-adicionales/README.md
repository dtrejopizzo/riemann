# 07-calculos-adicionales — Side computations from phase 115

Numerical side-investigations tied to `03-research/phase-115-the-mixed-class-and-the-green-extension/`,
kept outside `03-research/` because they are exploratory audits of a numerical curiosity in that
phase's constant `σ = e^{-(log 2)²}`, rather than steps in the phase's own argument. **Neither
result bears on RH** — both are closed, self-contained numerical questions with definite answers.

## Contents

| File(s) | Question | Answer |
|---|---|---|
| `115_08_THE_GOLDEN_RATIO_IS_NOT_THERE.md`, `115_08_golden_ratio_audit.py`, `115_08_resultados.txt`, `115_08_fig*.png`, `115_08_zeros.npy` | Does `σ = e^{-(log 2)²} ≈ 0.618503` (from `phase-115`'s doc 04) coincide with `1/φ ≈ 0.618034` (the golden ratio)? | **No.** Relative separation `7.59×10⁻⁴` (0.076%) — structural, not a precision artifact: `σ = 1/φ` would require `(log 2)² = log φ`, and the two sides differ from the third significant figure on. Traces exactly where the "2" in `(log 2)²` comes from (binary-digit counting in the underlying construction, `r(m) ≈ log m / log 2`) to show the resemblance to `φ` is coincidental. |
| `115_09_spirals.py`, `115_09_fig_girasol_aureo.png`, `115_09_fig_primos_polar.png` | Supporting figures for `115_08` and `115_10`: a sunflower/golden-angle spiral panel, and a polar plot of the primes that motivated `115_10`'s question. | — (figures only) |
| `115_10_POR_QUE_SE_CURVAN_LOS_RAYOS.md`, `115_10_por_que_se_curvan_los_rayos.py`, `115_10_resultados.txt`, `115_10_fig_rayos.png` | In the polar plot `115_09_fig_primos_polar.png`, every ray bends the same way. Why? | An exact, elementary geometric identity: `113 · 2π = 710 − δ` with `δ ≈ 6.03×10⁻⁵` rad. Advancing the prime index by 710 rotates the point by exactly `δ`, independent of which ray — so every ray is the *same* arc of an Archimedean spiral (`r = 710(θ−θ_a)/δ`, pitch `≈1.18×10⁷`), just rotated. Not a new phenomenon; an exact consequence of `710 ≈ 113·2π`. |

## Status

Both questions are closed and answered; neither reopens or advances phase 115's own argument
(see `03-research/phase-115-the-mixed-class-and-the-green-extension/` for that). Kept for
traceability, per the program's candor principle — a numerical curiosity that looked like it
might be signal was checked and shown to be coincidence.

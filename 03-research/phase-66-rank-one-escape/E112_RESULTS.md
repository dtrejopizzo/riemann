# E112 — the true growth rate of ‖T_N‖ is sub-exponential: a border-extension target

**Date:** 2026-07-05 · `E112_TN_growth.py` (numpy/scipy, 64-node Gauss–Laguerre, exact overlap integrals).

## What was measured
The whitened prime operator T_N of `prop:laguerre-entries` (P52), built exactly:
`(T_N)_{jk} = -1/log(t0/2pi) Σ_n Λ(n)/√n [n^{-it0} m_{jk}(log n) + n^{it0} m_{kj}(log n)]`,
`m_{jk}(λ) = e^{-yλ} ∫_0^∞ L_j(x+2yλ)L_k(x)e^{-x}dx`. We measured `λ_max(T_N)` vs N at t0=1e6, y=1.

The prime sum converges **absolutely** (m_{jk}(log n) ~ n^{-y}·poly = n^{-1}·poly, terms Λ(n)n^{-3/2});
200000 prime powers is more than sufficient. Values at t0=1e6 are trustworthy.

## Result: sub-exponential growth in N
| N | 2 | 11 | 20 | 29 | 38 | 50 |
|---|---|---|---|---|---|---|
| λ_max(T_N) | 0.060 | 1.025 | 1.571 | 2.068 | 2.479 | 2.824 |

- **Exponential fit `log λ_max ~ βN`:** β keeps SHRINKING as the N-window extends
  (0.083 at N≤30 crude → 0.048 → **0.024** at N≤50, large-N). A genuine exponential has constant β;
  a shrinking β is the signature of **sub-exponential** growth.
- **Polynomial fit `log λ_max ~ a log N`:** a ≈ 0.67 (large-N), residual 0.28 vs exponential 0.57 —
  the polynomial model fits ~2× better. Growth is ≈ **N^{2/3}**, decelerating.

The whitening `1/log(t0/2π)` scaling holds approximately for t0 ≤ 1e6 (product λ_max·log flat within
~30%); the t0=1e8 point is unreliable (lower-order corrections / phase resolution) and is not used.

## Consequence (the border extension — honest scope)
`cor:loglog-effective` bounds `λ_max(T_N) ≤ c0 N^2 e^{βN}/log(|t0|/2π)` (a crude sup-norm bound on the
Laguerre functions), giving contractivity only for **N ≤ loglog|t0|/β**. The measurement says the TRUE
rate is `λ_max(T_N) ≈ C N^{a}/log(|t0|/2π)` with **a ≈ 2/3**, not exponential. Substituting the true rate
into the same derivation extends the effective contractivity range to
> **N ≤ (log|t0| / C)^{1/a} ≈ (log|t0|)^{3/2}** — a power of log, vs the current iterated log.

This is a genuine, below-RH, non-circular improvement of `cor:loglog-effective` (it is an operator-norm
statement, not a positivity/zero-location statement). **It does NOT close Ω₇:** the residue
`N ∈ ((log|t0|)^{3/2}, N_*(t0) ≍ t0² log t0)` remains open. It is a real extension of the border, not
the border meeting the center.

## Status / honest caveats
1. **Numerical evidence, not yet a theorem.** To upgrade `cor:loglog-effective` one must PROVE
   `‖T_N‖ = O(N^{a}/log|t0|)` with a<1 analytically — a concrete operator-norm bound on the compressed
   Laguerre-shift (Toeplitz-type) operator. This is the below-RH analytic task this experiment sets.
2. **Exponent uncertainty:** a ∈ [0.6, 0.7] from N≤50; the exact value (and whether it drifts further
   down toward √N or log) needs larger N and multi-t0 confirmation.
3. **Normalization:** E112's T_N is a fresh construction from `prop:laguerre-entries`; absolute λ_max
   may differ from P52's convention by constants (does not affect the growth EXPONENT, which is the
   claim). A calibration against the P52 harness (h8lab.py) is the next check before amending P52.

## Next
(i) Extend N to ~100 and 2–3 values of t0 to pin a and confirm the 1/log scaling.
(ii) Attempt the analytic bound `‖T_N‖ = O(N^{2/3}/log|t0|)` (compressed Toeplitz/Laguerre-shift norm).
(iii) If (ii) holds, amend `cor:loglog-effective` in P52 with the extended range.

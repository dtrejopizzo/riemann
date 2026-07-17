# Calibration of E112/E113 against the P52 harness — FAILED (findings do not transfer)

**Date:** 2026-07-05. Essential honesty check before any P52 amendment (E113_RESULTS §caveat).

## The test
Compare the whitened prime operator's top eigenvalue vs N:
- **Exact (h8lab.py):** `δ_N = gen_min_eig(J_arith, A_N)`, i.e. matrix whitening by the archimedean
  Pick jet `A_N^{-1/2}`; `λ_max(A_N^{-1/2} Plam A_N^{-1/2}) = 1 - δ_N`.
- **E113:** scalar whitening by `1/log(t0/2π)` (leading Szegő factor of prop:laguerre-entries).

## Result (zeta, z0 = t0 - i):
| | N=4 | 8 | 12 | 16 | 20 |
|---|---|---|---|---|---|
| exact λ_max, t0=100 | 0.991 | 1.000 | 1.000 | 1.000 | 1.000 |
| exact λ_max, t0=1000 | 0.743 | 0.99998 | 1.000 | 1.000 | 1.000 |
| E113 scalar λ_max, t0=1e6 | ~0.6 | ~0.9 | ~1.1 | ~1.3 | ~1.6 (→2.27 sat) |

The exact operator has **λ_max → 1** (δ_N → 0⁺, marginal — "ζ at the de Branges boundary", as
AUDIT.md already established). The E113 scalar operator has **λ_max → 2.27 > 1** (would mean δ_N<0).

## Verdict
The scalar whitening `1/log(t0)` is NOT the paper's archimedean whitening `A_N^{-1/2}`. The matrix
whitening exactly balances the prime part to the margin λ_max=1; the scalar approximation destroys this
marginality. **E112 and E113 describe the wrong (leading-order scalar) operator.**

Therefore, RETRACTED as P52-relevant:
- the "sub-exponential N^{2/3}" and loglog→(log)^{3/2} border extension (E112);
- the Toeplitz structure / symbol = -ζ'/ζ on the critical line, ‖T_N‖ saturation, and the reframing
  "residue is t0-uniform not N-uniform" (E113).
These are properties of the scalar-approximate operator, not of P52's exact terminal defect.

## What actually holds
The exact operator confirms P52's stated picture: δ_N is marginally positive and → 0⁺ super-fast in N
(hitting the dps floor by N~24); the open problem is δ_N ≥ 0 for ALL N, exactly as `subsec:live-step5`
states. Nothing in Phase 66 amends P52.

**Lesson (add to protocol):** any operator built from a *leading-order* approximation of the archimedean
whitening must be calibrated against the exact `A_N^{-1/2}` (h8lab) BEFORE any structural claim; the
marginality of ζ is invisible to scalar approximations.

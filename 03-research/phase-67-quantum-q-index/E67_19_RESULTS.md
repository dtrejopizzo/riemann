# E67.19 -- honesty check: the Toeplitz structure is only approximate

**Date:** 2026-07-06.
**Script:** [E67_19_toeplitz_exactness.py](E67_19_toeplitz_exactness.py).

## Finding (A): not asymptotically Toeplitz

Band deviation of the jets vs N (z0=100-i):

| N | dev(A_N) | dev(P_lambda) |
|---|---|---|
| 6  | 0.228 | 0.099 |
| 10 | 0.228 | 0.149 |
| 14 | 0.227 | 0.165 |
| 16 | 0.226 | 0.170 |

`dev(A_N)` plateaus near 0.227; `dev(P_lambda)` GROWS with N (0.10 -> 0.17). The jets are **not**
asymptotically Toeplitz. The ~20% band deviation does not vanish.

## Finding (B): the zeta touch point

Clean quadratic touch at `theta* ~ 1.54` (near pi/2), `sigma_min = +0.037` (positive, marginal),
`sigma_min` decreasing with N (0.045 at N=12 -> 0.037 at N=16), consistent with an exact touch at 0 in
the limit. Descriptive, but heuristic by (A).

## Consequence -- temper the optimism honestly

- The symbol-positivity detector (E67.16-18, saved to 02-foundations) remains a **faithful
  leading-order detector**: it works because the Toeplitz part is dominant.
- But it is **not a rigorous reduction**. Since the jets are not genuinely Toeplitz (deviation ~0.2,
  non-vanishing, and growing for P_lambda), constant-symbol Szego / Fisher-Hartwig theory CANNOT be
  invoked to force `sigma >= 0`. The E67.18 Szego law held numerically because the symbol governs the
  leading eigenvalue distribution, not because the operator is exactly Toeplitz.
- The growth of `dev(P_lambda)` with N points to a **position-varying symbol**: the object is closer to
  a *pseudodifferential* operator (Widom / Guillemin-Sternberg theory for varying symbols) than to a
  fixed-symbol Toeplitz operator. The naive band symbol is only the leading term.

## Revised state

```
detector   : symbol nonnegativity, faithful, leading-order (kept in foundations, caveated)
NOT rigorous: jets are not asymptotically Toeplitz (dev ~0.2, P_lambda growing)
refinement : the true object is pseudodifferential (varying symbol) -- Widom theory, more subtle
open forcer: unchanged -- and cannot be closed by constant-symbol Szego
```

No regression: the detector is still beautiful and useful, and Omega_7 is exactly as open as before.
The honest correction is that the Szego/Fisher-Hartwig rigor is not available here; the varying-symbol
(pseudodifferential) refinement is the real object, and it is harder.

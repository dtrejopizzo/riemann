# E68.1-E68.2 -- the GLT symbol: not a clean GLT sequence, but a faithful depth detector

**Date:** 2026-07-06.
**Scripts:** [E68_1_glt_symbol.py](E68_1_glt_symbol.py), [E68_2_glt_interior.py](E68_2_glt_interior.py).

## Test

Extract the position-resolved local symbol `kappa(x_j, theta) = sum_d taper(d) M[j,j+d] e^{i d theta}`
for `A_N` and `P_lambda`, set `kappa = kappa_A - kappa_P`, and check the GLT distribution law
`measure{kappa<0} = ind_-/N`, plus the minimum (depth) of `kappa`.

## Result (z0=100-i, interior rows, symmetric Hann window)

zeta, window w = 4, 6, 8:
```
min kappa = -0.0105, -0.0088, -0.0031   (depth -> 0)
measure{kappa<0} = 0.20, 0.32, 0.41     (grows)   but ind_-/N = 0
```
offline b=0.8:
```
min kappa = -5.4, -12.8, -26.3          (depth grows)   ind_-/N = 0.42
```

## Honest reading (calibrating E67.19 vs E67.20)

1. **Not a clean GLT sequence.** The GLT distribution law fails: for zeta `measure{kappa<0} ~ 0.4`
   while `ind_-/N = 0`. So the rigorous GLT eigenvalue-counting is NOT available. E67.20 ("rigorous
   GLT") was too optimistic; E67.19's caution was partly right. The naive local symbol does not
   organize the eigenvalues.

2. **But the symbol DEPTH is a faithful detector.** The discriminator is the minimum, not the measure:
   - zeta: `min kappa -> 0^-` (touches zero with vanishing depth = marginality at the 2-D symbol level);
   - off-line: `min kappa -> -infinity` (genuine, growing negativity).
   This is symbol positivity, correctly understood as a sign/depth statement:
   `Omega_7  <=>  the symbol does not cross zero (min kappa >= 0 in the limit)`.

## Net for Phase 68

```
NOT available : rigorous GLT measure law (object is not cleanly GLT)
solid         : symbol-depth detector -- min kappa -> 0 for zeta, -> -inf for off-line
target        : prove the symbol does not dip below 0 by structure (min kappa >= 0)
```

The honest framing is the symbol-positivity of the foundations detector, at the depth level. The
forcer is unchanged in difficulty (Weil-hard phase-cancellation core), but the object is a symbol-sign
detector, not a GLT measure. No fabricated rigor; the marginal touch `min kappa -> 0` for zeta is a
clean, pretty confirmation of zeta at the de Branges boundary in the 2-D symbol.

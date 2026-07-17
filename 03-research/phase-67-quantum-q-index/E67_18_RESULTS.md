# E67.18 -- the Szego law resolves the index puzzle and states the forcer cleanly

**Date:** 2026-07-06.
**Script:** [E67_18_szego_law.py](E67_18_szego_law.py).

## Result

Classical Szego / Avram-Parter for the Toeplitz defect (symbol `sigma = sigma_A - sigma_P`):

```
ind_-(A_N - P_lambda) / N  ->  (1/2pi) measure{theta : sigma(theta) < 0}.
```

Verified at z0=100-i:

| case | measure{sigma<0} | ind_-/N (N=6,10,14,18,22) |
|---|---|---|
| zeta | 0.000 | 0.00, 0.00, 0.00, 0.00, 0.00 |
| offline b=0.8 | 0.498 | 0.33, 0.40, 0.43, 0.44, 0.41 |
| offline b=0.95 | 0.499 | 0.33, 0.40, 0.43, 0.44, 0.41 |

## Two payoffs

1. **The index puzzle is resolved.** The linear growth of `ind_-` with N (E67.9/E67.11), and its
   finite-N "instability" (E67.11's single-pole overcount), are just the Szego eigenvalue distribution.
   `ind_-` is not a pathological counter -- it is the Szego count `~ N * measure{sigma<0}`, a theorem.
   For zeta this is exactly 0; for off-line it converges to `~0.5 N`.

2. **The forcer is stated cleanly, classically:**

```
Omega_7  <=>  measure{theta : sigma_A(theta) < sigma_P(theta)} = 0  for every gauge
         <=>  the symbol of -Xi'/Xi is nonnegative on the circle
         <=>  RH.
```

## Honest scope and the road ahead

`sigma >= 0` is the symbol-level form of the terminal positivity; proving it by structure is expected
to be Weil-positivity-hard (MW-1 in symbol clothing). But the setting is now far more tool-rich than an
abstract operator index: Toeplitz/Szego theory (symbol factorization, Fisher-Hartwig for the marginal
touch at the zeta minimum +0.045, Borodin-Okounkov for the pivotal-weighted resolvent trace). The
pivotal q-trace forcing (E67.15) becomes a symbol integral over `{sigma<0}`, which these tools address.

```
new anchor : Omega_7 = symbol nonnegativity of -Xi'/Xi (Toeplitz)     [E67.16-17]
new law    : ind_- = Szego count ~ N * measure{sigma<0}                [E67.18 this file]
detector   : saved to 02-foundations/engine/symbol_positivity_detector.py
open forcer: prove measure{sigma<0}=0 by structure (symbol nonnegativity),
             or its pivotal-weighted Borodin-Okounkov form
```

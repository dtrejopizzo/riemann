# E67.20 -- audit of E67.19: the object is GLT/pseudodifferential (rigorous), not "heuristic"

**Date:** 2026-07-06.
**Script:** [E67_20_glt_audit.py](E67_20_glt_audit.py).
**Role:** re-audit E67.19. Its data was right; its interpretation ("heuristic, not rigorous") was
too pessimistic.

## What the audit shows

(1) The dominant bands of `P_lambda` vary SMOOTHLY and monotonically with position `j`:

```
band d=0 :  0.276 -> 0.244 -> 0.178   (roughness 0.69, range 0.216)
band d=2 : -0.419 -> -0.222 -> -0.173 (roughness 0.22, range 0.246)
```

Smooth position-variation is the signature of a **Generalized Locally Toeplitz (GLT) /
pseudodifferential** sequence: the symbol depends on position, `kappa(x,theta)`. Such sequences have a
RIGOROUS eigenvalue-distribution theory (Serra-Capizzano, Garoni; Widom):
`#{negative eigenvalues}/N -> measure{(x,theta) : kappa(x,theta) < 0}`. E67.18's Szego law holding is
exactly this distribution at leading (position-averaged) order.

Caveat (honest): the roughness is 0.2-0.76, not `<< 1`, so at these N there is finite-size noise. The
GLT reading is a well-motivated hypothesis, not a clean confirmation.

(2) `sigma_min` of the zeta symbol vs N: 0.038, 0.045, 0.037, 0.031 -- hovers ~0.035, not clearly -> 0.
The exact marginal touch is not confirmed in the 1-D band-averaged symbol; it presumably lives in the
2-D GLT symbol that position-averaging smooths.

## Correction to E67.19

- Data (not constant-Toeplitz; `dev(P_lambda)` grows): correct.
- Interpretation ("heuristic, not rigorous"): **wrong / too pessimistic**. The growing deviation with
  smooth position-variation means the object is GLT/pseudodifferential, which HAS rigorous
  distribution theory. The symbol reduction is not abandoned -- it is enriched to a rigorous
  2-variable symbol: `Omega_7 <=> kappa(x,theta) >= 0`.

## Net

```
Omega_7  <=>  GLT/pseudodifferential symbol  kappa(x,theta) >= 0   (rigorous framework)
detector : the 1-D band symbol is the position-averaged leading order (kept in foundations)
next     : identify kappa(x,theta) explicitly (GLT symbol calculus / Widom) -- Phase 68
```

The user's instinct was right: the result is better than E67.19 stated. The rigorous home is GLT/Widom,
not a heuristic dead-end.

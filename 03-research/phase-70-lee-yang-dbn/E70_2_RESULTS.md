# E70.2 -- monotonicity confirms the direction problem (numerically)

**Date:** 2026-07-07.
**Script:** E70_2_monotone.py.

## Result (true xi, min Im N_lambda over a grid in the upper half z-plane)

```
lambda   min Im N_lambda
+0.30    +0.0481
+0.10    +0.0435
+0.00    +0.0415
-0.10    +0.0396
-0.30    +0.0362
```

`Im N_lambda` is MONOTONE INCREASING in `lambda`: the heat flow improves the Nevanlinna positivity as
`lambda` increases. This is the de Bruijn / Rodgers-Tao direction (`Lambda >= 0`), the PROVEN half.
(That min Im N stays positive at lambda=-0.3 is a coarse-grid artifact -- the narrow region where a
complex zero forms is missed; it does not contradict `Lambda >= 0`.)

## Verdict for Phase 70

The Lee-Yang / de Bruijn-Newman heat-flow forcing is real and beautiful, and it places our problem
precisely: `Omega_7 <=> Lambda <= 0`, with `Lambda >= 0` proven, so `Omega_7 <=> Lambda = 0`. But the
forcing MONOTONICITY (now confirmed numerically) pushes the WRONG way for a proof -- toward `Lambda >= 0`,
not the `Lambda <= 0` that RH needs. No heat-flow monotonicity gives `Lambda <= 0`; if one did, RH would
be proved via dBN.

```
placed   : Omega_7 <=> Lambda = 0 (dBN / Rodgers-Tao framework)
confirmed: heat-flow monotonicity forces Lambda >= 0 (proven, wrong direction)
open     : Lambda <= 0 = the arithmetic/Euler direction -- Weil-hard, unsupplied by the flow
```

Phase 70 closes here: the quantum-stat-mech (Lee-Yang/dBN) route, like the quantum-algebra (Phase 67),
symbol (68), and gauge-invariant Nevanlinna (69) routes, lands on the same core -- now characterized as
the `Lambda <= 0` arithmetic direction, which none of the forcing mechanisms explored supplies.

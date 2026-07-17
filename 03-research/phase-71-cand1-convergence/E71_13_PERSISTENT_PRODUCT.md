# E71.13 -- persistent-divisor product probe

**Date:** 2026-07-07.
**Script:** `E71_13_persistent_product_probe.py`.
**Role:** test whether the persistent clusters from E71.12 behave like the physical determinant
divisor.

## Construction

Use the zero-independent clusters from E71.12:

```text
centers = roots persistent under refinement in N.
```

Build the provisional product

```text
D_pers(t) = product_c (1 - t^2/c^2),
```

where `c` runs over persistent cluster centers.

Compare `D_pers` with

```text
Xi(t)/Xi(0)
```

on `[0,12]`, below the first zero.

## Why this matters

E71.8 showed that the all-root product fails because it includes drifting background roots.

E71.12 showed that persistence isolates the low zeta divisor without using zero centers.

E71.13 tests whether keeping only the persistent divisor gives the correct determinant shape.

## Audit warning

This is still a diagnostic. A proof cannot define `D_pers` by numerical clustering. The clustering
must come from an intrinsic object:

```text
stable Riesz projection / Fredholm decomposition of the CCM m-function.
```

If such a projection is built and its determinant converges normally, E71.5 closes `Omega_7`.

## Result

The persistent product works as a diagnostic: for true zeta it gives `relL2 ~ 0.20` on `[0,12]`,
while the planted control gives `relL2 ~ 0.91`. Results are recorded in `E71_13_RESULTS.md`.

The next document, E71.14, turns this into the stable Riesz/Fredholm projection theorem target.

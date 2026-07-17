# E72.40 -- Post-main endpoint mass and the missing half-power

**Date:** 2026-07-08.
**Role:** estimate the post-main Chebyshev-discrepancy mass appearing in E72.39 and determine what
the compressed channel must supply.

## 0. The post-main scalar integral

After model-main matching, the scalar WRL discrepancy has the form

```text
I_x(z)=int_{1^-}^x f_{x,z}(u)dE(u),
E(u)=Psi(u)-u,
```

with the endpoint-tapered normalized weight

```text
f_{x,z}(u)=(u/x)^z u^(-1/2)(1-log u/log x).
```

Here `f_{x,z}(x)=0`.

## 1. PNT integration by parts

Assume only PNT:

```text
E(u)=o(u).
```

Abel integration gives

```text
I_x(z) = -int_1^x E(u) f'_{x,z}(u)du + endpoint at u=1.
```

For `sigma=Re z>1/2`,

```text
|f'_{x,z}(u)|
 <= C_z x^(-sigma) u^(sigma-3/2)
```

away from harmless logarithmic taper terms. Therefore, for every fixed compact `K` in `sigma>1/2`,

```text
|I_x(z)| <= x^(-sigma) int_1^x o(u) u^(sigma-3/2)du
          = o(x^(1/2)).                           (PNT-MASS)
```

This is the best unconditional scale from PNT alone.

## 2. Consequence

PNT plus endpoint taper does **not** by itself prove scalar WRL annihilation. It leaves a possible
`o(sqrt(x))` mass.

Thus E72.39 requires the compressed channel to supply the missing half-power:

```text
B_x(s)=o(x^(-1/2))
```

up to logarithmic and compact-height factors, or else a signed improvement beyond PNT.

## 3. Why this is still progress

The old Phase 70 route required RH-scale cancellation directly in `E(u)`.

Here the arithmetic discrepancy is tested after:

```text
1. endpoint taper,
2. Feshbach compression,
3. Cauchy Weyl testing.
```

The PNT leaves only a half-power channel requirement. If the compressed Weyl-Feshbach vector has
natural size `x^(-1/2)` in the cell coordinates, scalar WRL closes from PNT plus operator geometry.

## 4. New exact estimate

### Half-Power Channel Estimate

For two interior Cauchy heights,

```text
B_x(s) = o(x^(-1/2))
```

in the coordinate norm paired with the endpoint-tapered cells.

More invariantly:

```text
sup_{z in K}
|int f_{x,z}(u)dE(u)| *
||C_x^(-1)Q_x(sI-D_x)^(-1)1_x||_{cell-dual}
 -> 0.                                           (HPCE)
```

## 5. Status

```text
proved: PNT + endpoint taper gives post-main mass o(sqrt(x));
proved: scalar WRL follows if the compressed channel supplies o(x^-1/2);
open:   prove the half-power channel estimate from the prolate/CCM complement.
```

This is now the sharp quantitative form of the remaining problem.

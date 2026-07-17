# E72.31 -- Scalar Abel form of Weyl-reduced leakage

**Date:** 2026-07-08.
**Role:** expand the minimal WRL estimate from E72.30 into a single scalar Abel-Chebyshev kernel.

## 0. WRL

The minimal remaining estimate is:

```text
WRL_x(s)
 := < (sI-D_x)^(-1)1_x,
       C_x^(-1)Q_x(H_x-H_x^0)k_x >
 -> 0
```

for two interior heights, distributionally in `t` with `s=t+i eta`.

Since `C_x` is self-adjoint on the compressed complement, write formally:

```text
WRL_x(s)
 = < C_x^(-1)Q_x(sI-D_x)^(-1)1_x,
     (H_x-H_x^0)k_x >.                            (D)
```

Thus WRL is a scalar test of the arithmetic residual.

## 1. Scalar cell kernel

Let

```text
v_{x,s}:=C_x^(-1)Q_x(sI-D_x)^(-1)1_x.
```

For each prime-power cell operator `T_{x,n}`, define the scalar centered cell kernel

```text
L_x(s;n)
 := <v_{x,s}, T_{x,n}k_x>
    - <k_x,T_{x,n}k_x><v_{x,s},k_x>.
```

The second term is the Feshbach centering. Since `v_{x,s}` is compressed, it is usually zero, but it is
kept to make the formula gauge-stable.

Then the prime part of WRL is:

```text
WRL_x^{prime}(s)
 = - sum_{n<=x} Lambda(n) L_x(s;n).
```

The model/archimedean part supplies a main term `M_x(s)`.

## 2. Main-term matching

The scalar PNT/model matching condition is:

```text
M_x(s) = int_1^x L_x(s;u)du + err_x(s),
err_x(s)->0.
```

Under this condition,

```text
WRL_x(s)
 = - int_{1^-}^x L_x(s;u)dE(u) + err_x(s),
E(u)=Psi(u)-u.
```

## 3. Abel form

Assuming bounded variation in `u`,

```text
WRL_x(s)
 = -E(x)L_x(s;x)
   + int_1^x E(u)partial_u L_x(s;u)du
   + err_x(s).                                  (SAC)
```

Thus WRL is equivalent to a scalar Abel-Chebyshev cancellation:

```text
E(x)L_x(s;x)
 - int_1^x E(u)partial_uL_x(s;u)du -> 0.        (SACD)
```

## 4. Resonance expansion

By the explicit formula,

```text
SACD_x(s)
 = -sum_rho R_x^{WRL}(s;rho)/rho
   + lower-order terms,
```

where

```text
R_x^{WRL}(s;rho)
 := x^rho L_x(s;x)
    - int_1^x u^rho partial_uL_x(s;u)du.
```

So an off-line zero is invisible to WRL only if its scalar WRL resonance vanishes:

```text
R_x^{WRL}(s;rho) -> 0
```

on the two Cauchy heights.

## 5. Consequence

The minimum target has the same formal resonance obstruction as E72.15, but now with a much smaller
kernel:

```text
vector cumulative kernel K_x(u)
```

has been replaced by

```text
scalar Weyl-Feshbach kernel L_x(s;u).
```

This is progress only if `L_x` has a structural cancellation not present for arbitrary Hardy tests.

## 6. New sharp target

### Scalar WRL resonance annihilation

For every off-critical zero `rho`,

```text
x^rho L_x(s;x)
 - int_1^x u^rho partial_uL_x(s;u)du -> 0
```

distributionally in `s=t+i eta` on two interior heights, without using zero locations.

## 7. Status

```text
proved: WRL reduces exactly to scalar Abel-Chebyshev cancellation;
open:   prove scalar WRL resonance annihilation for the finite CCM/prolate kernel L_x.
```

This is the current smallest possible arithmetic statement.

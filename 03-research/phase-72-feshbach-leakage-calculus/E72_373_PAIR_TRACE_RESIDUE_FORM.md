# E72.373 - Pair trace residue form

## 1. Purpose

E72.372 gives the paired zero pressure as

```text
PAIR-Z(z)=4 sum_{w in Div(Z)/+-} e^(a(z-w))D_a(z,w)G_x(w),
a=L/2,
```

where

```text
Z(w)=xi(1/2+w)
```

is even.  This note rewrites the pair sum as a contour integral against `Z'/Z`.  The goal is to remove
explicit zero enumeration from the proof target.

## 2. The paired sampling kernel

Define

```text
H_z(w):=4e^(a(z-w))D_a(z,w)G_x(w),
```

with

```text
D_a(z,w)
=[cosh(az) w sinh(aw)-z sinh(az) cosh(aw)]/(w^2-z^2).
```

The numerator and denominator are even in `w`, so `D_a(z,-w)=D_a(z,w)`.  Since

```text
G_x(-w)=e^(-2aw)G_x(w),
```

we get

```text
H_z(-w)
=4e^(a(z+w))D_a(z,w)e^(-2aw)G_x(w)
=H_z(w).                                               (1)
```

Thus `H_z` is even on the shifted divisor in the exact sense needed for pair summation.

## 3. Residue theorem

Let `Gamma_R` be a rectangle symmetric under `w -> -w`, avoiding zeros of `Z`, containing all shifted
zeros with `|Im w|<=R`, and no zero on the boundary.  Then

```text
1/(2pi i) int_{Gamma_R} H_z(w) Z'(w)/Z(w) dw
= sum_{|Im w_rho|<=R} m_rho H_z(w_rho).                (2)
```

Because both the divisor and `H_z` are even, the full divisor sum is twice the pair sum:

```text
sum_{|Im w_rho|<=R} m_rho H_z(w_rho)
=2 sum_{w in Div(Z)/+-, |Im w|<=R} m_w H_z(w).          (3)
```

Therefore the truncated paired pressure is

```text
PAIR-Z_R(z)
=1/(4pi i) int_{Gamma_R} H_z(w) Z'(w)/Z(w) dw.          (4)
```

The full `PAIR-Z` is the symmetric limit of (4), provided the contour limit exists in the same
principal-value convention as the explicit formula used in E72.319.

## 4. What has been gained

Equation (4) replaces zero enumeration by one meromorphic integral:

```text
PAIR-Z(z)
=PV 1/(4pi i) int_Gamma
   4e^(a(z-w))D_a(z,w)G_x(w) Z'(w)/Z(w) dw.             (5)
```

Equivalently, using the shorthand `H_z`,

```text
PAIR-Z(z)
=PV 1/(4pi i) int_Gamma H_z(w) Z'(w)/Z(w) dw.           (6)
```

The normalization in (6) is load-bearing: `H_z` already includes the factor `4`, so there is no
extra scalar outside the integral.

## 5. Next theorem: contour compression

The analytic problem is now:

```text
CTRACE:
for fixed shifted strips in z,
PV int_Gamma H_z(w) Z'(w)/Z(w) dw
is polynomially bounded in L and z,
after adding the finite-tail contribution from E72.319.
```

Unlike the earlier zero-sum target, `CTRACE` can use:

```text
Z'/Z(w)=1/2 psi((1/2+w)/2)-1/2 log pi
        + zeta'/zeta(1/2+w)
        + elementary polar terms,
```

on vertical contour lines away from the critical strip.  The prime current enters through
`zeta'/zeta`, while the archimedean part is already matched by the construction of `D_a`.

## 6. Status

```text
proved: H_z(-w)=H_z(w);
proved: PAIR-Z_R is half the full divisor residue trace;
reduced: HPAIR to CTRACE plus finite-tail control;
open: prove the contour compression bound for the explicit integrand.
```

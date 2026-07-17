# E72.372 - Hyperbolic form of the paired zero kernel

## 1. Purpose

E72.321 reduces the complete-mesh zero pressure to symmetric pairs:

```text
Pair_z(w)
= G_x(w)/(w^2-z^2)
   [ w(1+e^(zL))(1-e^(-wL))
     + z(1-e^(zL))(1+e^(-wL)) ].
```

This note rewrites the bracket as a hyperbolic Wronskian.  The point is to expose the cancellation
before any absolute value is taken.

## 2. Hyperbolic factorization

Put

```text
a := L/2.
```

Then

```text
1+e^(zL)=2e^(az)cosh(az),
1-e^(zL)=-2e^(az)sinh(az),
1-e^(-wL)=2e^(-aw)sinh(aw),
1+e^(-wL)=2e^(-aw)cosh(aw).
```

Substitution gives the exact identity

```text
w(1+e^(zL))(1-e^(-wL))
+z(1-e^(zL))(1+e^(-wL))

=4e^(a(z-w))[w cosh(az)sinh(aw)-z sinh(az)cosh(aw)].       (1)
```

Therefore

```text
Pair_z(w)
=4e^(a(z-w))G_x(w)
  [w cosh(az)sinh(aw)-z sinh(az)cosh(aw)]
  /(w^2-z^2).                                             (2)
```

## 3. Divided-difference form

Define

```text
T_a(u):=u sinh(au),       C_a(u):=cosh(au).
```

Since

```text
w cosh(az)sinh(aw)-z sinh(az)cosh(aw)
=C_a(z)T_a(w)-T_a(z)C_a(w),
```

we get

```text
Pair_z(w)
=4e^(a(z-w))G_x(w)
  [ C_a(z)T_a(w)-T_a(z)C_a(w) ]/(w^2-z^2).              (3)
```

Equivalently, with the meromorphic even function

```text
R_a(u):=T_a(u)/C_a(u)=u tanh(au),
```

the same kernel is

```text
Pair_z(w)
=4e^(a(z-w))C_a(z)C_a(w)G_x(w)
  [ R_a(w)-R_a(z) ]/(w^2-z^2).                          (4)
```

Thus the apparent singularities at `w=+-z` are removable in the entire form (3): the numerator is a
divided difference of two even entire functions.

## 4. Proof of removability

The function `R_a(u)=u tanh(au)` is even and meromorphic only at the zeros of `cosh(au)`.  In (3) the
entire form is preferable:

```text
C_a(z)T_a(w)-T_a(z)C_a(w).
```

Both `C_a` and `T_a` are even entire functions.  Hence

```text
C_a(z)T_a(w)-T_a(z)C_a(w)
```

vanishes when `z^2=w^2`, because the two even functions take the same arguments.  Therefore it is
divisible in the ring of entire functions of `(z,w)` by `w^2-z^2`.  The quotient

```text
D_a(z,w):=[C_a(z)T_a(w)-T_a(z)C_a(w)]/(w^2-z^2)
```

is entire and symmetric:

```text
D_a(w,z)=D_a(z,w).
```

Formula (3) becomes

```text
Pair_z(w)=4e^(a(z-w))G_x(w)D_a(z,w).                    (5)
```

This expression is invariant under changing the representative of the pair.  Indeed,
`D_a(z,-w)=D_a(z,w)` and `G_x(-w)=e^(-2aw)G_x(w)`, so

```text
e^(a(z+w))G_x(-w)D_a(z,-w)=e^(a(z-w))G_x(w)D_a(z,w).
```

## 5. Consequence for the analytic target

The paired zero pressure is now

```text
PAIR-Z(z)
=4 sum_{w in Div(Z)/+-} e^(a(z-w)) D_a(z,w)G_x(w).    (6)
```

This is the first form in which the zero pressure is a weighted sampling of `G_x(w)` against an
entire divided-difference kernel.  The old incoherent expression had denominator `w^2-z^2`; (6) has
absorbed that denominator into an entire kernel.

The remaining theorem is therefore not a generic zero-sum bound.  It is:

```text
HPAIR:
the sampled entire-kernel transform in (6) is polynomially bounded in fixed shifted strips,
with the same finite tail convention as E72.319.
```

## 6. Why this is stronger than E72.321

E72.321 removed the diagonal `G_x(z)` term by symmetry.  E72.372 removes the Cauchy denominator from
the off-point pair kernel itself.  This matters because any proof of `PAIR-Z` can now use entire
function interpolation or contour deformation on `D_a(z,w)G_x(w)`, rather than estimating singular
Cauchy weights at the zero divisor.

## 7. Status

```text
proved: exact hyperbolic factorization of Pair_z(w);
proved: denominator divisibility by z^2-w^2;
reduced: PAIR-Z to HPAIR, an entire divided-difference sampling theorem;
open: prove HPAIR plus finite-tail control from the finite Feshbach-Weil construction.
```

# E72.322 -- Zero-node linear system for the packet equation

**Purpose.** Evaluate the paired packet equation of E72.321 at shifted zero nodes. This converts the
remaining interpolation problem into an explicit linear system for the values `G_x(w)` on the shifted
nontrivial-zero divisor.

This is the first place where an off-line zero produces an explicit diagonal forcing factor.

## 1. Paired packet equation

E72.321 gives, for shifted `z`,

```text
(mu+e_pole-2kappa_L)G_x(z)
= sum_{w in Div(Z)/+-} Pair_z(w)
   - Lcal(B_z^tail),
```

where

```text
Pair_z(w)
= M_z(w)+M_z(-w),
```

and `M_z(w)` is the factor form from E72.320:

```text
M_z(w)
= [ ((w+z)+e^(zL)(w-z))G_x(w) - 2wG_x(z) ]
   /(w^2-z^2).                                        (1)
```

## 2. Self-pair limit

Let `a` be one representative of a nontrivial shifted zero pair `{a,-a}`. Set `z=a`. The pair
`w=a` is removable in the original integral definition, so compute the limit from (1).

For `w -> z`,

```text
M_z(z)
= G_x'(z) + (e^(zL)-1)G_x(z)/(2z).                    (2)
```

For `w -> -z`, use the pole-even identity

```text
G_x(-z)=e^(-zL)G_x(z),
```

and its derivative consequence

```text
G_x'(-z)=e^(-zL)(LG_x(z)-G_x'(z)).
```

Then

```text
M_z(-z)
= -G_x'(z) + LG_x(z) - (e^(-zL)-1)G_x(z)/(2z).        (3)
```

Adding (2) and (3) gives the self-pair diagonal:

```text
Pair_z(z)
= [ L + (e^(zL)-e^(-zL))/(2z) ] G_x(z)
= [ L + sinh(zL)/z ] G_x(z).                          (4)
```

No derivative remains.

## 3. Linear system on zero nodes

Evaluate the paired equation at `z=a`. Separating the self-pair gives

```text
[mu+e_pole-2kappa_L - L - sinh(aL)/a] G_x(a)
= sum_{w != a, w in Div(Z)/+-} Pair_a(w)
   - Lcal(B_a^tail).                                  (5)
```

This is an explicit linear equation for the nodal values `G_x(a)`.

For a finite zero window `A_T`, write:

```text
D_a(L):=mu+e_pole-2kappa_L - L - sinh(aL)/a,
```

and

```text
K_{a,w}(L)
:= [ w(1+e^(aL))(1-e^(-wL))
     + a(1-e^(aL))(1+e^(-wL)) ]/(w^2-a^2).
```

Then the truncated system is

```text
D_a(L)G_x(a)
- sum_{w in A_T, w != a} K_{a,w}(L)G_x(w)
= Err_a(T,L),                                         (6)
```

where `Err_a` contains the zeros outside `A_T` and the finite Fourier tail.

## 4. Diagonal forcing for off-line zeros

If `Re a>0`, then

```text
sinh(aL)/a
```

has exponential size `e^(aL)/(2a)` along subsequences avoiding its oscillatory zeros. Thus the
diagonal coefficient `D_a(L)` contains an explicit exponential forcing term.

This is not yet a proof of suppression, because the off-diagonal coefficients `K_{a,w}` can also
contain exponentials. But it is a major structural reduction:

```text
off-line pressure is now a diagonal-dominance problem for the zero-node system (6).
```

## 5. New theorem target

For every fixed zero window `A_T`, prove:

```text
ZND:
the matrix D(L)-K(L) is invertible with
||(D-K)^(-1)|| <= e^(-c_T L)L^B
```

on the off-line subspace, and

```text
Err(T,L)
```

is at most polynomial after the same finite-tail normalization.

Then

```text
G_x(a)=O(e^(-c_T L)L^B)
```

for every off-line shifted zero `a` in the window. This supplies the nodal version of `PW-Cauchy`,
and the contour equation propagates it back to fixed shifted strips.

## 6. Status

```text
proved: self-pair limit Pair_a(a)=(L+sinh(aL)/a)G_x(a);
reduced: packet interpolation to the explicit zero-node system (6);
open:   prove diagonal dominance/invertibility ZND and bound Err_a(T,L).
```

The next step is to analyze the finite matrix `D(L)-K(L)` symbolically on a single off-line quadruple
and identify whether the functional-equation pairing already gives the required dominance.

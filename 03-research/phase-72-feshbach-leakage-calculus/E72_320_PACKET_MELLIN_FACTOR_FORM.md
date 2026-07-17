# E72.320 -- Factor form of the packet Mellin transform

**Purpose.** Compute the Mellin transform `M_{B_z^infty}(w)` from E72.319. The result is a closed
two-point formula involving only the cancelled Cauchy transform `G_x` at `z` and at `w`.

This is the main algebraic simplification of the transformed route so far.

## 1. Starting packet

From E72.318,

```text
B_z^infty(y)
= i[ (e^(z(L-y))-e^(zy))H_0(z)
     - H_+(z;y)
     + e^(zL)H_-(z;y) ],
```

where

```text
H_0(z)=sum_n xi_n/(z+i d_n),
H_+(z;y)=sum_n xi_n e^(i d_n y)/(z+i d_n),
H_-(z;y)=sum_n xi_n e^(-i d_n y)/(z+i d_n).
```

Also

```text
G_x(z)=(1-e^(zL))C_x(iz)=-i(1-e^(zL))H_0(z).          (1)
```

## 2. Mellin transform

Define

```text
M_z(w):=int_0^L e^(wy)B_z^infty(y)dy.
```

Integrating the four terms gives

```text
M_z(w)
= iH_0(z)[ (e^(wL)-e^(zL))/(w-z)
           -(e^((w+z)L)-1)/(w+z) ]
 -i(e^(wL)-1) sum_n xi_n/[(z+i d_n)(w+i d_n)]
 +i e^(zL)(e^(wL)-1) sum_n xi_n/[(z+i d_n)(w-i d_n)].
```

By evenness of `xi_n` and symmetry of the mesh,

```text
sum_n xi_n/[(z+i d_n)(w+i d_n)]
= [H_0(z)-H_0(w)]/(w-z),
```

and

```text
sum_n xi_n/[(z+i d_n)(w-i d_n)]
= [H_0(z)+H_0(w)]/(w+z).
```

Substitution and cancellation give:

```text
M_z(w)
= i(1-e^(zL))H_0(z) [ 1/(w-z)+1/(w+z) ]
 + i(e^(wL)-1)H_0(w) [ 1/(w-z)+e^(zL)/(w+z) ].
```

Using (1), this becomes the factor form:

```text
M_z(w)
= [ ((w+z)+e^(zL)(w-z))G_x(w) - 2wG_x(z) ]
   /(w^2-z^2).                                        (2)
```

The apparent poles at `w=+-z` are removable by the original integral definition.

## 3. Packet-zero equation

Set

```text
w_rho=rho-1/2.
```

The packet-zero term in E72.319 is therefore

```text
sum_rho M_z(w_rho)
= sum_rho
   [ ((w_rho+z)+e^(zL)(w_rho-z))G_x(w_rho)
     - 2w_rho G_x(z) ]
   /(w_rho^2-z^2).                                    (3)
```

Thus the transformed compact branch is governed by a scalar two-point equation for `G_x`.

## 4. Endpoint-renormalized TPW equation

E72.319 gave

```text
(mu+e_pole-2kappa_L)G_x(z)
= sum_rho M_z(w_rho) - Lcal(B_z^tail).
```

Using (3):

```text
(mu+e_pole-2kappa_L)G_x(z)
= sum_rho
   [ ((w_rho+z)+e^(zL)(w_rho-z))G_x(w_rho)
     - 2w_rho G_x(z) ]
   /(w_rho^2-z^2)
 - Lcal(B_z^tail).                                    (4)
```

This is the current sharpest analytic form of `TPW`.

## 5. Why this matters

Before E72.320, the remaining theorem involved:

```text
combined transformed model/prime/WR kernels.
```

After E72.320, the complete-mesh main is only:

```text
values of G_x at z and at the shifted zeta-zero parameters w_rho.
```

So the compact route has become a scalar interpolation/resolvent equation. The exponential factor
`e^(zL)` no longer floats freely; it is attached to the coefficient of `G_x(w_rho)`.

## 6. The next target

The new proof-facing statement is:

```text
G-interpolation bound:
the right side of (4) is polynomially bounded in fixed shifted strips.
```

Equivalently, after moving the `G_x(z)` part of the zero sum to the left:

```text
Lambda_x(z)G_x(z)
= sum_rho
   ((w_rho+z)+e^(zL)(w_rho-z))/(w_rho^2-z^2)
   G_x(w_rho)
 - Lcal(B_z^tail),                                    (5)
```

where

```text
Lambda_x(z)
= mu+e_pole-2kappa_L
   + sum_rho 2w_rho/(w_rho^2-z^2).
```

The zero sum in `Lambda_x` is understood in the same symmetric sense as `Xi'/Xi`.

## 7. Status

```text
proved: closed factor formula (2);
proved: endpoint-renormalized TPW becomes the scalar equation (4);
open:   control the zero-interpolation sum and the finite tail.
```

The next analytic step is to rewrite the symmetric sums in (5) through `Xi'/Xi`, so that no individual
zero tracking remains.

E72.321 sharpens this: because the shifted `Xi` divisor is even and
`G_x(-w)=e^(-wL)G_x(w)`, the part of the zero sum proportional to `G_x(z)` cancels exactly in pairs
`{w,-w}`. Thus no logarithmic-derivative renormalization of the left coefficient is needed. The
remaining complete-mesh zero pressure is the paired interpolation sum `PAIR-Z`.

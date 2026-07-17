# E72.391 - Tail coefficient as a Cauchy moment

## 1. Purpose

E72.390 removed the apparent harmonic coefficient of the finite Fourier tail by parity.  This note
proves a stronger statement: the whole off-mesh tail coefficient is exactly a Cauchy moment of the
cancelled transform `G_x` at the shifted zero parameters.

Thus the finite tail is not a separate analytic gate.  It is governed by the same nodal quantities
that appear in `PAIR-Z` and the maximal Cauchy block.

## 2. Exact divided-difference collapse

Recall

```text
Phi_w(d)=d/(w^2+d^2),          d_j=2pi j/L.
```

For `m != n`,

```text
[Phi_w(d_m)-Phi_w(d_n)]/[pi(n-m)]
= -2/L * [w^2-d_md_n]/[(w^2+d_m^2)(w^2+d_n^2)].       (1)
```

Indeed,

```text
Phi_w(d_m)-Phi_w(d_n)
= (d_m-d_n)(w^2-d_md_n)/[(w^2+d_m^2)(w^2+d_n^2)]
```

and

```text
(d_m-d_n)/(pi(n-m))=-2/L.
```

## 3. Pole-even cancellation of the odd moment

Sum (1) against the pole-even vector `xi_n`.  The odd moment vanishes:

```text
sum_n xi_n d_n/(w^2+d_n^2)=0.                         (2)
```

Therefore

```text
sum_n xi_n [Phi_w(d_m)-Phi_w(d_n)]/[pi(n-m)]
= -2w^2/[L(w^2+d_m^2)] U_0(w),                       (3)
```

where

```text
U_0(w):=sum_n xi_n/(w^2+d_n^2).
```

This is exact, not an asymptotic expansion.

## 4. Convert to the cancelled Cauchy transform

E72.310 gives

```text
U_0(w)=i C_x(iw)/w.
```

With

```text
G_x(w)=(1-e^(wL))C_x(iw),
```

the coefficient formula of E72.333 becomes

```text
Lcal(b_m)
= -2i/L sum_w w G_x(w)/(w^2+d_m^2).                  (4)
```

The sum is taken in the same symmetric explicit-formula sense as before, with removable values at
kinematic coincidences.

## 5. Consequence for the finite tail

Substitute (4) into

```text
Lcal(B_z^tail)=sum_{|m|>M} (1-e^(zL))/(iz-d_m)Lcal(b_m).
```

Then

```text
Lcal(B_z^tail)
= -2i/L sum_w w G_x(w)
   sum_{|m|>M} (1-e^(zL))/[(iz-d_m)(w^2+d_m^2)].       (5)
```

The inner `m`-sum is an explicit rational Fourier-tail kernel.  For fixed shifted strips away from
kinematic collisions it has the summable profile

```text
O_K(e^(sigma L) L^B/M^2),
```

and, more importantly, all zero dependence is now carried only by `wG_x(w)`.

## 6. Tail absorption principle

Equation (5) proves:

```text
TAIL-CM:
finite Fourier tail = explicit tail kernel applied to the same nodal vector {G_x(w)}.
```

Thus the tail is absorbed by the maximal-real-part Cauchy block once the nodal suppression theorem is
proved.  There is no independent tail positivity or incoherent absolute zero sum left.

In particular, for a maximal off-line cluster with `Re w=alpha>0`, the Cauchy block target

```text
G_x(w)=O(e^(-alpha L)L^B)
```

cancels the factor `1-e^(wL)` already contained in `G_x(w)`.  The remaining tail kernel is polynomial
after choosing any polynomial active cutoff with sufficiently large power.

## 7. Status

```text
proved: exact identity Lcal(b_m)=-(2i/L) sum_w wG_x(w)/(w^2+d_m^2);
proved: finite Fourier tail is not a separate spectral object;
reduced: TAIL-POLY to the same nodal suppression theorem used for PAIR-Z.
```


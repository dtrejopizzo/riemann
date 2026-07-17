# E72.317 -- Transformed eigenvector equation for PW-Cauchy

**Purpose.** Write the remaining `PW-Cauchy` theorem of E72.316 as an exact transformed eigenvector
identity. This is the analytic equation that has to be solved next.

## 1. Cancelled Cauchy transform

Define the cancelled Cauchy transform

```text
G_x(z):=(1-e^(zL))C_x(iz)
      =(1-e^(zL))sum_m xi_m/(iz-d_m).                   (1)
```

The target `PW-Cauchy` is:

```text
|G_x(z)| <= A_{sigma,H}L^B(1+|z|)^B
```

in fixed shifted strips.

## 2. Transform the eigenvector equation

The pole-even actual ground vector satisfies

```text
C_E xi = mu xi.                                           (2)
```

For each `z`, multiply the `m`-th component of (2) by

```text
K_z(m):=(1-e^(zL))/(iz-d_m)
```

and sum over `m`. This gives the exact identity

```text
mu G_x(z)
= sum_m K_z(m)(C_E xi)_m
= sum_n xi_n [sum_m K_z(m)C_E(m,n)].                     (3)
```

Define the transformed kernel

```text
T_E(z;n):=sum_m K_z(m)C_E(m,n).
```

Then

```text
mu G_x(z)=sum_n T_E(z;n)xi_n.                            (4)
```

This is just the eigenvector equation in the Cauchy plane.

## 3. Split the actual operator

Using the corrected compact form,

```text
C_E = W02 - WR - Prime - e_pole I.
```

The scalar pole shift contributes

```text
-e_pole sum_m K_z(m)xi_m = -e_pole G_x(z).
```

Thus

```text
(mu+e_pole)G_x(z)
= T_W02(z)[xi] - T_WR(z)[xi] - T_Prime(z)[xi].           (5)
```

This is the exact transformed PW equation.

## 4. What must be proved

Equation (5) closes `PW-Cauchy` if the right side is polynomially bounded in fixed shifted strips:

```text
|T_W02(z)[xi] - T_WR(z)[xi] - T_Prime(z)[xi]|
<= A_{sigma,H}L^B(1+|z|)^B.                              (6)
```

Since `mu+e_pole` has the pole-even lower scale already isolated by `GAP`, division by it is harmless.

The theorem to prove is therefore:

```text
TPW:
the transformed model-archimedean-prime combination in (5) has polynomial strip growth.
```

This is more precise than `PW-Cauchy`: it says exactly where the cancellation must occur.

## 5. Why termwise bounds are not allowed

Bounding `T_W02`, `T_WR`, and `T_Prime` separately by absolute values would reintroduce the incoherent
ceiling. The whole point of (5) is that the transformed operator combination must be kept intact:

```text
T_W02 - T_WR - T_Prime.
```

The cancellation between the model endpoint and the prime/archimedean pieces is the same cancellation
seen in E72.300--E72.305, now lifted to the Cauchy plane.

Thus the next analytic proof cannot estimate the prime transform alone. It must prove the combined
kernel identity (6).

## 6. Equivalent kernel form

For any cell kernel `Q_y(m,n)`, define

```text
KQ_z(y;n):=sum_m (1-e^(zL))/(iz-d_m) Q_y(m,n).
```

Then the prime transform has the form

```text
T_Prime(z)[xi]
= sum_{p^k<=e^L} Lambda(p^k)p^(-k/2)
   sum_n KQ_z(k log p;n)xi_n,
```

with the exact sign convention inherited from `C_E`.

The model and `WR` transforms are the corresponding continuous/archimedean analogues. Therefore
`TPW` is an identity about the Abel difference:

```text
model transform - archimedean transform - prime transform.
```

This is the same object as scalar WRL, but now expressed as a single Cauchy-plane eigen-equation.

## 7. Reduced chain

The compact branch now reads:

```text
TPW
=> PW-Cauchy
=> SQB
=> CB
=> RNS
=> MC-NZ
=> NZ-MSD
=> compact-root HPAC decay.
```

Every arrow after `TPW` has been isolated as an analytic lemma in E72.311--E72.316.

## 8. Status

```text
proved: exact transformed eigenvector identity (5);
proved: TPW implies PW-Cauchy;
open:   prove TPW without splitting the three transformed terms by absolute values.
```

This is the precise analytic theorem left in the compact-root route.

E72.318 computes the transformed cell kernel explicitly. On the complete Fourier mesh,

```text
(1-e^(zL))sum_m e^(id_m r)/(iz-d_m)=iL e^(z(L-r)),
```

so

```text
KQ_z(y;n)
= i/(z+i d_n)
   [ e^(z(L-y))-e^(i d_n y)+e^(zL)e^(-i d_n y)-e^(zy) ],
```

up to the finite mesh tail. Thus `TPW` is no longer an opaque transformed-matrix estimate: it is a
shifted Cauchy-packet Abel identity plus finite tail control.

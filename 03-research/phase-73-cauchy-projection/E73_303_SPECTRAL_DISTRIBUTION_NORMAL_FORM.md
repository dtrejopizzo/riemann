# E73.303 - Spectral distribution normal form

Date: 2026-07-16.

## 1. Purpose

E73.293 proves the continuous identity

```text
dW_omega/domega = i V_omega.
```

E73.286 shows that replacing this by a finite-difference integration by parts
on the mesh fails.  This note keeps the exact continuous identity without
using a false mesh derivative.

## 2. Distribution form

For the frequency packet

```text
B(y)=sum_omega c_omega e^(iomega y)
    +y sum_omega l_omega e^(iomega y),
```

the center is

```text
C=sum c_omega W_omega+sum l_omega V_omega.
```

Since `V_omega=(1/i)W'_omega=-iW'_omega`, define the finite first-order
distribution

```text
T_eta=sum_omega c_omega delta_omega
     +i sum_omega l_omega delta'_omega.
```

With the convention `<delta'_omega,phi>=-phi'(omega)`, we get exactly

```text
<T_eta,W>=sum c_omega W_omega+sum l_omega V_omega.      (SD)
```

Thus `BLOCK-FREQ-DIV` is equivalently:

```text
<T_{R_wxi_L},W>=O_M(L^(-M)).
```

Here `W(omega)` is the single closed Gamma-prime symbol from E73.287.

## 3. What this fixes

This removes a misleading two-block presentation:

```text
sum cW + sum lV
```

is not a cancellation between unrelated weights.  It is the action of one
finite spectral distribution on one analytic symbol.

It also avoids the rejected E73.286 branch:

```text
do not replace W' by a finite-difference derivative on the mesh.
```

The distribution keeps the derivative at the support point exactly.

## 4. Moment audit

The distribution form does not close the theorem by low moments.  For
`phi(omega)=omega^k`:

```text
<T,1>      = sum c_omega,
<T,omega>  = sum c_omega omega - i sum l_omega,
<T,omega^2>= sum c_omega omega^2 - 2i sum l_omega omega.
```

The companion probe reports:

```text
 lam      L gamma row centerB T1B TomB Tom2B derivB
  12    4.970  14.13   0   -21.26  -22.88  -10.41   -7.46  -10.41
  16    5.545  21.02   0   -18.21  -22.22   -9.55   -5.71   -9.55
  20    5.991  21.02   1   -18.80  -21.65   -9.54   -5.24   -9.54
```

Only `<T,1>` is at the endpoint floor.  Higher moments are much larger than
the center.  Therefore E73.303 is not a low-moment proof; it is the exact
one-symbol normal form.

## 5. New endpoint

The current frequency endpoint can now be stated as:

```text
One-Symbol Spectral Distribution Divisibility.
Let W_L(omega)=F_L[e^(iomega y)] be the closed Gamma-prime symbol.
For the exact Cauchy-Schur distribution

T_{a,w,L}=sum c_omega(R_wxi_L)delta_omega
        +i sum l_omega(R_wxi_L)delta'_omega,

prove

<T_{a,w,L},W_L>=O_M(L^(-M)).
```

This is equivalent to `GAUGE-FREQ-DIV`, `BLOCK-FREQ-DIV`, `TS-DIV`,
`FINAL-ETA-ADJ`, and `CURV-ABEL-neutral`.

## 6. Status

```text
proved: W,V pairing equals first-order spectral distribution action on W;
rejected: low moments of T explain the small center;
kept: exact one-symbol distribution normal form;
open: prove <T_{a,w,L},W_L>=O_M(L^(-M)) from Gamma-prime/eigenline structure.
```


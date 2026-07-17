# E73.199 - Finite-frequency certificate with digamma WR tail

Date: 2026-07-14.

## 1. Purpose

E73.195 showed that the transverse cell can be evaluated by a finite-frequency
formula, but the raw WR summation had to be pushed very deep.  E73.196 then
showed that coefficient-absolute WR tails lose the signed cancellation.  E73.197
and E73.198 fix the tail analytically.

This note records the proof-facing certificate:

```text
finite WR head + signed digamma tail + exact prime samples.
```

## 2. Certificate identity

For the transverse Cauchy packet

```text
B_a(y)=sum_omega c_omega e^(i omega y)
      +y sum_omega l_omega e^(i omega y),
```

the archimedean functional is

```text
A_L[B_a]
=int_0^L B_a(y)(e^(y/2)+e^(-y/2))dy
 -1/2(log4pi+gamma)B_a(0)
 -int_0^L (e^(y/2)B_a(y)-B_a(0))/(2sinh y)dy
 -1/2 log(tanh(L/2))B_a(0).
```

Using

```text
1/(2sinh y)=sum_{r>=0} e^(-(2r+1)y),
```

the singular WR part is evaluated as

```text
sum_{r=0}^{R-1}
 [ int_0^L e^(-(2r+1/2)y)B_a(y)dy
  -B_a(0)int_0^L e^(-(2r+1)y)dy ]
+T_R(B_a),
```

where the infinite signed tail is

```text
T_R(B_a)
=sum_omega c_omega D_1(R,omega)
 +sum_omega l_omega D_2(R,omega)
 +E_R(B_a,L),
```

with

```text
D_1(R,omega)=1/2[psi(R+1/2)-psi(R+1/4-iomega/2)],
D_2(R,omega)=1/4 psi_1(R+1/4-iomega/2).
```

The exponential correction `E_R` is bounded by the elementary geometric
estimates of E73.198.

The prime side remains finite and exact:

```text
P_L[B_a]=sum_{p^k<=e^L}(log p)p^(-k/2)B_a(klog p).
```

Thus

```text
F_L[B_a^bal]=F_L[B_a]
            =A_L^digamma[B_a]-P_L[B_a],
```

because the balanced ramp `r_*` was chosen in E73.193 so that `F_L[r_*]=0`.

## 3. Why this avoids the E73.196 failure

E73.196 bounded each WR frequency tail by absolute values and lost 7--12 powers
of `L`.  The displayed digamma formula keeps the paired signed quantity

```text
sum_{r>=R} [1/(2r+1/2-iomega)-1/(2r+1)]
```

before estimating.  This is the cancellation actually present in the functional;
it is not a numerical extrapolation.

## 4. Current theorem target

The remaining interval theorem is:

```text
INTERVAL-FF-CERT:
For every admissible finite window, the digamma certificate above admits
complex interval enclosures whose total width is o(L^-B) and whose midpoint
satisfies the TRANS-CELL budget.
```

This is a finite special-function certificate, not a new matrix computation.
The only non-elementary interval inputs are enclosures for `psi` and `psi_1`
at explicitly listed complex arguments.

## 5. Status

```text
proved: certificate identity;
proved: signed digamma tail formula;
verified: floating digamma certificate against matrix residuals;
open: rigorous complex interval implementation for psi/psi_1 and finite
      frequency coefficients.
```

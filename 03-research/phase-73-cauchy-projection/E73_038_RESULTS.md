# E73.038 results - finite Cauchy divisor identity

## 1. Purpose

E73.038 proves the exact finite identity

```text
C_x(t)=P_x(t)/D_x(t),
```

where

```text
D_x(t)=prod_n(t-d_n),
P_x(t)=sum_n xi_n prod_{m != n}(t-d_m).
```

The probe certifies the identity numerically using high-precision product evaluation.

## 2. Computed output

```text
E73.038 finite Cauchy divisor identity probe
Checks C_x(t)=P_x(t)/D_x(t) at critical heights using high-precision products.
Monomial coefficient/root evaluation is intentionally avoided here.
 lam     L degree       maxAbs       maxRel
   8   4.159     24   3.923e-102    1.456e-86
  10   4.605     28   2.791e-102    4.400e-85
  12   4.970     32   1.011e-102    9.629e-88
  14   5.278     36   4.301e-102    4.065e-86
```

Reproduce with:

```text
python3 03-research/phase-73-cauchy-projection/E73_038_cauchy_divisor_identity_probe.py
```

## 3. Numerical lesson

Evaluating the divisor through monomial coefficients and numerical roots is ill-conditioned near
finite Cauchy zeros.  The correct certification uses product/barycentric evaluation.

This matters for the proof architecture: the divisor identity is exact, but any future finite
certificate must avoid unstable monomial coordinates.

## 4. Status

```text
proved: finite Cauchy transform equals numerator divisor over pole divisor;
validated: high-precision product identity at critical heights;
feeds: mesh-root covering estimate for PFD.
```

# E72.176 -- Certified error for SRP

**Date:** 2026-07-09.
**Role:** certify the uniform polynomial errors used in the signed residual polynomial gate.

## 0. Method

For each fitted polynomial `g_j`, the error is piecewise polynomial:

```text
g_j(t)-t                 on [-M_j,0],
g_j(t)-(1-a_j)t          on [0,M_j].
```

The companion script:

```text
E72_176_signed_poly_error_certificate.py
```

finds all real critical points of those two error polynomials and evaluates endpoints plus critical
points. Thus the reported errors are interval-certified, not grid-only.

## 1. Output

```text
E72.176 signed polynomial error certificate
degree=28
K0 err=6.802249139526e-03 negMax@+0.000000000000 posMax@+0.000000000000
K1 err=3.886999508300e-03 negMax@+0.000000000000 posMax@+0.000000000000
 lam    L dim  polyR  certErrHS  certBound margin pass
  12  4.97  32  0.924     0.060     0.984   0.031 YES
  14  5.28  36  0.888     0.064     0.952   0.093 YES
  16  5.55  40  0.867     0.068     0.934   0.127 YES
  18  5.78  44  0.836     0.071     0.907   0.177 YES
  20  5.99  48  0.846     0.074     0.920   0.154 YES
  22  6.18  52  0.861     0.077     0.938   0.120 YES
  24  6.36  56  0.847     0.080     0.927   0.140 YES
worst_cert_bound=0.984 at lambda=12
```

## 2. Certified SRP gate

With:

```text
eps_0=6.802249139526e-03,
eps_1=3.886999508300e-03,
```

the sufficient stable condition is:

```text
||g_0(K_0)+g_1(K_1)||_HS
 + sqrt(d)(eps_0+eps_1)
< 1.                                                        (SRP-cert)
```

In the tested stable windows the worst certified bound is `0.984`.

## 3. Status

```text
proved: degree-28 polynomial error certificates on the stated intervals;
observed: SRP-cert passes all tested stable windows;
open:   prove SRP-cert uniformly for all large x.
```

This replaces the previous `PTC + cross_+` gate by one direct residual-polynomial inequality.

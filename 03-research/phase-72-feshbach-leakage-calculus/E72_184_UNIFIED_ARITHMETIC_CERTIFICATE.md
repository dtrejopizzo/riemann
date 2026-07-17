# E72.184 -- Unified arithmetic certificate

**Date:** 2026-07-09.
**Role:** combine the pre-stable direct certificate with the stable trace-cycle certificate.

## 0. Certificate split

The arithmetic gate is now split as:

```text
pre-stable windows: direct F2B-PSD;
stable windows:     NTC-8 + ASRP-0.05.
```

The stable certificate is:

```text
NTC-8:
Tr((K_0/0.90)^16)<1,
Tr((K_1/0.60)^16)<1.

ASRP-0.05:
D_x even,
D_x+1 >= 0.99 sqrt(d_x)/(0.05 pi),
Tr(G_{x,D_x}^2)<0.9025.
```

Together:

```text
NTC-8 + ASRP-0.05 => F2B-PSD.
```

The pre-stable part is:

```text
||K_rel-0.70K_0^+-0.60K_1^+||_HS<1.
```

## 1. Unified diagnostic

The companion script:

```text
E72_184_unified_arithmetic_certificate_probe.py
```

reports:

```text
E72.184 unified arithmetic certificate probe
prestable: direct F2B; stable: NTC-8 + ASRP-0.05
 lam    L dim mode    metric1   metric2    D   eps   gnorm  final  pass
   6  3.58  18 F2B     0.962    0.074    -     -       -  0.962 YES
   8  4.16  24 F2B     0.967    0.065    -     -       -  0.967 YES
  10  4.61  28 F2B     0.889    0.210    -     -       -  0.889 YES
  12  4.97  32 ASRP 1.41e-05 8.46e-03   36 0.048   0.922  0.970 YES
  14  5.28  36 ASRP 8.01e-06 8.47e-03   38 0.048   0.887  0.936 YES
  16  5.55  40 ASRP 2.60e-06 6.35e-03   40 0.049   0.864  0.913 YES
  18  5.78  44 ASRP 4.98e-07 3.03e-05   42 0.049   0.835  0.883 YES
  20  5.99  48 ASRP 5.36e-07 9.54e-03   44 0.049   0.845  0.893 YES
  22  6.18  52 ASRP 1.39e-07 5.39e-02   46 0.048   0.860  0.909 YES
  24  6.36  56 ASRP 3.24e-07 7.08e-02   48 0.048   0.846  0.894 YES
  26  6.52  60 ASRP 1.37e-07 4.24e-04   48 0.050   0.686  0.736 YES
  28  6.66  64 ASRP 2.26e-07 2.99e-02   50 0.049   0.745  0.794 YES
  30  6.80  68 ASRP 1.50e-07 7.04e-02   52 0.049   0.810  0.859 YES
  32  6.93  72 ASRP 2.35e-08 3.51e-06   54 0.049   0.697  0.746 YES
worst_certificate_value=0.970 at lambda=12
```

For ASRP rows:

```text
metric1 = Tr((K_0/0.90)^16),
metric2 = Tr((K_1/0.60)^16),
D       = Chebyshev degree,
eps     = certified Hilbert-Schmidt approximation error,
gnorm   = ||G_{x,D}||_HS,
final   = gnorm+eps.
```

For F2B rows:

```text
metric1 = direct residual norm,
metric2 = direct residual margin 1-metric1^2.
```

## 2. Reading

The worst tested certificate value is still the first stable window:

```text
lambda=12, final=0.970.
```

The extended windows `lambda=30,32` do not drift toward failure.

## 3. Current arithmetic theorem

With margin `m_*=0.05`, the exact uniform theorem left to prove is:

```text
For all sufficiently large x:
  Tr((K_0/0.90)^16)<1,
  Tr((K_1/0.60)^16)<1,
  D_x even and D_x+1 >= 0.99 sqrt(d_x)/(0.05 pi),
  Tr(G_{x,D_x}^2)<0.9025.
```

The pre-stable range is finite and handled by direct F2B-PSD.

All three stable inequalities are finite von Mangoldt cycle inequalities:

```text
cycle length 16 for the two NTC inequalities,
cycle length 2D_x=O(sqrt(d_x)) for ASRP-0.05.
```

This is currently the sharpest explicit Phase 72 arithmetic reduction.

E72.188 recommends using the more proof-friendly margin `m_*=0.03`, replacing the last line by:

```text
D_x even and D_x+1 >= 0.99 sqrt(d_x)/(0.03 pi),
Tr(G_{x,D_x}^2)<0.9409.
```

The structure is unchanged; only the degree/margin tradeoff changes.

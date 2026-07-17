# E72.122 -- Scale split for N-FIN

**Date:** 2026-07-09.
**Role:** separate the arithmetic size of the packet from the geometric decay of the shorted maps.

## 0. N-FIN factors

E72.118 reduced `N-FIN` to:

```text
MNorm  = sup ||m_x||||Y_x(tau_j)||,
S1Norm = sup sigma_1(R_x)||Y_x(tau_j)||,
SqNorm = sup sigma_{q+1}(R_x)||Y_x(tau_j)||.
```

The useful split is:

```text
packet size:       ||Y_x(tau_j)||,
shorted geometry:  ||m_x||, sigma_1(R_x), sigma_{q+1}(R_x).
```

## 1. Scale criterion

Let `L=log x`.  A sufficient scale package for `N-FIN` is:

```text
Y-scale:
sup_{tau_j<=T} ||Y_x(tau_j)||/sqrt(x) = O(A_x),

geometry-scale:
sqrt(x)||m_x|| = O(1/A_x),
sqrt(x)sigma_1(R_x)=O(1/A_x),
sqrt(x)sigma_{q+1}(R_x)=O(1/A_x).
```

Then `N-FIN` follows immediately.

The numerics suggest:

```text
A_x ~ L
```

up to small-window fluctuations.

## 2. Diagnostic

The companion script:

```text
E72_122_nfin_scaling_probe.py
```

prints:

```text
||Y||,
||Y||/sqrt(x),
sqrt(x)||m||,
sqrt(x)sigma_1,
sqrt(x)sigma_{q+1},
and the three N-FIN products.
```

Representative output:

```text
E72.122 N-FIN scaling probe q=3
 lam   L roots  max||Y||  Y/sqrtx  ||m||sqrtx  s1sqrtx  sq1sqrtx  maxM  maxS1  maxSq
   6  3.58     3  3.83e+01 6.38e+00   1.17e-01 1.55e-01  1.77e-02 7.50e-01 9.87e-01 1.13e-01
   8  4.16     4  5.91e+01 7.39e+00   8.75e-02 1.50e-01  2.19e-02 6.47e-01 1.11e+00 1.62e-01
  10  4.61     3  8.71e+01 8.71e+00   6.17e-02 9.90e-02  1.39e-02 5.38e-01 8.62e-01 1.21e-01
  12  4.97     4  1.23e+02 1.02e+01   5.91e-02 1.01e-01  1.32e-02 6.04e-01 1.04e+00 1.35e-01
  14  5.28     4  1.38e+02 9.84e+00   3.31e-02 6.45e-02  7.54e-03 3.26e-01 6.35e-01 7.42e-02
```

The products stay bounded because the geometric factors decay roughly like the reciprocal packet
scale after the `1/sqrt(x)` normalization.

## 3. Updated proof target for N-FIN

Instead of proving the three products directly, prove:

```text
Y-scale: finite endpoint discrepancy packet grows at most like sqrt(x)A_x,
G-scale: shorted mass and singular maps are O(1/(sqrt(x)A_x)).
```

With `A_x=L`, this becomes:

```text
||Y|| = O(sqrt(x)L),
||m||, sigma_1, sigma_{q+1}=O(1/(sqrt(x)L)).
```

The direct product form remains sharper and is the official finite condition.  The scale split is the
proof strategy.

## 4. Status

```text
proved: Y-scale + G-scale imply N-FIN;
observed: A_x~L is consistent with the finite harness;
open:   prove packet-size and shorted-geometry scale bounds uniformly.
```

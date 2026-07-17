# E72.118 -- Scalar BNORM certificate

**Date:** 2026-07-09.
**Role:** isolate the norm side of the final bad-subspace gate as three scalar finite bounds.

## 0. BNORM from E72.116

For fixed physical band `H` and bad-subspace rank `q`, E72.116 requires:

```text
sup_{tau_j} ||m_x||||Y_x(tau_j)|| = O(1),
sup_{tau_j} sigma_1(R_x)||Y_x(tau_j)|| = O(1),
sup_{tau_j} sigma_{q+1}(R_x)||Y_x(tau_j)|| = O(1).
```

This is already scalar.  Name:

```text
MNorm_x(H,T)  := sup_{tau_j<=T} ||m_x||||Y_x(tau_j)||,
S1Norm_x(H,T) := sup_{tau_j<=T} sigma_1(R_x)||Y_x(tau_j)||,
SqNorm_x(H,T) := sup_{tau_j<=T} sigma_{q+1}(R_x)||Y_x(tau_j)||.
```

Then:

```text
BNORM <=> MNorm_x(H,T)+S1Norm_x(H,T)+SqNorm_x(H,T)=O(1)
```

on finite root-height windows.

## 1. Finite data

All three quantities are finite:

```text
||m_x||          from the mass row,
sigma_1(R_x)    from the shorted pushforward operator,
sigma_{q+1}(R_x) from the singular tail,
||Y_x(tau_j)||  from endpoint discrepancy Fourier data.
```

No projection, determinant, or limiting zero is hidden in `BNORM`.

## 2. Diagnostic

The companion script:

```text
E72_118_bnorm_probe.py
```

reports these three scalar quantities for `q=3`.

Representative output:

```text
E72.118 BNORM scalar probe q=3
 lam   N roots  max||m||||Y||  max s1||Y||  max sq1||Y||
   6  18     3      7.500e-01    9.873e-01     1.129e-01
   8  24     4      6.469e-01    1.110e+00     1.622e-01
  10  28     3      5.375e-01    8.620e-01     1.213e-01
  12  32     4      6.039e-01    1.037e+00     1.350e-01
  14  36     4      3.260e-01    6.349e-01     7.423e-02
```

The three scalars remain bounded in the tested windows, and the singular tail scalar is well below
the leading singular scalar.

## 3. Current final finite package

Combining E72.117 and E72.118, the non-tail part of Phase 72 is now:

```text
BNORM:
MNorm + S1Norm + SqNorm = O(1),

GBORTH:
det(G_x[Y_j])/(det(G_x)||Y_j||^2) -> 1.
```

Together with `CCGD`, this implies scalar WRL resonance annihilation by E72.116 and E72.113.

## 4. Status

```text
proved: BNORM is equivalent to three scalar finite bounds;
observed: all three remain bounded in tested windows;
open:   prove the three bounds uniformly.
```

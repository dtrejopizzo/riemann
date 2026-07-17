# E72.123 -- Scale split for S-FIN

**Date:** 2026-07-09.
**Role:** reduce Gram determinant saturation to a packet-lower-bound plus bad-projection upper-bound.

## 0. S-FIN from E72.117

The determinant saturation condition is:

```text
Sat_x(H,q,T)
 := inf_{tau_j<=T} det(G_x[Y_j])/(det(G_x)||Y_j||^2) -> 1.
```

Equivalently:

```text
||P_{B,x}Y_j||/||Y_j|| -> 0.
```

Here `B_{x,H,q}` is the finite bad subspace of E72.116.

## 1. Scale criterion

Let `L=log x`.  A sufficient scale split for `S-FIN` is:

```text
Y-lower:
inf_{tau_j<=T} ||Y_x(tau_j)|| >= c sqrt(x)L,                 (YLOW)

bad-upper:
sup_{tau_j<=T} ||P_{B,x}Y_x(tau_j)|| <= C sqrt(x).           (BUP)
```

Then:

```text
sup_{tau_j<=T} ||P_BY_j||/||Y_j|| <= (C/c)L^(-1) -> 0,
```

and hence `S-FIN` follows.

This is only a sufficient route.  The determinant form of E72.117 remains the official exact finite
condition.

## 2. Explicit test form

`BUP` means that finitely many endpoint discrepancy tests are `O(sqrt(x))`:

```text
<Y_x(tau_j),e_a>
 = int_0^L exp(-i tau_jr)T_{x,H,q,a}(r)dE_x^leftarrow(r)
 = O(sqrt(x)).
```

`YLOW` says that the total endpoint discrepancy packet has size at least `sqrt(x)L` in the finite
packet norm.

Thus `S-FIN` is a separation of scales:

```text
finitely many bad tests:  O(sqrt(x)),
full packet:             Omega(sqrt(x)L).
```

## 3. Diagnostic

The companion script:

```text
E72_123_sfin_scale_probe.py
```

reports:

```text
||Y||/(sqrt(x)L),
||P_BY||/sqrt(x),
L||P_BY||/||Y||.
```

Representative output:

```text
E72.123 S-FIN scale split probe q=3
 lam   L roots  Y/(sqrtx L)  PB/sqrtx  L*PB/Y  maxProjRatio
   6  3.58     3    1.781e+00 9.691e-01 5.618e-01    1.568e-01
   8  4.16     4    1.778e+00 8.666e-01 5.295e-01    1.273e-01
  10  4.61     3    1.891e+00 7.527e-01 4.256e-01    9.242e-02
  12  4.97     4    2.058e+00 5.675e-01 3.124e-01    6.286e-02
  14  5.28     4    1.865e+00 5.436e-01 3.086e-01    5.847e-02
```

The data support:

```text
||Y|| ~ sqrt(x)L,
||P_BY|| = O(sqrt(x)).
```

## 4. Updated final checklist

The current endpoint may be attacked as:

```text
CGE-K,
Y-scale + G-scale,
YLOW + BUP.
```

These imply:

```text
CGE-K + N-FIN + S-FIN,
```

and hence scalar WRL resonance annihilation by E72.119.

## 5. Status

```text
proved: YLOW + BUP imply S-FIN;
observed: scale separation is consistent with the finite harness;
open:   prove YLOW and BUP uniformly.
```

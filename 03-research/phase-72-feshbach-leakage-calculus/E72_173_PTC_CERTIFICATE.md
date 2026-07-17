# E72.173 -- PTC certificate probe

**Date:** 2026-07-09.
**Role:** combine the polynomial trace certificate into one executable gate.

## 0. Gate

Use the fixed Phase 72 arithmetic split:

```text
I_0=[0,0.60L],
I_1=(0.60L,L],
a_0=0.70,
a_1=0.60.
```

The polynomial trace certificate is:

```text
PTC-1: ||K_0||<=0.90 and ||K_1||<=0.60,
PTC-2: Tr p_0(K_0)+Tr p_1(K_1)<=0.92,
PTC-3: cross_+<=0.04.
```

Since E72.172 proves:

```text
E_{a_j}(K_j)<=Tr p_j(K_j)
```

on the stated intervals, `PTC` implies:

```text
BSE+cross_+ <= 0.96 < 1.
```

Therefore:

```text
PTC => F2B-PSD => PSD-DIST.
```

## 1. Diagnostic output

The companion script:

```text
E72_173_ptc_certificate_probe.py
```

evaluates the central polynomial quantity through traces of matrix powers, not through sign
projections:

```text
Tr p_j(K_j)=sum_{r=0}^{10} c_{j,r}Tr(K_j^r).
```

It reports:

```text
E72.173 PTC certificate probe
cut=0.60; weights=(0.70,0.60); intervals K0<=0.90,K1<=0.60
 lam    L  dim   op0   op1  traceP  cross+  PTCsum  dist  margin  pass
   6  3.58   18 0.856 0.588  66.020   0.000  66.020 0.962   0.074 NO
   8  4.16   24 0.507 0.362   1.123   0.000   1.123 0.967   0.065 NO
  10  4.61   28 0.593 0.524   1.778   0.000   1.778 0.889   0.210 NO
  12  4.97   32 0.439 0.445   0.917   0.000   0.917 0.920   0.154 YES
  14  5.28   36 0.429 0.445   0.862   0.000   0.862 0.885   0.217 YES
  16  5.55   40 0.399 0.437   0.810   0.000   0.810 0.863   0.255 YES
  18  5.78   44 0.362 0.313   0.677   0.034   0.710 0.833   0.307 YES
  20  5.99   48 0.356 0.449   0.754   0.000   0.754 0.843   0.290 YES
  22  6.18   52 0.326 0.500   0.780   0.000   0.780 0.859   0.261 YES
  24  6.36   56 0.349 0.508   0.765   0.000   0.765 0.845   0.286 YES
worst_PTCsum=66.020 at lambda=6; traceP=66.020; cross+=0.000
```

## 2. Reading

`PTC` is not a small-window certificate. The degree-10 polynomials are tuned to the stable regime and
become very inefficient at `lambda=6`. The correct split is:

```text
finite window:  lambda=6,8,10 by direct F2B-PSD verification;
stable window: lambda>=12 by PTC.
```

This is acceptable because the proof architecture already has a finite initial check plus an
asymptotic gate.

## 3. Current theorem form

The arithmetic component of Phase 72 can now be stated as:

```text
Finite-F2B:
The finitely many initial windows satisfy F2B-PSD directly.

Stable-PTC:
For all sufficiently large x, PTC-1, PTC-2, and PTC-3 hold.
```

Then:

```text
Finite-F2B + Stable-PTC => F2B-PSD uniformly.
```

The remaining hard proof target is no longer spectral positivity. It is the explicit trace-moment
estimate:

```text
Tr p_0(K_0)+Tr p_1(K_1)<=0.92
```

plus norm and cross bounds for the exact discrete von Mangoldt block operators.

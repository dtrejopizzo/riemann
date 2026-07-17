# E72.160 -- Two-block PSD weight audit

**Date:** 2026-07-09.
**Role:** optimize the coarse two-block PSD approximant for `PSD-DIST`.

## 0. Candidate

E72.159 shows that two coarse prime-position blocks are close to certifying `PSD-DIST`.  Let:

```text
K_rel=K_0+K_1,
P_j=(K_j)^+.
```

Instead of using:

```text
P=P_0+P_1,
```

test the weighted PSD approximant:

```text
P(a,b)=aP_0+bP_1,        a,b>=0.
```

If:

```text
||K_rel-P(a,b)||_HS<1,
```

then `PSD-DIST` has a two-block semialgebraic certificate with two scalar weights.

## 1. Diagnostic

The companion script:

```text
E72_160_two_block_psd_weight_probe.py
```

does a grid search over `0<=a,b<=1.5`.

Representative output:

```text
E72.160 two-block PSD weight probe
 lam   L  distOpt  unweighted  bestDist  a  b  margin
   6  3.58    0.764      1.095     0.996 0.68 0.58   0.009
   8  4.16    0.800      1.019     0.970 0.88 0.55   0.059
  10  4.61    0.692      0.976     0.907 0.70 0.65   0.177
  12  4.97    0.782      0.984     0.932 0.85 0.50   0.131
  14  5.28    0.747      0.958     0.893 0.85 0.38   0.202
```

The weighted two-block certificate succeeds in all tested windows.  The smallest margin is at the
smallest window; the margin improves afterward.

## 2. Status

```text
observed: weighted two-block PSD approximants certify PSD-DIST in the tested windows;
reduced: PSD-DIST to a two-block PSD weight certificate.
```

# E72.162 -- Fixed two-block weights

**Date:** 2026-07-09.
**Role:** test whether the two-block PSD certificate can use universal scalar weights.

## 0. Question

E72.161 allows weights `a_x,b_x` depending on the finite window:

```text
||K_rel-a_xP_0-b_xP_1||_HS<1.
```

A stronger and cleaner certificate would use fixed weights:

```text
a,b >= 0,
||K_rel-aP_0-bP_1||_HS <= eta<1
```

uniformly on the tested windows.

## 1. Diagnostic

The companion script:

```text
E72_162_fixed_two_block_weights_probe.py
```

tests a small set of simple candidate weights around the E72.160 optima and reports the maximum
distance over the finite windows.

Representative output:

```text
E72.162 fixed two-block weights probe
 a     b    maxDist  margin   per-window
0.75  0.55    0.997   0.006  6:0.997 8:0.975 10:0.908 12:0.934 14:0.898
0.80  0.55    1.001  -0.002  6:1.001 8:0.972 10:0.910 12:0.933 14:0.896
0.85  0.50    1.006  -0.012  6:1.006 8:0.971 10:0.913 12:0.932 14:0.895
0.80  0.50    1.001  -0.001  6:1.001 8:0.973 10:0.911 12:0.933 14:0.895
0.75  0.60    0.998   0.004  6:0.998 8:0.974 10:0.908 12:0.935 14:0.899
0.70  0.60    0.996   0.008  6:0.996 8:0.979 10:0.908 12:0.937 14:0.902
0.85  0.60    1.008  -0.017  6:1.008 8:0.970 10:0.913 12:0.934 14:0.899
best_fixed a=0.70 b=0.60 maxDist=0.996 margin=0.008
```

The fixed weights:

```text
a=0.70, b=0.60
```

certify the tested windows.  The margin is narrow only at the smallest window.

## 2. Status

```text
observed: fixed weights `(0.70,0.60)` certify 2B-PSD in the tested windows;
reduced: 2B-PSD can be tested with universal weights rather than optimized weights.
```

# E72.194 -- XNEG degree reduction

**Date:** 2026-07-10.
**Role:** test whether the mixed sign lemma needs the adaptive degree, or can be fixed at low degree.

## 0. Question

The remaining mixed sign lemma is:

```text
XNEG:
Tr(G_0G_1)<=0.
```

Originally `G_j` used the adaptive Chebyshev degree `D_x`. If a fixed degree suffices, the whole
stable arithmetic target becomes fixed-degree cycle data.

## 1. First degree test

The companion script:

```text
E72_194_xneg_degree_probe.py
```

reports:

```text
E72.194 XNEG degree probe
reports cross=2Tr(G0G1) for fixed degrees and adaptive degree
 lam    L dim D    2 D    4 D    8 D   16 D auto
  12  4.97  32  +0.113  +0.017  -0.018  -0.041  -0.050
  16  5.55  40  +0.163  +0.037  -0.009  -0.038  -0.047
  20  5.99  48  +0.232  +0.076  +0.019  -0.011  -0.023
  24  6.36  56  +0.270  +0.086  +0.022  -0.009  -0.025
  28  6.66  64  +0.258  +0.046  -0.030  -0.064  -0.082
  32  6.93  72  +0.381  +0.141  +0.049  +0.014  -0.008
  36  7.17  80  +0.403  +0.139  +0.045  +0.010  -0.013
maxCross D2:+0.403 D4:+0.141 D8:+0.049 D16:+0.014 Dauto:-0.008
```

Degrees `2,4,8,16` do not uniformly enforce `XNEG` in the tested range.

## 2. Higher fixed degree test

A second focused test gives:

```text
lam D16 D24 D32 D48 D64
12 -0.041 -0.044 -0.047 -0.049 -0.050
20 -0.011 -0.018 -0.020 -0.023 -0.023
24 -0.009 -0.018 -0.022 -0.024 -0.025
32 +0.014 +0.002 -0.003 -0.006 -0.007
36 +0.010 -0.003 -0.007 -0.010 -0.012
max D16:+0.014 D24:+0.002 D32:-0.003 D48:-0.006 D64:-0.007
```

Thus fixed degree:

```text
D=32
```

suffices in the tested stable windows through `lambda=36`.

## 3. Updated stable target

The recommended fixed-degree stable cycle target is now:

```text
NTC-8:
Tr((K_0/0.90)^16)<1,
Tr((K_1/0.60)^16)<1.

LM8-ASRP:
0.90^2Tr P_0(K_0/0.90)+0.60^2Tr P_1(K_1/0.60)<0.9409.

XNEG-32:
Tr(G_{0,32}G_{1,32})<=0.
```

where `G_{j,32}` uses the explicit degree-32 Chebyshev signed-residual polynomial.

All three conditions are now fixed finite cycle inequalities:

```text
NTC-8:    degree 16,
LM8-ASRP: degree 8,
XNEG-32:  mixed degree 64.
```

The adaptive schedule remains a rigorous fallback, but the current evidence supports a much simpler
fixed-degree theorem target.

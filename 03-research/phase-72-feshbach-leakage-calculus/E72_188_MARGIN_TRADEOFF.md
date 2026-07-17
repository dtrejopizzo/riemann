# E72.188 -- ASRP margin tradeoff

**Date:** 2026-07-09.
**Role:** choose a proof-friendly margin for the adaptive ASRP certificate.

## 0. Motivation

E72.182 fixed:

```text
m_*=0.05,
Tr(G_{x,D_x}^2)<(1-m_*)^2=0.9025.
```

This passes numerically but is tight at the first stable window:

```text
lambda=12.
```

Reducing `m_*` raises the degree `D_x` but relaxes the cycle inequality:

```text
Tr(G^2)<(1-m_*)^2.
```

This may be a better theorem target.

## 1. Output

The companion script:

```text
E72_188_margin_tradeoff_probe.py
```

reports:

```text
E72.188 ASRP margin tradeoff probe
entries are ||G||+eps; target is ||G||<1-m and final<1
prepared lambda=12
prepared lambda=16
prepared lambda=20
prepared lambda=24
prepared lambda=28
prepared lambda=32
 m*  maxD  worstG@lam  target  worstFinal@lam  per-window
0.05    54  0.922@12  0.950  0.970@12 12:0.922+0.048 16:0.864+0.049 20:0.845+0.049 24:0.846+0.048 28:0.745+0.049 32:0.697+0.049
0.04    66  0.921@12  0.960  0.961@12 12:0.921+0.040 16:0.864+0.039 20:0.844+0.040 24:0.846+0.040 28:0.744+0.039 32:0.697+0.040
0.03    90  0.921@12  0.970  0.950@12 12:0.921+0.029 16:0.864+0.030 20:0.844+0.030 24:0.846+0.030 28:0.744+0.030 32:0.696+0.029
0.02   134  0.921@12  0.980  0.940@12 12:0.921+0.020 16:0.864+0.020 20:0.843+0.020 24:0.846+0.020 28:0.744+0.020 32:0.695+0.020
```

## 2. Recommended margin

The recommended theorem target is:

```text
m_*=0.03.
```

Then:

```text
Tr(G_{x,D_x}^2)<0.9409,
```

with automatic even degree:

```text
D_x+1 >= 0.99 sqrt(d_x)/(0.03 pi).
```

In the tested stable windows:

```text
worst ||G|| = 0.921 at lambda=12,
target     = 0.970,
worst final bound = 0.950.
```

Compared with `m_*=0.05`, this buys a much larger cycle inequality margin at the cost of increasing
the degree by about a factor `5/3`.

## 3. Updated final target

The proof-friendly stable arithmetic target is:

```text
NTC-8:
Tr((K_0/0.90)^16)<1,
Tr((K_1/0.60)^16)<1.

D-ASRP-0.03:
Tr(G_{0,D_x}^2)+Tr(G_{1,D_x}^2)<0.9409.

XNEG:
Tr(G_{0,D_x}G_{1,D_x})<=0.
```

where:

```text
D_x even,
D_x+1 >= 0.99 sqrt(d_x)/(0.03 pi).
```

Then:

```text
NTC-8 + D-ASRP-0.03 + XNEG => F2B-PSD.
```

This is now the recommended finite cycle target for the next proof attempt.

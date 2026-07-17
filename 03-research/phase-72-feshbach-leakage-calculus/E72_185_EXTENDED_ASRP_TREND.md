# E72.185 -- Extended ASRP trend

**Date:** 2026-07-09.
**Role:** stress the stable arithmetic certificate beyond E72.184 and identify the dominant term.

## 0. Question

E72.184 unified the arithmetic certificate:

```text
pre-stable: direct F2B,
stable:     NTC-8 + ASRP-0.05.
```

The next check is whether the stable certificate drifts toward failure as the window grows, and which
quantity dominates:

```text
NTC-8, approximation error, or ||G_{x,D_x}||_HS.
```

## 1. Output

The companion script:

```text
E72_185_extended_asrp_trend_probe.py
```

reports:

```text
E72.185 extended ASRP trend probe
stable certificate: NTC-8 + ASRP-0.05
 lam    L dim  op0  op1    ntc1    D   eps   gnorm    g2   final pass
  12  4.97  32 0.439 0.445 8.46e-03   36 0.048   0.922  0.850   0.970 YES
  16  5.55  40 0.399 0.437 6.35e-03   40 0.049   0.864  0.747   0.913 YES
  20  5.99  48 0.356 0.449 9.54e-03   44 0.049   0.845  0.713   0.893 YES
  24  6.36  56 0.349 0.508 7.08e-02   48 0.048   0.846  0.716   0.894 YES
  28  6.66  64 0.346 0.482 2.99e-02   50 0.049   0.745  0.555   0.794 YES
  32  6.93  72 0.300 0.274 3.51e-06   54 0.049   0.697  0.486   0.746 YES
  34  7.05  76 0.312 0.509 7.22e-02   54 0.050   0.808  0.652   0.858 YES
  36  7.17  80 0.306 0.508 7.05e-02   56 0.049   0.798  0.637   0.848 YES
worst_final=0.970 at lambda=12
```

## 2. Reading

The extended windows `lambda=34,36` pass. The worst stable row remains:

```text
lambda=12.
```

The approximation error is held near `0.05` by construction. `NTC-8` remains far below `1`; even the
larger `K1` rows have:

```text
NTC1 ~ 0.07.
```

Therefore the ASRP inequality is governed by:

```text
||G_{x,D_x}||_HS,
```

not by the norm-interval certificate or the polynomial approximation error.

## 3. Next proof target

The hard cycle inequality is:

```text
Tr(G_{x,D_x}^2)<0.9025.
```

The next useful decomposition is:

```text
Tr(G^2)
=Tr(g_0(K_0)^2)+Tr(g_1(K_1)^2)+2Tr(g_0(K_0)g_1(K_1)).
```

If the mixed term is consistently negative, the proof must retain block interaction. If it is small,
the proof can split into two one-block estimates.

# E72.186 -- G-cycle block decomposition

**Date:** 2026-07-09.
**Role:** decompose the ASRP cycle inequality into pure block terms and a mixed term.

## 0. Decomposition

For:

```text
G=g_0(K_0)+g_1(K_1)=G_0+G_1,
```

the ASRP cycle is:

```text
Tr(G^2)=Tr(G_0^2)+Tr(G_1^2)+2Tr(G_0G_1).
```

This asks whether the stable inequality:

```text
Tr(G^2)<0.9025
```

requires a large mixed cancellation, or whether the pure block terms are already small.

## 1. Output

The companion script:

```text
E72_186_gcycle_block_decomposition_probe.py
```

reports:

```text
E72.186 G-cycle block decomposition probe
G=g0(K0)+g1(K1); reports Tr(G0^2), Tr(G1^2), 2Tr(G0G1)
 lam    L dim   D   G0sq   G1sq   cross     G2  crossFrac final
  12  4.97  32  36  0.565  0.333   -0.048  0.850    -0.053  0.970
  16  5.55  40  40  0.457  0.337   -0.047  0.747    -0.059  0.913
  20  5.99  48  44  0.403  0.332   -0.022  0.713    -0.030  0.893
  24  6.36  56  48  0.373  0.368   -0.024  0.716    -0.033  0.894
  28  6.66  64  50  0.296  0.340   -0.082  0.555    -0.128  0.794
  32  6.93  72  54  0.320  0.173   -0.007  0.486    -0.014  0.746
  34  7.05  76  54  0.317  0.360   -0.025  0.652    -0.037  0.858
  36  7.17  80  56  0.307  0.342   -0.012  0.637    -0.018  0.848
```

## 2. Reading

The mixed term is consistently negative in this stress test, but it is not a large cancellation. The
pure diagonal energy:

```text
Tr(G_0^2)+Tr(G_1^2)
```

is already below the ASRP target `0.9025` in all tested stable windows. The worst row is:

```text
lambda=12: G0sq+G1sq=0.898.
```

Thus the ASRP theorem can be sharpened to the sufficient pair:

```text
D-ASRP:
Tr(G_0^2)+Tr(G_1^2)<0.9025.

XNEG:
Tr(G_0G_1)<=0.
```

Then:

```text
D-ASRP + XNEG => ASRP-0.05.
```

`XNEG` is a much smaller mixed statement than the full ASRP inequality. If `XNEG` proves structural,
the main arithmetic work splits into two one-block cycle estimates.

## 3. Updated target

The current best proof decomposition is:

```text
NTC-8 for intervals,
D-ASRP for pure residual energy,
XNEG for mixed sign.
```

All are finite cycle inequalities:

```text
NTC-8:  length 16,
D-ASRP: pure cycles up to length 2D_x,
XNEG:   mixed cycles up to length 2D_x.
```

The evidence suggests `D-ASRP` is the dominant estimate; `XNEG` should be tested and attacked as a
separate sign/ordering lemma.

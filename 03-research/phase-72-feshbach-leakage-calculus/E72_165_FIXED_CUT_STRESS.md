# E72.165 -- Fixed-cut stress for F2B-PSD

**Date:** 2026-07-09.
**Role:** stress the current fixed arithmetic certificate without changing any parameter.

## 0. Fixed certificate under stress

Keep the E72.163/E72.164 constants:

```text
I_0=[0,0.60L],
I_1=(0.60L,L],
a=0.70,
b=0.60.
```

Let:

```text
P_j=(K_j)^+.
```

The tested inequality is still:

```text
||K_rel-0.70P_0-0.60P_1||_HS < 1.                  (F2B-PSD)
```

No cut or weight is refit in this experiment.

## 1. Output

The companion script:

```text
E72_165_fixed_cut_stress_probe.py
```

reports:

```text
E72.165 fixed-cut fixed-weight 2B-PSD stress probe
cut=0.60, a=0.70, b=0.60
 lam    L   dim   distHS   margin  ||Krel||  ||P0||  ||P1||  opRes
   6  3.58    37    0.962    0.074    1.300   1.165   0.461  0.540
   8  4.16    49    0.967    0.065    1.315   0.950   0.502  0.526
  10  4.61    57    0.889    0.210    1.195   0.976   0.447  0.492
  12  4.97    65    0.920    0.154    1.204   0.888   0.401  0.617
  14  5.28    73    0.885    0.217    1.149   0.856   0.393  0.608
  16  5.55    81    0.863    0.255    1.115   0.802   0.398  0.586
  18  5.78    89    0.833    0.307    1.094   0.735   0.362  0.570
  20  5.99    97    0.843    0.290    1.071   0.755   0.359  0.596
worst lambda=8 dist=0.967 margin=0.065
```

## 2. Consequence

The worst case remains the previously tested window `lambda=8`; the larger windows do not drift
toward the boundary. This upgrades the status of the fixed certificate from a small-window fit to a
stable finite pattern:

```text
cut=0.60, weights=(0.70,0.60), margin >= 0.065
```

over all tested windows through `lambda=20`.

## 3. New proof target

The remaining arithmetic gate can now be sharpened to:

```text
F2B-PSD(0.60;0.70,0.60):
sup_x ||K_rel(x)-0.70(K_0(x))^+-0.60(K_1(x))^+||_HS <= eta < 1.
```

This is stronger than the abstract `PSD-DIST` target because it fixes both the positive approximant
and the constants. The next analytic task is to prove the two broad prime-position blocks have enough
coherent positive part to absorb the relative arithmetic perturbation with a uniform Hilbert-Schmidt
tail.

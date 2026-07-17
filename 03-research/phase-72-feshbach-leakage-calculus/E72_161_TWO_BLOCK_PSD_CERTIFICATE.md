# E72.161 -- Two-block PSD certificate

**Date:** 2026-07-09.
**Role:** replace abstract `PSD-DIST` by a constructive two-block certificate.

## 0. Blocks

Partition the prime-position interval:

```text
0<=y=m log p<=L
```

into two blocks:

```text
I_0=[0,L/2],
I_1=(L/2,L].
```

Write the relative arithmetic perturbation as:

```text
K_rel=K_0+K_1,
```

where `K_j` is the model-normalized sum of prime-power cells with `y in I_j`.

Let:

```text
P_j=(K_j)^+.
```

## 1. Certificate

Assume that there exist nonnegative scalars `a_x,b_x` and a constant `eta<1` such that:

```text
||K_rel-a_xP_0-b_xP_1||_HS <= eta.                          (2B-PSD)
```

Then `PSD-DIST` holds, because:

```text
P_x=a_xP_0+b_xP_1 >= 0.
```

Therefore:

```text
2B-PSD => PSD-DIST => RFBD => RCOER.
```

## 2. Consequence

The current route may now be stated with no abstract PSD existence:

```text
GCOER + 2B-PSD + B-scale + Y-scale + OPM + UKERN + ROP + CGE-K
=> scalar WRL resonance annihilation.
```

## 3. Numerical audit

E72.160 performs a grid search over `a,b>=0`.  Representative output:

```text
E72.160 two-block PSD weight probe
 lam   L  distOpt  unweighted  bestDist  a  b  margin
   6  3.58    0.764      1.095     0.996 0.68 0.58   0.009
   8  4.16    0.800      1.019     0.970 0.88 0.55   0.059
  10  4.61    0.692      0.976     0.907 0.70 0.65   0.177
  12  4.97    0.782      0.984     0.932 0.85 0.50   0.131
  14  5.28    0.747      0.958     0.893 0.85 0.38   0.202
```

## 4. Status

```text
proved: 2B-PSD implies PSD-DIST;
observed: 2B-PSD holds in tested windows with explicit weights;
open:   prove the two-block weighted distance bound uniformly.
```

# E72.144 -- Low-rank PSD certificate audit

**Date:** 2026-07-09.
**Role:** test whether `PSD-DIST` can be certified with a low-rank positive approximant.

## 0. Rank-truncated positive part

Let:

```text
K_rel = sum_a lambda_a u_au_a^*
```

and let the positive eigenvalues be ordered:

```text
lambda_1^+ >= lambda_2^+ >= ...
```

The best rank-`r` PSD approximation is:

```text
P_r=sum_{a<=r} lambda_a^+u_a^+(u_a^+)^*.
```

Its squared Frobenius distance is:

```text
||K_rel-P_r||_HS^2
 = ||K_rel^-||_HS^2 + sum_{a>r}(lambda_a^+)^2.
```

Thus a low-rank PSD certificate exists if this quantity is `<1` for small `r`.

## 1. Diagnostic

The companion script:

```text
E72_144_low_rank_psd_probe.py
```

reports:

```text
positive rank,
minimum positive rank needed for distance <1,
distance at that rank,
optimal distance,
top positive eigenvalue,
positive tail after the chosen rank.
```

Representative output:

```text
E72.144 low-rank PSD certificate probe
 lam   L  dim  posRank  minRank<1  dist@rank  optDist  topPos  tailPosHS
   6  3.58   18        6         3      0.896    0.764   0.607     0.468
   8  4.16   24        8         3      0.966    0.800   0.569     0.540
  10  4.61   28       10         3      0.923    0.692   0.495     0.612
  12  4.97   32       11         3      0.982    0.782   0.463     0.593
  14  5.28   36       13         3      0.952    0.747   0.398     0.589
  16  5.55   40       13         2      0.994    0.724   0.371     0.680
  18  5.78   44       13         2      0.981    0.728   0.347     0.658
```

Only two or three positive directions are enough to certify distance `<1` in the tested windows.
Therefore `PSD-DIST` can be attacked as a low-rank positive certificate plus a tail bound.

## 2. Status

```text
observed: rank 2--3 positive approximants already certify PSD-DIST numerically;
next:     identify the structural origin of the first positive relative modes.
```

# E72.136 -- Model coercivity first audit

**Date:** 2026-07-09.
**Role:** test whether model complement coercivity has an elementary diagonal-dominance proof.

## 0. Target

The model coercivity estimate is:

```text
C_model >= a_H L I.                                         (MCOER)
```

The first cheap proof route is Gershgorin:

```text
min_i (C_{ii}-sum_{j!=i}|C_{ij}|) >= a_H L.
```

If this works, `(MCOER)` is a finite entrywise inequality.

## 1. Diagnostic

The companion script:

```text
E72_136_model_gershgorin_probe.py
```

reports:

```text
lambda_min(C_model)/L,
min diagonal/L,
max off-row-sum/L,
Gershgorin lower bound/L.
```

Representative output:

```text
E72.136 model Gershgorin coercivity probe
 lam   L  minEig/L  minDiag/L  maxOffRow/L  GershLow/L
   6  3.58 7.296e-01 1.038e+00    1.125e+00   3.292e-01
   8  4.16 9.918e-01 1.383e+00    1.657e+00   4.122e-01
  10  4.61 1.221e+00 1.596e+00    1.702e+00   6.743e-01
  12  4.97 1.514e+00 1.893e+00    3.078e+00   7.593e-01
  14  5.28 1.711e+00 2.025e+00    2.716e+00   7.156e-01
  16  5.55 1.913e+00 2.283e+00    2.902e+00   1.043e+00
```

The Gershgorin lower bound is positive in the tested windows.  Thus `MCOER` can be attacked by a
finite entrywise inequality rather than a hidden spectral argument.

## 2. Status

```text
observed: Gershgorin lower bound proves model coercivity numerically;
reduced: MCOER to entrywise diagonal/off-row estimates for C_model.
```

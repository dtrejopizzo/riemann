# E72.156 -- Uniform tau-window kernel saturation

**Date:** 2026-07-09.
**Role:** test whether `KERN-ORTH` holds uniformly in a physical tau window.

## 0. Motivation

E72.155 shows that `KERN-ORTH` is not specific to actual finite roots.  The next possible strengthening
is:

```text
sup_{0<tau<=T}
||P_Row(M_x)Y_x(tau)||/||Y_x(tau)|| = O(1/L).               (UKERN)
```

If `(UKERN)` holds, then `CPM-Q` follows without using the root equation.

## 1. Diagnostic

The companion script:

```text
E72_156_uniform_tau_kernel_probe.py
```

samples a dense grid in `0.25<=tau<=6` and reports:

```text
max distance to ker(M_x),
L times max distance,
median L-distance,
tau where the maximum occurs.
```

Representative output:

```text
E72.156 uniform tau kernel probe
 lam   L  grid  maxDist  L*maxDist  medianLdist  tauAtMax
   6  3.58    41 1.593e-01  5.707e-01    3.531e-01    6.000
   8  4.16    41 1.501e-01  6.243e-01    4.254e-01    6.000
  10  4.61    41 1.236e-01  5.694e-01    4.261e-01    6.000
  12  4.97    41 1.405e-01  6.980e-01    1.761e-01    6.000
  14  5.28    41 1.076e-01  5.678e-01    2.911e-01    6.000
  16  5.55    41 1.401e-01  7.769e-01    2.827e-01    6.000
  18  5.78    41 3.993e-02  2.309e-01    1.858e-01    6.000
```

The maximum occurs at the window edge `tau=6` in these runs, and `L*maxDist` remains below `0.78`.
This supports the stronger uniform statement `(UKERN)`.

## 2. Status

```text
reduced: KERN-ORTH to the uniform tau-window estimate UKERN;
observed: UKERN holds on the tested tau grid with bounded L*distance.
```

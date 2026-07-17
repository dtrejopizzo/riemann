# E72.155 -- KERN-ORTH root specificity

**Date:** 2026-07-09.
**Role:** test whether the kernel saturation in E72.154 is genuinely tied to finite CCM roots.

## 0. Question

E72.154 shows:

```text
||P_Row(M_x)Y_x(tau_j)||/||Y_x(tau_j)|| = O(1/L)
```

at actual finite CCM roots `tau_j`.  To decide whether this is a root identity rather than a generic
size phenomenon, compare three sets of heights:

```text
actual roots: tau_j(xi),
model roots:  tau_j(k),
grid heights: generic tau in the same physical window.
```

If actual roots have much smaller distance to `ker(M_x)`, then `KERN-ORTH` is root-specific.

## 1. Diagnostic

The companion script:

```text
E72_155_kernorth_root_specificity_probe.py
```

reports:

```text
L*dist at actual roots,
L*dist at model roots,
L*dist at generic grid points,
actual/grid ratio.
```

Representative output:

```text
E72.155 KERN-ORTH root-specificity probe
 lam   L  act# mod#  L*actDist  L*modelDist  L*gridDist  act/grid
   8  4.16     4    3  6.202e-01    5.906e-01   6.071e-01 1.021e+00
  10  4.61     3    2  4.400e-01    4.268e-01   5.574e-01 7.895e-01
  12  4.97     4    2  3.223e-01    3.605e-01   6.614e-01 4.874e-01
  14  5.28     4    1  3.273e-01    3.327e-01   5.358e-01 6.109e-01
  16  5.55     5    2  7.020e-01    2.680e-01   7.691e-01 9.128e-01
  18  5.78     5    2  1.906e-01    1.952e-01   2.077e-01 9.177e-01
```

The effect is not actual-root specific.  Model roots and generic grid heights have comparable
`L*dist` values.  Therefore `KERN-ORTH` is likely a geometric packet/operator property rather than a
delicate actual-root cancellation.

## 2. Status

```text
observed: KERN-ORTH is not actual-root specific;
next:     test uniform tau-window kernel saturation.
```

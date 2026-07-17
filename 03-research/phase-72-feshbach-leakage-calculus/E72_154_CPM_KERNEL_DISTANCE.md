# E72.154 -- CPM kernel distance

**Date:** 2026-07-09.
**Role:** test whether `CPM-Q` is equivalent to nearness of root packets to `ker M_x`.

## 0. Kernel formulation

Let:

```text
M_x=B_x^*P_HLK_x.
```

Let `Row(M_x)` be the row space of `M_x`, equivalently `ker(M_x)^\perp`.  The distance from a packet
`Y` to the kernel is:

```text
dist(Y,ker M_x)/||Y|| = ||P_Row(M_x)Y||/||Y||.
```

If this distance is `O(1/L)`, then `CPM-Q` follows immediately because:

```text
||M_xY|| <= ||M_x||||P_Row(M_x)Y||.
```

## 1. Diagnostic

The companion script:

```text
E72_154_cpm_kernel_distance_probe.py
```

reports:

```text
rank(M_x),
dim ker(M_x),
max dist(Y,ker M_x)/||Y||,
L times that distance,
minimum nonzero singular value,
maximum singular value.
```

Representative output:

```text
E72.154 CPM kernel distance probe
 lam   L roots  rankM  nullDim  maxDistToKer  L*dist  minNonzeroSV  maxSV
   6  3.58     3      5      69    1.569e-01 5.623e-01    2.243e-01  0.529
   8  4.16     4      6      92    1.491e-01 6.202e-01    9.006e-02  0.621
  10  4.61     3      6     108    9.555e-02 4.400e-01    1.809e-01  0.524
  12  4.97     4      7     123    6.485e-02 3.223e-01    1.814e-01  0.641
  14  5.28     4      7     139    6.202e-02 3.273e-01    1.189e-01  0.593
  16  5.55     5      8     154    1.266e-01 7.020e-01    9.294e-02  0.591
  18  5.78     5      8     170    3.297e-02 1.906e-01    1.045e-01  0.922
```

The distance to the kernel is `O(1/L)` in the tested windows.  Therefore `CPM-Q` can be attacked as a
kernel-saturation statement:

```text
||P_Row(M_x)Y_x(tau_j)||/||Y_x(tau_j)|| = O(1/L).            (KERN-ORTH)
```

## 2. Status

```text
reduced: CPM-Q to KERN-ORTH;
observed: L*dist(Y,ker M_x) is bounded in the finite harness.
```

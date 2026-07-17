# E72.151 -- CPM alignment

**Date:** 2026-07-09.
**Role:** identify the cancellation behind `CPM-scale`.

## 0. Operator

Set:

```text
M_x := B_x^*P_HLK_x.
```

Then:

```text
c_H^{pm}(tau_j)=(2/(Lsqrt(x)))M_xY_x(tau_j).
```

E72.150 shows `||M_x||=O(1)`, so `CPM-scale` cannot follow from a raw operator norm estimate.  It
requires:

```text
||M_xY_x(tau_j)|| << ||M_x||||Y_x(tau_j)||.                 (CPM-ORTH)
```

## 1. Diagnostic

The companion script:

```text
E72_151_cpm_alignment_probe.py
```

reports:

```text
align = ||M_xY||/(||M_x||||Y||),
L*align,
relative top-3 singular energy,
relative tail-after-3 bound,
max||cpm||.
```

Representative output:

```text
E72.151 cpm alignment probe
 lam   L roots  maxAlign  L*align  topEnergy  tail3Bound  max||cpm||
   6  3.58     3 9.534e-02 3.416e-01 5.491e-02  5.428e-01  1.741e-01
   8  4.16     4 5.444e-02 2.264e-01 4.699e-02  3.606e-01  1.098e-01
  10  4.61     3 6.753e-02 3.110e-01 5.935e-02  5.509e-01  1.167e-01
  12  4.97     4 2.805e-02 1.394e-01 1.942e-02  4.862e-01  6.535e-02
  14  5.28     4 2.883e-02 1.522e-01 2.129e-02  4.315e-01  6.020e-02
  16  5.55     5 3.004e-02 1.666e-01 1.808e-02  5.341e-01  6.922e-02
  18  5.78     5 1.042e-02 6.023e-02 6.792e-03  3.497e-01  4.127e-02
```

The alignment is much stronger than a generic norm bound:

```text
||M_xY_x(tau_j)||/(||M_x||||Y_x(tau_j)||)=O(1/L)
```

in the tested windows.

## 2. Status

```text
reduced: CPM-scale to finite singular orthogonality CPM-ORTH;
observed: L*align is bounded and small in the finite harness.
```

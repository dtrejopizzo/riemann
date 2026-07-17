# E72.153 -- CPM quadratic certificate

**Date:** 2026-07-09.
**Role:** state `CPM-ORTH` as one finite quadratic inequality.

## 0. Operator

Let:

```text
M_x:=B_x^*P_HLK_x.
```

The alignment condition from E72.151 is:

```text
||M_xY_x(tau_j)|| <= C L^(-1)||M_x||||Y_x(tau_j)||.          (CPM-ORTH)
```

Equivalently:

```text
Q_CPM(x,tau_j)
 := Y_x(tau_j)^*M_x^*M_xY_x(tau_j)
    /(||M_x||^2 ||Y_x(tau_j)||^2)
 <= C^2 L^(-2).                                             (CPM-Q)
```

Thus `CPM-ORTH` is one finite positive quadratic Rayleigh certificate.

## 1. Diagnostic

The companion script:

```text
E72_153_cpm_quadratic_certificate_probe.py
```

reports:

```text
max Q_CPM,
L^2 max Q_CPM,
max||MY||,
max||Y||,
||M||.
```

Representative output:

```text
E72.153 CPM quadratic certificate probe
 lam   L roots  maxQ  L^2maxQ  max||MY||  max||Y||  ||M||
   6  3.58     3 9.089e-03 1.167e-01 1.872e+00 3.830e+01  0.529
   8  4.16     4 2.963e-03 5.126e-02 1.827e+00 5.914e+01  0.621
  10  4.61     3 4.560e-03 9.670e-02 2.688e+00 8.708e+01  0.524
  12  4.97     4 7.869e-04 1.944e-02 1.949e+00 1.227e+02  0.641
  14  5.28     4 8.313e-04 2.316e-02 2.224e+00 1.378e+02  0.593
  16  5.55     5 9.025e-04 2.775e-02 3.071e+00 1.899e+02  0.591
  18  5.78     5 1.086e-04 3.627e-03 2.147e+00 2.340e+02  0.922
```

The scaled quantity `L^2Q_CPM` is far below `1` in the tested windows.

## 2. Consequence

Replacing `CPM-ORTH` by `(CPM-Q)`, the refined route is:

```text
GCOER + PSD-DIST + B-scale + Y-scale + OPM + CPM-Q + ROP + CGE-K
=> scalar WRL.
```

This keeps the source cancellation finite and positive, avoiding componentwise or absolute
prime-sum estimates.

## 3. Status

```text
proved: CPM-Q is equivalent to CPM-ORTH;
open:   prove CPM-Q uniformly for finite CCM roots.
```

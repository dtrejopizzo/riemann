# E72.149 -- MSB scale split

**Date:** 2026-07-09.
**Role:** split the mass-source bound into separate finite scale estimates.

## 0. MSB

The mass-source bound in E72.146 is:

```text
sup_{tau_j<=T} ||b_H||||c_H^{pm}(tau_j)|| = O(1).             (MSB)
```

where:

```text
b_H=B_x^*W_H^T1_H,
c_H^{pm}(tau_j)=B_x^*P_HZ_x^{pm}(tau_j).
```

The expected split is:

```text
||b_H|| = O(sqrt(L)),
sup ||c_H^{pm}(tau_j)|| = O(1/sqrt(L)).
```

Together these imply `(MSB)`.

## 1. Diagnostic

The companion script:

```text
E72_149_msb_scale_probe.py
```

reports:

```text
||b_H||,
||b_H||/sqrt(L),
sup ||c_H^{pm}||,
sqrt(L)sup||c_H^{pm}||,
L sup||c_H^{pm}||,
product.
```

Representative output:

```text
E72.149 MSB scale probe
 lam   L roots  ||b||  b/sqrtL  max||cpm||  cpm*sqrtL  cpm*L  product
   6  3.58     3  2.453    1.296  1.741e-01  3.295e-01 6.238e-01 4.269e-01
   8  4.16     4  3.184    1.561  1.098e-01  2.240e-01 4.568e-01 3.498e-01
  10  4.61     3  2.861    1.333  1.167e-01  2.505e-01 5.376e-01 3.340e-01
  12  4.97     4  3.601    1.615  6.535e-02  1.457e-01 3.248e-01 2.353e-01
  14  5.28     4  3.410    1.484  6.020e-02  1.383e-01 3.178e-01 2.053e-01
  16  5.55     5  3.735    1.586  6.922e-02  1.630e-01 3.838e-01 2.585e-01
  18  5.78     5  3.774    1.570  4.127e-02  9.923e-02 2.386e-01 1.558e-01
```

The data support the split:

```text
||b_H|| = O(sqrt(L)),
sup ||c_H^{pm}(tau_j)|| = O(1/sqrt(L)).
```

The second estimate appears stronger in these windows.

## 2. Status

```text
reduced: MSB to B-scale plus CPM-scale;
observed: both scale estimates hold in the finite harness.
```

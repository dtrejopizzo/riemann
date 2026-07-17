# E72.150 -- CPM factor split

**Date:** 2026-07-09.
**Role:** reduce the post-main source scale in `MSB` to an operator factor bound.

## 0. Source vector

The source factor in E72.149 is:

```text
c_H^{pm}(tau_j)=B_x^*P_HZ_x^{pm}(tau_j).
```

Using the packet representation:

```text
Z_x^{pm}(tau_j) = (2/(L sqrt(x))) LK_x Y_x(tau_j),
```

we get:

```text
c_H^{pm}(tau_j)
 = (2/(L sqrt(x))) B_x^*P_HLK_xY_x(tau_j).
```

Thus:

```text
||c_H^{pm}(tau_j)||
 <= (2/(L sqrt(x))) ||B_x^*P_HLK_x|| ||Y_x(tau_j)||.
```

If:

```text
||Y_x(tau_j)|| = O(sqrt(x)L),
||B_x^*P_HLK_x|| = O(L^(-1/2)),
```

then:

```text
||c_H^{pm}(tau_j)||=O(L^(-1/2)).
```

This is exactly the `CPM-scale` needed for `MSB`.

## 1. Diagnostic

The companion script:

```text
E72_150_cpm_factor_probe.py
```

reports:

```text
||Y||/(sqrt(x)L),
||B^*P_HLK||,
(2/(Lsqrt(x)))||B^*P_HLK||sqrt(x)L,
max||cpm||.
```

Representative output:

```text
E72.150 cpm factor probe
 lam   L roots  max||Y||/(sqrtxL)  ||BPHLK||  factor*op*sqrtxL  max||cpm||
   6  3.58     3          1.781e+00  5.292e-01         1.058e+00   1.741e-01
   8  4.16     4          1.778e+00  6.205e-01         1.241e+00   1.098e-01
  10  4.61     3          1.891e+00  5.241e-01         1.048e+00   1.167e-01
  12  4.97     4          2.058e+00  6.412e-01         1.282e+00   6.535e-02
  14  5.28     4          1.865e+00  5.927e-01         1.185e+00   6.020e-02
  16  5.55     5          2.141e+00  5.910e-01         1.182e+00   6.922e-02
  18  5.78     5          2.249e+00  9.218e-01         1.844e+00   4.127e-02
```

The operator norm does not decay like `L^(-1/2)`.  Therefore `CPM-scale` is not a raw operator-norm
bound; it is an alignment/cancellation statement for `Y_x(tau_j)` under `B^*P_HLK`.

## 2. Status

```text
rejected: CPM-scale from operator norm decay;
kept:     CPM-scale must be proved as a packet alignment/cancellation estimate.
```

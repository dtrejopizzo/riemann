# E73.037 results - Hermite kernel bound

## 1. Purpose

E73.037 proves an explicit Taylor-Cauchy bound for the confluent Hermite kernel:

```text
||h_A(k)||_Herm <= G_theta,m(a,k).
```

The probe compares this scalar bound with the exact finite confluent solve.

## 2. Representative output

```text
E73.037 Hermite kernel bound probe
Compares exact confluent Hermite norm with explicit Taylor-Cauchy bound.
 sigma      tau   gamma   m theta       actual        bound      ratio
  0.05   14.135  14.135   1  0.50    1.000e+00    2.000e+00  2.000e+00
  0.05   14.135  14.135   2  0.50    1.050e+00    2.207e+00  2.102e+00
  0.05   14.135  14.135   3  0.50    1.051e+00    2.219e+00  2.110e+00
  0.05   14.135  21.022   2  0.50    5.415e+00    2.005e+01  3.703e+00
  0.05   14.135  21.022   3  0.50    1.952e+01    1.329e+02  6.808e+00
  0.20   14.135  14.135   3  0.50    1.220e+00    3.012e+00  2.468e+00
  0.20   21.022  21.022   3  0.50    1.220e+00    2.995e+00  2.455e+00
```

The full table is reproduced by:

```text
python3 03-research/phase-73-cauchy-projection/E73_037_hermite_kernel_bound_probe.py
```

## 3. Diagnosis

The bound is rigorous and usable for the low Hermite multiplicities that occur in the natural-height
cluster tests:

```text
m=1:  factor 2;
m=2:  typically factor 2--4;
m=3:  typically factor 2--8.
```

For larger artificial multiplicities the Cauchy bound becomes loose, but E73.026/E73.029 already
showed that the actual confluent object remains stable.  The analytic closure should therefore keep
natural-height multiplicity explicit instead of replacing it by a very high uniform worst case.

## 4. Consequence

The remaining positive factor budget can be written without any hidden Cauchy inverse:

```text
e^(alpha L) sum_k
G_theta,m(a,k)
|1-exp(i gamma_k L)| |C_x(i gamma_k)|
<= L^B.
```

This cleanly separates:

```text
geometry:     G_theta,m(a,k);
mesh:         |1-exp(i gamma_k L)|;
finite roots: |C_x(i gamma_k)|.
```

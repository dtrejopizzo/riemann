# E73.167 results - cauchy0 quotient identity

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_167_cauchy0_intersection_probe.py
```

Output:

```text
E73.167 cauchy0/image intersection probe
C is the 5D cauchy0 coefficient subspace; M is Image(B_principal).
 lam     L rankM rankC angleInt quotient imageRel  C_to_M  M_to_C  angles
   8   4.159     5     5        2        3  4.0e-06 7.75e-01 7.75e-01 1.00e+00,9.99e-01,3.71e-07,1.58e-08,5.29e-12
  10   4.605     5     5        2        3  1.9e-07 7.76e-01 7.76e-01 1.00e+00,9.96e-01,5.63e-06,6.85e-09,3.59e-10
  12   4.970     5     5        2        3  1.8e-06 7.75e-01 7.75e-01 1.00e+00,9.99e-01,8.77e-07,3.56e-08,9.38e-11
  14   5.278     5     5        2        3  9.5e-06 7.75e-01 7.75e-01 1.00e+00,9.97e-01,6.78e-06,2.55e-09,5.31e-10
  16   5.545     6     5        2        3  1.8e-04 7.75e-01 8.17e-01 1.00e+00,1.00e+00,1.98e-06,1.85e-08,1.71e-09
  20   5.991     4     5        0        5  5.2e-02 9.67e-01 9.59e-01 5.60e-01,8.32e-02,1.53e-06,5.58e-10
  24   6.356     5     5        0        5  2.6e-01 8.92e-01 8.92e-01 9.86e-01,2.17e-01,3.83e-06,5.36e-09,1.45e-09
  32   6.931     6     5        0        5  3.3e-02 8.98e-01 9.16e-01 9.81e-01,5.40e-02,7.15e-08,5.50e-09,2.13e-10
```

Reading:

```text
1. In trusted rows with imageRel <= 1e-3, the principal angle test gives:

   dim(C cap M)=2,
   dim C/(C cap M)=3.

2. This explains the rank-three transfer projector from E73.165.

3. Rows with imageRel >= 3e-2 are not reliable for the coefficient-intersection
   interpretation; symbolic partial fractions or better conditioning are
   needed there.
```

Conclusion:

```text
The cauchy0 obstruction is a three-dimensional quotient of the five critical
atoms by a two-dimensional generated intersection.
```


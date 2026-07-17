# E73.168 results - quotient dual audit

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_168_quotient_dual_probe.py
```

Output:

```text
E73.168 quotient dual probe
Measures the dual cancelled-Cauchy vector G_K after quotient projection P_Q,L.
 lam     L inter imageRel  |PQG|/|G|  |PIG| rows: scalarRatio maxPiQ
   8   4.159     2  4.0e-06  8.54e-01  3.44e-09 2.89e+00/9.73e-01/9.15e-01 6.37e-01
  10   4.605     2  1.9e-07  9.73e-01  6.92e-10 2.33e+00/8.93e-01/9.01e-01 3.92e-01
  12   4.970     2  1.8e-06  9.95e-01  1.42e-09 8.01e+00/7.60e-01/1.19e+00 6.46e-01
  14   5.278     2  9.5e-06  9.06e-01  1.28e-08 1.50e+01/1.84e-01/4.16e-01 4.70e-01
  16   5.545     2  1.8e-04  9.80e-01  1.00e-08 1.79e+00/9.95e-01/1.02e+00 6.60e-01
  20   5.991     0  5.2e-02  1.00e+00  3.42e-09 1.00e+00/1.00e+00/1.00e+00 1.00e+00
  24   6.356     0  2.6e-01  1.00e+00  8.22e-11 1.00e+00/1.00e+00/1.00e+00 1.00e+00
  32   6.931     0  3.3e-02  1.00e+00  5.22e-15 1.00e+00/1.00e+00/1.00e+00 1.00e+00
```

Reading:

```text
1. In trusted rows, P_Q G_K is not small:
   ||P_QG||/||G|| = 0.85--1.00.

2. The scalar after quotient projection is usually order one relative to the
   original scalar and can be larger when the original has cancellation.

3. Therefore the quotient is not a dual-orthogonality closure.
```

Conclusion:

```text
The remaining problem is the three-dimensional quotient pairing, not separate
smallness of either quotient factor.
```


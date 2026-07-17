# E73.164 results - canonical cauchy0 delta audit

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_164_cauchy0_delta_probe.py
```

Output:

```text
E73.164 cauchy0 delta probe
Compares canonical cauchy0 defect delta against original Pi source coefficients.
 lam     L   dim      bRe  ||d||/||Pi|| cos(d,Pi) maxRatio      expPi   expDelta scalarRatio
   8   4.159    25    0.200    9.810e-02     0.098 5.612e-02  2.642e-10  3.188e-10   1.206e+00
   8   4.159    25    0.200    5.884e-01     0.588 6.055e-01  3.913e-12  3.692e-12   9.436e-01
   8   4.159    25    0.200    6.246e-01     0.625 7.312e-01  8.963e-09  8.501e-09   9.484e-01
  10   4.605    29    0.200    2.073e-01     0.207 1.543e-01  2.773e-11  1.066e-10   3.843e+00
  10   4.605    29    0.200    6.133e-01     0.613 5.596e-01  4.394e-13  4.196e-13   9.550e-01
  10   4.605    29    0.200    2.918e-01     0.292 3.793e-01  8.725e-10  7.462e-10   8.552e-01
  12   4.970    33    0.200    1.998e-01     0.200 1.187e-01  2.783e-11  2.396e-10   8.608e+00
  12   4.970    33    0.200    7.479e-01     0.748 7.254e-01  3.284e-13  3.703e-13   1.128e+00
  12   4.970    33    0.200    5.975e-01     0.598 6.793e-01  1.152e-09  1.149e-09   9.969e-01
  14   5.278    37    0.200    4.754e-01     0.475 3.590e-01  6.283e-10  9.506e-09   1.513e+01
  14   5.278    37    0.200    6.470e-01     0.647 6.026e-01  1.013e-11  6.900e-12   6.808e-01
  14   5.278    37    0.200    5.896e-01     0.590 7.706e-01  1.885e-08  4.700e-09   2.493e-01
  16   5.545    41    0.200    1.301e-01     0.130 8.597e-02  8.150e-10  3.050e-09   3.743e+00
  16   5.545    41    0.200    7.104e-01     0.710 6.971e-01  1.241e-11  1.265e-11   1.019e+00
  16   5.545    41    0.200    6.642e-01     0.664 7.661e-01  2.678e-08  2.718e-08   1.015e+00
  20   5.991    49    0.200    7.452e-02     0.075 5.516e-02  2.328e-10  3.857e-11   1.657e-01
  20   5.991    49    0.200    5.257e-01     0.526 5.885e-01  3.272e-12  3.203e-12   9.791e-01
  20   5.991    49    0.200    7.245e-01     0.725 8.315e-01  8.329e-09  8.050e-09   9.666e-01
  24   6.356    57    0.200    2.090e-01     0.211 1.626e-01  6.974e-12  6.180e-11   8.862e+00
  24   6.356    57    0.200    5.886e-01     0.591 4.808e-01  1.071e-13  7.900e-14   7.376e-01
  24   6.356    57    0.200    5.350e-01     0.537 7.560e-01  2.268e-10  6.665e-11   2.939e-01
```

Reading:

```text
1. delta is not equal to Pi, but it is not negligible.  Norm ratios are often
   0.5--0.75 on two of the three diagnostic rows.

2. delta is often aligned with a large component of Pi; the cosine is of the
   same order as the norm ratio.

3. The scalar contribution after replacing Pi by delta is not uniformly
   smaller.  `scalarRatio` is often order one and sometimes much larger.

4. Therefore the canonical coefficient elimination does not provide a new
   scalar bound by itself.
```

Conclusion:

```text
The remaining endpoint is CANON-CRIT-DIV: prove the scalar smallness of the
canonical cauchy0 defect directly.
```


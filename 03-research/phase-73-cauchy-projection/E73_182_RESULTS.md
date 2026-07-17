# E73.182 results - closed-series archimedean certificate

Command:

```text
python3 E73_182_closed_series_arch_probe.py
```

Output:

```text
E73.182 closed-series archimedean probe
Compares arch matrix, quadrature, and closed exponential-series evaluation.
 lam     L gamma row modes   matB quadErr seriesErr seriesQuadErr
  12   4.970   14.13   0    66  -1.51 1.6e-14   3.2e-10       3.2e-10
  12   4.970   14.13   1    66  -2.11 4.8e-14   1.0e-09       1.0e-09
  12   4.970   21.02   0    66  -1.88 1.1e-14   3.8e-10       3.8e-10
  12   4.970   21.02   1    66  -2.72 3.1e-14   2.1e-09       2.1e-09
  16   5.545   14.13   0    82  -4.02 1.1e-12   2.3e-09       2.3e-09
  16   5.545   14.13   1    82  -0.88 2.9e-15   2.6e-10       2.6e-10
  16   5.545   21.02   0    82  -1.91 1.4e-14   2.1e-10       2.1e-10
  16   5.545   21.02   1    82  -0.97 4.1e-15   4.0e-10       4.0e-10
  20   5.991   14.13   0    98  -1.52 1.8e-13   7.1e-10       7.1e-10
  20   5.991   14.13   1    98  -2.05 4.8e-13   1.9e-09       1.9e-09
  20   5.991   21.02   0    98  -0.74 2.3e-14   4.7e-10       4.7e-10
  20   5.991   21.02   1    98  -0.92 3.5e-14   7.7e-10       7.7e-10
  24   6.356   14.13   0   114  -1.28 2.6e-13   1.5e-09       1.5e-09
  24   6.356   14.13   1   114  -0.91 9.5e-15   5.8e-10       5.8e-10
  24   6.356   21.02   0   114  -1.23 6.4e-14   1.9e-09       1.9e-09
  24   6.356   21.02   1   114  -0.98 2.9e-14   9.3e-10       9.3e-10
```

The script compares:

```text
mat:       q_j H_model xi_L,
quad:      direct adaptive quadrature,
series:    finite exponential primitives plus truncated WR series.
```

The intended pass condition is:

```text
seriesErr comparable to quadErr or smaller,
seriesQuadErr near the expected WR-series truncation/numerical floor.
```

Reading:

```text
The closed series is stable at about 1e-9 relative error with R=120 and
two Taylor tail accelerants.  This is much better structurally than adaptive
quadrature for proof purposes, but not yet enough to certify residuals at
the L^-17 level by subtraction alone.
```

The next certificate step is the explicit third-derivative tail bound, or a
higher-order Taylor accelerant, both of which are mechanical from the finite
mode expansion.

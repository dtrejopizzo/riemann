# E73.298 results

Command:

```text
python3 E73_298_curvature_rank_audit_probe.py
```

Output after the neutral-ramp correction:

```text
E73.298 balanced curvature rank audit
Rows are q_a (Q_y''+alpha_L(y)J) R_w sampled over y.
This tests only a shortcut; failure means CURV-ABEL remains full-kernel signed.
 lam     L gamma row n samp r90 r99 r999 tail4 tail8 scalarProj4 scalarProj8 rowNormRatio
  12   4.970   14.13   0  33   96   4  10   17 8.81e-02 1.39e-02    2.28e-01    1.96e-01    5.82e-01
  12   4.970   14.13   1  33   96   4  10   17 8.81e-02 1.39e-02    3.91e-01    2.00e-01    5.82e-01
  12   4.970   21.02   0  33   96   3  10   18 5.10e-02 1.52e-02    3.01e-01    2.63e-01    5.67e-01
  12   4.970   21.02   1  33   96   3  10   18 5.10e-02 1.52e-02    9.69e-01    9.21e-01    5.67e-01
  16   5.545   14.13   0  41   96   7  11   22 1.69e-01 5.13e-02    2.28e-01    1.31e-01    6.10e-01
  16   5.545   14.13   1  41   96   7  11   22 1.69e-01 5.13e-02    6.45e-01    4.44e-01    6.10e-01
  16   5.545   21.02   0  41   96   3   6   14 1.91e-02 2.87e-03    4.02e-01    1.34e-01    5.82e-01
  16   5.545   21.02   1  41   96   3   6   14 1.91e-02 2.87e-03    5.98e-01    3.94e-01    5.82e-01
  20   5.991   14.13   0  49   96   9  14   27 2.04e-01 1.01e-01    1.78e-01    6.23e-02    6.15e-01
  20   5.991   14.13   1  49   96   9  14   27 2.04e-01 1.01e-01    2.22e-01    9.04e-02    6.15e-01
  20   5.991   21.02   0  49   96   4   8   13 7.60e-02 8.37e-03    8.02e-01    7.49e-01    5.66e-01
  20   5.991   21.02   1  49   96   4   8   13 7.60e-02 8.37e-03    8.24e-01    7.63e-01    5.66e-01
```


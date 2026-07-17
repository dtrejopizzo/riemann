# E73.019 results - source image certificate

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_019_source_image_certificate_probe.py
```

Output:

```text
E73.019 source image certificate probe
Tests S_b in Image((C_E-mu)P_{O,K}).
 lam     L   dim  imgRank  imgCond       bRe       |S|      relRes    expPair
   8   4.159    25        7  7.7e+08     0.200  8.20e+00   1.45e-06   2.70e-10
   8   4.159    25        7  7.7e+08     0.200  2.26e-03   5.00e-05   4.00e-12
   8   4.159    25        7  7.7e+08     0.200  4.90e+00   2.36e-04   9.19e-09
  10   4.605    29        8  3.6e+09     0.200  9.11e+00   2.15e-06   2.96e-10
  10   4.605    29        8  3.6e+09     0.200  2.52e-03   1.25e-04   4.69e-12
  10   4.605    29        8  3.6e+09     0.200  5.83e+00   9.12e-05   9.35e-09
  12   4.970    33        8  1.9e+09     0.200  9.91e+00   2.91e-06   7.98e-12
  12   4.970    33        8  1.9e+09     0.200  2.70e-03   1.47e-04   2.26e-13
  12   4.970    33        8  1.9e+09     0.200  6.65e+00   1.66e-04   1.14e-10
  14   5.278    37        8  6.3e+08     0.200  1.05e+01   2.78e-06   2.60e-10
  14   5.278    37        8  6.3e+08     0.200  2.84e-03   1.23e-04   4.40e-12
  14   5.278    37        8  6.3e+08     0.200  8.37e+00   1.75e-04   7.12e-09
  16   5.545    41        9  2.0e+09     0.200  1.10e+01   5.13e-06   6.55e-10
  16   5.545    41        9  2.0e+09     0.200  2.99e-03   2.54e-04   1.01e-11
  16   5.545    41        9  2.0e+09     0.200  8.59e+00   2.53e-04   2.12e-08
```

Reading:

```text
S_b in Image((C_E-mu)P_{O,K})
```

holds numerically in the SVD-truncated effective image with `1e-6..2.6e-4` relative residual on
the tested windows.  More importantly for the Schur gate, the exponentially weighted residual
pairing with the ground vector is already `<=2.2e-8` in the tested range.

This is the first direct finite certificate for the load-bearing equation:

```text
S_b = (C_E-mu I)Y_b + R_b,
e^(Re b L)|<xi,R_b>| small.
```

It is stronger than checking that `(C_E-mu)P` lands in the finite source class: it checks that the
specific Cauchy-Schur source vector lies in that image.

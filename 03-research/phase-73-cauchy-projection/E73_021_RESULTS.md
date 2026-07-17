# E73.021 results - dual residual split

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_021_dual_residual_split_probe.py
```

Output:

```text
E73.021 dual residual split probe
Residual after Image((C_E-mu)P) projection split into xi and xi-orthogonal parts.
 lam     L   dim rank  eigDef      |res|/|S|    xiShare     expXi    orthShare  cokerDim
   8   4.159    25    7  4.6e-17     1.45e-06   9.89e-06   2.70e-10    1.00e+00        18
   8   4.159    25    7  4.6e-17     5.00e-05   1.54e-05   4.00e-12    1.00e+00        18
   8   4.159    25    7  4.6e-17     2.36e-04   3.46e-06   9.19e-09    1.00e+00        18
  10   4.605    29    8  2.3e-16     2.15e-06   6.01e-06   2.96e-10    1.00e+00        21
  10   4.605    29    8  2.3e-16     1.25e-04   5.92e-06   4.69e-12    1.00e+00        21
  10   4.605    29    8  2.3e-16     9.12e-05   7.00e-06   9.35e-09    1.00e+00        21
  12   4.970    33    8  1.8e-15     2.91e-06   1.02e-07   7.98e-12    1.00e+00        25
  12   4.970    33    8  1.8e-15     1.47e-04   2.10e-07   2.26e-13    1.00e+00        25
  12   4.970    33    8  1.8e-15     1.66e-04   3.82e-08   1.14e-10    1.00e+00        25
  14   5.278    37    8  5.4e-15     2.78e-06   3.09e-06   2.60e-10    1.00e+00        29
  14   5.278    37    8  5.4e-15     1.23e-04   4.39e-06   4.40e-12    1.00e+00        29
  14   5.278    37    8  5.4e-15     1.75e-04   1.69e-06   7.12e-09    1.00e+00        29
  16   5.545    41    9  6.6e-15     5.13e-06   3.82e-06   6.55e-10    1.00e+00        32
  16   5.545    41    9  6.6e-15     2.54e-04   4.37e-06   1.01e-11    1.00e+00        32
  16   5.545    41    9  6.6e-15     2.53e-04   3.22e-06   2.12e-08    1.00e+00        32
  18   5.781    45    9  3.6e-15     5.16e-06   2.47e-06   4.68e-10    1.00e+00        36
  18   5.781    45    9  3.6e-15     3.15e-04   2.09e-06   6.61e-12    1.00e+00        36
  18   5.781    45    9  3.6e-15     2.18e-04   2.69e-06   1.66e-08    1.00e+00        36
```

Reading:

```text
The residual outside Image((C_E-mu)P) is almost entirely xi-orthogonal.
```

The full residual norm is not zero, but its `xi` share is only `1e-7..1e-5`.  The rest lives in
the large cokernel of the restricted image and does not enter scalar WRL.

Thus the correct finite target is not:

```text
||P_I^perp S_b|| small.
```

It is:

```text
|<xi,P_I^perp S_b>| small.
```

This matches E73.020 exactly.

# E73.185 results - grouped-frequency WR tail

Command:

```text
python3 E73_185_grouped_frequency_tail_probe.py
```

Output:

```text
E73.185 grouped-frequency WR tail probe
Compares binomial absolute derivative bound with direct frequency-grouped bound.
 lam     L gamma row K actualB oldB newB gainB ratioNewB
  12   4.970   14.13   0  4   -15.79  -7.04  -7.17   0.13      -8.62
  12   4.970   14.13   0  6   -17.92 -10.10 -10.27   0.17      -7.64
  12   4.970   14.13   0  8   -21.62 -13.08 -13.29   0.22      -8.32
  12   4.970   14.13   0 10   -21.31 -16.00 -16.26   0.26      -5.04
  16   5.545   14.13   0  4   -15.67  -5.44  -5.55   0.11     -10.12
  16   5.545   14.13   0  6   -17.35  -8.31  -8.46   0.15      -8.89
  16   5.545   14.13   0  8   -19.42 -11.08 -11.27   0.18      -8.16
  16   5.545   14.13   0 10   -19.68 -13.79 -14.00   0.21      -5.69
  20   5.991   14.13   0  4   -13.78  -5.43  -5.54   0.11      -8.24
  20   5.991   14.13   0  6   -15.94  -8.22  -8.36   0.14      -7.58
  20   5.991   14.13   0  8   -18.53 -10.89 -11.06   0.17      -7.46
  20   5.991   14.13   0 10   -20.94 -13.45 -13.64   0.19      -7.29
  24   6.356   14.13   0  4   -12.50  -4.90  -5.00   0.10      -7.50
  24   6.356   14.13   0  6   -14.02  -7.43  -7.55   0.12      -6.47
  24   6.356   14.13   0  8   -16.66  -9.79  -9.93   0.14      -6.73
  24   6.356   14.13   0 10   -18.36 -12.03 -12.19   0.16      -6.17
  32   6.931   14.13   0  4   -12.52  -4.33  -4.39   0.07      -8.12
  32   6.931   14.13   0  6   -13.83  -6.52  -6.61   0.09      -7.22
  32   6.931   14.13   0  8   -15.86  -8.56  -8.66   0.10      -7.20
  32   6.931   14.13   0 10   -17.05 -10.51 -10.62   0.11      -6.43
```

Reading:

```text
gainB = log_L(old/new) measures improvement over E73.184.
ratioNewB <= 0 means the grouped bound still covers the observed tail.
```

Representative rows are shown.  The full script checks both Cauchy rows and
the first two critical heights for `lambda=12,16,20,24,32`.

Observed:

```text
gainB is positive but small, about 0.07--0.26 powers of L;
ratioNewB remains safely negative;
increasing K improves actualTailB much more than it improves the rigorous
coefficient-absolute bound.
```

Conclusion: grouping constant and linear terms at each frequency is valid,
but the dominant loss is now the absolute derivative envelope itself.  The
next useful theorem should target the signed model-prime principal residual,
not further local WR tail engineering.

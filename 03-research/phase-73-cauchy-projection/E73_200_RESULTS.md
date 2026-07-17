# E73.200 results - arch/prime split diagnostic

Command:

```text
python3 E73_200_arch_prime_split_probe.py
```

Output:

```text
E73.200 arch/prime split diagnostic
Compares each certificate side before final cancellation.
 lam     L gamma row archM archD archE primeM primeF primeE finalE
  12   4.970   14.13   0  -1.51  -1.51 -21.99   -1.51   -1.51  -21.59  -21.78  accelE=-20.73
  12   4.970   14.13   1  -2.11  -2.11 -22.46   -2.11   -2.11  -21.26  -21.36  accelE=-20.71
  12   4.970   21.02   0  -1.88  -1.88 -22.23   -1.88   -1.88  -22.66  -21.99  accelE=-20.91
  12   4.970   21.02   1  -2.72  -2.72 -22.78   -2.72   -2.72  -22.87  -22.35  accelE=-20.95
  16   5.545   14.13   0  -4.02  -4.02 -20.84   -4.02   -4.02  -19.03  -19.00  accelE=-19.45
  16   5.545   14.13   1  -0.88  -0.88 -19.70   -0.88   -0.88  -20.43  -19.59  accelE=-19.16
  16   5.545   21.02   0  -1.91  -1.91 -20.08   -1.91   -1.91  -20.91  -19.98  accelE=-19.41
  16   5.545   21.02   1  -0.97  -0.97 -20.48   -0.97   -0.97  -20.86  -20.24  accelE=-19.12
  20   5.991   14.13   0  -1.52  -1.52 -18.26   -1.52   -1.52  -18.06  -18.78  accelE=-18.23
  20   5.991   14.13   1  -2.05  -2.05 -18.13   -2.05   -2.05  -18.12  -20.79  accelE=-18.14
  20   5.991   21.02   0  -0.74  -0.74 -19.23   -0.74   -0.74  -17.93  -17.87  accelE=-18.10
  20   5.991   21.02   1  -0.92  -0.92 -19.38   -0.92   -0.92  -17.65  -17.62  accelE=-17.97
```


Reading:

```text
Both sides before cancellation are large compared with the final residual:
archM and primeM are typically between L^-1 and L^-4, while finalE is around
L^-18--L^-22.  The digamma archimedean formula and the prime frequency formula
match their matrix sides separately to roughly the same absolute floor as the
final discrepancy.

Therefore the E73.199 relative errors are not evidence of a wrong tail formula.
They measure a 17--20 power cancellation assembled in floating arithmetic.
The proof-facing route must evaluate the finite sums with high-precision ball
or interval arithmetic and cannot use double matrix residuals as final truth.
```

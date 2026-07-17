# E73.210 results - psi asymptotic enclosure budget

Command:

```text
python3 E73_210_psi_asymptotic_budget.py
```

Output:

```text
E73.210 psi asymptotic budget
Conservative Bernoulli next-term audit for D1/D2 entry radii.
 lam     L    N  dim    K   maxRadB  targetB  slack
   8   4.159    6   13    8    -49.32   -56.26  5.07e-05
   8   4.159    6   13   12    -67.62   -56.26  1.08e+07
   8   4.159    6   13   16    -83.97   -56.26  1.42e+17
   8   4.159    6   13   20    -98.88   -56.26  2.41e+26
   8   4.159    6   13   24   -112.65   -56.26  7.99e+34
   8   4.159    6   13   28   -125.46   -56.26  6.83e+42
   8   4.159    6   13   32   -137.46   -56.26  1.84e+50
  10   4.605    8   17    8    -46.03   -51.93  1.22e-04
  10   4.605    8   17   12    -63.11   -51.93  2.60e+07
  10   4.605    8   17   16    -78.37   -51.93  3.43e+17
  10   4.605    8   17   20    -92.28   -51.93  5.82e+26
  10   4.605    8   17   24   -105.13   -51.93  1.93e+35
  10   4.605    8   17   28   -117.09   -51.93  1.65e+43
  10   4.605    8   17   32   -128.29   -51.93  4.44e+50
  12   4.970   10   21    8    -43.84   -48.94  2.82e-04
  12   4.970   10   21   12    -60.11   -48.94  6.01e+07
  12   4.970   10   21   16    -74.65   -48.94  7.94e+17
  12   4.970   10   21   20    -87.90   -48.94  1.35e+27
  12   4.970   10   21   24   -100.14   -48.94  4.46e+35
  12   4.970   10   21   28   -111.53   -48.94  3.82e+43
  12   4.970   10   21   32   -122.20   -48.94  1.03e+51
```


Reading:

```text
The special-function enclosure is not the bottleneck.  With K=12 Bernoulli
terms, the conservative D1/D2 radius is already about 10^7 times smaller than
the per-entry target in all tested windows.  Larger K gives overwhelming slack.

Thus the remaining entry-radius work is elementary: outward rounding for finite
exponentials/rational operations, the finite WR head, and the finite prime sum.
The non-elementary psi/psi_1 tail can be certified within budget by a short
asymptotic expansion.
```

# E73.170 results - quotient budget

Date: 2026-07-14.

Script:

```text
E73_170_quotient_budget_probe.py
```

## Output

```text
E73.170 quotient budget probe
Measures QUOT-NORM versus exact QUOT-PAIR on the quotient.
 lam     L inter imageRel row  piQB  gQB normB pairB lossB pairVal normVal
   8   4.159     2  4.0e-06   0  -1.14 -13.67 -14.23 -15.15   0.92  4.20e-10  1.55e-09
   8   4.159     2  4.0e-06   1  -5.42 -13.67 -18.51 -18.60   0.09  3.09e-12  3.50e-12
   8   4.159     2  4.0e-06   2   0.20 -13.67 -12.89 -13.29   0.40  5.94e-09  1.05e-08
  10   4.605     2  1.9e-07   0  -0.58 -13.81 -13.78 -15.41   1.63  6.02e-11  7.22e-10
  10   4.605     2  1.9e-07   1  -5.03 -13.81 -18.24 -18.79   0.55  3.46e-13  8.02e-13
  10   4.605     2  1.9e-07   2  -0.31 -13.81 -13.52 -13.81   0.29  6.97e-10  1.08e-09
  12   4.970     2  1.8e-06   0  -0.57 -12.71 -12.66 -13.98   1.32  1.84e-10  1.53e-09
  12   4.970     2  1.8e-06   1  -4.67 -12.71 -16.75 -17.95   1.20  3.15e-13  2.16e-12
  12   4.970     2  1.8e-06   2   0.15 -12.71 -11.93 -12.93   0.99  9.94e-10  4.89e-09
  14   5.278     2  9.5e-06   0  -0.03 -10.92 -10.32 -11.06   0.74  1.03e-08  3.51e-08
  14   5.278     2  9.5e-06   1  -4.59 -10.92 -14.87 -15.51   0.63  6.25e-12  1.80e-11
  14   5.278     2  9.5e-06   2   0.14 -10.92 -10.15 -11.23   1.08  7.64e-09  4.64e-08
  16   5.545     2  1.8e-04   0  -0.79 -10.75 -10.89 -11.60   0.71  2.33e-09  7.92e-09
  16   5.545     2  1.8e-04   1  -4.40 -10.75 -14.50 -14.65   0.15  1.26e-11  1.63e-11
  16   5.545     2  1.8e-04   2   0.20 -10.75  -9.90 -10.26   0.36  2.35e-08  4.31e-08
  20   5.991     0  5.2e-02   0   0.39 -10.89  -9.83 -12.39   2.56  2.33e-10  2.27e-08
  20   5.991     0  5.2e-02   1  -4.02 -10.89 -14.24 -14.77   0.53  3.27e-12  8.52e-12
  20   5.991     0  5.2e-02   2   0.42 -10.89  -9.80 -10.39   0.59  8.33e-09  2.42e-08
  24   6.356     0  2.6e-01   0   0.38 -12.56 -11.49 -13.89   2.40  6.97e-12  5.87e-10
  24   6.356     0  2.6e-01   1  -3.89 -12.56 -15.76 -16.15   0.39  1.07e-13  2.21e-13
  24   6.356     0  2.6e-01   2   0.41 -12.56 -11.46 -12.01   0.55  2.27e-10  6.26e-10
  32   6.931     0  3.3e-02   0   0.36 -16.99 -15.91 -16.49   0.58  1.36e-14  4.18e-14
  32   6.931     0  3.3e-02   1  -3.71 -16.99 -19.98 -21.34   1.35  1.15e-18  1.57e-17
  32   6.931     0  3.3e-02   2   0.39 -16.99 -15.88 -16.43   0.56  1.52e-14  4.46e-14
```

## Reading

The trusted rows are the rows with `imageRel <= 1e-3`, where the
coefficient-image computation from E73.167 is numerically stable.  In those
rows:

```text
lossB = log_L(norm/pair) is about 0.1 to 1.6.
```

Thus replacing the exact quotient pairing by its Cauchy-Schwarz norm budget
does not show exponential loss in the tested range.

The budget separates cleanly:

```text
Pi_Q side: geometric/polynomial size.
G_Q side: spectral Cauchy smallness.
```

The resulting sufficient theorem is:

```text
QUOT-NORM:
e^(alpha L)||P_Q,L Pi_A|| ||P_Q,L G_K|| <= L^B.
```

Equivalently it is enough to prove the two bounds:

```text
QPI: e^(alpha L)||P_Q,L Pi_A|| <= L^B,
QG:  ||P_Q,L G_K|| <= L^B e^(-alpha L).
```

## Status

E73.170 does not prove `QUOT-NORM`.  It replaces the unstable exact pairing
target by a norm target whose measured loss is only polynomial in trusted
windows.  The remaining load-bearing analytic problem is `QG`.

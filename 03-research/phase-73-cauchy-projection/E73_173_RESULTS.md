# E73.173 results - eigenline Cauchy-transform audit

Date: 2026-07-14.

Script:

```text
E73_173_eigenline_cauchy_transform_probe.py
```

## Output

```text
E73.173 eigenline Cauchy-transform probe
Tests whether QG linear forms are controlled by the finite eigenline row equation.
 lam     L imageRel form qgB rowResB preB archB primeB muqB absErrB
   8   4.159  4.0e-06    0 -14.24  -12.52   9.29   -1.74   -1.74 -38.04  -27.44
   8   4.159  4.0e-06    1 -14.07  -12.14  10.00   -1.96   -1.96 -37.87  -27.16
   8   4.159  4.0e-06    2 -13.93  -12.33   9.17   -1.80   -1.80 -37.73  -26.75
  10   4.605  1.9e-07    0 -15.38  -12.71   8.46   -1.69   -1.69 -36.95  -26.32
  10   4.605  1.9e-07    1 -14.45  -11.90   9.42   -1.33   -1.33 -36.02  -24.51
  10   4.605  1.9e-07    2 -13.86  -11.62   9.70   -1.56   -1.56 -35.43  -24.89
  12   4.970  1.8e-06    0 -14.77  -13.00   7.26   -2.89   -2.89 -35.29  -23.20
  12   4.970  1.8e-06    1 -12.81  -10.73   8.90   -4.08   -4.08 -33.33  -23.54
  12   4.970  1.8e-06    2 -13.10  -10.77   7.87   -4.14   -4.14 -33.62  -23.68
  14   5.278  9.5e-06    0 -12.27  -11.42   7.64   -2.64   -2.64 -31.62  -31.62
  14   5.278  9.5e-06    1 -11.29  -10.32   8.35   -1.48   -1.48 -30.63  -22.13
  14   5.278  9.5e-06    2 -11.03  -10.04   8.56   -1.15   -1.15 -30.37  -22.50
  16   5.545  1.8e-04    0 -12.93  -12.13   6.67   -1.02   -1.02 -31.60  -21.37
  16   5.545  1.8e-04    1 -11.92  -11.14   7.79   -0.80   -0.80 -30.59  -21.08
  16   5.545  1.8e-04    2 -10.76   -9.97   8.85   -1.18   -1.18 -29.43  -21.62
```

## Reading

The row-space inverse route is not viable: `preB` is large, typically
between `6` and `10`.  Therefore `QG` should not be proved by solving
backwards through `H_L-mu_L`.

The exact identity

```text
Arch_r(L) - Prime_r(L) = mu_L ell_r(G_L)
```

is verified at the scale permitted by double precision.  The meaningful
diagnostic is the size separation:

```text
archB ~= primeB,
muqB is far smaller.
```

Thus the smallness of `ell_r(G_L)` is an arch/prime matching phenomenon, not
a smallness of either side separately.

## Current endpoint

The active theorem is:

```text
QG-MATCH:
|Arch_r(L)-Prime_r(L)| <= |mu_L| L^B e^(-alpha L),
r=1,2,3.
```

Together with `QPI`, this implies `QUOT-NORM`.

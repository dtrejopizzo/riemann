# E73.231 results - uniform scaling probe

Command:

```text
python3 E73_231_uniform_scaling_probe.py
```

Output:

```text
E73.231 uniform scaling probe
Diagnostic closed scalar wrapper beyond certified windows; rho is extrapolated.
 lam     L    N gamma row centerB RclosedB ratio maxW_B sumCoeffB rhoB
   8   4.159    6   14.13   0  -21.68   -46.32  5.6e-16   -0.43     -1.33 -45.98
  10   4.605    8   14.13   0  -18.50   -42.28  1.7e-16    0.71     -0.30 -43.11
  12   4.970   10   14.13   0  -20.62   -40.44  1.6e-14    0.55     -0.62 -41.26
  14   5.278   12   14.13   0  -18.38   -40.35  1.3e-16    1.53     -0.07 -43.16
  16   5.545   14   14.13   0  -20.52   -42.80  2.7e-17    1.42      0.13 -45.06
  18   5.781   16   14.13   0  -16.56   -42.25  2.7e-20    1.61      2.25 -46.96
```

Interpretation:

This is a diagnostic, not a certificate, because `rho` is extrapolated beyond
the certified Krawczyk windows.  It suggests that the coefficient/weight side
is not the visible uniform bottleneck; the uniform eigenline-radius production
is.

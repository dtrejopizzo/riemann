# E73.195 results - finite-frequency certificate

Command:

```text
python3 E73_195_finite_frequency_certificate_probe.py
```

Output:

```text
E73.195 finite-frequency certificate
Closed frequency evaluation of F[B_bal]=F[B_perp].
 lam     L gamma row modes matrixB closedB absErrB relErr cAbsB
  12   4.970   14.13   0    66  -20.85  -21.96  -20.97 8.3e-01   0.25
  12   4.970   14.13   1    66  -21.09  -22.59  -21.03 1.1e+00   0.25
  12   4.970   21.02   0    66  -20.40  -20.79  -20.87 4.7e-01   0.25
  12   4.970   21.02   1    66  -19.87  -19.77  -20.98 1.7e-01   0.25
  16   5.545   14.13   0    82  -19.19  -18.88  -19.40 6.9e-01  -0.07
  16   5.545   14.13   1    82  -19.98  -19.26  -19.11 4.4e+00  -0.07
  16   5.545   21.02   0    82  -18.18  -18.12  -19.44 1.2e-01  -0.07
  16   5.545   21.02   1    82  -19.03  -20.43  -19.09 9.1e-01  -0.07
  20   5.991   14.13   0    98  -19.09  -18.57  -18.85 1.5e+00   0.52
  20   5.991   14.13   1    98  -18.56  -18.52  -19.98 8.0e-02   0.52
  20   5.991   21.02   0    98  -17.65  -19.18  -17.62 1.1e+00   0.52
  20   5.991   21.02   1    98  -17.76  -17.80  -17.39 1.9e+00   0.52
```

Reading:

```text
The finite-frequency closed evaluation reaches the correct residual scale.
It is much better conditioned than the nested second-Abel quadrature.
Relative agreement is not uniformly small because the target value is itself
at the cancellation floor of the WR series and floating arithmetic.
```

Depth check:

```text
For lam=12, gamma=14.13, row 0:
R=80    abs error scale L^-14.4
R=180   abs error scale L^-15.9
R=400   abs error scale L^-17.4
R=1000  abs error scale L^-19.1
R=2000  abs error scale L^-20.5
R=5000  abs error scale L^-21.9
```

Conclusion:

```text
The certificate format is viable, but the proof implementation must use
rigorous WR tail bounds / interval arithmetic rather than ordinary floating
relative error.
```

Current endpoint:

```text
FF-SECOND-ABEL:
the finite-frequency expression for F_L[B_a^bal] decays rapidly.
```

# E73.263 results - commutator-Schur residual audit

Command:

```text
python3 E73_263_commutator_schur_residual.py
```

## Output

```text
E73.263 commutator-Schur residual audit
rho=qHR=qH-(qHQ*)GQ=-q[H,P]; reports arch/prime split paired with xi.
 lam      L gamma row centerB schurErrB commErrB archB primeB cancelB rhoNormB archNormB primeNormB
   8    4.159  14.13   0   -21.68    -28.42   -28.52   -1.52   -1.52   -21.68    -3.18     -0.05      -0.05
   8    4.159  14.13   1   -21.46    -28.71   -28.34   -1.50   -1.50   -21.46    -3.18     -0.05      -0.05
   8    4.159  21.02   0   -15.76    -28.71   -29.12   -2.18   -2.18   -15.76    -4.54     -0.37      -0.37
   8    4.159  21.02   1   -15.79    -28.87   -29.55   -2.15   -2.15   -15.79    -4.54     -0.37      -0.37
  10    4.605  14.13   0   -18.50    -25.43   -26.12   -0.14   -0.14   -18.50    -2.13      0.18       0.18
  10    4.605  14.13   1   -18.51    -26.28   -27.59   -0.14   -0.14   -18.51    -2.13      0.18       0.18
  10    4.605  21.02   0   -14.98    -26.94   -27.59   -0.42   -0.42   -14.98    -3.16     -0.15      -0.15
  10    4.605  21.02   1   -14.98    -28.33   -27.19   -0.42   -0.42   -14.98    -3.16     -0.15      -0.15
  12    4.970  14.13   0   -20.64    -26.11   -24.18   -1.32   -1.32   -20.64    -1.47      0.40       0.39
  12    4.970  14.13   1   -20.34    -25.56   -24.65   -1.33   -1.33   -20.34    -1.47      0.40       0.39
  12    4.970  21.02   0   -16.61    -25.39   -26.63   -2.09   -2.09   -16.61    -2.56      0.01       0.01
  12    4.970  21.02   1   -16.84    -25.93   -26.03   -2.10   -2.10   -16.84    -2.56      0.01       0.01
  16    5.545  14.13   0   -19.21    -21.79   -21.93   -4.02   -4.02   -19.22    -0.73      0.48       0.48
  16    5.545  14.13   1   -20.02    -21.15   -21.53   -0.88   -0.88   -19.90    -0.73      0.48       0.48
  16    5.545  21.02   0   -18.18    -21.35   -21.23   -1.91   -1.91   -18.18    -0.68      0.30       0.30
  16    5.545  21.02   1   -19.04    -22.72   -21.50   -0.97   -0.97   -19.05    -0.68      0.30       0.30
  20    5.991  14.13   0   -19.06    -19.96   -19.60   -1.52   -1.52   -19.21    -0.04      0.59       0.61
  20    5.991  14.13   1   -18.41    -19.36   -19.51   -2.05   -2.05   -18.38    -0.04      0.59       0.61
  20    5.991  21.02   0   -17.66    -20.54   -20.58   -0.74   -0.74   -17.67     1.18      1.35       1.46
  20    5.991  21.02   1   -17.79    -19.87   -19.48   -0.92   -0.92   -17.76     1.18      1.35       1.46
```

## Reading

The Schur and commutator formulas match the center to the available double
precision scale.  For larger `lambda` the error exponents are closer to the
center because the same finite-section conditioning already seen in E73.260 is
present; the identity itself is algebraic.

The important diagnostic is the scale separation:

```text
archB, primeB  = ordinary size;
centerB        = many powers smaller;
rhoNormB       = not rapidly small.
```

Thus a norm estimate for the Schur residual row is impossible.  The remaining
theorem must prove paired archimedean-prime cancellation after pairing with the
Gamma-prime eigenline:

```text
q_aH_L^A(I-P_w)xi_L - q_aH_L^P(I-P_w)xi_L = O_M(L^-M).
```

## Status

```text
validated: rho=qHR=qH-(qHQ*)GQ=-q[H,P];
validated: arch/prime terms are individually large;
confirmed: UNIF-ETA is a paired eigenline cancellation, not a row-norm theorem.
```


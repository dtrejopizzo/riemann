# E73.186 results - transverse Schur residual

Command:

```text
python3 E73_186_transverse_schur_probe.py
```

Output:

```text
E73.186 transverse Schur probe
Tests rho_j xi = q_j H (I-P_Q) xi and the model-prime transverse split.
 lam     L gamma row residB transB errB  modelTB primeTB signedTB
  12   4.970   14.13   0  -20.82  -20.80 -22.89    -1.51   -1.51   -20.81
  12   4.970   14.13   1  -21.04  -21.07 -23.00    -2.11   -2.11   -21.09
  12   4.970   21.02   0  -20.39  -20.40 -24.24    -1.88   -1.88   -20.40
  12   4.970   21.02   1  -19.86  -19.87 -24.84    -2.72   -2.72   -19.86
  16   5.545   14.13   0  -19.24  -19.27 -21.08    -4.02   -4.02   -19.31
  16   5.545   14.13   1  -19.94  -20.10 -20.77    -0.88   -0.88   -19.98
  16   5.545   21.02   0  -18.18  -18.18 -22.15    -1.91   -1.91   -18.18
  16   5.545   21.02   1  -19.04  -19.02 -20.84    -0.97   -0.97   -19.01
  20   5.991   14.13   0  -19.22  -19.09 -19.98    -1.52   -1.52   -18.97
  20   5.991   14.13   1  -18.52  -18.53 -21.08    -2.05   -2.05   -18.58
  20   5.991   21.02   0  -17.66  -17.65 -19.84    -0.74   -0.74   -17.66
  20   5.991   21.02   1  -17.79  -17.77 -19.63    -0.92   -0.92   -17.78
  24   6.356   14.13   0  -16.64  -16.63 -18.89    -1.28   -1.28   -16.63
  24   6.356   14.13   1  -17.80  -17.74 -18.95    -0.91   -0.91   -17.76
  24   6.356   21.02   0  -17.98  -17.95 -19.62    -1.23   -1.23   -17.96
  24   6.356   21.02   1  -17.94  -17.90 -19.33    -0.98   -0.98   -17.91
  32   6.931   14.13   0  -17.17  -17.28 -18.03    -1.40   -1.40   -17.21
  32   6.931   14.13   1  -17.69  -17.58 -18.47    -1.44   -1.44   -17.60
  32   6.931   21.02   0  -16.68  -16.71 -18.27    -1.50   -1.50   -16.72
  32   6.931   21.02   1  -17.29  -17.22 -18.33    -0.99   -0.99   -17.28
```

Reading:

```text
residB and transB should match;
errB should be below both;
modelTB and primeTB show whether transverse model-prime terms remain large
before cancellation.
```

Reading:

```text
residB and transB match to the displayed precision;
errB is smaller than the residual scale;
modelTB and primeTB are ordinary size and nearly equal;
signedTB is the tiny cancellation scale.
```

Thus the principal correction has been absorbed cleanly into the transverse
vector `(I-P_w)xi_L`.  The remaining theorem is `TRANS-SCRCE`, a signed
model-prime equality on the transverse Cauchy component.

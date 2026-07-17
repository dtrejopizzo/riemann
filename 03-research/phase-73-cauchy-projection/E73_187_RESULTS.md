# E73.187 results - transverse vector structure

Command:

```text
python3 E73_187_transverse_vector_structure_probe.py
```

Output:

```text
E73.187 transverse vector structure
Tests whether xi_perp is small, concentrated, or a genuine large transverse vector.
 lam     L gamma  parN perpN top eff  modelB primeB signedB gain angle parValB
  12   4.970   14.13 1.98e-16 1.00e+00 0.69  10.4   -1.47   -1.47   -20.70 -19.24 1.000  -21.62
  12   4.970   21.02 8.33e-15 1.00e+00 0.69  10.4   -1.86   -1.86   -19.81 -17.96 1.000  -20.01
  16   5.545   14.13 4.44e-16 1.00e+00 0.44  19.3   -0.88   -0.88   -19.28 -18.41 1.000  -20.04
  16   5.545   21.02 2.18e-15 1.00e+00 0.44  19.3   -0.96   -0.96   -18.16 -17.20 1.000  -19.12
  20   5.991   14.13 3.07e-16 1.00e+00 0.70  10.8   -1.48   -1.48   -18.50 -17.01 1.000  -19.29
  20   5.991   21.02 2.00e-16 1.00e+00 0.70  10.8   -0.62   -0.62   -17.51 -16.89 1.000  -18.50
  24   6.356   14.13 1.79e-15 1.00e+00 0.66  13.8   -0.85   -0.85   -16.63 -15.78 1.000  -17.62
  24   6.356   21.02 1.77e-16 1.00e+00 0.66  13.8   -0.89   -0.89   -17.75 -16.86 1.000  -18.86
  32   6.931   14.13 1.31e-16 1.00e+00 0.65  21.0   -1.24   -1.24   -17.15 -15.91 1.000  -18.24
  32   6.931   21.02 1.93e-16 1.00e+00 0.65  21.0   -0.95   -0.95   -16.68 -15.73 1.000  -17.77
```

Column meanings:

```text
parN    = ||P_w xi_L||_2
perpN   = ||(I-P_w)xi_L||_2
top     = max component of xi_perp divided by ||xi_perp||
eff     = participation ratio ||xi_perp||_1^2/||xi_perp||_2^2
modelB  = log_L ||Q_w H_model xi_perp||
primeB  = log_L ||Q_w Prime xi_perp||
signedB = log_L ||Q_w(H_model-Prime)xi_perp||
gain    = log_L(||signed||/max(||model||,||prime||))
angle   = Hermitian cosine between the two transverse two-vectors
parValB = log_L ||Q_w xi_L||
```

Reading:

```text
xi_perp is not small: perpN=1.00 in all rows.
xi_par is numerically zero at the sampled characteristic nodes.
xi_perp is not a single-coordinate artifact: eff ranges from about 10 to 21.
model and prime transverse two-vectors are ordinary size.
their angle is 1.000 to displayed precision.
the signed difference is tiny, with 15--20 powers of L of gain.
```

Conclusion:

```text
The scalar residual is not explained by projection smallness.
The load-bearing theorem is a transverse model-prime matching identity:

||Q_w(H_model,L-Prime_L)(I-P_w)xi_L||_2 <= C_R L^(-R).
```

This is the finite analytic target that remains after E73.181--E73.186.

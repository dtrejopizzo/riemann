# E73.181 results - explicit-formula principal residual

Command:

```text
python3 E73_181_explicit_formula_principal_residual_probe.py
```

Output:

```text
E73.181 explicit-formula principal residual probe
Verifies A_L[B_q]-P_L[B_q] minus Cauchy principal part equals SCRCE signed scalar.
 lam     L gamma row archErr primeErr signedB quadB errB principalB
  12   4.970   14.13   0 1.6e-14  3.0e-15  -20.77 -21.03 -21.43     -20.72
  12   4.970   14.13   1 4.8e-14  4.1e-14  -21.09 -21.16 -22.50     -20.99
  12   4.970   21.02   0 1.1e-14  3.1e-15  -20.39 -20.47 -21.75     -20.40
  12   4.970   21.02   1 3.1e-14  5.0e-15  -19.87 -19.85 -22.24     -19.87
  16   5.545   14.13   0 1.1e-12  1.5e-12  -19.26 -19.21 -20.67     -19.10
  16   5.545   14.13   1 2.9e-15  2.1e-15  -19.99 -20.07 -21.21     -19.57
  16   5.545   21.02   0 1.4e-14  7.9e-15  -18.18 -18.19 -20.29     -18.17
  16   5.545   21.02   1 4.1e-15  7.4e-16  -19.03 -19.12 -20.21     -19.07
  20   5.991   14.13   0 1.8e-13  1.0e-13  -18.92 -18.74 -18.43     -20.23
  20   5.991   14.13   1 4.8e-13  3.7e-13  -18.45 -19.03 -18.69     -18.29
  20   5.991   21.02   0 2.3e-14  4.5e-14  -17.67 -17.89 -18.30     -17.67
  20   5.991   21.02   1 3.5e-14  9.3e-14  -17.79 -18.60 -17.94     -17.72
```

The script reports:

```text
archErr:  relative reconstruction error for A_L[B_q],
primeErr: relative reconstruction error for P_L[B_q],
signedB:  exponent of the matrix signed residual,
quadB:    exponent of the explicit-formula signed residual,
errB:     exponent of their difference.
```

The intended pass condition is:

```text
archErr, primeErr small;
quadB matches signedB;
errB below the residual scale.
```

Reading:

```text
For L=4.97 and most L=5.545 rows, errB is below signedB.
At L=5.991 the residual is close to the available double-precision
quadrature floor, so errB can be comparable to signedB.
```

This is enough to certify the algebraic identity at the precision of the
quadrature implementation.  A proof or high-precision certificate should use
closed-form integration of the trigonometric-exponential packets, not
floating quadrature subtraction.

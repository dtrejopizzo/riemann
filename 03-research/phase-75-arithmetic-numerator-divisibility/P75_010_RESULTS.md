# P75.010 results

Command:

```text
python3 P75_010_scaling_falsifier_harness.py
```

Result:

```text
zeta L=4.970 N=49 dmax=30.342 mu=-2.148e-14
gamma       normQ        rootShift      |Cprime(root)|  gramCond      smin(T)      smax(T)
  14.135   3.990e-16    -1.776e-15       8.134e-01  1.031e+00   4.892e+00   5.076e+00
  21.022   1.776e-15    -3.553e-15       1.755e+00  1.003e+00   4.933e+00   4.948e+00
  25.011   5.412e-16     3.553e-15       5.029e-01  1.007e+00   4.943e+00   4.980e+00

planted L=4.970 N=49 dmax=30.342 mu=-4.995e+00
  14.135   1.271e-02     1.040e-01       4.314e-01  1.031e+00   9.911e+00   1.011e+01
  21.022   5.871e-02    -2.308e-01       7.026e-01  1.003e+00   9.799e+00   9.868e+00
  25.011   9.492e-03    -9.328e-03       3.882e+00  1.007e+00   3.920e+01   3.948e+01

Davenport-Heilbronn L=3.892 N=117 dmax=93.639 mu=-3.312e-01
   5.094   3.451e-03     8.275e-02       1.479e-01  1.089e+00   4.121e+00   4.559e+00
  14.404   3.921e-03    -7.775e-02       2.760e-01  1.017e+00   4.554e+00   4.621e+00
  19.309   3.726e-03    -1.003e-01       2.602e-01  1.007e+00   4.584e+00   4.603e+00

random-symbol L=12.000 N=48 dmax=12.566 mu=-8.849e+00
  14.135   2.291e-01           nan             nan  1.836e+00   8.884e+00   9.239e+00
  21.022   1.784e-01           nan             nan  6.306e+00   8.375e+00   9.863e+00
  25.011   1.679e-01           nan             nan  9.608e+00   8.239e+00   9.995e+00

random-kerQ L=4.970 gamma=14.135
normQ_at_gamma=1.214e-17
normQ_at_next_gamma=1.313e-02
```

The probe confirms the Phase 74 falsifier pattern under the P75 observables:
zeta locks at double precision; planted, Davenport-Heilbronn, and random
controls do not.  The two-row Gram condition and Schur singular values are
benign in these finite windows, but this remains empirical and conditional on
the unresolved signed arithmetic estimate.


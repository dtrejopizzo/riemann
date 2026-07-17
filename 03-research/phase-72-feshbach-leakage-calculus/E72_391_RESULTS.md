# E72.391 results - tail Cauchy moment identity

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_391_tail_cauchy_identity_probe.py
```

## Output

```text
E72.391 tail Cauchy identity probe
 lam    L     M      m       |orig|      |cauchy|    absErr     relErr
   8  4.159    12     24   5.940e-11   5.940e-11  2.240e-18  3.772e-08
   8  4.159    12     36   2.371e-11   2.371e-11  8.891e-19  3.751e-08
   8  4.159    12     48   9.988e-12   9.988e-12  1.584e-19  1.586e-08
  10  4.605    14     28   2.086e-09   2.086e-09  3.055e-18  1.465e-09
  10  4.605    14     42   6.412e-11   6.412e-11  2.240e-19  3.493e-09
  10  4.605    14     56   2.733e-11   2.733e-11  7.381e-19  2.701e-08
  12  4.970    16     32   2.213e-10   2.213e-10  1.129e-18  5.102e-09
  12  4.970    16     48   2.160e-11   2.160e-11  1.161e-19  5.374e-09
  12  4.970    16     64   9.514e-12   9.514e-12  2.790e-19  2.932e-08
  14  5.278    18     36   3.100e-10   3.100e-10  3.827e-19  1.234e-09
  14  5.278    18     54   5.680e-11   5.680e-11  2.104e-19  3.705e-09
  14  5.278    18     72   2.655e-11   2.655e-11  4.312e-19  1.624e-08
```

## Interpretation

The probe compares two independent formulas for the same tail coefficient:

```text
original: sum_w (1-e^(wL)) sum_n xi_n [Phi_w(d_m)-Phi_w(d_n)]/[pi(n-m)]
```

and

```text
Cauchy:  -2i/L sum_w wG_x(w)/(w^2+d_m^2).
```

They agree to roundoff.  The relative error is larger only when the coefficient itself is near
`10^-11`, so absolute error is the better diagnostic.

## Status

```text
verified: exact tail coefficient collapse to the Cauchy nodal vector;
consequence: finite Fourier tail is absorbed by the same nodal suppression theorem as PAIR-Z;
remaining: prove the nodal suppression theorem uniformly, including outside-window bookkeeping.
```


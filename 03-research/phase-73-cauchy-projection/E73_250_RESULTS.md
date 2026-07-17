# E73.250 results - Gram increment probe

Command:

```text
python3 E73_250_gram_increment_probe.py
```

## 1. Output

```text
E73.250 Gram increment probe
Vol_Q = product of Gram-Schmidt increments.
 lam      L pow order volB prodIncB minRowB maxRowB minSinB incB-values                     sinB-values
   8    4.159   0 native -45.28   -45.28  -11.15   -8.25   -3.06 -11.15 -11.52 -11.29 -11.31       0.00  -0.36  -3.04  -3.06
   8    4.159   0 norm   -45.28   -45.28  -11.15   -8.25   -3.55  -8.25  -8.28 -14.04 -14.70       0.00  -0.02  -2.89  -3.55
  10    4.605   0 native -37.08   -37.08   -8.32   -6.63   -3.48  -8.32  -8.78  -9.87 -10.11       0.00  -0.47  -3.24  -3.48
  10    4.605   0 norm   -37.08   -37.08   -8.32   -6.63   -3.89  -6.63  -6.72 -11.52 -12.21       0.00  -0.09  -3.21  -3.89
  12    4.970   0 native -32.24   -32.24   -6.99   -5.61   -3.25  -6.99  -7.81  -8.59  -8.85       0.00  -0.81  -2.98  -3.25
  12    4.970   0 norm   -32.24   -32.24   -6.99   -5.61   -3.77  -5.61  -5.89  -9.98 -10.77       0.00  -0.28  -2.98  -3.77
  16    5.545   0 native -18.15   -18.15   -3.25   -3.10   -2.46  -3.25  -4.27  -5.06  -5.56       0.00  -1.02  -1.96  -2.46
  16    5.545   0 norm   -18.15   -18.15   -3.25   -3.10   -3.11  -3.10  -3.48  -5.21  -6.36       0.00  -0.38  -1.96  -3.11
```

The full run also includes `pow=1,2`; they show the same pattern.

## 2. Verification

For every tested row:

```text
prodIncB = volB.
```

This validates the incremental Gram factorization:

```text
Vol_Q = prod_j dist(d_j, span(d_1,...,d_{j-1})).
```

## 3. Interpretation

The smallest angle sine remains polynomial-scale.  There is no evidence of a
super-polynomial angular collapse.  Therefore `GRAM-NONDEG` should be proved as
an independence theorem for the four DD-local quotient rows:

```text
QROW-INDEP:
dist(d_j, span(d_1,...,d_{j-1})) >= L^{-B}.
```

This makes the nondegeneracy half of the pivot route look tractable and
separates it from the real spectral cancellation:

```text
MAXMIN-PIV-DIV:
z_{J_*}=O_M(L^-M).
```

# E72.365 results - projective/scalar decomposition

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_365_projective_scalar_decomposition_probe.py
```

The probe checks the decomposition

```text
||KWin k - tail - Lambda k||^2
= ||P_k^perp(KWin k-tail)||^2
  + |lambda_win-Lambda|^2 ||k||^2.
```

It uses `mu` as a visible scalar proxy.  The theorem uses

```text
Lambda_L=mu+e_pole-2kappa_*,
```

so this is not a final scalar-consistency test.  It is a decomposition check.

## Table

```text
lam   N roots node    |lambda_win|  projDef     scalarDef(mu)  pythErr
 6.0  10     2 root           nan        nan            nan        nan
 6.0  10     2 shift   2.76106e+00  4.681e-01      3.470e+00  4.441e-16

 8.0  12     3 root    4.39129e+00  1.850e-12      1.360e-11  1.616e-27
 8.0  12     3 shift   4.50406e+00  4.779e+00      2.263e+01  1.066e-14

10.0  14     3 root    4.46939e+00  1.578e-12      1.331e-11  1.616e-27
10.0  14     3 shift   4.68375e+00  5.720e+00      2.308e+01  0.000e+00

12.0  16     3 root    4.76580e+00  1.056e-14      8.729e-14  1.262e-29
12.0  16     3 shift   4.34539e+00  9.064e+00      1.890e+01  0.000e+00
```

## Reading

The Pythagorean decomposition holds to roundoff:

```text
pythErr ~ 1e-14 or smaller.
```

Thus the split is numerically exact:

```text
projective defect + scalar defect = full CFIR residual for a chosen scalar.
```

This validates E72.365:

```text
PCFIR alone is not CFIR-H.
PCFIR + SCALAR-CONS is CFIR-H.
```

For shifted controls, the scalar defect using the proxy `mu` is often larger than the projective
defect, so `SCALAR-CONS` is not cosmetic.

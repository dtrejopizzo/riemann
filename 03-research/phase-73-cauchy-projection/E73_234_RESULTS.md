# E73.234 results - adjoint principal residual equivalence

Command:

```text
python3 E73_234_adjoint_principal_residual_probe.py
```

## 1. Output

```text
E73.234 adjoint principal residual equivalence
Checks qHRxi = rho xi = <rho*,xi>, rho=qHR, and Rq*=0.
 lam      L gamma row centerB rhoB adjB errRhoB errAdjB ||Rq*||B
   8    4.159  14.13   0   -21.68  -21.68  -21.68   -484.67    -28.55    -26.23
   8    4.159  14.13   1   -21.46  -21.46  -21.46   -484.67    -28.73    -26.25
   8    4.159  21.02   0   -15.76  -15.76  -15.76   -484.67    -29.28    -26.20
   8    4.159  21.02   1   -15.79  -15.79  -15.79   -484.67    -29.96    -26.30
  10    4.605  14.13   0   -18.50  -18.50  -18.50   -452.32    -25.38    -24.38
  10    4.605  14.13   1   -18.51  -18.51  -18.51   -452.32    -26.07    -24.38
  10    4.605  21.02   0   -14.98  -14.98  -14.98   -452.32    -26.91    -24.12
  10    4.605  21.02   1   -14.98  -14.98  -14.98   -452.32    -28.82    -23.86
  12    4.970  14.13   0   -20.64  -20.64  -20.64   -430.82    -24.61    -23.23
  12    4.970  14.13   1   -20.34  -20.34  -20.34   -430.82    -26.40    -23.16
  12    4.970  21.02   0   -16.61  -16.61  -16.61   -430.82    -25.49    -23.20
  12    4.970  21.02   1   -16.84  -16.84  -16.84   -430.82    -26.30    -23.35
```

## 2. Interpretation

The identities

```text
qHRxi = rho xi = <rho*,xi>,       rho=qHR,
Rq*=0
```

are numerically certified.  The direct `rho xi` equality is exact to the
floating zero floor in these tests.  The adjoint pairing agrees to
`L^-24`--`L^-30`, limited by floating Hermitian/projection rounding.

Thus:

```text
E73.233 paired commutator target
= E73.180/E73.181 Cauchy-principal residual target.
```

There is no separate commutator theorem to prove.  The unique U4 target is
`APR-U4`, the finite explicit principal residual estimate.


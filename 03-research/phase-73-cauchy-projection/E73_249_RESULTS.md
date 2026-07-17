# E73.249 results - Cauchy-Binet quotient volume

Command:

```text
python3 E73_249_cauchy_binet_volume_probe.py
```

## 1. Output

```text
E73.249 Cauchy-Binet quotient volume
vol^2=det(D_Q D_Q*)=sum_J |det D_Q[:,J]|^2.
 lam      L pow n r volB maxB rmsB combB gapMaxVolB svProdB cbRel
   8    4.159   0  13  4 -45.28 -46.48 -47.58   2.31       1.21   -45.28  3.9e-12
   8    4.159   1  13  4 -45.28 -46.48 -47.58   2.31       1.21   -45.28  9.7e-12
   8    4.159   2  13  4 -45.28 -46.48 -47.58   2.31       1.20   -45.28  5.2e-12
  10    4.605   0  17  4 -37.08 -38.38 -39.62   2.55       1.30   -37.08  1.2e-10
  10    4.605   1  17  4 -37.08 -38.38 -39.62   2.55       1.30   -37.08  4.6e-11
  10    4.605   2  17  4 -37.08 -38.38 -39.62   2.55       1.30   -37.08  6.0e-12
  12    4.970   0  21  4 -32.24 -33.65 -34.96   2.71       1.41   -32.24  3.1e-11
  12    4.970   1  21  4 -32.28 -33.69 -34.99   2.71       1.41   -32.28  4.0e-12
  12    4.970   2  21  4 -32.28 -33.69 -34.99   2.71       1.41   -32.28  8.5e-11
  16    5.545   0  41  4 -18.15 -19.69 -21.51   3.36       1.55   -18.15  1.4e-11
  16    5.545   1  41  4 -22.66 -24.31 -26.02   3.36       1.65   -22.66  1.6e-12
  16    5.545   2  41  4 -30.14 -31.44 -33.50   3.36       1.30   -30.14  3.3e-12
```

## 2. Verification

The Cauchy-Binet relative error is at numerical floor:

```text
cbRel <= 1.2e-10.
```

The singular-value product matches the Gram volume:

```text
svProdB = volB.
```

The maximal minor is close to the quotient volume:

```text
gapMaxVolB = log_L(Vol_Q/maxMinor) between 1.20 and 1.65
```

in the tested windows.

The deterministic bound is weaker but sufficient:

```text
max_J |minor_J| >= Vol_Q / sqrt(C(n,4)).
```

The observed combinatorial exponent is:

```text
combB = log_L sqrt(C(n,4)) between 2.31 and 3.36.
```

## 3. Endpoint update

`MAXMIN-NONDEG` is reduced to:

```text
GRAM-NONDEG:
det(D_QD_Q^*)^{1/2} >= L^{-B}.
```

Together with polynomial width, this gives the maximal-minor denominator lower
bound.  The remaining difficult statement is still:

```text
MAXMIN-PIV-DIV:
z_{J_*}=O_M(L^-M).
```

# E73.254 results - Laplace expansion of Cramer numerators

Command:

```text
python3 E73_254_laplace_cramer_alternation.py
```

## 1. Output excerpt

```text
E73.254 Laplace expansion of Cramer numerators
N_j=sum_a pair_a Cof_{a,j}; measures alternating cancellation.
 lam      L pow pivIdx              coord numB termMaxB termAbsB altGainB termExps
   8    4.159   0     [-5, -2, 2, 5]     0 -51.04   -51.21   -51.04     0.01 -54.63 -53.78 -52.17 -51.21
   8    4.159   0     [-5, -2, 2, 5]     1 -50.83   -50.65   -50.47     0.36 -53.45 -53.00 -51.66 -50.65
  10    4.605   0     [-7, -6, 6, 7]     0 -45.04   -44.17   -43.76     1.28 -45.96 -46.46 -44.17 -44.34
  10    4.605   0     [-7, -6, 6, 7]     1 -42.61   -42.95   -42.61     0.00 -44.63 -44.43 -43.43 -42.95
  12    4.970   0     [-9, -4, 4, 9]     1 -42.21   -41.28   -40.87     1.33 -43.34 -42.94 -41.41 -41.28
  16    5.545   0 [-20, -13, 18, 20]     1 -31.63   -31.92   -31.45     0.18 -32.14 -32.62 -31.92 -32.75
```

## 2. Interpretation

The key diagnostic is:

```text
altGainB = log_L(termAbs/|N_j|).
```

It is not large.  The numerator is not hiding a huge cancellation among four
large Laplace terms.  The dominant terms are already at the numerator scale.

Therefore a proof should not chase a large alternating cancellation identity.
It should prove the smallness of the bordered vector:

```text
b = D_Q xi_L.
```

with polynomial cofactor and denominator controls supplied by the
`GRAM-NONDEG/MAXMIN-NONDEG` side.

## 3. Status

```text
rejected: ALT-CRAMER as a major cancellation mechanism;
kept:     CRAMER-NUM-DIV;
next:     structural proof of b=D_Qxi_L small in the quotient packet.
```

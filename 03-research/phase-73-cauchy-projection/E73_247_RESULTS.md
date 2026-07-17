# E73.247 results - physical pivot quotient coordinates

Command:

```text
python3 E73_247_pivot_quotient_coordinates.py
```

## 1. Summary table

```text
E73.247 pivot quotient coordinates
Physical pivot coordinates J give D_Q xi = D_Q[:,J] z_J.
 lam      L pow MDranks qRank pivIdx condB pairMaxB zMaxB xiJMaxB transB reconErrB formulaErrB
   8    4.159   0    [5, 5]     4     [-5, 5, 2, -2]   6.89   -15.76  -4.31   -0.67   0.36     -38.47      -22.73
   8    4.159   1    [5, 5]     4     [-5, 5, -2, 2]   6.89   -15.76  -4.31   -0.67   0.36     -38.20      -23.48
   8    4.159   2    [5, 5]     4     [5, -5, 2, -2]   6.88   -15.75  -4.04   -0.67   0.36     -38.59      -22.53
  10    4.605   0    [5, 5]     4      [7, -7, 2, 0]   6.18   -14.98  -3.92   -0.24   0.60     -35.96      -21.64
  10    4.605   1    [5, 5]     4      [7, -7, 2, 0]   6.18   -14.98  -3.92   -0.24   0.60     -36.43      -20.41
  10    4.605   2    [5, 5]     4      [7, -7, 2, 0]   6.18   -14.98  -3.92   -0.24   0.60     -35.87      -20.99
  12    4.970   0    [5, 5]     4     [-9, 9, 3, -5]   5.89   -16.61  -7.54   -0.90   0.69     -37.89      -19.28
  12    4.970   1    [5, 5]     4     [-9, 9, 3, -5]   5.92   -16.64  -6.63   -0.90   0.69     -35.58      -19.64
  12    4.970   2    [5, 5]     4     [-9, 9, 3, -5]   5.92   -16.61  -7.63   -0.90   0.69     -37.36      -19.96
  16    5.545   0    [6, 6]     4 [20, -20, 18, -13]   4.20   -18.20 -11.94   -1.63   0.77     -37.47      -19.64
  16    5.545   1    [8, 7]     4 [20, -20, 18, -18]   4.00   -15.26  -8.18   -1.63   0.80     -34.54      -20.31
  16    5.545   2    [8, 8]     4 [-20, 20, -18, 18]   4.30   -17.03  -8.65   -1.63   0.44     -36.38      -19.54
```

## 2. Canonical `pow=0` pivot coordinates

```text
Canonical pow=0 pivot coordinates:
 lam      L pivIdx              zB-values
   8    4.159     [-5, 5, 2, -2]   -4.56   -4.55   -4.31   -4.35
  10    4.605      [7, -7, 2, 0]   -4.68   -4.68   -8.15   -3.92
  12    4.970     [-9, 9, 3, -5]   -8.57   -8.41   -7.54   -8.49
  16    5.545 [20, -20, 18, -13]  -12.60  -12.63  -12.38  -11.94
```

## 3. Interpretation

The pivot-coordinate identity is numerically exact:

```text
D_Q xi = D_Q[:,J] z_J,
z_J = xi_J + D_Q[:,J]^{-1}D_Q[:,R] xi_R.
```

The reconstruction errors are far below the scalar pairings.  The transfer
operator has small exponent (`transB` around `0.36--0.80`), while the pivot
condition exponent is moderate (`condB` around `4--7`).

The important observation is that `z_J` is much smaller than the raw pivot
entries `xi_J`; for example:

```text
lambda=16, pow=0:
xiJMaxB = -1.63,
zMaxB  = -11.94.
```

Thus the scalar obstruction is equivalent to a cancellation in the physical
coordinate formula

```text
xi_J + T_J xi_R.
```

## 4. Cautions

The pivot sets are not yet a symbolic law.  They are selected by QR pivoting,
and the `lambda=16` DD-local rank remains conditioning-sensitive as in E73.245.

Therefore this is not a final proof.  It is the first algebraizable coordinate
version of the quotient obstruction:

```text
PIV-QUOT-DIV:
xi_J + D_Q[:,J]^{-1}D_Q[:,R] xi_R = O_M(L^-M).
```

## 5. Status

```text
new endpoint: PIV-QUOT-DIV;
avoids:       full rowspace projection and transverse eigen-branch;
open:         symbolic pivot rule and analytic proof of the pivot coordinate
              cancellation.
```

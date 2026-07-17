# E72.365 - Projective CFIR and scalar consistency

## 1. Purpose

E72.363 rewrote the simple-window divisor block as the eigenline condition

```text
P_k^perp(KWin k - tail)=O(L^B).
```

This note identifies exactly what that condition proves and what it does not prove.  It is the
projectivization of the finite Hermite CFIR equation.  To recover the full equation one still needs
`SCALAR-CONS`.

## 2. Simple-window CFIR equation

For a simple Xi-zero window, write

```text
k := J_TG_x,
KWin_{ij}:=K_L(a_i,a_j),
t := J_TTail_T^M.
```

The finite Hermite equation is

```text
(Lambda_L I - KWin)k + t = O_T(L^B).                 (1)
```

Equivalently,

```text
KWin k - t = Lambda_L k + O_T(L^B).                  (2)
```

## 3. Projective part

Applying the quotient projection by `span{k}` gives

```text
P_k^perp(KWin k - t)=O_T(L^B).                       (3)
```

This is exactly the eigenline certificate of E72.363.  Thus:

```text
CFIR-H => projective CFIR.
```

Conversely, (3) implies the existence of a scalar `lambda_win` such that

```text
KWin k - t = lambda_win k + O_T(L^B).                 (4)
```

But (4) does not identify `lambda_win`.

## 4. Scalar consistency

The missing scalar condition is:

```text
SCALAR-CONS:
lambda_win = Lambda_L + O_T(L^B/||k||)
```

in the chosen normalization.  With this condition, (4) becomes (2), and hence the full CFIR-H
equation follows.

Therefore:

```text
projective CFIR + SCALAR-CONS => CFIR-H.
```

This is the precise role of `SCALAR-CONS` in E72.358.

## 5. Least scalar formula

When `k != 0`, the quotient scalar is explicitly

```text
lambda_win
= <k, KWin k - t>/<k,k>.                              (5)
```

The perpendicular residual is

```text
||(KWin k - t)-lambda_win k||.
```

Thus both projective CFIR and scalar consistency are finite computable quantities:

```text
projective defect:
  ||P_k^perp(KWin k-t)||;

scalar defect:
  |lambda_win-Lambda_L| ||k||.
```

## 6. Consequence for the proof strategy

E72.363 and E72.364 show that projective CFIR cannot be proved from `KWin` alone.  E72.365 adds that
even proving projective CFIR is not enough.  The full route requires two statements:

```text
PCFIR:
  P_k^perp(KWin k-t)=O_T(L^B).

SCALAR-CONS:
  lambda_win=Lambda_L+controlled error.
```

Together these are equivalent to the simple-window finite CFIR equation.

## 7. Status

```text
proved: CFIR-H implies projective CFIR;
proved: projective CFIR plus SCALAR-CONS implies CFIR-H;
specified: finite scalar formula lambda_win=<k,KWin k-t>/<k,k>;
open: prove PCFIR and SCALAR-CONS for Xi-zero windows from the coupled explicit formula.
```

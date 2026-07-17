# E72.363 - Residue eigenline certificate

## 1. Purpose

E72.362 shows that, for shifted controls, the dominant obstruction is the interpolation-window skew,
not the finite tail.  This note rewrites the window skew as an eigenline condition on the finite
residue space of the Xi-zero window.

## 2. Window operator on residue values

For a simple zero window `W_T={a_1,...,a_N}`, define the finite matrix

```text
KWin_{ij}:=K_L(a_i,a_j),
```

with removable diagonal values.  Let

```text
k_i:=K(a_i)=G_x(a_i),
t_i:=Tail_{a_i}^M xi.
```

Then

```text
s_i = -sum_j KWin_{ij} k_j + t_i.                    (1)
```

The CFIR divisor-block skew condition is

```text
s_i k_l - s_l k_i = O(L^B)                            (2)
```

for all `i,l`.

## 3. Eigenline form

Substitute (1) into (2).  The condition is equivalent to:

```text
(-KWin k + t) wedge k = O(L^B).                       (3)
```

Thus there must exist a scalar `lambda_win` such that

```text
KWin k = t + lambda_win k + O(L^B).                   (4)
```

In words:

```text
the interpolation window operator sends the residue vector k
back into the affine line t + span{k}.
```

If the tail is negligible in the fixed window, this becomes the eigenline condition

```text
KWin k = lambda_win k + O(L^B).                       (5)
```

## 4. Certificate

Let `P_k^\perp` denote any projection onto the quotient by the line `span{k}`.  The exact simple-window
certificate is:

```text
P_k^\perp (KWin k - t)=0.                             (6)
```

The polynomial version is:

```text
||P_k^\perp (KWin k - t)|| <= C_T L^B.                (7)
```

This is the same as the alternating matrix vanishing, but it is more structural: it says the
interpolation operator has a divisor-residue eigenline after the signed tail correction.

## 5. Why this is useful

The matrix `KWin` is built only from the universal kernel `K_L(a_i,a_j)`.  The vector `k` contains the
finite Feshbach/Cauchy data `G_x(a_i)`.  Therefore (6) is exactly the point where the Xi divisor must
interact with the finite Feshbach data.

The shifted controls fail because a generic shifted window does not make `k` an eigenline of
`KWin` modulo the tail.  An Xi-zero window would have to supply this relation through the explicit
formula.

## 6. Status

```text
proved: simple CFIR-DIV is equivalent to the residue eigenline condition (6);
observed: shifted controls fail because KWin k is not tail-corrected collinear with k;
open: prove the eigenline condition for Xi-zero windows from the completed explicit formula.
```

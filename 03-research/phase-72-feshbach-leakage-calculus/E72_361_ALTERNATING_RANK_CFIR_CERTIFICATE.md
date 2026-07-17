# E72.361 - Alternating-rank CFIR certificate

## 1. Purpose

For simple Xi-zero windows, E72.360 gives a double `Z'/Z` contour formulation of `CFIR-DIV`.
The compatibility minor has the special alternating form

```text
Delta(z,w)=S(z)K(w)-S(w)K(z).
```

This note packages the finite condition as a rank statement for an alternating residue form.

## 2. Simple-zero residue space

Let `W_T={a_1,...,a_N}` be a finite simple Xi-zero window.  The residue functional

```text
Res_T[F]
:= (1/2pi i) int_{Omega_T} F(z) Z'(z)/Z(z) dz
```

is the finite sum

```text
Res_T[F]=sum_{j=1}^N F(a_j)
```

for simple zeros inside the contour.

Choose any basis of test functions `phi_1,...,phi_N` whose evaluation matrix

```text
V_{ij}=phi_i(a_j)
```

is invertible.  This is just finite interpolation on the window.

## 3. Alternating matrix

Define

```text
A_{pq}
:= (1/(2pi i)^2) int int
   phi_p(z) phi_q(w)
   Delta(z,w)
   Z'(z)/Z(z) Z'(w)/Z(w) dw dz.                      (1)
```

For simple zeros,

```text
A_{pq}
= sum_{i,j} phi_p(a_i)phi_q(a_j)
   [S(a_i)K(a_j)-S(a_j)K(a_i)].                      (2)
```

Thus

```text
A = V [s k^T - k s^T] V^T,                           (3)
```

where

```text
s_i=S(a_i),       k_i=K(a_i).
```

## 4. Certificate

Because `V` is invertible,

```text
A=0
```

if and only if

```text
s k^T-k s^T=0.                                      (4)
```

Equation (4) holds if and only if `s` and `k` are collinear, i.e. if and only if there exists a scalar
`Lambda` such that

```text
s_i + Lambda k_i=0
```

for every node with the usual zero-denominator convention.

Therefore, for simple windows:

```text
CFIR-DIV
<=> alternating residue matrix A vanishes
<=> rank[s,k] <= 1
<=> Lambda-elimination minors vanish.
```

## 5. Polynomial version

The polynomial certificate is:

```text
||A|| <= C_T L^B
```

in a test basis with controlled condition number.  Equivalently,

```text
||s k^T-k s^T|| <= C_T L^B
```

after inverting the finite interpolation matrix `V`.

This is a finite matrix condition rather than a list of pairwise scalar identities.

## 6. Why this helps

The double explicit formula can attack `A` directly:

```text
A_{pq}
= int int phi_p(z)phi_q(w)
   [S(z)K(w)-S(w)K(z)]
   Z'/Z(z)Z'/Z(w).
```

The antisymmetry means any symmetric part cancels automatically.  Thus the next analytic expansion
should preserve the alternating structure and only estimate the skew part of the coupled
archimedean-prime expression.

This is sharper than expanding all pairwise minors separately.

## 7. Status

```text
proved: simple-window CFIR-DIV is equivalent to vanishing of an alternating residue matrix;
proved: this is equivalent to rank-one/collinearity of the finite residue vectors;
open: expand A by the completed explicit formula and prove polynomial smallness for exact S,K.
```

# E72.324 -- Maximal-real-part cluster Cauchy block

**Purpose.** Generalize E72.323 from one off-line quadruple to an arbitrary finite cluster of shifted
zeros with the same maximal positive real part in a fixed height window.

The leading block is a Cauchy matrix, hence explicitly invertible.

## 1. Maximal cluster

Fix a finite height window and suppose an off-line shifted zero exists. Let

```text
alpha := max Re w > 0
```

among shifted zeros in the window. Choose one representative from each `+-` pair and list the zeros
with real part `alpha`:

```text
A={a_1,...,a_N},        Re a_j=alpha.
```

Since representatives are chosen modulo `w ~ -w`, no two representatives satisfy

```text
a_j+a_k=0.
```

Assume first that the `a_j` are distinct. Multiple zeros are the confluent Cauchy case and are
separated below as bookkeeping.

## 2. Leading coefficients

From E72.322, for row `a_j`,

```text
D_{a_j}^lead=-e^(a_jL)/(2a_j).
```

For `j != k`, the same expansion as E72.323 gives

```text
K_{a_j,a_k}^lead=e^(a_jL)/(a_j+a_k).
```

Since the system is

```text
D_{a_j}G(a_j)-sum_{k != j}K_{a_j,a_k}G(a_k)=Err_j,
```

the full leading cluster matrix is

```text
-diag(e^(a_jL)) C_A,
```

where

```text
C_A(j,k):=1/(a_j+a_k).                                  (1)
```

The diagonal entry `C_A(j,j)=1/(2a_j)` reproduces the self-pair diagonal.

## 3. Cauchy determinant

The matrix `C_A` is a symmetric Cauchy matrix. Its determinant is

```text
det C_A
= prod_{j<k}(a_k-a_j)^2
   / prod_{j,k}(a_j+a_k).                               (2)
```

The denominator is nonzero because

```text
Re(a_j+a_k)=2alpha>0.
```

The numerator is nonzero for distinct cluster points. Therefore

```text
det C_A != 0.                                           (3)
```

Thus the maximal-real-part cluster block is invertible at leading exponential scale.

## 4. Consequence for nodal suppression

The inverse of the leading block has the form

```text
-C_A^(-1)diag(e^(-a_jL)).
```

Hence polynomial errors in the maximal block imply

```text
G(a_j)=O(e^(-alpha L)L^B)
```

for every `a_j in A`.

Couplings to zeros with smaller real part are lower in the descending induction. If their nodal values
have already been suppressed at their own real-part scale, their contribution to the maximal block is
polynomial or exponentially smaller after the same normalization.

## 5. Cluster theorem

The zero-node theorem should now be stated as:

```text
ZCB:
for each maximal-real-part off-line cluster in a fixed height window, the leading Cauchy block
C_A(j,k)=1/(a_j+a_k) is invertible, and the error/tail terms are polynomial after lower clusters have
been eliminated.
```

For simple clusters, E72.324 proves the invertibility.

## 6. Remaining bookkeeping

The unresolved parts are no longer the main exponential block. They are:

```text
1. confluent Cauchy blocks for multiple zeros;
2. finite Fourier tail `Lcal(B_z^tail)`;
3. outside-window zero contribution in the contour truncation;
4. propagation from nodal suppression back to strip `PW-Cauchy`.
```

## 7. Status

```text
proved: simple maximal-real-part cluster has invertible Cauchy leading block;
closed: confluent multiplicity block in E72.325;
open:   finite tail, outside-window error, and nodal-to-strip propagation.
```

This closes the cluster-invertibility part of the transformed compact route.

E72.325 proves the confluent Cauchy block is invertible by a partial-fraction nullspace argument.

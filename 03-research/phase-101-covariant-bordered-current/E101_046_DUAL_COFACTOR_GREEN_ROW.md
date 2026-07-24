# E101.046 - Dual cofactor Green row

## 1. Rectangular boundary matrix

Let `M` be an `r` by `r+1` matrix of full row rank.  Let `ell` be a row
functional which does not vanish on `ker M`, and form the square bordered
matrix

```text
A=[ell; M].                                         (1.1)
```

Then `A` is invertible.  The unique normalized boundary vector is

```text
y=A^(-1)e_0,
My=0,
ell y=1,                                            (1.2)
```

where `e_0` is the first coordinate vector in the bordered equation space.

For a row observation `c`, define

```text
B_y(c)=c y.                                         (1.3)
```

The safe Cauchy observation of E101.045 is obtained by taking

```text
c=c_z,
(c_z)_j=z/(z-d_j).                                  (1.4)
```

## 2. Dual Green row

### Theorem 2.1

There is a unique row `p_c` on the equation space of `M` such that

```text
p_c M=c-B_y(c)ell.                                  (2.1)
```

It is given explicitly by

```text
[B_y(c),p_c]=c A^(-1).                              (2.2)
```

If `k` is any vector with `ell k=1` and `e=Mk`, then

```text
B_y(c)-c k=-p_c e.                                  (2.3)
```

### Proof

Multiplying (2.2) by `A` gives

```text
c=B_y(c)ell+p_cM,                                   (2.4)
```

which proves existence and (2.1).  Since `M` has full row rank, the map
`p->pM` is injective, proving uniqueness.  Applying (2.4) to `k` gives

```text
c k=B_y(c)+p_c e,                                   (2.5)
```

and hence (2.3). `QED`

For `c=c_z`, Theorem 2.1 is the dual form of E101.045(2.4):

```text
p_(c_z)=Psi_z,
B_y(z)/B_k(z)-1=-p_(c_z)e/B_k(z).                  (2.6)
```

The restricted inverse has disappeared.  The same object is now
characterized by the adjoint equation (2.1).

## 3. Cofactor formula

Let `A[a<-c]` denote the matrix obtained from `A` by replacing row `a` by
`c`, with row zero equal to the boundary row `ell`.  Cramer's rule applied
to the row equation `xA=c` gives

```text
B_y(c)=det A[0<-c]/det A,
(p_c)_a=det A[a<-c]/det A,  1<=a<=r.               (3.1)
```

Therefore the complete directional error is

```text
B_y(c)-c k
=-{sum_(a=1)^r e_a det A[a<-c]}/det A.             (3.2)
```

This is a signed cofactor pairing.  No termwise absolute value is present.
In particular, the small denominator `det A` and the cofactor numerator
must be treated together.

## 4. Maximal-minor formula for the boundary transform

For `0<=j<=r`, let `M_hat_j` be the square matrix obtained by deleting
column `j` from `M`, and put

```text
Delta_j=(-1)^j det M_hat_j.                         (4.1)
```

The vector `Delta=(Delta_0,...,Delta_r)^T` spans `ker M`.  Hence

```text
y_j=Delta_j/sum_l ell_l Delta_l.                    (4.2)
```

For `ell=1^T` and the Cauchy row (1.4),

```text
B_y(z)
=z {sum_j Delta_j/(z-d_j)}/{sum_j Delta_j}.         (4.3)
```

Formula (4.3) is the projective Cauchy transform written entirely in terms
of adjacent maximal minors of the rectangular CCM block.  It remains valid
at a singular square subblock because it uses the full rectangular matrix,
not a selected square inverse.

### Proof of the kernel claim

The `a`-th component of `M Delta` is the Laplace expansion along the first
row of the square matrix obtained by adjoining row `a` of `M` to `M`.
That matrix has two equal rows, so the determinant vanishes.  Since `M` has
rank `r`, at least one maximal minor is nonzero and `Delta` spans its
one-dimensional kernel.  Normalization gives (4.2), and (4.3) follows by
substitution. `QED`

## 5. Rank-one determinant encoding of the paired residual

Let

```text
q_e=(0,e_1,...,e_r)^T.                              (5.1)
```

The matrix determinant lemma and (2.2) give

```text
det(A+q_e c)/det A
=1+c A^(-1)q_e
=1+p_c e.                                          (5.2)
```

Thus

```text
B_y(c)-c k
=1-det(A+q_e c)/det A.                             (5.3)
```

after using the scalar equality (2.3).  More explicitly, the right side of
(5.3) is dimensionless and equals `-p_c e`; the two terms `B_y(c)` and
`c k` retain their original normalization.

Equation (5.2), rather than separate estimates for `det A` and its
cofactors, is the stable determinant coordinate for the residual pairing.

## 6. Covariance under row changes

Let `S` be any invertible `r` by `r` matrix and replace

```text
M by M'=SM,
e by e'=Se.                                         (6.1)
```

The normalized kernel vector `y` is unchanged.  The dual row transforms as

```text
p'_c=p_c S^(-1),                                    (6.2)
```

so

```text
p'_c e'=p_c e.                                      (6.3)
```

The directional residual is therefore intrinsic to the rectangular
equation and the chosen observation.  It does not depend on a row basis or
on preconditioning of the equation space.

## 7. Consequence for IDENT

For the prolate vector `k_N`, write the radical decomposition

```text
e_N=E_(PROLATE,N)+E_(WEIL,N)+E_(FOURIER,N).         (7.1)
```

Then DIRECTIONAL-IDENT is exactly

```text
sup_(z in K)
|p_(N,z)[E_(PROLATE,N)+E_(WEIL,N)+E_(FOURIER,N)]|
/|B_(k_N)(z)| ->0.                                  (7.2)
```

The row `p_(N,z)` may be obtained in either of two inverse-free ways:

```text
adjoint equation: p_(N,z)M_N=c_z-B_(y_N)(z)ell_N;

cofactor formula: (p_(N,z))_a
                  =det A_N[a<-c_z]/det A_N.        (7.3)
```

The first form is suited to displacement identities.  The second form is
suited to exact determinant recombination.  Both retain the signed coupling
which is lost in an ambient norm estimate.

## 8. Status

```text
proved:
  unique dual Green row and its exact adjoint equation;
  cofactor representation of every directional component;
  maximal-minor formula for the normalized boundary transform;
  rank-one determinant encoding of the paired residual;
  invariance under arbitrary equation-row preconditioning;

reduced:
  DIRECTIONAL-IDENT to the scalar pairing (7.2);

open:
  cofinal decay of that scalar pairing for the arithmetic CCM blocks.
```

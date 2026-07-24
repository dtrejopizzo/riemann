# E101.043 - Squared rank-two secular reduction

## 1. One-boundary quotient operator

Let

```text
D=diag(d_1,...,d_m),
y in R^m,
a=1^T y!=0.                                         (1.1)
```

The quotient operator from P76.023 is

```text
D_y=D-(1/a)D y 1^T.                                 (1.2)
```

It satisfies

```text
D_y y=0.                                             (1.3)
```

Its nonzero eigenvalues are the real roots `kappa_j` of the cleared Cauchy
numerator associated with

```text
sum_i y_i/(z-d_i).                                   (1.4)
```

For the canonical right boundary, `y=(x,-1)` and (1.4), up to its fixed
sign, is exactly the transfer `T_N`.

## 2. Squaring lowers the perturbation to rank two

Put

```text
u=Dy/a,
r=1^T u,
p=(D-rI)u,
delta^T=1^T D.                                       (2.1)
```

### Lemma 2.1

```text
D_y^2=D^2-p1^T-u delta^T.                           (2.2)
```

In particular,

```text
rank(D_y^2-D^2)<=2.                                  (2.3)
```

### Proof

Since `D_y=D-u1^T`,

```text
D_y^2
 =D^2-Du1^T-u1^TD+u(1^Tu)1^T
 =D^2-(Du-ru)1^T-u delta^T,                         (2.4)
```

which is (2.2). `QED`

## 3. Two-by-two determinant

For `zeta` outside the squared mesh, set

```text
R_0(zeta)=(zeta I-D^2)^(-1),                         (3.1)
```

and define

```text
M_y(zeta)=
 [1+1^T R_0p       1^T R_0u       ]
 [delta^T R_0p     1+delta^T R_0u ].                (3.2)
```

### Theorem 3.1

```text
det(zeta I-D_y^2)/det(zeta I-D^2)=det M_y(zeta).     (3.3)
```

Moreover,

```text
det M_y(zeta)
 ={zeta prod_j(zeta-kappa_j^2)}
  /{prod_i(zeta-d_i^2)}.                            (3.4)
```

### Proof

By (2.2),

```text
zeta I-D_y^2
 =(zeta I-D^2)+[p,u][1^T;delta^T].                  (3.5)
```

The rank-two matrix determinant lemma gives (3.3).  Equation (1.3) supplies
the zero eigenvalue of `D_y`; its remaining eigenvalues are the `kappa_j`.
Taking determinants through the algebraic spectrum gives (3.4). `QED`

## 4. Bilateral scalar factorization

Define the scale-free one-boundary determinant

```text
B_y(z)
 =det(zI-D_y)/det(zI-D)
 ={z/a}sum_i y_i/(z-d_i).                            (4.1)
```

The matrix determinant lemma proves the second equality.  For either branch
of `sqrt(zeta)`,

```text
det M_y(zeta)
 =B_y(sqrt(zeta))B_y(-sqrt(zeta)).                  (4.2)
```

Thus the rank-two squared determinant is exactly the bilateral product in the
squared variable.  Formula (3.2) expresses it without evaluating either
branch and without a large determinant.

## 5. Resolvent and heat formulas

Logarithmic differentiation of (3.3) gives

```text
partial_zeta log det M_y(zeta)
 =Tr(zeta I-D_y^2)^(-1)-Tr(zeta I-D^2)^(-1).        (5.1)
```

At a safe point `x>0`, the core Stieltjes transform is therefore

```text
g_(L,N)(x)
 =Tr(D^2+xI)^(-1)-1/x
  -[partial_zeta log det M_y(zeta)]_(zeta=-x).       (5.2)
```

The subtraction `1/x` removes the forced zero eigenvalue in (1.3).

For a contour enclosing the two finite squared spectra,

```text
H_(L,N)(v)-Tr exp(-vD^2)
 ={1/(2pi i)}integral_Gamma
   exp(-v zeta)partial_zeta log det M_y(zeta)d zeta
  -1.                                                (5.3)
```

Thus both the Stieltjes and heat defects are determined by four scalar Cauchy
sums involving the boundary null vector `y`.

## 6. Numerical algebra check

For a nonsymmetric four-node example with a generic real vector `y`, direct
evaluation at a nonreal `zeta` gave

```text
|det M_y
 -det(zeta I-D_y^2)/det(zeta I-D^2)|
 =3.24e-16.                                          (6.1)
```

A centered finite-difference check of (5.1) had residual `2.82e-10`, while

```text
rank(D_y^2-D^2)=2,
||D_y y||=9.42e-16.                                  (6.2)
```

These checks use no symmetry and verify the signs in (2.2) and (3.2).

## 7. Consequence for the open comparison

`GAUSSIAN-WEIL-QUADRATURE` can now be attacked through

```text
det M_y(zeta)                                        (7.1)
```

rather than through all secular roots or the ill-conditioned rank-one matrix
`K_N`.  The remaining input is the arithmetic asymptotic of the four scalar
sums in (3.2), with `y` the canonical Gamma-prime boundary null vector.

This is not yet an identification theorem: replacing `y` by an arbitrary
kernel vector preserves the algebra but does not select the zeta limit.

## 8. Status

```text
proved:
  rank-two formula for the squared quotient operator;
  exact two-by-two determinant factorization;
  equality with the bilateral scalar product;
  root-free Stieltjes and heat formulas;

open:
  arithmetic asymptotics of the four boundary-vector Cauchy sums.
```

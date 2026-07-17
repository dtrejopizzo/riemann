# P76.023 - General displacement real-rootedness theorem

## Context

Connes--van Suijlekom prove real-rootedness for positive matrices of divided-
difference type with an even kernel (Proposition 5.10 of
`arXiv:2511.23257`).  The boundary Schur completion is one-sided, so its
kernel need not be even.  The same quotient argument extends to this case
provided the kernel vector has nonzero sum.

## Theorem

Let

```text
D=diag(d_1,...,d_m)
```

have distinct real entries.  Let `Q` be a real symmetric positive
semidefinite matrix of rank `m-1`, with `ker Q=span{xi}`, and suppose

```text
[D,Q]=beta 1^T-1 beta^T.                       (DR-1)
```

Assume

```text
a=1^T xi !=0.
```

Then the Cauchy numerator

```text
P_xi(z)=prod_j(z-d_j) sum_j xi_j/(z-d_j)
```

has only real zeros.

## Proof

Put

```text
b=beta^T xi.
```

Applying `(DR-1)` to `xi` and using `Qxi=0` gives

```text
-Q D xi=a beta-b 1,
Q D xi=-a beta+b 1.                            (DR-2)
```

Define

```text
D'=D-(1/a)D xi 1^T.                            (DR-3)
```

Using `(DR-2)`,

```text
Q D'
=Q D-(1/a)Q D xi 1^T
=D Q+1 beta^T-(b/a)1 1^T.
```

On the other hand, transposing `(DR-2)` gives

```text
xi^T D Q=-a beta^T+b 1^T,
```

and therefore

```text
D'^T Q
=D Q-(1/a)1 xi^T D Q
=D Q+1 beta^T-(b/a)1 1^T
=Q D'.                                         (DR-4)
```

Thus `D'` is selfadjoint for the positive inner product induced by `Q` on
the separated quotient `R^m/ker Q`.  Its quotient spectrum is real.
Moreover `D'xi=0`, so the full characteristic polynomial has zero plus the
real quotient eigenvalues.

The matrix determinant lemma gives, away from the mesh,

```text
det(D'-zI)
=det(D-zI)
 [1-(1/a)1^T(D-zI)^(-1)Dxi]

=(z/a)det(D-zI) sum_j xi_j/(z-d_j),             (DR-5)
```

up to the harmless global sign fixed by the ordering convention.  Therefore
the nonzero roots of `det(D'-zI)` are precisely the roots of `P_xi`.  They
are all real.  A possible root at zero is real as well.  QED.

## Application to the boundary characteristic

For either canonical one-boundary completion of P76.016-P76.017,

```text
Q_b=K_b^can-mu_N I>=0,
ker Q_b=span{y_b},
rank Q_b=m-1.
```

The diagonal-Loewner identity is unchanged by the canonical boundary
diagonal, hence

```text
[D,Q_b]=-(2/L)(s1^T-1s^T),
```

which has the form `(DR-1)`.  When `1^T y_b !=0`, the theorem applies and
the cleared numerator of

```text
T_b(z)=-r_z y_b
```

has only real zeros.  Multiplication by `sin(zL/2)` cancels the poles on the
finite mesh and contributes only real mesh zeros outside that pole set.
Consequently the entire boundary characteristic

```text
Phi_{L,N}(z)
=sin(zL/2)T_+(z)/Phi_{L,N}(0)
```

is real-rooted at every finite cutoff.

If `1^T y_b=0` occurs at an isolated parameter, the statement follows by a
nondegenerate perturbation and continuity of polynomial roots, provided the
kernel remains simple.  Alternatively it may be retained as an explicit
nondegeneracy hypothesis in the closure theorem.

## Consequence

Finite real-rootedness of `Phi_{L,N}` is now proved from:

```text
strict interlacing,
the exact Schur completion,
the rank-two Loewner displacement identity.
```

It does not require global Weil positivity, an even kernel, or numerical
root matching.  The remaining burden is analytic identification of the
locally uniform limit with `Xi`.

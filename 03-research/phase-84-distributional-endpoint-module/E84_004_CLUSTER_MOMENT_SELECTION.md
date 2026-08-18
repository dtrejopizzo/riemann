# E84.004 - Cluster moment selection

## 1. Moment map on a spectral cluster

Let `P` be an orthogonal spectral projection and define

```text
B:P ran -> R^2,
Bg=(1^Tg,s^Tg).                                       (1.1)
```

The required moment vector is

```text
m=(-L alpha/2,L beta/2)^T.                            (1.2)
```

### Theorem 1.1

A vector `g in ran P` satisfying the source moments exists if and only if

```text
m in ran B.                                           (1.3)
```

If the two-by-two Gram matrix

```text
G_B=B B^T
 =[[1^T P1,1^T Ps],
   [s^T P1,s^T Ps]]                                   (1.4)
```

is invertible, the unique solution of smallest norm is

```text
g_*=P[1 s]G_B^(-1)m.                                  (1.5)
```

### Proof

The existence statement is the definition of the range.  When `G_B` is
invertible, direct substitution gives `Bg_*=m`.  Every other solution is
`g_*+h` with `h in ker B`.  Formula (1.5) lies in `(ker B)^perp`, so the
Pythagorean identity proves minimality and uniqueness. `QED`

Only a two-by-two inverse appears.  It is a moment nondegeneracy condition,
not the collapsing CCM complement inverse.

## 2. Rank-one cluster

If `ran P=span{xi}` and neither required moment is singular, existence reduces
to

```text
s^T xi/(1^T xi)=-beta/alpha.                           (2.1)
```

Equivalently,

```text
xi^T f=alpha s^Txi+beta 1^Txi=0.                      (2.2)
```

For an exact null vector `Mxi=0`, condition (2.2) follows from `f=Mh` by
self-adjointness.  For a merely small eigenvalue it is an additional
quantitative compatibility, not an algebraic identity.

## 3. Cluster leakage bound before reduction

Suppose the spectrum of `M` on `ran P` lies in `[-eta,eta]`.  Then the
minimal moment vector satisfies

```text
norm(Mg_*)<=eta norm(g_*),                              (3.1)

norm(g_*)^2=m^T G_B^(-1)m.                             (3.2)
```

Hence the unreduced source error obeys

```text
norm(e)<=norm(QD P) eta sqrt(m^T G_B^(-1)m).           (3.3)
```

The estimate is useful only before applying `C^(-1)`.  It does not imply the
safe reduced estimate when the complement response diverges.

## 4. Exact identification of the surviving scalar

Substitution of (1.5) into E84.003 gives

```text
ell_z(C^(-1)e)
 =ell_z(C^(-1)QD M P[1 s]G_B^(-1)m).                  (4.1)
```

This is a finite, completely explicit scalar.  Its ingredients are:

```text
the cluster projection P;
the two moment Gram matrix G_B;
the spectral residual MP;
one D-commutator crossing from P to Q;
the safe complement response.                         (4.2)
```

Equation (4.1) is exactly the Weyl-reduced leakage structure isolated in the
earlier prolate route.  The distributional construction therefore closes the
missing corrector, but it does not remove the reduced leakage theorem.

## 5. Status

```text
proved:
  necessary and sufficient cluster moment condition;
  explicit minimal cluster vector;
  exact pre-response leakage bound;
  explicit scalar reduced error;

closed:
  moment selection whenever G_B is nonsingular;
  the distributional endpoint route as an independent escape from WRL;

open:
  quantitative nondegeneracy of G_B in the chosen cluster;
  safe annihilation of the scalar (4.1).
```


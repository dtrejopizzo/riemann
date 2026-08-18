# E101.032 - Integer heat compactification

## 1. Heat lift of the core resolvent

Fix an integer `n_0>=1`.  For a finite core secular measure

```text
mu_alpha=sum_j delta_(r_(alpha,j)^2),                (1.1)
```

define its heat trace by

```text
H_alpha(v)
 =integral_[0,infinity) exp(-tv)d mu_alpha(t)
 =sum_j exp(-r_(alpha,j)^2v),
v>0.                                                 (1.2)
```

The Stieltjes transform has the exact Laplace representation

```text
g_alpha(x)
 =integral_0^infinity exp(-xv)H_alpha(v)dv,
x>0.                                                 (1.3)
```

Indeed, Tonelli's theorem and

```text
1/(x+t)=integral_0^infinity exp(-(x+t)v)dv           (1.4)
```

give (1.3).  If `K_alpha` is the finite secular pencil, then

```text
H_alpha(v)=Tr exp(-vK_alpha^2).                      (1.5)
```

The trace identity uses only the algebraic spectrum and remains independent
of eigenvectors.

## 2. Integer values are Hausdorff moments

Put `y=exp(-v)`.  Equation (1.3) gives

```text
g_alpha(n_0+k)
 =integral_0^1 y^k d lambda_alpha(y),
k>=0,                                                (2.1)

d lambda_alpha(y)
 =y^(n_0-1)H_alpha(-log y)dy.                        (2.2)
```

Thus the complete integer sample sequence is the Hausdorff moment sequence
of one finite positive measure on `[0,1]`.  Its total mass is

```text
lambda_alpha([0,1])=g_alpha(n_0).                    (2.3)
```

The generating function is consequently

```text
G_alpha(q)
 =sum_(k>=0)q^k g_alpha(n_0+k)
 =integral_[0,1] d lambda_alpha(y)/(1-qy),
|q|<1.                                               (2.4)
```

## 3. Beta-mixture compactification

The measure in (2.2) retains more structure than an arbitrary Hausdorff
measure.  Define

```text
d nu_alpha(t)=d mu_alpha(t)/(n_0+t).                 (3.1)
```

For finite `t>=0`, let

```text
d beta_t(y)=(n_0+t)y^(n_0+t-1)dy,
0<y<1,                                               (3.2)
```

and put

```text
beta_infinity=delta_1.                               (3.3)
```

Each `beta_t` is a probability measure.  Moreover,

```text
lambda_alpha
 =integral_[0,infinity] beta_t d nu_alpha(t),        (3.4)

integral_[0,1]y^k d beta_t(y)
 =(n_0+t)/(n_0+t+k).                                 (3.5)
```

The map `t->beta_t` extends weakly and continuously to the one-point
compactification by (3.3).  In fact, for every continuous `phi` on `[0,1]`,
the beta densities in (3.2) concentrate at `y=1` as `t->infinity`.

If `nu_alpha` converges weakly on `[0,infinity]` to `nu`, then

```text
g(z)
 =integral_[0,infinity]
    (n_0+t)/(z+t)d nu(t),                            (3.6)
```

where the integrand at `t=infinity` is `1`.  Hence

```text
nu({infinity})
```

is exactly the constant Stieltjes term caused by spectral mass escaping to
infinity.  On the Hausdorff side it is the atom of `lambda` at `y=1`.

## 4. Integer closure in compact coordinates

### Theorem 4.1

Assume, along one directed family,

```text
g_alpha(n_0+k)->g_Xi(n_0+k)
for every k>=0.                                      (4.1)
```

Then the measures `nu_alpha` have a unique weak limit on `[0,infinity]`, its
mass at infinity is zero, and `Omega7` holds.

### Proof

The case `k=0` bounds the total masses of `nu_alpha` by (2.3), so weak
compactness applies.  Every sublimit `nu` gives the bounded analytic
Stieltjes function (3.6).  By (3.5) and (4.1), it agrees with `g_Xi` at every
integer `n_0+k`.  The half-plane uniqueness theorem E101.031 makes this
analytic function equal to `g_Xi` in the absolute half-plane.

Two sublimits therefore have the same Stieltjes transform, so uniqueness of
that transform makes the sublimits equal.  Finally,

```text
nu({infinity})
 =lim_(k->infinity)g_Xi(n_0+k)=0,                   (4.2)
```

where the first equality follows from dominated convergence in (3.6), and
the second from the arithmetic asymptotic of E101.021.  Thus `g_Xi` has a
positive Stieltjes representation without a constant term.  E101.021 gives
`Omega7`. `QED`

## 5. Status

```text
proved:
  exact heat-trace lift of the core Stieltjes transform;
  integer samples as one compact Hausdorff moment problem;
  beta-mixture compactification of the Stieltjes cone;
  identification of escape mass with the endpoint atom at y=1;
  integer closure in compact measure coordinates.
```

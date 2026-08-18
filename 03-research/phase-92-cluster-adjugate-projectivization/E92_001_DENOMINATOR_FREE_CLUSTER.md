# E92.001 - Denominator-free cluster numerator

## 1. Exact Feshbach data

Use

```text
G_t(z)
 =G_(t,z)^reg-h_(t,z)^eff F_t^(-1)b_t^eff           (1.1)
```

from E88.001.  Let the cluster dimension be `r` and define

```text
N_t(z)
 =G_(t,z)^reg det F_t
  -h_(t,z)^eff adj(F_t)b_t^eff.                       (1.2)
```

### Theorem 1.1

If `F_t` is invertible, then

```text
G_t(z)=N_t(z)/det F_t.                                (1.3)
```

### Proof

Use

```text
F_t^(-1)=adj(F_t)/det F_t
```

in (1.1) and place the two terms over the common denominator. `QED`

## 2. Extension through a singular cluster

The maps `det` and `adj` are polynomials in the entries of `F_t`.  Therefore,
if the regular Feshbach data are continuous or holomorphic in a parameter,
then `N_t(z)` has the same regularity even at `det F_t=0`.

No eigenvalue labeling, simplicity hypothesis or spectral gap inside the
cluster is needed to define (1.2).

## 3. Bordered determinant interpretation

The numerator is itself a determinant:

```text
N_t(z)
 =det[[F_t,             b_t^eff],
      [h_(t,z)^eff, G_(t,z)^reg]].                    (3.1)
```

The sign follows from the Schur determinant formula.  Equation (3.1) remains
valid when `F_t` is singular because both sides are polynomial identities.

## 4. Status

```text
proved:
  exact denominator-free cluster numerator;
  polynomial continuation through cluster singularities;
  bordered determinant formula;

open:
  projective convergence and arithmetic identification of N_t.
```


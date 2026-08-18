# E92.002 - Projective continuation through the endpoint

## 1. Exact normalized ratio

Fix a safe base point `z_*`.  Where `F_t` is invertible and both base values
are nonzero, E92.001 gives

```text
G_t(z)/G_t(z_*)=N_t(z)/N_t(z_*).                     (1.1)
```

The factor `det F_t` cancels exactly.  Since the right side is defined by the
polynomial numerator, it provides the projective continuation through every
cluster singularity at which `N_t(z_*)` remains nonzero.

## 2. Bilateral ratio

Put `u=s-1/2` and choose a safe base point `s_*`.  Then

```text
[G_t(iu)G_t(-iu)]
/[G_t(iu_*)G_t(-iu_*)]

 =[N_t(iu)N_t(-iu)]
  /[N_t(iu_*)N_t(-iu_*)].                            (2.1)
```

The cancellation is exact and uses the same cluster determinant in all four
factors.

## 3. Endpoint quotient without path regularity

For any two parameter values `t_0,t_1` for which the four numerator base
values are nonzero,

```text
Q_(t_1)(s;s_*)/Q_(t_0)(s;s_*)
 =B_(t_1)(s;s_*)/B_(t_0)(s;s_*),                     (3.1)
```

where

```text
Q_t(s;s_*)
 =[G_t(iu)G_t(-iu)]/[G_t(iu_*)G_t(-iu_*)],           (3.2)

B_t(s;s_*)
 =[N_t(iu)N_t(-iu)]/[N_t(iu_*)N_t(-iu_*)].           (3.3)
```

Thus an endpoint scattering quotient can be computed from endpoint numerator
values without selecting a simple branch along the path.  Zeros encountered
inside the path affect a logarithmic integral representation, but not the
algebraic quotient (3.1).

## 4. Consequence

One-line dominance is sufficient for reducing `N_t` to one rank-one term,
but it is not necessary for projective continuation.  The complete cluster
numerator is the canonical object.

## 5. Status

```text
proved:
  exact projective cancellation of det F_t;
  bilateral continuation through cluster singularities;
  endpoint quotient independent of eigenline tracking;

remaining nonvanishing:
  one numerator base value, or a finite atlas of safe base points.
```


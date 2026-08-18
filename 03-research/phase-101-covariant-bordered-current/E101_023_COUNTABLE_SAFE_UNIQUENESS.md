# E101.023 - Countable safe uniqueness theorem

## 1. Determining sequence

Let

```text
x_k>1/4,
x_k->x_0>1/4,                                        (1.1)
```

with all `x_k` distinct.  Let `g_alpha` be the positive finite Stieltjes
transforms of E101.020.

### Theorem 1.1

Assume, along one directed family,

```text
g_alpha(x_0)->g_Xi(x_0),                             (1.2)

g_alpha(x_k)->g_Xi(x_k) for every k.                 (1.3)
```

Then `Omega7` holds.

### Proof

Equation (1.2) bounds

```text
g_alpha(x_0)
 =integral d mu_alpha(t)/(t+x_0).                    (1.4)
```

For every compact subset `K` of the slit plane, there is a constant `C_K`
such that

```text
1/|t+z|<=C_K/(t+x_0),
t>=0,
z in K.                                              (1.5)
```

Hence (1.4) makes the family `g_alpha` locally bounded on the slit plane.
Every subnet has an analytic sublimit.  By (1.3), that sublimit agrees with
`g_Xi` on a set having the interior accumulation point `x_0`.  The identity
theorem makes the sublimit unique.

For completeness, put

```text
d nu_alpha(t)=d mu_alpha(t)/(t+x_0).                 (1.6)
```

Equation (1.4) bounds the total masses of `nu_alpha`.  On the compactification
of `[0,infinity)`, a subnet converges weakly to a positive measure.  Since

```text
g_alpha(z)=integral (t+x_0)/(t+z)d nu_alpha(t),       (1.7)
```

mass at infinity becomes a nonnegative constant and finite mass becomes a
positive Stieltjes integral.  Thus `g_Xi` belongs to the Stieltjes class.
Its arithmetic asymptotic makes the constant zero.  E101.021 gives `Omega7`.
`QED`

## 2. Cofactor corollary

By E101.022 and the independent convergence `g_(E,L)->g_Xi`, it is sufficient
to prove

```text
D_(L_alpha,N_alpha)(1/2+sqrt(x_0))->0,               (2.1)

D_(L_alpha,N_alpha)(1/2+sqrt(x_k))->0
for every k                                          (2.2)
```

along one directed family.

This is `COUNTABLE-COFACTOR-IDENT`.  It implies `Omega7` without uniform
control on an interval.

## 3. Cofinal diagonal

If, for every finite initial set `{x_0,x_1,...,x_m}` and every tolerance,
there exists a resolved cutoff beyond which (2.1)--(2.2) hold simultaneously,
the standard directed diagonal produces one family satisfying all countably
many conditions.  This selection is purely topological; the force-bearing
content is the finite-set cofactor identification.

## 4. Moment version

An equivalent determining family at the single point `x_0` is

```text
g_alpha^(k)(x_0)->g_Xi^(k)(x_0)
for every k>=0.                                      (4.1)
```

By E101.020, these are the convergence statements for the complete safe
Stieltjes moment hierarchy.

## 5. Status

```text
proved:
  countable safe uniqueness theorem;
  cofactor determining-sequence reduction;
  one-point moment-hierarchy equivalent;

open:
  COUNTABLE-COFACTOR-IDENT, equivalently the Stieltjes discriminant and
  Omega7.
```

# E96.003 - Bilateral determinant response kernel

## 1. One-cell response

On a simple characteristic branch define

```text
R_t(z;y)
 =J_y(P,chi)(t,mu_t,z)
  /[P(t,mu_t,z)partial_mu chi(t,mu_t)].               (1.1)
```

E96.002 and E95.002 give

```text
d/dt log P(t,mu_t,z)
 =-sum_n Lambda(n)n^(-1/2)R_t(z;log n).               (1.2)
```

## 2. Projective bilateral kernel

Put `u=s-1/2` and define

```text
BR_t(s;s_*;y)
 =-[R_t(iu;y)+R_t(-iu;y)
    -R_t(iu_*;y)-R_t(-iu_*;y)].                      (2.1)
```

Then the exact bilateral bordered current is

```text
BJ_t(s;s_*)
 =sum_(2<=n<=exp L)
   Lambda(n)n^(-1/2)BR_t(s;s_*;log n).               (2.2)
```

The base-point subtraction removes every factor independent of the safe
variable.  Formula (2.2) remains one coupled scalar sum.

## 3. No spectral coordinates

The response kernel uses only

```text
cofactors of the bordered matrix;
cofactors of the full characteristic matrix;
one cell direction Q_y;
safe Cauchy rows.                                     (3.1)
```

It uses no spectral decomposition and no zero data.

## 4. Status

```text
proved:
  exact global one-cell response;
  exact bilateral projective von Mangoldt sum.
```


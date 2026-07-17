# E72.201 - Scalar displacement factor audit

## Purpose

E72.200 suggested the possible factorization

```text
C_r(R) = W_r(log R) M_r(R),
```

where `W_r` would be a scalar Green-translation kernel and `M_r` a multiplicative von Mangoldt
correlation. This audit tests that simplification directly.

If the factorization were literally scalar, then after removing the positive weight

```text
prod_i beta_{n_i},       beta_n=Lambda(n)n^(-1/2),
```

the Green trace kernels of words with the same displacement `R=prod n_i^eps_i` should be nearly equal.

## Diagnostic

Script:

```text
E72_201_scalar_displacement_factor_probe.py
```

It groups high-block cubic signed Green-words by `R`, strips the `prod beta_n` weight, and reports the
relative spread of the remaining Green kernels inside each class.

Output:

```text
E72.201 scalar displacement factor test
tests whether same-R words share one scalar Green kernel
lam rank logR key words classSum wKernel relSpread absSpread
-- lambda=6
  6    1   -2.944 1/19    69 -1.008329e-02 +7.642194e-04 7.533e-01 1.595e-03
  6    2   +2.944 19/1    69 -1.008329e-02 +7.642194e-04 7.533e-01 1.595e-03
  6    3   +2.398 11/1    69 +9.367756e-03 -6.701876e-04 9.142e-01 1.901e-03
-- lambda=8
  8    1   +3.970 53/1   111 -4.971568e-03 +3.068015e-04 4.800e-01 4.717e-04
  8    2   -3.970 1/53   111 -4.971568e-03 +3.068015e-04 4.800e-01 4.717e-04
  8    3   +2.944 19/1   111 +4.821259e-03 -2.441218e-04 1.057e+00 7.631e-04
-- lambda=10
 10    1   +2.833 17/1   153 +3.362661e-03 -1.344834e-04 7.446e-01 4.054e-04
 10    2   -2.833 1/17   153 +3.362661e-03 -1.344834e-04 7.446e-01 4.054e-04
 10    3   +4.419 83/1   153 -2.503687e-03 +1.391393e-04 2.630e-01 1.885e-04
```

## Reading

The scalar factorization is too strong. The relative spread inside a fixed displacement class is often
`0.5--1.2`, so words with the same `R` are not governed by a single scalar kernel.

What survives is the weighted class identity:

```text
C_r(R)
 =
(-1)^r
sum_{prod n_i^eps_i=R}
  (prod_i beta_{n_i})
  W_x(eps_1n_1,...,eps_rn_r),
```

where

```text
W_x(eps_1n_1,...,eps_rn_r)
 =
Tr(U_{eps_1,y_1}^{rel}...U_{eps_r,y_r}^{rel})
```

with the exact model Green whitening included in each relative signed cell.

Thus the correct object is not a scalar displacement kernel. It is an operator-valued multiplicative
group-algebra coefficient.

## Consequence

The next exact theorem should be formulated in the group algebra of the multiplicative displacement
lattice:

```text
sum_n A_n^+ delta_n + A_n^- delta_{n^{-1}}.
```

The coefficient at `R` is exactly the signed Green-word class `C_r(R)`. The fixed certificate is an
augmentation/sign inequality for finitely many powers of this group-algebra element.

This is sharper than E72.200 and avoids a false scalar-kernel closure.

# P76.048 - Shell cocycle target

For fixed `L` and spectral parameter `mu=0`, write the nested CCM sections

```text
H_N=
[[C_- , B_-^T, E],
 [B_- , H_{N-1}, B_+],
 [E   , B_+^T, C_+]].
```

Eliminating `H_{N-1}` produces the exact two-by-two shell Schur complement

```text
Sigma_N=C_N-B_N^T H_{N-1}^(-1)B_N.              (SC-1)
```

The Cauchy boundary-transfer row at the same level is

```text
T_N(z)=r_z^bd-r_z^in H_{N-1}^(-1)B_N.           (SC-2)
```

Equations `(SC-1)`--`(SC-2)` form a rank-two linear-fractional update when
the next shell is added.  Centrosymmetry reduces the bilateral logarithmic
observable to the product of the reflected scalar components.

The theorem target is to write that update explicitly as

```text
T_{N+1,+}(z;0)/T_{N,+}(z;0)
=1+Delta_{L,N}(z),                               (SC-3)
```

with `Delta` expressed through `Sigma_N` and the two new Cauchy boundary
values, and prove on `z=i sigma`, `sigma` in compact safe intervals,

```text
|partial_sigma log[(1+Delta(i sigma))(1+Delta(-i sigma))]
  -Delta B_ext,N(sigma)|
 <=C_K L^2/N^2.                                  (SC-4)
```

Summing `(SC-4)` proves `SHELL-LOG`.  The subtraction of
`Delta B_ext` must remain coupled; P76.037 shows that its separate size is
load-bearing.

This is the next exact finite calculation.  It uses nested zero-level
sections and no eigenvector, fitted normalization, zero list or global
Loewner remainder.

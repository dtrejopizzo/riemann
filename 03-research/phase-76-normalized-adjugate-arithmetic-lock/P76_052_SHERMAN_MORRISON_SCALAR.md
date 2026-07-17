# P76.052 - Sherman--Morrison scalar endpoint

Fix the safe reference `z_0=i sigma_0`.  The bordered matrices of P76.051
differ only in their last Cauchy row:

```text
B(z)=B(z_0)+e_last delta r(z)^T.                 (SM-1)
```

Put `G=B(z_0)^(-1)` and

```text
den(z)=1+delta r(z)^T G e_last.                 (SM-2)
```

Sherman--Morrison gives

```text
B(z)^(-1)=G-[G e_last][delta r(z)^T G]/den(z).  (SM-3)
```

Restricting to the deleted-column/deleted-row `2x2` minor gives

```text
R(z)=R_0-a(z)b(z)^T/den(z),                     (SM-4)

a=(G e_last)_{deleted columns},
b^T=(delta r^T G)_{deleted rows}.
```

The `2x2` determinant lemma yields

```text
det R(z)/det R_0=1-theta_N(z),                  (SM-5)

theta_N(z)=b^T R_0^(-1)a/den(z).                (SM-6)
```

Combining with P76.051,

```text
[T_{N+1}(z)/T_N(z)]/[T_{N+1}(z_0)/T_N(z_0)]
=1/[1-theta_N(z)].                              (SM-7)
```

Thus the full finite-section theorem is reduced to one directional scalar:

```text
SM-SHELL:
sup_{z=i sigma, sigma in K}|theta_N(z)|
 <=C_K L^2/N^2.                                  (SM-8)
```

This is not an ambient inverse estimate.  The low-frequency pieces of
`delta r` must be paired with the selected inverse columns before taking
absolute values.

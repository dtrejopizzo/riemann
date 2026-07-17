# P76.051 - Jacobi minor form of the safe shell increment

Let `B_{N+1}(z)` be the bordered matrix for the right boundary `+(N+1)`:

```text
B_{N+1}(z)=
[[H_N,              b_{N+1}],
 [r_z|_{[-N,N]}, 1/(z-d_{N+1})]].               (JM-1)
```

Its determinant is the cleared right transfer numerator `P_{N+1}(z)` up to
a fixed sign and the factor `det H_N` already accounted for in the transfer.

Delete from `(JM-1)` the top rows indexed by `-N,+N` and the columns indexed
by `-N,+(N+1)`.  The retained square matrix is exactly the bordered matrix
for `P_N(z)`: the retained `+N` column becomes its boundary column.

Jacobi's complementary-minor identity therefore gives

```text
P_N(z)/P_{N+1}(z)=epsilon_N det R_N(z),          (JM-2)
```

where `epsilon_N` is independent of `z` and

```text
R_N(z)
 =[B_{N+1}(z)^(-1)]_{deleted columns,deleted rows}
```

is only `2x2`.

All `det H` factors and `epsilon_N` cancel between two safe points.  Hence
the exact shell cross ratio is

```text
[T_{N+1}(z)/T_N(z)]/[T_{N+1}(z_0)/T_N(z_0)]
=det R_N(z_0)/det R_N(z).                       (JM-3)
```

The bilateral increment is the squared modulus of `(JM-3)` on
`z=i sigma`, `z_0=i sigma_0`.

Thus `SHELL-LOG` is reduced from growing ambient determinants and unstable
Schur terms to a normalized `2x2` determinant:

```text
JACOBI-2x2:
sup_{sigma in K}
|det R_N(i sigma_0)/det R_N(i sigma)-1|
 <=C_K L^2/N^2.                                  (JM-4)
```

This estimate is the current finite-section endpoint.

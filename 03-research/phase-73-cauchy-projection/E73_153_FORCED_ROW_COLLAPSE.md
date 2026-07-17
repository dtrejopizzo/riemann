# E73.153 - Forced row collapse

Date: 2026-07-12.

## 1. Purpose

E73.149--E73.152 treated the signed forced Mellin row

```text
[r_{w,1};r_{w,2}]
=M_L(w)^(-1)[P_{z_1,w}^{signed};P_{z_2,w}^{signed}]
```

as a potentially sharper rowspace object.  This note records the exact
algebraic collapse:

```text
r_{w,1}(n)=1/(w+i d_n),
r_{w,2}(n)=1/(-w+i d_n).
```

Thus the complete signed forced row is not a new row.  It is exactly the
Cauchy divisor row.

This is a useful correction.  It prevents the program from treating the
two-row inversion as a source of extra cancellation.

## 2. Coordinate identity

Let

```text
q_w(n):=1/(w+i d_n),
q_-w(n):=1/(-w+i d_n).
```

E73.075 proves that for every vector `xi`,

```text
sum_n P_{z,w}^{signed}(n) xi_n
=A_L(z,w) sum_n q_w(n)xi_n
 +B_L(z,w) sum_n q_-w(n)xi_n.                 (1)
```

Since (1) holds for arbitrary `xi`, apply it to the coordinate vector
`e_n`.  Then for each coordinate,

```text
P_{z,w}^{signed}(n)
=A_L(z,w)q_w(n)+B_L(z,w)q_-w(n).              (2)
```

For two admissible rows `z_1,z_2`, equation (2) becomes

```text
[ P_{z_1,w}^{signed}(n) ]
[ P_{z_2,w}^{signed}(n) ]

=
M_L(w)
[ q_w(n)  ]
[ q_-w(n) ].
```

If `M_L(w)` is invertible, then

```text
[ r_{w,1}(n) ]
[ r_{w,2}(n) ]

=
M_L(w)^(-1)
[ P_{z_1,w}^{signed}(n) ]
[ P_{z_2,w}^{signed}(n) ]

=
[ q_w(n)  ]
[ q_-w(n) ].
```

This proves the forced row collapse.

## 3. Consequence for the alpha target

The spectral-cutoff coefficient from E73.152 is therefore

```text
alpha_{w,1}=r_{w,1}xi_L=sum_n xi_L(n)/(w+i d_n)=H_0(w),
alpha_{w,2}=r_{w,2}xi_L=sum_n xi_L(n)/(-w+i d_n)=H_0(-w).
```

So

```text
SFRL-CUT_17
```

is exactly

```text
ROW-KER_17 / LDIV_17:
|H_0(w)|+|H_0(-w)| <= C L^-17.
```

The two-row matrix `M_L(w)` is useful as an algebraic decoder of the pair
identity, but it cannot improve the exponent.  Changing `z_1,z_2` only
changes a representation of the same Cauchy row.

## 4. Anti-no-go reading

This does not invalidate E73.075.  Exact pair divisibility remains important:
it proves that the complete Mellin packet belongs to the Cauchy divisor
ideal.

But it does invalidate the hope that the complete signed two-row forcing
creates a new cancellation mechanism beyond the Cauchy divisor itself.

The remaining theorem is therefore not a rowspace theorem about a new row.
It is the direct analytic estimate:

```text
H0-DIV_17:
for every critical standard-box node w=-i gamma,
|sum_n xi_L(n)/(w+i d_n)| + |sum_n xi_L(n)/(-w+i d_n)| <= C L^-17.
```

Together with the already established reduction chain,

```text
H0-DIV_17
=> LDIV_17
=> CSV_17
=> Uniform GATE-73
=> scalar WRL
=> Omega_7.
```

## 5. What remains nontrivial

The nontrivial object is now the eigenvector `xi_L`.  The proof must use the
finite Feshbach/CCM eigenline equation

```text
H_L xi_L=mu_L xi_L
```

and the explicit arithmetic construction of `H_L` to show that the Cauchy
transform of `xi_L` is small at the critical divisor nodes.

The following routes are now ruled out for this endpoint:

```text
1. two-row decoder optimization;
2. full pseudoinverse reconstruction;
3. spectral-cutoff rowspace proximity for the decoded complete row;
4. adjugate/cofactor membership without a direct bound on H_0(w).
```

Thus the next analytic frontier is:

```text
derive H0-DIV_17 directly from the eigenline equation plus the signed
finite Feshbach structure.
```

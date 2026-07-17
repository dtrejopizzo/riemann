# P75.003 - Bordered determinant identity

## Diagonal bordered determinant

The finite numerator has the exact determinant representation

```text
P(z)=-det B(z),
B(z)= [[diag(z-d_n), xi],
       [1^T,          0 ]].
```

Indeed,

```text
det B(z)=det diag(z-d) * ( -1^T diag(z-d)^(-1) xi )
        = -D(z) C(z)
        = -P(z).
```

This identity is exact for zeta, planted, Davenport-Heilbronn, and random
controls.  It does not itself encode divisibility; it only canonicalizes the
finite numerator.

## Removing the explicit eigenvector

Let `A=H-mu I` and assume `mu` is a simple eigenvalue with normalized real
eigenvector `xi`.  Since `A` has rank `N-1`,

```text
adj(A)=k xi xi^T,     k=tr adj(A).
```

For the Cauchy row `r_z(n)=1/(z-d_n)`,

```text
|C(z)|^2 = r_z^* xi xi^T r_z
         = r_z^* adj(A) r_z / tr adj(A).
```

Equivalently,

```text
|P(z)|^2 = |D(z)|^2 r_z^* adj(H-mu I) r_z / tr adj(H-mu I).
```

This is the strongest P75.003 bridge: the nodal numerator can be written from
`H`, `mu`, and the fixed Cauchy border without choosing a phase for `xi`.

## Consequence for ARITH-LOCK

Any proof of `ARITH-LOCK` through this route must prove that the adjugate
minor

```text
r_gamma^* adj(H_L-mu_L I) r_gamma
```

has a critical Xi divisor, or has a signed Euler/Gamma expansion whose
remainder is `O_M(L^-M)`.  The identity remains exact for falsifiers; only the
divisibility is supposed to discriminate zeta from planted/DH/random controls.


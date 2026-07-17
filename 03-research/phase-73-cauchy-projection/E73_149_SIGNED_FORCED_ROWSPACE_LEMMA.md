# E73.149 - Signed Forced Rowspace Lemma

Date: 2026-07-12.

## 1. Setup

Let

```text
E_L = H_L - mu_L I,
E_L xi_L = 0,
||xi_L||=1.
```

For a critical divisor node `w`, choose two admissible rows `z_1,z_2` and
form

```text
M_L(w)=
 [ A_L(z_1,w)  B_L(z_1,w) ]
 [ A_L(z_2,w)  B_L(z_2,w) ].
```

Let

```text
P_{z,w}^{signed}(n):=p_infty(z,w;n)
```

be the complete signed row, i.e. active finite packet plus inactive mesh
tail:

```text
p_infty = p_active + (p_infty-p_active).
```

Define the forced rows

```text
[ r_{w,1} ]
[ r_{w,2} ]

:=
M_L(w)^(-1)
[
 P_{z_1,w}^{signed}
 P_{z_2,w}^{signed}
].
```

## 2. Algebraic identity

By exact pair divisibility,

```text
r_{w,1} xi_L = H_0(w),
r_{w,2} xi_L = H_0(-w),
```

up to the ordering fixed by `M_L(w)`.

Therefore

```text
|r_{w,1}xi_L|+|r_{w,2}xi_L| <= C L^-17
```

is exactly `LDIV_17`.

## 3. Rowspace form

Since `E_L` is Hermitian and has one-dimensional kernel spanned by `xi_L`,

```text
Row(E_L)=xi_L^perp.
```

Thus for any row `r`,

```text
dist(r,Row(E_L)) = |r xi_L|.
```

Consequently, `LDIV_17` is equivalent to:

```text
dist(r_{w,j},Row(E_L)) <= C L^-17,   j=1,2.           (SFRL)
```

This is the Signed Forced Rowspace Lemma.

## 4. Why this is sharper than previous rowspace targets

The old rowspace target tested the raw Cauchy row

```text
k_gamma(n)=1/(-gamma-d_n).
```

The forced row `r_{w,j}` is different.  It is built from the exact Mellin
pair divisor and includes the inactive mesh tail before testing rowspace
distance.

Thus the lemma uses the spectral/Mellin structure, not only the Cauchy
evaluation row.

## 5. Non-circular proof obligation

It is not enough to observe

```text
r_{w,j}xi_L = H_0(+-w)
```

and then import the desired smallness of `H_0`.

The proof must show rowspace proximity directly:

```text
r_{w,j}=y_{w,j}E_L+\alpha_{w,j}xi_L^*,
|alpha_{w,j}|<=C L^-17.
```

Equivalently, it must construct `y_{w,j}` and bound the residual

```text
||r_{w,j}-y_{w,j}E_L|| <= C L^-17
```

in the null direction.

## 6. Finite certificate

For each row, the certificate is explicit:

```text
alpha_{w,j}=r_{w,j}xi_L.
```

A stronger constructive certificate would provide a row multiplier `y_{w,j}`
and verify:

```text
r_{w,j}-y_{w,j}E_L = alpha_{w,j}xi_L^*.
```

This identity is exact in finite dimension once

```text
y_{w,j}=r_{w,j}E_L^+
```

is chosen, where `E_L^+` is the Moore-Penrose inverse on `xi_L^perp`.

Thus the analytic problem is reduced to bounding the scalar coefficient
`alpha_{w,j}` uniformly without using it as an assumption.

## 7. Current status

E73.148 verifies the certificate in the calibrated rows except for the
known transition failures:

```text
lambda=16, gamma=25.01,
lambda=28, gamma=14.13.
```

The uniform theorem still requires:

```text
1. INV_3 for M_L(w),
2. an admissible row-choice rule,
3. SFRL with transition rows absorbed by a finite manifest or removed by
   sharper row selection.
```

The attempted sharper row selection on the `lambda=28, gamma=14.13` row,
using a free grid of row heights rather than only zero ordinates, did not
cross the exponent `17`.  This points to finite-manifest absorption or scale
schedule repair, not merely to better row selection.

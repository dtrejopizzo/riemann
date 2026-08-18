# E77.7m - Pencil compatibility reduction

**Run:** 2026-07-18.

## 1. Purpose

E77.7k--l identified one interface gap inside

```text
BORDERED-WEYL-COMPLETENESS:
the Phase 76 finite projective family is written at mu=0,
while the LP/BTG front lives at the intrinsic fixed-L point mu_L.
```

This note shows that the Phase 76 formulas are not special to `mu=0`.
They extend algebraically to every finite section and every parameter `mu`
for which the inner block is invertible.  Therefore the `mu=0 <-> mu_L`
mismatch reduces to a directional transfer theorem in `mu`, plus treatment
of the singular sections.

## 2. General-mu finite projective scalar

For a centered section, let

```text
A_N(mu)=H_{L,N}^{inner}-mu I,
b_N = H_{L,N}[I_N,N].
```

Whenever `A_N(mu)` is invertible, define

```text
x_N(mu)=A_N(mu)^(-1)b_N,
T_N(z;mu)=r_z x_N(mu).
```

The bordered matrix is

```text
B_N(z;mu)=
[[A_N(mu), b_N],
 [r_z,     boundary(z)]].                      (M-1)
```

Every block inversion, Jacobi minor identity, and Sherman-Morrison step of
P76.051--P76.054 depends only on `(M-1)`, not on the special value `mu=0`.
Hence the same algebra gives canonical vectors

```text
g_N(mu), w_N(mu)
```

with

```text
r(z_0) g_N(mu) = 1,
r(z_0) w_N(mu) = 0,                            (M-2)
```

and the same normalized scalar identity

```text
theta_N(z;mu)=r(z)w_N(mu)/r(z)g_N(mu).         (M-3)
```

Likewise the complementary-minor formula persists:

```text
[T_{N+1}(z;mu)/T_N(z;mu)] / [T_{N+1}(z_0;mu)/T_N(z_0;mu)]
 = det R_N(z_0;mu) / det R_N(z;mu).            (M-4)
```

So the entire finite projective reduction is a **family in mu**.

## 3. Exact mu-transfer identity

For any `mu,nu` with both inner blocks invertible,

```text
x_N(mu)-x_N(nu)
 = (mu-nu) A_N(mu)^(-1) A_N(nu)^(-1) b_N.      (M-5)
```

Pairing with a safe Cauchy row gives

```text
T_N(z;mu)-T_N(z;nu)
 = (mu-nu) r_z A_N(mu)^(-1) A_N(nu)^(-1) b_N.  (M-6)
```

This is the exact algebraic bridge between the `mu=0` family of Phase 76
and the `mu=mu_L` family required by LP.

No ambient inverse norm appears in `(M-5)`--`(M-6)`.  The missing estimate is
entirely directional.

## 4. Reduction of the pencil mismatch

Because `(M-3)` and `(M-4)` hold for every nonsingular `mu`, the
`mu=0 <-> mu_L` compatibility problem is reduced to:

```text
PENCIL-TRANSFER-COMPATIBILITY:
for each safe compact K,
sup_{z in K} |T_N(z;mu_L)-T_N(z;0)| -> 0
```

or, more projectively, a version normalized by `T_N(z_0;mu)`:

```text
sup_{z in K}
| theta_N(z;mu_L) - theta_N(z;0) | -> 0.       (M-7)
```

By `(M-6)`, any proof of `(M-7)` must control the paired double resolvent
term, not an ambient operator norm.

Thus the pencil gap is no longer a vague structural mismatch.  It is a
precise directional `mu`-transfer target.

## 5. What remains open after this reduction

This note does **not** prove:

```text
1. local-uniform smallness of the paired double resolvent term in (M-6);
2. a lower bound preventing loss of normalization in the projective ratio;
3. treatment of sections where A_N(mu_L) is singular;
4. identification of the limiting mu_L family with the infinite normalized
   l2 solution class.
```

Those are the true residual interface obligations.

## 6. Consequence for BORDERED-WEYL-COMPLETENESS

Combining E77.7l with the present note, the LP interface decomposes as:

```text
finite projective reduction for arbitrary mu
+ directional mu-transfer to mu_L
+ singular-section regularization
+ infinite-class identification
+ simplicity/nonvanishing at mu_L
=> BORDERED-WEYL-COMPLETENESS.
```

This is strictly sharper than treating `mu=0 <-> mu_L` as part of the same
black-box theorem.

## 7. Minimal next object

The next admissible bridge theorem is:

```text
PENCIL-TRANSFER-COMPATIBILITY:
the paired mu-transfer identity (M-6) is locally uniformly small on safe
compacts along the finite family, after projective normalization and with a
declared treatment of the singular sections.
```

Then:

```text
PENCIL-TRANSFER-COMPATIBILITY
+ finite projective reduction
=> compatibility of the Phase 76 theta_N family with the intrinsic mu_L
   family.
```

Only after this bridge is closed does it make sense to ask for the final
boundary-relation/infinite-solution identification.

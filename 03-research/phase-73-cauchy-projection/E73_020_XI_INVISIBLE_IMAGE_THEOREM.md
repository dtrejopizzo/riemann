# E73.020 - Xi-invisible image theorem

## 1. Correction after SVD hardening

E73.019 hardened the source-image test by projecting onto the SVD effective image of
`(C_E-mu I)P_{O,K}`.  The full norm residual is not zero:

```text
relative residual: 1e-6 to 2.6e-4.
```

However the load-bearing scalar is not the full residual norm.  The Schur gate uses only

```text
<xi,S_b>.
```

The hardened test gives:

```text
e^(Re b L)|<xi,R_b>| <= 2.2e-8
```

on the tested windows.  Therefore the correct theorem is not strong image membership.  It is image
membership modulo an `xi`-invisible residual.

## 2. The right equivalence

Let

```text
M_L := C_E-mu I,
P_L := P_{O,K},
I_L := Image(M_L P_L).
```

For each off-line node `b`, write

```text
S_b = J_b + R_b,       J_b in I_L.
```

Since `M_L xi=0`, every `J_b` is invisible to `xi`:

```text
<xi,J_b>=0.
```

Thus

```text
<xi,S_b>=<xi,R_b>.
```

The sufficient condition for `NAT-SRC` is:

```text
XI-IMG:
inf_{J in I_L} e^(Re b L)|<xi,S_b-J>| <= L^B.
```

This is strictly weaker than

```text
dist(S_b,I_L) <= polynomially small.
```

and it is the actual scalar WRL condition.

## 3. Dual formulation

Let `P_I` be the orthogonal projection onto `I_L` and `P_I^perp=I-P_I`.  Then

```text
inf_{J in I_L} |<xi,S_b-J>|
= |<P_I^perp xi, P_I^perp S_b>|.
```

But `xi` is exactly in the kernel of `M_L`, hence orthogonal to `I_L` for the Hermitian finite
operator:

```text
xi in I_L^perp.
```

Therefore the condition reduces to the finite scalar identity

```text
XI-IMG:
e^(Re b L)|<xi,P_I^perp S_b>| <= L^B.
```

Since `xi=P_I^perp xi`, this is just the original pairing written after removing the image part.

The proof must show that the non-image component of `S_b` lies in the Phase 72 residual class, not
that the entire vector is small.

## 4. Why this avoids a false strengthening

The vector residual can contain directions orthogonal to `xi`.  Those directions do not enter scalar
WRL.  Requiring their norm to be small would reintroduce a global operator bound, the same type of
over-strong estimate that Phase 72 repeatedly rejected.

The correct object is the one-dimensional obstruction:

```text
xi-component of the Cauchy-Schur source outside the finite image.
```

This is exactly what E73.019 measures with `expPair`.

## 5. Analytic target

The new theorem to prove is:

```text
XI-INVISIBLE IMAGE THEOREM:
For every compact off-line window O and critical window K, through natural height,
the source vector S_b decomposes as

S_b = M_L Y_b + R_b,

with Y_b in P_{O,K} and

e^(Re b L)|<xi,R_b>| <= L^B.
```

The residual `R_b` may have non-small Hilbert norm.  It must be small only under the eigenfunctional
`xi`.

## 6. Remaining finite algebra

By E73.018, all vectors in this theorem are rational Cauchy functions on the mesh.  Thus the only
remaining proof obligation is:

```text
finite rational displacement identity
=> xi-invisible residual.
```

This is the sharpened endpoint of Phase 73.  It is weaker than norm-image membership and exactly
matched to scalar WRL.

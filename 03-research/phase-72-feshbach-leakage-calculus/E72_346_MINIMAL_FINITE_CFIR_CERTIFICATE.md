# E72.346 -- Minimal finite CFIR certificate

**Purpose.** State the current Phase 72 endpoint as one finite certificate.  This gathers
E72.339--E72.345 into a single proof-facing theorem: the transformed compact-root route closes once a
finite row-ideal identity for the interpolation residual is proved.

## 1. Data

Fix:

```text
1. an active pole-even mesh |m|<=M;
2. the pole-even operator C_E and ground eigenvalue mu;
3. a finite shifted zero-pair window W_T={(a_j,m_j)};
4. the Hermite jet map J_T;
5. the endpoint coefficient Lambda_L=mu+e_pole-2kappa_*.
```

Define:

```text
k_z(m)=(1-e^(zL))/(iz-d_m),
G_x(z)=k_z xi,
E_Lop=C_E-mu I.
```

The ground vector satisfies

```text
E_Lop xi=0.                                          (1)
```

## 2. Explicit interpolation row

Define the finite Hermite interpolation row matrix `R_T(L)` by

```text
R_T(L)xi
:= J_T[ Lambda_LG_x - I_T^HG_x + Tail_T^M ].         (2)
```

Here:

```text
I_T^H
```

is the removable Hermite zero-window interpolation operator of E72.342, and `Tail_T^M` is the finite
collapsed tail of E72.343:

```text
Tail_T^M(z)=sum_j m_j sum_n xi_n TailBasis_{z,n}^M(a_j),
TailBasis_{z,n}^M(a)=P_{z,n}^infty(a)-P_{z,n}^M(a).
```

Thus every entry of `R_T(L)` is explicit.

## 3. Certificate

The exact finite certificate is:

```text
CERT-CFIR:
R_T(L) belongs to Row(C_E-mu I).                      (3)
```

Equivalently, any of the following finite conditions holds:

```text
R_T(L)=A_T^1(L)(C_E-mu I)                             (4)
```

for some finite matrix `A_T^1`, or

```text
R_T(L) adj(C_E-mu I)=0,                               (5)
```

with the reduced adjugate convention at the simple pole-even ground eigenvalue, or all row-replacement
determinants vanish:

```text
det ReplaceRow(C_E-mu I; i, R_T[(a_j,p),*])=0         (6)
```

for every Hermite row `(a_j,p)` and every replacement row `i`.

The polynomial-residual version is:

```text
CERT-CFIR-poly:
R_T=A_T^1(C_E-mu I)+S_T,       ||S_T||<=C_TL^B.       (7)
```

## 4. Theorem

### Theorem 72.346

Assume `CERT-CFIR-poly` for every fixed shifted zero-pair window `W_T`.  Then `FINITE-CFIR` holds:

```text
||Def_CFIR,T|| <= C_TL^B.
```

Consequently:

```text
FINITE-CFIR
=> UREM-POLY
=> PW-Cauchy
=> SQB
=> CB
=> RNS
=> MC-NZ
=> NZ-MSD
=> compact-root HPAC decay.
```

Together with the already isolated Phase 72 transport/source/bordered-minor gates, this supplies the
Mellin spectral divisibility required for scalar WRL resonance annihilation.

### Proof

By E72.345, the full transformed Feshbach row splits as

```text
Full_CFIR_Row
= J_Tk_z(C_E-mu I)+R_T.
```

Applying this to `xi` and using (1) gives

```text
Def_CFIR,T=R_Txi.
```

If (7) holds, then

```text
Def_CFIR,T=S_Txi,
```

so `||Def_CFIR,T||<=C_TL^B` because `||xi||=1`.

E72.342 identifies this with the finite Hermite residual

```text
H_T(L)J_TG_x+J_TTail_T^M.
```

On every maximal off-line cluster, E72.324--E72.325 show that the leading block of `H_T(L)` is the
invertible confluent Cauchy block

```text
-diag(e^(a_jL))C_conf.
```

Therefore finite polynomial residuals force exponential suppression of the off-line Hermite jets.
E72.326 propagates this nodal suppression to `PW-Cauchy`; E72.314--E72.312 and E72.311 give the
remaining compact-root implication chain. `QED`

## 5. What remains

The remaining mathematical content is now fully localized:

```text
prove CERT-CFIR, or prove CERT-CFIR-poly.
```

This is finite, explicit, and verifiable.  It does not contain:

```text
1. outside zero sums;
2. infinite Fourier tails;
3. absolute prime sums;
4. derivative smoothness gates;
5. uncoupled archimedean/prime estimates.
```

It is exactly the finite row-ideal identity for the interpolation residual.

## 6. Position in the Phase 72 route

This certificate replaces the earlier analytic tail gates as follows:

```text
CERT-CFIR-poly
=> FINITE-CFIR
=> BER-POLY
=> UREM-POLY
=> Theorem 72.329
=> compact-root HPAC decay.
```

So `POSC` and `BER` are no longer separate proof targets once `CERT-CFIR-poly` is adopted.  They are
intermediate identities used to derive the finite row `R_T`.

## 7. Status

```text
proved: CERT-CFIR-poly implies FINITE-CFIR and the transformed compact-root chain;
reduced: the analytic endpoint to finite row-ideal/determinant identities (4)--(7);
open: prove the row-ideal identities themselves.
```

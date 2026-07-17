# E73.152 - Spectral-cutoff forced row lemma

Date: 2026-07-12.

## 1. Purpose

E73.149 reduced `LDIV_17` to the rowspace proximity of the signed forced
Mellin rows.  E73.150 showed that the full Moore-Penrose inverse of

```text
E_L=H_L-mu_L I
```

is not the right proof object: it amplifies harmless near-null complement
modes.  This note replaces the full inverse by a spectral cutoff.

The result is not a new closure claim.  It is the exact analytic theorem that
must now be proved.

## 2. Finite spectral decomposition

Let

```text
E_L v_0=0,        v_0=xi_L,       ||xi_L||=1,
E_L v_a=lambda_a v_a,             a>=1,
```

with an orthonormal eigenbasis.  For a row `r`, use the row action convention

```text
c_a(r):=r v_a.
```

Then

```text
r = c_0(r) xi_L^* + sum_{a>=1} c_a(r) v_a^*,
dist(r,Row(E_L))=|c_0(r)|.
```

For a cutoff `eps_L>0`, split the complement into

```text
G_L(eps)={a>=1: |lambda_a|>eps_L},
N_L(eps)={a>=1: 0<|lambda_a|<=eps_L}.
```

Define

```text
y_{eps}(r):=sum_{a in G_L(eps)} c_a(r)/lambda_a v_a^*.
```

Then the exact identity is

```text
r
= y_eps(r) E_L
 + c_0(r) xi_L^*
 + beta_eps(r),

beta_eps(r):=sum_{a in N_L(eps)} c_a(r)v_a^*.
```

This is just the spectral theorem, but with the near-null complement kept as
an explicit tail instead of inverted.

## 3. Application to forced Mellin rows

For a critical divisor node `w=-i gamma`, let `r_{w,1}, r_{w,2}` be the signed
forced rows of E73.149:

```text
[r_{w,1};r_{w,2}]
=M_L(w)^(-1)[P_{z_1,w}^{signed};P_{z_2,w}^{signed}].
```

By exact pair divisibility,

```text
c_0(r_{w,1})=r_{w,1}xi_L=H_0(w),
c_0(r_{w,2})=r_{w,2}xi_L=H_0(-w),
```

up to the fixed ordering.

Therefore `LDIV_17` is equivalent to

```text
|c_0(r_{w,1})|+|c_0(r_{w,2})| <= C L^-17.          (1)
```

The spectral-cutoff decomposition gives a non-pseudoinverse certificate:

```text
r_{w,j}
=y_{w,j,eps}E_L
 + alpha_{w,j}xi_L^*
 + beta_{w,j,eps},

alpha_{w,j}=c_0(r_{w,j}).
```

The near-null tail `beta` may be polynomially larger than `L^-17`; it is not
part of the rowspace distance.  It only obstructs proofs that try to invert
`E_L` on all of `xi_L^perp`.

## 4. The actual analytic target

The remaining theorem is:

```text
SFRL-CUT_17:
There exist admissible rows z_1,z_2 and constants C,A,B such that for every
critical box in the standard regime,

1. ||M_L(w)^(-1)|| <= C L^A,
2. ||r_{w,j}|| <= C L^B,
3. |alpha_{w,j}|=|r_{w,j}xi_L| <= C L^-17,     j=1,2.
```

Items 1 and 2 are conditioning/growth controls.  Item 3 is the only
arithmetically decisive statement.

Once `SFRL-CUT_17` is proved, the chain is:

```text
SFRL-CUT_17
=> LDIV_17
=> CSV_17
=> Asymptotic Standard-Box Theorem
=> Uniform GATE-73
=> scalar WRL
=> Omega_7.
```

## 5. Anti-tautology check

This lemma does not use the adjugate or the full pseudoinverse as a source of
cancellation.

It is also not the old rowspace repair no-go.  Adding a row of the form
`yE_L` after a defective row is built cannot change `alpha`.  Here the row
itself is different: it is the forced Mellin row obtained from exact pair
divisibility with the inactive signed tail already included.

Thus the proof obligation cannot be discharged by rowspace algebra.  It must
bound `alpha` from the explicit Mellin formula for `r_{w,j}`.

## 6. What a proof must look like

For each forced row, expand

```text
alpha_{w,j}
= sum_n r_{w,j}(n) xi_L(n).
```

The coefficients `r_{w,j}(n)` are explicit rational functions produced from

```text
M_L(w)^(-1) p_infty(z,w;n).
```

A valid proof of `SFRL-CUT_17` must show cancellation in this signed Mellin
sum before invoking any spectral inverse.  Equivalent forms are allowed:

```text
weighted Abel/Mellin cancellation,
finite Cauchy divisor identity with signed inactive tail,
or a model-normalized Green identity for the same alpha.
```

The following are not valid closures:

```text
1. alpha small because H_0(w) is assumed small;
2. alpha small because a full pseudoinverse reconstructs r;
3. alpha small after adding arbitrary rowspace rows;
4. adjugate divisibility without an independent bound on the scalar residue.
```

## 7. Status

proved:

```text
spectral-cutoff identity for every finite row;
SFRL-CUT_17 => LDIV_17 => CSV_17;
near-null complement explains the failure of the full pseudoinverse route.
```

open:

```text
prove the alpha bound from the explicit forced Mellin row.
```

This is now the narrow analytic frontier.

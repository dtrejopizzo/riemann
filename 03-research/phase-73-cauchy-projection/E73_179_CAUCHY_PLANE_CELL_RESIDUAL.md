# E73.179 - Cauchy-plane cell residual theorem target

Date: 2026-07-14.

## 1. Purpose

E73.178 identifies the remaining nodal theorem with characteristic smallness:

```text
CHAR-node <=> SDI-node <=> |H_0(w_gamma)| small.
```

Earlier attempts to prove this by placing the Cauchy row in the image of
`H_L-mu_L I` were tautological: adding a rowspace term cannot change its
pairing with the ground vector.  This note records the non-tautological
form that remains: a two-dimensional Cauchy-plane equation whose residual is
an explicit finite cell object.

## 2. Cauchy-plane decomposition

For `w=-i gamma`, define the two Cauchy rows

```text
q_w(n)=1/(w+i d_n),
q_-w(n)=1/(-w+i d_n),
Q_w=span{q_w,q_-w}.
```

For each `j in {1,2}`, decompose the row `q_j H_L` as

```text
q_j H_L = sum_k A_jk(w) q_k + rho_j(w),              (1)
```

where `rho_j` is the residual after projecting to the Cauchy plane.  In the
probe this projection is least squares; for a proof one may replace it by
any canonical two-row projection with polynomially bounded inverse.  The
identity below is independent of the choice once (1) is fixed.

Pair (1) against the normalized ground vector

```text
H_L xi_L = mu_L xi_L.
```

Writing

```text
h(w)=(q_w xi_L, q_-w xi_L)^T
     =(H_0(w),H_0(-w))^T,
r(w)=(rho_1(w)xi_L, rho_2(w)xi_L)^T,
```

gives the exact finite system

```text
(mu_L I-A(w)) h(w) = r(w).                         (2)
```

This is only associativity and self-adjointness:

```text
q_j H_L xi_L = mu_L q_j xi_L
```

and (1).

## 3. Sufficient theorem

The clean analytic replacement for `CHAR-node` is:

```text
CPINV:
||(mu_L I-A(w))^-1|| <= C L^a,

RCE-cell:
||r(w)|| <= C L^(-R-a)
```

for each critical standard-box node `w=-i gamma`.  Then (2) gives

```text
|H_0(w)|+|H_0(-w)| <= C' L^-R.
```

Choosing the `R` required by E73.123 gives `CSV_R`, hence the standard-box
gate and scalar WRL.

## 4. Why this is not the old rowspace tautology

The forbidden move is:

```text
q_w = y(H_L-mu_L I)+residual
```

because pairing with `xi_L` makes the image term vanish and the residual
scalar is just the original obstruction in disguise.

Here the residual is different:

```text
rho_j(w)=q_jH_L - projection_{Q_w}(q_jH_L).
```

It is produced before pairing with `xi_L`, by the finite cell action of
`H_L` on a fixed Cauchy plane.  The theorem to prove is therefore an
evaluated residual estimate:

```text
rho_j(w)xi_L small,
```

not a reconstruction of `q_w` modulo rowspace.

## 5. Cell form of the residual

Using the explicit CCM entries

```text
H_L(n,m)=Arch_L[q_nm]-Prime_L[q_nm],
```

the residual row has the finite formula

```text
rho_j(m)
= sum_n q_j(n)H_L(n,m) - sum_k A_jk(w)q_k(m).       (3)
```

Thus

```text
r_j(w)=sum_m rho_j(m)xi_L(m)
```

is an arithmetic-archimedean cell cancellation with no zero input.  The
proof-facing theorem is now:

```text
RCE-cell theorem:
the explicit residual (3), evaluated on the zeta-coupled ground vector,
has the required negative power uniformly in the critical standard boxes.
```

This is narrower than global `Phi_L -> Xi` convergence and stronger than a
generic Cauchy conditioning bound.

## 6. Status

```text
proved:   exact system (mu I-A)h=r for every finite L;
proved:   CPINV + RCE-cell => H0-DIV => CHAR-node/CSV;
open:     prove RCE-cell analytically from the explicit prime/Gamma cells.
```

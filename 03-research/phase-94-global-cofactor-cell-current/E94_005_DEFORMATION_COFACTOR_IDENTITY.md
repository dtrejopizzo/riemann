# E94.005 - Deformation cofactor identity

## 1. Arithmetic deformation

Use

```text
M_t=M_A-tM_P-mu_t I,
b_t=b_A-tb_P,                                        (1.1)
```

and construct `P_t(z)` from E94.003.  Every entry of `P_t` is a cofactor of
`M_t` combined with the raw boundary column.  Hence `P_t(z)` is differentiable
on every smooth finite spectral branch, including through an inner cluster
singularity after projective clearing.

## 2. Exact projective tangent

In a nonvanishing chart,

```text
partial_t log[P_t(z)/P_t(z_*)]
 =dot P_t(z)/P_t(z)-dot P_t(z_*)/P_t(z_*).            (2.1)
```

The numerator `dot P_t` is obtained by differentiating E94.003(1.4):

```text
dot P_t(z)
 =dot Delta_t C_t+Delta_t dot C_t
  +(2/L)[
    dot C_t U_(t,z)+C_t dot U_(t,z)
    +dot T_t V_(t,z)+T_t dot V_(t,z)].               (2.2)
```

All dotted quantities are derivatives of determinants or adjugate vectors.
Jacobi's cofactor formula defines them without `M_t^{-1}`.

## 3. Bilateral deformation defect

Let

```text
K_t(s;s_*)
 =partial_t log
  {[P_t(iu)P_t(-iu)]/[P_t(iu_*)P_t(-iu_*)]}
  -[J_L(s)-J_L(s_*)].                                (3.1)
```

Then

```text
log[R_1(s;s_*)/R_0(s;s_*)]
 =integral_0^1 K_t(s;s_*)dt,                         (3.2)
```

where `R_t` is the projective bordered ratio divided by the independent
Euler product.  Formula (3.2) is the inverse-free cofactor version of E87.003.

## 4. Autopsy of termwise matching

Neither `dot Delta`, `dot C`, `dot T`, `dot U` nor `dot V` is required to
match a separate part of the Euler current.  They are coordinate pieces of
one bordered determinant and may be large.  Only the coupled scalar (3.1) is
projectively meaningful.

Consequently a proof based on termwise absolute estimates of the differentiated
cofactors is inadmissible.  The next theorem must exploit a determinant-level
Gamma--Euler product rule or a signed Stieltjes identity for the complete
quotient.

## 5. Status

```text
proved:
  exact inverse-free deformation current;
  exact coupled cofactor identity;

rejected:
  termwise matching of differentiated cofactors;

open:
  determinant-level Gamma--Euler cancellation in (3.1).
```


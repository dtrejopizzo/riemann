# Finite-horizon storage gate

Status: stationary full-line storage is ruled out exactly.  The canonical
endpoint-leakage candidate is refuted, so it cannot close the global square.

## 1. No stationary square can close row (d)

For every nonempty active prime set,

    A_T(0)=theta_T-m_0-sum_p(log p)P_p(0),          (1)

with

    P_p(0)=(1+p^(-1/2))/(1-p^(-1/2))>1.            (2)

Hence

    A_T(0)<-m_0<0.                                  (3)

Suppose that a translation-invariant operator `D_T` on the full-line
profile space satisfied

    M_(A_T)=D_T^*D_T.                               (4)

Fourier diagonalization would make the right side a nonnegative multiplier,
contradicting (3).  Therefore neither the effective one-port reduction nor
the determinant identity can be completed by a stationary spectral factor.

The remaining geometric construction is required to use the information
discarded by a full-line stationary multiplier, namely

    compact support, the two Tate moments, and endpoint storage.          (5)

This proves that the finite-horizon qualification in the Herglotz--Gamma
gate is load-bearing, not technical.

## 2. Canonical support decomposition

Work in the time realization in which `Q` is multiplication by `t`.  Let

    P=P_[-T,T],  P_R=P_(T,infinity),
    P_L=P_(-infinity,-T).                           (6)

Then `P,P_R,P_L` commute with `Q` and

    I=P_L+P+P_R.                                    (7)

Use the independently constructed full-line unitary scattering multiplier
`K_T`; no passive realization of the signed global system is assumed.  For
an input `f=Pf`, define the three output components

    u_0=PK_Tf,  u_R=P_RK_Tf,  u_L=P_LK_Tf.          (8)

Unitarity gives the norm conservation

    ||f||^2=||u_0||^2+||u_R||^2+||u_L||^2.          (9)

The first-moment Green identity is the exact decomposition

    <K_Tf,QK_Tf>-<f,Qf>
      =[<u_0,Qu_0>-<f,Qf>]
       +<u_R,Qu_R>+<u_L,Qu_L>.                     (10)

On the exterior spaces put

    Q_R=Q-T>=0,
    Q_L=-Q-T>=0.                                   (11)

Using (9), equation (10) becomes

    <K_Tf,QK_Tf>-<f,Qf>
      =||Q_R^(1/2)u_R||^2-||Q_L^(1/2)u_L||^2
       +R_int,T(f),                                (12)

where the literal interior residual is

    R_int,T(f)=<u_0,Qu_0>-<f,Qf>
       +T(||u_R||^2-||u_L||^2).                    (13)

No sign has been asserted in (12); it is an exact bookkeeping identity.

## 3. The canonical endpoint mismatch

Let `J_T` be the fixed unitary reflection from the right exterior to the
left exterior,

    (J_Th)(t)=h(-t),  t<-T.                         (14)

For `f=L_0G` define, before taking the Green commutator,

    D_T^end G
      =J_TQ_R^(1/2)P_RK_TL_0G
        -Q_L^(1/2)P_LK_TL_0G.                      (15)

This is a literal source-defined mismatch of the two weighted endpoint
traces.  It contains no square root of `A_T`, no fitted contraction and no
free defect unitary.  Put `r=Q_R^(1/2)u_R` and
`ell=Q_L^(1/2)u_L`.  Direct expansion gives

    ||D_T^end G||^2
      =||r||^2+||ell||^2-2 Re <J_Tr,ell>.          (16)

Comparison with (12) proves the exact equivalence

    <A_TL_0G,L_0G>=||D_T^end G||^2                 (17)

if and only if

    R_int,T(L_0G)
      =2||ell||^2-2 Re <J_Tr,ell>.                 (18)

Equation (18) would have closed the square without a fitted defect operator,
but it is not a formal consequence of unitarity and is false for the present
scattering.  For `T=log 2`, active primes `{2,3}`, and
`G(t)=(1-(t/(.72T))^2)^4_+`, the converged Fourier calculation gives

    <A_TL_0G,L_0G>       =  35.2122860441...,
    ||D_T^end G||^2      = 213.8033515005...,
    difference           =-178.5910654564....       (19)

The independent time- and frequency-side evaluations of the first number
agree to `7e-14` on the largest grid.  The same discrepancy is stable under
the three grids `(2^16,24)`, `(2^17,32)`, `(2^18,40)`.  The reproducible
diagnostic is `scripts/p3_endpoint_mismatch_gate.py`.  Thus (18) is retired,
not promoted to a conjectural Hodge identity.

## 4. Cofinal compatibility

An inactive new prime contributes a lossless seam cylinder on `[-T,T]`.
It leaves the compressed commutator form unchanged by exact compact-support
stabilization, but it can reorganize the exterior vectors `u_L,u_R`.
Therefore vector-level invariance of (15) must not be inferred from form
stabilization.  The failed endpoint candidate illustrates why vector-level
invariance cannot be inferred from stabilization of the compressed form.
Cofinal stabilization remains available after a genuine finite positive
factor is constructed.

## 5. Classification

- stationary-square obstruction (1)--(4): **PROVED**;
- endpoint leakage identity (6)--(13): **PROVED**;
- canonical endpoint mismatch (14)--(16): **CONSTRUCTED**;
- equivalence of the global square with the scalar trace identity (18):
  **PROVED**;
- trace identity (18): **REFUTED BY (19)**;
- endpoint-mismatch route: **CLOSED NEGATIVELY**;
- cofinal passage after a genuine finite square: **PROVED AT FORM LEVEL**;
- global square and row (d): **OPEN**.

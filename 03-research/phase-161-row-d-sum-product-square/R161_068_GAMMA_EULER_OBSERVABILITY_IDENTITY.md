# R161_068 — Exact Gamma--Euler observability identity

**Domain correction (R161_070).** The full Laplace observation of LF and the bounded observation R on L2(-T,T) have different domains. Sections 4–5 do not establish admissible adjoint identities or the asserted equivalence of the factorization. Use R161_070's positive operator R*D_N R and explicit exterior collar instead. The full moment calculation remains valid in the stated right-shift convention. Novelty across the entire corpus is not established.

## 1. Gamma observation and translations

Let

    a_m=2m+1/2,        s_m=a_m+1/2=2m+1,       m>=1,

and for `delta>0` define

    (R_delta F)_m
      =sqrt(a_m)e^(-a_m(T+delta))K_F(a_m).                    (1.1)

This is the faithful Gamma observation of R161_026.  With the convention

    (tau_bF)(t)=F(t-b),

one has exactly

    K_(tau_bF)(a_m)=e^(-a_mb)K_F(a_m),                         (1.2)

hence

    R_delta tau_(log n)=D_n R_delta,
    (D_nx)_m=n^(-a_m)x_m.                                     (1.3)

No collar localization has been performed in (1.3), so the endpoint cancellation from
`P121_FIVE_NONCIRCULARITY_AUDITS`(2.2) does not apply to this full observation identity.

## 2. Von Mangoldt diagonal

Let the causal Euler generator be

    L=sum_(n>=2) Lambda(n)n^(-1/2)tau_(log n)                   (2.1)

first on compact sources and in the safe half-plane.  Equations (1.3) and absolute convergence at `s_m>1` give

    R_delta L F=C_zeta R_delta F,                              (2.2)

where

    (C_zeta x)_m=c_mx_m,
    c_m=sum_(n>=2)Lambda(n)n^(-s_m)
       =-zeta'(s_m)/zeta(s_m)>0.                               (2.3)

Therefore:

### Theorem 2.1 (Gamma--Euler observability; proved)

For every compact source for which the displayed expressions are defined,

    boxed:
    Re<R_delta F,R_delta LF>
      =sum_(m>=1)c_ma_me^(-2a_m(T+delta))|K_F(a_m)|^2
      >=0.                                                     (2.4)

The form in (2.4) vanishes if and only if `F=0`.

Proof.  Equations (2.2)--(2.3) give the equality and positivity.  Every `c_m` is strictly positive.  Vanishing
therefore kills every `K_F(a_m)`, and the moment-completeness theorem of R161_019 gives `F=0`.  QED.

This energy simultaneously contains:

- `Lambda*1=log`, through `-zeta'/zeta(s_m)`;
- the positive-odd Gamma lattice, through `a_m`;
- additive translations, through (1.3).

It cannot be instantiated by the abstract three-block model of R161_050.

## 3. Comparison with the pole energy

Since `c_m>0`, (2.4) has the same zero set as

    D_(T,delta)^Gamma(F)
      =sum_(m>=1)a_me^(-2a_m(T+delta))|K_F(a_m)|^2.             (3.1)

For fixed `delta>0` both are finite.  Moreover `c_m -> 0` exponentially in `m`, so (2.4) is weaker metrically but
equally faithful algebraically.  It is an arithmetic reweighting of the Gamma-pole energy, not a restatement by
definition: the weights arise from the von Mangoldt generator.

## 4. Primitive-pullback audit

Put

    G_delta=R_delta*R_delta>=0,
    h_delta(F)=Pi_TP_T L*G_delta F.                             (4.1)

The vector `h_delta(F)` is a source-defined primitive test.  For a first-contact radical of the completed Weil
form,

    <A_infinity F,h_delta(F)>=0.                               (4.2)

However, before the primitive projection is expanded, the unprojected pairing is

    <A_infinity F,L*G_delta F>
      =<R_delta L A_infinity F,R_delta F>,                     (4.3)

on a common commuting core.  It is **not** the faithful energy
`<R_delta LF,R_delta F>`.  The latter would require a test containing `A_infinity^(-1)L*G_delta F`; that inverse is
undefined on the hypothetical zero mode and would assume the conclusion.

Thus the initially proposed acceptance identity

    0=E_(T,delta)^(Gamma-Euler)(F)
       +B_(T,delta)^Tate(F)+B_(T,delta)^ext(F)                  (4.4)

does not follow from (4.2) and is withdrawn.  Expanding the projection yields boundary corrections to (4.3), but
cannot remove the extra `A_infinity`.

## 5. What additional law would connect the energy

A valid connection must intertwine the Gamma observation with the **compressed** first-contact operator without
inverting it.  Equivalently, one needs a division-free factorization on the equality locus,

    L*G_delta =A_infinity K_delta+Pi_T U_delta+V_delta(I-P_T), (5.1)

where the last two terms have a proved harmless Tate/exterior pairing and `K_delta` is source-defined and bounded
on the common graph.  Pairing (5.1) with `F` would then convert the faithful energy into a radical term plus
controlled boundary terms.  No such factorization is currently proved.

## 6. Noncircularity audit

The identity (2.4) is genuinely proved and new relative to the phase-161 Green attempts.  However, radicality does
not annihilate it: it inserts `A_infinity` in the observed vector.  Dropping that factor or using its inverse is
circular.  Thus the following are distinguished:

- Gamma--Euler faithful energy: **proved**;
- primitive radical pairing (4.2): **proved but does not contain the energy**;
- naive pullback identity (4.4): **withdrawn / wrong operator factor**;
- division-free factorization (5.1): **open**;
- annihilation of the faithful energy and D: **open**.

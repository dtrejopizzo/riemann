# Unified Gamma--Frobenius jump ledger

Status: rediscovery audit plus one sharpened scalar bound.  The underlying
Dirichlet reduction and its non-circularity gate were already proved in
`114_d_10_EXACT_DIRICHLET_REDUCTION.md`; the corresponding prime--Gamma
graph and the failure of fixed-cutoff Cheeger/Poincare closure were already
proved in `114_d_120_PRIME_GAMMA_CHEEGER_AUDIT.md`.  This file is not a new
route to row (d).

## 1. The Gamma reservoir is a continuum of translation edges

Put `a_n=n+1/4`.  The already proved Gamma multiplier is

    g_Gamma(tau)
      =sum_(n>=0) a_n^(-1) tau^2/(tau^2+4a_n^2).     (1)

For `b>0`,

    tau^2/(tau^2+b^2)
      =b integral_0^infinity exp(-bu)(1-cos(tau u))du. (2)

Using `b=2a_n` in (2) and summing the geometric series gives the exact
Levy--Khintchine representation

    boxed[
    g_Gamma(tau)
      =integral_0^infinity
          e^(u/2)(1-cos(tau u))/sinh(u) du.
    ]                                                (3)

Indeed

    2 sum_(n>=0)exp(-2(n+1/4)u)
      =2exp(-u/2)/(1-exp(-2u))=exp(u/2)/sinh(u).

For a Schwartz function `F`, Tonelli and Plancherel therefore give

    ||W_Gamma F||^2
      =(1/2)integral_0^infinity
          ||F-V_uF||_2^2 e^(u/2)du/sinh(u).         (4)

The integral is finite: near zero the difference is `O(u)` in `L2`, while
`e^(u/2)/sinh(u)=O(1/u)`; at infinity the density decays exponentially.

Thus the quarter-Gamma reservoir and a Frobenius cylinder have the same
literal type.  Both are translation edges.  Gamma is the continuous edge
measure `e^(u/2)du/(2sinh u)` and the arithmetic part is a discrete edge
measure.

## 2. Exact unified jump formula

At a finite horizon `T`, let

    Q_T={q=p^j: 2<=q<exp(2T)},
    ell_q=log q,
    w_q=Lambda(q)/sqrt(q),
    sigma_T=sum_(q in Q_T)w_q,
    c_T=m_0+2sigma_T.                               (5)

Define the positive jump map, entirely from the Gamma spectrum and the
row-(b) contact weights,

    (J_TF)_infty(u)= [e^(u/2)/(2sinh(u))]^(1/2)(F-V_uF),
    (J_TF)_q       = sqrt(w_q)(F-V_(ell_q)F).        (6)

Its target is

    L2((0,infinity) x R,du dt)
       direct-sum direct-sum_(q in Q_T)L2(R).        (7)

Zero extension is understood before every translation.  Equations (4) and

    w_q||F-V_(ell_q)F||^2
      =2w_q||F||^2
         -2w_q Re<F,V_(ell_q)F>                    (8)

give the exact identity

    boxed[
    <A_TF,F>=||J_TF||^2-c_T||F||^2.
    ]                                                (9)

There is no signed local summand left in `J_T`: every continuous and
discrete edge has positive weight.  The only negative object is the single
common source channel `sqrt(c_T)F`.

On the primitive space write `F=L_0G`,
`L_0=-partial_t^2+1/4`, with `G` compactly supported in `(-T,T)`.  Since
translations commute with `L_0`, (9) becomes

    <A_TL_0G,L_0G>
       =||J_TL_0G||^2-c_T||L_0G||^2.               (10)

This is a temporal identity, not a Fourier multiplier comparison and not a
difference of unrelated passive realizations.

## 3. The reconstruction restatement is not a new theorem

Let `R_T=closure(J_T P_T)`, where

    P_T=L_0 C_c^infinity((-T,T)).                   (11)

The acceptance test of `114_d_10`, Section 5, can be restated as a linear
reconstruction map

    E_T:R_T -> L2((-T,T))                           (12)

whose formula uses the common endpoint values of the translation edges and
which satisfies

    E_T J_TF=sqrt(c_T)F       (F in P_T),
    E_T E_T^* <= I.                                  (13)

If (13) is proved independently, then

    D_T=(I-E_T^*E_T)^(1/2)J_TP_T                   (14)

is admissible, because the square root is the defect of the independently
constructed edge reconstruction, and (9) gives

    D_T^*D_T=P_TA_TP_T.                             (15)

Abstractly, Douglas' lemma says that some contraction satisfying (13) exists
exactly when `P_TA_TP_T>=0`.  Thus `E_T` is the same Douglas gate already
encountered for `Phi` and for the Julia short.  It does not identify a new
missing object.

## 4. The actual new consequence: the raw scalar ratio is `1/2`

Let

    D_disc,T=(1/2)sum_(q in Q_T)w_q
       (I-V_(ell_q))^*(I-V_(ell_q)).                (16)

This is exactly the discrete part of the positive reference `R_T` in paper
42.  The proof of shift-chain coercivity establishes, before adjoining and
then discarding the nonnegative Gamma term,

    D_disc,T >= alpha_N I.                          (17)

By (6),

    J_T^*J_T=G_Gamma,T+2D_disc,T >=2alpha_N I.       (18)

The exact scalar load is

    c_T=m_0+2sigma_N,
    sigma_N=sum_(q in Q_T)w_q.                      (19)

Since `alpha_N~sqrt(N)` and `sigma_N~2sqrt(N)`,

    lim_(N->infinity)
       [2alpha_N/(m_0+2sigma_N)]=1/2.               (20)

Corollary `scalarnogo` compares `R_T>=alpha_N I` with the lossy estimate
`L_T<=(m_0+2sigma_N)I`, and therefore obtains `1/4`.  Unified jump
coordinates remove that factor-two loss and improve the raw ratio to
`1/2`.  The deficit nevertheless remains

    c_T-2alpha_N=(2+o(1))sqrt(N),                   (21)

of leading order.  The fixed-cutoff obstruction of `114_d_120` still
applies.  Equation (20) is a sharper ledger constant, not evidence for the
global square.

## 5. Classification

- Dirichlet reduction: **ALREADY `114_d_10`**;
- continuous Gamma conductance: **ALREADY PRESENT IN `114_d_120`**;
- common Levy notation (3)--(6): **NOTATIONAL REPACKAGING**;
- reconstruction gate (12)--(15): **DOUGLAS-EQUIVALENT, NOT NEW**;
- sharpened raw scalar ratio `1/2` and deficit `2sqrt(N)`: **PROVED HERE**;
- fixed-cutoff Poincare/Cheeger route: **CLOSED BY `114_d_120`**;
- global square and row (d): **OPEN**.

# Global square: exact two-bank elimination

Status: exact normal form and exact residual theorem.  This replaces the
formal matrix-inner claim in `P3_GLOBAL_SQUARE_ATTACK.md`.  The final
coherent intertwining identity is not proved here.

## 1. Canonical positive banks

Put `a_p=log p`, `r_p=p^(-1/2)` and, on the Fourier line,

    Z_p(tau)=exp(i a_p tau),
    B_p(tau)=(Z_p(tau)-r_p)/(1-r_p Z_p(tau)).        (1)

Both are ordinary inner multipliers in the upper half-plane.  With
`Q=-i d/dtau`, their Wigner--Smith operators are

    Z_p^*QZ_p-Q=a_p I,
    B_p^*QB_p-Q=a_p P_p,                            (2)

where `P_p=O_p^*O_p` is the physical place--Poisson multiplier.  The
quarter-Gamma Markov construction independently gives

    W_Gamma^*W_Gamma=M_(g_Gamma).                   (3)

Consequently the finite global commutator has the exact positive-minus-
positive form

    A_T=X_T^*X_T-Y_T^*Y_T,                          (4)

with the source-defined columns

    X_T F=(W_Gamma F,(sqrt(a_p)F)_p),
    Y_T F=(sqrt(m_0)F,(sqrt(a_p)O_pF)_p).            (5)

Indeed (4) is exactly

    g_Gamma+sum_p a_p-m_0-sum_p a_pP_p.            (6)

Thus every summand in both banks is positive before row (c), and no
meromorphic factor has been called an inner Hilbert-space transfer.

The scalar determinant multiplier still gives the useful signed identity

    A_T=K_T^*QK_T-Q,                                (7)

but (7) and (4) play different roles: (7) is the zero-residual Green
connection, while (4) is the only admissible starting point for a square.

## 2. D.247 eliminates the local Euler bank exactly

Let

    x_p=O_pF,
    q_p=sqrt(a_p)x_p,
    d(F)=sum_p sqrt(a_p)x_p.                         (8)

Tensoring the D.247 conservation law with the profile Hilbert space gives

    sum_p a_p||x_p||^2
      =||E_-x||^2+||d(F)||^2-||E_+x||^2.           (9)

Substitution in (4) produces the reduced banks

    X_red F=(W_Gamma F,(sqrt(a_p)F)_p,E_+x(F)),
    Y_red F=(sqrt(m_0)F,E_-x(F),d(F)),              (10)

and the operator identity

    A_T=X_red^*X_red-Y_red^*Y_red.                 (11)

The Real involution pairs the stabilized Poisson-resolvent traces
`T_p^-` and `T_p^+`.  It does **not** by itself identify those traces with
the older tangent coordinates `E_-x` and `E_+x`.  Thus (11) eliminates the
contact bank exactly, but it does not permit cancellation of the two
tangent ports.  The surviving block is precisely

    (Gamma,free delays,E_+x)
          versus (polar load,E_-x,coherent degree). (11a)

This distinction prevents the Real boundary theorem from being used one
step beyond what it proves.

## 3. Exact residual theorem

Let `P_T` be the two-Tate primitive projection and let `Theta_T` be any
contraction constructed from the Gamma, D.247 and Real boundary systems,
before comparison with `A_T`.  Define the literal transmission residual

    R_T=Y_red P_T-Theta_T X_red P_T.                (12)

Put `D_Theta=(I-Theta_T^*Theta_T)^(1/2)X_redP_T` in
the canonical defect space of the independently given contraction.  A
direct expansion, with no estimate, gives

    Delta_T-D_Theta^*D_Theta
      =-X_red^*Theta_T^*R_T
       -R_T^*Theta_TX_red-R_T^*R_T                 (13)

on the primitive core, where

    Delta_T=P_TA_TP_T.                              (14)

In particular the source transmission identity

    Y_redP_T=Theta_TX_redP_T                       (15)

implies immediately and exactly

    Delta_T=D_Theta^*D_Theta.                       (16)

Conversely, defining `Theta_T` by (15) is precisely the forbidden Douglas
construction: its contractivity is equivalent to `Delta_T>=0`.  Hence the
last theorem cannot be phrased as existence of a contraction.  It must
construct `Theta_T` from the coherent degree--Gamma boundary law and then
prove the vector identity `R_T=0`.

## 4. What the final calculation now contains

The global-square theorem has been reduced to the single **vector**
operator equality

    Y_red P_T=Theta_T X_red P_T.                    (17)

Here `Theta_T` must be fixed by one absolute transmission law acting on the
Gamma, tangent and coherent-degree ports.  All local contact components
have already been eliminated by (9).  The Real Bohr theorem fixes the
unitary identification of the additional stabilized resolvent boundaries,
but does not erase `E_-x` or `E_+x` from (17).

Equation (17) is not a scalar normalization and cannot be checked on a
finite list of vectors: `d(P_T)` has infinite Hilbert rank.  It is the one
remaining construction theorem.  Proving (17) closes the finite global
square through (13)--(16); failing (17) exposes the exact uncancelled
profile rather than a movable ``Maslov term.''

## 5. Classification

- canonical positive banks (4)--(6): **PROVED**;
- exact D.247 bank elimination (9)--(11): **PROVED**;
- Real matching of the stabilized Poisson-resolvent boundaries:
  **PROVED EARLIER**;
- identification of those boundaries with the D.247 tangent ports:
  **NOT PROVED AND NOT ASSUMED**;
- exact transmission-residual formula (13): **PROVED**;
- global Gamma--tangent--degree transmission identity (17): **OPEN**;
- global square: **OPEN**.

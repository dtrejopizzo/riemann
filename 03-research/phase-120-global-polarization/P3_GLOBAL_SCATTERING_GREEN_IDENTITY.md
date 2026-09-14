# Global determinant scattering and the exact Green identity

Status: proved on the common Schwartz/compact-support core. This closes the
construction of the quarter determinant transmission and the zero-residual
Green identity. It does not yet prove that the commutator is a positive
square on the primitive subspace.

## 1. Quarter determinant transmission

On `H_tau=L^2(R_tau)` define

    b_infty(tau)=pi^(-i tau)
      Gamma(1/4+i tau/2)/Gamma(1/4-i tau/2),

and let

    K_(1/4)=M_(b_infty).                              (1)

For real `tau`, `|b_infty(tau)|=1`, so (1) is unitary. Moreover

    b_infty(-tau)=conjugate(b_infty(tau)),

hence it preserves the Real Tate involution. It is defined entirely by the
quarter-twisted determinant and contains no `B_nuc` input.

Let

    Q=-i d/dtau,   Dom(Q)=H^1(R_tau).                (2)

On the Schwartz core, direct differentiation gives

    K_(1/4)^* Q K_(1/4)-Q
      =M_(g_Gamma-m_0),                              (3)

because

    (1/i)d/dtau log b_infty(tau)
      =Re psi(1/4+i tau/2)-log pi
      =g_Gamma(tau)-m_0.                            (4)

Thus `K_(1/4)` is the required determinant transmission. The earlier
Hilbert no-go is not contradicted: the signed connection is a unitary
commutator, not a Gram `K^*K`.

## 2. Relative prime scattering

For `r_p=p^(-1/2)`, `z_p(tau)=exp(i tau log p)`, put

    b_p(z)=(z-r_p)/(1-r_p z),
    c_p(z)=b_p(z)/z.                                  (5)

The boundary value `c_p(z_p(tau))` is unimodular. Although it is not a
one-sided Schur transfer, multiplication by it is a valid bilateral unitary
on `H_tau`. Its logarithmic derivative is

    (1/i)d/dtau log c_p(z_p(tau))
      =(log p)(P_p(tau)-1),                          (6)

where

    P_p(tau)=(1-p^(-1))
       /|1-p^(-1/2)exp(i tau log p)|^2.              (7)

The multiplier `P_p` is exactly `O_p^*O_p` in the Fourier realization.

## 3. Global finite-window scattering

Let `S_T={p:log p<2T}` and define the finite boundary-unitary multiplier

    Theta_T(tau)=b_infty(tau)
       product_(p in S_T)c_p(z_p(tau))^(-1),
    K_T=M_(Theta_T).                                 (8)

Every factor in (8) is source-defined before comparison with row (c).
Since the factors commute, (4) and (6) give

    (1/i)d/dtau log Theta_T(tau)
      =g_Gamma(tau)+theta_T-m_0
         -sum_(p in S_T)(log p)P_p(tau),             (9)

with `theta_T=sum_(p in S_T)log p`. The right side is precisely the
place-Poisson multiplier `A_T` already constructed independently.

Consequently, on the common Schwartz core,

    K_T^*QK_T-Q=M_(A_T).                             (10)

If `E_T` denotes zero extension from the support window, compression gives
the exact localized Green identity

    A_T^loc=E_T^*(K_T^*QK_T-Q)E_T.                  (11)

After the row-(c) comparison, and only then,

    -B_nuc,T(F,F)
      =<Q K_T E_TF,K_T E_TF>
         -<Q E_TF,E_TF>.                            (12)

There is no remainder in (10)--(12), no fitted scalar, and no use of a zero
or of the desired sign.

## 4. Primitive potential form

For primitive `F=L_0G`, equation (12) becomes

    -B_nuc,T(L_0G,L_0G)
      =<K_TE_TL_0G,QK_TE_TL_0G>
         -<E_TL_0G,QE_TL_0G>.                       (13)

Equation (13) is the complete bilateral multiplier Green formula and has no
algebraic remainder. The previously proved Real matching is compatible with
this orientation. A separate claim that every older state-space landing has
no Maslov term is neither needed nor made here.

## 5. Exact remaining theorem

Equation (13) is a signed commutator identity, not yet a positive square.
The next fixed task is to factor its primitive compression as

    P_T E_T^*(K_T^*QK_T-Q)E_T P_T=D_T^*D_T.         (14)

Defining `D_T` as a square root is forbidden. It must be obtained from the
matrix-valued D.247/Potapov completion of the poles of the relative factors.
Thus (14), and only (14), is now the finite global Hodge theorem still open.

## 6. Classification

- quarter determinant transmission `K_(1/4)`: **PROVED**;
- Real compatibility: **PROVED**;
- finite global scattering `K_T`: **CONSTRUCTED**;
- exact logarithmic derivative (9): **PROVED**;
- zero-residual Green identity (10)--(13): **PROVED**;
- positive primitive square (14): **OPEN**;
- row (d): **OPEN**.

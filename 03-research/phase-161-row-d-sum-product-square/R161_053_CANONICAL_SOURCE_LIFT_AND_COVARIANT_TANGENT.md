# R161_053 — Canonical source lift and the covariant Poisson tangent

> **TANGENT CORRECTION (R161_056).** The source lift and base identity (1.3) are valid. The covariant derivative of the unitary quotient does not retain the closing orientation difference: it is another coordinate for the derivative of the Poisson difference and hence for `U_N+V_N`. Sections 3 and 5 must not be used as a proof route to coherent saturation.

## 1. Mellin convention

Use the convention in which the renormalized Poisson defect has boundary action

    (E_N^ren F)^hat(tau)
      =[A_N(tau)u(tau)-B_N(tau)] Fhat(-tau),          (1.1)

where A_N=Z_N(1/2+i tau), B_N=Z_N(1/2-i tau), and u is the additive-Fourier reflection multiplier. This is the operator statement E_N^ren=S_N^ren Fcal-JS_N^ren written after extracting the common reflection Fhat(-tau).

Let U_N be multiplication by the unimodular theta_N=A_Nu/B_N of R161_052 and define the source lift

    x_N(F)(tau)=B_N(tau)Fhat(-tau).                     (1.2)

Then, almost everywhere and without division in the resulting equality,

    U_N x_N(F)=A_Nu Fhat(-tau),
    (U_N-I)x_N(F)=(E_N^ren F)^hat(tau).              (1.3)

Thus x_N is forced by the actual two Poisson histories. It is not obtained by pulling back a limiting scattering port.

## 2. Covariant differentiation

Let D_tau=(1/i)partial_tau on a common smooth core. For every multiplier U,

    D_tau(Ux)-U D_tau x=[D_tau,U]x
      =(1/i)U' x.                                      (2.1)

Apply this to U_N and x_N(F). The terms differentiating Fhat(-tau) cancel between the two covariant expressions. Hence

    U_N^*[D_tau,U_N]x_N(F)
      =q_N x_N(F),
    q_N=(1/i)theta_N'/theta_N real.                    (2.2)

This is the canonical tangent of the unitary Poisson colligation. Ordinary convergence U_Nx_N-x_N ->0 does not imply convergence of (2.2) to zero; differentiating before taking the graph limit retains the Chebyshev jet.

Multiplying (2.2) by conj(B_N) gives the division-free quadratic density

    |B_N|^2 q_N
      =(1/i)[conj(A_N)A_N'
             +|A_N|^2 u'/u
             -A_N conj(A_N')],                         (2.3)

using |A_N|=|B_N|. Formula (2.3) is R161_052(3.2) with its selfadjoint normalization displayed.

## 3. Operator meaning of the three terms

With the fixed Fourier convention, differentiating A_N and B_N is equivalent, up to the displayed factors of i, to inserting

    K_N^ren=-[X,S_N^ren].                               (3.1)

The first and third terms of (2.3) are a crossed phase pairing of the two differentiated Muntz orientations. The middle term is the Gamma connection furnished by the derivative of the additive Fourier multiplier. Derivatives of the source cancel by covariance. R161_056 performs the remaining chain-rule audit and shows that the resulting operator orientation is the mean `U_N+V_N`, not the closing difference.

Using Lambda*1=log on the completed hyperbola,

    K_N=L_M S_N-H_(M,N),                                (3.2)

so the tangent is expressible through the same finite data as PC. The polar derivative is retained because K_N^ren differentiates S_N-C_N rather than S_N alone.

## 4. Physical compression

Let P be the Hardy projection corresponding to the selected physical half-line and Q=I-P. The colligation identity gives

    ||P U_N x||^2+||Q U_Nx||^2=||x||^2.               (4.1)

For the source lift x_N(F), U_Nx_N is the Fourier-oriented history and x_N is the reflected causal history. Hence Q U_Nx_N is their exact exterior mismatch after the same physical compression. Its base-level difference is controlled by (1.3); its covariant tangent is controlled by (2.2)-(3.2).

The lift x_N(F) is not asserted to belong to PH. In physical space it is a finite causal/anticausal synthesis of a compact-window source and generally has interior and exterior components. Therefore the Toeplitz contraction formula of R161_052 may only be applied to Px_N after the complementary blocks have been retained. Treating x_N itself as a Hardy vector would delete the boundary history and assume the desired transfer.

The first-contact calculation must use a Tate-corrected tangent vector, because P applied to the polar derivative has two endpoint coordinates. R161_009 identifies these coordinates with the crossed Tate collar currents. Therefore no free boundary scalar remains, but an exact equality between the compressed quadratic tangent and the crossed Tate Gram still has to be derived.

## 5. Acceptance identity

The remaining finite identity can now be stated without an unspecified vector:

> Expand the PC-ren pairing on the full three-block decomposition of x_N(F), differentiate covariantly as in (2.1), and prove that on a primitive first-contact state
>
>     ||Q U_N x_N^Tate(F)||^2
>       + E_N^Gamma(F)+E_N^Tate(F)=o(1),              (5.1)
>
> where every term is obtained by orthogonal block expansion, E_N^Gamma is the positive Gamma-Hankel boundary term, and E_N^Tate is the literal crossed endpoint term with the parity sign fixed before taking the scalar pairing.

If both boundary terms in (5.1) are nonnegative with the asserted signs, all three vanish. The first term gives zero leakage; the Gamma term annihilates the complete moment detector; either conclusion closes D by the already proved downstream chain.

Equation (5.1) is an acceptance target. This note proves the canonical source lift and tangent entering it; it does not infer the sign or the equality from first contact.

## Status

- canonical source lift: proved;
- exact base colligation equation (1.3): proved;
- covariant tangent and cancellation of source derivatives: proved;
- occurrence of both Chebyshev orientations and Gamma in one phase tangent: proved, but with the nonclosing mean orientation by R161_056;
- full compressed PC-Gamma-Tate balance (5.1): open;
- D: open.

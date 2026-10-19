# R161_052 — Finite unimodular Poisson colligation

> **TANGENT CORRECTION (R161_056).** Sections 1--2 are valid. The unitary quotient phase in Section 3 differentiates the Poisson difference and therefore carries the orientation mean `U_N+V_N`, not the critical difference `U_N-V_N`. The claim in Sections 3--5 that this unitary tangent is the closing coherent jet is withdrawn. The critical jet differentiates the complementary Poisson sum, which is not unitary.

## 1. The two finite orientations define a unitary multiplier

On the critical line put s=1/2+i tau and let

    A_N(tau)=Z_N(s),
    B_N(tau)=Z_N(1-s)=conj(A_N(tau)),

where Z_N is the real-coefficient polar-renormalized Muntz multiplier of R161_003. Let u(tau) be the unit-modulus multiplier of the logarithmic additive Fourier transform, so the finite Poisson defect is

    e_N=A_N u-B_N.                                      (1.1)

Away from the common zero set define

    theta_N=A_N u/B_N.                                  (1.2)

Since |A_N|=|B_N| and |u|=1,

    |theta_N|=1                                         (1.3)

almost everywhere. On the zero set it may be assigned any unimodular value; multiplication by theta_N is therefore a unitary operator on boundary L2. Equation (1.1) becomes

    e_N=B_N(theta_N-1)                                  (1.4)

almost everywhere. This is an exact finite statement, not a limiting use of the zeta functional equation.

The quotient is used only to define an a.e. unitary boundary multiplier. No meromorphic division across a zeta zero, no Hardy range membership and no pole removability are asserted.

## 2. Exact Toeplitz-Hankel defect

Let P be any orthogonal Hardy/support projection, Q=I-P, U_N=M_(theta_N), and T_N=PU_NP on PH. Then

    I_(PH)-T_N^*T_N
      =P U_N^* Q U_N P
      =(Q U_NP)^*(Q U_NP)>=0,                         (2.1)

and

    I_(PH)-T_NT_N^*
      =P U_N Q U_N^*P
      =(Q U_N^*P)^*(Q U_N^*P)>=0.                    (2.2)

These follow by inserting I=P+Q into P U_N^*U_NP=P and P U_NU_N^*P=P. Thus the finite Poisson comparison has a canonical conservative colligation. Its defect is literally exterior leakage, with no choice of square root.

For x in PH,

    ||x||^2-||T_Nx||^2=||Q U_Nx||^2.                 (2.3)

If T_Nx=lambda x with |lambda|=1, (2.3) gives U_Nx=lambda x. This is the finite analogue of R161_020.

## 3. Division-free differentiated phase current

Where A_N is nonzero, logarithmic differentiation gives

    theta_N'/theta_N
       =A_N'/A_N+u'/u-B_N'/B_N.                      (3.1)

The expression can be written without division:

    |A_N|^2 theta_N'/theta_N
      =conj(A_N)A_N' + |A_N|^2 u'/u - A_N conj(A_N'). (3.2)

Here B_N'=conj(A_N') for differentiation in the real variable tau. Formula (3.2) extends continuously through every zero at which A_N and A_N' are finite, and in any case defines an L1_loc quadratic current. Since theta_N is unimodular, (1/i)theta_N'/theta_N is real distributionally; the right side of (3.2) is the weighted oriented phase velocity.

The first and third terms form the phase current of the two finite Muntz orientations and the middle term is the additive Fourier/Gamma connection. However R161_056 shows that, after the reflection chain rule is typed in the `s` variable, their operator combination is the orientation mean rather than the critical difference.

The derivative sign depends on the Fourier convention. The invariant content is the logarithmic derivative in (3.1) and its division-free form (3.2); no later argument may use a convention-dependent sign without recalculating it from (1.1).

## 4. Relation to PC-ren and the collars

The derivative A_N' is, up to the fixed i/sign convention, the multiplier of K_N^ren=-[X,S_N^ren]. Consequently the two non-Gamma terms in (3.2) are the Mellin form of the coherent orientations K_N^ren Fcal and J K_N^ren isolated in R161_035. Identity Lambda*1=log expresses K_N by L_MS_N-H_(M,N), so (3.2) is the quadratic location where the product identity enters the unitary Poisson colligation.

After physical compression, (2.1) produces an interior/exterior block decomposition. The polar continuum is already part of Z_N and therefore part of theta_N. Its moving support is the exterior image of R161_028. The two endpoint coefficients must still be expressed in the crossed Tate coordinates of R161_009 before passing to a first-contact limit.

## 5. The exact remaining proposition

This construction reduces the requested transfer to a concrete colligation statement:

> For the source-dependent finite vector x_(M,N,T)(F) obtained from the separated PC-ren port after the canonical crossed Tate correction, first-contact radicality makes the Toeplitz contraction extremal:
>
>     ||T_N x_(M,N,T)(F)||^2-||x_(M,N,T)(F)||^2 ->0.      (5.1)
>
> The graph limit of Q U_N x_(M,N,T)(F) is the physical left leakage of the corrected product port.

If both assertions hold, (2.3) forces zero leakage, unitary compression gives exact scattering, and R161_019 closes D.

Neither assertion is proved merely by constructing theta_N. In particular x must be obtained from PC-ren rather than defined from the limiting scattering port, and the Tate correction must be shown to cancel the complete endpoint block with the correct sign. This is now the only missing bookkeeping in the colligation route.

## Status

- finite unimodular Poisson multiplier: proved;
- canonical Toeplitz-Hankel leakage square: proved;
- division-free oriented phase current containing both Muntz derivatives and Gamma: proved;
- identification with the closing coherent difference: withdrawn by R161_056; the unitary tangent has the wrong orientation;
- first-contact extremality and graph identification in (5.1): open;
- D: open.

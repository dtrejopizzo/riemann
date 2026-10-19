# R161_061 — Candidate Poisson--Tate Lagrangian boundary identity

## 1. Why the crossed Tate matrix is naturally symplectic

Let V_T be the two-dimensional Tate coefficient space, C the exchange matrix and G_T the positive Tate Gram. Since G_T commutes with C,

    K_T:=G_TC                                             (1.1)

is symmetric, although it is generally indefinite. On the doubled boundary space

    B_T=V_T direct_sum V_T

define

    omega_T((v,j),(w,k))=<j,w>-<v,k>.                    (1.2)

The graph

    L_T^Tate={(v,K_Tv):v in V_T}                         (1.3)

is Lagrangian:

    omega_T((v,K_Tv),(w,K_Tw))
      =<K_Tv,w>-<v,K_Tw>=0.                              (1.4)

Thus the crossed matrix should not be used as a positive Gram. Its canonical role is a selfadjoint boundary response whose graph has zero Green form. This explains simultaneously why treating G_TC as an orthogonal Gram gives a wrong sign and why its occurrence can cancel a boundary concomitant exactly.

## 2. Infinite-dimensional Poisson boundary carrier

Let E_R and E_L denote the right and left exterior history spaces. Introduce

    B_(N,T)=
      (E_R direct_sum E_L)
       direct_sum
      (E_R direct_sum E_L),                              (2.1)

whose elements are written (xi,eta), with xi the exterior Weil/polar datum and eta the two causal Poisson histories. Define the canonical Green form

    Omega((xi,eta),(xi',eta'))
      =<eta,xi'>-<xi,eta'>.                              (2.2)

The finite compressed-commutator identity R161_059 is precisely the pullback of (2.2): its two terms Ybar*X-X*Y are the two orientations of Omega after reflection identifies the left and right components.

Add the Tate carrier and use

    Omega_total=Omega+omega_T.                           (2.3)

R161_009 proves that the polar endpoint coordinates of the Poisson histories are K_Tv. Therefore the finite polar/Tate correction lies on the Lagrangian graph (1.3), and its contribution to Omega_total vanishes for two corrected boundary data sets.

## 3. Proposed full boundary graph

Let Lambda_(N,T) map a primitive compact-window source to its complete corrected boundary data:

    Lambda_(N,T)f
      =(xi_(N,T)(f),eta_(N,T)(f);v(f),K_Tv(f)).           (3.1)

Here:

- xi is the exterior Weil image including the polar layer;
- eta is the ordered pair of one-sided integer-minus-continuum histories;
- v is the first-contact Tate forcing coordinate;
- K_Tv is the crossed collar current.

The desired new identity is

    boxed:
    Omega_total(Lambda_(N,T)f,Lambda_(N,T)h)
      =<PC_N f,h>-<f,PC_N h>,                            (3.2)

where PC_N is the finite renormalized Poisson--Chebyshev source operator before scalar recombination.

If PC_N is symmetric on the primitive first-contact source graph, the right side of (3.2) vanishes. Hence the image of that graph under Lambda_(N,T) is isotropic. Maximality is unnecessary for closure; isotropy for the source and its canonical conjugate test is enough.

Equation (3.2) is a genuine candidate identity, not a consequence asserted from the existing linear PC formula. It specifies both the boundary form and the required ordering.

## 4. Finite Tate part of (3.2)

The Tate contribution is already proved. For two forcing vectors v,w with currents j=K_Tv and k=K_Tw,

    <j,w>-<v,k>=0                                      (4.1)

by symmetry of K_T. Under parity, the source-derivative coordinate has opposite parity and each individual mixed Tate pairing also vanishes, recovering R161_043.

Therefore any failure of (3.2) lies in the infinite-dimensional exterior carrier, not in an unknown endpoint scalar.

## 5. Relation to the missing scalar gate

Choose h to be the finite canonical conjugate source producing the corrected right product port. If (3.2) holds and its graph limit is compatible with the Hardy construction, the exterior component of Omega_total is the antisymmetric ordering remainder of R161_023 and R161_044. The Tate component is zero by Section 4. The remaining scalar is then

    2 Re<g,P_R C_log g+epsilon g>                     (5.1)

up to the fixed global sign convention. Isotropy makes (5.1) zero. R161_021 gives exact scattering, and R161_019 gives F=0.

The factor and sign in (5.1) must be obtained by a literal finite expansion; they are not declared proved here.

## 6. What must be verified

The new route has three falsifiable steps:

1. derive (3.2) term by term from PC-ren, with the polar continuum included before compression;
2. prove that the exterior part for the canonical conjugate test is exactly (5.1), rather than the tautological full pairing of R161_023;
3. establish the common-graph limit without defining the conjugate source through an inverse of the primitive Weil operator.

The first step is an algebraic Green calculation. The second is the decisive orientation check. The third is analytic.

## 7. Status

- Tate boundary graph is Lagrangian: proved;
- identification of the crossed Tate matrix as the symmetric boundary response: proved;
- infinite-dimensional Green carrier matching the compressed commutator: proved at the formal block level;
- full PC boundary identity (3.2): proposed/open;
- identification with the extremal scalar (5.1): proposed/open;
- D: open.

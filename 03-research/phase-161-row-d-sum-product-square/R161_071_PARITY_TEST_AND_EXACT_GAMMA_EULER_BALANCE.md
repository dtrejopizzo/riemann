# R161_071 — Parity-preserving test and an exact equality-state balance

## 1. Finite observations and admissible test

Use the right shifts, interval I, and coefficients of R161_070. Truncate the moment index to 1<=m<=L and denote the observation by R_L. Define

    G_L=R_L*R_L, S_L=G_L+J G_L J,
    h_L=Pi S_L f.

S_L commutes with reflection J. Its kernel is a finite sum of smooth exponentials on the closed interval. The two-Tate projection Pi preserves smoothness on that interval. The zero extension of h_L therefore belongs to H^s(R) for every s<1/2 (endpoint jumps are allowed), hence to the logarithmic Gamma form domain. This gives an admissible primitive test without an inverse of H_T. The argument uses the corpus logarithmic Gamma form realization, not global operator-domain membership of h_L.

Let f be a parity first-contact vector, Jf=epsilon f. Use N>=exp(2T), so the interior arithmetic operator B=P L_N P includes every active shift. Write M for the Gamma multiplier and m_T for its window form. The local first-contact equation is

    (M-B-B*)f=r,

in weak form on I, with r in the two-dimensional Tate space. In particular the full window form a satisfies

    a(f,v)=<r,v>, a(f,Pi v)=0.

Taking v=S_L f yields the exact equality

    0=Re m_T(f,S_L f)
       -Re<(B+B*)f,S_L f>-Re<r,S_L f>.           (1.1)

All formulas use real parts and thus are independent of the choice of linear argument for the Hilbert inner product.

## 2. Both Euler orientations survive

Reflection gives JBJ=B*. Because f and S_L f have the same parity,

    Re<(B+B*)f,S_L f>
      =2 Re<Bf,G_L f>+2 Re<B*f,G_L f>.          (2.1)

The first term is the forward moment pairing. The second is the backward pairing; reflection does not make it equal to the first, because G_L itself does not commute with J.

Define explicit scalars

    c_(N,L)=<R_L f,D_(N,L)R_L f>,
    e_(N,L)=Re<R_L f,E_(N,L)f>,
    v_(N,L)=Re<R_L f,R_L B*f>.

The finite collar identity R161_070(2.1) implies

    Re<Bf,G_L f>=c_(N,L)-e_(N,L).             (2.2)

Substitution in (1.1) gives the exact balance

    0=2 c_(N,L)+Q_(N,L),                      (2.3)

where the remainder is explicitly

    Q_(N,L)=2 v_(N,L)-2 e_(N,L)
       -Re m_T(f,S_L f)+Re<r,S_L f>.          (2.4)

This constructs an equality-state identity with a positive finite Gamma–Euler detector as a term. It does not establish that the remainder is nonnegative.

## 3. Backward term without illegal global moments

For b=log n, the compressed backward shift is f(t+b) restricted to I. Its moment is exactly

    K_(P V_(-b) P f)(a_m)
      =exp(a_m b) integral_(-T+b)^T exp(-a_m u)f(u)du

when b<2T, and zero otherwise. Therefore

    (R_L B*f)_m=b_m sum_(2<=n<exp(2T))
       Lambda(n)n^(a_m-1/2)
       integral_(-T+log n)^T exp(-a_m u)f(u)du.   (3.1)

This finite formula is the legitimate backward observation. Replacing the truncated integral with a full moment would insert a left collar and large factors n^(a_m-1/2). Such a replacement is not justified by primitivity.

## 4. Tate coefficient and remaining sign problem

Let phi_-=exp(-t/2), phi_+=exp(t/2), r=alpha phi_-+beta phi_+. The Tate term in (2.4) is the explicitly computable pairing of r with S_L f. It is not automatically the crossed collar current of R161_009, nor the positive quantity epsilon<v,G_TC v>. Its source is S_L f, and its two moments must be evaluated as such.

Thus all four components of Q have specified sources: the backward truncated Euler moment (3.1), the forward collar from R161_070, the Gamma bilinear form, and the two forcing coefficients. There is no unspecified boundary scalar.

To close D by this balance it would suffice to prove Q_(N,L)>=0 for every L on every first-contact parity vector. Equation (2.3) would then imply c_(N,L)=0 for every L. Completeness of the Gamma moments would give f=0. Alternatively, a finite detecting collection on the finite-dimensional radical suffices by R161_046. No infinite-index graph passage is needed for these finite tests.

The sign must be proved from the explicit kernels. Positivity of M or G_L separately would not prove the sign of their bilinear product. Nor does parity determine the collar signs. This note proves (2.3), not the inequality on Q.

## Status

Constructed and proved on the imported form domain: admissible parity test; exact finite balance (2.3); explicit backward observation (3.1). Open: the sign of (2.4) on the first-contact radical, and D.

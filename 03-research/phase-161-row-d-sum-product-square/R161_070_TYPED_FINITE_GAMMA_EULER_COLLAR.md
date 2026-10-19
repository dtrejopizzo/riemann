# R161_070 — Typed finite Gamma–Euler detector and exact collar

## Scope corrections

R161_068's full Laplace-moment calculation is valid in its right-shift convention. But the bounded observation on L2(-T,T) cannot be applied unchanged to the exterior Euler tail. Its subsequent adjoint manipulations conflate these observation domains. R161_069 also conflates the global kernel with the kernel of primitive compression. Neither issue proves impossibility of an arithmetic closure identity.

Use V_b f(t)=f(t-b) throughout this note, independently of tau conventions elsewhere. Let I=(-T,T), P be physical projection, and Pi the primitive projection on L2(I).

## 1. Bounded detector

For delta>0 set

    a_m=2m+1/2, b_m=sqrt(a_m) exp[-a_m(T+delta)],
    (Rf)_m=b_m integral_I exp(-a_m t)f(t)dt.

R is Hilbert–Schmidt: its m-th coordinate functional has squared norm

    b_m^2 sinh(2a_m T)/a_m <= exp(-2a_m delta)/2.

For N>=2 define

    L_N=sum_(2<=n<=N) Lambda(n)n^(-1/2)V_(log n),
    c_(m,N)=sum_(2<=n<=N) Lambda(n)n^(-(a_m+1/2)),
    D_N=diag(c_(m,N)), C_N=R*D_N R.

C_N is positive trace class on L2(I), with

    <f,C_N f>=sum_m c_(m,N)b_m^2 |K_f(a_m)|^2.

All weights are strictly positive, already because of n=2. By moment completeness (R161_019), C_N is injective. Compactness prevents a uniform positive lower bound on the whole infinite-dimensional space.

Moreover D_N converges in operator norm to D=diag(-zeta'(2m+1)/zeta(2m+1)), since

    sup_m |c_m-c_(m,N)| <= sum_(n>N) (log n)n^(-3) ->0.

Consequently C_N converges in trace norm to C=R*DR, with trace-norm error at most ||R||_HS^2 times that tail.

## 2. Explicit collar and quadratic identity

Set B_N=P L_N P on L2(I). The full Laplace integral of L_N f is c_(m,N)K_f(a_m). Right shifts create no left exterior. Its right-exterior part is the bounded map E_N given by

    (E_N f)_m=b_m sum_(2<=n<=N) Lambda(n)n^(-(a_m+1/2))
       integral_(max(-T,T-log n))^T exp(-a_m u)f(u)du.

Changing variables t=u+log n and splitting the full integral at T proves

    R B_N=D_N R-E_N.                              (2.1)

This also proves boundedness of E_N. With G=R*R, multiply by R* and take Hermitian parts:

    C_N=(G B_N+B_N*G)/2+(R*E_N+E_N*R)/2.           (2.2)

Thus the exact quadratic identity is

    <f,C_N f>=Re<Rf,R B_Nf>+Re<Rf,E_Nf>.          (2.3)

No sign for the separate collar pairing has been proved. No first-contact hypothesis was used.

## 3. Inactive primes live entirely in the collar

If n>=exp(2T), P V_(log n)P=0 and the integral in E_N is the full K_f(a_m). Hence B_N stabilizes past that cutoff, while for N'>=N>=exp(2T),

    E_(N')-E_N=(D_(N')-D_N)R.                    (3.1)

Discarding the exterior term would discard the entire inactive-prime contribution to the detector. Finite-window stabilization does not remove it.

## 4. The operator that must enter the proof

Let H_T be the selfadjoint operator associated with the primitive compressed Weil form, with domains from the first-contact reduction. First contact gives H_T f=0; it does not give A_infinity f=0. The latter can have Tate and exterior components.

The correct detector on the primitive space is Pi C_N Pi, still faithful.

For clarity, global injectivity cannot replace compressed injectivity: A=[[0,1],[1,0]] is invertible, but with P=diag(1,0), PAP is zero on the nonzero range of P. The exterior component of A e_1 is exactly what compression deletes. This example refutes the global-to-compressed inference in R161_069, without modeling the arithmetic operator.

A sufficient comparison would construct an admissible map K and a nonnegative form Q on the actual primitive space with

    2 Re a_T(f,Kf)=<f,C_N f>+Q(f).                (4.1)

Here Kf must be primitive and in the form domain. Radicality would kill the left side and faithfulness would force f=0. A proof of (4.1) is not circular merely because it implies D. Circularity would arise from assuming its sign, inverting H_T without justification, or deleting a nonzero collar.

Equation (2.2) provides an explicit finite expansion for the detector. It does not yet construct K or Q. A global factorization through A_infinity alone does not settle this compressed comparison.

## Status

Proved: bounded faithful positive C_N; trace-norm convergence; exact exterior collar (2.1); Hermitian identity (2.2); stabilization law (3.1).

Open: comparison (4.1) with the primitive Weil form, and therefore D. No independence from all arithmetic hypotheses or exhaustion of possible constructions is asserted.

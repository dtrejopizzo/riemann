# P123.104 — Convergent tangential Fredholm determinants on the smooth test domain

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY for convolution on
the compact boundary Y=B_q with tests in S(Y). This is an analytic
Fredholm determinant, not an identification with the arithmetic RR line.

## 1. Trace-class integrated action with the declared Haar measure

Let dy have total mass a=log q and let Fourier coefficients use
probability Haar, as in P123.101. For f in S(Y), define on L2(Y,dy)

    (R(f)v)(y)=integral_Y f(y z^-1)v(z) dz.

The normalized character basis diagonalizes R(f), with eigenvalues
a f_hat(chi). Consequently

    ||R(f)||_1=a sum_chi |f_hat(chi)|=a rho_0(f),
    Tr R(f)=a sum_chi f_hat(chi)=a f(1).                     (1)

Every equality uses absolute Fourier convergence. This is an ordinary
Hilbert-space trace, not an integrated trace of decomposable fields.
It is also not the coefficient functional integral_Y f=a f_hat(1):
the two operations have different meanings and must not be identified.

For convolution defined with dy,
R(f*g)=R(f)R(g), and R(f^*)=R(f)^*, where f^*(y)=conjugate(f(y^-1)).
Fourier coefficients of f*g are a f_hat(chi)g_hat(chi), proving these
identities directly and showing convolution stays in S(Y).

## 2. The entire determinant and its quantitative limit

Define

    D_f(z)=product_(chi in L) (1+z a f_hat(chi)).             (2)

Since sum_chi |a f_hat(chi)| is finite, the product converges locally
uniformly in z and is independent of enumeration. It is the Fredholm
determinant of 1+zR(f), as follows by the diagonal finite-rank truncations.
It is entire, D_f(0)=1, and

    |D_f(z)|<=exp(|z|a rho_0(f)),
    D_f'(0)=Tr R(f)=a f(1).                                 (3)

Let P_n average f over N_n and let Q_n be the corresponding orthogonal
projection on L2(Y). In Fourier coordinates,

    R(P_n f)=Q_n R(f) Q_n,
    ||R(f)-R(P_n f)||_1=a rho_0(f-P_n f)->0.                 (4)

This compression is unitarily the convolution operator on Y_(N_n)
with the same quotient mass a, extended by zero on the complement.
Thus its determinant is exactly the finite-unit-level determinant,
not a rescaled determinant with additional multiplicity.

For |z|<=R, factor the product (2) into retained and omitted characters.
The elementary bound |product_j(1+w_j)-1|<=exp(sum_j|w_j|)-1 gives

    |D_f(z)-D_(P_n f)(z)|
       <=R a rho_0(f-P_n f) exp(R a rho_0(f)).               (5)

Here we used exp(t)-1<=t exp(t). This proves convergence of the
finite-unit determinants locally uniformly, with an explicit tail
estimate in the topology already constructed. At each fixed unit level
there remain infinitely many real Fourier modes; their determinant
converges by the same absolute-summability argument.

## 3. Multiplicative and logarithmic identities

For f,g in S(Y), let h=f+g+f*g. Then
1+R(h)=(1+R(f))(1+R(g)), and the products of eigenvalues prove

    D_h(1)=D_f(1)D_g(1).                                    (6)

The identity holds even if one factor vanishes; it is not based on
choosing a logarithm across a zero. Near z=0, where |z|a rho_0(f)<1,
absolute convergence permits expansion and summation:

    log D_f(z)=sum_(r>=1) (-1)^(r+1) z^r Tr(R(f)^r)/r.       (7)

These are identities of the represented convolution product. Complex
conjugation gives D_(f^*)(z)=conjugate(D_f(conjugate z)). Normalized
pullback through further finite-unit refinements preserves the same
operator on the invariant subspace and adds zero on its orthogonal
complement, so the finite-level identities are coherent.

## 4. Relation to the existing tangential character

For an external Bruhat test F on G=H_S, periodize along K_q as in
P123.041:

    b(gK_q)=integral_(K_q) F(gk) dk.

It belongs to a finite-unit smooth level and hence to S(Y). The
quotient integral formula identifies the tangential induced operator
of P123.041 with R(b). Equation (1) therefore recovers exactly

    Tr R(b)=(log q) integral_(K_q) F(k) dk.

Thus (2) supplies a convergent analytic determinant of that tangential
test-integrated representation and extends it continuously to S(Y).
The trace-class property comes from the summable test coefficients;
it does not contradict the heat-trace divergence in P123.103.

## 5. What is still required

This proves an actual infinite-unit-level determinant limit for the
tangential convolution test domain, preserving its product, involution
and tangential trace. It does not show convergence of the normal-cutoff
determinants after subtracting the linear counterterm of P123.043.
Control of the first trace alone does not control the higher traces
in a logarithmic determinant such as (7).

Nor is this scalar entire function identified with the determinant line
of the mixed diagonal, its arithmetic metric or the RR equality.
Higher diagonal homology, the normal determinant comparison and global
source/strata compatibility remain necessary for full A.

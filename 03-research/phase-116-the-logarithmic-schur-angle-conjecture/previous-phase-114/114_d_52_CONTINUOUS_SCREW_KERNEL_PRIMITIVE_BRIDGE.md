# D.52 — Continuous screw-kernel bridge for the primitive Hodge form

## 1. Purpose

D.32 identifies all prime powers, the complete Gamma contribution and the
two Tate jets in the distributional form.  The direct Hodge problem can be
put in a continuous-kernel form by integrating the test function once.  This
removes the distributional second derivative without changing either the
primitive conditions or the sign to be proved.

No positivity of the screw kernel, no zero of zeta and no Riemann-hypothesis
assumption is used in the comparison below.

## 2. The source-defined continuous kernel

Let

\[
\begin{aligned}
 g(t)={}&-4\bigl(e^{t/2}+e^{-t/2}-2\bigr)\\
 &+\sum_{n\leq e^{|t|}}{\Lambda(n)\over\sqrt n}
                    \bigl(|t|-\log n\bigr)\\
 &-{|t|\over2}\bigl(\psi(1/4)-\log\pi\bigr)\\
 &-{1\over4}\left(
    \Phi(1,2,1/4)
    -e^{-|t|/2}\Phi(e^{-2|t|},2,1/4)
                    \right),                                \tag{2.1}
\end{aligned}
\]

where `Phi` is the Hurwitz--Lerch function.  This is a continuous, real and
even function and `g(0)=0`.  Formula (2.1) is source-defined:

* the sum contains every `n=p^k`, with coefficient
  `Lambda(p^k)/sqrt(p^k)`;
* the last two lines are the integrated complete Gamma term, including its
  finite-part constant;
* the first line is the integrated polar block.

Put

\[
 K_g(t,s)=g(t-s)-g(t)-g(-s)+g(0).                            \tag{2.2}
\]

For a compact interval `I_T=[-T,T]`, (2.2) is a continuous hermitian kernel
and therefore defines a compact self-adjoint integral operator on
`L^2(I_T)`.

The formula (2.1), and the integration identity used below, are the
unconditional content of Suzuki's continuous realization of the Weil form
(`Weil's quadratic form via the screw function`, arXiv:2606.09096,
Theorem 1.1 and Proposition 3.1).  The assertion that (2.2) is positive on
all zero-mass tests is *not* imported: that assertion is equivalent to RH.

## 3. Exact derivative equivalence

Let `F in C_c^infinity((-T,T))` and put

\[
 u=F'.                                                       \tag{3.1}
\]

Then `int u=0`.  Integration by parts gives, for
`sigma in {+1/2,-1/2}`,

\[
 N_\sigma(u):=\int_{-T}^{T}e^{\sigma t}u(t)\,dt
   =-\sigma\int_{-T}^{T}e^{\sigma t}F(t)\,dt
   =-\sigma M_\sigma(F).                                    \tag{3.2}
\]

Conversely, if `u in C_c^infinity((-T,T))` has zero integral, then

\[
 F(t)=\int_{-T}^{t}u(s)\,ds                                 \tag{3.3}
\]

extends by zero to a compactly supported smooth function after using the
usual compact-core domain (or by density in the closed form domain), and
(3.2) holds.  Thus differentiation is a bijection, after closure, between

\[
 \mathcal P_T=ker M_+\cap\ker M_-                           \tag{3.4}
\]

and

\[
 \mathcal U_T=\left\{u:\int u=0,\quad N_+(u)=N_-(u)=0\right\}.
                                                                    \tag{3.5}
\]

The unconditional continuous-kernel identity is

\[
 QW_T(F,G)
 =\int_{I_T}\!\int_{I_T}
       g(t-s)F'(s)\overline{G'(t)}\,ds\,dt.                  \tag{3.6}
\]

Because both derivatives have zero integral, the three separated terms in
(2.2) vanish after integration.  Hence

\[
 QW_T(F,G)
 =\langle K_{g,T}F',G'\rangle.                              \tag{3.7}
\]

D.49 gives independently

\[
 QW_T(F,G)=\langle M_TF,CM_TG\rangle-B_{{\rm nuc},T}(F,G),
 \qquad
 C=\begin{pmatrix}0&1\\1&0\end{pmatrix}.                  \tag{3.8}
\]

Combining (3.2), (3.7) and (3.8) yields the exact primitive pullback

\[
 \boxed{
 -B_{{\rm nuc},T}(F,G)
 =\langle K_{g,T}F',G'\rangle,
 \qquad F,G\in\mathcal P_T.}                                \tag{3.9}
\]

Thus (3.9) retains every `p^k` and Gamma term already certified in D.32,
but represents their sum by a continuous compact kernel.

## 4. Equivalent continuous Hodge theorem

Equation (3.9) proves the following exact equivalence:

\[
 \boxed{
 B_{{\rm nuc},T}(F,F)\leq0\quad(F\in\mathcal P_T)
 \quad\Longleftrightarrow\quad
 \langle K_{g,T}u,u\rangle\geq0\quad(u\in\mathcal U_T).}   \tag{4.1}
\]

Strict equality on nonzero primitive tests is equivalent to strict
positivity of `K_(g,T)` on `U_T`.  By the compact-support version of Weil's
criterion, proving (4.1) for every `T` proves RH.  Consequently one may not
declare `g` to be a screw function in order to prove (4.1): that declaration
is exactly the missing theorem.

The gain is analytic rather than logical.  The target is now a compact
continuous-kernel problem with two boundary functionals on the already
zero-mass space, rather than an unbounded distributional operator.

## 5. Two-dimensional Schur gate

Work on

\[
 H_T^0=\left\{u\in L^2(I_T):\int u=0\right\},                \tag{5.1}
\]

and let

\[
 N_Tu=(N_-(u),N_+(u)).                                      \tag{5.2}
\]

For a Galerkin compression `G_(T,N)` of `K_(g,T)` on `H_T^0`, assume
temporarily that `G_(T,N)` and

\[
 \mathcal G_{T,N}=N_TG_{T,N}^{-1}N_T^*                     \tag{5.3}
\]

are invertible.  The constrained Haynsworth identity of D.47 gives

\[
 \mathrm{In}\,\bigl(G_{T,N}|_{\ker N_T}\bigr)
 =\mathrm{In}(G_{T,N})-
  \mathrm{In}(\mathcal G_{T,N}).                      \tag{5.4}
\]

This is the continuous screw-kernel version of the two-ruling Green
calculation.  It separates D into two independently checkable statements:

1. an index theorem for the compact kernel (2.2);
2. a two-by-two signature and nondegeneracy theorem for (5.3).

At singular parameters the Moore--Penrose conditions are exactly the ones
in D.47: the boundary vectors must lie in the operator range and no
primitive zero mode may occur.

## 6. Acceptance criterion for the next step

A valid closure from (5.4) must prove the finite-window index and boundary
signature directly from (2.1), uniformly under Galerkin and support
exhaustion.  It may use the positivity of individual local measures, the
Lerch/Gamma representation, total positivity or a source-side oscillation
theorem.  It may not:

* assume that `g` is a screw function;
* complete in the norm defined by `QW` before proving its sign;
* select a positive spectral subspace of `K_(g,T)` by definition;
* use the nontrivial zeta zero divisor to choose the polarization.

With these exclusions, (3.9)--(5.4) give a faithful continuous operator on
which the missing Hodge theorem can be attacked without any distributional
ambiguity.

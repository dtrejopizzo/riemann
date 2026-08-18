# D.145 — Stable analytic Legendre matrix for the Gamma resolvent kernels

## Verdict

The low-block certificate at (T=\tfrac12\log5) must not use a long
Fourier quadrature: the cusp of (e^{-b|x-y|}) produces aliasing precisely
in the high oscillator modes.  It also must not evaluate a polynomial
antiderivative with an (e^{+bT}) boundary term, because that creates a
catastrophic cancellation.

There is an exact stable formula.  Let

\[
 \phi_n(x)=\sqrt{{2n+1\over2T}}P_n(x/T),
 \qquad k=bT>0,                                       \tag{0.1}
\]

and put

\[
 E_{mn}(b,T)=
 \int_{-T}^T\!\int_{-T}^T
 \phi_m(x)e^{-b|x-y|}\phi_n(y)\,dx\,dy.              \tag{0.2}
\]

For each (n), let (Q_n) be the unique polynomial solving

\[
 Q_n'+kQ_n=P_n.                                      \tag{0.3}
\]

Write (Q_n=\sum_jq_{jn}P_j), (q_n^-=Q_n(-1)), and

\[
 e_m^-(k)=2(-1)^me^{-k}i_m(k)
 =2(-1)^m\sqrt{{\pi\over2k}},e^{-k}I_{m+1/2}(k).    \tag{0.4}
\]

Then

\[
 \boxed{
 E_{mn}(b,T)={T\over2}\sqrt{(2m+1)(2n+1)}
 \left[
 {2q_{mn}\over2m+1}-e_m^-(k)q_n^-
 +{2q_{nm}\over2n+1}-e_n^-(k)q_m^-
 \right].}                                           \tag{0.5}
\]

Every factor in (0.5) is bounded or exponentially scaled.  In particular,
there is no (e^{+k}).  Formula (0.5), exact polynomial integration for
the three translated contacts (2,3,4), and exact exponential moments
reduce the entire constrained low block to finitely many evaluations of
(\log5), scaled Bessel functions and rational operations.  This is the
correct input for an interval LDL/Cholesky certificate.

No sign of the final block is asserted here.  The formula replaces two
unreliable numerical assemblies by an exact one.  The paper is not
modified.

## 1. Polynomial resolvent

The derivative of a Legendre polynomial is

\[
 P_\ell'(u)=
 \sum_{\substack{0\leq j<\ell\\ \ell-j\ {m odd}}}
 (2j+1)P_j(u).                                        \tag{1.1}
\]

Hence (D+kI) is upper triangular on polynomials of degree at most (n),
with diagonal (k>0).  Equation (0.3) therefore has a unique polynomial
solution.  Its coefficients are obtained by descending substitution:

\[
 kq_{jn}+(2j+1)
 \sum_{\substack{j<\ell\leq n\\ \ell-j\ {m odd}}}
 q_{\ell n}=\delta_{jn}.                              \tag{1.2}
\]

This recurrence uses only rational operations and (k).  For small (k)
it must be evaluated with enough precision because the final polynomial is
a cancellation of large coefficients; this is a precision issue, not a
singularity of (0.5).

## 2. The stable one-sided Green integral

Define

\[
 q_n(u)=\int_{-1}^{u}e^{-k(u-v)}P_n(v)\,dv.           \tag{2.1}
\]

It satisfies

\[
 q_n'+kq_n=P_n,qquad q_n(-1)=0.                      \tag{2.2}
\]

Comparison with (0.3) gives the exact identity

\[
 \boxed{q_n(u)=Q_n(u)-Q_n(-1)e^{-k(u+1)}.}            \tag{2.3}
\]

The second term decays from the left boundary; no growing exponential is
present.

The Laplace--Legendre integral is

\[
\begin{aligned}
 \int_{-1}^1P_m(u)e^{-k(u+1)}\,du
 &=e^{-k}\int_{-1}^1P_m(u)e^{-ku}\,du\\
 &=2(-1)^me^{-k}i_m(k)=e_m^-(k),                     \tag{2.4}
\end{aligned}
\]

which proves (0.4).  The scaled Bessel expression remains of polynomial
size as (k\to\infty).

## 3. Proof of the matrix formula

On the lower triangle (v\leq u), (2.1)--(2.3) give

\[
\begin{aligned}
 I_{mn}^{\triangle}(k)
 &:=\int_{-1}^1P_m(u)
       \int_{-1}^{u}e^{-k(u-v)}P_n(v)\,dv\,du\\
 &=\int_{-1}^1P_m(u)Q_n(u)\,du
   -Q_n(-1)e_m^-(k)\\
 &={2q_{mn}\over2m+1}-q_n^-e_m^-(k).                \tag{3.1}
\end{aligned}
\]

The upper triangle is the same expression with (m,n) exchanged.  The
diagonal has measure zero, so

\[
 \int_{-1}^1\!\int_{-1}^1
 P_m(u)e^{-k|u-v|}P_n(v)\,du\,dv
 =I_{mn}^{\triangle}+I_{nm}^{\triangle}.             \tag{3.2}
\]

Finally (x=Tu,y=Tv) in (0.2) contributes the normalization

\[
 {T\over2}\sqrt{(2m+1)(2n+1)},                       \tag{3.3}
\]

and (0.5) follows.

As a normalization check, (m=n=0) gives

\[
 \int_{-1}^1\!\int_{-1}^1e^{-k|u-v|}\,du\,dv
 ={4\over k}-{2(1-e^{-2k})\over k^2}.                \tag{3.4}
\]

## 4. The other low-block entries

For a translated contact (a<T\cdot2), put (d=a/T).  Its normalized
Legendre entry is

\[
 C_{mn}(a,T)
 ={1\over2}\sqrt{(2m+1)(2n+1)}
 \int_{-1}^{1-d}P_m(u)P_n(u+d)\,du.                  \tag{4.1}
\]

The integrand is a polynomial of degree (m+n).  Thus (4.1) is exactly
computable by polynomial antiderivatives or by Gauss--Legendre quadrature
of order greater than ((m+n)/2), with interval nodes and weights.

The two Tate moment columns are

\[
 M_{\sigma,n}(T)
 =\int_{-T}^T\phi_n(x)e^{\sigma x}\,dx
 =2\sqrt{{T(2n+1)\over2}},i_n(\sigma T),
 \qquad \sigma=\pm{1\over2},                         \tag{4.2}
\]

where (i_n(-z)=(-1)^ni_n(z)).  Therefore the two constraints also need
no physical or Fourier quadrature.

Equations (0.5), (4.1) and (4.2) give an analytic center and an interval
radius for every entry of the (170\)-mode block selected in D.94.  A
directed congruence must still prove that the interval block restricted by
the two moment columns is positive; a floating eigenvalue is not accepted.

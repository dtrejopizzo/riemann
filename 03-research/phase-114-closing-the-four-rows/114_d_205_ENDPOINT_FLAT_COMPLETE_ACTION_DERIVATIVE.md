# D.205 — Complete twentieth derivative on the endpoint-flat safe space

## Verdict

For the endpoint-flat space used at \(T=\tfrac12\log6\), the derivative
Gram required by D.204 has a cancellation-free one-dimensional formula.
The twentieth weak derivative of the complete row-D action contains:

* a finite polynomial interior Gamma term;
* endpoint layers \(H_s\), with only \(H_1\) logarithmically singular;
* the twentieth derivatives of the four active contacts
  \(n=2,3,4,5\);
* the constant Gamma mass.

There are no delta masses at the translated cut points because the first
nineteen endpoint jets vanish.  This reduces the outstanding tail capacity
to a finite interval quadrature.  The note supplies that reduction; it does
not assert the numerical Schur sign.

## 1. Endpoint-flat domain

Put \(M=20\) and

\[
 F(t)=\left(1-{t^2\over T^2}\right)^M R(t),            \tag{1.1}
\]

where \(R\) is a polynomial.  Then

\[
 F^{(r)}(\pm T)=0\qquad(0\le r<M).                    \tag{1.2}
\]

If \(\widetilde F\) denotes zero extension to the real line, (1.2) implies
in distributions

\[
 D^M\widetilde F=\widetilde{F^{(M)}}.                 \tag{1.3}
\]

Indeed, the boundary terms in the repeated distributional integration by
parts are precisely the jets in (1.2).  It follows for
\(C_aF(t)=\widetilde F(t+a)+\widetilde F(t-a)\) that

\[
 D^MC_aF=C_a(F^{(M)}).                                \tag{1.4}
\]

Thus every translated contact belongs to the weighted derivative domain
of D.204, despite its internal cut points.

## 2. Differentiating the complete Gamma action

Use the notation of D.150,

\[
 H_s(x)=\sum_{j\ge0}{e^{-(2j+1/2)x}\over(2j+1/2)^s},
 \qquad H_s'(x)=-H_{s-1}(x).                          \tag{2.1}
\]

For a polynomial \(F\) of degree \(d\), D.150 gives

\[
\begin{aligned}
G_\Gamma F(t)={}&-2\sum_{\substack{2\le r\le d\\r\ {m even}}}
 2^{-(r+1)}\zeta(r+1,1/4)F^{(r)}(t)\\
&+\sum_{r=0}^d(-1)^rF^{(r)}(-T)H_{r+1}(t+T)\\
&+\sum_{r=0}^dF^{(r)}(T)H_{r+1}(T-t).
\end{aligned}                                         \tag{2.2}
\]

Using (1.2) and differentiating (2.2) exactly \(M\) times gives, for even
\(M=20\),

\[
\boxed{
\begin{aligned}
D^MG_\Gamma F(t)={}&-2
 \sum_{\substack{2\le r\le d-M\\r\ {m even}}}
 2^{-(r+1)}\zeta(r+1,1/4)F^{(r+M)}(t)\\
&+\sum_{r=M}^d(-1)^rF^{(r)}(-T)H_{r+1-M}(t+T)\\
&+\sum_{r=M}^dF^{(r)}(T)H_{r+1-M}(T-t).
\end{aligned}}                                        \tag{2.3}
\]

The smallest suffix in the boundary sums is \(1\).  Since
\(H_1(x)=-\tfrac12\log x+O(1)\) and every \(H_s\), \(s>1\), is bounded at
zero, (2.3) has only logarithmic endpoint singularities.

## 3. Completed derivative

Let

\[
 A_T=G_\Gamma-m_0I-
 \sum_{n\in\{2,3,4,5\}}{\Lambda(n)\over\sqrt n}C_{\log n},
 \qquad m_0=\log\pi-\psi(1/4).                        \tag{3.1}
\]

Combining (1.4) and (2.3),

\[
 \boxed{
 D^MA_TF=D^MG_\Gamma F-m_0F^{(M)}-
 \sum_{n\in\{2,3,4,5\}}{\Lambda(n)\over\sqrt n}
 C_{\log n}(F^{(M)}).}                               \tag{3.2}
\]

This includes the prime square \(4=2^2\), with
\(\Lambda(4)=\log2\); no mixed integer is inserted.

The weighted integrand in D.204 is

\[
 \left(1-{t^2\over T^2}\right)^M
 (D^MA_TF_i)(t)\overline{(D^MA_TF_j)(t)}.             \tag{3.3}
\]

Near either endpoint it is bounded by
\(C x^M(1+|\log x|^2)\), hence is integrable.  On the interior it is
piecewise analytic.  Splitting \((-T,T)\) at
\(\pm T\mp\log n\), for every active \(n\), leaves a finite list of
ordinary intervals on which directed Gauss--Jacobi or tanh--sinh
quadrature applies.

## 4. Certificate obligations

A full interval certificate must retain all of the following:

1. an exact or interval-enclosed primitive endpoint-flat frame;
2. the complete expression (3.2), rather than a truncated oscillator sum;
3. outward-rounded quadrature errors for (3.3), including the two endpoint
   logarithms;
4. an interval lower factor for the finite safe Gram \(B=S^*A_TS\);
5. the sharp D.204 coefficient and the primitive graph correction;
6. the corrected low block and cross term from D.200.

Only after these six objects have compatible directed signs does the
endpoint become a theorem.


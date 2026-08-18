# Regularised Euler generating identity

## Purpose

This note gives an exact Euler-product generating identity for the Li/A1
family, with a regulator that makes every prime sum absolutely convergent.
It also records why the identity is not itself a positivity proof.  In
particular, the unregularised coefficientwise Euler expansion at the Li
base point is invalid: the Euler factor has a pole there and its apparent
prime coefficient is divergent.

No zero-location assertion is used below.

## 1. The regulator and its domain

Fix \(\varepsilon>0\), put \(a=1+\varepsilon\), and set
\[
 s_a(z)={a\over1-z},\qquad |z|<\varepsilon.
\]
For \(|z|\le r<\varepsilon\),
\[
 \Re s_a(z)\ge {a\over1+r}>1.                                      \tag{1}
\]
Thus the Euler logarithm is absolutely and locally uniformly convergent:
\[
 \log\zeta(s_a(z))
 =\sum_{m\ge2}{\Lambda(m)\over\log m}\,m^{-a}
   \exp\!\left(-{a(\log m)z\over1-z}\right).                       \tag{2}
\]
The Laguerre generating function with parameter \(-1\) is
\[
 \exp\!\left(-{xz\over1-z}\right)
 =\sum_{j\ge0}L_j^{(-1)}(x)z^j.                                      \tag{3}
\]

> **Proposition 1 (regularised prime coefficients).**  For every
> \(n\ge1\) and \(\varepsilon>0\),
> \[
> \boxed{
> n[z^n]\log\zeta\!\left({1+\varepsilon\over1-z}\right)
> =-(1+\varepsilon)\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
> L_{n-1}^{(1)}\bigl((1+\varepsilon)\log m\bigr).}                  \tag{4}
> \]

*Proof.*  Estimate the absolute value of the summands in (2) by the Euler
series at the exponent in (1).  This proves normal convergence on
\(|z|\le r\), so (3) may be inserted and coefficients may be exchanged
with the \(m\)-sum.  Finally use the exact identity
\[
 nL_n^{(-1)}(x)=-xL_{n-1}^{(1)}(x).
\]
This gives (4). \(\square\)

## 2. Completed identity and the limiting Li coefficient

Define the completely explicit regulator-dependent archimedean coefficient
\[
 \mathcal A_{n}(\varepsilon)
 :=n[z^n]\log\!\left[
 {1\over2}s_a(z)(s_a(z)-1)\pi^{-s_a(z)/2}
 \Gamma\!\left({s_a(z)\over2}\right)\right].                       \tag{5}
\]
The logarithm is analytic in a sufficiently small disk about zero because
\(\Re s_a(z)>1\) there.  Combining (4) with the defining product for
\(\xi\) gives the exact identity
\[
 \boxed{
 \lambda_n(\varepsilon)
 :=n[z^n]\log\xi\!\left({1+\varepsilon\over1-z}\right)
 =\mathcal A_n(\varepsilon)
 -(1+\varepsilon)\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}\bigl((1+\varepsilon)\log m\bigr).}                  \tag{6}
\]

Since \(\xi(1)\ne0\), the completed logarithm is analytic jointly near
\((\varepsilon,z)=(0,0)\).  Hence, for each fixed \(n\),
\[
 \lim_{\varepsilon\downarrow0}\lambda_n(\varepsilon)=\lambda_n.    \tag{7}
\]
The two terms on the right of (6) generally diverge separately in this
limit.  This is not a defect: it is the exact cancellation of the zeta pole
against the completed pole factor.  In particular, the tempting expression
\[
 -\sum_{m\ge2}{\Lambda(m)\over m}L_{n-1}^{(1)}(\log m)               \tag{8}
\]
is not an ordinary convergent prime formula for \(\lambda_n\).  Any use of
it must retain the regulator and the compensating term \(\mathcal A_n\).

## 3. Positivity test and exact factorwise obstruction

An Euler--Gamma positivity theorem strong enough to close A1 could, for
example, establish a uniform one-sided limit inequality for the right side
of (6) which implies
\[
 \liminf_{\varepsilon\downarrow0}\lambda_n(\varepsilon)\ge0
 \qquad(n\ge1).                                                       \tag{9}
\]
Together with (7), that is Li positivity and therefore RH.  Formula (6)
is a legitimate target because it was derived entirely in \(\Re s>1\)
and then passed to a completed, locally analytic limit; it does **not**
assume a bound for \(\sum_\rho e^{\rho u}/\rho^2\), or any zero location.

It is nevertheless not enough to invoke positivity of the Euler factors.
For the single positive local factor
\[
 Z_p(s)=(1-p^{-s})^{-1},
\]
the \(n=1\) instance of (4) is exactly
\[
 [z]\log Z_p\!\left({a\over1-z}\right)
 =-{a\log p\over p^a-1}<0.                                         \tag{10}
\]
Thus a factor with positive Euler/Dirichlet coefficients produces a
strictly negative transformed coefficient.  This algebraic counterexample
rules out every termwise or factorwise-positivity proof of (9).

The identity does use a property absent from the broad monotone competitors:
the exact Euler rigidity
\[
 \Lambda(p^k)=\log p\quad(k\ge1),\qquad \Lambda(m)=0
 \quad\text{for non-prime-powers}.                                   \tag{11}
\]
But (10) shows that (11) alone supplies no sign.  A successful inequality
must make a genuinely global comparison between the collective prime sum in
(6) and the Gamma/pole coefficient \(\mathcal A_n(\varepsilon)\).  No such
comparison is proved here.

## 4. Relation to the direct A1 integral

The finite-window identity of `103_12` is the real-variable analogue of
the cancellation in (6): a divergent or large signed prime object becomes
manageable only after its exact compensating endpoint terms are retained.
For the expanding A1 interval, (6) does not turn the sign-changing Laguerre
weights into positive ones.  It therefore supplies a rigorous global
coordinate and eliminates an invalid unregularised Euler expansion, but it
does not close the RH-strength A1 gate.

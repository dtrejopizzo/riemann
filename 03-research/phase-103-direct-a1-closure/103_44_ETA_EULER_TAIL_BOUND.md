# Euler-transformed eta generator: an explicit geometric tail

Put

\[
 \eta(1+t)=\sum_{k\ge0}2^{-k-1}H_k(t),\qquad
 H_k(t)=\sum_{j=0}^k(-1)^j{k\choose j}(j+1)^{-1-t}. \tag{1}
\]

This is the Euler/Hasse transform.  Unlike the alternating Dirichlet series,
it has a uniform geometric tail for the Taylor data needed at \(t=0\).

## Uniform tail lemma

For \(|t|\le1/2\), the beta-integral identity gives

\[
 H_k(t)=\frac1{\Gamma(1+t)}
 \int_0^\infty x^t e^{-x}(1-e^{-x})^kdx. \tag{2}
\]

The Weierstrass product for reciprocal Gamma, with \(\gamma<1\) and
\(\zeta(2)<2\), gives

\[
 \left|\Gamma(1+t)^{-1}\right|
 \le\exp\left(\tfrac12+
 \frac{(1/2)^2}{2(1-1/2)}\zeta(2)\right)<3. \tag{3}
\]

The estimate must retain both signs of \(\Re t\).  For \(|t|\le1/2\),
\(x^{\Re t}\le x^{-1/2}+x\).  After \(y=e^{-x}\), and using
\(-\log y\ge1-y\),

\[
\begin{aligned}
 \int_0^\infty x^{\Re t}e^{-x}(1-e^{-x})^kdx
 &\le\frac2{k+1}+\int_0^1(-\log y)(1-y)^kdy\\
 &=\frac{2+H_{k+1}}{k+1}
 \le\frac{3+\log(k+1)}{k+1}. \tag{4}
\end{aligned}
\]

Thus

\[
 \boxed{|H_k(t)|\le\frac{9+3\log(k+1)}{k+1}\quad(|t|\le1/2).} \tag{5}
\]

The right side of (5) decreases with \(k\).  Hence, for the tail after
\(K-1\), (1) and Cauchy's coefficient estimate imply

\[
 \left|[t^m]\sum_{k\ge K}2^{-k-1}H_k(t)\right|
 \le\frac{(9+3\log(K+1))2^{m-K}}{K+1}. \tag{6}
\]

## Division to obtain (t\zeta(1+t))

Set \(d(t)=(1-2^{-t})/t\), with \(d(0)=\log2\).  On \(|t|\le1/2\),

\[
 \left|d(t)/\log2-1\right|
 \le e^{(\log2)/2}-1=\sqrt2-1,
\]

so \(|d(t)^{-1}|<3\) (using \(\log2>2/3\) and
\(2-\sqrt2>1/2\)).  This is a supnorm bound on the same disk, so Cauchy's
estimate applies to the quotient error.  Since
\(t\zeta(1+t)=\eta(1+t)/d(t)\), the corresponding coefficient error is

\[
 \boxed{\left|[t^m]\,\mathrm{error}\bigl(t\zeta(1+t)\bigr)\right|
 \le\frac{(27+9\log(K+1))2^{m-K}}{K+1}.} \tag{7}
\]

For \(m\le149\), choosing \(K=830\) makes (7) smaller than \(10^{-200}\).
This is a proved geometric tail, substantially better suited than the
high-order Euler--Maclaurin remainder for the requested constants.

## Computational frontier

The finite sum through \(K=829\) still has alternating binomial terms of
size about \(2^{829}\).  A fixed-point implementation can handle this with
a common scale chosen above the roughly 247 decimal cancellation digits plus
the desired output precision; every \(\log(j+1)\) can be enclosed by the
rational `artanh` series already used in `103_35`.  This note proves the
tail and parameter budget.  It does not claim that the finite fixed-point
sum through 829, nor the resulting range through 149, has yet been executed.

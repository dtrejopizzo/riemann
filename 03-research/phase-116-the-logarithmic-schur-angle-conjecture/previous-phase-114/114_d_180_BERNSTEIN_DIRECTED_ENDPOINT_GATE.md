# D.180 — Bernstein-directed endpoint gate

## Purpose

The five-dimensional endpoint problem at

\[
        T={1\over2}\log 5
\]

has already been reduced to fifteen scalar integrals.  Expanding the
degree-199 Legendre columns and the degree-288 analytic Gamma action in
monomials is exact, but it is a poor directed representation: individual
coefficients are enormous whereas the final Gram entries are small.  This
note gives an equivalent cellwise Bernstein calculation in which all
logarithmic moments are closed formulae.  It is a numerical representation
theorem only; it changes neither the form nor the Feshbach inequality.

## 1. Stable polynomial basis

Write

\[
 B_{k,n}(x)={n\choose k}x^k(1-x)^{n-k},\qquad 0\le k\le n.
\]

The shifted Legendre polynomial has the exact Bernstein expansion

\[
 P_n(2x-1)=\sum_{k=0}^n(-1)^{n+k}{n\choose k}B_{k,n}(x).       \tag{1.1}
\]

This follows by comparing the Rodrigues formula with the Bernstein
derivative formula, or directly by expanding both sides.  Products do not
require a dense change of basis:

\[
 B_{i,n}B_{j,m}
 ={ {n\choose i}{m\choose j}\over {n+m\choose i+j}}
 B_{i+j,n+m}.                                         \tag{1.2}
\]

Degree elevation is likewise positive:

\[
 B_{k,n}={n+1-k\over n+1}B_{k,n+1}
          +{k+1\over n+1}B_{k+1,n+1}.                \tag{1.3}
\]

Consequently interval radii are propagated without the alternating
monomial cancellation which occurred in the first Arb implementation.

## 2. Exact endpoint logarithmic moments

Put

\[
 H_r=\sum_{j=1}^r{1\over j},\qquad
 H_r^{(2)}=\sum_{j=1}^r{1\over j^2},
\]

with \(H_0=H_0^{(2)}=0\).  Differentiating Euler's beta integral gives

\[
 \int_0^1B_{k,n}(x)\,dx={1\over n+1},                \tag{2.1}
\]

\[
 \int_0^1B_{k,n}(x)\log x\,dx
 ={H_k-H_{n+1}\over n+1},                            \tag{2.2}
\]

\[
 \int_0^1B_{k,n}(x)\log(1-x)\,dx
 ={H_{n-k}-H_{n+1}\over n+1},                        \tag{2.3}
\]

\[
 \int_0^1B_{k,n}(x)\log^2x\,dx
 ={(H_k-H_{n+1})^2+H_{n+1}^{(2)}-H_k^{(2)}\over n+1},\tag{2.4}
\]

\[
 \int_0^1B_{k,n}(x)\log^2(1-x)\,dx
 ={(H_{n-k}-H_{n+1})^2+H_{n+1}^{(2)}-H_{n-k}^{(2)}
   \over n+1},                                       \tag{2.5}
\]

and

\[
\begin{split}
 \int_0^1B_{k,n}(x)\log x\log(1-x)\,dx
 ={1\over n+1}\big[& (H_k-H_{n+1})(H_{n-k}-H_{n+1})\\
                     &-\zeta(2)+H_{n+1}^{(2)}\big]. \tag{2.6}
\end{split}
\]

Thus the complete singular--singular block is a finite rational--\(\zeta(2)\)
combination in Bernstein coordinates.

## 3. Contact cells

For a contact cell \(I=[a,a+h]\), use \(x=a+h\xi\).  Polynomial
restriction and degree elevation are affine Bernstein operations.  On the
two boundary cells, the singular logarithm is

\[
 \log x=\log h+\log\xi
 \quad\hbox{or}\quad
 \log(1-x)=\log h+\log(1-\xi),                       \tag{3.1}
\]

so (2.1)--(2.6) apply verbatim.  On every interior cell both logarithms
are analytic.  Their Taylor series about the midpoint have ratio

\[
 \rho_I={h\over 2\min(a,1-a-h)}<1,                  \tag{3.2}
\]

and the remainder after order \(r\) is bounded directly by the geometric
majorant

\[
 {\rho_I^{r+1}\over(r+1)(1-\rho_I)}.                \tag{3.3}
\]

After multiplication by the Bernstein polynomial, (2.1) bounds its
integral because \(B_{k,n}\ge0\) and has mass \((n+1)^{-1}\).

## 4. Directed Feshbach criterion

Let \(\mathbf H\) be the resulting interval Gram, let \(\mathbf K\) be
the already directed five-dimensional Schur block, and let
\(\gamma>0.218\) be the certified complement gap.  Define

\[
       \mathbf S=\mathbf K-\gamma^{-1}\mathbf H.     \tag{4.1}
\]

For any rational or outward-rounded preconditioner \(P\), positivity is
certified if

\[
 (P^*\mathbf SP)_{ii}
   -\sum_{j\ne i}|(P^*\mathbf SP)_{ij}|>0
 \quad(1\le i\le5).                                 \tag{4.2}
\]

Equations (1.1)--(3.3) prove that every entry used in (4.2) encloses the
exact continuum Gram, including the endpoint logarithms, all active
prime-power translations and the analytic Gamma remainder.  Hence a PASS
of (4.2), together with the existing finite block and complement
certificates, proves positivity of the full primitive endpoint operator;
it is not a Galerkin assertion.


# Euler truncation with simultaneous continuous renormalisation

## Purpose

This note tests a genuinely Euler-specific approximation, unavailable to the
finite theta competitors.  The truncated Euler product is renormalised by
the continuous prime-number-theorem mass before the pole limit is taken.
The resulting coefficient identities are exact, but individual prime jumps
already have both signs.  Thus truncation in the prime cutoff has no useful
monotonicity for A1.

## 1. Exact renormalised product

For \(X>2\) and \(\Re s>1\), define
\[
 \log\zeta_X(s)=\sum_{p\le X}\sum_{k\ge1}{p^{-ks}\over k},
\]
and choose the continuous main-mass factor
\[
 C_X(s)=\int_2^X{x^{-s}\over\log x}\,dx,
 \qquad P_X(s)=\exp C_X(s).                                         \tag{1}
\]
It has exactly the requested logarithmic-derivative mass:
\[
 -{d\over ds}\log P_X(s)=\int_2^Xx^{-s}\,dx.                       \tag{2}
\]
Put \(R_X(s)=\log\zeta_X(s)-C_X(s)\).  The pole is retained, rather than
discarded, through the exact decomposition
\[
 \log\bigl((s-1)\zeta_X(s)\bigr)
 =R_X(s)+\bigl(\log(s-1)+C_X(s)\bigr).                              \tag{3}
\]
For \(\Re s>1\), all expressions are ordinary absolutely convergent finite
prime sums or integrals.  As \(X\) tends to infinity, the second bracket in
(3) is precisely the continuous term which cancels the logarithmic pole;
it must remain present before that limit.

## 2. Exact Li--Laguerre coefficients

Use \(a=1+\varepsilon>1\), \(s_a(z)=a/(1-z)\), and \(n\ge1\).  Normal
convergence gives
\[
 n[z^n]\log\zeta_X(s_a(z))
 =-a\sum_{p\le X}\sum_{k\ge1}\log p\,p^{-ka}
     L_{n-1}^{(1)}(ak\log p),                                      \tag{4}
\]
whereas changing variables \(u=\log x\) in (1) gives
\[
 n[z^n]C_X(s_a(z))
 =-a\int_{\log2}^{\log X}e^{-(a-1)u}
     L_{n-1}^{(1)}(au)\,du.                                         \tag{5}
\]
Consequently the renormalised residual has the exact coefficient
\[
 \boxed{
 n[z^n]R_X(s_a(z))
 =a\left[
 \int_{\log2}^{\log X}e^{-(a-1)u}L_{n-1}^{(1)}(au)\,du
 -\sum_{p\le X}\sum_{k\ge1}\log p\,p^{-ka}
     L_{n-1}^{(1)}(ak\log p)\right].}                              \tag{6}
\]
This is an Euler-specific, pole-renormalised version of the signed A1
correlation.  The remaining bracket in (3), as well as the Gamma factor,
must be added for the completed Li coefficient.

## 3. One prime already destroys cutoff monotonicity

The factor \(P_X\) is continuous in \(X\).  Hence at a prime \(p\), the
jump of (6) is exactly the local Euler contribution.  With \(q=p^{-a}\)
the first three jumps are
\[
 \Delta_{p,1}=-{a\log p\,q\over1-q}<0,                              \tag{7}
\]
\[
 \Delta_{p,2}=
 {a\log p\,q\over(1-q)^2}
 \left[a\log p-2(1-q)\right],                                      \tag{8}
\]
\[
 \Delta_{p,3}=-a\log p\left[
 {3q\over1-q}-{3a(\log p)q\over(1-q)^2}
 +{a^2(\log p)^2q(1+q)\over2(1-q)^3}\right].                       \tag{9}
\]
These are obtained by summing respectively \(1\), \(2-x\), and
\(3-3x+x^2/2\) against the geometric powers \(q^k\).

Equation (8) has both signs.  At \(a=1,p=2\), its bracket is
\(\log2-1<0\), and the same remains true for \(a>1\) sufficiently close
to one.  For every fixed \(a>1\), the bracket is positive for all
sufficiently large primes.  Therefore the second coefficient of the
renormalised product is neither nondecreasing nor nonincreasing at the
prime jumps.  Formula (9) gives the analogous signed cubic kernel; its
large-prime sign is controlled by
\(L_2^{(1)}(a\log p)\), which also changes sign before becoming positive.

No continuous variation of \(P_X\) between primes can remove this
obstruction, because it has no jump at the prime itself.  In particular,
there is no prime-cutoff monotonicity which could pass a finite Euler-product
positivity statement to the limit.

## 4. Why an absolute repair is not competitive

Taking absolute values in (6) replaces the signed prime measure by a
positive mass of order at least its original Euler mass and loses the
Laguerre cancellation.  It is therefore the same absolute-load failure
already exposed in the direct A1 route, now with the extra continuous
renormalisation term.  The construction is useful only as an exact
renormalised identity; it supplies no new bound of order \(n\log n\).

## Status

The simultaneous pole renormalisation is valid and retains all endpoint
terms.  Its individual Euler increments have both signs already at order
two, so it cannot provide the required uniform A1 inequality through
monotonicity in the Euler cutoff.

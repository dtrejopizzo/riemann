# Selberg convolution: exact positive coefficients, signed Laguerre pullback

## Purpose

This note tests whether the multiplicative rigidity absent from the theta
counterexamples can repair A1.  In the half-plane of absolute convergence,
Selberg's differentiated Euler identity does create a Dirichlet series with
nonnegative coefficients.  The exact Laguerre pullback, however, immediately
reintroduces a signed kernel.  Thus coefficient positivity of
\(\Lambda*\Lambda\) does not supply the desired A1 sign.

## 1. Positive Selberg coefficients

For \(\Re s>1\), put \(L(s)=-\zeta'(s)/\zeta(s)\).  Then
\[
 L(s)=\sum_{m\ge2}\Lambda(m)m^{-s},
\]
and termwise differentiation and multiplication are absolutely justified.
Consequently
\[
 {\zeta''\over\zeta}(s)=-L'(s)+L(s)^2
 =\sum_{m\ge1}A(m)m^{-s},                                          \tag{1}
\]
where
\[
 \boxed{\ A(m)=\Lambda(m)\log m+(\Lambda*\Lambda)(m)\ge0.\ }       \tag{2}
\]
This is the desired Selberg-type positive arithmetic measure.

## 2. Its exact transformed kernels

Use the regulator of `103_14`, \(a=1+\varepsilon>1\) and
\(s_a(z)=a/(1-z)\).  For every integer \(r\ge0\), normal convergence in
\(|z|<\varepsilon\) gives
\[
 {D(s_a(z))\over(1-z)^{r+1}}
 =\sum_{n\ge0}z^n
   \sum_{m\ge1}d(m)m^{-a}L_n^{(r)}(a\log m),                        \tag{3}
\]
whenever \(D(s)=\sum d(m)m^{-s}\) is absolutely convergent there.
Indeed, (3) is exactly the Laguerre generating function after interchanging
the normally convergent sums.

Taking \(D=\zeta''/\zeta\) inserts the positive coefficients (2), but its
kernel is still signed.  Already the first three kernels are
\[
 L_0^{(r)}(x)=1,
 \qquad L_1^{(r)}(x)=r+1-x,
 \qquad
 L_2^{(r)}(x)={ (r+1)(r+2)\over2}-(r+2)x+{x^2\over2}.                \tag{4}
\]
Thus for every fixed \(r\), the \(n=1\) kernel is negative for
\(x>r+1\), while the \(n=2\) kernel changes sign between its two positive
zeros.  Positivity of \(A(m)\) is therefore not preserved by the exact
conformal/Laguerre transformation.

This includes the derivatives which arise naturally from the change of
variable.  Each factor \((1-z)^{-q}\) merely increases \(r\) in (3); it
cannot remove the negative tail \(-x\) in the \(n=1\) kernel.  Hence no
finite positive linear combination of these Selberg derivative pullbacks
can yield coefficientwise positivity without a further, sign-sensitive
comparison of the actual arithmetic mass.

## 3. Relation to the regularised Li coefficient

The prime term in `103_14` is the \(r=0\) pullback of a logarithmic
derivative and has the same obstruction.  Replacing \(\Lambda\) by the
stronger positive measure \(A\) changes its size but not the sign geometry.
Estimating (3) by absolute values is worse, not better: (2) contains the
submeasure \(\Lambda(m)\log m\), so it discards at least the oscillatory
information already needed for the original \(\Lambda\)-sum and adds the
nonnegative convolution mass.

The pole and Gamma terms have not been dropped in this test: they remain in
the completed identity `103_14`, equation (6).  Equations (1)--(4) show
only that the proposed *arithmetic positive part* cannot be inserted as a
separately positive replacement for its signed prime term.  A viable
Selberg route would need a new identity coupling (2) to the completed
Gamma/pole contribution before the Laguerre pullback; none is supplied by
the Dirichlet-series positivity alone.

## Status

The Selberg convolution gives a real additional rigidity of \(\Lambda\),
but its straightforward use fails at the exact kernels (4).  This is a
kernel-sign obstruction, not an appeal to a monotone competitor or to an
absolute envelope.

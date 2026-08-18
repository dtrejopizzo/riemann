# Li moment renormalization obstruction

## Purpose

The Toeplitz, Fejer and Poisson gates in `161`--`166` are correct as moment
theorems for finite positive measures on the circle.  This note records a
necessary correction for the Li zero divisor:

an ordinary finite Herglotz measure cannot directly be the unweighted
completed nontrivial-zero divisor in Li normalization.

Therefore any successful positive-boundary route must specify its
renormalization before applying the finite circle moment theorem.

## Finite measure bound

Let \(\nu\) be a finite positive measure on \(\partial\mathbb D\), with
moments
\[
  m_k=\int_{\partial\mathbb D}\zeta^k\,d\nu(\zeta).
\]

Then
\[
  |m_k|\le m_0=\nu(\partial\mathbb D)
  \qquad(k\in\mathbb Z).
\tag{1}
\]

If Li coefficients were represented by the naive finite-measure formula
\[
  \lambda_n=m_0-m_n,
\tag{2}
\]
then
\[
  |\lambda_n|\le 2m_0
  \qquad(n\ge1).
\tag{3}
\]

Thus a finite measure with bounded moments can only produce a bounded
sequence through the difference \(m_0-m_n\).

## Conflict with the unweighted zero divisor

The Li formula is a paired sum over the nontrivial zero divisor:
\[
  \lambda_n=\sum_\rho\left(1-\left(1-{1\over\rho}\right)^n\right),
\tag{4}
\]
with the usual symmetric limiting prescription.

This is not the moment difference of a finite measure placing unit mass at
each transformed zero.  The zero divisor is infinite, and the expression
(4) is defined by pairing and renormalization, not by an absolutely
convergent finite-mass integral.

Consequently, the implication
\[
  \hbox{finite positive measure with moments }m_k
  \quad\Longrightarrow\quad
  \lambda_n=m_0-m_n
\tag{5}
\]
is not available for the actual unweighted Li divisor without an additional
renormalization map.

## Corrected positive-boundary target

A valid positive-boundary theorem must choose one of the following precise
frameworks.

### 1. Weighted finite measure plus recovery operator

Construct a finite positive measure \(\nu\) with moments \(m_k\), together
with an explicit positivity-preserving linear or differential recovery
operator \(\mathcal R\), such that
\[
  \lambda_n=\mathcal R_n(m_0,m_1,\ldots)
\tag{6}
\]
and the singularities of the associated analytic object encode the
unweighted zero divisor.

The recovery operator cannot be arbitrary: it must preserve enough positivity
to imply \(\lambda_n\ge0\).

### 2. Renormalized Herglotz current

Construct a positive current or distributional boundary object whose
subtracted moments are finite and satisfy the paired Li normalization.

In this setting, the Toeplitz condition is not simply
\[
  [m_{j-k}]\ge0.
\]
One must state the exact cone of admissible test functions and prove
positivity on that cone.

### 3. Vanishing-test Hilbert space

Work in a Hilbert space where the tests vanish strongly enough at the
renormalization point to make the infinite divisor action finite.  The Li
test
\[
  1-z^n
\]
vanishes at \(z=1\), suggesting a possible quotient or Dirichlet-type norm.

This would replace the finite Herglotz moment matrix by a renormalized
kernel acting on differences or vanishing polynomials.  Positivity of this
kernel would need to imply the Li square tests and the support theorem.

## Consequence for Schur margins

The identity
\[
  \lambda_n={1\over2}Q_n(1-z^n)
\tag{7}
\]
is valid only after a moment normalization in which the quadratic form
\(Q_n\) is finite on the vanishing polynomial \(1-z^n\).

For an ordinary finite measure, (7) is elementary but too small to encode the
unweighted infinite zero divisor.  For the actual Li problem, \(Q_n\) must be
a renormalized Euler--Gamma quadratic form, not merely the quadratic form of
a finite measure with bounded moments.

Thus the Schur margin theorem from `164_A1_TOEPLITZ_SCHUR_MARGIN.md` should
be read as:

1. construct the renormalized Euler--Gamma Toeplitz/Schur form;
2. prove it is positive on the required vanishing-polynomial cone;
3. prove the archimedean margin
   \[
     Q_n(1-z^n)\ge\lambda_n^{\rm arch}\qquad(n\ge8).
   \]

## Consequence for Poisson positivity

The Carathéodory condition
\[
  \Re H_{\rm EG}(z)\ge0
\]
cannot be asserted for the naive logarithmic derivative series if that
series represents an infinite unweighted divisor without subtraction.

The corrected analytic target is:

1. define the completed, renormalized \(H_{\rm EG}\);
2. identify the precise positive cone or finite measure after subtraction;
3. prove the relevant real-part or kernel positivity in that framework;
4. recover the unweighted Li coefficients and the transformed zero
   singularities.

Only after these steps does Herglotz/Carathéodory positivity imply the
support theorem.

## Eliminated shortcut

The following shortcut is invalid:
\[
  \hbox{construct any finite positive circle measure}
  \quad\Longrightarrow\quad
  \hbox{it represents the Li zero divisor}.
\]

A finite measure can represent a finite-mass moment problem.  The Li divisor
requires pairing, subtraction or a different Hilbert-space form.

## Status

Closed as an obstruction and correction.  A1 remains open.

The global positivity route is still viable, but its first obligation is now
sharper: construct the correct renormalized Euler--Gamma positive object
before invoking Toeplitz, Fejer, Poisson or Schur margin positivity.

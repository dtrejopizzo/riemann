# Renormalized vanishing-test kernel target

## Purpose

`167_LI_MOMENT_RENORMALIZATION_OBSTRUCTION.md` shows that the Li divisor
cannot be represented naively by a finite circle measure with unit mass at
every transformed zero.  This note isolates the natural renormalized
replacement:

a positive quadratic form on polynomials that vanish at the accumulation
point \(1\).

This is the correct Hilbert-space shape for the Li tests
\[
  1-z^n,
\]
since they vanish at \(z=1\).

## Critical-line model

Assume for this model paragraph that all transformed zeros
\[
  w_\rho=1-{1\over\rho}
\]
lie on \(\partial\mathbb D\).  Let
\[
  \mathcal V=\{p\in\mathbb C[z]:p(1)=0\}.
\]

For \(p\in\mathcal V\), define formally
\[
  \mathfrak Q_{\rm CL}(p)
  =
  \sum_\rho |p(w_\rho)|^2,
\tag{1}
\]
with symmetric zero-pairing.

This is the finite-mass obstruction corrected by a vanishing condition.  If
\(|\rho|\to\infty\), then
\[
  w_\rho=1-{1\over\rho}
\]
and, since \(p(1)=0\),
\[
  p(w_\rho)=p'(1)(w_\rho-1)+O(|w_\rho-1|^2)
  =
  -{p'(1)\over\rho}+O(|\rho|^{-2}).
\tag{2}
\]

Therefore
\[
  |p(w_\rho)|^2=O(|\rho|^{-2}).
\tag{3}
\]

Using the standard zero-counting growth \(N(T)=O(T\log T)\), the series
\[
  \sum_\rho |p(w_\rho)|^2
\]
converges absolutely for every fixed \(p\in\mathcal V\).  Thus the
vanishing condition turns the infinite divisor into a finite quadratic
action on Li-type tests.

## Li square identity in the model

Take
\[
  p_n(z)=1-z^n\in\mathcal V.
\]

On the critical-line model, \(w_\rho^{-1}=\overline{w_\rho}\), and paired
zeros give
\[
\begin{aligned}
  |1-w_\rho^n|^2
  &=
  (1-w_\rho^n)(1-\overline{w_\rho}^{\,n})\\
  =
  2-w_\rho^n-w_\rho^{-n}.
\end{aligned}
\tag{4}
\]

Under the usual symmetric Li pairing this gives
\[
  \boxed{
  \mathfrak Q_{\rm CL}(1-z^n)=2\lambda_n.
  }
\tag{5}
\]

Hence positivity of the vanishing-test form would imply Li positivity, and
an archimedean margin
\[
  \mathfrak Q_{\rm EG}(1-z^n)\ge 2\lambda_n^{\rm arch}
\tag{6}
\]
would imply the compact A1 margin after A0, in the normalization of
`164_A1_TOEPLITZ_SCHUR_MARGIN.md`.

## Non-circular theorem needed

The critical-line model (1) cannot be used as a proof, because it assumes
the support conclusion.  The required theorem is:

**Renormalized Euler--Gamma vanishing-kernel theorem.**  Construct a
sesquilinear form
\[
  \mathfrak Q_{\rm EG}:\mathcal V\times\mathcal V\to\mathbb C
\]
from completed Euler--Gamma data, without assuming \(|w_\rho|=1\), such
that:

1. \(\mathfrak Q_{\rm EG}\) is positive semidefinite:
   \[
     \mathfrak Q_{\rm EG}(p,p)\ge0
     \qquad(p\in\mathcal V);
   \tag{7}
   \]
2. for every \(n\ge1\),
   \[
     \mathfrak Q_{\rm EG}(1-z^n,1-z^n)=2\lambda_n;
   \tag{8}
   \]
3. the reproducing or Cauchy singularities of the completed kernel are
   exactly the transformed nontrivial zero divisor;
4. the construction is compatible with the pole-prime-Gamma pairing used in
   the Li coefficients.

Then (7)--(8) imply
\[
  \lambda_n\ge0\qquad(n\ge1),
\]
and Omega7 closes by Li.

For the existing A0/A1 decomposition, the stronger margin
\[
  \mathfrak Q_{\rm EG}(1-z^n,1-z^n)
  \ge
  2\lambda_n^{\rm arch}
  \qquad(n\ge8)
\tag{9}
\]
would close compact A1 after the A0 tail budget.

## Why this avoids the finite-measure obstruction

A finite measure on \(\partial\mathbb D\) tests arbitrary polynomials and has
bounded moments.  The Li zero divisor instead gives a natural finite action
only on differences at the accumulation point \(1\).  The space
\[
  \mathcal V=(z-1)\mathbb C[z]
\]
builds that subtraction into the test class.

Thus the correct positivity problem is not necessarily a finite Herglotz
moment problem on all trigonometric polynomials.  It may be a Dirichlet-type
positive kernel on \(\mathcal V\).  This is still strong enough for Li,
because every Li test \(1-z^n\) lies in \(\mathcal V\).

## Off-line sensitivity

If some transformed zero satisfies \(|w_\rho|>1\), then the square model
\[
  \sum_\rho |p(w_\rho)|^2
\]
is no longer the Euler--Gamma form obtained by boundary pairing.  The
renormalized kernel must therefore be constructed before choosing boundary
conjugation.  This is exactly where the RH-strength support theorem enters.

Equivalently, a candidate form that is positive only after replacing
\(\overline{w_\rho}\) by \(w_\rho^{-1}\) has already assumed boundary
support.  A valid Euler--Gamma form must define its adjoint, pairing and
positivity intrinsically.

## Status

Closed as a sharpened target.  A1 remains open.

The next global positivity obligation is now precise: construct a positive
renormalized Euler--Gamma kernel on \((z-1)\mathbb C[z]\) whose Li-square
values are \(2\lambda_n\), or whose stronger values supply the archimedean
margin required for compact A1.

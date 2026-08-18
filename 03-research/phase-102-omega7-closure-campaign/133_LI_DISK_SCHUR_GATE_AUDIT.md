# Li disk Schur gate audit

## Purpose

The Li transform maps each zero \(\rho\) to
\[
  w_\rho=1-{1\over\rho}.
\]
This document writes Omega7 in the corresponding disk coordinates and
records what a Schur, Carathéodory or positive-real proof would have to
establish.

## Li generating transform

Let
\[
  F(z)=\log \xi\!\left({1\over1-z}\right).
\]

Near \(z=0\),
\[
  F(z)=F(0)+\sum_{n\ge1}{\lambda_n\over n}z^n,
\]
and
\[
  zF'(z)=\sum_{n\ge1}\lambda_n z^n.
\tag{1}
\]

Using the zero-side product formally, a zero \(\rho\) contributes
\[
  -\log(1-w_\rho z)
  =
  \sum_{n\ge1}{w_\rho^n\over n}z^n,
\]
up to the paired normalization that also supplies the constant and
linear-compensation terms.  Thus the Li coefficients test the power sums of
the transformed zero multiset \(\{w_\rho\}\).

## Disk meaning of the critical line

For \(\rho=1/2+it\),
\[
  \left|1-{1\over\rho}\right|=1.
\]

If \(\rho\) is off the critical line, the functional-equation quartet
contains a transformed point with
\[
  |w_\rho|>1.
\]

Therefore the critical-line statement is equivalent to saying that the
paired transformed divisor has no point outside the unit circle.

## Schur-Carathéodory target

A disk-function proof would close Omega7 if it constructs, from
Euler--Gamma data, a function with a positive-real or Schur representation
whose singularities encode the transformed zeros and whose representing
measure lives on the unit circle.

One possible target is a positive boundary measure \(\nu\) on
\(\partial\mathbb D\) such that
\[
  zF'(z)
  =
  \int_{\partial\mathbb D}
  {z\zeta\over1-z\zeta}\,d\nu(\zeta)
  +
  \hbox{explicit harmless terms},
\tag{2}
\]
with the same paired normalization as the Li coefficients.

Then
\[
  \lambda_n=\int_{\partial\mathbb D}\zeta^n\,d\nu(\zeta)
  +\hbox{paired nonnegative form}
\]
would have to be converted into the usual Li square form.  More directly,
if the singularities of \(F\) are shown to lie only on \(\partial\mathbb D\),
then all zeros lie on the critical line and Omega7 follows.

## Why coefficient positivity alone is not a Schur theorem

The statement
\[
  \lambda_n\ge0\qquad(n\ge1)
\]
is a coefficient positivity statement for \(zF'(z)\).  It does not by itself
provide a Schur or Carathéodory representation unless one also proves the
corresponding kernel positivity or representing measure.

Conversely, defining a measure by the transformed zeros is circular unless
one first proves that its support lies on \(\partial\mathbb D\) or that the
off-circle parts cancel by a positive mechanism.

The following proof pattern is therefore invalid:

1. write the singularities of \(F\) as transformed zeros;
2. call the resulting divisor a boundary measure;
3. infer coefficient positivity.

Step 2 assumes the support statement equivalent to RH.

## Off-line obstruction

If an off-line zero yields \(|w|>1\), then its contribution to the Li
sequence contains a geometric term
\[
  -2\mathrm{Re}(w^n)
\]
along the paired quartet.  Along a subsequence this term is negative with
exponential size.  No archimedean term of polynomial-logarithmic size can
hide it.

Thus any Schur-disk theorem strong enough to prove A1 must forbid exterior
singularities before coefficient positivity is concluded.

## Relation to existing gates

The disk gate is the same support-collapse problem in another coordinate:

- the line-coordinate positive boundary measure asks for support on the
  imaginary axis;
- the disk-coordinate Schur gate asks for support on \(\partial\mathbb D\);
- the Li coefficients are the power-sum tests of the transformed divisor.

The maps are:
\[
  s={1\over2}+z_{\rm line},
  \qquad
  w=1-{1\over s}.
\]

Therefore a disk Schur proof is viable only if it constructs the boundary
support from Euler--Gamma data.  If it assumes the support, it is the same
circularity as the positive boundary measure route.

## Status

Closed as a coordinate audit.  The disk transform gives a clean target:
prove a Schur/Carathéodory boundary-support theorem for the Li transform from
Euler--Gamma data.  Coefficient positivity or a divisor-defined boundary
measure alone does not close A1.

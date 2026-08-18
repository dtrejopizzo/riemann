# Total positivity and Li sequence audit

## Purpose

This document tests whether total positivity, Pólya frequency sequences or
log-concavity can close the remaining A1 inequality.

## Li generating function

The Li coefficients satisfy
\[
  {d\over dz}\log \xi\left({1\over1-z}\right)
  =
  \sum_{n\ge1}\lambda_n z^{n-1}
\]
near \(z=0\).

Thus Omega7 is positivity of all coefficients of this transformed logarithmic
derivative.

## Total positivity route

A possible closure would prove that
\[
  F(z)=\log \xi\left({1\over1-z}\right)
\]
or a derivative of \(F\) belongs to a class whose Taylor coefficients are
nonnegative. Examples include Stieltjes functions, Pick functions with
positive representing measure, or Pólya frequency generating functions.

## Equivalence obstruction

For this particular \(F\), membership in such a positive coefficient class
forces strong restrictions on the singularities of \(F\). The singularities
come from the zeros of \(\xi\), transported by
\[
  z=1-{1\over\rho}.
\]

If a zero is off the critical line, one transported singularity lies outside
the unit circle with reciprocal pairing, and the coefficient sequence
contains a geometric sign-destroying component. Therefore total positivity or
coefficient positivity of the transformed function is another form of
excluding off-line zeros.

## Eliminated class

The following class does not close A1:
\[
  \hbox{prove finite log-concavity, finite Hankel positivity, or finite
  total positivity of }\{\lambda_n\}_{n\le N}.
\]

Finite coefficient structure cannot exclude a later off-line geometric mode.
It is a useful consistency check, not a proof of Omega7.

## Live theorem

A total-positivity route remains viable only if it proves the infinite
statement:

The transformed logarithmic derivative
\[
  {d\over dz}\log \xi\left({1\over1-z}\right)
\]
is a coefficient-positive Pick/Stieltjes object by construction from
Euler--Gamma data.

This theorem would imply \(\lambda_n\ge0\) for every \(n\) and hence close
Omega7. It is equivalent in strength to the positive boundary measure target.

## Status

Finite total positivity routes are eliminated. Infinite total positivity is a
valid force-RH target, but it is currently the same missing positive boundary
measure in transformed coordinates.

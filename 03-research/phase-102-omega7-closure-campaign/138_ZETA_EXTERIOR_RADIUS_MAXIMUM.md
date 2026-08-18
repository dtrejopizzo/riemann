# Zeta exterior radius maximum

## Purpose

The isolated-radius reduction left a possible infinite-support obstruction:
exterior radii in the Li disk coordinate might fail to have a maximal
isolated shell.  For zeta zeros in the critical strip, this obstruction can
be removed on the zero side.

This document proves that if any zeta zero is off the critical line, then
the transformed exterior radii have a finite maximal shell.  Combined with
the finite-shell dominance lemma, this recovers the zero-side direction of
Li's criterion:

\[
  \hbox{Li positivity}
  \Longrightarrow
  \hbox{no off-line zero}.
\]

This is not yet an arithmetic proof of A1; it is a completion of the
zero-side discriminator.

## Disk coordinate

For a zero
\[
  \rho=\beta+i\gamma,
\]
put
\[
  w_\rho=1-{1\over\rho}={\rho-1\over\rho}.
\]

Then
\[
  |w_\rho|^2
  =
  {(\beta-1)^2+\gamma^2\over \beta^2+\gamma^2}.
\tag{1}
\]

Consequently
\[
  |w_\rho|^2-1
  =
  {1-2\beta\over \beta^2+\gamma^2}.
\tag{2}
\]

Thus
\[
  |w_\rho|>1
  \quad\Longleftrightarrow\quad
  \beta<{1\over2}.
\tag{3}
\]

By the functional equation, a zero with \(\beta>1/2\) is paired with one at
\(1-\beta<1/2\), so every off-line quartet contains an exterior disk point.

## Uniform decay of exterior excess at height

For nontrivial zeros in the critical strip,
\[
  0<\beta<1.
\]

If \(\beta<1/2\), then from (2)
\[
  0<|w_\rho|^2-1
  =
  {1-2\beta\over \beta^2+\gamma^2}
  \le {1\over \gamma^2}
\tag{4}
\]
whenever \(\gamma\ne0\).

Hence, uniformly in \(\beta\),
\[
  |w_\rho|\to1
  \qquad(|\gamma|\to\infty)
\tag{5}
\]
for exterior disk points coming from zeta zeros.

## Existence of a maximal exterior shell

Assume there is at least one off-line zero.  Then there is at least one
exterior disk point with radius
\[
  R_\ast>1.
\]

Choose \(H\) so large that
\[
  1+{1\over H^2}<R_\ast^2.
\tag{6}
\]

By (4), every exterior disk point with
\[
  |\gamma|>H
\]
has radius strictly smaller than \(R_\ast\).  Therefore any exterior point
with radius at least \(R_\ast\) must come from a zero in the bounded height
region
\[
  |\gamma|\le H.
\]

The zeros of \(\xi\) are discrete, hence only finitely many lie in a bounded
height region.  Therefore the set of exterior radii has a maximum
\[
  R_{\max}>1,
\]
and the shell
\[
  \{|w_\rho|=R_{\max}\}
\]
is finite.

Thus every off-line zeta zero produces a finite maximal exterior shell in
the Li disk coordinate.

## Consequence with shell dominance

By the finite exterior shell dominance theorem, a nonzero maximal shell of
radius \(R_{\max}>1\) contributes a negative geometric subsequence to the Li
coefficients:
\[
  \lambda_n\le -cR_{\max}^n+o(R_{\max}^n)
\]
along an infinite subsequence, after the paired zero-side normalization.

The archimedean contribution satisfies
\[
  \lambda_n^{\rm arch}=O(n\log n)=o(R_{\max}^n).
\]

Therefore Li positivity for all \(n\) rules out the existence of any
off-line zeta zero.

## What is closed

The possible infinite exterior-support obstruction is closed on the zero
side for zeta: an off-line zero cannot hide in an exterior cloud accumulating
only at the unit circle without creating a finite maximal exterior shell.

This strengthens the disk-coordinate discriminator:

\[
  \hbox{off-line zero}
  \Longrightarrow
  \hbox{finite maximal exterior shell}
  \Longrightarrow
  \hbox{negative Li subsequence}.
\]

## What remains open

This does not prove A1, because A1 requires an arithmetic proof of Li
positivity or of the compact signed core.  The present theorem proves only
the zero-side consequence:

\[
  \lambda_n\ge0\ \hbox{for all }n
  \Longrightarrow
  \hbox{RH}.
\]

The missing phase-102 theorem is still one of the accepted arithmetic gates:
direct A1, strong margin, one-sided tail, positive boundary measure,
Schur support, Laguerre--Pólya, heat-flow threshold, or an equivalent signed
Euler--Gamma construction.

## Status

Closed on the zero side.  The infinite exterior-support caveat is removed
for zeta zeros in the critical strip.  The arithmetic A1 sign remains open.

# Isolated exterior radius reduction

## Purpose

The finite exterior shell lemma proves dominance when a finite maximal
exterior shell exists.  This document records the next reduction: if an
exterior radius is separated from all larger or nearby exterior radii, then
the same geometric dominance argument survives.  The remaining obstruction is
therefore not a finite off-line mode, but possible infinite exterior support
accumulating toward the unit circle.

## Disk-coordinate divisor

Write
\[
  w_\rho=1-{1\over\rho}.
\]

Critical-line zeros correspond to
\[
  |w_\rho|=1.
\]

An off-line zero gives a functional-equation quartet containing an exterior
point
\[
  |w_\rho|>1.
\]

## Isolated exterior radius hypothesis

Assume that the transformed divisor contains exterior points and that there
is a radius \(R>1\) such that:

1. the shell
   \[
     \{w_\rho: |w_\rho|=R\}
   \]
   is finite and has nonzero paired shell contribution;
2. all remaining exterior points satisfy
   \[
     |w_\rho|\le R_0
   \]
   for some \(1<R_0<R\), except possibly finitely many points already
   included in the shell;
3. the paired summation prescription bounds the lower-radius contribution by
   \[
     O(R_0^n)
   \]
   in the Li coefficient.

Then the finite exterior shell dominance theorem applies to the shell of
radius \(R\).  Along an infinite subsequence its contribution is
\[
  \le -cR^n
\]
for some \(c>0\), while all lower-radius contributions are
\[
  O(R_0^n)=o(R^n).
\]

The archimedean term is
\[
  O(n\log n)=o(R^n).
\]

Therefore Li positivity fails along that subsequence.

## Consequence

Under the isolated exterior radius hypothesis, Omega7 implies that no such
exterior shell can exist.  Equivalently, any proof of Omega7 by contradiction
may reduce an isolated exterior shell to the finite-shell discriminator.

This closes the isolated-shell case.

## What remains in the infinite divisor case

The zeta divisor is not a finite typed control.  If exterior points existed,
the difficult scenarios not covered by the isolated-shell reduction are:

1. exterior radii with no maximal isolated shell;
2. infinitely many exterior radii accumulating down to \(1\);
3. infinitely many exterior points on shells whose paired sums cancel in the
   leading radius;
4. lack of a uniform \(O(R_0^n)\) bound for the lower-radius remainder under
   the paired summation prescription.

These are precisely support-collapse problems.  They cannot be solved by a
finite trigonometric argument alone.

## Relation to Li's criterion

Li's theorem handles the full infinite divisor by a global analytic
argument.  In phase-102 terms, an arithmetic proof must reproduce the same
global exclusion through one of the accepted gates:

- positive boundary measure;
- disk Schur support;
- Laguerre--Pólya/Jensen cofinality;
- heat-flow threshold;
- direct A1 signed core.

The isolated-shell reduction is useful because it shows that all finite or
radially separated off-line controls are already excluded by elementary
asymptotics.  The remaining work is genuinely infinite and global.

## Status

Closed as a reduction.  The isolated exterior radius case is handled.  The
open problem is exterior support accumulating or interacting infinitely near
the unit circle.

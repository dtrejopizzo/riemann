# Li test family scope

## Purpose

A1 only asks for positivity of the Li test family, not for the full Weil
class. This document checks whether that narrower family might avoid the
full support problem.

## Li test functions

For each \(n\ge1\), the zero-side Li kernel is
\[
  \mathcal K_n(\rho)
  =
  1-\left(1-{1\over\rho}\right)^n.
\]

Pairing \(\rho\) with \(1-\rho\) and conjugates, the kernel is nonnegative
on the critical line:
\[
  \mathcal K_n(1/2+it)+\mathcal K_n(1/2-it)
  =
  4\sin^2\left({n\theta(t)\over2}\right).
\]

Thus the Li family is a countable family of nonnegative trigonometric tests
on the line.

## Off-line sensitivity of the family

If a zero is off the line, one Li multiplier
\[
  w_\rho=1-{1\over\rho}
\]
has \(|w_\rho|>1\). Then the sequence
\[
  \mathrm{Re}(w_\rho^n)
\]
has exponentially large positive values along a subsequence. The paired Li
contribution contains the corresponding negative term, so some Li coefficient
is eventually negative.

Therefore the Li test family is already separating for the off-line
phenomenon. It is narrower than the full Weil class, but it is not too weak:
positivity on all Li tests is equivalent to the critical-line statement.

## Consequence for A1

Any proof of A1 for every \(n\ge8\), together with the finite certificate for
\(1\le n\le7\), proves positivity on the whole Li family and hence RH.

Thus the fact that A1 uses only Li tests does not lower the difficulty below
RH. It merely gives a minimal countable test family.

## Possible advantage

The advantage is technical, not logical. A proof may exploit special
structure of
\[
  L_{n-1}^{(1)}(\log y)
\]
and avoid proving positivity for all Weil tests. Such a proof would still
have to contain a mechanism that blocks every off-line multiplier
\(|w_\rho|>1\).

## Status

The Li test family is the minimal exact target. It is valid to attack only
this family, but success is still a proof of RH. No additional weakening is
obtained.

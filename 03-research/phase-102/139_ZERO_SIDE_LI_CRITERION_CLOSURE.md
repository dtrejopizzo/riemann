# Zero-side Li criterion closure

## Purpose

This document consolidates the zero-side work in phase 102.  It proves, in
the disk-coordinate language developed here, that Li positivity is equivalent
to the critical-line statement for the zeta divisor.

This does not prove A1.  It closes the zero-side implication and identifies
the remaining problem as the arithmetic proof of Li positivity.

## Li coefficients on the zero side

The zero-side Li expression is
\[
  \lambda_n
  =
  \sum_\rho
  \left[
    1-\left(1-{1\over\rho}\right)^n
  \right],
\tag{1}
\]
with the usual symmetric paired interpretation.

Put
\[
  w_\rho=1-{1\over\rho}.
\]

## Critical line implies Li positivity

If
\[
  \rho={1\over2}+i\gamma,
\]
then
\[
  |w_\rho|=1.
\]

Pairing conjugate zeros, write
\[
  w_\rho=e^{i\theta_\gamma}.
\]
The paired contribution is
\[
  2-w_\rho^n-\overline{w_\rho}^n
  =
  2-2\cos(n\theta_\gamma)
  =
  4\sin^2\left({n\theta_\gamma\over2}\right)
  \ge0.
\tag{2}
\]

Summing over the paired divisor in the standard Li sense gives
\[
  \lambda_n\ge0
  \qquad(n\ge1).
\]

Thus
\[
  \hbox{critical-line support}
  \Longrightarrow
  \lambda_n\ge0\quad(n\ge1).
\tag{3}
\]

## Li positivity excludes off-line zeros

Assume conversely that an off-line zero exists.  By the functional equation,
the zero quartet contains a member with
\[
  \beta<{1\over2}.
\]

For that member,
\[
  |w_\rho|^2-1
  =
  {1-2\beta\over \beta^2+\gamma^2}
  >
  0,
\]
so
\[
  |w_\rho|>1.
\]

The zeta exterior-radius theorem proves that any off-line zero produces a
finite maximal exterior shell in the Li disk coordinate.  The finite-shell
dominance theorem then gives an infinite subsequence for which the zero-side
Li contribution is negative of geometric size:
\[
  \lambda_n
  \le
  -cR^n+o(R^n)
\]
for some \(R>1\) and \(c>0\), after paired summation.

The archimedean split has only
\[
  \lambda_n^{\rm arch}=O(n\log n)=o(R^n),
\]
so no phase-102 archimedean budget can hide this negative subsequence.

Therefore Li positivity for every \(n\) rules out off-line zeros:
\[
  \lambda_n\ge0\quad(n\ge1)
  \Longrightarrow
  \hbox{critical-line support}.
\tag{4}
\]

## Zero-side criterion

Combining (3) and (4), phase 102 has the zero-side equivalence
\[
  \boxed{
  \lambda_n\ge0\quad(n\ge1)
  \Longleftrightarrow
  \hbox{all nontrivial zeros lie on the critical line}.
  }
\tag{5}
\]

This is Li's criterion in the disk-coordinate form used by this phase.

## Relation to A1

The phase-102 direct arithmetic decomposition is
\[
  \lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime}.
\]

The finite certificate closes
\[
  \lambda_n>0
  \qquad(1\le n\le7).
\]

For \(n\ge8\), A0 removes the far tail, and A1 is the remaining compact
signed theorem:
\[
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
  +{3\over4}\lambda_n^{\rm arch}\ge0.
\tag{A1}
\]

If A1 is proved, then the phase-102 assembly gives
\[
  \lambda_n\ge0\quad(n\ge1),
\]
and (5) gives RH.

Thus the zero side is closed.  The open work is not the implication from Li
positivity to RH; it is the arithmetic proof of Li positivity, equivalently
A1 or one of the accepted stronger gates.

## Status

Closed on the zero side.  The remaining live theorem is the arithmetic
signed positivity of the Li coefficients, concentrated in A1.

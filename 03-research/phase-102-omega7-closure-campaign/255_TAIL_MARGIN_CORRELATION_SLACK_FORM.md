# Tail-margin correlation slack form

## Purpose

`196_A1_REMAINING_THEOREMS_CANONICAL_FORM.md` states Theorem D as a
one-sided tail theorem and mentions a useful tail--margin correlation.  The
notation there can collide with the established tail surplus
\[
  \delta_n={1\over4}A_n-R_n(T_n).
\]

This note fixes the correlation in a separate slack variable and records
the exact equivalence with A1.

## Basic variables

Let
\[
  A_n=\lambda_n^{\rm arch}>0,
  \qquad
  M_n=\lambda_n-\frac12A_n,
  \qquad
  R_n=R_n(T_n).
\]

The compact A1 coefficient is
\[
\boxed{
  C_n(T_n)=\lambda_n-\frac14A_n-R_n.
}
\tag{1}
\]

Equivalently,
\[
  C_n(T_n)=M_n+\left({1\over4}A_n-R_n\right).
\tag{2}
\]

## Correlation slack

Introduce a nonnegative correlation slack \(h_n\) by asking for a signed
tail improvement
\[
\boxed{
  R_n\le {1\over4}A_n-h_n.
}
\tag{3}
\]

Then
\[
  C_n(T_n)
  \ge
  \lambda_n-\frac14A_n-\left({1\over4}A_n-h_n\right)
  =
  M_n+h_n.
\tag{4}
\]

Therefore A1 follows from (3) if
\[
\boxed{
  h_n\ge (-M_n)_+
  =
  \left({1\over2}A_n-\lambda_n\right)_+.
}
\tag{5}
\]

This is the tail--margin correlation in unambiguous slack form.

## Sharpness

The condition is sharp.  If (3) holds with
\[
  h_n<(-M_n)_+
\]
and \(M_n<0\), then the lower bound (4) permits
\[
  C_n(T_n)<0.
\]

Thus a useful correlation theorem must provide the slack pointwise in
\(n\); an averaged or asymptotic slack that does not dominate
\((-M_n)_+\) at the same index does not prove compact A1.

## Normalized form

Normalize
\[
  \sigma_n={h_n\over A_n}.
\]

Then (3) is
\[
  {R_n\over A_n}\le {1\over4}-\sigma_n,
\tag{6}
\]
and (5) is
\[
\boxed{
  \sigma_n\ge d_n
  =
  \max\left(0,{1\over2}-{\lambda_n\over A_n}\right).
}
\tag{7}
\]

Since
\[
  s_n={1\over4}-{R_n\over A_n},
\]
the largest admissible slack supplied by the actual tail is \(s_n\).
Therefore (6)--(7) are exactly the gate
\[
  s_n\ge d_n
\]
from `240`.

## Relation to A0 and special points

A0 gives (3) only with \(h_n=0\):
\[
  R_n\le {1\over4}A_n.
\]
This closes A1 precisely when \(M_n\ge0\), i.e. under strong margin.

If quarter margin holds,
\[
  \lambda_n\ge {1\over4}A_n,
\]
then \((-M_n)_+\le A_n/4\).  The nonpositive-tail theorem
\[
  R_n\le0
\]
is exactly (3) with \(h_n=A_n/4\), hence it supplies enough slack.  This is
the special route isolated in `247`.

If one only has Li positivity, the worst permitted deficit is
\[
  (-M_n)_+\le {1\over2}A_n,
\]
so the tail theorem must provide as much as \(h_n=A_n/2\), i.e.
\[
  R_n\le -{1\over4}A_n.
\]

## Status

Closed as the canonical tail--margin slack formulation.

A1 remains open.  The missing theorem is a pointwise signed correlation
that supplies \(h_n\ge(-M_n)_+\), equivalently \(s_n\ge d_n\), for every
\(n\ge8\).

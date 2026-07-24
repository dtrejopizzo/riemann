# Archimedean growth bound

## Purpose

The off-line geometric mode lemma shows that an exterior Li multiplier
\(|w|>1\) produces a negative subsequence of geometric size.  This document
records the elementary growth bound for the phase-102 archimedean term,
showing that such a geometric mode cannot be hidden by the archimedean
budget.

## Archimedean formula

The phase-102 split uses
\[
  \lambda_n^{\rm arch}
  =
  1-{n\over2}(\gamma+\log(4\pi))
  +
  \sum_{\substack{r\ge1\\ r\ {\rm odd}}}
  \left[
    \left(1-{1\over r}\right)^n-1+{n\over r}
  \right].
\tag{1}
\]

Put
\[
  A_n=\lambda_n^{\rm arch}.
\]

## Elementary bound on the summand

For \(0\le x\le1\), define
\[
  q_n(x)=(1-x)^n-1+nx.
\]

Since
\[
  (1-x)^n\le1,
\]
one has
\[
  q_n(x)\le nx.
\tag{2}
\]

Also, by Taylor's formula with nonnegative second derivative on
\([0,1]\),
\[
  q_n(x)
  =
  n(n-1)\int_0^x (x-t)(1-t)^{n-2}\,dt
  \le {n(n-1)\over2}x^2.
\tag{3}
\]

Combining (2) and (3),
\[
  0\le q_n(x)\le \min\left(nx,{n(n-1)\over2}x^2\right).
\tag{4}
\]

## Summation over odd indices

For \(r\le n\), use \(q_n(1/r)\le n/r\).  Then
\[
  \sum_{\substack{1\le r\le n\\ r\ {\rm odd}}}q_n(1/r)
  \le
  n\sum_{1\le r\le n}{1\over r}
  \le n(1+\log n).
\tag{5}
\]

For \(r>n\), use \(q_n(1/r)\le n(n-1)/(2r^2)\).  Then
\[
  \sum_{\substack{r>n\\ r\ {\rm odd}}}q_n(1/r)
  \le
  {n(n-1)\over2}\sum_{r>n}{1\over r^2}
  \le
  {n(n-1)\over2}\cdot {1\over n}
  \le {n\over2}.
\tag{6}
\]

From (1), (5), and (6),
\[
  |A_n|
  \le
  1+{n\over2}|\gamma+\log(4\pi)|
  +n(1+\log n)+{n\over2}.
\tag{7}
\]

Thus
\[
  \boxed{
  \lambda_n^{\rm arch}=O(n\log n).
  }
\tag{8}
\]

More explicitly, for \(n\ge2\),
\[
  |\lambda_n^{\rm arch}|
  \le
  C_{\rm arch}\,n\log n
\]
with any constant \(C_{\rm arch}\) larger than the evident bound obtained
from (7).

## Consequence for exterior Li multipliers

If \(|w|>1\), the off-line geometric mode lemma gives infinitely many
\(n\) for which the paired zero-side contribution is at most
\[
  -c|w|^n
\]
for some \(c>0\).

Since
\[
  n\log n=o(|w|^n),
\]
the archimedean term cannot compensate that negative subsequence.

Therefore any proof of A1, the strong margin, the Schur disk support
theorem, or the positive boundary measure theorem must exclude exterior Li
multipliers.  No rearrangement of the phase-102 archimedean budget can
absorb them.

## Status

Closed.  The archimedean growth bound is elementary and supports the
off-line discriminator.  It does not prove that exterior multipliers are
absent for zeta.

# Strong margin reduction

## Purpose

The truncation gate shows that A1 follows from the strong margin
\[
  \lambda_n\ge {1\over2}\lambda_n^{\rm arch}\qquad(n\ge8).
\tag{SM}
\]

This document rewrites that margin in the prime/arch split and records the
exact additional strength it requires.

## Equivalent prime lower bound

Since
\[
  \lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime},
\]
the strong margin (SM) is equivalent, for \(n\ge8\), to
\[
  \lambda_n^{\rm prime}\ge -{1\over2}\lambda_n^{\rm arch}.
\tag{1}
\]

Omega7 itself asks only for
\[
  \lambda_n^{\rm prime}\ge -\lambda_n^{\rm arch}.
\tag{2}
\]

Thus the strong margin is a strictly stronger one-sided prime lower bound.

## Why absolute estimates still fail

An absolute estimate would need
\[
  |\lambda_n^{\rm prime}|\le {1\over2}\lambda_n^{\rm arch}.
\tag{3}
\]

This is stronger than necessary and belongs to the already-audited absolute
domination family. The phase has no mechanism proving (3). Moreover, the
known no-go for absolute Laguerre/PNT estimates applies with even more force:
the compact oscillatory region cannot be controlled by magnitudes within the
\({1\over2}\lambda_n^{\rm arch}\) budget.

## Valid route

The strong margin remains a valid target only as a signed theorem:
\[
  \lambda_n^{\rm prime}+{1\over2}\lambda_n^{\rm arch}\ge0
  \qquad(n\ge8),
\]
proved from Euler--Gamma arithmetic without separating the signed core into
absolute values.

This is not easier than A1 in any formal sense currently proved. It is useful
only because it avoids the tail allocation issue: once (SM) is known, any A0
tail with budget \({1\over4}\lambda_n^{\rm arch}\) closes A1.

## Off-line sensitivity

If an off-line zero exists, its Li multiplier creates a negative geometric
subsequence in \(\lambda_n\). That subsequence eventually violates not only
Omega7 but also (SM). Therefore any proof of (SM) must contain the same
off-line discriminator as A1.

## Status

The strong margin gate is reduced to the sharper signed lower bound (1). It
is a legitimate force-RH target, but it is not supplied by existing absolute
or truncation estimates.

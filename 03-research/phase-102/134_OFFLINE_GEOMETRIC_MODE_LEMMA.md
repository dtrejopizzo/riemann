# Off-line geometric mode lemma

## Purpose

Several phase-102 gates use the same zero-side discriminator: if a transformed
Li multiplier lies outside the unit circle, then the Li coefficients acquire
a negative geometric subsequence.  This document proves that elementary
claim cleanly.

## Elementary angular lemma

Let
\[
  w=re^{i\theta},
  \qquad r>1.
\]

Then there exist a number \(\delta>0\) and infinitely many integers \(n\ge1\)
such that
\[
  \operatorname{Re}(w^n)\ge \delta r^n.
\tag{1}
\]

### Proof

It is enough to show that \(\cos(n\theta)\) is bounded below by a positive
constant along an infinite subsequence.

If \(\theta/2\pi\) is rational, the sequence \(e^{in\theta}\) is periodic.
One of its values is \(1\), occurring for infinitely many \(n\).  Along that
subsequence,
\[
  \cos(n\theta)=1.
\]

If \(\theta/2\pi\) is irrational, the sequence \(e^{in\theta}\) is dense on
the unit circle.  Hence it enters the arc
\[
  \{e^{i\alpha}:|\alpha|<\pi/3\}
\]
infinitely often.  Along that subsequence,
\[
  \cos(n\theta)>{1\over2}.
\]

Thus (1) holds with \(\delta=1\) in the rational case and
\(\delta=1/2\) in the irrational case.  This proves the lemma.

## Quartet contribution

The Li transform of a zero is
\[
  w_\rho=1-{1\over\rho}.
\]

If a functional-equation quartet contains a member with
\[
  |w_\rho|>1,
\]
then the paired zero-side contribution to \(\lambda_n\) contains a term of
the shape
\[
  -2\operatorname{Re}(w_\rho^n)
\tag{2}
\]
plus terms whose exponential rate is no larger than the reciprocal partner
or the unit-circle partners, depending on the normalization of the quartet.

By the lemma, there is an infinite subsequence for which
\[
  -2\operatorname{Re}(w_\rho^n)
  \le
  -2\delta |w_\rho|^n.
\tag{3}
\]

Thus the quartet produces a negative subsequence of geometric size.

## Dominance over archimedean growth

The phase-102 archimedean contribution has at most polynomial-logarithmic
growth in the relevant Li index.  In particular it is negligible compared
with
\[
  |w_\rho|^n
\]
when \(|w_\rho|>1\).  Therefore an exterior Li multiplier cannot be hidden by
the archimedean split: it eventually violates any lower bound whose budget
grows slower than \(|w_\rho|^n\).

This explains why every successful A1 proof must exclude exterior
disk-coordinate singularities before invoking coefficient positivity.

## Consequences for phase-102 gates

The lemma supplies the common discriminator for the following gates:

1. the disk Schur gate, where exterior points must be excluded;
2. the positive boundary measure gate, where support must collapse to the
   boundary line or circle;
3. the Jensen and Laguerre--Pólya gates, where real-rootedness excludes
   exterior multipliers;
4. the heat-flow gate, where the threshold must reach the original time;
5. the direct A1 gate, where the signed compact core must contain a
   mechanism forbidding the geometric negative subsequence.

## What the lemma does not prove

The lemma is only a discriminator.  It proves that an off-line multiplier
would break Li positivity.  It does not prove that zeta lacks such a
multiplier.

Therefore it cannot close A1 by itself.  It tells every proposed proof what
kind of obstruction it must remove.

## Status

Closed as an elementary zero-side lemma.  It strengthens the off-line
sensitivity audit but leaves the arithmetic exclusion theorem open.

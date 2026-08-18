# Finite exterior shell dominance

## Purpose

The elementary off-line lemma treats one exterior Li multiplier
\[
  |w|>1.
\]
This document proves the corresponding finite-shell statement: a nonempty
finite set of exterior multipliers with maximal modulus produces a negative
geometric subsequence in the paired Li contribution, unless its signed
coefficient on that shell is identically zero.

It also records why this finite statement is not yet a proof for the full
zeta divisor.

## Finite trigonometric lemma

Let
\[
  S(n)=\sum_{j=1}^J c_j e^{in\theta_j},
  \qquad c_j\in\mathbb C,
\]
and suppose \(S\) is not identically zero.  Then there exist \(\delta>0\)
and infinitely many \(n\) such that
\[
  \operatorname{Re} S(n)\ge\delta.
\tag{1}
\]

### Proof

The sequence
\[
  (e^{in\theta_1},\ldots,e^{in\theta_J})
\]
has compact closure in the torus \(\mathbb T^J\).  The function
\[
  P(z_1,\ldots,z_J)=\sum_{j=1}^J c_j z_j
\]
is continuous on that closure.

Since \(S\) is not identically zero, \(P\) is not identically zero on the
orbit closure.  Hence
\[
  M=\max \operatorname{Re} P
\]
on the orbit closure is positive after multiplying the whole shell by a
unit complex number if necessary.  For the Li paired contribution the phase
is fixed, but the same conclusion applies to either the real part or its
negative unless the shell contribution is identically zero.

By recurrence of the orbit in its compact closure, values with
\[
  \operatorname{Re}S(n)>M/2
\]
occur infinitely often.  Taking \(\delta=M/2\) proves (1).

## Exterior shell contribution

Let a finite exterior shell be
\[
  w_j=R e^{i\theta_j},
  \qquad R>1,
  \qquad 1\le j\le J,
\]
with signed multiplicity coefficients \(c_j\).  Its contribution to the
zero-side Li expression has the form
\[
  -2R^n\operatorname{Re}
  \left(\sum_{j=1}^J c_j e^{in\theta_j}\right)
\tag{2}
\]
after the usual conjugate pairing and up to harmless lower-radius terms.

If the shell trigonometric polynomial is not identically zero, the finite
trigonometric lemma gives an infinite subsequence with
\[
  -2R^n\operatorname{Re}
  \left(\sum_{j=1}^J c_j e^{in\theta_j}\right)
  \le
  -2\delta R^n.
\tag{3}
\]

Thus a nonzero finite maximal exterior shell forces a negative geometric
subsequence.

## Dominance over lower shells

Suppose all other exterior or boundary contributions have modulus at most
\[
  R_0<R.
\]
Then their total contribution is
\[
  O(R_0^n)
\]
for a finite divisor, and therefore
\[
  O(R_0^n)=o(R^n).
\]

Combining this with the archimedean bound
\[
  \lambda_n^{\rm arch}=O(n\log n)=o(R^n),
\]
the finite maximal exterior shell dominates all lower shells and the
archimedean budget along the subsequence in (3).

## What this proves

For a finite off-line control, or for a divisor with a genuine finite maximal
exterior shell separated from all other exterior radii, Li positivity must
fail unless the maximal shell cancels identically.

This is the exact finite-shell version of the off-line discriminator.

## What remains open for zeta

The zeta zero divisor is infinite.  Exterior radii in the disk coordinate,
if any existed, could accumulate down toward \(1\).  A single off-line zero
has \(R>1\), but there may be no globally maximal exterior radius if there
are infinitely many exterior points with radii approaching a supremum or
distributed without a finite top shell.

Therefore the finite-shell lemma is not a substitute for Li's full theorem
or for a support-collapse proof.  A full disk-support argument must control:

1. infinite exterior collections;
2. possible cancellations between many radii;
3. limiting shells with \(R\downarrow1\);
4. the paired summation prescription for the entire divisor.

Those are exactly the analytic difficulties handled abstractly by Li's
criterion or by a positive boundary/support theorem.

## Status

Closed as a finite-shell discriminator.  It strengthens typed off-line tests
and finite controls, but the full zeta support theorem remains open.

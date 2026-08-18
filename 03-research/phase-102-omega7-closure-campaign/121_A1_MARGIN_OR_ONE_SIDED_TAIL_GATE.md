# A1 margin or one-sided tail gate

## Purpose

This note records the exact extra theorem that would let the A0 truncation
machinery close A1.  It is a gate, not a proof.

## Setup

For \(n\ge8\), put
\[
  A_n=\lambda_n^{\rm arch}>0,
\]
and write
\[
  \lambda_n^{\rm prime}=K_n(T_n)+R_n(T_n),
\]
where
\[
  K_n(T_n)
  =
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
\]
and \(R_n(T_n)\) is the paired tail.  A0 gives
\[
  |R_n(T_n)|\le {1\over4}A_n.
\tag{1}
\]

A1 is
\[
  K_n(T_n)+{3\over4}A_n\ge0.
\tag{2}
\]

Since
\[
  \lambda_n=K_n(T_n)+R_n(T_n)+A_n,
\]
equation (2) is equivalent to
\[
  \lambda_n\ge R_n(T_n)+{1\over4}A_n.
\tag{3}
\]

## Gate A: strong Li margin

If one proves the stronger margin
\[
  \lambda_n\ge {1\over2}A_n\qquad(n\ge8),
\tag{4}
\]
then (1) implies
\[
  R_n(T_n)+{1\over4}A_n\le {1\over2}A_n\le\lambda_n,
\]
and hence A1 follows from (3).

Therefore a valid replacement target for A1 is the strong margin theorem
\[
  \boxed{\lambda_n\ge {1\over2}\lambda_n^{\rm arch}\qquad(n\ge8).}
\]

This target is at least as strong as the Li sign on the infinite range.  It
cannot be assumed, but if proved from Euler--Gamma data it would close A1
through A0.

## Gate B: one-sided tail

Alternatively, if one proves the one-sided tail inequality
\[
  R_n(T_n)\le \lambda_n-{1\over4}A_n,
\tag{5}
\]
then (3) gives A1 immediately.

In terms of the compact core, (5) is just
\[
  K_n(T_n)+{3\over4}A_n\ge0.
\]
Thus Gate B is not a simplification unless the tail has an independent
one-sided arithmetic description.

## Gate C: signed tail budget

More generally, suppose A0 is improved to
\[
  |R_n(T_n)|\le \alpha A_n,\qquad 0<\alpha<1,
\]
and the compact target is adjusted to
\[
  K_n(T_n)+(1-\alpha)A_n\ge0.
\]
Then the corresponding strong margin gate is
\[
  \lambda_n\ge 2\alpha A_n.
\]

Letting \(\alpha\) be small makes this gate closer to Li positivity, but it
does not remove the need for a signed theorem.  The absolute tail estimate
never supplies the sign by itself.

## Numerical reconnaissance

A short high-precision Taylor expansion of
\[
  \log\xi\!\left({1\over1-z}\right)
  =
  \log\xi(1)+\sum_{n\ge1}{\lambda_n\over n}z^n
\]
shows that the strong margin is numerically plausible for small \(n\ge8\).
For example, using the standard archimedean split:

| \(n\) | \(\lambda_n\) | \(\lambda_n^{\rm arch}\) | ratio |
|---:|---:|---:|---:|
| 8 | 1.465755677 | 0.020759934 | 70.605 |
| 9 | 1.850916048 | 0.460139644 | 4.023 |
| 10 | 2.279339363 | 0.955310683 | 2.386 |
| 11 | 2.750360838 | 1.500643067 | 1.833 |
| 12 | 3.263255321 | 2.091527079 | 1.560 |

These numbers are only reconnaissance.  They do not prove the uniform
statement and cannot replace the required Euler--Gamma argument.

## Status

This note closes the algebra of the truncation gate:

- A0 plus a strong Li margin closes A1.
- A0 plus a genuinely one-sided tail theorem closes A1.
- A0 alone, even with an optimized cutoff, does not close A1.

The remaining mathematical load is therefore one of the two boxed signed
theorems above.

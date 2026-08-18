# Explicit archimedean positive lower bound

## Purpose

The A0 tail theorem needs an explicit positive lower bound
\[
  0<B_n\le \lambda_n^{\rm arch}\qquad(n\ge8).
\]
This note supplies such a bound from the phase-102 archimedean formula.

This closes the archimedean lower-bound input for A0.  It does not close
A1, because A1 is the remaining signed arithmetic core.

## Archimedean formula

The phase split uses
\[
  \lambda_n^{\rm arch}
  =
  1-{n\over2}\bigl(\gamma+\log(4\pi)\bigr)
  +
  \sum_{\substack{r\ge1\\ r\ {\rm odd}}}
  \left[
    \left(1-{1\over r}\right)^n-1+{n\over r}
  \right].
\tag{1}
\]

Put
\[
  q_n(x)=(1-x)^n-1+nx.
\]
For \(0\le x\le1\),
\[
  q_n(x)\ge0.
\tag{2}
\]

Also,
\[
  q_n(1/r)
  =
  \left(1-{1\over r}\right)^n-1+{n\over r}
  \ge {n\over r}-1.
\tag{3}
\]

We use the elementary numerical upper bound
\[
  \gamma+\log(4\pi)<C,\qquad C={3109\over1000}.
\tag{4}
\]
This follows by standard interval arithmetic, for example from independent
rational intervals for \(\gamma\), \(\pi\), and the logarithm.

## Large range \(n\ge19\)

Let
\[
  K=\left\lfloor {n+1\over2}\right\rfloor,
  \qquad
  M=2K-1,
\]
so that \(M\) is the largest odd integer not exceeding \(n\).  Keeping only
the odd terms \(1,3,\ldots,M\) and using (3),
\[
\begin{aligned}
  \lambda_n^{\rm arch}
  &\ge
  1-{Cn\over2}
  +
  n\sum_{j=1}^{K}{1\over 2j-1}
  -
  K.
\end{aligned}
\tag{5}
\]

For \(K\ge8\), split off the first eight odd reciprocals:
\[
  H_8^{\rm odd}
  =
  \sum_{j=1}^{8}{1\over 2j-1}
  =
  {91072\over45045}.
\tag{6}
\]

Since \(x\mapsto (2x-1)^{-1}\) is decreasing,
\[
  \sum_{j=9}^{K}{1\over2j-1}
  \ge
  \int_{8}^{K}{dx\over 2x+1}
  =
  {1\over2}\log {2K+1\over17}.
\tag{7}
\]

Therefore, for \(n\ge19\),
\[
  \boxed{
  \lambda_n^{\rm arch}
  \ge
  B_n^{\rm arch}
  :=
  1-{Cn\over2}
  +n\left(
    {91072\over45045}
    +{1\over2}\log {2K+1\over17}
  \right)
  -K,
  }
\tag{8}
\]
where \(K=\lfloor(n+1)/2\rfloor\).

For \(n\ge19\), one has \(K\le(n+1)/2\) and \(2K+1\ge n\).  Hence (8) gives
\[
  B_n^{\rm arch}
  \ge
  {1\over2}
  +
  n\left(
    {91072\over45045}
    -{1+C\over2}
    +{1\over2}\log {n\over17}
  \right).
\tag{9}
\]
The bracket is positive already at \(n=19\), and it is increasing
thereafter.  Thus \(B_n^{\rm arch}>0\) for every \(n\ge19\).

Thus (8) is an explicit positive lower bound for every \(n\ge19\).

## Finite range \(8\le n\le18\)

For the remaining indices, use the same formula (1), the upper bound (4),
and only finitely many nonnegative odd summands.  Exact rational arithmetic
gives the following certified lower bounds:

| \(n\) | odd terms retained | certified lower bound |
|---:|---:|---:|
| 8 | \(1\le r\le999\) | \(>1/300\) |
| 9 | \(1\le r\le49\) | \(>1/10\) |
| 10 | \(1\le r\le49\) | \(>1/2\) |
| 11 | \(1\le r\le19\) | \(>1/5\) |
| 12 | \(1\le r\le19\) | \(>1/2\) |
| 13 | \(1\le r\le19\) | \(>9/10\) |
| 14 | \(1\le r\le19\) | \(>13/10\) |
| 15 | \(1\le r\le19\) | \(>17/10\) |
| 16 | \(1\le r\le19\) | \(>2\) |
| 17 | \(1\le r\le19\) | \(>5/2\) |
| 18 | \(1\le r\le19\) | \(>3\) |

For example, the certified quantity for \(n=8\) is
\[
  1-{8C\over2}
  +
  \sum_{\substack{1\le r\le999\\r\ {\rm odd}}}
  \left[
    \left(1-{1\over r}\right)^8-1+{8\over r}
  \right]
  >
  {1\over300}.
\tag{10}
\]
All omitted summands are nonnegative by (2), so each retained partial sum is
a genuine lower bound for \(\lambda_n^{\rm arch}\).

## A0 lower-bound input

Define
\[
  B_n=
  \begin{cases}
    1/300,& n=8,\\
    1/10,& n=9,\\
    1/2,& n=10,\\
    1/5,& n=11,\\
    1/2,& n=12,\\
    9/10,& n=13,\\
    13/10,& n=14,\\
    17/10,& n=15,\\
    2,& n=16,\\
    5/2,& n=17,\\
    3,& n=18,\\
    B_n^{\rm arch},& n\ge19,
  \end{cases}
\tag{11}
\]
with \(B_n^{\rm arch}\) as in (8).

Then
\[
  \boxed{
  0<B_n\le \lambda_n^{\rm arch}\qquad(n\ge8).
  }
\tag{12}
\]

This is the explicit lower-bound input required by
`102_A0_UNIFORM_TAIL_THEOREM.md`.

## Status

Closed.  The archimedean positivity and lower-bound input for A0 is now
internal to phase 102.

The remaining external A0 input is the explicit PNT/zero-free-region
remainder.  The remaining RH-strength obstruction is still A1.

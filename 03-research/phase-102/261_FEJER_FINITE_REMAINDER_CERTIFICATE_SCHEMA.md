# Fejer finite-remainder certificate schema

## Purpose

`259_FEJER_LOG_DENSITY_CLOSURE_THEOREM.md` proves the infinite-range
closure of the Fejer/log-density route once the positive increment measure
and an effective lower Fejer bound are available.  `264` makes the resulting
threshold explicit.

This note records the remaining finite certificate precisely.  It is not a
new asymptotic argument: below the threshold every surviving index must be
checked pointwise, either through the strong margin or directly through the
compact A1 coefficient.

## Infinite-range input

Assume the hypotheses of `264`: there are constants
\[
  a>{1\over2},\qquad B_h,\qquad 0<\theta_0\le\pi
\]
and a positive increment-measure decomposition satisfying the local
log-density lower bound.  Put
\[
  B_h^\ast
  =
  \max\{B_h,\ a(-\log(2\sin(\theta_0/2)))_+\}.
\]

Then `264` gives strong margin for every
\[
\boxed{
  n\ge
  N_\infty
  =
  \max\left(
    2,\,
    \left\lceil
      \exp\left(
        {3+a+B_h^\ast\over a-1/2}
      \right)
    \right\rceil
  \right).
}
\tag{1}
\]

Together with A0, this proves compact A1 for every \(n\ge N_\infty\).

Thus the only indices left by this route are
\[
\boxed{8\le n<N_\infty.}
\tag{2}
\]

## Strong-margin finite certificate

For a finite set \(E\subset\mathbb N\), a strong-margin interval certificate
consists of rational intervals
\[
  \lambda_n\in[\lambda_n^-,\lambda_n^+],
  \qquad
  A_n\in[A_n^-,A_n^+]
  \qquad(n\in E),
\]
with rigorous outward rounding, such that
\[
\boxed{
  \lambda_n^- - {1\over2}A_n^+\ge0
  \qquad(n\in E).
}
\tag{3}
\]

Then
\[
  \lambda_n\ge {1\over2}A_n
  \qquad(n\in E),
\]
and A0 gives
\[
  R_n(T_n)\le {1\over4}A_n.
\]
Consequently
\[
  C_n(T_n)
  =
  \lambda_n-{1\over4}A_n-R_n(T_n)
  \ge
  {1\over2}A_n-{1\over4}A_n-{1\over4}A_n
  =
  0.
\tag{4}
\]

So (3) closes compact A1 on the finite set \(E\).

For the Fejer route, the required finite set is exactly
\[
  E=\{n\in\mathbb N:8\le n<N_\infty\}.
\tag{5}
\]

## Direct compact-A1 finite certificate

The strong-margin check is sufficient but not necessary.  A sharper finite
certificate may instead enclose the actual compact coefficient
\[
  C_n(T_n)
  =
  \lambda_n-{1\over4}A_n-R_n(T_n)
\tag{6}
\]
directly.

Namely, if rigorous intervals satisfy
\[
  C_n(T_n)\in[C_n^-,C_n^+],
  \qquad
  C_n^-\ge0
  \qquad(n\in E),
\tag{7}
\]
then compact A1 is proved on \(E\).  This route may use the finite
prime-power expressions from `148`, the moving-diagonal generator from
`149`, or the single-transform form from `230`, provided every endpoint,
prime-power sum, and special-function value is enclosed with certified
outward rounding.

## Why this is the exact finite remainder

Let the log-density theorem of `264` hold.  For \(n\ge N_\infty\), A1 is
already proved by the infinite-range strong-margin argument.  For
\(8\le n<N_\infty\), no averaging, density-one statement, or asymptotic
slack can replace a pointwise certificate, by `256` and `257`.

Therefore the following implication is exact:
\[
\boxed{
\begin{gathered}
  \hbox{positive increment measure plus local log-density of `264`}\\
  \hbox{and either (3) or (7) for all }8\le n<N_\infty\\
  \Longrightarrow
  \hbox{compact A1 for every }n\ge8.
\end{gathered}
}
\tag{8}
\]

The initial range \(1\le n\le7\) is already covered by the phase-102 base
certificate.  Hence (8), A0, and the base certificate complete the compact
A1 assembly.

## Status

Closed as the finite-remainder schema for the Fejer/log-density route.
It does not prove the positive measure or local density theorem; it states
the exact finite interval verification needed after that theorem is proved.

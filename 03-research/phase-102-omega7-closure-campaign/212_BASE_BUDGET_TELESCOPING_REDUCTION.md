# Base-budget telescoping reduction

## Purpose

`210_BASE_BUDGET_QUADRATIC_COEFFICIENT_GATE.md` introduced the coefficient
\[
  \Gamma_{\mathcal B}
  =
  {\Delta_8^\ast\over16}
  +
  {1\over2}\sum_{k=8}^{\infty}
  {1+\frac34D_k^{\rm arch}\over k(k+1)}.
\tag{1}
\]

This note removes the infinite archimedean series from (1).  The weighted
second-difference combination \(D_k^{\rm arch}\) telescopes exactly.

## Telescoping identity

Let
\[
  A_n=\lambda_n^{\rm arch}
\]
and
\[
  D_k^{\rm arch}
  =
  kA_{k+1}-(2k+1)A_k+(k+1)A_{k-1}.
\tag{2}
\]

For \(M\ge8\),
\[
\begin{aligned}
  \sum_{k=8}^{M}{D_k^{\rm arch}\over k(k+1)}
  &=
  \sum_{k=8}^{M}
  \left(
    {A_{k+1}\over k+1}
    -{(2k+1)A_k\over k(k+1)}
    +{A_{k-1}\over k}
  \right).
\end{aligned}
\tag{3}
\]

All interior coefficients cancel.  The only boundary terms are
\[
\boxed{
  \sum_{k=8}^{M}{D_k^{\rm arch}\over k(k+1)}
  =
  {A_7-A_8\over8}
  +
  {A_{M+1}-A_M\over M+1}.
}
\tag{4}
\]

Since
\[
  A_n={1\over2}n\log n+O(n),
\]
one has
\[
  {A_{M+1}-A_M\over M+1}\to0.
\tag{5}
\]
Therefore
\[
\boxed{
  \sum_{k=8}^{\infty}{D_k^{\rm arch}\over k(k+1)}
  =
  {A_7-A_8\over8}.
}
\tag{6}
\]

Also
\[
\boxed{
  \sum_{k=8}^{\infty}{1\over k(k+1)}={1\over8}.
}
\tag{7}
\]

Substituting (6)--(7) into (1) gives the finite formula
\[
\boxed{
  \Gamma_{\mathcal B}
  =
  {\Delta_8^\ast\over16}
  +
  {1\over16}
  +
  {3(A_7-A_8)\over64}.
}
\tag{8}
\]

Equivalently,
\[
\boxed{
  64\,\Gamma_{\mathcal B}
  =
  4\Delta_8^\ast+4+3(A_7-A_8).
}
\tag{9}
\]

## Consequence

The large-\(n\) terminal budget sign is not controlled by an infinite
archimedean tail.  It is a finite boundary question:
\[
\boxed{
  4\Delta_8^\ast+4+3(A_7-A_8)>0
}
\tag{10}
\]
is exactly the condition \(\Gamma_{\mathcal B}>0\).

Here
\[
  \Delta_8^\ast=C_8^\ast-C_7^\ast
\tag{11}
\]
in the moving-diagonal recurrence notation, and \(A_7,A_8\) are the
explicit archimedean terms from the phase split.

Thus the terminal absorption problem from `208` and `210` has been reduced
to a finite base certificate.  It is no longer an infinite asymptotic
series problem.

Using the phase archimedean formula,
\[
  A_8-A_7
  =
  0.37663065569551211096705549126733534516\ldots .
\tag{12}
\]
Consequently (10) is equivalent to
\[
\boxed{
  \Delta_8^\ast
  >
  -1+{3\over4}(A_8-A_7)
  =
  -0.71752700822836591677470838154949849113\ldots .
}
\tag{13}
\]

This is the exact finite threshold for positivity of
\(\Gamma_{\mathcal B}\).

## Why this still does not close A1

Even if (10), equivalently (13), is verified, it proves only that the base budget is eventually
large enough to absorb the terminal \(O(\log n)\) load.  It does not prove:

1. the finite threshold and finite range for terminal absorption;
2. domination of the mixed off-diagonal load from `211`;
3. the signed compact A1 inequality directly.

Therefore this is a genuine simplification of Theorem B's terminal budget,
not a closure of A1.

## Status

Closed as a telescoping reduction of \(\Gamma_{\mathcal B}\).

A1 remains open.  The next finite task in this subroute is to certify
\(\Delta_8^\ast>-0.7175270082283659\ldots\), then return to the
mixed-interval load.

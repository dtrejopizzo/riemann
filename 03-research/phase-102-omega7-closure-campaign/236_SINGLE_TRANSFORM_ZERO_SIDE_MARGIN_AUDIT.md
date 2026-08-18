# Single-transform zero-side margin audit

## Purpose

`230_SINGLE_TRANSFORM_A1_FRONTIER.md` reduces A1 to the signed transform
\[
  S_n(T_n)=
  \sum_{m\le e^{T_n}}{\Lambda(m)\over m}L_{n-1}^{(1)}(\log m).
\]

`113_MELLIN_COBORDER_NORMAL_FORM.md` writes the same compact core by
Perron/Mellin inversion.  This note records what a zero-side or explicit
formula attack would have to prove.

The point is subtle but important:

\[
  \hbox{critical-line support / Li positivity}
  \quad\hbox{does not by itself give compact A1.}
\]

A1 requires an additional margin or one-sided tail placement.

## Compact A1 versus Li positivity

From `150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md` and the later base
certificates, the compact quantity satisfies
\[
\boxed{
  C_n(T_n)
  =
  \lambda_n
  -
  {1\over4}\lambda_n^{\rm arch}
  -
  R_n(T_n).
}
\tag{1}
\]

A0 gives the absolute tail estimate
\[
\boxed{
  |R_n(T_n)|\le {1\over4}\lambda_n^{\rm arch}.
}
\tag{2}
\]

Therefore A1 follows from the strong margin
\[
\boxed{
  \lambda_n\ge {1\over2}\lambda_n^{\rm arch}.
}
\tag{3}
\]

Li positivity alone gives only
\[
  \lambda_n\ge0.
\tag{4}
\]

Equations (1)--(2) show why (4) is not enough for compact A1: the worst
allowed tail and the explicit subtraction can consume
\(\frac12\lambda_n^{\rm arch}\).

Thus an explicit-formula proof of A1 must prove more than the ordinary
zero-side Li criterion.  It must prove either (3), a one-sided tail theorem
for \(R_n(T_n)\), or an equivalent comparative/global theorem.

## Mellin explicit-formula gate

For fixed \(T\), `113` gives the finite Mellin kernel
\[
  P_{n,T}(s)=\int_0^T e^{-su}L_{n-1}^{(1)}(u)\,du
\tag{5}
\]
and the Perron representation
\[
  S_n(T)
  =
  {1\over2\pi i}
  \int_{c-i\infty}^{c+i\infty}
  -{\zeta'\over\zeta}(1+s)P_{n,T}(s)\,ds.
\tag{6}
\]

After completion and contour shifting, the nontrivial zeros enter through
terms of the schematic form
\[
\boxed{
  \mathfrak Z_{n,T}
  =
  \sum_\rho P_{n,T}(\rho-1),
}
\tag{7}
\]
plus pole, Gamma, and endpoint terms.

The zero-side Li kernel
\[
  1-\left(1-{1\over\rho}\right)^n
\tag{8}
\]
has a positive paired form on the critical line.  The truncated compact
kernel \(P_{n,T}(\rho-1)\) is a different object.  It depends on \(T\), and
its paired critical-line contribution is not a manifest nonnegative square
without an additional margin theorem.

Consequently, a contour-shift identity for (6) is not a proof of A1.  It
only moves the signed compact problem from prime powers to zero residues.

## Exact zero-side theorem that would close A1

The zero-side route must prove, for the moving cutoffs \(T_n\),
\[
\boxed{
  \lambda_n
  -
  {1\over4}\lambda_n^{\rm arch}
  -
  R_n(T_n)
  \ge0
  \qquad(n\ge8),
}
\tag{9}
\]
using the completed explicit formula before invoking the desired compact
sign.

Equivalent sufficient versions are:

1. strong margin:
   \[
     \lambda_n\ge {1\over2}\lambda_n^{\rm arch};
   \]
2. one-sided tail:
   \[
     R_n(T_n)\le \lambda_n-{1\over4}\lambda_n^{\rm arch};
   \]
3. a completed-kernel positivity theorem whose diagonal is exactly (9);
4. a global half-plane theorem that implies (9) directly.

Ordinary Li positivity or critical-line support proves RH, but it is not
the same internal compact statement as A1 unless one of the extra margin
links above is supplied.

## Status

Closed as a zero-side margin audit for the single-transform frontier.

A1 remains open.  The explicit-formula route must prove a compact margin,
not merely restate Li/RH.

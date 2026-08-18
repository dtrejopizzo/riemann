# Bordered Euler current audit for A1

## Purpose

The second surviving mechanism for A1 is a bordered Euler current. This
document separates a genuine proof mechanism from a determinant tautology.

## Desired form

Let
\[
  C_n
  =
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
  +{3\over4}\lambda_n^{\rm arch}.
\]

The desired bordered-current proof would construct finite Hermitian data
\[
  H_n^{\rm base}>0,\qquad H_n^{\rm border},
\]
from Euler--Gamma arithmetic such that
\[
  C_n={\det H_n^{\rm border}\over \det H_n^{\rm base}},
\tag{1}
\]
and such that nonnegativity of the quotient follows from an independent
structural theorem.

## Schur complement identity

Every bordered Hermitian matrix
\[
  H^{\rm border}
  =
  \begin{pmatrix}
    H^{\rm base} & v\\
    v^* & a
  \end{pmatrix},
  \qquad H^{\rm base}>0,
\]
satisfies
\[
  {\det H^{\rm border}\over\det H^{\rm base}}
  =
  a-v^*(H^{\rm base})^{-1}v.
\tag{2}
\]

The right side is the Schur complement. Therefore
\[
  {\det H^{\rm border}\over\det H^{\rm base}}\ge0
  \quad\Longleftrightarrow\quad
  H^{\rm border}\ge0.
\tag{3}
\]

If (1) is built by choosing \(a,v,H^{\rm base}\) so that the Schur complement
equals \(C_n\), then (3) says only
\[
  C_n\ge0\Longleftrightarrow H_n^{\rm border}\ge0.
\]

That is a coordinate change, not a proof.

## Tautological class eliminated

The following class does not close A1:
\[
  \hbox{construct }H_n^{\rm border}
  \hbox{ so that its Schur complement equals }C_n,
  \hbox{ then assert }H_n^{\rm border}\ge0.
\]

It is exactly equivalent to the missing inequality unless the positivity of
the bordered form is derived from a separate Euler--Gamma theorem.

## Non-tautological requirement

A bordered Euler current remains viable only if it proves all of the
following:

1. \(H_n^{\rm base}>0\) from a known positive structure independent of Li.
2. The identity (1) by algebraic expansion, with no use of \(C_n\ge0\).
3. \(H_n^{\rm border}\ge0\) from an Euler--Gamma energy, monotonicity,
   Herglotz property, or variational principle that fails for an admissible
   off-line control.

The third item is the actual force-RH theorem. The determinant quotient is
only useful if it exposes that theorem.

## Minimal live theorem

The bordered route closes A1 exactly if it proves:

For every \(n\ge8\), there exists a canonically constructed bordered form
whose Schur complement is \(C_n\), and whose positivity follows from a
zeta-specific Euler--Gamma principle not valid for off-line controls.

## Status

The determinant algebra is closed. The tautological bordered route is
eliminated. The non-tautological bordered route remains open and is equivalent
to proving an independent positivity theorem for \(H_n^{\rm border}\).

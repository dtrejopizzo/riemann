# Quarter-margin generator RH-strength audit

## Purpose

`247_QUARTER_MARGIN_NONPOSITIVE_TAIL_GATE.md` isolates the sufficient route
\[
  \lambda_n\ge {1\over4}A_n,
  \qquad
  R_n(T_n)\le0,
  \qquad A_n=\lambda_n^{\rm arch}.
\]

This note writes the exact generator for the first inequality and records
its logical strength.  The quarter margin is weaker than the strong margin,
but it is still an infinite Li-family positivity theorem strong enough to
imply RH once the finite low indices are certified.

## Quarter-margin generator

Let
\[
  \mathcal L(z)=\sum_{n\ge1}\lambda_nz^n,
  \qquad
  \mathcal A(z)=\sum_{n\ge1}A_nz^n.
\]

Define
\[
\boxed{
  \mathcal Q_{1/4}(z)
  =
  \mathcal L(z)-{1\over4}\mathcal A(z).
}
\tag{1}
\]

Then
\[
\boxed{
  [z^n]\mathcal Q_{1/4}
  =
  \lambda_n-{1\over4}A_n.
}
\tag{2}
\]

Thus the quarter margin is exactly
\[
\boxed{
  [z^n]\mathcal Q_{1/4}\ge0
  \qquad(n\ge8).
}
\tag{3}
\]

Using the Euler--Gamma split
\[
  \mathcal L(z)
  =
  \mathcal A(z)
  -
  {z\over(1-z)^2}
  -
  {z\over(1-z)^3}
  \int_0^\infty
    E(e^u)\exp\!\left(-{u\over1-z}\right)\,du,
\]
we have
\[
\boxed{
  \mathcal Q_{1/4}(z)
  =
  {3\over4}\mathcal A(z)
  -
  {z\over(1-z)^2}
  -
  {z\over(1-z)^3}
  \int_0^\infty
    E(e^u)\exp\!\left(-{u\over1-z}\right)\,du.
}
\tag{4}
\]

Coefficientwise, if
\[
  \lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime},
\]
then
\[
\boxed{
  [z^n]\mathcal Q_{1/4}
  =
  {3\over4}A_n+\lambda_n^{\rm prime}.
}
\tag{5}
\]

So the quarter margin is the signed prime lower bound
\[
\boxed{
  \lambda_n^{\rm prime}\ge-{3\over4}A_n
  \qquad(n\ge8).
}
\tag{6}
\]

## Relation to compact A1

From the compact-tail identity,
\[
  C_n(T_n)=\lambda_n-{1\over4}A_n-R_n(T_n).
\]

Hence
\[
\boxed{
  C_n(T_n)
  =
  [z^n]\mathcal Q_{1/4}
  -
  R_n(T_n).
}
\tag{7}
\]

Therefore
\[
\boxed{
  [z^n]\mathcal Q_{1/4}\ge0
  \quad\hbox{and}\quad
  R_n(T_n)\le0
  \quad\Longrightarrow\quad
  C_n(T_n)\ge0.
}
\tag{8}
\]

This is the generator form of `247`.

## RH-strength

For \(n\ge8\), the archimedean coefficients satisfy
\[
  A_n>0.
\tag{9}
\]

Thus the quarter margin (3) implies
\[
  \lambda_n\ge {1\over4}A_n>0
  \qquad(n\ge8).
\tag{10}
\]

Together with the finite low-index certificate for \(1\le n\le7\), this
gives
\[
\boxed{
  \lambda_n\ge0
  \qquad(n\ge1).
}
\tag{11}
\]

By Li's criterion, (11) is equivalent to RH.  Therefore
\[
\boxed{
  \hbox{quarter margin for }n\ge8
  \quad+\quad
  \hbox{finite low-index Li certificate}
  \quad\Longrightarrow\quad
  \mathrm{RH}.
}
\tag{12}
\]

Consequently a proof of the quarter-margin generator positivity (3) is not
a soft consequence of A0 or symmetric PNT envelopes.  It is an RH-strength
infinite positivity theorem, albeit with a lower archimedean barrier than
the strong margin.

## Status

Closed as the quarter-margin generator and RH-strength audit.

A1 remains open.  The quarter-margin route still needs both generator
positivity (3) and the signed tail theorem \(R_n(T_n)\le0\), or an
equivalent direct proof of \(C_n(T_n)\ge0\).

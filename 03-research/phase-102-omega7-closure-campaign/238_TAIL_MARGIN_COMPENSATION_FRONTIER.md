# Tail-margin compensation frontier

## Purpose

`236_SINGLE_TRANSFORM_ZERO_SIDE_MARGIN_AUDIT.md` records that Li positivity
alone does not imply compact A1.  The exact identity is
\[
  C_n(T_n)=\lambda_n-{1\over4}A_n-R_n(T_n),
  \qquad A_n=\lambda_n^{\rm arch}.
\]

This note writes the remaining one-sided-tail route in its sharp
non-tautological form.  It separates the strong-margin deficit from the
tail surplus.

## Margin variables

Define the strong-margin excess
\[
\boxed{
  M_n=\lambda_n-{1\over2}A_n,
}
\tag{1}
\]
and the A0 tail surplus
\[
\boxed{
  \delta_n={1\over4}A_n-R_n(T_n).
}
\tag{2}
\]

A0 gives the upper tail bound
\[
  R_n(T_n)\le {1\over4}A_n,
\tag{3}
\]
so
\[
\boxed{
  \delta_n\ge0.
}
\tag{4}
\]

Substituting (1)--(2) into the compact identity gives
\[
\boxed{
  C_n(T_n)=M_n+\delta_n.
}
\tag{5}
\]

Therefore A1 is exactly
\[
\boxed{
  M_n+\delta_n\ge0
  \qquad(n\ge8).
}
\tag{6}
\]

This is the tail-margin compensation frontier.

## Relation to known sufficient gates

The strong-margin gate is
\[
  M_n\ge0.
\tag{7}
\]
Together with (4), it immediately gives (6).

The one-sided tail gate can be written as
\[
  \delta_n\ge -M_n.
\tag{8}
\]

This is more precise than simply saying
\[
  R_n(T_n)\le \lambda_n-{1\over4}A_n,
\]
because it shows exactly what must be compensated: only the negative part
of the strong-margin excess.

## Why global Li positivity is insufficient

Li positivity gives
\[
  \lambda_n\ge0,
\tag{9}
\]
or equivalently
\[
  M_n\ge -{1\over2}A_n.
\tag{10}
\]

A0 gives only \(\delta_n\ge0\).  The data (10) and (4) allow
\[
  M_n=-{1\over2}A_n,\qquad \delta_n=0,
\tag{11}
\]
which would give \(C_n(T_n)<0\).

Thus any proof that uses global Li positivity plus A0 must add a
quantitative compensation theorem:
\[
\boxed{
  \delta_n\ge \max(0,-M_n)
  \quad\hbox{or directly}\quad
  M_n+\delta_n\ge0.
}
\tag{12}
\]

## Arithmetic content of \(\delta_n\)

By definition,
\[
  R_n(T_n)
  =
  -\int_{T_n}^{\infty}
  E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du,
\tag{13}
\]
so
\[
\boxed{
  \delta_n
  =
  {1\over4}A_n
  +
  \int_{T_n}^{\infty}
  E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
}
\tag{14}
\]

A0 proves that the integral in (14) is not less than \(-A_n/4\).  A1 needs
the stronger, index-dependent lower bound
\[
\boxed{
  \int_{T_n}^{\infty}
  E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  \ge
  -{1\over4}A_n-M_n.
}
\tag{15}
\]

This is a signed tail correlation theorem.  A two-sided estimate for
\(|E|\) cannot prove (15) unless it is strong enough to force the left side
above the required signed threshold, and all previous VK-scale absolute
routes fail in the Laguerre bulk.

## Current live theorem

The one-sided-tail route now has the exact target:
\[
\boxed{
  \lambda_n-{1\over2}A_n
  +
  {1\over4}A_n
  +
  \int_{T_n}^{\infty}
  E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  \ge0.
}
\tag{16}
\]

Equivalently,
\[
\boxed{
  \lambda_n-{1\over4}A_n
  +
  \int_{T_n}^{\infty}
  E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  \ge0.
}
\tag{17}
\]

This is just \(C_n(T_n)\ge0\) in tail-margin coordinates, but it isolates
the only non-tautological way the one-sided tail can help: it must provide
enough positive surplus \(\delta_n\) to cover any failure of strong margin.

## Status

Closed as the exact tail-margin compensation frontier.

A1 remains open.  The missing theorem is a signed lower bound for
\(\delta_n\) relative to the strong-margin deficit \(-M_n\), or a direct
proof that \(M_n+\delta_n\ge0\).

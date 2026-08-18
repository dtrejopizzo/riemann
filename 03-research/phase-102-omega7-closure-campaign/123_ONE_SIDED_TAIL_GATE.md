# One-sided tail gate

## Purpose

The A0 theorem gives an absolute tail estimate. This document states the
one-sided tail theorem that would be strong enough to close A1 and records
why ordinary PNT control does not supply it.

## Tail notation

For \(n\ge8\), write
\[
  A_n=\lambda_n^{\rm arch}>0
\]
and
\[
  R_n(T)
  =
  \lim_{\varepsilon\downarrow0}
  \int_{e^T}^{\infty}(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy .
\]

A0 gives, for a suitable \(T_n\),
\[
  |R_n(T_n)|\le {1\over4}A_n.
\tag{1}
\]

## One-sided theorem sufficient for A1

Since
\[
  \lambda_n
  =
  K_n(T_n)+R_n(T_n)+A_n,
\]
where
\[
  K_n(T_n)=
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy,
\]
A1 is equivalent to
\[
  K_n(T_n)+{3\over4}A_n\ge0.
\]

Equivalently,
\[
  \lambda_n\ge R_n(T_n)+{1\over4}A_n.
\tag{2}
\]

Thus a one-sided tail theorem closes A1 if it proves
\[
  R_n(T_n)\le \lambda_n-{1\over4}A_n.
\tag{3}
\]

This is not useful in this form because it mentions \(\lambda_n\). A useful
version would be an arithmetic upper bound
\[
  R_n(T_n)\le S_n
\tag{4}
\]
together with a signed compact or archimedean theorem proving
\[
  S_n+{1\over4}A_n\le \lambda_n.
\tag{5}
\]

Equations (4)--(5) must be proved without already knowing Li positivity.

## Why PNT tails do not give it

A PNT estimate controls
\[
  |\psi(y)-y|.
\]
After multiplying by \(f'_{n,\varepsilon}(y)\), whose sign oscillates with the
Laguerre kernel, this gives only an absolute bound. It does not determine
whether the tail helps or hurts the compact core.

The sign of \(R_n(T_n)\) depends on the relative phase between prime-power
fluctuations and the Laguerre derivative. A zero-free-region error term does
not encode that phase sharply enough.

## Valid live target

A valid one-sided tail theorem would need a signed explicit formula for the
tail:
\[
  R_n(T_n)
  =
  \mathcal R_n^{+}-\mathcal R_n^{-},
\]
with a proof that the negative part is dominated in the required direction
after the pole/Gamma pairing. Such a theorem would be another form of the
positive boundary measure target.

## Status

The one-sided tail gate is formulated but open. Ordinary A0/PNT tails are
insufficient; a signed tail theorem would carry the same arithmetic
discriminant as A1.

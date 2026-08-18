# A1 - Signed compact core reduction

## Core theorem

For each \(n\ge8\), let \(T_n\) be any cutoff satisfying A0. Define
\[
  C_n
  =
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
  +{3\over4}\lambda_n^{\rm arch}.
\]

A1 is the assertion
\[
  C_n\ge0\qquad(n\ge8).
\]

## Equivalent prime-power form

For \(X=e^{T_n}\), Stieltjes integration gives
\[
  -n+\int_1^X(\psi(y)-y)f'_{n,0}(y)\,dy
  =
  -n+(\psi(X)-X)f_{n,0}(X)
  -\int_{1^-}^X f_{n,0}(y)\,d(\psi(y)-y).
\]
Thus
\[
  C_n=
  -n+(\psi(X)-X)f_{n,0}(X)
  -\sum_{m\le X}\Lambda(m)m^{-1}L_{n-1}^{(1)}(\log m)
  +\int_1^X y^{-1}L_{n-1}^{(1)}(\log y)\,dy
  +{3\over4}\lambda_n^{\rm arch}.
\]

The continuous integral is explicit:
\[
  \int_1^X y^{-1}L_{n-1}^{(1)}(\log y)\,dy
  =
  \int_0^{T_n}L_{n-1}^{(1)}(t)\,dt.
\]

## Why this is the live core

Every term in \(C_n\) is finite. No divergent polar or prime series remains.
The expression still keeps the signed Laguerre oscillation against the prime
powers. This is exactly where a proof must create new arithmetic control.

## Failed local routes

The following routes do not close A1:

- bounding each prime-power term by its magnitude;
- grouping by a bounded number of Laguerre lobes;
- replacing \(\psi(y)-y\) by a PNT envelope on the compact core;
- proving positivity for \(n\le N\) without a uniform theorem;
- using a positive factorization whose symbol is equivalent to Li positivity.

These failures eliminate only their own classes. They do not rule out a
global signed identity for \(C_n\).

## Status

Open. The phase has reduced \(\Omega_7\) to the nonnegativity of \(C_n\) for
all \(n\ge8\).

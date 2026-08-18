# Explicit PNT input adapter

## Purpose

After `151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md`, the only
external input left in A0 is the explicit prime-number-theorem remainder.
This note records exactly what kind of PNT estimate is compatible with the
A0 tail theorem and what kind is not.

## A0-compatible form

The A0 theorem needs constants \(A\ge1\), \(U_0\), and an increasing
function \(\eta\) on \([U_0,\infty)\) such that
\[
  |\psi(y)-y|\le A y e^{-\eta(\log y)}
  \qquad(y\ge e^{U_0})
\tag{1}
\]
and
\[
  {\eta(u)\over \log(1+u)}\to+\infty.
\tag{2}
\]

Any explicit Vinogradov--Korobov PNT remainder of the form
\[
  |\psi(y)-y|
  \le
  A y
  \exp\!\left(
    -a {(\log y)^{3/5}\over(\log\log y)^{1/5}}
  \right)
  \qquad(y\ge e^{U_0})
\tag{3}
\]
is admissible.  In A0 notation this is
\[
  \eta(u)=a{u^{3/5}\over(\log u)^{1/5}}.
\tag{4}
\]
Then (2) holds because
\[
  {u^{3/5}\over(\log u)^{6/5}}\to+\infty.
\]

Thus, once concrete published constants \(A,a,U_0\) are selected, the A0
cutoff condition becomes
\[
  a{u^{3/5}\over(\log u)^{1/5}}
  \ge
  (n+1)\log(1+u)+
  \log {12A n^2\over B_n}
  \qquad(u\ge T_n),
\tag{5}
\]
where \(B_n\) is supplied by `151`.

## Why a constant relative Chebyshev bound is insufficient

Bounds of the form
\[
  |\psi(y)-y|\le \varepsilon y
  \qquad(y\ge Y_0)
\tag{6}
\]
are useful explicit Chebyshev estimates, but they do not close A0.

Indeed, after the change of variables \(u=\log y\), the A0 majorant has the
shape
\[
  |E(e^u)|e^{-u}(1+u)^{n-1}.
\tag{7}
\]
If (6) is used, this becomes
\[
  \varepsilon(1+u)^{n-1},
\]
whose integral over \(u\ge T\) diverges.  Therefore A0 requires a decaying
relative error, not only a small constant relative error.

This explains why sharp finite-range Chebyshev bounds do not by themselves
provide the A0 tail cutoff.

## Mechanical cutoff choice

Given (3), define \(T_n\) as any number satisfying:

1. \(T_n\ge U_0\);
2. \(T_n\) lies beyond a monotonicity threshold for
   \[
     a{u^{3/5}\over(\log u)^{1/5}}
     -
     (n+1)\log(1+u);
   \]
3. inequality (5) holds at \(u=T_n\).

Then (5) holds for all \(u\ge T_n\), and the proof of
`102_A0_UNIFORM_TAIL_THEOREM.md` gives
\[
  \sup_{0\le\varepsilon\le1}
  \left|
  \int_{e^{T_n}}^\infty
  (\psi(y)-y)f'_{n,\varepsilon}(y)\,dy
  \right|
  \le {1\over4}\lambda_n^{\rm arch}.
\tag{8}
\]

## Status

Closed as an adapter.  The A0 theorem now has:

- an internal archimedean lower bound \(B_n\) from `151`;
- an exact external PNT shape to import, namely an explicit decaying
  Vinogradov--Korobov bound such as (3).

This is not an A1 result.  The signed compact core remains the only
RH-strength obstruction in the direct route.

# Moving-cutoff flow normal form

## Purpose

The fixed-cutoff generating function isolates a coefficient route for the
compact A1 core, but A0 supplies cutoffs \(T_n\) depending on \(n\).  This
document writes the exact flow of the compact core as the cutoff moves.  The
result is a new normal form for the missing signed theorem.

## Compact core as a function of the cutoff

For \(n\ge1\), define
\[
  K_n(T)
  =
  -n+\int_1^{e^T}(\psi(y)-y)f'_{n,0}(y)\,dy.
\]

With \(y=e^u\) and
\[
  L_n(u)=L_{n-1}^{(1)}(u),
\]
one has
\[
  f'_{n,0}(e^u)e^u
  =
  e^{-u}\left(L'_n(u)-L_n(u)\right).
\]

Thus
\[
  K_n(T)
  =
  -n+\int_0^T
  (\psi(e^u)-e^u)e^{-u}
  \left(L'_n(u)-L_n(u)\right)\,du.
\tag{1}
\]

## Cutoff derivative

Differentiating (1) gives the exact flow
\[
  {d\over dT}K_n(T)
  =
  (\psi(e^T)-e^T)e^{-T}
  \left(L'_n(T)-L_n(T)\right).
\tag{2}
\]

Therefore, for any two cutoffs \(S<T\),
\[
  K_n(T)-K_n(S)
  =
  \int_S^T
  (\psi(e^u)-e^u)e^{-u}
  \left(L'_n(u)-L_n(u)\right)\,du.
\tag{3}
\]

This identity is exact and contains no limiting operation.

## Generating function for the flow

The Laguerre generating identity gives
\[
  \sum_{n\ge1}L_n(u)z^n
  =
  {z\over(1-z)^2}
  \exp\!\left(-{uz\over1-z}\right).
\]

Differentiating in \(u\) and subtracting yields
\[
  \sum_{n\ge1}
  \left(L'_n(u)-L_n(u)\right)z^n
  =
  -{z\over(1-z)^3}
  \exp\!\left(-{uz\over1-z}\right).
\tag{4}
\]

Combining (2) and (4),
\[
  \sum_{n\ge1}{d\over dT}K_n(T)z^n
  =
  -(\psi(e^T)-e^T)e^{-T}
  {z\over(1-z)^3}
  \exp\!\left(-{Tz\over1-z}\right).
\tag{5}
\]

This is the exact boundary-current density for the moving cutoff.

## Moving-cutoff decomposition

Fix a reference cutoff \(S\).  Then the A1 quantity satisfies
\[
\begin{aligned}
  K_n(T_n)+{3\over4}\lambda_n^{\rm arch}
  &=
  K_n(S)+{3\over4}\lambda_n^{\rm arch}  \\
  &\quad+
  \int_S^{T_n}
  (\psi(e^u)-e^u)e^{-u}
  \left(L'_n(u)-L_n(u)\right)\,du.
\end{aligned}
\tag{6}
\]

Thus a fixed-cutoff coefficient theorem closes A1 only if the moving-flow
remainder in (6) has a one-sided lower bound compatible with the fixed-core
margin.

## Exact signed gate

A sufficient moving-cutoff theorem is the following.

There exist a reference cutoff \(S\) and nonnegative margins \(M_n\) such
that
\[
  K_n(S)+{3\over4}\lambda_n^{\rm arch}\ge M_n
  \qquad(n\ge8),
\tag{7}
\]
and
\[
  \int_S^{T_n}
  (\psi(e^u)-e^u)e^{-u}
  \left(L'_n(u)-L_n(u)\right)\,du
  \ge -M_n
  \qquad(n\ge8).
\tag{8}
\]

Then A1 follows.

The hard part is (8).  It is a signed correlation between the prime-power
error \(\psi(e^u)-e^u\) and the Laguerre boundary current.  The A0 theorem
controls the absolute value of this integral only after \(T_n\), not the
one-sided sign of the interval between a fixed reference cutoff and \(T_n\).

## Why absolute flow estimates do not close the gate

Replacing (8) by
\[
  \left|
  \int_S^{T_n}
  (\psi(e^u)-e^u)e^{-u}
  \left(L'_n(u)-L_n(u)\right)\,du
  \right|
  \le M_n
\]
is a valid sufficient theorem only if the margin \(M_n\) is large enough.
Known PNT/Laguerre absolute bounds on the moving interval are too large in
the oscillatory range, because the degree \(n\) grows while \(T_n\) is chosen
precisely to dominate that growth only in the far tail.

Thus the moving-flow gate again requires sign preservation before taking
magnitudes.

## Relation to A0

A0 says that the flow from \(T_n\) to infinity is small in absolute value:
\[
  \left|K_n(\infty)-K_n(T_n)\right|
  \le {1\over4}\lambda_n^{\rm arch}
\]
in the paired limiting sense.

The present document concerns the earlier flow from a fixed \(S\) to
\(T_n\).  This is part of the compact core, not the A0 tail.  It is exactly
where A1 still lives.

## Eliminated class

The following proof pattern is eliminated:

1. prove positivity for a fixed-cutoff generating function;
2. vary the cutoff to \(T_n\);
3. ignore or absolutely bound the moving-flow term without a matching
   signed margin.

The moving-flow term is an exact finite integral and must be controlled
one-sidedly.

## Status

The moving-cutoff normal form is closed.  It does not prove A1.  It reduces
the coefficient-route obstruction to the signed boundary-current inequality
(8).

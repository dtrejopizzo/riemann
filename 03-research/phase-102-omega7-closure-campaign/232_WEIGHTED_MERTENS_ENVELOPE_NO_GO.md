# Weighted Mertens envelope no-go

## Purpose

`231_HIGH_BLOCK_PARTIAL_SUMMATION_FORM.md` rewrites the high block in
terms of
\[
  A_8(u)=\sum_{e^{T_8}\le m\le e^u}{\Lambda(m)\over m}
\]
and its discrepancy
\[
  E_8^\sharp(u)=A_8(u)-(u-T_8).
\]

This note audits whether a two-sided size bound for \(E_8^\sharp\) can
close the remaining signed theorem.  It cannot.  Such a bound again
produces an absolute \(L^1\) Laguerre load, now for \(L_{n-2}^{(2)}\), and
VK-scale decay is still subexponential compared with Laguerre bulk growth.

## Symmetric discrepancy envelope

Suppose one knows only
\[
  |E_8^\sharp(u)|\le M(u)
  \qquad(T_8\le u\le T_n),
\tag{1}
\]
where \(M(u)\ge0\).

The unresolved signed object from `231` is
\[
  E_8^\sharp(T_n)L_{n-1}^{(1)}(T_n)
  +
  \int_{T_8}^{T_n}E_8^\sharp(u)L_{n-2}^{(2)}(u)\,du.
\tag{2}
\]

Using only (1), its worst possible lower control is
\[
\boxed{
  -M(T_n)|L_{n-1}^{(1)}(T_n)|
  -
  \int_{T_8}^{T_n}M(u)|L_{n-2}^{(2)}(u)|\,du.
}
\tag{3}
\]

Thus a symmetric envelope closes the signed theorem only if it dominates
the absolute load
\[
\boxed{
  \int_{T_8}^{T_n}M(u)|L_{n-2}^{(2)}(u)|\,du
}
\tag{4}
\]
by the remaining polynomial-size budget.

## VK-scale weighted Mertens bounds

A VK relative PNT estimate for \(\psi(e^u)-e^u\) yields a weighted Mertens
discrepancy of subexponential type,
\[
  M(u)\le C\exp(-c u^\theta(\log u)^q)
  \qquad(0<\theta<1),
\tag{5}
\]
up to harmless local and endpoint constants.  The precise logarithmic
power is not important for this audit.

In the Laguerre bulk \(u\asymp n\), Plancherel--Rotach gives absolute mass
with exponential factor \(e^{u/2}\):
\[
  \int_{2n}^{3n}|L_{n-2}^{(2)}(u)|\,du
  \ge
  c_0 n^a e^{3n/2}
\tag{6}
\]
for some fixed power \(a\).  Since \(T_n\asymp n^{5/3}(\log n)^2\), the
bulk interval \([2n,3n]\) lies inside \([T_8,T_n]\) for all sufficiently
large \(n\).

Combining (5) and (6) gives
\[
\boxed{
  \int_{T_8}^{T_n}M(u)|L_{n-2}^{(2)}(u)|\,du
  \ge
  \exp\!\left(c_1 n-O(n^\theta(\log n)^q)\right),
}
\tag{7}
\]
along the same bulk scale, whenever \(M\) has only VK-subexponential
decay.

This is exponential in \(n\), while the available base-archimedean budget
is polynomial.

## Consequence

The partial-summation form of `231` is useful, but it cannot be closed by
a two-sided weighted Mertens estimate.  The proof must use the sign of
\[
  E_8^\sharp(u)
\]
relative to the oscillations of
\[
  L_{n-2}^{(2)}(u),
\]
or avoid this route via one-sided tail, strong margin, comparative
Loewner--Schur, or the global theorem.

## Status

Closed as a no-go for symmetric weighted-Mertens envelopes.

A1 remains open.  The partial-summation frontier requires signed
correlation, not a VK-size discrepancy bound.

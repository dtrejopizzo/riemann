# Bounded-density bad-set zero-coefficient gate

## Purpose

`292_POISSON_WEIGHTED_BAD_SET_ANTI_CONCENTRATION_GATE.md` reduces the
Abel-transfer route to a logarithmic bound
\[
  \int_{B_{n,\tau}}P_n\,d\nu_g
  \le b_\tau\log n+B_B.
\]

`293`--`294` show that this is a genuine arithmetic anti-concentration
condition for the actual increment measure.  This note isolates one part
that is harmless: any absolutely continuous component with bounded density
contributes only \(O(1)\), hence has zero logarithmic coefficient.

## Statement

Let \(m\) be normalized Haar measure on \(\partial\mathbb D\), and let
\[
  d\nu_{\rm bd}=h\,dm,\qquad 0\le h\le H<\infty.
\]

For every \(n\ge2\) and every measurable set \(E\subset\partial\mathbb D\),
\[
\boxed{
  \int_E P_{1-1/n}\,d\nu_{\rm bd}\le H.
}
\tag{1}
\]

In particular, for the bad sets
\[
  B_{n,\tau}=\{F_n<\tau P_{1-1/n}\},
\]
one has
\[
\boxed{
  \int_{B_{n,\tau}}P_{1-1/n}\,d\nu_{\rm bd}\le H.
}
\tag{2}
\]

Thus the bounded-density component contributes
\[
\boxed{b_\tau^{\rm bd}=0}
\tag{3}
\]
to the logarithmic coefficient in `292`.

## Proof

Since \(h\le H\),
\[
  \int_E P_{1-1/n}\,d\nu_{\rm bd}
  =
  \int_E P_{1-1/n}h\,dm
  \le
  H\int_E P_{1-1/n}\,dm
  \le
  H\int_{\partial\mathbb D}P_{1-1/n}\,dm.
\]

With the standard Poisson normalization,
\[
  \int_{\partial\mathbb D}P_{1-1/n}\,dm=1.
\]

This proves (1), hence (2)--(3).

## Decomposition consequence

If
\[
  \nu=\nu_{\rm bd}+\nu_{\rm rem}
\]
with \(d\nu_{\rm bd}=h\,dm\), \(0\le h\le H\), then
\[
\boxed{
  \int_{B_{n,\tau}}P_{1-1/n}\,d\nu
  \le
  H+
  \int_{B_{n,\tau}}P_{1-1/n}\,d\nu_{\rm rem}.
}
\tag{4}
\]

Therefore the leading logarithmic coefficient required by `292` is carried
entirely by the remaining non-bounded part:
\[
\boxed{
  b_\tau(\nu)=b_\tau(\nu_{\rm rem})
  \quad\hbox{at the leading logarithmic level.}
}
\tag{5}
\]

This gives a useful diagnostic for any proposed Euler--Gamma increment
measure:

1. the bounded absolutely continuous part is harmless for Abel-defect
   anti-concentration;
2. any logarithmic bad-set obstruction must come from atoms, singular
   continuous mass, or an unbounded density component;
3. local lower density near \(\zeta=1\) is not enough, by `294`; one also
   needs an upper/distributional control on the non-bounded remainder.

## Relation to compact A1

If a non-circular construction of \(\nu_g\) splits it as
\[
  \nu_g=h\,dm+\nu_{\rm rem},
  \qquad 0\le h\le H,
\]
then the Abel-transfer closure of `291`--`292` reduces to proving the
small-coefficient bad-set estimate only for \(\nu_{\rm rem}\).  This does
not close A1 by itself, but it removes the bounded absolutely continuous
component from the obstruction.

## Status

Closed as a bounded-density reduction for the bad-set route.  A1 remains
open until the actual Euler--Gamma increment measure is constructed and
the required bad-set anti-concentration is proved for its non-bounded
remainder, or another Fejer/Herglotz/RDI route closes the compact core.

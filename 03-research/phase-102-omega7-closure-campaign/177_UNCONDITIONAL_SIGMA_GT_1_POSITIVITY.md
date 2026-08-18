# Unconditional sigma greater than one positivity

## Purpose

`176_HORIZONTAL_XI_MODULUS_MONOTONICITY_GATE.md` states the RH-equivalent
target
\[
  \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2).
\]

This note records the portion that is unconditional:
\[
  \Re{\xi'\over\xi}(s)>0\qquad(\Re s>1).
\]

Thus the missing theorem is not positivity everywhere from scratch.  It is
the extension of this positivity through the critical strip down to
\(\Re s>1/2\).

## Hadamard-product proof

The completed function \(\xi\) is entire of order one and has its nontrivial
zeros in the strip
\[
  0<\Re\rho<1.
\]

Using the paired Hadamard logarithmic derivative,
\[
  {\xi'\over\xi}(s)
  =
  \sum_\rho {1\over s-\rho},
\tag{1}
\]
with the standard symmetric limiting prescription.

Let
\[
  s=\sigma+it,\qquad \sigma>1.
\]

For every nontrivial zero \(\rho=\beta+i\gamma\), one has
\[
  \sigma-\beta>0.
\]

Therefore
\[
  \Re {1\over s-\rho}
  =
  {\sigma-\beta\over(\sigma-\beta)^2+(t-\gamma)^2}
  >0.
\tag{2}
\]

The paired locally uniform convergence preserves nonnegative real part, and
since zeros exist, the real part is strictly positive:
\[
  \boxed{
  \Re{\xi'\over\xi}(s)>0\qquad(\sigma>1).
  }
\tag{3}
\]

## Equivalent modulus statement

Since
\[
  \Re{\xi'\over\xi}(s)
  =
  \partial_\sigma\log|\xi(\sigma+it)|,
\]
equation (3) says
\[
  \partial_\sigma\log|\xi(\sigma+it)|>0
  \qquad(\sigma>1).
\tag{4}
\]

Thus for each fixed \(t\), the completed modulus is already known to be
strictly increasing in the Euler-product half-plane.

## The exact remaining strip target

The RH-equivalent part is the missing continuation of (3) into
\[
  {1\over2}<\sigma\le1.
\]

Equivalently, one must prove
\[
  \partial_\sigma\log|\xi(\sigma+it)|\ge0
  \qquad(1/2<\sigma\le1)
\tag{5}
\]
from Euler--Gamma data.

This is precisely where zeros could occur.  A zero \(\rho\) with
\(\Re\rho>1/2\) would create a pole of \(\xi'/\xi\) in the target strip and
force sign changes of the real part in every small neighborhood.

## Relation to Euler product

For \(\sigma>1\),
\[
  {\zeta'\over\zeta}(s)
  =
  -\sum_{m\ge2}{\Lambda(m)\over m^s}.
\]

The full completed inequality is
\[
  \Re{1\over s}
  +
  \Re{1\over s-1}
  -{1\over2}\log\pi
  +
  {1\over2}\Re\psi\!\left({s\over2}\right)
  +
  \Re{\zeta'\over\zeta}(s)>0.
\tag{6}
\]

Although (6) is true for \(\sigma>1\), its proof by the zero-side product
does not provide a sign-preserving continuation of the Euler product across
\(\sigma=1\).  Crossing the line \(\sigma=1\) requires the same pole-prime
pairing and signed continuation that appears in A1.

## Status

Closed as an unconditional region theorem.  A1 remains open.

The live half-plane target is now sharpened to the critical strip:
\[
  \Re{\xi'\over\xi}(s)\ge0\qquad(1/2<\Re s\le1).
\]

# Prime-pole integral generator

## Purpose

The Euler--Gamma Li generator separates the archimedean part from the
prime-pole part.  This document writes the prime-pole generator as the same
signed \(\psi(e^u)-e^u\) integral that appears in the Laguerre formulation.

The goal is to show that the generator coefficient problem and A1 are the
same arithmetic sign problem.

## Prime-pole generator

Let
\[
  s=s(z)={1\over1-z}.
\]

The paired prime-pole generator is
\[
  \mathcal P(z)
  =
  {z\over(1-z)^2}
  \left[
    {1\over s-1}+{\zeta'\over\zeta}(s)
  \right].
\tag{1}
\]

For \(\Re s>1\),
\[
  -{\zeta'\over\zeta}(s)
  =
  \int_{1^-}^{\infty}y^{-s}\,d\psi(y),
\]
and
\[
  {1\over s-1}
  =
  \int_1^\infty y^{-s}\,dy.
\]

Therefore
\[
  {1\over s-1}+{\zeta'\over\zeta}(s)
  =
  \int_1^\infty y^{-s}\,dy
  -
  \int_{1^-}^{\infty}y^{-s}\,d\psi(y).
\tag{2}
\]

This is the Stieltjes form of the paired pole-prime cancellation.

## Integration by parts

Let
\[
  E(y)=\psi(y)-y.
\]

The right side of (2) is
\[
  -\int_{1^-}^{\infty}y^{-s}\,dE(y).
\]

For \(\Re s>1\), Stieltjes integration by parts gives
\[
  -\int_{1^-}^{\infty}y^{-s}\,dE(y)
  =
  -[E(y)y^{-s}]_{1^-}^{\infty}
  -
  s\int_1^\infty E(y)y^{-s-1}\,dy.
\tag{3}
\]

Since
\[
  E(1^-)=\psi(1^-)-1=-1
\]
and the boundary at infinity vanishes in the half-plane,
\[
  -[E(y)y^{-s}]_{1^-}^{\infty}=-1.
\]

Thus
\[
  {1\over s-1}+{\zeta'\over\zeta}(s)
  =
  -1
  -
  s\int_1^\infty E(y)y^{-s-1}\,dy.
\tag{4}
\]

Multiplying by \(z/(1-z)^2\) gives the exact integral generator
\[
  \boxed{
  \mathcal P(z)
  =
  -{z\over(1-z)^2}
  -
  {z\,s(z)\over(1-z)^2}
  \int_1^\infty
  E(y)y^{-s(z)-1}\,dy.
  }
\tag{5}
\]

Since \(s(z)=1/(1-z)\),
\[
  {z\,s(z)\over(1-z)^2}
  =
  {z\over(1-z)^3}.
\]

Hence
\[
  \mathcal P(z)
  =
  -{z\over(1-z)^2}
  -
  {z\over(1-z)^3}
  \int_1^\infty
  E(y)y^{-1/(1-z)-1}\,dy.
\tag{6}
\]

## Additive variable

Put \(y=e^u\).  Then
\[
  y^{-1/(1-z)-1}\,dy
  =
  e^{-u/(1-z)}\,du.
\]

Therefore
\[
  \boxed{
  \mathcal P(z)
  =
  -{z\over(1-z)^2}
  -
  {z\over(1-z)^3}
  \int_0^\infty
  (\psi(e^u)-e^u)
  \exp\!\left(-{u\over1-z}\right)\,du.
  }
\tag{7}
\]

This is the infinite-cutoff version of the fixed-cutoff compact generator
already recorded in the phase.

## Coefficient extraction and Laguerre kernel

The Laguerre generating identity gives
\[
  \sum_{n\ge1}
  \left[
    {d\over du}L_{n-1}^{(1)}(u)-L_{n-1}^{(1)}(u)
  \right]z^n
  =
  -{z\over(1-z)^3}
  \exp\!\left(-{uz\over1-z}\right).
\tag{8}
\]

Since
\[
  \exp\!\left(-{u\over1-z}\right)
  =
  e^{-u}
  \exp\!\left(-{uz\over1-z}\right),
\]
the integral term in (7) has coefficients
\[
  \int_0^\infty
  (\psi(e^u)-e^u)e^{-u}
  \left[
    {d\over du}L_{n-1}^{(1)}(u)-L_{n-1}^{(1)}(u)
  \right]du.
\tag{9}
\]

Returning to \(y=e^u\), this is exactly
\[
  \int_1^\infty
  (\psi(y)-y)f'_{n,0}(y)\,dy.
\tag{10}
\]

The first term of (7),
\[
  -{z\over(1-z)^2}
  =
  -\sum_{n\ge1}n z^n,
\]
contributes \(-n\).  Therefore
\[
  [z^n]\mathcal P(z)
  =
  -n+\int_1^\infty(\psi(y)-y)f'_{n,0}(y)\,dy
\tag{11}
\]
in the same paired boundary sense as the phase.

This recovers the phase-102 identity
\[
  \lambda_n^{\rm prime}
  =
  -n+\int_1^\infty(\psi(y)-y)f'_{n,0}(y)\,dy.
\]

## Relation to A0 and A1

Splitting the integral in (10) at \(e^{T_n}\) gives:

- A0: the tail from \(e^{T_n}\) to infinity is small in absolute value;
- A1: the compact core plus \({3\over4}\lambda_n^{\rm arch}\) is
  nonnegative.

Thus the coefficient positivity of the Euler--Gamma generator is not a
separate route from A1.  It is the generating-function form of exactly the
same compact signed problem.

## Status

Closed as a normal form.  The prime-pole generator, the Laguerre integral,
and A1 are now explicitly identified.  The missing theorem remains the
signed compact inequality.

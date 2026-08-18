# Disk Herglotz measure half-plane gate

## Purpose

`174_LOG_DERIVATIVE_HALF_PLANE_POSITIVITY_GATE.md` identifies the global
closure route
\[
  \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2).
\]

This note writes the same theorem as a disk Herglotz measure statement.
The advantage is that it states exactly what positive object must be
constructed from Euler--Gamma data, without defining the measure from the
zero divisor after the fact.

## Disk coordinate and Carathéodory function

Use
\[
  s={1\over1-z},
  \qquad
  z=1-{1\over s}.
\]

Then
\[
  |z|<1
  \quad\Longleftrightarrow\quad
  \Re s>{1\over2}.
\]

Define
\[
\boxed{
  H_\xi(z)
  =
  2{\xi'\over\xi}\!\left({1\over1-z}\right).
}
\tag{1}
\]

By `174` and `175`, the half-plane theorem is exactly
\[
\boxed{
  \Re H_\xi(z)\ge0
  \qquad(|z|<1),
}
\tag{2}
\]
with \(H_\xi\) holomorphic in the disk.

## Herglotz representation

If (2) holds, the Herglotz theorem gives a positive finite measure
\(\nu_\xi\) on \(\partial\mathbb D\) such that
\[
\boxed{
  H_\xi(z)
  =
  i\beta
  +
  \int_{\partial\mathbb D}
    {\zeta+z\over \zeta-z}\,d\nu_\xi(\zeta),
  \qquad |z|<1,
}
\tag{3}
\]
with \(\beta\in\mathbb R\).

In the present normalization \(H_\xi(0)=2\lambda_1\) is real, so
\[
  \beta=\Im H_\xi(0)=0,
\]
and
\[
\boxed{
  \nu_\xi(\partial\mathbb D)=2\lambda_1.
}
\tag{4}
\]

Conversely, any representation (3) with a positive finite measure implies
\(\Re H_\xi(z)\ge0\) in the disk.  Thus the global half-plane theorem is
equivalent to constructing the positive measure \(\nu_\xi\) and proving
that its Herglotz transform is the completed Euler--Gamma function (1).

## Moment form

Expanding (3) at \(z=0\),
\[
  {\zeta+z\over\zeta-z}
  =
  1+2\sum_{m\ge1}\overline{\zeta}^{\,m}z^m.
\]

Therefore
\[
\boxed{
  H_\xi(z)
  =
  2\lambda_1
  +
  2\sum_{m\ge1}
    \left(
      \int_{\partial\mathbb D}\overline{\zeta}^{\,m}\,d\nu_\xi(\zeta)
    \right)z^m.
}
\tag{5}
\]

Comparing with `172`--`175`, the moments are exactly the second-difference
Toeplitz coefficients
\[
\boxed{
  g_m
  =
  \int_{\partial\mathbb D}\overline{\zeta}^{\,m}\,d\nu_\xi(\zeta),
  \qquad
  g_0=2\lambda_1,\quad
  g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}.
}
\tag{6}
\]

Thus the disk Herglotz measure theorem is equivalent to positivity of every
Toeplitz block \([g_{j-k}]\).

## Why the measure must be constructed first

Let a zero \(\rho\) of \(\xi\) be mapped to
\[
  w_\rho=1-{1\over\rho}.
\]

If \(\Re\rho>1/2\), then \(|w_\rho|<1\).  At such a point,
\[
  H_\xi(z)=2{\xi'\over\xi}\!\left({1\over1-z}\right)
\]
has a non-removable pole.  But a Herglotz transform of a positive finite
measure is holomorphic in \(|z|<1\).  Hence (3) rules out every
\(\Re\rho>1/2\) zero.  The functional equation then rules out
\(\Re\rho<1/2\) zeros as well.

Therefore the positive measure construction implies RH and closes Omega7
through Li.

The construction is circular if one first assumes the zeros lie on the
critical line and then defines \(\nu_\xi\) as their boundary divisor.  A
valid proof must build \(\nu_\xi\) from completed Euler--Gamma data or from
an independent Toeplitz/Herglotz positivity theorem before using zero
support.

## Relation to compact A1

The disk Herglotz theorem closes Omega7 externally:
\[
  \nu_\xi\ge0
  \quad\Longrightarrow\quad
  \Re H_\xi\ge0
  \quad\Longrightarrow\quad
  \mathrm{RH}
  \quad\Longrightarrow\quad
  \lambda_n\ge0.
\]

It does not by itself prove the compact A1 inequality
\[
  C_n(T_n)\ge0
\]
unless accompanied by the already isolated margin-tail bridge
\[
  s_n\ge d_n.
\]

Thus there are two valid closure modes:

1. construct \(\nu_\xi\) non-circularly and close Omega7 through RH/Li;
2. prove the compact margin-tail inequality directly and close A1.

## Status

Closed as the disk Herglotz measure form of the global half-plane gate.

A1 remains open.  Omega7 remains open until this positive measure is
constructed non-circularly, or until the compact A1 gate is proved directly.

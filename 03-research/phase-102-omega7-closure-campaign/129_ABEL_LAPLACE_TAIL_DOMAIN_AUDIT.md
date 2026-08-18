# Abel-Laplace tail domain audit

## Purpose

The tail generator in the \(z\)-disk has the natural factor
\[
  {z\over1-z}.
\]
This document changes variables to
\[
  w={z\over1-z},\qquad z={w\over1+w},
\]
and shows that the A0 tail is a signed Laplace transform in the right
half-plane.  This identifies exactly what A0 gives and what it does not give.

## Tail generator in \(w\)-coordinates

For fixed \(T\), the formal tail generator is
\[
  \mathcal R_T(z)
  =
  -{z\over(1-z)^3}
  \int_T^\infty
  (\psi(e^u)-e^u)e^{-u}
  \exp\!\left(-{uz\over1-z}\right)\,du.
\tag{1}
\]

Set
\[
  w={z\over1-z}.
\]
Since
\[
  1-z={1\over1+w},
  \qquad
  {z\over(1-z)^3}=w(1+w)^2,
\]
equation (1) becomes
\[
  \boxed{
  \mathcal R_T\!\left({w\over1+w}\right)
  =
  -w(1+w)^2
  \int_T^\infty
  (\psi(e^u)-e^u)e^{-u}e^{-uw}\,du.
  }
\tag{2}
\]

Thus the analytic core is the signed Laplace transform
\[
  \mathcal E_T(w)
  =
  \int_T^\infty
  (\psi(e^u)-e^u)e^{-u}e^{-uw}\,du.
\tag{3}
\]

## Domain supplied by A0/PNT

The unconditional PNT envelope in A0 gives
\[
  |(\psi(e^u)-e^u)e^{-u}|
  \le
  A\exp(-\eta(u)),
\]
where \(\eta(u)/\log(1+u)\to\infty\).

Therefore (3) converges absolutely on the closed right half-plane
\[
  \Re w\ge0
\]
after \(T\) is chosen beyond the PNT threshold.  It also converges in any
larger strip
\[
  \Re w>-\sigma
\]
only if the available error term dominates \(e^{\sigma u}\).  The A0
hypothesis does not provide such exponential domination.

In \(z\)-coordinates, the right half-plane \(\Re w\ge0\) is
\[
  \Re {z\over1-z}\ge0.
\]
Writing \(z=x+iy\), this is
\[
  x(1-x)\ge y^2,
\]
the closed disk with diameter \([0,1]\).  This is a proper subdomain of the
unit disk.

## Why this is not a Herglotz proof

A right-half-plane Laplace transform of a positive measure has strong
positivity properties.  Here the measure density is
\[
  d\nu_T(u)
  =
  (\psi(e^u)-e^u)e^{-u}\mathbf 1_{u\ge T}\,du.
\]

This is a signed density.  The prime number theorem controls its size, not
its sign.  Therefore A0 supplies convergence of \(\mathcal E_T(w)\), but not
Herglotz, Pick, Stieltjes or completely monotone positivity.

Indeed, complete monotonicity on the positive real axis would require
\[
  (-1)^k{d^k\over dw^k}\mathcal E_T(w)
  =
  \int_T^\infty u^k(\psi(e^u)-e^u)e^{-u}e^{-uw}\,du
  \ge0
\]
for every \(k\) and \(w>0\), after a fixed sign convention.  This is a
sequence of signed moment inequalities for \(\psi(e^u)-e^u\).  It is not a
consequence of the PNT envelope.

## Coefficient implication

The \(z\)-coefficients of \(\mathcal R_T(z)\) are obtained by expanding
\[
  \mathcal R_T\!\left({w\over1+w}\right)
\]
at \(w=0\) and then re-expanding \(w=z/(1-z)\).  Positivity of those
coefficients is therefore not implied by analyticity of the Laplace transform
on \(\Re w\ge0\).

To use (2) for A1 one needs a new theorem of one of the following kinds:

1. positivity or one-sided control of the signed Laplace transform
   \(\mathcal E_T(w)\);
2. a boundary Herglotz representation after combining the tail with the
   compact core and archimedean part;
3. a signed moment theorem for the density
   \((\psi(e^u)-e^u)e^{-u}\);
4. a direct coefficient theorem for
   \(\mathcal L(z)-{1\over4}\mathcal A(z)-\mathcal R_T(z)\).

Each option is A1-strength.  None follows from A0 alone.

## Eliminated class

The following proof pattern is eliminated:

1. transform the tail to the \(w\)-half-plane;
2. use absolute convergence of its Laplace transform from PNT;
3. infer Herglotz, Stieltjes, complete monotonicity, or positive
   coefficients.

The second step gives analytic existence only.  The third step requires a
positive measure or a signed compensation theorem, which is precisely the
missing A1 input.

## Status

The Abel-Laplace domain is closed.  It sharpens the tail obstruction:
A0 gives a signed Laplace transform on the right half-plane, not a positive
Laplace transform.  The missing theorem is positivity-preserving
continuation or signed moment control.

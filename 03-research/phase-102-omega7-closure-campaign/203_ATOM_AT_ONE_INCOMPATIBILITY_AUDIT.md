# Atom at one incompatibility audit

## Purpose

`202_FEJER_DENSITY_SCALE_GATE.md` records that an atom of the increment
measure \(\nu_g\) at \(\zeta=1\) would be more than enough to prove the
strong margin.  This note checks whether that atom is compatible with the
Euler--Gamma Li generator.

The conclusion is:

\[
  \boxed{
  \hbox{an atom of }\nu_g\hbox{ at }1\hbox{ would force quadratic growth of
  }\lambda_n\hbox{ and a cubic pole in }\mathcal L(z).
  }
\]

That is incompatible with the actual large-\(s\) generator scale
\[
  \mathcal L(z)
  =
  {z\over(1-z)^2}{\xi'\over\xi}\!\left({1\over1-z}\right)
  =
  O\!\left({\log(1/(1-z))\over(1-z)^2}\right)
  \qquad(z\to1^-),
\]
provided the standard large-real-\(s\) estimate
\[
  {\xi'\over\xi}(s)=O(\log s)
\]
is used.

Thus the atom mechanism is a useful sufficient model, but it is not
compatible with the completed Euler--Gamma normalization of the Li
generator.  A Fejer route must instead seek a logarithmic or other
non-atomic concentration near \(1\), or return to a signed compact proof.

## Atom contribution to the second-difference moments

Let the positive increment measure have an atom
\[
  \nu_g\{1\}=a_0>0.
\]

Then its moments contain the constant contribution
\[
  g_m^{\rm atom}=a_0
  \qquad(m\ge0).
\tag{1}
\]

Using the exact second-difference recovery formula from `198`,
\[
  2\lambda_n
  =
  n g_0+2\sum_{m=1}^{n-1}(n-m)g_m,
\tag{2}
\]
the atom contributes
\[
\begin{aligned}
  2\lambda_n^{\rm atom}
  &=
  n a_0+2a_0\sum_{m=1}^{n-1}(n-m)\\
  &=
  n a_0+2a_0{n(n-1)\over2}\\
  &=
  a_0n^2.
\end{aligned}
\tag{3}
\]

Hence
\[
\boxed{
  \lambda_n^{\rm atom}={a_0\over2}n^2.
}
\tag{4}
\]

This is why an atom at \(1\) would dominate the archimedean margin
\(O(n\log n)\).  It is also why the atom is too strong for the actual Li
generator scale.

## Atom contribution to the generating function

Let
\[
  \mathcal G_+(z)=g_0+\sum_{m\ge1}g_mz^m.
\]

The atom contributes
\[
  \mathcal G_+^{\rm atom}(z)
  =
  a_0\sum_{m\ge0}z^m
  =
  {a_0\over1-z}.
\tag{5}
\]

From `172`,
\[
  \mathcal G_+(z)
  =
  \lambda_1+{(1-z)^2\over z}\mathcal L(z),
\tag{6}
\]
so the atom would force
\[
  \mathcal L^{\rm atom}(z)
  =
  {z\over(1-z)^2}\mathcal G_+^{\rm atom}(z)
  =
  {a_0z\over(1-z)^3},
\tag{7}
\]
up to terms less singular at \(z=1\).

Equivalently, the coefficient growth is quadratic, as in (4).

## Euler--Gamma generator scale

The exact generator from `140` is
\[
  \mathcal L(z)
  =
  {z\over(1-z)^2}
  {\xi'\over\xi}\!\left({1\over1-z}\right).
\tag{8}
\]

For \(s\to+\infty\),
\[
  {\xi'\over\xi}(s)
  =
  {1\over s}
  +{1\over s-1}
  -{1\over2}\log\pi
  +{1\over2}\psi(s/2)
  +{\zeta'\over\zeta}(s).
\tag{9}
\]

Here
\[
  \psi(s/2)=\log(s/2)+O(1/s),
\]
and
\[
  {\zeta'\over\zeta}(s)=O(2^{-s})
\]
on the positive real axis.  Therefore
\[
  {\xi'\over\xi}(s)=O(\log s)
  \qquad(s\to+\infty,\ s\in\mathbb R).
\tag{10}
\]

With \(s=1/(1-z)\), (8) gives
\[
\boxed{
  \mathcal L(z)
  =
  O\!\left(
    {\log(1/(1-z))\over(1-z)^2}
  \right)
  \qquad(z\to1^-).
}
\tag{11}
\]

This growth is incompatible with a positive cubic pole
\[
  {a_0z\over(1-z)^3},
  \qquad a_0>0.
\tag{12}
\]

Thus a nonzero atom at \(1\) cannot be present in any positive increment
measure representing the actual completed Euler--Gamma second-difference
sequence.

## Consequence for the Fejer route

The Fejer strong-margin route cannot rely on an atom at \(1\).  The viable
near-\(1\) mechanisms are therefore more delicate:

1. a logarithmic absolutely continuous density, as isolated in `202`;
2. a singular continuous concentration whose Fejer averages grow like
   \(\log n\) but do not create a cubic pole;
3. a direct proof of the exact Fejer lower bound
   \[
     n\int F_n\,d\nu_g\ge\lambda_n^{\rm arch}
   \]
   from Euler--Gamma data;
4. abandonment of the Fejer-margin route in favor of the compact signed
   core.

## Status

Closed as an atom audit for the Fejer strong-margin route.

A1 remains open.  The atom-at-\(1\) shortcut is eliminated for the actual
Euler--Gamma Li generator; the remaining Fejer route requires logarithmic
or singular-continuous concentration compatible with the
\((1-z)^{-2}\log(1/(1-z))\) generator scale.

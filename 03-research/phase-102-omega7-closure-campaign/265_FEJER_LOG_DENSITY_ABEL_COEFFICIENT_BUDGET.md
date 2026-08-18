# Fejer log-density Abel coefficient budget

## Purpose

`264_FEJER_ROUTE_EXPLICIT_THRESHOLD_LEDGER.md` reduces the Fejer
strong-margin route to a positive increment measure with local logarithmic
density coefficient
\[
  a>{1\over2}.
\]

This note records the opposite constraint coming from the actual
Euler--Gamma increment generator.  If the positive increment measure has a
local lower density \(aL\) near \(\zeta=1\), then the Abel growth of the
generator forces
\[
\boxed{a\le1.}
\]

Thus the Fejer/log-density route is not inconsistent, but its possible
coefficient window is sharp:
\[
\boxed{{1\over2}<a\le1.}
\]

## Abel kernel and logarithmic model

Let
\[
  L(\theta)=-\log|2\sin(\theta/2)|.
\]
For \(0<r<1\),
\[
  \mathrm{Re}{1\over1-re^{i\theta}}
  =
  1+\sum_{m\ge1}r^m\cos(m\theta).
\tag{1}
\]

The boundary Fourier expansion
\[
  L(\theta)=\sum_{k\ge1}{\cos(k\theta)\over k}
\tag{2}
\]
gives, with normalized measure \(dm=d\theta/(2\pi)\),
\[
\begin{aligned}
  \int_{\partial\mathbb D}
  \mathrm{Re}{1\over1-r\zeta}\,
  L(\zeta)\,dm(\zeta)
  &=
  \sum_{m\ge1}r^m
  \int\cos(m\theta)L(\theta)\,dm        \\
  &=
  {1\over2}\sum_{m\ge1}{r^m\over m}      \\
  &=
  {1\over2}\log {1\over1-r}.
\end{aligned}
\tag{3}
\]

So a density \(aL\) contributes Abel real growth
\[
  {a\over2}\log {1\over1-r}.
\tag{4}
\]

## Local lower density implies an Abel lower coefficient

Assume a positive increment measure has a decomposition
\[
  d\nu_g(e^{i\theta})=h(\theta)\,dm(\theta)+d\nu_{\rm rem}(e^{i\theta}),
  \qquad h\ge0,\qquad \nu_{\rm rem}\ge0,
\tag{5}
\]
and that on \(|\theta|\le\theta_0\),
\[
  h(\theta)\ge aL(\theta)-B_h.
\tag{6}
\]

As in `263`, this gives a global lower bound
\[
  h(\theta)\ge aL(\theta)-B_h^\ast
\tag{7}
\]
with an explicit finite \(B_h^\ast\).  Since
\[
  \mathrm{Re}{1\over1-r\zeta}
\]
is not everywhere nonnegative, it is cleaner to use the Carathéodory
Poisson kernel
\[
  P_r(\theta)
  =
  \mathrm{Re}{1+re^{i\theta}\over1-re^{i\theta}}
  =
  1+2\sum_{m\ge1}r^m\cos(m\theta)\ge0.
\tag{8}
\]

The associated Carathéodory transform is
\[
  H_g(r)=g_0+2\sum_{m\ge1}g_mr^m
  =
  \int_{\partial\mathbb D}{\zeta+r\over \zeta-r}\,d\nu_g(\zeta),
\tag{9}
\]
so
\[
  \mathrm{Re}\,H_g(r)=\int P_r\,d\nu_g.
\tag{10}
\]

Using (2),
\[
\begin{aligned}
  \int P_rL\,dm
  &=
  2\sum_{m\ge1}r^m
  \int \cos(m\theta)L(\theta)\,dm       \\
  &=
  \sum_{m\ge1}{r^m\over m}
  =
  \log {1\over1-r}.
\end{aligned}
\tag{11}
\]

Also \(\int P_r\,dm=1\).  Therefore (7), \(h\ge0\), and
\(\nu_{\rm rem}\ge0\) imply
\[
\boxed{
  \mathrm{Re}\,H_g(r)
  \ge
  a\log {1\over1-r}-B_h^\ast
  \qquad(0<r<1).
}
\tag{12}
\]

Equivalently, since \(H_g=2\mathcal G_+-g_0\), the one-sided increment
generator satisfies
\[
  \mathrm{Re}\,\mathcal G_+(r)
  \ge
  {a\over2}\log {1\over1-r}+O(1).
\tag{13}
\]

## Actual Euler--Gamma Abel coefficient

By `172` and `174`,
\[
  \mathcal G_+(r)
  =
  \lambda_1+
  {\xi'\over\xi}\!\left({1\over1-r}\right).
\tag{14}
\]

For \(s\to+\infty\),
\[
  {\xi'\over\xi}(s)
  =
  {1\over2}\log s+O(1),
\tag{15}
\]
more precisely from the gamma factor,
\[
  {\xi'\over\xi}(s)
  =
  {1\over2}\log {s\over2\pi}+O(1/s)
  \qquad(s\to+\infty,\ s\in\mathbb R).
\tag{16}
\]

With \(s=(1-r)^{-1}\), this gives
\[
\boxed{
  \mathrm{Re}\,\mathcal G_+(r)
  =
  {1\over2}\log {1\over1-r}+O(1).
}
\tag{17}
\]

Combining (13) and (17) yields
\[
  {a\over2}\le {1\over2},
\]
hence
\[
\boxed{a\le1.}
\tag{18}
\]

## Consequence for the live Fejer route

The Fejer route needs a lower logarithmic density coefficient
\[
  a>{1\over2}
\]
by `259`--`264`.  The Abel coefficient budget proves that any such
coefficient must also satisfy
\[
  a\le1.
\]

Therefore the exact coefficient window is
\[
\boxed{
  {1\over2}<a\le1.
}
\tag{19}
\]

This is a useful consistency check:

- an atom at \(1\) is impossible by `203`;
- bounded density is too small by `202`;
- logarithmic density is the only scale compatible with the generator;
- the coefficient must be large enough to beat the archimedean margin but
  cannot exceed the generator's Abel leading coefficient.

The route remains open because no non-circular positive increment measure
with such lower local density has been constructed.

## Status

Closed as an Abel coefficient budget.  It narrows the Fejer/log-density
route to the sharp possible range \(1/2<a\le1\), but it does not prove the
existence of the positive increment measure or the required lower density.

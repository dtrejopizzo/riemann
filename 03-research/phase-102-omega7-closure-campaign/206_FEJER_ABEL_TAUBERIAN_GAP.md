# Fejer-Abel Tauberian gap

## Purpose

`205_FEJER_LOG_CONSTANT_AUDIT.md` shows that the leading constants are
favorable for the Fejer/log-density route.  The remaining danger is a false
Tauberian step:
\[
  \mathrm{Re}\,\mathcal G_+(r)
  \sim {1\over2}\log {1\over1-r}
  \quad\not\Longrightarrow\quad
  \int F_n\,d\nu_g\ge {1\over2}\log n+O(1)
\]
without extra regularity.

This note records the exact gap.  Abel kernels are smooth and strictly
positive.  Fejer kernels are positive but have moving zeros.  Therefore
there is no pointwise lower comparison capable of transferring the Abel
logarithm into the Fejer lower bound.

## Kernels at the matching scale

Put
\[
  r_n=1-{1\over n}
\]
and write
\[
  A_n(\theta)
  =
  \mathrm{Re}{1\over1-r_ne^{i\theta}}
  =
  {1-r_n\cos\theta\over |1-r_ne^{i\theta}|^2}.
\tag{1}
\]
Near \(\theta=0\),
\[
  A_n(\theta)
  \asymp
  {n\over 1+n^2\theta^2}.
\tag{2}
\]

The normalized Fejer kernel is
\[
  F_n(e^{i\theta})
  =
  {1\over n}
  \left({\sin(n\theta/2)\over\sin(\theta/2)}\right)^2.
\tag{3}
\]
It has the exact zeros
\[
  F_n(e^{2\pi i k/n})=0,
  \qquad
  1\le k\le n-1.
\tag{4}
\]

At the first moving zero
\[
  \theta_n={2\pi\over n},
\tag{5}
\]
one has
\[
  F_n(e^{i\theta_n})=0,
\tag{6}
\]
but
\[
  A_n(\theta_n)
  \asymp n.
\tag{7}
\]
Indeed, (2) gives \(A_n(2\pi/n)\asymp n/(1+4\pi^2)\).

Thus no absolute constant \(c>0\) can satisfy
\[
  F_n(e^{i\theta})\ge c\,A_n(\theta)
\tag{8}
\]
on the \(1/n\)-scale.

## Quantitative hiding near a moving zero

Let
\[
  J_n=\left\{\theta:\left|\theta-{2\pi\over n}\right|\le {c\over n^2}\right\}
\tag{9}
\]
with fixed small \(c>0\).  On \(J_n\),
\[
  A_n(\theta)\asymp n,
\tag{10}
\]
while Taylor expansion at the zero gives
\[
  F_n(e^{i\theta})\ll {1\over n}.
\tag{11}
\]
Consequently, for a positive measure mass \(m_n=\nu(J_n)\),
\[
  \int_{J_n}A_n(\theta)\,d\nu
  \asymp n\,m_n,
\tag{12}
\]
but the strong-margin integrand satisfies
\[
  n\int_{J_n}F_n\,d\nu
  \ll m_n.
\tag{13}
\]

So a component of the measure can be highly visible to the Abel kernel at
the matching scale while being almost invisible to the \(n\)-th Fejer test.
This is a structural obstruction, not a defect of constants.

## Consequence for the log-density route

The Abel asymptotic of the Euler--Gamma generator gives only a smoothed
radial statement:
\[
  \int A_n\,d\nu_g
  =
  {1\over2}\log n+O(1)
\tag{14}
\]
if a positive increment measure \(\nu_g\) has already been constructed.

The strong margin requires the different statement
\[
  n\int F_n\,d\nu_g
  \ge
  \lambda_n^{\rm arch}
  =
  {1\over2}n\log n+O(n).
\tag{15}
\]

Because of (6)--(13), (14) does not imply (15) without a theorem excluding
concentration near the moving Fejer zeros.  A valid transfer theorem must
provide at least one of the following:

1. an absolutely continuous lower density near \(0\), such as
   \(h(\theta)\ge a\log(e/|\theta|)-O(1)\) with \(a>1/2\);
2. a direct lower bound for \(\int F_n\,d\nu_g\);
3. a Tauberian anti-concentration theorem controlling the mass of
   neighborhoods of \(2\pi k/n\) at the \(1/n^2\) scale;
4. a stronger structural theorem that makes the Fejer tests positive with
   the required margin.

## Status

Closed as a Tauberian-gap audit.

The Abel logarithm and the favorable constants from `205` are not enough.
A1 remains open until the phase proves a positive increment measure together
with a Fejer lower theorem, a log-density lower theorem, or an
anti-concentration theorem strong enough to bridge Abel and Fejer.

# Fejer log-constant audit

## Purpose

`204_LOG_DENSITY_INCREMENT_GENERATOR_GATE.md` identifies the correct
boundary scale for the increment generator,
\[
  \mathcal G_+(z)
  =
  \lambda_1+
  {\xi'\over\xi}\!\left({1\over1-z}\right).
\]

This note audits the constants.  The point is to separate three different
statements:

1. the crude local-mass sufficient theorem from `200`;
2. the exact Fejer lower bound needed for the strong margin;
3. the Abel/Cauchy logarithmic coefficient visible in \(\mathcal G_+\).

The crude local theorem loses constants.  It is useful as a sufficient
criterion, but it is not the right constant test for the Fejer route.

## Archimedean leading coefficient

The phase split uses
\[
  \lambda_n^{\rm arch}
  =
  1-{n\over2}(\gamma+\log(4\pi))
  +
  \sum_{\substack{r\ge1\\ r\ {\rm odd}}}
  \left[
    \left(1-{1\over r}\right)^n-1+{n\over r}
  \right].
\tag{1}
\]

The logarithmic coefficient comes only from the odd harmonic range
\(1\le r\le n\).  Standard summation by parts, or the same integral
comparison used in `135` and `151` with matching upper and lower bounds,
gives
\[
  \sum_{\substack{r\ge1\\r\ {\rm odd}}}
  \left[
    \left(1-{1\over r}\right)^n-1+{n\over r}
  \right]
  =
  {1\over2}n\log n+O(n).
\tag{2}
\]
All remaining terms in (1) are \(O(n)\).  Therefore
\[
\boxed{
  \lambda_n^{\rm arch}
  =
  {1\over2}n\log n+O(n).
}
\tag{3}
\]

Thus the exact Fejer strong-margin target
\[
  n\int F_n\,d\nu_g\ge\lambda_n^{\rm arch}
\tag{4}
\]
requires, at leading order,
\[
  \int F_n\,d\nu_g
  \ge
  {1\over2}\log n+O(1).
\tag{5}
\]

## Cauchy logarithmic coefficient

Assume model absolute continuity near \(1\):
\[
  d\nu_g(e^{i\theta})
  =
  h(\theta)\,{d\theta\over2\pi},
  \qquad
  h(\theta)=a\log {e\over|\theta|}+O(1)
  \quad(\theta\to0).
\tag{6}
\]

If
\[
  G_\nu(r)
  =
  \int_{\partial\mathbb D}{1\over1-r\zeta}\,d\nu_g(\zeta),
\tag{7}
\]
then the singular real kernel is
\[
  \operatorname{Re}{1\over1-re^{i\theta}}
  =
  {1-r\cos\theta\over |1-re^{i\theta}|^2}.
\tag{8}
\]

Put \(\delta=1-r\).  Near \(\theta=0\),
\[
  {1-r\cos\theta\over |1-re^{i\theta}|^2}
  =
  {\delta\over \delta^2+\theta^2}+O(1).
\tag{9}
\]
The \(O(1)\) part contributes only \(O(1)\) after integration against
\(\log(e/|\theta|)\) on a fixed small arc.  Hence
\[
\begin{aligned}
  \operatorname{Re}G_\nu(r)
  &=
  {a\over2\pi}
  \int_{-\theta_0}^{\theta_0}
  {\delta\over\delta^2+\theta^2}
  \log {e\over|\theta|}
  \,d\theta
  +O(1)\\
  &=
  {a\over2}\log {1\over1-r}+O(1).
\end{aligned}
\tag{10}
\]

For the Euler--Gamma increment generator,
\[
  \mathcal G_+(r)
  =
  \lambda_1+
  {\xi'\over\xi}\!\left({1\over1-r}\right).
\tag{11}
\]
The completed xi logarithmic derivative satisfies, on the positive real
axis,
\[
  {\xi'\over\xi}(s)
  =
  {1\over2}\log s+O(1)
  \qquad(s\to+\infty).
\tag{12}
\]
Therefore
\[
\boxed{
  \operatorname{Re}\mathcal G_+(r)
  =
  {1\over2}\log {1\over1-r}+O(1).
}
\tag{13}
\]

Comparing (10) and (13), the absolutely continuous model compatible with
the Euler--Gamma boundary coefficient would have
\[
\boxed{
  a=1.
}
\tag{14}
\]

This is only a compatibility computation.  It does not construct a positive
measure, and it does not prove that the boundary component is absolutely
continuous with this lower density.

## Exact Fejer coefficient for a logarithmic density

The normalized Fejer kernel is
\[
  F_n(e^{i\theta})
  =
  {1\over n}
  \left({\sin(n\theta/2)\over\sin(\theta/2)}\right)^2,
  \qquad
  \int F_n\,dm=1.
\tag{15}
\]

For the same model density (6), the Fejer mean satisfies
\[
\boxed{
  \int F_n(e^{i\theta})h(\theta)\,dm(\theta)
  =
  a\log n+O(1).
}
\tag{16}
\]

One way to see the constant is to use the Fourier series
\[
  -\log|2\sin(\theta/2)|
  =
  \sum_{k\ge1}{\cos(k\theta)\over k}
\tag{17}
\]
in the local singular part.  Since
\[
  \widehat{F_n}(k)=
  \left(1-{|k|\over n}\right)_+,
\tag{18}
\]
the singular contribution is
\[
  \sum_{k=1}^{n-1}
  \left(1-{k\over n}\right){1\over k}
  =
  \log n+O(1).
\tag{19}
\]
The difference between \(\log(e/|\theta|)\) and
\(-\log|2\sin(\theta/2)|\) on a fixed arc, and the contribution away from
the arc, are bounded in Fejer mean.

Combining (16) with (4), a logarithmic density coefficient \(a\) gives
\[
  n\int F_n\,d\nu_g
  =
  a\,n\log n+O(n).
\tag{20}
\]
By (3), the exact strong-margin leading coefficient is satisfied whenever
\[
\boxed{
  a>{1\over2},
}
\tag{21}
\]
with finite and \(O(n)\) terms then requiring explicit control.  The model
coefficient \(a=1\) inferred from the Euler--Gamma Abel coefficient would
therefore have enough leading constant for the exact Fejer inequality.

## Why the local-mass constant is misleading

`200` used only the very small arc \(|\theta|\le1/n\) and the crude lower
bound
\[
  F_n(e^{i\theta})\ge {4\over\pi^2}n
  \qquad(|\theta|\le1/n).
\tag{22}
\]
Together with
\[
  \nu_g(|\theta|\le1/n)
  \sim {a\over\pi}{\log n\over n},
\tag{23}
\]
this gives the sufficient leading lower bound
\[
  n\int F_n\,d\nu_g
  \gtrsim
  {4a\over\pi^3}n\log n.
\tag{24}
\]
Comparing with (3) would demand
\[
  a\ge{\pi^3\over8}
\tag{25}
\]
at the leading level.  This is far stronger than the exact Fejer
requirement (21).

The discrepancy is not a contradiction.  It is the cost of discarding most
of the positive Fejer kernel and keeping only a crude uniform lower bound on
one small arc.  Therefore the local-mass theorem remains a valid sufficient
criterion, but it should not be used as the decisive constant test for the
log-density route.

## Remaining theorem after the constant audit

The Fejer/log-density route would close the strong margin if the following
non-circular theorem were proved.

There exists a positive increment measure \(\nu_g\) for the Euler--Gamma
second-difference sequence and a decomposition near \(\zeta=1\) with
\[
  d\nu_g(e^{i\theta})
  =
  h(\theta)\,dm(\theta)+d\nu_{\rm rem},
\tag{26}
\]
where \(d\nu_{\rm rem}\) contributes nonnegatively to the Fejer means and
\[
  h(\theta)\ge a\log {e\over|\theta|}-O(1)
  \qquad(\theta\to0)
\tag{27}
\]
for some \(a>1/2\).  Equivalently, it is enough to prove directly that
\[
\boxed{
  \int F_n\,d\nu_g
  \ge
  {1\over2}\log n+O(1)
  \qquad(n\to\infty),
}
\tag{28}
\]
with the \(O(1)\) term made explicit enough to cover every \(n\ge8\).

The Abel asymptotic
\[
  \operatorname{Re}\mathcal G_+(r)
  =
  {1\over2}\log {1\over1-r}+O(1)
\tag{29}
\]
does not by itself imply (28).  Abel kernels and Fejer kernels are both
positive, but they are not uniformly comparable from below: Fejer has moving
zeros, while the Abel kernel is smooth.  A Tauberian regularity theorem,
local density theorem, or direct Fejer estimate is still required.

## Status

Closed as a constant audit.

The constants do not eliminate the Fejer/log-density route.  They eliminate
only the false objection coming from the crude local-mass constant.  A1
remains open because the necessary positive increment measure and the
lower Fejer/log-density theorem have not been proved.

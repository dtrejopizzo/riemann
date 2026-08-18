# Local density is not bad-set anti-concentration

## Purpose

The Fejer route now has two sufficient distributional inputs:

1. a local logarithmic density lower bound near \(\zeta=1\), as in `263`;
2. a Poisson-weighted bad-set anti-concentration theorem, as in `292`.

This note records that input 1 does not imply input 2.  Local mass near
\(\zeta=1\) can coexist with arbitrary sparse positive spikes at moving
Fejer zeros, and those spikes are seen by the Poisson kernels on the bad
sets of `292`.

Thus the Abel-defect route still needs a genuine global arithmetic
anti-concentration theorem for the actual increment measure.

## Setup

Let \(L(\theta)=\log(e/|\theta|)\) near \(\theta=0\), and let \(\nu_0\) be
any positive finite measure with a local absolutely continuous component
\[
\boxed{
  d\nu_0=h(\theta)\,d\theta+d\nu_{\rm rem},
  \qquad
  h(\theta)\ge aL(\theta)-B
}
\tag{1}
\]
on some fixed neighborhood of \(0\), with \(a>0\).

This is the type of local lower-density information used by the Fejer
closure route.

Now choose a superexponentially increasing sequence \(N_j\) and set
\[
  \zeta_j=e^{2\pi i/N_j},
  \qquad
  \mu_j=M{\log N_j\over N_j},
  \qquad M>0.
\]

Define the positive spike measure
\[
\boxed{
  \sigma_M=\sum_{j\ge1}\mu_j\delta_{\zeta_j}.
}
\tag{2}
\]

Because \(N_j\) grows superexponentially,
\[
  \sum_j{\log N_j\over N_j}<\infty,
\]
so \(\sigma_M\) is finite.  Put
\[
\boxed{\nu_M=\nu_0+\sigma_M.}
\tag{3}
\]

Then \(\nu_M\) still satisfies the same local lower-density bound (1),
since only positive mass has been added.

## Bad-set mass from the spikes

Let
\[
  P_N=P_{1-1/N},\qquad
  B_{N,\tau}=\{F_N<\tau P_N\}.
\]

For every \(0<\tau\) and every \(j\), the point \(\zeta_j\) lies in
\(B_{N_j,\tau}\), because
\[
  F_{N_j}(\zeta_j)=0,
  \qquad
  P_{N_j}(\zeta_j)>0.
\]

As in `281`, there is an absolute constant
\[
  c_0=(1+2\pi)^{-2}
\]
such that
\[
\boxed{
  P_{N_j}(\zeta_j)\ge c_0N_j.
}
\tag{4}
\]

Therefore
\[
\begin{aligned}
  \int_{B_{N_j,\tau}}P_{N_j}\,d\nu_M
  &\ge
  \mu_jP_{N_j}(\zeta_j)                                      \\
  &\ge
  Mc_0\log N_j.
\end{aligned}
\tag{5}
\]

Since \(M>0\) is arbitrary, the logarithmic bad-set coefficient forced by
the spikes can be made arbitrarily large while preserving the local
lower-density bound (1).

## Consequence

The local density theorem of `263` can close the Fejer route directly once
the positive increment measure is constructed and the density coefficient
is in the window of `265`.  But the same local lower bound does not prove
the Abel-defect anti-concentration estimate
\[
\boxed{
  \int_{B_{n,\tau}}P_n\,d\nu
  \le b_\tau\log n+B_B
}
\tag{6}
\]
with the small coefficient required by `292`.

Indeed, the measures \(\nu_M\) satisfy the local lower-density hypothesis
but force
\[
  b_\tau\ge Mc_0
\]
along the subsequence \(n=N_j\).  Taking \(M\) large violates any prescribed
coefficient target.

Thus the implications are separated:
\[
\boxed{
  \hbox{local log-density near }1
  \not\Rightarrow
  \hbox{Poisson-weighted bad-set anti-concentration.}
}
\tag{7}
\]

## Relation to A1

This does not weaken the local-density closure route: that route uses the
local lower bound to give a direct Fejer lower bound.  It only prevents a
shortcut in the Abel-transfer route.  If one works through `291`--`292`,
one must prove the bad-set estimate from additional arithmetic structure
of the actual Euler--Gamma increment measure, not merely from positivity,
finite total mass, radial size, or local lower density near \(\zeta=1\).

## Status

Closed as a no-go separating local log-density from Poisson-weighted
bad-set anti-concentration.  A1 remains open until one proves either the
direct Fejer lower theorem/local-density route, or the independent bad-set
anti-concentration theorem required by `292`.

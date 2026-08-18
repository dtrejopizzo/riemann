# Abel spike versus Fejer zero model no-go

## Purpose

`265` fixes the Abel coefficient budget for the Euler--Gamma increment
generator, `266` isolates the Abel--Fejer defect, and `270` proves that no
positive inverse kernel transfers radial Poisson lower bounds to Fejer
lower bounds.

This note adds an explicit positive-measure model showing the obstruction
at the level of scales.  A finite positive measure can have logarithmic
Poisson/Abel spikes at the radii
\[
  r_N=1-{1\over N}
\]
while the matching Fejer tests remain bounded along the same indices,
because the mass is placed on the moving zero set of \(F_N\).

Thus radial data of the one-sided generator \(\mathcal G_+\), even with the
correct logarithmic size on a cofinal sequence, do not imply the compact
Fejer lower theorem or a local absolutely continuous log-density theorem.

## Kernels

Let
\[
  P_N(e^{i\theta})
  =
  P_{1-1/N}(e^{i\theta})
  =
  {1-(1-1/N)^2\over |1-(1-1/N)e^{i\theta}|^2}
\]
and
\[
  F_N(e^{i\theta})
  =
  {1\over N}
  \left({\sin(N\theta/2)\over\sin(\theta/2)}\right)^2.
\]

At the nontrivial \(N\)-th root
\[
  \zeta_N=e^{2\pi i/N},
\]
one has
\[
  F_N(\zeta_N)=0.
\tag{1}
\]

On the other hand, since
\[
  |1-(1-1/N)e^{2\pi i/N}|
  \le {1\over N}+{2\pi\over N}
  ={1+2\pi\over N}
\]
and
\[
  1-(1-1/N)^2\ge {1\over N},
\]
we have the uniform lower bound
\[
\boxed{
  P_N(\zeta_N)\ge c_0N,\qquad
  c_0=(1+2\pi)^{-2}.
}
\tag{2}
\]

Thus the same point is invisible to \(F_N\) but visible to the Abel kernel
with size \(N\).

## A finite positive spike measure

Choose a rapidly increasing integer sequence \(N_j\), for example
\[
  N_j=\left\lceil \exp(\exp(2^j))\right\rceil,
\]
and put
\[
  \zeta_j=e^{2\pi i/N_j},
  \qquad
  \mu_j={\log N_j\over N_j}.
\]

The measure
\[
\boxed{
  \nu=\sum_{j\ge1}\mu_j\delta_{\zeta_j}
}
\tag{3}
\]
is finite, because \(\sum_j(\log N_j)/N_j<\infty\).

At the matching Abel radius \(r_{N_j}=1-1/N_j\), (2) gives
\[
\boxed{
  \int P_{N_j}\,d\nu
  \ge
  \mu_jP_{N_j}(\zeta_j)
  \ge
  c_0\log N_j.
}
\tag{4}
\]

So the Poisson transform has logarithmic spikes of the same scale as the
Euler--Gamma Carathéodory normalization.

## The matching Fejer tests do not see the spike

The \(j\)-th atom gives no contribution to the \(N_j\)-th Fejer test by
(1):
\[
  \mu_jF_{N_j}(\zeta_j)=0.
\tag{5}
\]

The remaining atoms can be made uniformly harmless.  For \(k<j\), the
standard Fejer envelope gives
\[
  F_{N_j}(e^{2\pi i/N_k})
  \le
  {\pi^2\over N_j(2\pi/N_k)^2}
  =
  {N_k^2\over4N_j}.
\tag{6}
\]
Hence
\[
  \sum_{k<j}\mu_kF_{N_j}(\zeta_k)
  \le
  {1\over4N_j}
  \sum_{k<j}N_k\log N_k.
\tag{7}
\]

For \(k>j\), the trivial bound \(F_{N_j}\le N_j\) gives
\[
  \sum_{k>j}\mu_kF_{N_j}(\zeta_k)
  \le
  N_j\sum_{k>j}{\log N_k\over N_k}.
\tag{8}
\]

With the displayed superexponential choice of \(N_j\), both right-hand
sides are bounded uniformly in \(j\), and in fact tend to \(0\).  Therefore
\[
\boxed{
  \int F_{N_j}\,d\nu=O(1)
  \qquad(j\to\infty),
}
\tag{9}
\]
while (4) gives
\[
  \int P_{N_j}\,d\nu\ge c_0\log N_j.
\tag{10}
\]

This is the concrete Abel-spike/Fejer-zero separation.

## Consequence

The compact Fejer route needs
\[
  \int F_N\,d\nu_g
  \ge {A_N\over N}
  =
  {1\over2}\log N+O(1).
\tag{11}
\]

The model above satisfies a logarithmic radial lower bound along the same
indices \(N_j\), yet its Fejer integrals along those indices are bounded.
Therefore the following inference is false:
\[
  \int P_{1-1/N}\,d\nu\hbox{ has logarithmic Euler-scale growth}
  \quad\Longrightarrow\quad
  \int F_N\,d\nu\ge {1\over2}\log N-O(1).
\tag{12}
\]

It is also false that such radial data force an absolutely continuous
local lower density
\[
  d\nu=h\,dm+d\nu_{\rm rem},\qquad
  h(\theta)\ge aL(\theta)-B
\]
near \(1\): the model measure (3) is purely atomic, positive, finite, and
accumulates at \(1\) along the moving Fejer-zero scales.

## Relation to the Euler--Gamma increment measure

This construction is not claimed to be the zeta increment measure.  It is a
logical no-go:

1. positivity of a representing measure is not enough for compact A1
   (`271`);
2. radial Abel growth of the correct logarithmic scale is not enough
   (`270` and the explicit model above);
3. a proof from the actual Euler--Gamma generator must use additional
   structure that rules out concentration near the moving Fejer zeros.

Equivalently, the surviving Fejer closure inputs remain exactly:
\[
\boxed{
\begin{gathered}
  \hbox{construct }\nu_g\ge0\hbox{ with the Euler--Gamma increment moments,}\\
  \hbox{then prove either a direct Fejer lower bound,}\\
  \hbox{or a local log-density theorem with }1/2<a\le1,\\
  \hbox{or an Abel--Fejer defect/anti-concentration theorem.}
\end{gathered}
}
\tag{13}
\]

Only after one of these distributional inputs is proved does the explicit
threshold ledger `264` and the finite certificate `261` close compact A1.

## Status

Closed as an explicit no-go model for Abel-spike data.  A1 remains open:
the missing theorem is still a non-circular construction of the actual
positive increment measure together with a Fejer lower-density,
direct-Fejer, or anti-concentration theorem.

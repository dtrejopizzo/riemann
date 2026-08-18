# Bad-set Carleson window sufficient condition

## Purpose

`292_POISSON_WEIGHTED_BAD_SET_ANTI_CONCENTRATION_GATE.md` reduces the
Abel-transfer route to
\[
  \int_{B_{n,\tau}}P_{1-1/n}\,d\nu_g
  \le b_\tau\log n+B_B,
  \qquad
  B_{n,\tau}=\{F_n<\tau P_{1-1/n}\}.
\]

`293_FEJER_POISSON_BAD_SET_GEOMETRY_GATE.md` proves that the bad set
contains \(1/n\)-scale windows around nontrivial \(n\)-th roots.  This
note records the complementary sufficient direction: root-window
Carleson upper control implies the required Poisson-weighted bad-set
estimate.

It does not prove that the Euler--Gamma increment measure satisfies that
condition.  It converts the missing anti-concentration theorem into a
concrete local-window estimate with constants.

## A uniform cover of the bad set

Let
\[
  r_n=1-{1\over n},\qquad P_n=P_{r_n},
\]
and write
\[
  R_n(e^{i\theta})={F_n(e^{i\theta})\over P_n(e^{i\theta})}.
\]
Let
\[
  \delta_n(\theta)=
  \mathrm{dist}\,\!\left(\theta,{2\pi\over n}\mathbb Z\right)
  \in[0,\pi/n].
\]

For \(n\ge2\),
\[
\boxed{
  R_n(e^{i\theta})\ge {1\over\pi^2}n^2\delta_n(\theta)^2.
}
\tag{1}
\]

Indeed,
\[
  F_n(e^{i\theta})
  =
  {1\over n}\left|
  {e^{in\theta}-1\over e^{i\theta}-1}
  \right|^2.
\]
Since \(n\delta_n(\theta)\in[0,\pi]\),
\[
  |e^{in\theta}-1|
  \ge {2\over\pi}n\delta_n(\theta).
\]
Also, with \(h=1/n\),
\[
  |e^{i\theta}-r_n|^2
  =
  h^2+(1-h)|e^{i\theta}-1|^2,
\]
so
\[
  {|e^{i\theta}-r_n|^2\over |e^{i\theta}-1|^2}
  \ge 1-h\ge {1\over2}.
\]
Finally,
\[
  1-r_n^2={2\over n}-{1\over n^2}\le {2\over n}.
\]
Combining these estimates gives (1).

Consequently,
\[
\boxed{
  B_{n,\tau}
  \subset
  U_{n,\tau}
  :=
  \bigcup_{k=0}^{n-1}
  \left\{
    e^{i\theta}:
    \left|\theta-{2\pi k\over n}\right|_{\mathbb T}
    <
    {\pi\sqrt{\tau}\over n}
  \right\}.
}
\tag{2}
\]

Thus, at fixed \(\tau\), the possible hiding region for Abel mass is a
moving union of root windows of radius comparable to \(1/n\).

## Poisson weight on root windows

For \(|\theta|\le\pi\),
\[
\boxed{
  P_n(e^{i\theta})
  \le
  C_P {n\over 1+n^2\theta^2}
}
\tag{3}
\]
with an absolute constant \(C_P\); for instance \(C_P=2\pi^2\) is enough.
This follows from
\[
  |e^{i\theta}-r_n|^2
  =
  {1\over n^2}+\left(1-{1\over n}\right)|e^{i\theta}-1|^2,
\]
\[
  |e^{i\theta}-1|\ge {2\over\pi}|\theta|,
  \qquad
  1-r_n^2\le {2\over n}.
\]

Put
\[
  I_{n,k}(\tau)=
  \left\{
    e^{i\theta}:
    \left|\theta-{2\pi k\over n}\right|_{\mathbb T}
    <
    {\pi\sqrt{\tau}\over n}
  \right\},
  \qquad
  \kappa(k)=\min(k,n-k).
\]
Then for all \(\zeta\in I_{n,k}(\tau)\),
\[
\boxed{
  P_n(\zeta)
  \le
  C_\tau {n\over 1+\kappa(k)^2},
}
\tag{4}
\]
where \(C_\tau\) depends only on \(\tau\).  This is just (3) plus the
comparison between the angular distance from \(1\) and
\(\kappa(k)/n\) on a fixed \(1/n\)-scale root window.

## Carleson-window sufficient condition

Suppose that \(\nu\) is a positive measure and that for some constants
\(\rho_\tau,B_\tau\), all \(n\ge N_0\), and all \(0\le k\le n-1\),
\[
\boxed{
  \nu(I_{n,k}(\tau))
  \le
  {\rho_\tau\log n+B_\tau\over n}.
}
\tag{5}
\]

Then (2)--(4) give
\[
\begin{aligned}
  \int_{B_{n,\tau}}P_n\,d\nu
  &\le
  \sum_{k=0}^{n-1}\int_{I_{n,k}(\tau)}P_n\,d\nu                       \\
  &\le
  C_\tau
  \sum_{k=0}^{n-1}
  {n\over1+\kappa(k)^2}
  {\rho_\tau\log n+B_\tau\over n}                                      \\
  &\le
  C_\tau'(\rho_\tau\log n+B_\tau),
\end{aligned}
\]
because
\[
  \sum_{k=0}^{n-1}{1\over1+\kappa(k)^2}
  \le
  1+2\sum_{k=1}^{\infty}{1\over1+k^2}<\infty.
\]

Thus the bad-set estimate of `292` holds with
\[
\boxed{
  b_\tau=C_\tau'\rho_\tau.
}
\tag{6}
\]

## Optimized constant target

In the Euler--Gamma normalization of `292`, the defect route is possible
at a fixed \(\tau\) precisely when there exists \(0<\alpha<2\) such that
\[
  b_\tau+(1-\alpha\tau)_+<1-{\alpha\over2}.
\]

Optimizing over \(\alpha\) gives the equivalent open window
\[
\boxed{
  \tau>{1\over2}
  \qquad\hbox{and}\qquad
  b_\tau<1-{1\over2\tau}.
}
\tag{7}
\]

Indeed, if \(\alpha\tau\le1\), the condition is
\[
  b_\tau<\alpha(\tau-1/2),
\]
which requires \(\tau>1/2\) and is maximized at
\(\alpha=1/\tau\).  If \(\alpha\tau\ge1\), the condition is
\[
  b_\tau<1-\alpha/2,
\]
which is again maximized at the boundary \(\alpha=1/\tau\).

Combining (6) and (7), the Carleson-window route closes the Abel
anti-concentration input whenever
\[
\boxed{
  C_\tau'\rho_\tau<1-{1\over2\tau}
  \qquad(\tau>1/2).
}
\tag{8}
\]

## Status

Closed as a sufficient reduction.  Root-window Carleson control with
constant satisfying (8) implies the Poisson-weighted bad-set estimate of
`292`, hence the Abel-defect threshold of `291`, hence eventual strong
margin plus the finite remainder `261`.

A1 remains open.  The missing mathematical input is to prove such a
window estimate, or a sharper substitute, for the actual Euler--Gamma
increment measure \(\nu_g\).

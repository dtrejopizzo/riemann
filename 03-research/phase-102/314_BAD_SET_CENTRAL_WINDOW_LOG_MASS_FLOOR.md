# Bad-set central-window log-mass floor

## Purpose

The optimized Abel bad-set route in `292`--`311` requires
\[
  \tau>{1\over2}.
\]
This note records a necessary cost of that choice.  When \(\tau>1/2\), the
bad set
\[
  B_{n,\tau}=\{F_n<\tau P_{1-1/n}\}
\]
contains a central \(1/n\)-scale window around \(\zeta=1\), not only
windows around the nontrivial Fejer zeros.  Therefore any logarithmic lower
density near \(1\) forces a positive logarithmic contribution to the
Poisson-weighted bad-set mass.

This is not a no-go by itself.  It is a necessary coefficient floor that
any successful Abel-defect proof must budget.

## Scaling ratio at the central point

Let \(P_n=P_{1-1/n}\).  At \(\theta=0\),
\[
  F_n(1)=n,
  \qquad
  P_n(1)= {1+(1-1/n)\over1-(1-1/n)}=2n-1.
\]
Thus
\[
\boxed{
  {F_n(1)\over P_n(1)}
  =
  {n\over 2n-1}
  \longrightarrow {1\over2}.
}
\tag{1}
\]

More generally, with \(\theta=u/n\),
\[
  {1\over n}P_n(e^{iu/n})\to p(u):={2\over1+u^2},
  \qquad
  {1\over n}F_n(e^{iu/n})\to
  f(u):=\left({2\sin(u/2)\over u}\right)^2 .
\]
Hence the central scaling ratio is
\[
\boxed{
  R(u):={f(u)\over p(u)}
  =
  {1+u^2\over2}
  \left({2\sin(u/2)\over u}\right)^2,
  \qquad R(0)={1\over2}.
}
\tag{2}
\]

## Central bad window

Fix \(\tau>1/2\).  Choose \(c_\tau>0\) so that
\[
\boxed{
  \sup_{|u|\le c_\tau}R(u)<\tau .
}
\tag{3}
\]
This is possible by continuity and \(R(0)=1/2\).

Then for all sufficiently large \(n\),
\[
\boxed{
  \left\{e^{i\theta}:\ |\theta|\le {c_\tau\over n}\right\}
  \subset B_{n,\tau}.
}
\tag{4}
\]
Indeed, the convergence of \(F_n(e^{iu/n})/P_n(e^{iu/n})\) to \(R(u)\) is
uniform on \(|u|\le c_\tau\), so (3) eventually implies
\[
  {F_n(e^{iu/n})\over P_n(e^{iu/n})}<\tau
  \qquad(|u|\le c_\tau).
\]

## Forced logarithmic bad-set mass from local density

Assume that a positive measure has an absolutely continuous component
\[
  d\nu=h(\theta)\,dm+d\nu_{\rm rem},
  \qquad dm={d\theta\over2\pi},
\]
with local lower density
\[
\boxed{
  h(\theta)\ge aL(e^{i\theta})-B,
  \qquad
  L(e^{i\theta})=-\log|2\sin(\theta/2)|,
}
\tag{5}
\]
on a fixed neighborhood of \(0\), where \(a>0\).  Since \(\nu_{\rm rem}\ge0\),
(4) gives
\[
  \int_{B_{n,\tau}}P_n\,d\nu
  \ge
  \int_{|\theta|\le c_\tau/n}P_n(e^{i\theta})h(\theta)\,dm .
\]
Changing variables \(u=n\theta\), using the same scaling as above, and
using
\[
  L(e^{iu/n})=\log n-\log|u|+O_{c_\tau}(1)
\]
in \(L^1([-c_\tau,c_\tau])\), we obtain
\[
\boxed{
  \liminf_{n\to\infty}
  {1\over\log n}
  \int_{B_{n,\tau}}P_n\,d\nu
  \ge
  a\,\beta(c_\tau),
}
\tag{6}
\]
where
\[
\boxed{
  \beta(c)
  =
  {1\over2\pi}\int_{-c}^{c}{2\over1+u^2}\,du
  =
  {2\over\pi}\arctan c.
}
\tag{7}
\]
The bounded term \(-B\) contributes only \(O(1)\), because
\[
  \int_{|\theta|\le c_\tau/n}P_n\,dm=O_{c_\tau}(1).
\]

## Budget consequence

The optimized `292`--`311` target is
\[
  b_\tau<1-{1\over2\tau},
  \qquad \tau>{1\over2}.
\]
But any lower log-density component with coefficient \(a\) forces
\[
\boxed{
  b_\tau\ge a\,\beta(c_\tau)
}
\tag{8}
\]
for every \(c_\tau\) satisfying (3).

Thus a successful Abel bad-set proof must fit between the lower floor
coming from the central logarithmic mass and the upper target
\[
\boxed{
  a\,\beta(c_\tau)
  \le
  b_\tau
  <
  1-{1\over2\tau}.
}
\tag{9}
\]
This is a coefficient-budget constraint, not a contradiction: taking
\(c_\tau\) small gives a small floor.  Its role is to prevent treating the
bad-set coefficient as if it came only from nontrivial Fejer-zero windows.

## Status

Closed as a necessary central-window floor for the Abel bad-set route.  A1
remains open until the full Euler--Gamma bad-set upper coefficient is
proved below the `292` threshold, or the direct Fejer/local-density route
closes strong margin.

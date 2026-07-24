# Central-floor weighted budget gate

## Purpose

`296_WEIGHTED_CARLESON_BAD_SET_GATE.md` gives a sufficient upper
condition for the Abel bad-set route, while
`314_BAD_SET_CENTRAL_WINDOW_LOG_MASS_FLOOR.md` gives a necessary lower
cost caused by local logarithmic mass near \(\zeta=1\).

This note combines them into a coefficient compatibility test.

## Central floor function

Let
\[
  p(u)={2\over1+u^2},
  \qquad
  f(u)=\left({2\sin(u/2)\over u}\right)^2,
  \qquad
  R(u)={f(u)\over p(u)}.
\]

For \(\tau>1/2\), define
\[
\boxed{
  K(\tau)
  =
  \sup\left\{
    {1\over2\pi}\int_{-c}^{c}p(u)\,du:
    c>0,\ \sup_{|u|\le c}R(u)<\tau
  \right\}.
}
\tag{1}
\]

Equivalently,
\[
  K(\tau)=
  \sup_{c:\ \sup_{|u|\le c}R(u)<\tau}
  {2\over\pi}\arctan c.
\]

Since \(R(0)=1/2\), \(K(\tau)>0\) for every \(\tau>1/2\).

## Necessary lower coefficient

If a positive measure has local lower density
\[
  h(\theta)\ge aL(e^{i\theta})-B,
  \qquad
  L(e^{i\theta})=-\log|2\sin(\theta/2)|,
\]
near \(\theta=0\), then `314` implies
\[
\boxed{
  \liminf_{n\to\infty}
  {1\over\log n}
  \int_{B_{n,\tau}}P_{1-1/n}\,d\nu
  \ge aK(\tau).
}
\tag{2}
\]

Thus any bad-set upper coefficient \(b_\tau\) must satisfy
\[
\boxed{
  b_\tau\ge aK(\tau).
}
\tag{3}
\]

## Compatibility with the Abel-defect target

The optimized `292`/`311` target is
\[
\boxed{
  b_\tau<1-{1\over2\tau},
  \qquad \tau>{1\over2}.
}
\tag{4}
\]

Combining (3)--(4), a necessary condition for the Abel bad-set route at
this \(\tau\) is
\[
\boxed{
  aK(\tau)<1-{1\over2\tau}.
}
\tag{5}
\]

If (5) fails, then no proof of the `292` bad-set estimate at that \(\tau\)
can coexist with the local density coefficient \(a\).  The obstruction is
not from nontrivial Fejer-zero windows; it is already forced by the central
window near \(\zeta=1\).

## Compatibility with the weighted Carleson sufficient condition

The sufficient condition in `296` gives
\[
  b_\tau=C_\tau\beta_\tau.
\]

Therefore a weighted-window proof must fit the two-sided budget
\[
\boxed{
  aK(\tau)
  \le
  C_\tau\beta_\tau
  <
  1-{1\over2\tau}.
}
\tag{6}
\]

This is not a contradiction by itself.  It says that the weighted
Carleson coefficient cannot be treated as arbitrarily small once a local
log-density component is present.  The central mass consumes part of the
available Abel-defect budget before any nontrivial-root concentration is
considered.

## Route consequence

For the live Euler--Gamma window \(1/2<a\le1\) from `265`, the bad-set
route can only use values of \(\tau>1/2\) for which
\[
  aK(\tau)<1-{1\over2\tau}.
\]

If no such \(\tau\) is available for the actual coefficient \(a\), the
Abel-defect route cannot close strong margin through `292`.  If such a
\(\tau\) is available, the remaining obligation is exactly the weighted
Carleson upper estimate of `296`, with enough room left after the central
floor.

## Status

Closed as the central-floor compatibility budget for the weighted bad-set
route.  A1 remains open until the actual Euler--Gamma increment measure
is constructed and shown to satisfy the remaining upper estimate with
constants inside this budget, or until another Fejer/Herglotz/RDI route
closes the compact core.

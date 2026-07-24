# Weighted Carleson bad-set gate

## Purpose

`311_BAD_SET_CARLESON_WINDOW_SUFFICIENT_CONDITION.md` gives a simple
sufficient condition for the bad-set estimate of `292`: uniformly control
the mass of every \(1/n\)-scale window around every \(n\)-th root.

This note records the sharper weighted form.  The Poisson kernel is much
larger near \(\zeta=1\) than near roots far from \(1\), so the natural
condition is not a uniform window bound but a Poisson-weighted window sum.

## Root-window notation

Let
\[
  P_n=P_{1-1/n},
  \qquad
  B_{n,\tau}=\{F_n<\tau P_n\}.
\]

As in `311`, for fixed \(\tau>0\) define root windows
\[
  I_{n,k}(\tau)
  =
  \left\{
    e^{i\theta}:
    \left|\theta-{2\pi k\over n}\right|_{\mathbb T}
    <
    {\pi\sqrt{\tau}\over n}
  \right\},
  \qquad
  0\le k\le n-1,
\]
and
\[
  \kappa(k)=\min(k,n-k).
\]

The cover and Poisson estimate of `311` give constants \(C_\tau\) such that
\[
\boxed{
  B_{n,\tau}\subset\bigcup_{k=0}^{n-1}I_{n,k}(\tau),
  \qquad
  P_n(\zeta)\le C_\tau {n\over 1+\kappa(k)^2}
  \quad(\zeta\in I_{n,k}(\tau)).
}
\tag{1}
\]

## Weighted sufficient condition

Let \(\nu\) be a positive measure.  Suppose that for all \(n\ge N_0\),
\[
\boxed{
  \sum_{k=0}^{n-1}
  {n\,\nu(I_{n,k}(\tau))\over 1+\kappa(k)^2}
  \le
  \beta_\tau\log n+B_\tau.
}
\tag{2}
\]

Then
\[
\boxed{
  \int_{B_{n,\tau}}P_n\,d\nu
  \le
  C_\tau(\beta_\tau\log n+B_\tau).
}
\tag{3}
\]

Indeed, by (1),
\[
\begin{aligned}
  \int_{B_{n,\tau}}P_n\,d\nu
  &\le
  \sum_{k=0}^{n-1}
  \int_{I_{n,k}(\tau)}P_n\,d\nu        \\
  &\le
  C_\tau
  \sum_{k=0}^{n-1}
  {n\,\nu(I_{n,k}(\tau))\over1+\kappa(k)^2}.
\end{aligned}
\]
This proves (3).

Thus the `292` coefficient is
\[
\boxed{
  b_\tau=C_\tau\beta_\tau.
}
\tag{4}
\]

## Closure threshold

Combining (4) with `292`, the weighted-window route feeds into the
Abel-defect threshold of `291` whenever
\[
\boxed{
  C_\tau\beta_\tau<1-{1\over 2\tau}
  \qquad(\tau>1/2),
}
\tag{5}
\]
after optimizing over \(\alpha\) as in `311`.

Then `291` gives an explicit \(N_\infty\), A0 gives compact A1 above that
threshold through strong margin, and the interval \(8\le n<N_\infty\) is
the finite certificate of `261`.

## Why this is sharper than uniform Carleson control

The uniform condition in `311`,
\[
  \nu(I_{n,k}(\tau))
  \le
  {\rho_\tau\log n+B_\tau\over n}
  \qquad(0\le k<n),
\]
implies (2), because
\[
  \sum_{k=0}^{n-1}{1\over1+\kappa(k)^2}=O(1).
\]

But the converse is false and is not needed.  Windows far from
\(\zeta=1\) have \(\kappa(k)\gg1\), and their Poisson weight is smaller by
the factor \((1+\kappa(k)^2)^{-1}\).  A large amount of mass in those
windows may be harmless for the Abel defect, while mass in the windows
near \(k=0\) is expensive.

Thus the true missing input can be stated more economically as the
weighted estimate (2), not necessarily as uniform unweighted Carleson
control.

## Harmless bounded-density component

`295` is recovered immediately from (2).  If \(d\nu=h\,dm\) with
\(0\le h\le H\), then
\[
  \nu(I_{n,k}(\tau))\le {C_\tau H\over n}.
\]
Therefore the weighted sum in (2) is \(O_{\tau,H}(1)\), so
\[
  \beta_\tau=0.
\]

This agrees with the direct Poisson proof in `295`.

## Status

Closed as the weighted Carleson sufficient gate for the Abel-defect route.
A1 remains open until the actual Euler--Gamma increment measure is
constructed and shown to satisfy (2) with a coefficient obeying (5), or
until another Fejer/Herglotz/RDI route proves the compact core.

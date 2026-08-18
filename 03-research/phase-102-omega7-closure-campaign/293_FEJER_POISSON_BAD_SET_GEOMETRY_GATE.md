# Fejer--Poisson bad-set geometry gate

## Purpose

`292_POISSON_WEIGHTED_BAD_SET_ANTI_CONCENTRATION_GATE.md` reduces the
Abel-transfer route to controlling the Poisson-weighted mass of
\[
  B_{n,\tau}=\{\zeta:\ F_n(\zeta)<\tau P_{1-1/n}(\zeta)\}.
\]

This note records the basic geometry of \(B_{n,\tau}\): it contains
macroscopic-in-\(1/n\) windows around every nontrivial \(n\)-th root of
unity.  Therefore the required estimate in `292` is not a formal
small-set estimate.  It is an arithmetic anti-concentration theorem for
the actual Euler--Gamma increment measure.

## Normalization

Write \(z=e^{i\theta}\), \(r_n=1-1/n\), and use
\[
\boxed{
  F_n(e^{i\theta})
  =
  {1\over n}
  \left({\sin(n\theta/2)\over \sin(\theta/2)}\right)^2,
  \qquad
  P_n(e^{i\theta})
  =
  {1-r_n^2\over |e^{i\theta}-r_n|^2}.
}
\tag{1}
\]

The nontrivial zeros of \(F_n\) are
\[
  \theta_k={2\pi k\over n},\qquad k=1,\ldots,n-1.
\]

## Uniform window contained in the bad set

Fix \(0<c\le1\).  If
\[
  |\theta-\theta_k|\le {c\over n},
  \qquad k=1,\ldots,n-1,
\tag{2}
\]
then
\[
\boxed{
  {F_n(e^{i\theta})\over P_n(e^{i\theta})}
  \le 4c^2
  \qquad(n\ge2).
}
\tag{3}
\]

Indeed, since \(\sin(n\theta_k/2)=0\),
\[
  |\sin(n\theta/2)|
  =
  |\sin(n(\theta-\theta_k)/2)|
  \le {n|\theta-\theta_k|\over2}.
\]
Therefore
we use the exact cancellation form
\[
  F_n(e^{i\theta})
  =
  {1\over n}
  \left|{e^{in\theta}-1\over e^{i\theta}-1}\right|^2.
\]
Multiplying by \(|e^{i\theta}-r_n|^2/(1-r_n^2)\) and using
\[
  |e^{in\theta}-1|
  =
  |e^{in(\theta-\theta_k)}-1|
  \le n|\theta-\theta_k|,
\]
gives
\[
  {F_n(e^{i\theta})\over P_n(e^{i\theta})}
  \le
  {n|\theta-\theta_k|^2\over 1-r_n^2}
  \left({|e^{i\theta}-r_n|\over |e^{i\theta}-1|}\right)^2.
\]

It remains to bound the last ratio.  Because \(k\ne0\) and
\(|\theta-\theta_k|\le1/n\), the distance from \(\theta\) to \(2\pi\mathbb Z\)
is at least \((2\pi-1)/n\).  Hence
\[
  |e^{i\theta}-1|\ge {2\over\pi}{2\pi-1\over n}>{3\over n}.
\]
Also
\[
  |e^{i\theta}-r_n|\le |e^{i\theta}-1|+{1\over n}
  \le {4\over3}|e^{i\theta}-1|.
\]
Finally,
\[
  1-r_n^2={2\over n}-{1\over n^2}\ge {1\over n},
\]
(3) follows, with room to spare.

Consequently,
\[
\boxed{
  \bigcup_{k=1}^{n-1}
  \left\{
    e^{i\theta}:\ |\theta-2\pi k/n|\le{\sqrt{\tau}\over 2n}
  \right\}
  \subset B_{n,\tau}
  \qquad(0<\tau\le1).
}
\tag{4}
\]

## Consequence

The bad set is not confined to a small fixed neighborhood of
\(\zeta=1\).  It follows the moving Fejer zeros through the whole circle.
For fixed \(0<\tau\le1\), (4) contains \(n-1\) windows of radius
\(\sqrt{\tau}/(2n)\).

Thus any proof of the `292` estimate
\[
  \int_{B_{n,\tau}}P_n\,d\nu_g
  \le b_\tau\log n+B_B
\tag{5}
\]
must show that the actual increment measure \(\nu_g\) does not place too
much Poisson-visible mass in those moving windows.  Positivity, total mass,
radial Abel growth, and local density near \(\zeta=1\) do not by themselves
control that distribution.

This is precisely why the spike model in `281` defeats a purely radial
argument: placing mass at a nontrivial \(n\)-th root puts it inside
\(B_{n,\tau}\), where Poisson can be large while Fejer is zero.

## Status

Closed as the deterministic geometry of the Poisson--Fejer bad sets.  The
A1 Abel-transfer route remains open until the arithmetic
Poisson-weighted anti-concentration estimate of `292` is proved for the
actual Euler--Gamma increment measure.

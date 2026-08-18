# Central-floor compatibility window

## Purpose

`297_CENTRAL_FLOOR_WEIGHTED_BUDGET_GATE.md` gives a necessary budget for
the Abel bad-set route:
\[
  aK(\tau)\le C_\tau\beta_\tau<1-{1\over2\tau},
  \qquad \tau>{1\over2}.
\]
This note checks that the central-window floor alone does not make the
route impossible in the live Euler--Gamma coefficient range
\[
  {1\over2}<a\le1.
\]

The result is only a compatibility lemma.  It does not prove the remaining
weighted Carleson upper estimate for the actual increment measure.

## Scaling ratio bound

Recall
\[
  R(u)
  =
  {1+u^2\over2}
  \left({2\sin(u/2)\over u}\right)^2 .
\]
We claim that
\[
\boxed{
  R(u)<{3\over2}
  \qquad(|u|\le3/2).
}
\tag{1}
\]

Put \(y=|u|/2\le3/4\).  Since
\[
  \sin y\le y-{y^3\over6}+{y^5\over120}
  \le y-{y^3\over8}
  \qquad(0\le y\le3/4),
\]
we have
\[
  {2\sin(u/2)\over u}
  \le 1-{u^2\over32}.
\]
Therefore, for \(x=u^2\le9/4\),
\[
  R(u)
  \le
  {1+x\over2}\left(1-{x\over32}\right)^2 .
\]
The right side is increasing for \(0\le x\le9/4\), because its derivative
is
\[
  {1\over2}\left(1-{x\over32}\right)
  \left({15\over16}-{3x\over32}\right)>0.
\]
Thus
\[
  R(u)
  \le
  {13\over8}\left({119\over128}\right)^2
  =
  {184093\over131072}
  <
  {3\over2}.
\]
This proves (1).

## A concrete nonempty window and a strict upper budget

Taking \(\tau=3/2\), (1) shows that \(c=3/2\) is admissible in the
definition of \(K(\tau)\).  Hence the central bad window is nonempty and
\[
  K(3/2)\ge {2\over\pi}\arctan(3/2)>0.
\]

We also need an upper bound for the full floor \(K(3/2)\).  At
\(u=17/10\), with \(y=u/2=17/20\),
\[
  \sin y\ge y-{y^3\over6}.
\]
Therefore
\[
\begin{aligned}
  R(17/10)
  &=
  {1+(17/10)^2\over2}
  \left({\sin(17/20)\over 17/20}\right)^2              \\
  &\ge
  {389\over200}
  \left(1-{(17/20)^2\over6}\right)^2                  \\
  &=
  {389\over200}\left({2111\over2400}\right)^2
  =
  {1733508869\over1152000000}
  >
  {3\over2}.
\end{aligned}
\tag{2}
\]
Thus no admissible \(c\) for \(\tau=3/2\) can satisfy \(c\ge17/10\).
Consequently
\[
  K(3/2)
  \le
  {2\over\pi}\arctan(17/10).
\]

Since \(17/10<\sqrt3\), we have
\[
  \arctan(17/10)<\arctan(\sqrt3)={\pi\over3},
\]
and hence
\[
\boxed{
  K(3/2)<{2\over3}.
}
\tag{3}
\]

On the other hand, the optimized Abel target at \(\tau=3/2\) is
\[
  1-{1\over2\tau}
  =
  1-{1\over3}
  =
  {2\over3}.
\]
Thus for every \(0<a\le1\),
\[
\boxed{
  aK(3/2)
  <
  1-{1\over2(3/2)}.
}
\tag{4}
\]

## Consequence

The central logarithmic mass forced by `314` consumes a positive part of
the Abel bad-set coefficient budget, but it does not by itself contradict
the optimized `292` target in the coefficient range allowed by `265`.

For example, at \(\tau=3/2\), the remaining open task is still meaningful:
prove the weighted upper estimate of `296` with a coefficient
\[
  C_{3/2}\beta_{3/2}
  <
  {2\over3}
\]
while respecting the necessary lower floor \(aK(3/2)\).

Equivalently, `297` should be read as a two-sided budget constraint, not as
a no-go for the Abel-defect route.

## Status

Closed as a compatibility check for the central-floor budget.  A1 remains
open: the missing theorem is still the actual Euler--Gamma weighted
Carleson/bad-set upper estimate, or another route proving strong margin or
the compact tail inequality.

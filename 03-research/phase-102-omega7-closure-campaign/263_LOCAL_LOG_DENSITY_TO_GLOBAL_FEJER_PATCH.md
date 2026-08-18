# Local log-density to global Fejer patch

## Purpose

`259_FEJER_LOG_DENSITY_CLOSURE_THEOREM.md` states the log-density input
near the boundary point \(\zeta=1\), while the Fejer conclusion is a global
integral over \(\partial\mathbb D\).  This note closes that bookkeeping gap.

The local lower bound is enough, provided the density is nonnegative
globally.  The price is an explicit constant depending on the arc where the
local logarithmic lower bound is known.

## Setup

Let
\[
  L(\theta)=-\log|2\sin(\theta/2)|
\]
and let
\[
  d\nu_g(e^{i\theta})
  =
  h(\theta)\,dm(\theta)+d\nu_{\rm rem}(e^{i\theta})
\]
with
\[
  h(\theta)\ge0,
  \qquad
  \nu_{\rm rem}\ge0.
\]

Assume there are constants
\[
  a>{1\over2},\qquad B_h\in\mathbb R,\qquad \theta_0\in(0,\pi]
\]
such that
\[
\boxed{
  h(\theta)\ge aL(\theta)-B_h
  \qquad(|\theta|\le\theta_0).
}
\tag{1}
\]

## Global extension of the lower bound

For \(|\theta|\ge\theta_0\),
\[
  |2\sin(\theta/2)|
  \ge
  2\sin(\theta_0/2),
\]
and therefore
\[
  L(\theta)
  \le
  C_{\theta_0},
  \qquad
  C_{\theta_0}:=-\log(2\sin(\theta_0/2)).
\]

Define
\[
\boxed{
  B_h^\ast
  =
  \max\{B_h,\ a(C_{\theta_0})_+\}.
}
\tag{2}
\]

On the local arc, (1) gives
\[
  h(\theta)\ge aL(\theta)-B_h^\ast.
\]
Outside the arc,
\[
  aL(\theta)-B_h^\ast
  \le
  aC_{\theta_0}-a(C_{\theta_0})_+
  \le0,
\]
while \(h(\theta)\ge0\).  Hence
\[
\boxed{
  h(\theta)\ge aL(\theta)-B_h^\ast
  \qquad(\theta\in[-\pi,\pi]).
}
\tag{3}
\]

Thus the local logarithmic density theorem is equivalent, for Fejer lower
bounds, to a global lower bound with a worsened explicit constant.

## Fejer consequence

Since \(F_n\ge0\) and \(\nu_{\rm rem}\ge0\),
\[
\begin{aligned}
  \int F_n\,d\nu_g
  &\ge
  \int F_nh\,dm                                   \\
  &\ge
  a\int F_nL\,dm
  -
  B_h^\ast\int F_n\,dm.
\end{aligned}
\]

The normalized Fejer kernel satisfies
\[
  \int F_n\,dm=1.
\]
By `260`,
\[
  \int F_nL\,dm\ge\log n-1.
\]
Therefore
\[
\boxed{
  \int F_n\,d\nu_g
  \ge
  a\log n-(a+B_h^\ast)
  \qquad(n\ge1).
}
\tag{4}
\]

This is the direct Fejer lower theorem required by `259`, with
\[
\boxed{
  \eta=a-{1\over2},\qquad
  B_F=a+B_h^\ast,\qquad
  N_F=1.
}
\tag{5}
\]

## Updated live obligation

The Fejer/log-density route no longer needs a global density theorem as a
separate assumption.  It is enough to prove:

1. a non-circular positive increment measure \(\nu_g\);
2. a decomposition with \(h\ge0\) and \(\nu_{\rm rem}\ge0\);
3. a local logarithmic lower density near \(\zeta=1\) with coefficient
   \(a>1/2\) and explicit constants \(B_h,\theta_0\).

Then (4) supplies the global Fejer lower bound, and `259` supplies the
effective strong-margin threshold.

## Status

Closed as a local-to-global patch for the conditional Fejer route.  It does
not construct the positive increment measure or the local lower density;
those remain the actual open inputs.

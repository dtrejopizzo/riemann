# Positive increment versus Fejer mass separation

## Purpose

`259`--`265` reduce the Fejer strong-margin route to a positive increment
measure with enough logarithmic mass near \(\zeta=1\).  This note records
the exact logical separation:

\[
\boxed{
  \nu_g\ge0\hbox{ proves Li/global positivity, but it does not by itself
  prove the compact A1 strong margin.}
}
\]

The missing datum is quantitative:
\[
  \int_{\partial\mathbb D}F_n\,d\nu_g
  \ge {A_n\over n}
  \qquad(n\ge8),
\]
or one of the lower-density hypotheses from `259`--`264`.

## What a positive increment measure gives

Let
\[
  g_0=2\lambda_1,\qquad
  g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}\quad(m\ge1).
\]

Assume that a finite positive measure \(\nu_g\) on \(\partial\mathbb D\)
has the increment moments
\[
  g_m=\int_{\partial\mathbb D}\overline{\zeta}^{\,m}\,d\nu_g(\zeta)
  \qquad(m\ge0).
\tag{1}
\]

Then the second-difference recovery formula gives
\[
\begin{aligned}
  2\lambda_n
  &=
  ng_0+2\sum_{m=1}^{n-1}(n-m)g_m                                      \\
  &=
  n\int_{\partial\mathbb D}
  \left[
    1+2\sum_{m=1}^{n-1}\left(1-{m\over n}\right)\Re(\zeta^{-m})
  \right]d\nu_g(\zeta)                                                  \\
  &=
  n\int_{\partial\mathbb D}F_n(\zeta)\,d\nu_g(\zeta),
\end{aligned}
\tag{2}
\]
where
\[
  F_n(e^{i\theta})
  =
  {1\over n}
  \left|
    1+e^{i\theta}+\cdots+e^{i(n-1)\theta}
  \right|^2.
\tag{3}
\]

Since \(F_n\ge0\), (2) implies
\[
  \lambda_n\ge0\qquad(n\ge1).
\tag{4}
\]

Thus a non-circular construction of (1) would close Omega7 globally through
Li.  This is the global Herglotz/Toeplitz route.

## What compact A1 needs

The compact route after A0 needs the strong margin
\[
  \lambda_n\ge {1\over2}A_n
  \qquad(n\ge8),
\tag{5}
\]
where \(A_n=\lambda_n^{\rm arch}\).  By (2), (5) is exactly
\[
\boxed{
  \int_{\partial\mathbb D}F_n\,d\nu_g
  \ge {A_n\over n}
  \qquad(n\ge8).
}
\tag{6}
\]

Therefore positivity of \(\nu_g\) supplies the sign of the Fejer integral,
but A1 asks for its size.  The missing gap is
\[
  \int F_n\,d\nu_g\ge0
  \quad\Longrightarrow\quad
  \int F_n\,d\nu_g\ge {A_n\over n},
\tag{7}
\]
and (7) is false as a matter of measure theory.

## Positivity and total mass are insufficient

Let \(\nu\) be any finite positive measure supported away from
\(\zeta=1\).  More explicitly, suppose that for some \(0<\theta_0\le\pi\),
\[
  \operatorname{supp}\nu\subset\{e^{i\theta}:|\theta|\ge\theta_0\}.
\tag{8}
\]

On this support,
\[
  |\sin(\theta/2)|\ge \sin(\theta_0/2),
\]
and hence
\[
  F_n(e^{i\theta})
  =
  {1\over n}
  \left({\sin(n\theta/2)\over\sin(\theta/2)}\right)^2
  \le
  {1\over n\sin^2(\theta_0/2)}.
\tag{9}
\]

Therefore
\[
  n\int F_n\,d\nu
  \le
  {\nu(\partial\mathbb D)\over\sin^2(\theta_0/2)}
  \qquad(n\ge1).
\tag{10}
\]

But the archimedean term has order
\[
  A_n\asymp n\log n.
\tag{11}
\]

So (6) fails for all sufficiently large \(n\).  This proves that positivity
and finite total mass do not imply the strong margin.

The same obstruction appears even more sharply at Fejer zeros.  If
\[
  \zeta^n=1,\qquad \zeta\ne1,
\]
then
\[
  F_n(\zeta)=0.
\tag{12}
\]
Thus a positive measure can be completely invisible to the \(n\)-th Fejer
test while remaining positive and finite.

These examples are not proposed as the zeta increment measure.  They prove
only the logical point needed in the phase: a proof of A1 cannot stop after
constructing a positive Herglotz measure.  It must prove a distributional
lower theorem for that specific measure.

## Necessary near-one concentration scale

The odd-harmonic formula behind the archimedean estimates gives
\[
  A_n={1\over2}n\log n+O(n).
\]
In particular, the explicit upper input
\[
  A_n\le {1\over2}n\log n+3n
\]
from `262` is on the correct scale, and the required lower bound (6) is a
logarithmic Fejer-mass condition:
\[
  \int F_n\,d\nu_g
  \gtrsim {1\over2}\log n.
\tag{13}
\]

A measure supported away from \(1\) gives \(O(1/n)\).  A bounded density
gives \(O(1)\), as shown in `202`.  An atom at \(1\) is too large and is
incompatible with the Euler--Gamma generator scale by `203`.

The only absolutely continuous scale compatible with the generator and
large enough for (13) is logarithmic concentration:
\[
  h(\theta)\ge aL(\theta)-B,
  \qquad
  L(\theta)=-\log|2\sin(\theta/2)|.
\tag{14}
\]

By `259`--`264`, coefficient
\[
  a>{1\over2}
\tag{15}
\]
is enough for the Fejer strong margin after a finite verification.  By
`265`, the actual Abel coefficient of the Euler--Gamma increment generator
forces
\[
  a\le1.
\tag{16}
\]

Thus the live Fejer window is exactly
\[
\boxed{
  {1\over2}<a\le1.
}
\tag{17}
\]

## Exact theorem still needed

The strong-margin/A1 Fejer route is now reduced to the following theorem,
with no hidden positivity-to-size step:

\[
\boxed{
\begin{gathered}
  \hbox{Construct the Euler--Gamma increment measure }\nu_g\ge0
  \hbox{ with moments }g_m,\\
  d\nu_g=h\,dm+d\nu_{\rm rem},\qquad h\ge0,\qquad\nu_{\rm rem}\ge0,\\
  h(\theta)\ge aL(\theta)-B_h
  \hbox{ on }|\theta|\le\theta_0
  \hbox{ for some }1/2<a\le1,\\
  \hbox{and verify the finite interval }
  8\le n<N_\infty(a,B_h,\theta_0).
\end{gathered}
}
\tag{18}
\]

Then `264` gives the strong margin for all larger \(n\), the finite
certificate closes the rest, and A0 gives compact A1.

Without (18), a positive increment measure still closes Omega7 globally by
Li if constructed non-circularly, but it does not close the compact A1
decomposition.

## Status

Closed as a separation theorem.  It eliminates the shortcut
\[
  \hbox{positive increment measure}\Rightarrow\hbox{A1 strong margin}
\]
and leaves the precise remaining Fejer obligation: a positive
Euler--Gamma increment measure with lower logarithmic density coefficient
\(1/2<a\le1\), plus the finite interval certificate.

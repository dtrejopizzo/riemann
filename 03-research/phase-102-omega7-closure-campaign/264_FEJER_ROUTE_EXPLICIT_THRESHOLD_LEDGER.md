# Fejer route explicit threshold ledger

## Purpose

`259` gives the conditional Fejer/log-density closure theorem.  The files
`260`, `262`, and `263` now provide the explicit constants needed in that
theorem.  This ledger records the resulting one-line threshold.

It does not prove A1.  It states exactly what remains to be proved in the
Fejer strong-margin route and what finite range would remain afterward.

## Required inputs

Assume the following have been proved non-circularly from the completed
Euler--Gamma data.

First, a positive increment measure decomposition:
\[
  d\nu_g(e^{i\theta})
  =
  h(\theta)\,dm(\theta)+d\nu_{\rm rem}(e^{i\theta}),
  \qquad h\ge0,\qquad \nu_{\rm rem}\ge0.
\tag{1}
\]

Second, a local logarithmic lower density near \(\zeta=1\):
\[
  h(\theta)\ge aL(\theta)-B_h
  \qquad(|\theta|\le\theta_0),
\tag{2}
\]
where
\[
  L(\theta)=-\log|2\sin(\theta/2)|,\qquad
  a>{1\over2},\qquad 0<\theta_0\le\pi.
\]

Define
\[
\boxed{
  B_h^\ast
  =
  \max\{B_h,\ a(-\log(2\sin(\theta_0/2)))_+\}.
}
\tag{3}
\]

## Fejer lower bound with explicit constants

By `263`, the local lower density implies the global lower bound
\[
  \int F_n\,d\nu_g
  \ge
  a\log n-(a+B_h^\ast)
  \qquad(n\ge1).
\tag{4}
\]

Thus in the notation of `259`,
\[
\boxed{
  \eta=a-{1\over2},\qquad
  B_F=a+B_h^\ast,\qquad
  N_F=1.
}
\tag{5}
\]

By `262`, the archimedean upper input is
\[
  A_n\le {1\over2}n\log n+3n
  \qquad(n\ge2),
\tag{6}
\]
so
\[
\boxed{
  B_A=3,\qquad N_A=2.
}
\tag{7}
\]

## Effective strong-margin threshold

Substituting (5) and (7) into `259`, the strong margin
\[
  \lambda_n\ge {1\over2}A_n
\]
holds for every
\[
\boxed{
  n\ge
  N_\infty(a,B_h,\theta_0)
  =
  \max\left(
    2,\,
    \left\lceil
      \exp\left(
        {3+a+B_h^\ast\over a-1/2}
      \right)
    \right\rceil
  \right).
}
\tag{8}
\]

For those \(n\), A0 gives
\[
  R_n(T_n)\le {1\over4}A_n,
\]
and therefore
\[
  C_n(T_n)
  =
  \lambda_n-{1\over4}A_n-R_n(T_n)
  \ge0.
\tag{9}
\]

Thus compact A1 is reduced to the finite interval
\[
\boxed{
  8\le n<N_\infty(a,B_h,\theta_0).
}
\tag{10}
\]

## Exact remaining theorem

The Fejer route is now reduced to this precise theorem:

\[
\boxed{
\begin{gathered}
  \hbox{Construct }\nu_g\ge0\hbox{ with moments }g_m,\\
  d\nu_g=h\,dm+d\nu_{\rm rem},\quad h\ge0,\quad\nu_{\rm rem}\ge0,\\
  h(\theta)\ge aL(\theta)-B_h
  \hbox{ on }|\theta|\le\theta_0
  \hbox{ for some }a>{1\over2}.
\end{gathered}
}
\tag{11}
\]

Together with the finite verification (10), this theorem closes the strong
margin, then compact A1 through A0, and hence Omega7 through the existing
phase assembly.

Without (11), the route remains conditional.  The constants and threshold
are no longer the obstruction.

## Status

Closed as an explicit threshold ledger for the Fejer/log-density route.
A1 remains open until the positive increment measure, local lower density,
and finite interval certificate are proved.

# Poisson-to-Fejer positive inverse no-go

## Purpose

`265_FEJER_LOG_DENSITY_ABEL_COEFFICIENT_BUDGET.md` shows that the Abel
growth of the increment generator leaves only the coefficient window
\[
  {1\over2}<a\le1
\]
for a Fejer/log-density closure.  This note records the next obstruction:
even a correct Abel or Poisson lower scale does not by itself imply the
Fejer lower bounds needed for the strong margin.

The obstruction is exact.  There is no positive inverse that recovers the
Fejer kernels from radial Poisson kernels.

## Kernels

Let
\[
  P_r(e^{i\theta})
  =
  \mathrm{Re}{1+re^{i\theta}\over1-re^{i\theta}}
  =
  {1-r^2\over |1-re^{i\theta}|^2},
  \qquad 0<r<1,
\]
and
\[
  F_N(e^{i\theta})
  =
  {1\over N}
  \left|
    1+e^{i\theta}+\cdots+e^{i(N-1)\theta}
  \right|^2.
\]

Then
\[
  P_r(e^{i\theta})>0
  \qquad(\theta\in\mathbb R,\ 0<r<1),
\tag{1}
\]
while
\[
  F_N(\zeta)=0
  \qquad(\zeta^N=1,\ \zeta\ne1).
\tag{2}
\]

## No positive reconstruction

Fix \(N\ge2\).  Suppose a positive finite combination of Poisson kernels
were dominated by \(F_N\):
\[
  F_N(e^{i\theta})
  \ge
  \sum_{j=1}^J \alpha_jP_{r_j}(e^{i\theta}),
  \qquad
  \alpha_j\ge0,\quad 0<r_j<1.
\tag{3}
\]

Evaluate (3) at any nontrivial \(N\)-th root of unity.  The left side is
zero by (2), while each term on the right is strictly positive by (1).
Therefore
\[
  \sum_{j=1}^J\alpha_jP_{r_j}(\zeta)=0
\]
forces
\[
  \alpha_j=0\qquad(1\le j\le J).
\]

Thus
\[
\boxed{
  \hbox{no nonzero positive combination of radial Poisson kernels lies
  below }F_N.
}
\tag{4}
\]

The same conclusion holds for positive integrals
\[
  \int_0^1 P_r\,d\sigma(r)
\]
with \(\sigma\ge0\): if such an integral is pointwise bounded above by
\(F_N\), evaluating at a nontrivial \(N\)-th root and using positivity of
\(P_r\) forces \(\sigma=0\).

## Consequence for Abel lower bounds

Assume one has radial Abel or Poisson lower bounds of the form
\[
  \int_{\partial\mathbb D}P_r\,d\nu_g\ge A(r)
  \qquad(0<r<1).
\tag{5}
\]

A proof of a Fejer lower bound
\[
  \int_{\partial\mathbb D}F_N\,d\nu_g\ge B_N
\tag{6}
\]
by positive kernel algebra would require a nonnegative measure
\(\sigma_N\) such that
\[
  F_N\ge\int_0^1P_r\,d\sigma_N(r),
\tag{7}
\]
and then
\[
  B_N\le\int_0^1 A(r)\,d\sigma_N(r).
\]

But (4) shows that (7) is possible only with \(\sigma_N=0\), giving no
positive lower bound.  Hence Abel lower data do not automatically transfer
to Fejer lower data by any positive inverse kernel.

This is the precise kernel reason behind the Tauberian gap in `206`.

## What additional theorem is needed

The Fejer strong-margin route must therefore prove one of the following
non-Abelian inputs:

1. a direct Fejer lower bound
   \[
     \int F_N\,d\nu_g
     \ge
     \left({1\over2}+\eta\right)\log N-B_F;
   \]
2. a local lower density theorem as in `263`, which can be integrated
   directly against \(F_N\);
3. an anti-concentration theorem excluding mass placement near the moving
   zero set
   \[
     \{\zeta:\zeta^N=1,\ \zeta\ne1\}.
   \]

Without one of these, Abel scale and Abel coefficient information remain
only radial data.  They do not see the moving zeros of \(F_N\).

## Relation to A1

The compact A1 route through Fejer strong margin needs
\[
  n\int F_n\,d\nu_g\ge A_n
  \qquad(n\ge8).
\]

The no-go above proves that this pointwise Fejer inequality cannot be
deduced from radial Poisson lower bounds alone.  The remaining Fejer input
in `264` is therefore genuine:
\[
  \nu_g\ge0
  \quad\hbox{plus}\quad
  \hbox{local log-density or direct Fejer anti-concentration}.
\]

## Status

Closed as a positive-inverse no-go.  A1 remains open.  The Fejer/log-density
route still requires an actual local density or direct Fejer lower theorem,
not just Abel growth of the increment generator.

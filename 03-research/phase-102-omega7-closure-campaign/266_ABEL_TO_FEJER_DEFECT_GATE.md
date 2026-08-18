# Abel-to-Fejer defect gate

## Purpose

`206_FEJER_ABEL_TAUBERIAN_GAP.md` shows that Abel logarithmic growth does
not imply the Fejer lower bound because the Fejer kernels have moving
zeros.  This note records the exact quantitative defect that must be
controlled to turn Abel information into the Fejer strong margin.

It is a reduction, not a proof of A1: the new input is an anti-concentration
bound for the positive increment measure near the moving Fejer zero set.

## Kernels

Let
\[
  P_r(e^{i\theta})
  =
  \operatorname{Re}{1+re^{i\theta}\over1-re^{i\theta}}
  =
  1+2\sum_{m\ge1}r^m\cos(m\theta)
\]
be the Poisson kernel, and set
\[
  r_n=1-{1\over n},\qquad P_n=P_{r_n}.
\]

Let
\[
  F_n(e^{i\theta})
  =
  {1\over n}
  \left|
    1+e^{i\theta}+\cdots+e^{i(n-1)\theta}
  \right|^2
\]
be the normalized Fejer kernel.

Both kernels are nonnegative and have normalized Lebesgue integral \(1\),
but \(F_n\) vanishes at the nontrivial \(n\)-th roots of unity whereas
\(P_n\) does not.

## Defect identity

For \(\alpha>0\), define the positive Abel--Fejer defect
\[
\boxed{
  D_{n,\alpha}(\zeta)
  =
  \bigl(P_n(\zeta)-\alpha F_n(\zeta)\bigr)_+.
}
\tag{1}
\]

Pointwise,
\[
  P_n\le \alpha F_n+D_{n,\alpha}.
\tag{2}
\]

Therefore, for every positive measure \(\nu\),
\[
  \int P_n\,d\nu
  \le
  \alpha\int F_n\,d\nu+\int D_{n,\alpha}\,d\nu,
\]
and hence
\[
\boxed{
  \int F_n\,d\nu
  \ge
  {1\over\alpha}
  \left(
    \int P_n\,d\nu-\int D_{n,\alpha}\,d\nu
  \right).
}
\tag{3}
\]

Thus all possible Abel-to-Fejer loss is concentrated in the single positive
defect integral \(\int D_{n,\alpha}\,d\nu\).

## Sufficient anti-concentration theorem

Assume that a positive increment measure \(\nu_g\) has been constructed.
Suppose there are constants
\[
  c_P>0,\quad B_P,\quad \alpha>0,\quad d\ge0,\quad B_D,\quad N
\]
such that, for every \(n\ge N\),
\[
\boxed{
  \int P_n\,d\nu_g\ge c_P\log n-B_P
}
\tag{4}
\]
and
\[
\boxed{
  \int D_{n,\alpha}\,d\nu_g\le d\log n+B_D.
}
\tag{5}
\]

Then by (3),
\[
  \int F_n\,d\nu_g
  \ge
  {c_P-d\over\alpha}\log n
  -
  {B_P+B_D\over\alpha}.
\tag{6}
\]

Consequently the Fejer lower theorem of `259` holds whenever
\[
\boxed{
  {c_P-d\over\alpha}>{1\over2}.
}
\tag{7}
\]

In that case the constants in `259` may be taken as
\[
  \eta={c_P-d\over\alpha}-{1\over2},
  \qquad
  B_F={B_P+B_D\over\alpha}.
\tag{8}
\]

Then the strong margin holds above the explicit threshold from `259`, and
the finite remainder is handled by `261`.

## Euler--Gamma normalization

For the Euler--Gamma increment generator, if the positive measure exists,
then the Carathéodory transform satisfies
\[
  H_g(r)=g_0+2\sum_{m\ge1}g_mr^m
  =
  2\mathcal G_+(r)-g_0.
\]

By `204` and `265`,
\[
  \mathcal G_+(r)
  =
  \lambda_1+
  {\xi'\over\xi}\!\left({1\over1-r}\right)
  =
  {1\over2}\log {1\over1-r}+O(1)
\]
on the positive radius.  Hence
\[
\boxed{
  \int P_n\,d\nu_g
  =
  \operatorname{Re}H_g(r_n)
  =
  \log n+O(1).
}
\tag{9}
\]

Thus the natural Euler--Gamma value in (4) is
\[
\boxed{c_P=1.}
\tag{10}
\]

With \(\alpha=1\), condition (7) becomes
\[
\boxed{d<{1\over2}.}
\tag{11}
\]

So an Abel-based Fejer proof must show that the part of the positive
measure seen by \(P_n\) but not by \(F_n\) contributes strictly less than
half of the logarithmic Abel mass.

## Relation to moving Fejer zeros

The defect \(D_{n,\alpha}\) is large precisely where \(P_n\) remains large
but \(F_n\) is small.  This includes neighborhoods of
\[
  e^{2\pi ik/n},\qquad 1\le k\le n-1,
\]
on the \(1/n^2\) scale described in `206`.

Therefore (5) is an anti-concentration theorem: it prevents the increment
measure from hiding a logarithmic portion of its Abel mass near the moving
Fejer zeros.

A local lower-density theorem such as `263` is one way to avoid this
problem directly, because it proves the Fejer lower bound without passing
through Abel.  The present gate records the alternative Abel-transfer route
and its exact loss term.

## Status

Closed as the exact Abel-to-Fejer defect reduction.  A1 remains open until
one proves either the log-density theorem of `264` or, alternatively, the
defect bound (5) with constants satisfying (7), plus the finite
verification of `261`.

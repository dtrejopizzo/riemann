# Fejer log-density closure theorem

## Purpose

`205_FEJER_LOG_CONSTANT_AUDIT.md` shows that the Fejer/log-density constants
are favorable.  This note turns that audit into a precise closure theorem
for the strong-margin route.

The theorem is conditional: it does not construct the positive increment
measure.  It states exactly what lower boundary theorem would close the
strong margin, hence compact A1 through A0.

## Increment measure normalization

Let
\[
  g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}
\]
be the Li second-difference sequence in the normalization of
`172`--`175`.

Assume there is a positive finite measure \(\nu_g\) on
\(\partial\mathbb D\) such that
\[
\boxed{
  g_m=\int_{\partial\mathbb D}\overline{\zeta}^{\,m}\,d\nu_g(\zeta)
  \qquad(m\ge0).
}
\tag{1}
\]

For
\[
  F_n(e^{i\theta})
  =
  {1\over n}\left|
    1+e^{i\theta}+\cdots+e^{i(n-1)\theta}
  \right|^2,
\]
the second-difference recovery formula gives
\[
\boxed{
  2\lambda_n
  =
  n\int_{\partial\mathbb D}F_n\,d\nu_g .
}
\tag{2}
\]

Therefore the strong margin
\[
  \lambda_n\ge {1\over2}A_n
\]
is equivalent to
\[
\boxed{
  n\int_{\partial\mathbb D}F_n\,d\nu_g\ge A_n.
}
\tag{3}
\]

## Explicit archimedean upper input

Assume that an explicit constant \(B_A\) and threshold \(N_A\) have been
proved such that
\[
\boxed{
  A_n\le {1\over2}n\log n+B_A n
  \qquad(n\ge N_A).
}
\tag{4}
\]

This is the upper companion to the lower archimedean estimates already used
for A0.  It is elementary from the odd-harmonic formula for
\(A_n=\lambda_n^{\rm arch}\).

## Direct Fejer lower theorem

Assume that there are constants \(\eta>0\), \(B_F\), and \(N_F\) such that
\[
\boxed{
  \int_{\partial\mathbb D}F_n\,d\nu_g
  \ge
  \left({1\over2}+\eta\right)\log n-B_F
  \qquad(n\ge N_F).
}
\tag{5}
\]

Then, for \(n\ge\max(N_A,N_F)\),
\[
\begin{aligned}
  n\int F_n\,d\nu_g-A_n
  &\ge
  n\left[
    \left({1\over2}+\eta\right)\log n-B_F
  \right]
  -
  \left({1\over2}n\log n+B_A n\right)\\
  &=
  n\left(\eta\log n-B_A-B_F\right).
\end{aligned}
\tag{6}
\]

Hence (3) holds whenever
\[
\boxed{
  \log n\ge {B_A+B_F\over\eta}.
}
\tag{7}
\]

Thus the strong margin is proved for every
\[
\boxed{
  n\ge
  N_\infty
  =
  \max\left(
    N_A,\,
    N_F,\,
    \left\lceil
      \exp\left({B_A+B_F\over\eta}\right)
    \right\rceil
  \right).
}
\tag{8}
\]

The remaining range \(8\le n<N_\infty\) is finite and can be closed by the
rational Li/Euler--Gamma interval verifier once (1) and (5) are established
with explicit constants.

## Log-density theorem implying the Fejer lower theorem

Let \(m=d\theta/(2\pi)\) be normalized boundary measure.  Suppose that near
\(\zeta=1\) the positive measure has a decomposition
\[
\boxed{
  d\nu_g(e^{i\theta})
  =
  h(\theta)\,dm(\theta)+d\nu_{\rm rem}(e^{i\theta}),
}
\tag{9}
\]
where the remainder contributes nonnegatively to all Fejer tests:
\[
\boxed{
  \int F_n\,d\nu_{\rm rem}\ge0
  \qquad(n\ge1).
}
\tag{10}
\]

Since \(F_n\ge0\), (10) is automatic if \(\nu_{\rm rem}\) is positive.

Assume that for \(|\theta|\) sufficiently small,
\[
\boxed{
  h(\theta)\ge a\,L(\theta)-B_h,
  \qquad
  L(\theta)=-\log|2\sin(\theta/2)|,
}
\tag{11}
\]
with
\[
\boxed{a>{1\over2}.}
\tag{12}
\]

The standard Fourier expansion
\[
  L(\theta)=\sum_{k\ge1}{\cos(k\theta)\over k}
\tag{13}
\]
holds in the usual boundary sense, and the Fejer Fourier coefficients are
\[
  \widehat F_n(k)=\left(1-{|k|\over n}\right)_+.
\tag{14}
\]

Therefore
\[
\begin{aligned}
  \int F_n L\,dm
  &=
  \sum_{k=1}^{n-1}
    \left(1-{k\over n}\right){1\over k}\\
  &=
  H_{n-1}-{n-1\over n}\\
  &=
  \log n+O(1).
\end{aligned}
\tag{15}
\]

More explicitly, any bound
\[
\boxed{
  \int F_nL\,dm\ge \log n-B_L
  \qquad(n\ge N_L)
}
\tag{16}
\]
gives, by (9)--(11),
\[
\boxed{
  \int F_n\,d\nu_g
  \ge
  a\log n-(aB_L+B_h)
  \qquad(n\ge N_L).
}
\tag{17}
\]

Thus (5) holds with
\[
\boxed{
  \eta=a-{1\over2},\qquad
  B_F=aB_L+B_h,\qquad
  N_F=N_L.
}
\tag{18}
\]

Combining (8) and (18), the log-density theorem (11) closes strong margin
for all sufficiently large \(n\), with an explicit finite remainder.

## Consequence for A1

If (1) and either (5) or (11) are proved with explicit constants, then
\[
  \lambda_n\ge {1\over2}A_n
\]
for all \(n\ge N_\infty\), and the remaining finite interval can be checked
directly.

Once strong margin holds for every \(n\ge8\), A0 gives
\[
  R_n(T_n)\le {1\over4}A_n,
\]
so
\[
  C_n(T_n)
  =
  \lambda_n-{1\over4}A_n-R_n(T_n)
  \ge
  {1\over2}A_n-{1\over4}A_n-{1\over4}A_n
  =
  0.
\tag{19}
\]

Hence A1 follows.

Together with the finite low-index Li certificate and the phase assembly,
Omega7 follows.

## Remaining mathematical input

This theorem reduces the Fejer route to two concrete obligations:

1. construct the positive increment measure \(\nu_g\) from Euler--Gamma data;
2. prove a lower Fejer theorem (5), or a lower logarithmic density theorem
   (11) with coefficient \(a>1/2\).

The Abel logarithm of the generator suggests the correct scale, but by the
Tauberian gap in `206` it does not imply either obligation.  The missing
step is a genuine boundary lower-density or anti-concentration theorem.

## Status

Closed as a conditional Fejer/log-density closure theorem.

A1 remains open.  The Fejer route is now concentrated into the construction
of a positive increment measure with lower logarithmic boundary density
coefficient strictly greater than \(1/2\), or an equivalent direct Fejer
lower bound.

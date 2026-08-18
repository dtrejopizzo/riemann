# Exact Fejer log-kernel constant

## Purpose

`259_FEJER_LOG_DENSITY_CLOSURE_THEOREM.md` uses a lower bound
\[
  \int_{\partial\mathbb D}F_n(\zeta)L(\zeta)\,dm(\zeta)
  \ge \log n-B_L.
\]
This note closes that analytic constant exactly.  With normalized boundary
measure \(dm=d\theta/(2\pi)\),
\[
  L(e^{i\theta})=-\log|2\sin(\theta/2)|,
\]
and the normalized Fejer kernel
\[
  F_n(e^{i\theta})
  =
  {1\over n}
  \left|1+e^{i\theta}+\cdots+e^{i(n-1)\theta}\right|^2,
\]
one may take
\[
\boxed{B_L=1\qquad(n\ge1).}
\]

## Fourier coefficients

The Fejer kernel has Fourier expansion
\[
  F_n(e^{i\theta})
  =
  \sum_{|k|<n}
  \left(1-{|k|\over n}\right)e^{ik\theta}.
\]
The logarithmic kernel has the boundary Fourier expansion
\[
  L(e^{i\theta})
  =
  \sum_{k\ge1}{\cos(k\theta)\over k},
\]
in \(L^1\) and distribution sense.  Therefore, by pairing Fourier
coefficients,
\[
\begin{aligned}
  \int_{\partial\mathbb D}F_nL\,dm
  &=
  \sum_{k=1}^{n-1}
  \left(1-{k\over n}\right){1\over k}        \\
  &=
  \sum_{k=1}^{n-1}{1\over k}
  -
  {1\over n}\sum_{k=1}^{n-1}1                 \\
  &=
  H_{n-1}-{n-1\over n}.
\end{aligned}
\tag{1}
\]

Thus the constant problem is finite and exact.

## Uniform lower bound

For \(n\ge1\),
\[
  H_{n-1}
  =
  \sum_{k=1}^{n-1}{1\over k}
  \ge
  \int_1^n {dx\over x}
  =
  \log n,
\]
with the empty sum convention at \(n=1\).  Hence (1) gives
\[
  \int F_nL\,dm
  \ge
  \log n-{n-1\over n}
  \ge
  \log n-1.
\]
Therefore
\[
\boxed{
  \int_{\partial\mathbb D}F_nL\,dm
  \ge
  \log n-1
  \qquad(n\ge1).
}
\tag{2}
\]

This proves the promised explicit choice
\[
\boxed{B_L=1,\qquad N_L=1.}
\]

## Sharper asymptotic

The exact identity (1) also gives
\[
  \int F_nL\,dm
  =
  \log n+\gamma-1+O(1/n),
\]
but the closure theorem in `259` only needs the elementary lower bound
(2).  No Tauberian step is involved in this computation: it is a direct
Fourier coefficient pairing for a fixed positive test kernel.

## Consequence for the Fejer closure threshold

In the log-density alternative of `259`, if
\[
  h(\theta)\ge aL(e^{i\theta})-B_h,
  \qquad a>{1\over2},
\]
and the remaining positive measure contributes nonnegatively to Fejer
tests, then (2) yields
\[
  \int F_n\,d\nu_g
  \ge
  a\log n-(a+B_h).
\]
Thus the constants in `259` may be fixed as
\[
\boxed{
  \eta=a-{1\over2},\qquad
  B_F=a+B_h,\qquad
  N_F=1.
}
\]

The unresolved input is now not the Fejer/log-kernel constant.  It is the
construction of the positive increment measure and the lower logarithmic
density theorem with coefficient \(a>1/2\).

## Status

Closed as an exact analytic subcertificate for the Fejer/log-density route.
It does not prove A1 by itself, but it removes one constant ambiguity from
the conditional strong-margin theorem.

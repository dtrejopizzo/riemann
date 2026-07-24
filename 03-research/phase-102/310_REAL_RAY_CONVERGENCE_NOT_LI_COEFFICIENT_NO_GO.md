# Real-ray convergence is not Li-coefficient convergence

## Purpose

`251_RDI_LI_COEFFICIENT_EXTRACTION_GATE.md` requires local uniform
convergence in the Li disk coordinate before passing to coefficients.

This note supplies the explicit model behind that requirement: pointwise
convergence on a real ray, even with the correct pointwise limit, does not
control Taylor coefficients.  Therefore an RDI/LP argument that identifies
only real-axis values of a normalized logarithm cannot imply
\(\lambda_n\ge0\).

## Model

Let the target function be \(F(z)\equiv0\), and define
\[
\boxed{
  F_N(z)={z\over 1+N^2z^2}.
}
\tag{1}
\]

For every real \(x\),
\[
  F_N(x)\to0.
\tag{2}
\]

Indeed \(F_N(0)=0\), and for fixed \(x\ne0\),
\[
  |F_N(x)|={|x|\over 1+N^2x^2}\to0.
\]

Thus the sequence converges pointwise to the correct real-axis limit.

## Coefficients do not converge

Near \(z=0\),
\[
  F_N(z)
  =
  z-N^2z^3+N^4z^5-\cdots.
\tag{3}
\]

Therefore
\[
\boxed{
  [z]F_N(z)=1
  \qquad(N\ge1),
}
\tag{4}
\]
whereas
\[
  [z]F(z)=0.
\]

So coefficient passage fails completely:
\[
  [z]F_N\not\to[z]F.
\tag{5}
\]

The reason is also explicit.  The poles of \(F_N\) are at
\[
  z=\pm {i\over N},
\]
which collapse to the origin.  Hence the family is not locally uniformly
convergent in any complex neighborhood of \(0\), and Cauchy's coefficient
formula cannot be passed to the limit.

## Consequence for RDI

The Li generator is
\[
  \mathcal L(z)
  =
  {z\over(1-z)^2}{\xi'\over\xi}\!\left({1\over1-z}\right)
  =
  \sum_{n\ge1}\lambda_nz^n.
\]

To infer \(\lambda_n\ge0\) from approximants \(\mathcal L_N\), it is not
enough to know that \(\mathcal L_N(x)\to\mathcal L(x)\) on a real ray or
on a set of real parameters.  One needs local uniform convergence on a
complex disk around \(z=0\), or another theorem that gives coefficient
convergence directly.

Thus the acceptable RDI bridge remains exactly the one in `251`:
\[
  \mathcal L_N(z)\to\mathcal L(z)
  \quad\hbox{locally uniformly near }0,
\]
with nonnegative approximating coefficients, or a locally uniform
real-rooted entire-function convergence theorem for the true \(\Xi\).

## Status

Closed as a real-ray convergence no-go for the RDI bridge.  A1 and Omega7
remain open until RDI supplies complex local uniform convergence,
coefficient convergence, real-rooted convergence to the true \(\Xi\), or
the compact A1 route is proved directly.

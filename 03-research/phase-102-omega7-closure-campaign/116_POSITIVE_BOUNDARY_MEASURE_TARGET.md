# Positive boundary measure target

## Purpose

The Mellin, bordered-current and Weil-Herglotz routes all point to the same
missing object: a positive boundary measure for the completed logarithmic
derivative at the Li boundary. This document states the exact theorem that
would close A1 and hence Omega7.

## Boundary variable

Write
\[
  s={1\over2}+z,
  \qquad
  \Phi(z)={\xi'\over\xi}\!\left({1\over2}+z\right).
\]

The functional equation gives
\[
  \Phi(-z)=-\Phi(z).
\]

The zeros of \(\xi\) correspond to poles of \(\Phi\). If every zero has the
form \(1/2+i\gamma\), then \(\Phi\) is the Cauchy transform of a real symmetric
divisor on the imaginary axis.

## Target theorem

The positive boundary measure target is:

There exists a positive symmetric measure \(\mu\) on \(\mathbb R\), constructed
from the Euler product, Gamma factor, functional equation and paired boundary
prescription, such that for \(z\) in the right half-plane of the line
coordinate,
\[
  \Phi(z)
  =
  A z+
  \int_{\mathbb R}
  \left({1\over z-it}+{1\over z+it}\right)d\mu(t),
\tag{1}
\]
with the integral understood in the same paired sense as the Li coefficients.

If (1) is proved without assuming real zeros, then the support of the divisor
is on the critical line and the Li sum-of-squares formula follows.

## Why the representation forces the critical line

Assume \(\Phi\) is meromorphic and has a representation of the form (1) in
the paired principal-value sense. The singularities of the integral in (1)
lie only at points \(z=it\) and \(z=-it\) belonging to the support of
\(\mu\), while \(Az\) is entire.

Therefore every pole of \(\Phi\) lies on the imaginary axis in the line
coordinate. But the poles of
\[
  \Phi(z)={\xi'\over\xi}\left({1\over2}+z\right)
\]
are precisely the shifted zeros \(z=\rho-1/2\), with multiplicity. Hence
\[
  \rho-1/2\in i\mathbb R
\]
for every zero \(\rho\), which is the critical-line statement.

## Implication to A1

For every \(n\ge1\),
\[
  \lambda_n
  =
  \sum_\rho\left[1-\left(1-{1\over\rho}\right)^n\right].
\]

Under (1), the divisor is represented by a positive real boundary measure.
For a zero \(\rho=1/2+it\), define \(\theta(t)\) by
\[
  1-{1\over\rho}=e^{i\theta(t)}.
\]
The paired contribution becomes
\[
  4\sin^2\left({n\theta(t)\over2}\right)d\mu(t).
\]

Therefore
\[
  \lambda_n
  =
  4\int_{\mathbb R}
  \sin^2\left({n\theta(t)\over2}\right)d\mu(t)\ge0.
\]

This proves Omega7 directly. In the phase-102 decomposition, it proves A1
after combining with the finite certificate and A0.

## Why this is not circular

The theorem is circular only if positivity of \(\mu\), or real support of the
divisor, is assumed. It is not circular if \(\mu\ge0\) is derived from a new
Euler--Gamma construction before any zero-location conclusion is invoked.

Thus the target is allowed to carry force-RH: proving it is proving RH.

## Off-line failure

For an admissible off-line control, a zero \(\rho\) gives
\[
  \left|1-{1\over\rho}\right|>1
\]
for one member of its quartet. The Li coefficient then has a geometric
negative subsequence. Such a control cannot admit a representation (1) with
\(\mu\ge0\).

Therefore (1) is discriminating: it is not build-neutral.

## Current obstruction

The Euler product gives an arithmetic construction in a half-plane of
absolute convergence. The missing theorem is positivity-preserving
continuation of that construction to the Li boundary. Standard analytic
continuation preserves identities, not positivity.

## Status

Open. This is the cleanest single target currently visible. It closes A1,
Omega7 and RH if proved from Euler--Gamma data.

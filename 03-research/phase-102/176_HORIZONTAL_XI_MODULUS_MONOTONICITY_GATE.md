# Horizontal xi modulus monotonicity gate

## Purpose

`175_LOG_DERIVATIVE_RH_EQUIVALENCE.md` proves that
\[
  \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2)
\]
is equivalent to RH.  This note rewrites the same theorem as horizontal
monotonicity of the completed modulus:
\[
  \partial_\sigma\log|\xi(\sigma+it)|\ge0
  \qquad(\sigma>1/2).
\]

This is a useful analytic target because it isolates the missing theorem as
monotonicity away from the symmetry axis.

## Exact identity

For
\[
  s=\sigma+it
\]
with \(\xi(s)\ne0\),
\[
  \partial_\sigma\log|\xi(s)|
  =
  \Re{\xi'\over\xi}(s).
\tag{1}
\]

Thus the half-plane gate is exactly
\[
  \boxed{
  \partial_\sigma\log|\xi(\sigma+it)|\ge0
  \qquad(\sigma>1/2).
  }
\tag{2}
\]

Equivalently,
\[
  |\xi(\sigma_2+it)|\ge|\xi(\sigma_1+it)|
  \qquad
  (1/2<\sigma_1<\sigma_2).
\tag{3}
\]

## RH equivalence

If (2) holds, then \(\xi\) has no zeros in the open half-plane
\(\sigma>1/2\), because a zero would create a logarithmic singularity whose
horizontal derivative changes sign in every punctured neighborhood.  By the
functional equation, no zero can lie in \(\sigma<1/2\).  Hence RH follows.

Conversely, under RH, the paired Hadamard product gives
\[
  {\xi'\over\xi}(s)=\sum_\rho {1\over s-\rho}.
\]
For \(\rho=1/2+i\gamma\) and \(\sigma>1/2\),
\[
  \Re {1\over s-\rho}
  =
  {\sigma-1/2\over(\sigma-1/2)^2+(t-\gamma)^2}>0.
\]
Hence (2) holds.

Therefore
\[
  RH
  \Longleftrightarrow
  \hbox{horizontal monotonicity }(2).
\tag{4}
\]

## Explicit Euler--Gamma form

Using
\[
  \xi(s)=
  {1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]
the derivative in (1) is
\[
\begin{aligned}
  \partial_\sigma\log|\xi(s)|
  &=
  \Re{1\over s}
  +
  \Re{1\over s-1}
  -{1\over2}\log\pi\\
  &\quad+
  {1\over2}\Re\psi\!\left({s\over2}\right)
  +
  \Re{\zeta'\over\zeta}(s).
\end{aligned}
\tag{5}
\]

In the Euler-product half-plane \(\sigma>1\),
\[
  \Re{\zeta'\over\zeta}(\sigma+it)
  =
  -\sum_{m\ge2}{\Lambda(m)\over m^\sigma}\cos(t\log m).
\tag{6}
\]

Thus the required inequality is the global signed inequality
\[
\boxed{
  \Re{1\over s}
  +
  \Re{1\over s-1}
  -{1\over2}\log\pi
  +
  {1\over2}\Re\psi\!\left({s\over2}\right)
  -
  \sum_{m\ge2}{\Lambda(m)\over m^\sigma}\cos(t\log m)
  \ge0
}
\tag{7}
\]
where the prime sum is initially valid for \(\sigma>1\) and must be continued
in the completed paired sense for \(1/2<\sigma\le1\).

This is the half-plane analogue of A1: pole, Gamma and primes must be kept
paired before estimating signs.

## Why symmetry is not enough

The functional equation gives
\[
  |\xi(1/2+u+it)|=|\xi(1/2-u+it)|.
\tag{8}
\]

Thus \(\sigma=1/2\) is a symmetry axis for the horizontal modulus.  But
symmetry alone does not imply that the axis is a minimum.  The missing
theorem is exactly that every horizontal line has no descent as
\(\sigma\) moves right.

Subharmonicity of \(\log|\xi|\) also does not by itself imply (2).
Subharmonicity controls two-dimensional averages; (2) is a one-dimensional
monotonicity statement along every horizontal line.

## Relation to A1

The compact A1 inequality is a coefficient/cutoff version of the same sign
problem.  The horizontal monotonicity theorem would close Omega7 globally
through RH and Li, but it does not automatically supply the A0/A1 compact
margin unless the stronger diagonal budget is proved.

The live analytic target is therefore:

\[
  \boxed{
  \partial_\sigma\log|\xi(\sigma+it)|\ge0
  \qquad(\sigma>1/2,\ t\in\mathbb R)
  }
\]
from the Euler--Gamma expression (5), without assuming RH.

## Status

Closed as an equivalent monotonicity gate.  A1 remains open.

The gate translates the weighted Toeplitz positivity problem into horizontal
monotonicity of the completed modulus.

# Tail and strong-margin generators

## Purpose

This document packages two remaining A1 gates as coefficient problems:

1. the strong-margin gate;
2. the one-sided tail gate.

The point is not to prove either gate.  The point is to state exactly what
coefficient positivity would have to be proved and to record the analytic
domain issue that appears for the infinite tail.

## Li and strong-margin generators

Let
\[
  \mathcal L(z)
  =
  z{d\over dz}\log \xi\!\left({1\over1-z}\right).
\]

Then, near \(z=0\),
\[
  \mathcal L(z)=\sum_{n\ge1}\lambda_n z^n.
\tag{1}
\]

Let
\[
  \mathcal A(z)=\sum_{n\ge1}\lambda_n^{\rm arch}z^n
\]
be the archimedean generating function recorded in the fixed-cutoff
document.  The strong-margin theorem
\[
  \lambda_n\ge {1\over2}\lambda_n^{\rm arch}\qquad(n\ge8)
\tag{SM}
\]
is equivalent to coefficient positivity, from index \(8\) onward, of
\[
  \boxed{
  \mathcal M(z)=\mathcal L(z)-{1\over2}\mathcal A(z).
  }
\tag{2}
\]

Equivalently, since
\[
  \lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime},
\]
this is the coefficient statement
\[
  \lambda_n^{\rm prime}+{1\over2}\lambda_n^{\rm arch}\ge0
  \qquad(n\ge8).
\]

Thus the strong-margin gate is not a new analytic object hidden from Li:
it is the Li generating transform with half of the archimedean generator
subtracted.

## Tail coefficients

For a fixed cutoff \(T\), define the coefficientwise tail
\[
  R_n(T)=
  \int_T^\infty
  (\psi(e^u)-e^u)e^{-u}
  \left(L'_{n-1}^{(1)}(u)-L_{n-1}^{(1)}(u)\right)\,du,
\tag{3}
\]
where the integral is understood coefficientwise, or with the same paired
boundary prescription as the phase.

The Laguerre generating identity gives
\[
  \sum_{n\ge1}
  \left(L'_{n-1}^{(1)}(u)-L_{n-1}^{(1)}(u)\right)z^n
  =
  -{z\over(1-z)^3}
  \exp\!\left(-{uz\over1-z}\right).
\tag{4}
\]

Formally, therefore,
\[
  \boxed{
  \mathcal R_T(z)
  :=
  \sum_{n\ge1}R_n(T)z^n
  =
  -{z\over(1-z)^3}
  \int_T^\infty
  (\psi(e^u)-e^u)e^{-u}
  \exp\!\left(-{uz\over1-z}\right)\,du.
  }
\tag{5}
\]

This is the exact generating transform for the tail whenever the interchange
of sum and integral is justified.

## Domain warning

The compact-core generator is holomorphic in the unit disk for fixed finite
cutoff.  The tail generator is subtler.  The available unconditional PNT
input has the shape
\[
  |\psi(e^u)-e^u|e^{-u}\le A\exp(-\eta(u)),
\]
where \(\eta(u)\) grows faster than \(\log u\), but not linearly in \(u\).

Hence the integral in (5) is controlled in the half-domain
\[
  \Re {z\over1-z}\ge0
\]
by the PNT envelope.  If
\[
  \Re {z\over1-z}<0,
\]
the exponential factor in (5) grows like
\[
  \exp\!\left(u\left| \Re {z\over1-z}\right|\right),
\]
and the current A0/PNT input does not justify convergence of the integral.

Therefore \(\mathcal R_T\) cannot be treated, from A0 alone, as an ordinary
holomorphic function on the whole unit disk.  It is a coefficientwise or
Abel-side object unless a stronger signed continuation theorem is proved.

## One-sided tail as coefficient gate

The A1 gate can be written as
\[
  K_n(T_n)+{3\over4}\lambda_n^{\rm arch}\ge0.
\]

Since
\[
  \lambda_n=K_n(T_n)+R_n(T_n)+\lambda_n^{\rm arch},
\]
this is equivalent to
\[
  \lambda_n-R_n(T_n)-{1\over4}\lambda_n^{\rm arch}\ge0.
\tag{6}
\]

Thus the moving-tail coefficient gate is:
\[
  [z^n]\left(\mathcal L(z)-{1\over4}\mathcal A(z)\right)
  -
  R_n(T_n)
  \ge0
  \qquad(n\ge8).
\tag{7}
\]

For a fixed cutoff \(T\), the analogous fixed-tail statement would be
coefficient positivity of
\[
  \mathcal L(z)-{1\over4}\mathcal A(z)-\mathcal R_T(z).
\tag{8}
\]

But A1 uses \(T_n\), not a fixed \(T\), and \(\mathcal R_T\) has the domain
warning above.  Therefore (8) is only a discovery coordinate unless the
moving cutoff and boundary continuation are handled by an additional signed
theorem.

## Eliminated class

The following proof pattern is eliminated:

1. form a formal tail generating integral;
2. treat it as holomorphic throughout the unit disk using only A0/PNT;
3. infer coefficient positivity by an ordinary disk argument.

The obstruction is analytic before it is arithmetical: A0 gives polynomial
tail domination coefficientwise, not a full-disk exponential Laplace
transform.

## Status

The strong-margin and tail gates are now written as exact coefficient
problems.  The strong-margin generator is a genuine Li-side holomorphic
object.  The tail generator is valid coefficientwise or in the Abel
half-domain supplied by the PNT envelope.  Closing A1 still requires a signed
continuation or one-sided coefficient theorem beyond A0.

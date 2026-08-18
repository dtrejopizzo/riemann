# 102 A1 zero-side discriminant

## Purpose

A1 must be proved arithmetically.  Still, the zero-side formula gives the
correct diagnostic for any proposed mechanism: it must be able to prevent the
off-line exponential mode.

## Li transform of a zero

For a zero `rho`, put

[
  w_\rho=1-{1\over\rho}.
]

The Li coefficient is formally organized by

[
  \lambda_n=\sum_\rho \left(1-w_\rho^n\right),
]

with the usual symmetric limiting prescription.  If RH holds, the paired
zeros have `|w_rho|=1`, and the expression becomes the nonnegative
sum-of-squares form.

If a zero lies off the critical line, one member of its symmetry quartet has

[
  |w_\rho|>1.
]

The quartet then contains a term of the form

[
  -2\operatorname{Re}(w_\rho^n)
]

along a subsequence, with geometric size.  This eventually dominates the
archimedean growth, which is only of order `n log n`.

## Discriminant requirement

Therefore any arithmetic proof of A1 must contain a mechanism that forbids
the off-line mode before the zero-side formula is invoked as a conclusion.
Equivalently, the arithmetic core must distinguish:

- the zeta data, where the signed core is required to satisfy A1;
- an Euler--Gamma control with an off-line quartet, where the same formal
  mechanism must fail.

This is not an optional numerical test.  It is the structural meaning of
point 9 and point 10.

## No-go class eliminated

The following class cannot close A1:

[
  \hbox{finite signed fit}+\hbox{zero-side diagnosis after the fact}.
]

Such a method can detect that an off-line quartet would break Li, but it does
not provide the arithmetic inequality that excludes the quartet.  It is a
valid falsification tool and not a proof.

## Surviving form

The surviving mechanism must be a signed arithmetic identity or variational
principle of the shape

[
  -n+\int_1^{e^{T(n)}}E(y)f'_{n,0}(y)\,dy
  +{3\over4}\lambda_n^{arch}
  =
  \mathcal E_n+\mathcal B_n,
]

where

[
  \mathcal E_n\ge0,
  \qquad
  \mathcal B_n\ge0,
]

are proved directly from Euler product, Gamma factor, functional equation,
and the paired boundary prescription.  If either nonnegativity is merely
equivalent to Li positivity, it remains a valid target only when proved
independently from those data.

## Status

The off-line sensitivity control is formulated.  It is not a proof of A1.
It fixes the minimum discriminant that any successful A1 proof must contain.

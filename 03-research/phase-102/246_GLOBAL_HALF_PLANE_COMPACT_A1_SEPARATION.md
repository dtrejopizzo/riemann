# Global half-plane versus compact A1 separation

## Purpose

The global half-plane route is a legitimate way to close Omega7:
\[
  \Re{\xi'\over\xi}(s)\ge0
  \qquad(\Re s>1/2)
\tag{1}
\]
is equivalent to RH by `175_LOG_DERIVATIVE_RH_EQUIVALENCE.md`, and RH
implies Li positivity.  This note records, in the current margin-tail
coordinates, exactly what (1) contributes to compact A1 and what it does
not contribute.

## What the global theorem gives

If the half-plane theorem (1) is proved non-circularly, then
\[
\boxed{
  \lambda_n\ge0
  \qquad(n\ge1).
}
\tag{2}
\]

With
\[
  A_n=\lambda_n^{\rm arch}>0,
  \qquad
  M_n=\lambda_n-{1\over2}A_n,
\]
this gives only
\[
\boxed{
  M_n\ge-{1\over2}A_n.
}
\tag{3}
\]

Equivalently, for the deficit ratio of `240`,
\[
\boxed{
  d_n={(-M_n)_+\over A_n}\le {1\over2}.
}
\tag{4}
\]

Thus global half-plane positivity controls the maximum possible
strong-margin deficit, but it does not eliminate that deficit.

## What A0 gives

A0 gives the upper tail half
\[
\boxed{
  R_n(T_n)\le {1\over4}A_n,
}
\tag{5}
\]
or
\[
\boxed{
  \delta_n={1\over4}A_n-R_n(T_n)\ge0.
}
\tag{6}
\]

In normalized form,
\[
\boxed{
  s_n={\delta_n\over A_n}\ge0.
}
\tag{7}
\]

## Exact remaining compact gap

Compact A1 is
\[
  C_n(T_n)=M_n+\delta_n\ge0.
\]

Equivalently,
\[
\boxed{
  s_n\ge d_n.
}
\tag{8}
\]

The combination of global half-plane positivity and A0 gives only
\[
  d_n\le {1\over2},
  \qquad
  s_n\ge0.
\tag{9}
\]

These inequalities do not imply (8).  They allow the formal endpoint
\[
  d_n={1\over2},\qquad s_n=0,
\tag{10}
\]
which gives
\[
  C_n(T_n)=-{1\over2}A_n<0.
\tag{11}
\]

This is not a zeta counterexample.  It is a sharp separation of proof
data: the global theorem supplies Li positivity, while compact A1 needs
either strong margin, tail compensation, or direct compact positivity.

## Project-level consequence

There are two distinct closure modes:

1. **External Omega7 closure.**  Prove the global half-plane theorem (1).
   This proves RH, hence Li positivity, and closes Omega7 by the global
   route.

2. **Internal compact A1 closure.**  Prove
   \[
     C_n(T_n)\ge0\qquad(n\ge8),
   \]
   equivalently \(s_n\ge d_n\).  This requires one of:
   strong margin, one-sided tail compensation, Loewner cone domination, or
   a direct signed compact theorem.

Therefore a successful proof of (1) would close Omega7 even if the compact
A1 obligation remains unproved as a separate internal certificate.  But if
the phase requirement is to close A1 itself, then (1) must be supplemented
by the compact bridge (8) or by an equivalent direct A1 proof.

## Status

Closed as the global half-plane versus compact A1 separation.

A1 remains open.  Omega7 remains open unless either the global half-plane
theorem is proved non-circularly or the compact A1 gate is proved directly.

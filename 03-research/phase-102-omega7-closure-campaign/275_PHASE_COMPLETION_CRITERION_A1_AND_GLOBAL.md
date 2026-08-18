# Phase completion criterion: A1 and global closure

## Purpose

This phase contains external closure routes for Omega7 and internal compact
routes for A1.  This note records the exact completion criterion for the
current requested goal:

\[
\boxed{
  \hbox{Omega7 must be closed, and A1 must be closed as a compact
  certificate.}
}
\]

The distinction matters.  A global RH/Li proof closes Omega7 externally,
but it does not automatically prove the compact margin-tail inequality
isolated as A1.

## Compact A1 target

For \(n\ge8\), write
\[
  A_n=\lambda_n^{arch},
  \qquad
  M_n=\lambda_n-{1\over2}A_n,
  \qquad
  \delta_n={1\over4}A_n-R_n(T_n).
\]

Then compact A1 is
\[
\boxed{
  C_n(T_n)=M_n+\delta_n\ge0
  \qquad(n\ge8).
}
\tag{1}
\]

Equivalently,
\[
\boxed{
  s_n\ge d_n,
  \qquad
  s_n={\delta_n\over A_n},
  \qquad
  d_n={(-M_n)_+\over A_n}.
}
\tag{2}
\]

The finite base range \(1\le n\le7\) is handled by the phase base
certificate, and the \(n=8\) half-arch margin is certified by the interval
verifier.

## External Omega7 closure routes

Omega7 is closed externally if any one of the following is proved
non-circularly.

### Global half-plane theorem

\[
\boxed{
  \Re{\xi'\over\xi}(s)\ge0
  \qquad(\Re s>1/2).
}
\tag{3}
\]

By the log-derivative equivalence, (3) is equivalent to RH and therefore
implies Li positivity.

### Disk Herglotz theorem

Construct a positive finite measure \(\nu_\xi\) on \(\partial\mathbb D\)
such that
\[
\boxed{
  2{\xi'\over\xi}\!\left({1\over1-z}\right)
  =
  \int_{\partial\mathbb D}{\zeta+z\over\zeta-z}\,d\nu_\xi(\zeta).
}
\tag{4}
\]

By `253`, this is the disk form of (3).  The measure must be constructed
before using zero support.

### RDI coefficient or real-rooted bridge

Prove one of the bridges in `251`:
\[
\boxed{
  zF_N'(z)\to
  {z\over(1-z)^2}{\xi'\over\xi}\!\left({1\over1-z}\right)
  \quad\hbox{locally uniformly near }0
}
\tag{5}
\]
with nonnegative approximating coefficients, or
\[
\boxed{
  \Theta_N\to\Xi
  \quad\hbox{locally uniformly as entire functions, with all }\Theta_N
  \hbox{ real-rooted}.
}
\tag{6}
\]

Either bridge gives Li positivity or RH directly, hence closes Omega7.

## Why external closure is not A1 closure

If an external route proves
\[
  \lambda_n\ge0\qquad(n\ge1),
\tag{7}
\]
then
\[
  M_n=\lambda_n-{1\over2}A_n\ge-{1\over2}A_n,
\]
or
\[
  d_n\le {1\over2}.
\tag{8}
\]

A0 gives only
\[
  \delta_n\ge0,
  \qquad s_n\ge0.
\tag{9}
\]

The pair (8)--(9) does not imply
\[
  s_n\ge d_n.
\]

Thus an external RH/Li proof closes Omega7, but it does not by itself prove
the compact A1 certificate (1).  If A1 is part of the deliverable, the
phase remains internally incomplete until (1) or an equivalent compact
bridge is proved.

## Compact A1 closure routes

The A1 part of the goal is closed if any one of the following is proved for
every \(n\ge8\).

### Direct compact positivity

\[
\boxed{
  C_n(T_n)\ge0.
}
\tag{10}
\]

### Margin-tail bridge

\[
\boxed{
  s_n\ge d_n.
}
\tag{11}
\]

### Strong margin plus A0

\[
\boxed{
  \lambda_n\ge {1\over2}A_n
  \qquad(n\ge8).
}
\tag{12}
\]

Then \(d_n=0\), and A0 gives \(s_n\ge0\), so (11) follows.

The Fejer route `259`--`273` is one conditional mechanism for proving
(12): construct \(\nu_g\ge0\), prove the required Fejer distribution lower
bound, and certify the finite remainder.

### Tail compensation

The slack form of `255` is
\[
\boxed{
  R_n(T_n)\le {1\over4}A_n-h_n,
  \qquad
  h_n\ge(-M_n)_+.
}
\tag{13}
\]

Equivalently, \(\delta_n\ge(-M_n)_+\), which is (11).

### Signed tail phase/lobe theorem

The full A0-improvement route is the phase/lobe inequality of `254` and
`274` with the deficit-compensating lower bound:
\[
\boxed{
  I_n(T_n)\ge \left(d_n-{1\over4}\right)A_n.
}
\tag{14}
\]

The simpler nonpositive-tail sufficient route is
\[
  R_n(T_n)\le0
\]
plus the quarter margin \(\lambda_n\ge A_n/4\).

### Loewner/Schur comparative order

Any comparative form proving
\[
\boxed{
  \left(
  \mathfrak Q^{\mathcal L}
  -
  {1\over4}\mathfrak Q^{\mathcal A}
  -
  \mathfrak Q^{\mathcal R,T_n}
  \right)(1-z^n,1-z^n)
  \ge0
}
\tag{15}
\]
for every \(n\ge8\) is a compact A1 proof in quadratic-form coordinates.

## Completion theorem

For the current objective, completion requires both:

1. **Omega7 closure:** Li positivity/RH is proved, either by compact A1
   assembly or by a valid external route.
2. **A1 closure:** the compact inequality (1), or an equivalent condition
   (10)--(15), is proved for every \(n\ge8\).

If only item 1 is proved by an external route, Omega7 is closed but the
explicit request "including A1" is not fully satisfied.  If item 2 is
proved, then item 1 follows by the existing phase assembly and Li's
criterion.

Thus compact A1 is the stronger completion target for this phase.

## Status

Closed as a completion criterion and route ledger.  It does not prove A1;
it fixes the exact evidence required before the phase can be marked
complete.

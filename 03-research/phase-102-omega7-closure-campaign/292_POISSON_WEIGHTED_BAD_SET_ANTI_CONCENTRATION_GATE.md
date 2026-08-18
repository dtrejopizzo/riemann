# Poisson-weighted bad-set anti-concentration gate

## Purpose

`291_ABEL_DEFECT_CONSTANT_THRESHOLD_LEDGER.md` says that the Abel route
closes strong margin if the defect
\[
  D_{n,\alpha}=(P_{1-1/n}-\alpha F_n)_+
\]
has logarithmic coefficient \(d_\alpha<1-\alpha/2\) in the natural
Euler--Gamma normalization.

This note rewrites that defect bound as a more geometric
anti-concentration theorem: the positive increment measure must not place
too much Poisson-weighted mass on the moving set where Fejer is small
relative to Poisson.

## Bad sets

Fix \(\tau>0\).  Define
\[
\boxed{
  B_{n,\tau}
  =
  \{\zeta\in\partial\mathbb D:\ F_n(\zeta)<\tau P_n(\zeta)\},
  \qquad
  P_n=P_{1-1/n}.
}
\tag{1}
\]

The set \(B_{n,\tau}\) contains the nontrivial \(n\)-th roots of unity,
because \(F_n\) vanishes there while \(P_n>0\).

On the complement \(B_{n,\tau}^c\), one has
\[
  P_n\le {1\over\tau}F_n.
\]
Equivalently,
\[
  P_n-\alpha F_n\le (1-\alpha\tau)P_n
  \qquad\hbox{on }B_{n,\tau}^c.
\tag{2}
\]

On \(B_{n,\tau}\), the trivial bound is
\[
  (P_n-\alpha F_n)_+\le P_n.
\tag{3}
\]

Combining (2)--(3) gives the pointwise estimate
\[
\boxed{
  D_{n,\alpha}
  \le
  P_n{\bf 1}_{B_{n,\tau}}
  +
  (1-\alpha\tau)_+P_n{\bf 1}_{B_{n,\tau}^c}.
}
\tag{4}
\]

This is exact enough for the constant ledger.

## Defect from Poisson-weighted bad-set mass

Let \(\nu\) be a positive measure.  Suppose that, for all \(n\ge N_0\),
\[
\boxed{
  \int P_n\,d\nu\le C_P\log n+B_P^+
}
\tag{5}
\]
and
\[
\boxed{
  \int_{B_{n,\tau}}P_n\,d\nu\le b_\tau\log n+B_B.
}
\tag{6}
\]

Then (4) gives
\[
\begin{aligned}
  \int D_{n,\alpha}\,d\nu
  &\le
  \int_{B_{n,\tau}}P_n\,d\nu
  +(1-\alpha\tau)_+\int_{B_{n,\tau}^c}P_n\,d\nu       \\
  &\le
  \left(b_\tau+(1-\alpha\tau)_+C_P\right)\log n
  +B_B+(1-\alpha\tau)_+B_P^+.
\end{aligned}
\]

Thus the defect coefficient may be taken as
\[
\boxed{
  d_\alpha(\tau)=b_\tau+(1-\alpha\tau)_+C_P.
}
\tag{7}
\]

## Natural Euler--Gamma constant condition

For the Euler--Gamma increment measure, the expected two-sided Abel scale is
\[
  \int P_n\,d\nu_g=\log n+O(1),
\]
so \(C_P=1\) at the leading-coefficient level.

The `291` condition becomes
\[
  b_\tau+(1-\alpha\tau)_+<1-{\alpha\over2}.
\tag{8}
\]

There are two useful regimes.

### Regime 1: \(\alpha\tau\le1\)

Then (8) is
\[
\boxed{
  b_\tau<\alpha\left(\tau-{1\over2}\right).
}
\tag{9}
\]

This requires \(\tau>1/2\).  In words: if the bad set is defined by
Fejer carrying less than a \(\tau\)-fraction of Poisson, then the
Poisson-weighted mass of that bad set must have logarithmic coefficient
strictly smaller than \(\alpha(\tau-1/2)\).

### Regime 2: \(\alpha\tau\ge1\)

Then the good-set contribution vanishes and (8) is
\[
\boxed{
  b_\tau<1-{\alpha\over2}.
}
\tag{10}
\]

This is only useful for \(\alpha<2\), as already forced by `291`.

## Interpretation

The Poisson kernel measures radial Abel mass.  The Fejer kernel measures
the strong-margin mass.  The bad set \(B_{n,\tau}\) is precisely where
radial Abel mass can hide from Fejer.

Therefore the Abel-transfer route can be attacked by proving the
Poisson-weighted anti-concentration estimate
\[
\boxed{
  \int_{B_{n,\tau}}P_n\,d\nu_g
  \le b_\tau\log n+B_B
}
\tag{11}
\]
with constants satisfying either (9) or (10).

This is more localized than bounding \(D_{n,\alpha}\) directly, and it
separates the problem into:

1. geometric analysis of the moving ratio \(F_n/P_n\);
2. arithmetic distribution of the actual increment measure \(\nu_g\) on
   the moving bad sets.

## Relation to the spike obstruction

The model in `281` places mass at points where \(F_{N_j}=0\) and
\(P_{N_j}\asymp N_j\).  Those points lie in every \(B_{N_j,\tau}\).  The
Poisson-weighted bad-set mass is then \(\gg\log N_j\), so \(b_\tau\) is too
large to satisfy (9)--(10).

Thus the bad-set condition is not a formal consequence of positivity or
Abel size.  It is exactly the missing arithmetic anti-concentration
against the moving Fejer-zero geometry.

## Closure consequence

If a positive Euler--Gamma increment measure \(\nu_g\) is constructed and
there exist \(0<\alpha<2\), \(\tau>0\), and effective constants satisfying

\[
  \int P_n\,d\nu_g\ge\log n-B_P^-,
  \qquad
  \int P_n\,d\nu_g\le\log n+B_P^+,
\]
\[
  \int_{B_{n,\tau}}P_n\,d\nu_g\le b_\tau\log n+B_B,
\]
and
\[
  b_\tau+(1-\alpha\tau)_+<1-\alpha/2,
\]
then `291` gives an explicit threshold above which strong margin holds.
The finite remainder is handled by `261`, and A0 then closes compact A1.

## Status

Closed as a geometric anti-concentration reduction for the Abel-defect
route.  A1 remains open until the positive increment measure and the
Poisson-weighted bad-set bound are proved for the actual Euler--Gamma
measure.

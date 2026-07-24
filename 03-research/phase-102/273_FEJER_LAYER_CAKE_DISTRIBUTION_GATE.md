# Fejer layer-cake distribution gate

## Purpose

`271_POSITIVE_INCREMENT_FEJER_MASS_SEPARATION.md` isolates the remaining
compact Fejer mass requirement
\[
  \int_{\partial\mathbb D}F_n\,d\nu_g\ge {A_n\over n},
  \qquad A_n=\lambda_n^{arch}.
\]

This note rewrites that requirement as an exact distribution theorem for
the superlevel sets of \(F_n\).  It separates three possible ways to close
the Fejer route:

1. local logarithmic density near \(\zeta=1\);
2. anti-concentration against the moving zero set of \(F_n\);
3. a direct lower bound on the layer-cake distribution function.

No positivity is hidden here.  The result is an equivalent form of the
remaining Fejer lower theorem.

## Layer-cake identity

Let \(\nu\) be any finite positive measure on \(\partial\mathbb D\).  Since
\[
  0\le F_n(\zeta)\le n,
\]
the layer-cake formula gives
\[
\boxed{
  \int_{\partial\mathbb D}F_n(\zeta)\,d\nu(\zeta)
  =
  \int_0^n
  \nu\{\zeta:F_n(\zeta)\ge t\}\,dt.
}
\tag{1}
\]

Indeed,
\[
  F_n(\zeta)=\int_0^n{\bf 1}_{\{t\le F_n(\zeta)\}}\,dt,
\]
and Tonelli's theorem applies because the integrand is nonnegative.

Thus compact strong margin is exactly
\[
\boxed{
  \int_0^n
  \nu_g\{F_n\ge t\}\,dt
  \ge {A_n\over n}
  \qquad(n\ge8).
}
\tag{2}
\]

This is the distribution form of the Fejer gate.

## Dyadic certificate form

Let
\[
  J_n=\lceil\log_2 n\rceil.
\]
For \(0\le j\le J_n\), put
\[
  E_{n,j}=\{\zeta:F_n(\zeta)\ge2^j\}.
\]

From (1),
\[
  \int F_n\,d\nu
  \ge
  \sum_{j=0}^{J_n-1}
  \int_{2^j}^{2^{j+1}}\nu\{F_n\ge t\}\,dt
  \ge
  \sum_{j=0}^{J_n-1}2^j\,\nu(E_{n,j+1}).
\tag{3}
\]

Therefore a sufficient dyadic certificate for compact A1 through strong
margin is
\[
\boxed{
  \sum_{j=0}^{J_n-1}2^j\,\nu_g(E_{n,j+1})
  \ge {A_n\over n}
  \qquad(n\ge8).
}
\tag{4}
\]

Conversely, the exact criterion remains (2), so any proof of the Fejer
lower theorem must supply comparable information on the distribution
function
\[
  t\mapsto \nu_g\{F_n\ge t\}.
\]

## Relation with the local density route

The local density theorem in `263` is one way to prove (2).  On the main
arc \(|\theta|\le1/n\), `200` gives
\[
  F_n(e^{i\theta})\ge {4\over\pi^2}n.
\]
Thus
\[
  \nu_g\{F_n\ge {4\over\pi^2}n\}
  \ge
  \nu_g\{|\theta|\le1/n\}.
\]

If a lower logarithmic density gives
\[
  \nu_g\{|\theta|\le1/n\}
  \gg {\log n\over n},
\]
then the top layer alone contributes
\[
  n\cdot{\log n\over n}\asymp\log n,
\]
which is the required scale for \(A_n/n\).

## Relation with the Abel-defect route

The Abel-transfer gate in `266` controls a different distributional
quantity:
\[
  D_{n,\alpha}=(P_{1-1/n}-\alpha F_n)_+.
\]

A small defect integral says that the part of \(\nu_g\) seen by the Poisson
kernel but lying in low Fejer layers is not too large.  In layer-cake
language, it prevents the distribution
\[
  \nu_g\{F_n<t\}
\]
from carrying too much of the Abel logarithmic mass near the moving Fejer
zeros.

Thus `266` is an anti-concentration route to (2), while `263` is a direct
local-density route to (2).

## Exact remaining theorem

The compact Fejer route can now be stated without naming a preferred
mechanism:

\[
\boxed{
  \int_0^n
  \nu_g\{F_n\ge t\}\,dt
  \ge {A_n\over n}
  \qquad(n\ge8).
}
\tag{5}
\]

Together with a non-circular construction of the positive increment measure
\(\nu_g\), (5) gives the strong margin
\[
  \lambda_n\ge {1\over2}A_n
\]
and A0 then gives compact A1.

If only an eventual version of (5) is proved, the finite interval below the
effective threshold is exactly the finite certificate of `261`.

## Status

Closed as an equivalent distribution form of the Fejer mass theorem.  A1
remains open until the positive increment measure and the layer-cake lower
bound, or one of its sufficient forms, is proved.

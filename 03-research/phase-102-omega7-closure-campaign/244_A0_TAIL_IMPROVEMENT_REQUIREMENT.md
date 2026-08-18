# A0 tail-improvement requirement

## Purpose

`238_TAIL_MARGIN_COMPENSATION_FRONTIER.md`,
`240_DEFICIT_RATIO_TAIL_SURPLUS_GATE.md`, and
`241_TAIL_SURPLUS_GENERATOR_DIAGONAL_NO_GO.md` show that A0 supplies only
nonnegative tail surplus.  This note rewrites the remaining A1 gap as the
exact quantitative improvement over A0.

It is a calibration lemma, not a proof of A1.

## Normalizations

Let
\[
  A_n=\lambda_n^{\rm arch},
  \qquad
  M_n=\lambda_n-\frac12A_n,
  \qquad
  \delta_n=\frac14A_n-R_n(T_n).
\]

Define the normalized A0 surplus
\[
\boxed{
  \eta_n
  =
  {\,\delta_n\over A_n}
  =
  \frac14-{R_n(T_n)\over A_n}.
}
\tag{1}
\]

A0 is exactly
\[
\boxed{\eta_n\ge0.}
\tag{2}
\]

Define the normalized strong-margin deficit
\[
\boxed{
  d_n
  =
  {(-M_n)_+\over A_n}
  =
  \max\left(0,\frac12-{\lambda_n\over A_n}\right).
}
\tag{3}
\]

## Exact improvement theorem

Compact A1 is
\[
  M_n+\delta_n\ge0.
\]
Dividing by \(A_n>0\) gives the sharp condition
\[
\boxed{
  \eta_n\ge d_n.
}
\tag{4}
\]

Equivalently,
\[
\boxed{
  R_n(T_n)\le {1\over4}A_n-d_nA_n.
}
\tag{5}
\]

Thus the missing theorem is not merely A0.  It is an A0-improvement theorem
whose required strength is exactly the strong-margin deficit.

## Distinguished regimes

1. If \(d_n=0\), i.e.
   \[
     \lambda_n\ge\frac12A_n,
   \]
   then A0 is enough.

2. If
   \[
     \lambda_n\ge\frac14A_n,
   \]
   then \(d_n\le1/4\).  In that regime it is enough to prove the one-sided
   tail sign
   \[
     R_n(T_n)\le0.
   \]

3. If one only knows Li positivity,
   \[
     \lambda_n\ge0,
   \]
   then the worst-case deficit is \(d_n=1/2\), and A1 would require
   \[
     R_n(T_n)\le-{1\over4}A_n.
   \]
   Therefore Li positivity alone does not supply the compact A1 budget.

## Signed tail form

Using the tail identity from `150` and the cutoff-flow reductions,
\[
  R_n(T_n)
  =
  -\int_{T_n}^{\infty}
    E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du,
\]
with \(E(x)=\psi(x)-x\), the surplus is
\[
\boxed{
  \eta_n
  =
  {1\over4}
  +
  {1\over A_n}
  \int_{T_n}^{\infty}
    E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
}
\tag{6}
\]

Therefore the exact signed-tail improvement theorem is
\[
\boxed{
  \int_{T_n}^{\infty}
    E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  \ge
  \left(d_n-{1\over4}\right)A_n.
}
\tag{7}
\]

For \(d_n\le1/4\), the right side is nonpositive; for \(d_n>1/4\), it is
positive and demands genuine signed gain from the Chebyshev--Laguerre
tail.

## Relation to previous gates

Equation (4) is the normalized version of
\[
  \delta_n\ge -M_n
\]
from `238` and `240`.

Equation (7) is the tail-integral version of the diagonal comparison
\[
  [z^n]\Delta_{T_n}\ge -[z^n]\mathcal M
\]
from `241`.

The Loewner condition
\[
  \mathfrak Q^{\Delta,T_n}\succeq\mathfrak Q^{\mathcal M}_-
\]
from `243` is a finite-space strengthening of the same inequality.

## Status

Closed as the exact A0-improvement requirement.

A1 remains open.  A successful continuation must prove \(\eta_n\ge d_n\)
for all \(n\ge8\), or prove a stronger special case such as strong margin,
quarter margin plus nonpositive tail, Loewner negative-part domination, or
the direct compact inequality \(C_n(T_n)\ge0\).

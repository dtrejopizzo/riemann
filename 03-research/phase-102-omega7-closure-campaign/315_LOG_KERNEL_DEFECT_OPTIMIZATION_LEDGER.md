# Log-kernel defect optimization ledger

## Purpose

`312` gives the exact model coefficient
\[
  \kappa_\alpha
  =
  {1\over 2\pi}
  \int_{\mathbb R}
  \left(
    {2\over 1+u^2}
    -
    \alpha
    \left({2\sin(u/2)\over u}\right)^2
  \right)_+du
\]
for the canonical logarithmic kernel
\[
  L(e^{i\theta})=-\log|2\sin(\theta/2)|.
\]

This note records the threshold comparison with the Abel-defect budget.  It
shows that the pure logarithmic model leaves positive leading margin.  Thus
the obstruction in the Abel-to-Fejer subroute is not the log-kernel itself;
it is the possible Euler--Gamma remnant concentrated near moving Fejer
zeros.

## Defect budget

The Abel-defect route requires, for some \(0<\alpha<2\),
\[
\boxed{
  \int (P_{1-1/n}-\alpha F_n)_+\,d\nu_g
  \le
  b_\alpha\log n+O(1)
}
\tag{1}
\]
with
\[
\boxed{
  b_\alpha<1-{\alpha\over2}.
}
\tag{2}
\]

For the pure log-kernel model \(d\nu=L\,dm\), `312` gives
\[
  b_\alpha=\kappa_\alpha.
\]
Hence the model margin is
\[
\boxed{
  \mathfrak m(\alpha)=1-{\alpha\over2}-\kappa_\alpha.
}
\tag{3}
\]

If \(\mathfrak m(\alpha)>0\), then the pure log-kernel model is compatible
with the Abel-defect threshold at that \(\alpha\).

## Numerical calibration

Direct quadrature of the one-dimensional integral gives the following
values:

| \(\alpha\) | \(\kappa_\alpha\) | \(1-\alpha/2\) | margin |
|---:|---:|---:|---:|
| \(1/4\) | \(0.7500644314\) | \(0.8750000000\) | \(0.1249355686\) |
| \(1/2\) | \(0.5062427834\) | \(0.7500000000\) | \(0.2437572166\) |
| \(3/4\) | \(0.3520355633\) | \(0.6250000000\) | \(0.2729644367\) |
| \(1\) | \(0.2444561597\) | \(0.5000000000\) | \(0.2555438403\) |
| \(5/4\) | \(0.1634095077\) | \(0.3750000000\) | \(0.2115904923\) |
| \(3/2\) | \(0.1023118286\) | \(0.2500000000\) | \(0.1476881714\) |
| \(7/4\) | \(0.0588943939\) | \(0.1250000000\) | \(0.0661056061\) |
| \(19/10\) | \(0.0418477928\) | \(0.0500000000\) | \(0.0081522072\) |

The largest value in this coarse grid occurs near
\[
\boxed{
  \alpha={3\over4},
  \qquad
  \mathfrak m(\alpha)\approx0.2729644367.
}
\tag{4}
\]

The numerical table is not a closure proof.  Its role is to calibrate the
remaining constants and show that the model log-density is not already
fatal to the Abel-defect route.

## Consequence for a decomposed measure

Suppose a future construction gives
\[
  d\nu_g=aL\,dm+d\rho
\]
with \(0<a\le1\) and \(\rho\ge0\).  If
\[
\boxed{
  \int (P_{1-1/n}-\alpha F_n)_+\,d\rho
  \le
  e_\alpha\log n+O(1),
}
\tag{5}
\]
then the leading defect coefficient is bounded by
\[
  a\kappa_\alpha+e_\alpha.
\]

The Abel-defect threshold becomes
\[
\boxed{
  a\kappa_\alpha+e_\alpha<1-{\alpha\over2}.
}
\tag{6}
\]

At the calibrated point \(\alpha=3/4\), this sufficient condition is
\[
\boxed{
  e_{3/4}<0.625-a\,0.3520355633\ldots .
}
\tag{7}
\]

For the natural coefficient \(a=1\), the allowable remnant coefficient is
approximately
\[
\boxed{
  e_{3/4}<0.2729644367\ldots .
}
\tag{8}
\]

Thus the remaining quantitative target is not zero remnant.  A positive but
small enough remnant is compatible with the Abel-to-Fejer closure.

## Relation to the central-floor and Carleson gates

`297` records that the bad set may contain an unavoidable central
contribution when a lower log-density is present.  The present ledger says
that, after this unavoidable model contribution is accounted for, there is
still positive leading budget in the pure logarithmic case.

Therefore the live Abel-defect route is:

1. construct the positive increment measure \(\nu_g\);
2. split off its logarithmic component \(aL\,dm\);
3. prove a weighted bad-set or Carleson estimate for the remnant \(\rho\)
   with coefficient satisfying (6).

## Status

Closed as a model optimization ledger.

A1 remains open.  The Abel-to-Fejer route is not blocked by the canonical
logarithmic density; it is reduced to constructing the measure and
controlling the residual bad-set mass.

# D.94 — `T=log(5)/2` endpoint ledger

## Closed, directed components

1. The complete Fourier multiplier, with the `n=2,3,4` contacts included,
   satisfies `r_X(tau)>-8.315` globally and `r_X(tau)>0.22` for
   `|tau|>=150`.  This is certified by D.91.
2. The joint-multiplier prolate split is proved abstractly in D.89.
3. For the explicit low space formed by the first 170 normalized Legendre
   functions on the interval, the band concentration of the orthogonal
   complement is below `7.198e-7`.  The Bessel-majorant proof and directed
   evaluation are D.93.
4. Consequently the complete Weil form on that orthogonal complement has
   lower bound `0.2199938569`.  Finite-contact partial translations are never
   estimated separately.

## Corrected finite-block audit

The former Fourier selector used a 500-node spatial quadrature at frequencies
as large as 2000.  It aliases those frequencies, so the previously reported
`0.007` gap is withdrawn.

D.95 replaces it by the analytic Legendre antiderivative formula of D.145,
with no Fourier or cusp quadrature.  At dimensions 40 and 80 the anchored
lower model stabilizes at three small negative modes, approximately

`-3.87664e-6, -2.47822e-6, -1.18332e-6`.

This does not refute the exact form: D.96 evaluates the omitted positive gamma
tail on these modes and obtains respective lifts

`4.13042e-6, 2.56516e-6, 1.25012e-6`,

leaving positive floating margins `2.54e-7, 8.69e-8, 6.68e-8`.  The remaining
endpoint obligation is therefore a three-level directed capacity/Feshbach
certificate plus a directed congruence on its complement, not a Cholesky
certificate for the anchored lower model alone.

## Withdrawn routes

* The original `-0.158` value was caused by omitting non-aligned translated
  overlaps and is invalid.
* Discontinuous Galerkin and generic `QCP` norm bounds are rejected because
  incommensurable truncated translations move jumps and are non-compact.
* No negative endpoint claim and no complete row-(d) claim follows from the
  floating low-block calculation.

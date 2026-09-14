# Ihara prime-cycle dichotomy

## Proposed mechanism

Realize the Euler product as the Ihara/Fredholm determinant of a weighted
non-backtracking operator.  Then try to use a Bass identity to turn the
determinant into the determinant of a positive graph Laplacian, with the two
Tate modes as the only boundary defect.

## Proposition (mixed-cycle dichotomy)

Let `G` be a directed graph whose oriented edges carry prime colours.  Assume
that the logarithmic determinant of its weighted non-backtracking operator has
support only at prime powers: every primitive closed non-backtracking orbit is
monochromatic.  Then every strongly connected component containing a closed
orbit is monochromatic.  Consequently the recurrent part of the
non-backtracking operator is a direct sum over prime colours.

### Proof

Suppose a recurrent strongly connected component contains recurrent edges of
two colours `p != q`.  Choose closed non-backtracking orbits through edges of
each colour.  Strong connectivity supplies directed connecting paths in both
directions.  After cyclic reduction of the concatenation, one obtains a
closed reduced orbit containing both colours (if a connector cancels at an
endpoint, start farther inside the corresponding closed orbit).  Its primitive
root is again mixed-colour.  This contradicts the hypothesis.  Hence every
recurrent component is monochromatic.  Transient edges do not occur in a
closed orbit and do not contribute to the logarithmic determinant.  The
recurrent non-backtracking operator is therefore block diagonal by colour.
QED.

## Corollary for the global square

There are only two possibilities.

1. Prime colours interact in the recurrent graph.  Then the Ihara logarithm
   contains mixed primitive words and produces forbidden coefficients at
   composite norms having at least two prime factors.
2. The Euler support is exact.  Then the determinant-bearing operator splits
   by primes and has no cross-place covariance; a Bass determinant identity
   preserves that decomposition.

Thus an unsigned graph/Ihara realization cannot simultaneously reproduce the
von Mangoldt support and supply the cross-place Green transmission.  Cancelling
mixed cycles would require a graded/signed trace, whose positivity is a new
input rather than a consequence of the Bass Laplacian.

## Verdict

The non-backtracking/Ihara route is closed for ordinary positive graph
realizations.  The obstruction is algebraic and precedes convergence or
analytic continuation.

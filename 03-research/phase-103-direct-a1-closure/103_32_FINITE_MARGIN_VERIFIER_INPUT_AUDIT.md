# Finite \(9\le n\le149\) margin verifier: input audit

## Verdict

The existing `217` program is an exact **interval propagator**, not a
constant-enclosure generator.  It can certify a supplied list of rational
intervals, but it presently contains only

\[
 \gamma_0,\ldots,\gamma_7,qquad \zeta(2),\ldots,\zeta(8),
\]

as hard-coded inputs.  It therefore cannot be extended candidly to
\(9\le n\le149\) from the data currently in the repository.  The missing
objects are explicit, independently proved rational enclosures for

\[
 \gamma_8,\ldots,\gamma_{148},qquad
 \zeta(9),\ldots,\zeta(149),                                    \tag{1}
\]

together with an explicit provenance/bound for every endpoint.  No
floating-point values, diagnostic `zeta_tools.py` values, or unproved decimal
tables were promoted to a certificate here.

## 1. Exact finite reduction

For each fixed \(n\), the verifier's identities are algebraic:

\[
 q_r=\frac{(-1)^{r-1}\gamma_{r-1}}{(r-1)!},\qquad
 p_r=q_r-\frac1r\sum_{k=1}^{r-1}kp_kq_{r-k},                    \tag{2}
\]

\[
 \lambda_n^{\rm prime}
 =n\sum_{k=1}^n{n-1\choose k-1}p_k,                              \tag{3}
\]

\[
 A_n=1-\frac n2(\gamma_0+\log(4\pi))
 +\sum_{k=2}^n(-1)^k{n\choose k}(1-2^{-k})\zeta(k).             \tag{4}
\]

Consequently the proposed finite strong-margin check is exactly

\[
 M_n:=\lambda_n-\frac12A_n
=\lambda_n^{\rm prime}+\frac12A_n>0.                            \tag{5}
\]

For \(n\le149\), (2)--(5) require precisely the constants in (1), plus
the already present intervals for \(\gamma_0\) and \(\log(4\pi)\).  Once
those intervals are supplied, every operation in `217` is addition,
multiplication, and division by a nonzero integer; the existing `Fraction`
class is adequate for fully exact outward interval propagation.

This is a certificate for the strong margin, not by itself a direct
evaluation of the signed A1 integral.  Its stated use in phase 103 also
requires the separately declared A0 tail inequality.

## 2. Exact failure point in the present verifier

The array `gamma` in
`phase-102-omega7-closure-campaign/RH-MASTER-CONTEXT/tools/omega7_point4_interval_verify.py` has
eight entries, indexed 0 through 7.  Calling `prime_coeffs(9)` accesses
`gamma[8]` and raises an index error.  Similarly, `lambda_arch(9)` accesses
the absent key `zeta[9]`.  These are not numerical-precision issues: the
finite inputs do not exist in the checked-in certificate.

The only documented Euler--Maclaurin construction in
`OMEGA7_POINT4_FINITE_CERTIFICATE.md` is written for \(0\le j\le6\), with
eight Bernoulli corrections and \(N=256\).  It establishes neither a
remainder bound nor rational endpoints for \(j=8,\ldots,148\).  The later
addition of \(\gamma_7\) and \(\zeta(8)\) in `217` is likewise an endpoint
table, not a checked-in generator for the needed range.

## 3. What a valid extension must contain

A genuine extension can be built entirely with rational arithmetic, but it
must add the following auditable layer before invoking (2)--(5).

1. Choose explicit integers \(N,R,K\) for Euler--Maclaurin, Bernoulli
   correction order, and the rational logarithm series truncation.
2. Generate the integer derivative polynomials
   \(P_{j,q+1}=P'_{j,q}-(q+1)P_{j,q}\) through every needed
   \(j\le148\) and a stated remainder order.
3. Bound the Euler--Maclaurin remainder for every \(\gamma_j\) by an
   explicit rational expression, using rational enclosures for all occurring
   logarithms.  The bound must be strong enough after the binomial
   amplification in (3).
4. Enclose \(\zeta(k)\), \(9\le k\le149\), by positive partial sums and
   rational integral tails (or an explicitly bounded Euler--Maclaurin
   formula); include an independent rational enclosure of \(\pi\) wherever
   even values are derived from it.
5. Store the resulting intervals and a reproducible script which verifies
   their derivation, then run the existing fraction-only propagation and
   print the 141 lower endpoints of (5).

The binomial coefficients in (3) reach size comparable with \(2^{148}\).
Thus a few correct decimal digits for the Stieltjes constants are not enough:
the generator must select its precision from an explicit propagated error
budget.  This is a finite computational task, but its required input data and
remainder analysis have not yet been supplied.

## Status

No certificate for \(9\le n\le149\) is asserted.  The finite reduction is
exact and the blocker is confined to the missing rationally proved constant
enclosures (1), not to a zero computation or a conceptual ambiguity.

# D.227 — Correctly typed (200{:}400) band falsifier

## Question

D.222 certifies, for the (196)-dimensional safe source of D.219 and the
orthogonal primitive band

\[
 W_{260}=(V_{260}^{\rm prim})\ominus(V_{200}^{\rm prim}),
\]

the finite Green estimate

\[
 C_{260}E_{260}^{-1}C_{260}^*\leq0.09B.
\]

Would replacing (260) by (400) capture enough additional Green energy
to make the remaining scalar-gap estimate plausible?

## Correct typing

D.227 uses

\[
 W_{400}=(V_{400}^{\rm prim})\ominus(V_{200}^{\rm prim}).
\]

The two Tate equations and orthogonality to the complete primitive
(V_{200}) are imposed simultaneously.  Hence (W_{400}) lies in the
high block on which D.185 proves the (0.2199) gap.  This is the correct
trial space for D.210; unlike D.226, no endpoint-flat property is claimed.

## Numerical falsifier

The Gamma centre comes from the directed 3400-digit Gamma-400 cache.  Until
the directed contact cache is complete, the contact centre is assembled by
a polynomial-exact binary64 Gauss rule.  No radius or sign conclusion is
drawn from this calculation.

The centre calculation gives

\[
 \lambda_{\max}
 \left(B^{-1/2}C_{400}E_{400}^{-1}C_{400}^*B^{-1/2}\right)
 \approx0.0883559960.                                  \tag{0.1}
\]

The trial-band spectrum is numerically contained in

\[
 [2.98559929,8.92793904],
\]

and the Galerkin orthogonality residual is below (9\cdot10^{-16}).

Equation (0.1) is slightly below the already certified allowance (0.09)
at cutoff (260); the latter is an upper bound, so there is no conflict.
The point is route selection: enlarging the correctly typed band from
(260) to (400) does not produce a substantial new fraction of the
(0.7) budget.  It therefore cannot by itself repair the corrected
residual of D.223, whose centre remains far above the scalar target.

## Decision

An Arb rebuild of the full (196\times200) Green merely to sharpen
(0.09) toward (0.0884) is not presently justified.  The active route is
the exact flat/boundary decomposition of D.225:

* the two nearly null directions have squared principal cosines
  (0.99999187) and (0.99984342) with the endpoint-flat sector;
* the (120)-dimensional boundary channel is the complementary robust
  jet sector;
* D.208 can control the flat tail, whereas D.171--D.172 can control the
  non-flat boundary action with its endpoint cancellation retained.

## Classification

* construction and typing of (W_{400}): **ALGEBRAIC**;
* numbers in (0.1) and the displayed spectrum: **HEURISTIC / NUMERICAL
  FALSIFIER**;
* conclusion that no theorem is obtained from these numbers: **AUDIT
  DECISION**;
* D.222 finite (0.09) inequality: **CERTIFIED BY INTERVALS**;
* endpoint (T=\frac12\log6) and row D: **OPEN**.

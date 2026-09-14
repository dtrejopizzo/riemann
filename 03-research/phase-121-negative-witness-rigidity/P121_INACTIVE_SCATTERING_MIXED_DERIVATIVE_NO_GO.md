# Phase 121 -- inactive scattering has zero mixed source curvature

## Status

The consecutive-prime return theorem remains correct, but the scalar Green
identity of phase 120 cannot supply its source hypothesis.  This note proves
the obstruction exactly: relative Euler scattering has an additive Wigner
connection.  Opposite-prime return terms which appear in a state expansion
cancel identically in the complete `K^*QK-Q` expression.  Its mixed
derivative in two distinct Euler coordinates is zero for every source, not
the normalized return operator.

## 1. Deformed relative Euler factor

For `a>0`, `0<=r<1`, put

\[
 z_a(\tau)=e^{ia\tau},\qquad
 c_{a,r}(\tau)={1-rz_a(\tau)^{-1}\over1-rz_a(\tau)},
 \qquad C_{a,r}=M_{c_{a,r}}.                       \tag{1.1}
\]

The multiplier is unitary on the real line.  With `Q=-i d/dtau`, phase
120 gives

\[
 C_{a,r}^*QC_{a,r}-Q
 =a\{P_{a,r}-I\},                                  \tag{1.2}
\]

where

\[
 P_{a,r}=I+\sum_{j\ge1}r^j
             (M_{z_a^j}+M_{z_a^{-j}}).             \tag{1.3}
\]

In the physical variable the nonconstant terms in (1.3) are translations
by `+-ja`.

### Proposition 1.1 -- inactive connection vanishes after compression

If `a>2T`, then for every `0<=r<1`,

\[
 E_T^*(C_{a,r}^*QC_{a,r}-Q)E_T=0.                 \tag{1.4}
\]

#### Proof

Every translation in (1.3) has length at least `a>2T`, hence its
compression to `(-T,T)` is zero.  QED.

This is why arbitrary inactive relative factors may be inserted into the
phase-120 scalar scattering without changing the localized Green identity.

## 2. Exact zero mixed curvature

Let `(a,r)` and `(b,s)` be two Euler coordinates and let
`epsilon in {+1,-1}`.  Since all objects are scalar multipliers,

\[
 C_{a,r}C_{b,s}^{\epsilon}
 =C_{b,s}^{\epsilon}C_{a,r}.                       \tag{2.1}
\]

### Theorem 2.1 -- additive Wigner connection

One has

\[
\boxed{
 (C_{a,r}C_{b,s}^{\epsilon})^*Q
       (C_{a,r}C_{b,s}^{\epsilon})-Q
 =a(P_{a,r}-I)+\epsilon b(P_{b,s}-I).}             \tag{2.2}
\]

Consequently

\[
 \boxed{
 \partial_r\partial_s
 \bigl[(C_{a,r}C_{b,s}^{\epsilon})^*Q
       (C_{a,r}C_{b,s}^{\epsilon})-Q\bigr]=0.}     \tag{2.3}
\]

#### Proof

For a scalar unimodular multiplier `C=M_(e^(i phi))`, its Wigner
connection is multiplication by `phi'`.  The phase of a product is the sum
of the phases, while inversion changes its sign.  Equations (1.2) and
(2.1) therefore give (2.2); differentiating distinct parameters gives
(2.3).  QED.

## 3. Where the apparent return went

Expanding the state

\[
 C_{a,r}C_{b,s}^{-1}u
\]

to order `rs` produces compositions of translations by `a` and `-b`.
After window compression these contain

\[
                    PU_a(I-P)U_{-b}P=PU_{a-b}P,    \tag{3.1}
\]

the exact return of
`P121_INACTIVE_PRIME_PAIR_RETURN_RIGIDITY.md`.  But the quadratic Green
expression also differentiates the transport of `Q` and the second-order
normalization of the unitary factors.  The sum of all these terms is (2.3),
so the coefficient (3.1) cancels exactly.

This cancellation occurs before compression, before the Tate projection
and for every `u`.  First contact cannot undo it.  Extracting only (3.1)
from the scalar Green formula would therefore omit terms of the same order.

## 4. Consequence for the source search

The normalized consecutive-prime return is still a faithful terminal
observable, but it cannot be obtained by

1. inserting inactive scalar relative factors into `K_T`;
2. differentiating the zero-residual identity `K_T^*QK_T-Q`; or
3. keeping only the mixed state term of that differentiation.

Any valid source must be nonadditive before scalar supertrace.  In
particular it must retain a genuinely matrix-valued/root-valued operation
whose two orientations do not commute, and then derive its equality-state
law without replacing it by a positive bank.  This is consistent with the
rank-one Hankel root observable of phase 121 and explains why the scalar
determinant loses precisely the desired mixed coefficient.

The global square is not closed by this calculation.

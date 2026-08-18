# 114.a.119 — H7: one characteristic-zero pseudofinite bio for all odd moments

```
+------------------------------------------------------------------------+
| PRIMES      p_j == 2 modulo every small odd prime.                     |
| LIMIT       K=prod_U F_(p_j) has characteristic zero.                  |
| POWERS      x -> x^s is bijective on K for every fixed odd s.          |
| BIO         All transported additions and rational denominators coexist.|
| GAIN        Algebraic DEN-TRANS/evaluation compatibility is closed.     |
| LIMIT       K is infinite; finite entropy/RR dimension is still open.   |
+------------------------------------------------------------------------+
```

## 1. A simultaneous prime sequence

Let

\[
 M_j=\prod_{\substack{\ell\le 2j+1\\\ell\ {m odd\ prime}}}\ell.      \tag{1.1}
\]

By Dirichlet's theorem, because `gcd(2,M_j)=1`, there are infinitely many
primes congruent to `2 mod M_j`.  Choose inductively an increasing sequence

\[
 p_j\equiv2\pmod{M_j}.                                                  \tag{1.2}
\]

For every fixed odd positive integer `s`, all prime divisors of `s` occur in
`M_j` for large `j`.  Equation (1.2) then gives

\[
 \gcd(s,p_j-1)=1                                                        \tag{1.3}
\]

eventually.  Hence `x -> x^s` is a permutation of `F_(p_j)` for all
sufficiently large `j`.

## 2. The characteristic-zero ultraproduct

Fix a nonprincipal ultrafilter `U` on the positive integers and put

\[
 K=\prod_j\mathbb F_{p_j}/\mathcal U.                                  \tag{2.1}
\]

Since `p_j` tends to infinity, Łoś's theorem implies that `K` has
characteristic zero.  Thus the prime field of `K` contains a canonical copy
of `Q`; every nonzero rational denominator is invertible.

For a fixed odd `s`, (1.3) and Łoś's theorem also imply that

\[
 P_s:K\longrightarrow K,\qquad x\longmapsto x^s                       \tag{2.2}
\]

is a multiplicative bijection.  Let `T_s=P_s^(-1)` and transport addition:

\[
 x+_{(s)}y=P_s(T_s(x)+T_s(y)).                                         \tag{2.3}
\]

Then `(K,+_(s),multiplication)` is a field, and all these field laws share
the same multiplication and unary scalar action.

## 3. One compatible bio target

Apply the homogeneous-endomorphism construction of `a49` to each field law
(2.3), restore the involution by the opposite-product construction, and take
the product over all positive odd `s`.  Denote the resulting commutative
involutive bio by `D_U`.

### Theorem 3.1 (universal odd-moment target)

There is one bio map from the full signed Haran plane to `D_U` such that its
`s`-coordinate evaluates

\[
 i_1(a)i_2(b)\longmapsto a b^s                                        \tag{3.1}
\]

for every `a,b in Q` and every positive odd `s`.  All rational denominators,
all scalar trees and all finite odd-moment truncations are defined in this
same target.  Truncation from a larger finite exponent set to a smaller one
is literal coordinate projection.

### Proof

For each `s`, the two regular field bios agree on multiplication and unary
scalars, so `a49` gives the full-plane map.  Products of commutative
involutive bios retain the maps coordinatewise.  Characteristic zero makes
every rational scalar available, and coordinate projections commute with
all operations.  QED.

Thus the changing-denominator obstruction of `a57` disappears at the level
of algebraic evaluation: no old positive characteristic is retained, and no
denominator ever becomes zero.

## 4. Why this does not yet define the desired dimension

The target `K` is infinite.  Raw image cardinality is therefore not the
finite normalized invariant used in `a33`--`a56`.  Moreover, a fixed finite
set of rational code sections has pseudofinite counting dimension zero in
`K`: its componentwise cardinalities stay bounded while `p_j` tends to
infinity.

The bounded interpolation surjectivity of `a55` also does not transfer to a
fixed standard divisor in `K`.  Its centered lifts use coefficients and
denominators depending on `p_j`; their ultraproduct is an internal
nonstandard section, not one rational section of the original `H^0(D)`.

Therefore the following extra theorem is required:

> **H7-PF-DIM.** Construct a canonical height/Loeb or internal asymptotic
> dimension on images of genuine bounded section systems in `D_U`, prove the
> calibrated coefficient, and show restriction/exact-sequence additivity.

Without H7-PF-DIM, the ultraproduct closes algebraic DEN-TRANS but not
H7-SEL-RR/EXACT, the gauge, row A or RH.

## 5. Verification scope

`114_a_119_h7_pseudofinite_bio_verify.py` constructs initial terms of (1.2),
checks simultaneous power permutations and denominator invertibility, and
checks transported field laws in finite components.  Characteristic zero
and the all-odd statement are the exact ultraproduct argument above.

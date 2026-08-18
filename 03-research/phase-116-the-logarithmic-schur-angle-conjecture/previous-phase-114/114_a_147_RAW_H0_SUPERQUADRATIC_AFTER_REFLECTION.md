# 114.a.147 — Raw bounded `H^0` stays superquadratic after reflection

## 1. Statement

Let `Y^locreg` be the supportwise regular pro-square.  At bidegree

\[
 D_d=2d\,e_{2,1}+d\,e_{q,2},\qquad q\ge3,
\]

consider the complete dyadic averaging tree with `N=2^d` leaves.  Fill its
leaves with a multiset of the `Q=q^d` positive sections `k/Q`, `1<=k<=Q`.
The resulting scalar section is

\[
 S_d(\nu)=4^{-d}\sum_{k=1}^Q\nu_k\,i_2(k/Q),
 \qquad \nu_k\ge0,\quad \sum_k\nu_k=N.
\]

### Theorem 1.1

Every `S_d(nu)` is a bounded scalar pro-section on `Y^locreg`, distinct
multisets give distinct sections, and

\[
 \log\#H^0_{\rm bd}(Y^{\rm locreg},D_d)
 \ge (2^d-1)\log2.
\]

In particular the raw cardinality of all bounded scalar sections has no
surface-type upper bound `O(d^2)`.

## 2. Proof

The averaging row and column `(1/2,1/2)` have Euclidean norm `1/sqrt(2)`.
Every leaf has absolute value at most one.  The finite denominators are
exactly `2^(2d)` and `q^d`.  Hence all trees are bounded sections on every
literal chart.

Here is the separation argument, including the point needed by the regular
reflection.  For every `u>0`, transport the ordinary addition of `R` through

\[
 T_u(x)=\mathrm{sgn}(x)|x|^{1/u}.
\]

The integer of the transported field is then
`i_{2,u}(n)=sgn(n)|n|^u`.  The ordinary and transported field bios map to
the commutative involutive homogeneous-endomorphism bio

\[
 \mathcal D=\mathrm{End}_{\mathbb R^\times\text{-Set}}(\mathbb R)
 \times
 \mathrm{End}_{\mathbb R^\times\text{-Set}}(\mathbb R)^{op}.
\]

Consequently its scalar shadow sends a Laurent label `[r]` to `r^u`.
For two different multisets the difference is a nonzero finite exponential
polynomial

\[
 f(u)=\sum_{k=1}^{Q}(\nu_k-\nu'_k)(k/Q)^u.
\]

Distinct positive exponentials are linearly independent (differentiate at
one point and use the Vandermonde determinant), so `f(u) != 0` for some
`u>0`.  The corresponding map to `D` separates the two trees.

Every nonzero integer acts on every operation set of `D` by pointwise scalar
multiplication on real-valued homogeneous maps (and componentwise on the
opposite factor); this action is injective.  Moreover the integers in
`{2,q}` act by units, with inverses `1/2` and `1/q`.  Thus `D` is a
`Z`-regular target and the separating map exists on every localized chart
of the cofinal subsystem supporting `{2,q}`.  By the universal property of
the supportwise reflector it factors through each reflected chart.
Therefore reflection does not identify two different leaf multisets.

The number of multisets is

\[
 {N+Q-1\choose N}.
\]

Since `Q>=N`,

\[
 {N+Q-1\choose N}\ge {2N-1\choose N}\ge2^{N-1}.
\]

Taking logarithms and substituting `N=2^d` proves the theorem.  QED.

## 3. Consequence

The selected finite images used by the calibrated construction cannot be
reinterpreted as the full bounded-section cardinality.  This is not merely
an absent upper-bound proof: the required upper bound is false.

Any intrinsic unpolarized RR theory on this carrier must therefore use a
different dimension functor (for example a proved minimal-generator or
derived Euler-characteristic invariant), a geometric complexity quotient,
or a different local gauge.  Raw `log #H^0_bd` is closed negatively.

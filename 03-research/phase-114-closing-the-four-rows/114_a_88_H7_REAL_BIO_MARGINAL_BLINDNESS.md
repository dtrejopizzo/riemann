# 114.a.88 — H7: the unary real-bio family forgets bilateral leaf matching

```
+-------------------------------------------------------------------------+
| DATUM       A scalar operation is (F,G,sigma,epsilon).                  |
| LEFT BIO    The input column duplicates x at every G-leaf; after sigma, |
|             F receives only its signed leaf list.                       |
| RIGHT BIO   The involutive factor does the same with F and G reversed.  |
| BLINDNESS   Pairings inside equal-sign fibers of sigma are invisible.    |
| MINIMAL     Three leaves already admit distinct incidence cores with the |
|             same two signed marginals.                                  |
| CONSEQUENCE H7-REAL-RES requires H7-MARGINAL-COMPLETE; it is not supplied |
|             by the homogeneous representation alone.                    |
+-------------------------------------------------------------------------+
```

## 1. Exact factorization of unary evaluation

Write a scalar representative of the arithmetic plane as Haran's datum

\[
 a=(F,G,\sigma,\varepsilon),                                         \tag{1.1}
\]

where `sigma` bijects the leaves of the two rooted colored trees and
`epsilon` labels the matched strands by signs.  In a regular ring-bio
representation, the transpose of an addition row is its diagonal column.
Consequently every column tree sends a scalar input `x` to one copy of `x`
at every leaf, independently of the internal shape of that column tree.

After applying `sigma` and the signs, the row tree `F` therefore receives
only the sign-labelled list on its own leaves.  The detailed partner in
`G` of a fixed `F`-leaf does not enter.  In the opposite factor the same
argument exchanges `F` and `G`.

Define the **signed marginal datum**

\[
 M(a)=\bigl((F,\varepsilon_F),(G,\varepsilon_G)\bigr),                \tag{1.2}
\]

where `epsilon_F` is the sign on each `F`-leaf and `epsilon_G` is its
transport through `sigma`.  Then every `rho_u` of `a87` factors as

\[
 A_1\longrightarrow M(A_1)\longrightarrow\mathbb R\times\mathbb R. \tag{1.3}
\]

### Proposition 1.1 (marginal blindness)

If two representatives have the same two signed marginal trees, all their
homogeneous unary evaluations `rho_u` agree for every `u>0`.

### Proof

The first coordinate is obtained by duplicating the scalar input, applying
the `F`-leaf signs, and evaluating the row tree `F`; it depends only on
`(F,epsilon_F)`.  The involutive-opposite coordinate applies the identical
calculation to `(G,epsilon_G)`.  Neither calculation retains which equal-sign
leaf of one tree was paired with which equal-sign leaf of the other.  QED.

## 2. A three-leaf ambiguity already exists before quotienting

Let both `F` and `G` have a root with two children: one leaf and one binary
subtree.  Their leaf-parent block sizes are therefore `(1,2)`, so the two
blocks cannot be exchanged by a rooted-tree automorphism.

With all signs positive, compare two leaf bijections.  Their parent-block
incidence matrices are

\[
 B_0=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad
 B_1=\begin{pmatrix}0&1\\1&1\end{pmatrix}.                           \tag{2.1}
\]

They have the same row sums `(1,2)`, column sums `(1,2)`, trees and signs,
but different incidence cores.  Since block sizes distinguish both rows and
columns, no tree automorphism changes `B_0` into `B_1`.  Proposition 1.1
nevertheless gives identical `rho_u` values for every `u`.

This is **not** asserted to be a pair of distinct classes in the full Haran
quotient: cancellation can be inserted contextually, and cut-commutativity
may relate presentations that are not visibly isomorphic.  The example
proves blindness of the proposed invariant, not nonfaithfulness of the
quotient map.

## 3. The exact new requirement

For the characteristic-zero route of `a87` to work, one must prove

> **H7-MARGINAL-COMPLETE.** Whenever two scalar Haran classes have the same
> values under every signed left/right marginal evaluation, they are equal
> in the full cancellation quotient.

Equivalently, one may enrich the target by a genuinely bilateral invariant
that records leaf-pair correlations and prove that the enriched product map
is injective.  The multivariable Hessian invariant of `a74` records such
correlations only in the read-once one-sided sector; it does not establish
this scalar bilateral statement.

Thus `a87` remains a correct sufficient theorem, but the real family already
constructed does not by itself prove its H7-REAL-RES hypothesis.  The live
alternatives are now precise:

1. prove H7-MARGINAL-COMPLETE from cancellation and cut-commutativity;
2. construct a correlation-sensitive characteristic-zero bio target; or
3. return to direct component injectivity in the macro graph.

Corrected `a89` proves more cancellation, but less marginal invariance, on
every single two-level incidence grid: both ruling contrast families make
the quotient depend only on total signed mass.  Thus the three-leaf ambiguity
above is zero, while ordinary row/column marginals are not quotient invariants.
Nested cut-changing contexts remain outside that theorem.  H7-REAL-RES,
H7-NESTED-CONTEXT-SAT, H7-PRIME-REG and row A remain open.

## 4. Verification scope

`114_a_88_h7_real_bio_marginal_blindness_verify.py` checks the primary tree
and involution formulas, the two nonisomorphic three-leaf incidence cores,
and exact marginal blindness in ordinary and finite twisted-field bios.
It does not assert that the two representatives survive as distinct quotient
classes.

Primary source: Haran, [*Geometry over F1*](https://arxiv.org/abs/1709.05831),
equations (10.9)--(10.21).

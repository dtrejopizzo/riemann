# 114.a.103 — H7: every cross-commutativity defect is an explicit nontameness witness

```
+-------------------------------------------------------------------------+
| DEFECT      X(a,b)=a o b versus (sum_Y b) o (sum_I a),                 |
|             a:Y<-1 a column, b:1<-I a row.                             |
| SOURCE      In every commutative F-ring, all scalar sandwiches of the   |
|             two sides agree.                                           |
| DICHOTOMY   Equality is cross-commutativity; inequality is an explicit   |
|             witness that the F-ring is not tame.                        |
| FIRST TEST  For the plane, use the mixed colors a=delta_1^t,b=delta_2.  |
| OPEN        Decide equality after the full integer cancellation quotient.|
+-------------------------------------------------------------------------+
```

## 1. The canonical pair

Let `A` be a commutative Haran `F`-ring.  For

\[
 a\in A_{Y,[1]},\qquad b\in A_{[1],I},
\]

put

\[
 L(a,b)=a\circ b,\qquad
 R(a,b)=\left(\bigoplus_Y b\right)
        \circ\left(\bigoplus_I a\right)\in A_{Y,I}.          \tag{1.1}
\]

Their equality is exactly Haran's definition of `cross`-commutativity
(`times`-commutativity in the source notation).

### Theorem 1.1 (automatic sandwich blindness)

For every row `u in A_(1,Y)` and every column `v in A_(I,1)`, commutativity
gives

\[
 u\circ L(a,b)\circ v=u\circ R(a,b)\circ v.                \tag{1.2}
\]

### Proof

Associativity writes the left side as

\[
 u\circ a\circ b\circ v.
\]

Haran's commutativity identity, applied to the middle operation and the
row-column pair `b,v`, is precisely

\[
 u\circ a\circ b\circ v
 =u\circ\left(\bigoplus_Y b\right)
       \circ\left(\bigoplus_I a\right)\circ v.
\]

This is (1.2).  It is also the calculation printed immediately after
Definition 1.4.3 in the long source.  QED.

### Corollary 1.2 (source-level tame test)

If `L(a,b) != R(a,b)` for one pair, then `A` is not tame.  Equivalently,

\[
 \text{commutative}+\text{tame}
 \Longrightarrow\text{cross-commutative}.                    \tag{1.3}
\]

### Proof

The distinct pair has identical complete scalar-sandwich signature by
Theorem 1.1, contradicting the definition of tameness.  QED.

This is stronger than merely observing that the matrix-coefficient map is
noninjective: (1.2) includes every scalar row and column in `A`, not only
the structural coordinate probes.

## 2. The first mixed arithmetic-plane defect

Let `A` now be the signed arithmetic plane and let `delta_1,delta_2` be its
two binary addition rows.  Take

\[
 a=\delta_1^t\in A_{[2],[1]},\qquad
 b=\delta_2\in A_{[1],[2]}.                                  \tag{2.1}
\]

The two operations are

\[
 D_{12}^{\rm centre}=\delta_1^t\circ\delta_2,                 \tag{2.2}
\]

and

\[
 D_{12}^{\rm grid}
 = (\delta_2\oplus\delta_2)
   \circ(\delta_1^t\oplus\delta_1^t).                         \tag{2.3}
\]

In the graph presentation, (2.2) is a mixed merge-then-split centre and
(2.3) is the Cartesian `2 by 2` grid.  Every one-input/one-output coefficient
is the same, and Theorem 1.1 says much more: every scalar sandwich is the
same.

Therefore exactly one of the following holds:

1. `D_centre != D_grid` in the full signed cancellation quotient.  Then
   this pair explicitly disproves H7-TAME-PLANE.
2. `D_centre = D_grid`.  Then this first cross defect vanishes, but tameness
   still requires equality of (1.1) for every `a,b` and separation of all
   other pairs.

The transpose gives the opposite-color version, so it is not an independent
test.

Same-color versions vanish because each individual ring `F`-ring is already
totally commutative.  Hence (2.2)--(2.3) is the smallest generator-level
mixed test.

## 3. What the existing results do and do not decide

Haran proves that the commutative positive plane does not collapse to its
diagonal (`delta_1 != delta_2`).  That is not the inequality in (2.2): the
two addition rows are separated by scalar evaluations, whereas the cross
defect is sandwich-invisible by construction.

The `K2,2` result of `a81` also cannot be reused as a proof of inequality:
that signed candidate is a contextual image of cancellation and is zero.
Likewise, equality of the two matrix shadows proves only their common fold,
not equality in the nonmatrix plane.

The exact new gate is

> **H7-XDEF-12.** Decide whether (2.2) and (2.3) are equal in
> `G(Z) tensor_(F{+-1}) G(Z)` after all commutativity and cancellation
> contexts.

A positive-graph separation alone would not suffice unless it is shown to
survive the signed cancellation quotient.  Conversely, proving equality
only closes this first necessary test; it does not establish tameness.

Thus `a103` does not prove or refute H7-TAME-PLANE.  It replaces an
unstructured all-pairs search by the canonical first obstruction forced by
Haran's own implication (1.3).  H7-AUG-FLAT, H7-TAME-PLANE,
H7-PRIME-REG and row A remain open.

## 4. Verification scope

`114_a_103_h7_cross_defect_tameness_verify.py` exhausts finite
sandwich-signature systems to verify the logical implication that any
surviving cross defect is nontame, checks the centre/grid matrix shadows,
and enforces the signed-quotient/open-scope warnings.  The general identity
is proved above directly from the displayed source axiom; the finite code is
regression evidence only and does not decide H7-XDEF-12.

Primary source: Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Definitions 1.3.1 and 1.4.3 and the implication immediately following them.

**Later resolution (`a104`).**  H7-XDEF-12 is negative: Haran's
commutative infinitesimal target `F(Z) Pi N` separates the centre from the
grid by a nonzero nine-coordinate element of `N_(2,2)`.  Consequently
H7-TAME-PLANE is false.  The open statements above record the state at
`a103`; they are superseded by `a104`.

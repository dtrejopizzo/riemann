# 114.a.90 — H7: laminar nested cut contexts are saturated at every depth

```
+-------------------------------------------------------------------------+
| SECTOR      Nested bilateral cuts are laminar; no contraction reuses a   |
|             boundary strand in two incomparable blocks.                  |
| LOCAL       Every fixed two-level grid has the total-mass quotient a89.   |
| TRANSPORT   Each surviving strand fiber crosses adjacent cut charts       |
|             individually, with coefficient +1 or -1.                     |
| MATRIX      The global relation matrix is a direct sum of oriented graph  |
|             incidence matrices.                                          |
| RESULT      All Smith factors are 1; every prime is regular in this sector.|
| OPEN        Nonlaminar reuse/contraction and aggregated fiber maps.        |
+-------------------------------------------------------------------------+
```

## 1. Laminar cut systems

Fix a bilateral network and a finite family `C` of displayed cuts.  Call the
family **laminar** when any two cut blocks are disjoint or one contains the
other.  Require in addition that every boundary strand belongs to one child
block at each refinement: no contraction duplicates the same strand into
two incomparable blocks.

The containment poset of the nonempty blocks is then a forest.  A strand
determines one chain in that forest.  Passing between two adjacent cut
charts transports that strand along a unique edge; it is never summed with
a second fiber before the next chart.

This includes arbitrary depth, arbitrary vertex arity, both tree sides and
arbitrary signs.  It excludes precisely repeated-variable/contraction data
whose occurrences meet again across incomparable cuts.

## 2. Local reduction and fiberwise gluing

At each adjacent pair of cut levels, collect the signed strands into its
two-level incidence grid.  Corrected `a89` identifies the full local
cancellation quotient with the total signed mass in each retained boundary
fiber.  Because the cut system is laminar and has no reuse, a fiber on one
chart is identified with exactly one fiber on an adjacent chart.

Choose an orientation of the chart-overlap graph.  For one fixed strand
fiber, the gluing relations therefore have columns

\[
 e_{t(h)}-e_{s(h)}                                                     \tag{2.1}
\]

for overlap edges `h`.  This is the oriented incidence matrix of a finite
graph.  Different strand fibers give a direct sum of such matrices; signs
only reverse column orientations.

The crucial conclusion is **H7-FIBER-RETENTION** in this sector: no row is
replaced by the sum of all incident rows.  The latter replacement would
produce the Laplacian obstruction of `a83`; laminar unique transport keeps
the individual incidence columns.

## 3. Saturation theorem

### Lemma 3.1 (incidence cokernel)

For any finite graph `G`, the image of its oriented incidence map

\[
 \partial:\mathbb Z^{E(G)}\longrightarrow\mathbb Z^{V(G)}             \tag{3.1}
\]

is saturated.  Its cokernel is `Z^{pi_0(G)}`.

### Proof

Choose a spanning forest.  In each connected component, successively use
the leaf edge of the forest to eliminate the leaf coordinate.  Every pivot
is `+1` or `-1`; the remaining coordinate is the component total.  Nonforest
edges add relations already in the zero-total lattice.  Hence the Smith
normal form has `|V|-pi_0(G)` nonzero entries, all equal to one.  QED.

### Theorem 3.2 (laminar nested saturation)

The cancellation relation lattice of every finite laminar, no-reuse nested
cut subsystem is saturated at every prime.

### Proof

Apply the complete fixed-grid reduction of `a89` at each adjacent cut pair.
Section 2 decomposes the remaining gluing relations as a direct sum, over
individual strand fibers, of maps (3.1).  Lemma 3.1 makes each summand's
cokernel free abelian; a direct sum of free abelian groups is free.  Thus the
whole relation subgroup is pure.  Equivalently, `pF~pG` implies `F~G` inside
this subsystem for every prime `p`.  QED.

### Corollary 3.3

H7-PRIME-REG holds on arbitrary-depth bilateral read-once data under every
laminar sequence of cut changes.  This extends the one-sided Hessian sector
of `a74`--`a75` across both tree sides and across all laminar cut charts.

## 4. Exact residual shape

A counterexample not already excluded must violate fiberwise incidence.  It
must contain at least one of:

1. a contraction/repeated occurrence feeding one strand into incomparable
   cut blocks;
2. a nonlaminar overlap in which two blocks intersect without containment;
3. a normalization that retains only an aggregate of several fiber rows.

In matrix language, the first possible danger is a weighted or aggregated
overlap map rather than an oriented incidence column.  `a83` shows why this
distinction is exact: replacing individual incidence data by a cycle
Laplacian creates `Z/n` Smith torsion.

The next gate is therefore

> **H7-NONLAMINAR-FIBER.** Prove that Haran's full sandwich contexts can be
> refined until individual fibers survive even with contraction/reuse, or
> exhibit an actual weighted/aggregated overlap with a nonunit Smith factor.

Theorem 3.2 does not assert this refinement.  H7-NONLAMINAR-FIBER,
H7-PRIME-REG and row A remain open.

## 5. Verification scope

`114_a_90_h7_laminar_nested_verify.py` verifies the cut/cancellation source
markers; exhausts all simple overlap graphs through five vertices; computes
their incidence Smith factors by exact integer minors/normal reduction; and
checks direct sums and sign reversals.  It also contrasts incidence with the
cycle-Laplacian obstruction.  The uniform result is Lemma 3.1 together with
the unique-fiber argument in Section 2.

Primary sources: Haran, [*Geometry over F1*](https://arxiv.org/abs/1709.05831),
equations (10.16)--(10.21); Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Appendix A.2.9.

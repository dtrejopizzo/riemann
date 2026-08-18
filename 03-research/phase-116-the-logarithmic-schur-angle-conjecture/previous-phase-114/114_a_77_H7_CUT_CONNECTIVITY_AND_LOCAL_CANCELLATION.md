# 114.a.77 — H7: fixed-network cuts and isolated cancellation bundles are pure

> **Scope correction (`a_81`).** `a_79` closes the topology-changing overlap
> only for visible cancellation sites on a fixed incidence presentation.
> General multiplication/contraction contexts can create macro cancellation
> relations, such as the locally irreducible but contextually zero `K2,2`
> grid.  Full contextual confluence and saturation remain open.

```
+-------------------------------------------------------------------------+
| NETWORK     Glue the two boundary trees and orient every strand from an |
|             input root toward the output root.                          |
| CUTS        Admissible cuts are boundaries of order ideals in the finite |
|             reachability poset of this directed acyclic network.        |
| CONNECTED   All cuts of one fixed network are joined by elementary       |
|             consistent-commutativity moves.                             |
| LOCAL       Opposite signs in one fixed parallel bundle have the unique  |
|             normal form given by their integral net multiplicity.       |
| PURE        Multiplication by every prime cancels on that local normal    |
|             form.                                                        |
| RESIDUAL    Only cancellation followed by pruning/contraction that       |
|             changes the network core can still obstruct PRIME-REG.       |
+-------------------------------------------------------------------------+
```

## 1. The expanded directed network

For bilateral data

\[
 F=([F_1];[\bar F_x]_{x\in X};\sigma;\mu),                            \tag{1.1}
\]

reverse every input tree `bar F_x`, keep the output tree `F_1` directed
toward its root, and glue the paired leaves using `sigma`.  After subdividing
at a glued leaf this gives a finite directed network `N(F)` from the roots
indexed by `X` to the output root.  It is acyclic: height decreases toward
the root on `F_1`, height increases away from the root on every reversed
input tree, and a directed path crosses the glued boundary only from the
input side to the output side.

The presentation in Haran (10.17), equivalently (8.3.48)/(8.3.50), moves the
chosen boundary through a multiplication/contraction rectangle.  It changes
the factorization of a fixed expanded network, not that network itself.

## 2. All cuts of a fixed network are connected

Let `P_N` be the reachability poset of the internal vertices of a finite
directed acyclic network `N`: `v <= w` when a directed path goes from `v` to
`w`.  A cut separating all inputs from the output determines the set `I` of
vertices lying on the input side.  This set is an order ideal.  Conversely,
the oriented edge boundary of an order ideal is an admissible cut.  Empty
terminal conventions cause no difficulty and may be fixed once at the
external roots.

### Theorem 2.1 (cut connectivity)

Any two admissible cuts of a fixed expanded network are connected by a
finite chain of elementary consistent-commutativity moves.

### Proof

It is enough to connect their order ideals `I,J`.  Remove maximal elements
of `I \ J` one at a time; the result remains an order ideal.  Then add minimal
elements of `J \ I` one at a time; again every intermediate set is an order
ideal.  Thus the Hasse graph of the finite distributive lattice `J(P_N)` is
connected.

Crossing one vertex changes the cut by moving one multiplication past one
contraction.  This is Haran's right-linearity pair (8.3.48); (8.3.50) is its
contracted/context form.  Hence every edge of the Hasse graph is an allowed
consistent-commutativity move.  QED.

This proves that a *cut choice on one fixed network* contributes no new
normal-form ambiguity.  It does not say that cancellation cannot change the
network.

## 3. A fixed cancellation bundle is prime-pure

Haran's cancellation picture (10.16) removes a `+1,-1` pair of parallel
strands between vertices bearing the same ruling label.  Freeze the two
endpoints and everything outside this bundle.  If the bundle contains `a`
positive and `b` negative strands, every cancellation sequence ends at

\[
 (a-b)_+\text{ positive strands},\qquad
 (b-a)_+\text{ negative strands}.                                    \tag{3.1}
\]

Indeed each move replaces `(a,b)` by `(a-1,b-1)`.  The difference `a-b` is
invariant and the terminal condition is `min(a,b)=0`, which uniquely gives
(3.1).

### Corollary 3.1 (local prime purity)

For a fixed parallel bundle and a prime `p`, equality after `p`-fold
replication implies equality before replication.

### Proof

The normal form is the integer `a-b`.  Equality after replication is
`p(a-b)=p(c-d)` in `Z`; cancellation of the nonzero integer `p` gives
`a-b=c-d`.  Formula (3.1) then gives the same bundle normal form.  QED.

Thus neither changing the cut of a fixed network nor cancellation confined
to a fixed pair of endpoints can create prime torsion.

## 4. Exact residual gate

The remaining critical pairs are those in which cancellation changes the
available tree reductions.  Removing a signed pair can make an internal
vertex unary or empty; subsequent `1`-reduction can splice two portions of
the network, and `lhd`-reduction can then contract newly adjacent vertices.
That may create a new parallel bundle at different endpoints.  The local
integer invariant of Section 3 does not compare two such changing cores.

Replace H7-RF-BICUT by the sharper statement

> **H7-CORE-CONFLUENCE.** On every arity and affine pro-chart, the rewrite
> system consisting of opposite-pair cancellation, empty-branch pruning,
> `1`-reduction and alternating reduction has a canonical reduced directed
> network core; moreover `p`-fold replication is injective on those cores.

Theorem 2.1 removes the independent cut-choice clause: all cuts of any one
core are already connected.  Corollary 3.1 removes isolated parallel
bundles.  Consequently any counterexample to H7-CANCEL-PURE must use an
overlap between cancellation and a topology-changing pruning/contraction.

No confluence theorem for those overlaps is asserted here.  Therefore
H7-CANCEL-PURE, H7-PRIME-REG and the completed lattice remain open.

## 5. Verification scope

`114_a_77_h7_cut_and_local_bundle_verify.py` exhausts every naturally
topologically ordered DAG through six vertices, verifies connectivity of its
order-ideal cut graph, exhausts all cancellation paths in parallel bundles
through multiplicity eight, and checks local prime-root closure.  The
uniform proofs are Theorem 2.1 and Corollary 3.1; the computation is a
regression check, not their logical basis.

Primary sources: Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Section 13.2 and equations (8.3.48)/(8.3.50); and [*Geometry over F1*](https://arxiv.org/abs/1709.05831),
equations (10.16)--(10.18).

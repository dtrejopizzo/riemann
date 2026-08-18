# 114.a.82 — H7: every separable rectangular macro-context is saturated

```
+-------------------------------------------------------------------------+
| CONTEXT     Insert x_0 or x_1 through independent corollas.              |
| INDEX       Boundary strands are indexed by a finite Cartesian product.  |
| RELATIONS   Cancellation acts along coordinate fibers by e_u-e_v.        |
| MATRIX      These rows form an oriented graph-incidence matrix.           |
| SMITH       Every nonzero Smith invariant is 1; the relation subgroup is  |
|             saturated for every prime.                                   |
| INCLUDES    K2,2 and arbitrary finite rectangular depth/arity.             |
| OPEN        Nonseparable contractions which sum or overlap distinct fibers.|
+-------------------------------------------------------------------------+
```

## 1. Rectangular context family

Start with one of Haran's cancellation generators `x_epsilon`, whose two
signed branches are indexed by `A_0={0,1}`.  Insert finite corollas with
index sets `A_1,...,A_d` independently through multiplication and
contraction, without identifying two different coordinate fibers.  Formula
(10.19) indexes the resulting boundary by

\[
 V=A_0\times A_1\times\cdots\times A_d.                              \tag{1.1}
\]

Consistent commutativity changes the order in which the coordinates are
displayed but not the Cartesian indexing.  The `K2,2` datum of `a_81` is the
case `d=1`, `|A_0|=|A_1|=2`.

Allowing cancellation in any binary coordinate direction gives relations

\[
 e_{(a_0,\ldots,0,\ldots,a_d)}
 -e_{(a_0,\ldots,1,\ldots,a_d)}.                                    \tag{1.2}
\]

More general finite corollas decompose into a spanning tree of binary
differences in that coordinate, so the same relation subgroup is obtained.

## 2. Incidence-matrix theorem

Let `G` be the graph with vertex set `V` and one oriented edge for every
relation (1.2).  Its boundary map is

\[
 \partial:\mathbb Z^{E(G)}\longrightarrow\mathbb Z^{V(G)},
 \qquad \partial(u\to v)=e_v-e_u.                                   \tag{2.1}
\]

### Theorem 2.1 (rectangular saturation)

The subgroup `im(partial)` is saturated in `Z^V`.  Equivalently every
nonzero Smith invariant of the rectangular macro-context relation matrix is
`1`.  Hence its quotient has no `p`-torsion for any prime.

### Proof

For each connected component of `G`, choose a spanning tree and a root.
The differences `e_v-e_root` along tree paths form a basis of the subgroup

\[
 \{(n_v):\sum_{v\text{ in the component}}n_v=0\}.                    \tag{2.2}
\]

All graph-edge differences lie in this subgroup, and the spanning-tree
edges generate it.  The quotient on one component is therefore `Z`, via the
coordinate sum.  Over all components the cokernel is free abelian of rank
`#pi_0(G)`.  Thus the image is saturated.  QED.

This is the standard total-unimodularity theorem for oriented graph
incidence matrices, proved here directly at the Smith-group level needed for
H7.

### Corollary 2.2

All context images obtained from `x_0,x_1` by independent Cartesian corolla
substitution are `p`-root-closed for every prime, uniformly in their finite
depth and arity.

## 3. Safe coordinate identifications

If a pointed-set map merely identifies grid vertices, every edge relation
pushes forward either to zero or to another difference `e_q-e_r`.  The
result is again a graph-incidence subgroup and Theorem 2.1 applies.  Thus
vertex quotients and parallel repeated rows do not create torsion.

What is not covered is a contraction that **sums several distinct fibers
before** their individual difference rows are retained.  Such a context can
produce a genuine integer relation with coefficients of magnitude greater
than one or a hypergraph-style matrix.  Total unimodularity is then not
automatic.

## 4. Sharpened macro gate

The K2,2 correction of `a_81` is no longer an isolated exception: it belongs
to a completely saturated infinite rectangular family.  Replace the broad
macro gate by

> **H7-MACRO-OVERLAP.** Prove that every multiplication/contraction context
> row reduces to graph-incidence rows as above, or classify the first
> nonseparable overlapping-fiber matrices and determine their Smith factors.

Any prime-torsion counterexample must use a nonseparable fiber overlap, not
mere Cartesian depth, arity, cut permutation or vertex identification.

This does not settle H7-MACRO-CONTEXT-SAT for all Haran contexts, and it does
not settle boundary-chart transport.  H7-PRIME-REG and row A remain open.

## 5. Verification scope

`114_a_82_h7_rectangular_macro_smith_verify.py` constructs rectangular
context graphs through several dimensions/arities, computes exact Smith
normal forms, exhausts vertex identifications on the small grids, and checks
that all nonzero invariant factors are one.  The uniform proof is Theorem
2.1.

Primary source: Haran, [*Geometry over F1*](https://arxiv.org/abs/1709.05831),
equations (10.16)--(10.21).

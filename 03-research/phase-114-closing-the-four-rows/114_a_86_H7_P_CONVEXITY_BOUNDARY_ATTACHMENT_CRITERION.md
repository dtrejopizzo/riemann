# 114.a.86 — H7: p-convexity is a one-boundary-component attachment condition

```
+-------------------------------------------------------------------------+
| GRAPH       G is the full sandwich-context graph; S=pP its divisible set. |
| INSIDE      Collapse connected components of the induced graph G[S].      |
| OUTSIDE     Collapse connected components of G\S.                         |
| CRITERION   S is path-convex iff every outside component is adjacent to   |
|             at most one inside component.                                 |
| WITNESS     A minimal escape is one connected nondivisible region with    |
|             two gates into distinct divisible components.                 |
+-------------------------------------------------------------------------+
```

## 1. Abstract graph theorem

Let `G` be an undirected graph and `S` a subset of its vertices.  Say that
`S` is **component-convex** when any two vertices of `S` connected in `G`
are already connected in the induced graph `G[S]`.  This is precisely
H7-p-CONVEX for `S=pP` in the macro graph of `a_85`.

Let `Q` be a connected component of `G\S`.  Its boundary components are the
connected components of `G[S]` containing neighbors of vertices of `Q`.

### Theorem 1.1 (boundary attachment criterion)

`S` is component-convex if and only if every component `Q` of `G\S` has at
most one boundary component in `G[S]`.

### Proof

If one `Q` touches distinct inside components `A,B`, a path in `A`, one edge
into `Q`, a path through `Q`, one edge out, and a path in `B` connects two
vertices of `S` in `G` but not in `G[S]`.  Thus convexity fails.

Conversely, take a path in `G` with endpoints in `S`.  Each maximal segment
outside `S` lies in one component `Q`; by hypothesis it exits into the same
inside component from which it entered.  Replace that outside excursion by
an inside path.  Repeating for all excursions produces a path in `G[S]`.
QED.

## 2. Exact Haran witness shape

For the sandwich graph `C_{Y,X}` and `S=pP`, a failure of p-CONVEX is
equivalent to data

\[
 pF\;--\;H_0\;--\;\cdots\;--\;H_m\;--\;pG,                         \tag{2.1}
\]

where every `H_j` is nondivisible, the `H_j` lie in one outside component,
and `pF,pG` belong to distinct components of the induced divisible graph.
The outside segment may be long, but it is one connected object with two
boundary gates.

Thus a bounded search should enumerate components of nondivisible macro
states and record their divisible boundary components, rather than enumerate
all endpoint paths.  Finding a component with boundary degree at least two
is an exact p-CONVEX counterexample.  Proving boundary degree at most one
uniformly proves p-CONVEX.

## 3. Relation to available invariants

Every macro edge preserves the diagonal fold, so each outside component lies
inside one fold fiber.  This does not bound its divisible boundary degree:
two distinct divisible components can have the same fold.  The twisted-field
and Hessian invariants close this attachment condition on the read-once and
rectangular sectors (`a_74`--`a_75`, `a_82`), but not on general overlapping
contexts.

The remaining exact gate can be stated as

> **H7-p-ONE-BOUNDARY.** Every connected component of non-p-divisible
> sandwich-context vertices has neighbors in at most one component of the
> p-divisible induced subgraph.

By Theorem 1.1 this is equivalent to H7-p-CONVEX.  H7-p-DIVPATH remains a
separate condition after it.  Neither is proved for the full plane; row A remains open.

## 4. Verification scope

`114_a_86_h7_p_convex_boundary_verify.py` exhausts all graphs through five
vertices and every vertex subset, comparing component-convexity directly
with the one-boundary criterion and extracting minimal two-gate witnesses.

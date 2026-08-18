# 114.a.92 — H7: the ternary parity obstruction is a legitimate fiber diagram

```
+-------------------------------------------------------------------------+
| LEAVES      E=F_2^2 has four elements.                                  |
| CUT MAPS    pi_1(i,j)=i, pi_2(i,j)=j, pi_3(i,j)=i+j.                    |
| PAIRWISE    Every (pi_a,pi_b):E -> F_2^2 is a bijection.                |
| TRIPLE      The joint image is exactly the even-parity 2x2x2 hypergraph. |
| SOURCE      Haran multiplication/contraction accepts arbitrary finite    |
|             set maps and operates fiber by fiber.                        |
| CLOSED      H7-PARITY-TYPE: the ancestry diagram is well typed.          |
| OPEN        Produce a macro collision with these fibers and prove its     |
|             divided endpoints inequivalent.                              |
+-------------------------------------------------------------------------+
```

## 1. The finite-set diagram

Let

\[
 E=\mathbb F_2^2
\]

and define three maps to `F_2` by

\[
 \pi_1(i,j)=i,\qquad \pi_2(i,j)=j,\qquad
 \pi_3(i,j)=i+j.                                                       \tag{1.1}
\]

Their joint map is

\[
 \Pi:E\longrightarrow\mathbb F_2^3,
 \qquad(i,j)\longmapsto(i,j,i+j).                                    \tag{1.2}
\]

Its image is

\[
 \{000,011,101,110\}=H_{\rm even},                                  \tag{1.3}
\]

the parity hypergraph isolated in `a91`.

### Proposition 1.1 (pairwise invisibility)

For every distinct `a,b in {1,2,3}`, the map
`(pi_a,pi_b):E->F_2^2` is a bijection.

### Proof

The pair `(pi_1,pi_2)` is the identity.  From `(i,i+j)` recover
`j=i+(i+j)`; from `(j,i+j)` recover `i=j+(i+j)`.  QED.

Thus every two-cut projection is the complete `K2,2` incidence and lies in
the binary sector closed by `a89`--`a91`.  The obstruction is genuinely
three-way: it disappears after forgetting any one coordinate.

## 2. Typing in Haran's operations

Definitions (3.4)--(3.8) take **every** map of finite sets `f:X->Y` as a
valid multiplication/contraction index and perform the operations separately
on its fibers.  Hence each map (1.1), their products and their composites are
legitimate typed contraction data.  Formula (3.14)--(3.15) uses the finite
fiber product of two such maps in the commutativity move; Proposition 1.1
shows that all pairwise products retain the four leaves individually.

Therefore the diagram

\[
 E\overset{\pi_1,\pi_2,\pi_3}{\rightrightarrows}\mathbb F_2             \tag{2.1}
\]

is not an abstract hypergraph foreign to the category.  It is a legitimate
finite-set ancestry skeleton for nested multiplication/contraction contexts.

> **H7-PARITY-TYPE is closed:** the first ternary matching obstruction of
> `a91` occurs among the finite-set diagrams permitted by Haran's axioms.

## 3. Why this is still not a torsion counterexample

A typed ancestry skeleton does not specify operation labels, signs, outer
sandwiches or two endpoints of an equivalence path.  In particular, (2.1)
does not prove the existence of classes `F,G` such that

\[
 2F\sim2G\quad\text{but}\quad F\not\sim G.                            \tag{3.1}
\]

The remaining tasks are now separated:

1. **H7-PARITY-MACRO:** choose typed tree labels, signs and sandwich
   contexts producing a path between two 2-divisible endpoints whose copy
   ancestry is (1.3);
2. **H7-PARITY-CLOSURE:** compute all extra cut/cancellation moves incident
   to that path, not merely its matching decomposition;
3. **H7-PARITY-SEPARATE:** find a quotient invariant separating the divided
   endpoints, or show the extra moves connect them.

Failure of matching alone proves none of (3.1): a macro path may divide by
moves that do not correspond to a fixed perfect-matching decomposition.
The `K2,2` correction of `a81` remains the mandatory warning.

Thus H7-PARITY-TYPE is closed, while H7-PARITY-MACRO/CLOSURE/SEPARATE,
H7-PRIME-REG and row A remain open.

## 4. Verification scope

`114_a_92_h7_parity_fiber_verify.py` checks the source's arbitrary-map and
fiberwise formulas, exhausts the three pair projections, verifies the exact
even-parity image and its regularity/no-matching property, and enforces the
non-counterexample markers.

Primary source: Haran, [*Geometry over F1*](https://arxiv.org/abs/1709.05831),
equations (3.4)--(3.8) and (3.14)--(3.15).

# 114.a.91 — H7: binary copy mixing divides; the first matching obstruction is ternary

```
+-------------------------------------------------------------------------+
| SOURCE      Contraction is performed fiber by fiber (3.8).              |
| BINARY      Copy mixing across one interface is a regular bipartite      |
|             multigraph.                                                  |
| HALL        Every p-regular bipartite multigraph decomposes into p        |
|             perfect matchings.                                           |
| CONSEQUENCE One binary nonlaminar interface admits copywise p-division.   |
| TERNARY     The even-parity 2x2x2 hypergraph is 2-regular but has no       |
|             perfect matching.                                            |
| EXACT GATE  Realize this shape by Haran sandwich contexts and prove it     |
|             survives, or prove the axioms force an additional edge/move. |
+-------------------------------------------------------------------------+
```

## 1. Fiberwise contraction and copy mixing

For maps of finite sets `X -> Y -> Z`, Haran's formula (3.8) performs
contraction separately over every fiber of `Y -> Z`.  After multiplying a
presentation by a prime `p`, label its `p` displayed copies.  At a single
interface where two cut families meet, forgetting those labels records how
left copies are paired with right copies by a bipartite multigraph.

If both endpoints of the interface are `p`-divisible, each copy label has
the same degree `d`; after separating independent strand fibers, the mixing
graph is `d`-regular on equal-size left and right copy sets.  A division of
the interface into copywise paths is exactly a decomposition into perfect
matchings.  (The letter `d` is used here because the tested prime and the
fiber degree need not be numerically identical; the theorem applies to both.)

## 2. Binary matching theorem

### Theorem 2.1 (regular bipartite decomposition)

Every finite `d`-regular bipartite multigraph is the disjoint union of `d`
perfect matchings.

### Proof

For a set `S` of left vertices, the `d|S|` incident edges all end in
`N(S)`, which has total degree at most `d|N(S)|`.  Hence
`|N(S)|>=|S|`.  Hall's theorem supplies a perfect matching.  Removing it
leaves a `(d-1)`-regular bipartite multigraph.  Induction on `d` proves the
claim.  QED.

### Corollary 2.2 (binary copywise division)

Inside a macro subsystem whose only failure of laminarity is one binary
copy-mixing interface, a path with divisible endpoints can be refined across
that interface into copywise layers.  Checkerboard contexts from corrected
`a89` implement the exchanges between two matching decompositions.  Thus
this isolated binary interface does not produce a H7-p-DIVPATH obstruction.

The corollary is local to the stated interface.  Several incompatible
interfaces cannot in general choose their perfect matchings independently.

## 3. The first hypergraph obstruction

Let each of three parts be `F_2={0,1}` and take the four triples

\[
 H_{\rm even}=\{(0,0,0),(0,1,1),(1,0,1),(1,1,0)\}.                  \tag{3.1}
\]

Every vertex in every part occurs in exactly two triples, so this is a
2-regular 3-partite 3-uniform hypergraph.

### Proposition 3.1

`H_even` has no perfect matching.

### Proof

A perfect matching would consist of two disjoint triples, so the second
triple would be the coordinatewise complement of the first.  Complementing
three bits changes even parity to odd parity.  Therefore the complement of
every edge of (3.1) is absent.  QED.

Consequently `H_even` cannot be decomposed into two perfect matchings.  It
is the smallest copy-mixing pattern for which the binary Hall argument
fails: with only two parts, regularity is sufficient by Theorem 2.1.

## 4. What this does and does not prove for Haran

The parity hypergraph is an exact **candidate shape** for failure of
copywise division across three simultaneous nonlaminar overlaps.  It is not
yet an element of the Haran quotient and it is not a 2-torsion class.
Establishing an actual obstruction requires all of:

1. **H7-PARITY-REALIZE:** construct typed multiplication/contraction
   contexts whose retained ancestry relation is exactly (3.1);
2. **H7-PARITY-CLOSED:** prove cut-commutativity and additional cancellation
   contexts do not add an odd-parity edge or an equivalent matching move;
3. **H7-PARITY-NONZERO:** give an invariant showing the divided candidate is
   not already zero/equivalent, avoiding the `K2,2` error corrected in `a81`.

Conversely, if Haran's axioms always complete (3.1) by an odd-parity edge or
refine it to individual binary interfaces, the matching obstruction
disappears and H7-NONLAMINAR-FIBER advances toward closure.

Thus the live residual gate is no longer an unspecified contraction:

> **H7-TERNARY-OVERLAP.** Decide realizability and closure of the even-parity
> `2x2x2` copy-mixing pattern, then extend the decision to arbitrary
> multi-overlaps.

H7-TERNARY-OVERLAP, H7-PRIME-REG and row A remain open.

## 5. Verification scope

`114_a_91_h7_binary_matching_verify.py` checks the fiberwise source formula;
exhausts small regular bipartite multigraph matrices and constructs their
matching decompositions; verifies the parity hypergraph's degrees and lack
of a matching; and enforces the non-counterexample scope markers.

Primary source: Haran, [*Geometry over F1*](https://arxiv.org/abs/1709.05831),
equations (3.7)--(3.8), (10.16)--(10.21).

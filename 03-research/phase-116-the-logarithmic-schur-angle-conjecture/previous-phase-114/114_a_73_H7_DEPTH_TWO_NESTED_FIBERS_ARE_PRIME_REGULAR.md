# 114.a.73 — H7: all depth-two read-once fibers are prime-regular

> **All-depth extension (`a_74`).** The real homogeneous bio and the two
> mixed-Hessian graphs `H(F)`, `H(F^(1/u))` recursively reconstruct every
> reduced unsigned read-once tree, without any depth or arity bound.

```
+-------------------------------------------------------------------------+
| TREES       Two alternating addition levels on a partition of the leaves.|
| PROBES      Evaluate only Boolean inputs of support one or two.          |
| VALUES      A pair contributes 8 inside the cubic law and 2 otherwise.   |
| RECOVER     The 2/8 pair table reconstructs the entire leaf partition.   |
| CROSS ROOT  Opposite root colors collide only at the two pure additions. |
| CANCEL      An auxiliary characteristic q != ell cancels the tested prime.|
| RESULT      H7-RF-FOLD holds for every read-once tree of depth at most 2. |
| OPEN        Depth >=3, repeated variables, contractions and cut moves.   |
+-------------------------------------------------------------------------+
```

## 1. The complete depth-two family

Let `X` be a finite input set and let `P` be a set partition of `X`.  Write
`delta_c(S)` for the commutative `|S|`-ary sum with color `c in {1,2}`.
The two alternating read-once trees attached to `P` are

\[
 R^{1|2}_P=
 \delta_1\bigl(\delta_2(B)\bigr)_{B\in P},
 \qquad
 R^{2|1}_P=
 \delta_2\bigl(\delta_1(B)\bigr)_{B\in P}.                            \tag{1.1}
\]

Unary vertices are identities.  Consequently

\[
 R^{1|2}_{\{X\}}=R^{2|1}_{\{\{x\}:x\in X\}}=\delta_2(X),
 \qquad
 R^{1|2}_{\{\{x\}:x\in X\}}=R^{2|1}_{\{X\}}=\delta_1(X).             \tag{1.2}
\]

These are the only identifications that should be built into the reduced
two-level syntax.

Under the diagonal fold, every operation in (1.1) becomes the ordinary sum
of all inputs.  Thus the entire family lies in one fold fiber.

## 2. Cubic Boolean probes reconstruct the partition

Choose an auxiliary prime `q>8`, `q=2 mod 3`, and use the full cubic bio
evaluation `E_{q,3}` from `a_72`.  For a subset `S subset X`, evaluate a tree
at the Boolean vector `1_S`.

For a singleton `{i}`, both colors give the value `1`.  For a pair `{i,j}`,
the two root colors give

\[
 E_{q,3}(R^{1|2}_P)(1_{\{i,j\}})=
 \begin{cases}
 8,&i\sim_Pj,\\
 2,&i\not\sim_Pj,
 \end{cases}                                                         \tag{2.1}
\]

and

\[
 E_{q,3}(R^{2|1}_P)(1_{\{i,j\}})=
 \begin{cases}
 2,&i\sim_Pj,\\
 8,&i\not\sim_Pj.
 \end{cases}                                                         \tag{2.2}
\]

Indeed, two ones in one inner cubic block give `(1+1)^3=8`, while two
different blocks are added ordinarily and give `2`.  With the colors
reversed, one inner ordinary block gives `2`; two distinct outer cubic
inputs give `8`.

Since `q>8`, the values `2` and `8` are distinct.

### Theorem 2.1 (same-root separation)

For fixed root color, the full-bio evaluation is injective on the family
`{R_P}` of all set partitions.

### Proof

Equations (2.1)--(2.2) recover, for every pair `i,j`, whether
`i~_Pj`.  That equivalence relation determines `P`.  QED.

## 3. Opposite root colors

Suppose a color-`1` root with partition `P` and a color-`2` root with
partition `Q` have equal pair probes.  Equations (2.1)--(2.2) imply

\[
 i\sim_Pj\quad\Longleftrightarrow\quad i\not\sim_Qj                 \tag{3.1}
\]

for all distinct `i,j`.

### Lemma 3.1 (complementary equivalence relations)

For `|X|>=3`, if both a relation and its off-diagonal complement are
equivalence relations, one is universal and the other is discrete.

### Proof

If `P` has a same pair `a~_Pb` and a point `c` outside their block, then
`a not~_Q b`, while `a~_Q c` and `b~_Q c`.  Transitivity of `Q` gives
`a~_Qb`, a contradiction.  Hence any non-discrete `P` is universal.  The
claim follows symmetrically.  QED.

For `|X|=2`, the same direct dichotomy holds.  Therefore the only
cross-color coincidences are precisely the two boundary identities (1.2).

### Theorem 3.2 (depth-two separation)

After deleting unary vertices, `E_{q,3}` is injective on all alternating
read-once trees of depth at most two and arbitrary finite arity.

## 4. Prime cancellation

Fix the prime `ell` whose regularity is tested and choose

\[
 q>\max(8,\ell),\qquad q=2\pmod3.                                     \tag{4.1}
\]

As in `a_72`, first-ruling multiplication by `ell` is multiplication of the
target functions by the nonzero scalar `ell mod q`, hence is injective.

### Corollary 4.1 (depth-two PRIME-REG)

If `F,G` are reduced alternating read-once trees of depth at most two, then

\[
 \ell F=\ell G\quad\Longrightarrow\quad F=G.                           \tag{4.2}
\]

### Proof

Apply `E_{q,3}`, cancel `ell`, and use Theorem 3.2.  QED.

This proves H7-RF-FOLD for the complete depth-two read-once fiber, not just
for the pair-block words of `a_72`.

## 5. Exact remaining tree problem

Any counterexample to H7-PRIME-REG must now evade both `a_72` block
extraction and the complete depth-two partition reconstruction above.  The
remaining target is

> **H7-RF-DEEP.** Separate same-fold reduced trees of alternating depth at
> least three, including repeated variables, contractions and the
> cut-commutativity relation, uniformly on an affine pro-cover.

Depth alone is not the only issue: arbitrary cut moves can change a nested
presentation without changing its class, so a proof must be invariant under
Haran's full quotient rather than count raw colored trees.

## 6. Verification scope

`114_a_73_h7_depth_two_regular_verify.py` enumerates every set partition
through seven leaves, both root colors, and verifies that the complete
one/two-point signature has exactly the reduced identifications (1.2).  It
also checks prime cancellation in auxiliary characteristics.  The general
proof is Theorems 2.1--3.2; the verifier does not assert H7-RF-DEEP.

# 114.a.96 — H7: parity bits admit intrinsic same-fold rigidification

```
+-------------------------------------------------------------------------+
| BIT 0       D_0=delta_1(x_1,x_2,x_3), a ternary corolla.                |
| BIT 1       D_1=delta_1(delta_2(x_1,x_2),x_3), a nested tree.            |
| SAME TYPE   Both have three leaves and root color 1.                     |
| SAME FOLD   Identifying the rulings sends both to x_1+x_2+x_3.           |
| DISTINCT    D_0 and D_1 are nonisomorphic reduced colored trees and are   |
|             separated by the real bio/Hessian invariant.                 |
| RIGID       A cut-block automorphism cannot exchange the two bits.        |
| CLOSED      H7-PARITY-RIGID-TYPE.                                        |
| OPEN        Even macro replacement paths and endpoint realization.        |
+-------------------------------------------------------------------------+
```

## 1. Two intrinsically different blocks with the same fold

Let

\[
 D_0=\delta_1(x_1,x_2,x_3),\qquad
 D_1=\delta_1(\delta_2(x_1,x_2),x_3).                                \tag{1.1}
\]

Both are reduced unsigned read-once trees.  They have the same external
arity three and the same root color.  Their internal rooted colored trees
are not isomorphic: `D_0` has one internal vertex, while `D_1` has two and
contains a color-2 binary child.

Under the diagonal fold `delta_2=delta_1`, associativity gives

\[
 \operatorname{fold}(D_0)=x_1+x_2+x_3
 =\operatorname{fold}(D_1).                                         \tag{1.2}
\]

The distinction also survives the Haran quotient.  In the positive real
bio of `a49` with parameter `u>1`, evaluate at `(1,1,1)`:

\[
 D_0(1,1,1)=3,\qquad D_1(1,1,1)=2^u+1>3.                            \tag{1.3}
\]

Equivalently, the all-depth Hessian theorem of `a74` reconstructs the two
different reduced trees.  Hence no permitted tree isomorphism or relation
can identify `D_0` with `D_1`.

## 2. Rigidifying the parity skeleton

In each of the three two-element parts of `a92`, replace the bare vertex
label `0` by a copy of `D_0` and `1` by a copy of `D_1`.  The joint ancestry
still uses the four even triples

\[
 000,011,101,110,                                                     \tag{2.1}
\]

now interpreted as choices of decorated blocks.

An internal swap of a two-element cut would have to carry `D_0` to `D_1`.
This is impossible by Section 1.  Thus the swap columns that killed the bare
Smith obstruction in `a95` are no longer isomorphism relations of the
decorated presentation.

The decorations do not change the diagonal fold of a bit block, so all four
ancestry triples remain compatible with the same folded external operation.

> **H7-PARITY-RIGID-TYPE is closed:** there is a typed, intrinsically
> labelled version of the parity skeleton in which coordinate flips are not
> supplied by commutativity and all bit decorations have equal fold.

## 3. What rigidification does not supply

Rigidification removes the specific `a95` automorphism, but it can also make
the desired even replacements harder: a path from decorated `000` to
decorated `011` must change two nonisomorphic blocks through genuine
cancellation/sandwich moves, not by relabelling children.

The remaining exact gates are:

1. **H7-RIGID-EVEN-MOVES:** realize the three fold-zero even differences of
   `a94` with the `D_0,D_1` decorations;
2. **H7-RIGID-ODD-CLOSURE:** prove no larger context creates an odd
   decorated replacement;
3. **H7-RIGID-ENDPOINTS:** lift the Smith witness to operations
   `2F~2G`;
4. **H7-RIGID-SEPARATE:** descend a mod-two invariant proving `F not~G`.

It is possible that the first gate fails: same fold does not imply
equivalence in the plane, and (1.3) deliberately separates the decorations.
If it fails, this rigidification kills the even moves together with the odd
ones and yields no torsion candidate.

H7-PARITY-RIGID-TYPE is closed; the four macro gates above, H7-PRIME-REG and
row A remain open.

## 4. Verification scope

`114_a_96_h7_parity_rigid_verify.py` checks exact tree signatures, equal
folds, separation in rational power-norm models, preservation of the even
parity incidence and absence of coordinate-flip automorphisms.  It enforces
that macro replacement paths are not asserted.

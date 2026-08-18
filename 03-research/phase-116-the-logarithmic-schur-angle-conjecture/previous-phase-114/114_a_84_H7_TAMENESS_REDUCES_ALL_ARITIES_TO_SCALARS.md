# 114.a.84 — H7: tameness reduces prime regularity to scalar sandwiches

```
+-------------------------------------------------------------------------+
| TAME        Elements are separated by all scalar sandwiches b o (-) o d. |
| CENTRAL p   Sandwiching pF=pG gives p(bFd)=p(bGd) in A_[1],[1].          |
| SCALAR REG  If p cancels in the scalar monoid, every sandwich agrees.     |
| CONCLUDE    Tameness then gives F=G in every arity.                       |
| MISSING     Haran does not prove the arithmetic-plane quotient tame or    |
|             matrix; scalar macro saturation is also open.                |
+-------------------------------------------------------------------------+
```

## 1. Source notion

For a prop/generalized ring `A`, Haran calls `A` **tame** when, for every
`a,a' in A_{Y,X}`,

\[
 b\circ a\circ d=b\circ a'\circ d
 \quad\text{for every }b\in A_{1,Y},\ d\in A_{X,1}                  \tag{1.1}
\]

implies `a=a'`.  Matrix props are tame.  A tame equivalence ideal is one
whose quotient is tame and is then determined by its scalar equivalence
relation, with all sandwich contexts included.

The arithmetic plane is commutative and hence its scalar monoid acts
centrally, but the source does not state that the quotient by `E_cancel` is
tame or matrix.

The same source proves the necessary implication

\[
 \text{commutative}+\text{tame}\Longrightarrow
 \text{cross-commutative}.
\]

`a103` isolates its first mixed-generator acceptance test H7-XDEF-12.  A
nonzero cross defect has identical scalar sandwiches on both sides and would
therefore refute H7-TAME-PLANE explicitly.

## 2. Scalar reduction theorem

### Theorem 2.1 (tame scalar criterion)

Let `A` be a central tame prop and let `p in A_{1,1}`.  If multiplication by
`p` is injective on `A_{1,1}`, then multiplication by `p` is injective on
every `A_{Y,X}`.

### Proof

Assume `pF=pG` in `A_{Y,X}`.  For arbitrary scalar sandwich maps
`b in A_{1,Y}` and `d in A_{X,1}`, centrality gives

\[
 p\,(b\circ F\circ d)
 =b\circ(pF)\circ d
 =b\circ(pG)\circ d
 =p\,(b\circ G\circ d).                                             \tag{2.1}
\]

Scalar injectivity cancels `p`, so every pair of sandwiches in (1.1)
agrees.  Tameness yields `F=G`.  QED.

### Corollary 2.2

For Haran's base arithmetic plane, the conjunction

1. **H7-TAME-PLANE:** the quotient by `E_cancel` is tame; and
2. **H7-SCALAR-SAT:** `(E_cancel:p)=E_cancel` on `[1,1]` for every prime,

implies base H7-PRIME-REG in all arities.  Central localizations then inherit
the result as in `a_71`.

## 3. Relation to the macro-context problem

Tameness does not remove macro contexts; it says they are completely tested
by scalar sandwiches.  The general generator-path formula in the source,

\[
 c\circ(a_i\oplus id_V)\circ d,                                     \tag{3.1}
\]

shows why `a_81` occurs: even a scalar sandwich can contain a nonlocal
Cartesian grid.  Thus `a_82` handles the rectangular scalar sector and
`a_83` supplies exact Smith acceptance tests for aggregated scalar fibers.

If H7-TAME-PLANE fails, a witness consists of two distinct operations with
all scalar sandwiches equal; that is another precise negative outcome for
the completed-lattice route.  If it holds, only scalar macro saturation and
boundary charts remain.

Neither H7-TAME-PLANE nor H7-SCALAR-SAT is proved here.  The theorem is a
rigorous reduction, not a claim that the arithmetic plane satisfies its
hypotheses.  H7-PRIME-REG and row A remain open.

**Later sharpening (`a102`).**  For the first-ruling ordinary scalar ring,
the fold gives `R=Z direct-sum K` with `K=ker(nabla)`.  H7-SCALAR-SAT for all
primes is exactly torsion-freeness, equivalently ordinary `Z`-flatness, of
`K`; it is renamed H7-AUG-FLAT there.  The fold retraction alone does not
prove this property.

**Later resolution (`a104`).**  The signed plane fails H7-TAME-PLANE: its
first mixed centre/grid defect survives in a commutative infinitesimal
target.  Therefore this theorem remains correct as a conditional theorem,
but its tame-promotion route is not available for the Haran plane.  Direct
componentwise prime regularity is the live route.

## 4. Verification scope

`114_a_84_h7_tame_scalar_reduction_verify.py` checks the primary-source
definitions, exhausts finite separating sandwich systems and verifies the
central scalar-cancellation implication.  It enforces the two open
hypotheses in the document scope.

Primary source: Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Definition 1.4.3 and Appendix A.2.

# 114.a.79 — H7: local fixed-incidence confluence, not the full cancellation quotient

```
+-------------------------------------------------------------------------+
| SUBSYSTEM   Visible opposite parallel edges plus pruning and the two tree |
|             reductions on one fixed incidence presentation.              |
| TERMINATE   Every oriented rule decreases strands or vertices.            |
| CONFLUENT   Local C/C, tree/tree and C/tree critical pairs are joinable.   |
| CORRECTION  Context images of x_0,x_1 need not expose a visible parallel  |
|             pair in that presentation.                                    |
| WITNESS     a81: a locally irreducible K2,2 grid is a contextual image of  |
|             x_0 and hence is zero in the full quotient.                    |
| VERDICT     The local subsystem is solved; presentation-completeness and   |
|             prime saturation remain open.                                 |
+-------------------------------------------------------------------------+
```

## 1. The restricted rewrite system

Fix one bilateral tree presentation and its displayed leaf incidence.  Use
only these oriented rules:

1. `C`: delete a visible `+1,-1` pair of parallel leaf strands with the same
   endpoints;
2. `Z`: restrict affected trees to surviving boundary subsets;
3. `U`: suppress unary vertices;
4. `A`: contract a nonroot vertex having its parent's orientation.

This is a genuine subsystem of Haran's cancellation congruence.  The earlier
version of this file asserted that every multiplication/contraction context
instance of the generators `x_0,x_1` expanded into this subsystem.  That
assertion is false and is retracted in Section 4.

## 2. Termination

The lexicographic measure

\[
 (\text{number of displayed signed strands},
   \text{number of tree vertices})                                   \tag{2.1}
\]

strictly decreases: `C` deletes two strands, while every nontrivial `Z/U/A`
move deletes at least one vertex.  Hence the restricted system terminates.

## 3. Local confluence inside the subsystem

### Theorem 3.1 (fixed-incidence local confluence)

The `C/Z/U/A` subsystem is confluent up to rooted-tree isomorphism.

### Proof

For two `C` moves, disjoint bundles commute and one common bundle has the
unique integer excess `#plus-#minus` (`a_77`).  The `Z/U/A` subsystem is
jointly confluent: restrictions intersect, and the two tree reductions have
joinable critical pairs (`a_78`).

For a mixed pair, disjoint moves commute.  In an overlap, tree restriction
or suppression transports the two displayed labels through the same common
factor `s in {0,+1,-1}`.  Thus `(+1,-1)` becomes `(+s,-s)`; it is deleted by
`Z` when `s=0` and remains cancelable otherwise.  If visible bundles merge,
their integer excesses add independently of order.  These cases exhaust the
critical pairs of the restricted rules.  Termination and Newman's lemma give
confluence.  QED.

This theorem usefully closes all finite cascades **once every cancellation
redex is already visible in the fixed incidence presentation**.

## 4. Why this is not the full Haran quotient

An equivalence ideal is closed under arbitrary multiplication and
contraction contexts.  Such a context can replace the two strands of a
cancellation generator by a Cartesian grid.  The resulting datum need not
contain any visible parallel-edge pair in its chosen tree presentation.

`a_81` gives the minimal example.  A binary other-ruling context applied to
`x_0` produces a depth-two `K2,2` grid with signs constant by row.  It has no
local `C/Z/U/A` redex, but it is equivalent to zero because it is literally
a context image of `x_0~0`.

Therefore Theorem 3.1 does **not** give a normal form for
`E_cancel`, does not prove H7-CORE-CONFLUENCE for the full contextual system,
and cannot support a prime-regularity conclusion.

The corrected remaining gate is

> **H7-MACRO-CONTEXT-NF.** Construct a terminating confluent calculus, or an
> equally faithful invariant, for every multiplication/contraction context
> image of `x_0,x_1` modulo consistent commutativity.

Prime saturation then becomes H7-MACRO-CONTEXT-SAT.  Both remain open.

## 5. Verification scope

`114_a_79_h7_core_critical_pairs_verify.py` verifies only the restricted
critical-pair identities and termination measure.  Its scope markers forbid
using that result as presentation-completeness.  The `K2,2` macro-context
failure is checked separately in `a_81`.

Primary sources: Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Sections 8.3.6 and 13.2; [*Geometry over F1*](https://arxiv.org/abs/1709.05831),
equations (10.16)--(10.21).

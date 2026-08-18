# 114.a.78 — H7: one topology-changing cancellation site is confluent

> **Scope correction (`a_81`).** `a_79` extends this result to every finite
> cascade of visible sites on one fixed incidence presentation.  It does not
> cover macro context images of the cancellation generators; full contextual
> confluence and prime purity remain open.

```
+-------------------------------------------------------------------------+
| INPUT       One active signed parallel bundle in an otherwise fixed      |
|             bilateral network core.                                     |
| CANCEL      Every sequence leaves the same signed excess a-b.            |
| PRUNE       If branches disappear, Haran's restriction F|_B is canonical.|
| REDUCE      The resulting individual trees have unique 1- and            |
|             alternating-reduced representatives.                         |
| RESULT      The completed reduction of one isolated site is unique.       |
| RESIDUAL    A minimal obstruction needs two interacting sites or a        |
|             cancellation/pruning cascade which creates a second site.     |
+-------------------------------------------------------------------------+
```

## 1. Isolated-site setup

Fix an expanded directed network and two same-ruling vertices joined by a
parallel bundle containing `a` strands labelled `+1` and `b` strands
labelled `-1`.  Freeze all other branches.  Call this the only **active
site** when no other opposite-signed parallel pair is cancelable before this
bundle is reduced.

An isolated-site completion consists of:

1. canceling opposite pairs at this site until none remain;
2. restricting every affected input/output tree to the surviving boundary
   subset using Haran's `F|_B`;
3. applying the unique `1`-reduction and `lhd`-reduction of the resulting
   individual oriented trees;
4. stopping before canceling any *new* active site created by the splice.

The stopping convention separates one critical overlap from a genuine
cascade.  It does not discard the new site; that site is the input of the
next cascade stage.

## 2. Joint confluence of the two tree reductions

The source states uniqueness for `1`-reduction and `lhd`-reduction
separately.  The isolated-site argument needs their union, so this point must
be proved rather than inferred.

### Lemma 2.1 (joint tree-reduction confluence)

On a finite oriented rooted tree, the rewrite system generated jointly by
`1`-reduction and `lhd`-reduction is terminating and confluent up to rooted
oriented-tree isomorphism.

### Proof

Every move deletes one vertex, so termination is immediate.  By Newman's
lemma it is enough to check local confluence.  Two deletions at disjoint,
nonadjacent vertices commute.  For adjacent vertices there are four cases.

1. Two unary suppressions merely suppress a length-two chain in either
   order.
2. Two alternating reductions contract three consecutive equal-oriented
   vertices in either order.
3. If a unary parent has an equal-oriented child, suppressing the parent
   keeps the child, while contracting the child keeps the parent with the
   child's descendants.  The two results are isomorphic because parent and
   child have the same orientation.  This includes the root case.
4. If an equal-oriented parent has a unary child, deleting either first and
   then applying the surviving rule attaches the unary child's only
   descendant to the same grandparent.  Again the results agree.

Nested moves not sharing an edge reduce to one of these cases after the
outer context is restored.  Hence every critical pair is joinable; Newman's
lemma gives confluence.  QED.

## 3. Unique completion theorem

### Theorem 3.1 (single-site confluence)

Every isolated active site has a unique completion, independently of the
order in which its opposite pairs are canceled and the forced tree
reductions are performed.

### Proof

Each cancellation replaces `(a,b)` by `(a-1,b-1)`.  Hence every maximal
sequence has the unique terminal signed bundle

\[
 ((a-b)_+,(b-a)_+).                                                    \tag{2.1}
\]

In particular, the surviving boundary subset is independent of the
sequence.  Haran defines the restricted tree `F|_B` directly from this
subset by deleting the other leaves and then iteratively deleting vertices
with no surviving descendants.  Therefore the pruned tree is unique.

If the remaining bundle has one strand, an endpoint can become unary.  Its
suppression is precisely `1`-reduction.  If that splice makes adjacent
vertices of the same orientation inside one tree, their contraction is
`lhd`-reduction.  Lemma 2.1 gives a unique joint normal form.  Thus the reduced trees and
their surviving leaf bijection are determined by (2.1), not by the order of
the moves.  We stop if this forced splice exposes a new cancellation site,
so no second cancellation choice enters the statement.  QED.

### Corollary 3.2 (minimal-cascade criterion)

A failure of H7-CORE-CONFLUENCE cannot be supported on one isolated active
site.  A minimal failure must contain either

1. two active cancellation bundles whose reductions overlap; or
2. one active bundle whose unique completion creates another active bundle,
   with nonjoinable results after the second stage.

At this stage the next local object was a two-site cancellation cascade,
denoted **H7-CASCADE-2**.  It is absorbed, together with all higher visible
finite cascades, by Theorem 3.1 of `a_79`; macro contexts remain separate.

## 4. Prime-purity consequence on the stable one-site sector

Suppose additionally that `p`-fold replication stays in the same isolated
site and creates no cross-copy active bundle.  Its signed excess is
`p(a-b)`.  If two replicated completions agree, torsion-freeness of `Z`
cancels `p`, giving the same excess before replication.  Theorem 3.1 then
gives the same pruned and reduced completion.

This proves H7-CANCEL-PURE on the stable one-site sector.  The stability
hypothesis is essential for this file's theorem; `a_79` later closes cascade
confluence but not prime purity of the full additive relation system.

## 5. Verification scope

`114_a_78_h7_single_site_confluence_verify.py` checks the source definitions
of tree restriction and unique individual reductions, exhausts joint tree
reduction through seven vertices, exhausts bundle and
fixed-context degrees, checks the three zero/unary/multiple topology cases,
and verifies prime-root closure in the stable one-site sector.  It does not
assert H7-CASCADE-2 or full H7-CANCEL-PURE.

Primary source: Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Sections 8.3.6 and 13.2.

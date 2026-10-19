# P123.021 — classical cone and transpose tests


## Verdict

`REFUTED-AS-AN-IDENTIFICATION` for P123.011 §4's inference that the full
source sum-of-squares cone specializes to the effective graph-cycle cone.
The elementary two-point example below disproves even containment in either
direction under the literal graph-matrix identification.

`PROVED` for the distinction between transpose and inverse on finite
Frobenius graphs. These tests do not refute a future differently defined
cycle map or an explicitly normalized rational correspondence model.

## 1. A two-point exact counterexample

Let X={1,2}, e the identity graph and t the transposition graph. The
faithful matrices are

    e = [[1,0],[0,1]],   t = [[0,1],[1,0]].

They satisfy t*=t and t²=e. The effective graph cone in their real span is

    Eff_graph={a e+b t : a,b>=0}.

The source algebra of linear combinations, however, also contains x=e-t,
and

    x*x=2e-2t = [[2,-2],[-2,2]].

It is a square and positive semidefinite: its eigenvalues are 0 and 4.
It is not an effective cycle, since its coefficient at the transposition
graph is -2. Conversely t is effective but has eigenvalues 1 and -1, so
cannot be a sum of operator squares or a limit of such sums.

No issue of noncommutativity is needed: the span of e,t is commutative.
Even self-adjoint effective correspondences need not be C*-positive.
The trace pairing Tr(A B*) is nondegenerate on this span, with e,t
orthogonal and both squared norms 2. Thus passage to this model's numerical
quotient does not remove the counterexample.

This disproves the literal cone identification, not the separate
properness proof for the source cone in P123.010.

## 2. Transpose of finite maps

For a morphism f:C->C, the graph convention is (x,f(x)). Its first
projection is an isomorphism. The first projection of its transposed graph
is f. If f has degree d>1, the transposed graph cannot be the graph of a
scheme inverse. Bijectivity on geometric points does not change this fact.

In particular take C=P^1 over F_Q and the Q-power Frobenius morphism F.
Its degree is Q and its derivative is zero, so it is not an invertible
scheme morphism. Its iterates have degree Q^m.

In the **cycle correspondence** category, either composition of Gamma_F
and Gamma_F^t is Q Delta. One composition is pushforward along the finite
map; the other is the radicial fiber product, supported on the diagonal
with generic length Q. Therefore its inverse, if rational coefficients
are allowed, is Q^-1 Gamma_F^t, not Gamma_F^t itself.

This statement concerns cycle composition. An isomorphism of perfect
kernels, including nilpotent or derived structure, needs a separate
comparison and does not follow from this cycle equality.

Consequently a comparison of E_u^dagger=E_(u^-1) with Frobenius transpose
must specify normalization and the coefficient category. An additive
category of invertible automorphism bimodules is not automatically the
category of integral finite Frobenius correspondences.

## 3. Correct scope of the existing classical control

The classical operations written in P123.011 can be studied on their own
smooth proper scheme. Their existence there does not establish a functor
from the semilocal analytic category to that classical category.

What remains required is:

1. a specified coefficient/category comparison;
2. its action on a noninvertible finite graph and its transpose;
3. a comparison of the scalar kernel trace with cycle intersection,
   including any RR corrections and the relevant domain;
4. a geometric effective class or a separately proved relation to source
   squares, without discarding cross terms;
5. an explicit account of the two ruling classes.

The elementary counterexample makes (4) necessary before A.9 can be
accepted as a full cone comparison. It supplies no arithmetic Hodge sign.

## Provenance

This note records elementary finite-set linear algebra and finite-map
cycle calculations, checked independently in the first approved campaign.
It makes no novelty claim. The affected assertions are in
[P123.011](P123_011_FINITE_FIELD_WEIL_CONTROL.md) §4 and the inverse analogy
in §2; the valid source-cone statement remains in
[P123.010](P123_010_SOURCE_EFFECTIVE_CONE.md).

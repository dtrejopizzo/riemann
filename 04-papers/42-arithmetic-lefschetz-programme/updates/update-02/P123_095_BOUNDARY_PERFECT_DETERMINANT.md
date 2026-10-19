# P123.095 — A genuine determinant line on the corner-generated perfect sector

Status: PROVED-IN-REPOSITORY for the single-zero
orbit-decay boundary. The target is a graded line bundle on B_q.
No arithmetic metric, degree or mixed Riemann--Roch is asserted.

Let J, e and B=eJe=C(B_q) be as in P123.093–094. All modules below
are right modules, with their stated direct-summand topologies.

## 1. The precise perfect domain

Let P_e(J) consist of images of continuous idempotents on finite direct
sums of eJ. Such an endomorphism is a matrix over eJe=B: for a map
eJ->eJ, its value on e belongs to eJe and determines its value on ej
as f(e)j. Conversely left multiplication by every element of eJe is
a continuous right-J-module map. The same argument works for matrices
and retracts. Thus

    M -> Me,       N -> N tensorhat_B eJ                    (1)

are inverse equivalences between P_e(J) and finite projective B-modules.
On eJ, multiplication B tensorhat_B eJ->eJ has inverse x->e tensor x;
finite sums and continuous idempotent images preserve those identities.
This proves (1) on the declared domain without an assumption about all
topological J-modules. Morphism spaces identify with the corresponding
closed matrix corners over B, with their sup-norm topology.

For an idempotent P in M_n(C(B_q)), its images P(y)C^n form a continuous
finite-rank vector bundle E_P. Rank is locally constant: nearby
idempotents have the same rank, and restriction of a fixed independent
set of image vectors provides a local frame. Conversely a vector bundle
on compact B_q has a finite trivializing cover; a subordinate partition
of unity and local frames give finitely many global spanning sections.
A continuous Hermitian metric gives a splitting of their surjection
from a finite trivial bundle, producing an idempotent presentation.
Module maps are exactly the continuous maps of these bundles, as is
seen in local frames. Thus (1) has a concrete vector-bundle realization.

## 2. Determinants of bounded complexes

Let K be a bounded complex in P_e(J), and E^i its corresponding bundle
complex. Define the graded line bundle

    Det_e(K)=tensor_i (det E^i)^( (-1)^i ),
    degree(K)=sum_i (-1)^i rank(E^i),                         (2)

where exponent -1 means the dual line, and degree is an integer-valued
locally constant function on B_q. The parity is degree modulo two.
For variable rank, the exterior-power definition is made on the open
and closed rank loci. This constructs a line bundle, not merely the
exponential of a scalar trace. The degree in (2) is virtual rank, not
an arithmetic intersection degree.

An exact sequence of bundles has its canonical exterior-power
isomorphism det E=det E' tensor det E''. Applying these degreewise,
and commuting graded factors with their Koszul signs, gives additivity
for termwise exact short sequences of complexes. In particular, for
f:K->L, the terms Cone(f)^i=L^i direct_sum K^(i+1) give

    Det_e(Cone(f))=Det_e(L) tensor Det_e(K)^(-1).             (3)

These identifications are coherent: locally they are the exterior-power
identities for ordered bases, and any permutation contributes precisely
the stated graded sign. Independence of bases follows by cancellation
of their transition determinants; local equalities glue.

A bounded exact bundle complex has a canonical trivialization of (2).
Indeed exactness makes the image ranks locally constant, inductively
from either endpoint, so the images are subbundles. The exact sequences
0->im d^(i-1)->E^i->im d^i->0 cancel successive determinant factors.
The resulting trivialization does not depend on a chosen splitting.
A bounded acyclic complex of finite projective B-modules splits by
induction from an endpoint and has the same construction. Consequently
quasi-isomorphisms in this perfect domain induce determinant
identifications through their acyclic cones. No closed-image assertion
for arbitrary Frechet complexes is imported into this argument.

## 3. Compatibility with the source's function-valued trace

Let T:J->C(B_q) be the exact shadow map of P123.094, and apply F
entrywise to matrices over B. For a corner endomorphism u represented
on an idempotent summand, define its source matrix trace by summing
T of its diagonal J entries. Since T(F(h))=h, this is exactly the
ordinary bundle trace of u. In particular

    sum_i (-1)^i Tr_source(id_(K^i))=degree(K).               (4)

The same equality holds for supertraces of chain endomorphisms. It is
independent of an idempotent presentation: cyclicity makes traces agree
under inverse module identifications, or equivalently they are the same
fiberwise bundle traces.

For a differentiable path of chain automorphisms g(t), Jacobi's
finite-dimensional identity in a local frame gives

    d/dt log Det_e(g(t))
       =sum_i (-1)^i Tr_source((g^i(t))^-1 d g^i(t)/dt).      (5)

Here the left side means the logarithmic derivative, so no global choice
of a logarithm is assumed. Transition determinants cancel in this
derivative, making (5) global on B_q. The identity follows directly by
differentiating the alternating multilinear determinant in each frame.
Applying quotient Haar integration to (4) or (5) recovers the original
scalar boundary trace of P123.094. No new normalization is introduced.

## 4. Independence of cutoff

For another normalized compact cutoff d, the elements V_(d,c) and
V_(c,d) of P123.090 lie in J by P123.092. Left multiplication gives
inverse right-module isomorphisms e_c J -> e_d J, since their products
are the respective projections. On corners the induced isomorphism
V_(d,c) b V_(c,d) identifies the same scalar function in C(B_q).
Thus the bundle complex, determinant line and trace identities above
are canonically transported between cutoffs. Triple transport is
coherent by the exact partial-isometry identities in P123.090.

## 5. Exact remaining burden for A

This gives a perfect-module domain, an actual graded determinant line,
cone and acyclic compatibility, cutoff independence, and equality of its
infinitesimal determinant trace with the previously computed source
shadow. All statements concern bundles over the compact boundary B_q.

It does not prove that the diagonal of the designated mixed
correspondences lies in this perfect domain. Nor does it provide the
intrinsic periodic ruling metric, a finite arithmetic degree, normal
regularized determinant or the required mixed RR equality. Extending
and identifying those structures remains necessary; the boundary
determinant alone does not close A.5 or A.8 for the full source.

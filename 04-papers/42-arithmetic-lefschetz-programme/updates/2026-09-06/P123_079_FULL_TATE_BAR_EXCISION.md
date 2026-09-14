# P123.079 — Full Tate bar comparison by the ideal-word filtration

Date: 2026-09-06. Status: PROVED as a strict quasi-isomorphism of the
displayed completed augmented bar complexes. A continuously split
chain-homotopy equivalence or general mixed RR is not asserted.

Keep the original rapid C_0 source A -> D, its algebra section j and
ideal I. For a Tate augmentation chi=lambda e write
J=ker chi=I direct_sum j(m), where m=ker lambda in D. Let B(J) and
B(m) be their normalized augmentation bar complexes, with degree n
the completed n-fold tensor and degree zero C. The map B(J) -> B(m)
has the continuous chain section induced by j. Its kernel K has, in
degree n, precisely the finite direct sum of words containing at least
one I factor.

Filter K by the number of j(m) factors, using the increasing filtration
F_k of words with at most k such factors. Multiplication never increases
this number: I is an ideal and j(m) is a subalgebra. The degree-n
filtration is finite, with k<=n-1. Each filtration piece is closed and
has a continuous linear complement by the tensor decomposition.

In the associated graded for exactly k scalar factors, only multiplication
of two adjacent I factors survives. Multiplication involving a scalar
factor lowers the filtration. Each graded word has the form

    I^tensor a_0 tensor j(m) tensor I^tensor a_1
       tensor ... tensor j(m) tensor I^tensor a_k,

where the a_i are nonnegative and at least one is positive. The subset
of positive a_i is preserved by the graded differential: an I block of
length one has no internal multiplication boundary, and longer blocks
remain nonempty. For each such pattern, its complex is the tensor of
the nonunital ideal bars for the nonempty blocks, separated by the fixed
scalar factors, with the usual totalization signs and degree shifts.

Every pattern complex is exact. Select one nonempty I block and filter
by the total degrees of the other blocks. In each resulting column,
P123.078 gives exactness after tensoring the selected ideal bar with the
complete Fréchet space of all the other factors. The first-quadrant
totalization has finitely many terms in each degree, so successively
lifting cycles proves exactness of its total complex. There is no
infinite product totalization or unproved preservation of arbitrary
exact sequences by projective tensor in this argument: the required
tensor exactness is exactly the one proved in P123.078.

It follows that every associated-graded piece of K is exact. This gives
an elementary finite filling argument for K itself. For a cycle z of
degree n, choose its largest nonzero scalar-count component k. Fill
that component in gr_k K, lift the filling to F_k K_(n+1), and subtract
its boundary from z. The new cycle has scalar count at most k-1.
Repeat down to zero. At most n steps produce an exact filling of z.
Thus K is acyclic. Its boundary images equal closed kernels; the
Fréchet open mapping theorem makes its boundary surjections strict.

Since B(J)=K direct_sum j B(m) as continuous chain complexes, projection
to B(m) is a strict quasi-isomorphism. Its mapping cone is the direct
sum of a shift of K and the continuously contractible cone of identity
on B(m), so it too is strictly exact. The induced ordinary and reduced
homology comparisons are topological isomorphisms: the split chain
decomposition induces the corresponding quotient decompositions, and
the K summand has zero homology.

Combining this result with P123.076 gives the full-source self-Tate bar
homology, not merely its scalar retract:

    H_k(C_chi tensor_A^(bar) C_chi)=exterior^k C^r,
                          0<=k<=r=|S_f|,

and zero above r. Here the superscript specifies the completed bar
model. In the category localizing continuous complexes at strict
quasi-isomorphisms, that model is equivalent to the finite zero-differential
exterior complex from the scalar Koszul calculation. The maps e and j
and the filtration commute with repaired semilocal chart embeddings.

The proof supplies exact fillings, not continuous linear choices of
all fillings. Therefore it must not be presented as a chain-homotopy
equivalence in the more restrictive continuously split exact category
without an additional argument. The finite model now determines the
self-Tate contribution in the strict derived category. Its metric,
comparison with the intrinsic ruling determinant, mixed fibers and
mixed correspondence RR still require their own constructions. This
does not close A.8 merely by computing this excess contribution.

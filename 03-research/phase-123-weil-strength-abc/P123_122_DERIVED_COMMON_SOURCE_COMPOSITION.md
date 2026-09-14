# P123.122 — Relative derived composition and cyclic shadow on the common source

Date: 2026-09-07. Status: PROVED-IN-REPOSITORY in the continuously
linearly split exact structure below. This constructs a derived category
and composition on the common coefficient source of P123.121. It is not
a claim of all geometric localization/descent or a determinant RR theorem.

## 1. Exact structure and objects

Let A be the coefficient-unitized rapid algebra A_sm^u(P) of P123.121.
It has the actual identity and gauge unitaries. Take unital complete
Frechet A-bimodules with continuous actions and continuous bimodule maps.
An admissible short exact sequence is one split by a continuous complex
linear map after forgetting both actions. The section need not preserve
either action. The induced exact structure is stable under pushout and
pullback: after a linear splitting its middle space is a finite direct
sum, and the usual pushout or pullback is again such a split space.

Use bounded-above cochain complexes in this exact category. Admissibly
acyclic means each cycle sequence is admissible, equivalently its
underlying Frechet complex has a degreewise continuous contraction.
The relative derived category D_rel^-(A-A) is the homotopy category
localized at maps with admissibly acyclic cones. This is a specified
relative exact structure, not an assertion of invariance under all
ordinary quasi-isomorphisms of topological complexes.

The free bimodule F(V)=A tensorhat V tensorhat A is relatively
projective: a map out of it is determined on 1 tensor V tensor 1;
a continuous linear section of an admissible surjection lifts that map.
Extending by the two actions gives the required continuous bimodule lift.
This is P123.066 on the common algebra, and applies to arbitrary complete
Frechet V, not only finite-dimensional generators.

## 2. Enough continuous projective resolutions for complexes

For a bimodule M take the left/right double bar with terms

    A tensorhat A^(tensorhat r) tensorhat M
           tensorhat A^(tensorhat s) tensorhat A,
           r,s>=0.                                      (1)

Its augmentations use the two M actions. The two bar boundaries commute
before totalization; introduce the usual degree sign so they anticommute.
After forgetting the actions, insertion of the unit contracts an
augmented left bar and then the augmented right bar. These insertions
also commute with the internal differential of a complex M, with the
cochain totalization signs. Thus the total augmentation Q(M)->M is an
underlying continuous chain-homotopy equivalence. Equivalently one can
first contract the augmented left bar as a right-module complex and
then contract the remaining right bar as a complex of spaces.

A term M^i in bar degrees r,s has total degree i-r-s. If M^i=0 for
i>N, a fixed total degree n permits only n<=i<=N and r+s=i-n.
Consequently each total degree contains finitely many summands, all
relatively free. There is no uncontrolled infinite direct-sum topology
in this resolution. It is bounded above, and all differentials and
augmentation contractions are continuous degree by degree.

Bounded-above complexes of relative projectives are relative K-projective.
To see this, a map into an admissibly acyclic complex is null-homotopic
by downward induction from the highest degree: at each stage the
remaining component lands in cycles, and relative projectivity lifts
it through the admissible differential onto those cycles. This also
proves comparison and uniqueness up to homotopy for (1). Thus projective
resolutions give actual models for the relative derived category.

## 3. Derived composition, associativity and unit

Define

    M star N=Q(M) tensorhat_A Q(N)                         (2)

with the ordinary cochain totalization. Each degree again has finitely
many summands since both complexes are bounded above. A tensor of two
relatively free bimodules is relatively free:

    (A tensorhat V tensorhat A) tensorhat_A
    (A tensorhat W tensorhat A)
        =A tensorhat V tensorhat A tensorhat W tensorhat A.

The maps are multiplication of the balanced middle factors and insertion
of a unit for the inverse. Thus (2) remains a bounded-above complex of
relative projectives.

These complexes are also relatively K-flat on either side. For a single
free term, tensoring reduces to tensoring a continuously split complex
of spaces by fixed complete spaces; the explicit splitting is preserved.
For a bounded-above complex of free terms, the usual double-complex
contraction follows by perturbing this vertical contraction by the
horizontal differential. The perturbation raises the projective-term
index and therefore terminates at its upper bound, on every input and
in every fixed total degree. All resulting maps in that degree are
finite sums of continuous maps. Retracts satisfy the same property.
This proves that (2) is independent of resolution in D_rel^-.

The associator is the canonical associator of the three completed
balanced factors on projective models. Closed balancing relations give
the same completed quotient of the triple projective tensor in either
order. It commutes with the total differential and satisfies the pentagon
on elementary tensors, hence everywhere by continuity. Its unit is the
actual bimodule A: augmenting its bar resolution gives

    A star M ~= M ~= M star A.                            (3)

Mapping cones and shifts are preserved with the standard tensor signs.
This constructs a triangulated monoidal derived category on the common
source, with actual continuous complex models and a two-sided unit.
It does not assert a complete locally convex topology on arbitrary
localized Hom spaces or that their homotopy quotients are Hausdorff.

## 4. One cyclic derived shadow of the same composition

For a complex M define its relative diagonal shadow by the total complex

    Tr_A(M)=Tot [M tensorhat A^(tensorhat n)]_(n>=0),      (4)

with Hochschild and internal boundaries and total degree i-n. The same
finite-diagonal argument makes every degree a finite sum of complete
Frechet spaces. Relative projective resolution comparison, as in
P123.066, makes (4) the relative derived diagonal tensor; it respects
admissibly acyclic replacements and mapping cones.

The double-bar comparison of P123.067–069 applies on this common algebra
and to these bounded-above complexes. Its typical word is
M tensorhat A^r tensorhat N tensorhat A^s, with suspended bar factors.
Rotation exchanges the two segments with their Koszul sign and identifies
the two cyclic total complexes. Contracting the redundant bar resolutions
on either side yields

    Tr_A(M star N) ~= Tr_A(N star M).                     (5)

All multiple-bar total degrees remain finite because the internal degrees
are bounded above. Thus the same unit insertions and finite perturbations
prove continuity and the coherence of the rotations. This is an actual
cyclic shadow of (2), not a scalar value selected for a later arithmetic
correspondence. On degreewise nuclear modules it is a degreewise nuclear
complex, since the common A is nuclear and its terms are finite sums of
completed projective tensors. No determinant of an arbitrary unbounded
complex or finite scalar trace is inferred from this statement.

## 5. Semilocal functors: coherence without a false monoidal assertion

For the unital inclusion A->B supplied by P123.121 there is a defined
relative derived induction

    I_(A,B)(M)=B tensorhat_A^L M tensorhat_A^L B.           (6)

The relative bar model defines it on all continuous bimodule maps;
there is no attempt to extend an old intertwiner by reusing its scalar
coefficient. For A->B->C, association and the identity of B as a
B-module give I_(B,C) I_(A,B) ~= I_(A,C), coherently on triples.
These are well-typed derived functors of the algebra embeddings.

They are not automatically strong monoidal. In fact composition of
I(M) and I(N) over B has the middle factor B, regarded as an A-bimodule,
whereas I(M star N) has the middle factor A. Inserting A->B gives the
natural comparison from I(M star N) to I(M) star_B I(N); multiplication
also gives I(A)=B tensorhat_A^L B -> B. Neither is asserted invertible.
This retains the earlier induction obstruction instead of replacing it
by an unproved base-change identity. Full monoidal descent needs more.

## 6. The source involution is not silently a contravariant duality

There is a defined conjugate opposite bimodule T(M), with elements
bar m and actions a bar m b=overline(b^* m a^*). It preserves exact
sequences and continuous maps, reverses tensor order, and T^2=identity.
It therefore supplies an involutive reversal of source composition.
On morphisms it is covariant: a map M->N induces T(M)->T(N).
It must not be called the contravariant dagger required in A.4.
A contravariant duality, with reflexivity and order reversal on a suitable
geometric subcategory, remains an additional construction. Infinite
Frechet modules cannot be declared dualizable from (1)–(5).

## 7. Position in the unchanged A requirements

This establishes a relative derived category, associative composition,
unit and cyclic diagonal complex on the common semilocal source itself,
with coherent, explicitly non-strong-monoidal induction functors.
The designated smooth single-zero layer is the one already identified
in P123.120–121; its perfect/periodic computations are available for a
future excision and localization comparison.

The category of all these bimodules is not asserted to be the required
geometrically localized correspondence category on the noncollapsed
square. Such localization, the true contravariant duality, admissible
trace-class/determinant subcategory, numerical radical, source effectivity,
classical comparison, and mixed RR metric identity remain load-bearing
requirements. This construction supplies the common derived operations;
it does not certify the full A tuple by changing those requirements.

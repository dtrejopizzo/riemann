# P123.125 — Finite projective Cech models for the closed zero-stratum quotients

Date: 2026-09-07. Status: PROVED-IN-REPOSITORY for the common source,
coordinate-open arrangements, and the relative exact structure of P123.122.
The assertion is a derived quotient/localization theorem for that source;
it does not erase the nonzero closed strata or establish mixed RR.

## 1. Coordinate-open arrangements in the original algebra

Let A=A_sm^u(P), with the ideals I_J of P123.124. Choose a finite
nonempty list J_1,...,J_m of subsets of P, and set

    O=union_(a=1)^m U_(J_a),
    I_O=sum_(a=1)^m I_(J_a),      B_O=A/I_O.               (1)

The sum is a closed ideal and the quotient is continuously linearly
split. To see this directly, use the finite coefficient decomposition
of P123.121: label a summand by the subset L of coordinates carrying
F_p, all other coordinates carrying chi_p. The ideal I_J consists
exactly of summands with J contained in L, together with their real
coefficient and rapid lattice factors. Thus I_O is the finite direct
sum of summands for which some J_a is contained in L. Projecting onto
these summands is continuous in all source seminorms. The scalar lattice
summand of A is separate and is not in I_O.

This is a vector-space decomposition for the proof, not a decomposition
of A as a product of independent stratum algebras. The dilation attaching
terms of P123.121 mix these coefficient summands.

## 2. A finite admissibly exact augmented resolution

For a nonempty subset T of {1,...,m}, put J_T=union_(a in T) J_a.
Form the augmented complex of right A-modules

    P_O^0=A,
    P_O^(-n)=direct_sum_(|T|=n) I_(J_T), 1<=n<=m,
    P_O^0 -> B_O,                                        (2)

with the alternating inclusion maps. The degree -1 differential is
the sum of the ideal inclusions into A. Repeated deletion of two indices
cancels with opposite signs, so the differential squares to zero.

This complex is admissibly exact. On a coefficient summand L, define
A_L={a: J_a contained in L}. If A_L is nonempty, (2) on that summand
is the augmented simplex chain complex on the finite vertex set A_L.
It contracts by inserting its least vertex, with the usual orientation
sign and zero for repeated vertices. If A_L is empty, only the A to
B_O identity on that summand remains. The scalar lattice summand has
the same latter form. These contractions, combined with the continuous
finite summand projections, give a continuous linear contraction of the
augmented complex. They need not be A-linear; that is exactly the
admissibility condition of P123.122.

Every negative-degree term is relatively projective on the right by
P123.124, and A is free. Hence (2) is a finite relative projective
resolution of B_O as a right A-module. The same construction works
on the left. It retains the actual quotient and all its residual
lattice actions.

## 3. The derived self-tensor of the quotient

Every ideal I_(J_T) in a negative degree of (2) satisfies

    I_(J_T) tensorhat_A B_O=0.                            (3)

Indeed choose a in T. P123.124 gives the surjective multiplication
I_(J_T) tensorhat_A I_(J_a) -> I_(J_T), since J_a is contained in J_T.
After tensoring with B_O, each balanced elementary product is zero
because I_(J_a) annihilates B_O. The continuous product splitting in
P123.124 extends this to the whole completed tensor, proving (3).

Tensor (2) with the left module B_O. The resulting complex is B_O in
degree zero and zero in every other degree. Therefore the multiplication
counit is a relative derived isomorphism

    B_O tensorhat_A^L B_O ~= B_O.                         (4)

In particular the higher relative Tor groups in this self-tensor vanish.
This conclusion follows from the displayed projective resolution;
surjectivity of A->B_O or density in another algebra is not its proof.
It is entirely different from the semilocal injection obstruction in
P123.123: (4) concerns these quotient maps, not prime-adjoining embeddings.

## 4. One-sided derived localization and its exact domain

For bounded-above right module complexes, restriction from B_O to A
has left adjoint - tensorhat_A^L B_O. Equation (4) gives the counit
isomorphism on every such B_O complex N:

    Res(N) tensorhat_A^L B_O
       ~= N tensorhat_B_O^L (B_O tensorhat_A^L B_O) ~= N.  (5)

These identifications can be obtained directly by the relative bar
models; hence they use the same linearly split exact structure at both
algebras. Derived restriction is fully faithful: the adjunction and
its invertible counit identify the morphisms between restricted objects
with their original derived B_O-module morphisms. The analogous left
module assertion holds.

The complexes annihilated by this quotient functor, and the quotient-
supported complexes in its essential image, are thus specified by actual
derived operations. This is a derived localization statement on the
common source. It does not claim that arbitrary two-sided coefficient
extension preserves composition of all correspondences. An intermediate
correspondence can pass through the removed region and return, and (4)
alone does not identify every such composition after two-sided projection.

## 5. All zero-count closed layers are covered

For the closed set F_k with at least k zero coordinates among r=|P|,
its open complement is the union of U_J over subsets J of size r-k+1,
for 1<=k<=r. Apply sections 1–4 to this finite list. The quotient
B_O is the coefficient-unitized restriction of the common source to
F_k, with its original Gamma action. Thus every such zero-count closed
restriction has an explicit finite projective model and satisfies (4).
Intersections and unions of these coordinate opens are handled by the
same formulas. Redundant generators do not change B_O or the resulting
derived functor; the resolution is a model for that canonical quotient.

For nested closed loci, the quotient algebra maps compose literally.
The derived localization functors and their multiplication counits
compose by associativity of the relative bar tensors, hence coherently
on triples. If one further removes the entire coefficient carrier,
the remaining quotient of A is its scalar lattice algebra, not zero.
This keeps the coefficient-unitization/Tate sector explicit.

## 6. Relation to the unfinished A theorem

This supplies actual derived quotient comparisons for every finite-zero
closed layer of the common source, using one finite coordinate system
and admissibly split Cech resolutions. The higher-zero algebras and their
return actions remain in the quotients; (4) is not a vanishing theorem
for their traces or their diagonal homology.

Together with P123.124 it provides localized open ideals and closed
restriction models compatible with the source multiplication. It still
requires the full geometric correspondence descent on the square, its
contravariant duality, the specified cyclic/excisive trace and determinant
comparison, numerical/effectivity structures, and the intrinsic mixed RR
metric. Those are not consequences of one-sided derived localization
and are not declared proved here.

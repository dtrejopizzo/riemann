# P123.081 — Exact chart correction for the Tate excess determinant

Date: 2026-09-06. Status: PROVED for the finite Tate models of P123.080,
including their coherent determinant transitions. No analytic metric
or general mixed-correspondence RR is asserted.

For one Tate fiber put C_S=exterior^* V_S with exterior degree k in
cohomological degree -k, and E_S=Cone(C_S -> C), where the map is
identity in degree zero. Use the reduced model of E_S: exterior^k V_S
in degree -k-1 for k>=1. For the two Tate fibers take two copies of
every formula below. The bar/Koszul comparison of P123.076–080 identifies
these with the stated strict derived objects.

If T=S union {ell}, write V_T=V_S direct_sum C epsilon_ell. Order the
new generator after the old ones and define the chart map by the exterior
inclusion. There are exact decompositions of zero-differential complexes

    C_T=C_S direct_sum (C_S tensor C epsilon_ell)[1],
    E_T=E_S direct_sum (C_S tensor C epsilon_ell)[2].

The second follows because the new summand maps to zero under the
augmentation to C and the mapping cone shifts that summand once more.
It is also immediate in degree -k-1 by decomposing exterior^k V_T.
Hence the relative chart cone has the explicit finite model

    Cone(E_S -> E_T) ~= (C_S tensor C epsilon_ell)[2].

The contractible cone of identity on E_S has been removed here by its
explicit standard contraction. Thus chart transport of the excess
complex is not a quasi-isomorphism; the missing summand is now specified.

Determinant multiplicativity gives the exact line comparison

    det E_T ~= det E_S tensor det(C_S tensor C epsilon_ell).

For nonempty S, the Euler characteristic of C_S is (1-1)^|S|=0, so
tensoring by the new one-dimensional generator contributes no power of
that line to the determinant. Also

    det C_S ~= (det V_S)^(-1) if |S|=1,

whereas for |S|>=2 its exterior-basis determinant is naturally trivial
under the same fixed graded ordering convention as P123.080. Therefore
the first new-prime transition precisely cancels the one-prime factor
in det E_S; later transitions have canonically trivial underlying
correction lines. Their correction complexes remain nonzero. For the
two Tate fibers these line formulas are tensor-squared, and the virtual
rank of the excess remains two, as previously computed.

For several added primes W, decompose the exterior algebra by subsets
J of W. In C_T the J component is C_S tensor det(C^J)[|J|]; in the
relative excess it is C_S tensor det(C^J)[|J|+1] for J nonempty.
This single decomposition refines every order of adding the new primes.
Exterior permutation signs and the graded determinant signs implement
the corresponding reorderings, proving chart-triple coherence. This is
an equality of determinant comparisons induced by actual finite complexes,
not an assumed equality of numerical degrees.

The coefficient maps on normalized scalar bar complexes carry the
old prime generators to themselves and commute with evaluation. Thus
the finite chart inclusion above represents that bar-level map under
the Koszul comparison. The full-source comparison in P123.079–080 is
induced by the same e and j maps and commutes with old-label charts;
no new full-Hom correspondence transport is implied by this statement.

This computes the semilocal correction to this Tate excess determinant.
It does not equip the line with the intrinsic ruling metric, establish
a mixed determinant functor for general correspondences, or show that
these finite corrections equal the geometric trace terms of RR. Those
remain necessary to close A.8. In particular triviality of an underlying
correction line does not mean its complex or its possible metric
contribution can be discarded.

# P123.020 — normalized idele transitions and gauge-generated functors


## Status

`PROVED-IN-REPOSITORY` for the explicit normalized class maps, compatible
unital rapid coefficient embeddings, Tate characters, and chart functors
on the **gauge-generated** correspondence category defined below.

`OPEN` for descent of arbitrary complete bimodules, extension to all their
intertwiners, completed smooth section categories, and the comparison of
traces. This is a repair of the displayed maps in P123.014, not acceptance
of the former full completed-stack claim.

## 1. A multiplicative normal form over Q

Use Gamma_S^+ and A_S^u from P123.019. For a=(a_v) in A_S^times put

    r_S(a)=product_(p in S_f) p^(v_p(a_p)),
    N_S(a)=r_S(a)^(-1) a.

Here r_S(a) is a positive rational S-unit embedded diagonally. Each finite
component of N_S(a) belongs to Z_p^times. For gamma in Gamma_S^+,

    r_S(gamma a)=gamma r_S(a),
    N_S(gamma a)=N_S(a).

Both r_S and N_S are multiplicative and continuous: the finitely many
valuations are locally constant. Consequently every class has exactly one
representative in

    H_S = R^times times product_(p in S_f) Z_p^times.

Uniqueness follows because a positive S-unit which is a unit at all finite
S-places equals 1. The decomposition a=r_S(a) N_S(a), with both factors
continuous, proves a topological group isomorphism

    A_S^times = Gamma_S^+ times H_S,
    C_S^+ = Gamma_S^+ backslash A_S^times ~= H_S.

This uses the rational primes and positive normalization in Q. It does not
supply a canonical principalization of ideals in an arbitrary number field.
The existence of this splitting also shows that a nontrivial lift cocycle
is not an intrinsic necessity on these semilocal Q charts: the normalized
section is a group homomorphism. Other sections can still produce cocycles.

## 2. Corrected maps on lifts and classes

For S subset T define

    L_ST(a)_v = a_v               (v in S),
    L_ST(a)_v = r_S(a)            (v in T minus S).

Each new component is a unit at its new prime. Thus

    r_T(L_ST(a))=r_S(a),
    N_T(L_ST(a))=(N_S(a),1_new).

L_ST is a continuous group homomorphism. It satisfies

    L_ST(gamma a)=gamma L_ST(a),
    L_TU L_ST = L_SU.

The first identity is literal equality at both old and new components.
The second uses r_T(L_ST(a))=r_S(a). It therefore descends to an injective
continuous class homomorphism i_ST:C_S^+ -> C_T^+. In normal coordinates
this is extension by 1; **it is not extension by 1 of an arbitrary lift**.
The inverse onto its image is coordinate projection in those normal
coordinates, so i_ST is a topological embedding.

For the P123.018 example, (1,1) maps to (1,1,1), while (2,2) maps to
(2,2,2). The images now differ by the diagonal gauge 2, as required.

## 3. Compatibility with the actual coefficient maps

Let R_new=product_(p in T minus S) Z_p. Define

    j_ST(f+c1)=f tensor 1_Rnew + c1

on B_S^+, then coefficientwise on the old group labels to A_S^u -> A_T^u.
The image has zero coefficients at labels outside Gamma_S^+.

This is a unital star homomorphism. Multiplication of coefficients works
because 1_Rnew is idempotent. Its norm is the old coefficient norm:
inside R_new the old function is recovered; outside it the value is c,
and |c| is already bounded by ||f+c||. Hence j_ST is isometric at every
p_k, j_TU j_ST=j_SU, and j_ST restricts to the old P123.006 map on K_S.

For gamma in Gamma_S^+, gamma is a unit at all new places. This proves
gauge equivariance and j_ST(U_gamma)=U_gamma. More generally r_S(a) is
also a unit at all new places, so it preserves 1_Rnew. Therefore

    beta_(L_ST(a)) j_ST = j_ST beta_a.                 (3.1)

This is where the relation with coefficient restriction is proved. The
changed new idele components do not change the characteristic function of
the added integral coordinates.

## 4. Exact scope of the categorical functor

Define G_S as the presentation groupoid with objects idele lifts a and a
specified arrow gamma:a' -> a when a'=gamma a. Represent it by E_(beta_a)
over A_S^u and the right-multiplication map x |-> x U_gamma. Tensor is the
product of lifts with the coherent tensor isomorphism of P123.019.

The assignments

    a |-> L_ST(a),    gamma |-> gamma

define a monoidal functor of these groupoids. Their bimodule realizations
are compatible with j_ST via the continuous semilinear maps

    E_(beta_a) -> E_(beta_L(a)),   x |-> j_ST(x).

Equation (3.1) proves compatibility with both actions. The images of gauge
arrows are genuine bimodule intertwiners for **all** target coefficients,
since L_ST(gamma a)=gamma L_ST(a). Tensor compatibility is

    j_ST(x beta_a(y))
      =j_ST(x) beta_L(a)(j_ST(y)).

Inversion/star and the formulas for L imply dagger compatibility. Triple
chart composition is strict in these coordinates.

One may take the complex linear, finite additive and idempotent envelope
of the gauge-generated morphisms: matrices of these arrows remain
continuous; continuous idempotents have closed complete ranges; all
relations are preserved under j_ST. This yields a specified, generally
**non-full** category of realized bimodules with chart functors.

Do not infer a functor on the full category of arbitrary bimodule maps.
For an arbitrary intertwiner t, j_ST(t) is only known a priori to intertwine
j_ST(A_S^u), not all A_T^u. Nor does a unital embedding of algebras by itself
prove a Morita equivalence or effective stack descent. These remain distinct
obligations if the later construction needs them.

## 5. Norm, Tate and sign

The semilocal norm is

    |a|_S=|a_infinity| product_(p in S_f) p^(-v_p(a_p)).

Since r_S(a) is an S-unit, product formula gives |r_S(a)|_S=1.
All new components of L_ST(a) have new-place norm 1; consequently

    |L_ST(a)|_T=|a|_S=|N_S(a)_infinity|.

The two Tate characters |a|_S^(+-1/2) descend and commute with every i_ST.
This proves the boundary-character compatibility, not a mixed intersection
or a ruling embedding.

For full S-units set r_S(a)=sign(a_infinity) product p^v_p(a_p). The same
proofs hold, with H_S=R_+^times times product Z_p^times. Positive and full
unit conventions must still be kept separate in comparisons.

## 6. Global-group boundary: direct limit is not the full class group

The union of H_S under extension by 1 contains only finite-support tuples
of local units. It is a proper subgroup of

    H_global^+ = R^times times product_p Z_p^times.

For example infinitely many nonidentity unit components cannot lie in that
union. Its inductive-limit topology must not be identified with the product
topology of H_global^+ without a theorem.

There is a compatible global normalized action on the coefficient system:
for h in H_global^+, act on A_S^u through its S-components. At new places
h_p is a unit and preserves 1_Zp, so these actions commute with j_ST.
Continuity on each chart follows from the finite projection to H_S and
P123.019. This constructs the action on each algebra and compatibility;
it does not by itself prove continuity on an unspecified completed global
section category.

For a full rational idele, the valuation product r(a)=product_p p^v_p(a_p)
is finite. Normalizing by it proves directly
Q_+^times backslash A_Q^times ~= H_global^+ (or the positive-real variant
for all Q^times). This standard normal form is consistent with the general
idele norm formalism; see [class-field notes, idele section](https://math.uchicago.edu/~linus/cft11.pdf).
The elementary formulas above are the proofs needed here.

## 7. Acceptance consequence

The two explicit failures in P123.018 have replacements: P123.019 changes
the algebra so gauge maps are defined; this note changes the lift transition
so it is gauge equivariant and preserves the coefficient system.

The repaired result is a coherent diagram of gauge-generated local
correspondence categories with complete Frechet coefficient algebras.
It is not a theorem of arbitrary kernel descent, completed Fell topology,
trace comparison, integral effectivity or RR. Those gates remain open.

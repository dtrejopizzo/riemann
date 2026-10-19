# P123.123 — Semilocal unit obstruction and equivariant crossed composition

Status: PROVED-IN-REPOSITORY for the actual common
source inclusions and the tempered equivariant domains specified below.
This repairs transport through the added lattice on that domain. It does
not assert that every old correspondence already has the needed lift.

## 1. The old induction really fails the unit test

Let A=A_sm^u(P) and B=A_sm^u(T), with a new prime ell in T minus P.
On B define the continuous label derivation

    delta_ell(sum_gamma b_gamma U_gamma)
       =sum_gamma v_ell(gamma) b_gamma U_gamma.            (1)

The valuation is additive under multiplication of labels, so (1) is
a derivation for the original crossed product. It is continuous because
|v_ell(gamma)| is bounded by a constant times one additional height
weight. It vanishes on the image of A, whose labels are in Gamma_P.

Consequently b tensor c -> b delta_ell(c) is a continuous A-balanced
map B tensorhat_A B -> B. Indeed delta_ell(a c)=a delta_ell(c) for
a in A. It annihilates closed balancing relations. For the actual new
gauge unitary U_ell, the element

    x=U_ell tensor 1-1 tensor U_ell                       (2)

has image -U_ell under that map, so x is nonzero. Multiplication sends
x to zero. Thus B tensorhat_A B -> B is not injective.

The same witness lives in degree zero of the bar model for
B tensorhat_A^L B: the map (1) annihilates every degree-one bar boundary,
while evaluating (2) nontrivially. Its degree-zero homology class is
therefore nonzero and killed by the multiplication augmentation. Hence

    B tensorhat_A^L B -> B                               (3)

is not a relative quasi-isomorphism. This is a concrete failure of the
unit comparison for the induction in P123.122 on the actual source,
not merely the absence of a proof. A strong monoidal chart functor
cannot be obtained by declaring (3) invertible.

## 2. Factor out the new lattice without changing its coefficients

Retain the full coefficient algebra E_T direct_sum C of P123.121,
but first cross it only with the old lattice Gamma_P. Call that algebra
C. Let G=Gamma_(T minus P), written additively as Z^d. New-prime dilation
acts on C by automorphisms alpha_g, using the actual action on E_T and
commutation with the old labels. These actions have the tempered bounds
of P123.121 (7). There is a topological algebra identification

    B = C crossed_rapid G.                               (4)

In (4), rapid means all weighted sums exp(k||g||_1) nu(c_g). Joint
old/new label weights and the original height weights are cofinal:
log H is between one half and one times the sum of the absolute prime
exponents times their logarithms. Iterated and joint weighted sums
therefore give the same topology and crossed multiplication.
The map A->C still includes the new coefficient cutoffs. It is not
assumed to be a strong monoidal coefficient extension. Formula (4)
is the portion of transport addressed in the next sections.

## 3. The objects must carry the new action

A tempered G-equivariant C-bimodule M is a complete Frechet bimodule
with a representation rho_g satisfying

    rho_g(c m d)=alpha_g(c) rho_g(m) alpha_g(d),
    p(rho_g m)<=K exp(k||g||_1) p'(m)                     (5)

for each seminorm p and suitable p',k,K. Morphisms are continuous
C-bimodule maps commuting with these representations. The action on
M tensorhat_C N is the diagonal action; projective quotient seminorms
and (5) prove it is again tempered. The tensor unit is C with alpha.

Define M crossed_rapid G as the rapidly weighted M-valued sequences,
with actions

    (c U_g)(m U_h)=c rho_g(m) U_(g+h),
    (m U_g)(c U_h)=m alpha_g(c) U_(g+h).                  (6)

The estimates (5) and convolution of label weights prove continuity
and completeness. Semilinearity proves the two actions commute and
are associative. This is a B-bimodule, with B the actual algebra (4).

## 4. An invertible composition comparison, with its inverse

There is a topological B-bimodule isomorphism

    (M crossed G) tensorhat_B (N crossed G)
           ~= (M tensorhat_C N) crossed G,               (7)

given on finite elementary tensors by

    (m U_g) tensor (n U_h)
            -> (m tensor rho_g(n)) U_(g+h).              (8)

Here rho on n denotes the specified action on N. The inverse is

    (m tensor n) U_k -> (m U_0) tensor (n U_k).            (9)

The map (8) is balanced over coefficients by semilinearity and over
gauge unitaries by the group law. Formula (9) is C-balanced. Applying
(9) after (8) recovers the original tensor, since balancing over the
actual B unit U_g gives

    (m U_0) tensor [U_g(n U_h)]
       =[(m U_0)U_g] tensor(n U_h).

The other inverse identity is immediate. To justify the completions,
exp(k||g+h||)<=exp(k||g||)exp(k||h||), while rho_g costs only a higher
exponential g weight by (5). This bounds (8) in every projective target
seminorm by a pair of source seminorms. For (9), its projective seminorm
at label k is bounded by exp(k' ||k||) times the corresponding balanced
projective seminorm of m tensor n. Summing these bounds proves absolute
convergence and continuity. Thus the inverse identities extend by
density to the declared completed tensors.

With M=C, the crossed module is B. The maps (7) preserve this unit
exactly. For three objects, both associated maps send a tensor of labels
g,h,k to

    (m tensor rho_g(n) tensor rho_(g+h)(z)) U_(g+h+k).

This proves associativity coherence; the same identity proves the
pentagon. Iterating commuting added lattice directions is likewise
independent of their order when the full commuting G-action is given.

## 5. Relative derived extension: no flatness assumption is omitted

Take bounded-above complexes of the equivariant modules (5), with
equivariant differentials. The left/right bar resolution over C has
the diagonal G action, is tempered in each degree, and has the same
continuous underlying augmentation contraction as P123.122. It need
not be projective for every exact structure on equivariant modules;
only its stated underlying C-module flatness is used here.

After crossing, each of its terms is free on either individual B side.
Indeed if a left C-free term is C tensorhat V with its diagonal G
action, the map

    B tensorhat V -> (C tensorhat V) crossed G,
    (c U_g) tensor v -> (c tensor rho_g(v)) U_g            (10)

is a continuous left B-module isomorphism. Its inverse uses rho_(-g).
The rapid sequence/projective tensor identity follows by absolutely
convergent coordinate tensors in each weighted seminorm; (5) bounds
both maps. The right-free version is proved the same way. Apply this
to V equal to all the remaining factors of a bimodule bar term.

Crossing a continuous underlying linear contraction preserves it
coefficientwise; its seminorm bound is independent of the label. Hence
crossed bar resolutions still resolve the crossed objects in the
linearly split relative structure. By (10) their terms are relatively
flat on both B sides, and the bounded-above contraction argument in
P123.122 makes them relative K-flat. They therefore compute the actual
relative derived tensor over B.

Apply (7) termwise to these resolutions and totalize, with finitely
many summands in each degree. This proves

    (M crossed G) tensorhat_B^L (N crossed G)
         ~= (M tensorhat_C^L N) crossed G.                (11)

The unit and associativity coherences descend from (8)–(10). Replacements
with underlying continuously split acyclic cones are preserved. Thus
(11) is a genuine derived monoidal transport on the declared equivariant
domain, not the noninvertible induction of section 1.

## 6. The remaining semilocal burden is precisely identified

The added lattice part of the actual common source now has composition-
preserving transport, provided a correspondence is first defined over
C and supplied with a tempered semilinear action of the new generators.
The two required data are essential. An arbitrary A-bimodule does not
come with either a C-bimodule lift or the operators rho_g. Assigning them
without a construction would skip the remaining coefficient/geometric
extension problem. Moreover the maps (11) do not supply determinant,
trace-class, numerical or metric descent on their own.

This gives an explicit repair for one failed mechanism, and a concrete
nonzero witness excluding its naive alternative. Full row A still
requires the geometric admissible class, its compatible coefficient
lifts and duality, and the mixed RR determinant and ruling metric.

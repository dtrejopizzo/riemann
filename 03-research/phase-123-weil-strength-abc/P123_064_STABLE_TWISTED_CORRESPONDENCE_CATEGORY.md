# P123.064 — A stable enlargement of the repaired twisted correspondences

Date: 2026-09-06. Status: CONSTRUCTED at fixed S, with continuous dg
composition and a tensor unit. This addresses the stable-category part
of A.2–A.3, not the whole localization, descent or RR contract of A.

## 1. Full morphisms at fixed source algebra

Let A be the repaired unital Fréchet algebra of P123.019, or the
two-prime integrable unital algebra of P123.053. For an external
automorphism beta write E_beta={}_1 A_beta. A continuous bimodule map
E_beta -> E_eta is uniquely right multiplication by an element v in A
satisfying

    beta(a)v=v eta(a) for all a in A.             (1.1)

Indeed left linearity gives f(x)=xf(1), and right linearity is exactly
(1.1). Conversely multiplication by such v is continuous. Give this
intertwiner space its closed-subspace topology in A: it is the
intersection of the kernels of the continuous maps
v -> beta(a)v-v eta(a). It is therefore complete and Fréchet.

Finite direct sums of the E_beta have matrix intertwiner spaces, with
the corresponding complete finite-product topology. Composition is
continuous matrix multiplication, with the multiplication order obtained
from right multiplication: f_w composed with f_v sends x to x v w.
This is a full morphism calculation at fixed A, not the previously
refuted assertion that every such morphism extends under a chart map.

## 2. Bounded twisted complexes and cones

Define C_tw(A) to have objects bounded cochain complexes whose terms
are finite direct sums of E_beta and whose differentials are the
intertwiner matrices of section 1, with d²=0. Its dg Hom space has

    Hom^r(K,L)=product_i Hom_(A-A)(K^i,L^(i+r)),
    partial f=d_L f-(-1)^r f d_K.

All products here are finite. The differential and composition are
continuous, and partial²=0 follows by cancellation using d_K²=d_L²=0.
Shifts remain in the category. For a closed degree-zero map f:K -> L,
the cone has terms L^i plus K^(i+1) and differential matrix

    [ d_L   f ]
    [  0  -d_K].

Its square vanishes by the chain-map identity. Thus shifts, finite sums
and cones are actual objects of this dg category, rather than formal
labels outside it. Its degree-zero homotopy category has the usual cone
triangles of bounded complexes. We do not quotient its Hom spaces by
possibly nonclosed boundaries and then assert a Hausdorff topology;
the declared topological enrichment is the complete dg Hom complex.

## 3. Continuous tensor composition of the complexes

For elementary terms use the completed balanced tensor isomorphism
of P123.019 or P123.053,

    E_beta tensor_A E_eta ~= E_(beta eta),
    x tensor y -> x beta(y).

Define K star L by the finite direct-sum totalization of these tensors,
with differential

    d(x tensor y)=d_K x tensor y+(-1)^i x tensor d_L y,
                     x in K^i.

The two mixed terms in d² cancel and the other terms vanish. Tensoring
continuous bimodule maps is balanced and continuous on the completed
projective quotient, so the differentials are again admissible maps.
Finite direct sums commute with the construction, keeping every term
in the same category.

The complex A in degree zero is the two-sided tensor unit. The termwise
associator sends either parenthesization to x beta(y) beta eta(z);
it commutes with the total differentials and has the same coherence
as the elementary associator. On homogeneous dg morphisms use the
Koszul convention (f tensor g)(x tensor y)=(-1)^(deg(g)deg(x))
f(x) tensor g(y); this gives the dg tensor interchange identity.

The tensor functors preserve shifts and mapping cones with these
standard totalization signs. In addition each elementary E_beta is
rank one free as a left module and isomorphic to a rank one free module
as a right module by untwisting beta. Thus bounded complexes of these
terms are algebraically K-flat on each side. This last statement is
about algebraic derived tensor, not an automatic exactness theorem for
every topological completed tensor product.

## 4. Scope of the declared completion and remaining A requirements

All coefficient and dg Hom spaces use the actual completed topology of
A. The objects use finite sums and bounded cones; no infinite-object
completion, Karoubi completion, arbitrary perfect-kernel identification
or nuclearity is asserted. The construction genuinely enlarges the
single-automorphism objects to a dg category closed under stable
operations at fixed S. It is independent of a chosen arithmetic family,
prime-contact values or the desired sign.

The outstanding work is geometric localization of this enlargement,
compatible semilocal transport of its full intertwiner spaces, the
appropriate dagger on the enlarged category, and a diagonal shadow
with the numerical, effectivity and mixed RR requirements of A.5–A.9.
The old full-Hom chart counterexample still applies unless a new
transport operation is proved; this category alone does not remove it.
Accordingly A remains open under its unchanged acceptance specification.

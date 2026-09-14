# P123.100 — Derived finite-unit transitions with every deck graph retained

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY for finite unit
refinements of the smooth boundary mapping tori. The completion over
all levels and the arithmetic normal determinant remain separate.

## 1. Finite covering and its entire lifted diagonal

Use M contained in N, Y_M->Y_N and B_L=C^infinity(Y_L) from P123.099.
The covering is the quotient by the finite unit group H=N/M. Its action
is free: a unit translation fixing a point of the mapping torus would
require zero real displacement in (1) of that note, hence the trivial
deck element. It follows that

    (pi times pi)^(-1)(Delta_N)
       =disjoint_union_(h in H) Gamma_h,
    Gamma_h={(y,h y): y in Y_M}.                             (1)

Each component is a closed embedded circle union; distinct deck graphs
are disjoint. Smooth functions on this lifted relation consequently
split as a finite direct sum of graph modules.

Write R_L=C^infinity(Y_L times Y_L). Pullback makes R_M a finite
projective R_N-module. To verify this, locally trivialize the finite
cover of product manifolds: over each evenly covered set its smooth
function module is free with basis the sheet indicators. A finite
partition of unity gives finitely many global generating sections of
the associated finite-rank bundle and a continuous splitting of the
surjection from a finite free module, as in P123.095. Thus tensoring
with R_M is exact on the relevant split smooth resolutions; no arbitrary
Frechet flatness assertion is needed here.

## 2. Explicit maps of finite free resolutions

Let g_N generate the coarse diagonal ideal as in P123.099, and set
g=(pi times pi)^*g_N. Its zeros are exactly (1), and its derivative
normal to each graph is nonzero, since pi is a local diffeomorphism.
Consequently

    K=[R_M --g--> R_M]

resolves the smooth functions on the lifted relation. Smooth division
is continuous on the vanishing ideal, by local transverse integration
as in P123.098, followed by a finite partition of unity.

For each h choose a global smooth graph generator g_h: pull the diagonal
generator on Y_M times Y_M back by (y,z)->(y,h^-1 z). It has a simple
zero precisely on Gamma_h. The quotient k_h=g/g_h extends smoothly
across that graph by the same division argument. It defines a chain map

    K -> K_h=[R_M --g_h--> R_M],
    degree 0: identity,    degree 1: multiplication by k_h.  (2)

The chain identity is g_h k_h=g. Combining (2) for every h gives

    K -> direct_sum_(h in H) K_h.                           (3)

On degree-zero homology this is precisely simultaneous restriction to
the disjoint graphs, which is an isomorphism by (1); all other homology
vanishes. It is a homotopy equivalence of bounded finite free complexes.
Indeed its cone is bounded, exact and finite projective, so induction
from an endpoint splits it and constructs a contracting homotopy.
These module splittings are continuous: maps from finite free modules
are finite tuples of smooth coefficients, and maps between projective
summands have the inherited continuous topology.

Thus (3) proves the entire derived base-change decomposition, including
all extra graphs, in the declared completed smooth framework.

## 3. Selecting the actual diagonal is a specified morphism

The identity element of H singles out Gamma_1=Delta_M. Projection to
that summand of (3) is the canonical derived restriction

    R_M tensorhat_(R_N)^L B_N -> B_M.                       (4)

It is a projection, not an assertion that every other summand is zero.
Its action on conormal lines is the differential of pi. In the physical
coordinate t this is dt->dt, agreeing with P123.099; the multiplier
k_1 in (2) records the corresponding change of a chosen graph generator.

For a tower L contained in M contained in N, the maps (4) compose:
both routes restrict a smooth function on the fully lifted relation to
the actual diagonal of Y_L. At the level of resolutions, lifts of this
same module map are homotopic by projective-resolution comparison.
Hence the derived morphisms agree. The full decomposition also agrees:
refining graphs groups the elements of N/L according to their image
in N/M; the intermediate kernel M/L accounts for every further lift.
There is no dependence on a noncanonical choice of coset representatives
in the resulting relation or the identity-graph projection.

## 4. Moving graphs and determinant transitions

Derived pullback of (3) along the moving graph (s,y)->(y,a_s y)
gives a homotopy equivalence of perfect complexes over the smooth
parameter/base algebra:

    pullback K  = direct_sum_(h in H) pullback K_h.          (5)

This follows by tensoring the finite free chain maps and their
homotopies, so it does not assume transverse intersection after pullback.
In particular (5) remains valid at parameters with fixed points.
The identity summand is the fine-level moving diagonal; the other
summands are its intersections with the nonidentity deck graphs.

Taking determinant lines of this perfect comparison gives

    Det(pullback K)
       = tensor_(h in H) Det(pullback K_h).                  (6)

The factors are graded determinant lines, and permutations use their
Koszul signs. Formula (6) is coherent under further refinement because
the decomposition is the same disjoint lifted relation and exterior
determinants are compatible with regrouping direct sums. It supplies a
finite-level determinant correction rather than deleting extra graphs.

## 5. Remaining burden

This establishes full finite-level derived transition maps for the
smooth tangential diagonal and moving-graph families, not only their
degree-one homology map. It does not establish convergence of (6) over
infinitely many unit levels, identify a metric or a finite scalar degree,
or compare the result with the normal regularized character. Those
steps, the common completed source and multi-stratum gluing remain
necessary for the mixed RR and full row A.

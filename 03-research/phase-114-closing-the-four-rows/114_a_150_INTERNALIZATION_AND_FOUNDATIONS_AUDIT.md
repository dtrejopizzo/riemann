# Foundations and internalization audit for the valuative square

This note records the exact statements that survive a source-level audit of
the geometric carrier and of the external periodic section packet.  It is
deliberately divided into theorems and an open comparison problem.

## 1. The supportwise reflector is a small quotient

Let `A` be a commutative involutive F-ring and let `Sigma` be a finite set of
central unary scalars.  Write

`R_A = disjoint_union_(X,Y) (A_(Y,X) x A_(Y,X))`.

This is a set.  Every equality kernel of a map from `A` is a subset of
`R_A`; consequently the collection of distinct equality kernels is a set,
even though the targets range through a proper class.  Haran's equivalence
ideals are precisely equivalence relations on the operation sets stable
under composition, direct sum and involution.  Intersections preserve all
these conditions, so the intersection `E_Sigma(A)` of kernels of maps to
objects on which every member of `Sigma` acts injectively is again an
equivalence ideal.  The quotient exists by Haran, Section 8.

The quotient `A/E_Sigma(A)` is regular.  Indeed it is a subdirect product of
the images of `A` in the regular targets, and injectivity of each scalar is
inherited by subobjects and products, operation set by operation set.  A map
from `A` to a regular target kills `E_Sigma(A)`, so it factors uniquely.
This proves the universal property without forming a product over a proper
class.

For a central localization `S^{-1}A`, the two universal properties give

`S^{-1}Reg_Sigma(A) ~= Reg_Sigma(S^{-1}A)`.

The only additional observation needed is that regularity of an active
central scalar survives localization: an equality after localization can be
cleared by an element of `S`, and centrality moves the active scalar outside
the cleared equality, where it can be cancelled.

At a compactification level containing every active prime, the overlap of a
finite and a real chart inverts those primes.  Thus their injectivity is
automatic on the overlap.  The localization isomorphisms are unique, hence
obey the triple-overlap cocycle.  The index category of pairs `(T,N)` is
countable, directed and cofinite: below a fixed `(T,N)` there are only
finitely many divisors of `N` and subsets of the finite set of its prime
divisors.  It therefore has exactly the form required in Haran's definition
of a pro-scheme.

## 2. What the boundary norm proves

Haran's rank-one objects have transition functions in `GL_1(K)` and frame
changes in `GL_1(O)`.  Add the Euclidean norm at the valued real boundary
and restrict morphisms to isometries.  A frame change then has norm one.
For a finite prime vector `a=(a_p)`, the boundary transition is

`q_a = product_p p^(a_p)`.

Changing valued frames multiplies it by two norm-one units.  Therefore
`log|q_a|` is invariant.  If the valued torsor is trivial, `|q_a|=1`;
positivity and unique factorization imply every `a_p=0`.

This proves conservativity on the anti-diagonal subgroup that is the only
possible kernel after diagonal pullback.  It does **not** prove that one
mixed boundary embeds the full two-ruling lattice; that stronger wording is
unnecessary and should not be used.

## 3. External tropical dimension

For the Connes--Consani special module `E_(N,p)`, Appendix A and the proof of
their dimension theorem provide offsets `u_i` such that every one of the
`d=N-p+1` extremal generators is uniquely active on a nonempty interval.
Choose witnesses `x_i` in these intervals.  Do the same for `E_(M,q)`, with
offsets `v_j` and witnesses `y_j`.

For the external tensor, use the base coefficient matrix

`c^0_(ij)=u_i+v_j`.

At `(x_i,y_j)` the pair `(i,j)` is the unique maximizer.  Finiteness gives a
uniform positive dominance gap.  On a sufficiently small open cube around
`c^0`, evaluation at the `de` witness pairs recovers all coefficients.  This
embeds an open `de`-cell and proves the lower dimension bound.

For the upper bound, stratify coefficient space by the subset of finite
coordinates and exhaust every stratum by compact cubes.  The coefficient
map to the uniform function space is 1-Lipschitz.  Its compact images are
closed and have covering dimension at most the Hausdorff dimension of the
source cube.  The countable closed-sum theorem gives dimension at most
`de`.  Thus the dimension is exactly `de`.

The cofinal product formula follows by applying this finite-depth result to
the principal-translation/effective-inclusion squeeze in the published
periodic Riemann--Roch proof, and then dividing by the two Frobenius scaling
factors.

## 4. The precise universal property of the external packet

`PerExt` is the finite-support coproduct completion of the categories of
pairwise periodic external tensors indexed by `(p,q)`.  Hence an additive
dimension invariant on `PerExt` is uniquely determined by its restrictions
to those generators.  If the restriction is the Connes--Consani normalized
continuous dimension, its value is necessarily

`sum_(p,q) a_(p,1)b_(q,2) log(p)log(q)`.

This is a relative universal property.  It does not classify theories that
do not split supportwise, derived extensions between different prime pairs,
or archimedean correction terms.  The coefficient one is canonical inside
`PerExt`; uniqueness among all possible global section theories has not been
proved.

## 5. Principal descent: quotient theorem versus local product formula

Boundary faithfulness proves

`Div_pr = Prin direct_sum D_pr`

on the sector under consideration.  Projection to `D_pr`, followed by the
two logarithmic degree maps, therefore defines functions on the quotient and
annihilates every principal divisor.  This is a valid quotient-theoretic
descent theorem.

For fractions pulled back from either ruling it agrees with the ordinary
Arakelov product formula.  For a genuinely mixed fraction, however, no
family of local valuations on every chart of the square has been
constructed whose sum is zero.  The projection formula must not be described
as such a local--global theorem.

## 6. Internalization gate and no-go for an ordinary pullback

An internalization would require a valued sheaf or category
`O_val` on the regularized square and a functor

`R Gamma_val(Y,D)`

whose restriction to every `(p,q)` boundary component is the external
periodic tensor, which glues, is principal-translation invariant and lax
monoidal, and whose continuous determinant gives the coefficient-one RR
line and the reduced contact determinant.

No ordinary morphism to an idempotent structure sheaf can do this.  If
`phi: Z -> T` preserves addition and the unit and addition in `T` is
idempotent, then `phi(n)=1` for every positive integer `n`.  It kills every
prime multiplier and its contact norm.  The all-prime ideal valuation avoids
this collapse because it is only subadditive:

`nu(a+b) >= min(nu(a),nu(b))`.

But that inequality is not a sheaf morphism and, by itself, gives neither
pullback of rank-one torsors nor a section functor on higher-arity Haran
operations.  Cancellation also shows why the value of a sum is not
determined by the two input valuation vectors when their coordinates tie.

Therefore the carrier and the periodic packet are presently canonically
coupled by prime labels and masses, but not internalized into one section
theory.  A bend, hyperfield-valued, or dequantization construction together
with the comparison properties above is the exact missing theorem.  Until
it is supplied, the result is a carrier plus a canonically coupled external
numerical theory, not a complete Weil surface.

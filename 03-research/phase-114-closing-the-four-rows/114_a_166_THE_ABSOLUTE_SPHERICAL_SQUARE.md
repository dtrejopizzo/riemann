# The absolute spherical square

## 1. The carrier

Let `X=overline(Spec Z)` with the unital spherical structure sheaf `O` of
Connes--Consani.  For divisor metrics with rational radius, their theorem
gives the exact rule

`O(D) smash_O O(E) ~= O(D+E)`.

Every integral prime-generated divisor has rational radius: its
archimedean factor is a finite product of integral powers of primes.  Thus,
on the sector needed below, `O(D)` is invertible with inverse `O(-D)`.
Principal
translation by `q in Q^x` is the explicit isomorphism given by
multiplication by `q^-1`.

For arbitrary real radii, the same source constructs strict modules
`O_<(D)` over a nonunital strict structure object and proves the exact
multiplication rule there.  We do not need that extension to define the
unital derived category on the integral prime sector.

Form the product in spherical ringed spaces

`Y_S = X x_S X`

with structure object

`O_(Y_S)=pr_1^-1 O smash_S pr_2^-1 O`.

The square does not collapse to one copy of `X`: already on the generic
finite chart its spherical algebra contains the nontrivial smash product
`H Z smash_S H Z`, which Connes--Consani prove is not isomorphic to `H Z`.
The mixed polynomial class `(t_1-1)(t_2-1)` in their proof is invisible to
both coordinate marginals and witnesses the extra direction.

## 2. Genuine invertible modules on the square

For arithmetic divisors `D,E` on `X`, define

`L(D,E)=pr_1^-1 O(D) smash_S pr_2^-1 O(E)`.

It is an `O_(Y_S)`-module.  Associativity of the relative smash product and
the one-dimensional multiplication theorem give

`L(D,E) smash_(O_(Y_S)) L(D',E')
 ~= L(D+D',E+E')`.

Taking `(-D,-E)` proves invertibility.  Thus

`Pic(X) x Pic(X) -> Pic(Y_S)`

is realized by actual modules, not by a declared prime lattice.  A pair of
principal changes `(q,r)` acts by the explicit multiplication
`q^-1 smash r^-1`, so principal invariance is internal.

The unital assertion includes arbitrary finite components and the rational-
radius archimedean components produced by them.  The strict nonunital
version extends the tensor law to arbitrary real radii.

## 3. A well-typed derived global-section functor

Simplicial modules over a spherical algebra carry the standard homotopical
framework used for Gamma-rings.  Apply it objectwise to sheaves of
`O_(Y_S)`-modules, localize at local stable equivalences, and take a
fibrant replacement `I`.  Define

`R Gamma_S(Y_S,L)=Gamma(Y_S,I(L))`.

This is a genuine derived functor on the spherical square.  It is invariant
under the explicit principal isomorphisms above and is lax symmetric
monoidal.  Hence the absolute square now has an internal carrier, actual
invertible divisor modules, and a well-typed `R Gamma`; none of these is an
external constant coefficient packet.

## 4. The external-product comparison morphism

The derived smash product of the two one-dimensional adelic cohomology
objects gives a canonical morphism

`R Gamma_S(X,O(D)) derived-smash_S R Gamma_S(X,O(E))
 -> R Gamma_S(Y_S,L(D,E))`.

This is the correct Kunneth comparison.  The one-dimensional factors are
the Gamma-space cohomology objects constructed from the short adelic
complexes; their `H^0`, `H^1`, integer dimensions and Serre duality are
published theorems.  The 2024 absolute-base formula is

`chi_S(D)=dim_S H^0(D)-dim_S H^1(D)
         = ceil'(deg(D)/log 2)+1`.

Consequently, if the comparison is an equivalence and the absolute
dimension is multiplicative on these derived smash products, its Euler
dimension is

`chi_S(D) chi_S(E)`.

Along positive rays this has leading term

`deg(D)deg(E)/(log 2)^2`,

with only linear and bounded ceiling corrections.  Unlike the former
finite-field interpolation, base `2` here is the published absolute-base
normalization `S[X]`, `1+1=X+X^2`.

## 5. Why the Kunneth conclusion is not automatic

The point-set smash product of Gamma-sets is a Day convolution.  It is not
ordinary tensor product: the published theorem

`H Z smash_S H Z not~= H Z`

shows that it has genuine mixed information.  At the spectral level,
`H Z derived-smash_S H Z` also has nonzero positive homotopy.  Therefore one
cannot infer the Kunneth equivalence or multiply the generator dimensions
by analogy with vector spaces.

Nor does finite generator dimension imply that a Gamma-module is a finite
free or perfect spherical module.  A determinant functor on perfect
modules cannot be applied until perfection of the displayed derived global
sections is proved.

## 6. Exact advance and remaining theorem

The absolute spherical construction closes three earlier gates:

1. a literal noncollapsed product carrier exists;
2. external arithmetic divisors are genuine invertible modules with
   internal principal descent and tensor product;
3. an actual derived global-section functor is well typed on the same
   carrier.

The remaining surface theorem is now precise and no longer a missing
definition:

* prove the Kunneth comparison for the adelic spherical divisor complexes;
* compute the absolute dimensions of all resulting Tor/higher-homotopy
  terms and establish multiplicativity of Euler dimension;
* prove perfection (or construct an appropriate nuclear determinant) and
  compare its determinant with finite contact.

Until those computations are supplied, the product formula in Section 4 is
a conditional consequence, not a proved surface Riemann--Roch theorem.

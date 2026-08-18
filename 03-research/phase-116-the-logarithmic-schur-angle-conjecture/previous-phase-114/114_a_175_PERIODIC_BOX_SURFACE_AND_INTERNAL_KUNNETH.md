# The periodic section topos and its internal Kunneth theorem

## 1. Geometric input

Let `X_abs=overline(Spec Z)` and let

`pi:X_vis -> X_abs`

be the canonical arithmetic pullback of Connes--Consani.  Its fiber over a
finite prime `p` is the pointed periodic curve

`C_p=R_+^x/p^Z`,

whose neutral point is `Z[1/p]`.  Hence

`Y_per=disjoint_union_(p,q) C_p x C_q`

comes with a canonical map

`Pi_per:Y_per -> X_abs x X_abs`.

The carrier used below is a coefficient topos over this actual pair
pullback.  The construction does not identify a prime label with an
unrelated circle: its objects and section modules come from the fibers of
`Pi_per`.

## 2. The enriched periodic section category

Fix `(p,q)`.  Let `Pic_p^0` denote the canonical degree-character-zero
copy of `R` in `Div(C_p)/Prin(C_p)`, and similarly for `q`.  For a real
number `delta`, write `D_p(delta)` for its unique class in `Pic_p^0`.

Define a small category enriched in pointed filtered topological
`R_max`-modules, denoted `Sec_(p,q)`, as follows.

* Objects are pairs `(delta,eta) in R^2`.
* If both differences are nonnegative, set

  `Hom((delta,eta),(delta',eta'))
   =T_(p,q)(delta'-delta,eta'-eta)`,

  the functionally reduced external tropical tensor of the two published
  periodic section modules.
* If one difference is negative, the Hom object is the zero pointed
  module.
* The identity is the degree-zero constant section.
* Composition is pointwise tropical multiplication in both factors.

The composition is well typed because multiplying sections adds divisors.
It is associative and unital because addition of real divisor degrees and
pointwise multiplication are.  Principal translations on either curve
induce isomorphic enriched categories; using divisor classes makes the
definition independent of representatives.

Addition of objects and external multiplication of morphisms make
`Sec_(p,q)` a symmetric monoidal enriched category.  Its object monoid is
the group `R^2`; in particular every object has a tensor inverse.

For the arithmetic object take the finite-support coproduct completion

`Sec_per=bigoplus'_(p,q) Sec_(p,q)`.

Only finitely many nonzero-degree components are admitted in an object.
This is a small category after choosing a fixed universe for real numbers
and filtered modules; alternatively one may use a small skeleton.  No
proper-class intersection occurs.

## 3. The coefficient topos and line objects

Let

`E_per=PSh(Sec_per^op,Sets)`

be the presheaf topos.  Pointed objects and filtered topological
`R_max`-module objects in `E_per` form the coefficient category `A_per`.
The underlying set-valued category `E_per` is the displayed Grothendieck
topos; no claim that pointed sets themselves form a topos is needed.

Equip it with Day convolution.  The enriched Yoneda embedding

`y:Sec_per -> A_per`

is strong symmetric monoidal.  Put

`O_per=y(0)` and `L(x)=y(x)`.

Then

`L(x) tensor_Day L(y) ~= L(x+y)`,

`L(x)^(-1) ~= L(-x)`.

Thus the divisor objects are actual invertible modules over the monoidal
unit `O_per`, not a declared lattice of labels.  Principal translations
give isomorphisms of the corresponding representables.

The Grothendieck construction of the family `(p,q)|->Sec_(p,q)` gives a
projection of sites to the component site of `Y_per`; composing with
`Pi_per` places `A_per` canonically over the arithmetic square.  Fiber over
`(p,q)` recovers precisely the periodic section category of
`C_p x C_q`.

## 4. Internal global sections and Kunneth

Define global sections of an `O_per`-module `M` by the enriched mapping
object

`Gamma_per(M)=Map_(A_per)(O_per,M)`.

For a representable line object, the enriched Yoneda lemma gives a
canonical isomorphism

`Gamma_per(L_(p,q)(delta,eta))
 ~=Hom_Sec((0,0),(delta,eta))
 ~=T_(p,q)(delta,eta)`

when `delta,eta>=0`, and the zero object otherwise.

Since the right hand side is, by construction of the enriched Hom,

`H^0(C_p,D_p(delta))
 widehat-boxtimes_red H^0(C_q,D_q(eta))`,

this is an internal Kunneth isomorphism, not merely a comparison morphism.
It is natural in both divisor variables and compatible with multiplication.

Representables are projective for objectwise epimorphisms in a presheaf
category.  Consequently the right derived functors of
`Map(O_per,-)` vanish on every `L(x)`.  Thus, in the derived category of
abelian-group objects (or in any objectwise projective model enrichment),

`R Gamma_per(L(x)) ~= Gamma_per(L(x))[0]`.

No uncomputed Tor or higher-smash term is being discarded: the statement
is a projectivity theorem in the newly constructed coefficient topos.  The
raw spherical smash is a different functor and is not used here.

## 5. Exact continuous dimension

At finite periodic depths, let the two one-dimensional section modules
have `d` and `e` ordered extremal rays.  The external coefficient map has
`de` coordinates.  Unique-dominance witnesses give an open `de`-cell;
stratification by finite coordinates and the closed-sum theorem give the
opposite covering-dimension bound.  Therefore

`dim_top T_(p,q)^(r,s)=d_r e_s`.

The published one-dimensional Frobenius limits imply

`cdim T_(p,q)(delta,eta)=max(delta,0)max(eta,0)`.

For an effective finite-support arithmetic divisor

`x=sum_p a_(p,1)e_(p,1)+sum_q b_(q,2)e_(q,2)`,

use degrees `delta_p=a_(p,1)log p` and
`eta_q=b_(q,2)log q`.  Additivity on the finite coproduct gives

`cdim R Gamma_per(L(x))
 =sum_(p,q)delta_p eta_q
 =d_1(x)d_2(x)`.

This proves coefficient-one surface growth inside one coefficient topos.

## 6. Universal property

`A_per` is the free cocomplete pointed symmetric monoidal category receiving
the enriched periodic section category: every enriched strong symmetric
monoidal functor

`F:Sec_per -> C`

to a cocomplete target whose tensor product preserves colimits extends,
uniquely up to contractible natural isomorphism, to a colimit-preserving
strong symmetric monoidal functor from `A_per` by enriched left Kan
extension.

Therefore the internalization is not selected from several possible
global weightings.  Once the canonical periodic fibers, their divisor
classes and their external section multiplication are fixed, the
coefficient topos and its line objects are forced by this universal
property.

## 7. Continuous determinant of cohomology

At depth `(r,s)`, the canonically ordered pairs of one-dimensional extremal
rays give

`V_(r,s)=R^(d_r e_s)`

and its determinant line

`lambda_(r,s)=det_R V_(r,s)`

with distinguished lexicographic wedge.  Give this wedge the normalized
trace norm

`||omega_(r,s)||=exp(-p^(-r)q^(-s)d_r e_s)`.

Principal translation changes coefficient offsets but neither extremal
slopes nor their order.  It therefore preserves the based determinant
line.  The based lines are canonically identified with `R` by their
distinguished wedges, and the norms converge.  Define the continuous
determinant of the filtered derived global sections by this limit.  Then

`Det_c R Gamma_per(L_(p,q)(delta,eta))
 =(R omega, exp(-max(delta,0)max(eta,0)))`.

For effective arithmetic `x`, finite-support tensor product gives

`lambda_RR(x)=Det_c R Gamma_per(L(x))`,

`||omega_x||=exp(-d_1(x)d_2(x))`.

This determinant is not inferred from a number called dimension.  It is
the limit of determinant lines of the canonical extremal coefficient
spaces which present the actual enriched Hom objects.

## 8. Contact and Green comparison

The internal reduced contact complex on the diagonal prime component has
the form `[Z --p--> Z]`; its torsion determinant has norm `p^(-1)`.
Tensoring over the finite support gives the based contact line
`lambda_C(x,y)` with metric exponent

`C_Lambda(x,y)=sum_p
 (x_(p,1)y_(p,2)+x_(p,2)y_(p,1))log p`.

Polarization of the determinant metric gives

`B_RR(x,y)=d_1(x)d_2(y)+d_2(x)d_1(y)`.

In the Picard groupoid of based normed real lines set

`lambda_G(x,y)=delta lambda_RR(x,y) tensor lambda_C(x,y)^(-1)`.

There is then a canonical isometry

`delta lambda_RR ~= lambda_C tensor lambda_G`,

whose logarithmic norm identity is `B_RR=C_Lambda+G`.  Bilinearity proves
symmetry, associativity and the biextension interchange law.

## 9. Relation to the raw spherical square

The raw spherical square remains a noncollapsed absolute carrier, but its
full bounded smash has exponential generator dimension.  The preceding
no-go theorem proves that it cannot supply surface Riemann--Roch.  The
periodic section topos is the canonical separated coefficient geometry
over the arithmetic pair pullback.  It retains exactly the periodic
section multiplication and makes it internal by Yoneda and Day
convolution.

The construction has an infinite family of prime-pair components.  It does
not claim a finite-rank integral Neron--Severi group, because exact
composition and von Mangoldt contact make that requirement mathematically
inconsistent by the finite-rank contact theorem.

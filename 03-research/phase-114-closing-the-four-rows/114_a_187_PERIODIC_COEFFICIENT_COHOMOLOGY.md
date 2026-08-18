# Periodic coefficient cohomology on the spherical square

## 1. Input and scope

The intrinsic-section no-go rules out using all raw spherical sections as
the finite perfect surface cohomology.  This note constructs instead a
coefficient cohomology on the same arithmetic square.  Its input is the
canonical prime-fiber geometry of the arithmetic pullback, not a constant
sheaf whose fiber is a previously declared numerical answer.

Let

`Pi_per:H_per=coprod_(p,q)(C_p x C_q) -> Y_S`

be the finite-prime part of the pair arithmetic pullback, where
`C_p=R_+^x/p^Z`.  The existence and canonicity of the prime fibers are the
geometric input.  Everything below is relative to this map.

## 2. The fiberwise section category

For a fixed pair `(p,q)`, let `V_(p,q)` be the symmetric monoidal category
of pointed filtered complete tropical modules used for periodic sections.
Define a `V_(p,q)`-enriched category `Sec_(p,q)` as follows.

* Objects are pairs of periodic divisor classes `(delta,eta) in R^2`, with
  the neutral points of `C_p,C_q` fixing the degree representatives.
* For `delta' >=delta` and `eta'>=eta`, put

  `Hom((delta,eta),(delta',eta'))
     =H^0(C_p,D_p(delta'-delta))
        boxtimes_red
      H^0(C_q,D_q(eta'-eta))`.

* If either difference is negative, use the zero pointed object.
* Composition is external pointwise tropical multiplication.

Associativity and the unit follow from the corresponding laws for
periodic sections.  Addition of divisor classes makes `Sec_(p,q)` a
symmetric monoidal enriched category.

This definition uses the actual one-dimensional periodic section objects
and their multiplication.  It does not insert their dimensions as
structure constants.

## 3. Free coefficient geometry and line objects

Let

`A_(p,q)=PSh_V(Sec_(p,q)^op,V_(p,q))`

with enriched Day convolution, and let `y_(p,q)` be the enriched Yoneda
embedding.  The enriched Yoneda and Day theorems give canonical
isomorphisms

`y(x) tensor_Day y(x') ~=y(x+x')`,

`Map_(A_(p,q))(y(0),y(x)) ~=Hom_(Sec_(p,q))(0,x)`.

Thus `L_(p,q)(x):=y_(p,q)(x)` is an actual invertible coefficient line and
its internal global sections are the periodic external section object.
The construction is universal: `A_(p,q)` is the free cocomplete enriched
symmetric monoidal category receiving `Sec_(p,q)`.  This is the enriched
Yoneda/left-Kan-extension universal property and does not depend on a
choice of generators for a section module.

## 4. Descent to the arithmetic square

The disjoint union of the categories `A_(p,q)` is a sheaf of coefficient
categories `A_per` on `H_per`: on a component it is `A_(p,q)`, and
restriction to an open subset is restriction of the corresponding
periodic section objects.  There are no cross-component cocycle conditions
because the components are open and closed.

For a finite-support external divisor `x`, define the line
`L_per(x)` componentwise by the periodic divisor

`(a_(p,1)log p,b_(q,2)log q)`.

Define its coefficient object on the spherical square by geometric direct
image

`F_per(x):=R Pi_(per,*) L_per(x)`.

This is not the constant sheaf with fiber `H_val(x)`: the source is the
sheaf of enriched representable lines on the actual periodic fibers, and
the direct image is applied only after that source object has been
constructed.

The adjunction for the geometric morphism gives the canonical identity

`R Gamma(Y_S,F_per(x)) ~=R Gamma(H_per,L_per(x))`.

On every component, `y(0)` is representable and therefore projective for
the objectwise model structure.  Hence

`R Map(y(0),y(x)) ~=Map(y(0),y(x))`

and enriched Yoneda yields

`R Gamma(Y_S,F_per(x))
 ~=prod'_(p,q)
   (H^0(C_p,D_p(a_(p,1)log p))
      boxtimes_red
    H^0(C_q,D_q(b_(q,2)log q)))[0]`.

The prime denotes finite support.  This is an internal global-section
theorem for a geometrically induced coefficient object on `Y_S`, not an
identification with the raw line `L(D,E)`.

## 5. Descent, tensor product and Kunneth

Principal translation on a periodic curve is an isomorphism of its divisor
line and section object.  Applying Yoneda and then `R Pi_(per,*)` proves
principal descent for `F_per`.

Day convolution gives componentwise maps

`L_per(x) tensor L_per(y) ->L_per(x+y)`.

Since right direct image is lax symmetric monoidal, these induce coherent
maps

`F_per(x) tensor F_per(y) ->F_per(x+y)`.

The displayed formula for `R Gamma` is the Kunneth theorem: on `(p,q)` its
right side is, by definition and enriched Yoneda, the reduced external
tensor of the two actual one-dimensional section objects.  No Kunneth
claim for the raw Day smash is made.

## 6. Continuous dimension

At finite periodic depths `(u,v)`, let `d_u(delta)` and `e_v(eta)` be the
numbers of ordered extremal rays in the two periodic section objects.  The
external coefficient presentation has `d_u e_v` coordinates.  The
unique-dominance witnesses give an open cell of that dimension, while the
coefficient presentation and the closed-sum theorem give the opposite
covering-dimension inequality.  Hence the finite-depth dimension is
exactly `d_u e_v`.

The one-dimensional periodic Riemann--Roch limits then give

`cdim R Gamma(Y_S,F_per(x))
   =sum_(p,q) a_(p,1)b_(q,2)log p log q
   =d_1(x)d_2(x)`.

Thus the coefficient-one quadratic form is derived from internal global
sections of `F_per`.

## 7. What this construction closes

The construction proves:

1. a coefficient object on the same spherical square;
2. an intrinsic total global-section functor for that coefficient object;
3. principal descent and lax monoidal multiplication;
4. an internal Kunneth identity by enriched Yoneda;
5. coefficient-one continuous dimension.

It also explains precisely why this does not contradict the exponential
raw-section theorem: `F_per(x)` is a geometrically induced coefficient
object, not the raw spherical divisor line.

## 8. Remaining comparison gates

The full goal is not yet closed.  Three nonformal theorems remain.

1. **Perfect presentation.**  Construct the finite-depth extremal
   coefficient spaces as functorial perfect objects in `Perf_DN`, rather
   than only use them to compute covering dimension.
2. **Code comparison.**  Compare those perfect objects with the
   negabinary cotangent pro-system.  Their finite-stage ranks are not
   canonically equal, so the comparison must either give an explicit
   cofinal reindexing and stabilization or be stated only at the continuous
   determinant level.
3. **Arithmetic action.**  Lift the Witt/Frobenius correspondences and the
   nuclear Dirichlet action to `F_per`, and prove compatibility with the
   reduced derived prime contact on `Y_S`.

No completion claim is made until these three gates are proved.

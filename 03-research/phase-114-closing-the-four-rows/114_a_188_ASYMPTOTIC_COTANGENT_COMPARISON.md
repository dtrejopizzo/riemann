# Asymptotic comparison of periodic cohomology and the negabinary cotangent

## 1. The comparison problem

The periodic coefficient object has intrinsic global sections.  At finite
Frobenius depth, their extremal rays give a finite perfect linearization.
The negabinary construction gives a different finite perfect object.  The
finite ranks are not equal and there is no candid finite-stage
isomorphism.

What enters surface Riemann--Roch is the normalized two-dimensional
asymptotic class.  This note constructs the exact quotient category in
which the two systems can legitimately be compared and proves that their
classes and determinant lines agree there.

## 2. The quadratic asymptotic perfect category

Fix a prime pair `(p,q)`.  Let `SeqPerf_DN(p,q)` be the stable category of
bi-indexed systems `K_(r,s)` of based perfect Deligne--nuclear objects whose
real ranks are `O(p^r q^s)`.  Morphisms are compatible systems after a
cofinal change of indices.

Let `Neg_(p,q)` be the full stable subcategory of systems satisfying

`rank_R K_(r,s)=o(p^r q^s)`

as `r,s->infinity` independently.  It is a thick subcategory: shifts do not
change rank, and the rank of a cone is bounded by the sum of the ranks of
its two terms.  It is also stable under tensoring by a one-ruling system of
rank `O(p^r)` or `O(q^s)` in the other variable.  Define

`Aperf_DN^(2)(p,q)=SeqPerf_DN(p,q)/Neg_(p,q)`.

Pass first to the stable envelope of the split exact category of based
systems.  The displayed quotient is its genuine Verdier quotient, not an
equality of leading numerical coefficients.  A morphism whose cone has
subquadratic total cohomology rank becomes an isomorphism.

For based degree-zero free objects, equip a system with weights
`w_(r,s)>0` satisfying `w_(r,s)p^r q^s->1`.  Its continuous determinant is

`Det_c(K)=lim_(r,s) (det K_(r,s),
                    ||omega_(r,s)||=exp(-w_(r,s)rank K_(r,s)))`

whenever the normalized ranks converge.  A negligible cone contributes
norm exponent `o(1)`, so `Det_c` descends to the based determinant Picard
groupoid on the quotient.

## 3. The two systems

Let `E_(p,r)(a)` be the finite-depth periodic section module of degree
`a>0`, and write

`d_(p,r)(a)=#Ext(E_(p,r)(a))`.

The one-dimensional periodic Riemann--Roch theorem gives

`p^(-r)d_(p,r)(a)->a`.

The intrinsic mixed coefficient cohomology has perfect extremal
linearization

`P_(r,s)(a,b)=R[Ext(E_(p,r)(a))]
                 tensor
              R[Ext(E_(q,s)(b))]`,

with its integral lattice and nuclear scalar extension.  It has rank
`d_(p,r)(a)d_(q,s)(b)` and periodic determinant weight `p^(-r)q^(-s)`.

For the code system choose the cofinal integer scales

`t_(p,r)=floor(p^r log 2)`,
`t_(q,s)=floor(q^s log 2)`.

Let

`R_(p,r)(a)=r(floor(exp(t_(p,r)a)))`.

Negabinary admissibility gives

`R_(p,r)(a)/p^r ->a`,

because `r(floor(exp(ta)))=ta/log 2+O(1)`.  The mixed code cotangent at
these scales is

`C_(r,s)(a,b)=R^(R_(p,r)(a)R_(q,s)(b))`

with its ordered digit-pair basis, integral lattice and nuclear scalar
extension.  Its determinant-density weight is

`w^C_(r,s)=(log 2)^2/(t_(p,r)t_(q,s))`,

and

`w^C_(r,s)/(p^(-r)q^(-s))->1`.

## 4. Canonical stable comparison

Order the periodic extremal-pair basis lexicographically by slopes and the
code basis lexicographically by digit indices.  Let `U_(r,s)` be the based
free object whose rank is the maximum of the two ranks.  The order-preserving
inclusions give a zigzag

`P_(r,s)(a,b) ->U_(r,s)<-C_(r,s)(a,b)`.

Now

`d_(p,r)(a)-R_(p,r)(a)=o(p^r)`

and similarly in the second variable.  Therefore

`rank P_(r,s)-rank C_(r,s)=o(p^r q^s)`.

Both cones in the zigzag are negligible.  Hence the zigzag is a canonical
isomorphism

`[P(a,b)] ~= [C(a,b)]`

in `Aperf_DN^(2)(p,q)`.  It is natural under principal translations and
interchange of the two rulings because those maps preserve the ordered
extremal and digit bases.

This is the precise fixed-divisor cotangent comparison: it is not a false
finite-stage isomorphism, but it is stronger than equality of dimensions
because it is an isomorphism in a specified quotient of perfect systems.
Principal translations preserve both total orders, so the comparison is
principal-invariant.  Naturality for arbitrary effective inclusions is not
automatic: an order-preserving inclusion of periodic extremal sets need
not add the same initial block as digit zero-extension.  That compatibility
is retained as a separate gate below.

## 5. Determinant comparison

For the periodic system,

`p^(-r)q^(-s)rank P_(r,s)->ab`.

For the code system,

`w^C_(r,s)rank C_(r,s)->ab`.

The two based determinant lines therefore converge to

`(R*1,||1||=exp(-ab))`.

The comparison zigzag sends the ordered basis of each smaller object to the
initial ordered block of `U`.  Its negligible complementary block has
determinant exponent `o(1)`.  Consequently the quotient isomorphism induces
the canonical isometry

`Det_c P(a,b) ~=lambda_code(a,b)`.

For finite prime support, tensoring these componentwise isometries gives
the metric exponent `d_1(x)d_2(x)` and commutes with polarization.

## 6. Kunneth compatibility

The one-ruling periodic systems have ranks `O(p^r)` and `O(q^s)`, and their
external tensor is `P_(r,s)`.  The one-ruling code systems have ranks
`O(p^r)` and `O(q^s)`, and their tensor is `C_(r,s)`.  Tensoring a
one-dimensional negligible comparison error by an `O(q^s)` or `O(p^r)`
system gives a two-dimensional negligible error.  Thus the comparison
commutes with Kunneth in the quotient category.

## 7. Exact scope

This theorem supplies:

1. a perfect realization of intrinsic periodic coefficient cohomology;
2. a canonical fixed-divisor asymptotic cotangent comparison with the
   existing Deligne--nuclear code system;
3. equality of their continuous determinant lines as an induced isometry,
   not merely as an equality of exponents;
4. compatibility with principal descent and Kunneth.

Two closure gates remain.  First, the comparison must be made natural for
the effective divisor transition systems, either by constructing compatible
cofinal flags of extremal rays or by proving that the discrepancy of the
transition squares factors functorially through negligible systems.
Second, the Witt/Frobenius correspondences and the nuclear Dirichlet action
must be lifted to the periodic coefficient objects and the comparison must
be shown to carry their diagonal contact to the reduced derived contact on
the spherical square.

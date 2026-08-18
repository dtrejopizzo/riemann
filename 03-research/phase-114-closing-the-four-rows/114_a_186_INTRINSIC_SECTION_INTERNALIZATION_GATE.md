# The intrinsic-section internalization gate

## 1. Purpose

The Deligne--nuclear construction has a perfect cotangent object obtained
from the smooth envelope of the negabinary section code.  To promote it to
an intrinsic cohomology theory one would like to identify that object with
the cotangent of a functor of sections determined by the spherical divisor
line itself.

There are two different assertions which must not be conflated:

1. the spherical square has an intrinsic derived global-section functor;
2. the cotangent of that functor is the finite perfect negabinary object.

The first assertion is true.  This note proves that the second is false for
the functor of *all* spherical sections.  It then isolates the exact form a
viable coefficient-cohomology internalization must have.

## 2. The intrinsic derived section functor

Let

`Y_S=X x_S X`

be the spherical square and let `L(D,E)` be an external divisor line.  In
the local stable model category of sheaves of simplicial modules over
`O_(Y_S)`, choose a fibrant replacement `I` and set

`R Gamma_S(Y_S,L(D,E))=Gamma(Y_S,I(L(D,E)))`.

Equivalently, in the associated stable infinity-category,

`R Gamma_S(Y_S,L)=Map_(O_Y)(O_Y,L)`.

This definition is independent of the fibrant model, is invariant under
the explicit principal isomorphisms of divisor lines, and is lax symmetric
monoidal.  It is therefore the intrinsic total derived-section object of
the literal spherical square.

For an additive coefficient algebra `A`, its linear section stack is

`Sec_L(A)=Omega^infinity Map_(O_Y tensor A)
                    (O_Y tensor A,L tensor A)`.

Because the target category is stable, this stack is already linear.  Its
tangent spectrum at the zero section is canonically

`T_0 Sec_L ~=R Gamma_S(Y_S,L) tensor A`.

Indeed a square-zero extension `A+M` splits as an `A`-module, and the fiber
of `Sec_L(A+M)->Sec_L(A)` over zero is

`Omega^infinity(R Gamma_S(Y_S,L) tensor_A M)`.

Thus an additive tangent construction cannot discard additive classes of
the derived global-section object.

## 3. Exponential tangent obstruction

On a principally normalized archimedean chart, the bounded modules are

`H_m=(H Z)_[-m,m]`, `H_n=(H Z)_[-n,n]`.

Put

`r(n)=floor(log_2(n+1))`

and `B_s=(1,-2,...,(-2)^(s-1))`, with `s=r(n)`.  Its `l^1` norm is
`2^s-1<=n`, so `B_s` is an admissible element of `H_n(s_+)`.

For every nonempty subset `J` of `{0,...,s-1}`, the Day presentation gives
a section `z_J` of `H_m smash_S H_n`.  Under the canonical additive
assembly morphism,

`z_J |-> [sum_(j in J)(-2)^j] in Z[Z]/Z[0]`.

Negabinary uniqueness makes the `2^s-1` displayed basis vectors distinct.
Consequently the additive linearization of the intrinsic section object
has rank at least

`2^(r(n))-1`.

This statement applies in particular to the tangent of every additive
section stack compatible with the canonical assembly map.

By contrast, the mixed negabinary code envelope has cotangent rank

`r(m)r(n)`.

Taking `m_t=floor(exp(t a))` and `n_t=floor(exp(t b))`, with `a,b>0`, gives

`rank T_0 Sec_(L(tD,tE)) >=exp(t b+O(1))`,

whereas

`rank H_t^cot(D,E)=t^2 ab/(log 2)^2+O(t)`.

The two objects therefore cannot be equivalent, cannot differ by a
subquadratic perfect error, and cannot have the same determinant density.
The conclusion remains true after interchanging the two rulings.

### Intrinsic-section no-go theorem

There is no natural equivalence between the cotangent of the additive
derived moduli functor of all bounded spherical sections and the perfect
negabinary code cotangent which is compatible with restriction to the
generic chart and with additive assembly.

This is not a missing technical comparison.  It follows from incompatible
rank lower bounds.  In particular, calling the code cotangent the
cotangent of *all* sections would contradict a theorem already proved on
the same carrier.

## 4. Why the Boolean and affine repairs do not evade the theorem

The literal Boolean parameter scheme

`Spec F_2[x_1,...,x_r]/(x_i^2-x_i)`

is etale and has zero cotangent.  Replacing it by `A^r_(F_2)` creates a
smooth framed relaxation, but no morphism from `F_2` to `Z` turns its
coordinates into an additive family of integral sections.

Over `Z` there is a polynomial evaluation map

`A^r_Z -> A^1_Z`, `(x_i)|->sum_i x_i(-2)^i`.

Its differential has rank one, not rank `r`.  Hence an ordinary algebraic
family of scalar sections collapses the independent framed digit
directions infinitesimally.  This gives a second, local explanation for
the failure of the desired identification.

## 5. The viable internalization statement

The no-go concerns the functor of all raw spherical sections.  It does not
exclude a cohomology theory on the spherical square with a geometrically
specified coefficient object.  The available canonical source is the
arithmetic pullback whose prime fiber is the periodic curve

`C_p=R_+^x/p^Z`.

Let `Pi_per` denote the pair pullback of the finite-prime periodic fibers
to the arithmetic square.  A viable intrinsic object must be constructed
in the following order.

1. Construct a sheaf (or sheaf of stable coefficient categories)
   `O_per` on the pair pullback and the geometric direct image
   `R Pi_(per,*) O_per` on the *same* spherical square.
2. For every divisor line `L(D,E)`, construct from pullback and the
   periodic divisor theory a coefficient object `F_per(D,E)`, rather than
   declaring a constant sheaf with a precomputed section module.
3. Prove the internal identity

   `R Gamma(Y_S,F_per(D,E))
      ~=R Gamma(C_p,D_p) boxtimes R Gamma(C_q,D_q)`

   componentwise, including descent, multiplication and higher terms.
4. Construct finite perfect presentations of these actual coefficient
   sections and their determinant.  Only after this step may their
   cotangent/determinant be compared with the negabinary system.
5. Define the comparison category precisely.  A comparison only of the
   limiting based normed determinant lines is weaker than an equivalence of
   finite-stage cotangent pro-objects and must be stated as such.
6. Prove that the Witt/Frobenius action of row B and the nuclear trace of
   row C act on `F_per`, preserve the Kunneth maps, and recover the derived
   reduced prime contact already constructed on the spherical square.

The first published geometric input needed for this route is present: the
absolute arithmetic curve produces the periodic orbit `C_p` canonically
from its prime fiber.  It does not by itself supply Steps 2--6.

## 6. Closure criterion

Row A can be promoted from the framed package to intrinsic total
cohomology only when all six steps above are proved.  The promotion cannot
be obtained by identifying the framed code cotangent with the tangent of
all raw sections.  The correct target is a geometrically induced
coefficient cohomology on the square, followed by an explicit comparison
theorem.

Until that construction exists, the goal remains active.  This note closes
one false route and converts the word “internalization” into a list of
testable theorems without weakening the requested final objective.

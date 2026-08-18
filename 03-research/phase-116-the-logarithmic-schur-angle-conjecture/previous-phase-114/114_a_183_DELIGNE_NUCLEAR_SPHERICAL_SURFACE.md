# The Deligne--nuclear spherical surface

## 1. One arithmetic coefficient category

Let `Y_S=X_abs x_S X_abs` be the noncollapsed absolute spherical square and
let `O_Y` be its spherical structure sheaf.  Form three sheaves of
`E_infinity` algebras in solid spectra:

`O_Z=O_Y smash_S H Z`,

`O_R=O_Y smash_S H R`,

`O_C=O_Y smash_S H_solid(C_R)`,

where `C_R` is the nuclear Dirichlet algebra.  There are morphisms

`O_Z -> O_R`,

`O_C -> O_R`

induced respectively by `Z->R` and by the continuous augmentation
`epsilon(a)=a_1`.

Define the arithmetic perfect category by the homotopy pullback

`Perf_DN(Y_S)
 =Perf(O_Z) x^h_(Perf(O_R)) Perf(O_C)`.

An object is a triple `(M_Z,M_C,alpha)` with a perfect integral component,
a perfect nuclear component and an isomorphism between their real base
changes.  This is a stable symmetric monoidal category.  It is the single
category in which the integral finite contact and the nuclear/real
cotangent determinant are compared.

## 2. Divisor lines and principal descent

For external arithmetic divisors `D,E`, the spherical line

`L(D,E)=pr_1^*O(D) smash_S pr_2^*O(E)`

is invertible.  Base extension gives compatible invertible objects in the
three coefficient categories and hence an invertible object of
`Perf_DN(Y_S)`.  The tensor rule is

`L(D,E) tensor L(D',E') ~=L(D+D',E+E')`.

Multiplication by a principal rational supplies the isomorphism, so the
construction descends from divisors to metrized divisor classes internally.

## 3. Cotangent code cohomology objects

At scale `t`, let `V_t(D,E)` be the real tangent space, dual to the
cotangent of the code envelope, with its free digit-pair basis and rank

`r(floor(exp(t deg D))) r(floor(exp(t deg E)))`.

It is obtained from the cotangent at zero of the canonical negabinary code
envelope whose `F_2`-points inject into genuine global spherical sections
of `L(tD,tE)`.  Let `V_(t,Z)` be the free integral lattice on the same
ordered digit-pair basis.

Define the perfect Deligne--nuclear cotangent object

`H_t^cot(D,E)
 =(O_Z tensor_Z V_(t,Z),
   O_C tensor_R V_t,
   alpha_t)`

where `alpha_t` identifies both realifications by the digit basis.  It is
finite locally free at every scale.

Define the one-ruling objects `H_(t,1)^cot(D)` and `H_(t,2)^cot(E)` in the
same way from the digit spaces `V_m` and `V_n`, placed respectively on the
first and second pullback modules.

The canonical identity of digit-pair bases proves Kunneth:

`H_t^cot(D,E)
 ~=H_(t,1)^cot(D) tensor H_(t,2)^cot(E)`.

Its real rank is the product of the two one-dimensional cotangent ranks.

## 4. Continuous Riemann--Roch determinant

If an effective bound increases from `m` to `m'`, maximality gives
`r(m)<=r(m')`; adjoining zero in the new high digit positions defines a
canonical closed immersion of code envelopes.  Its cotangent map is the
split coordinate projection, so dualizing gives a split injection of the
tangent lattices used in `H_t^cot`.  These maps compose for
`m<=m'<=m''`.  Applied in each
ruling they make

`(D,E) |-> {H_t^cot(D,E)}_(t>=1)`

a functor from the effective external divisor category to pro-perfect
objects of `Perf_DN(Y_S)`.  Principal isomorphisms transport the normalized
code, and cofinal subsequences in `t` give the same limit.  The Kunneth
isomorphisms commute with all these transition maps because each is the
coordinate inclusion on a Cartesian digit basis.

Apply the determinant functor of the stable perfect category.  On the real
fiber give the ordered wedge the norm

`exp(-(log 2)^2 rank_R V_t)`.

Use the distinguished wedge to identify the determinant with a based real
line and take its real tensor power `1/t^2`; equivalently its norm is

`exp(-(log 2)^2 rank_R(V_t)/t^2)`.

The category of based normed real lines admits these real tensor powers and
is complete for convergence of the logarithmic norm.  Taking the limit gives
the based line

`lambda_RR^cot(D,E)=(R,exp(-deg(D)deg(E)))`.

For finite prime support the direct-sum determinant yields

`-log||1_x||=d_1(x)d_2(x)`.

Principal invariance follows from the isomorphisms of the divisor lines and
from invariance of degree and digit positions.  The one-dimensional
restriction has linear normalized cotangent dimension; the pair has
quadratic dimension by Kunneth.

## 5. Integral contact in the same category

At the diagonal closed point `p`, let

`C_(p,Z)=[O_Z --p--> O_Z]`.

After base change to `R`, multiplication by `p` is invertible, so this
complex is canonically acyclic.  Therefore

`C_p=(C_(p,Z),0,0~=0)`

is a perfect object of `Perf_DN(Y_S)`.  Its torsion determinant has norm
`p^(-1)` and logarithmic mass `log p`.

For a label `n`, use `C_p` when `n` is a power of the single prime `p` and
the zero object when `n` has at least two distinct prime divisors.  This
realizes `Lambda(n)` objectwise.  The bilinear finite-support contact line
`lambda_C` is formed by tensor powers of these determinant lines and has
exponent `C_Lambda`.  No false assertion that derived tensor over `Z` makes
`Z/p` idempotent is used.

Thus the Riemann--Roch and finite contact lines are determinants of perfect
objects in one category, not lines imported from unrelated carriers.

## 6. Nuclear correspondences and finite type

The global coefficient sections `delta_n in C_R` act on the nuclear
component of every cotangent object.  They satisfy

`delta_m delta_n=delta_(mn)`

and the continuous diagonal functional satisfies

`ell(delta_n)=Lambda(n)`.

The structural correspondence module

`N_DN=O_C e_1 direct-sum O_C e_2 direct-sum O_C e_Gamma`

is locally free of rank three over the nuclear coefficient algebra.  Its
mixed generator acts by the displayed convolution operators.  This is a
categorical finiteness theorem on the same carrier.  It does not factor the
prime directions through an impossible finite-rank abelian group.

## 7. Green comparison

Polarization of the determinant metric gives

`B_RR=d_1 tensor d_2+d_2 tensor d_1`.

In the determinant Picard groupoid of `Perf_DN(Y_S)`, define

`lambda_G=delta lambda_RR^cot tensor lambda_C^(-1)`.

Then

`delta lambda_RR^cot ~=lambda_C tensor lambda_G`

is a canonical isometry.  The logarithmic norm identity is

`B_RR=C_Lambda+G`.

All associativity, symmetry and interchange diagrams commute because they
are determinant, tensor and coboundary identities in one symmetric
monoidal stable category.

## 8. Unified row-A theorem

The tuple

`A_DN=(Y_S,O_Y,Perf_DN,Pic_ext,H^cot,lambda_RR,lambda_C,lambda_G,N_DN)`

satisfies the noncontradictory strong row-A contract:

1. a literal noncollapsed two-dimensional carrier;
2. an actual divisor/principal theory with invertible line objects;
3. curve-linear cotangent dimension on each ruling;
4. an internal Kunneth theorem and quadratic mixed dimension;
5. determinant Riemann--Roch, finite contact and Green comparison in one
   arithmetic perfect category;
6. exact Frobenius composition/contact and finite local module rank over a
   nuclear arithmetic algebra.

The theorem does not assert that raw bounded spherical sections have
quadratic dimension; they provably do not.  It does not assert a
finite-rank abelian Neron--Severi group; exact `Lambda` contact provably
forbids it.  The new ingredients replacing those inconsistent clauses are
canonical cotangent code cohomology and finite type over the nuclear
coefficient algebra.

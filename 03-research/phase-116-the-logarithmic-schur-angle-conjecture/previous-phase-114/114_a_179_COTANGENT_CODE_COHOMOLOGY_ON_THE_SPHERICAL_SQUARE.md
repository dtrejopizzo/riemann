# Cotangent code cohomology on the spherical square

## 1. Why a tangent construction is compatible with the no-go

The raw level-one section set of a spherical smash has exponentially many
independent assembly labels.  This prevents its minimal-generator dimension
from being quadratic.  It does not prevent a canonical finite-dimensional
deformation object attached to a distinguished family of sections.  Over a
finite field, a vector space of dimension `r` has `2^r` points; recovering
`r` from a linear or tangent envelope is precisely the operation required
before applying a Riemann--Roch dimension.

The absolute presentation

`S[X]/(1+1=X+X^2) -> H Z`, `X |-> -2`,

provides such an envelope without choosing an auxiliary prime or
interpolation base.

## 2. Canonical one-dimensional code

For `r>=0`, put

`A_r=(1,-2,...,(-2)^(r-1))`

and let `M_r` be the largest absolute value of a subset sum.  Negabinary
uniqueness identifies the Boolean cube

`G_r=F_2^r`

with the contiguous interval of subset sums of `A_r`.  For the bounded
spherical module `H_m=(H Z)_[-m,m]`, define

`r(m)=max{r:M_r<=m}`.

Then the code map

`c_m:G_(r(m)) -> H_m(1_+)`,
`epsilon |-> sum_i epsilon_i(-2)^i`

is injective, contains the zero section and is canonical from the absolute
generator `X=-2`.

Let

`Q_m=Spec Sym_F2(G_(r(m))^vee)=A_F2^(r(m))`.

Its `F_2`-points are exactly the code parameters.  We call `Q_m` the
linear code envelope, not the full moduli scheme of every bounded section.
It is characterized by the universal property that every map from the code
parameters to an `F_2`-vector space which is linear in the digit coordinates
factors uniquely through `G_r`.

At its zero point,

`Omega_m=m_0/m_0^2 ~=G_r^vee`

is the ordinary cotangent space of the smooth affine scheme `Q_m`; it has
dimension `r(m)` and no derived obstruction group.

## 3. The mixed code inside genuine spherical sections

For `m,n>=1`, let `r=r(m)`, `s=r(n)`.  The matrix construction of the
preceding negabinary theorem gives an injective family

`c_(m,n):G_r tensor_F2 G_s ->
 (H_m smash_S H_n)(1_+)`,

`epsilon |->z_epsilon`.

Injectivity is not declared: the canonical assembly map sends `z_epsilon`
to

`sum_i(-2)^i [sum_j epsilon_(ij)(-2)^j]`,

and two such expressions agree only when all matrix entries agree, by
negabinary uniqueness first in the row coefficients and then in the
column exponents.

Thus every `F_2`-point of the affine space

`Q_(m,n)=Spec Sym_F2((G_r tensor G_s)^vee)`

labels a distinct actual section of the noncollapsed spherical square.  The
family is internal to the global sections of

`pr_1^*O(D) smash_S pr_2^*O(E)`

after the standard principal normalization of `D,E` to their archimedean
bounds.

Again, `Q_(m,n)` is the linear envelope of this canonical section code; it
is not asserted to parametrize every raw spherical section over arbitrary
coefficient rings.

## 4. Cotangent Kunneth theorem

At the zero code section,

`Omega_(m,n)=m_0/m_0^2
 ~= (G_r tensor_F2 G_s)^vee`.

Finite-dimensional duality gives the canonical isomorphism

`Omega_(m,n) ~= Omega_m tensor_F2 Omega_n`.

This is the cotangent Kunneth theorem.  In particular

`dim_F2 Omega_(m,n)=r(m)r(n)`.

It is an identity of cotangent spaces of smooth affine code envelopes, not
a false claim about the dimension of the full non-special Day smash.

## 5. Arithmetic scaling and coefficient one

Let `D,E` have positive Arakelov degrees `a,b` and put

`m_t=floor(exp(t a))`, `n_t=floor(exp(t b))`.

The exact closed form for `M_r` gives

`r(m_t)=t a/log 2+O(1)`,
`r(n_t)=t b/log 2+O(1)`.

Define the absolute cotangent dimension by

`cdim_cot(D,E)
 =(log 2)^2 lim_(t->infinity)
   t^(-2) dim_F2 Omega_(m_t,n_t)`.

The limit exists and the Kunneth theorem yields

`cdim_cot(D,E)=ab`.

For a finite-support effective divisor on the two rulings, take the direct
sum over prime pairs.  The finite sum factors and gives

`cdim_cot(x)=d_1(x)d_2(x)`.

The factor `log 2` in each direction is forced by the absolute relation
`1+1=X+X^2`; it is the same normalization as the published one-dimensional
absolute Riemann--Roch theorem.

## 6. Principal invariance

An integral arithmetic divisor on `overline(Spec Z)` has a canonical
positive rational normalization: multiply by the product of its finite
prime powers to move its finite part to infinity.  The remaining ambiguity
is the norm-one unit `-1`.  Multiplication by a principal rational gives an
isomorphism of the spherical divisor modules and transports the code family.
The unit `-1` changes the signs of the represented sections but acts
trivially on the digit-index vector space `G_r`.

The degree, the maximal admissible length, the cotangent vector space and
its determinant norm therefore depend only on the metrized divisor class.

## 7. Determinant of cotangent cohomology

Order the cotangent basis lexicographically by the digit pair `(i,j)` and
put

`lambda_t(D,E)=det_R(R tensor_F2 Omega_(m_t,n_t))`.

Here `R tensor_F2` means the real vector space with the same distinguished
digit basis, not scalar extension along a nonexistent field morphism
`F_2->R`.  Equivalently it is `R[G_r^vee tensor G_s^vee]` on that basis.

Give its wedge generator the norm

`exp(-(log 2)^2 r(m_t)r(n_t))`.

After the determinant-density normalization by `t^2`, the based normed
lines converge to

`lambda_RR^cot(D,E)=(R 1,exp(-ab))`.

For finite prime support their tensor product has norm

`exp(-d_1(x)d_2(x))`.

This is an ordinary determinant at every finite stage, of the cotangent
cohomology vector space of the canonical code envelope.

## 8. Contact and Green comparison

Polarization gives

`B_RR^cot(x,y)=d_1(x)d_2(y)+d_2(x)d_1(y)`.

Let `lambda_C(x,y)` be the determinant of the actual reduced contact
complexes `[Z --p--> Z]`.  Define

`lambda_G^cot=delta lambda_RR^cot tensor lambda_C^(-1)`.

Then

`delta lambda_RR^cot ~=lambda_C tensor lambda_G^cot`

is a canonical isometry of based normed lines, and its logarithmic identity
is exactly `B_RR^cot=C_Lambda+G`.

## 9. Exact status of the new construction

This construction closes the former spherical Kunneth contradiction at the
correct logical level: the raw section object remains exponentially large,
while its canonical mixed negabinary code has a smooth linear envelope with
quadratic cotangent dimension and determinant.

What remains to call the whole row complete is not Kunneth or the metric
calculation.  It is the compatibility of this cotangent cohomology with the
nuclear Frobenius correspondence action: the action must preserve the code
envelopes or induce functorial maps on their cotangent limits, including
even prime powers where ordinary reduction modulo `2` may vanish.  That is
the next gate.


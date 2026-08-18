# Split holonomy Euler package on the external sector

## 1. The split graded coefficient category

For a periodic orbit `C_p`, let `Per_p` be the additive envelope of its
filtered tropical section modules and principal-translation isomorphisms.
Work in the bounded split graded category: an object is a finite graded
family of periodic section objects and every differential is zero.  This is
*not* called a derived category: no exact or abelian category of tropical
section modules has been supplied from which it could be derived.  The
construction below records the two terms in the published periodic
Riemann--Roch identity and nothing more.

For a periodic divisor `D`, define

`R_p(D) = H^0(C_p,D)[0] direct-sum H^0(C_p,-D)[-1]`.

Equivalently,

`H^0(R_p(D))=H^0(C_p,D)`,

`H^1(R_p(D))=H^0(C_p,-D)`.

Principal translation isomorphisms act in both degrees, so `R_p(D)` depends
only on the divisor class.

Define continuous Euler dimension by the alternating sum.  The
Connes--Consani periodic Riemann--Roch theorem gives

`chi_p(D)=cdim H^0(C_p,D)-cdim H^0(C_p,-D)=deg D`.

This is a theorem imported from the one-dimensional periodic geometry, not
an axiom imposed on the square.

## 2. Split external tensor and Kunneth formula

For divisors `D` on `C_p` and `E` on `C_q`, form the split total complex

`R_(p,q)(D,E)=R_p(D) widehat-boxtimes R_q(E)`.

Its graded objects are

`H^0 = H^0(D) boxtimes H^0(E)`,

`H^1 = [H^0(D) boxtimes H^0(-E)] direct-sum
       [H^0(-D) boxtimes H^0(E)]`,

`H^2 = H^0(-D) boxtimes H^0(-E)`.

The exact external-dimension theorem applies to every summand.  Therefore

`chi_(p,q)(D,E)
 = [cdim H^0(D)-cdim H^0(-D)]
   [cdim H^0(E)-cdim H^0(-E)]
 = deg(D) deg(E)`.

This is the split Kunneth identity for Euler dimensions.  If both degrees are positive, the
negative-divisor section modules have continuous dimension zero, and the
quadratic term is carried by degree zero.  For arbitrary signs, the higher
degrees supply the required alternating corrections.

This construction is functorial under principal translation.  It is not a
monoidal functor of `D`: multiplication of a degree-zero section of `D` by
a degree-one term `H^0(-E)` lands in `H^0(D-E)`, not in a graded term of
`R_p(D+E)`.  Thus no tensor or cup-product assertion is made here.

## 3. Internal split coefficient object on the Haran carrier

The metrized boundary torsors reconstruct `C_p` and `C_q` as their positive
holonomy objects.  Let `i_infinity` denote the associated valued boundary
geometric point of the pro-square.  Regard `R_(p,q)(D,E)` as a complex of
coefficient objects at that point and apply the exact skyscraper direct
image `i_infinity,*`.

For a finite-support external divisor

`x=sum_p a_(p,1)e_(p,1)+sum_q b_(q,2)e_(q,2)`,

define the internal split graded coefficient object

`E_val(x)
 = product_(p,q) i_infinity,* R_(p,q)
   (D_p(a_(p,1)log p),D_q(b_(q,2)log q))`,

over the finitely many pairs in the support.  Global sections of a
skyscraper coefficient object are its fiber.  Hence

`Gamma(Y,E_val(x))`

is canonically the displayed finite product of pair complexes.

Restriction to a chart containing the valued boundary retains the complex;
restriction to a disjoint chart is zero.  These restrictions satisfy the
sheaf equalizer because skyscraper sheaves do.  Supportwise pro-refinement
pulls back the same metrized torsors, so the complexes are eventually
constant bounded pro-data.

Principal invariance follows componentwise from periodic translation and
then from the finite product and skyscraper direct image.  As explained in
Section 2, the split graded object is not asserted to be monoidal.

## 4. Surface Euler characteristic

Additivity over the finite prime-pair support and the pair Kunneth identity
give

`chi_val(x)
 = sum_(p,q) a_(p,1)b_(q,2) log(p)log(q)
 = d_1(x)d_2(x)`.

Thus the coefficient-one surface Riemann--Roch term is the Euler dimension
of an internal split graded coefficient object on the carrier.
It is derived from the two one-dimensional periodic Riemann--Roch theorems.

Polarization gives

`B_RR(x,y)=d_1(x)d_2(y)+d_2(x)d_1(y)`.

No interpolation base, zeta zero or positivity condition enters.

## 5. Exact status: this is not yet `R Gamma`

Finite covering dimension of a polyhedral section module does not by itself
produce a determinant line: the module is not a finite-dimensional vector
space, and a coordinate presentation would be an extra choice.  Therefore
this note constructs neither a determinant line nor an inverse-limit
determinant functor.

Likewise, placing `H^0(-D)` in degree one is a bookkeeping device.  It is
not the first derived functor of global sections.  A perfect evaluation
pairing realizing it as Serre duality has not been proved.

What *is* proved is exact and useful: there is an internal coefficient
object whose split Euler dimension equals `d_1d_2`, functorially under
principal translations, and the coefficient is inherited from periodic
Riemann--Roch rather than chosen by interpolation.  Calling this object
`R Gamma`, a determinant of cohomology, or a surface cohomology theory would
add claims not established by the construction.

The next two gates are therefore precise:

1. construct an exact/derived category in which the periodic section
   objects occur and prove that its derived global sections give the two
   displayed terms;
2. construct a normalized determinant functor there, rather than infer one
   from covering dimension;
3. glue the finite torsion contact complexes to this boundary object and
   identify the Green metric as a determinant comparison.

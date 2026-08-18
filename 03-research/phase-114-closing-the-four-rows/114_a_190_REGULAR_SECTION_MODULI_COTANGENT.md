# The cotangent of the regular periodic section moduli

## 1. Finite-depth section moduli

Fix primes `(p,q)` and special positive periodic divisors at finite depths.
Let

`E={phi_0,...,phi_(d-1)}` and `F={psi_0,...,psi_(e-1)}`

be their canonically slope-ordered extremal rays.  Put

`B_(i,j)(x,y)=phi_i(x)+psi_j(y)`.

The actual functionally reduced external section module is the subset

`S_(d,e)={max_(i,j)(B_(i,j)+c_(i,j)):c_(i,j) in R_max}`

of continuous tropical functions on `C_p x C_q`, with the uniform topology.
This is the finite-depth moduli space of periodic mixed sections.  It is not
an affine envelope of a set of labels: its points are the section functions
themselves.

## 2. The intrinsic regular locus

Call a section `f in S_(d,e)` regular if it has a presentation in which,
for every extremal pair `(i,j)`, there is a point `(x_(i,j),y_(i,j))` at
which `B_(i,j)+c_(i,j)` is the unique maximizer.  This condition is
intrinsic.  Indeed the extremal rays of the section module are intrinsic,
and unique activity says that deleting that ray changes the function in a
neighborhood of the witness point.

Write `S_(d,e)^reg` for this locus.

### Proposition (regular coefficient theorem)

The following statements hold.

1. `S_(d,e)^reg` is nonempty and open in `S_(d,e)`.
2. Every regular section has a unique finite coefficient vector
   `(c_(i,j)) in R^(de)` relative to the fixed extremal representatives.
3. The coefficient map restricts to a local homeomorphism

   `Sigma^reg:U^reg subset R^(de) ->S_(d,e)^reg`.

4. Consequently `S_(d,e)^reg` is a real `de`-manifold (possibly with
   several open chambers) whose cotangent bundle is canonically trivialized
   by the ordered differentials `dc_(i,j)`.

### Proof

The strict-dominance construction for the one-dimensional extremal rays
provides offsets `u_i,v_j` and witnesses `x_i,y_j` such that

`phi_i(x_i)+u_i>phi_k(x_i)+u_k` for `k!=i`,

and similarly in the second factor.  At `(x_i,y_j)`, the pair `(i,j)` is
then the unique maximizer of the mixed presentation with coefficients
`u_i+v_j`.  This proves nonemptiness.

For a fixed regular section choose one witness for every pair.  Finiteness
gives a minimum positive dominance gap `gamma`.  Perturbing every
coefficient by less than `gamma/4` preserves all unique-dominance
inequalities.  On that coefficient cube,

`f_c(x_(i,j),y_(i,j))=B_(i,j)(x_(i,j),y_(i,j))+c_(i,j)`.

Hence evaluation recovers all coefficients continuously, proving local
injectivity and a continuous local inverse.  The maximum operation is
1-Lipschitz in the coefficient sup norm, so the forward map is continuous.

There is also an intrinsic recovery formula.  If `k=(i,j)` and `B_k` is
active somewhere, then

`c_k=inf_z(f(z)-B_k(z))`.

Indeed `f>=B_k+c_k` everywhere, while equality holds at an activity point.
Thus every active coefficient is uniquely determined by the section.  The
infimum functional is 1-Lipschitz for the uniform norm, so the recovered
coefficient vector varies continuously with `f`.  If `f'` is sufficiently
uniformly close to a regular `f`, its recovered coefficients remain close
to those of `f`; the positive dominance gaps at the fixed witnesses then
show that every extremal remains active.  Hence the regular image is open
in the section-moduli topology and the coefficient recovery is its local
inverse.

The recovered coefficient maps are compatible on overlaps because both
recover the unique minimal coefficient vector.  They therefore define the
claimed manifold atlas and the global ordered cotangent frame.  QED.

## 3. Intrinsic cotangent cohomology

Let `Omega_(d,e)^per` be the cotangent sheaf of
`S_(d,e)^reg`.  The proposition gives

`Omega_(d,e)^per ~=O_(S^reg) tensor_R R[Ext(E)xExt(F)]^vee`.

Thus every fiber has rank `de`, and its determinant has the distinguished
lexicographic generator.  This is now the cotangent of an open moduli space
of actual periodic sections.  No Boolean affine relaxation and no freely
adjoined tangent directions enter its definition.

The external-product identity for extremal rays gives the canonical
Kunneth isomorphism

`Omega_(d,e)^per
 ~=Omega_d^per boxtimes Omega_e^per`

on the product regular charts.  Principal translations add the same
function to every section, preserve unique-dominance regions and act by
translations in coefficient coordinates; their differential is the
identity.  Therefore the cotangent and its determinant descend through
principal classes.

## 4. Placement on the spherical square

Apply the construction on every component of the periodic pair pullback
and to every finite depth.  The resulting cotangent bundles are finite free
coefficient objects on the periodic section topos.  Derived direct image
along `Pi_per` places them on `Y_S`.  Their integral lattices are the free
groups on the ordered extremal pairs, and their nuclear components are
obtained by scalar extension to `O_C`; hence they define objects of
`Perf_DN(Y_S)`.

Evaluation at the Yoneda unit identifies the underlying section object
with `R Gamma(Y_S,F_per(x))`.  The cotangent is therefore attached to the
regular locus of the intrinsic total coefficient-section moduli of
`F_per(x)`.

## 5. Continuous determinant

At Frobenius depths `(r,s)`, the ranks are `d_(p,r)(a)d_(q,s)(b)`.  Give
the ordered determinant generator the norm

`exp(-p^(-r)q^(-s)d_(p,r)(a)d_(q,s)(b))`.

The one-dimensional periodic Riemann--Roch limits give the canonical
continuous determinant

`lambda_per(a,b)=(R*1,exp(-ab))`.

For finite prime support its exponent is `d_1(x)d_2(x)`.  The asymptotic
comparison with the negabinary system identifies this based determinant
with `lambda_code`; the latter becomes an independent spherical
certificate of the intrinsic periodic answer.

## 6. What is and is not proved

This construction resolves the central conceptual objection to the framed
code: the replacement cotangent is the cotangent of a genuine regular
section moduli space.  It does not identify that moduli space with the raw
spherical bounded-section functor, which is impossible by the exponential
rank theorem.

For arbitrary positive periodic divisors, the published squeeze maps must
be used to pass from special divisors to cofinal special approximants.  The
continuous determinant is independent of that cofinal choice by the
one-dimensional limit theorem.  A full pro-functorial cotangent comparison
with every negabinary effective transition is not required after
`Omega^per` replaces `H^cot` as the cohomology object, but no such
comparison is claimed.

# Deligne--nuclear and arithmetic compatibility of periodic cohomology

## 1. Perfect Deligne--nuclear realization

For a fixed prime pair and finite periodic depths `(r,s)`, let

`Ext_(r,s)(x)=Ext(E_(p,r)(x_1)) x Ext(E_(q,s)(x_2))`.

It is a finite canonically slope-ordered set.  Define

`P_(r,s),Z(x)=O_Z tensor_Z Z[Ext_(r,s)(x)]`,

`P_(r,s),C(x)=O_C tensor_R R[Ext_(r,s)(x)]`.

Their real base changes are canonically identified by the common extremal
basis.  Hence

`P_(r,s),DN(x)=(P_Z,P_C,alpha_ext)`

is a finite free object of `Perf_DN(Y_S)`.  Enriched Yoneda identifies the
underlying extremal module with the finite-depth global sections of the
periodic coefficient line.  Thus this is a perfect linearization of actual
intrinsic coefficient cohomology, not of a separately chosen digit set.

Cartesian products of extremal sets give canonical Kunneth isomorphisms

`P_(r,s),DN(x) ~=P_(r),DN(x_1) tensor P_(s),DN(x_2)`.

Principal translations preserve slopes and their order, so these objects
and their determinant lines descend through principal divisor classes.

## 2. Continuous determinant and the code line

Give the ordered extremal wedge the periodic trace norm

`exp(-p^(-r)q^(-s)#Ext_(r,s)(x))`.

The periodic one-dimensional limits prove that the based determinant lines
converge to

`lambda_per(x)=(R*1,exp(-d_1(x)d_2(x)))`.

The asymptotic comparison theorem of the preceding note constructs, for
each divisor, an isomorphism in the quadratic asymptotic perfect category
between this system and the cofinally rescaled negabinary cotangent.  Its
determinant is the canonical based isometry

`lambda_per(x) ~=lambda_code(x)`.

Accordingly the intrinsic object should replace `H^cot` in the row-A
tuple.  The negabinary system remains an independent spherical chart and
a certificate for the same continuous determinant; it is not renamed as
the intrinsic section cotangent.

## 3. Nuclear arithmetic action

On the nuclear component define

`rho_n^per(delta_r v)=delta_(nr)v`.

Equivalently this is left convolution by `delta_n` on the
`C_R`-coefficient.  It commutes with restrictions of periodic section
objects, with the extremal linearization and with Kunneth, because it acts
only on the scalar factor.  It satisfies

`rho_m^per rho_n^per=rho_(mn)^per`.

For `n>1`, augmentation to the real component sends `delta_n` to zero.
Taking the zero endomorphism on the integral component therefore gives a
well-typed endomorphism of the Deligne homotopy-pullback object.  For `n=1`
take the identity.  Thus the action is defined in the same
Deligne--nuclear category as the cohomology and contact complexes.

## 4. Compatibility with the Witt contact

Row B constructs from the Witt orbit of `F_n` the perfect complex

`L_n=[O_Z --Phi_n(1)--> O_Z]`.

It proves the objectwise equivalence

`L_n ~=C_p` for `n=p^k`, and `L_n~=0` for mixed prime support.

The nuclear coefficient action and this dynamic contact are joined by the
same point mass:

`ell(delta_n)=Lambda(n)
 =-log||det_tor L_n||`.

This is a commutative determinant-degree comparison in `Perf_DN`; no trace
of a raw section operator is substituted for it.  Since the periodic
cohomology action is left convolution by the same `delta_n`, its arithmetic
label, composition and contact functional agree with row B.

## 5. Compatibility with the nuclear Lefschetz character

The distributional map of row C sends

`delta_n |->delta_(n^-1)`

and left convolution to the multiplier `U_n`.  Consequently the action on
periodic Deligne--nuclear cohomology fits into the already proved chain

`rho_n^per ->delta_n ->U_n`,

while the contact fits into

`L_n ->deg_det(L_n)=ell(delta_n)=Lambda(n)`.

Therefore

`sum_(n>=2)deg_det(L_n)U_n
   =sum_(n>=2)Lambda(n)U_n
   =Z partial(Z^-1)`

is unchanged.  Rows B and C use the same coefficient action and the same
perfect contact after replacing framed code cohomology by intrinsic
periodic coefficient cohomology.

## 6. Remaining naturality issue

The arithmetic action is compatible with the periodic transition maps and
with the continuous determinant.  What is not yet proved is that the
objectwise asymptotic cotangent comparison with the negabinary system is a
natural transformation for every effective divisor inclusion.  This does
not obstruct using `P_DN` as the intrinsic cohomology object, but it does
obstruct claiming a global equivalence of the two cotangent pro-functors.

The clean closure route is therefore:

1. promote `P_DN`, not the code tangent, to the cohomology entry of row A;
2. retain the proved based determinant isometry with `lambda_code`;
3. state the negabinary construction as an auxiliary spherical
   determinant certificate;
4. do not claim an equivalence of cotangent transition systems unless the
   remaining naturality square is proved.

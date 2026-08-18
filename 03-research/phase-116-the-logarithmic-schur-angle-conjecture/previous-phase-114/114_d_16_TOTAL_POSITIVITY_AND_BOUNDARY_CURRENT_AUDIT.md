# Row (d): typed audit of total positivity and the boundary current

## Status

This note records a pivot in the attempt to prove row (d).  It proves that
ordinary total positivity is not the missing Hodge mechanism, identifies the
exact potential space on which a boundary-current construction must act, and
separates a genuine geometric input from a reformulation of Weil positivity.
No zero of `xi` and no sign conclusion equivalent to RH is used.

## 1. Three positivity notions which must not be confused

In logarithmic coordinates put

\[
 F(t)=e^{t/2}f(e^t),\qquad (S_aF)(t)=F(t-a).
\]

The finite-place contact has the exact form

\[
 K(F,F)=2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
       \operatorname{Re}\langle F,S_{\log n}F\rangle .       \tag{1}
\]

The measure

\[
 \mu_{\rm pp}=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                  \delta_{\log n}
\]

is positive.  This fact has only order-one content.  It does **not** imply
either of the following stronger assertions:

1. that the completed heat kernel is positivity preserving;
2. that the corresponding convolution kernel is totally positive of order
   two;
3. that the completed Weil form has the required sign on the primitive
   subspace.

The first two assertions fail in the literal completed system.  The first
Beurling--Deny cross inequality fails for separated nonnegative bumps, and
the exact Gamma density is strictly log-convex, so its adjacent `TP_2` minor
has the wrong sign.  Independently, the Euler-product exponent lattice has
the exact minor

\[
 w(6)^2-w(3)w(12)=-\frac1{2916}.                         \tag{2}
\]

Thus neither a pointwise positive semigroup nor a variation-diminishing
factorization into totally positive local Euler blocks can prove row (d).
These failures do not decide the third assertion, which is conditional
positivity after two boundary conditions.

## 2. The exact primitive potential space

Let

\[
 L=\frac{d^2}{dt^2}-\frac14
\]

and define

\[
 \mathcal P=
 \left\{F\in C_c^\infty(\mathbb R):
   \int_{\mathbb R}e^{t/2}F(t)\,dt=
   \int_{\mathbb R}e^{-t/2}F(t)\,dt=0\right\}.           \tag{3}
\]

### Proposition 2.1

The map

\[
 L:C_c^\infty(\mathbb R)\longrightarrow\mathcal P       \tag{4}
\]

is a linear bijection.

### Proof

For `u` compactly supported, two integrations by parts give

\[
 \int e^{\pm t/2}Lu(t)\,dt=0,
\]

so the image lies in `P`.  Conversely, for `F in P` set

\[
 u(t)=\int_{\mathbb R}e^{|t-s|/2}F(s)\,ds.               \tag{5}
\]

If `t` is to the right of the support of `F`, the first condition in (3)
or the second one, according to the displayed exponential, makes (5) zero;
the other condition does the same on the left.  Hence `u` is compactly
supported.  Distributionally,

\[
 \left(\frac{d^2}{dt^2}-\frac14\right)e^{|t|/2}=\delta_0,
\]

and therefore `Lu=F`.  Finally, a compactly supported solution of `Lu=0`
is zero, since on every interval it is a linear combination of
`e^{t/2}` and `e^{-t/2}` and unique continuation applies.  Thus (4) is
bijective.

### Consequence 2.2

The two ruling degrees are not auxiliary constraints.  They are exactly the
two boundary values which make the Green potential (5) compactly supported.
Every primitive mixed class has a unique compact potential `u`.

## 3. The continuous Hodge form and the arithmetic defect

For `F=Lu`, integration by parts gives

\[
 Q_0(F,F)=\iint e^{|t-s|/2}F(t)\overline{F(s)}\,dt\,ds
 =-\int\left(|u'|^2+\frac14|u|^2\right)dt.              \tag{6}
\]

This is an unconditional Hodge-index form, with equality only for `F=0`.
The completed arithmetic form is

\[
 B_{\rm nuc}(F,F)=Q_0(F,F)+R_{\rm ar}(F,F),              \tag{7}
\]

where `R_ar` is the paired prime-discrepancy plus the forced Gamma current.
Equation (7) shows precisely what a compactifying boundary must control:
not the positive jump measure by itself, but a signed cross-place current.

## 4. Boundary-current gate

Let `W` denote the completed Weil distribution in the logarithmic
coordinate.  A proposed compactification current `Theta` is called
*independent* if it is obtained from the section theory and its boundary
functors before identifying its intersection pairing with `W`.

### Theorem 4.1

Suppose a boundary-current construction has the following properties.

1. Its mixed class associated with `F=Lu` depends functorially on `u`.
2. Its two boundary degrees are the two functionals in (3).
3. Its primitive self-intersection is nonpositive by an intrinsic Hodge or
   Castelnuovo--Severi theorem.
4. Only after that theorem is proved, a comparison theorem identifies the
   self-intersection with `B_nuc(F,F)`.

Then row (d) follows.  Conversely, if `Theta` is defined from `W` and its
claimed curvature positivity is exactly the nonpositivity of
`B_nuc` on `P`, the construction is an equivalent reformulation of row (d),
not a proof of it.

### Proof

The forward implication applies property 3 to the unique potential supplied
by Proposition 2.1 and then property 4.  The converse is logical: the
asserted curvature sign, after the defining identification with `W`, is the
desired inequality on precisely the full primitive test space `P`.

### Corollary 4.2 (screw-function audit)

Passing from `W` to its twice integrated continuous screw kernel removes the
distributional singularity but does not add a sign theorem.  Positivity of
that kernel on every finite window is equivalent to Weil positivity and
hence to RH.  Consequently the screw kernel is the correct analytic model
for the missing boundary current, but its positivity cannot be imported as
the geometric proof required in Theorem 4.1(3).

## 5. What an extension of row (a) must actually provide

The periodic Yoneda construction in row (a) gives effective section objects
on the external ruling sector.  To supply the independent input in
Theorem 4.1 it must be extended to the completed mixed correspondence module
with all of the following structures:

1. an object `H^0(M)` for every mixed class and functorial multiplication
   `H^0(M) tensor H^0(N) -> H^0(M+N)`;
2. two boundary restriction maps whose degrees are (3);
3. a duality object and a Riemann--Roch identity defined before using the
   Meyer spectral quotient;
4. an effectivity theorem strong enough to run the dimension estimate in
   the Castelnuovo--Severi argument;
5. a comparison theorem identifying the resulting intersection with
   `B_nuc`.

Kunneth, determinant additivity and the local identities
`deg_det(L_n)=Lambda(n)` do not imply item 4.  They determine Euler
characteristics and local contacts, whereas Castelnuovo--Severi requires an
inequality for actual effective sections.  Likewise the odd Meyer quotient
cannot be used to define effectivity: its spectral decomposition already
contains the zero divisor and would make the sign argument circular.

## 6. Result of this pivot

The ordinary total-positivity route is closed in its natural pointwise
cone.  The boundary-current route survives, but only in the typed form of
Theorem 4.1: its missing input is an intrinsic mixed section/effectivity
theorem, not another representation of the Weil distribution.  The next
construction attempt must therefore work in the enriched periodic category
and build mixed effective sections before comparison with the nuclear trace.


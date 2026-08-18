# The canonical arithmetic-pullback bridge

## 1. New geometric input

Connes--Consani, *On the Jacobian of the completed spectrum of Z*
(arXiv:2602.15941), constructs the completed arithmetic curve

`X_abs = overline(Spec Z)`

with a spherical structure sheaf and, for every arithmetic divisor
`D=(L,||.||)`, an actual sheaf of modules `O(D)`.  The same paper constructs
the arithmetic pullback

`pi : X_vis -> X_abs`

of the Riemann sector along the extended Abel--Jacobi map.  Its fiber over a
finite prime `p` is canonically

`C_p = R_+^x / p^Z`.

The neutral point is not chosen by hand: it is the standard subgroup
`Z[1/p] subset R`.  The group law is induced by tensor product of the
corresponding rank-one groups.

Connes--Consani, *On the Absolute Geometry of Spec Z*
(arXiv:2606.06604), further derives the same `C_p` as the real locus of the
complex Tate curve obtained from the absolute `F_1`-curve, and relates its
structure to the Scaling Site.  Thus the periodic orbit is a canonical
geometric fiber of the arithmetic curve, rather than an object attached to
a prime label after the fact.

## 2. Passage to the square

Form the square

`Y_abs = X_abs x X_abs`

and the product pullback

`Pi = pi x pi : X_vis x X_vis -> Y_abs`.

Over the closed point `(p,q)`, its fiber is canonically

`Pi^-1(p,q)=C_p x C_q`.

Let `H_per` be the union of these finite-prime pair fibers.  Restriction of
`Pi` gives a canonical map

`Pi_per : H_per -> Y_abs`.

Every component has a distinguished point `(Z[1/p],Z[1/q])`.  The periodic
quasi-tropical structure sheaves `O_p,O_q` and their external product are
therefore attached to an actual geometric fiber.  This resolves the
earlier carrier-identification problem at the level of spaces: the map is a
pullback from the arithmetic Abel--Jacobi geometry, not a dictionary
`e_p <-> C_p`.

## 3. Canonical divisors on the fibers

Write `o_p` for the neutral point of `C_p`.  For a real number `t`, let

`D_p(t)=t[o_p]`.

Its degree is `t`.  For an external prime divisor

`x=sum_p a_(p,1)e_(p,1)+sum_q b_(q,2)e_(q,2)`,

the pair `(p,q)` receives the external periodic divisor

`D_(p,q)(x)=pr_1^*D_p(a_(p,1)log p)
             +pr_2^*D_q(b_(q,2)log q)`.

No origin or period is chosen: both come from the arithmetic pullback.
Principal translation on either periodic curve gives canonical
isomorphisms of the corresponding section objects.

## 4. An induced coefficient sheaf with exact global sections

For finite support, let `M_(p,q)(x)` be the functionally reduced external
tensor of the two published periodic section modules.  Put the constant
coefficient sheaf with this fiber on the connected component
`C_p x C_q`, and define

`F_pull(x)=Pi_per,* product_(p,q) underline(M_(p,q)(x))`.

Direct image is a sheaf, and global sections of a constant sheaf on each
connected component are the coefficient object itself.  Consequently

`Gamma(Y_abs,F_pull(x))=product_(p,q)M_(p,q)(x)`

and

`cdim Gamma(Y_abs,F_pull(x))=d_1(x)d_2(x)`.

Compared with the former holonomy construction, the improvement is
structural: `Pi_per` is now the restriction of a canonical arithmetic
pullback of spaces, and the origins used to define the periodic divisors
are its canonical neutral sections.

## 5. What this bridge proves and what it does not

This construction proves:

1. a canonical geometric map from all periodic pair carriers to the square
   of one arithmetic curve;
2. canonical origins, periods and pair divisors on its fibers;
3. an induced sheaf on that square whose global coefficient sections are
   exactly the external packet and whose dimension is `d_1d_2`;
4. principal invariance inherited from actual periodic divisor theory.

The source papers do not prove that the constant coefficient sheaf
`F_pull(x)` is an invertible `O_(Y_abs)`-module.  Nor do they identify its
global sections with all sections of the external product line bundle on
`C_p x C_q`.  A nonconstant local section of the periodic structure sheaf
does not preserve a constant coefficient subsheaf, so module invertibility
cannot be asserted from the direct-image construction.

Likewise, the construction supplies ordinary global sections but not the
missing middle cohomology of the square.  The canonical arithmetic
pullback closes the *carrier comparison* gate; it does not by itself close
the line-bundle, `R Gamma`, determinant or surface Riemann--Roch gates.

## 6. Consequence for the research route

The correct carrier for the next internalization attempt is no longer an
ad hoc union of holonomy tori over the Haran boundary.  It is the canonical
pair pullback `X_vis x X_vis -> X_abs x X_abs`.  The remaining problem can
now be stated internally: construct an exact section functor for external
products of the divisor modules `O(D)` whose restriction to every fiber is
the periodic continuous section theory and whose determinant compares with
finite contact.  No label-only comparison remains in that formulation.


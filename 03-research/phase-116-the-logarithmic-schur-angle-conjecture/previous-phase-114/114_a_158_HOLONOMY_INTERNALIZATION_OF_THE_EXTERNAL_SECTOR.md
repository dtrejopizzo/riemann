# Holonomy internalization of the external valuative sector

## 1. Prime periodic orbits from boundary torsors

Let `L_p` be the metrized rank-one torsor obtained by restricting a prime
Cartier class to a valued mixed boundary.  On its two-chart presentation the
positive transition is `p` or `p^-1`, according to orientation.  The group
of positive frames is `R_+^x`.  Iterating the Cech transition gives the
holonomy action

`z |-> p^k z,  k in Z`.

Define the positive holonomy object

`Hol^+(L_p)=R_+^x / p^Z`.

This construction is independent of the two choices involved:

* reversing the boundary orientation replaces `p` by `p^-1` and leaves the
  generated subgroup unchanged;
* an isometric change of rational frame multiplies both endpoint frames by
  positive norm-one rational units, hence by `1`, and leaves the positive
  transition unchanged.

Therefore `Hol^+(L_p)` is canonically the periodic orbit `C_p` of length
`log p`.  The equality is not a dictionary based only on the label: the
period and its metric are reconstructed from the Cech holonomy of an actual
torsor on the Haran carrier.

## 2. The pair-holonomy fibration

Let `B` be the disjoint union of the two valued mixed boundaries of the
regularized pro-square.  For every ordered prime pair `(p,q)`, form over `B`
the associated positive pair-holonomy object

`H_(p,q)=Hol^+(L_(p,1)) x Hol^+(L_(q,2)) = C_p x C_q`.

Let

`pi : H_ext = disjoint_union_(p,q) H_(p,q) -> Y`

be the morphism which first projects each associated holonomy object to its
boundary anchor and then includes `B` in `Y`.  This is a morphism of sites if
`H_ext` is equipped with the disjoint-union topology and `Y` with its pro-
Zariski chart topology: inverse image of an open is the union of the
components whose anchor lies in that open, and covers pull back to covers.

The construction is functorial under supportwise refinement.  Once `p,q`
belong to the active support, their metrized torsors pull back along every
later transition with the same holonomy.  Thus the associated objects form
bounded eventually constant pro-data, exactly as the prime torsors do.

## 3. A valued coefficient sheaf on the carrier

For an effective external divisor

`D=sum_p a_(p,1)e_(p,1)+sum_q b_(q,2)e_(q,2)`,

retain only the finitely many components with `a_(p,1)b_(q,2)!=0`.  Let

`M_(p,q)(D)=H^0(C_p,D_p) widehat-boxtimes_red H^0(C_q,D_q)`

be the already proved functionally reduced external tensor module, where the
periodic divisor classes have degrees

`a_(p,1) log p` and `b_(q,2) log q`.

Put the constant sheaf with fiber `M_(p,q)(D)` on the connected compact
holonomy space `H_(p,q)=C_p x C_q`.  Define the internal valued coefficient
sheaf on `Y` by finite pushforward

`F_val(D)=pi_* product_(p,q) underline(M_(p,q)(D))`.

This is an candid sheaf of coefficient modules on `Y`: direct image of a
sheaf along a morphism of sites is a sheaf, and only finitely many factors
occur for each `D`.  Since every pair-holonomy component is connected, the
global sections of its constant sheaf are its fiber.  Consequently

`Gamma(Y,F_val(D)) = product_(p,q) M_(p,q)(D)`.

The right side is exactly the previously constructed packet `H_val(D)`.  The equality
is now a direct-image theorem from a holonomy fibration canonically derived
from the carrier's metrized torsors.

## 4. Functorial properties

### Principal invariance

A principal change of the prime torsor changes its Cech representative by
endpoint frames.  Its positive metric holonomy is unchanged.  On each
periodic orbit, a principal tropical function translates the section sheaf
isomorphically.  The componentwise isomorphisms push forward, proving that
`F_val(D)` depends only on the metrized external divisor class.

### Tensor product

Periodic pointwise tropical multiplication gives on the fibers

`M_(p,q)(D) x M_(p,q)(E) -> M_(p,q)(D+E)`.

After inserting the degree-zero unit on a component absent from one factor,
the finite products and direct image give associative, symmetric maps

`F_val(D) x F_val(E) -> F_val(D+E)`.

Thus `D |-> F_val(D)` is a lax symmetric monoidal internal coefficient-sheaf
functor on the effective external prime sector.

### Continuous dimension and determinant

The external dimension theorem on every component and additivity over the
finite disjoint union give

`cdim Gamma(Y,F_val(D)) = d_1(D)d_2(D)`.

The determinant norm `exp(-d_1d_2)` and its polarization consequently agree
with the coefficient-one RR line.  This is no longer merely an attachment
of two carriers by a common label: the periodic carrier is the holonomy
object associated to the actual metrized boundary torsor, and its sheaf is
pushed forward to `Y`.

## 5. Exact scope

This construction internalizes the previously external packet as the global
sections of a canonical coefficient sheaf on `Y`.  It supplies a concrete
`F_val(D)`, principal invariance, tensor maps, global sections and
coefficient-one dimension.  It does **not** yet identify `F_val(D)` with a
sheaf of local tropical functions or with a line-bundle twist of a single
structure sheaf: the use of a constant sheaf deliberately proves no more
than the data justify.

It does not yet close strong row A because:

1. the pair-holonomy fibration is supported at the valued boundary and has
   no component for a genuinely mixed correspondence divisor;
2. reduced finite contact `[Z --p--> Z]` has not been glued to the boundary
   holonomy coefficient sheaf by an exact or derived square;
3. the construction gives `Gamma`, not a derived `R Gamma` with higher
   cohomology and a surface Riemann--Roch theorem;
4. it has not been compared with the internal nuclear correspondence sheaf
   of the preceding note.

The next required object is a derived gluing category whose finite fiber is
   the contact complex and whose boundary fiber is `F_val(D)`, with mixed
correspondences acting on both.

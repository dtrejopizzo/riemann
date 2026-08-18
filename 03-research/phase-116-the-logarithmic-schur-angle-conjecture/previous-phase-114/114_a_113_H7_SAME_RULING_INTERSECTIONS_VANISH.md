# 114.a.113 — H7: distinct same-ruling prime intersections vanish

```
+------------------------------------------------------------------------+
| INPUT       Regular prime Cartier data D_(p,i) on Y^reg.               |
| PUSHOUT     Their fiber product is the quotient killing both scalars.  |
| BEZOUT      On one ruling, p and q generate 1 whenever p != q.         |
| RESULT      D_(p,i) x_Y D_(q,i) is empty; its intersection mass is 0.  |
| REMAINS     Self and opposite-ruling products, plus Delta^2.           |
+------------------------------------------------------------------------+
```

## 1. Double principal quotients

Let `A` be a chart of the repaired square `Y^reg`.  For central scalars
`s,t`, the two principal closed data have coordinate objects

\[
 A_s=A/E((s)),\qquad A_t=A/E((t)).                                     \tag{1.1}
\]

The universal property of quotient and pushout gives

\[
 A_s\otimes_A A_t\simeq A/E((s,t)),                                   \tag{1.2}
\]

where the right side is the universal quotient in which both scalars vanish.
Indeed, maps from either side to a target are exactly maps from `A` sending
both `s` and `t` to zero.  Consequently

\[
 D_A(s)\times_{\operatorname{Spec}A}D_A(t)
 \simeq\operatorname{Spec}A/E((s,t)).                                  \tag{1.3}
\]

This argument is valid chartwise and is compatible with restriction because
central localization commutes with the regular reflection by `a110`.

## 2. Bézout on a fixed ruling

Fix a ruling `i` and distinct rational primes `p != q`.  Choose integers
`u,v` with

\[
 up+vq=1.                                                              \tag{2.1}
\]

The ruling map `F(Z)->A` preserves the ordinary ring addition encoded by its
distinguished binary vector.  Hence every map from `A` to a generalized ring
which kills both `i_i(p)` and `i_i(q)` also kills the image of the right side
of (2.1), namely the unit.  Such a map factors only through the zero object.
By the universal property in Section 1,

\[
 A/E((i_i(p),i_i(q)))=0.                                               \tag{2.2}
\]

### Theorem 2.1 (same-ruling disjointness)

For `p != q` and `i in {1,2}`,

\[
 D_{p,i}\times_{Y^{\rm reg}}D_{q,i}=\varnothing.                       \tag{2.3}
\]

The proof is local by (2.2), and the empty identifications agree on overlaps.
It uses no assumed intersection theory and survives every pro-transition.

## 3. The corresponding partial intersection entries

The degree of the empty zero-cycle is canonically zero.  Thus every global
intersection theory extending scheme-theoretic proper intersections is
forced to satisfy

\[
 I(D_{p,i},D_{q,i})=0\qquad(p\ne q).                                   \tag{3.1}
\]

Together with `a112`, the presently geometric part of the matrix is

\[
 I(\Delta,D_{p,i})=\log p,
 \qquad
 I(D_{p,i},D_{q,i})=0\quad(p\ne q).                                   \tag{3.2}
\]

For two formal effective divisors on one ruling with disjoint prime supports,
all pairwise products are empty, so their partial intersection is zero.
This is bilinear on the domain of disjoint-support pairs.

## 4. Exact unresolved block

No entry below follows from Bézout:

\[
 I(\Delta,\Delta),\qquad
 I(D_{p,i},D_{p,i}),\qquad
 I(D_{p,1},D_{q,2}).                                                    \tag{4.1}
\]

The first two are improper self-intersections and require normal/Green data.
The last fiber product exists as the generalized quotient

\[
 \operatorname{Spec}A/E((i_1(p),i_2(q))),                              \tag{4.2}
\]

but the two scalars belong to different additions, so (2.1) cannot be used.
Haran provides no length or Euler-characteristic functor assigning (4.2) a
canonical real degree.  H7-REG-MIXDEG is therefore reduced to the
opposite-ruling block and the three self-intersection types in (4.1).

This advances but does not close H7-REG-INTER, row A or RH.

## 5. Verification scope

`114_a_113_h7_same_ruling_intersection_verify.py` checks Bézout certificates,
the quotient universal-property model in finite rings, disjoint-support
bilinearity and the exact unresolved matrix markers.  The generalized-ring
statement is the displayed universal-property proof.

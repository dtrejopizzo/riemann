# 114.a.104 — H7: the signed arithmetic plane is not tame

```
+------------------------------------------------------------------------+
| TARGET      D_centre = delta_1^t o delta_2 versus its Cartesian grid.  |
| SEPARATOR   F(Z) Pi N, Haran's commutative infinitesimal extension.     |
| RESULT      Their N-components differ by nine independent generators.  |
| CLOSED      H7-XDEF-12 is NEGATIVE; H7-TAME-PLANE is FALSE.            |
| SCOPE       This kills the tame-promotion route, not PRIME-REG itself.  |
+------------------------------------------------------------------------+
```

## 1. A commutative signed target

Put `C=F{+-1}` and `R=F(Z)`.  Haran constructs the commutative
`R`-module

\[
 N_{Y,X}=\mathbb Z\langle[a|b]:a\in\mathbb Z^Y,
 b\in\mathbb Z^X\rangle/
 \bigl(\lambda[a|b]=[\lambda a|b]=[a|\lambda b]\bigr).       \tag{1.1}
\]

It has an involution and a relative derivation `d:R->N`.  On a binary row,

\[
 d(a,b)=[a|e_1]+[b|e_2]-[1|(a,b)],                           \tag{1.2}
\]

and `d` vanishes on `C`.  Since `R` is totally commutative and `N` is a
commutative `R`-module, Haran's infinitesimal extension

\[
 H=R\Pi N,\qquad
 (x,m)\circ(y,n)=(x\circ y,x\circ n+m\circ y),               \tag{1.3}
\]

is a commutative `F`-ring with involution.  The derivation adjunction makes

\[
 \phi_1(x)=(x,0),\qquad \phi_2(x)=(x,d x)                    \tag{1.4}
\]

homomorphisms of `F`-rings with involution.  They agree on `C`; hence the
pushout property gives a homomorphism from the **full signed plane**

\[
 P=R_1\otimes_C R_2\longrightarrow H.                       \tag{1.5}
\]

Thus separation in `H` survives every commutativity and integer-cancellation
relation used to define `P`; it is not merely a positive-graph separation.

There is no category mismatch here.  Haran 2017 gives an adjunction
`F:CGR -> CFR^t:U` with `U F ~= id`; hence `F` is fully faithful and, being
a left adjoint, preserves the signed pushout.  The prop plane used above is
therefore `F` of the commutative-generalized-ring plane used in the tree
presentation.  Equivalently, the two ruling maps to `H` induce the required
map directly by the pushout universal property in `CFR^t`.

## 2. Exact image of the first cross defect

Write

\[
 c=(1,1)^t,\quad r=(1,1),\quad
 f_1=(1,0)^t,\ f_2=(0,1)^t,\quad e_1=(1,0),\ e_2=(0,1).
\]

Send the first ruling through `phi_1` and the second through `phi_2`.  From
(1.2), `h=d(r)=[1|e_1]+[1|e_2]-[1|r]`.  Therefore the `N_{2,2}` components
of the two operations from `a103` are

\[
 E_{\rm centre}=[c|e_1]+[c|e_2]-[c|r],                       \tag{2.1}
\]

and, after the canonical grid permutation,

\[
 E_{\rm grid}=\sum_{i=1}^2
   \bigl([f_i|e_1]+[f_i|e_2]-[f_i|r]\bigr).                  \tag{2.2}
\]

The base `R`-component of both complete operations is the all-one matrix.
The two displayed infinitesimal components have the same ordinary matrix
image, namely zero, but they are not equal in `N`.

### Lemma 2.1 (normal form for `N`)

For a nonzero integer vector `v`, write uniquely
`v=s(v) g(v) p(v)`, where `g(v)>0` is its content, `s(v) in {+-1}`, and
the primitive vector `p(v)` has first nonzero coordinate positive.  Then

\[
 [a|b]\longmapsto
 s(a)s(b)g(a)g(b)\,[p(a),p(b)]                               \tag{2.3}
\]

identifies `N_{Y,X}` with the free abelian group on ordered pairs of such
primitive directions; a generator with a zero vector maps to zero.

### Proof

Formula (2.3) respects all three terms of the scaling relation in (1.1),
including negative and zero scalars.  Conversely, (1.1) reduces every
generator to exactly the displayed multiple of its primitive-direction
pair.  The two maps are inverse.  QED.

The three column directions `c,f_1,f_2` and the three row directions
`e_1,e_2,r` are pairwise distinct.  Consequently

\[
 E_{\rm centre}-E_{\rm grid}                                \tag{2.4}
\]

has nine distinct primitive-direction coordinates, each with coefficient
`+1` or `-1`, and is nonzero.  Hence its two preimages in `P` cannot be
equal.

### Theorem 2.2

\[
 \delta_1^t\circ\delta_2\ne
 (\delta_2\oplus\delta_2)\circ
 (\delta_1^t\oplus\delta_1^t)\quad\text{in }P.               \tag{2.5}
\]

Therefore H7-XDEF-12 is closed negatively.  By the sandwich-blindness
theorem of `a103`, the distinct pair (2.5) has identical scalar sandwiches,
so the signed arithmetic plane is **not tame**.  H7-TAME-PLANE is false.

## 3. Consequence for route A

This is a genuine decision, not a completion of row A.  It removes both
conditional promotions that required tameness:

* H7-AUG-FLAT plus H7-TAME-PLANE no longer proves all-arity PRIME-REG;
* H7-REAL-RES plus H7-TAME-PLANE is likewise unavailable.

It does **not** prove that H7-PRIME-REG is false: nontameness says that
scalar sandwiches do not separate all operations, whereas prime regularity
asks whether multiplication by each prime is injective on every component.
The live route is now direct: prove the componentwise cancellation purity
`(E_cancel:p)=E_cancel`, equivalently finish the residual p-CONVEX/p-DIVPATH
analysis, and only then transport the lattice, degree and gauge.

Primary source: Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Sections 7.5--7.8 (infinitesimal extensions, derivations, and the module
`N`).  The use of `N` avoids relying on the unproved injectivity statements
that are commented out in that source.

## 4. Verification scope

`114_a_104_h7_signed_plane_nontame_verify.py` implements the normal form
(2.3), computes (2.1)--(2.4), checks the common matrix shadow, and enforces
the scope distinction between nontameness and PRIME-REG.  The categorical
factorization (1.5) is the source theorem applied above; the script is an
exact symbolic regression check, not a substitute for it.

# 114.a.33 — H7 finite-moment dimension on the balanced ray

```
+--------------------------------------------------------------------------+
| CORRECTION  A lower-bound family need not itself be a section ring.      |
| CONSTRUCTION Retain 2r power moments modulo the least prime              |
|              ell>max(Q,3^r).                                             |
| SEPARATION  Vandermonde + balanced ternary uniqueness separate every     |
|             c in I_r(Q).                                                  |
| UPPER       The Laurent-sector moment image has at most ell^(2r)          |
|             elements.                                                     |
| ON A RAY    For r=Theta(d), Q=q^n and n asymp d, its log-size is          |
|             Theta(dn): quadratic, not operadically exponential.          |
| DESCENT     CLOSED by a_49 through H7-LNF.                               |
| OPEN        Extension/cofinality for all scalar trees and RR remain.     |
+--------------------------------------------------------------------------+
```

## 1. Correction to the acceptance test

Proposition 2.1 of `114_a_32` is an obstruction only to declaring the
balanced witnesses themselves to be the entire section algebra. A family
used to prove a lower bound for `H^0(D)` need not be closed under products;
the ambient section objects already carry the external multiplication of
`114_a_12`.

What must be compatible with the geometry is the quotient or normalized
dimension applied to the **ambient** bounded section set. This distinction
keeps the bounded family of `a_30` alive and changes the target from
"multiply two codes" to "measure all sections without counting every tree
presentation".

## 2. A finite moment quotient

Fix `r,Q>=1` and choose

\[
 H=\max(Q,3^r),\qquad
 \ell=\min\{p\text{ prime}:p>H\}.                       \tag{2.1}
\]

Let

\[
 G_{(\ell)}=\{x\in\mathbb Q_{>0}^{\times}:v_\ell(x)=0\},
 \qquad L_{(\ell)}=\mathbb Z_{(\ell)}[G_{(\ell)}].       \tag{2.2}
\]

Every label `|c_j|/Q` in the balanced code and the common dyadic tree
coefficient belong to this ring, because `ell>max(Q,3^r)>=3`. Reduction is
therefore literal; unlike a map from all of `Q`, it never attempts to reduce
`1/ell`. For `1<=s<=2r`, define

\[
 \chi_{s,\ell}:L_{(\ell)}\longrightarrow\mathbb F_\ell,
 \qquad [a/Q]\longmapsto(aQ^{-1})^s,                   \tag{2.3}
\]

with signs carried by the coefficient field. Their product is the ring map

\[
 \mathcal E_{r,Q}:L_{(\ell)}\longrightarrow(\mathbb F_\ell)^{2r}.
                                                               \tag{2.4}
\]

This is a finite quotient of the **Laurent source**. It becomes a quotient
of Haran's scalar subring `A_12` exactly when

\[
 \ker(\Phi|_{L_{(\ell)}})
 \subseteq\bigcap_{s=1}^{2r}\ker\chi_{s,\ell}.          \tag{H7-FMD}
\]

H7-FMD is weaker and more targeted than full H7-LNF: it asks only for the
finite moments needed in the specified bidegree.

## 3. Unconditional separation in the Laurent source

For `c=(c_0,...,c_{r-1}) in I_r(Q)`, put

\[
 B_r(c)=\sum_{j=0}^{r-1}3^j\mathrm{sgn}(c_j)
              [|c_j|/Q],                               \tag{3.1}
\]

omitting zero coordinates.

### Theorem 3.1 (finite-moment separation)

The restriction of `mathcal E_{r,Q}` to the family (3.1) is injective.

### Proof

Suppose two codes have the same `2r` moments. After grouping equal nonzero
absolute values in their difference, write

\[
 \sum_{i=1}^{t}C_i[x_i],\qquad t\le2r,                 \tag{3.2}
\]

where the `x_i` are distinct elements among
`1/Q,...,Q/Q`. For every `i`,

\[
 |C_i|\le2\sum_{j=0}^{r-1}3^j=3^r-1<\ell.             \tag{3.3}
\]

The first `t` moment equations have coefficient matrix

\[
 (x_i^s)_{1\le s,i\le t}.                              \tag{3.4}
\]

Its determinant is

\[
 \left(\prod_i x_i\right)
 \prod_{i<j}(x_j-x_i),                                 \tag{3.5}
\]

which is nonzero in `F_ell`: all numerators lie between `1` and `Q<ell`
and `Q` is invertible. Hence every `C_i` is zero modulo `ell`, and (3.3)
makes it zero as an integer.

For each fixed absolute value, the equality `C_i=0` is a balanced ternary
relation

\[
 \sum_j d_j3^j=0,\qquad d_j\in\{-2,-1,0,1,2\}.         \tag{3.6}
\]

At the largest nonzero digit, its absolute contribution is at least `3^j`,
whereas all lower digits total at most `3^j-1`. Thus every `d_j=0`, and the
two signed coordinate vectors agree. QED.

### Corollary 3.2 (Haran separation; unconditional after `a_49`)

If H7-FMD holds for `(r,Q)`, the bounded Haran trees `T_{d,n}(c)` of `a_30`
are pairwise distinct for every `c in I_r(Q)`.

This corollary uses only factorization of (2.4) through `A_12`; it does not
assume raw-cardinality H7-U.

Corollary 4.2 of `a_49` proves full H7-LNF, so the kernel on the left of
(H7-FMD) is zero. Therefore H7-FMD descent holds for every `(r,Q)` used here,
and the conclusion of Corollary 3.2 is unconditional.

## 4. Matching normalized upper bound in the Laurent sector

For every subset `S` of `L_(ell)`,

\[
 \#\mathcal E_{r,Q}(S)\le\ell^{2r}.                    \tag{4.1}
\]

Bertrand's postulate gives `ell<2H`, hence

\[
 \log\#\mathcal E_{r,Q}(S)
 \le2r\bigl(\log2+\max(\log Q,r\log3)\bigr).           \tag{4.2}
\]

Take `r=r_d=(log2/log3)d+O(1)` and `Q=q^n`. Along every fixed positive ray
`n/d -> lambda`, (4.2) is `O(dn)`. Theorem 3.1 and `a_30` give the matching
lower bound

\[
 \log\#\mathcal E_{r_d,q^n}
       \{B_{r_d}(c):c\in I_{r_d}(q^n)\}
 =\frac{\log2\,\log q}{\log3}dn-O(d\log d+n).          \tag{4.3}
\]

Thus the finite-moment image of the
ambient **Laurent sector `A_12`** has `Theta(dn)` logarithmic size on the
balanced ray.
The superquadratic leaf-multiset explosion of `a_31` is automatically
collapsed because the target itself has only `ell^(2r)` points.

This is the first lower-and-upper quadratic package on the same bounded
Laurent sector that does not require raw-cardinality H7-U. It is not yet an
upper bound or a dimension on every alternating scalar tree in Haran's
chosen-addition ring.

## 5. What is and is not closed

Closed unconditionally:

1. the finite quotient (2.4) on the Laurent source;
2. injectivity on the complete balanced code;
3. the matching `Theta(dn)` lower/upper size on fixed positive rays;
4. multiplicativity of each component moment on the Laurent source.
5. H7-FMD descent to `A_12`, by H7-LNF from `a_49`.

Still open:

1. **RR promotion:** `a_51` extends finite moments to every scalar tree on
   fixed rays. `a_57` later retracts the global cone claimed in `a_52` and
   hence the global moment dimension of `a_53`. What remains includes
   denominator-compatible transitions, sheaf exactness and the sharp
   comparison with the optimal code; `a_55` later proves that this comparison
   is false for the complete bounded image and replaces it by H7-SEL-RR/EXACT;
2. **degree functoriality beyond fixed rays:** `a_50` constructs compatible
   nested moduli on every fixed effective ray; arbitrary divisor
   presentations still require a common intrinsic system;
3. **canonicity beyond the two-prime ray:** replace `Q=q^n` by an intrinsic
   denominator-height attached to an arbitrary effective divisor;
4. **intersection/RR:** prove that the polarized leading coefficient of the
   finite-moment dimension is the intersection form required by row A.

Haran's equations (10.19)--(10.22) give multiplication and the two ordinary
ring structures; `a_49` supplies the missing factorization. They still do
not provide a global dimension/RR theorem. No claim about RH follows.

**Later strengthening (`a_51`).** Finite twisted-field bios extend odd
moments to the complete scalar bio, and an odd Vandermonde separates the
balanced code. This closes all-tree extension on fixed rays with a compatible
quadratic cofinal system. Global divisor-presentation canonicity remains.

**Attempted finite-global strengthening (`a_52`; retracted by `a_57`).**
Uniform blocks work separately at each bounded height, but their accumulated
old characteristics cannot evaluate all later denominators.

**Picard code strengthening (`a_53`; global target retracted by `a_57`).**
Standard representatives and odd-moment unit invariance extend the code
coefficient continuously to real degrees. They do not define a global
moment dimension without H7-DEN-TRANS.

**Bounded-saturation no-go (`a_55`).** A single genuine bounded cross-
contraction realizes every vector of a full moment block in linear bidegree.
Consequently the complete bounded moment image has a quadratic excess over
the code coefficient; the sharp comparison just mentioned is false for this
candidate dimension.

## 6. Verification scope

`114_a_33_h7_finite_moment_verify.py` exhaustively checks finite-moment
injectivity on small cross-polytopes, the Vandermonde determinants and the
finite-image upper bound. It treats H7-FMD as an explicit hypothesis and
does not by itself assert descent through `J_Har`; that categorical descent
is proved separately in `a_49`.

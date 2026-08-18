# 114.a.114 — H7: reduced cross-ruling intersection on the prime axes

```
+------------------------------------------------------------------------+
| CROSS       Q_(p,q)=A/E((p_1,q_2)) is the literal cross fiber product. |
| SAME PRIME  The fold makes F_p a canonical retract of Q_(p,p).         |
| OFF PRIME   No nonzero finite scalar bio has characteristics p and q.  |
| REDUCED     Contact retracts give <D_(p,1),D_(q,2)>_red=delta_pq log p. |
| LIMIT       Q_(p,q) may contain generalized excess; full degree open.  |
+------------------------------------------------------------------------+
```

## 1. The cross quotient

On an affine chart `A` of `Y^reg`, put

\[
 Q_{p,q}=A/E((i_1(p),i_2(q))).                                         \tag{1.1}
\]

By the quotient-pushout theorem of `a113`,

\[
 \mathrm{Spec}\,Q_{p,q}
 \simeq D_{p,1}\times_{Y^{\rm reg}}D_{q,2}.                            \tag{1.2}
\]

Unlike two primes on one ruling, the two relations in (1.1) belong to
different additions.  Bézout does not make this quotient zero.

## 2. The same-prime ordinary retract

Let `R=F(Z)`.  The fold `nabla:A->R` agrees with both ruling maps.  For
`q=p` it descends to

\[
 \bar\nabla_p:Q_{p,p}\longrightarrow R/E((p))=F(\mathbb F_p).          \tag{2.1}
\]

Each ruling map also descends modulo `p` to a section

\[
 s_{p,i}:F(\mathbb F_p)\longrightarrow Q_{p,p},
 \qquad \bar\nabla_p s_{p,i}=\mathrm{id}.                        \tag{2.2}
\]

### Proposition 2.1 (canonical same-prime contact retract)

The ordinary residue object `F(F_p)` is a split retract of the cross quotient
`Q_(p,p)`.  Therefore the cross fiber product contains a canonically selected
ordinary finite contact of mass

\[
 \log\#\mathbb F_p=\log p.                                             \tag{2.3}
\]

There are two canonical sections in (2.2); the retraction and its finite
target are independent of choosing one.  No claim is made that `Q_(p,p)` is
equal to `F(F_p)`: the homotopy fiber/excess can be nonzero.

## 3. Why off-prime cross quotients have no finite scalar bio

Haran's equations (10.3) and (10.21) say that a generalized ring under each
copy of `F(Z)` gives its unary scalars an ordinary commutative ring structure,
with the common multiplication and with the addition belonging to that
ruling.

Suppose a nonzero finite scalar bio receives `Q_(p,q)` with `p != q`.  Under
the first addition its finite additive group has characteristic `p`, hence
cardinality `p^a` for some `a>=1`.  Under the second it has characteristic
`q`, hence the same underlying finite set has cardinality `q^b` for some
`b>=1`.  Thus

\[
 p^a=q^b,                                                              \tag{3.1}
\]

contradicting unique factorization.

### Theorem 3.1 (finite-bio obstruction)

For distinct primes `p,q`, every finite scalar bio quotient of `Q_(p,q)` is
the zero object.  In particular a degree for (1.2) cannot be defined as the
logarithmic cardinality of a nonzero finite unary coordinate object.

This does not prove `Q_(p,q)=0`: a nonzero quotient may be intrinsically
infinite or visible only in higher arities.  It rules out precisely the naive
finite-cardinality degree.

## 4. The reduced cross-intersection pairing

The canonical contact projectors of `a69`, retained after reflection, attach
to `D_(p,i)` the ordinary module `F_p[1]`.  Tensoring the selected contacts
gives

\[
 \mathbb F_p\otimes_{\mathbb Z}\mathbb F_q
 \simeq
 \begin{cases}
   \mathbb F_p,&p=q,\\
   0,&p\ne q.
 \end{cases}                                                          \tag{4.1}
\]

For the all-prime axis lattices

\[
 \mathfrak D_1=\bigoplus_p\mathbb ZD_{p,1},\qquad
 \mathfrak D_2=\bigoplus_p\mathbb ZD_{p,2},                            \tag{4.2}
\]

define

\[
 I_{12}^{\rm red}\left(\sum_pm_pD_{p,1},\sum_qn_qD_{q,2}\right)
 =\sum_p m_pn_p\log p.                                                 \tag{4.3}
\]

### Theorem 4.1

Equation (4.3) is a well-defined symmetric-under-ruling-exchange bilinear
pairing.  Every coefficient is the Euler mass of the canonical reduced
contact (4.1); for `p=q` it agrees with the actual split ordinary retract
(2.1), and for `p!=q` the reduced contact is zero.

Thus the entire opposite-ruling **reduced** prime block is constructed:

\[
 I_{12}^{\rm red}(D_{p,1},D_{q,2})=\delta_{p,q}\log p.                  \tag{4.4}
\]

## 5. Full versus reduced intersection

The pairing (4.3) intentionally forgets the complementary generalized
excess, just as `a69` projects the diagonal cotangent object onto its
canonical `F_p[1]` summand.  A full intersection theory must additionally:

1. define a degree/Euler characteristic for the excess of every `Q_(p,q)`;
2. prove that this excess is zero or account for it in the product formula;
3. define `Delta^2` and same-divisor self-intersections;
4. add the archimedean Green contribution and prove principal invariance.

Accordingly H7-REG-MIXDEG is closed for the reduced prime-contact quotient,
but H7-REG-INTER, Riemann--Roch, the gauge, row A and RH remain open.

## 6. Verification scope

`114_a_114_h7_reduced_cross_intersection_verify.py` checks the split fold
identities in the quotient presentation, the finite-cardinality obstruction,
the residue tensor law and bilinearity of (4.3).  It does not assert absence
of generalized excess.

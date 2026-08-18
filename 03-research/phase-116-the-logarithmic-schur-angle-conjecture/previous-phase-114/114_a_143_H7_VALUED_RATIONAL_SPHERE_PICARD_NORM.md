# 114.a.143 — H7: the valued rational-sphere boundary detects every prime class

~~~
+------------------------------------------------------------------------+
| PROBLEM     The reduced sphere K forgets radial size.                    |
| REPAIR      Retain the Euclidean valuation as a metric on K-torsors.     |
| FRAMES      Metric coboundaries use isometric frames, hence norm one.    |
| PRIME       The transition q_a=prod p^{a_p} has norm q_a.               |
| INJECTIVE   Norm one forces q_a=1, hence a_p=0 for every p.              |
| RESULT      The metrized prime Picard lattice survives the mixed edge    |
|             and supportwise reflection.                                 |
+------------------------------------------------------------------------+
~~~

## 1. Do not discard the valuation when taking the residue

Let

\[
 B_\infty=\mathbb Q\cap\mathbb Z_{\mathbb R},
 \qquad K=\kappa_\infty=B_\infty/\mathfrak m_\infty .              \tag{1.1}
\]

The reduced object (K) remembers rational unit-sphere operations but
forgets their radial size.  The quotient nevertheless comes from the
canonical Euclidean valuation on (B_\infty).  We retain that valuation as
a metric datum at the mixed boundary.

For a rank-one (GL_1)-torsor (L) after rational-sphere base change, a
metric is a positive norm on its local frames satisfying

\[
 \|u e\|=|u|_\infty\|e\|                                             \tag{1.2}
\]

for lifted unary scalars.  Morphisms of metrized torsors are isometries.
This is the rank-one Arakelov category

\[
 \mathrm{Pic}^{\rm met}_{\rm tor}(B_i^{\rm locreg}).          \tag{1.3}
\]

It is not a retraction (K\to S): higher rational-sphere operations remain
present.  It only retains the valuation that existed before reduction.

## 2. The boundary norm homomorphism

On the two-chart cover of a138, the prime word

\[
 q_a=\prod_{p\in T}p^{a_p}>0                                       \tag{2.1}
\]

is the overlap transition of (L_a).  Give its pullback the metric induced
from (B_\infty).  Define

\[
 \nu_\infty(L_a)=\log|q_a|_\infty
 =\sum_{p\in T}a_p\log p.                                           \tag{2.2}
\]

Changing local frames by isometries (g_U,g_V) multiplies the transition
by (g_U^{-1}g_V).  By definition of an isometry,

\[
 |g_U|_\infty=|g_V|_\infty=1,                                      \tag{2.3}
\]

so (2.2) is unchanged.  Tensor product adds logarithmic norms and duality
negates them.  Thus (2.2) is a homomorphism on the metrized prime Picard
subgroup, derived from the real valuation rather than from the numerical
Green biextension.

### Theorem 2.1 (metrized boundary faithfulness)

The pullback of the prime lattice to either valued mixed boundary is
faithful in \(\mathrm{Pic}^{\rm met}_{\rm tor}\).

### Proof

If (L_a) becomes metrically trivial, it has an isometric Cech
trivialization.  Equations (2.2)--(2.3) give

\[
 0=\nu_\infty(L_a)=\log q_a,
\]

hence (q_a=1).  Unique factorization in (mathbb Q_{>0}^{\times}) then
gives (a_p=0) for every (p\in T).  QED.

Notice that a higher-arity sphere operation can participate in an
unmetrized trivialization without contradicting this proof.  It cannot
participate in an *isometric* trivialization with nonzero radial defect.
This is why the no-retraction theorem a136 and Theorem 2.1 are compatible.

## 3. Compatibility with the supportwise reflection

The relative reflection of a132 is an inverse-image construction on each
cofinal ((T,N))-tail.  Equip every inverse image with the pulled-back norm.
Pullback carries isometries to isometries and preserves (1.2).  Therefore a
metric trivialization after reflection would already have zero value under
the pulled-back homomorphism (2.2), and the same unique-factorization proof
applies.

Consequently the supportwise reflection does not create a kernel on the
metrized prime lattice.

## 4. Consequences and exact scope

Theorem 2.1 constructs the **Picard norm** alternative left open in a136.
It proves the metrized form of H7-MIXED-BDRY-PIC and hence the
anti-diagonal faithfulness needed for the Arakelov divisor/intersection
theory of row A.  It does not prove the stronger unmetrized equality

\[
 Q_T\cap G_UG_V^{-1}=\{1\}                                         \tag{4.1}
\]

from a138; H7-RSPH-UNIT remains open as a statement about bare torsors.
That stronger statement is no longer necessary for the metrized row-A
construction.

Because the injectivity proof uses the pre-existing Euclidean valuation,
not (B_{RR}), (C_\Lambda), or (G_{\rm num}), descending the determinant
biextensions of a141--a142 along this metrized lattice is not circular.

The remaining task is to assemble the metrized divisor group, the two
determinant factors and the contact-framed kernels into one a1--a5 object
and audit a4-strong.  Row A and RH are not yet claimed here.

## 5. Verification

`114_a_143_h7_valued_boundary_norm_verify.py` checks exact prime-word
injectivity, tensor/dual laws, invariance under norm-one frame changes and
the non-circular scope markers.

# 114.a.144 — Row A: the metrized bivariant arithmetic square

~~~
+------------------------------------------------------------------------+
| BASE        Haran's literal pro-square, repaired supportwise: Y^locreg. |
| BOUNDARY    Keep the canonical real valuation on the rational residue.  |
| DIVISORS    Metrized Cartier torsors plus principal metrized divisors.   |
| KERNELS     Contact-framed Gamma_n compose faithfully.                  |
| RR          Normalized section determinants give the RR Deligne line.   |
| CONTACT     Torsion determinants give exactly Lambda(n).                |
| GREEN       The quotient RR/contact gives the canonical Green gauge.    |
| RESULT      One metrized bivariant object satisfies a1--a5.             |
+------------------------------------------------------------------------+
~~~

## 1. The single object

Let (Y^{\rm locreg}) be the supportwise regular pro-square of a132.  On its
two mixed real boundaries retain, in addition to the rational-sphere
residue, the Euclidean valuation metric of a143.  Denote the resulting
valued pro-object by

\[
 \mathscr Y_A=(Y^{\rm locreg},B_{1,\infty}^{\rm val},
               B_{2,\infty}^{\rm val}).                             \tag{1.1}
\]

This does not replace Haran's square by a formal rank-two lattice.  Its
finite charts, real charts, overlaps, Cartier acts, cotangent contacts and
supportwise reflections are those already constructed on (Y^{\rm locreg}).
The extra datum is precisely the archimedean metric needed in an Arakelov
divisor theory.

For each prime (p) and ruling (i=1,2), let (V_{p,i}) be the repaired
Cartier prime with its valued boundary metric.  Put

\[
 \mathfrak D_{\rm pr}=\bigoplus_p
   (\mathbb Ze_{p,1}\oplus\mathbb Ze_{p,2}),
 \qquad e_{p,i}\longmapsto[V_{p,i}].                                \tag{1.2}
\]

The finite-support lattices exist by a111--a112 and a132.  The exact kernel
formula a112/a129 confines every possible relation to the prime
anti-diagonal.  Its restriction to either mixed boundary is the curve prime
lattice of a130, and the valued Picard norm of a143 is injective there.
Hence the anti-kernel is zero and (1.2) is injective in the metrized Picard
group.

Define

\[
 \begin{split}
 \operatorname{Prin}_A&=\operatorname{im}
   \bigl(GL_1(\mathcal K)\to D_1^{\rm met}(\mathscr Y_A)\bigr),\\
 \operatorname{Div}_A&=\operatorname{Prin}_A+\mathfrak D_{\rm pr},\\
 \operatorname{Pic}_A&=\operatorname{Div}_A/\operatorname{Prin}_A
   \simeq\mathfrak D_{\rm pr}.                                    \tag{1.3}
\end{split}
\]

The metric on a principal divisor is the canonical one induced by its
global fraction.  Thus (1.3), rather than a declared zero principal group,
is the actual divisor/principal quotient on the valued square.

## 2. Degrees, sections and products

For (x=(x_{p,i})\in\mathfrak D_{\rm pr}), define the two geometric degrees

\[
 d_i(x)=\sum_px_{p,i}\log p.                                       \tag{2.1}
\]

They are the logarithmic boundary norms, hence are intrinsic on
(\operatorname{Pic}_A).  Tensor product of metrized Cartier torsors adds
the two degrees.

Let \(H_X(tA)\) and \(H_X(tB)\) be the fixed-rank curve section objects on
the two arithmetic factors, and let \(S_t(x)\) be the calibrated cross image
of a120 (zero when one ruling degree is zero). Define the single section
determinant object by

\[
 \det H_A(tx)=\det H_X(tA)\otimes\det H_X(tB)
               \otimes\det_{\rm tor}S_t(x).                         \tag{2.2}
\]

The first two factors have the established curve-like
\(\Theta(\deg D)\) growth of a3. For a positive divisor with both degrees
nonzero, a120 constructs the third factor from genuine bounded
pro-sections. With the normalized determinant construction of a142,

\[
 h_A(t x)
 ={t^2d_1(x)d_2(x)\over2\log3}+O(t).                               \tag{2.3}
\]

The source sections multiply before evaluation.  Products are reevaluated
in the canonical fresh target belonging to the output degree, as in
a118--a120; no nonexistent transition between different finite
characteristics is used.  Thus the product is the actual product of
bounded source operations, while (2.2) is its determinant dimension.

## 3. The bivariant pairing and the dynamic kernels

The symmetric RR pairing is

\[
 B_{RR}(x,y)=
 {d_1(x)d_2(y)+d_2(x)d_1(y)\over2\log3}.                            \tag{3.1}
\]

By a142 it is the logarithmic norm of the Deligne second difference of the
normalized section determinant line.  The local diagonal contact is

\[
 C_\Lambda(x,y)=\sum_p
 (x_{p,1}y_{p,2}+x_{p,2}y_{p,1})\log p.                             \tag{3.2}
\]

By a140--a141 this is the torsion determinant of the canonical reduced
cotangent contacts, on the same Cartier torsors and not on a separate
numerical model.  Define

\[
 G_A=B_{RR}-C_\Lambda,
 \qquad q_A(x)={1\over2}G_A(x,x).                                   \tag{3.3}
\]

The determinant isometry is

\[
 \delta\lambda_{RR}\simeq\lambda_C\otimes\lambda_G.               \tag{3.4}
\]

It supplies the canonical Green line and gauge on \(\operatorname{Pic}_A\).

For every (n\ge1), take the contact-framed kernel of a140,

\[
 \Gamma_n=(T_n,M_n,\{H_1(C_p)\leftrightarrows\mathbb F_p\}_{p\mid n}).
                                                                         \tag{3.5}
\]

These are bivariant objects over the same (mathscr Y_A); their torsor
labels are the classes (1.2), their reduced diagonal pullbacks are the
contact complexes used in (3.2), and their RR line is the restriction of
(3.4).  Therefore

\[
 \Gamma_m\circ\Gamma_n\simeq\Gamma_{mn},
 \qquad \deg_C(\Gamma_n,\Delta)=\Lambda(n).                         \tag{3.6}
\]

Faithfulness comes from the torsor provenance (T_n), while mixed-prime
zero and prime-power mass come from the geometric contact retracts.  No
ordinary undecorated Chow representative is assumed.

## 4. Verification of the authoritative a1--a5 contract

### Theorem 4.1

The metrized bivariant object

\[
 \mathscr A=(\mathscr Y_A,\operatorname{Div}_A,
 \operatorname{Prin}_A,h_A,\delta\lambda_{RR},
 \lambda_C,\lambda_G,\{\Gamma_n\})                                 \tag{4.1}
\]

satisfies the five requirements of row A.

### Proof

1. **a1 (Div/Prin).** Equations (1.2)--(1.3) give an actual metrized
   Cartier divisor group, actual global principal subgroup and faithful
   all-prime quotient on the repaired Haran square.
2. **a2 (principal invariance).** All three determinant lines live on
   \(\operatorname{Pic}_A\).  Changing a representative by the divisor of a
   global fraction gives the canonical isometric principal
   trivialization, so (3.1)--(3.4) are unchanged.
3. **a3 (curve dimension).** On either axis the cross factor in (2.2) is
   zero, so the same section determinant is the fixed-rank curve theory and
   has \(\Theta(\deg D)\) growth.
4. **a4 (quadratic product).** Tensor product is the geometric product of
   Cartier torsors and bounded source sections; (2.3) proves quadratic
   determinant growth on every positive two-ruling ray.
5. **a5 (graded pairing).** The Deligne determinant pairing (3.1) is
   biexact and symmetric; (3.2)--(3.4) identify its geometric contact and
   Green factors.  Equation (3.6) recovers the required von Mangoldt
   diagonal mass inside that same bivariant theory.

Every item is therefore carried by the single object (4.1). QED.

## 5. Status and limits

This is **a4-strong in the metrized bivariant sense required by the row-A
contract**.  The stronger bare-torsor unit normal form H7-RSPH-UNIT remains
an interesting statement about the unmetrized rational-sphere coproduct,
but it is not required after the canonical valuation metric is retained.
Likewise an ordinary undecorated Chow-cycle model would be an optional
strengthening.

The construction does not prove RH by itself.  It closes row A only; rows
B, C and D and the RH-equivalent effectivity/positivity comparison must
still be assembled and audited.  No RH statement is used in Theorem 4.1.

## 6. Verification

`114_a_144_a4_strong_metrized_square_verify.py` checks the divisor-degree
laws, principal-quotient model, quadratic polarization, contact/Green/RR
splitting, von Mangoldt masses, a1--a5 markers and all named dependency
files.  It is a regression verifier for the stated algebra; the geometric
existence proofs are the cited documents.

The complete 143-component row-A suite through this verifier passed on
2026-08-05 in 566.97 seconds.

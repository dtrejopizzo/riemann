# 114.a.138 — H7: rational-sphere conservativity is an exact Cech unit intersection

~~~
+------------------------------------------------------------------------+
| COVER       X_N is glued from Z and A_N along Z[1/N].                   |
| PRIME CLASS A finite vector a has overlap transition q_a=prod p^a_p.    |
| BASE CHANGE Tensor all three charts with kappa_infty over S.             |
| TRIVIALITY  The pulled class dies iff q_a=g_U g_V^{-1} on the overlap.  |
| EXACT GATE  Q_T intersect (G_U G_V^{-1}) must be {1}.                   |
| BASELINE    Before rational-sphere base change both endpoint unit groups |
|             are {+-1}, so the intersection is indeed trivial.           |
+------------------------------------------------------------------------+
~~~

## 1. The two-chart presentation

Fix a finite prime support \(T\), put \(n_T=\prod_{p\in T}p\), and choose a
square-free level \(N\) divisible by \(n_T\). Haran (9.4) presents

\[
 X_N=\operatorname{Spec}\mathbb Z
 \coprod_{\operatorname{Spec}\mathbb Z[1/N]}
 \operatorname{Spec}A_N,\qquad
 A_N=\mathbb Z[1/N]\cap\mathbb Z_{\mathbb R}.                         \tag{1.1}
\]

Write \(U,V,W=U\cap V\) for these finite, real and overlap charts. For
\(a=(a_p)_{p\in T}\), set

\[
 q_a=\prod_{p\in T}p^{a_p}\in\mathbb Z[1/N]^\times.                   \tag{1.2}
\]

Up to the fixed inverse-uniformizer orientation, the prime bundle
\(L_a=\bigotimes_pL_p^{a_p}\) is represented on this cover by the overlap
transition \(q_a\). Replacing every \(a_p\) by \(-a_p\) only reverses the
orientation and does not change the kernel criterion.

## 2. Rational-sphere base change

Let \(S=\mathbb F\{\pm1\}\), \(K=\kappa_\infty\), and define

\[
\begin{aligned}
 R_U&=\mathbb Z\otimes_S K,\\
 R_V&=A_N\otimes_S K,\\
 R_W&=\mathbb Z[1/N]\otimes_S K,
\end{aligned}                                                        \tag{2.1}
\]

with unit groups \(G_U=GL_1(R_U)\), \(G_V=GL_1(R_V)\), and
\(G_W=GL_1(R_W)\). Both endpoint groups map to \(G_W\).

For a two-chart torsor, changing the local frames by \(g_U\in G_U\) and
\(g_V\in G_V\) changes the transition by \(g_U^{-1}g_V\). Therefore:

### Theorem 2.1 (Cech unit criterion)

\[
 L_a|_{X_N\times_Sx_\infty}\simeq1
 \quad\Longleftrightarrow\quad
 q_a\in G_U\,G_V^{-1}\subseteq G_W.                                  \tag{2.2}
\]

Consequently rational-sphere base change is faithful on the \(T\)-prime
lattice if and only if

\[
 Q_T\cap G_U G_V^{-1}=\{1\},\qquad
 Q_T=\langle p:p\in T\rangle\subseteq G_W.                            \tag{2.3}
\]

Here the product denotes the image of pairs of endpoint units; no claim
that it is a subgroup in a noncommutative higher-rank setting is needed.
For \(GL_1\) in the commutative prime sector it is a subgroup.

## 3. Baseline before base change

On unary scalars,

\[
 GL_1(\mathbb Z)=\{\pm1\},\qquad GL_1(A_N)=\{\pm1\}.                  \tag{3.1}
\]

Indeed, if \(x,x^{-1}\in A_N\), the real-ball conditions give
\(|x|\le1\) and \(|x^{-1}|\le1\), hence \(|x|=1\). Thus the unextended
intersection in (2.3) is trivial by unique factorization.

The difficulty is now exact: tensoring with \(K\) may create unary units
from higher-arity rational-sphere operations. The no-retraction theorem
a136 neither creates nor excludes such units.

## 4. Supportwise reflection

On the cofinal \((T,N)\) tail of a132, every \(p\in T\) is already a unit on
the finite/real overlap, so imposing or forgetting \(p\)-regularity there is
automatic. To deduce H7-RSPH-CONS for \(B_i^{locreg}\), it is enough to prove
both:

1. the unit intersection (2.3) after rational-sphere base change;
2. supportwise reflection does not enlarge the endpoint coboundary image
   inside \(G_W\).

Call their conjunction **H7-RSPH-UNIT**. It is equivalent to the required
prime-lattice faithfulness for this Cech presentation, rather than merely a
sufficient numerical detector.

## 5. Status

The mixed-boundary problem is reduced to an explicit \(GL_1\) calculation.
No unit normal-form theorem for the tensor products (2.1) is present in the
audited source, so (2.3) is not asserted. H7-RSPH-UNIT, H7-ARCH-BDRY, row A
and RH remain open.

The verifier 114_a_138_h7_cech_unit_criterion_verify.py checks the ordinary
endpoint units, unique-factorization intersection, Cech coboundary algebra
and source anchors.

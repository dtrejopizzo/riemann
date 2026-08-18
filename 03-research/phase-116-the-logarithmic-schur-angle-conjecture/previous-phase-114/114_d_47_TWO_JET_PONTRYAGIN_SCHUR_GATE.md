# D.47 — Two-jet Pontryagin index and Schur-complement gate

## 1. Purpose

D.32--D.45 identify the primitive sign with

\[
 B_{\rm nuc}(F,F)\leq 0,
 \qquad
 M_TF=(M_-(F),M_+(F))=0.                              \tag{1.1}
\]

This note replaces the search for a pointwise positive kernel by a sharper
finite-index target.  The two ruling jets form a **hyperbolic** plane, not a
positive plane: their matrix is

\[
 C=\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad \operatorname{In}(C)=(1,1,0).                        \tag{1.2}
\]

Accordingly, on every compact support window row D has the classical Hodge
target: one positive direction, a two-dimensional hyperbolic boundary
quotient, and a negative primitive complement.

The sign is fixed by the exact polar/local decomposition (spelled out in
D.49):

\[
 QW_T=M_T^*CM_T-B_{{\rm nuc},T}.                             \tag{1.3}
\]

Thus `QW_T>=0` implies
`B_(nuc,T)<=M_T^*CM_T`.  Since `C` has only one positive direction,
`B_(nuc,T)` has positive index at most one; on `ker M_T` the same identity
becomes `B_(nuc,T)=-QW_T<=0`.  This is the Hodge-index-one, rather than
index-two, geometry of the two jets.

No zero of zeta is used in the reduction.

## 2. The constrained inertia identity

Let `H` be a finite-dimensional Hilbert space, let `A=A*` be invertible, and
let

\[
 M:H\longrightarrow\mathbb C^r                              \tag{2.1}
\]

be surjective.  Put `K=ker M` and suppose that

\[
 G:=MA^{-1}M^*                                               \tag{2.2}
\]

is invertible.

> **Theorem 2.1 (constrained Haynsworth identity).**
> The restriction of the hermitian form of `A` to `K` satisfies
> \[
> \operatorname{In}(A|_K)
>   =\operatorname{In}(A)-\operatorname{In}(G),              \tag{2.3}
> \]
> where inertia is the triple `(n_+,n_-,n_0)` and subtraction is
> componentwise (the zero components are zero under the hypotheses).

**Proof.** Define

\[
 R=A^{-1}M^*G^{-1}:\mathbb C^r\longrightarrow H.             \tag{2.4}
\]

Then `MR=I`, so `H=K direct-sum R(C^r)`.  For `k in K` and `c in C^r`,

\[
 \langle k,ARc\rangle
 =\langle Mk,G^{-1}c\rangle=0,                              \tag{2.5}
\]

whereas

\[
 R^*AR=G^{-1}.                                                \tag{2.6}
\]

Thus the form of `A` is congruent to the orthogonal direct sum of `A|_K`
and `G^{-1}`.  Sylvester inertia and
`In(G^{-1})=In(G)` give (2.3).  QED.

For `r=2` this has the following exact consequence.

> **Corollary 2.2 (hyperbolic two-jet Hodge certificate).** If
> \[
> \operatorname{In}(A)=(1,\dim H-1,0),
> \qquad \operatorname{In}(G)=(1,1,0),                       \tag{2.7}
> \]
> then
> \[
> \langle k,Ak\rangle<0\qquad(0\ne k\in\ker M).             \tag{2.8}
> \]
> Conversely, (2.8) forces `n_+(A)<=2`.  To obtain the Hodge value
> `n_+(A)=1`, one must additionally identify the boundary quotient with the
> hyperbolic ruling plane and exclude a second positive direction.

The last assertion follows because any positive subspace of dimension at
least three intersects the codimension-two space `ker M` nontrivially.
The codimension argument alone does not distinguish positive index one from
positive index two.  That distinction is supplied by the hyperbolic ruling
comparison, not by the mere existence of two scalar constraints.

## 3. Application to a compact support window

Fix `T>0`.  Let `q_T` be the closed upper-bounded form obtained by restricting
the exact expression of D.10 to functions supported in `[-T,T]`.  Its Gamma
part has symbol

\[
 m_\infty(\tau)=-\log(1+|\tau|)+O(1),                         \tag{3.1}
\]

and the finitely many prime-power translations with `log n<=2T` are bounded.
Consequently the self-adjoint form operator `A_T` has compact resolvent from
above and only finitely many positive eigenvalues.  The boundary map is

\[
 M_TF=
 \left(\int_{-T}^T e^{-t/2}F(t)\,dt,
       \int_{-T}^T e^{ t/2}F(t)\,dt\right).                   \tag{3.2}
\]

It is surjective.  On a Galerkin space avoiding the discrete exceptional
parameters at which `A_T` or (2.2) is singular, define

\[
 G_T=M_TA_T^{-1}M_T^*.                                       \tag{3.3}
\]

Theorem 2.1 gives the exact finite-dimensional certificate

\[
 \boxed{
 q_T|_{\ker M_T}<0
 \quad\Longleftarrow\quad
 \operatorname{In}(A_T)=(1,\infty,0),\quad
 \operatorname{In}(G_T)=(1,1,0).}                            \tag{3.4}
\]

Here `(1,infinity,0)` denotes one positive direction, no kernel and a
negative complement in the compact-resolvent form sense.  Conversely,
strict negativity on the primitive subspace together with the hyperbolic
boundary identification gives the reverse implication.  Passing
through a singular parameter is controlled by the Moore--Penrose version of
(2.3): one must additionally verify

\[
 M_T^*(\mathbb C^2)\subseteq\operatorname{Ran}A_T
 \quad\text{and}\quad
 \ker A_T\cap\ker M_T=0.                                    \tag{3.5}
\]

The second condition is exactly the equality gate already isolated in D.24
and D.44.

The infinite-dimensional statement follows by the min--max principle and
Galerkin exhaustion, provided the following estimates are uniform:

1. `n_+(A_T)=1`;
2. `G_T` stays nondegenerate with signature `(1,1)` away from the singular
   alternatives (3.5);
3. no primitive zero mode appears in the exhaustion.

These are source-side assertions about the explicit nonlocal operator; no
spectral zero is part of their definition.

## 4. Why the index bound is the substantive theorem

The two moment constraints alone do not imply (1.1).  They imply only the
dimension estimate

\[
 q_T|_{\ker M_T}<0\quad\Longrightarrow\quad n_+(A_T)\le2.     \tag{4.1}
\]

Thus a proposed proof must furnish a genuine oscillation, variation, or
Morse-index theorem showing that the prime--Gamma operator has exactly one
positive direction.  Declaring the two-jet plane positive would be a sign
error: its ruling matrix is hyperbolic.  The absence of a second positive
direction must be proved independently.

The result also sharpens the first-crossing formulation.  A failure of row D
does not merely mean that a scalar determinant vanishes.  It means that one
of the following typed events occurs:

\[
 \begin{array}{ll}
 \text{(i)} & n_+(A_T)\text{ reaches }2,\\
 \text{(ii)}& G_T\text{ loses signature }(1,1)\text{ or becomes singular},\\
 \text{(iii)}& \ker A_T\cap\ker M_T\ne0.
 \end{array}                                                  \tag{4.2}
\]

The three alternatives can be tested separately.  Alternative (iii) is
already excluded once the Hodge sign is known; excluding (i) is the new
global index theorem, while (ii) is a two-by-two boundary calculation.

## 5. Relation with a Pontryagin polarization

If `n_+(A_T)=1`, the completion of the form domain is a Pontryagin space of
positive index one.  If additionally `G_T` has signature `(1,1)`, the
boundary map identifies its quotient with the hyperbolic Tate-ruling plane,
and `ker M_T` is a negative Hilbert subspace.  The induced fundamental
symmetry then supplies the finite-window Weil operator required by D.37.

Conversely, a faithful positive row-D polarization makes the central action
unitary and forces (3.4).  Hence the Pontryagin construction does not weaken
the target; it gives a geometrically typed way to prove it:

\[
 \boxed{
 \text{row-D Hodge certificate on every window}
 \Longleftrightarrow
 \text{positive index one with hyperbolic two-ruling boundary}.}    \tag{5.1}
\]

The implication from right to left is Theorem 2.1.  The reverse implication
uses the two independent ruling directions and min--max.

## 6. Surviving construction route

The remaining route is no longer an unspecified search for a square root of
`Delta_H`.  It is the following concrete program.

1. Construct the resolvent of `A_T` relative to the Gamma operator.
2. Prove a nonlocal oscillation theorem fixing its positive Morse index at
   one under the support cutoff.
3. Compute the two-by-two Green matrix (3.3) from the Poisson boundary maps
   and prove that it has signature `(1,1)`.
4. Pass through the support exhaustion using (3.5).

If these four statements are proved from the A--B--C source data, (3.4)
gives the primitive inequality and D.24 gives strict equality.  No appeal to
the zero divisor or to an assumed positive spectral sector is needed.

What is proved in this note is the exact Schur/inertia mechanism and the
separation of the infinite-dimensional sign into a Morse-index theorem plus
a two-dimensional boundary calculation.  The missing assertion is the
uniform index bound in step 2; it is not asserted here.

## 7. Exact finite certificate

The companion script
`114_d_47_schur_inertia_verify.py` checks (2.3)--(2.6) over the rationals in
two independent five-dimensional examples.  The first has an indefinite
boundary Green matrix and verifies the full inertia subtraction; the second
has Hodge index one and a hyperbolic Green matrix, and verifies that the
three-dimensional primitive kernel is negative definite.  The script is a certificate of the
linear-algebra identity, not evidence for the unresolved uniform index bound.

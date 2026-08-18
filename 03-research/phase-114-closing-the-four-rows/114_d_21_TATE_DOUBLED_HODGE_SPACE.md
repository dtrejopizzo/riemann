# Row (d): the Tate-doubled mixed Hodge space

## Status

This note upgrades the one-boundary Szego theorem to a self-dual
two-ruling space.  It constructs, for every finite prime-power cut, a
canonical real mixed space with two degrees, a Tate involution, one positive
direction, and a strict primitive Hodge inequality.  The construction is
independent of the nuclear Weil form.  Comparison with the completed test
module remains the outstanding step.

## 1. Two orientations

Use the notation of
`114_d_20_LORENTZIAN_SZEGŐ_TOWER_THEOREM.md`.  For a finite set `S` of
prime powers take two copies

\[
 E_S^+,\qquad E_S^-                                      \tag{1}
\]

with torsor-orthonormal bases, degree maps `d_+`, `d_-`, and tail maps
`R_+`, `R_-` obtained from the normalized Szego vectors.  Put

\[
 N_S=E_S^+\oplus E_S^- .                                \tag{2}
\]

The Tate involution is

\[
 \mathscr J(v_+,v_-)=(v_-,v_+).                         \tag{3}
\]

Define the symmetric form

\[
 \begin{split}
 Q_S((v_+,v_-),(w_+,w_-))={}&
 d_+(v_+)d_-(w_-)+d_-(v_-)d_+(w_+)\\
 &+\langle R_+v_+,R_+w_+\rangle
  +\langle R_-v_-,R_-w_-\rangle\\
 &-\langle v_+,w_+\rangle-\langle v_-,w_-\rangle .
 \end{split}                                            \tag{4}
\]

The first line is the hyperbolic ruling intersection.  The second is the
archimedean oscillator tail, and the third is the graded torsor metric.
Every term is constructed before comparison with row (c).

## 2. Hodge theorem

### Theorem 2.1

For every finite `S` with at least two labels, the form (4) has signature
`(1,2|S|-1)`.  If

\[
 d_+(v_+)=d_-(v_-)=0,                                  \tag{5}
\]

then

\[
 Q_S(v,v)\le-c_0(\|v_+\|^2+\|v_-\|^2),
 \qquad
 c_0=1-\frac{1627}{2640}=\frac{1013}{2640}>0.          \tag{6}
\]

In particular equality on the two-ruling primitive subspace occurs only at
zero.

### Proof

Lemma 2.1 of the preceding note gives

\[
 \|R_\pm\|^2\le\frac{1627}{2640}.
\]

Under (5), the hyperbolic term vanishes, so (6) follows immediately.

For the full inertia use the orthogonal decomposition under the Tate
involution into symmetric vectors `(u,u)` and antisymmetric vectors
`(u,-u)`.  If `C=aa^t+R^*R` is the Szego Gram matrix, the symmetric block
of (4), up to the harmless factor two, is

\[
 C-I,
\]

which has signature `(1,|S|-1)` by Theorem 3.1 of the preceding note.  The
antisymmetric block is

\[
 R^*R-I-aa^t.
\]

It is strictly negative because `||R||<1`.  The two blocks are orthogonal,
so their signatures add and give `(1,2|S|-1)`.

For a singleton cut the symmetric block is zero and the antisymmetric block
is negative.  This harmless degenerate initial object disappears as soon as
a second mixed label is present; the theorem deliberately starts at that
stage.

## 3. Effectivity and functoriality

Define the finite effective cone by nonnegative coordinates in both torsor
bases.  Every nonzero effective vector has at least one positive degree.
Finite-support inclusions preserve the cone, both degrees, the involution
and the form.  Consequently (2)--(4) define a cofinal mixed numerical space
with a uniform primitive gap.

The construction also has a natural effective **linear** realization: send
a positive coordinate vector to the corresponding positive linear
combination of its normalized Szego sections in the two oriented Hardy
modules.  This statement does not supply a multiplication law: products of
Szego kernels do not remain in the displayed finite span.  A projective
tensor envelope is a candidate for such a law, but its descent and a surface
Riemann--Roch asymptotic have not been proved.  The Hodge inequality here
comes directly from the contraction theorem, not from an RR argument.

## 4. Comparison gate

The two degrees in (4) have the correct formal role of
`hat f(1)` and `hat f(0)`.  To close row (d), one must construct a continuous
Tate-equivariant map

\[
 \mathcal J_{\rm Tate}:\mathcal T\longrightarrow
       \widehat{\varinjlim_S N_S}                     \tag{7}
\]

such that

\[
 (d_+,d_-)\mathcal J_{\rm Tate}f
   =(\widehat f(1),\widehat f(0))                     \tag{8}
\]

and, independently of Theorem 2.1,

\[
 Q(\mathcal J_{\rm Tate}f,\mathcal J_{\rm Tate}g)
   =B_{\rm nuc}(f,g).                                 \tag{9}
\]

If (7)--(9) are proved with dense image, Theorem 2.1 gives row (d), its
equality case and RH immediately.  Defining `J_Tate` by a square root of
`B_nuc` is forbidden; it must be assembled from the Witt correspondences,
torsor grading, derived contacts and oscillator boundary vectors already
listed.

# D.197 — Periodic boundary graph test and the global Poisson gluing defect

## Verdict

The full periodic boundary modules found in D.196 are exactly the modules
already present in row A, but the image of a primitive test does **not** lie
in the graph of an isometry between them.  At every prime, the trace map

\[
 \mathcal B_p:F\longmapsto(b_{p,+},b_{p,-})in
 L^2(C_p)^+\oplus L^2(C_p)^-                              \tag{0.1}
\]

is surjective already on functions supported in two adjacent logarithmic
cells.  On the two-Tate primitive subspace its image is exactly the product
of two codimension-one hyperplanes, not a graph.

Consequently the residue form

\[
 q_{p,\partial}(g_+,g_-)
 =r_p\|g_+\|^2-r_p^{-1}\|g_-\|^2                         \tag{0.2}
\]

takes both signs on primitive source images.  Row A's Kunneth multiplication
and row B's reduced contact weight \(\log p\) preserve (0.1)--(0.2); they do
not impose a relation \(g_-=Ug_+\).

The additive Fourier--Poisson identity is a global equality after the full
zeta product and Gamma chart are assembled.  Isolating one prime leaves the
complementary Euler product, so it does not furnish a local periodic
isometry.  A global graph relation would be precisely the still-missing
prime--Gamma polarization, not a consequence of local Poisson summation.

This gives a source counterexample to the proposed local graph mechanism
without making any spectral assumption.  No paper file is modified.

## 1. Boundary trace on two adjacent cells

Fix \(p\), and put

\[
 a=\log p,qquad r=p^{-1/2},qquad C_p=\mathbb R/a\mathbb Z. \tag{1.1}
\]

In the Zak coordinates of D.196, take a test supported only in the cells
\(j=0,1\):

\[
 f_u(0)=f_0(u),\qquad f_u(1)=f_1(u),qquad0\le u<a.        \tag{1.2}
\]

The two tail functions are

\[
 \binom{b_+}{b_-}
 =\begin{pmatrix}1&r^{-1}\\1&r\end{pmatrix}
 \binom{f_0}{f_1}.                                        \tag{1.3}
\]

The determinant is \(r-r^{-1}\ne0\).  Hence for arbitrary
\((g_+,g_-)\in L^2(C_p)^2\), the unique preimage is

\[
 \begin{aligned}
 f_1&={g_+-g_-\over r^{-1}-r},\\
 f_0&={r^{-1}g_- -rg_+\over r^{-1}-r}.
 \end{aligned}                                             \tag{1.4}
\]

Thus

\[
 \boxed{\mathcal B_p\text{ is onto }L^2(C_p)^+\oplus L^2(C_p)^-.} \tag{1.5}
\]

No completion or limiting argument is involved.

## 2. Exact primitive image

D.196 identifies the two moments as

\[
 M_+(F)=\langle b_+,e^{u/2}\rangle,qquad
 M_-(F)=\langle b_-,e^{-u/2}\rangle.                      \tag{2.1}
\]

Define

\[
 \begin{aligned}
 H_{p,+}^0&=\{g\in L^2(C_p):
       \langle g,e^{u/2}\rangle=0\},\\
 H_{p,-}^0&=\{g\in L^2(C_p):
       \langle g,e^{-u/2}\rangle=0\}.
 \end{aligned}                                             \tag{2.2}
\]

Equations (1.4) and (2.1) prove

\[
 \boxed{
 \mathcal B_p(\ker M_+\cap\ker M_-)
 =H_{p,+}^0\oplus H_{p,-}^0.}                             \tag{2.3}
\]

In particular, choose \(g_+\ne0\) in \(H_{p,+}^0\), put \(g_-=0\), and
use (1.4).  The resulting compact two-cell test is primitive and has

\[
 q_{p,\partial}=r\|g_+\|^2>0.                             \tag{2.4}
\]

Interchanging the two charts gives a primitive test with

\[
 q_{p,\partial}=-r^{-1}\|g_-\|^2<0.                       \tag{2.5}
\]

Therefore no operator \(U_p:H_{p,+}^0\to H_{p,-}^0\) can have

\[
 \mathcal B_p(\mathcal P)=\{(g,U_pg):g\in H_{p,+}^0\},    \tag{2.6}
\]

whether \(U_p\) is isometric or not.  The image contains both coordinate
axes.

## 3. What an isometric graph would have proved

If, contrary to (2.3), the image satisfied \(g_-=U_pg_+\) with \(U_p\)
isometric, then

\[
 q_{p,\partial}(g_+,U_pg_+)
 =(r-r^{-1})\|g_+\|^2\le0.                               \tag{3.1}
\]

Thus the proposed graph mechanism would indeed have supplied the desired
local sign.  Equations (2.3)--(2.5) show exactly why it cannot be obtained
from the raw periodic trace: its hypothesis is false on the primitive
source.

Allowing a contraction \(\|U_p\|\le r\) changes the coefficient but not the
logic; the coordinate-axis vectors still rule out a graph.

## 4. Kunneth and reduced contact do not add a relation

Row A's periodic coefficient category constructs the two copies of
\(L^2(C_p)\), their effective multiplication, and Kunneth tensor products.
These operations send a pair \((g_+,g_-)\) to tensor/multiplication data;
they do not identify the two factors.

Row B's contact at \(p^k\) is the idempotent label \(e_p\) in the contact
GNS algebra.  Tensoring (0.1) with \(e_p\) multiplies (0.2) by

\[
 \tau_\Lambda(e_p)=\log p>0.                              \tag{4.1}
\]

It therefore preserves both the surjectivity (1.5) and the inertia in
(2.4)--(2.5).  The perfect complex remembers why different primes multiply
to zero and why all powers of the same prime have one mass; it supplies no
map between the \(+\) and \(-\) periodic tail functions.

Thus the A--B local data give the correct boundary **objects and weights**,
but not the desired graph subobject.

## 5. What the Fourier--Poisson relation actually glues

For \(\phi\in\mathcal H_\cap\), the additive Poisson identity is

\[
 Z\phi=JZ\mathcal F\phi.                                  \tag{5.1}
\]

This is an equality of the two **global** Poisson charts.  Formally isolating
one Euler factor gives

\[
 Z=A_pZ^{(p)},\qquad
 Z^{(p)}=\prod_{q\ne p}A_q,                                \tag{5.2}
\]

with the Gamma/Fourier conversion between the opposite charts.  Substitution
in (5.1) relates the \(p\)-chart only after applying \(Z^{(p)}\) and the
archimedean transform.  It does not imply

\[
 b_{p,-}=U_pb_{p,+}.                                      \tag{5.3}
\]

Indeed (5.3) contradicts the explicit source image (2.3).

Attempting to solve (5.1) for a local \(U_p\) requires inversion of the
complementary Poisson range.  In the faithful Fréchet topology this is only
defined on the closed range; in the critical Hilbert topology the range is
dense and nonclosed.  This is the range obstruction of D.74 and D.191 in
periodic-boundary form.

Hence Fourier--Poisson gluing may still impose a **global** relation among
all prime boundary modules and Gamma, but no placewise isometry follows.

## 6. The global boundary map

For a finite prime set \(P\), define

\[
 \mathcal B_PF=
 \bigoplus_{p\in P}\sqrt{\log p}
 \left(r_p^{1/2}b_{p,+}(F),,r_p^{-1/2}b_{p,-}(F)\right).  \tag{6.1}
\]

Its natural residue metric is the Krein form

\[
 [\mathcal B_PF,\mathcal B_PG]_P
 =\sum_{p\in P}\log p
 \left(r_p\langle b_{p,+}(F),b_{p,+}(G)\rangle
 -r_p^{-1}\langle b_{p,-}(F),b_{p,-}(G)\rangle\right).    \tag{6.2}
\]

Add the Gamma boundary feature \(D_\infty F\).  The row-C comparison says
that the stabilized relative combination of these features has character
\(B_{\rm nuc}\).  It does not assert that the image of \(\mathcal B_P\)
plus Gamma is a negative graph in (6.2).

A global graph theorem would require a source-defined operator

\[
 \mathcal U_{P,\infty}:
 \left(\bigoplus_pH_{p,+}^0\right)\oplus H_{\Gamma,+}
 \longrightarrow
 \left(\bigoplus_pH_{p,-}^0\right)\oplus H_{\Gamma,-}     \tag{6.3}
\]

whose graph contains every primitive boundary image and whose norm has the
sharp arithmetic normalization.  By D.190 and D.195, the contractivity of
such a map is equivalent to the remaining global shorted-capacity estimate.
Thus (6.3), not the false placewise relation (5.3), is the exact next datum.

## 7. Source counterexample and scope

The counterexample (1.4) is a compact logarithmic test satisfying the exact
two moments.  The Weil criterion must hold for all such primitive tests, so
no additional restriction to a preferred Poisson-source subspace can be
used unless one first proves that it is dense for the complete
\(B_{\rm nuc}\) form and that the graph relation extends continuously.
Neither local Kunneth nor the contact determinant supplies such a density
theorem.

This note rules out only a **local** periodic isometry.  It leaves the global
prime--Gamma graph (6.3) as the remaining possible source polarization.

## 8. Reproducible certificate

The companion script `114_d_197_periodic_boundary_graph_verify.py` checks:

1. pointwise inversion of the two-cell trace matrix;
2. exact two-moment primitivity for independently prescribed boundary
   functions;
3. positive and negative residue values on primitive source images;
4. failure of every graph relation by presence of both coordinate axes.

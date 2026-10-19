# R183.004 — Poisson--Möbius factorization of the semilocal scattering

> **WITHDRAWN by type audit (R183.012).** The domain note that
> follows is not enough: the article's co-Poisson map goes from an additive
> space to a multiplicative one and is not built there as a bounded
> automorphism of `L²(X_S)`. Hence (0.1), its blocks, and the norm
> comparisons are not proved as operator identities. This file is kept
> only as a formal kernel computation.

> **Domain note.** The identities with \(E_S\) and \(M_S\) are proved
> first on the locally finite algebraic core. Their closed extension
> and the block identities in the limit are part of the open typing
> problem; it is not claimed that the two factors are separately bounded
> operators.

## 0. Result

Möbius inversion was already built in R170.850 and its exterior loop in R170.878. By itself it has no sign. The additional datum of the semilocal framework is Poisson's intertwining. Combining them **before compressing** gives a Wiener--Hopf factorization of Tate's unitary:

\[
 \boxed{u_S=M_S^\vee E_S,\qquad M_S^\vee:=I M_S I.}       \tag{0.1}
\]

Here \(E_S\) is the co-Poisson comb of the integers of \(M_S\), \(M_S=E_S^{-1}\) is its Möbius inverse, and \(I\) inverts the scale. The formula places the comb and its inverse in opposite orientations. It is a joint Euler--Poisson identity that does not exist for a Beurling comb lacking a self-dual additive lattice.

The factorization allows computing the defect of a half-line compression. The result is a difference of two Hankel squares. Unitarity proves that both squares balance globally; the restricted sign requires proving that the support condition and the two Tate moments make the output square dominant. This is exactly R183.003's return theorem, now with explicit source factors.

## 1. Algebraic identity

We work first on the algebraic core of compactly supported functions, where every sum reaching a compact set is finite. Let

\[
 E_S=\sum_{m\in M_S}m^{-1/2}D_m,
 \qquad
 M_S=\sum_{m\in M_S}\mu(m)m^{-1/2}D_m.              \tag{1.1}
\]

Dirichlet convolution gives

\[
                  M_SE_S=E_SM_S=1.                 \tag{1.2}
\]

The semilocal Poisson formula is

\[
                  E_S{\cal F}_S=I E_S.              \tag{1.3}
\]

Multiplying (1.3) by \(M_S\) on the left produces

\[
                  {\cal F}_S=M_S I E_S.             \tag{1.4}
\]

The multiplicative scattering is \(u_S=I{\cal F}_S\). Hence

\[
 u_S=I M_S I E_S=M_S^\vee E_S,                     \tag{1.5}
\]

which proves (0.1). Neither the explicit formula nor the zeros are involved.

## 2. Triangular blocks

Let \(P\) be the projector of a scaling half-line and \(Q=1-P\). Choose the orientation so that \(E_S\) is causal. Then

\[
             PE_SQ=0,\qquad PM_SQ=0,                \tag{2.1}
\]

and, after reflecting,

\[
             QM_S^\vee P=0.                         \tag{2.2}
\]

With respect to \(P\oplus Q\), we write

\[
 E_S=\begin{pmatrix}e&0\\ g&k\end{pmatrix},
 \qquad
 M_S^\vee=\begin{pmatrix}\alpha&\beta\\0&\delta\end{pmatrix}.
                                                               \tag{2.3}
\]

Thus

\[
 u_S=M_S^\vee E_S
 =\begin{pmatrix}
   \alpha e+\beta g&\beta k\\
   \delta g&\delta k
  \end{pmatrix}.                                    \tag{2.4}
\]

The two relevant Hankel blocks are, hence,

\[
 b:=Qu_SP=\delta g,
 \qquad
 c:=Pu_SQ=\beta k.                                  \tag{2.5}
\]

This gives a source interpretation of the two diagonal terms of R183.002(3.2):

\[
 P(u_S^*Pu_S-P)P=-g^*\delta^*\delta g=-b^*b,        \tag{2.6}
\]

\[
 Q(u_S^*Pu_S-P)Q=k^*\beta^*\beta k=c^*c.           \tag{2.7}
\]

Identities (2.6)--(2.7) are squares, but with opposite signs. R183.002's transversal term is

\[
 P(u_S^*Pu_S-P)Q
 = (\alpha e+\beta g)^*\beta k.                    \tag{2.8}
\]

Hence separating the two triangular factors destroys the orientation. The sum must be eliminated as a single network.

## 3. Global conservation

Since \(u_S\) is unitary, (2.4) satisfies

\[
 (\alpha e+\beta g)^*(\alpha e+\beta g)+g^*\delta^*\delta g=1_P,
                                                               \tag{3.1}
\]

\[
 k^*\beta^*\beta k+k^*\delta^*\delta k=1_Q,        \tag{3.2}
\]

\[
 (\alpha e+\beta g)^*\beta k+g^*\delta^*\delta k=0.\tag{3.3}
\]

The last equality is the oriented Euler--Poisson cancellation. Substituting it into R183.002's form, for \(x=x_P+x_Q\), gives

\[
 \begin{aligned}
 \langle x,(u_S^*Pu_S-P)x\rangle
 ={}&-\|\delta g x_P\|^2+\|\beta kx_Q\|^2\\
    &-2\operatorname{Re}\langle\delta gx_P,\delta kx_Q\rangle.
                                                               \tag{3.4}
 \end{aligned}
\]

Equivalently,

\[
 \boxed{
 \langle x,(u_S^*Pu_S-P)x\rangle
 =\|\beta kx_Q\|^2+\|\delta kx_Q\|^2
  -\|\delta(gx_P+kx_Q)\|^2.}                       \tag{3.5}
\]

Using (3.2), also

\[
 \boxed{
 -\langle x,(u_S^*Pu_S-P)x\rangle
 =\|\delta E_Sx\|^2-\|x_Q\|^2.}                  \tag{3.6}
\]

This last formula coincides with R183.003's tail difference, but now \(Qu_Sx=\delta E_Sx\) comes directly from factorization (0.1).

## 4. Inserting the short support

Take \(S=S(q)\) and \(T=\tfrac12\log q\). For the rough comb

\[
 m\in M_S,\ m>1\Longrightarrow \log m\ge2T.        \tag{4.1}
\]

In the physical representation, \(M_h\) is the convolution operator
\(C_h\). The support hypothesis controls its **kernel**, not the support of
\(x=C_hf\):

\[
 K_{C_h}(y,y')=0\qquad\text{if }|y-y'|\geq T.       \tag{4.2}
\]

A nontrivial term \(D_mC_h\) of \((E_S-1)C_h\) has an oriented shift of
modulus at least \(2T-T=T\). Hence it has no block remaining strictly
within a cell of width \(T\). This is a statement about kernel propagation;
it does not authorize replacing \(C_hf\) by a vector supported in the
window.

In finite truncations, the arithmetic elimination of the oriented paths
is given exactly by

\[
 M_S=\sum_{m\in M_S}{\mu(m)\over\sqrt m}D_m.       \tag{4.3}
\]

This reproduces R170.878's exterior loop, but (0.1) adds the Poisson
reflection and fixes which of the two tails is input and which is output.

The sought inequality becomes, by (3.6),

\[
 \boxed{
 \|QC_hf\|\leq\|\delta E_SC_hf\|,
 \qquad h^0=h^2=0.}                               \tag{4.4}
\]

The right-hand side is the tail after the integer sum and the reflected
anti-causal elimination. The left-hand side is the original tail. This is
the typed version of the return:

\[
 {\cal R}_{q,h}(\delta E_SC_hf)=QC_hf.              \tag{4.5}
\]

For (4.5) to be a construction and not a circular Douglas argument, it
remains to directly prove:

\[
 \delta E_SC_hf=0\Longrightarrow QC_hf=0,           \tag{4.6}
\]

\[
 \|QC_hf\|\leq\|\delta E_SC_hf\|.                \tag{4.7}
\]

The formula for \({\cal R}_{q,h}\) is then determined on an explicit
source range, with no pseudo-inverse.

## 5. Relation to the corpus and exact boundary

R170.850 proves \(M_SE_S=1\) and R170.878 correctly keeps the exterior
tail. It also proves that Möbius alone does not sign the Wronskian. Equations
(1.3)--(1.5) are this route's extra datum: they place the Möbius inverse
in the opposite orientation via the self-dual additive Fourier transform.

Unitarity alone also does not prove (4.7): for an arbitrary vector,
(3.6) can have either sign. The pending content lies precisely in the
convolution columns

\[
 C_h,\qquad \operatorname{supp}h\subset(-T,T),\qquad
 h^0=h^2=0,                                          \tag{5.1}
\]

and must use (4.1). Replacing this class by the entire Hilbert space recovers
the inner criterion refuted by Connes--Consani.

## 6. Logical status

* Möbius inversion (1.2): **PROVED**; already present in R170.850.
* Joint factorization \(u_S=M_S^\vee E_S\): **WITHDRAWN** as an
  operator identity; remains only as a formal computation not suitable for
  comparing norms.
* Source blocks (2.4)--(2.8): algebraic computation **CONDITIONAL** on a
  factorization with compatible domains; semilocal application unproved.
* Cancellation (3.3) and balance (3.5)--(3.6): **CONDITIONAL** on that
  factorization and its unitarity; not established source identities.
* Oriented kernel propagation after the gap: **PROVED**.
* Restricted injectivity (4.6): **OPEN**.
* Restricted contraction (4.7): **OPEN**.
* Row D: **OPEN**.

The next proof must not refactor Möbius again. It must prove
(4.6)--(4.7) at the level of convolution kernels, via a
decomposition of the paths of \(E_SC_h\) by their first boundary crossing,
keeping together the reflection \(M_S^\vee\) and the two Tate residues.

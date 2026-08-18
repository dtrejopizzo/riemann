# 106.155 — The Fourier-doubled polarized relative complex

## 1. Purpose

The CCM degree-one object is a relative cokernel: adeles map to the ideles
class group by the summation/restriction morphism, and \(H^1\) is obtained
from its cyclic cokernel.  A polarization cannot be imposed after taking
the spectral trace.  It must be present on a source-side relative complex.

This document constructs the canonical polarization on the analytic
two-term relative complex.  The construction uses the self-dual additive
Fourier transform, inversion on the ideles class group, and Poisson
summation.  It produces an actual positive polarized reduced cohomology,
with the correct weight-one scaling identity.  Section 7 isolates the
remaining comparison with the finer cyclic \(H^1\).

## 2. Fourier and inversion

Let \(\mathbb A=\mathbb A_{\mathbb Q}\), equipped with the self-dual Haar
measure for the standard additive character.  Let

\[
 \mathcal H_A=L^2(\mathbb A;\mathbb R)_{\rm ev}
\]

be the real Hilbert space of even functions, and let \(\mathcal F\) be the
additive Fourier transform.  On the even real subspace,

\[
 \mathcal F^*=\mathcal F,\qquad \mathcal F^2=I.                 \tag{1}
\]

For an idele \(a\) of module \(|a|=e^t\), put

\[
 (S_tf)(x)=e^{t/2}f(ax).                                       \tag{2}
\]

Then \(S_t\) is orthogonal and

\[
 \mathcal F S_t=S_{-t}\mathcal F.                             \tag{3}
\]

On the ideles class group \(C_{\mathbb Q}\), let

\[
 \mathcal H_C=L^2(C_{\mathbb Q},d^*x;\mathbb R),
 \qquad (Ih)(x)=h(x^{-1}).                                     \tag{4}
\]

For multiplicative translation \(T_t\), one has

\[
 I^*=I,\qquad I^2=I,\qquad IT_t=T_{-t}I.                       \tag{5}
\]

## 3. The doubled complex structures

Set

\[
 \mathbb H_A=\mathcal H_A\oplus\mathcal H_A,
 \qquad
 \mathbb H_C=\mathcal H_C\oplus\mathcal H_C.                  \tag{6}
\]

Define

\[
 J_A(f_0,f_1)=(-\mathcal Ff_1,\mathcal Ff_0),
 \qquad
 J_C(h_0,h_1)=(-Ih_1,Ih_0).                                   \tag{7}
\]

### Lemma 3.1 — Source and target polarizations

On both doubled spaces, \(J^2=-I\), \(J^*=-J\).  With the direct-sum real
Hilbert metric \(g\), the form

\[
 \Omega(u,v):=g(Ju,v)                                         \tag{8}
\]

is continuous, alternating, and nondegenerate, and

\[
 \Omega(u,Jv)=g(u,v).                                         \tag{9}
\]

#### Proof

Equations (1) and (5) give \(J_A^2=J_C^2=-I\).  Self-adjointness of
\(\mathcal F\) and \(I\) gives \(J_A^*=-J_A\), \(J_C^*=-J_C\).  Hence
\(g(Ju,v)=-g(u,Jv)\), proving alternation.  Finally
\(\Omega(u,Jv)=g(Ju,Jv)=g(u,v)\), since \(J\) is orthogonal. \(\square\)

Define doubled normalized flows

\[
 \mathbb S_t=\begin{pmatrix}S_t&0\\0&S_{-t}\end{pmatrix},
 \qquad
 \mathbb T_t=\begin{pmatrix}T_t&0\\0&T_{-t}\end{pmatrix}.    \tag{10}
\]

Equations (3) and (5) imply

\[
 J_A\mathbb S_t=\mathbb S_tJ_A,
 \qquad
 J_C\mathbb T_t=\mathbb T_tJ_C.                              \tag{11}
\]

Thus both normalized flows preserve \(g,\Omega,J\).  Their weight-one
versions \(e^{t/2}\mathbb S_t\), \(e^{t/2}\mathbb T_t\) scale \(g\) and
\(\Omega\) by \(e^t\).

## 4. Poisson summation is exactly the descent identity

On the usual Poisson domain

\[
 \mathscr D_0=\{f\in\mathcal S(\mathbb A)_{\rm ev}:
                 f(0)=\mathcal Ff(0)=0\},                     \tag{12}
\]

define the normalized summation map

\[
 (Ef)(x)=|x|^{1/2}\sum_{q\in\mathbb Q^*}f(qx).                \tag{13}
\]

Poisson summation and the vanishing conditions give

\[
 \boxed{E\mathcal F=IE.}                                      \tag{14}
\]

Moreover, normalized scaling gives

\[
 ES_t=T_tE.                                                    \tag{15}
\]

Define the doubled differential

\[
 d=E\oplus E:\mathscr D_0\oplus\mathscr D_0
                 \longrightarrow\mathbb H_C.                 \tag{16}
\]

### Theorem 4.1 — The relative differential is polarized

On its domain,

\[
 \boxed{dJ_A=J_Cd,\qquad d\mathbb S_t=\mathbb T_td.}          \tag{17}
\]

#### Proof

For ((f_0,f_1)), equation (14) gives

\[
 dJ_A(f_0,f_1)=(-E\mathcal Ff_1,E\mathcal Ff_0)
               =(-IEf_1,IEf_0)=J_Cd(f_0,f_1).
\]

Equation (15), applied to the two time directions, gives the second
identity. \(\square\)

This is the source-side compatibility that was absent from a direct
spectral definition of \(J\): the complex structure is fixed by additive
Fourier duality, and its descent is the Poisson formula.

## 5. Graph completion and polarized reduced cohomology

Give \(\mathscr D_0\) the graph norm

\[
 \|f\|_E^2=\|f\|_{\mathcal H_A}^2+\|Ef\|_{\mathcal H_C}^2,    \tag{18}
\]

and let \(\mathcal D_E\) be its completion.  Equations (14)--(15) show
that \(\mathcal F\) and normalized scaling act isometrically on this graph
completion.  Hence \(d:\mathcal D_E^2\to\mathbb H_C\) is bounded and
intertwines \(J\) and scaling.

Consider the two-term Hilbert complex

\[
 0\longrightarrow\mathcal D_E^2
   \mathop{\longrightarrow}^{d}\mathbb H_C
   \longrightarrow0.                                          \tag{19}
\]

Its reduced first cohomology is

\[
 \overline H^1_{\rm rel}:=\mathbb H_C/\overline{\operatorname{Ran}d}
 \simeq(\overline{\operatorname{Ran}d})^\perp.                \tag{20}
\]

### Theorem 5.1 — Unconditional polarization of the reduced relative cohomology

The space \(\overline H^1_{\rm rel}\) carries induced operators and forms

\[
 (\overline\Omega,\overline J,\overline g,\overline{\mathbb T}_t)
\]

such that

\[
 \boxed{
 \overline J^2=-I,\qquad
 \overline g(u,v)=\overline\Omega(u,\overline Jv),\qquad
 \overline g(u,u)>0\quad(u\ne0),\qquad
 \overline J\overline{\mathbb T}_t
 =\overline{\mathbb T}_t\overline J.}                         \tag{21}
\]

For the weight-one flow \(\vartheta_t=e^{t/2}\overline{\mathbb T}_t\),

\[
 \boxed{
 \overline\Omega(\vartheta_tu,\vartheta_tv)
 =e^t\overline\Omega(u,v),qquad
 \Theta^\dagger+\Theta=I.}                                   \tag{22}
\]

#### Proof

Theorem 4.1 makes \(\overline{\operatorname{Ran}d}\) invariant under
(J_C) and \(\mathbb T_t\).  Since both operators are orthogonal, its
orthogonal complement is also invariant.  Restrict (8)--(11) to that
complement.  Positivity in (21) is the ambient Hilbert norm.  The scaling
law and generator identity follow exactly as in Theorem 4.1 of 106.154.
\(\square\)

Thus a genuine polarized relative cohomology has been constructed without
using the zero spectrum.

## 6. Incorporating the prime coefficient descent

Regard the two real polarized Hilbert spaces as complex Hilbert spaces via
their respective complex structures and form their balanced complex Hilbert
tensor product.  On this product
\(J_C\otimes I=I\otimes J_{\mathscr K}\); its imaginary Hermitian part is
the alternating form and its real part is the positive metric.  Tensor the
target term in (19) with the polarized Cauchy-dilation module
\(\mathscr K\) of 106.154.  The embeddings

\[
 \iota_{\log p}:\mathcal V_p^1\hookrightarrow\mathscr K
\]

then place every finite-prime coefficient module inside the same polarized
relative complex.  The resulting normal state has the exact local moments

\[
 \tau(U_{\log p}^k)=p^{-|k|/2}.                               \tag{23}
\]

The finite-prime polarization, the generic scaling interpolation, and the
Fourier/Poisson complex structure therefore coexist in one source-defined
Hilbert complex.

## 7. Why the degree-zero cone is not the cyclic comparison object

CCM's object is not merely the Hilbert cokernel of the degree-zero map
\(E\).  It is

\[
 H^1_{\rm CCM}
 =\operatorname{Tor}(\mathbb C^\natural,
     \operatorname{coker}(\rho^\natural)),                    \tag{24}
\]

formed in cyclic modules with a Schwartz/Meyer topology chosen so that all
zeros, including hypothetical noncritical zeros, occur in the spectral
trace.  The construction above produces the positive reduced Hilbert
cohomology of the degree-zero shadow.

The formula below records only the first attempted bridge; it is not a
valid comparison target:

\[
 \boxed{
 \mathbf R\operatorname{Coker}(\rho^\natural)
 \ \widehat\otimes^{\mathbf L}_{\rm cyc}\ \mathbb C^\natural
 \longrightarrow
 \operatorname{Cone}(d)\widehat\otimes\mathscr K
 }
                                                                    \tag{25}
\]

The assertion that this map is a quasi-isomorphism must not be made.  The
right-hand side is only the degree-zero Hilbert shadow and can have zero
reduced cohomology.  It therefore discards precisely the derived
information which carries the zero spectrum.

The naive degree-zero argument cannot prove (25).  Under Mellin transform,
the corresponding Hilbert range is multiplication by the completed Euler
multiplier on a real spectral line.  Since its zero set has Lebesgue measure
zero, that multiplication range is dense: if (h) is orthogonal to the
range, the conjugate multiplier times (h) vanishes almost everywhere, so
(h=0).  Consequently the reduced degree-zero Hilbert quotient may vanish
even while the derived cyclic cokernel is nonzero.  The information is in
the derived/cyclic degrees and cannot be recovered by changing the Hilbert
norm after taking the range.

The correct bridge must instead be a cyclic enhancement

\[
 \boxed{
 \mathfrak D:\operatorname{Cone}(\rho^\natural)
 \longrightarrow \mathfrak C_{\rm FP}}
                                                                    \tag{26}
\]

with all of the following properties:

1. \(\mathfrak C_{\rm FP}\) is a cyclic or mixed \((b,B)\)-complex, not a
   two-term Hilbert cone;
2. its degree-zero shadow is (19), including the Fourier--Poisson identity;
3. it carries a chain complex structure \(J_{\rm FP}\) with
   \(J_{\rm FP}^2=-I\) and \([J_{\rm FP},b+B]=0\);
4. its Hermitian real part is positive before taking cohomology;
5. normalized scaling commutes with \(J_{\rm FP}\);
6. \(\mathfrak D\) is a scaling-equivariant quasi-isomorphism in degree one
   and is compatible with the CCM trace pairing.

Only (26), rather than the raw Hilbert cone in (25), can transfer a
source-defined polarization to the actual CCM \(H^1\).

## 8. Status

Proved:

* a Fourier-defined complex structure independent of zeta zeros;
* a positive symplectic polarization on source and target;
* exact descent through the adelic summation map by Poisson summation;
* a genuine polarized reduced relative Hilbert cohomology;
* compatibility with the weight-one scaling flow;
* coexistence with all prime modules through the Cauchy dilation.

Not proved:

* the cyclic Fourier--Poisson complex \(\mathfrak C_{\rm FP}\) and the
  derived comparison (26);
* transfer of this polarization to the full CCM cyclic \(H^1\);
* RH.

# D.87 — Periodic dagger landing: the first naturality obstruction

## Status

D.86 constructs the canonical two-output preparation complex and proves
that its Krein pullback is exactly \(-4B_{\rm nuc}\).  This note attempts
the remaining natural transformation from the intrinsic periodic Yoneda
cohomology of row A to that preparation state.

The scalar part can be constructed: once a seed is chosen,
\(J(\phi_r)=\delta_r\) and row C force its whole orbit to be the orbit under
\(U_r\).  A bilateral primitive annihilator also kills the two Tate
jets exactly and commutes with every \(U_r\).

There is, however, no direct normed natural transformation from a periodic
fibre \(C_p\) to the round-trip Hilbert state.  Descent from
\(\mathbb R/(\log p)\mathbb Z\) makes the deck transformation the identity
(or a fixed line monodromy), whereas its proposed analytic realization is
translation \(U_p\) on \(L^2(\mathbb R)\).  That translation has empty
point spectrum.  The first naturality square therefore forces every
extremal generator to map to zero, contradicting its ordered-frame norm.
Distributional periodic combs repair descent but have no finite Hilbert
norm and do not enter the round-trip colligation.

If deck naturality is forgotten, arbitrary primitive seeds give a
scalar-natural map.  Its preparation Gram is exactly \(-4B_{\rm nuc}\),
including every \(p^k\) and the complete Gamma term.  Its positive Hilbert
Gram is a different form, and convolution is not an isometric realization
of the periodic Künneth norm.

No RH, sign-selected subspace, or norm defined from \(B_{\rm nuc}\) is
used.  The paper is not modified.

## 1. The scalar-natural candidate

At finite periodic depth write

\[
 E_{p,r}(a)=
 \mathbb R\{e_{p,r,0},\ldots,e_{p,r,d_{p,r}(a)-1}\},
 \qquad d_{p,r}(a)=ap^r-p+1.                              \tag{1.1}
\]

For a pair of fibres, Künneth gives the ordered frame

\[
 E_{p,r}(a)\otimes E_{q,s}(b)
 =\mathbb R\{e_{p,r,i}\boxtimes e_{q,s,j}\}_{i,j}.        \tag{1.2}
\]

After nuclear scalar extension a generator is
\(e_\alpha\otimes\delta_m\), with
\(\alpha=(p,q,r,s,i,j)\).  The common A--B--C action is

\[
 V_m\phi_t\longmapsto\delta_m*\delta_t=\delta_{mt}
 \longmapsto U_m.                                        \tag{1.3}
\]

This discussion starts after row A has passed from the idempotent tropical
section module to the free real cotangent frame.  An additive map directly
from a max-plus module to a real vector space would indeed kill the
idempotent sum, but that is not the map being tested: the source of (1.4)
is the already constructed real linearization of the extremal coefficient
differentials.

Consequently every scalar-linear transformation to the row-C test
representation is determined by seed vectors \(h_\alpha\) and must satisfy

\[
 \eta(e_\alpha\otimes\delta_m)=U_mh_\alpha.              \tag{1.4}
\]

This is the unique map for which

\[
\begin{CD}
 e_\alpha\otimes\delta_t @>{L_{\delta_m}}>>
 e_\alpha\otimes\delta_{mt}\\
 @V{\eta}VV @VV{\eta}V\\
 U_th_\alpha @>{U_m}>> U_{mt}h_\alpha
\end{CD}                                                   \tag{1.5}
\]

commutes.  Crucially, the Witt cyclic vector \(\phi_t\) is not a periodic
extremal \(e_{p,r,i}\).  The point mass \(\delta_m\) acts on the common
coefficient factor and leaves the extremal index fixed.

## 2. Exact bilateral primitive annihilator

Put \(R=\log n\), let \(S_R\) be central logarithmic translation, and set

\[
 \Pi_n=I-\frac{S_R+S_{-R}}{2\cosh(R/2)}.                  \tag{2.1}
\]

For the two Tate moments,

\[
 M_\pm(S_{\epsilon R}h)=e^{\pm\epsilon R/2}M_\pm(h).
                                                                  \tag{2.2}
\]

Therefore

\[
 M_\pm(\Pi_nh)=
 \left(1-\frac{e^{R/2}+e^{-R/2}}{2\cosh(R/2)}\right)
 M_\pm(h)=0.                                             \tag{2.3}
\]

The operator \(\Pi_n\) is not asserted to be idempotent.  It commutes with
every translation and its image lies in the primitive ideal.  After arbitrary seed
choices \(k_\alpha\), the formula

\[
 F_\alpha=\Pi_nk_\alpha,\qquad
 \eta_{\rm prim}(e_\alpha\otimes\delta_m)=U_mF_\alpha    \tag{2.4}
\]

is scalar-natural and lands in the two-jet primitive kernel.

This uses both orientations \(S_R,S_{-R}\).  One is supplied by the
Dirichlet action and the other by the Tate involution.  Neither orientation
alone annihilates both moments.  Thus (2.4) already belongs to the doubled
analytic realization, not to one periodic component by itself.

## 3. The first failed naturality square

Let \(\pi_p:\mathbb R\to C_p=\mathbb R/(\log p)\mathbb Z\) be the universal
cover.  A section of a line on \(C_p\), pulled to the cover, satisfies

\[
 \tau_p^*s=\chi_ps,                                      \tag{3.1}
\]

where \(\chi_p=1\) for the coefficient unit and more generally denotes its
fixed line monodromy.  On the regular-moduli cotangent used by row A, this
fixed transition adds no coefficient differential: the ordered extremal
cotangent frame is deck-fixed.  Thus its relevant value is
\(\chi_p=1\).  Keeping a general scalar \(\chi_p\) below shows that even a
unitary character twist cannot repair the problem.

A direct natural transformation from this real cotangent frame to the
central Hilbert realization must make

\[
\begin{CD}
 H^0(C_p,D) @>{\tau_p^*}>> H^0(C_p,D)\\
 @V{\eta_p}VV @VV{\eta_p}V\\
 L^2(\mathbb R) @>{U_p}>> L^2(\mathbb R)
\end{CD}                                                   \tag{3.2}
\]

commute.  Hence

\[
 U_p\eta_p(s)=\chi_p\eta_p(s).                           \tag{3.3}
\]

The bilateral translation \(U_p=S_{\log p}\) has no nonzero eigenvector in
\(L^2(\mathbb R)\).  After Fourier transform, (3.3) becomes

\[
 (e^{-i\tau\log p}-\chi_p)\widehat{\eta_p(s)}(\tau)=0.   \tag{3.4}
\]

If \(|\chi_p|\ne1\), the multiplier never vanishes.  If
\(|\chi_p|=1\), its zero set is discrete and has Lebesgue measure zero.
Thus an \(L^2\) function supported there is zero:

\[
 \boxed{\eta_p=0.}                                       \tag{3.5}
\]

But the ordered-frame realization assigns

\[
 \|e_{p,r,i}\|_{\rm Ext}=1.                              \tag{3.6}
\]

> **Proposition 3.1 (periodic landing no-go).**  There is no nonzero
> norm-preserving natural transformation from the real linearized
> extremal cotangent frames of the periodic Yoneda fibres
> to the central round-trip Hilbert state which identifies deck
> translation with \(U_p\).  The first failed relation is (3.2), before any
> dagger inequality is considered.

A periodic Dirac comb solves (3.3) distributionally.  It is not in
\(L^2(\mathbb R)\), has no finite preparation norm, and is outside the
domains of \(P,C,D_T\) and the observability map.  It therefore does not
define \(\mathfrak p_\dagger\).

This does not contradict A--C.  Their comparison uses \(U_p\) on the
**nuclear scalar factor** and never identifies it with deck translation of
an extremal section.

## 4. Künneth and norm after forgetting descent

If (3.2) is forgotten and external products are realized by convolution,

\[
 F_{\alpha\boxtimes\beta}=F_\alpha*F_\beta,              \tag{4.1}
\]

then scalar covariance and the two moments are preserved.  The norm is not:

\[
 \|F_\alpha*F_\beta\|_2^2
 ={1\over2\pi}\int
 |\widehat F_\alpha(\tau)|^2|\widehat F_\beta(\tau)|^2d\tau,
                                                                  \tag{4.2}
\]

whereas the ordered-frame Künneth norm is
\(\|e_\alpha\otimes e_\beta\|^2
=\|e_\alpha\|^2\|e_\beta\|^2\).
For \(f=(1,1)/\sqrt2\), ordinary sequence convolution gives

\[
 \|f*f\|_2^2={3\over2}\ne1=\|f\|_2^4.                   \tag{4.3}
\]

Thus the seed construction is monoidal only algebraically; it is not a
dagger Künneth functor.

## 5. Complete preparation Gram

For arbitrary primitive seeds let

\[
 (p_{\alpha,m},z_{\alpha,m})
 =(p(U_mF_\alpha),z(U_mF_\alpha))                        \tag{5.1}
\]

be their Halmos coordinates, and apply

\[
 \mathcal Q(p,z)=(2D_Tp-C^{1/2}z,\ C^{1/2}z),\qquad
 J=\operatorname{diag}(I,-I).                            \tag{5.2}
\]

The global preparation Gram is

\[
 \boxed{
 G_{(\alpha,m),(\beta,n)}
 =\langle\mathcal Q_{\alpha,m},J\mathcal Q_{\beta,n}\rangle
 =-4B_{\rm nuc}(U_mF_\alpha,U_nF_\beta).}               \tag{5.3}
\]

The first equality defines the source round-trip Gram; the second is the
previously proved Halmos pullback, not a definition from \(B_{\rm nuc}\).

At a support window \([-T,T]\), put

\[
 \mathcal P_T=\{(p,k):k\log p\le2T\},\qquad
 c_{p,k}={\log p\over p^{k/2}},                           \tag{5.4}
\]

\[
 b_T(\tau)=m_\infty(\tau)
 +2\sum_{(p,k)\in\mathcal P_T}
 c_{p,k}\cos(k\log p\,\tau),                            \tag{5.5}
\]

where the complete Gamma finite part is

\[
 m_\infty(\tau)=
 \log\pi-\operatorname{Re}\psi
 \left({1\over4}+{i\tau\over2}\right).                  \tag{5.6}
\]

Then

\[
 \boxed{
 G_{(\alpha,m),(\beta,n)}
 =-{4\over2\pi}\int_{\mathbb R}
 b_T(\tau)\overline{\widehat F_\alpha(\tau)}
 \widehat F_\beta(\tau)e^{i\tau\log(n/m)}d\tau.}         \tag{5.7}
\]

Changing Fourier sign conjugates the phase and leaves the Hermitian matrix
unchanged.  Equation (5.5) contains every prime power capable of meeting
the support window; (5.6) contains the complete Gamma term.  Cofinal
support enlargement is stationary because correlations beyond \(2T\)
vanish.

Equivalently,

\[
\begin{aligned}
 G_{(\alpha,m),(\beta,n)}
 ={}&\langle r_0(p_{\alpha,m},z_{\alpha,m}),
              r_0(p_{\beta,n},z_{\beta,n})\rangle\\
 &-\langle C^{1/2}z_{\alpha,m},
              C^{1/2}z_{\beta,n}\rangle.                \tag{5.8}
\end{aligned}
\]

Replacing \(J\) by the positive metric changes the minus to a plus.  That
form is positive but exceeds (5.8) by twice the boundary Gram, so it is not
row D.

## 6. Conclusion

The common scalar action determines (1.4), and (2.1) imposes the two
A--B--C moments exactly.  The complete preparation Gram is (5.3)--(5.8),
with every \(p^k\) and Gamma.

The desired \(\mathfrak p_\dagger\) cannot be a direct natural
transformation from one periodic fibre: deck descent forces its Hilbert
image to vanish.  Forgetting descent permits arbitrary seeds but loses
canonicity and the dagger Künneth norm.  A viable map must first form a
global prime--Gamma quotient or induced representation in which deck
monodromy is absorbed, and only then land in the round-trip state.

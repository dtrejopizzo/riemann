# 106.169 — Tate suspension and the middle relative polarization

## 1. Purpose

The absolute arithmetic curve supplies, over every finite prime \(p\), the
complex Tate curve

\[
 E_p=\mathbb C^\times/p^\mathbb Z
     \simeq C_p\times\mathbb S^1,
 \qquad C_p=\mathbb R/(\log p)\mathbb Z.                    \tag{1}
\]

The second factor is independent of \(p\). This is the first geometric
place where all prime orbits possess a common Hodge partner. This note uses
that partner to construct the finite-prime gluing map left undefined in
106.160.

Ordinary relative cohomology removes the common phase class but leaves its
Hodge conjugate, so it is not preserved by the complex structure. The
correct polarized object is the largest \(J\)-invariant part of the
relative kernel, equivalently the orthogonal complement of the full
generic Hodge plane. The result is described by two global balance
equations, one for phase and one for its arithmetic conjugate.

The construction is source-defined from the Tate curves and the common
Cauchy-dilation coefficient module of 106.154. It uses neither zeta zeros
nor Weil positivity.

## 2. The Hodge plane of one Tate curve

Write

\[
 \ell_p=\log p,\qquad
 E_p=(\mathbb R/\ell_p\mathbb Z)_u
       \times(\mathbb R/2\pi\mathbb Z)_\theta .              \tag{2}
\]

Give \(E_p\) the orientation \(du\wedge d\theta\), the flat metric
\(du^2+d\theta^2\), and complex coordinate \(u+i\theta\). Put

\[
 a_p=\frac{du}{\ell_p},\qquad
 b_p=\frac{d\theta}{2\pi},\qquad
 c_p=\frac{2\pi}{\ell_p}.                                  \tag{3}
\]

Then \(a_p,b_p\) are the integral harmonic basis of
\(H^1(E_p;\mathbb R)\), and

\[
 \int_{E_p}a_p\wedge b_p=1.                                 \tag{4}
\]

Let \(J_p=\star_p\) be the Hodge star on harmonic one-forms. Directly from
the flat metric,

\[
 \boxed{
 J_pa_p=c_pb_p,\qquad
 J_pb_p=-c_p^{-1}a_p.}                                      \tag{5}
\]

Define

\[
 \Omega_p(\alpha,\beta)=\int_{E_p}\alpha\wedge\beta,\qquad
 g_p(\alpha,\beta)=\Omega_p(\alpha,J_p\beta).                \tag{6}
\]

Thus

\[
 g_p(a_p,a_p)=c_p,\qquad
 g_p(b_p,b_p)=c_p^{-1},\qquad
 g_p(a_p,b_p)=0.                                             \tag{7}
\]

Therefore
\((H^1(E_p),\Omega_p,J_p,g_p)\) is a positive polarized real Hodge
structure obtained from the actual complex Tate curve.

## 3. The common coefficient object

Let

\[
 (\mathscr K,g_{\mathscr K},V_t)                             \tag{8}
\]

be the real Cauchy-dilation Hilbert module of 106.154. The normalized flow
\(V_t\) is orthogonal, and its constant cyclic vector
\(\Omega_{\rm gen}\) satisfies

\[
 \langle\Omega_{\rm gen},V_{k\ell_p}\Omega_{\rm gen}\rangle
 =p^{-k/2},\qquad k\geq1.                                   \tag{9}
\]

Every local prime coefficient module of 106.153 embeds isometrically in
this one common object. For a finite nonempty set of primes \(S\), put

\[
 \mathscr V_S
 =\bigoplus_{p\in S}
   \left(H^1(E_p;\mathbb R)\widehat\otimes_{\mathbb R}
         \mathscr K\right).                                 \tag{10}
\]

Define

\[
 J_S=\bigoplus_{p\in S}(J_p\otimes I),\qquad
 g_S=\bigoplus_{p\in S}(g_p\otimes g_{\mathscr K}),\qquad
 \Omega_S(u,v)=g_S(J_Su,v).                                 \tag{11}
\]

Then \(J_S^2=-I\), \(\Omega_S\) is alternating, and \(g_S\) is positive.
The common normalized flow

\[
 \mathcal V_t=\bigoplus_{p\in S}(I\otimes V_t)               \tag{12}
\]

commutes with \(J_S\) and preserves both forms. Its weight-one version
\(e^{t/2}\mathcal V_t\) scales them by \(e^t\).

## 4. Pullback to the generic Tate cylinder

Let

\[
 \widetilde E=\mathbb R_u\times
               (\mathbb R/2\pi\mathbb Z)_\theta
 \simeq\mathbb C^\times                                     \tag{13}
\]

be the common generic Tate cylinder. The quotient
\(u\bmod\ell_p\) gives a covering
\(\pi_p:\widetilde E\to E_p\). On cohomology,

\[
 \pi_p^*[a_p]=0,\qquad
 \pi_p^*[b_p]=[b],\qquad b=\frac{d\theta}{2\pi},             \tag{14}
\]

because \(du/\ell_p\) is exact on the cylinder and the phase circle
survives.

The topological pullback adds phase components with unit coefficient. The
CCM/Lefschetz normalization also contains the orbit volume and critical
half-density return. In the integral basis (3), the resulting amplitude is

\[
 \alpha_p
 =\sqrt{\frac{\ell_p}{c_p}}\,p^{-1/2}
 =\frac{\ell_p}{\sqrt{2\pi p}}.                              \tag{15}
\]

Its squared Hodge norm is

\[
 c_p\alpha_p^2=\frac{\ell_p}{p},                             \tag{16}
\]

the literal first primitive Euler layer. Define the normalized generic
restriction

\[
 R_S:\mathscr V_S\longrightarrow\mathscr K,\qquad
 R_S\!\left(
   \sum_{p\in S}a_p\otimes x_p+b_p\otimes y_p
 \right)
 =\sum_{p\in S}\alpha_py_p.                                 \tag{17}
\]

It is surjective and intertwines the common coefficient flow. Ordinary
relative degree one is \(\ker R_S\), but

\[
 R_SJ_S\!\left(
   \sum_pa_p\otimes x_p+b_p\otimes y_p
 \right)
 =\sum_{p\in S}\alpha_pc_px_p.                              \tag{18}
\]

Thus deleting only the generic phase is precisely the parity error found
in the heat/winding construction.

## 5. The middle relative space

Define

\[
 \boxed{
 IH^1_S:=\ker R_S\cap\ker(R_SJ_S).}                          \tag{19}
\]

Equivalently,

\[
 \boxed{
 IH^1_S=
 \left\{
  \sum_{p\in S}(a_p\otimes x_p+b_p\otimes y_p):
  \sum_{p\in S}\alpha_pc_px_p=0,\quad
  \sum_{p\in S}\alpha_py_p=0
 \right\}.}                                                 \tag{20}
\]

### Theorem 5.1 — Maximal polarized relative descent

The space \(IH^1_S\):

1. is preserved by \(J_S\) and by the common normalized flow;
2. carries the positive polarization obtained by restricting
   \((\Omega_S,J_S,g_S)\);
3. is the largest \(J_S\)-invariant linear subspace of \(\ker R_S\);
4. is defined without spectral input.

#### Proof

If \(v\in IH^1_S\), then \(R_Sv=R_SJ_Sv=0\). Since \(J_S^2=-I\),

\[
 R_S(J_Sv)=0,\qquad
 R_SJ_S(J_Sv)=-R_Sv=0.
\]

Hence \(J_Sv\in IH^1_S\). The common flow commutes with \(J_S\) and
\(R_S\), hence also preserves (19). Restriction of a positive metric and
of a compatible symplectic complex structure proves item 2.

If \(W\subseteq\ker R_S\) and \(J_SW=W\), then for \(w\in W\), both
\(R_Sw=0\) and \(R_SJ_Sw=0\). Hence \(W\subseteq IH^1_S\), proving
maximality. Item 4 follows from (2), (8), and (15). \(\square\)

This is a linear middle extension: it imposes both the relative boundary
condition and its Hodge-conjugate boundary condition.

## 6. Orthogonal removal of the full generic Hodge plane

Put

\[
 C_S=\sum_{p\in S}c_p\alpha_p^2
 =\sum_{p\in S}\frac{\log p}{p}.                             \tag{21}
\]

Define

\[
 \Gamma_S:\mathscr K\oplus\mathscr K\longrightarrow\mathscr V_S,\qquad
 \Gamma_S(z,w)=
 \sum_{p\in S}\alpha_p
 \bigl(a_p\otimes z+c_pb_p\otimes w\bigr).                  \tag{22}
\]

Then

\[
 J_S\Gamma_S(z,w)=\Gamma_S(-w,z),                            \tag{23}
\]

and

\[
 g_S(\Gamma_S(z,w),\Gamma_S(z,w))
 =C_S(\|z\|^2+\|w\|^2).                                     \tag{24}
\]

### Theorem 6.1 — Exact polarized splitting

There is a \(J_S\)-orthogonal decomposition

\[
 \boxed{
 \mathscr V_S=IH^1_S\ \widehat\oplus\
               \mathrm{Ran}\,\Gamma_S.}                \tag{25}
\]

The orthogonal projection \(P_S^{\rm mid}\) onto \(IH^1_S\) is

\[
\begin{aligned}
 \bar x&=C_S^{-1}\sum_{p\in S}c_p\alpha_px_p,
 & (P_S^{\rm mid}x)_p&=x_p-\alpha_p\bar x,\\
 \bar y&=C_S^{-1}\sum_{p\in S}\alpha_py_p,
 & (P_S^{\rm mid}y)_p&=y_p-\alpha_pc_p\bar y.
                                                               \tag{26}
\end{aligned}
\]

Thus the quotient by the full generic Hodge plane, unlike the ordinary
relative quotient by its phase half, inherits a canonical positive
polarization.

#### Proof

Formula (24) gives closed range. A vector
\(v=(x_p,y_p)_{p\in S}\) is orthogonal to every \(\Gamma_S(z,w)\)
exactly when

\[
 \sum_pc_p\alpha_px_p=0,\qquad
 \sum_p\alpha_py_p=0,
\]

which is (20). This proves (25). Subtracting
\(\Gamma_S(\bar x,\bar y)\) gives (26); direct substitution verifies both
balance equations. \(\square\)

The generic subtraction is therefore the orthogonal removal of a complete
complex plane. Its arithmetic half is forced by Hodge conjugacy.

## 7. Compatibility under adjoining primes

For finite sets \(S\subset T\), extend a vector by zero in the components
\(T\setminus S\). Both equations in (20) are unchanged. Hence there are
isometric polarized inclusions

\[
 IH^1_S\hookrightarrow IH^1_T.                              \tag{27}
\]

### Theorem 7.1 — Algebraic global polarization

The directed union

\[
 IH^1_{\rm fin}:=\varinjlim_S IH^1_S                         \tag{28}
\]

is the space of finitely supported families satisfying

\[
 \sum_p\alpha_pc_px_p=0,\qquad
 \sum_p\alpha_py_p=0.                                       \tag{29}
\]

It carries a well-defined nondegenerate alternating form, compatible
complex structure, positive metric, and normalized scaling action.

#### Proof

The inclusions preserve the local direct-sum forms and \(J\). Every
nonzero vector lies in some finite \(IH^1_S\), where its norm is strictly
positive. Compatibility and nondegeneracy follow from Theorem 5.1.
\(\square\)

This is not a direct sum of independent prime polarizations: the two
equations (29) couple every occupied prime through one common generic
coefficient object.

## 8. The cofinal topology is not Hilbertian

The ambient Hilbert direct sum has squared norm

\[
 \sum_p\left(c_p\|x_p\|^2+c_p^{-1}\|y_p\|^2\right).          \tag{30}
\]

Euler's divergence of \(\sum_p1/p\) implies

\[
 \sum_pc_p\alpha_p^2
 =\sum_p\frac{\log p}{p}=+\infty.                            \tag{31}
\]

Hence the balance maps in (29) are not continuous for (30).

### Proposition 8.1 — Dense middle space in Hilbert completion

The space \(IH^1_{\rm fin}\) is dense in the Hilbert direct sum (30).
Thus its Hilbert completion forgets both generic balance conditions.

#### Proof

Start with a finitely supported family and let

\[
 d=\sum_pc_p\alpha_px_p,\qquad e=\sum_p\alpha_py_p.
\]

Choose a disjoint finite set \(T\) with
\(C_T=\sum_{p\in T}c_p\alpha_p^2\) arbitrarily large. Add

\[
 x_p^{\rm corr}=-\alpha_pC_T^{-1}d,\qquad
 y_p^{\rm corr}=-\alpha_pc_pC_T^{-1}e,\qquad p\in T.         \tag{32}
\]

These corrections cancel \(d,e\), while their total squared norm is

\[
 C_T^{-1}(\|d\|^2+\|e\|^2)\longrightarrow0.                 \tag{33}
\]

Therefore every finite vector is approximated by balanced vectors.
\(\square\)

### Corollary 8.2 — The raw boundary operator is not closable

On the algebraic direct sum let

\[
 \mathcal B(x,y)=
 \left(\sum_pc_p\alpha_px_p,\sum_p\alpha_py_p\right).        \tag{34}
\]

Viewed from the Hilbert space (30) to
\(\mathscr K\oplus\mathscr K\), \(\mathcal B\) is not closable.

#### Proof

The corrections (32), with fixed nonzero boundary value, converge to zero
in (30). This is the standard criterion for nonclosability. \(\square\)

Thus the global object must retain the LF/nuclear finite-support topology
before Hodge completion. This is the same nonreduced topology needed by
the CCM cokernel to retain resonant classes.

## 9. Relation to the CCM comparison

The construction supplies a concrete finite-prime gluing differential:

\[
 \boxed{
 \partial_{\rm Tate}=R\oplus RJ,\qquad
 IH^1_{\rm fin}=\ker\partial_{\rm Tate}.}                    \tag{35}
\]

It also proves positivity of the induced source form. What remains is to
show that localization of the CCM cyclic cone is a quasi-isomorphism onto
(35) after adding the archimedean spin and polar pages. Proposition 8.1
shows why Hilbert completion cannot prove this: it erases the relative
conditions.

The next identity is therefore the nuclear chain equality

\[
 \boxed{
 \mathrm{Loc}\,\circ d_{\rm CCM}
 =\partial_{\rm Tate}\circ\mathrm{Loc}_0
   \ \oplus\ d_{\Gamma,0,2},}                                \tag{36}
\]

where \(d_{\Gamma,0,2}\) is the explicit Gamma/polar boundary page of
106.160. If (36) is a degree-one quasi-isomorphism, Theorem 7.1 transfers
the positive form without a spectral sign assumption. Construction and
proof of this nuclear comparison remain open.

## 10. Status

Proved without RH or zero input:

* the actual Tate-curve Hodge planes over every ordinary prime;
* the common generic restriction with the exact primitive normalization;
* the largest \(J\)-invariant relative kernel;
* its two global arithmetic balance equations;
* a positive alternating polarization and weight-one scaling law;
* orthogonal splitting into the middle space and the full generic Hodge
  plane;
* compatibility under adjoining primes;
* the precise nonclosability of the cofinal Hilbert boundary map.

Still required:

* construction of the nuclear localization map in (36);
* inclusion of the Gamma/polar differential in that chain map;
* proof that (36) is a degree-one quasi-isomorphism onto the CCM spectral
  cokernel.

The global polarization is constructed on the complete finite-support
Tate-localized source. The remaining issue is faithful derived descent to
the existing CCM degree-one object.

## 11. Primary geometric input

The decomposition \(E_p=C_p\times\widetilde{\mathcal X}_\infty\), the
prime-independent phase circle, and the holomorphic form
\(d\lambda/\lambda+i\,d\theta\) are from Connes and Consani,
*On the Absolute Geometry of Spec Z and the Fargues--Fontaine Curve*.
The arithmetic Picard monoid, generic orbit, and prime fibres \(C_p\) are
from Connes and Consani, *On the Jacobian of the Arithmetic Curve*.

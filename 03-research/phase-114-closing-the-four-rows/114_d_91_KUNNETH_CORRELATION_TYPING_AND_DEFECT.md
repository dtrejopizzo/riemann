# D.91 — Künneth correlation, polarized defect and Schur homogeneity

## Status

D.88--D.90 construct a valid transverse trace and a coherent normed
landing, but they expose a type distinction which must be enforced before
using them for row D.

For the Weil quadratic form the geometric Künneth input is
\(f\boxtimes\widetilde g\).  Addition pushforward produces the correlation
\(f*\widetilde g\), and the row-C character is then applied **linearly**:
\[
 \ell(f*\widetilde g)=B_{\rm nuc}(f,g).
\]
Feeding the correlation back as a new test into
\(B_{\rm nuc}(h,h)\) is a different, quartic construction.

With the correct typing, the transverse trace remains useful as a nuclear
and Hilbert coisometry, but its positive defect is a quadratic form on the
tensor variable.  On the diagonal tensor \(f\boxtimes\widetilde f\) it is
quartic in \(f\), whereas the Schur tower and \(B_{\rm nuc}(f,f)\) are
quadratic.  No fixed linear compression or norm of the transverse defect
can identify the two while preserving polarization.

Moreover, the transverse defect lies in the kernel of addition
pushforward.  Every functional which factors through the row-C character
annihilates it.  A nonzero compression of that defect would be a new
character and would alter the exact prime-power--Gamma Gram.

Finally, the actual Connes--Consani extremals do not supply a hidden
finite-dimensional restriction after real group completion.  Their hinge
points are dense in each periodic interval as depth varies; their real
linear spans are dense in the piecewise-linear, hence continuous and
\(L^2\), section realizations.  Tensor products are correspondingly dense.
Thus effectivity cannot exclude the bad round-trip directions by a formal
finite-rank argument.

No RH or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. Correct Künneth--character diagram

Let \(X\) be the smooth compact logarithmic test space, \(X_0\) its
two-Tate-moment kernel, and let
\[
 \widetilde g(t)=\overline{g(-t)}.                       \tag{1.1}
\]
Define the linear correlation map on the projective tensor product
\[
 \kappa:X\widehat\otimes_\pi\overline X\longrightarrow
 \mathcal S(\mathbb R),\qquad
 \kappa(f\otimes\overline g)=f*\widetilde g.             \tag{1.2}
\]
Row C supplies a continuous linear character
\[
 \ell:\mathcal S(\mathbb R)\longrightarrow\mathbb C.    \tag{1.3}
\]
The Weil form is
\[
 \boxed{
 B_{\rm nuc}(f,g)=\ell\!\left(\kappa
 (f\otimes\overline g)\right).}                          \tag{1.4}
\]
Both sides are linear in \(f\) and conjugate-linear in \(g\).

The round-trip state realization is a linear map
\[
 R:X_0\longrightarrow\mathcal P^0,\qquad
 Rf=(p(f),z(f)),                                         \tag{1.5}
\]
and D.86 proves
\[
 \boxed{
 \langle\mathcal QRf,J\mathcal QRg\rangle
 =-4\ell\!\left(\kappa(f\otimes\overline g)\right).}     \tag{1.6}
\]
Thus the two constructions compare as sesquilinear forms:
\[
 R^*\mathcal Q^*J\mathcal QR=-4\,\kappa^*\ell.           \tag{1.7}
\]

The two Tate moments belong to \(f\) and \(g\) separately.  Their
correlation has moments
\[
 M_\pm(f*\widetilde g)=M_\pm(f)\,
 \overline{M_\pm(g)},                                    \tag{1.8}
\]
up to the fixed reflection convention.  Hence \(f,g\in X_0\) makes the
correlation primitive, but it does not turn the correlation into the
source variable of (1.5).

## 2. What the mixed periodic cotangent represents

At finite depth the one-ruling real cotangent frames are
\[
 E_p=\mathbb R\{e_i\}_{i<d},\qquad
 E_q=\mathbb R\{e'_j\}_{j<e}.                            \tag{2.1}
\]
The regular mixed moduli has full cotangent
\[
 E_p\otimes E_q=\mathbb R\{e_i\boxtimes e'_j\}_{i,j},    \tag{2.2}
\]
not only the rank-one coefficient locus.  A chosen one-ruling analytic
realization \(e_i\mapsto f_i\), \(e'_j\mapsto\widetilde g_j\) gives the
linear map
\[
 e_i\boxtimes e'_j
 \longmapsto f_i\otimes\widetilde g_j
 \xrightarrow{\kappa}f_i*\widetilde g_j
 \xrightarrow{\ell}B_{\rm nuc}(f_i,g_j).                \tag{2.3}
\]
This is the correctly typed use of the Cartesian extremal-pair basis.

Tropical pure tensors have coefficient matrices \(u_i+v_j\), and finite
maxima generate arbitrary coefficient matrices.  After taking the regular
cotangent, all entries in (2.2) vary independently.  There is therefore no
rank-one constraint on the linearized mixed source.

## 3. Polarized transverse defect on decomposable tensors

Use \(s=1\) and the sharply normalized Hilbert space from D.89.  Its trace
defect is
\[
 \mathcal D_1(F,G)
 ={\pi\over2}\left(\langle F,G\rangle
 +\langle uF,uG\rangle\right)
 -\langle\mathcal AF,\mathcal AG\rangle,\qquad u=x-y.   \tag{3.1}
\]
For decomposable tensors
\[
 F_{12}=f_1\otimes h_2,\qquad F_{34}=f_3\otimes h_4,     \tag{3.2}
\]
direct expansion gives
\[
\begin{aligned}
 \langle uF_{12},uF_{34}\rangle
={}&\langle xf_1,xf_3\rangle\langle h_2,h_4\rangle\\
 &+\langle f_1,f_3\rangle\langle yh_2,yh_4\rangle\\
 &-\langle xf_1,f_3\rangle\langle h_2,yh_4\rangle\\
 &-\langle f_1,xf_3\rangle\langle yh_2,h_4\rangle,       \tag{3.3}
\end{aligned}
\]
and
\[
 \langle\mathcal AF_{12},\mathcal AF_{34}\rangle
 =\langle f_1*h_2,f_3*h_4\rangle.                        \tag{3.4}
\]
Equations (3.1)--(3.4) are the complete polarized defect.  They are
sesquilinear in the tensor variables \(F_{12},F_{34}\), hence four-linear
in the original one-ruling inputs.

For \(h=\widetilde g\), put
\[
 N_f=\|f\|^2,\quad m_f=\langle xf,f\rangle,\quad
 Q_f=\|xf\|^2                                             \tag{3.5}
\]
and similarly for \(h\).  On a decomposable diagonal,
\[
\begin{aligned}
 \|f\otimes h\|_{\perp,1}^2
 =N_fN_h+Q_fN_h+N_fQ_h-2m_fm_h.                         \tag{3.6}
\end{aligned}
\]
Reflection changes the sign of the first moment of \(g\), as prescribed by
(1.1), but does not alter the homogeneity conclusion.

## 4. Homogeneity obstruction to a Schur identification

Under \(f\mapsto\lambda f\),
\[
 f\otimes\widetilde f\longmapsto
 |\lambda|^2(f\otimes\widetilde f).                      \tag{4.1}
\]
Therefore
\[
 \mathcal D_1(f\otimes\widetilde f,
              f\otimes\widetilde f)
 \longmapsto|\lambda|^4\mathcal D_1(
              f\otimes\widetilde f,f\otimes\widetilde f).
                                                                  \tag{4.2}
\]
In contrast,
\[
 B_{\rm nuc}(\lambda f,\lambda f)
 =|\lambda|^2B_{\rm nuc}(f,f),                           \tag{4.3}
\]
and the positive Schur tower satisfies
\[
 \sum_{j\ge1}\|K_jz(\lambda f)\|^2
 =|\lambda|^2\sum_{j\ge1}\|K_jz(f)\|^2.                 \tag{4.4}
\]

> **Proposition 4.1 (homogeneity no-go).**  No fixed linear compression
> \(C\) of the transverse residual can satisfy
> \[
> \|C(I-\mathcal A^\dagger\mathcal A)
> (f\otimes\widetilde f)\|^2
> =\sum_{j\ge1}\|K_jz(f)\|^2
> \]
> for every scalar multiple of every nonzero \(f\), unless both sides
> vanish identically.

Normalizing \(f\otimes\widetilde f\) by \(\|f\|\) would repair degree, but
it is nonlinear at zero, fails additivity, and has no sesquilinear
polarization.  Taking a Hessian at a chosen vacuum also produces a
quadratic form, but it depends on that vacuum; the coefficient unit is not
an \(L^2\) primitive vacuum.

## 5. Kernel invisibility of the trace defect

The coisometry of D.89 gives
\[
 \mathcal K_s=\ker\mathcal A\widehat\oplus
 \mathrm{Ran}\,\mathcal A^\dagger,\qquad
 I-\mathcal A^\dagger\mathcal A=P_{\ker\mathcal A}.      \tag{5.1}
\]
Every row-C functional on the Künneth tensor factors through
\(\mathcal A\).  Hence
\[
 \ell\mathcal A P_{\ker\mathcal A}=0.                    \tag{5.2}
\]
The positive transverse defect is precisely the norm on this invisible
kernel.

Consequently no compression of the defect which remains compatible with
the existing row-C character can reproduce a nonzero part of
\(B_{\rm nuc}\), including its Schur channel.  A functional nonzero on
\(\ker\mathcal A\) would be a new character.  Adding it in one parity
changes the exact prime-power--Gamma formula; adding it in both parities
cancels and supplies no sign.

The elementary \(2\times2\) tensor already exhibits this.  Addition sends
\[
 \begin{pmatrix}0&1\\-1&0\end{pmatrix}\longmapsto0,       \tag{5.3}
\]
while the tensor has nonzero Hilbert and transverse energy.  No
postcomposition of addition can see (5.3).

## 6. Density of the actual periodic extremals

For \(N>p\), the Connes--Consani extremals are
\[
 \phi_{a,b}(x)=\max\{-a(x-1),\,b(x-p)\},\qquad
 b=\left\lfloor{N-a\over p}\right\rfloor.                \tag{6.1}
\]
Conversely, every pair of positive integers \(a,b\) occurs by taking
\(N=a+pb\).  The hinge point is
\[
 x_{a,b}={a+bp\over a+b}.                                \tag{6.2}
\]
Writing \(r=a/b\),
\[
 x_{a,b}={r+p\over r+1}.                                 \tag{6.3}
\]
Positive rational \(r\) are dense in \((0,\infty)\), and (6.3) is a
homeomorphism from that interval to \((1,p)\) with reversed orientation.
Thus the hinge points of the actual extremals are dense in \((1,p)\).

After real cotangent linearization, scalar multiples and differences of
the hinge functions generate continuous piecewise-linear functions with
knots in this dense set, together with the affine and constant parts.
Such functions are uniformly dense in \(C([1,p])\) and dense in
\(L^2([1,p])\).  Bloch integration of all unitary local systems transports
this to a dense subspace of the logarithmic regular representation.
Tensor products are dense in the projective nuclear source and in the
corresponding Hilbert Künneth completion.

Hence no closed proper analytic subspace is forced merely by using the
published extremals at all depths.  The original nonlinear effective cone
is smaller, but passing to the primitive vector space and polarizing
requires signed differences; its real linear span has the density just
proved.

## 7. Correct scope of the transverse construction

The transverse trace theorem remains a genuine construction:
\[
 \mathcal A:
 \mathcal S(\mathbb R^2)\to\mathcal S(\mathbb R)
\]
is nuclear-continuous and has the conormal Hilbert coisometry of D.89--D.90.
Its proper row-D use is the linear factorization (1.4), not the iterated
quadratic composite
\[
 F\longmapsto h=\mathcal AF
 \longmapsto B_{\rm nuc}(h,h).                           \tag{7.1}
\]
The latter is mathematically defined on suitable domains but is not the
Weil Künneth pairing and has the wrong homogeneity on decomposable
diagonals.

## 8. Conclusion

The correctly typed comparison is (1.6): the round-trip Krein Gram and the
linear row-C character of Künneth correlation are the same polarized
quadratic form.  The conormal trace defect is an orthogonal kernel energy,
invisible to that character.  On diagonal tensors it is quartic and cannot
be the quadratic Schur tower.

The all-depth extremal realization is dense after real group completion,
so it does not exclude the positive Halmos graph by finite-dimensional
effectivity.  A successful continuation must construct a new **linear**
one-ruling preparation or duality whose squared norm is quadratic in the
test and whose polarization equals (1.6); a positive norm on the quadratic
Künneth diagonal cannot do this.

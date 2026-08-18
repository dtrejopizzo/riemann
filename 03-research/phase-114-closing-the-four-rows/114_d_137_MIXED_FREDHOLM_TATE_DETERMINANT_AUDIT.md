# D.137 — Mixed Fredholm--Tate determinant from the exact factorization

## Verdict

The exact factorization of D.134 produces two distinct determinant-type
objects, and separating them resolves the existence question.

First, there is a canonical **virtual coherent determinant line** on the
two-Tate primitive test space.  If \(X_T\) denotes the complete positive
reference feature (Gamma screw plus all antisymmetric prime-power channels)
and \(Y_T\) the complete positive load feature (the \(\beta\)-line, the
resolvent kernel, and all symmetric prime-power channels), then

\[
 B_{\rm nuc}(f,g)=\langle Y_Tf,Y_Tg\rangle
                  -\langle X_Tf,X_Tg\rangle.            \tag{0.1}
\]

The based metrized line

\[
 \lambda_{\rm mix}(f)=\operatorname {Exp}(Y_Tf)
             \otimes\operatorname {Exp}(X_Tf)^{-1}     \tag{0.2}
\]

has exact second metric cross-effect \(B_{\rm nuc}\).  It exists without a
sign assumption and without a Schatten estimate.

Second, the Birman--Schwinger defect

\[
 F_T=I-A_T^*A_T,
 \qquad A_T=Y_T(X_T^*X_T)^{-1/2},                      \tag{0.3}
\]

is Fredholm because \(A_T\) is compact.  Therefore its Fredholm determinant
line \(\operatorname {Det}(F_T)\) exists even though \(A_T^*A_T\) is in no
finite Schatten class.  What does **not** exist canonically is a scalar
Fredholm product, a Quillen product metric, or the usual restricted-Tate
determinant gerbe: all finite-order regularized determinant series diverge.
The Fredholm line records finite kernel and cokernel data, not the whole
quadratic form (0.1).

The mixed line (0.2) is always a legitimate metrized virtual line, but its
effectivity/positive-curvature assertion is exactly row D:

\[
 \boxed{
 -B_{\rm nuc}^{\rm prim}\geq0
 \Longleftrightarrow I-A_T^*A_T\geq0
 \Longleftrightarrow\|A_T\|\leq1.}                    \tag{0.4}
\]

Equivalently, a positive Hilbert feature whose Gram form is
\(-B_{\rm nuc}^{\rm prim}\) exists if and only if (0.4) holds.  Neither the
Fredholm determinant line nor its orientation supplies this positivity:
they see invertibility and spectral-flow parity, whereas D requires absence
of every negative eigenvalue.

All prime powers, the full Gamma place, both Tate jets and directed support
compatibility are included below.  No RH or sign of \(B_{\rm nuc}\) is
used, and the paper is not modified.

## 1. Identification of the two jets with the A--B--C moments

Let \(f\in C_c^\infty(\mathbb R_+^\times)\) and use the central logarithmic
unitary

\[
 (\mathcal Uf)(t)=F(t)=e^{t/2}f(e^t).                  \tag{1.1}
\]

With \(d^*x=dx/x\) and
\(\widehat f(s)=\int_0^\infty f(x)x^s\,d^*x\), direct substitution gives

\[
\begin{aligned}
 M_-(F)&:=\int_{\mathbb R}e^{-t/2}F(t)\,dt=\widehat f(0),\\
 M_+(F)&:=\int_{\mathbb R}e^{ t/2}F(t)\,dt=\widehat f(1).             \tag{1.2}
\end{aligned}
\]

These are exactly the two degree characters of the ruling classes in A,
the two Tate characters transported by the normalized Witt
correspondences in B, and the two polar characters removed from the even
part of the nuclear trace in C.  This is an equality of functionals, not a
dimension count.  If

\[
 \widehat F(\zeta)=\int_{\mathbb R}F(t)e^{-i\zeta t}\,dt,
\]

then also

\[
 M_+(F)=\widehat F(i/2),\qquad
 M_-(F)=\widehat F(-i/2).                              \tag{1.3}
\]

Thus the two jets at the Tate points are precisely the two primitive
moments of A--B--C, and

\[
 \mathcal U(\mathcal T^0)
 =\mathcal P:=\ker M_-\cap\ker M_+.                    \tag{1.4}
\]

Translations carry the same characters:

\[
 M_\pm(S_aF)=e^{\pm a/2}M_\pm(F),\qquad
 (S_aF)(t)=F(t-a).                                    \tag{1.5}
\]

Consequently this identification is compatible with every normalized
Frobenius translation \(a=k\log p\), not merely with the two endpoint
values.

## 2. The exact feature object and the A--B--C pullback

Let \(I_T=[-T,T]\), extend functions by zero, and put

\[
 \mathcal P_T=\ker M_+\cap\ker M_-,
 \qquad M_\pm(F)=\int_{-T}^{T}e^{\pm t/2}F(t)\,dt.      \tag{2.1}
\]

For every active \(n=p^k\), set

\[
 a_n=k\log p,\qquad
 w_n={\log p\over p^{k/2}}={\Lambda(p^k)\over\sqrt{p^k}}, \tag{2.2}
\]

and on \([-T,T-a_n]\)

\[
 J_{n,\pm}F(t)={F(t+a_n)\pm F(t)\over\sqrt2}.          \tag{2.3}
\]

The Gamma screw density and difference map are

\[
 \gamma_{5/4}(r)={e^{-5r/2}\over1-e^{-2r}},
 \qquad
 (D_\infty F)(r,t)=\sqrt{\gamma_{5/4}(r)}
       (\widetilde F(t)-\widetilde F(t-r)).             \tag{2.4}
\]

Let \(Q_{1/2}\) be the full-line Fourier multiplier
\((\tau^2+1/4)^{-1/2}\), applied to the zero extension.  Finally put

\[
 \beta=\log\pi-\psi(5/4)>0.                            \tag{2.5}
\]

Define the two Hilbert feature maps

\[
\begin{aligned}
 X_TF&=\left(D_\infty F,
       (\sqrt{w_n}J_{n,-}F)_{p^k\leq e^{2T}}\right),\\
 Y_TF&=\left(\sqrt\beta F,Q_{1/2}F,
       (\sqrt{w_n}J_{n,+}F)_{p^k\leq e^{2T}}\right).  \tag{2.6}
\end{aligned}
\]

Their target is a finite prime-power sum of ordinary Hilbert channels,
together with the continuous Gamma channel.  D.134 proves, by the digamma
integral, Tate--Chebyshev shorting and the identity
\(J_+^*J_+-J_-^*J_-=S_{a_n}+S_{-a_n}\), that

\[
 \boxed{
 B_{\rm nuc}(F,G)=\langle Y_TF,Y_TG\rangle
                  -\langle X_TF,X_TG\rangle
 \quad(F,G\in\mathcal P_T).}                           \tag{2.7}
\]

Here is the term-by-term proof of the pullback, included to make clear that
no Euler or archimedean summand has been suppressed.  For every \(n=p^k\),

\[
\begin{aligned}
 &\langle J_{n,+}F,J_{n,+}G\rangle
 -\langle J_{n,-}F,J_{n,-}G\rangle\\
 &\hspace{18mm}=
 \langle F,S_{a_n}G\rangle+\langle S_{a_n}F,G\rangle. \tag{2.8}
\end{aligned}
\]

Multiplication by \(w_n=\Lambda(n)/\sqrt n\) is exactly the degree of the
derived A--B contact times the central orbit depth of B--C.  If \(n\) has
two different prime factors, the reduced contact and \(\Lambda(n)\) both
vanish.  Hence the sum of (2.8) over the displayed channels is exactly the
complete finite-place part of C, including every \(p^k\).

At infinity, the digamma identity gives

\[
 \|D_\infty F\|^2
 ={1\over2\pi}\int_{\mathbb R}
 \bigl(\operatorname {Re}\psi(5/4+i\tau/2)-\psi(5/4)\bigr)
 |\widehat F(\tau)|^2\,d\tau,                         \tag{2.9}
\]

while

\[
 \|Q_{1/2}F\|^2
 ={1\over2\pi}\int_{\mathbb R}{|\widehat F(\tau)|^2
 \over\tau^2+1/4}\,d\tau.                            \tag{2.10}
\]

The exact Tate--Chebyshev identity on (1.4) changes the continuous
Chebyshev main term into (2.10), and its finite part is
\(\beta\|F\|^2\).  Thus (2.9), (2.10), and the \(\beta\)-channel are the
complete Gamma/Poisson contribution of C.  Combining them with (2.8)
proves (2.7) by polarization.

Thus the Krein feature

\[
 Z_TF=(Y_TF,X_TF),\qquad
 J=I_{\mathcal Y_T}\oplus(-I_{\mathcal X_T})          \tag{2.11}
\]

satisfies

\[
 \boxed{Z_T^*JZ_T=B_{\rm nuc}\big|_{\mathcal P_T}.}   \tag{2.12}
\]

This is defined before asking whether the pulled-back Krein metric is
positive or negative.

## 3. The virtual coherent determinant and its cross-effect

For a complex Hilbert space \(H\), let \(\operatorname {Exp}_H(v)\) denote
the based coherent line with distinguished vector \(e_v\) and metric

\[
 \|e_v\|=\exp\left({1\over2}\|v\|^2\right).            \tag{3.1}
\]

Its multiplication carries the standard Heisenberg phase
\(\exp(\tfrac i2\operatorname {Im}\langle v,w\rangle)\).  Bilinearity of
the phase gives the associativity cocycle.  Define

\[
 \lambda_{\rm mix,T}(f)
 =\operatorname {Exp}_{\mathcal Y_T}(Y_Tf)
  \otimes
  \operatorname {Exp}_{\mathcal X_T}(X_Tf)^{-1}.       \tag{3.2}
\]

Then

\[
 \log\|e_f\|={1\over2}
  \left(\|Y_Tf\|^2-\|X_Tf\|^2\right)
 ={1\over2}B_{\rm nuc}(f,f).                           \tag{3.3}
\]

The second cross-effect line

\[
 \delta^2\lambda(f,g)=\lambda(f+g)\otimes\lambda(f)^{-1}
 \otimes\lambda(g)^{-1}\otimes\lambda(0)             \tag{3.4}
\]

therefore has

\[
 \boxed{
 \log\|\delta^2e(f,g)\|=\operatorname {Re}B_{\rm nuc}(f,g),} \tag{3.5}
\]

while the Heisenberg phase in (3.1) recovers
\(\operatorname {Im}B_{\rm nuc}(f,g)\).  Hence (3.2), not a formal
Fredholm product, is the object whose complete Hermitian second
cross-effect is \(B_{\rm nuc}\).

This construction is a Picard/Tate determinant biextension: a difference
of two coherent Hilbert determinant lines.  It is not an assertion that
the virtual Krein space has a positive Hilbert completion.

## 4. Shorting the two Tate jets

On the fixed window the moment Gram matrix is

\[
 \mathsf G_T=\begin{pmatrix}2\sinh T&2T\\2T&2\sinh T\end{pmatrix}>0. \tag{4.1}
\]

If \(V_T(a,b)=ae^{-t/2}+be^{t/2}\), the canonical projection is

\[
 P_T=I-V_T\mathsf G_T^{-1}V_T^*.                       \tag{4.2}
\]

The actual mixed line on all of \(L^2(I_T)\) is obtained by replacing
\(X_T,Y_T\) with \(X_TP_T,Y_TP_T\).  On \(\mathcal P_T\), this is (3.2)
literally.  Thus the polar plane is removed by a proved rank-two shorting,
not by declaring its determinant contribution zero.

Under the unitary (1.1), \(V_T^*F=(M_-(F),M_+(F))\).  Therefore this
shorting is exactly the pullback of the two ruling/polar moments of A--B--C;
there is no second, auxiliary notion of primitivity in the determinant
construction.

The construction remains infinite-rank after this shorting.  Codimension
two does not alter compactness, Schatten failure or the feature identity.

## 5. The Fredholm defect object

Let

\[
 R_T=X_T^*X_T                                             \tag{5.1}
\]

be the positive reference form on \(\mathcal P_T\).  The zero-extension
Gamma form has compact form-domain embedding and trivial kernel, so
\(R_T\geq c_TI\), \(c_T>0\), and \(R_T^{-1/2}\) is compact.  Define

\[
 A_T=Y_TR_T^{-1/2},\qquad
 K_T=A_T^*A_T,
 \qquad F_T=I-K_T.                                     \tag{5.2}
\]

The load \(Y_T\) is bounded, hence \(A_T\) and \(K_T\) are compact.  The
form identity is

\[
 \boxed{
 -B_{\rm nuc}^{\rm prim}
 =R_T^{1/2}F_TR_T^{1/2}.}                              \tag{5.3}
\]

For a symmetric Fredholm presentation one may equivalently use

\[
 \mathscr D_T=
 \begin{pmatrix}I&-A_T^*\\-A_T&I\end{pmatrix}.        \tag{5.4}
\]

It is identity plus compact and its Schur complement is \(F_T\).

Let \(\mathsf{Fred}_0\) be the category of index-zero Fredholm operators
on separable Hilbert spaces with continuous Fredholm diagrams.  The usual
determinant functor assigns

\[
 \operatorname {Det}(F_T)
 =\det\ker F_T\otimes(\det\operatorname {coker}F_T)^{-1}. \tag{5.5}
\]

Both vector spaces in (5.5) are finite-dimensional.  Thus this line exists
for every \(T\), including a value at which an eigenvalue of \(K_T\) is
one.  No trace ideal is required for (5.5).

## 6. What non-Schatten compactness prevents

D.134 proves the quantitative lower bound

\[
 \lambda_j(K_T)\geq{c_T'\over\log(2+j)}                \tag{6.1}
\]

for a positive constant depending on the window.  Consequently

\[
 K_T\notin\mathcal S_p\qquad(0<p<\infty).              \tag{6.2}
\]

The implications are exact:

* \(\det(I-K_T)\) is not an ordinary Fredholm determinant;
* no finite-order regularized determinant \(\det_p(I-K_T)\) is defined;
* the formal series
  \(-\sum_{m\geq1}\operatorname {Tr}(K_T^m)/m\) has no finite first
  power at which all subsequent traces become defined; and
* the usual restricted linear/Tate central extension, which requires a
  trace-class determinant comparison (or a Hilbert--Schmidt polarization
  for its standard gerbe), is not furnished by \(A_T\).

Thus (5.5) is a Fredholm **line**, defined from kernel and cokernel.  It
does not carry a canonical eigenvalue-product section or Quillen product
metric.  The nuclear topology of row C does not change this conclusion:
``nuclear'' there describes the test-function character and its summable
Poisson realization, whereas (6.2) is a Hilbert-operator ideal statement
  about the mixed comparison.

Even in a hypothetical trace-class regularization, the scalar
\(\log\det(I-K_T)\) would be nonlinear in \(K_T\) and would not equal the
quadratic potential (3.3).  The two determinant objects answer different
questions.

## 7. Compatibility as the support window varies

For a fixed compactly supported primitive test \(f\), enlarging the window
does not change (2.7):

* the zero-extended Gamma difference is the same;
* a newly listed prime power with \(\log p^k\) larger than the support
  diameter has zero \(J_+^*J_+-J_-^*J_-\) contribution;
* the full-line resolvent feature \(Q_{1/2}f\) is unchanged; and
* the two Tate moments are global and remain zero.

Therefore the Gram metric and the coherent line (3.2) have canonical
directed identifications

\[
 \lambda_{\rm mix,T'}(f)\simeq\lambda_{\rm mix,T}(f)
 \qquad(T'\geq T\text{ containing }\operatorname {supp}f). \tag{7.1}
\]

This directed compatibility applies to the **difference** of the two
feature metrics.  It does not make the positive feature maps separately
norm-continuous.  At a prime-power threshold the new \(J_+\) and \(J_-\)
channels have equal norm on old compact supports and hence cancel in
(2.7), but each channel is nonzero.  More sharply, after the overlap layer
is born, normalized vectors supported on its two endpoint pieces give an
off-diagonal translation block of operator norm one, whereas the block is
zero at the threshold.  Thus the contact is not operator-norm continuous
at birth.

Consequently each \(F_T=I-K_T\) has the Fredholm line (5.5), and on an open
cell containing no threshold the usual fixed-domain transport gives a
local determinant-line family.  The present construction does **not**
canonically glue those local Fredholm lines across every threshold.  Such a
gluing would require a form-domain blow-up or another specified
stabilization of the newly born infinite-dimensional annular channel.

The coherent mixed line avoids this problem because it is defined by the
cross-effect (2.7), whose new \(J_+\) and \(J_-\) contributions cancel for
tests of smaller support.  The Fredholm comparison depends on the separate
positive decomposition and therefore carries strictly more threshold
data.  In particular, no global spectral-flow divisor is asserted here.

## 8. Metric positivity and effectivity

There are three successively stronger notions which must not be confused.

1. The line (3.2) has a positive numerical norm for every \(f\), simply
   because exponentials of real numbers are positive.  This is not Hodge
   positivity.
2. Its dual is semipositive/effective on primitive rays precisely when
   \(B_{\rm nuc}(f,f)\leq0\) for every primitive \(f\).
3. A positive Hilbert feature \(D_T\) satisfying

   \[
    -B_{\rm nuc}(f,g)=\langle D_Tf,D_Tg\rangle          \tag{8.1}
   \]

   exists precisely when the Hermitian form on the left is nonnegative.

Using (5.3), these conditions give

\[
\begin{aligned}
 -B_{\rm nuc}^{\rm prim}\geq0
 &\Longleftrightarrow F_T\geq0\\
 &\Longleftrightarrow K_T\leq I\\
 &\Longleftrightarrow\|A_T\|\leq1.                    \tag{8.2}
\end{aligned}
\]

If (8.2) holds, one may take

\[
 D_T=F_T^{1/2}R_T^{1/2}.                               \tag{8.3}
\]

Conversely, (8.1) forces nonnegativity and hence (8.2).  Therefore a
positive/effective metric cannot be extracted independently from the
Fredholm or coherent determinant data: its existence is exactly D.

## 9. Why determinant orientation is insufficient

The determinant line detects the finite-dimensional kernel at
\(\lambda(K_T)=1\).  Away from crossings, a real orientation can at most
record the parity of the number of negative eigenvalues of \(F_T\).  Row D
requires that number to be zero.

Already in dimension two,

\[
 F_+=\begin{pmatrix}2&0\\0&2\end{pmatrix},
 \qquad
 F_-=\begin{pmatrix}-2&0\\0&-2\end{pmatrix}            \tag{9.1}
\]

have the same determinant \(4\), the same index zero and the same positive
determinant orientation, but \(F_+\geq0\) while \(F_-<0\).  Adding an
infinite identity summand makes them compact perturbations of the identity
without changing this conclusion.

Thus neither an oriented Fredholm line, a vanishing-free determinant
section nor even spectral-flow parity proves effectivity.  A positive cone
or contraction theorem is additional information, and by (8.2) it is
exactly the missing row-D assertion.

## 10. Exact categorical status

The mixed object naturally lives in the product of two categories:

\[
 \mathsf{Pic}^{\rm coh}_{\rm Tate}
 \times\mathsf{Fred}_0.                                \tag{10.1}
\]

The first factor contains the virtual coherent line (3.2) and remembers
the complete Hermitian cross-effect.  The second contains (5.5) and
remembers finite-dimensional eigenvalue-one crossings.  The comparison
operator lies only in the compact ideal, not in a nuclear/Schatten
determinant ideal.

### 10.1. The exact extra datum a global category would have to supply

Because (R_T=X_T^*X_T\geq c_TI\), the map (X_T) is injective.  There is
therefore an algebraic comparison on its range,

\[
 C_T^0:X_T(\mathcal P_T)\longrightarrow\mathcal Y_T,
 \qquad C_T^0(X_TF)=Y_TF.                              \tag{10.2}
\]

The following statements are equivalent:

\[
\begin{array}{ll}
\text{(i)}&C_T^0\text{ extends to a contraction }
 \overline{X_T(\mathcal P_T)}\to\mathcal Y_T;\\
\text{(ii)}&\|Y_TF\|\leq\|X_TF\|\quad(F\in\mathcal P_T);\\
\text{(iii)}&-B_{\rm nuc}\big|_{\mathcal P_T}\geq0.
\end{array}                                             \tag{10.3}
\]

Indeed (i) implies (ii), (ii) and (2.7) imply (iii), and (iii) makes
(C_T^0) norm-decreasing, hence continuously extendible.  Thus the exact
additional categorical datum is not another determinant line or another
trace.  It is a support-compatible contractive natural transformation

\[
 C_T:\overline{X_T(\mathcal P_T)}\longrightarrow\mathcal Y_T,
 \qquad C_TX_T=Y_T,                                   \tag{10.4}
\]

compatible with the two Tate-character kernels, all Witt translations
(k\log p), the Gamma/Poisson channel, and the directed maps
(T\leq T'\).

A Tate or Ind-nuclear enhancement can prove D independently only if it
constructs (10.4) from its monoidal/positive structure and proves its
contractivity before invoking (B_{\rm nuc}\).  The nuclear Fr\'echet
topology alone supplies summability and traces but no order cone; the
Fredholm category supplies kernels, cokernels and spectral flow but no
contraction; and a Picard determinant supplies a line and curvature but no
Hilbert-module comparison.  A sufficient enhancement would be a
(C^*\)- or Hilbert-module-valued positive monoidal realization together
with a completely contractive transformation inducing (10.4) in every
window.

Defining (C_T^0) by (10.2) and then asserting that it is contractive is
not an independent construction: by (10.3) it is exactly row D.  Likewise,
quotienting by the positive spectral subspace of (B_{\rm nuc}) would put
the desired sign into the category.  This identifies precisely both the
needed datum and the non-circular acceptance test for any proposed global
Tate/Ind-nuclear solution.

To promote (10.1) to a Quillen determinant object with a scalar metric one
would need an additional source-defined renormalization cancelling the
universal \(1/\log j\) tail, compatible with every support inclusion and
prime threshold.  Choosing counterterms from the spectrum of \(K_T\) would
be noncanonical and could import the desired sign.

The object with the required second cross-effect already exists by (3.2).
What remains unavailable is not its line but a positive effectivity
structure on it.

## 11. Conclusion

The D.134 factorization gives the following exact answer:

\[
 \begin{array}{c|c|c}
 \text{object}&\text{exists?}&\text{information retained}\\ \hline
 \lambda_{\rm mix}&\text{yes}&B_{\rm nuc}\text{ as second cross-effect}\\
 \operatorname {Det}(I-K_T)&\text{yes}&\ker(I-K_T),\operatorname {coker}(I-K_T)\\
 \det(I-K_T)\text{ as scalar product}&\text{no}&K_T\notin\mathcal S_p\\
 \text{standard restricted-Tate gerbe}&\text{not canonically}&A_T\notin\mathcal S_p\\
 \text{positive Hilbert/effective metric}&\text{iff D}&\|A_T\|\leq1
 \end{array}
\]

All local and archimedean terms are internal to the feature maps, the two
jets are exactly shorted, and the construction is compatible under support
enlargement.  The determinant formalism does not supply an independent
positivity theorem; it isolates the missing datum as the contraction of the
mixed comparison operator.

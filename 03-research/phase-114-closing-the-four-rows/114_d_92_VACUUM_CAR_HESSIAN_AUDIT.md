# D.92 — Vacuum tangent, Krein CAR and the missing convex Hessian

## Status

D.91 restores the correct linear Künneth character.  This note tests
whether the unit object and the effective determinant of row A construct a
positive vacuum whose Hessian is the row-C form.

The formal tangent calculation works.  In
\[
 (1+\varepsilon f)\boxtimes
 (1+\overline\eta\,\widetilde g)
\]
the two linear terms are the two polar/Tate boundary directions, and the
mixed term is \(f\boxtimes\widetilde g\).  On the primitive tangent the
linear terms vanish under the completed character, while the mixed
derivative is exactly \(B_{\rm nuc}(f,g)\), including all prime powers and
Gamma.

The effective determinant of row A does not provide the needed Hessian.
At a fixed divisor its norm depends on extremal rank and fibre lengths, not
on the coefficient coordinates of the regular section cell.  Its
coefficient Hessian is therefore zero.  Varying divisor degrees gives the
hyperbolic degree form, not the Schwartz/contact form.

There is an exact algebraic Fock realization.  The full prime--Gamma
feature map of D.32 lands in a positive Hilbert space with a fundamental
symmetry.  Ordinary CAR vacuum gives the sum of the two feature Grams;
inserting the fundamental symmetry gives \(B_{\rm nuc}\).  The inserted
functional is a Krein/super functional and is not positive.  An
Osterwalder--Schrader reflection can make its reflected Gram positive only
after a source involution intertwining the fundamental symmetry is
constructed.  On the primitive source, existence of the required
reflection/polarization is equivalent to the missing contractive
factorization.

Thus the CAR route types the quadratic form correctly but does not create
its sign.  Defining a log-concave vacuum potential with Hessian
\(-B_{\rm nuc}\) would state row D rather than prove it.

No RH or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. Formal unit expansion

Let \(\mathbf1\) denote the coefficient unit and use formal dual numbers
\(\varepsilon^2=\eta^2=0\), retaining the mixed product
\(\varepsilon\overline\eta\).  Künneth multiplication gives
\[
\begin{aligned}
 (\mathbf1+\varepsilon f)\boxtimes
 (\mathbf1+\overline\eta\,\widetilde g)
 ={}&\mathbf1+\varepsilon(f\boxtimes\mathbf1)
 +\overline\eta(\mathbf1\boxtimes\widetilde g)\\
 &+\varepsilon\overline\eta
 (f\boxtimes\widetilde g).                              \tag{1.1}
\end{aligned}
\]
After addition pushforward,
\[
 \kappa(f\boxtimes\widetilde g)=f*\widetilde g.          \tag{1.2}
\]

The completed row-C character has two polar linear boundary functionals,
which in the central logarithmic normalization are \(M_-\) and \(M_+\).
Consequently, on \(f,g\in X_0=\ker M_-\cap\ker M_+\), the first
derivatives of the completed vacuum character vanish and
\[
 \boxed{
 {\partial^2\over\partial\varepsilon\partial\overline\eta}
 \ell\kappa\!\left[
 (\mathbf1+\varepsilon f)\boxtimes
 (\mathbf1+\overline\eta\,\widetilde g)\right]_{0}
 =B_{\rm nuc}(f,g).}                                    \tag{1.3}
\]

Using D.32, the mixed Hessian is explicitly
\[
\begin{aligned}
 B_{\rm nuc}(f,g)
 ={}&\sum_p(\log p)\sum_{k\ne0}p^{-|k|/2}
       \langle f,S_{k\log p}g\rangle\\
 &+m_0\langle f,g\rangle
 -\langle\partial_\infty f,\partial_\infty g\rangle.     \tag{1.4}
\end{aligned}
\]
Thus the formal vacuum expansion loses no \(p^k\) and no Gamma term.

Equation (1.3) is a tangent identity, not yet convexity or positivity.

## 2. Hessian of the row-A determinant

At fixed finite periodic depth, a regular mixed section is
\[
 F_c(x,y)=\max_{i,j}
 \{\phi_i(x)+\psi_j(y)+c_{ij}\}.                         \tag{2.1}
\]
Residuation identifies the regular cell with an open set in
\(\mathbb R^{de}\), and its cotangent frame is \(dc_{ij}\).  The intrinsic
determinant metric constructed in row A is
\[
 \|\omega_{p,q;r,s}\|
 =\exp\!\left(-(\log p)(\log q)p^{-r}q^{-s}de\right).    \tag{2.2}
\]
For fixed divisor and depth, \(d,e,p,q,r,s\) are constant throughout the
cell.  Therefore
\[
 {\partial\over\partial c_{ij}}\log\|\omega\|=0,\qquad
 {\partial^2\over\partial c_{ij}\partial c_{kl}}
 \log\|\omega\|=0.                                      \tag{2.3}
\]

The same is true of the spherical code determinant: its metric counts the
number of framed coordinates and does not vary with their values.  Thus
neither determinant has (1.4) as a coefficient Hessian.

Varying the divisor degrees instead gives
\[
 \log\|\lambda_{\rm int}(a,b)\|=-ab,                    \tag{2.4}
\]
whose Hessian is the fixed two-dimensional hyperbolic matrix.  There is no
constructed map from an arbitrary primitive Schwartz tangent \(f\) to
degree variations \((\delta a,\delta b)\) which pulls (2.4) back to the
infinite-rank prime--Gamma form (1.4).  The finite-rank obstruction of row A
rules out such a factorization for the full contact kernel.

Hence effective determinant convexity at the presently constructed level
is either zero in section coordinates or finite-rank in degree
coordinates.

## 3. Source-defined Krein one-particle space

At a fixed support window let the exact D.32 feature maps be
\[
\begin{aligned}
 \mathbf S f&=((\sqrt{\log p}\,A_pf)_p,\sqrt{m_0}f),\\
 \mathbf B f&=((\sqrt{\log p}\,f)_p,\partial_\infty f).
                                                                  \tag{3.1}
\end{aligned}
\]
Only primes active on the support are present; each \(A_p^*A_p\) contains
the full norm-convergent tower
\[
 A_p^*A_p=\sum_{k\in\mathbb Z}p^{-|k|/2}S_{k\log p}.     \tag{3.2}
\]
Put
\[
 \mathcal K_{\rm one}=\mathcal K_S\oplus\mathcal K_B,
 \qquad
 J_{\rm one}=\begin{pmatrix}I&0\\0&-I\end{pmatrix},
 \qquad
 Wf=(\mathbf Sf,\mathbf Bf).                             \tag{3.3}
\]
Then
\[
 \boxed{
 \langle Wf,J_{\rm one}Wg\rangle=B_{\rm nuc}(f,g).}      \tag{3.4}
\]
The cofinal value is the stabilized paired difference, exactly as in
D.32.

Let \({\rm CAR}(\mathcal K_{\rm one})\) be the ordinary CAR algebra over
the positive Hilbert direct sum, with Fock vacuum \(\Omega\).  For the
annihilation field \(a(x)\),
\[
 \langle\Omega,a(x)a(y)^*\Omega\rangle
 =\langle x,y\rangle.                                    \tag{3.5}
\]
Thus the ordinary vacuum produces
\[
 \langle\mathbf Sf,\mathbf Sg\rangle
 +\langle\mathbf Bf,\mathbf Bg\rangle,                   \tag{3.6}
\]
not (3.4).

Second quantization of \(J_{\rm one}\) gives a bounded self-adjoint unitary
\(\Gamma(J_{\rm one})\).  The signed two-point functional
\[
 \omega_J(a(Wf)a(Wg)^*)
 :=\langle\Omega,a(Wf)\Gamma(J_{\rm one})
 a(Wg)^*\Omega\rangle                                   \tag{3.7}
\]
has, with the equivalent standard placement of \(\Gamma(J_{\rm one})\),
the covariance
\[
 \omega_J(a(Wf)a(Wg)^*)=\langle Wf,J_{\rm one}Wg\rangle
 =B_{\rm nuc}(f,g).                                      \tag{3.8}
\]
This is an exact Krein/CAR realization of every \(p^k\) and Gamma.

It is not a positive state.  Positivity of a quasi-free CAR vacuum would
require its covariance operator to be positive (and, after normalization,
bounded by the identity).  The covariance \(J_{\rm one}\) has both signs.

## 4. Osterwalder--Schrader reflection gate

An OS construction would require an antilinear source involution
\(\Theta:X_0\to X_0\) and a positive-time subspace \(X_+\) such that
\[
 -B_{\rm nuc}(f,\Theta g)\quad(f,g\in X_+)               \tag{4.1}
\]
is positive semidefinite, together with covariance and gluing.

On the one-particle target, choosing the reflection
\(-J_{\rm one}\) makes the reflected ambient form positive:
\[
 -\langle x,J_{\rm one}(-J_{\rm one})y\rangle
 =\langle x,y\rangle.                                    \tag{4.2}
\]
But (4.2) descends to the source only if
\[
 W\Theta=-J_{\rm one}W.                                  \tag{4.3}
\]
Equation (4.3) says simultaneously
\[
 \mathbf S\Theta=-\mathbf S,\qquad
 \mathbf B\Theta=\mathbf B.                              \tag{4.4}
\]
No such involution is supplied by periodic Yoneda, Tate reflection, or
the half-density.  Tate reflection exchanges orientations and gives the
Paugam/Krein swap, not (4.4).

More generally, a source OS projection whose reconstructed positive norm
implies \(B_{\rm nuc}(f,f)\le0\) on all of \(X_0\) is exactly a negative
polarization of the image \(W(X_0)\).  In the round-trip coordinates this
is equivalent to
\[
 \|C^{1/2}z(f)\|\le\|r_0(f)\|,                           \tag{4.5}
\]
the Douglas factorization isolated in D.86.  Selecting it from the sign of
\(J_{\rm one}\) would be circular.

## 5. Vacuum Gram audit

The local contact functional satisfies
\[
 \ell(1)=0,\qquad
 \ell(\delta_p)=\ell(\delta_{p^2})=\log p.               \tag{5.1}
\]
On \(\{1,\delta_p\}\), its Gram is
\[
 \begin{pmatrix}
 0&\log p\\
 \log p&\log p
 \end{pmatrix},\qquad
 \det=-(\log p)^2.                                      \tag{5.2}
\]
Hence it cannot be the two-point function of a positive unital vacuum.
This does not by itself refute **conditional** negativity on the primitive
tangent: the unit and the two polar directions are removed there.  It
does prove that the positive vacuum cannot be obtained by simply declaring
the row-C contact functional to be a CAR state before taking the primitive
quotient.

For actual primitive analytic tests, the complete Gram is (1.4), not just
(5.2).  Asking that \(-B_{\rm nuc}\) be positive on every finite primitive
Gram matrix is precisely row D.  Thus a positive quasi-free vacuum with
two-point function \(-B_{\rm nuc}\) exists exactly after the desired
conditional positivity has been proved.

## 6. Convexity formulation and circularity test

Suppose a source-defined effective volume \(\mathcal V\) existed on a
neighbourhood of the vacuum with
\[
 {\rm Hess}_0\log\mathcal V(f,\overline g)
 =-B_{\rm nuc}(f,g)\qquad(f,g\in X_0).                   \tag{6.1}
\]
Log-concavity of \(\mathcal V\) would prove row D.  This is a legitimate
target theorem.

The current row-A determinant cannot be this \(\mathcal V\) by (2.3).
Defining
\[
 \mathcal V_{\rm formal}(f)
 =\exp\!\left(-{1\over2}B_{\rm nuc}(f,f)\right)          \tag{6.2}
\]
forces (6.1) by definition and uses the desired form as its own volume
potential.  Likewise, choosing a CAR covariance from the negative spectral
part of \(B_{\rm nuc}\) assumes its sign.  Both are excluded.

Any new volume must therefore be constructed from actual effective section
geometry and then compared, term by term, with (1.4).  Its nontrivial
coefficient Hessian and its log-concavity are both absent from the current
determinant package.

## 7. Conclusion

The unit expansion identifies the correct mixed Hessian and the
source-defined Krein CAR realizes it with every prime power and Gamma.
The ordinary positive CAR vacuum computes the feature sum, while the
fundamental-symmetry insertion computes the required difference and loses
positivity.

Row A's existing effective determinant has zero Hessian in section
coordinates, so it cannot supply the missing OS vacuum.  Constructing a
source involution satisfying (4.3), or a genuinely log-concave effective
volume satisfying (6.1), is a precise new route; neither follows from the
current Yoneda unit or determinant.

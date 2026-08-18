# D.88 — Bloch–Floquet landing and the global character obstruction

## Status

D.87 shows that a single periodic character cannot land nontrivially in
the regular logarithmic Hilbert representation.  This note performs the
correct repair: it adds every unitary local system on \(C_p\) and takes
their direct integral.  For one prime, the resulting Bloch–Floquet
transform is unitary, intertwines deck translation with \(U_p\), preserves
the ordered-extremal norm, and gives a bounded normed landing to the
round-trip state.  Conjugating the full preparation Gram by this unitary
still gives exactly \(-4B_{\rm nuc}\).  The displayed local Poisson
multiplier contains all powers \(p^k\), and the Bloch-decomposed oscillator
contains the complete Gamma factor.

The one-prime no-eigenvector obstruction is therefore not the final
obstruction.

The first obstruction after this repair occurs at mixed Künneth.  A pair
of periodic fibres lands naturally in \(L^2(\mathbb R^2)\).  Row C and the
round-trip colligation use one logarithmic variable.  The required
pushforward along addition is convolution, equivalently restriction of a
two-variable Fourier transform to the diagonal.  It is unbounded from
\(L^2(\mathbb R^2)\) to \(L^2(\mathbb R)\).  The ordered-frame norm and
the Gamma graph norm provide no transverse half-derivative which could
make that trace bounded.

The same obstruction appears globally.  The dual of
\(\log\mathbb Q_{>0}\simeq\bigoplus_p\mathbb Z\) is
\(\prod_pS^1\), but the row-C representation sees only the correlated
archimedean characters
\[
 \chi_\tau(p)=p^{-i\tau}.
\]
This one-parameter subgroup is dense and product-Haar null.  Restricting
the independent local-system direct integral to it is therefore not a
bounded Hilbert map.  A new global quotient with a source-derived
transverse trace norm is needed before the dagger comparison can be
formulated.

No RH or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. Fixed-prime Bloch–Floquet theorem

Fix \(p\), put \(L=\log p\), write \(\chi=e^{i\theta}\), and normalize Haar
measure on \(S^1\) as \(d\theta/(2\pi)\).  For
\(f\in C_c^\infty(\mathbb R)\), define

\[
 (\mathcal Z_Lf)(\theta,x)
 =\sum_{k\in\mathbb Z}f(x+kL)e^{ik\theta},
 \qquad 0\le x<L.                                        \tag{1.1}
\]

Parseval in the integer variable gives

\[
\begin{aligned}
 \int_0^L\int_0^{2\pi}
 |(\mathcal Z_Lf)(\theta,x)|^2{d\theta\over2\pi}\,dx
 &=\int_0^L\sum_{k\in\mathbb Z}|f(x+kL)|^2dx\\
 &=\|f\|_{L^2(\mathbb R)}^2.                             \tag{1.2}
\end{aligned}
\]

Conversely,

\[
 f(x+kL)=\int_0^{2\pi}
 (\mathcal Z_Lf)(\theta,x)e^{-ik\theta}{d\theta\over2\pi}.
                                                                  \tag{1.3}
\]

Thus (1.1) extends to a unitary

\[
 \boxed{
 \mathcal Z_L:L^2(\mathbb R)
 \xrightarrow{\sim}
 \int_{S^1}^{\oplus}L^2([0,L],\mathcal L_\chi)\,d\chi.}   \tag{1.4}
\]

Here \(\mathcal L_\chi\) denotes the unitary local system whose deck
holonomy is \(\chi\).  With the convention
\((S_Lf)(t)=f(t-L)\),

\[
 \mathcal Z_LS_L\mathcal Z_L^{-1}=M_\chi.                \tag{1.5}
\]

Equations (1.4)--(1.5) prove that integrating all monodromies repairs the
failed square D.87(3.2): a single fibre has generalized eigenvectors,
while their Haar integral is the regular representation.

## 2. Bloch extension of periodic extremals

Let \(E_{p,r}(a)\) be the finite real ordered-extremal cotangent frame of
row A, and let \(\mathscr H_{p,\chi}\) be the Hilbert sheaf of
square-integrable sections of the flat Hermitian line with holonomy
\(\chi\).  The extension is made after taking the intrinsic cotangent of
the actual section moduli: tensor its complexified frame with
\(\mathscr H_{p,\chi}\) and integrate.  At the Hilbert level,

\[
 \widetilde E_{p,r}(a)
 =\int_{S^1}^{\oplus}
 E_{p,r}(a)_\mathbb C\otimes
 L^2([0,L],\mathcal L_\chi)\,d\chi.                      \tag{2.1}
\]

This explicitly extends the Yoneda object used here: apply the intrinsic
cotangent/frame functor to each representable coefficient line and tensor
its spatial factor with \(\mathscr H_{p,\chi}\).  It does not assert a
scalar extension \(\mathbb R_{\max}\to\mathbb C\), and it does not
linearize max-plus addition a second time.  Principal translations act
trivially on coefficient differentials; unitary holonomy acts only on the
flat factor.

For two primes,

\[
\begin{aligned}
 \widetilde E_{p,r}(a)\widehat\otimes
 \widetilde E_{q,s}(b)
 \simeq
 \int_{S^1\times S^1}^{\oplus}
 &(E_{p,r}(a)\otimes E_{q,s}(b))_\mathbb C\\
 &\otimes H_{p,\chi}\otimes H_{q,\psi}\,d\chi\,d\psi .
                                                                  \tag{2.2}
\end{aligned}
\]

The ordered Cartesian extremal basis gives the original Künneth
isomorphism, and Fubini gives the local-system Künneth isomorphism.  Hence
(2.2) preserves norms exactly.

It is a Hilbert enhancement of the cotangent realization of enriched
Yoneda, not a new family of tropical divisors and not an identification
with raw bounded spherical sections.

## 3. Fixed-prime normed landing and its Gram

Tensoring \(\mathcal Z_L^{-1}\) with the identity of the finite extremal
frame gives a unitary covariant landing

\[
 \Lambda_p:\widetilde E_{p,r}(a)
 \xrightarrow{\sim}
 E_{p,r}(a)_\mathbb C\otimes L^2(\mathbb R).              \tag{3.1}
\]

At a fixed regularized window, apply the bounded primitive annihilator
\[
 \Pi_p=I-\frac{S_L+S_{-L}}{2\cosh(L/2)}
                                                                  \tag{3.2}
\]
and then the source realization and Halmos coordinate map
\[
 F\longmapsto(p(F),z(F)).
                                                                  \tag{3.3}
\]
The composite is a well-defined bounded, \(U_p\)-covariant landing to the
round-trip preparation space.  The Bloch step is unitary; \(\Pi_p\) is
bounded but is neither idempotent nor claimed to be isometric.  It kills
both Tate moments because
\[
 M_\pm(\Pi_pF)=0.                                        \tag{3.4}
\]

This settles existence of a bounded normed landing.  It does not settle existence
of a dagger-positive landing: the target metric required by row D is the
Krein grading \(J={\rm diag}(I,-I)\), not the positive Hilbert metric.

Bloch decomposition preserves the exact local character.  Put
\(r=p^{-1/2}\).  Since \(S_L\) is multiplication by \(\chi\),
\[
 A_p^*A_p
 =P_r(S_L)
 \longleftrightarrow
 P_r(\chi)
 =\sum_{k\in\mathbb Z}p^{-|k|/2}\chi^k.                 \tag{3.5}
\]
Thus every \(p^k\) is present before any sign is taken.

The Gamma oscillator commutes with \(S_L\), so it is decomposable under
\(\mathcal Z_L\).  In the quasiperiodic Fourier basis its frequencies are
\[
 \tau_{\theta,j}={\theta+2\pi j\over L},\qquad j\in\mathbb Z,
                                                                  \tag{3.6}
\]
and its finite-part multiplier is
\[
 m_\infty(\tau)=
 \log\pi-\mathrm{Re}\,\psi
 \left({1\over4}+{i\tau\over2}\right).                  \tag{3.7}
\]

For Bloch fields \(F=(F_\theta)\), \(G=(G_\theta)\), the fixed-prime plus
Gamma part of the preparation Gram is
\[
\boxed{
\begin{aligned}
 \langle\mathcal QF,J\mathcal QG\rangle
 =-4\int_{S^1}
 \Big\langle F_\theta,\big[
 &(\log p)(P_{p^{-1/2}}(e^{i\theta})-1)\\
 &+M_{\infty,p}(\theta)\big]G_\theta
 \Big\rangle\,{d\theta\over2\pi}.
\end{aligned}}                                           \tag{3.8}
\]

Here \(M_{\infty,p}(\theta)\) is diagonal with entries (3.7) at (3.6).
Equation (3.8) is exactly the \(p\)-power and Gamma part of
\(-4B_{\rm nuc}\).  It follows by conjugating the already source-defined
round-trip preparation with the unitary (1.4), so no sign is inserted.

For the complete Gram retain every prime \(q\):
\[
\boxed{
 \langle\mathcal QF,J\mathcal QG\rangle
 =-4\left[
 \sum_q(\log q)
 \langle F,(P_{q^{-1/2}}(S_{\log q})-I)G\rangle
 +\langle F,M_\infty G\rangle\right].}                  \tag{3.9}
\]
Every \(S_{\log q}\) commutes with \(S_L\), hence is decomposable in the
\(p\)-Bloch representation.  For \(q=p\) its fibre multiplier is the
scalar in (3.8); for \(q\ne p\) it is a non-scalar fibre translation.
Thus choosing one Bloch lattice loses no \(q^k\) and no Gamma term.

The positive target metric replaces the difference in (3.8) by the sum of
the two round-trip output norms.  It is positive but differs from
\(-4B_{\rm nuc}\) by twice the boundary energy.  Bloch–Floquet has repaired
descent, not the dagger inequality.

## 4. The mixed Künneth landing is unbounded

Under (1.4) in the two factors, (2.2) lands unitarily in
\[
 (E_p\otimes E_q)_\mathbb C\otimes L^2(\mathbb R^2).
                                                                  \tag{4.1}
\]
The row-C product of the two one-variable coefficient functions is
multiplicative convolution, which on the logarithmic line is the
addition pushforward
\[
 (\mathcal A F)(t)=\int_{\mathbb R}F(x,t-x)\,dx.          \tag{4.2}
\]
In Fourier variables,
\[
 \widehat{\mathcal AF}(\tau)=\widehat F(\tau,\tau).       \tag{4.3}
\]

Neither (4.2) nor (4.3) is bounded from \(L^2(\mathbb R^2)\) to
\(L^2(\mathbb R)\).  For an exact discrete model let
\[
 F_N(i,j)={1\over N}\mathbf1_{\{0,\ldots,N-1\}^2}(i,j).
                                                                  \tag{4.4}
\]
Then
\[
 \|F_N\|_{\ell^2(\mathbb Z^2)}^2=1,                      \tag{4.5}
\]
while its addition pushforward has triangular coefficients and
\[
 \|\mathcal AF_N\|_{\ell^2(\mathbb Z)}^2
 ={2N^3+N\over3N^2}
 ={2N+N^{-1}\over3}\longrightarrow\infty.               \tag{4.6}
\]
Smooth compact functions approximating these rectangles give the same
unboundedness in the continuous model.

> **Proposition 4.1 (mixed landing obstruction).**  The normed
> Bloch–Floquet landings of the two periodic factors do not combine to a
> bounded landing in the one-variable row-C test space.  The first failed
> map after the fixed-prime repair is the Künneth-to-addition pushforward
> (4.2).

A diagonal Fourier trace would be bounded from a Sobolev space with more
than one half derivative in the transverse variable.  The ordered-extremal
norm has no transverse derivative.  The Gamma graph norm controls the
single archimedean frequency through logarithmic digamma growth; it does
not control a derivative normal to the diagonal in \(\mathbb R^2\).
Therefore the existing Gamma term does not repair (4.2).

## 5. All primes and the adelic character group

Let
\[
 \Gamma=\log\mathbb Q_{>0}
 =\bigoplus_p(\log p)\mathbb Z
                                                                  \tag{5.1}
\]
as an abstract discrete group.  Unique factorization proves that the
\(\log p\) are linearly independent over \(\mathbb Q\), and
\[
 \widehat\Gamma\simeq\prod_pS^1.                         \tag{5.2}
\]
Independent Bloch local systems naturally carry product Haar measure on
(5.2).

The logarithmic regular representation of row C restricts to \(\Gamma\)
with joint characters
\[
 \iota(\tau)=(p^{-i\tau})_p,\qquad \tau\in\mathbb R.      \tag{5.3}
\]
The map \(\iota\) is injective and its image is dense.  Density follows
from Kronecker on every finite set of primes, using the rational
independence just proved.

Its image is nevertheless product-Haar null.  Project to any two distinct
primes \(p,q\).  The image of each compact interval
\([-N,N]\) is a rectifiable one-dimensional curve in \(S^1\times S^1\)
and has two-dimensional Haar measure zero.  The whole projected orbit is a
countable union of these curves and still has measure zero.  Hence
\[
 m_{\rm Haar}(\iota(\mathbb R))=0.                       \tag{5.4}
\]

The actual spectral measure class of the row-C representation is the
pushforward of an absolutely continuous measure on \(\mathbb R\) through
\(\iota\).  It is concentrated on the Haar-null correlated characters
(5.3).  Therefore there is no bounded restriction
\[
 L^2\left(\prod_pS^1,m_{\rm Haar}\right)
 \longrightarrow L^2(\iota(\mathbb R),\iota_*d\tau).     \tag{5.5}
\]
The left space is the independent all-local-system completion; the right
space is the archimedean row-C realization.

Equation (5.5) is the character-group version of the diagonal trace
failure (4.3).  Replacing product Haar by the singular measure on
\(\iota(\mathbb R)\) makes an analytic landing possible, but then the
independent periodic Künneth norm has been replaced by a correlated
archimedean norm.  A proof must construct that replacement from geometry
and show that its dagger preparation is contractive; declaring it to be
the pullback norm would merely restate row D.

## 6. Conclusion

Bloch–Floquet completely repairs the fixed-prime descent problem.  All
unitary monodromies integrate to \(L^2(\mathbb R)\), the extremal frame and
flat Künneth norms extend, and the round-trip Gram remains the exact
prime-power--Gamma form.

The construction ceases to be normed when the two periodic Künneth factors
are collapsed to the single analytic variable required by row C.  The
addition pushforward is unbounded, and globally the required
archimedean character curve is singular with respect to the product-Haar
measure on \(\widehat\Gamma\).  The next constructive target is therefore
a geometrically defined transverse trace/Poisson operator from the global
periodic coefficient object to the correlated character curve, equipped
with enough source regularity to make (5.5) bounded.  Its preparation Gram
must remain (3.8) summed over all primes, and its contractivity must be
proved independently of \(B_{\rm nuc}\).

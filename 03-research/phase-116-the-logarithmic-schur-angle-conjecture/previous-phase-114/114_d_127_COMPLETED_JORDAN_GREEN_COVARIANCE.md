# D.127 — Jordan--Green covariance and the completed beta factor

## Verdict

The positive Jordan capacity of D.126 tensorizes exactly with the ordered
depth Green kernel.  At a prime \(p\), its infinitesimal kernel is

\[
 (\log p)p^{-|r-s|/2},                                  \tag{0.1}
\]

which is precisely the difference-depth covariance required by D.109--D.110.
The associated orbit landing produces the positive preparation operator
\(S_p^*S_p\), including every power \(p^k\).

At infinity, the Gamma quotient in the completed Jordan deformation is a
positive beta moment kernel.  Its derivative at \(t=0\) is exactly

\[
 {1\over2}\bigl(\log\pi-\psi(s/2)\bigr),                \tag{0.2}
\]

and on the central line its real double is the full Gamma multiplier
\(m_0-L_\infty\).  The rational polar quotient has exactly two simple
derivative channels, at \(s=0,1\), matching the two Tate jets.

Thus all local ingredients of a completed positive deformation now have
source-defined moment models.  The remaining deficit is not a missing local
factor: after landing, the exact form is still

\[
 B_{\rm nuc}=S^*S-B^*B.                                 \tag{0.3}
\]

Jordan--Green constructs \(S^*S\); the boundary differential constructs
\(B^*B\).  Shorting the two polar jets does not prove that the landing map
from \(B\) to \(S\) is contractive.  That norm-one comparison is exactly D.

## 1. Tensoring contact and depth

For one prime, D.126 gives the reduced infinitesimal covariance

\[
 J_p(r,s)=\log p\qquad(r,s\ge1).                        \tag{1.1}
\]

Put

\[
 \rho_p=p^{-1/2},\qquad G_p(r,s)=\rho_p^{|r-s|}.        \tag{1.2}
\]

Both kernels are positive.  The Schur product theorem gives

\[
 \boxed{(J_p\odot G_p)(r,s)
 =(\log p)p^{-|r-s|/2}\ge0.}                            \tag{1.3}
\]

This is the cofinal difference-depth kernel, rather than the original
sum-depth torsion kernel.

## 2. Orbit landing and every prime power

Let \(U_p=S_{\log p}\) and

\[
 A_p=\sqrt{1-\rho_p^2}(I-\rho_pU_p)^{-1}.              \tag{2.1}
\]

Then

\[
 A_p^*A_p-I=\sum_{k\ne0}\rho_p^{|k|}U_p^k.             \tag{2.2}
\]

Define

\[
 S_pF=\sqrt{\log p}\,A_pF,\qquad
 B_pF=\sqrt{\log p}\,F.                                \tag{2.3}
\]

Consequently

\[
 \langle F,(S_p^*S_p-B_p^*B_p)G\rangle
 =\log p\sum_{k\ne0}p^{-|k|/2}
   \langle F,S_{k\log p}G\rangle.                      \tag{2.4}
\]

For \(k>0\), the coefficient is
\((\log p)p^{-k/2}=\Lambda(p^k)/\sqrt{p^k}\); negative \(k\) give the
reflected Tate orientation.  Thus every prime power lands with the exact
central weight.

## 3. The archimedean beta moment kernel

Let

\[
 \gamma(s)=\pi^{-s/2}\Gamma(s/2)
\]

and, for \(0<t<\operatorname{Re}s\), put

\[
 A_t^\infty(s)={\gamma(s-t)\over\gamma(s)}
 =\pi^{t/2}{\Gamma((s-t)/2)\over\Gamma(s/2)}.           \tag{3.1}
\]

The beta integral gives

\[
 \boxed{
 A_t^\infty(s)
 ={\pi^{t/2}\over\Gamma(t/2)}
 \int_0^1u^{s/2-t/2-1}(1-u)^{t/2-1}\,du.}              \tag{3.2}
\]

After \(u=x^2\), this is the Mellin transform of a positive measure.
Therefore

\[
 K_t^\infty(s,w)=A_t^\infty(s+\overline w)             \tag{3.3}
\]

is a positive Hankel kernel whenever
\(\operatorname{Re}(s+\overline w)>t\), in particular on the central
spectral line for \(0<t<1\).

## 4. Exact Gamma derivative

Since \(A_0^\infty=1\),

\[
 \boxed{\left.\partial_tA_t^\infty(s)\right|_{t=0}
 ={1\over2}\left(\log\pi-\psi(s/2)\right).}             \tag{4.1}
\]

At \(s=1/2+i\tau\),

\[
 2\operatorname{Re}\left.\partial_tA_t^\infty(s)\right|_0
 =\log\pi-\operatorname{Re}\psi(1/4+i\tau/2)
 =m_0-\ell_\infty(\tau).                               \tag{4.2}
\]

Thus the beta deformation recovers the complete Gamma finite part.

## 5. Exactly two polar jet channels

The rational part of \(\xi(s-t)/\xi(s)\) is

\[
 P_t(s)={(s-t)(s-t-1)\over s(s-1)}.                    \tag{5.1}
\]

Its derivative is

\[
 \left.\partial_t\log P_t(s)\right|_0
 =-{1\over s}-{1\over s-1}.                            \tag{5.2}
\]

There are precisely two simple boundary channels, at \(s=0,1\).  In central
logarithmic coordinates they are the evaluations at \(\pm i/2\), namely
\(M_-\) and \(M_+\).  Passing to their common kernel is exactly polar
shorting.

## 6. Separate positive models and the relative landing

At finite Euler cutoff, the Jordan covariance, Green kernels and beta kernel
are positive coefficient/moment models.  Tensor and Schur products preserve
positivity inside their common Hankel coefficient category.

They do **not** form a single positive kernel whose derivative is pulled
back to the annulus source by one fixed positive landing.  Indeed, if
\(K_t\geq0\), \(K_0\) vanishes on a subspace \(N\), and \(J:N\to
\operatorname{Dom}K_t\) is independent of \(t\), then

\[
 \langle Jv,K_tJv\rangle\geq0,\qquad
 \langle Jv,K_0Jv\rangle=0
\]

imply

\[
 \left.{d\over dt}\langle Jv,K_tJv\rangle\right|_{0+}
 \geq0.                                                 \tag{6.1}
\]

Such a fixed positive pullback cannot equal a form whose sign is precisely
the row-D question.  The actual construction has three distinct operations:
positive moment realization, Hankel-depth to Toeplitz/annulus landing, and
subtraction of the relative diagonal/Gamma-energy channels.  The last two
are not one positive pullback.  After them one obtains the exact signed Gram
decomposition

\[
 \boxed{B_{{\rm nuc},X}(F,G)
 =\langle SF,SG\rangle-\langle BF,BG\rangle,}           \tag{6.2}
\]

where

\[
 SF=((S_pF)_p,\sqrt{m_0}F),\qquad
 BF=((B_pF)_p,\partial_\infty F).                       \tag{6.3}
\]

This is D.79's signed pullback, now with positive Jordan/beta moment origins
for the coefficient pieces.  It must not be described as the derivative of
one positive kernel after one fixed positive pullback.

## 7. Exact remaining deficit

Row D is

\[
 \|SF\|^2\le\|BF\|^2
 \qquad(F\in\ker M_-\cap\ker M_+).                     \tag{7.1}
\]

Equivalently, Douglas factorization asks for a contraction

\[
 C:\overline{\operatorname{Ran}B}\to
   \overline{\operatorname{Ran}S},\qquad
 S=CB,\qquad\|C\|\le1.                                  \tag{7.2}
\]

The positive moment construction proves and determines \(S^*S\).  It does
not compare it with \(B^*B\).  Positivity before landing is preserved only
by a contractive landing; proving that the annulus/Poisson landing has norm
at most one is exactly (7.1).

The finite kernels are positive without a zero hypothesis, but their
cofinal Hilbert landing is not uniformly contractive.  The nuclear character
limit exists; the Hilbert norm-one limit is the substantive row-D theorem.

## 8. Conclusion

\[
 \boxed{
 \text{Jordan contact}\odot\text{depth Green}
 \;+\;\text{Gamma beta moment}
 \xrightarrow{\text{landing/shorting}}
 B_{\rm nuc}=S^*S-B^*B.}
\]

Every \(p^k\), both orientations, the complete Gamma multiplier and exactly
two Tate jets occur with their correct coefficients.  The remaining gap is
the single global contraction \(S=CB\), \(\|C\|\le1\).  No local Euler,
Green, beta or polar datum is missing.

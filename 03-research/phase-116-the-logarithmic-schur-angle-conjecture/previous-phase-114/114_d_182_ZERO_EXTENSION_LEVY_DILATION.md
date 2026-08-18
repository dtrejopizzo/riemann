# D.182 — Exact zero-extension Lévy dilation of the complete reference

## Verdict

The balanced prime-power factorization of D.134 admits a stronger exact
choice.  Replace the regional channels by the zero-extension channels

\[
 (\widehat J_{n,\pm}F)(t)
 ={\widetilde F(t+\log n)\pm\widetilde F(t)\over\sqrt2},
 \qquad t\in\mathbb R.                               \tag{0.1}
\]

The same nonnegative boundary term is added to the \(+\) and \(-\)
energies, so their difference, and hence \(B_{\rm nuc}\), is unchanged.
With this choice the ambient positive reference is the part on \(I_T\) of
the translation-invariant Lévy generator with symbol

\[
 \boxed{
 r_T(\tau)=h_{5/4}(\tau)
 +\sum_{p^j\le e^{2T}}{\log p\over p^{j/2}}
       \bigl(1-\cos(j\log p\,\tau)\bigr).}           \tag{0.2}
\]

This contains the complete Gamma place and every active prime power.
For \(\lambda>0\), the full-line massive resolvent is convolution by the
positive measure

\[
 \nu_{T,\lambda}=\int_0^\infty e^{-\lambda t}\mu_{T,t}\,dt,
 \qquad \widehat\mu_{T,t}(\tau)=e^{-t r_T(\tau)},     \tag{0.3}
\]

and

\[
 \boxed{\|\nu_{T,\lambda}\|_{\rm TV}=\lambda^{-1}}. \tag{0.4}
\]

If \(\widehat{\mathcal R}_T\) is the killed/part operator on \(I_T\), its
massive resolvent is dominated by this convolution resolvent:

\[
 \boxed{
 0\le(\widehat{\mathcal R}_T+\lambda)^{-1}f
 \le\nu_{T,\lambda}*\widetilde f
 \quad(f\ge0).}                                      \tag{0.5}
\]

Thus the reference has an exact convolution-dominated inverse tail with
uniform row and column mass \(1/\lambda\).  This is the inverse-closed
replacement that the solid Wiener/Jaffard norms of D.180 could not
provide.  It is uniform precisely because the prime mass is normalized
inside a Markov semigroup rather than estimated by total variation before
exponentiation.

The two Tate jets again alter the massive Green operator by rank at most
two.  Therefore all failures of translation invariance caused by Tate are
finite-rank; all failures caused by the boundary are dominated by killing;
the remaining bulk is the exact Toeplitz/Lévy convolution (0.3).

## 1. Exact equality after adding the boundary energy

Put \(b=\log n\le2T\), and retain the regional channels of D.134 on
\(A_{n,T}=[-T,T-b]\).  Direct expansion gives

\[
 \|\widehat J_{n,\pm}F\|_2^2
 =\|F\|_2^2\pm\operatorname {Re}C_F(b),              \tag{1.1}
\]

whereas

\[
 \|J_{n,\pm}F\|_2^2
 =\|F\|_2^2-B_{n,T}(F)
   \pm\operatorname {Re}C_F(b),                      \tag{1.2}
\]

with

\[
 B_{n,T}(F)={1\over2}
 \left(\int_{-T}^{-T+b}|F(t)|^2dt
       +\int_{T-b}^{T}|F(t)|^2dt\right)\ge0.         \tag{1.3}
\]

Consequently

\[
 \|\widehat J_{n,+}F\|^2-\|\widehat J_{n,-}F\|^2
 =\|J_{n,+}F\|^2-\|J_{n,-}F\|^2
 =2\operatorname {Re}C_F(b).                        \tag{1.4}
\]

Define

\[
\begin{aligned}
 \widehat{\mathcal R}_T(F)
 &=\mathcal H_{5/4}(F)+\sum_nw_n\|\widehat J_{n,-}F\|^2,\\
 \widehat{\mathcal W}_TF
 &=\left(\sqrt\beta F,Q_{1/2,T}F,
          (\sqrt{w_n}\widehat J_{n,+}F)_n\right),
 \qquad w_{p^j}={\log p\over p^{j/2}}.
\end{aligned}                                        \tag{1.5}
\]

Equation (1.4) proves the exact identity

\[
 \boxed{-B_{\rm nuc}^{\rm prim}
 =\widehat{\mathcal R}_T-
  \widehat{\mathcal W}_T^*\widehat{\mathcal W}_T.}  \tag{1.6}
\]

No inequality and no asymptotic replacement occurs here.  Relative to
D.134, both positive sides have received the same multiplication operator
\(\sum_nw_nB_{n,T}\).

## 2. The exact bulk Lévy symbol

On the full line, Plancherel gives

\[
 \|\widehat J_{n,-}F\|^2
 ={1\over2\pi}\int_{\mathbb R}
 (1-\cos(b\tau))|\widehat F(\tau)|^2d\tau.           \tag{2.1}
\]

Together with the Gamma screw formula

\[
 h_{5/4}(\tau)=2\int_0^\infty
 {e^{-5s/2}\over1-e^{-2s}}(1-\cos(s\tau))\,ds,      \tag{2.2}
\]

this proves (0.2).  It is a continuous negative-definite function: its
Lévy measure is

\[
 {e^{-5|s|/2}\over1-e^{-2|s|}}\,ds
 +{1\over2}\sum_{p^j\le e^{2T}}w_{p^j}
   (\delta_{j\log p}+\delta_{-j\log p}).             \tag{2.3}
\]

Therefore \(e^{-t r_T}\) is positive definite and is the Fourier
transform of a symmetric probability measure \(\mu_{T,t}\).  The Gamma
part may have infinite jump activity near zero, but (2.2) is its exact
Lévy--Khintchine representation; the finite prime-power part is a compound
Poisson process.  Their convolution is still a probability measure.

Equation (0.3) is consequently a positive measure, and Tonelli gives

\[
 \|\nu_{T,\lambda}\|_{\rm TV}
 =\int_0^\infty e^{-\lambda t}\|\mu_{T,t}\|_{\rm TV}dt
 =\int_0^\infty e^{-\lambda t}dt={1\over\lambda},   \tag{2.4}
\]

proving (0.4).

## 3. Boundary killing gives domination, not an error term

The zero-extension form \(\widehat{\mathcal R}_T\) is the part form of
the full-line Lévy form on the open interval \(I_T\): paths are killed
when they leave the interval.  The standard part-semigroup domination,
which also follows directly from the Beurling--Deny path construction,
is

\[
 0\le e^{-t\widehat{\mathcal R}_T}f
 \le\mathbf1_{I_T}\bigl(\mu_{T,t}*\widetilde f\bigr),
 \qquad f\ge0.                                       \tag{3.1}
\]

Multiplication by \(e^{-\lambda t}\), integration in \(t\), and Tonelli
give (0.5).  In particular

\[
 \|(\widehat{\mathcal R}_T+\lambda)^{-1}\|_{1\to1},
 \ \|(\widehat{\mathcal R}_T+\lambda)^{-1}\|_{\infty\to\infty}
 \le\lambda^{-1}.                                   \tag{3.2}
\]

Unlike a solid matrix estimate, (3.1) preserves the exact arithmetic jump
labels: the prime component of \(\mu_{T,t}\) is the Poisson sum of ordered
words in the atoms \(\pm j\log p\), with the canonical factor \(1/k!\) at
depth \(k\).  Thus the same semigroup that localizes the inverse already
contains the Witt word combinatorics, including repeated prime powers.

## 4. Tate shorting is rank two also in the massive family

Let \(M=(J_0,J_1)\) be the exact A--B--C moment map and set

\[
 G_{T,\lambda}=(\widehat{\mathcal R}_T+\lambda)^{-1}. \tag{4.1}
\]

The Green operator after imposing \(MF=0\) is

\[
 G_{T,\lambda}^{\rm prim}
 =G_{T,\lambda}-G_{T,\lambda}M^*
 (MG_{T,\lambda}M^*)^{-1}MG_{T,\lambda}.             \tag{4.2}
\]

Thus

\[
 \operatorname {rank}
 (G_{T,\lambda}-G_{T,\lambda}^{\rm prim})\le2.       \tag{4.3}
\]

Equations (0.4)--(0.5) and (4.2)--(4.3) give the desired exact separation:

* bulk: convolution dominated by a positive measure of mass
  \(\lambda^{-1}\);
* boundary: killed and therefore dominated by the bulk;
* Tate: an explicit rank-two correction;
* arithmetic: every \(p^j\) remains an atom of the same Lévy measure;
* archimedean place: the complete \(5/4\)-Gamma Lévy density remains in
  the same exponent.

## 5. Remaining word comparison

The compound-Poisson expansion in (3.1) supplies factorial denominators,
but a final bookkeeping theorem is still required to identify its
arithmetic product-label grouping with the D.178 coefficient

\[
 \theta_k={2^kk!\over(2k)!}.                         \tag{5.1}
\]

The exact object to compare is no longer an arbitrary noncommuting
inverse.  It is the killed compression of the Toeplitz convolution
potential (0.3), plus the rank-two Tate term (4.2).  Hence the remaining
comparison is a positive path-counting statement: killing can only remove
paths, while the full-line prime paths group by products through
\(\Gamma_m\Gamma_n=\Gamma_{mn}\).  The Gamma paths carry no arithmetic
label and act by a probability convolution.


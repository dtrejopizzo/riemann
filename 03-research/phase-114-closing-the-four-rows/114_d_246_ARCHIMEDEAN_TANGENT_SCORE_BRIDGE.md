# D.246 — The Gaussian Fourier tangent gives the complete Gamma score

## Verdict

The first-order tangent–dual identity of D.245 has an exact archimedean
analogue.  The central Gaussian is additively self-Fourier.  Splitting its
logarithmic tangent into Fourier parity and pairing the even tangent with
the dual central state gives

\[
 2\operatorname{Re}{L_\infty'\over L_\infty}
\]

on the critical line.  The odd tangent gives the conjugate phase score.
This proves the source-level first-order port of the complete Gamma factor,
using only the local Tate functional equation.

Together D.245 and D.246 recover the full unlocalized prime--Gamma
logarithmic metric derivative of D.240 from additive self-dual local
vectors.  Support shorting and the sharp sign remain open.

## 1. Gaussian deformation

On \(\mathbb R\), use the self-dual additive character and let

\[
 g_0(x)=e^{-\pi x^2},\qquad \mathcal F_\infty g_0=g_0.
                                                               \tag{1.1}
\]

For real \(\sigma\) near \(1/2\), put

\[
 g_\sigma(x)=|x|^{\sigma-1/2}g_0(x),\qquad
 d_\infty=\left.\partial_\sigma g_\sigma\right|_{\sigma=1/2}
          =(\log|x|)g_0(x).                         \tag{1.2}
\]

For the even Mellin transform

\[
 \mathcal Mf(s)=\int_0^\infty f(x)x^s\,{dx\over x},
\]

direct Gaussian integration gives

\[
 \mathcal Mg_\sigma(s)
 ={1\over2}L_\infty(s+\sigma-\tfrac12),\qquad
 L_\infty(s)=\pi^{-s/2}\Gamma(s/2).                 \tag{1.3}
\]

Consequently

\[
 \mathcal Mg_0(s)={1\over2}L_\infty(s),\qquad
 \mathcal Md_\infty(s)={1\over2}L_\infty'(s).       \tag{1.4}
\]

## 2. Local Fourier functional equation

The local Tate equation has the form

\[
 \mathcal M(\mathcal F_\infty f)(s)
 =\chi_\infty(s)\mathcal Mf(1-s).                  \tag{2.1}
\]

Applying it to the self-Fourier Gaussian and using (1.4) determines

\[
 \chi_\infty(s)={L_\infty(s)\over L_\infty(1-s)}.   \tag{2.2}
\]

Therefore

\[
 \mathcal M(\mathcal F_\infty d_\infty)(s)
 ={1\over2}L_\infty(s)
   {L_\infty'(1-s)\over L_\infty(1-s)}.             \tag{2.3}
\]

Define

\[
 d_{\infty,\pm}
 ={d_\infty\pm\mathcal F_\infty d_\infty\over2}.
                                                               \tag{2.4}
\]

Combining (1.4) and (2.3) gives the two exact ratios

\[
 \boxed{
 {2\mathcal Md_{\infty,+}(s)\over\mathcal Mg_0(s)}
 ={L_\infty'(s)\over L_\infty(s)}
  +{L_\infty'(1-s)\over L_\infty(1-s)},
 }                                                   \tag{2.5}
\]

\[
 \boxed{
 {2\mathcal Md_{\infty,-}(s)\over\mathcal Mg_0(s)}
 ={L_\infty'(s)\over L_\infty(s)}
  -{L_\infty'(1-s)\over L_\infty(1-s)}.
 }                                                   \tag{2.6}
\]

## 3. Critical-line score

For \(s=\frac12+i\tau\), one has \(1-s=\bar s\) and
\(\overline{L_\infty'(s)/L_\infty(s)}
=L_\infty'(1-s)/L_\infty(1-s)\).  Hence

\[
 \boxed{
 {2\mathcal Md_{\infty,+}(s)\over\mathcal Mg_0(s)}
 =2\operatorname{Re}{L_\infty'(s)\over L_\infty(s)}
 =\left.\partial_\sigma
   \log|L_\infty(\sigma+i\tau)|^2
  \right|_{\sigma=1/2}.
 }                                                   \tag{3.1}
\]

Similarly,

\[
 {2\mathcal Md_{\infty,-}(s)\over\mathcal Mg_0(s)}
 =2i\operatorname{Im}{L_\infty'(s)\over L_\infty(s)}. \tag{3.2}
\]

The even tangent is therefore the Gamma norm score, while the odd tangent
is the Gamma phase anomaly.

Using
\[
 {L_\infty'\over L_\infty}(s)
 =-\frac12\log\pi+\frac12\psi(s/2),
\]
equation (3.1) is exactly the complete digamma multiplier used in
D.133--D.137 and D.240, before the already proved Tate--Chebyshev finite
part is removed.

## 4. Type of the global port

For a multiplicative test vector \(F(\tau)\), multiplication by
\(\mathcal Md_{\infty,+}/\mathcal Mg_0\) gives the complete
archimedean score channel.  Since the denominator \(L_\infty(s)\) has no
zeros, this ratio is source-defined on the common Schwartz/form core and
its closure is the standard digamma form.

Combining (3.1) with D.245(2.2) gives, place by place,

\[
 \partial_\sigma\log|E_{S,\sigma}|^2
 =2\,(\text{even local tangent})\,
       (\text{dual central local state}).           \tag{4.1}
\]

This is the local-vector construction underlying D.240(3.4).  It includes
Gamma and every \(p^k\), and it is unavailable in a Beurling prime system
without additive local fields and their Tate functional equations.

Equation (4.1) remains a first-order Krein pairing.  The missing theorem is
that after support/Tate compression its old/born Schur residual is the
transport of the Lorentzian tangent contraction constructed in D.244,
with the Gamma tangent included.

## 5. Classification

* Gaussian Mellin identities (1.3)--(1.4): **PROVED**.
* Fourier-transform tangent identities (2.3)--(2.6): **PROVED FROM THE
  LOCAL TATE EQUATION**.
* Complete Gamma score identity (3.1): **PROVED**.
* Prime--Gamma source port (4.1): **PROVED ON THE COMMON CORE**, using
  D.245.
* Closed-form realization: **PROVED**, by the standard digamma form already
  audited in D.133--D.137.
* Sharp support-shorted tangent comparison: **OPEN**.
* Row D: **OPEN**.

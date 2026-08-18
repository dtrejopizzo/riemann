# 106.57 — Intermediate-defect radical shorting and the two-channel gate

## Purpose and verdict

Document 106.54 factors the intermediate-position defect as

\[
 \mathcal D_{\varepsilon,N}=C_{\varepsilon,N}^*C_{\varepsilon,N},
 \qquad
 C_{\varepsilon,N}
 =M_{\sqrt{1-\eta^2}}H_{\varepsilon,N}M_\eta .       \tag{1}
\]

This note tests whether the defect can be absorbed by the exact Riemann
radical before the complementary spectral estimate is made.  The answer is
exact but degenerate: at every common finite cutoff the images under
\(C_{\varepsilon,N}\) of the centered radical vectors are dense in the
entire even output space.  Consequently the optimal positive short of
\(\mathcal D_{\varepsilon,N}\) to the radical complement is the zero
operator.

There is an exact two-channel Stinespring dilation of the theta sandwich,
but its loss channel therefore supplies no nonzero quotient coercivity.
Moreover, the defect occurs with a negative sign in the physical curvature,
so deleting it after shorting would have the wrong lower-bound direction
unless the diagonal, Gamma and polar terms were shorted jointly.  This is a
stop-gate for the isolated-defect strategy, not a proof of the spectral
floor.

## 1. Finite-cutoff notation

Work in the even subspace of \(L^2(\mathbb R,dx)\).  Use the notation of
106.54:

\[
 w=\frac{hK}{c_K},\qquad
 \eta=\left(\frac{c_KK}{h}\right)^{1/2},\qquad
 \zeta_\eta=\sqrt{1-\eta^2},\qquad
 \mathcal U=M_{\sqrt w}.                             \tag{2}
\]

Thus

\[
 T=M_\eta H M_\eta,\qquad C=M_{\zeta_\eta}HM_\eta,
 \qquad
 T^*T+C^*C=M_\eta H^2M_\eta .                       \tag{3}
\]

Here and below \(H=H_{\varepsilon,N}\), with
\(0<\varepsilon<1\) and \(N<\infty\), is the common-cutoff symmetric
prime--Gamma convolution.  Its Fourier multiplier is

\[
 m_{\varepsilon,N}(t)
 =2\int_\varepsilon^{\varepsilon^{-1}}g(u)\cos(tu)\,du
  +2\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n}
       \cos(t\log n).                                \tag{4}
\]

It is a real even entire function, and
\(m_{\varepsilon,N}(0)>0\).  Hence it is nonzero almost everywhere on
the real axis.

Let

\[
 r_j=\frac{K^{(2j)}}K,\qquad
 \bar r_j=r_j-4^{-j}\quad(j\ge1),                   \tag{5}
\]

and put

\[
 \widetilde{\mathcal R}
 =\overline{\mathrm{span}}
   \{\mathcal U\bar r_j:j\ge1\}\subset L^2_{\rm even}(dx). \tag{6}
\]

The centering constant in (5) is exact.  Indeed,
\(c_K=\widehat K(i/2)\) and
\(\widehat {K^{(2j)}}(z)=(-1)^jz^{2j}\Xi(z)\), so

\[
 \mu_K(r_j)
 =\frac{\widehat {K^{(2j)}}(i/2)}{\widehat K(i/2)}
 =4^{-j}.                                           \tag{7}
\]

## 2. The transformed radical is a polynomial ideal

The two multiplication factors in (2) cancel exactly:

\[
 M_\eta\mathcal U\bar r_j
 =K\bar r_j=K^{(2j)}-4^{-j}K.                       \tag{8}
\]

After applying \(H\) and Fourier transform, (8) becomes

\[
 \widehat{HM_\eta\mathcal U\bar r_j}(t)
 =m_{\varepsilon,N}(t)\Xi(t)
   \left\{(-1)^jt^{2j}-4^{-j}\right\}.             \tag{9}
\]

Every polynomial in braces vanishes at \(t^2=-1/4\).  More precisely,

\[
 \mathrm{span}\,\left\{(-1)^jt^{2j}-4^{-j}:j\ge1\right\}
 =(t^2+1/4)\,\mathbb C[t^2].                        \tag{10}
\]

This follows because, as polynomials in \(s=t^2\), the functions
\(s^j-(-1/4)^j\), \(j\ge1\), form a triangular basis for the ideal of
polynomials vanishing at \(-1/4\).

## 3. Density of the defect-radical images

### Lemma 1 — Weighted even-polynomial density

Let

\[
 F(t)=m_{\varepsilon,N}(t)\Xi(t),\qquad
 W(t)=|F(t)|^2(t^2+1/4)^2.                           \tag{11}
\]

Then \(W>0\) almost everywhere, and \(\mathbb C[t^2]\) is dense in
\(L^2_{\rm even}(W(t)dt)\).

#### Proof

Both factors of \(F\) are nonzero entire functions, hence their real zero
sets are discrete unless a factor is identically zero.  Neither is
identically zero.  Thus \(W>0\) almost everywhere.

The cutoff multiplier \(m_{\varepsilon,N}\) is bounded on the real axis.
Stirling's formula for the Gamma factor in \(\Xi\), together with the
standard polynomial vertical-strip bound for \(\zeta\), gives an
\(a>0\) for which

\[
 \int_{\mathbb R}e^{2a|t|}W(t)\,dt<\infty.           \tag{12}
\]

Suppose \(v\in L^2_{\rm even}(Wdt)\) is orthogonal to every polynomial
in \(t^2\).  By Cauchy--Schwarz and (12),

\[
 \Phi(z)=\int_{\mathbb R}v(t)W(t)e^{izt}\,dt         \tag{13}
\]

is analytic in a strip around the real axis.  All its even derivatives at
zero vanish by the assumed orthogonality, and all its odd derivatives
vanish by parity.  Hence \(\Phi\) vanishes identically in that strip.
Uniqueness of the Fourier transform gives \(vW=0\), and therefore
\(v=0\).  This proves density. \(\square\)

### Theorem 2 — Radical saturation of the loss channel

At every common finite cutoff,

\[
 \boxed{
 \overline{C_{\varepsilon,N}\widetilde{\mathcal R}}
 =L^2_{\rm even}(\mathbb R,dx).}                    \tag{14}
\]

#### Proof

Let \(y\in L^2_{\rm even}(dt)\).  Since
\(F(t)(t^2+1/4)\ne0\) almost everywhere, the function

\[
 v(t)=\frac{y(t)}{F(t)(t^2+1/4)}                    \tag{15}
\]

belongs to \(L^2_{\rm even}(Wdt)\), with norm \(\|y\|_2\).  By Lemma 1
there are polynomials \(q_k(t^2)\) such that

\[
 F(t)(t^2+1/4)q_k(t^2)\longrightarrow y(t)
 \quad\hbox{in }L^2(dt).                            \tag{16}
\]

Equations (9)--(10) show that the left side of (16) belongs to the span of
the Fourier transforms of \(HM_\eta\mathcal U\bar r_j\).  Fourier
unitarity therefore proves that

\[
 \overline{HM_\eta\widetilde{\mathcal R}}
 =L^2_{\rm even}(dx).                               \tag{17}
\]

By 106.54, \(\eta^2<1/2\).  Consequently

\[
 2^{-1/2}<\zeta_\eta\le1,                           \tag{18}
\]

so \(M_{\zeta_\eta}\) is boundedly invertible.  Applying it to the
dense space in (17) proves (14). \(\square\)

Theorem 2 does not contradict the non-completeness of the radical in
106.39.  In fact, \(C\) is injective: both multiplication factors are
strictly positive, and the zero set of the Fourier multiplier of \(H\) has
Lebesgue measure zero.  The space \(\widetilde{\mathcal R}\) is proper by
the explicit zero modes of 106.39.  Hence
\(C\widetilde{\mathcal R}\) cannot equal the whole even space: otherwise,
for nonzero \(f\in\widetilde{\mathcal R}^{\perp}\), one could write
\(Cf=Cr\) with \(r\in\widetilde{\mathcal R}\), and injectivity would give
\(f=r\), a contradiction.  Its dense range is therefore nonclosed, and
\(C|_{\widetilde{\mathcal R}}\) is not bounded below.  The
polynomial-moment completion occurs only after the full cutoff convolution
is applied.

## 4. The exact optimal short

For a closed subspace \(\mathcal R\) and a bounded operator \(C\), the
largest positive operator below \(C^*C\) whose kernel contains
\(\mathcal R\) has quadratic form

\[
 \begin{aligned}
 \langle f,(C^*C)_{/\mathcal R}f\rangle
 &=\inf_{r\in\mathcal R}\|C(f+r)\|^2\\
 &=\mathrm{dist}(Cf,\overline{C\mathcal R})^2\\
 &=\left\|(I-P_{\overline{C\mathcal R}})Cf\right\|^2.
 \end{aligned}                                      \tag{19}
\]

Equivalently,

\[
 (C^*C)_{/\mathcal R}
 =C^*(I-P_{\overline{C\mathcal R}})C.               \tag{20}
\]

For completeness, put \(Q=I-P_{\overline{C\mathcal R}}\).  The operator
\(C^*QC\) is positive, is at most \(C^*C\), and annihilates
\(\mathcal R\).  Conversely, if \(0\le B\le C^*C\) and
\(\mathcal R\subset\ker B\), Douglas factorization gives a contraction
\(D\) such that \(B^{1/2}=DC\).  Since \(DCr=0\) for every
\(r\in\mathcal R\), continuity gives \(D=DQ\).  Hence

\[
 \|B^{1/2}f\|=\|DQCf\|\le\|QCf\|,                  \tag{20a}
\]

so \(B\le C^*QC\).  This proves both the maximality assertion and
(19)--(20).

Applying Theorem 2 yields the exact answer:

### Corollary 3 — The shorted intermediate defect vanishes

On the even sector,

\[
 \boxed{
 (\mathcal D_{\varepsilon,N})_{/\widetilde{\mathcal R}}=0,}
 \qquad
 \boxed{
 \inf_{r\in\widetilde{\mathcal R}}
 \|C_{\varepsilon,N}(f+r)\|^2=0.}                  \tag{21}
\]

Thus no positive fraction of the intermediate defect survives optimal
radical shorting.  In particular, there can be no estimate

\[
 (\mathcal D_{\varepsilon,N})_{/\widetilde{\mathcal R}}
 \ge cB,
 \qquad c>0,\ B\ne0,                                \tag{22}
\]

on the quotient.

## 5. Exact two-channel dilation and its direction

Define

\[
 Jf=\binom{M_\eta f}{M_{\zeta_\eta}f},
 \qquad X=HM_\eta.                                  \tag{23}
\]

Since \(\eta^2+\zeta_\eta^2=1\), \(J^*J=I\).  Moreover,

\[
 \boxed{
 JXf=\binom{Tf}{Cf},\qquad
 X^*X=T^*T+C^*C.}                                   \tag{24}
\]

This is the exact two-channel Stinespring dilation of the theta sandwich.
It proves the contraction

\[
 T^*T\le X^*X.                                      \tag{25}
\]

However, the physical curvature is

\[
 \widetilde L^2-\frac12\widetilde L
 =X^*X-C^*C+B_T,                                    \tag{26}
\]

with \(B_T\) the joint diagonal, Gamma, polar and threshold expression of
106.56.  Therefore discarding \(-C^*C\) gives an upper bound, not a lower
bound.  Corollary 3 does not permit termwise replacement of \(C^*C\) by
zero in (26), because the minimizing radical vector in (19) simultaneously
changes \(X^*X\) and \(B_T\).  The complete curvature annihilates the
threshold radical, whereas its separate terms do not.

The source radical projection \(P_{\mathscr M}\) of 106.39 is also not the
output projection \(P_{\overline{C\widetilde{\mathcal R}}}\).  The latter
is the identity by (14).  Identifying the two would erase the entire even
loss channel, including every complementary zero mode, and would provide
no norm estimate.

## 6. Conclusion

The isolated intermediate-defect pivot is now decided exactly:

* the theta sandwich has a canonical two-channel isometric dilation;
* the loss-channel images of the centered Riemann radical are dense;
* the optimal radical short of the positive defect is identically zero;
* the dilation supplies only the already known upper comparison
  \(T^*T\le X^*X\);
* no noncircular lower bound for
  \(\widetilde L(\widetilde L-1/2)\) follows from this channel alone.

Any surviving proof must short the *complete signed curvature* at common
cutoff, not the intermediate defect separately.  Its remaining diagonal
block is exactly the joint cluster sign isolated in 106.56.

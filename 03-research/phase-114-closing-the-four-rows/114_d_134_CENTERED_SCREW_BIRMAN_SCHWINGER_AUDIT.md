# D.134 — Centred Chebyshev screw factorization and Birman--Schwinger audit

## Verdict

The Tate--Chebyshev identity of D.133 admits an exact, non-perturbative
factorization on every bounded support window.  After the two Tate moments
have removed the continuous Chebyshev main term, the positive
\(5/4\)-Gamma form is the square of a continuous screw/difference map.  The
centred contact splits into a positive symmetric channel and a positive
antisymmetric channel at every prime power.  More precisely,

\[
 \boxed{
 -B_{\rm nuc}^{\rm prim}=\mathcal R_T-\mathcal W_T^*\mathcal W_T,} \tag{0.1}
\]

where

\[
 \mathcal R_T=\mathcal H_{5/4}
       +\sum_{p^k<e^{2T}}{\log p\over p^{k/2}}J_{p^k,-}^*J_{p^k,-}\geq0 \tag{0.2}
\]

and \(\mathcal W_T\) contains the \(\beta\)-channel, the resolvent kernel
\(e^{-|t-s|/2}\), and every symmetric prime-power channel
\(\sqrt{(\log p)p^{-k/2}}J_{p^k,+}\).

This yields a genuine positive Birman--Schwinger operator

\[
 \mathcal K_T=\mathcal W_T\mathcal R_T^{-1}\mathcal W_T^*\geq0, \tag{0.3}
\]

or equivalently its source-space version
\(\mathcal R_T^{-1/2}\mathcal W_T^*\mathcal W_T\mathcal R_T^{-1/2}\).
It is compact for every finite \(T\).  Therefore it has only finitely many
dangerous eigenvalues \(>1\), and their number is exactly the Morse index
of \(-B_{\rm nuc}^{\rm prim}\).

The compactness is weak: because \(\beta>0\) supplies an identity channel
and the Gamma eigenvalues grow only logarithmically, \(\mathcal K_T\) is
not in any Schatten class \(\mathcal S_p\), \(p<\infty\).  Thus no Fredholm
determinant, trace bound or finite-rank argument counts the dangerous
channels.  The two Tate constraints can reduce an ambient index by at most
two; they do not bound the remaining index by two.

Finally,

\[
 \boxed{
 \|\mathcal W_T\mathcal R_T^{-1/2}\|\leq1
 \Longleftrightarrow -B_{\rm nuc}^{\rm prim}\geq0.}     \tag{0.4}
\]

Consequently proving the requested norm bound for all \(T\) is exactly row
D, not a consequence of compactness or of the screw factorization.  The
factorization is nevertheless useful: it replaces the signed Stieltjes
measure by one canonical positive reference and one canonical positive
load, and makes the remaining short-capacity theorem completely explicit.

No RH, zero location or positivity of the Weil form is assumed.  The paper
is not modified.

## 1. The centred measure in logarithmic coordinates

D.133 gives

\[
 dE_\beta(x)=d\psi_C(x)-dx+{\beta\over2}\delta_1,
 \qquad \beta=\log\pi-\psi(5/4)>0,                     \tag{1.1}
\]

and, for a two-Tate primitive \(F\) supported in \(I_T=[-T,T]\),

\[
 -B_{\rm nuc}(F,F)=\mathcal H_{5/4}(F)
 -2\int_{[1,e^{2T}]}x^{-1/2}\operatorname {Re}C_F(\log x)\,dE_\beta(x). \tag{1.2}
\]

Put \(a=\log x\).  Before using the Tate identity, the symmetrized
logarithmic measure is

\[
 \sum_{p,k\geq1}{\log p\over p^{k/2}}
       (\delta_{k\log p}+\delta_{-k\log p})
 -e^{|a|/2}\,da+\beta\delta_0.                         \tag{1.3}
\]

Only atoms with \(k\log p\leq2T\) act nontrivially on \(I_T\).
The continuous part in (1.3) is not a finite signed measure, and taking its
total variation is the spurious \(e^T\) loss removed in D.133.

On the primitive space, the exact Tate identity changes the continuous
quadratic form according to

\[
 -2\int_0^{2T}e^{a/2}\operatorname {Re}C_F(a)\,da
 =2\int_0^{2T}e^{-a/2}\operatorname {Re}C_F(a)\,da.    \tag{1.4}
\]

The right side is the positive resolvent form

\[
 \langle F,R_{1/2,T}F\rangle,
 \qquad
 (R_{1/2,T}F)(t)=\int_{-T}^{T}e^{-|t-s|/2}F(s)\,ds.    \tag{1.5}
\]

Indeed the full-line Fourier multiplier of \(e^{-|u|/2}\) is
\((\tau^2+1/4)^{-1}\).  Thus the complete centred contact, restricted to
the primitive source, is

\[
\boxed{
 \mathcal C_{E,T}
 =\beta I+R_{1/2,T}
 +\sum_{p^k\leq e^{2T}}{\log p\over p^{k/2}}
    (S_{k\log p}+S_{-k\log p}).}                       \tag{1.6}
\]

Formula (1.6) is an operator identity at the level of primitive quadratic
forms.  It includes every prime power and the full continuous
renormalization.

## 2. Exact continuous screw kernel

The positive Gamma multiplier is

\[
 h_{5/4}(\tau)=\operatorname {Re}\psi(5/4+i\tau/2)-\psi(5/4). \tag{2.1}
\]

The integral representation of the digamma difference gives

\[
 \boxed{
 h_{5/4}(\tau)=2\int_0^\infty
 {e^{-5r/2}\over1-e^{-2r}}(1-\cos\tau r)\,dr.}         \tag{2.2}
\]

Set

\[
 \gamma_{5/4}(r)={e^{-5r/2}\over1-e^{-2r}}.            \tag{2.3}
\]

For the zero extension \(\widetilde F\) of \(F\), Plancherel and Tonelli
give the exact continuous kernel

\[
\boxed{
 \mathcal H_{5/4}(F)
 =\int_0^\infty\gamma_{5/4}(r)
       \|\widetilde F-S_r\widetilde F\|_2^2\,dr
 ={1\over2}\iint_{\mathbb R^2}
 \gamma_{5/4}(|t-s|)|\widetilde F(t)-\widetilde F(s)|^2\,dt\,ds.} \tag{2.4}
\]

The apparent singularity \(\gamma_{5/4}(r)\sim(2r)^{-1}\) is cancelled by
the difference.  At infinity it is \(O(e^{-5r/2})\).  Thus (2.4) is the
Dirichlet form of a symmetric pure-jump screw process.

Equivalently, define

\[
 (D_\infty F)(r,t)=\sqrt{\gamma_{5/4}(r)}
       (\widetilde F(t)-\widetilde F(t-r)).             \tag{2.5}
\]

Then

\[
 \mathcal H_{5/4}=D_\infty^*D_\infty.                 \tag{2.6}
\]

This is the non-perturbative screw factorization.  It is source-defined by
the shifted Gamma oscillator and contains no zero of \(\xi\).

For completeness, splitting the double integral into the window and its
exterior gives

\[
\begin{aligned}
 \mathcal H_{5/4}(F)={}&{1\over2}\iint_{I_T^2}
 \gamma_{5/4}(|t-s|)|F(t)-F(s)|^2\,dt\,ds\\
 &+\int_{I_T}|F(t)|^2
   \int_{\mathbb R\setminus I_T}\gamma_{5/4}(|t-s|)\,ds\,dt. \tag{2.7}
\end{aligned}
\]

The second line is the exact exterior killing term; omitting it would give
the regional, rather than the zero-extension, Gamma operator.

## 3. Balanced factorization of every prime-power channel

For \(n=p^k\), put \(a_n=\log n\),
\(w_n=(\log p)p^{-k/2}\), and

\[
 A_{n,T}=[-T,T-a_n].                                   \tag{3.1}
\]

When \(a_n\leq2T\), define

\[
 (J_{n,\pm}F)(t)={F(t+a_n)\pm F(t)\over\sqrt2},
 \qquad t\in A_{n,T}.                                  \tag{3.2}
\]

Then

\[
 \|J_{n,+}F\|^2-\|J_{n,-}F\|^2
 =2\operatorname {Re}C_F(a_n)
 =\langle F,(S_{a_n}+S_{-a_n})F\rangle.               \tag{3.3}
\]

Let \(Q_{1/2,T}=R_{1/2,T}^{1/2}\), the positive square root of the
resolvent kernel, and define

\[
\begin{aligned}
 \mathcal R_T(F,F)
  &:=\mathcal H_{5/4}(F)
    +\sum_{p^k\leq e^{2T}}w_{p^k}\|J_{p^k,-}F\|^2,    \tag{3.4}\\
 \mathcal W_TF
  &:=\left(\sqrt\beta F,\ Q_{1/2,T}F,
       (\sqrt{w_{p^k}}J_{p^k,+}F)_{p^k\leq e^{2T}}\right). \tag{3.5}
\end{aligned}
\]

Equations (1.6) and (3.3) prove

\[
 \boxed{-B_{\rm nuc}^{\rm prim}
 =\mathcal R_T-\mathcal W_T^*\mathcal W_T.}            \tag{3.6}
\]

This is both a Krein decomposition (one positive square minus another) and
the short-capacity form requested in D.133.  Unlike a perturbative
Hadamard formula, it remains valid for the entire open cell.

## 4. Coercivity and compact resolvent of the reference

Let \(\mathcal P_T\) be the two-Tate primitive subspace.  The Gamma form
domain is

\[
 \mathcal Q_T=\left\{F\in L^2(I_T):
 \int h_{5/4}(\tau)|\widehat F(\tau)|^2d\tau<\infty\right\}. \tag{4.1}
\]

Since

\[
 h_{5/4}(\tau)=\log(1+|\tau|)+O(1)                    \tag{4.2}
\]

at high frequency, bounded sets in the form norm have uniformly small
Fourier tails.  Their low-frequency restrictions are precompact on a
bounded interval.  Hence

\[
 \mathcal Q_T\hookrightarrow L^2(I_T)\quad\text{compactly}. \tag{4.3}
\]

If \(\mathcal H_{5/4}(F)=0\), (2.4) makes \(\widetilde F\) invariant under
almost every translation, so a compactly supported such function is zero.
Compactness then implies the Poincare bound

\[
 \mathcal H_{5/4}(F)\geq c_T\|F\|^2,\qquad c_T>0.       \tag{4.4}
\]

Adding the antisymmetric channels preserves (4.3)--(4.4).  Therefore the
self-adjoint operator associated with \(\mathcal R_T\), restricted to
\(\mathcal P_T\), is strictly positive and has compact resolvent.  In
particular \(\mathcal R_T^{-1/2}\) is compact.

The map \(\mathcal W_T\) is bounded from \(L^2(I_T)\) to its channel
space: \(\beta I\) is bounded, \(\|R_{1/2,T}\|\leq4\), and there are only
finitely many active prime powers, with

\[
 \sum_{p^k\leq e^{2T}}w_{p^k}<\infty.                 \tag{4.5}
\]

## 5. The centred Birman--Schwinger operator

Define on the source

\[
 K_T=\mathcal R_T^{-1/2}\mathcal W_T^*\mathcal W_T
          \mathcal R_T^{-1/2}\geq0.                   \tag{5.1}
\]

Equivalently, on the channel closure define

\[
 \mathcal K_T=\mathcal W_T\mathcal R_T^{-1}\mathcal W_T^*. \tag{5.2}
\]

Their nonzero spectra, with multiplicity, agree.  Since
\(\mathcal R_T^{-1/2}\) is compact and \(\mathcal W_T\) is bounded,

\[
 \boxed{K_T\text{ and }\mathcal K_T\text{ are compact positive operators}.} \tag{5.3}
\]

The Birman--Schwinger principle applied to (3.6) gives

\[
\begin{aligned}
 d_T&:=\dim E_{K_T}((1,\infty))\\
 &=\operatorname {ind}_-
    \left(\mathcal R_T-\mathcal W_T^*\mathcal W_T\right)
 =\operatorname {ind}_-(-B_{\rm nuc}^{\rm prim}).      \tag{5.4}
\end{aligned}

Thus \(d_T<\infty\) for every finite window.  It is the exact number of
dangerous channels.  Moreover

\[
 \boxed{d_T=0\Longleftrightarrow\|K_T\|\leq1.}         \tag{5.5}
\]

No assertion that \(d_T=0\) has been used.

A coarse source-side upper bound is also immediate.  Put

\[
 M_T=\beta+4+2\sum_{p^k\leq e^{2T}}w_{p^k}.            \tag{5.6}
\]

Then \(\mathcal W_T^*\mathcal W_T\leq M_TI\).  By min--max,

\[
 \boxed{d_T\leq N_{\mathcal R_T}(M_T),}                \tag{5.7}
\]

where \(N_{\mathcal R_T}(M)\) counts eigenvalues of \(\mathcal R_T\)
below \(M\).  This proves finiteness but gives no uniform rank bound as
\(T\to\infty\).

## 6. Compact but in no Schatten class

The identity channel in (3.5) gives

\[
 K_T\geq\beta\mathcal R_T^{-1}.                        \tag{6.1}
\]

The antisymmetric prime channels are bounded, so for a finite constant
\(C_T\),

\[
 \mathcal R_T\leq H_{5/4,T}+C_TI.                      \tag{6.2}
\]

The standard sine-space min--max estimate for a logarithmic multiplier
gives

\[
 \lambda_j(H_{5/4,T})\leq C_T'\log(2+j).              \tag{6.3}
\]

Inverse order, (6.1)--(6.3), and min--max imply

\[
 \lambda_j(K_T)\geq{\beta\over C_T''\log(2+j)}.       \tag{6.4}
\]

For every finite \(p>0\),

\[
 \sum_{j\geq1}(\log(2+j))^{-p}=\infty.                \tag{6.5}
\]

Therefore

\[
 \boxed{K_T\notin\mathcal S_p\quad\text{for every }p<\infty.} \tag{6.6}
\]

In particular, ordinary trace, Hilbert--Schmidt and Fredholm-determinant
methods are unavailable.  Compactness only says that the spectrum can
accumulate at zero; it does not make the arithmetic defect finite-rank.

## 7. Why the two Tate jets do not bound the dangerous count

Before imposing moments, the two evaluations span a two-dimensional
boundary plane.  Compression to their common kernel changes the inertia
of any finite spectral section by at most two.  It cannot turn an
arbitrary finite number of eigenvalues of \(K_T\) above one into zero.

The exact count (5.4) is not determined by the rank of the polar plane, the
rank-three nuclear coefficient module, or the number of factors in
\(dE_\beta\).  The latter contains a growing family of independent
translation channels.  Equation (5.7) is the strongest general count
available from compactness alone.

This supplies an exact no-go: any argument claiming \(d_T\leq2\) merely
because there are two Tate jets confuses codimension of the constraint with
Morse index of the compressed operator.

## 8. The norm bound and the remaining short capacity

Let

\[
 A_T=\mathcal W_T\mathcal R_T^{-1/2}.                  \tag{8.1}
\]

Then (3.6) becomes

\[
 -B_{\rm nuc}^{\rm prim}
 =\mathcal R_T^{1/2}(I-A_T^*A_T)\mathcal R_T^{1/2}.    \tag{8.2}
\]

Therefore

\[
 \boxed{
 -B_{\rm nuc}^{\rm prim}\geq0
 \Longleftrightarrow A_T^*A_T\leq I
 \Longleftrightarrow\|A_T\|\leq1.}                    \tag{8.3}
\]

The corresponding shorted capacity in channel space is

\[
 \operatorname {Cap}_T=I-\mathcal W_T\mathcal R_T^{-1}\mathcal W_T^*
 =I-\mathcal K_T.                                      \tag{8.4}
\]

Its nonnegativity is precisely (8.3).  This is the global,
non-perturbative version of the balanced threshold capacity in D.133.

The screw factorization proves that \(\mathcal R_T\) is positive and that
\(A_T\) is compact.  It does not prove \(\|A_T\|\leq1\).  Establishing
that sharp contraction for every \(T\), with all prime powers acting
together, is the centred-discrepancy inequality (5.1) of D.133 and hence
row D itself.

## 9. Exact conclusion

The centred Tate--Chebyshev route succeeds in constructing all requested
objects:

\[
 \begin{array}{c|c}
 \text{datum}&\text{exact realization}\\ \hline
 \mathcal H_{5/4}&D_\infty^*D_\infty\text{ with kernel }\gamma_{5/4}\\
 -dx\text{ after Tate shorting}&R_{1/2,T}\text{ with kernel }e^{-|t-s|/2}\\
 p^k\text{ contact}&w_{p^k}(J_+^*J_+-J_-^*J_-)\\
 \text{positive reference}&\mathcal R_T\\
 \text{positive load}&\mathcal W_T^*\mathcal W_T\\
 \text{Birman--Schwinger operator}&K_T\text{ compact, non-Schatten}\\
 \text{dangerous count}&d_T=\#\{\lambda(K_T)>1\}<\infty\\
 \text{row D}&\|\mathcal W_T\mathcal R_T^{-1/2}\|\leq1
 \end{array}
\]

The factorization is a genuine advance over perturbative cell opening, but
its final norm inequality is neither automatic nor finite-dimensional.
Compactness localizes the obstruction to finitely many channels on each
window; the logarithmic spectral order prevents a determinant or uniform
rank shortcut.  A new global arithmetic estimate is still required to
show that none of those channels crosses one.

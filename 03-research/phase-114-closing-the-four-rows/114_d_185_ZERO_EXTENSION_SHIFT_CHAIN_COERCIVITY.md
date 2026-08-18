# D.185 — Exact shift-chain coercivity of the zero-extension reference

## Verdict

The zero-extension reference of D.182 has a global lower bound which is
much stronger than the Gamma-only prolate bound.  Put

\[
 I_T=(-T,T),\qquad L=2T,qquad N=\lfloor e^L\rfloor,
\]

and let

\[
 w_n={\Lambda(n)\over\sqrt n},\qquad b_n=\log n.
\]

For the complete positive reference

\[
 \widehat {\mathcal R}_T
 =\mathcal H_{5/4}+\sum_{n\le N}w_n
       \widehat J_{n,-}^*\widehat J_{n,-},           \tag{0.1}
\]

one has the exact operator inequality

\[
 \boxed{
 \widehat {\mathcal R}_T\ge A_N I,
 \qquad
 A_N=\sum_{n\le N}w_n
 \left[1-\cos{\pi\over\lceil L/b_n\rceil+1}\right].} \tag{0.2}
\]

In particular

\[
 \boxed{
 A_N\ge {2\over9L^2}
 \sum_{n\le N}{\Lambda(n)(\log n)^2\over\sqrt n}.} \tag{0.3}
\]

The prime number theorem and partial summation give

\[
 A_N\ge\left({4\over9}+o(1)\right)\sqrt N.          \tag{0.4}
\]

All prime powers are retained in (0.2)--(0.3); retaining only primes
already proves (0.4).  Restriction to the two-Tate primitive subspace does
not weaken the bound.  Hence the exact primitive Green operator satisfies

\[
 \|G_T^{\rm prim}\|\le A_N^{-1}=O(N^{-1/2}).        \tag{0.5}
\]

This removes the need for a growing prolate-low block when the complete
zero-extension reference is considered.  It does not by itself prove the
signed form: the positive \(\widehat J_{n,+}\) side received the same
boundary energy in D.182.  The remaining theorem is a Douglas estimate
showing that the actual centered old--born cross is divisible by the
small defect, rather than merely by the large common reference.

## 1. Direct-integral chain decomposition

For \(0<b\le L\), let

\[
 (S_bF)(t)=\widetilde F(t+b),\qquad t\in I_T,        \tag{1.1}
\]

where \(\widetilde F\) denotes zero extension.  After translating
\(I_T\) to \((0,L)\), disintegrate Lebesgue measure by
\(t=r+jb\), \(0\le r<b\).  Almost every fibre is a finite chain and its
number of vertices is at most

\[
 m_b=\lceil L/b\rceil.                              \tag{1.2}
\]

On a chain of length \(m\), \(S_b\) is the nilpotent unilateral Jordan
shift \(J_m\).  Its Hermitian part is one half of the path adjacency
matrix, whose largest eigenvalue is

\[
 \lambda_{\max}\left({J_m+J_m^*\over2}\right)
 =\cos{\pi\over m+1}.                               \tag{1.3}
\]

Since the right side increases with \(m\), the direct integral gives

\[
 \mathrm{Re}\,\langle F,S_bF\rangle
 \le\cos{\pi\over m_b+1}\,\|F\|_2^2.              \tag{1.4}
\]

The zero-extension channel obeys

\[
 \|\widehat J_{b,-}F\|_2^2
 =\|F\|_2^2-\mathrm{Re}\,\langle F,S_bF\rangle.
                                                               \tag{1.5}
\]

Equations (1.4)--(1.5) prove the summand in (0.2).  The Gamma form is
nonnegative, so summing proves (0.2).

## 2. Elementary uniform lower bound

Because \(b\le L\),

\[
 \lceil L/b\rceil+1\le L/b+2\le3L/b.               \tag{2.1}
\]

Consequently

\[
 {\pi\over\lceil L/b\rceil+1}\ge {\pi b\over3L}.
                                                               \tag{2.2}
\]

Both angles lie in \([0,\pi/2]\), and

\[
 1-\cos x\ge {2x^2\over\pi^2}\qquad(0\le x\le\pi/2).
                                                               \tag{2.3}
\]

Monotonicity of \(1-\cos x\), followed by (2.2)--(2.3), yields

\[
 1-\cos{\pi\over\lceil L/b\rceil+1}
 \ge {2b^2\over9L^2}.                               \tag{2.4}
\]

Multiplying by \(w_n\) and summing gives (0.3).

## 3. Asymptotic size

Keeping only the prime terms in (0.3), the required sum is

\[
 \sum_{p\le N}{(\log p)^3\over\sqrt p}.
\]

Writing \(d\vartheta(x)\) for the Chebyshev measure, this is

\[
 \int_{2^-}^{N}{(\log x)^2\over\sqrt x}\,d\vartheta(x).
                                                               \tag{3.1}
\]

The prime number theorem \(\vartheta(x)\sim x\), followed by partial
summation, gives

\[
 \int_2^N{(\log x)^2\over\sqrt x}\,dx
 =2\sqrt N(\log N)^2+O(\sqrt N\log N).              \tag{3.2}
\]

Substitution in (0.3), with \(L=\log N+O(N^{-1})\) on an integer cell,
proves (0.4).  Prime-power terms are nonnegative and therefore can only
increase the lower bound.

## 4. Tate restriction

For every \(F\) in the primitive subspace \(\ker M_-\cap\ker M_+\),
(0.2) remains the same quadratic inequality.  The inverse of the
restricted form therefore has norm at most \(A_N^{-1}\).  No rank-two
loss is needed for this norm statement; the rank-two Green formula of
D.181 is needed only when comparing kernels or separating Tate from the
ambient convolution dilation.


# D.188 — Global \(\sqrt N\) gap and the long-time return contraction

## Verdict

The exact shift-chain constant of D.185 has the sharper asymptotic

\[
 \boxed{A_N\sim\sqrt N.}                              \tag{0.1}
\]

For every \(\theta>0\), the complete zero-extension Green operator admits
the exact split

\[
\begin{aligned}
 \widehat G_T&=K_{\theta,N}+H_{\theta,N},\\
 K_{\theta,N}
 &=\int_0^{\theta/A_N}e^{-t\widehat{\mathcal R}_T}\,dt,\\
 H_{\theta,N}
 &=e^{-\theta\widehat{\mathcal R}_T/A_N}\widehat G_T.
\end{aligned}                                        \tag{0.2}
\]

It satisfies

\[
 \boxed{
 \|K_{\theta,N}\|_{1\to1},\|K_{\theta,N}\|_{\infty\to\infty}
 \le{\theta\over A_N},\qquad
 \|H_{\theta,N}\|\le{e^{-\theta}\over A_N}.}         \tag{0.3}
\]

Let

\[
 M_N=\beta+4+2\sum_{n\le N}{\Lambda(n)\over\sqrt n}
 =(4+o(1))\sqrt N                                   \tag{0.4}
\]

be the global load bound of D.134.  With \(\theta=3\),

\[
 \boxed{
 M_N\|H_{\theta,N}\|\le4e^{-3}+o(1)<0.2.}            \tag{0.5}
\]

Thus every occurrence of the long-time residual in a return word has a
strict, depth-independent contraction.

For the exact endpoint arithmetic synthesis of D.164,

\[
 \boxed{
 \|\mathcal B_N^*K_{\theta,N}\mathcal B_N\|
 \le{\theta\over A_N}(V_N+H_N)
 =O\left({(\log N)^2\over\sqrt N}\right).}           \tag{0.6}
\]

Consequently both the localized endpoint block and the long-time bridge
are strictly contractive for large \(N\), uniformly in all prime powers.
There is no prolate low block.

Equations (0.5)--(0.6) still do not prove the unit Schur budget: common
killing preserves the inertia by D.186, and the centered old–born cross
must be divisible by the defect.  What they prove is that no divergence
or inverse realignment remains in the reference.  The only unsolved term
is the exact Douglas quotient of that centered cross.

## 1. Sharp asymptotic of the chain constant

Recall

\[
 A_N=\sum_{n\le N}w_n
 \left[1-\cos{\pi\over\lceil L/\log n\rceil+1}\right],
 \quad w_n={\Lambda(n)\over\sqrt n},\quad L=\log N.  \tag{1.1}
\]

Fix \(K>0\).  For

\[
 Ne^{-K}\le n<N
\]

and all sufficiently large \(N\),

\[
 1<{L\over\log n}<2,
\]

so \(\lceil L/\log n\rceil=2\) and the bracket in (1.1) is exactly

\[
 1-\cos(\pi/3)={1\over2}.                            \tag{1.2}
\]

The PNT and partial summation give

\[
 \sum_{n\le x}{\Lambda(n)\over\sqrt n}
 =2\sqrt x+o(\sqrt x).                               \tag{1.3}
\]

Therefore

\[
 \liminf_{N\to\infty}{A_N\over\sqrt N}
 \ge1-e^{-K/2}.                                      \tag{1.4}
\]

Letting \(K\to\infty\) gives the lower limit at least one.

Except for a possible atom at \(n=N\), every bracket in (1.1) is at most
\(1/2\).  That atom has size \(O(\log N/\sqrt N)=o(\sqrt N)\).  Hence

\[
 A_N\le{1\over2}\sum_{n\le N}w_n+o(\sqrt N)
 =(1+o(1))\sqrt N.                                   \tag{1.5}
\]

Equations (1.4)--(1.5) prove (0.1).

## 2. Semigroup split at the global gap

D.185 proves

\[
 \widehat{\mathcal R}_T\ge A_NI.                     \tag{2.1}
\]

Functional calculus gives (0.2), and

\[
 \|H_{\theta,N}\|
 \le\sup_{\lambda\ge A_N}{e^{-\theta\lambda/A_N}\over\lambda}
 ={e^{-\theta}\over A_N}.                            \tag{2.2}
\]

The semigroup is sub-Markov.  Integrating its \(L^1\)- and
\(L^\infty\)-contractions over an interval of length \(\theta/A_N\)
proves the first two bounds in (0.3).

The complete Gamma process and every jump \(j\log p\) remain in the
semigroup.  By D.182, \(K_{\theta,N}\) is dominated by a full-line
probability convolution integrated over the same time interval, whose
total mass is exactly \(\theta/A_N\).

## 3. Long-time load bridge

D.134 gives

\[
 \widehat{\mathcal W}_T^*\widehat{\mathcal W}_T
 \le M_NI.                                           \tag{3.1}
\]

The added zero-extension boundary energy occurs on both sides, but the
same bound has leading prime mass \(2\sum w_n\).  Equation (1.3) gives
(0.4).  Therefore

\[
 \|\widehat{\mathcal W}_TH_{\theta,N}
       \widehat{\mathcal W}_T^*\|
 \le M_N{e^{-\theta}\over A_N}
 =(4e^{-\theta}+o(1)).                               \tag{3.2}
\]

Taking \(\theta=3\) proves (0.5).  This estimate is global and does not
use a fixed-depth expansion.

## 4. Localized endpoint block

On an integer cell, D.164 gives the exact Gram

\[
 \|\mathcal B_N\|^2=V_N+H_N
 =\left({1\over2}+o(1)\right)(\log N)^2.             \tag{4.1}
\]

The \(L^2\)-norm of \(K_{\theta,N}\) is also at most \(\theta/A_N\), so

\[
 \|\mathcal B_N^*K_{\theta,N}\mathcal B_N\|
 \le{\theta\over A_N}\|\mathcal B_N\|^2,             \tag{4.2}
\]

which proves (0.6).  D.183 gives the stronger pathwise statement that
every localized insertion preserves the exact higher Witt Grams; D.187
now makes their sum uniform in the full depth range.

## 5. Residual unit-budget statement

Let \(D_{\rm old}=I-T_{\rm old}\) and let \(q_N\) be the actual
Tate-centered old–born cross.  D.175 reduces the non-telescoping capacity
to

\[
 q_N^*D_{\rm old}^\dagger q_N.                       \tag{5.1}
\]

Equations (0.5)--(0.6) prove that the reference kernels used to construct
\(q_N\) have a uniformly convergent short/long expansion.  D.187 proves
the same for all arithmetic word depths.  To finish the Schur budget one
still needs

\[
 q_N=D_{\rm old}^{1/2}a_N,\qquad
 \|a_N\|^2\le\hbox{born diagonal margin}.             \tag{5.2}
\]

No reference norm estimate implies (5.2), by D.186.  It is the unique
remaining sign-sensitive statement.


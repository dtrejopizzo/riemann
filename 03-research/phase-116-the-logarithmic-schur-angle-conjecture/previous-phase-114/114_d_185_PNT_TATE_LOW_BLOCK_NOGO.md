# D.185 — PNT plus two Tate moments cannot close the low block

## Verdict

The finite-rank estimate of D.180--D.184 does not imply a small
finite-block capacity.  More sharply, neither the prime number theorem
with its classical zero-free-region error nor the two Tate moments can
control the centered discrepancy on the band required by the crude high
geometric sum.

Let

\[
 E_N(\tau)=
 \sum_{n\le N}{\Lambda(n)\over\sqrt n}e^{-i\tau\log n}
 -{N^{1/2-i\tau}-1\over1/2-i\tau}.                  \tag{0.1}
\]

Writing \(A(x)=\psi(x)-x\) and \(s=1/2+i\tau\), Stieltjes integration by
parts gives the exact identity

\[
 \boxed{
 E_N(\tau)=N^{-s}A(N)
 +s\int_1^NA(x)x^{-s-1}\,dx.}                       \tag{0.2}
\]

Even the hypothetical RH estimate

\[
 A(x)=O(\sqrt x\log^2x)                              \tag{0.3}
\]

would yield by absolute values only

\[
 |E_N(\tau)|=O\bigl(\log^2N+(1+|\tau|)\log^3N\bigr). \tag{0.4}
\]

For the D.184 band \(|\tau|\le R=N^{4/5}\), (0.4) is much larger than the
available logarithmic reference scale.  The classical PNT error is weaker.

This is not merely a defect of that calculation.  There exist smooth
signed perturbations of the continuous Chebyshev measure which:

1. satisfy a relative PNT error \(O(e^{-\sqrt{\log x}})\);
2. have two prescribed Tate-type moments equal to zero exactly;
3. have a Fourier spike at some \(|\tau|\le N^{4/5}\) of size
   \[
   \asymp \sqrt N\,e^{-\sqrt{\log N}}.               \tag{0.5}
   \]

Thus no theorem whose arithmetic hypotheses are only a PNT remainder and
two linear moments can prove the needed low-block bound.  The missing
input must use the exact multiplicative correlations of \(\Lambda\), an
Euler-product/de Branges positivity, or an equivalent new estimate.

This is a route no-go, not evidence that the actual \(\Lambda\) violates
the desired inequality.

## 1. Exact Abel formula

Since

\[
 \sum_{n\le N}\Lambda(n)n^{-s}=\int_{1^-}^Nx^{-s}\,d\psi(x)
\]

and

\[
 {N^{1-s}-1\over1-s}=\int_1^Nx^{-s}\,dx,
\]

their difference is \(\int_{1^-}^Nx^{-s}\,dA(x)\).  Integration by parts
proves (0.2), with the harmless convention at \(x=1\).

Under (0.3),

\[
 |N^{-s}A(N)|=O(\log^2N),
\]

and

\[
 |s|\int_1^N|A(x)|x^{-3/2}dx
 =O\left((1+|\tau|)\int_1^N{\log^2x\over x}\,dx\right)
 =O((1+|\tau|)\log^3N),
\]

which proves (0.4).  Hence even assuming the conclusion's standard PNT
consequence does not close this particular absolute-value estimate.

## 2. Exact resonant countermodel

Put \(u=\log x\), choose a large \(L\), set

\[
 R_L=e^{4L/5},\qquad \varepsilon_L=e^{-\sqrt L},
\]

and work on \(L\le u\le L+1\).  Perturb \(d\psi=dx\) there by

\[
 dA_L(x)=\varepsilon_L\cos(R_L(u-L))\,dx
 +dC_L(x),                                           \tag{2.1}
\]

where \(dC_L\) is a linear combination of two fixed smooth densities on
the same block, chosen to annihilate two prescribed independent moments.

Before the correction, every fixed smooth moment of the oscillatory term
is \(O(\varepsilon_Le^L/R_L)\) by integration by parts.  The \(2\times2\)
moment matrix of the two fixed correctors is nonsingular, so their
coefficients are

\[
 O(\varepsilon_L/R_L).                               \tag{2.2}
\]

Consequently the cumulative error throughout the block satisfies

\[
 |A_L(x)|\ll {\varepsilon_L\over R_L}x
 \le\varepsilon_Lx,                                  \tag{2.3}
\]

which is stronger than the stated relative PNT error.

After multiplying by \(x^{-1/2}\), the resonant Fourier value at
\(\tau=R_L\) contains

\[
\begin{aligned}
 \varepsilon_Le^{L/2}\int_0^1e^{v/2}
 \cos(R_Lv)e^{-iR_Lv}\,dv
 &={\varepsilon_Le^{L/2}\over2}\int_0^1e^{v/2}dv\\
 &\quad+O(\varepsilon_Le^{L/2}/R_L).                 \tag{2.4}
\end{aligned}
\]

The correcting densities contribute only
\(O(\varepsilon_Le^{L/2}/R_L^2)\) at this frequency.  Thus (2.4) is
\(\asymp\varepsilon_Le^{L/2}\), which is (0.5), while both prescribed
moments vanish exactly.

Disjoint blocks with \(L\to\infty\) produce one global smooth countermodel.
It has no Euler product and is not claimed to model the von Mangoldt
function beyond the hypotheses explicitly listed.  Its purpose is to
prove logical insufficiency of those hypotheses.

## 3. The high/low exponent tradeoff

The crude, depth-uniform high-word contraction of D.184 requires

\[
 c>{1\over\sqrt2(1-\eta)}=0.714\ldots                \tag{3.1}
\]

when \(R=N^c\).  A frequency \(R\) resolves logarithmic spacings of order
\(R^{-1}\), corresponding near \(N\) to additive intervals of length

\[
 H\asymp{N\over R}=N^{1-c}.                          \tag{3.2}
\]

At the threshold (3.1), \(1-c<0.286\).  The global PNT contains no such
short-interval information.  Formula (2.4) shows why a first-moment
estimate cannot manufacture it.

This tradeoff is exact for the current crude split:

* increasing \(c\) makes the high Green word contractive;
* increasing \(c\) also enlarges the low band and asks for finer signed
  prime distribution;
* two Tate conditions remove two coherent modes, not an
  \(O(N^c\log N)\)-dimensional band.

## 4. Correct pivot

There are two noncircular exits.

1. Prove a **uniform-in-depth** Witt simplex majorant strong enough to sum
   the high words with \(c<1/2\).  Fixed-\(k\) asymptotics are insufficient.
2. Prove the low capacity directly from the exact Euler/de Branges
   structure, without replacing \(E_N\) by a PNT remainder.

In either route the required conclusion is the full normalized Schur
budget from D.184,

\[
 {\|y_{\rm hi}\|^2\over1-\rho^2}
 +\mathrm{Cap}_{\rm lo}
 +\mathrm{Cap}_{\rm cross}\le1.              \tag{4.1}
\]

A finite rank, a convergent return series, or a PNT bound alone proves
none of the three terms has the required unit budget.


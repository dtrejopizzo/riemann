# D.130 — exact sign and normalization audit at the first three-contact window

## Verdict

At (T=\tfrac12\log 5), the apparent negative Ritz value reported by the
first floating assembly was not a negative value of the completed primitive
Weil form.  Its contact selector used midpoint matching rather than the
common refinement, and its Gamma block was only a numerically defective
moderate approximation.  Re-evaluating that original selected vector by
direct common-refinement integration and direct Fourier evaluation gives

\[
 Q_W(F)=-B_{\rm nuc}(F,F)
 =-0.1512496093135758+0.2010703419259205
 =0.0498207326123447>0.
\]

After rebuilding the contact matrix itself by common refinement and
reselecting the lowest vector, the stress test becomes substantially closer
to the boundary:

\[
 Q_W(F)=0.1210703574720051-0.1210699815814595
       =3.7589054554\,10^{-7}>0
\]

before the remaining positive Gamma tail.  The matrix Ritz value
(-0.0018707978) is the same-cell Gamma quadrature defect; direct Fourier
evaluation removes it.  This is a normalization audit, not an endpoint
certificate and not a proof of row D.  It removes both floating candidates
as counterexamples and fixes the exact convention to be used in the
jet/moment pullback.  The paper is not modified.

## 1. Central transform and the sign of the finite contacts

For a multiplicative test (f), put

\[
 F(t)=e^{t/2}f(e^t),
 \qquad
 f^*(x)=x^{-1}\overline{f(x^{-1})}.
\]

If (h=f*f^*), then its central additive transform is the ordinary
correlation convolution

\[
 H(t)=e^{t/2}h(e^t)=F*\widetilde F(t),
 \qquad \widetilde F(t)=\overline{F(-t)}.
\]

Consequently

\[
 H(a)=\int_{\mathbb R}F(u)\overline{F(u-a)}\,du,
 \qquad H(-a)=\overline{H(a)}.
\]

The finite side of the completed Lefschetz distribution is

\[
 B_{{\rm nuc},{\rm fin}}(f,f)
 =2\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
       \mathrm{Re}\,H(\log n).
\]

Therefore the row-D form (Q_W=-B_{\rm nuc}) has finite part

\[
 Q_{W,{\rm fin}}(F)
 =-2\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
       \mathrm{Re}\,\langle F,S_{\log n}F\rangle.       \tag{1.1}
\]

The minus sign in (1.1) agrees with the spectral identity: after the two
polar moments vanish,

\[
 -B_{\rm nuc}(f,f)=\sum_\rho m_\rho
 G(z_\rho)\overline{G(\overline{z_\rho})}.
\]

On RH this becomes a sum of squares.  Thus neither the finite-contact sign
nor the global sign may be reversed in an attempted positivity proof.

## 2. Which contacts occur at (T=\tfrac12\log5)

Since a translate can overlap the support only for (log n<2T=log5),
the interior contacts are exactly

\[
 n=2,3,4.
\]

The endpoint (n=5) has zero Lebesgue overlap.  The three weights are

\[
 {\Lambda(2)\over\sqrt2}={\log2\over\sqrt2},\qquad
 {\Lambda(3)\over\sqrt3}={\log3\over\sqrt3},\qquad
 {\Lambda(4)\over\sqrt4}={\log2\over2}.                 \tag{2.1}
\]

In particular the (p^2) term uses (Lambda(p^2)=\log p), not
(2\log p).  The direct correlations of the selected primitive vector are

\[
\begin{array}{c|r|r}
n&\mathrm{Re}\,\langle F,S_{\log n}F\rangle
  &-2\Lambda(n)n^{-1/2}\mathrm{Re}\,\langle F,S_{\log n}F\rangle\\ \hline
2&  0.3483692194407488&-0.3414917642905753\\
3& -0.2830855046821839& 0.3591132694590929\\
4&  0.2436295194127086&-0.1688711144820934
\end{array}
\]

Their total is (-0.1512496093135758).

## 3. Why the first contact matrix was wrong

The seven macrocells encode the initial overlap endpoints, but neither they
nor their independent subdivisions are closed under the translations.  For
example, translating one such endpoint by (log2) need not produce another
endpoint.  The first sparse contact matrix nevertheless paired microcells by
index and midpoint.  That is invalid when a translate crosses distinct
microcell boundaries; the (n=3) contribution is the most visible victim.

For cells (I_i=[l_i,r_i]), (I_j=[l_j,r_j]) and shift (a), the exact
overlap is instead

\[
 [\max(l_i,l_j-a),\min(r_i,r_j-a)].                     \tag{3.1}
\]

On each nonempty interval (3.1), both factors are degree-nine
polynomials.  Ten-point Gauss--Legendre quadrature is therefore exact up to
binary floating roundoff.  The independent implementation
`114_d_86_log5_direct_overlap.py` agrees with the term-breakdown common
refinement to better than (10^{-13}).

## 4. The complete Gamma multiplier

With Fourier convention

\[
 G(\tau)=\int_{-T}^{T}F(t)e^{-i\tau t}\,dt,
\]

the completed archimedean contribution to (Q_W) is

\[
 Q_{W,\infty}(F)
 ={1\over2\pi}\int_{\mathbb R}
 \left(\mathrm{Re}\,\psi\!\left({1\over4}+{i\tau\over2}\right)
       -\log\pi\right)|G(\tau)|^2\,d\tau.              \tag{4.1}
\]

Equivalently, writing

\[
 m_0=\log\pi-\psi(1/4),
\]

the positive Gamma jump Laplacian has symbol

\[
 \ell_\infty(\tau)
 =\mathrm{Re}\,\psi\!\left({1\over4}+{i\tau\over2}\right)
  -\psi(1/4),
\]

and (4.1) has symbol (ell_\infty-m_0).  Direct Fourier integration of
(4.1) for the selected vector gives

\[
 Q_{W,\infty}(F)=0.2010703419259205.
\]

The old truncated matrix gave (-0.00717); it was not the multiplier
(4.1).  It therefore cannot be combined with the exact contact block to
evaluate (Q_W).

## 5. Polar jets and primitive restriction

The two polar moments are

\[
 M_+(F)=\int_{-T}^{T}F(t)e^{t/2}\,dt,
 \qquad
 M_-(F)=\int_{-T}^{T}F(t)e^{-t/2}\,dt.                 \tag{5.1}
\]

For (G(z)=\int F(t)e^{-izt}dt), these are exactly

\[
 M_+(F)=G(i/2),\qquad M_-(F)=G(-i/2).                  \tag{5.2}
\]

The full completed formula contains the polar bilinear form

\[
 2\mathrm{Re}\,\bigl(M_-(F)\overline{M_+(F)}\bigr).
\]

It vanishes only after orthogonal projection to the exact kernel of both
moments.  Numerical penalty removal is not a substitute for this exact
projection.  Equations (1.1), (4.1), and (5.2) are the normalization gate
for every subsequent pullback comparison.

## 6. Consequence for the decisive comparison

The two jets are exactly the two primitive moments, and the source-derived
operator containing every (p^k) and the complete Gamma oscillator pulls
back to

\[
 -B_{{\rm nuc},X}^{\rm prim}
 =P_T\bigl(L_X-(2A_X+m_0)I\bigr)P_T,
\]

or, after Fourier transform, to the Toeplitz compression

\[
 P_TT_{r_X}P_T,
\quad
 r_X(\tau)=
 2\sum_{p^k\le X}{\log p\over p^{k/2}}
       (1-\cos(k\tau\log p))
 +\ell_\infty(\tau)-(2A_X+m_0).
\]

Thus the requested identification and pullback are exact.  What remains is
to prove positivity of this already fixed primitive operator uniformly in
(X,T); changing signs, deleting prime powers, or truncating Gamma cannot
serve as that proof.

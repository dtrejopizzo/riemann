# D.80 — Primitive Poisson telescope and conservation of Schur mass

## Status

D.79 proves that a finite ordered correction cannot remove the
Fourier--Poisson cross channel.  This note constructs the natural infinite
resolution suggested by the primitive approximate identity of D.75 and
computes both of its boundary terms.

There are two unconditional convergence results.  The primitive averaging
remainder tends to zero in the Gamma graph norm, and its full row-C nuclear
character tends to zero without RH because its Mellin multiplier is a
strict contraction at every nonpolar point of the critical strip.  At a
fixed Poisson window, the alternating-projection remainder is `C^N`, where
`C=P P_hat P`; it tends to zero in trace norm because `C` is a positive
trace-class contraction with no eigenvalue `1`.

The calculation nevertheless does not prove effectivity.  The positive
Schur channel is not the limiting boundary: it is the **sum of all the
interior boundary layers**.  Explicitly, it is a convergent infinite sum of
positive squares plus a remainder whose trace tends to zero.  Domination of
that complete positive tower by the supported negative channel is exactly
`B_nuc<=0` on the primitive image.  Thus boundary convergence is proved;
the extra estimate which would turn it into row D is identified exactly and
is equivalent to row D, not a consequence of the telescope.

Every identity is source-defined and retains all `p^k` and the complete
Gamma term.  No RH or sign-dependent spectral polarization is used.  The
paper is not modified.

## 1. The primitive averaging pair

Fix `R>0` and, on the logarithmic line, put

\[
 \mathcal A_R
 ={S_R+S_{-R}\over2\cosh(R/2)},
 \qquad
 \mathcal E_R=I-\mathcal A_R.                              \tag{1.1}
\]

The convolution kernel of `E_R` is the D.75 measure

\[
 \epsilon_R
 =\delta_0-{\delta_R+\delta_{-R}\over2\cosh(R/2)}.        \tag{1.2}
\]

For the two Tate characters,

\[
 \chi_\pm(\mathcal A_R)=1,
 \qquad \chi_\pm(\mathcal E_R)=0.                         \tag{1.3}
\]

Hence `E_R` sends every compact measure to the primitive ideal, `A_R`
preserves that ideal, and both maps commute with translations, Tate
involution and the Gamma oscillator.  Their supports satisfy

\[
 \mathrm{supp}(\mathcal A_R^NF)
 \subseteq\mathrm{supp}(F)+[-NR,NR].                \tag{1.4}
\]

The exact telescope is

\[
 I=\sum_{j=0}^{N-1}\mathcal E_R\mathcal A_R^j
       +\mathcal A_R^N.                                    \tag{1.5}
\]

Thus (1.5) is a directed resolution by compact primitive charts; no
individual periodic Dirac is regularized.

## 2. Gamma graph convergence

On the unitary logarithmic representation,

\[
 \|\mathcal A_R\|
 \le \eta_R:={1\over\cosh(R/2)}<1.                         \tag{2.1}
\]

Let

\[
 \|F\|_\Gamma^2=\|F\|_2^2+\|\partial_\infty F\|_2^2.      \tag{2.2}
\]

Since `partial_infinity` is a translation-invariant multiplier,

\[
 \boxed{
 \|\mathcal A_R^NF\|_\Gamma
 \le\eta_R^N\|F\|_\Gamma.}                               \tag{2.3}
\]

In particular the Gamma boundary obeys

\[
 \begin{aligned}
 &\left|m_0\|\mathcal A_R^NF\|^2
       -\|\partial_\infty\mathcal A_R^NF\|^2\right|\\
 &\qquad\le \max(m_0,1)\eta_R^{2N}\|F\|_\Gamma^2
 \longrightarrow0.                                       \tag{2.4}
 \end{aligned}
\]

This is a genuine uniform graph-norm estimate.  The corresponding estimate
for the finite-prime distribution does not follow from (2.3) alone: the
support in (1.4) expands at exactly the central Tate exponent, so the number
of newly active prime contacts grows while the Hilbert norm decays.  Full
trace convergence must use the global Poisson character, not an absolute
place-by-place norm.

## 3. Exact preservation of the local character

Because `A_R` commutes with every shift, every finite stage retains the
complete local formula

\[
 \begin{aligned}
 B_{\rm nuc}(\mathcal A_R^NF,\mathcal A_R^NG)
={}&\sum_p\log p\sum_{k\ne0}p^{-|k|/2}
 \langle\mathcal A_R^NF,
 S_{k\log p}\mathcal A_R^NG\rangle\\
 &+m_0\langle\mathcal A_R^NF,\mathcal A_R^NG\rangle
 -\langle\partial_\infty\mathcal A_R^NF,
          \partial_\infty\mathcal A_R^NG\rangle .         \tag{3.1}
\end{aligned}
\]

At a fixed `N` the support is compact, so (3.1) has exactly the same finite
support stabilization as D.73; no power `p^k` has been discarded.

The quadratic Euler telescope is

\[
 \begin{aligned}
 B_{\rm nuc}(F,G)
={}&\sum_{j=0}^{N-1}\bigl[
 B_{\rm nuc}(\mathcal A_R^jF,\mathcal A_R^jG)
 -B_{\rm nuc}(\mathcal A_R^{j+1}F,
              \mathcal A_R^{j+1}G)\bigr]\\
 &+B_{\rm nuc}(\mathcal A_R^NF,\mathcal A_R^NG).          \tag{3.2}
\end{aligned}
\]

Equation (3.2) is trace-compatible but alternating.  The bracket is a
two-chart Euler difference, not an ordered square.

## 4. Nuclear convergence of the primitive boundary

The central Mellin symbol of `A_R` is

\[
 a_R(s)={\cosh(R(s-1/2))\over\cosh(R/2)}.                  \tag{4.1}
\]

It satisfies

\[
 a_R(0)=a_R(1)=1.                                         \tag{4.2}
\]

If `0<Re(s)<1`, write `R(s-1/2)=x+iy`.  Then `|x|<R/2` and

\[
 |\cosh(x+iy)|^2=\sinh^2x+\cos^2y
 \le\cosh^2x<\cosh^2(R/2).                               \tag{4.3}
\]

Therefore

\[
 \boxed{|a_R(s)|<1\quad(0<\mathrm{Re}\,s<1).}         \tag{4.4}
\]

The row-C character is nuclear on the smooth compact test algebra.  Under
its spectral expansion, applying `A_R^N` to both entries multiplies the
term paired at `s` and `1-s` by

\[
 a_R(s)^Na_R(1-s)^N=a_R(s)^{2N}.                           \tag{4.5}
\]

The two polar terms at `s=0,1` vanish on the primitive ideal.  Every other
spectral point lies in the open strip and hence its factor in (4.5) tends
to zero.  The original nuclear summability supplies a dominating summable
family, since `|a_R(s)|<=1` on the closed strip.  Dominated convergence
gives

\[
 \boxed{
 B_{\rm nuc}(\mathcal A_R^NF,\mathcal A_R^NG)
 \longrightarrow0}                                       \tag{4.6}
\]

for primitive smooth compact `F,G`.

This proof uses the already established row-C nuclear character and the
classical fact that its nonpolar spectrum is in the open critical strip.
It uses neither the critical-line assertion nor a sign of the character.
On the prime side, (4.6) is the global cancellation of all the terms in
(3.1), including Gamma; it is not termwise decay of absolute local norms.

## 5. The alternating-projection boundary

At a fixed regularized semilocal window let

\[
 P=P_\Lambda,
 \qquad \widehat P=U^*PU,
 \qquad C=P\widehat PP:PH\longrightarrow PH.              \tag{5.1}
\]

The time--frequency limiting operator `C` is positive and trace class, and

\[
 0\le C\le I.                                              \tag{5.2}
\]

There is no eigenvalue `1`.  Indeed, an eigenvector with eigenvalue `1`
would belong simultaneously to the position-supported and
Fourier-supported subspaces.  Paley--Wiener analytic continuation forces
such a vector to be zero.  If `(lambda_j)` are the eigenvalues, then

\[
 0\le\lambda_j<1,
 \qquad \sum_j\lambda_j=\mathrm{Tr}\,C<\infty.        \tag{5.3}
\]

For `N>=1`, `lambda_j^N<=lambda_j`; hence dominated convergence proves

\[
 \boxed{\|C^N\|_1=\mathrm{Tr}(C^N)
       =\sum_j\lambda_j^N\longrightarrow0.}               \tag{5.4}
\]

The associated ordered telescope is

\[
 I-C^N=\sum_{j=0}^{N-1}C^j(I-C),                           \tag{5.5}
\]

or, for `x in PH`,

\[
 \|x\|^2
 =\sum_{j=0}^{N-1}|(I-C)^{1/2}C^{j/2}x\|^2
  +\|C^{N/2}x\|^2.                                       \tag{5.6}
\]

Thus an infinite Poisson resolution with a trace-zero terminal boundary
does exist at every fixed window.

## 6. Exact Schur residual after `N` stages

Relative to `PH direct-sum QH`, write

\[
 \widehat P=\begin{pmatrix}C&\beta\\\beta^*&\delta\end{pmatrix},
 \qquad D=C-I.                                             \tag{6.1}
\]

The projection equation gives

\[
 \beta\beta^*=C(I-C).                                     \tag{6.2}
\]

Let

\[
 \beta=[C(I-C)]^{1/2}V                                   \tag{6.3}
\]

be its polar decomposition on the generic part.  The positive Schur
channel of the Hermitian corner is

\[
 S=-{1\over4}\beta^*D^\dagger\beta
   ={1\over4}V^*CV.                                       \tag{6.4}
\]

Applying (5.5) to `C`, now starting at `C`, gives the exact `N`-stage
decomposition

\[
 \boxed{
 S={1\over4}\sum_{j=1}^N
 V^*C^j(I-C)V+S_N,}                                       \tag{6.5}
\]

where

\[
 \boxed{S_N={1\over4}V^*C^{N+1}V\ge0.}                   \tag{6.6}
\]

Every interior term is a square:

\[
 {1\over4}V^*C^j(I-C)V
 =K_j^*K_j,
 \qquad
 K_j={1\over2}(I-C)^{1/2}C^{j/2}V.                        \tag{6.7}
\]

By (5.4),

\[
 \|S_N\|_1\le {1\over4}\|C^{N+1}\|_1\longrightarrow0.  \tag{6.8}
\]

But (6.5) also gives

\[
 \mathrm{Tr}\,S
 ={1\over4}\sum_{j\ge1}\|C^{j/2}(I-C)^{1/2}V\|_{\rm HS}^2.
                                                                  \tag{6.9}
\]

Thus the positive Schur mass has **not** gone to zero.  Only its terminal
remainder has.  The mass has been transferred into the infinite family of
interior positive charts.

## 7. The exact additional estimate

After the congruence of D.78, pull the semilocal corner back along the
primitive A--B--C realization.  Denote its negative supported coordinate
by `L_-F` and its auxiliary coordinate by `q(F)`.  Equations (6.5)--(6.8)
give

\[
 \begin{aligned}
 B_{\rm nuc}(F,F)
 ={}&-\|L_-F\|^2
   +\sum_{j=1}^N\|K_jq(F)\|^2
   +\langle q(F),S_Nq(F)\rangle.                           \tag{7.1}
\end{aligned}
\]

The local evaluation of the left side is (3.1), so (7.1) still contains
all prime powers and Gamma.  Passing to the limit using (6.8),

\[
 \boxed{
 B_{\rm nuc}(F,F)
 =-\|L_-F\|^2+\sum_{j\ge1}\|K_jq(F)\|^2.}                \tag{7.2}
\]

The condition which converts the trace-zero boundary into effectivity is
therefore exactly

\[
 \boxed{
 \sum_{j\ge1}\|K_jq(F)\|^2\le\|L_-F\|^2
 \quad\text{for every primitive }F.}                      \tag{7.3}
\]

By (7.2), (7.3) is equivalent to

\[
 B_{\rm nuc}(F,F)\le0
 \quad\text{on }\ker M_-\cap\ker M_+.                     \tag{7.4}
\]

This is precisely row D (and, through the already established Weil
criterion, the RH sign statement).  In Douglas form, (7.3) says that the
row operator

\[
 F\longmapsto(K_jq(F))_{j\ge1}                             \tag{7.5}
\]

factors contractively through `F mapsto L_-F`.  Constructing that
contraction from the Poisson geometry would be a noncircular proof;
declaring (7.3) from the vanishing of `S_N` would omit the entire positive
series in (7.2).

## 8. Audit of the two possible limits

The two telescopes answer different analytic questions:

1. `A_R^N` is compactly generated, primitive and directed.  Its Gamma
   graph boundary tends to zero by (2.3), and its full character tends to
   zero by the nuclear dominated-convergence argument (4.6).
2. `C^N` is the intrinsic alternating-projection boundary.  It tends to
   zero in trace norm by (5.4), and makes the Schur layers explicit through
   (6.5).

Neither limit orders the Euler differences in (3.2), and neither cancels
the positive sum in (7.2).  This is the precise reason why an infinite
resolution can have a vanishing boundary without proving the desired
inequality.

## 9. Noncircular continuation

The remaining route is now narrower than the abstract request for an
infinite resolution.  The resolution and its trace convergence are already
constructed.  What remains is to build, from A--B--C data and before taking
a sign, a chain map

\[
 \mathcal K=(K_jq)_{j\ge1}=\mathcal C L_-                \tag{9.1}
\]

whose comparison `C` is a contraction for a geometric reason independent
of (7.4).  Possible inputs must couple finite places and Gamma globally;
placewise maps are excluded by D.76.  Any proposed construction can now be
tested against the exact identities (3.1), (6.5) and (7.2).

## 10. Conclusion

The primitive Poisson telescope exists, preserves every local contact and
has a vanishing nuclear boundary.  The alternating-projection telescope
also has a vanishing trace-class boundary.  These are genuine advances over
the finite-chart audit.

The computation of the residual is decisive: the terminal Schur remainder
is `S_N=(1/4)V*C^(N+1)V` and tends to zero, but the total positive Schur
mass survives as the sum of the squares `K_j*K_j`.  Domination of that sum
by the supported leakage is exactly the row-D inequality.  Hence the next
step is not another convergence proof; it is a geometric construction of
the contraction (9.1).


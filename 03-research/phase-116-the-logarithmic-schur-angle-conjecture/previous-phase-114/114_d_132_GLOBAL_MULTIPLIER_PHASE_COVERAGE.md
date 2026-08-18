# D.132 — global prime-phase coverage and the Logvinenko--Sereda loss

## Verdict

For a support window \([-T,T]\), the exact primitive operator is the
Paley--Wiener compression of

\[
 r_T(\tau)=
 \operatorname {Re}\psi\!\left({1\over4}+{i\tau\over2}\right)-\log\pi
 -2\sum_{2\leq n<e^{2T}}{\Lambda(n)\over\sqrt n}
       \cos(\tau\log n).                                  \tag{0.1}
\]

Thus every prime power and the complete Gamma factor are present before
any estimate.  A multiscale B-spline averaging argument gives a new
unconditional geometric fact: outside a fixed central band, no connected
component of \(\{r_T<0\}\) has length exceeding

\[
 a_T=O(\log(2+T)).                                        \tag{0.2}
\]

This uses only the positivity of the coefficients and the frequency bands
\(\log n\), not zeta zeros.

The estimate is not yet strong enough for row D.  Converting (0.2) to a
measurable thick-set statement requires a derivative bound of size
\(O(T^2e^T)\).  The resulting thickness fraction is at best

\[
 \gamma_T\gg {e^{-T}\over T^2\log(2+T)}.                 \tag{0.3}
\]

Kovrijkine's quantitative Logvinenko--Sereda theorem then gives only

\[
 \int_{E_T}|G|^2
 \geq \exp\{-C T^2\log(2+T)\}\,\|G\|_2^2,                \tag{0.4}
\]

whereas positivity of (0.1) against its global negative lower bound would
require the mass on the positive set to be
\(1-O(e^{-T})\), not merely the tiny lower bound (0.4).

The large-sieve/Kronecker route has a different but worse loss.  Pairwise
orthogonality starts at interval length \(e^{2T}\); its
Logvinenko--Sereda exponent is \(Te^{2T}\).  Higher moments improve the
density of bad phases but enlarge the averaging scale to \(e^{2kT}\).
Hence neither generic route closes D.  The correct continuation is a
weighted prolate inequality exploiting the actual depth of the negative
wells, not only thickness of their complement.  The two Tate zeros remove
two prolate directions but do not alter these cofinal exponents.

No paper file is modified.

## 1. Exact multiplier and negative set

Put

\[
 A_T=\sum_{2\leq n<e^{2T}}{\Lambda(n)\over\sqrt n},
 \qquad
 D_T(\tau)=\sum_{2\leq n<e^{2T}}{\Lambda(n)\over\sqrt n}
 e^{i\tau\log n},                                       \tag{1.1}
\]

and

\[
 \Gamma(\tau)=
 \operatorname {Re}\psi\!\left({1\over4}+{i\tau\over2}\right)-\log\pi .
                                                                    \tag{1.2}
\]

Then

\[
 r_T(\tau)=\Gamma(\tau)-2\operatorname {Re}D_T(\tau).    \tag{1.3}
\]

The elementary bounds \(\Lambda(n)\leq\log n\) and
\(\sum_{n\leq X}n^{-1/2}\leq2\sqrt X\) give

\[
 A_T\leq4Te^T.                                           \tag{1.4}
\]

Since \(\Gamma\) is even and increasing on \([0,\infty)\),

\[
 r_T(\tau)\geq\Gamma(\tau)-2A_T.                         \tag{1.5}
\]

The asymptotic \(\Gamma(\tau)=\log|\tau|-\log(2\pi)+O(|\tau|^{-1})\)
therefore gives an unconditional positive tail, but (1.4) places its
elementary start near

\[
 \log R_T\asymp Te^T.                                    \tag{1.6}
\]

A direct prolate split at \(R_T\) has Shannon dimension
\(2TR_T/\pi\), already double exponential in the support parameter.  This
explains why the successful fixed-window split at \(T=\tfrac12\log5\)
does not directly globalize by the crude tail bound.

## 2. Pairwise large sieve

The frequencies \(\lambda_n=\log n\), \(n\leq X=e^{2T}\), satisfy

\[
 |\lambda_m-\lambda_n|
 \geq\log(1+1/X)\geq {1\over2X}\qquad(m\neq n).          \tag{2.1}
\]

The Montgomery--Vaughan form of Hilbert's inequality therefore yields,
for any interval \(I\) of length \(L\),

\[
 \int_I|D_T(\tau)|^2\,d\tau
 \leq(L+C X)V_T,                                        \tag{2.2}
\]

where

\[
 V_T=\sum_{n<X}{\Lambda(n)^2\over n}
 \leq\sum_{n<X}{(\log n)^2\over n}
 \leq {8\over3}T^3+O(T^2).                              \tag{2.3}
\]

Sharper prime counting improves (2.3) to \(V_T=O(T^2)\), but it does not
change the separation scale \(L\asymp X=e^{2T}\).

Chebyshev gives

\[
 {|\{\tau\in I:|D_T(\tau)|>u\}|\over |I|}
 \leq {C V_T\over u^2}\qquad(L\geq X).                  \tag{2.4}
\]

Taking \(u\) a large multiple of \(T^{3/2}\) gives a positive-density good
set in every interval of length \(e^{2T}\).  But a
\((\gamma,e^{2T})\)-thick set has Logvinenko--Sereda exponent

\[
 aT\asymp Te^{2T}.                                      \tag{2.5}
\]

The resulting sampling constant is far below what is needed to compare a
positive multiplier of polynomial size with the negative mass
\(M_T\asymp A_T\).

## 3. Higher moments and quantitative Kronecker scale

The \(k\)-th power \(D_T^k\) has frequencies

\[
 \log{m\over n},
 \qquad 1\leq m,n\leq X^k.
\]

Distinct such frequencies are separated by at least

\[
 \left|\log{m\over n}\right|\geq {1\over2X^k}.           \tag{3.1}
\]

Thus a \(2k\)-th moment time average begins to approximate the Bohr-torus
moment only on scales

\[
 L_k\gtrsim X^k=e^{2kT}.                                \tag{3.2}
\]

On the Bohr torus, the prime phases are independent.  Bernstein's
inequality for the centered local prime sums gives schematically

\[
 \mathbb P_{\mathrm{Bohr}}\{
 \operatorname {Re}D_T>u\}
 \leq
 \exp\!\left[-c\min\!\left({u^2\over V_T},{u\over b_*}\right)\right],
                                                                    \tag{3.3}
\]

where

\[
 b_*=\sup_p{\log p\over\sqrt p-1}<\infty.               \tag{3.4}
\]

This is a genuine phase-independence gain.  Its quantitative transfer back
to a physical \(\tau\)-interval, however, pays (3.2).  Increasing \(k\)
improves the density in (3.3) while worsening the sampling exponent from
\(Te^{2T}\) to \(Te^{2kT}\).  Baker bounds for more general integer linear
forms cannot improve the elementary rational separation (3.1) at the
moment order used here.

## 4. Multiscale B-spline no-long-excursion theorem

The preceding scale loss can be improved for the weaker question of
contiguous negative intervals.

Let \(\lambda_0=\log2\), and partition the active frequencies into bands

\[
 \mathcal B_j=[\lambda_j,2\lambda_j),
 \qquad \lambda_j=2^j\lambda_0,                           \tag{4.1}
\]

stopping when \(\lambda_j\geq2T\).  Let \(J_T\) be the number of nonempty
bands.  For a band define

\[
 A_j=\sum_{\log n\in\mathcal B_j}{\Lambda(n)\over\sqrt n}.
\]

The crude bound used in (1.4) gives

\[
 A_j\leq4\lambda_j e^{\lambda_j}.                         \tag{4.2}
\]

Let \(u_h=h^{-1}\mathbf1_{[-h/2,h/2]}\), put

\[
 h_j={2\pi\over\lambda_j},
\qquad
 m_j=
 \left\lceil{
 \lambda_j+\log(4\lambda_jJ_T/\varepsilon)
 \over\log\pi}\right\rceil,                              \tag{4.3}
\]

and set

\[
 \kappa_T=*_{j=0}^{J_T-1}u_{h_j}^{*m_j}.                 \tag{4.4}
\]

This is a nonnegative probability kernel.  If
\(\lambda\in\mathcal B_j\), then

\[
 |\widehat u_{h_j}(\lambda)|
 =\left|{\sin(h_j\lambda/2)\over h_j\lambda/2}\right|
 \leq {1\over\pi}.                                      \tag{4.5}
\]

All the other convolution factors have Fourier multiplier at most one.
Therefore

\[
 \begin{aligned}
 |D_T*\kappa_T|
 &\leq\sum_j A_j\pi^{-m_j}
 \leq\varepsilon.                                       \tag{4.6}
 \end{aligned}
\]

The total support length of \(\kappa_T\) is

\[
 a_T=\sum_jm_jh_j
 \leq C_\varepsilon\log(2+T).                            \tag{4.7}
\]

Indeed the leading contribution of each nonempty band is at most
\(2\pi/\log\pi+o(1)\), and \(J_T=O(\log(2+T))\).

> **Theorem 4.1 (multiscale no-long-excursion).**  
> No interval of length \(a_T\) can satisfy
> \(\operatorname {Re}D_T(\tau)>\varepsilon\) at every point.
> Consequently, wherever \(\Gamma(\tau)\geq2\varepsilon\), every connected
> component of \(\{r_T<0\}\) has length less than \(a_T\).

The proof is immediate: averaging a strict inequality
\(\operatorname {Re}D_T>\varepsilon\) against the probability kernel
\(\kappa_T\) contradicts (4.6).  This establishes (0.2).

## 5. From one good point to measurable thickness

To use Logvinenko--Sereda one needs positive measure, not merely one good
point.  Differentiate (1.3).  Since \(\log n\leq2T\),

\[
 |D_T'(\tau)|\leq2TA_T.                                  \tag{5.1}
\]

The trigamma series gives the uniform bound

\[
 0\leq\Gamma'(\tau)
 \leq{1\over2}\psi_1(1/4)<9
 \qquad(\tau\geq0).                                      \tag{5.2}
\]

Hence

\[
 |r_T'(\tau)|\leq 9+4TA_T
 \leq9+16T^2e^T=:L_T.                                   \tag{5.3}
\]

Choose a fixed \(g>0\), and let \(R_0\) be fixed so that
\(\Gamma\geq2\varepsilon+2g\) on \(|\tau|\geq R_0\).
Equation (4.6) supplies in every interval of length \(a_T\) lying outside
that central band a point with
\(\operatorname {Re}D_T\leq\varepsilon\), hence \(r_T\geq2g\).
The derivative bound gives an interval of length at least \(2g/L_T\) on
which \(r_T\geq g\).  Thus the set

\[
 E_{T,g}=\{\tau:r_T(\tau)\geq g\}
\]

is globally thick after enlarging the observation scale to
\(a'_T=2R_0+2a_T\): every interval of that length contains an exterior
subinterval of length \(a_T\).  Its parameters satisfy

\[
 a=a'_T,\qquad
 \gamma\geq{2g\over a'_TL_T}
 \gg_g{e^{-T}\over T^2\log(2+T)}.                        \tag{5.4}
\]

This proves (0.3).

## 6. Exact Logvinenko--Sereda loss

For \(G\in PW_T\), Kovrijkine's quantitative theorem has the form

\[
 \|G\|_{L^2(E_{T,g})}^2
 \geq
 \left({\gamma\over C}\right)^{C(aT+1)}
 \|G\|_2^2.                                             \tag{6.1}
\]

Inserting (4.7) and (5.4) gives

\[
 \eta_T:=
 \left({\gamma\over C}\right)^{C(aT+1)}
 \geq\exp\{-C_gT^2\log(2+T)\}.                           \tag{6.2}
\]

The direction of this estimate is important: it proves only that a
Paley--Wiener function leaves at least the tiny fraction \(\eta_T\) of its
mass on the positive set.

The global negative bound from (1.4) is

\[
 r_T\geq-M_T,\qquad M_T\leq m_0+8Te^T.                  \tag{6.3}
\]

Splitting the quadratic form between \(E_{T,g}\) and its complement gives
only

\[
 \langle r_TG,G\rangle
 \geq\bigl((g+M_T)\eta_T-M_T\bigr)\|G\|^2.              \tag{6.4}
\]

For positivity, (6.4) would require

\[
 \eta_T\geq{M_T\over M_T+g}=1-O_g(e^{-T}/T),             \tag{6.5}
\]

whereas (6.2) tends rapidly to zero.  The loss is therefore qualitative,
not a matter of optimizing a universal constant.

## 7. The two Tate zeros do not repair the generic sampling loss

The primitive space is

\[
 PW_T^0=\{G\in PW_T:G(i/2)=G(-i/2)=0\}.                 \tag{7.1}
\]

It has codimension two.  If \(K_N\) is the concentration operator on a
measurable negative region and its eigenvalues are
\(\lambda_1\geq\lambda_2\geq\cdots\), the min--max principle gives

\[
 \sup_{\substack{G\in PW_T^0\\\|G\|=1}}
 \langle K_NG,G\rangle\geq\lambda_3.                    \tag{7.2}
\]

Thus the two jets can remove at most two concentration directions.  They
are decisive for deleting the polar terms, but a negative region with
time--bandwidth product larger than two still has primitive functions
concentrated in it.  Generic Logvinenko--Sereda estimates are therefore
not strengthened cofinally by merely inserting the two zeros.

## 8. Surviving route

The fixed-window prolate method remains valid: if
\[
 r_T\geq-M,\qquad r_T\geq g>0\quad(|\tau|\geq R),
\]
then the complement of the first \(K\) prolate modes has lower bound
\[
 g-(g+M)\lambda_{K+1}(RT).
\]
The \(T=\tfrac12\log5\) calculation makes this quantitative with a
directed tail and a finite low block.

For cofinal \(T\), D.132 shows what a new theorem must improve.  It must
control the **weighted concentration on the actual negative wells**, not
only sample a thick subset of their complement.  A viable statement would
bound the concentration eigenvalues using both:

1. the multiscale phase widths from Section 4; and
2. the depth \(r_T^-\), whose large values require simultaneous phase
   alignment and whose Bohr probability has the Bernstein decay (3.3).

Such a weighted prolate/large-deviation inequality could reduce the low
space before the two Tate constraints are imposed.  The ordinary
Logvinenko--Sereda and pairwise large-sieve inequalities quantified above
do not.

## 9. Conclusion

The prime phases do give a uniform structural restriction:

\[
 \operatorname {length}(\text{each high negative component})
 =O(\log(2+T)).
\]

Pairwise and higher-moment phase independence also give density estimates,
but only on exponentially growing recurrence scales.  Once converted to a
generic Paley--Wiener sampling inequality, both mechanisms lose far more
than the multiplier can pay.

Therefore D132 neither assumes zero distribution nor claims D.  It
eliminates the unweighted Logvinenko--Sereda route in its present form and
isolates the sharper target: a weighted prolate inequality coupling
negative-well depth to arithmetic phase large deviations.

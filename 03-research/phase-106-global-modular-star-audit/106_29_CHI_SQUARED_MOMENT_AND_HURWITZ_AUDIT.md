# 106.29 — The extra \(\chi^2\) moment and the Hurwitz carrier audit

## Purpose

This note independently audits the partial-power-sum identity of 106.28 and
asks whether the prolate constraints contain one more usable moment.  There
is a genuine additional identity:

\[
 \int_\lambda^\infty(1-P_\lambda)\widehat f(t)\,dt
 =-\frac12\sum_j c_j\chi_j^2\psi_j(0)
 \tag{1}
\]

whenever \(f(0)=0\).  For the three-mode vector already used in 106.12,
the right side is in fact \(\Theta(d_4d_8)\), rather than merely
\(O(d_4)\).  With the four modes \(0,4,8,12\), it can be made exactly zero
without changing the leading leakage scale \(d_4\).

All Fourier-tail integrals in this note use the symmetric improper
convention inherited from 106.12.  They are ordinary integrals after the
interior smooth regularization used there.

This removes the continuum term in the Hurwitz decomposition.  It does not,
by itself, prove the uniform carrier estimate of 106.26: the remaining floor
kernel still requires an ordinate-uniform oscillatory estimate for the
specific exterior prolate solution.

## 1. Nonduplication audit

A semantic search through Phases 1--106 and Papers 1--39 found the
following related material:

1. 106.12 uses the two exact rows
   \(\psi_j(0)\) and \(\chi_j\psi_j(0)\) to impose
   \(f(0)=\int f=0\);
2. 106.12 proves the angle identity
   \(\|(1-P_\lambda)\widehat f\|_2^2
     =\sum_j|c_j|^2(1-\chi_j^2)\);
3. the Bernoulli lemmas of Phase 73 concern fixed-right-half-plane
   digamma remainders, not a co-Poisson floor sum of unbounded complex
   order;
4. 104.85 uses Hurwitz's convergence theorem, not the Hurwitz zeta
   function.

The CCM source contains the compressed-Fourier identity and

\[
 \int\psi_{j,\lambda}
 =\chi_j(\lambda)\psi_{j,\lambda}(0),
 \tag{2}
\]

but it does not form the exterior \(\chi_j^2\) moment (1), the partial
power sum of 106.28, or the three-row constrained vector below.  Suzuki's
Hurwitz and Hurwitz--Lerch formulas occur in the archimedean screw-function
expansion; they do not involve the co-Poisson floor, PSWF eigenvalues, or
the moment (1).  Thus (1) and the scale calculation below are not present
in either primary source.  Their ingredients are classical, so the novelty
claim is the combined lemma, not the individual Fourier or Vandermonde
identities.

## 2. Exact exterior-mass identity

Let

\[
 f=\sum_{r=0}^{m}c_r\psi_{4r,\lambda},
 \qquad
 a_r=\psi_{4r,\lambda}(0),
 \qquad
 x_r=a_rc_r,
 \tag{3}
\]

and put

\[
 \ell=(1-P_\lambda)\widehat f,
 \qquad
 \chi_r=\chi_{4r}(\lambda),
 \qquad
 q_r=1-\chi_r,
 \qquad
 d_r=1-\chi_r^2.
 \tag{4}
\]

### Lemma 1 — Exterior mass

If \(f(0)=0\), then

\[
 \boxed{
 M_0:=\int_\lambda^\infty\ell(t)\,dt
 =-\frac12\sum_{r=0}^{m}\chi_r^2x_r
 =\frac12\sum_{r=0}^{m}d_rx_r.}
 \tag{5}
\]

#### Proof

Fourier inversion, evenness, and (2) give

\[
\begin{aligned}
 2M_0
 &=\int_{|t|>\lambda}\widehat f(t)\,dt\\
 &=f(0)-\int_{-\lambda}^{\lambda}\widehat f(t)\,dt\\
 &=\sum_rx_r-\sum_r c_r\chi_r\int\psi_{4r,\lambda}\\
 &=\sum_rx_r-\sum_r\chi_r^2x_r.
\end{aligned}
\]

The first sum vanishes by hypothesis, proving both forms in (5).
\(\square\)

## 3. The existing three-mode vector has a double defect

For the normalized vector on modes \(0,4,8\), the two constraints are

\[
 \sum_{r=0}^{2}x_r=0,
 \qquad
 \sum_{r=0}^{2}\chi_rx_r=0,
 \tag{6}
\]

or equivalently \(\sum x_r=\sum q_rx_r=0\).  Before normalization take

\[
 x=(q_1-q_2,\ q_2-q_0,\ q_0-q_1).
 \tag{7}
\]

Let

\[
 \mathcal N_\lambda
 =\left(\sum_{r=0}^{2}\frac{|x_r|^2}{|a_r|^2}\right)^{-1/2}.
 \tag{8}
\]

Fixed-order prolate localization gives \(|a_r|\asymp1\), while

\[
 q_0\ll q_1\ll q_2,
 \qquad q_0/q_1,q_1/q_2=O(\lambda^{-8}).
 \tag{9}
\]

Hence \(\mathcal N_\lambda\asymp q_2^{-1}\).  Since
\(d_r=2q_r-q_r^2\), (6) yields

\[
 \sum_{r=0}^{2}d_rx_r
 =-\sum_{r=0}^{2}q_r^2x_r
 =(q_1-q_0)(q_2-q_1)(q_2-q_0).
 \tag{10}
\]

Therefore the normalized three-mode vector satisfies the sharper identity

\[
 \boxed{
 M_{0,\lambda}
 =\frac{\mathcal N_\lambda}{2}
  (q_1-q_0)(q_2-q_1)(q_2-q_0)
 \asymp q_1q_2\asymp d_4d_8.}
 \tag{11}
\]

Thus the estimate \(M_{0,\lambda}=O(d_4)\) in 106.28 is correct but loses
an entire fixed-order prolate defect.

## 4. Exact cancellation with four modes

On modes \(0,4,8,12\), impose

\[
 \boxed{
 \sum_{r=0}^{3}x_r=0,
 \qquad
 \sum_{r=0}^{3}\chi_rx_r=0,
 \qquad
 \sum_{r=0}^{3}\chi_r^2x_r=0.}
 \tag{12}
\]

Equivalently, \(x\) annihilates \(1,q,q^2\).  A nonzero spanning vector is

\[
 x_r=(-1)^r
 \prod_{\substack{0\le i<k\le3\\i,k\ne r}}(q_k-q_i),
 \qquad 0\le r\le3.
 \tag{13}
\]

The first two rows give \(f(0)=\int f=0\); the third row and (5) give

\[
 \boxed{M_{0,\lambda}=0.}
 \tag{14}
\]

This extra constraint does not consume the \(d_4\) angle scale.  Indeed,
using \(q_0\ll q_1\ll q_2\ll q_3\), (13) gives

\[
 |x_0|,|x_1|\asymp q_2q_3^2,
 \quad |x_2|\asymp q_1q_3^2,
 \quad |x_3|\asymp q_1q_2^2.
 \tag{15}
\]

Consequently

\[
 \sum_r|c_r|^2\asymp q_2^2q_3^4,
 \qquad
 \sum_rd_r|c_r|^2\asymp q_1q_2^2q_3^4,
 \tag{16}
\]

where the uniformly nonzero factors \(a_r\) have been absorbed in the
comparison constants.  After normalization,

\[
 \boxed{
 \|(1-P_\lambda)\widehat f\|_2^2\asymp q_1\asymp d_4.}
 \tag{17}
\]

Thus the leading continuum term in 106.28(13) can be deleted exactly
without weakening the prolate leakage budget.

## 5. What remains after the extra moment

At a zero \(\rho\), put \(w=\rho-1/2\).  The exact power-sum identity of
106.28 may be written

\[
 A_\lambda(w)+A_\lambda(-w)
 =\int_\lambda^\infty\ell(t)K_{\rho,\lambda}(t)\,dt,
 \tag{18}
\]

where

\[
 K_{\rho,\lambda}(t)
 =t^{-\rho}\sum_{n\le t/\lambda}n^{\rho-1}
  +t^{\rho-1}\sum_{n\le t/\lambda}n^{-\rho}.
 \tag{19}
\]

The two complete zeta constants have vanished because
\(\zeta(\rho)=\zeta(1-\rho)=0\).  Euler summation separates from (19) the
constant-in-\(t\) continuum carrier

\[
 C_{\rho,\lambda}
 =\frac{\lambda^{-\rho}}{\rho}
  +\frac{\lambda^{\rho-1}}{1-\rho}.
 \tag{20}
\]

Equation (14) annihilates its pairing with \(\ell\) exactly.  What remains
is precisely the joint periodic-floor term in 106.28(24).

This is a sharper reduction, not a carrier bound.  To see the missing
information directly, on the first cell \(\lambda\le t<2\lambda\),

\[
 K_{\rho,\lambda}(t)=t^{-\rho}+t^{\rho-1}.
 \tag{21}
\]

For fixed \(0<\beta<1\) and \(\rho=\beta+i\gamma\), the cross term in its
cellwise \(L^2(dt)\) norm is \(O(|\gamma|^{-1})\), while

\[
 \int_\lambda^{2\lambda}
 \left(t^{-2\beta}+t^{2\beta-2}\right)dt>0.
 \tag{22}
\]

Moreover \(C_{\rho,\lambda}=O_\lambda(|\gamma|^{-1})\).  Hence

\[
 \liminf_{|\gamma|\to\infty}
 \|K_{\rho,\lambda}-C_{\rho,\lambda}\|_{L^2([\lambda,2\lambda])}>0.
 \tag{23}
\]

Thus neither the extra scalar moment nor an \(L^2\) absolute estimate can
produce the ordinate decay \((1+|\gamma|)^{-q}\), \(q>1/2\), required in
106.26.  Equation (23) does not exclude an estimate for the specific PSWF
leakage: such an estimate must use its oscillatory phase (and, globally,
the two Mellin orientations), rather than only its norm and finitely many
moments.

## 6. Verdict

\[
\begin{array}{c|c}
\text{statement}&\text{status}\\ \hline
\text{co-Poisson/Hurwitz floor identity}
 &\text{genuinely absent from the audited sources}\\
M_{0,\lambda}\asymp d_4d_8\text{ for the three-mode vector}
 &\text{proved exactly up to fixed-order comparisons}\\
M_{0,\lambda}=0\text{ with modes }0,4,8,12
 &\text{proved exactly}\\
\text{extra moment with leakage }\asymp d_4
 &\text{proved}\\
\text{extra moment}\Longrightarrow\text{uniform FM carrier bound}
 &\text{false as a norm/moment-only inference}\\
\text{specific PSWF periodic-floor cancellation}
 &\text{open}.
\end{array}
\tag{24}
\]

No result in this note proves the diagonal Rayleigh limit, the
complementary inertia estimate, or RH.

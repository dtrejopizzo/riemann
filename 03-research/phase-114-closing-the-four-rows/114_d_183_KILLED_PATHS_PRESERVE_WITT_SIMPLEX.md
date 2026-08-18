# D.183 — Killed Lévy paths preserve the Witt simplex constant

## Verdict

The localized bulk term of D.181 does preserve the complete fixed-depth
Witt Gram of D.178.  The statement is an exact positive-kernel theorem.

Let \(K_1,\ldots,K_{k-1}\) be positive killed kernels on \(I_T\), and
assume that each is dominated by a full-line convolution

\[
 0\le K_jf\le\nu_j*\widetilde f\quad(f\ge0),
 \qquad \mu_j:=\|\nu_j\|_{\rm TV}.                  \tag{0.1}
\]

Insert them between the directed prime-power shifts in the depth-\(k\)
boundary synthesis.  Then on an integer cell,

\[
 \boxed{
 \|\mathcal B_{N,k}^{K_1,\ldots,K_{k-1}}\|^2
 \le\left(\prod_{j=1}^{k-1}\mu_j^2\right)
       (V_{N,k}+H_{N,k}),}                           \tag{0.2}
\]

where, with no prime power omitted,

\[
 V_{N,k}=\sum_{m\le N}{\Lambda_k(m)^2\over m},
 \qquad H_{N,k}={\Lambda_{2k}(N)\over\sqrt N}.       \tag{0.3}
\]

For the sub-Markov potentials of D.181--D.182,

\[
 \mu_j\le a^{-1}.                                   \tag{0.4}
\]

Therefore, after the natural normalization by one Gamma/reference factor
\(a\) per inserted inverse, the leading fixed-depth constant is unchanged:

\[
 \boxed{
 {V_{N,k}\over V_{N,1}^k}\longrightarrow
 \theta_k={2^kk!\over(2k)!}={1\over(2k-1)!!}.}       \tag{0.5}
\]

This proves the D.178 reference-resolvent word inequality for the
**directed arithmetic Witt boundary sector**, including every \(p^j\),
both shift directions, the Gamma paths inside the inverse, and boundary
killing.  The proof does not estimate a sum of prime weights and does not
assume that the killed operator commutes with shifts.

What remains after (0.2) is exactly the residual ledger of D.181:

* words with a high residual occurrence, carrying \(e^{-1}\) per such
  occurrence;
* words which meet the prolate-low/Tate block, of rank at most
  \(2TR/(\pi\eta)+2\).

Thus inverse realignment cannot destroy the simplex in the arithmetic
boundary sector.  This is not yet a statement about the complete cross
\(q\): D.177 proves that \(q\) also contains the nonzero centered
atomic--continuous discrepancy \(E_N\) and endpoint Volterra pieces.
Those terms are not automatically finite-dimensional and are not replaced
by (0.2).  In addition to the finite residual blocks, their localized
return words still have to be estimated.

## 1. Directed shifts and word collapse

Write \(b_n=\log n\), \(w_n=\Lambda(n)/\sqrt n\), and let \(U_n\) be
translation by \(b_n\) on the zero-extension dilation.  For an ordered
word \(\boldsymbol n=(n_1,\ldots,n_k)\),

\[
 U_{n_k}\cdots U_{n_1}=U_{n_1\cdots n_k},
 \qquad
 \prod_{i=1}^kw_{n_i}={\prod_i\Lambda(n_i)\over
                    \sqrt{n_1\cdots n_k}}.           \tag{1.1}
\]

Summing over ordered factorizations of \(m\) gives

\[
 \sum_{n_1\cdots n_k=m}\prod_iw_{n_i}
 ={\Lambda_k(m)\over\sqrt m}.                       \tag{1.2}
\]

This is the A--B--C Witt composition law and includes repetitions and
proper prime powers.

## 2. Positive path domination

Let \(P_T\) be multiplication by \(\mathbf1_{I_T}\).  A killed path word
has the form

\[
 W_{\boldsymbol n}
 =P_TU_{n_k}P_TK_{k-1}P_TU_{n_{k-1}}P_T\cdots
   P_TK_1P_TU_{n_1}P_T.                              \tag{2.1}
\]

All translations and projections are positivity preserving.  From (0.1)
and \(|Af|\le A|f|\) for a positive operator,

\[
 |W_{\boldsymbol n}f|
 \le P_TU_{n_k}C_{\nu_{k-1}}U_{n_{k-1}}\cdots
 C_{\nu_1}U_{n_1}|\widetilde f|,                    \tag{2.2}
\]

where \(C_\nu f=\nu*f\).  On the full line every \(C_{\nu_j}\) commutes
with every translation, so

\[
 |W_{\boldsymbol n}f|
 \le P_TC_{\nu_{k-1}*\cdots*\nu_1}
       U_{n_1\cdots n_k}|\widetilde f|.              \tag{2.3}
\]

The convolution on the right has total mass \(\prod_j\mu_j\).  Notice
that no commutation has been asserted for the killed kernels themselves;
only their positive full-line majorants commute.

The same argument applies to the reflected/right placements, using the
negative translations.  Since each \(\nu_j\) is symmetric for the
complete reference, the same convolution majorant works on both sides.

## 3. Integer-cell Gram after the majorant

Let \(E_L,E_R\) insert the two endpoint strips.  Sum (2.3) with the
nonnegative weights \(\prod_iw_{n_i}\), then group by the product label
using (1.2).  Pointwise,

\[
 |\mathcal B_{N,k}^{K_1,\ldots,K_{k-1}}(f_L,f_R)|
 \le C_{\nu_{k-1}*\cdots*\nu_1}
 \mathcal B_{N,k}(|f_L|,|f_R|),                      \tag{3.1}
\]

where \(\mathcal B_{N,k}\) is exactly the raw synthesis of D.178.
Young's inequality and D.178's exact integer-cell Gram give

\[
\begin{aligned}
 \|\mathcal B_{N,k}^{K_1,\ldots,K_{k-1}}(f_L,f_R)\|_2
 &\le\left(\prod_j\mu_j\right)
       \|\mathcal B_{N,k}(|f_L|,|f_R|)\|_2\\
 &\le\left(\prod_j\mu_j\right)
       \sqrt{V_{N,k}+H_{N,k}}
       \|(f_L,f_R)\|_2.                              \tag{3.2}
\end{aligned}
\]

This proves (0.2).  The collision term \(H_{N,k}\) already includes the
only possible left/right overlap \(mn=N\); passing to absolute values
selects the larger eigenchannel \(V_{N,k}+H_{N,k}\), so it introduces no
additional loss.

## 4. Gamma and prime paths inside the majorant

For the complete reference of D.182,

\[
 \widehat\mu_{T,t}(\tau)=
 \exp\left[-t h_{5/4}(\tau)
 -t\sum_{p^j\le e^{2T}}w_{p^j}
          (1-\cos(j\log p\,\tau))\right].            \tag{4.1}
\]

It is a probability measure.  The Gamma factor is a symmetric
infinite-activity probability convolution.  The prime factor has the
positive compound-Poisson expansion

\[
 e^{-tW_T}\sum_{r=0}^\infty{t^r\over r!}
 \left[{1\over2}\sum_{p^j\le e^{2T}}w_{p^j}
       (\delta_{j\log p}+\delta_{-j\log p})\right]^{*r},
 \quad W_T=\sum_{p^j\le e^{2T}}w_{p^j}.              \tag{4.2}
\]

The factorial in (4.2) makes the path expansion absolutely convergent,
but (0.2) is stronger than a termwise estimate: all reference paths are
summed into a probability measure before the Witt labels are estimated.
Thus the large quantity \(W_T\asymp e^T\) never appears as a loss.

For

\[
 K_a=\int_0^{1/a}e^{-t\widehat{\mathcal R}_T}\,dt,   \tag{4.3}
\]

killed-semigroup domination gives (0.1) with

\[
 \nu_a=\int_0^{1/a}\mu_{T,t}\,dt,
 \qquad\|\nu_a\|_{\rm TV}=a^{-1},                   \tag{4.4}
\]

which proves (0.4).

## 5. Exact scope of the theorem

Equation (0.2) covers every **arithmetic boundary-synthesis** return
subword whose inverse occurrences use the localized potentials \(K_a\).
It also covers mixtures of different massive/killed potentials by
retaining the product \(\prod\mu_j\).

It does not replace the finite block \(F_a\) of D.181 by a scalar.  That
would erase the two Tate jets and the low-frequency PNT discrepancy.  Nor
does it treat the high residual \(H_a^{\rm hi}\) as a positive kernel;
that term is controlled instead by its strict operator contraction
\(e^{-1}a^{-1}\).  Expanding the exact inverse at every occurrence
therefore leaves an arithmetic bulk series with the superfactorial
constants (0.5), a geometric high-residual series, and a finite-rank
low/Tate series.  For the complete cross one must add the \(E_N\) and
endpoint-word series of D.177.  These are disjoint, explicitly typed
obligations; no collision-only or finite-rank reduction of \(E_N\) is
asserted.

# Independent audit of the effective conditional threshold

## Object and verdict

This note independently audits
103_58_EFFECTIVE_CONDITIONAL_THRESHOLD.md.  The audit checks the numerical
constants and every exponent used in its conditional transport theorem.

> **Verdict.** The theorem in 103_58 is valid as stated: assuming RH,
> \[
> |{\cal J}_n|\le q(n)\qquad(n\ge n_{\rm eff}),
> \]
> where
> \[
> n_{\rm eff}=\left\lceil\{72C_2(8\log(72C_2))\}^{4}\right\rceil
> \]
> and its definitions of \(B,P,K,C_2\) are explicit.  The bound
> \(\log n_{\rm eff}<833334000\) has ample slack.

No numerical experiment is used as proof below.

## 1. Bessel and energy constants

On \(1\le t\le4\), the series bounds in 103_58 give
\[
 |Y_m(t)|<4300,\qquad
 |\sqrt tY_m(t)|<8600,\qquad
 |(\sqrt tY_m(t))'|<10750.
\]
For \(m=1,2,3\),
\[
 q_m(t)=1+{1-4m^2\over4t^2}\ge {29\over64}\qquad(t\ge4).
\]
The propagation identity
\[
 \left({W'^2+q_mW^2\over q_m}\right)'
 =-{q_m'\over q_m^2}W'^2\le0
\]
and the exact integer inequality
\[
 64(10750^2+8600^2)<29(21000)^2
\]
prove that the \(Y_m\) solution and its derivative are each less than
21000 after \(t=4\).

It is essential not to apply this same coarse number independently to both
Bessel solutions and then add them.  For \(J_m\), the earlier bound
\(|J_m|\le1\) and its derivative recurrence give at \(t=4\)
\[
 |\sqrt tJ_m|\le2,\qquad |(\sqrt tJ_m)'|\le {5\over2}.
\]
The exact rational check
\[
 {64\over29}\left(2^2+{25\over4}\right)<25
\]
propagates both quantities below 5.  Hence
\[
 21000+5<25000=B.
\]
This resolves the only ambiguity found in the first reading of 103_58.
The two separate energy estimates are now written explicitly in that
document.

## 2. Volterra and \(C_2\)

With both value and derivative sums bounded by \(B\), the Green kernel and
its derivative satisfy
\[
 |G(t,r)|,\ |\partial_tG(t,r)|
 \le{\pi\over2}B^2<2B^2.
\]
Moreover,
\[
 \int_1^{2\nu^{2/3}}{r^2\over16\nu^2}\,dr\le{1\over6}.
\]
Thus Gronwall has exponent
\[
 P={B^2\over3}.
\]
Cramer's rule at the joining point contributes at most \(4B^2\), so
\[
 K=4B^2e^P,\qquad
 |w|\le KA_{N,\alpha},\qquad
 |w'|\le(1+P)KA_{N,\alpha}
\]
are valid.

The three order-two Laguerre pieces in 103_22 become
\[
 32Ka^{-1/4}N^{3/4},\quad
 160(1+P)KN^{3/4},\quad
 2N^{3/4}.
\]
Since \(a^{-1/4}<9/8\), their coefficient is at most
\[
 36K+160(1+P)K+2=(196+160P)K+2=C_2.
\]
Therefore the full-half-line estimate
\[
 \int_{\log2}^{\infty}e^{-u/2}|L_N^{(2)}(u)|\,du
 \le C_2N^{3/4}
\]
is correctly normalized.

For order three, the independent orthogonality estimate is
\[
 \int_{\log2}^{\infty}e^{-u/2}|L_N^{(3)}(u)|\,du
 \le{\sqrt{12}\over\log2}N^{3/2}
 <{21\over4}N^{3/2}.
\]
The powers and the constant \(21/4\) are correct.

## 3. Jensen zero count and partial summation

The positive theta representation bounds the maximum of \(\xi\) on the
outer Jensen circle by its value at \(2+2R\).  The inequalities
\[
 R<{51\over50}T,\quad 2+2R<{9\over4}T,\quad
 \log((9/4)T)<{3\over2}\log T,\quad\log2>{2\over3}
\]
leave more than a factor two of slack in
\[
 {\cal N}(T)\le25T\log T\qquad(T\ge10).
\]
Thus no hidden constant from the Riemann--von Mangoldt asymptotic is used.

Under RH,
\[
 \sum_\rho|\rho|^{-2}=2+\gamma-\log(4\pi)<1.
\]
Stieltjes partial summation then gives
\[
 \sum_{|\gamma|\le Y}|\rho|^{-1}\le28\log^2Y,
\qquad
 \sum_{|\gamma|>Y}|\rho|^{-2}
 \le{50(\log Y+1)\over Y}.
\]
The first constant includes the block below height 10.  The second follows
from the exact integral
\[
 2\int_Y^\infty {25t\log t\over t^3}\,dt
 ={50(\log Y+1)\over Y}.
\]

## 4. Transport constants

At \(Y=N^{3/4}\), the low-zero coefficient is
\[
 28\left({3\over4}\right)^2={63\over4}<16.
\]
The high-zero integration by parts is performed once on
\([\log2,\infty)\) and once on \([T_n,\infty)\).  Each primitive costs
\(2\sigma(Y)\); hence the combined factor is 4, not 2.  Consequently
\[
 4\cdot50\cdot{21\over4}=1050,
\]
and the high block is bounded by
\[
 1050N^{3/4}\log N.
\]
After adding the elementary term, \(18C_2N^{3/4}\log^2N\) is a valid
common upper bound.

## 5. Reserve and threshold

The Bessel--Laplace identity used for the endpoint gives
\[
 |L_k(x)|\le e^x,\qquad
 |L_n^{(1)}(\log2)|\le2(n+1).
\]
Together with the explicit archimedean lower bound,
\[
 q(n)\ge {3\over8}n(\log n-3)-2(n+1)+1
 \ge {1\over4}n\log n
\]
when \(\log n\ge27\).

Thus the final comparison is exactly
\[
 n^{1/4}\ge72C_2\log n.
\]
Writing \(A=72C_2\), \(L=\log A\), the proposed value
\[
 x=4\{L+\log(8L)\}
\]
satisfies
\[
 e^{x/4}=8AL\ge Ax
\]
because \(L>\log(8L)\).  Since \(e^{x/4}/x\) increases for \(x>4\),
the threshold works uniformly above it.

The rough logarithmic checks
\[
 P<208333334,\quad \log(4B^2)<22,\quad
 \log(196+160P)<25,\quad\log(8\log A)<22
\]
give
\[
 \log n_{\rm eff}<833334000.
\]
A diagnostic evaluation gives approximately \(833333619\), but this
decimal is not used in the proof.

## Caveats preserved

1. Every zero estimate after the Jensen count uses RH through
   \(|e^{\rho u}|=e^{u/2}\) and
   \(|\rho|^2=\rho(1-\rho)\).
2. The theorem proves an eventual conditional implication only.
3. The interval \(150\le n<n_{\rm eff}\) has no finite certificate.
4. Therefore 103_58 and this audit do not prove RH and do not validate the
   diagnostic threshold 150.

Subject to precisely these caveats, the effective conditional threshold is
approved.

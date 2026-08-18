# D.187 — Uniform Bohr–Rankin bound for all Witt depths

## Verdict

The fixed-depth asymptotic of D.178 has a uniform replacement sufficient
for summing every arithmetic Witt depth.  Let

\[
 V_{N,k}=\sum_{m\le N}{\Lambda_k(m)^2\over m},
 \qquad 1\le k\le\lfloor\log_2N\rfloor.              \tag{0.1}
\]

For every \(\epsilon>0\) there are \(\delta>0\), \(C_\epsilon\), and
\(N_\epsilon\) such that, uniformly for
\(1\le k\le\delta\log N\),

\[
 \boxed{
 V_{N,k}\le C_\epsilon\sqrt{k}\,e^{\epsilon k}
 {k!\over(2k)!}(\log N)^{2k}.}                      \tag{0.2}
\]

For the remaining depths \(\delta\log N\le k\le\log_2N\), and every fixed
\(c>0\),

\[
 \boxed{
 \sum_{k\ge\delta\log N}
 {V_{N,k}\over(c\log N)^{2k}}=o_{c,\delta}(1).}      \tag{0.3}
\]

The exact two-sided collision satisfies

\[
 0\le H_{N,k}={\Lambda_{2k}(N)\over\sqrt N}
 \le V_{N,k},                                       \tag{0.4}
\]

because it is the off-diagonal entry of the positive Gram in D.178.
Consequently

\[
 \boxed{
 \sup_N\sum_{k\ge1}
 {V_{N,k}+H_{N,k}\over(c\log N)^{2k}}<\infty}        \tag{0.5}
\]

for every fixed \(c>0\).  In fact the small-depth majorant is a summable
series because \(k!/(2k)!\) beats every exponential.

Thus the arithmetic bulk of D.183 is uniformly summable for all return
depths even when the Gamma/reference cutoff is \(c\log N\) with arbitrarily
small fixed \(c>0\).  This removes the fixed-\(k\) gap noted in D.178 and
allows a low-frequency cutoff below \(N^{1/2}\) if that route is needed.

This theorem concerns the exact arithmetic Witt synthesis.  It does not
by itself prove the unit Schur budget for the centered
atomic–continuous cross \(E_N\).

## 1. Exact Bohr lift

For \(\sigma>0\), let \((z_p)_p\) be independent Haar variables on the
unit circle and define

\[
 g_\sigma(z)=
 \sum_p(\log p)\sum_{j\ge1}
 p^{-j(1/2+\sigma)}z_p^j.                            \tag{1.1}
\]

The coefficient of the monomial corresponding to \(m\) in
\(g_\sigma^k\) is

\[
 {\Lambda_k(m)\over m^{1/2+\sigma}}.                \tag{1.2}
\]

Orthogonality of distinct monomials on the infinite torus gives the exact
identity

\[
 \boxed{
 \|g_\sigma\|_{L^{2k}}^{2k}
 =\sum_{m\ge1}{\Lambda_k(m)^2\over m^{1+2\sigma}}.} \tag{1.3}
\]

Since \(m\le N\) implies \(m^{2\sigma}\le N^{2\sigma}\), Rankin's trick
gives

\[
 V_{N,k}\le N^{2\sigma}\|g_\sigma\|_{2k}^{2k}.       \tag{1.4}
\]

## 2. Prime-linear part

Split

\[
 P_\sigma=\sum_p{\log p\over p^{1/2+\sigma}}z_p,
 \qquad Q_\sigma=g_\sigma-P_\sigma.                 \tag{2.1}
\]

Put

\[
 \mathcal V(\sigma)=
 \sum_p{(\log p)^2\over p^{1+2\sigma}}.              \tag{2.2}
\]

Expanding the \(2k\)-th Steinhaus moment and grouping multiplicities gives

\[
\begin{aligned}
 \mathbb E|P_\sigma|^{2k}
 &=(k!)^2\sum_{\sum\alpha_p=k}
   \prod_p{|a_p|^{2\alpha_p}\over(\alpha_p!)^2}\\
 &\le k!\left(\sum_p|a_p|^2\right)^k
 =k!\mathcal V(\sigma)^k.                           \tag{2.3}
\end{aligned}
\]

The PNT and partial summation imply

\[
 \boxed{\mathcal V(\sigma)
 ={1+o(1)\over4\sigma^2}\qquad(\sigma\downarrow0).} \tag{2.4}
\]

Equivalently, for every \(\epsilon_0>0\), after choosing
\(\sigma_0>0\) sufficiently small,

\[
 \mathcal V(\sigma)\le{1+\epsilon_0\over4\sigma^2},
 \qquad0<\sigma\le\sigma_0.                         \tag{2.5}
\]

## 3. Proper prime powers are uniformly subgaussian

For one prime,

\[
 Q_{\sigma,p}(z_p)
 =(\log p)\sum_{j\ge2}p^{-j(1/2+\sigma)}z_p^j.       \tag{3.1}
\]

It has mean zero and

\[
 |Q_{\sigma,p}|
 \le M_p:={(\log p)p^{-1}\over1-p^{-1/2}},
 \qquad
 \sum_pM_p^2<\infty,                                \tag{3.2}
\]

uniformly in \(\sigma>0\).  The variables \(Q_{\sigma,p}\) are independent.
Applying the real Hoeffding lemma to their real and imaginary parts, then
integrating the subgaussian tail, gives an absolute \(C_0\) such that

\[
 \boxed{\|Q_\sigma\|_{2k}\le C_0\sqrt k}             \tag{3.3}
\]

for every \(k\ge1\) and every \(\sigma>0\).

Minkowski, (2.3), and Stirling's lower bound
\((k!)^{1/(2k)}\ge c_0\sqrt k\) now yield

\[
\begin{aligned}
 \|g_\sigma\|_{2k}
 &\le(k!)^{1/(2k)}\mathcal V(\sigma)^{1/2}
       +C_0\sqrt k\\
 &\le(k!)^{1/(2k)}\mathcal V(\sigma)^{1/2}
       (1+C_1\sigma),                               \tag{3.4}
\end{aligned}
\]

for \(0<\sigma\le\sigma_0\).  Therefore

\[
 \boxed{
 \|g_\sigma\|_{2k}^{2k}
 \le k!\mathcal V(\sigma)^k(1+C_1\sigma)^{2k}.}     \tag{3.5}
\]

## 4. Small and intermediate depths

Write \(L=\log N\) and take

\[
 \sigma={k\over L}.                                  \tag{4.1}
\]

For \(k\le\sigma_0L\), (1.4), (2.5), and (3.5) give

\[
 V_{N,k}\le
 e^{2k}k!\left({(1+\epsilon_0)L^2\over4k^2}\right)^k
 \exp(C_2k^2/L).                                    \tag{4.2}
\]

Stirling's upper bound gives

\[
 {e^{2k}(2k)!\over4^kk^{2k}}\le C\sqrt k.           \tag{4.3}
\]

Dividing and multiplying (4.2) by \((2k)!\), and first choosing
\(\sigma_0,\epsilon_0\) small in terms of \(\epsilon\), proves (0.2).
The estimate is uniform even when \(k\to\infty\) with \(N\), provided
\(k\le\delta L\).

## 5. Large depths

Fix the same small \(\sigma_0>0\) in (1.4).  Equations (2.3), (3.3), and
Minkowski give, for a constant \(C_{\sigma_0}\),

\[
 \|g_{\sigma_0}\|_{2k}^{2k}
 \le(C_{\sigma_0}k)^k.                              \tag{5.1}
\]

Hence

\[
 {V_{N,k}\over(cL)^{2k}}
 \le\exp\left(
 2\sigma_0L+k\log(C_{\sigma_0}k)-2k\log(cL)
 \right).                                           \tag{5.2}
\]

For \(\delta L\le k\le L/\log2\),

\[
 \log(C_{\sigma_0}k)-2\log(cL)
 \le-\log L+O_{c,\delta,\sigma_0}(1).               \tag{5.3}
\]

Thus the right side of (5.2) is at most
\(\exp(-\tfrac12\delta L\log L)\) for all sufficiently large \(L\),
uniformly over the whole range.  There are only \(O(L)\) possible depths,
which proves (0.3).

## 6. Uniform summation

For \(k\le\delta L\), (0.2) and (0.4) give

\[
 {V_{N,k}+H_{N,k}\over(cL)^{2k}}
 \le2C_\epsilon\sqrt k\,e^{\epsilon k}
 {k!\over(2k)!}\,c^{-2k}.                           \tag{6.1}
\]

The series on the right converges for every \(c>0\).  The large-depth
tail tends to zero by (0.3).  Enlarging the constant to cover bounded
\(N\) proves (0.5).


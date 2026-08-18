# Cubic gate: exact covariance coordinates and the strong-curvature boundary

## Result

Write
\[
 m_p=\int_0^\infty u^p f(u)\,du,\qquad
 a_p={m_p\over p!},\qquad q_p={a_{p+1}\over a_p},               \tag{1}
\]
and let \(\nu_p\) be the probability measure with density
\(u^pf(u)/m_p\).  If \(h=-f'/f\), then the ratio drops have the exact
covariance representation
\[
 \boxed{\quad q_j-q_{j+1}
 ={q_j\over j+2}\,\mathrm{Cov}_{\nu_{j+1}}(u,h).\quad} \tag{2}
\]
Consequently the cubic condition of `103_36` can indeed be written wholly
in tilted covariances.  This makes explicit what the first-minor proof
uses, but it also exposes the missing datum: one needs *quantitative
control of the change of these covariances as the tilt changes*.

In particular, the pointwise curvature lower bound used for the theta
kernel,
\[
 h'(u)>4\pi-2.49,                                                \tag{3}
\]
does not imply the cubic gate, even if it is replaced by an arbitrarily
large positive constant and even if \(f'(0)=0\).  A smooth, positive,
decreasing, rapidly decreasing counterfamily is constructed below.  Thus
the curvature theorem in `103_34` is a complete PF\(_2\) input, but cannot
by itself be upgraded to PF\(_3\) or to RH.

This is a no-go for a *generic strong-log-concavity proof*.  It says
nothing negative about the actual theta kernel, whose further structure
would have to supply the missing quantitative estimate.

## 1. The exact tilted-covariance formulas

Integration by parts under \(\nu_p\), for \(p\geq1\), gives
\[
 \mathbb E_p h={p\,m_{p-1}\over m_p}={1\over q_{p-1}},
 \qquad
 \mathbb E_p u=(p+1)q_p,
 \qquad
 \mathbb E_p(uh)=p+1.                                          \tag{4}
\]
Hence, on putting
\[
 \Gamma_p:=\mathrm{Cov}_{\nu_p}(u,h),
\]
one obtains the exact identity
\[
 \Gamma_p=(p+1)\left(1-{q_p\over q_{p-1}}\right),
 \qquad
 \delta_j:=q_j-q_{j+1}={q_j\Gamma_{j+1}\over j+2}.             \tag{5}
\]
This proves (2).  For a nonconstant increasing \(h\), \(\Gamma_p>0\),
which is exactly the strict normalized-moment log-concavity proved in
`103_34`.

For the central subsequence \(c_N=a_{2N}\), set \(p=2N\).  Then
\[
 r_N={c_{N+1}\over c_N}=q_pq_{p+1},                            \tag{6}
\]
and a telescoping expansion gives
\[
 \boxed{\quad
 d_N=r_N-r_{N+1}
 =q_{p+1}(\delta_p+\delta_{p+1})
  +q_{p+2}(\delta_{p+1}+\delta_{p+2}).\quad}                  \tag{7}
\]
Equations (5)--(7) express both \(d_N\) and \(d_{N+1}\) in the
covariances \(\Gamma_{p+1},\ldots,\Gamma_{p+5}\).  In particular, the
remaining exact condition from `103_36` is
\[
 d_N(d_N+d_{N+1})^2>q_pq_{p+1}(d_N-d_{N+1})^2.                  \tag{8}
\]
Thus it is not a sign question for one covariance.  It compares five
successive tilted covariances, with their normalizing ratios, at their
natural vanishing scale.

The curvature lower bound \(h'\geq\kappa\) only supplies the elementary
one-tilt estimate
\[
 \Gamma_p=\mathrm{Cov}_{\nu_p}(u,h)
 \geq\kappa\mathrm{Var}_{\nu_p}(u).                    \tag{9}
\]
Indeed \(h(u)-\kappa u\) is increasing and the covariance square used in
`103_34` applies.  It contains no comparison between \(\Gamma_p\) and
\(\Gamma_{p+1}\), which is precisely what (8) needs.

## 2. An exact limiting failure of the cubic gate

Consider first the elementary decreasing log-concave density
\[
 g(u)=
 \begin{cases}
  1,&0\leq u\leq1,\\
  e^{-(u-1)},&u>1.
 \end{cases}                                                    \tag{10}
\]
It is only a limiting model, not the promised smooth counterexample.  Its
moments are nevertheless rational:
\[
 m_p={1\over p+1}+\sum_{j=0}^p {p\choose j}j!.                 \tag{11}
\]
For the even normalized moments this gives
\[
 a_0=2,\quad a_2={8\over3},\quad a_4={163\over60},\quad
 a_6={685\over252},                                             \tag{12}
\]
and therefore
\[
 r_0={4\over3},\qquad r_1={163\over160},\qquad
 r_2={3425\over3423},                                          \tag{13}
\]
\[
 d_0={151\over480},\qquad d_1={9949\over547680}.              \tag{14}
\]
The cubic bracket in (8), at \(N=0\), is exactly
\[
 \begin{aligned}
 B_0&:=d_0(d_0+d_1)^2-r_0(d_0-d_1)^2\\
 &=-{28403537\over345038400}<0.                                \tag{15}
 \end{aligned}
\]
So even a log-concave decreasing density can fail the desired cubic
inequality by a strict, rational margin.

## 3. Smoothing while imposing any prescribed positive curvature

The preceding kink can be smoothed without losing (15).  Let
\(\sigma(t)=(1+e^{-t})^{-1}\), and, for \(\kappa,\varepsilon>0\), put
\[
 \begin{aligned}
 W_\varepsilon(u)
 &=\varepsilon\log {1+e^{(u-1)/\varepsilon}\over
                         1+e^{-1/\varepsilon}}
   -\sigma(-1/\varepsilon)u,\\
 f_{\kappa,\varepsilon}(u)
 &=\exp\!\left(-{\kappa u^2\over2}-W_\varepsilon(u)\right).
                                                                    \tag{16}
 \end{aligned}
\]
This density is positive and smooth on \([0,\infty)\), has a rapidly
decreasing tail, and satisfies
\[
 h_{\kappa,\varepsilon}(0)=0,\qquad
 h'_{\kappa,\varepsilon}(u)
 =\kappa+{\sigma((u-1)/\varepsilon)
 (1-\sigma((u-1)/\varepsilon))\over\varepsilon}>\kappa.     \tag{17}
\]
Thus it is decreasing, has \(f'_{\kappa,\varepsilon}(0)=0\), and is
uniformly strongly log-concave with constant \(\kappa\).

As \((\kappa,\varepsilon)\to(0,0)\), its potential converges pointwise
to \((u-1)_+\), so \(f_{\kappa,\varepsilon}\to g\).  For, say,
\(0<\varepsilon\leq1/4\), the family is dominated by a fixed integrable
exponential on \([1,\infty)\); multiplying by any fixed power \(u^p\)
preserves domination.  Hence every moment through order six converges to
the corresponding moment in (11).  The expression \(B_0\) is a continuous
rational function of those positive moments.  Its strict negativity in
(15) proves that
\[
 B_0(f_{\kappa,\varepsilon})<0                                \tag{18}
\]
for all sufficiently small positive \(\kappa,\varepsilon\).

Finally, if \(F(u)=f_{\kappa,\varepsilon}(au)\), then
\(- (\log F)''\geq a^2\kappa\).  Its normalized ratios satisfy
\(q_j(F)=a^{-1}q_j(f)\); hence \(r_N\) and \(d_N\) both scale by
\(a^{-2}\), and the two sides of (8) scale by the same factor \(a^{-6}\).
The negative sign in (18) is therefore preserved.  Choosing \(a\) large
proves the following statement.

> **Strong-curvature no-go.** For every \(K>0\), there is a smooth,
> positive, decreasing, rapidly decreasing density on \([0,\infty)\) with
> \(f'(0)=0\) and \(- (\log f)''>K\) everywhere, for which the cubic
> Jensen condition (8) fails already at \(N=0\).

In particular this applies to the numerical lower bound
\(K=4\pi-2.49\) available for the theta kernel.

## 4. The genuinely absent higher-order input

For the smooth counterfamily,
\[
 h''_{\kappa,\varepsilon}(u)
 ={\sigma((u-1)/\varepsilon)(1-\sigma((u-1)/\varepsilon))
 (1-2\sigma((u-1)/\varepsilon))\over\varepsilon^2},          \tag{19}
\]
which changes sign sharply across the transition.  The curvature lower
bound sees none of this.  In the theta notation, this is the uncontrolled
quantity
\[
 h''=-(\log\Phi)'''.                                           \tag{20}
\]
Merely assigning a sign to (20) has not been shown sufficient; the exact
requirement is stronger and is already visible in (5)--(8): a uniform,
scale-sensitive comparison of the *successive tilted covariances*
\(\Gamma_p\).  Any theta-specific cubic proof must establish such a
comparison, or an equivalent four-moment inequality.  It cannot follow
from the curvature constant in `103_34` alone.

# 104_76 — Height localization of the deep tail and moment gate

**Result.** The extremely weak arithmetic target of `104_75`,

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{Q_{n,\varepsilon_X}\ge
 A_n+p_n(\varepsilon_X)+\log(n+1)+e^{\sqrt X}\}}
 \longrightarrow0,                                      \tag{1}
\]

does not require controlling all the zeros collectively. Uniformly for
\(1\le n\le X\), the contribution of zeros of height
\(\gamma>X^{1/4}\) satisfies

\[
 \boxed{|\lambda_n^{(>X^{1/4})}|
 \ll X\log(X+2)\exp(\tfrac12\sqrt X).}                  \tag{2}
\]

Therefore, if every zero with \(0<\gamma\le X^{1/4}\) lies on the
critical line, then, for \(X\) sufficiently large, the indicator of
(1) is identically zero for **every** \(n\le X\). In particular, the
high tail already has exponential margin \(e^{-\sqrt X/2+O(\log X)}\)
with respect to the threshold.

This exactly localizes the gap: to prove (1) asymptotically, what
remains is to exclude exterior modes of height \(\gamma\le X^{1/4}\)
as \(X\to\infty\). That requirement runs over every height and is not
a known unconditional input. A second-moment, Markov, or Chernoff
argument does not fail because of the high zeros: it fails precisely
if it does not control this low block. The fixed exterior quartet
shows that no bound using only (2) can close (1).

This document proves a new quantitative localization within the
phase; it does not prove (1), A1, or RH.

**No internal duplication.** `104_63` identifies the full energy and
the Parseval/Christoffel--Darboux collapse; `104_70` studies variable
temperature; `104_73`, the Bernstein pressure; and `104_75`, the deep
gate and the linear Bessel mean. Here no other observable is
introduced: it is shown that the level \(e^{\sqrt X}\) localizes every
possible violation at heights \(O(X^{1/4})\), with the complementary
tail summed absolutely by functional quartets.

---

## 1. Functional quartets and their size

Let \(\rho=\beta+i\gamma\), with \(\gamma>0\) and
\(1/2\le\beta<1\), be a representative of an orbit under conjugation
and \(\rho\mapsto1-\rho\). Set

\[
 w_\rho=1-{1\over\rho}={\rho-1\over\rho}
           =e^{-a_\rho+i\theta_\rho},\qquad a_\rho\ge0. \tag{3}
\]

If the orbit has four elements, its contribution to the Li coefficient
is

\[
 q_n(\rho)
 =4-2\Re\{w_\rho^n+w_\rho^{-n}\}
 =4-4\cosh(na_\rho)\cos(n\theta_\rho).                  \tag{4}
\]

On the critical line the orbit has two elements and the contribution
is half of (4). In particular it is non-negative:

\[
 q_n(\tfrac12+i\gamma)/2
 =2\{1-\cos(n\theta_\rho)\}\ge0.                        \tag{5}
\]

The radial deviation has the universal bound

\[
\begin{aligned}
 e^{2a_\rho}=|w_\rho|^{-2}
 &= {\beta^2+\gamma^2\over(1-\beta)^2+\gamma^2}\\
 &=1+{2\beta-1\over(1-\beta)^2+\gamma^2}
 \le1+{1\over\gamma^2},
\end{aligned}                                            \tag{6}
\]

and therefore

\[
 \boxed{0\le a_\rho\le{1\over2\gamma^2}.}              \tag{7}
\]

From (4) and (7), counting multiplicities,

\[
 |q_n(\rho)|\le4+4e^{n/(2\gamma^2)}.                     \tag{8}
\]

The inequality preserves the radial amplification produced by an
exterior excursion; it does not replace \(w_\rho\) by a unit modulus.

---

## 2. The tail above a moving height

Write \(N(T)\) for the zero count with multiplicity. We will only use
the unconditional consequence of Riemann--von Mangoldt

\[
 N(T)\ll T\log(T+2).                                     \tag{9}
\]

For \(2\le Y\le2X\), split the symmetric sum over zeros into
\(Y<\gamma\le2X\) and \(\gamma>2X\). The first part is finite. By (8)
and (9), uniformly for \(n\le X\),

\[
 \sum_{Y<\gamma\le2X}|q_n(\rho)|
 \ll X\log(X+2)\{1+e^{X/(2Y^2)}\}.                      \tag{10}
\]

The infinite part converges absolutely after grouping by orbits.
Indeed, if \(\gamma>2X\), then
\(|1-w_\rho|=|\rho|^{-1}\le\gamma^{-1}<1/2\), and the series
for \(\log(1-1/\rho)\) gives

\[
 |\theta_\rho|\le {2\over\gamma},\qquad
 a_\rho\le {1\over2\gamma^2}.                           \tag{11}
\]

Since \(n|\theta_\rho|\le1\) and \(na_\rho\le1/8\), (4) implies

\[
 |q_n(\rho)|
 \le4\{|1-\cos(n\theta_\rho)|+\cosh(na_\rho)-1\}
 \ll {n^2\over\gamma^2}.                                \tag{12}
\]

Partial summation in (9) gives

\[
 \sum_{\gamma>T}{m_\rho\over\gamma^2}
 \ll {\log(T+2)\over T},                                \tag{13}
\]

whence

\[
 \sum_{\gamma>2X}|q_n(\rho)|\ll X\log(X+2).             \tag{14}
\]

The unconditional Li formula over zeros is interpreted with the
symmetric cutoff in height. That cutoff contains each full functional
orbit or contains none of its elements, because all its elements have
the same ordinate in absolute value. For each fixed \(n\), (12)--(13)
prove the absolute convergence of the series once grouped by orbits;
hence this grouping introduces no new convention and its sum is
precisely the usual Li coefficient \(\lambda_n\).

Equations (10) and (14) prove the following lemma.

**Lemma 2.1 (uniform localization).** For \(2\le Y\le2X\),

\[
 \boxed{
 \sup_{1\le n\le X}|\lambda_n^{(>Y)}|
 \ll X\log(X+2)\{1+e^{X/(2Y^2)}\}.}                    \tag{15}
\]

The notation \(\lambda_n^{(>Y)}\) means the sum over orbits of zeros
with ordinate larger than \(Y\). The bound further shows that this
tail does not depend on a summation convention.

Taking \(Y=X^{1/4}\) in (15) gives (2). More generally, for the
threshold \(e^{X^\alpha}\), \(0<\alpha<1\), the natural choice is

\[
 Y=X^{(1-\alpha)/2},\qquad
 {X\over2Y^2}={1\over2}X^\alpha.                         \tag{16}
\]

Thus the exponent \(1/4\) is not accidental: it is the dual scale of
the gate \(e^{\sqrt X}\).

---

## 3. Consequence for the real weights \(\Lambda(m)\)

Suppose that every zero with \(0<\gamma\le X^{1/4}\) lies on the
critical line. By (5), its contribution to each \(\lambda_n\) is
non-negative. Lemma 2.1 then gives, uniformly for \(n\le X\),

\[
 \lambda_n\ge
 -C X\log(X+2)e^{\sqrt X/2}.                              \tag{17}
\]

For \(X\) sufficiently large, the error side of (17) is smaller than
\(e^{\sqrt X}/2\).

Now use the real diagonal of `104_69`--`104_75`,

\[
 \lambda_{n,\varepsilon_X}
 =A_n+p_n(\varepsilon_X)-Q_{n,\varepsilon_X},\qquad
 \varepsilon_X=e^{-X/100},                               \tag{18}
\]

for which

\[
 \sup_{n\le X}|\lambda_{n,\varepsilon_X}-\lambda_n|=o(1). \tag{19}
\]

From (17)--(19), also for every \(n\le X\),

\[
 \lambda_{n,\varepsilon_X}+\log(n+1)>-e^{\sqrt X}.       \tag{20}
\]

Since the event of (1) is exactly equivalent to the opposite
inequality in (20), it is proved:

**Theorem 3.1 (finite vanishing of the deep observable).** There
exists an absolute \(X_0\) such that, if \(X\ge X_0\) and RH is
verified up to height \(X^{1/4}\), then the observable of (1) is
exactly zero.

This theorem uses the real weights \(\Lambda(m)\) in (18), not a
prime-support competitor. But its height hypothesis cannot be made
asymptotic from a fixed finite verification.

---

## 4. What a moment attack obtains

Set

\[
 Z_{n,X}=\{-\lambda_n-\log(n+1)\}_+,\qquad S_X=e^{\sqrt X}. \tag{21}
\]

Under the partial hypothesis of Theorem 3.1, (17) implies

\[
 \sup_{n\le X}Z_{n,X}\ll X\log(X+2)e^{\sqrt X/2}.       \tag{22}
\]

Consequently,

\[
 {1\over H_X}\sum_{n\le X}{Z_{n,X}^2\over n}
 \ll X^2\log^2(X+2)e^{\sqrt X}
 =o(e^{2\sqrt X}).                                       \tag{23}
\]

Chebyshev applied to (23), together with the uniform error \(o(1)\)
of (19), proves (1): shifting the threshold \(e^{\sqrt X}\) by
\(o(1)\) does not alter the Markov bound. The gain is diagnostic: the
second moment already has the required scale once the low exterior
zeros are removed; the high zeros do not demand any additional
cancellation.

Without that hypothesis, `104_63` gives the exact Parseval/CD
identity, but bounding it by \(o(e^{2\sqrt X})\) would precisely
exclude a low exterior mode. The same happens with Chernoff at
temperature \(t_X=e^{-\sqrt X}\): a bound on the exponential moment
controls (1), but a fixed mode of rate \(R>1\) makes that moment
explode on a set of positive density. There is no inference from the
first linear moment of `104_75` to (23).

---

## 5. Localized falsifier

Take a fixed exterior quartet \(w=e^{-a+i\theta}\), \(a>0\). Its
contribution is

\[
 q_n=4-4\cosh(an)\cos(n\theta).                           \tag{24}
\]

The returns of the rotation \(n\theta\) to a neighborhood of zero form
a syndetic set of positive density; there

\[
 q_n\le-c e^{an}.                                        \tag{25}
\]

For \(n\ge2\sqrt X/a\), (25) crosses the threshold
\(-e^{\sqrt X}\). Removing the first \(O(\sqrt X)\) degrees only
removes asymptotically half of the harmonic mass up to \(X\), so a
positive logarithmic density persists. In the rational example
\(w=2i\) of `104_75`, the deep density is exactly \(1/8\).

This quartet satisfies every tail bound used in Lemma 2.1 once placed
in the low block. Therefore (15) cannot, by itself, prove (1): what
remains is an arithmetic theorem excluding those low modes for the
real zeta function. This is a localization of the gap, not a claim of
impossibility for every future arithmetic identity.

---

## 6. Verdict

**Proved:** the radial bound (7), the absolute tail sum (15), the
general dual scale (16), the vanishing of the indicator under partial
RH up to \(X^{1/4}\), and the second-moment bound (23) under the same
hypothesis.

**Gain:** the large-deviation attack is reduced to the block of zeros
with \(\gamma\le X^{1/4}\). Zeros above that height have sufficient
exponential margin even when taken in absolute value by full
quartets.

**Not proved:** an unconditional control of that low block as
\(X\to\infty\), the limit (1), A1, or RH. A fixed-height verification
only gives a finite range, however large.

---

## 7. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 deep_tail_height_localization_check.py
```

The checker verifies the quartet identity, (7), the elementary bound
of the very high tail, and the exponential separation between (2) and
the threshold of (1).

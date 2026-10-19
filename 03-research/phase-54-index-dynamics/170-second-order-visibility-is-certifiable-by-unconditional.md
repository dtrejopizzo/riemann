# Document 170 — Second-order visibility: is $I(0^+)$ certifiable by unconditional averaging tools?

**Program:** Riemann Hypothesis — Phase 54 (index dynamics)
**Mandate:** decide ONE question: is the second-order quantity $I(0^+)=\sum_j b_j^2$ (or upper bounds on it, even just $\ell^2$ finiteness, GAP 167.A) certifiable by unconditional averaging tools, or does the quadratic wall kill it just like the first-order one (no-go 141.B2)?
**Prerequisites read at source:** Doc 167 (§3 GAP 167.A, §5 ζ-free table and the "signed→quadratic" nuance), Doc 168 (§5.2 second-order finding and warning), Doc 141 in full (Lemmas 141.B0/141.B, Cor. 141.B2, Computations 141.M1–M5, GAP-141.G1), Phase 48 memory (D152, impurity spectrum).
**Contract:** [NEW-DEFINITION] free; [THEOREM]/[PROP]/[LEMMA] full proof or unlabeled; [COMPUTATION] shown; [BRIDGE] honest; [GAP]/[WISH] declared. A false victory is worse than failure.

**Coordinates.** We work in ζ coordinates: off zero $\rho=\tfrac12+b_j+i\gamma_j$, $b_j\in(0,\tfrac12)$, $\gamma_j>0$, one representative per quadruple $\{\rho,\bar\rho,1-\rho,1-\bar\rho\}$. $I(0):=\sum_j b_j^2$ (upper half; in the $H_t$ chart of Polymath 15 the energy is $4\sum_j b_j^2$ — factor from the dilation by 2, Doc 168 KILL-2; here everything is in the ζ chart, no mixing). For a test $h$ and a zero we write $h(\gamma_\rho)$ with $\gamma_\rho=\gamma_j-ib_j$ (convention $\rho=\tfrac12+i\gamma_\rho$).

**Admissible class $\mathcal A$.** $h:\mathbb R\to\mathbb R$ even, extending holomorphically to $|\mathrm{Im}\,z|\le\tfrac12+\varepsilon$ with $|h(z)|\le C(1+|\mathrm{Re}\,z|)^{-1-\delta}$ uniformly in the strip, and $g(u):=\frac1{2\pi}\int_{\mathbb R}h(r)e^{-iru}\,dr$ (even, real). This is the class of Weil's explicit formula [W52; IK04, Thm. 5.12]:
$$\sum_{\rho}h(\gamma_\rho)\;=\;h(\tfrac i2)+h(-\tfrac i2)\;-\;2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,g(\log n)\;+\;\frac1{2\pi}\int_{\mathbb R}h(r)\,\Omega(r)\,dr,$$
with $\Omega(r)=\mathrm{Re}\,\frac{\Gamma'}{\Gamma}(\tfrac14+\tfrac{ir}2)-\log\pi$ (Stirling: $\Omega(r)=\log\frac{|r|}{2\pi}+O((1+r^2)^{-1})$).

---

## 0. Executive summary and verdict

**VERDICT: (C), partial, with the exact cut at the resolution scale $b\cdot\log\gamma$ and at the rate/total dichotomy.**

1. **Unconditionally certifiable (proved here, §4):** the truncated-with-rate version of GAP 167.A. **[THEOREM 170.5]** $E(T):=\sum_{\gamma_j\le T}b_j^2\ \ll\ T/\log T$ (Selberg density + layers). **[COR 170.6]** the energy in Lehmer units has density bounded by zero, $\frac1{N(T)}\sum_{\gamma_j\le T}(b_j\log\gamma_j)^2=O(1)$, and the total weighted sum $\sum_j b_j^2/\bigl(\gamma_j(\log\log\gamma_j)^{1+\varepsilon}\bigr)$ **converges**. This is the program's first unconditional certificate on an RH-relevant second-order quantity — but it is a **growth envelope**, not a decision on $I(0^+)$.
2. **Not certifiable (proved here, §2–§3, §4.3):** (a) the average over $\tau$ of the second-order signal is **exactly zero to every order in $b$** ([THEOREM 170.3], contour shift) — the zero-integral mechanism of 141.M5/141.B2 **reappears at second order**, not in the pointwise signal but in the average over translations and in the weight ($\int h''=0$ for every admissible test; **no admissible test exists with $h''$ of constant sign**); (b) the three certification routes by window (pointwise, linear, quadratic) have the **same unconditional threshold $\omega=\tfrac14$** = the pole = the exact jurisdiction of D152 ([COMPUTATIONS 170.4]); (c) $I(0^+)<\infty$ is not separable by averaging data ([THEOREM 170.8], successor of 141.B2: a configuration with $I=\infty$ and $\varepsilon$-indistinguishable data).
3. **The marginal scale (§3.4, the new fact that vindicates the 168 auditor):** with tests of maximal evaluable support $L\asymp\log\gamma$, the second-order signal of a quadruple at the LP-134 scale ($b=c/\log\gamma$) is $\Theta(c^2)$ — **order one, not sub-resolution**: unlike the first order (signal identically averaged to zero), the second order is NOT buried by size. What blocks certification at the marginal scale is exclusively (i) the unconditional evaluation of the prime side by individual window (= GAP-141.G1, the old wall) and (ii) the quadratic statistic of the sea at resolution $\asymp1$ (= Montgomery's pair correlation, conditional on RH). The second-order wall is real but is **the same old wall relocated**, not a new one.

---

## 1. The exact second-order footprint

### 1.1. The identity, with the correct sign

**[PROP 170.1] (exact footprint).** Let $h\in\mathcal A$ and let $Z$ be the zero configuration of ζ, $Z^\flat$ its projection onto the line (identical ordinates). Then:

(i) *(spectral decomposition)* $\displaystyle\sum_{\rho\in Z}h(\gamma_\rho)-\sum_{\rho\in Z^\flat}h(\gamma_\rho)\;=\;2\sum_j\Delta_j(h),\qquad \Delta_j(h):=2\mathrm{Re}\,h(\gamma_j+ib_j)-2h(\gamma_j),$
(the outer factor 2: the two sides $\pm\gamma_j$ of the quadruple, $h$ even; $2\mathrm{Re}\,h(\gamma_j+ib_j)=h(\gamma_j+ib_j)+h(\gamma_j-ib_j)$ by Schwarz reflection, $h$ real on $\mathbb R$).

(ii) *(expansion)* $\displaystyle \Delta_j(h)\;=\;-\,b_j^2\,h''(\gamma_j)\;+\;R_j,\qquad |R_j|\;\le\;\tfrac1{12}\,b_j^4\sup_{|y|\le b_j}\bigl|h^{(4)}(\gamma_j+iy)\bigr|,$
and in fact $\Delta_j(h)=2\sum_{k\ge1}\frac{(-1)^k b_j^{2k}}{(2k)!}h^{(2k)}(\gamma_j)$ (convergent series, $h$ holomorphic in the strip). **Sign note:** the footprint is $-\sum_j b_j^2h''(\gamma_j)$, not $+$; the statement in Doc 168 §5.2 has the sign flipped (erratum E-170.1, §6; harmless there). For a test peaked at $\gamma_j$ ($h''(\gamma_j)<0$) the zero side has a **positive excess** relative to the projected world.

(iii) *(the matching prime functional)* With $N^\flat(t)$ the ordinate count, $\bar N(t)=\frac t{2\pi}\log\frac t{2\pi e}+\frac78$ and $S(t)=N^\flat(t)-\bar N(t)+O(1/t)$ (Riemann–von Mangoldt, [T86, Thm. 9.4]; identical on $Z$ and $Z^\flat$, Lemma 141.B0):
$$\boxed{\;-2\sum_j b_j^2\,h''(\gamma_j)\;+\;2\sum_j R_j\;=\;\underbrace{h(\tfrac i2)+h(-\tfrac i2)-2\sum_n\frac{\Lambda(n)}{\sqrt n}g(\log n)+\Bigl[\tfrac1{2\pi}\!\int h\,\Omega-\!\int h\,d\bar N\Bigr]}_{=:\ \mathfrak D(h)\ \text{(von Mangoldt bias vs. RvM prediction — computable)}}\;-\;\underbrace{\int h\,dS}_{=:\ F(h)\ \text{(sea fluctuation)}}\;}$$

*Proof.* (i): count the quadruple against its projection. (ii): $f(b):=2\mathrm{Re}\,h(\gamma+ib)$ is even and real-analytic; Taylor with integral remainder in $b^2$; the bound on $R_j$ by Cauchy on the segment. (iii): Weil's formula for $Z$ (exact) minus $\sum_{Z^\flat}h=\int h\,dN^\flat=\int h\,d\bar N+\int h\,dS+O(\|h\|_\infty)$ small. $\square$

**Reading.** The second-order footprint of $I$ is the **bias of the prime sum relative to the smooth RvM prediction, modulo the sea fluctuation $F(h)$**. Every certificate must separate three numbers: $\mathfrak D(h)$ (computable only trivially without RH), $F(h)$ (ordinate statistics — σ-blind but unknown), and the signal. This is the exact structure on which §2–§3 operate.

### 1.2. The D152 impurity spectrum IS the second-order window

**[PROP 170.2] (term-by-term comparison with D152).** Take $g(u)=e^{-u^2/4T^2}\cos(\tau u)$, i.e. the impurity-spectrum test $S_T(\tau)=\sum_n\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\cos(\tau\log n)$. Then $h_\tau(t)=\sqrt\pi\,T\bigl[e^{-T^2(t-\tau)^2}+e^{-T^2(t+\tau)^2}\bigr]$ and the contribution of a quadruple $(\gamma_j,b_j)$, core term, is **exactly**
$$2\mathrm{Re}\,h_\tau(\gamma_j+ib_j)-2h_\tau(\gamma_j)\;=\;2\sqrt\pi\,T\,e^{-T^2(\gamma_j-\tau)^2}\Bigl[e^{T^2 b_j^2}\cos\bigl(2T^2(\gamma_j-\tau)b_j\bigr)-1\Bigr].$$
Consequently:
1. *(sub-resolution regime $b_jT\le1$)* the bracket is $-b_j^2\,\partial_t^2\bigl[\sqrt\pi Te^{-T^2(t-\tau)^2}\bigr]_{t=\gamma_j}/(\sqrt\pi T e^{-T^2(\gamma_j-\tau)^2})\cdot(1+O(b^2T^2))$: the footprint of Prop. 170.1 at leading order — at $\tau=\gamma_j$, $+2\sqrt\pi\,b_j^2T^3$ from the zero side, **negative** bias in $S_T$ (the zeros enter with a $-$ sign): the permanent bias of D152.
2. *(super-resolution regime $b_jT\gg1$)* the factor $e^{T^2b_j^2}$ is the **full resummation** of the series in (ii) of Prop. 170.1 (the Gaussian sums its Taylor series exactly), and the exponential rate $\frac1{T^2}\log|\cdot|\to b_j^2-(\gamma_j-\tau)^2$ reproduces **exactly** the impurity weight $\omega(\tau)=\max\bigl(0,\max_j(b_j^2-(\gamma_j-\tau)^2)\bigr)$ of Theorem 152.2.

**Answer to the Phase 48 memory question: YES — the impurity spectrum is the second-order window, resummed.** The quadratic weight ω in $\delta_j$ is not a coincidence: it is the footprint $b^2h''$ of the Lehmer = 2 exponent, seen at super-resolution; the permanent negative bias $\sim-2\sqrt\pi\,m_JTe^{\delta^2T^2}$ is the signature of $I>0$ read from the primes. D152 and GAP 167.A are **the same object** in two regimes of the same test. (And that is why the $\omega\le\tfrac14$ jurisdiction of D152 will reappear as a threshold in §3.)

---

## 2. The "signed→quadratic" attack: the concave test dies globally, survives locally

The mandate's hope: choose $h$ with $h''$ of fixed sign where it matters, so that $-\sum b_jh''(\gamma_j)$ is one-signed and an average accumulates it while the noise cancels. The following theorem measures exactly how much of that hope exists.

**[THEOREM 170.3] (second-order zero-integral — the structural successor of 141.M5).** Let $h\in\mathcal A$.
1. $\displaystyle\int_{\mathbb R}h''(t)\,dt=0$ and hence $\int(h'')_+=\int(h'')_-$: **the second-order weight of every admissible test is a profile with exactly zero mean.** In particular there is no non-constant $h\in\mathcal A$ with $h''$ of constant sign on $\mathbb R$ (also directly: a non-constant concave function on $\mathbb R$ tends to $-\infty$ at some extreme — incompatible with decay).
2. *(exact blindness of linear averages over translations, to EVERY order in $b$)* For every $0<b\le\tfrac12$ and every $\gamma$:
$$\int_{\mathbb R}\Bigl[h\bigl(\gamma+ib-\tau\bigr)+h\bigl(\gamma-ib-\tau\bigr)-2h\bigl(\gamma-\tau\bigr)\Bigr]\,d\tau\;=\;0\qquad\textbf{exactly}.$$
Consequently, **any statistic that is a $\tau$-average (with slowly varying weight) of translated windows of a fixed test has identically zero sensitivity to $I$** — not $O(b^4)$: zero, to every order, including exponential resummation.

*Proof.* (1): $h'\to0$ at $\pm\infty$ (decay in the strip + Cauchy for $h'$). (2): $\int_{\mathbb R}h(x+ib)\,dx=\int_{\mathbb R}h(x)\,dx$ by Cauchy's theorem on the rectangle $[-R,R]\times[0,b]$ (vertical sides $\to0$ by uniform decay in the strip, $b\le\tfrac12<\tfrac12+\varepsilon$); subtract twice the same integral. For a slowly varying weight $w$, the $w$-average of translations = evaluation of the composite test $h\star w$, which is again a fixed test: it reduces to a single window (§3). $\square$

**Verdict on the §5.1 attack of Doc 167 on GAP 167.A: the attack is confirmed, but with the mechanism relocated.** The "signed→quadratic" obstruction does not kill the pointwise signal (which is one-signed in the window's core — that is real and new relative to first order); it kills the **accumulation**: the second-order signal is one-signed *locally* but has globally zero mean *in $\tau$* — the flanks ($h''>0$ outside the core, with exactly equal mass by (1)) compensate the core with theorem-level precision. The route "one-signed signal accumulates linearly, noise cancels" **does not exist**: linear accumulation cancels the signal, not the noise. Any accumulation that preserves sign is quadratic in the window — and pays the price of §3.3.

---

## 3. Signal/noise: the three routes and the common threshold ¼

We fix the Gaussian window of Prop. 170.2 (computations with compact-support tests of Fejér/Beurling–Selberg type give the same picture; §3.4 uses them where they are better). We normalize by the peak height $\sqrt\pi T$: signal per quadruple at the center $s_j=2(e^{b_j^2T^2}-1)$ ($\approx2b_j^2T^2$ sub-resolution).

### 3.1. [COMPUTATION 170.4a] Pointwise route (one window, individual certification)

To certify an upper bound on $s_j$ via the identity of Prop. 170.1(iii) one must bound $\mathfrak D(h_\tau)$ and $|F(h_\tau)|$ from above. Unconditionally: (α) the prime sum only admits the trivial bound $\sum_n\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\le(1+o(1))\sqrt\pi\,T\,e^{T^2/4}$ (saddle point $u=T^2$ of the exponent $u/2-u^2/4T^2$, value $T^2/4$); (β) $|S(t)|\le C\log t$ (Backlund, unconditional) gives $|F|\le C'T\log\tau$ — and nothing better per individual window. The trivial bound (α), normalized, is $e^{T^2/4}$; the maximal resummed signal is $e^{b^2T^2}$ with $b<\tfrac12$, i.e. $e^{b^2T^2}<e^{T^2/4}$ **always**: the trivial bound never certifies anything below $\omega=\tfrac14$. This is exactly the Λ≥0 jurisdiction of D152 (Props. 152.4–152.7), re-derived: **the only unconditional pointwise certificate is $\omega\le\tfrac14$, reached only by the pole.**

### 3.2. [COMPUTATION 170.4b] Linear route (average in τ)

Killed exactly by Theorem 170.3(2): zero sensitivity to every order. (Independent check in the closed form of Prop. 170.2: $\int_{\mathbb R}e^{-T^2(x^2-b^2)}\cos(2T^2xb)\,dx=\frac{\sqrt\pi}T$, identical to the on-line value $\int e^{-T^2x^2}dx$ — the amplification $e^{T^2b^2}$ and the cosine's oscillation cancel exactly.)

### 3.3. [COMPUTATION 170.4c] Quadratic route (second moment in τ)

The unconditional part: by Montgomery–Vaughan's mean value theorem [MV74], for $T^2\le(2-\varepsilon)\log T_0$,
$$\int_0^{T_0}\bigl|S_T(\tau)\bigr|^2d\tau\;=\;\Bigl(\tfrac12\sum_n\frac{\Lambda(n)^2}{n}e^{-(\log n)^2/2T^2}\Bigr)\,T_0\,(1+o(1))\;=\;c\,T^2\,T_0\,(1+o(1)),$$
(diagonal $\asymp T^2$; error $\sum_n n|a_n|^2\asymp T^2e^{T^2/2}\ll T^2T_0$ exactly under the support restriction $T^2\le(2-\varepsilon)\log T_0$ — the classical budget). This **fixes the total** unconditionally. But the total = sea + impurity, and the quadratic statistic of the sea alone (the variance of ordinate counting at resolution $1/T$ with $T^2\asymp\log T_0$, i.e. the pair correlation $F(\alpha)$ at $|\alpha|\asymp1$) is **unconditionally unknown at leading order**: Montgomery's theorem [M73] is conditional on RH, and the unconditional variants (Goldston–Montgomery [GM87]) do not determine it. (Selberg's unconditional moments of $S(t)$ [S46] are long-range statistics — frequencies $\alpha=o(1)$ — and do not fix the variance at resolution.) Hence the sea can absorb, within the uncertainty $\Theta(T^2T_0)$, any smaller one-signed impurity excess: a quadruple contributes excess $\asymp T(e^{b^2T^2}-1)^2$ (plus an even larger signed cross term), and it exceeds the sea's uncertainty only if $e^{2b^2T^2}\gtrsim T\,T_0$, i.e. $b^2\ge\tfrac14(1+o(1))$: **the pole again, $\omega=\tfrac14$.**

**Synthesis of 170.4a–c:** three independent routes, the same threshold. The $\omega\le\tfrac14$ jurisdiction of D152 is **optimal within the class of unconditional averages**; below ¼ no average certifies anything about a window.

### 3.4. [COMPUTATION 170.4d] The marginal scale: exactly where sub-resolution lies

Compact-support tests: $g$ supported on $[-L,L]$ (Fejér/Beurling–Selberg), resolution $1/L$, $|h''(\text{center})|\asymp L^2h(\text{center})$, off amplification $\le e^{b_jL}$. Normalized signal per quadruple at the center: $\asymp(b_jL)^2$ (sub-resolution $b_jL\le1$). The maximal support with the prime side within the unconditional on-average evaluation budget is $L=(2-\varepsilon)\log\gamma$ ($n\le\gamma^{2-\varepsilon}$, the MV limit; beyond it, not even on average). Then, at the **LP-134 scale** $b_j=c/\log\gamma_j$:
$$\text{signal}\;\asymp\;(b_jL)^2\;=\;\bigl(c\,(2-\varepsilon)\bigr)^2\;=\;\Theta(c^2)\;=\;\Theta(1).$$
The noise per window: at resolution $1/L\asymp1/(2\log\gamma)$ — finer than the average gap $2\pi/\log\gamma$ — the window contains $O(1)$ ordinates, and its fluctuation (presence/absence of a zero) is $\Theta(1)$. **Scale conclusion, in three bands:**

| scale | signal per optimal window | status |
|---|---|---|
| $b\log\gamma\to\infty$ | $\to\infty$ (resummation $e^{bL}$) | visible; and in fact density **counts** it (Lemma 141.M1: exactly its non-triviality threshold) — this is the §4 band |
| $b\log\gamma\asymp1$ | $\Theta(c^2)$ vs. sea $\Theta(1)$ | **marginal: NOT buried by size.** Blocked only by (i) evaluation of the prime side per individual window with error $o(1)$ = **GAP-141.G1** (Conj. 108-N, the old wall), and (ii) sea variance at resolution = pair correlation, conditional on RH |
| $b\log\gamma\to0$ | $\to0$ | buried in EVERY evaluable window; only tests of support $\gg\log\gamma$ would see it (not evaluable; this is Rigidity 153.M′ territory, super-logarithmic support) |

**This quantifies and confirms the auditor's finding (Doc 168):** the second-order wall is genuinely **different and weaker** than the first-order one. At first order the signal was identically zero on average and of individual size $O(\delta a)$; at second order the signal at the critical scale is $\Theta(1)$ per window — there is no size deficit. But the wall is not crossed: it is **rerouted** — certification requires either individual-window evaluation (GAP-141.G1) or the sea's quadratic statistic (RH-conditional). The circle of Doc 141's §3.3 closes also at second order: *the quadratic quantity, attacked with analysis, reroutes to the old half of the wall.* No side door — but, unlike first order, it is no longer a zero-integral no-go of the signal: it is an *evaluation* no-go.

---

## 4. The density computation: what IS actually an unconditional theorem

Here is the positive side of the verdict. Density tools are the only σ-sensitive tools above the resolution (Lemma 141.M1), and the truncated ℓ² is exactly a monotone integral of the counts $N(\sigma,T)$ — on the good side.

**[THEOREM 170.5] (unconditional envelope for the truncated instability energy).** Unconditionally,
$$E(T)\;:=\;\sum_{0<\gamma_j\le T}\Bigl(\beta_j-\tfrac12\Bigr)^2\;\ll\;\frac{T}{\log T}.$$
More generally, any density theorem of the form $N(\sigma,T)\le A\,T^{1-c(\sigma-1/2)}\log^B T$ ($\tfrac12\le\sigma\le1$) gives $E(T)\le\frac{2A}{c^2}\,T\log^{B-2}T\,(1+o(1))$.

*Proof.* Layer-cake: $b_j^2=\int_0^{1/2}2b\,\mathbf 1_{\{b<b_j\}}\,db$, so $E(T)=\int_0^{1/2}2b\,N(\tfrac12+b,\,T)\,db$ (zero-measure boundary). With Selberg's density theorem [S46], $N(\tfrac12+b,T)\le C\,T^{1-b/4}\log T=CT\log T\,e^{-(b/4)\log T}$ uniform in $b\in[0,\tfrac12]$:
$$E(T)\;\le\;2CT\log T\int_0^{1/2}b\,e^{-b\log T/4}\,db\;\le\;2CT\log T\cdot\frac{16}{\log^2T}\int_0^\infty s\,e^{-s}\,ds\;=\;\frac{32\,C\,T}{\log T}.$$
The general form: identical with $(A,c,B)$. $\square$

**Remarks.** (a) Near $\sigma=\tfrac12$ Selberg ($c=\tfrac14$, $B=1$) is the best known; Ingham [I40] ($T^{3(1-\sigma)/(2-\sigma)}\log^5T$: $c=\tfrac43$ but $B=5$) and Huxley [H72] are optimized far from the line and give $T\log^3T$ — worse. (b) The trivial bound is $E(T)\le\tfrac14N(T)\asymp T\log T$: the gain is $\log^2T$. (c) **Geometric reading:** $T/\log T$ is exactly the energy of a configuration with 100% of the zeros at distance $\asymp1/\log\gamma$ — the envelope says that the total energy behaves *as if all the zeros were at resolution scale*, the ℓ² version of the Bohr–Landau/Selberg clustering (Prop. 141.M2). (d) Comparison with the classical ℓ¹ route: Littlewood's lemma + Jensen give $\sum_{\gamma\le T}(\beta-\tfrac12)^+\ll T\log\log T$ ([L24]; [T86, §9.9]) and from that only $E(T)\ll T\log\log T$ — the density route is strictly better for the ℓ². **[Literature GAP]:** the bound $E(T)\ll T/\log T$ is an immediate corollary of [S46] and should be folklore; we know of no reference stating it as such.

**[COR 170.6] (normalized and convergent forms).** Unconditionally:
1. *(bounded Lehmer energy density)* $\displaystyle\sum_{\gamma_j\le T}\bigl(b_j\log\gamma_j\bigr)^2\;\ll\;T\log T\;\asymp\;N(T)$: in the units where the Lehmer exponent is 2, the average instability energy per zero is $O(1)$.
2. $\displaystyle\sum_{\gamma_j\le T}\frac{b_j^2}{\gamma_j}\;\ll\;\log\log T$, and for every $\varepsilon>0$: $\displaystyle\sum_{j}\frac{b_j^2}{\gamma_j\,(\log\log\gamma_j)^{1+\varepsilon}}\;<\;\infty$ — **a weighted total version of GAP 167.A is a theorem**, with the exact weight dictated by the envelope.

*Proof.* (1): dyadic blocks $T_k=2^k$: $\sum_{\gamma\in(T_{k-1},T_k]}(b\log\gamma)^2\le\log^2T_k\,E(T_k)\ll T_k\log T_k$; sum. (2): partial summation against $E(t)\ll t/\log t$: $\int_2^T t^{-1}dE=E(T)/T+\int_2^TE(t)t^{-2}dt\ll1/\log T+\int_2^T\frac{dt}{t\log t}=\log\log T+O(1)$; for weight $u(t)=(\log\log t)^{1+\varepsilon}$, $\int\frac{dt}{t\log t\,u(t)}<\infty$. $\square$

### 4.3. What density CANNOT give: total finiteness

**[PROP 170.7] (GAP 167.A is out of reach of averages — quantified).**
1. *(consistency of $I=\infty$)* For every fixed $b_0\in(0,\tfrac12)$, the configuration with one quadruple at distance $b_0$ at every height $\gamma_k=2^k$ above the numerical verification bound ($3\cdot10^{12}$, [PT21]) is consistent with **everything** unconditional known: densities (one zero per dyadic block $\ll$ any bound), zero-free region (Vinogradov–Korobov only excludes $b\ge\tfrac12-c/(\log\gamma)^{2/3}(\log\log\gamma)^{1/3}$ — take $b_0<\tfrac12$ fixed), vertical statistics (Lemma 141.B0), and the envelope of Theorem 170.5 ($E(T)\ll\log T$ here). It has $I=\sum b_0^2=\infty$. **Not even the fat part $\sum_{b_j\ge b_0}b_j^2$ is certifiably finite for any $b_0<\tfrac12$.**
2. *(what the density route would require)* Convergence of $\sum_jb_j^2$ via counts requires $N(\tfrac12+b_0,T)=O_{b_0}(1)$ as $T\to\infty$ for every $b_0>0$ — **asymptotically zero-free half-strips** — while all known technology gives exponents $T^{a}$ with $a>0$ for every $\sigma<1$ (the VK boundary is at distance $o(1)$ from $\sigma=1$, not from $\sigma=\tfrac12+b_0$).
3. *(the individual content of GAP 167.A, distilled)* $I(0^+)<\infty\implies\forall b_0>0:\ \#\{j:b_j\ge b_0\}<\infty$ — **finiteness by half-strips**, i.e. "$m<\infty$ in each half-strip $b\ge b_0$" plus summability near the line. GAP 167.A is closer to $m<\infty$ than its ℓ² form suggested: its content behind the certifiable envelope is exactly an individual-quantifier statement.

*Proof.* (1) direct check against each item of the table in Doc 141 §2.6. (2): $\sum_kb_0^2\,[N(\tfrac12+b_0,2^{k+1})-N(\tfrac12+b_0,2^k)]<\infty$ requires the sequence $N(\tfrac12+b_0,2^k)$ to be bounded. (3): terms $\ge b_0^2$ of a convergent series are finite in number. $\square$

**Note on Cramér and $\psi(x)-x$:** the second moment $\int_1^X(\psi(x)-x)^2x^{-2}dx\sim c\log X$ is **conditional on RH** (Cramér 1921 [C21]); unconditionally, an upper bound on the second moment of $\psi$ would already imply density/Θ results beyond reach (a single zero with $\beta$ contributes $\gg x^{2\beta}$ to the mean square). The diagonal of the second moment sees $\sum x^{2b_j-1}|\rho_j|^{-2}$: exponential amplification $e^{2b_jL}$ with $L=\log x$ — the same window structure of §3, same threshold, no new lever. Not usable.

---

## 5. The relative second-order no-go (the successor of 141.B2)

**[THEOREM 170.8] (ℓ² finiteness is not separable by averaging data).**
1. *(clean finite version)* Let $\mathcal F=\{F_1,\dots,F_M\}$ be any **finite** family of admissible tests fixed in advance, and $\varepsilon>0$. There exists an admissible configuration $Z$ with $I(Z)=\sum_jb_j^2=\infty$ (in fact with $b_j\to0$) such that $|\sum_{\rho\in Z}h_{F_i}(\gamma_\rho)-\sum_{\rho\in Z^\flat}h_{F_i}(\gamma_\rho)|\le\varepsilon$ for all $i\le M$, and $Z$, $Z^\flat$ have identical vertical statistics (Lemma 141.B0) and respect the envelope of Theorem 170.5. No argument whose input is finite Weil data + ordinate statistics can prove $I(0^+)<\infty$.
2. *(countable version, weighted metric)* For $\{F_i\}_{i\in\mathbb N}$ countable and the metric $d(\mathcal D,\mathcal D')=\sum_i2^{-i}\min(1,|\mathcal D_i-\mathcal D'_i|)$: there exists $Z$ with $I(Z)=\infty$ and $d(\mathcal D(Z),\mathcal D(Z^\flat))\le\varepsilon$.

*Proof.* Take $b_j:=1/\sqrt{\log(j+2)}$ (so $\sum_jb_j^2=\sum1/\log(j+2)=\infty$, $b_j\to0$) and $\gamma_j$ inductively increasing. By Lemma 141.B (with $N=2$), the contribution of quadruple $j$ to datum $i$ is $\le C_2(F_i)\,(b_jL_i)^2e^{b_jL_i}(1+\gamma_j)^{-2}\le C'_i\,(1+\gamma_j)^{-2}$, which $\to0$ as $\gamma_j\to\infty$ **without touching $b_j$** — unlike 141.B2, where indistinguishability was bought by shrinking $\delta_j$, here it is bought only with height, and that is why the divergence of $\sum b_j^2$ is compatible. (1): finitely many conditions per step ($i\le M$), each with budget $\varepsilon2^{-j}/M$: choose $\gamma_j$ sufficiently large. (2): given $\varepsilon$, fix $I_0$ with $\sum_{i>I_0}2^{-i}\le\varepsilon/2$ and apply (1) to $\{F_i\}_{i\le I_0}$ with budget $\varepsilon/2$; data $i>I_0$ are absorbed by the metric. The envelope: one quadruple per step with super-exponential $\gamma_j$ gives $E(T)=o(T/\log T)$. $\square$

**Honesty about the scope, as in Obs. 3.1 of 141:** this is a no-go **relative to the data class**, with an additional restriction compared to 141.B2: the per-datum-uniform version with a countable family is not recovered (the finite heads $j<i$ are not controllable with $b_j$ fixed because of the divergence); the two stated versions cover every effective argument (finite data, or a uniform modulus of dependence on the data). It does not exclude arguments using the real arithmetic of ζ at all supports simultaneously (GAP-141.G1) nor global rigidity of the Euler class — exactly the same two loopholes as at first order.

**Structural moral (the difference with 141.B2, stated plainly):** at first order the invisibility was of the *signal* (zero integral per quadruple, Computation 141.M5); at second order the signal is robust (Θ(1) at the marginal scale, §3.4) and the inseparability is of the *total value*: the divergence of $\sum b_j^2$ can hide at arbitrarily large heights at an arbitrarily slow rate, below any envelope. Rate certifiable, total not — that is the cut.

---

## 6. Final verdict

**On the mandate's single question: (C) — partial, with the exact cut at two independent coordinates.**

**Coordinate 1 (scale, per window):** certifiable ⟺ above resolution.
- $b\log\gamma\to\infty$: countable by density (the only σ-sensitive technology surviving; Lemma 141.M1 marks exactly this threshold).
- $b\log\gamma\asymp1$: signal $\Theta(1)$ per window of support $L\asymp\log\gamma$ — **not buried** (the favorable finding: the sub-resolution wall feared by Doc 168 is not one of size); certification blocked by per-window evaluation (GAP-141.G1) and by the sea's variance at resolution (Montgomery, conditional). Unconditional window-certification threshold: $\omega=\tfrac14$ in all three routes (pointwise/linear/quadratic) — D152's jurisdiction is optimal.
- $b\log\gamma\to0$: buried in every evaluable window.

**Coordinate 2 (rate vs. total):** the growth envelope is a theorem ([THEOREM 170.5–COR 170.6]); the total value $I(0^+)$ (even $<\infty$) is not separable by averages ([THEOREM 170.8]) and its residual content is individual (finiteness by half-strips, [PROP 170.7.3]).

**GAP 167.A thus stands:** NOT certifiable with unconditional averaging tools — confirming the §5.1 attack of Doc 167 but with the mechanism corrected (the cancellation is not in the signal but in the average over translations, [THEOREM 170.3]); its weighted version $\sum b_j^2/(\gamma_j(\log\log\gamma_j)^{1+\varepsilon})<\infty$ and its envelope $E(T)\ll T/\log T$ are unconditional theorems; its non-certifiable content is exactly "$m<\infty$ per half-strip" — the Fredholm half again, now measured precisely.

**[Declared WISH, the only gap with a statement shape:]** an unconditional evaluation of $\mathfrak D(h_\tau)$ (Prop. 170.1(iii)) per individual window at support $L\asymp\log\gamma$ with error $o(1)$ — this is GAP-141.G1/Conj. 108-N. At second order that is the ONLY blockage at the marginal scale; at first order not even that was enough (the signal was zero). It is the weakest known formulation of the wall where crossing it would yield something (window bounds on $\sum_{j:\gamma_j\approx\tau}(b_j\log\gamma_j)^2$).

### Errata
- **E-170.1 (Doc 168 §5.2):** the footprint is $\Delta_j=-b_j^2h''(\gamma_j)+O(b_j^4)$ (minus sign); the statement "$\sum_jb_j^2h''(\gamma_j)$" has the sign flipped. Harmless for 168's conclusions (it only uses size and order). Record in 06-papers/ERRATA.md if propagated.

### References
Weil, A. (1952), *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Lund. — Iwaniec, H., Kowalski, E. (2004), *Analytic Number Theory*, AMS Colloq. 53, Thm. 5.12. — Selberg, A. (1946), *Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. 48 (density theorem $N(\sigma,T)\ll T^{1-(\sigma-1/2)/4}\log T$; moments of $S(t)$). — Littlewood, J.E. (1924), *On the zeros of the Riemann zeta-function*, Proc. Camb. Phil. Soc. 22 (Littlewood's lemma; $\int_0^TS$). — Titchmarsh, E.C. (1986), *The Theory of the Riemann Zeta-Function*, 2nd ed. (Heath-Brown), §9. — Ingham, A.E. (1940), *On the estimation of $N(\sigma,T)$*, Quart. J. Math. 11. — Huxley, M.N. (1972), *On the difference between consecutive primes*, Invent. Math. 15. — Montgomery, H.L. (1973), *The pair correlation of zeros of the zeta function*, Proc. Symp. Pure Math. 24 (conditional on RH). — Goldston, D.A., Montgomery, H.L. (1987), *Pair correlation of zeros and primes in short intervals*, in Analytic Number Theory and Dioph. Probl. — Montgomery, H.L., Vaughan, R.C. (1974), *Hilbert's inequality*, J. London Math. Soc. 8 (mean value theorem). — Cramér, H. (1921), *Ein Mittelwertsatz in der Primzahltheorie*, Math. Z. 12 (**conditional on RH** — cited only as such). — Bohr, H., Landau, E. (1914), C. R. Acad. Sci. Paris 158. — Backlund, R. (1918), *Über die Nullstellen der Riemannschen Zetafunktion*, Acta Math. 41 ($S(t)\ll\log t$). — Platt, D., Trudgian, T. (2021), *The Riemann hypothesis is true up to $3\cdot10^{12}$*, Bull. LMS 53. — Internal docs: 134, 141, 152 (Phase 48), 167, 168.

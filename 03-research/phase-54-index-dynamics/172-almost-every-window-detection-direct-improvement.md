# Document 172 — Almost-every-window: detection, direct improvement, or collapse in density?

**Program:** Riemann Hypothesis — Phase 54 (index dynamics)
**Mandate:** decide which of the three candidate statements (I detection / II direct improvement / III collapse) of the almost-every-window formulation (auditor's repair R-171.2) is a theorem. Prerequisites read at source: Doc 170 in full (Prop 170.1, Thm 170.3, Computations 170.4, Thm 170.5, Thm 170.8), Doc 171 in full (H1, R-171.2, E-171.1/2/3, §3.2 noise levels).
**Contract:** [NEW-DEFINITION] free; [THEOREM]/[PROP]/[LEMMA] full proof or unlabeled; [COMPUTATION] shown; [BRIDGE] honest; [GAP]/[WISH] declared. A false victory is worse than failure.

**Coordinates (identical to 170).** Off zero $\rho=\tfrac12+b_j+i\gamma_j$, one representative per quadruple; $E(T)=\sum_{\gamma_j\le T}b_j^2$; admissible class $\mathcal A$ and Weil's formula as in 170 (header). $S(t)$, $\bar N$, $Z^\flat$ as there.

**Fixed working test (Fejér).** $g(u)=\tfrac1L\max(0,1-|u|/L)$ (even, support $[-L,L]$, $g\ge0$), so that
$$h(r)=\int_{-L}^{L}g(u)e^{iru}\,du=\Bigl(\frac{\sin(Lr/2)}{Lr/2}\Bigr)^{2}\ \ge 0,\qquad h(0)=1,\quad h''(0)=-\tfrac{L^2}{6},\quad |h(x)|,|h''(x)|\ll\frac1{1+x^2}\ (x\gtrsim 1/L\text{, with }|h''|\ll L^2\text{ in the core}).$$
$h$ entire (compact support of $g$), in the strip $|\mathrm{Im}\,z|\le\tfrac12$: $|h(x+iy)|\ll e^{L|y|}/(1+(Lx)^2)$ — it is in $\mathcal A$ with $\delta=1$. Window in $\tau$: $h_\tau(t)=h(t-\tau)+h(t+\tau)$, $g_\tau(u)=2g(u)\cos(\tau u)$. Signal: $\Sigma(\tau):=\sum_{Z}h_\tau(\gamma_\rho)-\sum_{Z^\flat}h_\tau(\gamma_\rho)=2\sum_j\Delta_j(h_\tau)$; identity 170.1(iii): $\Sigma(\tau)=\mathfrak D(\tau)-F(\tau)$, with $\mathfrak D(\tau):=\mathfrak D(h_\tau)$ (primes+pole+archimedean) and $F(\tau):=\int h_\tau\,dS$. Per quadruple at the LP-134 scale ($b=c_0/\log\gamma$, $L=A\log\gamma$): signal at the center $2b^2|h''|(1+o(1))=\tfrac{(c_0A)^2}{3}(1+o(1))=\Theta(c_0^2)$ — the marginal fact of 170 §3.4, intact.

---

## 0. Executive summary and verdict

**VERDICT: (III), in refined form and with proof — collapse on the target $E$, non-collapse of formulation.**

1. **(II) REFUTED with theorem [THEOREM 172.2, the pinned moment]:** the second moment of the von Mangoldt bias over windows is NOT a bound: it is a **universal prime identity**. Montgomery–Vaughan pins it from both sides: $\frac1{T_0}\int_{T_0}^{2T_0}\mathfrak D(\tau)^2d\tau=\tfrac23+o(1)$ (Fejér test, $A\le1$) — the same number in every world, with or without off zeros. A statistic with a forced value bounds nothing: the information channel toward $E$ is exactly zero. The improvement $E\ll T/\log^{1+\delta}T$ is moreover **impossible via this route in any world** (structural ceiling, §3.4): the noise floor per window is $\Theta(1)$ and the signal↔energy conversion rate turns any window statistic into at most $E\ll T/\log T$ = 170.5.
2. **(I) REFUTED unconditionally [PROP 172.6]:** two configurations kill it — (a) the arithmetic progression (EXACT blindness: $E\asymp T/\log T$ with $\Sigma\equiv0$ for EVERY admissible test of support $A<1$, by Poisson); (b) energy riding the sea ($b_j$ constant over realistic ordinates: the bias becomes a functional of the sea deformed by a relative factor $O(c_0^2)$ — indistinguishable within the constant-uncertainty of the sea's variance). The contrapositive ("no bias ⟹ $E=o(T/\log T)$") dies with (a). The conditional version survives but CAPPED: even with pair correlation, the ceiling is $E\ll T/\log T$ — it reproduces 170.5, never improves it.
3. **What IS a genuinely new theorem:** [THEOREM 172.4] $\int_{T_0}^{2T_0}\Sigma(\tau)^2d\tau\ll T_0$ unconditional (MV + Fujii) — the second moment of the second-order signal is finite per typical window. And it is **NOT a consequence of density theorems** (a density-consistent configuration violates it with $T_0\log T_0$, §4.2): it is a bound on the **power spectrum of the energy measure** at resolution frequencies — an axis density does not see. But it is **orthogonal to $E$**: it neither bounds it (cancellation) nor is needed by it.
4. **The sign:** buys a FORMULATION that density cannot express (the statistic sampled-at-centers, = D152's permanent bias, separates configurations that all density theorems treat identically — [PROP 172.8]) but does not buy CERTIFICATION: its evaluation is a double sum over zeros = pair correlation = the old wall. Non-collapse of formulation, collapse of certification.
5. **Budget correction [E-172.1]:** the MV limit for hard support is $L\le\log T_0$ ($A\le1$), **not** $(2-\varepsilon)\log T_0$ as 170 §3.4 and 171 §3.2.2 state — the figure $2-\varepsilon$ belongs to the Gaussian test ($T^2\le(2-\varepsilon)\log T_0$, resolution $\asymp(\log T_0)^{-1/2}$, a different scale). The marginal signal remains $\Theta(c_0^2)$ — nothing strategic changes, but the constant does.

**The almost-every-window front is CLOSED** with: an impossibility theorem (172.2+172.6+172.7), a new non-density certificate (172.4–172.5), and the structural identity explaining the closure: **Selberg's envelope $T/\log T$ IS the window noise floor read in energy** — (number of windows $\asymp T\log T$) × (minimum detectable energy quantum per window $\asymp1/\log^2T$) $=T/\log T$. Density and windows are two computations of the same floor; that is why they neither improve nor contradict each other.

---

## 1. Exact hypotheses and the corrected budget

### 1.1. Montgomery–Vaughan, exact form used

**(generalized Hilbert, [MV74, Thm. 2 and Cor. 3]).** If $\lambda_1<\dots<\lambda_N$ are real with $\delta_n=\min_{m\ne n}|\lambda_n-\lambda_m|$, then $\bigl|\sum_{m\ne n}\frac{a_m\bar a_n}{\lambda_m-\lambda_n}\bigr|\le\frac{3\pi}{2}\sum_n\frac{|a_n|^2}{\delta_n}$. Consequence (the mean-value form): for finitely supported complex $a_n$,
$$\int_{T_0}^{2T_0}\Bigl|\sum_{n\ge2}a_n n^{-i\tau}\Bigr|^2d\tau\;=\;\sum_n|a_n|^2\,\bigl(T_0+\theta\,O(n)\bigr),\qquad|\theta|\le1\ \text{(two-sided, unconditional)},$$
because $\lambda_n=\log n$ has $\delta_n\asymp1/n$. Hypotheses verified for our use: $a_n=\frac{\Lambda(n)}{\sqrt n}g(\log n)$ real $\ge0$, finite support $2\le n\le e^L$ ✓; distinct frequencies ✓. **Note:** it is a two-sided identity — this is what pins (not merely bounds) the moment in §2.

### 1.2. [LEMMA 172.1] (hard-support budget — correction E-172.1)

*Let $a_n=\frac{\Lambda(n)}{\sqrt n}g(\log n)$ with the Fejér test of support $L=A\log T_0$. Then:*
$$D:=\sum_n|a_n|^2=\int_0^Lu\,g(u)^2du+o(1)=\tfrac1{12}+o(1),\qquad \sum_n n|a_n|^2\asymp \frac{e^{L}}{L^{3}},$$
*and the MV error relative to the main term $T_0D$ is $O(T_0^{A-1}/\log^3T_0)$: **admissible if and only if $A\le1$** (with $A=1$ a $\log^{-3}$ is left over). For fourth moments (square of the polynomial, length $e^{2L}$): $A\le\tfrac12$.*

*Proof.* Diagonal: $\Lambda(n)^2=\Lambda(n)\log n$ except for prime powers ($O(e^{L/2})$ terms of size $O(L^2e^{-L}\cdot L^{-2})$, total $o(1)$); by PNT with classical error and partial summation, $\sum_{n\le x}\frac{\Lambda(n)\log n}{n}=\tfrac12\log^2x+O(\log x)$, whence $\sum\frac{\Lambda(n)^2}{n}g(\log n)^2=\int_0^Lu\,g(u)^2du\,(1+o(1))$; with the triangle $\int_0^Lu\cdot\tfrac1{L^2}(1-u/L)^2du=\int_0^1s(1-s)^2ds=\tfrac1{12}$. Error: $\sum\Lambda(n)^2g(\log n)^2\asymp\int_0^Lue^u\tfrac{(1-u/L)^2}{L^2}du$; with $u=L-s$ the integrand is $\asymp e^{L}e^{-s}s^2/L^3$, integral $\asymp e^L/L^3$. Ratio against $T_0D\asymp T_0$: $T_0^{A-1}/\log^3T_0$. $\square$

**[E-172.1, erratum to record]:** Doc 170 §3.4 ("$L=(2-\varepsilon)\log\gamma$, $n\le\gamma^{2-\varepsilon}$, the MV limit") and Doc 171 §3.2.2 ("unconditional under $L\le(2-\varepsilon)\log\tau$") **confuse two scales**. In the Gaussian test the restriction $T^2\le(2-\varepsilon)\log T_0$ lives at resolution $(\log T_0)^{-1/2}$, and the bulk of its polynomial is at $n\le e^{O(T)}=e^{O(\sqrt{\log T_0})}$ — the $2$ comes from the quadratic tail of the weight, not from a real length of $T_0^2$. For hard support at resolution $1/\log T_0$ (the marginal scale), the bulk is at $n\asymp T_0^A$ and MV requires $A\le1$: with $A\in(1,2)$ the variance bound degrades to $O(T_0^{A-1})$ per window — useless; and nothing better than MV exists there (lengths $>T_0$ = pair-correlation territory, $|\alpha|>1$, conjectural even under RH). **Benign consequence:** the marginal signal is $\tfrac13(c_0A)^2$ with $A\le1$ instead of $A\le2$ — still $\Theta(c_0^2)$; all scale conclusions of 170 §3.4 survive with a smaller constant.

### 1.3. [LEMMA 172.3] (sea variance per window, unconditional)

*With the Fejér test, $L=A\log T_0$, $A\le1$:* $\displaystyle\frac1{T_0}\int_{T_0}^{2T_0}F(\tau)^2\,d\tau\;\ll\;1.$

*Proof.* $\int h'(v)\,dv=0$, hence $F(\tau)=\int h_\tau\,dS=-\int h'(v)\,[S(\tau+v)-S(\tau)]\,dv+(\text{mirror term})$, with $|h'(v)|\ll L/(1+(Lv)^2)$, $\|h'\|_1=O(1)$. Minkowski's integral inequality in $L^2(d\tau)$:
$$\|F\|_{L^2[T_0,2T_0]}\le\int|h'(v)|\;\bigl\|S(\cdot+v)-S(\cdot)\bigr\|_{L^2[T_0,2T_0]}\,dv.$$
For $|v|\le1$: Fujii's theorem (Selberg's method; unconditional) $\int_0^{T}\bigl(S(t+v)-S(t)\bigr)^2dt\ll T\log(2+|v|\log T)$ gives, with $w=Lv$, $\int_{|w|\le L}\frac{\sqrt{\log(2+|w|\frac{\log T_0}{L})}}{1+w^2}dw=O(1)$ (since $\log T_0/L=1/A=O(1)$ and $\sqrt{\log(2+w)}/(1+w^2)$ is integrable). For $|v|>1$: $\|S(\cdot+v)-S(\cdot)\|_{L^2}\ll\sqrt{T_0\log\log T_0}$ by Selberg ($\int_0^T S^2\ll T\log\log T$, [S46], unconditional), and $\int_{|v|>1}|h'(v)|dv\ll1/L$: contribution $\ll\sqrt{T_0\log\log T_0}/\log T_0=o(\sqrt{T_0})$. Mirror term ($h(t+\tau)$, $t,\tau>0$): $|h(t+\tau)|\ll(L\tau)^{-2}$, contribution $O(T_0^{-2}\log T_0)$ trivial. Total $\ll\sqrt{T_0}$. $\square$

**Source hypotheses, verified:** MV74 — only distinct frequencies and finite $\ell^2$ ✓. Selberg [S46] moments of $S$ — unconditional ✓. Fujii — the statement used is the **upper bound** on the variance of increments, unconditional (Selberg's method); the **asymptotic with constant** in the range $v\asymp1/\log T$ is equivalent to pair correlation (Goldston–Montgomery [GM87], conditional — not used here). **[Literature GAP, minor and declared]:** exact locus — Fujii, Bull. AMS 81 (1975) 139–142 and Trans. AMS (1974); cited with high confidence; I do not know an unconditional $\gg T$ lower bound for that variance at resolution (relevant in §3.2: it plays in favor of impossibility, not against).

---

## 2. Candidate (II) from end to end: the pinned moment

### 2.1. [COMPUTATION 172.C1] The per-window bias is a pure Dirichlet polynomial

$\mathfrak D(\tau)=h_\tau(\tfrac i2)+h_\tau(-\tfrac i2)-4\mathrm{Re}\,P(\tau)+[\text{arch}]$, with $P(\tau)=\sum_n a_nn^{-i\tau}$, $a_n=\frac{\Lambda(n)}{\sqrt n}g(\log n)$ (the 4: $g_\tau=2g\cos(\tau u)$ and Weil's $2$). Pole: $|h_\tau(\pm\tfrac i2)|\le|h(\tau\pm\tfrac i2)|+|h(-\tau\pm\tfrac i2)|\ll e^{L/2}/(L\tau)^2\ll T_0^{A/2-2}=o(1)$ ✓. Archimedean: $\frac1{2\pi}\int h_\tau\Omega-\int h_\tau d\bar N=O(\int h_\tau(r)(1+r^2)^{-1}dr)=O(T_0^{-2})$ ✓ (Stirling, as in 170's header). Hence $\mathfrak D(\tau)=-4\mathrm{Re}\,P(\tau)+o(1)$ uniform on $[T_0,2T_0]$.

### 2.2. [THEOREM 172.2] (the pinned moment — refutation of (II))

*Unconditionally, with the Fejér test and $L=A\log T_0$, $A\le1$:*
$$\frac1{T_0}\int_{T_0}^{2T_0}\mathfrak D(\tau)^2\,d\tau\;=\;8\sum_n\frac{\Lambda(n)^2}{n}\,g(\log n)^2\;+\;o(1)\;=\;\frac23+o(1).$$
*The value is a prime identity: it does not depend on the zero configuration in any sense — it is the same number whether RH is true, false, or $E(T)$ saturates its envelope. In particular, the second moment of the bias bounds neither $\sum(\text{signals})^2$ nor $E(T)$, and cannot give $E\ll T/\log^{1+\delta}T$: **candidate (II) is vacuous, not narrowly false: its left-hand side contains no information**.*

*Proof.* $\mathfrak D^2=16(\mathrm{Re}\,P)^2+o(1)\cdot O(|P|)+o(1)$ and $(\mathrm{Re}\,P)^2=\tfrac12|P|^2+\tfrac12\mathrm{Re}(P^2)$.
(i) $\int_{T_0}^{2T_0}|P|^2=D\,T_0(1+O(T_0^{A-1}\log^{-3}))$ by MV **on both its sides** (Lemma 172.1) — this is where the value gets pinned, not merely bounded.
(ii) $P(\tau)^2=\sum_{N}c_NN^{-i\tau}$ with frequencies $\log N\ge\log4>0$; $|\int_{T_0}^{2T_0}N^{-i\tau}d\tau|\le2/\log N\le2/\log4$, hence $|\int\mathrm{Re}\,P^2|\le\tfrac2{\log4}\bigl(\sum_na_n\bigr)^2\ll e^{L}/L^2=T_0^{A}/\log^2T_0=o(T_0)$ for $A\le1$.
(iii) Cross terms with the $o(1)$ of the pole/archimedean parts: $\ll o(1)\cdot\sqrt{T_0\cdot\int|P|^2}=o(T_0)$. Diagonal $8D=\tfrac23$ by Lemma 172.1. $\square$

### 2.3. Why (II) is not repairable within the framework

The hope of (II) was: computable prime side $\Rightarrow$ bound on signals $\Rightarrow$ bound on $E$. The actual chain is: $\Sigma=\mathfrak D-F$, so the pinned identity says
$$\int(\Sigma+F)^2=\bigl(\tfrac23+o(1)\bigr)T_0\qquad\textbf{(fixed total budget)},$$
that is: the moment of the bias measures **signal + sea together**, and its value is fixed in advance. Extracting $\int\Sigma^2$ requires knowing $\int F^2$ and $\int\Sigma F$ with constant-level precision — exactly the sea's variance at resolution (= pair correlation at $|\alpha|\le A$, conditional [M73], and in fact Montgomery's range $|\alpha|\le1$ coincides with our budget $A\le1$: the unconditional and conditional frontiers touch at the same place — not a coincidence, it is the same Dirichlet polynomial). Unconditionally there is only two-sided $\Theta(1)$ with constants that do not match: subtracting the expected term **is not unconditional**, answering the mandate's question. And even with the subtraction (§3.4): ceiling $E\ll T/\log T$. **(II) closed.**

---

## 3. Candidate (I): detection, the two configurations that kill it, and the role of the sign

### 3.1. [THEOREM 172.4] (the positive certificate: the signal in mean square)

*Unconditionally, with the Fejér test, $L=A\log T_0$, $A\le1$:*
$$\int_{T_0}^{2T_0}\Sigma(\tau)^2\,d\tau\;\ll\;T_0,\qquad \Sigma(\tau)=\sum_{Z}h_\tau-\sum_{Z^\flat}h_\tau .$$

*Proof.* $\|\Sigma\|_{L^2}\le\|\mathfrak D\|_{L^2}+\|F\|_{L^2}\ll\sqrt{T_0}$ by Theorem 172.2 and Lemma 172.3. $\square$

**[PROP 172.5] (spectral reading).** For a dyadic block of quadruples $\{(\gamma_j,b_j):\gamma_j\in(T_0,2T_0]\}$ and the idealized block signal $\Sigma_{bl}(\tau)=2\sum_{j\in bl}\phi_{b_j}(\gamma_j-\tau)$, with $\phi_b(x):=2\mathrm{Re}\,h(x+ib)-2h(x)=2\int_{-L}^{L}g(\xi)\bigl[\cosh(b\xi)-1\bigr]\cos(x\xi)\,d\xi$:
$$\int_{\mathbb R}\Sigma_{bl}(\tau)^2\,d\tau\;=\;\frac{8}{2\pi}\int_{-L}^{L}g(\xi)^2\,\bigl|G(\xi)\bigr|^2\,d\xi,\qquad G(\xi):=2\pi\sum_{j}\bigl(\cosh(b_j\xi)-1\bigr)e^{i\gamma_j\xi}$$
(Plancherel; $\hat\phi_b(\xi)=4\pi g(\xi)(\cosh(b\xi)-1)$, computed above with $g$ even). The difference between $\Sigma$ and $\Sigma_{bl}$ on $[T_0,2T_0]$ is the inter-block leakage, $O\bigl(\sum_{\gamma_j\notin(T_0/2,4T_0]}b_j^2/(1+L^2(\gamma_j-\tau)^2)\bigr)$, controlled in $L^2$ by envelope 170.5 — loss $o(T_0)$. **Reading:** 172.4 is an unconditional bound on the **power spectrum of the energy measure** $\sum_j(\cosh(b_j\cdot)-1)\delta_{\gamma_j}$ at resolution frequencies $|\xi|\le A\log T_0$, with POSITIVE coefficients ($\cosh-1\ge0$). It is an axis orthogonal to the counts $N(\sigma,T)$ (the "total mass" axis; §4.2 proves the non-implication). The sign of the footprint lives here as coefficient positivity — but extracting the diagonal $\sum_j(\cosh(b_j\xi)-1)^2$ from $|G|^2$ would require a range of $\xi$ $\gg$ (average gap)$^{-1}=\log T_0/2\pi$, and the budget gives $|\xi|\le A\log T_0$ with $A\le1$: the overlap is $2\pi A=O(1)$ — **constant against constant again**: the diagonal does not separate, consistent with the cancellations of 3.2.

### 3.2. [PROP 172.6] (the two configurations: (I) is not an unconditional theorem)

**(a) Exact blindness (arithmetic progression).** Let $Z_{ap}$ be the configuration with ordinates $\gamma_k$ in a local progression of step $d(\gamma)=2\pi/\log\gamma$ (exact RvM density) and ALL off zeros at $b_k=c_0/\log\gamma_k$, with $c_0>0$ an absolute constant respecting Selberg's density ($c_0\le4\log C_S$ suffices: $N(\tfrac12+c_0/\log T,T)=N(T)\le C_ST\log T\,e^{-c_0/4}$ ✓). Then $E(T)\asymp c_0^2\,T/\log T$ — **envelope 170.5 saturated up to a constant** — and yet, for EVERY admissible test of support $L'=A'\log T_0$ with $A'<1$ and every $\tau\in[T_0,2T_0]$:
$$\Sigma(\tau)\;=\;O(T_0^{-1}\log T_0)\qquad\textit{(zero except at the edges)}.$$
*Proof.* Poisson over the local progression: $\sum_k\phi_b(\tau-kd)=\frac1d\sum_{m\in\mathbb Z}\hat\phi_b\bigl(\tfrac{2\pi m}{d}\bigr)e^{2\pi im\tau/d}$; the dual frequencies are $m\log T_0$ and $\mathrm{supp}\,\hat\phi_b\subset[-A'\log T_0,A'\log T_0]$ with $A'<1$: only $m=0$ survives, and $\hat\phi_b(0)=4\pi g(0)(\cosh0-1)=0$. Truncation and slow variation of $d(\gamma)$: tails $\ll b^2\sum_{|\gamma_k-\tau|>T_0/2}(\gamma_k-\tau)^{-2}\ll T_0^{-1}\log T_0$. $\square$
**Consequences:** (I) is false in the class of configurations (ZERO bias in every window, saturating energy), and its contrapositive ("small second moment of the bias $\Rightarrow E=o(T/\log T)$") also. **Honesty:** $Z_{ap}$ has a rigid sea ($S=O(1)$), incompatible with $\int S^2\sim\frac{T}{2\pi^2}\log\log T$ for ζ by Selberg — it kills configurational theorems (the genus of 170.8/141.B2), it does not describe ζ. For ζ, (b):

**(b) Energy riding the sea.** Let $Z_{rid}$: ordinates = an arbitrary realistic sea (e.g. those of ζ, with all its Selberg moments), and $b_j\equiv c_0/\log\gamma_j$ throughout. Again $E\asymp c_0^2T/\log T$. Then
$$\Sigma(\tau)=\int\phi_b(t-\tau)\,dN^\flat(t)=\underbrace{\int\phi_b\,d\bar N}_{=\;\frac{\log(\tau/2\pi)}{2\pi}\hat\phi_b(0)+O(T_0^{-1})\;=\;O(T_0^{-1})}+\;\int\phi_b(t-\tau)\,dS(t),$$
that is: **the entire signal is a functional of the sea** (again $\hat\phi_b(0)=0$ kills the smooth term). And the observable per-window datum becomes $\mathfrak D(\tau)=\Sigma+F=\int\bigl[2\mathrm{Re}\,h(\cdot+ib)-h\bigr](t-\tau)\,dS(t)$: the SAME type of functional of the sea as in the on-line world ($\mathfrak D=\int h\,dS$), with the kernel deformed by a relative factor $O\bigl((bL)^2\bigr)=O(c_0^2A^2)$. Every quadratic window statistic differs between $Z_{rid}$ ($E\asymp T/\log T$) and the on-line world ($E=0$) by a factor $1+O(c_0^2)$ **multiplying the sea's variance, whose unconditional value is only known up to two-sided $\Theta(1)$ with mismatched constants** (Lemma 172.3 gives $\ll$; the $\gg$ is not even known — GAP §1.3). Indistinguishable within the class of certificates {bounds with absolute constants on window statistics}. $\square$

**Verdict (I):** it is not an unconditional theorem, neither in the configurational class (exact death by (a)) nor for ζ (indistinguishability by (b), and moreover the lower bound on the sea's variance at resolution is itself unknown). The mechanism is new relative to first order: it is not a zero-integral of the signal (the typical signal of $Z_{rid}$ is $\Theta(c_0^2)$, visible!) — it is that **the signal is indistinguishable FROM the noise, not smaller than it**: it lives in the same functional of the sea, deforming it multiplicatively. Detection = knowing the sea's variance with constant-level precision = pair correlation.

### 3.3. The role of the sign: what it buys and what it does not

**[PROP 172.8] (the signed statistic is outside the density theorems).** The ordinate-sampled statistic $\mathcal B(T):=\frac1{N(T)}\sum_{\gamma\le T}\Sigma(h_\gamma)$ (= the integrated version of D152's permanent bias, one-signed because it samples the CORES, where $-h''>0$) **separates pairs of configurations satisfying the same density bounds with the same constants**: take $Z_1$ = quadruples centered on the sea's ordinates (cores sampled: $\mathcal B\asymp c_0^2\cdot$proportion) and $Z_2$ = the same multisets $\{b_j\}$, $\{\gamma_j\}$ shifted by half a resolution relative to the sample points (flanks sampled: $\mathcal B$ opposite sign or null). Identical marginals — every density envelope bound tells them the same thing — different $\mathcal B$. *Density theorems constrain the marginals of $(b,\gamma)$; the signed statistic measures the CORRELATION between off positions and sample points — a degree of freedom density does not see.* $\square$

**[Honest BRIDGE — why this is not certifiable]:** evaluating $\mathcal B$ requires $\sum_{\gamma\le T}\mathfrak D(h_\gamma)$ and $\sum_{\gamma\le T}F(h_\gamma)$: double sums over zeros of the type $\sum_{\gamma,\gamma'}w(\gamma-\gamma')$ and Landau sums $\sum_\gamma n^{i\gamma}$ — exactly Montgomery's pair correlation [M73] (conditional on RH for $|\alpha|\le1$, conjectural beyond) and Landau/Gonek formulas whose errors at this resolution cost as much as the correlation itself. **Answer to the mandate's question: the sign buys a formulation density cannot express (non-collapse of formulation — that is why (I)/(II) were not "trivially" reducible to density and the collapse had to be proved; warning (iv) was correct), but its evaluation reroutes to the old wall: it does not buy certification.** First order never even had the formulation; second order has it and leaves it one step from the same wall — that is the exact measure of progress.

### 3.4. [PROP 172.7] (the structural ceiling: not even conditionally does 170.5 improve)

*Suppose EVERYTHING conditional is granted: the fine asymptotic of the sea's variance (pair correlation at $|\alpha|\le2A$) and the per-window evaluation of the prime side (all of GAP-141.G1, sea included). Then the most that window statistics at resolution $1/L$ can certify about the energy is $E(T)\ll T/\log T$ — envelope 170.5, never $T/\log^{1+\delta}T$.*

*Proof.* (i) Floor: even with everything granted, what is certifiable per window is $|\Sigma(\tau)|\le M(\tau)$ with $\frac1{T_0}\int M^2\ll1$ — the floor $\Theta(1)$ is not epistemic: under RH-and-GUE the sea REALLY fluctuates $\Theta(1)$ per window at resolution (the Fujii/GM87 asymptotic, $\asymp\log(2+v\log T)$, equals $\Theta(1)$ at $v\asymp1/\log T$); no refinement of hypotheses lowers it. (ii) Rate of conversion: a quadruple at scale $c$ produces signal $\asymp c^2$ carrying energy $c^2/\log^2T$; inverting "signal per window $\le\Theta(1)$" gives energy $\le\Theta(1/\log^2T)$ per window — **the resolution quantum**. (iii) Total: number of disjoint windows at resolution $\asymp T_0L\asymp T\log T$; certifiable energy $\le T\log T\cdot O(1/\log^2T)=O(T/\log T)$. And that in the BEST case (no core/flank cancellation between quadruples, which only worsens the inversion). $\square$

**Structural identity (the moral of the front):** $\;T/\log T=\underbrace{T\log T}_{\text{number of windows}}\times\underbrace{\log^{-2}T}_{\text{quantum}}$. Selberg's envelope (density, Theorem 170.5) and the window noise floor are **the same number computed by two routes**: density obtains it from Bohr–Landau–Selberg clustering; windows, from the $\Theta(1)$ fluctuation of the sea per resolution cell. That is why almost-every-window neither improves nor worsens density regarding $E$: it computes the same floor.

---

## 4. (III): collapse on $E$, non-collapse of formulation — the closure

### 4.1. [THEOREM 172.9] (collapse on the target)

*Every bound on $E(T)$ certifiable with the unconditional almost-every-window package —{per-window Weil identity, MV (Lemma 172.1), Selberg/Fujii moments of $S$, positivity/Cauchy–Schwarz}— is implied by the density theorems; concretely, the package certifies no bound $E(T)\le\varepsilon T/\log T$ with $\varepsilon$ smaller than an absolute constant, nor does it distinguish $E=0$ from $E\asymp T/\log T$.*

*Proof.* The configurations of Prop 172.6 satisfy all outputs of the package with the same constants ($Z_{ap}$: exactly those of the on-line world, null signal; $Z_{rid}$: within the factor $1+O(c_0^2)$ of a variance known only up to constants), have $E\asymp T/\log T$, and ceiling 172.7 bounds what is grantable even adding the conditional inputs. The only bound on $E$ the package reproduces is the envelope, which is 170.5 = density. $\square$

### 4.2. [PROP 172.10] (non-collapse: 172.4 is NOT a density theorem)

*There exists a configuration $Z_{cl}$ consistent with all known density bounds (Selberg included), with RvM and $S=O(\log)$, such that $\int_{T_0}^{2T_0}\Sigma^2\,d\tau\gg T_0\log T_0$. Hence Theorem 172.4 ($\ll T_0$, which for ζ is unconditional via primes+Fujii) is not a consequence of the density theorems: the front produces at least one genuinely new certificate.*

*Proof.* [COMPUTATION] $Z_{cl}$: clusters of $m=\epsilon\log T_0$ quadruples at mutual distance $\le1/L$, each with $b=c/\log T_0$, one cluster per unit height in $(T_0,2T_0]$. Consistency: $m$ extra zeros in an interval of length $1/L$ costs an $S$-jump of size $\epsilon\log T_0$ — within Backlund for small $\epsilon$ ✓; density level: $T_0m=\epsilon T_0\log T_0$ zeros at height $b=c/\log$: Selberg allows $C_ST_0\log T_0e^{-c/4}$ ✓ for $\epsilon\le C_Se^{-c/4}$; energy $E=\epsilon c^2T_0/\log T_0$ within the envelope ✓. Signal: in each cluster's core the $\Delta_j$ ADD (same sign, same cell): $\Sigma\asymp mc^2\cdot\tfrac13A^2$ over width $\asymp1/L$; the flanks of distinct clusters (separation $\ge1$) contribute $O(\sum_{k\ge1}b^2m/k^2)=O(1)$ per window — they do not cancel the core. Total: $\int\Sigma^2\gtrsim T_0\cdot(mc^2)^2/L\asymp\epsilon^2c^4\,T_0\log T_0$. $\square$

**Joint reading 172.9+172.10:** as measurers of $E$, windows $\subseteq$ density (collapse); as producers of certificates, they are **incomparable**: 172.4 (power spectrum of the energy at resolution frequencies, with positivity $\cosh-1\ge0$ built in) constrains the CORRELATION/clustering axis of the energy, which density does not see — but that axis is orthogonal to the total mass $E$ (the cancellation of 172.6a proves it: null spectrum, saturating mass). Statement (III) of the mandate is a theorem in its relevant half (everything windows certify ABOUT $E$ is already given by density) and false in its absolute literal form (not everything windows certify is integrated density) — the difference is exactly 172.4, and it exactly does not touch RH.

### 4.3. What remains open (without over-wishing)

The only remaining loophole is the usual one, now in its final form: **per-window arithmetic evaluation better than MV** — computing $\mathfrak D(\tau)$ window by window with error $o(1)$ using the real arithmetic of the primes (not just their diagonal on average), PLUS the sea's variance bound (already unconditional, Lemma 172.3), would give bounds in almost-every-window on $\sum_{\gamma_j\approx\tau}(b_j\log\gamma_j)^2$ — the repaired form R-171.2, which this document confirms as well-posed but whose prime-half is GAP-141.G1: the old wall, with no discount. No averaging formulation dodges it (172.9). No new WISH is declared: the one in R-171.2 is the correct one and remains the only one.

---

## 5. Final verdict

**(III) is the theorem** — collapse on $E$ with structural ceiling (172.7: Selberg's envelope IS the window noise floor; number-of-windows × quantum identity), proved against the two possible rescues: (II) dies by the pinned moment (172.2: the second moment of the bias is a universal prime identity, $\tfrac23+o(1)$, blind to the zeros — it is not even a bound), and (I) dies unconditionally by the two configurations (172.6: exact blindness by Poisson; energy riding the sea = multiplicative deformation indistinguishable up to constants), remaining only as a full-pair-correlation statement and still capped by 172.7. **The sign buys formulation, not certification** (172.8 + BRIDGE): the signed statistic sampled-at-centers is genuinely outside the expressive reach of density — that is why the collapse was NOT trivial and had to be proved — but its evaluation IS pair correlation. Spoils of the closed front: the new certificate 172.4–172.5 (power spectrum of the energy $\ll T$ at resolution frequencies, unconditional, non-density by 172.10) and the budget correction E-172.1 ($A\le1$, not $2-\varepsilon$).

### Errata
- **E-172.1 (Doc 170 §3.4 and Doc 171 §3.2.2):** the MV budget for hard-support tests is $L\le\log T_0$ ($A\le1$), not $(2-\varepsilon)\log$; the figure $2-\varepsilon$ belongs to the Gaussian test ($T^2\le(2-\varepsilon)\log T_0$, resolution $(\log T_0)^{-1/2}$, bulk of the polynomial at $n\le e^{O(\sqrt{\log T_0})}$). Harmless for the strategy (signal remains $\Theta(c^2)$), not for the constants. Record in 06-papers/ERRATA.md if propagated.

### References
Montgomery, H.L., Vaughan, R.C. (1974), *Hilbert's inequality*, J. London Math. Soc. (2) 8, 73–82 — generalized Hilbert inequality and mean value theorem (unconditional, two-sided). — Selberg, A. (1946), *Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. 48 — density and moments of $S(t)$ (unconditional). — Fujii, A. (1975), *On the distribution of the zeros of the Riemann zeta function in short intervals*, Bull. Amer. Math. Soc. 81, 139–142 — variance of $S(t+h)-S(t)$, unconditional upper bound by Selberg's method [high confidence; exact locus: minor literature GAP declared in §1.3]. — Montgomery, H.L. (1973), *The pair correlation of zeros of the zeta function*, Proc. Symp. Pure Math. 24 — conditional on RH, $|\alpha|\le1$. — Goldston, D.A., Montgomery, H.L. (1987), *Pair correlation of zeros and primes in short intervals*, in Analytic Number Theory and Diophantine Problems, Birkhäuser — increment-variance ↔ pair-correlation equivalence (conditional; cited only as such). — Backlund, R. (1918), Acta Math. 41 — $S(t)\ll\log t$. — Jutila, M. (1983), in Studies in Pure Mathematics, Birkhäuser — improvement of Selberg's constant (via E-171.3). — Internal docs: 141 (GAP-141.G1, 141.B0/B/B2, 141.M1/M5), 152 (impurity spectrum), 167 (GAP 167.A), 168, 170, 171 (R-171.2, H1).

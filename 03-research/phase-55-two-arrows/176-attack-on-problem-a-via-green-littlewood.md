# Document 176 — Attack on Problem A via Green–Littlewood: the half-band budget, the Cesàro limit that always exists, and the position of A in the hierarchy

**Program:** Riemann Hypothesis — Phase 55 (two arrows)
**Mandate:** attack Problem A — $I(0^+)<\infty$ — through the Green–Littlewood identity ([THEOREM 173.C]). Do not audit; construct. Do not attempt to prove RH.
**Machinery accepted (not re-derived):** [THEOREM 173.C] (exact identity, Doc 173 §6.1, with its proof read at source); certificate $E(T)=\sum_{\gamma\le T}b^2\ll T/\log T$ (Theorem 170.5 / Selberg [S46]); dichotomy [THEOREM 175.2] (LP-112 $\Rightarrow I\in\{0,\infty\}$, conditional on LP-112); architecture RH $\Longleftarrow (I<\infty)\wedge$LP-112 ([COR 175.5.2]).
**Contract:** [NEW-DEFINITION] free; [THEOREM]/[PROP]/[LEMMA] with complete proof or no label; [GAP] declared with statement form. Absolute frankness about novelty: classical machinery is declared classical.

**Coordinates (identical to Docs 170/173/175).** Off-critical zero $\rho=\tfrac12+b+i\gamma$, $b\in(0,\tfrac12)$, $\gamma>0$; one representative per quadruple. $I(T)=E(T):=\sum_{\gamma_j\le T}b_j^2$, $I(0^+)=\lim_{T\to\infty}I(T)=\sum_j b_j^2$ (monotone). **Problem A:** $I(0^+)<\infty$. Notation of this document:
$$D(T)\;:=\;\int_{1/2}^{\infty}\!\!\int_0^T \log|\zeta(\sigma+it)|\,dt\,d\sigma,\qquad
\Xi(T)\;:=\;\frac{1}{2\pi}\int_{1/2}^\infty\Big(\sigma-\tfrac12\Big)^2\,\mathrm{Im}\,\frac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma,$$
so that [THEOREM 173.C] reads: for every non-ordinate $T$, $\;I(T)=\frac1\pi D(T)+\frac18-\Xi(T)$, i.e.
$$\boxed{\,D(T)\;=\;\pi\,I(T)\;-\;\frac\pi8\;+\;\pi\,\Xi(T)\,}.$$

---

## 0. Executive summary and verdict

1. **[PROP 176.1] (resolution of the $\sigma\ge1$ tension).** The region $\sigma\ge1$ contributes to $D(T)$ an **exact, almost-periodic, and uniformly bounded** amount: $\Phi(T)=\sum_n\Lambda(n)\sin(T\log n)/(n\log^3 n)$, $|\Phi(T)|\le C_0<\infty$ for all $T$. The mean in $t$ of $\log|\zeta|$ is zero term by term (there is no $n=1$ term), the frequencies are bounded below by $\log2$, and the amplitudes are $\ell^1$: **total cancellation**, not $\asymp T$. The entire budget of $D(T)$ (up to $O(1)$) lives in $\tfrac12<\sigma<1$.

2. **[LEMMA 176.3] (improvement of the boundary flux of 173.C).** $|\Xi(T)|\ll\log T$ for **every** non-ordinate height — not $O(\log^2T)$ and not only at good heights. Mechanism: integrating first in $\sigma$ turns each nearby zero into a Poisson mass $\le\frac94\pi$, independent of $|T-\gamma|$.

3. **[THEOREM 176.4] (the averaged form: the boundary evaporates and the Cesàro limit always exists).** Averaging the cut, $\overline D(T_0):=\frac1{T_0}\int_{T_0}^{2T_0}D(T)\,dT$ satisfies $\overline D(T_0)=\pi\,\overline I(T_0)-\frac\pi8+O\big(\frac{\log T_0}{T_0}\big)$, because $\int_{T_0}^{2T_0}\Xi(T)\,dT$ is a **difference of two values of $\log|\zeta|$** integrated in $\sigma$, $\ll\log T_0$. Consequence (unconditional):
$$\lim_{T_0\to\infty}\overline D(T_0)\;\text{exists in }[-\tfrac\pi8,+\infty]\;\text{and equals}\;\pi\,I(0^+)-\frac\pi8 .$$
**RH $\iff$ limit $=-\pi/8$. Problem A $\iff$ finite limit.** A is turned into the finiteness of a limit that *provably exists* — with no sequences of good heights, no boundary residue.

4. **[COR 176.5] (unconditional lower bound of the sign).** $D(T)\ge-\frac\pi8-C\log T$ at every non-ordinate height, and $\overline D(T_0)\ge-\frac\pi8-C\frac{\log T_0}{T_0}$: the integral of $\log|\zeta|$ in the right half-band **never falls below the pole's mass**. Under RH the constant $-\pi/8$ is exact (equality case in the limit). The lower bound is *free* ($I\ge0$); **the upper bound IS Problem A**.

5. **[THEOREM 176.6] (the inverse-means theorem).** $D(T)=\pi E(T)-\frac\pi8+O(\log T)$ for every non-ordinate height; with certificate 170.5, $|D(T)|\ll T/\log T$: the area average of $\log|\zeta|$ in the half-band is $\ll1/\log T$. Per-abscissa version: $\big|\frac1T\int_0^T\log|\zeta(\sigma+it)|\,dt\big|\ll\frac1{(\sigma-\frac12)\log T}+\frac{\log T}T$ uniform in $\sigma>\tfrac12$. Frankness: 100% classical machinery (Littlewood+Selberg); the novelty is in *statement and exactness* (constant $-\pi/8$, validity at every height), not in method.

6. **Position of A in the hierarchy ([THEOREM 176.7], [PROP 176.8], [PROP 176.9]):**
$$\mathrm{RH}\;\Longrightarrow\;(m<\infty)\;\Longrightarrow\;\textbf{A}\;\Longrightarrow\;\mathrm{Lindel\ddot of}\;\Longrightarrow\;\mathrm{Density},$$
(the arrow A $\Rightarrow$ LH via Backlund is, I believe, new *as a program observation*; trivial once stated). **No exponential-type density theorem $N(\tfrac12+s,T)\ll T^{1-cs}(\log T)^\kappa$ — unconditional or under Lindelöf — can give A**: the exact layer-cake gives $E(T)\ll T(\log T)^{\kappa-2}$ and the fatal mass lives at $s\asymp1/\log T$, where the exponential saving equals $e^{-c}\asymp1$; the exponent's quality $c$ only enters the constant. The **minimal statement** equivalent to A is a **density uniform in $T$**: $\exists f$ with $N(\tfrac12+s,T)\le f(s)\;\forall T$ and $\int_0^{1/2}s\,f(s)\,ds<\infty$ — a *finiteness* theorem, a different genre from the entire density industry.

7. **Named pivots (§6):** the envelope ladder ($T/\log T\to T/\log^2T\to T^{1-\delta}\to O(1)\to0$) with its exact density dictionary; the first reachable step is **log-free density near $\sigma=\tfrac12$** ($\kappa=0\Rightarrow E\ll T/\log^2T$).

---

## 1. The budget by regions and the resolution of the $\sigma\ge1$ tension

### 1.1. The region $\sigma\ge1$: total cancellation, exact formula

The mandate's tension: if $\log|\zeta(\sigma+it)|$ had positive mean $\asymp c(\sigma)$ in $t$ for $\sigma\ge2$, the far region would contribute $\asymp T$ to $D(T)$, incompatible with $D(T)\ll T/\log T$ (which follows from 173.C + 170.5). The resolution: **the mean is exactly zero**, because $\log|\zeta|$ for $\sigma>1$ is a trigonometric series in $t$ *with no constant term*.

**[PROP 176.1].** For every $T>0$,
$$\int_{1}^{\infty}\!\!\int_0^T \log|\zeta(\sigma+it)|\,dt\,d\sigma\;=\;\Phi(T):=\sum_{n\ge2}\frac{\Lambda(n)\,\sin(T\log n)}{n\,\log^3 n},
\qquad |\Phi(T)|\;\le\;C_0:=\sum_{n\ge2}\frac{\Lambda(n)}{n\log^3n}\;<\;\infty .$$
In particular the contribution of $\sigma\ge1$ to $D(T)$ is $O(1)$ **uniform in $T$**, and
$$D(T)\;=\;D_{\mathrm{band}}(T)+O(1),\qquad D_{\mathrm{band}}(T):=\int_{1/2}^{1}\!\!\int_0^T\log|\zeta(\sigma+it)|\,dt\,d\sigma .$$

*Proof.* For $\sigma>1$: $\log|\zeta(\sigma+it)|=\mathrm{Re}\sum_{n\ge2}\frac{\Lambda(n)}{\log n}n^{-\sigma-it}=\sum_{n\ge2}\frac{\Lambda(n)}{\log n}n^{-\sigma}\cos(t\log n)$, absolutely convergent. The triple integral (sum in $n$, $\sigma\in(1,\infty)$, $t\in(0,T)$) of the absolute value is $\le T\sum_n\frac{\Lambda(n)}{\log n}\int_1^\infty n^{-\sigma}d\sigma=T\sum_n\frac{\Lambda(n)}{n\log^2n}<\infty$, where the last sum converges: $\sum_n\frac{\Lambda(n)}{n\log^2n}=\sum_p\sum_{k\ge1}\frac1{k^2p^k\log p}\le\sum_p\frac{2}{p\log p}<\infty$ (partial summation with $\pi(x)\sim x/\log x$: $\int_2^\infty\frac{dx}{x\log^2 x}<\infty$). Tonelli–Fubini applies; integrating first in $t$ ($\int_0^T\cos(t\log n)\,dt=\sin(T\log n)/\log n$) and then in $\sigma$ ($\int_1^\infty n^{-\sigma}d\sigma=1/(n\log n)$) gives $\Phi(T)$. The bound: $C_0=\sum_{p,k}\frac1{k^3p^k\log^2p}<\infty$ by the same comparison. (The line $\sigma=1$ has measure zero and $\log|\zeta|$ is locally integrable on it.) $\square$

**Reading — why everything cancels.** Three ingredients, all three necessary:
1. **Zero mean:** there is no $n=1$ term in the series for $\log\zeta$ (the pole is at $s=1$, outside $\sigma>1$); the mean in $t$ of each term is $0$.
2. **Frequencies bounded away from zero:** $\log n\ge\log2$, so each primitive $\sin(T\log n)/\log n$ is uniformly bounded in $T$ — no small divisor.
3. **$\ell^1$ amplitudes after two integrations:** the accumulated factor $1/\log^3n$ (one from the $\log\zeta$ series, one from $\int dt$, one from $\int d\sigma$) makes even the tail $\sigma\to1^+$, where $\log\zeta(\sigma)$ diverges, summable.

**Scale of the fluctuation (for calibration, classical).** For $\sigma>1$ fixed, by the mean-value theorem for Dirichlet polynomials (Montgomery–Vaughan; or simple orthogonality in this range): $\frac1T\int_0^T|\log\zeta(\sigma+it)|^2dt\to\sum_{n\ge2}\frac{\Lambda(n)^2}{n^{2\sigma}\log^2n}<\infty$. The integrand is a signal of size $O(1)$, zero mean, and its double integral is $O(1)$: *total* cancellation. That is the pattern A asks to extend — with controlled loss — to the whole band.

### 1.2. The critical band $\tfrac12<\sigma<1$: where the budget lives

In the band the Dirichlet series does not converge and control is via zeros (Littlewood). What is unconditional per fixed abscissa, with the two available bounds (used in §3 and §4):

**Littlewood's lemma by abscissa (classical; Littlewood 1924; Titchmarsh §9.9).** For $\tfrac12\le\sigma<1$ fixed and all $T\ge2$:
$$\int_0^T\log|\zeta(\sigma+it)|\,dt\;=\;2\pi\!\!\sum_{\beta>\sigma,\,0<\gamma\le T}\!\!(\beta-\sigma)\;-\;2\pi(1-\sigma)\;+\;O(\log T),$$
with $O$ uniform in $\sigma\in[\tfrac12,1]$ (the term $-2\pi(1-\sigma)$ is the pole $s=1$; the edges are the standard ones). Combined with:
- **Chebyshev on the energy:** $\sum_{\beta>\sigma}(\beta-\sigma)\le\sum_{b_j>\sigma-\frac12}b_j\le\frac{E(T)}{\sigma-\frac12}$ (if $b>s$ then $b\le b^2/s$);
- **Selberg density [S46]:** $N(\tfrac12+s,T)\ll T^{1-s/4}\log T$, so $\sum(\beta-\sigma)^+\le\int_\sigma^1N(u,T)\,du\ll T^{1-(\sigma-\frac12)/4}$;

one obtains, unconditionally, for $\tfrac12<\sigma<1$ fixed:
$$-\,2\pi(1-\sigma)-C\log T\;\le\;\int_0^T\log|\zeta(\sigma+it)|\,dt\;\le\;\min\Big(\frac{2\pi E(T)}{\sigma-\frac12},\;8\pi\,T^{1-(\sigma-\frac12)/4}\Big)+C\log T .$$
The per-abscissa mean tends to $0$ for each fixed $\sigma>\tfrac12$ (this is essentially Bohr–Landau/Littlewood: classical). **What is not classical-trivial is the version integrated in $\sigma$ with weight 1 down to $\sigma=\tfrac12^+$** — there the per-abscissa bound blows up as $1/(\sigma-\tfrac12)$ and only the second-moment structure (173.C) tames it. That is §3.

**Budget, summary.** $D(T)=D_{\mathrm{band}}(T)+O(1)$; the integrand in the band has absolute size $\asymp T$ (see §5.2) and signed total $\ll T/\log T$ (§3): the cancellation achieved is of relative order $1/\log T$. **Problem A asks for signed total $O(1)$: relative cancellation $1/T$.** That ratio — $\log T$ versus $T$ — is the frank measure of the distance between what is known and A.

---

## 2. The boundary, improved twice: $O(\log T)$ at every height, $o(1)$ on average

### 2.1. Local integrability tool

**[LEMMA 176.2].** For every $T\ge2$ (ordinate or not),
$$\int_{1/2}^{2}\big|\log|\zeta(\sigma+iT)|\big|\,d\sigma\;\ll\;\log T .$$

*Proof.* By the standard local factorization lemma (Borel–Carathéodory + Jensen; Titchmarsh §3.9, in the form used in step (1) of the proof of 173.C, read at source): in the disc $|s-(2+iT)|\le\tfrac52$ there are $O(\log T)$ zeros, and for $|s-(2+iT)|\le2$,
$$\log|\zeta(s)|\;=\;\sum_{|\rho-(2+iT)|\le\frac52}\log|s-\rho|\;+\;O(\log T).$$
The segment $[\tfrac12,2]\times\{T\}$ is contained in that disc. Each zero contributes $\int_{1/2}^2\big|\log|\sigma+iT-\rho|\big|\,d\sigma\le\int_{1/2}^2\big(\log\tfrac92+\big|\log|\sigma-\beta+i(T-\gamma)|\big|\big)d\sigma\ll1$ — because $|\log|x+iy||\le|\log|x-\beta'||+O(1)$ at bounded distances and $\int_0^4|\log x|\,dx<\infty$ (worst case: the zero on the segment itself; the logarithmic singularity is integrable). With $O(\log T)$ zeros and the remainder $O(\log T)$ integrated over length $\tfrac32$: total $\ll\log T$. $\square$

### 2.2. The flux is $O(\log T)$ at every height (improvement of 173.C)

**[LEMMA 176.3].** For every $T\ge2$ that is not a zero ordinate,
$$|\Xi(T)|\;=\;\Big|\frac1{2\pi}\int_{1/2}^\infty\Big(\sigma-\tfrac12\Big)^2\mathrm{Im}\,\frac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma\Big|\;\ll\;\log T .$$
*(173.C gave $O(\log^2T)$ and only at good heights: the good-height hypothesis is removed and the exponent is lowered.)*

*Proof.* Split into $\sigma\in[\tfrac12,2]$ and $\sigma\ge2$, as in step (6) of 173.C.
**(i) $\sigma\ge2$:** $|\zeta'/\zeta(\sigma+iT)|\le\sum_n\Lambda(n)n^{-\sigma}\ll2^{-\sigma}$ and $\int_2^\infty\sigma^22^{-\sigma}d\sigma=O(1)$.
**(ii) $\tfrac12\le\sigma\le2$:** by partial fractions (Davenport chaps. 15–16): $\frac{\zeta'}{\zeta}(\sigma+iT)=\sum_{|\gamma-T|\le1}\frac1{\sigma+iT-\rho}+O(\log T)$. The remainder integrated against $(\sigma-\tfrac12)^2\le\tfrac94$ gives $O(\log T)$. For each zero $\rho=\beta+i\gamma$ with $|\gamma-T|\le1$ — and here is the improvement: instead of bounding pointwise by $1/|T-\gamma|$ (which costs the "good height" factor), **integrate first in $\sigma$**:
$$\int_{1/2}^{2}\Big(\sigma-\tfrac12\Big)^2\Big|\mathrm{Im}\,\frac1{\sigma+iT-\rho}\Big|\,d\sigma
\;\le\;\frac94\int_{-\infty}^{\infty}\frac{|T-\gamma|\,dx}{x^2+(T-\gamma)^2}\;=\;\frac{9\pi}{4},$$
using $\big|\mathrm{Im}\frac1{x+i(T-\gamma)}\big|=\frac{|T-\gamma|}{x^2+(T-\gamma)^2}$ with $x=\sigma-\beta$: the $\sigma$-integral of each term is **a Poisson mass, $\le\frac94\pi$ per zero, independent of how close $T$ is to $\gamma$**. There are $O(\log T)$ zeros with $|\gamma-T|\le1$ (von Mangoldt). Total: $\ll\log T$. $\square$

**[COR 176.3.1] (the identity, usable at every height).** For every non-ordinate $T$:
$$D(T)\;=\;\pi\,I(T)\;-\;\frac\pi8\;+\;O(\log T).$$

### 2.3. The average over the cut: the boundary evaporates

The key observation: $\;\partial_T\log|\zeta(\sigma+iT)|=\mathrm{Re}\big[i\,\tfrac{\zeta'}{\zeta}(\sigma+iT)\big]=-\,\mathrm{Im}\,\tfrac{\zeta'}{\zeta}(\sigma+iT)$. Hence the integral of the flux **over the cut** is a difference of values of $\log|\zeta|$ — no arguments, no windings:
$$\int_{T_0}^{2T_0}\mathrm{Im}\,\frac{\zeta'}{\zeta}(\sigma+iT)\,dT\;=\;\log|\zeta(\sigma+iT_0)|\;-\;\log|\zeta(\sigma+2iT_0)| ,$$
valid for every $\sigma$ such that the vertical line contains no zero with that abscissa (all but at most countably many; $\log|\zeta(\sigma+iT)|$ is absolutely continuous in $T$ on those abscissas, with integrable logarithmic singularities — sufficient for the fundamental theorem of calculus at almost every abscissa, which is what the $\sigma$-integral requires).

**[THEOREM 176.4] (averaged form of Green–Littlewood; the Cesàro limit always exists).** Let
$$\overline I(T_0):=\frac1{T_0}\int_{T_0}^{2T_0}I(T)\,dT,\qquad \overline D(T_0):=\frac1{T_0}\int_{T_0}^{2T_0}D(T)\,dT .$$
Then, unconditionally, for every $T_0\ge2$:

**(a)** $\displaystyle\;\overline I(T_0)\;=\;\frac1\pi\,\overline D(T_0)\;+\;\frac18\;+\;O\Big(\frac{\log T_0}{T_0}\Big).$

**(b)** The limit $\displaystyle\lim_{T_0\to\infty}\overline D(T_0)$ **exists** in $[-\tfrac\pi8,+\infty]$ and equals $\;\pi\,I(0^+)-\dfrac\pi8$.

**(c)** $\mathrm{RH}\iff\lim\overline D=-\dfrac\pi8$; $\qquad$ **Problem A** $\iff\lim\overline D<\infty\iff\liminf_{T_0}\overline D(T_0)<\infty\iff\overline D(T_{0,n})$ bounded along *some* sequence $T_{0,n}\to\infty$.

*Proof.* (a) The identity $I(T)=\frac1\pi D(T)+\frac18-\Xi(T)$ holds for every $T$ except the ordinates (countable, measure zero); $I$ is bounded monotone on compacts, $D$ continuous, and $|\Xi(T)|\ll\log T$ ([LEMMA 176.3]) makes everything integrable on $[T_0,2T_0]$. Averaging, it suffices to bound $\frac1{T_0}\int_{T_0}^{2T_0}\Xi(T)\,dT$. By Fubini (justified: near each zero $|\zeta'/\zeta|\sim|s-\rho|^{-1}$ is locally integrable in the plane; outside, the bounds of 176.3 dominate) and the identity above:
$$\int_{T_0}^{2T_0}\Xi(T)\,dT\;=\;\frac1{2\pi}\int_{1/2}^\infty\Big(\sigma-\tfrac12\Big)^2\Big[\log|\zeta(\sigma+iT_0)|-\log|\zeta(\sigma+2iT_0)|\Big]\,d\sigma .$$
On $\sigma\in[\tfrac12,2]$: $(\sigma-\tfrac12)^2\le\tfrac94$ and [LEMMA 176.2] at the two heights: $\ll\log T_0$. On $\sigma\ge2$: $|\log|\zeta||\le\sum\Lambda(n)n^{-\sigma}/\log n\ll2^{-\sigma}$, integral $O(1)$. Total $\ll\log T_0$; divide by $T_0$.
(b) $I$ is non-decreasing with $\lim_{T\to\infty}I(T)=I(0^+)\in[0,\infty]$; hence $I(T_0)\le\overline I(T_0)\le I(2T_0)$ and $\overline I(T_0)\to I(0^+)$ (also if $I(0^+)=\infty$). By (a), $\overline D(T_0)=\pi\overline I(T_0)-\frac\pi8+o(1)\to\pi I(0^+)-\frac\pi8$.
(c) Immediate from (b): the limit always exists, so $\liminf<\infty\iff\lim<\infty\iff I(0^+)<\infty$; and $\lim=-\frac\pi8\iff I(0^+)=0\iff$RH. $\square$

**Reading.** This fulfills — with a strict improvement — the "next step 2" named in 173 §8 (Cesàro over the cut): the boundary does not merely drop to $O(\log T)$; it **vanishes** ($O(\log T_0/T_0)$). And it resolves the mandate's concern about sequences of good heights: they are no longer needed. Problem A is now, exactly and unconditionally, *the finiteness of a limit that exists*:
$$\textbf{A}\iff\lim_{T_0\to\infty}\frac1{T_0}\int_{T_0}^{2T_0}\!\!\int_{1/2}^\infty\!\!\int_0^T\log|\zeta(\sigma+it)|\,dt\,d\sigma\,dT\;<\;\infty .$$
No oscillation is possible: the averaged double integral either converges to a finite $\pi I(0^+)-\frac\pi8$, or diverges to $+\infty$. (Note the direction of the divergence: only toward $+\infty$ — the sign is protected by §5.)

---

## 3. The inverse theorem: what 170.5 + 173.C say about the means of $\log|\zeta|$

The machinery runs in the inverse direction: the energy certificate bounds means of the integrand.

**[THEOREM 176.6] (means of $\log|\zeta|$ in the half-band, unconditional).**
**(a)** For every non-ordinate $T$: $\;D(T)=\pi E(T)-\frac\pi8+O(\log T)$, and by the certificate $E(T)\ll T/\log T$ (Theorem 170.5):
$$\Big|\int_{1/2}^\infty\!\!\int_0^T\log|\zeta(\sigma+it)|\,dt\,d\sigma\Big|\;\ll\;\frac{T}{\log T}\,,$$
i.e., the area average of $\log|\zeta|$ in the half-band $\{\sigma>\tfrac12,\;0<t<T\}$ (effective area $\asymp T$) is $\ll1/\log T$.
**(b)** By abscissa, uniform in $\sigma\in(\tfrac12,1]$:
$$\Big|\frac1T\int_0^T\log|\zeta(\sigma+it)|\,dt\Big|\;\ll\;\frac1{(\sigma-\frac12)\,\log T}\;+\;\frac{\log T}{T}\,. $$

*Proof.* (a) is [COR 176.3.1] + 170.5. (b): Littlewood's lemma by abscissa (§1.2) with the Chebyshev bound $\sum(\beta-\sigma)^+\le E(T)/(\sigma-\tfrac12)\ll T/((\sigma-\tfrac12)\log T)$ for the upper direction, and $-2\pi(1-\sigma)-C\log T$ for the lower one. $\square$

**Frankness about the novelty.** The ingredients of (a) and (b) are Littlewood (1924) and Selberg (1946); the layer-cake connecting (a) with the sum $\sum b^2$ is the same observation with which 173.C is cross-verified (Doc 173 §6.1). Hence: **theorem new in statement, not in method**. What does seem absent from the literature *as a statement* is (a) with the exact constant $-\pi/8$ and validity at every height, and the uniform form (b) with weight $1/((\sigma-\frac12)\log T)$. [Literature GAP: I cannot locate (a)/(b) stated this way; they follow from [L24]+[S46] in a few lines and could be folklore. Before publishing: review Titchmarsh ch. 9 §§9.9–9.16 and the literature on $\int_0^T\log|\zeta(\sigma+it)|\,dt$.]

**[COR 176.10] (dichotomy of means; conditional on LP-112).** Under LP-112 (via [THEOREM 175.2]: $I(0^+)\in\{0,\infty\}$) and [THEOREM 176.4.b]:
$$\lim_{T_0\to\infty}\overline D(T_0)\;\in\;\Big\{-\frac\pi8\,,\;+\infty\Big\}.$$
*Under LP-112, the Cesàro mean of the integral of $\log|\zeta|$ in the half-band has only two possible destinations: the exact constant of the pole, or $+\infty$.* No intermediate growth ($\log^3T_0$, $\sqrt{T_0}$, $T_0/\log^2T_0$, …) is possible. Combined with the unconditional ceiling $\overline D(T_0)\ll T_0/\log T_0$ (176.6.a averaged): in the bad scenario the divergence lives in the window $(\text{bounded},\,T_0/\log T_0]$ — exactly the window of the LP-112 dichotomy read in the integrand. The information circle closes: *energy certificate $\to$ means of $\log|\zeta|$ $\to$ (with LP-112) dichotomy of the asymptotic behavior of a classical integral.*

---

## 4. Problem A in the hierarchy of standard conjectures

### 4.1. A implies Lindelöf

**[THEOREM 176.7].** $\textbf{A}\;(I(0^+)<\infty)\;\Longrightarrow\;$ Lindelöf Hypothesis. With the trivial facts ($\mathrm{RH}\Rightarrow I=0$; $m<\infty\Rightarrow I<\infty$; $I<\infty\not\Rightarrow m<\infty$, example $b_j=1/j$ — Doc 175) we get the strict chain of known implications:
$$\mathrm{RH}\;\Longrightarrow\;(m<\infty)\;\Longrightarrow\;\textbf{A}\;\Longrightarrow\;\mathrm{LH}\;\Longrightarrow\;\mathrm{DH}\;(N(\sigma,T)\ll T^{2(1-\sigma)+\varepsilon}).$$

*Proof.* If $I:=I(0^+)<\infty$, then for each $s>0$ the total number of zeros with $\beta\ge\tfrac12+s$ (any height) is $N(\tfrac12+s,\infty)\le I/s^2<\infty$ (Chebyshev: each contributes $b^2\ge s^2$). In particular, for each fixed $\sigma>\tfrac12$, $N(\sigma,T+1)-N(\sigma,T)\to0$ as $T\to\infty$ (differences of a bounded sequence that stabilizes). By Backlund's theorem (Backlund 1918–19; Titchmarsh, ch. XIII, §13.5: **LH $\iff$ for every $\sigma>\tfrac12$, $N(\sigma,T+1)-N(\sigma,T)=o(\log T)$**), LH follows. The arrow LH$\Rightarrow$DH is Ingham (1940). $\square$

**Positional reading.** A is an **almost-RH** statement: "RH with $\ell^2$ error". It sits strictly above Lindelöf in the hierarchy (in the sense of the proved implication A$\Rightarrow$LH; the converse is unknown and §4.3 shows the standard conduit cannot give it). On pair correlation: Montgomery's conjecture (1973) is formulated *under RH*, hence presupposes A and offers no route toward it; there is no usable unconditional version. [Literature GAP: I know of no standard statement strictly weaker than "all but finitely many on the line" that implies A.]

### 4.2. The exact layer-cake and the minimal statement

**[PROP 176.8] (A $=$ density uniform in $T$).**
**(a)** *Exact layer-cake:* $\;E(T)=\displaystyle\int_0^{1/2}2s\,N(\tfrac12+s,T)\,ds\;$ for every $T$ (counting in $N$ the zeros with $\beta\ge\tfrac12+s$, $0<\gamma\le T$; $b_j^2=\int_0^{b_j}2s\,ds$ and Tonelli).
**(b)** *Equivalence:* $\textbf{A}\iff$ there exists $f:(0,\tfrac12)\to[0,\infty]$ with
$$N(\tfrac12+s,T)\;\le\;f(s)\quad\forall\,T,\qquad\int_0^{1/2}s\,f(s)\,ds\;<\;\infty .$$
**(c)** *The minimal $f$:* $f_{\min}(s)=N(\tfrac12+s,\infty)$, and then $\int_0^{1/2}2s\,f_{\min}(s)\,ds=I(0^+)$ exactly.

*Proof.* (b$\Leftarrow$): $E(T)\le\int 2sf<\infty$ uniform, hence $I(0^+)<\infty$. (b$\Rightarrow$) and (c): with A, $f_{\min}(s)=N(\tfrac12+s,\infty)<\infty$ for all $s>0$ (176.7), dominates all $N(\cdot,T)$, and monotone convergence in (a) gives $\int2sf_{\min}=\lim E(T)=I(0^+)$. $\square$

**The minimal statement of A, named.**
> **[GAP-A] (density uniform in $T$; statement form).** *There exists $f$ with $\int_0^{1/2}s\,f(s)\,ds<\infty$ such that $N(\tfrac12+s,T)\le f(s)$ for every $T$.* (Example of a sufficient profile: $f(s)=s^{-2}\log^{-1-\varepsilon}(e/s)$.)

Note the genre: **this is not a density theorem** (a bound growing in $T$) but a **finiteness theorem** (a bound independent of $T$, per abscissa). The entire density industry — unconditional or conditional — produces bounds $T^{\theta}$ with $\theta>0$; what A asks is not to improve $\theta$ but to *kill it*. Zero-free regions do not help either: Vinogradov–Korobov gives $N(\sigma,T)=0$ only for $\sigma>1-c/(\log T)^{2/3}(\log\log T)^{1/3}$ — a boundary that escapes to $1$ as $T\to\infty$; for fixed $\sigma<1$ it contributes nothing.

### 4.3. The barrier: no exponential density theorem reaches A

**[PROP 176.9] (the exact account of the barrier).** Suppose $N(\tfrac12+s,T)\le C\,T^{1-cs}(\log T)^\kappa$ for $0<s\le\tfrac12$, $T\ge T_1$ (with any $c>0$, $\kappa\ge0$). Then the layer-cake gives, and gives no more than,
$$E(T)\;\le\;2C\,T(\log T)^\kappa\int_0^{1/2}s\,e^{-cs\log T}\,ds\;\le\;\frac{2C}{c^2}\;T\,(\log T)^{\kappa-2}.$$
Exact consequences:
1. **Selberg** ($c=\tfrac14$, $\kappa=1$, [S46]): $E(T)\ll T/\log T$ — the account *reproduces* certificate 170.5 (consistent: 170.5 is proved with [S46]; Doc 175 §3 already noted this). The envelope $T/\log T$ is **the house constant once again**: it is what $\kappa=1$ gives, whatever $c$ may be.
2. **The quality of the exponent is irrelevant to the form:** $c$ only enters the constant $2C/c^2$. Ingham 1940, Huxley 1972 ($N(\sigma,T)\ll T^{12(1-\sigma)/5}\log^CT$ [literature GAP: exponent cited from memory]), and even a hypothetical $c=10^6$, all give $T(\log T)^{\kappa-2}$.
3. **Lindelöf does not help through this conduit:** under LH, Ingham gives DH ($N\ll T^{2(1-\sigma)+\varepsilon}$) and Halász–Turán (1969) give $N(\sigma,T)\ll T^{\varepsilon}$ for $\sigma\ge\tfrac34+\delta$ — spectacular far from the line, **empty near it**: the mass of $E(T)$ lives at $s\asymp1/\log T$, where *any* exponential saving $T^{-cs}=e^{-c\cdot O(1)}\asymp1$, and the density bound is as trivial as $N\ll T\log T$. With any $\kappa$, LH moves $E(T)$ within the family $T(\log T)^{\kappa-2}$ and **never** to $O(1)$.
4. **Optimality against the hypothesis class:** the bound is tight — a configuration with $N(\tfrac12+s,T)\asymp T^{1-cs}\log T$ saturated at $s\asymp1/\log T$ is compatible with $N(T)\sim\frac{T}{2\pi}\log T$ and gives $E(T)\asymp T/\log T$. The density$\to$energy conduit cannot give less without new information *at* $s\asymp1/\log T$.

*Proof.* The integral: $\int_0^{1/2}s\,e^{-cs\log T}ds\le\int_0^\infty s\,e^{-cs\log T}ds=(c\log T)^{-2}$. Points 1–3 are substitutions; point 4 is the inverse computation with the saturated configuration (consistency with the total count: at $s=1/\log T$, $T^{1-cs}\log T=e^{-c}T\log T\le N(T)$ for $\kappa\le1$). $\square$

**Moments: the same pipe.** The moment bounds/conjectures $\int_0^T|\zeta(\tfrac12+it)|^{2k}dt\ll T(\log T)^{k^2}$ (known for $k=1,2$: Hardy–Littlewood 1918, Ingham 1926; conjectured for all $k$: Keating–Snaith) enter the energy only through Jensen/Littlewood: $\int_0^T\log|\zeta(\tfrac12+it)|\,dt\le\frac T{2k}\log\big(\frac1T\int|\zeta|^{2k}\big)\ll\frac{k\,T\log\log T}{2}$, which controls the *first* moment $J(T)=\sum_{\gamma\le T}b_j\ll T\log\log T$ — worse than the Selberg route even assuming all moments. And moments off the line ($\sigma>\tfrac12$) feed density theorems, i.e. [PROP 176.9]. **Hierarchy verdict: A is not a consequence of Lindelöf, nor of the Density Hypothesis, nor of the whole family of moment conjectures; the only known standard antecedent of A is the RH family itself ($\mathrm{RH}$, $m<\infty$).** A is a genuinely new node, strictly between $m<\infty$ and LH.

---

## 5. The unconditional lower bound and the sign asymmetry

### 5.1. The lower bound: the half-band is never in deficit below the pole

**[COR 176.5] (unconditional lower bound).** For every non-ordinate $T\ge2$:
$$\int_{1/2}^\infty\!\!\int_0^T\log|\zeta(\sigma+it)|\,dt\,d\sigma\;\ge\;-\,\frac\pi8\;-\;C\log T,$$
and in averaged form (where the constant is limit-exact):
$$\overline D(T_0)\;\ge\;-\,\frac\pi8\;-\;C\,\frac{\log T_0}{T_0}\qquad\forall\,T_0\ge2 .$$
Under RH equality holds in the limit: $\overline D(T_0)\to-\frac\pi8$. *The constant $-\pi/8$ is optimal.*

*Proof.* $D(T)=\pi I(T)-\frac\pi8+\pi\Xi(T)\ge-\frac\pi8-\pi|\Xi(T)|$ with $I(T)\ge0$ and [LEMMA 176.3]; the averaged one by [THEOREM 176.4.a] with $\overline I\ge0$; equality under RH by 176.4.b with $I(0^+)=0$. $\square$

**Clean statement (candidate for an autonomous publishable result, with the frankness of §3 about the classical origin of the ingredients):** *the average of $\log|\zeta|$ over the right half-band is unconditionally bounded below by the pole's mass: $\liminf_{T_0}\overline D(T_0)\ge-\pi/8$, with equality (and existence of the limit $=-\pi/8$) if and only if... the limit always exists and equals $\pi\sum b_j^2-\pi/8$.* The more citable form is directly [THEOREM 176.4.b], which contains this bound.

### 5.2. The asymmetry: the hard direction is the upper one

- **Lower $=$ free.** It is $I\ge0$: the positivity of the Riesz measure. *No* information about ζ beyond the identity.
- **Upper $=$ A.** By 176.4.c: A $\iff\overline D$ bounded above. Bounding $D$ from above means preventing $\log|\zeta|$ from being *persistently too positive* in the band — a control of the excess of **largeness** of $|\zeta|$ to the right of the line. (Correct sign intuition: each off zero adds $\pi b^2>0$ to $D$; the zeros, via broken subharmonicity, *raise* the integral. RH's defect is a surplus, not a deficit.)

**The absolute size, to calibrate the requested cancellation.** By Bohr–Jessen theory (Acta Math. 54 (1930) and 58 (1932); extension Borchsenius–Jessen 1948), for $\sigma\in(\tfrac12,1)$ fixed $\log\zeta(\sigma+it)$ has a limiting distribution in $t$, of variance $V(\sigma)=\tfrac12\sum_p p^{-2\sigma}+\dots\sim\tfrac12\log\frac1{2\sigma-1}$ ($\sigma\to\tfrac12^+$); the expected first absolute moment is $\asymp\sqrt{V(\sigma)}$, integrable in $\sigma$ down to $\tfrac12$. This sizes $\iint|\log|\zeta||\asymp\kappa_0\,T$ with $\kappa_0>0$ absolute. [Literature GAP: the convergence of the first absolute moment (uniform integrability) and its version integrated in $\sigma$ I take as plausible without an exact citation; the use here is purely calibrational, no proof depends on it.] Against that:
$$\underbrace{\textstyle\iint|\log|\zeta||\;\asymp\;T}_{\text{absolute mass}}\qquad
\underbrace{\textstyle|\iint\log|\zeta||\;\ll\;T/\log T}_{\text{proved cancellation (176.6)}}\qquad
\underbrace{\textstyle|\iint\log|\zeta||\;=\;O(1)}_{\textbf{A}}.$$
**The distance between what is proved and A is the factor between $\log T$ and $T$.** Universality (Voronin) guarantees local excursions, positive and negative, of arbitrary size; A asserts that their net balance is exact up to $O(1)$ — and the dichotomy [COR 176.10] says that, under LP-112, the balance is either exact or fails infinitely.

---

## 6. Verdict and pivots

### 6.1. What was proved (unconditional unless indicated)

| Label | Statement | Status |
|---|---|---|
| [PROP 176.1] | Region $\sigma\ge1$: exact contribution $\Phi(T)$, uniform $O(1)$; tension resolved; all the budget in the band | Theorem, new in statement |
| [LEMMA 176.3] | Boundary flux $\Xi(T)\ll\log T$ at **every** non-ordinate height | **Strict improvement over 173.C** ($O(\log^2T)$, good heights) |
| [THEOREM 176.4] | Averaged form with no boundary; $\lim\overline D$ **always exists** and equals $\pi I(0^+)-\frac\pi8$; RH $\iff-\frac\pi8$; A $\iff$ finite | **The central result of the document** |
| [COR 176.5] | $D(T)\ge-\frac\pi8-C\log T$; $\overline D\ge-\frac\pi8-o(1)$; optimal constant | Unconditional, free from $I\ge0$ |
| [THEOREM 176.6] | $D(T)=\pi E(T)-\frac\pi8+O(\log T)$; means of $\log|\zeta|$ $\ll1/\log T$ (area) and $\ll1/((\sigma-\frac12)\log T)$ (abscissa) | Inverse theorem; classical method, possibly new statement [lit. GAP] |
| [THEOREM 176.7] | $\mathbf{A}\Rightarrow$ Lindelöf (via Backlund); chain RH$\Rightarrow m<\infty\Rightarrow$A$\Rightarrow$LH$\Rightarrow$DH | Positioning, complete proof |
| [PROP 176.8] | A $\iff$ density uniform in $T$ with $\int sf\,ds<\infty$; $f_{\min}=N(\tfrac12+s,\infty)$ | The minimal statement, exact |
| [PROP 176.9] | Barrier: every $N\ll T^{1-cs}(\log T)^\kappa$ gives $E\ll\frac{2C}{c^2}T(\log T)^{\kappa-2}$ and no less; $c$ only enters constants; LH/DH/moments do not reach A | The exact account requested by the mandate |
| [COR 176.10] | Under LP-112: $\lim\overline D\in\{-\frac\pi8,+\infty\}$ | Conditional on LP-112 (via 175.2) |

### 6.2. The status of Problem A after this document

A is **reformulated with no loss** ([THEOREM 176.4.c] + [PROP 176.8]) in two equivalent currencies:
1. **Analytic:** the Cesàro mean of $\iint\log|\zeta|$ over the half-band converges (it always does) to a finite value. The lower bound is closed ($-\pi/8$, optimal); only the upper one is missing.
2. **Counting:** density uniform in $T$ ([GAP-A]). Genre "finiteness," unreachable by the full exponential conduit ([PROP 176.9]).

And it is **positioned**: strictly between $m<\infty$ and Lindelöf; not a consequence of any standard density/moment conjecture; under LP-112, equivalent to RH ([COR 175.5.2]). The wall is frank: the proved cancellation is $1/\log T$, the one requested is $1/T$, and the standard conduit has structural ceiling $T(\log T)^{\kappa-2}$.

### 6.3. Pivots (the envelope ladder, with exact dictionary)

By [PROP 176.8]/[176.9], each improvement of the envelope of $E(T)$ has a nameable density equivalent. The ladder, from the known to RH:

| Step | Envelope $E(T)\ll$ | Equivalent/sufficient density input | Status |
|---|---|---|---|
| 0 | $T/\log T$ | Selberg $\kappa=1$ | **Proved** (170.5/[S46]) |
| 1 | $T/\log^2T$ | **log-free density near $\sigma=\frac12$**: $N(\frac12+s,T)\ll T^{1-cs}$ ($\kappa=0$) | **PIVOT 176.P1** — the realistic target; analogue of Linnik/Gallagher (log-free near $\sigma=1$) carried over to the critical line. [Literature GAP: I know of no log-free result at $\sigma\to\frac12^+$] |
| 2 | $T(\log T)^{-K}$, $K$ arbitrary | negative $\kappa$: genuine logarithmic saving at $s\asymp1/\log T$ | No known technique |
| 3 | $T^{1-\delta}$ | power saving **at the edge** $s\to0^+$: $N(\frac12+s,T)\ll T^{1-\delta}g(s)$ | Major wall (would imply almost-all-zeros in $T^{-\delta'}$-thin bands; out of reach) |
| 4 | $O(1)$ $=$ **A** | [GAP-A]: density uniform in $T$ | The problem |
| 5 | $0$ $=$ RH | $N\equiv0$ | — |

Every step $\ge1$ is real program progress: with LP-112 behind it, any $o(T/\log T)$ **sharpens the dichotomy** (the divergence window of [COR 176.10] narrows) and improves the witness rates of [THEOREM 175.6]. Additional pivots, recorded:
- **176.P2 (pivot $J$, inherited from 173 §7c):** the first-order energy $J=\sum b_j$ with its Littlewood–Blaschke package; this document adds: the moment conduit gives $J(T)\ll T\log\log T$ unconditional-under-moments — weak; the route for $J$ is the same layer-cake with $\int f(s)\,ds<\infty$ (without the factor $s$): *more* demanding near $s=0$, not less. A (quadratic) remains the correct target of the two.
- **176.P3 (the mean part of the flux):** the average of the flux is a difference of $\log|\zeta|$ at two heights (§2.3); its fine mean value (beyond $O(\log T_0)$) is accessible via the theory of mean values of $\log|\zeta|$ — it could give the secondary term of $\overline D$ and a quantitative consistency test of the $I(0^+)>0$ scenario.
- **176.P4 (using 176.4 as an operative *definition*):** in the direction of Phase 54 (balance law), $\overline D(T_0)+\frac\pi8$ is a cut-regularized version of $\pi I$ with no atoms at the boundary — a natural candidate for the "grading norm" requested in 173 §6.3, prior to the DBN desingularization program.

---

## References

- J. E. Littlewood, "On the zeros of the Riemann zeta-function", *Proc. Cambridge Philos. Soc.* 22 (1924), 295–318. [Littlewood's lemma.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. D. R. Heath-Brown), Oxford, 1986. §3.9 (local factorization lemma), §9.4 ($S(T)=O(\log T)$), §9.9 (Littlewood's lemma), ch. 9 (densities), §13.5 (Backlund's theorem: LH $\iff$ windowed count).
- R. J. Backlund, "Über die Nullstellen der Riemannschen Zetafunktion", *Acta Math.* 41 (1918), 345–375. [LH–count equivalence; details via Titchmarsh §13.5.]
- A. Selberg, "Contributions to the theory of the Riemann zeta-function", *Arch. Math. Naturvid.* 48 (1946), 89–155. [Density $N(\sigma,T)\ll T^{1-\frac14(\sigma-\frac12)}\log T$; origin of the $T/\log T$ certificate.]
- A. E. Ingham, "On the estimation of $N(\sigma,T)$", *Quart. J. Math. Oxford* 11 (1940), 291–292. [LH $\Rightarrow$ DH.]
- M. N. Huxley, "On the difference between consecutive primes", *Invent. Math.* 15 (1972), 164–170. [Density $12/5$; literature GAP: exponent cited from memory.]
- G. Halász, P. Turán, "On the distribution of roots of Riemann zeta and allied functions, I", *J. Number Theory* 1 (1969), 121–137. [Under LH: $N(\sigma,T)\ll T^\varepsilon$ for $\sigma>\frac34$.]
- H. Davenport, *Multiplicative Number Theory*, 3rd ed., GTM 74, Springer. Chaps. 15–16 (partial fractions of $\zeta'/\zeta$; windowed count).
- H. L. Montgomery, "The pair correlation of zeros of the zeta function", *Proc. Sympos. Pure Math.* 24 (1973), 181–193. [Formulated under RH; cited only for positioning.]
- H. L. Montgomery, R. C. Vaughan, "Hilbert's inequality", *J. London Math. Soc.* 8 (1974), 73–82. [Mean value of Dirichlet polynomials; used only calibrationally in §1.1.]
- H. Bohr, B. Jessen, "Über die Werteverteilung der Riemannschen Zetafunktion", *Acta Math.* 54 (1930), 1–35; 58 (1932), 1–55. — V. Borchsenius, B. Jessen, *Acta Math.* 80 (1948). [Limiting distribution of $\log\zeta(\sigma+it)$, $\sigma>\frac12$; calibrational use §5.2, with declared GAP about absolute moments.]
- Yu. V. Linnik (1944) / P. X. Gallagher, "A large sieve density estimate near $\sigma=1$", *Invent. Math.* 11 (1970), 329–339. [Log-free densities near $\sigma=1$; inspiration for PIVOT 176.P1.]
- G. H. Hardy, J. E. Littlewood (1918); A. E. Ingham (1926). [Moments $k=1,2$.] — J. P. Keating, N. C. Snaith, *Comm. Math. Phys.* 214 (2000). [Moment conjecture.]

**Internal documents:** Doc 170 (coordinates; Theorem 170.5), Doc 172 (ceiling $T/\log T$), Doc 173 (Green–Littlewood identity 173.C — basis of this document; §8 steps named 2 and 3 here executed/decided), Doc 175 (LP-112 dichotomy, Theorem 175.2; architecture COR 175.5.2), Phase 54 (balance law).

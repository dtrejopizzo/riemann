# Document 171 — Adversarial audit of Doc 170 (second-order visibility)

**Program:** Riemann Hypothesis — Phase 54 (index dynamics)
**Mandate:** destroy the theorems of Doc 170. Protocol: closed re-derivation of 170.5 (Selberg density verified against the literature + layer-cake + weighted), classification of 170.3 (trivial/fine/false), the full signal/noise account of the marginal scale, verification of 170.8, dictionary with D152.
**Method:** no numerics; by-hand re-derivation and literature verification (Selberg 1946 verified via explicit secondary literature; Ω-results for S(t) cited from memory with declared confidence). Sources read in the original: Doc 170 in full, Doc 152 §2.2 (152.E, Theorem 152.2, full proof), Doc 141 (Lemmas 141.M1/M4/M5, 141.B0, 141.B, Cor. 141.B2, Obs. 3.1, GAP-141.G1 in its original statement).

---

## 0. Verdict per piece

| piece | statement | verdict |
|---|---|---|
| (a) [THEOREM 170.5] + [COR 170.6] | $E(T)\ll T/\log T$; Lehmer density $O(1)$; $\sum b_j^2/(\gamma_j(\log\log\gamma_j)^{1+\varepsilon})<\infty$ | **HOLDS.** Selberg density verified against the literature (exact form and constant); layer-cake re-derived, constant $32C$ confirmed; weighted version re-derived, the exponent $1+\varepsilon$ is exactly what is needed and what is claimed. A minor literature imprecision (Jutila 1983 improves the ¼ constant — in favor, not against). |
| (b) [THEOREM 170.3] | $\int h''=0$; average over $\tau$ zero to every order | **(1) trivial-correct; (2) correct but trivial (full integral); the bold-faced corollary about slowly varying weights is FALSE as a literal statement** (small sensitivity, not identically zero) — repairable, the strategic mechanism survives via the reduction to a single window that the proof itself uses. |
| (c) [PROP 170.2] | D152 impurity spectrum = second-order window | **HOLDS.** Term-by-term verification against the original Doc 152 (test, bracket, rate, sign, bias constant): everything matches. The signs in 170 itself are correct. |
| (d) [THEOREM 170.8] | relative no-go: $I=\infty$ with $\varepsilon$-indistinguishable data | **HOLDS as a relative no-go**, with the same (declared) caveats as 141.B2; construction verified (divergence, envelope, vertical statistics proved — not merely claimed); one decay exponent cited with harmless sloppiness. |
| (e) marginal scale $\Theta(c^2)$ | order-one signal; "the only blockage is GAP-141.G1" | **The SIGNAL count is correct ($\Theta(c^2)$, verified). The §3.4 signal/noise picture (TWO blockages) is correct. But the §6 [WISH] is BROKEN as a statement: it identifies GAP-141.G1 with "evaluating $\mathfrak D(h_\tau)$" (primes+archimedean only) and declares it the ONLY blockage — this omits $F(h_\tau)$ (the sea), which per INDIVIDUAL window admits no $o(1)$ bound, neither unconditionally nor under RH ($S(t)$ unbounded). Main finding of this audit (H1).** |

New errata found: E-171.1, E-171.2, E-171.3 (§6 of this document). No [THEOREM]/[PROP]-labeled result of 170 dies; what dies is the final strategic sentence (the WISH as written) and one bold-faced sentence of 170.3.

---

## 1. [THEOREM 170.5] — full re-derivation

### 1.1. Selberg's density: literature verification

The actual statement of Selberg 1946 (*Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. 48) is, as recorded by literature that makes it explicit (Simonič, *Explicit zero density estimate for the Riemann zeta-function near the critical line*, J. Math. Anal. Appl. 491 (2020); arXiv:1910.08274):
$$N(\sigma,T)\;\ll\;T^{1-\frac14(\sigma-\frac12)}\log T\qquad\text{uniformly on }\tfrac12\le\sigma\le1,$$
with $N(\sigma,T)=\#\{\rho:\beta\ge\sigma,\ 0<\gamma\le T\}$ counted with multiplicity. **This is exactly the form Doc 170 uses ($c=\tfrac14$, $B=1$), and the same one the program already cited in Doc 141 §2.1.** The document does NOT use a stronger form than the real one. The uniformity near $\sigma=\tfrac12$ (where the bound degenerates smoothly to the trivial $T\log T$) is part of the theorem and is what the layer-cake needs. Literature nuance: observation (a) of §4 ("Selberg is the best known near ½") is imprecise — Jutila (1983, *Zeros of the zeta-function near the critical line*, Studies in Pure Mathematics) improved the constant $\tfrac14$; this only IMPROVES the constant of 170.5 via the general form $(A,c,B)$, it does not touch the statement. [Minor erratum E-171.3.]

### 1.2. The layer-cake, redone

Identity: for $b_j\in(0,\tfrac12)$, $b_j^2=\int_0^{1/2}2b\,\mathbf 1_{\{b<b_j\}}db$ — exact. And $\#\{j:b_j>b,\ \gamma_j\le T\}=N(\tfrac12+b,T)$: with one representative per quadruple in $\{\beta>\tfrac12,\gamma>0\}$, $N(\sigma,T)$ with $\sigma>\tfrac12$ counts exactly one per quadruple (the one with $\beta=\tfrac12+b_j\ge\sigma$), with multiplicity (repeated $j$'s). The $\ge$ vs $>$ discrepancy is a zero-measure boundary in $db$. **Multiplicity and sides: consistent** — the other half of the quadruple ($\beta<\tfrac12$) is counted neither in $E$ nor in $N(\sigma,T)$ with $\sigma>\tfrac12$; if $E$ over all zeros were wanted, factor 2 absorbed into $\ll$. Then
$$E(T)=\int_0^{1/2}2b\,N(\tfrac12+b,T)\,db\le 2CT\log T\int_0^{1/2}b\,e^{-\frac{b}{4}\log T}db\le 2CT\log T\cdot\frac{16}{\log^2T}\int_0^\infty s e^{-s}ds=\frac{32CT}{\log T}.$$
Verified step by step: $T^{1-b/4}=Te^{-(b/4)\log T}$ ✓; substitution $s=b\log T/4$, $b\,db=(16/\log^2T)s\,ds$ ✓; $\int_0^\infty se^{-s}=1$ ✓. Constant $32C$ ✓. Separation requested by the protocol: for $b\le1/\log T$ the integrand is $\le 2b\cdot N(T)\sim 2b\,T\log T$, contribution $\le T\log T\cdot(1/\log T)^2=T/\log T$ ✓; for $b>1/\log T$ the exponential tail $\int_{1/\log T}^\infty be^{-b\log T/4}db\asymp1/\log^2T$ again gives $T/\log T$ ✓ — **converges to $O(T/\log T)$, not to $T\cdot$log-power**. The general form: $E\le 2AT\log^BT/(c\log T)^{-2}\cdot1=(2A/c^2)T\log^{B-2}T$ ✓ exactly as stated. Ingham at $\sigma=\tfrac12+b$: exponent $3(\tfrac12-b)/(\tfrac32-b)=1-\tfrac{2b}{3/2-b}$, i.e. $c\approx\tfrac43$ near ½, $B=5$ → $T\log^3T$ ✓ worse, as the document says.

**[THEOREM 170.5] CERTIFIED.**

### 1.3. The corollaries, re-derived

**170.6.1 (Lehmer density).** Dyadic blocks $T_k=2^k$: $\sum_{\gamma\in(T_{k-1},T_k]}(b\log\gamma)^2\le\log^2T_k\,[E(T_k)]\ll T_k\log T_k$; $\sum_{k\le K}T_k\log T_k\asymp T_K\log T_K\asymp T\log T\asymp N(T)$ ✓.

**170.6.2 (weighted).** Partial summation against $E(t)\ll t/\log t$:
$$\sum_{\gamma_j\le T}\frac{b_j^2}{\gamma_j}=\frac{E(T)}{T}+\int_2^T\frac{E(t)}{t^2}dt\ll\frac1{\log T}+\int_2^T\frac{dt}{t\log t}=\log\log T+O(1)\ ✓.$$
With weight $u(\gamma)=(\log\log\gamma)^{1+\varepsilon}$: the relevant integral is $\int\frac{dt}{t\log t(\log\log t)^{1+\varepsilon}}$; substituting $v=\log\log t$ ($dv=dt/(t\log t)$) gives $\int v^{-1-\varepsilon}dv<\infty$ **if and only if the $\log\log$ exponent is $>1$**. The document claims exactly $1+\varepsilon$ with $\varepsilon>0$ — **the exponent is correct and the minimal possible one via this route** (with exponent 1 it diverges: the protocol's warning was pertinent and the document correctly avoids it). Boundary term $E(t)/(tu(t))\to0$ ✓. **[COR 170.6] CERTIFIED.** (Also verified the geometric reading (c): $N(T)\cdot(1/\log T)^2\asymp T/\log T$ ✓; and the ℓ¹ comparison: Littlewood gives $\sum(\beta-\tfrac12)^+\ll T\log\log T$ [T86 §9.9], whence only $E\ll T\log\log T$ — the density route is strictly better ✓.)

---

## 2. [THEOREM 170.3] — classification

**(1)** $\int_{\mathbb R}h''=[h']_{-\infty}^\infty=0$ with $h'\to0$ by Cauchy in the strip + decay ✓; "there is no non-constant concave $h\in\mathcal A$ on $\mathbb R$" ✓ (non-constant concave $\to-\infty$). **Trivial-correct.**

**(2)** The identity shown is for the **full integral** over $\tau\in\mathbb R$: $\int h(x\pm ib)dx=\int h\,dx$ by Cauchy's theorem on the rectangle (vertical sides $\to0$ by uniform decay, $b\le\tfrac12<\tfrac12+\varepsilon$ ✓); subtracting twice gives an exact $0$, to every order in $b$, resummation included. **Correct — and trivial in the protocol's sense: it is $(\int h)(1+1-2)=0$.** There are no boundary terms because there is no truncation.

**The fine point — where the statement overreaches:** the bold-faced sentence *"any statistic that is a $\tau$-average (with slowly varying weight) of translated windows has identically zero sensitivity to $I$"* is **FALSE as a literal statement**. For a non-constant weight $w$ (e.g. Gaussian of scale $T_0$, or smoothly truncated), the average is the evaluation of the composite test $h\star w$ — as the proof itself states — and the second-order footprint of the composite is $-b^2(h''\star w)(\gamma_j)\ne0$ in general: it is $O(b^2/T_0^2)$-small (the derivatives come from $w$), **small, not identically zero**; and with sharp truncation there are also boundary terms of the size of quadruples near the endpoints. Two more defects in the same paragraph: (i) $h\star w$ can fall outside $\mathcal A$ (a truncated $w$ degrades the decay from $-1-\delta$ to $-\delta$); (ii) "reduces to a single window (§3)" and "identically zero sensitivity" are distinct claims — the proof shows the first, the statement proclaims the second. **Final classification: (1) trivial; (2) correct-trivial for the full integral; the slowly-varying-weight corollary: false as written, true in the repaired form** "the average with a scale-$T_0$ weight has sensitivity $O(b^2/T_0^2)$ per quadruple, i.e. it reduces to a single window of resolution $1/T_0$, where §3 applies". The strategic conclusion (no linear accumulation of one-signed signal) **survives** in the repaired form. **Repair R-171.1 mandatory in the text if 170 is propagated.**

---

## 3. The marginal scale (e) — the full signal/noise account

### 3.1. The signal: verified

Document's convention: $h(r)=\int_{-L}^Lg(u)e^{iru}du$, I normalize $h(0)=\int g\asymp1$ (Fejér: $g\ge0$, $g\asymp1/L$ over the bulk of $[-L,L]$). Then $|h''(0)|=\int u^2g\asymp L^2$ ✓ ("$|h''|\asymp L^2h$ at the center"). Signal per quadruple at the center, sub-resolution: $|\Delta_j|\asymp b_j^2L^2=(b_jL)^2$ ✓. With $b=c/\log\gamma$ and $L=A\log\gamma$, $A\le2-\varepsilon$ (MV budget): signal $=(cA)^2=\Theta(c^2)$. **The power-of-log count is correct: no hidden log in the signal.** Off amplification $e^{bL}=e^{cA}=O(1)$ at this scale ✓ consistent.

### 3.2. The noise: the count the document does only halfway

By identity 170.1(iii), certification requires bounding $F(h_\tau)=\int h_\tau\,dS$ in addition to $\mathfrak D(h_\tau)$. Three levels:

1. **By individual window, unconditional:** $|F|=|\int h_\tau'(t)S(t)dt|\le\sup_{t\approx\tau}|S(t)|\cdot\mathrm{TV}(h)$. For Fejér $\mathrm{TV}(h)=O(1)$ (side lobes $\asymp k^{-2}$, summable); Backlund gives $|S|\le C\log\tau$. **Certifiable bound per window: $O(\log\gamma)$ — a factor $\log\gamma$ ABOVE the signal $\Theta(c^2)$.** At the level of an individual unconditional certificate the signal IS buried by a log.
2. **In variance (mean square over $\tau$), unconditional under $L\le(2-\varepsilon)\log\tau$:** $F$ = (prime sum via the explicit formula) + smooth; Montgomery–Vaughan, diagonal: $\frac1{T_0}\int_0^{T_0}|F|^2d\tau\asymp\sum_n\frac{\Lambda(n)^2}{n}g(\log n)^2\asymp\int_0^Lu\,g(u)^2du\asymp\frac1{L^2}\cdot L^2\asymp1$. **Typical fluctuation $\Theta(1)$ — the claim "the window contains $O(1)$ ordinates and fluctuates $\Theta(1)$" of §3.4 is correct in this L² sense, and is unconditional** (it does not require conditional Montgomery; what is conditional is the fine asymptotic/pair correlation, not the upper bound on variance in this support range). The protocol asked whether the variance is $\sim\log T$: not with a normalized smooth test ($g\asymp1/L$); it would be $\asymp\log$ with a sharp window of height 1 — the document uses the smooth one, the count is correct.
3. **By individual window, conditional:** not even under RH is there $o(1)$: $S(t)=\Omega_\pm\bigl((\log t/\log\log t)^{1/2}\bigr)$ (Montgomery 1977, under RH; unconditionally there are weaker Ω-results, Tsang — [high confidence, cited from memory: minor literature GAP on the exact unconditional exponent]). **There exist exceptional windows with $|F|\to\infty$: the per-individual-window bound with error $o(1)$ does NOT exist in any world.**

### 3.3. Consequence: where Doc 170's error lies

- **§3.4 and §0.3 are correct**: two blockages, (i) prime side per window (G1) and (ii) quadratic statistic of the sea at resolution. "Not buried by size" is true **in the typical/L² sense** (signal $\Theta(c^2)$ vs. typical fluctuation $\Theta(1)$ — same order, no deficit log), not per individual window (deficit of $\log\gamma$ against the only certifiable individual bound, level 1 above).
- **The §6 [WISH] is broken (FINDING H1):** it states that *"an unconditional evaluation of $\mathfrak D(h_\tau)$ per individual window with error $o(1)$ — this is GAP-141.G1 — is the ONLY blockage and crossing it would give window bounds on $\sum_{\gamma_j\approx\tau}(b_j\log\gamma_j)^2$"*. Two flaws:
  1. **Imprecise internal attribution:** the ORIGINAL GAP-141.G1 (Doc 141 §3.3) requires error $o((\delta L)^2)$ of "**archimedean + primes + on-line sea**" — it includes $F$. 170 trims it to "prime side"/"$\mathfrak D$" when citing it. $\mathfrak D$ and G1 are not the same: G1 is strictly stronger.
  2. **The WISH statement with $\mathfrak D$ alone is insufficient:** signal $=\mathfrak D-F$; with $\mathfrak D$ evaluated to $o(1)$ what remains is $|F|$, which per individual window is $O(\log\gamma)$ unconditionally and $\Omega(\sqrt{\log/\log\log})$ on exceptional windows even under RH (3.2.3). **Crossing the WISH as written would NOT give the promised window bounds.** Honest repair (R-171.2): either (a) rewrite the WISH with the original G1 (which already includes the sea — but then "the only blockage" is a tautology: G1 = the whole blockage by definition), or (b) downgrade the promise to **almost every window** (in density): $\mathfrak D$ with error $o(1)$ per window + sea variance $\Theta(1)$ (level 3.2.2, unconditional in this range!) would give bounds on $\sum(b_j\log\gamma_j)^2$ for 100% of windows in density — which is probably what the index dynamics needs. Option (b) is moreover MORE optimistic than the current text: blockage (ii) "conditional pair correlation" is unnecessary for upper bounds on almost-every-window, because the upper bound on the variance is unconditional (MV); what is conditional is only the asymptotic.
- **Additional omitted detail (minor):** inferring an energy bound per window requires control of the flanks — neighboring quadruples fall in the $h''>0$ zone and contribute with the opposite sign (the one-signedness is only in the core, as §2 itself explains). For upper bounds on the core's energy this adds a signed term from quadruples at a distance of a few resolutions; controllable by envelope 170.5 on average but not per individual window. This must appear in any repaired version of the WISH.

### 3.4. Verification of the numerical computations of §3 of 170

- **170.4a (saddle):** $\sum_n\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\approx\int_0^\infty e^{u/2-u^2/4T^2}du$: maximum at $u=T^2$, value $T^2/4$ ✓, Gaussian width $\Rightarrow$ total $=2\sqrt\pi\,Te^{T^2/4}(1+o(1))$. **170 writes $\sqrt\pi\,Te^{T^2/4}$: factor of 2 lost, and inconsistent with its own source (D152, proof of 152.2(c), which gives $2\sqrt\pi Te^{T^2/4}$, consistency check included). Erratum E-171.1, harmless** (only the exponent ¼ is load-bearing; the threshold $\omega=\tfrac14$ and the "only the pole" conclusion remain intact). The logic $e^{b^2T^2}<e^{T^2/4}$ for all $b<\tfrac12$ ✓.
- **170.4c (MV):** diagonal $\tfrac12\sum\Lambda(n)^2n^{-1}e^{-(\log n)^2/2T^2}\approx\int ue^{-u^2/2T^2}du\asymp T^2$ ✓. MV error term $\sum n|a_n|^2=\sum\Lambda(n)^2e^{-(\log n)^2/2T^2}\approx\int ue^{u-u^2/2T^2}du$: saddle at $u=T^2$, value $T^2/2$, width $T$ → $\asymp T^3e^{T^2/2}$, **not $T^2e^{T^2/2}$ as the document writes — erratum E-171.2, harmless** (under $T^2\le(2-\varepsilon)\log T_0$ it remains $\ll T^2T_0$). Excess from one quadruple: $\int T^2e^{2T^2(b^2-(\tau-\gamma)^2)}\cos^2 d\tau\asymp Te^{2b^2T^2}$ ✓; the threshold: $e^{2b^2T^2}\gtrsim TT_0$ with $T^2=(2-\varepsilon)\log T_0$ gives $b^2\ge\tfrac1{2(2-\varepsilon)}\to\tfrac14$ ✓. **The ¼ threshold in all three routes: verified.**

---

## 4. [THEOREM 170.8] — verification

**Construction:** $b_j=1/\sqrt{\log(j+2)}$: $\sum b_j^2=\sum1/\log(j+2)=\infty$ ✓ (comparison series with $\int dx/\log x$), $b_j\to0$ ✓.

**The mechanism (height, not width):** the bound used is exactly Lemma 141.B (verified in the original, proof by Taylor with remainder + integration by parts $N$ times): contribution of quadruple $j$ to datum $i$ $\le C_N(F_i)(b_jL_i)^2e^{b_jL_i}(1+\gamma_j)^{-N}$. With $i$ fixed, $b_j\le1$: $\le C_i'(1+\gamma_j)^{-N}\to0$ **without touching $b_j$** ✓ — the structural point (in 141.B2 indistinguishability was bought with $\delta_j\to0$ fast, incompatible with $I=\infty$; here with $\gamma_j\to\infty$, compatible) is correct and is genuinely the novelty. Harmless sloppiness: the $(1+\gamma_j)^{-2}$ of 170 presupposes $F_i$ of type $C_c^\infty$ (where 141.B gives any $N$); for general $h\in\mathcal A$ the guaranteed decay of $h''$ by Cauchy is $(1+\gamma)^{-1-\delta}$ — equally sufficient ($\to0$), the proof is unaffected. Version (1): finitely many conditions per step, budget $\varepsilon2^{-j}/M$, choose $\gamma_j$ large ✓. Version (2): head $I_0$ + tail absorbed by the metric ✓.

**Admissibility and density (the Doc 144 counterexample problem):** one quadruple per step with super-exponential $\gamma_j$ adds $O(\log\log T)$ zeros up to $T$ — RvM intact at the $O(1)$-per-window level; densities: one zero per block $\ll$ any bound ✓; envelope: $E(T)=\sum_{j\le J(T)}1/\log(j+2)\ll\log J(T)\ll\log\log\log T=o(T/\log T)$ ✓ (the document says $o(T/\log T)$ — correct with an absurd margin). **"Identical vertical statistics": PROVED, not merely claimed** — $Z$ and $Z^\flat$ share ordinates as multisets by construction, and Lemma 141.B0 (verified in the original: $N(t)$ does not reference $\beta$ within the band) converts that into an identity of all ordinate functionals. ✓

**Scope:** the theorem is a no-go **relative to the data class**, and the document declares it with the honesty of Obs. 3.1 of 141, including the real new restriction (the countable per-datum-uniform version is NOT recovered: the heads $j<i$ are not controllable with $b_j$ fixed by the divergence — declared ✓). What it does NOT cover (and does not claim to): configurations realizable as zeros of a function with an Euler product (global rigidity), and arithmetic at all supports (G1). **Same loopholes as 141.B2, correctly listed. CERTIFIED within its declared scope.**

---

## 5. Dictionary with D152 — term-by-term verification

Checked against the original (`phase-48-audit-and-purity/152-attack-purity-rigidity-the-two-purities-semi.md`, §2.2):

| item | D152 (original) | D170 | matches? |
|---|---|---|---|
| off coordinate | $t_\rho=\gamma-i\delta$, $\delta=\beta-\tfrac12\in(0,\tfrac12)$ | $\gamma_\rho=\gamma_j-ib_j$, $b_j=\beta_j-\tfrac12$ | ✓ ($b_j\equiv\delta_j$) |
| test | $h_{T,\tau}=e^{-T^2(t-\tau)^2}+e^{-T^2(t+\tau)^2}$, $g=\tfrac1{\sqrt\pi T}e^{-u^2/4T^2}\cos(\tau u)$ | $g=e^{-u^2/4T^2}\cos(\tau u)$, $h_\tau=\sqrt\pi T[\,\cdots]$ | ✓ ($h_\tau=\sqrt\pi T\,h_{T,\tau}$, transform re-derived: $\widehat{e^{-u^2/4T^2}}=2\sqrt\pi Te^{-T^2r^2}$, cosine halves ✓) |
| quadruple bracket | $\mathrm{Re}\,e^{-T^2(\gamma-\tau-i\delta)^2}=e^{T^2(\delta^2-(\gamma-\tau)^2)}\cos(2T^2(\gamma-\tau)\delta)$ (152, proof (iii)) | $2\sqrt\pi Te^{-T^2(\gamma-\tau)^2}[e^{T^2b^2}\cos(2T^2(\gamma-\tau)b)-1]$ | ✓ (re-derived: $(\gamma-\tau+ib)^2=(\gamma-\tau)^2-b^2+2ib(\gamma-\tau)$; identical) |
| exponential rate | $\omega(\tau)=\max(0,\max_{|\gamma_j-\tau|<\delta_j}(\delta_j^2-(\gamma_j-\tau)^2))$ [Thm 152.2(a)] | $\tfrac1{T^2}\log|\cdot|\to b_j^2-(\gamma_j-\tau)^2$ | ✓ (with the nuance that the full limit requires 152's Besicovitch non-cancellation lemma — which 152 proved; the 170 "reproduces exactly" is legitimate resting on 152, not autonomous) |
| bias sign | zeros enter with $-$ in (152.E); $S_T(\gamma_J)=-2\sqrt\pi m_JTe^{\delta_{\max}^2T^2}(1+o(1))$ [152.2(b)] | "zeros enter with $-$ sign: permanent negative bias $\sim-2\sqrt\pi m_JTe^{\delta^2T^2}$" | ✓ sign and constant |
| signal at center | — | $+2\sqrt\pi b^2T^3$ (zero side, $\tau=\gamma_j$) | ✓ re-derived: $2\sqrt\pi T(e^{T^2b^2}-1)\approx2\sqrt\pi b^2T^3$; and it matches $-b^2\partial_t^2[\sqrt\pi Te^{-T^2(t-\tau)^2}]_{t=\tau}=+2\sqrt\pi b^2T^3$ — the footprint $-b^2h''$ of 170.1(ii) with the sign RIGHT |
| ¼ jurisdiction | $S_T(0)=2\sqrt\pi Te^{T^2/4}$, $\omega\le\tfrac14$ [152.2(c), 152.4] | threshold $\omega=\tfrac14$ in all three routes | ✓ (except for the factor-2 of E-171.1, which lives only in 170 §3.1 and does not touch the exponent) |

**170's own signs:** verified from scratch. 170.1(i): the quadruple gives $h(\gamma\pm ib)+h(-\gamma\pm ib)=2[h(\gamma+ib)+h(\gamma-ib)]$ by parity, the projection gives $4h(\gamma)$; difference $=2\Delta_j$ with the outer factor 2 correctly counted ✓. 170.1(ii): $f(b)=2\,\mathrm{Re}\,h(\gamma+ib)$, $f''(0)=-2h''(\gamma)$ → $\Delta_j=-b^2h''(\gamma)+R$, $|R|\le\tfrac1{12}b^4\sup|h^{(4)}|$ (Taylor to order 4 with $f^{(4)}=2\mathrm{Re}\,h^{(4)}$: $2/24=1/12$ ✓). **Erratum E-170.1 (the 168 sign) is correctly fixed in 170; 170 introduces no new sign errors.** [PROP 170.2] CERTIFIED.

---

## 6. Errata and repairs

- **E-171.1 (170 §3.1(α)):** the trivial bound is $2\sqrt\pi\,Te^{T^2/4}(1+o(1))$, not $\sqrt\pi\,Te^{T^2/4}$ (saddle redone; matches D152). Harmless: only the exponent ¼ is load-bearing.
- **E-171.2 (170 §3.3):** the MV error term is $\sum n|a_n|^2\asymp T^3e^{T^2/2}$, not $T^2e^{T^2/2}$. Harmless under the support restriction.
- **E-171.3 (170 §4 Obs. (a)):** "Selberg is the best known near ½" — Jutila (1983) improved the ¼ constant; it only improves the constant of 170.5. Citation to be added.
- **R-171.1 (170 Theorem 170.3(2), bold-faced sentence):** replace "identically zero sensitivity" with "sensitivity $O(b^2/T_0^2)$ per quadruple for a scale-$T_0$ weight (reduction to the composite test $h\star w$, single window of resolution $1/T_0$)"; with constant weight (full integral) it is indeed exactly zero.
- **R-171.2 (170 §6 [WISH] — the mandatory repair):** the WISH as written (evaluate $\mathfrak D$ per individual window = G1 = only blockage) is insufficient and imprecisely attributed (§3.3 of this document). Proposed repaired form: *"an unconditional evaluation of $\mathfrak D(h_\tau)$ per window with error $o(1)$ (the prime-half of GAP-141.G1) would give, combined with the MV variance bound of the sea (unconditional for support $\le(2-\varepsilon)\log\gamma$), bounds on $\sum_{\gamma_j\approx\tau}(b_j\log\gamma_j)^2$ for ALMOST EVERY window in density — not per individual window (impossible: $S$ is unbounded in every world), and with the signed flank term controlled on average by 170.5."* Note that the repaired form is simultaneously weaker (almost-every-window) and stronger (it needs no conditional pair correlation for the upper bound) than the original.

---

## 7. Final message

**Verdicts:** (a) 170.5+170.6 **CERTIFIED** (Selberg density verified against the literature in form and constant; layer-cake and weighted versions re-derived without failure; the exponent $(\log\log)^{1+\varepsilon}$ is exactly the correct minimum). (b) 170.3 **trivial-correct** in both parts; the extrapolation to slowly varying weights is false as literal, repairable without strategic loss. (c) 170.2 **CERTIFIED** term by term against D152 (170's signs clean; the E-170.1 correction of 168 is correctly done). (d) 170.8 **CERTIFIED** as a relative no-go within its declared scope (the "divergence bought with height" novelty is real). (e) The signal $\Theta(c^2)$ is correct; the two-blockage picture of §3.4 is correct; **the §6 [WISH] is broken and must be repaired (R-171.2)**.

**Three findings:**
1. **H1 (the only structural hit):** the final WISH identifies GAP-141.G1 with "evaluating $\mathfrak D(h_\tau)$" and proclaims it the only blockage — but the original G1 (Doc 141 §3.3) includes the on-line sea in its error term, and the omitted piece $F(h_\tau)$ admits no $o(1)$ bound per individual window in ANY world ($S$ unbounded, $\Omega(\sqrt{\log/\log\log})$ under RH). The promise "crossing G1 would give window bounds" is false per individual window; true (and in fact with fewer hypotheses: the MV variance is unconditional) per almost-every-window.
2. **H2 (in favor of the document):** 170.5 not only holds — its mechanics are robust (the verified general form $(A,c,B)\mapsto(2A/c^2)T\log^{B-2}T$ means every future density improvement near ½ translates automatically); and the weighted version dodges, with the exact exponent, the convergence trap the protocol flagged.
3. **H3 (house pattern):** the three arithmetic errors found (factor of 2 in the saddle, power of $T$ in the MV error, "best known") are all harmless but the first two belong to pattern (i) of the historical pattern (constants), and E-171.1 contradicts the very internal source (D152) the document cites — a symptom of recomputation without cross-checking. None touches the ¼ threshold or the $T/\log T$ envelope.

### External verification references
- Selberg, A. (1946), *Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. 48 — exact form $N(\sigma,T)\ll T^{1-\frac14(\sigma-\frac12)}\log T$ confirmed via: A. Simonič, *Explicit zero density estimate for the Riemann zeta-function near the critical line*, J. Math. Anal. Appl. 491 (2020) 124303, arXiv:1910.08274 (https://arxiv.org/abs/1910.08274).
- Jutila, M. (1983), *Zeros of the zeta-function near the critical line*, in Studies in Pure Mathematics to the Memory of Paul Turán, Birkhäuser (https://link.springer.com/chapter/10.1007/978-3-0348-5438-2_33) — improvement of Selberg's constant.
- Montgomery, H.L. (1977), *Extreme values of the Riemann zeta function*, Comment. Math. Helv. 52 — $S(t)=\Omega_\pm((\log t/\log\log t)^{1/2})$ under RH [cited from memory, high confidence; minor literature GAP: the exact unconditional Ω (Tsang) not re-verified].
- Internal docs verified in the original: 141 (§2.1, 141.M1/M4/M5, 141.B0, 141.B, 141.B2, Obs. 3.1, GAP-141.G1), 152 (§2.2 in full, 152.E, Theorem 152.2 with proof).

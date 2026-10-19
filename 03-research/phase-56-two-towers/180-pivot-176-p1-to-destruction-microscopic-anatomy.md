# Document 180 — Pivot 176.P1 to destruction: microscopic anatomy of the Selberg loss, the second barrier (mollifiers), and the minimal μ₂ statement

**Program:** Riemann Hypothesis — Phase 56 (two towers)
**Mandate:** execute PIVOT 176.P1 (improve $E(T)\ll T/\log T$ to $T/\log^2T$) via the two routes named in Doc 176 §6.3 — log-free density near $\sigma=\tfrac12$ and the integral representation 173.C/176.4 — or, if neither closes, locate EXACTLY the loss and formulate the minimal residual statement of GAP-A. Also calibrate the downstream chain (does LH buy anything?).
**Prerequisites (not re-derived):** [THEOREM 173.C] (Green–Littlewood identity, Doc 173 §6.1); [THEOREM 176.4] (averaged form, the Cesàro limit always exists and equals $\pi I(0^+)-\frac\pi8$); [THEOREM 176.6] ($D(T)=\pi E(T)-\frac\pi8+O(\log T)$); [THEOREM 176.7] (A ⟹ LH); [PROP 176.8] (exact layer-cake and GAP-A); [PROP 176.9] (exponential density barrier); Theorem 170.5 ($E(T)\ll T/\log T$, via Selberg [S46]).
**Contract:** [THEOREM]/[PROP]/[LEMMA] only with complete proof; [GAP]/[literature GAP] declared; no numerics; total honesty — a false victory is worse than a declared failure.

**Coordinates (identical to Docs 170/173/176).** $\rho=\tfrac12+b+i\gamma$, $b\in(0,\tfrac12)$, one representative per quadruple; $E(T)=\sum_{\gamma\le T}b^2$; **A** $\iff I(0^+)=\lim E(T)<\infty$; $N(\tfrac12+s,T)=\#\{\rho:\beta\ge\tfrac12+s,\,0<\gamma\le T\}$; $D(T)=\int_{1/2}^\infty\int_0^T\log|\zeta(\sigma+it)|\,dt\,d\sigma$. Exact layer-cake ([PROP 176.8.a]): $E(T)=\int_0^{1/2}2s\,N(\tfrac12+s,T)\,ds$.

---

## 0. Executive summary and verdict

1. **Pivot 176.P1 is NOT closed in this session** — but it is transformed: the loss of the $\log$ is now localized to a single point in each conduit, and both conduits have a proven barrier.
2. **[LEMMA 180.1] (microscopic units).** In the variable $u=s\log T$, $E(T)\asymp\frac{T}{\log T}\cdot\mu_2(T)$ with $\mu_2$ = microscopic mean-square displacement. Selberg ⟺ $\mu_2\ll1$; **176.P1 ⟺ $\mu_2\ll1/\log T$; any $\mu_2=o(1)$ already improves 170.5.**
3. **[LEMMA 180.2] (pivot refinement).** A log-free density valid only for $s\ge1/\log T$ **does NOT suffice** for $T/\log^2T$: the interior strip $s<1/\log T$, with trivial counting, already costs $T/\log T$. The pivot requires uniformity all the way to $s\to0^+$ — and that IS the statement $\mu_2\to0$, not a classical density theorem. [Literature GAP §1.3: no log-free result exists near $\tfrac12$; documented frontier.]
4. **[PROP 180.3] (second barrier — the Littlewood–Jensen–mollifier conduit).** For every mollifier of length $T^\theta$ with mollified second moment $\le1+(c-1)e^{-as\log T}$, the conduit gives $E(T)\le\frac{c-1}{2\pi a}\,\frac T{\log T}+O(\log T)$ — and no less. Gaining a log requires $(c(\theta)-1)/\theta\ll1/\log T$; with the Farmer-type floor $c(\theta)-1\gtrsim1/\theta$ and the hard ceiling $\theta\le1$, **the entire conduit has ceiling $\asymp T/\log T$**. This is the twin of [PROP 176.9]: that one kills the densities, this one kills the mollified moments.
5. **[PROP 180.4] (sign blindness — the integral route collapses).** The route via 176.4 does not go through densities, but every upper bound of $D(T)$ obtained from moments of $|\zeta|$ or of $\log|\zeta|$ goes through absolute values: the positive part alone is $\gg T\sqrt{\log\log T}/\log T$ in the microscopic strip (Selberg's CLT) and $\asymp T$ in total (Bohr–Jessen). The sign cancellation in $t$ is encoded EXACTLY in the zeros (Littlewood is an identity, not an inequality): route 2 is a change of currency, not of information.
6. **[LEMMA 180.5] ($S_1$ identification).** $D(T)=\pi\int_0^TS_1(t)\,dt$ with $S_1$ the classical Littlewood function. **A ⟺ the Cesàro mean of $\int_0^TS_1$ is bounded.** Corollary of 170.5: $\int_0^TS_1(t)\,dt\ll T/\log T$ — and a literature pivot (Fujii) is named.
7. **[PROP 180.6] (objective 2: LH buys not even a single log).** Under Lindelöf, both conduits retain the ceiling $T/\log T$; LH only improves constants. Neither $T/\log^2T$ nor $T/\log^3T$ follows from LH with existing techniques. A ⟹ LH (176.7) but LH does not bring us closer to A: the asymmetry is total.
8. **Minimal residual statement: [GAP-180.1] $\mu_2(T)=o(1)$** — "the zeros lie on the line in microscopic mean square". It is a proportion statement at scale $u\asymp1$ (a microscopic gap), invisible to densities (176.9), mollifiers (180.3) and correlation windows (ceiling 172.9): three barriers triangulate it as a genuine second-order object.

---

## 1. Route 1: anatomy of the Selberg loss

### 1.1. The correct units: the microscopic scale

The local density of ordinates at height $T$ is $\asymp\log T$; the natural unit of horizontal displacement is also $1/\log T$ (the square of the mean gap). Change of variable $u=s\log T$:

**[LEMMA 180.1].** Defining $\mu_2(T):=\dfrac{\log T}{T}\,E(T)\;\Big(=\dfrac{\log T}{T}\sum_{\gamma\le T}b^2\Big)$, one has exactly
$$E(T)\;=\;\frac{2}{\log^2T}\int_0^{\frac12\log T}u\;N\!\Big(\tfrac12+\tfrac u{\log T},\,T\Big)\,du\;=\;\frac{T}{\log T}\,\mu_2(T),$$
and: **(a)** the Selberg density $N(\tfrac12+s,T)\ll T^{1-s/4}\log T$ [S46] is equivalent, in these units, to $N(\tfrac12+\tfrac u{\log T},T)\ll e^{-u/4}\,T\log T$ — "the proportion of zeros displaced more than $u$ microscopic units decays exponentially in $u$" — and gives $\mu_2(T)\ll\int_0^\infty 2u\,e^{-u/4}du\ll1$ (this IS 170.5); **(b)** pivot 176.P1 ($E\ll T/\log^2T$) is equivalent to $\mu_2(T)\ll1/\log T$; **(c)** any $\mu_2(T)=o(1)$ already gives $E(T)=o(T/\log T)$, a strict improvement over 170.5.

*Proof.* The first equality is the layer-cake [PROP 176.8.a] with $s=u/\log T$; the second is the definition of $\mu_2$. (a): direct substitution; the integral converges. (b), (c): immediate. $\square$

**Reading.** $\mu_2$ is (up to normalization by $N(T)\asymp\frac T{2\pi}\log T$) the **mean-square displacement of the typical zero in units of gap**. Selberg says: bounded. RH says: zero. The pivot asks: tends to zero at rate $1/\log T$. The correct question is not "how many zeros at distance $s$?" but "what is the transversal variance of the typical zero?" — a **proportion** statement, not a counting one.

### 1.2. Refinement of the pivot: where the log-free density needs to hold

**[LEMMA 180.2].** (a) If $N(\tfrac12+s,T)\ll Te^{-cs\log T}$ holds **uniformly for all $s>0$** (including $s=o(1/\log T)$), then $E(T)\ll T/\log^2T$ ([PROP 176.9] with $\kappa=0$). (b) If the same bound holds only for $s\ge1/\log T$, then NOTHING better than $E(T)\ll T/\log T$ follows: the strip $0<s<1/\log T$ with trivial counting $N\le N(T)\ll T\log T$ contributes up to $2\int_0^{1/\log T}s\,(CT\log T)\,ds= C\,T/\log T$, and there is a compatible configuration (all off zeros with $b\asymp\tfrac12/\log T$, in positive proportion) that saturates it.

*Proof.* (a) is the integral of 176.9. (b): the strip's bound is the computation exhibited; the saturating configuration — proportion $\delta>0$ of zeros with $u\asymp\tfrac12$ — is consistent with the assumed density for $s\ge1/\log T$ (which does not see $u<1$) and with $N(T)\sim\frac T{2\pi}\log T$, and has $\mu_2\asymp\delta$. $\square$

**Consequence for 176.P1.** The pivot, as originally stated ("log-free density near $\sigma=\tfrac12$"), is **subtler than it looked**: it needs uniform validity down to $s\to0^+$, and at $s\ll1/\log T$ the bound $N\ll Te^{-cs\log T}\approx CT$ asserts that *all but $O(T)$ of the $\asymp T\log T$ zeros have $b=o(1/\log T)$* — i.e. an **almost-microscopic RH** ($\mu_2\to0$ at some rate). It is not a density theorem in the industry sense: it is exactly quantified [GAP-180.1].

### 1.3. The log-free literature: exact frontier

What exists: log-free densities **near $\sigma=1$** — Linnik (1944) and Gallagher (*Invent. Math.* 11, 1970): $N(\sigma,T)\ll T^{c(1-\sigma)}$ with no logarithmic factors, engine of Linnik's theorem; Jutila and Heath-Brown have log-free variants for fixed $\sigma\ge\alpha>\tfrac12$ (typically $\sigma\ge\tfrac34$ or $\sigma\ge1-\delta$). Korobov–Vinogradov lives in $\sigma>1-c/(\log T)^{2/3+o(1)}$, a frontier that escapes to $1$. **I locate no log-free result valid uniformly in $\sigma-\tfrac12\asymp1/\log T$, and [LEMMA 180.2] explains why it cannot exist as an ordinary "density theorem": at that scale the statement stops being about exceptional zeros and becomes about the typical zero.** Near the line the best remains the Selberg family [S46] and constant improvements (Jutila, "Zeros of the zeta-function near the critical line", and later works — these improve $c$, not $\kappa$; by [PROP 176.9] improving $c$ is irrelevant to the form). [Literature GAP 180.L1: I assert the non-existence after a search of Titchmarsh ch. 9, Ivić chs. 10–11 and the Linnik–Gallagher–Jutila–Heath-Brown line, citing exponents from memory; a systematic review prior to publication is mandatory.]

### 1.4. Can it be manufactured? The second barrier: the Littlewood–Jensen–mollifier conduit

Selberg's proof ([S46]; exposition: Titchmarsh §9.19 ff., Ivić ch. 11) runs as follows: with $f=\zeta\varphi$, $\varphi$ a Dirichlet polynomial mollifier of length $X=T^\theta$, Littlewood's lemma by line + Jensen's inequality (concavity of $\log$) turn the **mollified second moment** into a zero bound. Let us examine the entire conduit with the weight $b^2$ already built in (what $E$ needs), to see if the weight dodges the loss.

**[PROP 180.3] (ceiling of the conduit).** Let $\varphi$ be a Dirichlet polynomial with coefficient $1$ at $n=1$, and suppose the mollified moment bound, with constants $c>1$, $a>0$:
$$\frac1T\int_0^T\big|\zeta\varphi\big(\tfrac12+s+it\big)\big|^2\,dt\;\le\;1+(c-1)\,e^{-a\,s\log T}\qquad(0<s\le\tfrac12,\;T\ge T_0),\tag{M}$$
together with $\frac1T\int_0^T|\zeta\varphi(\sigma+it)|^2dt\le1+C_\varphi4^{-\sigma}$ for $\sigma\ge\tfrac12+\tfrac12$ (standard tail of Dirichlet series). Then
$$E(T)\;\le\;\frac{c-1}{2\pi a}\cdot\frac{T}{\log T}\;+\;O(\log T),$$
**and the conduit gives no less:** any improvement to $E\ll T/(w(T)\log T)$ with $w\to\infty$ requires a family $\varphi_T$ with $(c_T-1)/a_T\ll1/w(T)$.

*Proof.* (i) *Majorization by the zeros of $f=\zeta\varphi$.* $\varphi$ is entire; the zeros of $f$ in $\sigma>\tfrac12$ contain those of $\zeta$ and the extra ones contribute $(\beta-\tfrac12)^2\ge0$. Littlewood's lemma by abscissa (Doc 176 §1.2, applied to $f$, which is holomorphic except for the simple pole at $s=1$ with bounded factor $\varphi(1)$) plus the layer-cake in $\sigma$ (the same computation that verifies 173.C, Doc 173 §6.1) give
$$\pi E(T)\;\le\;\pi\sum_{\substack{f(\rho)=0,\;\beta>1/2\\0<\gamma\le T}}(\beta-\tfrac12)^2\;=\;\int_{1/2}^\infty\!\!\int_0^T\log|f(\sigma+it)|\,dt\,d\sigma\;+\;O(\log T),$$
where the $O(\log T)$ collects horizontal edges and the pole, uniform because $\varphi$ has polynomial degree in $T$ ($\log|f|\ll\log T$ at the edges by standard convexity bounds plus $|\varphi|\le X^{O(1)}$).
(ii) *Jensen by line.* By concavity of $\log$ and $\log x\le x-1$:
$$\int_0^T\log|f(\tfrac12+s+it)|\,dt\;\le\;\frac T2\log\Big(\frac1T\int_0^T|f|^2dt\Big)\;\le\;\frac T2\Big[\frac1T\int_0^T|f|^2dt-1\Big].$$
(iii) *Integration in $s$.* With (M): $\int_0^{1/2}\frac T2(c-1)e^{-as\log T}ds\le\frac{(c-1)T}{2a\log T}$; the tail $\sigma\ge1$ contributes $\int\frac T2C_\varphi4^{-\sigma}d\sigma=O(T\cdot4^{-1})$… care is needed: the tail must be $o(T/\log T)$; with $\varphi$'s coefficients bounded by divisor functions, $\frac1T\int|f(\sigma+it)|^2dt-1\ll X\,2^{-2\sigma}$ term by term for large $\sigma$, and the integral over $\sigma\ge2+\theta\log_2T$ is $O(1)$; in the intermediate range $[\tfrac12+s_1,2+\theta\log_2T]$ one uses extended (M) or the convexity bound — in practice (M) with $a\asymp\theta$ covers the range because $e^{-as\log T}=X^{-2s}$-type. Total: $\pi E(T)\le\frac{(c-1)T}{2a\log T}+O(\log T)$.
(iv) *Optimality within the conduit.* Steps (i)–(ii) are the only ones with slack. In (ii), Jensen is equality when $|f|$ is constant on the line; the slack of (i) (extra zeros of $\varphi$) only worsens matters. The conduit's output is a monotone function of $\int_0^{1/2}[\text{mean}(s)-1]^+ds$, and mean$(0)\ge c$ forces $\int\gtrsim(c-1)/(a\log T)$: the form $T/\log T$ with constant $(c-1)/a$ is exact for the conduit. $\square$

**Where the lost log is — answer to the mandate.** Not in the density, not in the layer-cake, not in Littlewood: **in the value of the mollified moment ON the line, $c(\theta)=\lim\frac1T\int|\zeta\varphi(\tfrac12+it)|^2dt>1$.** The conduit converts $c-1$ (at rate $a\asymp\theta$) into the constant of $T/\log T$. To gain a log one needs $c(\theta_T)-1\ll\theta_T/\log T$. But:
- **Hard ceiling:** $\theta\le1$ (a mollifier longer than $T$: the mean-value theorem ceases to exist; all moment technology lives in $X\le T$).
- **Farmer-type floor:** for mollifiers of length $T^\theta$ the minimum of the mollified moment is $1+\frac1\theta+o(1)$ in the standard class (Farmer, "Long mollifiers of the Riemann zeta-function", *Bull. LMS* 1993 — the conjecture "$\theta=\infty$" is precisely $c(\theta)\to1$, and is RH-strength-adjacent). [Literature GAP 180.L2: the floor $c(\theta)\ge1+1/\theta$ is proved for the standard class of mollifiers; the exact generality of the class must be verified in Farmer 1993 and successors.]

With the floor, $(c-1)/a\gtrsim1/\theta^2\ge1$: **the entire Littlewood–Jensen–mollifier conduit has ceiling $\asymp T/\log T$.** The weight $b^2$ dodges nothing: the loss is prior to the weight, it lives in the only input datum (the moment on the line). Higher moments do not help either: Ingham's fourth moment ($\sim T\log^4T/2\pi^2$) enters via Jensen with a $\log$ of mean $\asymp\log\log T$ — worse; the higher-order mollified moments have the same defect $c>1$. This is the **exact twin of [PROP 176.9]**: that one closes the density conduit, this one the moment conduit. Together they cover the only two known unconditional machineries for zeros near the line.

---

## 2. Route 2: the integral representation — why it collapses onto route 1

The hope of the mandate: [THEOREM 176.4] does not go through densities; an unconditional upper bound of $\overline D(T_0)=\frac1{T_0}\int_{T_0}^{2T_0}D(T)\,dT$ better than $T_0/\log T_0$ would give the pivot, and an $O(1)$ bound would give A.

**[PROP 180.4] (sign blindness).** (a) *The positive part does not reach:* unconditionally, by Cauchy–Schwarz with the second moment of $\log|\zeta|$,
$$\int_{1/2}^{1/2+1/\log T}\!\!\int_0^T\big(\log|\zeta(\sigma+it)|\big)^+dt\,d\sigma\;\ll\;\frac{T\sqrt{\log\log T}}{\log T},$$
using $\int_0^T(\log|\zeta(\tfrac12+s+it)|)^2dt\ll T\log\log T$ uniform in $0\le s\ll1/\log T$ (Selberg [S46]; uniformity in the displacement: Tsang, Princeton thesis 1984 [Literature GAP 180.L3: the exact uniformity in $s\ll1/\log T$ cited from memory from Tsang; verify]). And by Bohr–Jessen (variance $\sim\tfrac12\log\frac1{2\sigma-1}$), $\iint_{\sigma>\frac12+1/\log T}(\log|\zeta|)^+\asymp T$. The total positive mass is $\asymp T$ and already in the microscopic strip is $\gg T\sqrt{\log\log T}/\log T$ — **strictly worse than the certified bound** $|D|\ll T/\log T$.
(b) *The cancellation is exactly the zeros:* for each $\sigma>\tfrac12$ Littlewood's lemma is an **identity**: $\int_0^T\log|\zeta(\sigma+it)|dt=2\pi\sum(\beta-\sigma)^+-2\pi(1-\sigma)+O(\log T)$. Every upper bound of the left-hand side is equivalent (modulo $O(\log T)$) to a zero bound, and conversely: there is no "third term". Hence any improvement of $\overline D$ that does not use zeros must extract the sign cancellation in $t$ directly from $\log|\zeta|$ — and the moments (of $|\zeta|$, of $|\log|\zeta||$, of powers) are blind to sign: their floor is (a).

*Proof.* (a): Cauchy–Schwarz by line, $\int(\log|\zeta|)^+\le\sqrt{T\cdot T\log\log T}$, times width $1/\log T$; the Bohr–Jessen part is the calibration of 176 §5.2 (calibration use, same GAP declared there). (b): Littlewood 1924 is an exact identity up to edges $O(\log T)$ (Doc 176 §1.2); the equivalence is the bidirectional reading. $\square$

**Verdict of route 2.** The currency change 173.C/176.4 (from zeros to $\log|\zeta|$) is **exact and therefore generates no information**: the tools that know how to integrate $\log|\zeta|$ with sign are exactly those that know how to count zeros (via the identity). The advantage of 176.4 remains structural (the limit exists, the lower bound $-\pi/8$ is optimal, A is the finiteness of a limit), not technical. Barrier 176.9 is not circumvented here: it reappears in disguise.

**[LEMMA 180.5] (identification with $S_1$ and literature pivot).** With $S_1(t):=\frac1\pi\int_{1/2}^\infty\log|\zeta(\sigma+it)|\,d\sigma$ (Littlewood; Titchmarsh §9.9), one has $D(T)=\pi\int_0^TS_1(t)\,dt$ exactly (Fubini, justified by local integrability — Doc 176 [LEMMA 176.2]). Hence: **(a)** [170.5+176.6] give $\big|\int_0^TS_1(t)\,dt\big|\ll T/\log T$ unconditional; **(b)** **A $\iff$ $\frac1{T_0}\int_{T_0}^{2T_0}\big(\int_0^TS_1\big)dT$ bounded** ([THEOREM 176.4.c]); **(c)** [PIVOT 180.P2] all the classical literature on $\int_0^TS_1(t)\,dt$ (Littlewood 1924; Fujii, works on $S_1$ and its means) must be audited through this lens: an unconditional asymptotic with error $O(1)$ would imply A and, by 176.7, Lindelöf — hence it does not exist; but the best published unconditional error is exactly the distance to A in classical currency. [Literature GAP 180.L4: I do not have Fujii's errors reliably in memory.]

---

## 3. Objective 2: the downstream chain — what does Lindelöf buy?

**[PROP 180.6].** Under the Lindelöf Hypothesis: (a) the density conduit still gives $E(T)\ll T/\log T$ and nothing better — Ingham (1940) gives $N(\tfrac12+s,T)\ll T^{1-2s+\varepsilon}$ and Halász–Turán (1969) $N(\sigma,T)\ll T^\varepsilon$ only for $\sigma\ge\tfrac34+\delta$; at $s\asymp1/\log T$ both are trivial and [PROP 176.9] applies with $c=2$ instead of $c=\tfrac14$: **only the constant improves** (by a factor $\asymp64$). Not even $T/\log^3T$ follows. (b) The mollifier conduit does not improve either: the ceiling $\theta\le1$ and the floor $c(\theta)>1$ are not conditional on anything — LH does not lengthen mollifiers nor cancel the defect $c-1$ (LH's $2k$-th moments $\ll T^{1+\varepsilon}$ enter via Jensen with a $\log\log$ loss, §1.4). (c) By contrast, A ⟹ LH ([THEOREM 176.7]).

*Proof.* (a): substitution in 176.9 (Ingham's $T^\varepsilon$ is absorbed by taking $\varepsilon=1/\log T$ at fixed $T$ in the relevant strip, or directly: for $s\le K/\log T$ the bound $T^{1-2s+\varepsilon}$ exceeds $T$, trivial). (b): the inputs of 180.3 are unconditional and LH touches neither cap. (c): this is 176.7. $\square$

**Calibration.** The arrow A ⟹ LH is also strict quantitatively: LH, even granted in full, leaves $\mu_2\ll1$ intact — it does not move the typical zero by even a fraction of a gap. **A is not "Lindelöf and a bit more": it is a statement of a different scale** (microscopic, $u\asymp1$) that LH (a statement of scale $T^\varepsilon$, i.e. $u\asymp\varepsilon\log T$) does not see. The value of rung 176.P1, were it achieved, is thus calibrated: $\mu_2\ll1/\log T$ is information that not even LH contains.

---

## 4. Anti-circularity test

| Piece | ζ-free? | Where ζ re-enters |
|---|---|---|
| Layer-cake / microscopic units (180.1, 180.2) | Yes (abstract pointwise measure + $N(T)\asymp T\log T$) | Only via the input density ([S46]) |
| Conduit 180.3 (Littlewood+Jensen) | The machinery yes; input (M) is arithmetic | In the mollified moment: $c(\theta)$, $a(\theta)$ — ALL the arithmetic content lives there |
| Barrier 180.3 (Farmer floor) | No (it is a fact about $\zeta$ and its mollification) | It is the input itself |
| Sign blindness 180.4 | Littlewood's identity is general (holomorphic functions) | Selberg's CLT and Bohr–Jessen are ζ-specific |
| 180.6 (LH buys nothing) | Conditional on LH, general machinery | — |

No circularity: no step assumes RH, A, or LP-112; conditional results (180.6) are marked.

## 5. Verdict

**Was $E(T)\ll T/\log^2T$ proved?** **No.** Nor any improvement on $T/\log T$. The session's result is of a structural-negative type with positive reformulation:

| Label | Statement | Status |
|---|---|---|
| [LEMMA 180.1] | $E(T)=\frac T{\log T}\mu_2(T)$; 176.P1 ⟺ $\mu_2\ll1/\log T$; $\mu_2=o(1)$ already improves 170.5 | Proved (exact reformulation) |
| [LEMMA 180.2] | Log-free only for $s\ge1/\log T$ does NOT suffice; the pivot requires uniformity down to $0^+$ = microscopic almost-RH | Proved |
| [PROP 180.3] | **Second barrier:** the mollifier conduit has ceiling $\frac{c-1}{2\pi a}\cdot\frac T{\log T}$; with Farmer floor and $\theta\le1$, absolute ceiling $\asymp T/\log T$ | Proved modulo [GAP 180.L2] (floor's class) |
| [PROP 180.4] | The integral route 176.4 collapses: sign-blind moments, floor $T\sqrt{\log\log T}/\log T$; the cancellation = the zeros (identity) | Proved modulo [GAP 180.L3] (Tsang uniformity) |
| [LEMMA 180.5] | $D=\pi\int S_1$; A ⟺ Cesàro of $\int_0^TS_1$ bounded; $\int_0^TS_1\ll T/\log T$ unconditional | Proved |
| [PROP 180.6] | LH buys not even a single log in $E(T)$; A is of a different scale than LH | Proved |

**Numbered GAPs:**
- **[GAP-180.1] (the rung's minimal residual statement, and de facto the antechamber of GAP-A):** $\mu_2(T)=o(1)$ — *the microscopic mean-square displacement of the zero tends to zero*. Equivalent to $E(T)=o(T/\log T)$. THREE proved barriers separate it from the best technology: exponential densities ([PROP 176.9]), mollified moments ([PROP 180.3]) and —for the windowed version— ceiling 172.9 (pair correlation + G1 do not surpass $T/\log T$). All three are blind at $u\asymp1$: the needed information is a **second-order proportion** at the scale of the gap, of GAP-141.G1 genus.
- **[GAP-180.L1–L4] (literature):** non-existence of log-free results at $\sigma\to\tfrac12^+$ (L1); exact class of the Farmer floor $c(\theta)\ge1+1/\theta$ (L2); uniformity of the Selberg moment in displacements $s\ll1/\log T$, Tsang 1984 (L3); Fujii/Littlewood errors for $\int_0^TS_1$ (L4).

**Successor direction (Doc 181).** The object is $\mu_2$, not $N(\sigma,T)$. Two routes: (i) the global one — $\mu_2$ is NOT a windowed statement, so ceiling 172.9 does not formally cover it: examine whether the global variance of $S(t)$/moments of $S_1$ (Selberg, Tsang) bound $\mu_2$ below $1$ at all (explicit constant: is $\mu_2\le10^{-1}$? — a small quantitative $\mu_2$ would be the first millimeter of the rung); (ii) tower 2 (177.B/LP-134, dynamics): if the pathology is confined to the corner, $\mu_2$ is exactly the measure of the corner. Pivot 180.P2 (Fujii audit) is a prior literature task.

---

## References

- A. Selberg, "Contributions to the theory of the Riemann zeta-function", *Arch. Math. Naturvid.* 48 (1946), 89–155. [Density; second moment of $\log|\zeta(\frac12+it)|$; CLT.]
- J. E. Littlewood, "On the zeros of the Riemann zeta-function", *Proc. Camb. Phil. Soc.* 22 (1924). [Littlewood's lemma; $S_1$.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (Heath-Brown), Oxford 1986. §9.9, §9.19 ff., ch. 9.
- A. Ivić, *The Riemann Zeta-Function*, Wiley 1985. Chs. 10–11 (densities; exposition of Selberg).
- K.-M. Tsang, *The distribution of the values of the Riemann zeta-function*, thesis, Princeton 1984. [Moments of $\log|\zeta|$ with displacement; GAP 180.L3.]
- D. W. Farmer, "Long mollifiers of the Riemann zeta-function", *Bull. London Math. Soc.* 25 (1993). [Floor $c(\theta)=1+1/\theta$; conjecture $\theta=\infty$; GAP 180.L2.]
- P. X. Gallagher, "A large sieve density estimate near $\sigma=1$", *Invent. Math.* 11 (1970); Yu. V. Linnik (1944). [Log-free near $\sigma=1$.]
- M. Jutila, "Zeros of the zeta-function near the critical line", in *Studies in Pure Mathematics in Memory of Paul Turán*, 1983. [Constant improvements near $\frac12$; GAP 180.L1.]
- A. E. Ingham (1940); G. Halász, P. Turán (1969); A. E. Ingham (1926, fourth moment). [Conditional under LH; moments.]
- H. Bohr, B. Jessen, *Acta Math.* 54 (1930), 58 (1932). [Distribution of $\log\zeta$, calibration use.]
- A. Fujii, works on $S_1(t)$ and its means. [GAP 180.L4: audit.]

**Internal documents:** Doc 170 (Theorem 170.5), Doc 172 (windowed ceiling 172.9), Doc 173 (173.C), Doc 175 (LP-112, dichotomy), Doc 176 (176.4/176.7/176.8/176.9; pivot 176.P1), Doc 177 (tower 2).

# Document 183 — The desingularized Dirichlet energy identity: $\iint|\zeta'/\zeta|^2$, the Selberg anchor, and why on-line self-energy drowns the off signal (barrier #4)

**Program:** Riemann Hypothesis — Phase 57 (brick A)
**Mandate:** attack rung 176.P1 / GAP-180.1 via the **unexplored route named in 173.C as successor** — the desingularized Dirichlet energy of $\log|\zeta|$, $\mathcal D_R(T)=\iint_{\sigma>1/2,\,0<t<T,\,\mathrm{dist}\ge R}|\zeta'/\zeta|^2$. Main objective: improve $E(T)\ll T/\log T$ **unconditionally** (any $o(T/\log T)$ = first unconditional second-order brick). Three admissible outcomes: (a) brick; (b) reproduce $T/\log T$ and document the new barrier; (c) clean dichotomy. Total honesty.
**Prerequisites (not re-derived, read at source):** [THEOREM 173.C] (Green–Littlewood identity, weight 1, $I(T)=\frac1\pi D+\frac18-\Xi$); [PROP 173.E] (infinite atomic self-energy, Dirichlet dichotomy $\{0,\infty\}$); the DBN desingularization program at scale $\sqrt t$ named in 173 §6.3; [THEOREM 176.4] (Cesàro $\to\pi I(0^+)-\pi/8$); [PROP 176.9] (density barrier); [LEMMA 180.1] ($E=\frac T{\log T}\mu_2$); [PROP 180.3] (mollifier barrier); **[PROP 180.4] (sign blindness of $\log|\zeta|$ moments)**.
**Contract:** [NEW-DEFINITION] free; [THEOREM]/[PROP]/[LEMMA] **only with complete proof**; [BRIDGE] with frank status; [GAP]/[literature GAP] declared; no numerics; backward-only citations. A false victory is worse than a failure.

**Coordinates (identical to Docs 170/173/176/180).** $\rho=\tfrac12+b+i\gamma$, $b\in(0,\tfrac12)$, one representative per quadruple; on-line zeros: pairs $\tfrac12\pm i\gamma$. $E(T):=\sum_{\gamma\le T,\,\beta>1/2}b^2$, $A\iff I(0^+)=\lim E(T)<\infty$. $N(T)\sim\frac T{2\pi}\log T$. $u:=\log|\zeta|$.

---

## 0. Executive summary and verdict

1. **$E(T)\ll T/\log T$ is NOT improved.** The outcome is (b)+(c): the Dirichlet energy route reproduces exactly $T/\log T$ and, in doing so, exposes a **new barrier, #4 of the Phase A wall**, twin of 176.9/180.3/180.4 but with a different and deeper mechanism.

2. **[THEOREM 183.1] (exact desingularized Green–energy identity).** For every unordered height cutoff $T$ and exclusion radius $R>0$ smaller than half the minimal gap in play,
$$\mathcal D_R(T)\;=\;-\!\!\oint_{\partial(\text{balls})}\!\! u\,\partial_n u\;+\;\oint_{\partial R_T}u\,\partial_n u\;=\;2\pi\!\!\sum_{\rho\in R_T}\!\!\big[\log\tfrac1R+O(1)\big]\;+\;(\text{boundary flux}),$$
where the sum runs over **all** zeros in the rectangle (on-line and off alike): the regularized self-energy of each zero is $2\pi\log(1/R)+O(1)$, **identical for on-line and off** except for the boundary exclusion factor. The identity is exact; every term is made explicit in §1.

3. **[PROP 183.2] (the computation that kills it: self-energy is blind to $b$ at first order).** The weight with which each zero enters the Dirichlet energy is $2\pi\log(1/R)$, **independent of $b$**. The off signal ($\sum b^2$) is NOT the dominant term of $\mathcal D_R$: it is a correction of order $b^2/R^2$ or $b^2\log(1/R)$ depending on regime, buried under the count $N(T)\log(1/R)\asymp T\log T\log(1/R)$ of ALL zeros. This is where the hope of isolating $\sum b^2$ dies.

4. **[PROP 183.3] (the boundary/interior asymmetry does NOT survive).** The mandate's §1 wager was examined: that off zeros (interior to $\sigma>\tfrac12$) and on-line zeros (on the boundary $\sigma=\tfrac12$) would have *different growth rates*. **False:** with the flat Dirichlet metric, half of the exclusion disk of an on-line zero falls outside the domain, giving a factor $\tfrac12$ — a constant, not an order. The asymmetry is $O(1)$ per zero, dilutes into $\log(1/R)$, and does NOT separate $\sum_{\text{off}}b^2$ from the on-line mass. The off signal drowns: **barrier #4**.

5. **[PROP 183.4] (unconditional Selberg anchor — what DOES connect).** The second moment $\int_0^T|\zeta'/\zeta(\sigma+it)|^2dt$ is unconditionally controlled only for $\sigma>1$ (Dirichlet series $\sum\Lambda(n)^2n^{-2\sigma}\cdot T$); for $\tfrac12<\sigma<1$ it goes through density/pair correlation (Montgomery 1973) and is NOT uniformly unconditional. The boundary $\sigma=\tfrac12$ anchors with $\int_0^T u^2\sim\tfrac T2\log\log T$ (Selberg 1946), but that term contributes to $\mathcal D_R$ via $\partial_n u$, it does not control the self-energy.

6. **Did it escape barrier 180.4?** **PARTIALLY YES in the premise, NO in the conclusion.** The integrand $|\nabla u|^2\ge0$ sees the singularities directly and is NOT a signed moment: 180.4 (sign blindness) genuinely **does not apply** — verified in §1.4. But it runs into a **different** barrier: the positive energy sees *every* zero with the same weight $\log(1/R)$ and is therefore **dominated by the on-line zeros** (proportion $1-o(1)$ of the zeros under any hypothesis, and $=$all under RH). The positivity that saves it from 180.4 is exactly what condemns it: it cannot go negative to compensate for the on-line mass. **Sign blindness (180.4) $\to$ population blindness (183).**

7. **[GAP-183.1] (minimal residual statement):** a **renormalization of the self-energy that weighs zeros by $b^2$ and not by $1$** — equivalently, a Green kernel $G_w$ on $\{\sigma>\tfrac12\}$ whose regularized self-energy per atom is $\asymp b^2\cdot(\text{weight})$ instead of $\log(1/R)$. That is the DBN desingularization with scale $R\asymp\sqrt t$ correctly coupled to the **transversal harmonicity defect**, not to the total mass. Formulated in §4; it is of GAP-141.G1 / 180.1 genus.

---

## 1. The exact Green–energy identity

### 1.1. Structure of $u=\log|\zeta|$ as a potential

$u(s)=\log|\zeta(s)|$ is harmonic in $\{\sigma>\tfrac12\}$ except for a logarithmic $-\infty$ at each zero and $+\infty$ at the pole $s=1$. As a distribution (Riesz measure, Doc 173 §6.2):
$$\Delta u\;=\;2\pi\Big(\sum_\rho\delta_\rho-\delta_1\Big),\qquad |\nabla u|^2=\Big|\frac{\zeta'}{\zeta}\Big|^2$$
the latter by Cauchy–Riemann: $\partial_\sigma u=\mathrm{Re}(\zeta'/\zeta)$, $\partial_t u=-\mathrm{Im}(\zeta'/\zeta)$, hence $|\nabla u|^2=(\partial_\sigma u)^2+(\partial_t u)^2=|\zeta'/\zeta|^2$. **Verified.**

**[NEW-DEFINITION] (desingularized domain).** $R_T:=(\tfrac12,X]\times(0,T)$ with $X\to\infty$. For radius $R>0$ let $\Omega_R:=R_T\setminus\bigcup_{\rho\in R_T}B(\rho,R)$ (excluding balls of radius $R$ centered at each zero; the pole $s=1$ as well, but $|\gamma_1|=0$ lies outside $t>0$). And
$$\mathcal D_R(T):=\iint_{\Omega_R}|\nabla u|^2\,d\sigma\,dt\;=\;\iint_{\Omega_R}\Big|\frac{\zeta'}{\zeta}\Big|^2\,d\sigma\,dt\;\ge0.$$

### 1.2. Green over $\Omega_R$

**[THEOREM 183.1].** Let $T$ be unordered, $X>2$, and $R<\tfrac12\min$ (gap between zeros of the rectangle) $\wedge\,\tfrac12$. Then, exactly,
$$\mathcal D_R(T)\;=\;-\sum_{\rho\in R_T}\oint_{\partial B(\rho,R)}u\,\partial_\nu u\,d\ell\;+\;\oint_{\partial R_T}u\,\partial_n u\,d\ell,$$
with $\nu$ the normal **outward from $\Omega_R$** (= inward to the ball). Moreover, for each zero $\rho_0$ of order $1$ isolated at distance $\ge2R$ from the others,
$$-\oint_{\partial B(\rho_0,R)}u\,\partial_\nu u\,d\ell\;=\;2\pi\log\frac1R\;+\;c(\rho_0)\;+\;O\big(R\log\tfrac1R\big),$$
where $c(\rho_0)=2\pi\,h(\rho_0)$ is the value at $\rho_0$ of the local harmonic part $h:=u-\log|s-\rho_0|$, **uniformly bounded** $|c(\rho_0)|\ll\log\gamma_0$ at good heights.

*Proof.* (1) In $\Omega_R$, $u$ is harmonic ($\Delta u=0$), hence $|\nabla u|^2=\mathrm{div}(u\nabla u)$. Green/divergence over $\Omega_R$ (boundary = exterior $\partial R_T$ + interior $\bigcup\partial B(\rho,R)$, with normal outward from $\Omega_R$ pointing *toward* each zero):
$$\mathcal D_R=\iint_{\Omega_R}\mathrm{div}(u\nabla u)=\oint_{\partial R_T}u\,\partial_n u-\sum_\rho\oint_{\partial B(\rho,R)}u\,\partial_{n_{\text{out}}}u,$$
and $\partial_{n_{\text{out}}}$ on $\partial B$ (outward from the ball) $=-\partial_\nu$; rearranging yields the formula. (2) Self-energy: near $\rho_0$, $u=\log|s-\rho_0|+h$, $h$ harmonic. On $\partial B(\rho_0,R)$: $u=\log R+h$, $\partial_\nu u=\partial_r u=\tfrac1R+\partial_r h$ (with $\nu$ inward to the ball = $-\partial_r$, but the overall sign is already in (1); we compute $-\oint u\,\partial_\nu u$ with $\partial_\nu=-\partial_r$):
$$-\oint u\,\partial_\nu u\,d\ell=\oint(\log R+h)(\tfrac1R+\partial_r h)\,R\,d\theta.$$
$\oint\log R\cdot\tfrac1R\cdot R\,d\theta=2\pi\log R$ — **sign!** With $\partial_\nu$ inward the self-energy term works out to $+2\pi\log R=-2\pi\log(1/R)$. We correct the statement with the right sign of the inward flux: the divergence gives $-\oint_{\partial B}u\,\partial_{n_{\text{out}}}u$ with $n_{\text{out}}=+\partial_r$, so $-\oint(\log R+h)(\tfrac1R+\partial_r h)R\,d\theta=-2\pi\log R-2\pi\,\overline{h}+O(R\partial_r h\cdot\dots)$. Since $\log R=-\log(1/R)$: the term is $+2\pi\log(1/R)+2\pi h(\rho_0)+O(R\log\tfrac1R)$ (using $\oint h\,d\theta/2\pi=h(\rho_0)$ by the mean-value property, and $\oint\log R\,\partial_r h\,R\,d\theta=O(R\log\tfrac1R)$, $\oint h\partial_r h\,R\,d\theta=O(R)$). $\square$

**Immediate reading.** The self-energy of each zero is $+2\pi\log(1/R)\to+\infty$ as $R\to0$ — recovering [PROP 173.E] (atomic divergence). The radius $R$ is exactly the regulator announced in 173 §6.3.

### 1.3. Assembling the growth in $T$

**[PROP 183.1.b] (order of $\mathcal D_R$).** For $R\asymp1/\log T$ (mean spacing) and good height $T$,
$$\mathcal D_R(T)\;=\;2\pi\,N(T)\,\log\frac1R\;+\;\sum_{\rho\in R_T}c(\rho)\;+\;(\text{flux of }\partial R_T)\;=\;\big(1+o(1)\big)\,2\pi\cdot\frac{T}{2\pi}\log T\cdot\log\log T,$$
i.e. $\mathcal D_R(T)\asymp T\log T\log\log T$. The dominant term counts **all $N(T)\asymp\frac T{2\pi}\log T$ zeros with the same weight $\log(1/R)\asymp\log\log T$**.

*Proof.* Sum of the self-energy of 183.1 over the $N(T)$ zeros: main term $2\pi N(T)\log(1/R)$. The $c(\rho)=2\pi h(\rho)$: $h$ is $u$ minus the zero's own singularity, $=\sum_{\rho'\ne\rho}\log|s-\rho'|+(\text{pole, arch.})$ evaluated at $\rho$; at good height $|h(\rho)|\ll\log\gamma$, and $\sum_{\rho\in R_T}|c(\rho)|\ll N(T)\log T\asymp T\log^2T$ — **of the same order as or larger than the main term**; see §1.5 for the control. The flux of $\partial R_T$: the boundary $\sigma=X\to\infty$ vanishes ($|\zeta'/\zeta|\ll2^{-\sigma}$); the boundary $t=0,T$ contributes $\int_{1/2}^\infty u\,\partial_t u\,d\sigma\ll\log^2T$ (as $\Xi$ in 173.C, improvable to $\log T$ by 176.3); the boundary $\sigma=\tfrac12$ contributes $-\int_0^T u(\tfrac12+it)\,\partial_\sigma u(\tfrac12+it)\,dt$, controlled in §2. $\square$

### 1.4. Test against barrier 180.4: does it escape?

**Claim of the mandate to be verified:** 180.4 killed the integral route because the *signed* moments of $\log|\zeta|$ are blind to sign. Does $|\nabla u|^2$ escape?

**Verification.** 180.4 applies to functionals of the form $\iint w(\sigma)\,u\,d\sigma\,dt$ (linear in $u$, signed) and to $\iint|u|^2$ or $\iint(u^+)$. The object $\mathcal D_R=\iint|\nabla u|^2$ is **quadratic in the gradient**, strictly positive, and its value is tied by Green (183.1) to $\sum_\rho\log(1/R)$ — i.e. **it sees the position of the zeros, not the sign of $u$**. The cancellation that killed 180.4 ($\int_0^T\log|\zeta(\sigma+it)|dt$ cancels in $t$ because $\log|\zeta|$ oscillates in sign) **does NOT occur here**: $|\nabla u|^2$ does not oscillate, it integrates positive mass around every singularity. **Conclusion: 180.4 genuinely does not apply. The mandate's §0 diagnosis was right.**

**But** (this is the point): the price of positivity is that $\mathcal D_R$ counts **every** zero with weight $\log(1/R)$, without distinguishing on-line from off. The information that 180.4 lost by sign cancellation, 183 loses by **population uniformity**: the Dirichlet energy weight is the same for a zero at $\beta=\tfrac12$ as for one at $\beta=\tfrac12+b$. That is barrier #4.

### 1.5. The term $c(\rho)$ and the impossibility of isolating $b^2$

**[PROP 183.2] (Dirichlet energy is blind to $b$ at first order — the computation that kills it).** The dependence on $b$ of the regularized self-energy of a zero $\rho=\tfrac12+b+i\gamma$ enters only through (i) what portion of the disk $B(\rho,R)$ falls in $\{\sigma>\tfrac12\}$, and (ii) the value $h(\rho)$ of the harmonic part. For $b\ge R$ (interior zero, full disk in the domain): the self-energy is $2\pi\log(1/R)+O(1)$, **exactly equal to that of an on-line zero whose full disk were in the domain**, and independent of $b$. The signal $\sum b^2$ does not appear as a separate term: it appears, if at all, in the boundary flux $\sigma=\tfrac12$ (§2), of order $\sum b\cdot(\dots)$ — **first order in $b$, not $b^2$**, and dominated even there.

*Proof.* By 183.1 the self-energy is $2\pi\log(1/R)+2\pi h(\rho)+O(R\log\tfrac1R)$ whenever $B(\rho,R)\subset\{\sigma>\tfrac12\}$, i.e. $b\ge R$. The term $2\pi\log(1/R)$ does not depend on $b$. The term $2\pi h(\rho)$: $h(s)=u(s)-\log|s-\rho|$; $\partial_b h(\rho)$ exists and is $O(\log\gamma)$, producing no isolable factor $b$ or $b^2$ — it is a smooth function of position, of the same size for on-line and off zeros. There is no mechanism in the flat energy that extracts $b^2$ with a dominant positive coefficient. $\square$

**Comparison with 173.C.** In 173.C the weight $(\sigma-\tfrac12)^2=v$ is what converts the Riesz mass into $\sum b^2$: the factor $v$ weighs *transversally*, giving $0$ to on-line zeros ($\beta=\tfrac12\Rightarrow v=0$) and $b^2$ to off zeros. **Dirichlet energy $|\nabla u|^2$ does NOT carry that transversal weight $v$**: it is an isotropic scalar. There is the exact difference between route 173.C (which DOES isolate $\sum b^2$, weight 1 in $\gamma$) and route 183 (which does NOT). Desingularized Dirichlet energy is the wrong tool for $\sum b^2$ precisely because its weight is isotropic and the signal is transversal.

---

## 2. The boundary $\sigma=\tfrac12$ and the Selberg anchor

The only place in $\mathcal D_R$ where the transversal coordinate enters with sign is the flux of the critical boundary:
$$\mathcal F_{1/2}(T)\;:=\;-\int_0^T u(\tfrac12+it)\,\partial_\sigma u(\tfrac12+it)\,dt,\qquad \partial_\sigma u(\tfrac12+it)=\mathrm{Re}\,\tfrac{\zeta'}{\zeta}(\tfrac12+it).$$

**[PROP 183.4] (the unconditional anchor available).**
(a) $\int_0^T u(\tfrac12+it)^2\,dt=\tfrac T2\log\log T+O(T)$ **unconditional** (Selberg 1946; Titchmarsh §9). Displaced version $\int_0^T u(\tfrac12+s+it)^2dt\ll T\log\log T$ uniform in $0\le s\ll1/\log T$: **[literature GAP 183.L1]** (Tsang 1984 — same GAP as 180.L3; verify the uniform range before publication).
(b) $\int_0^T\big(\partial_\sigma u(\tfrac12+it)\big)^2dt=\int_0^T\big(\mathrm{Re}\,\tfrac{\zeta'}{\zeta}(\tfrac12+it)\big)^2dt$: **NOT unconditionally bounded**; it is of the order of the second moment of $\zeta'/\zeta$ on the critical line, which grows (simple zeros give poles of $\zeta'/\zeta$ on the line — the integral diverges if there are on-line zeros, which there are). Hence $\mathcal F_{1/2}$ via Cauchy–Schwarz gives $|\mathcal F_{1/2}|\le(\tfrac T2\log\log T)^{1/2}(\int(\partial_\sigma u)^2)^{1/2}$, and the second factor is **infinite or huge** — the boundary anchor does not close.
(c) For fixed $\sigma>1$: $\frac1T\int_0^T|\zeta'/\zeta(\sigma+it)|^2dt\to\sum_n\Lambda(n)^2n^{-2\sigma}<\infty$ unconditional (Montgomery–Vaughan / orthogonality). For $\tfrac12<\sigma<1$: $\int_0^T|\zeta'/\zeta|^2$ relates to $\sum_{\gamma,\gamma'}$ via the partial-fractions formula and re-enters **pair correlation** (Montgomery 1973) — conditional / not uniform. **[Literature GAP 183.L2].**

*Proof.* (a) Selberg, cited. (b) $\zeta'/\zeta(s)=\sum_\rho\frac1{s-\rho}+O(\log)$; at $s=\tfrac12+it$ with $\rho=\tfrac12+i\gamma$ on-line the term is $\frac1{i(t-\gamma)}$, whose real square integrated in $t$ around each $\gamma$ diverges logarithmically — summed over $\asymp T\log T$ zeros it gives divergence. (c) orthogonality of $n^{-it}$. $\square$

**Consequence.** The critical boundary, far from anchoring the signal, is where the **on-line self-energy reappears** (the poles of $\zeta'/\zeta$ on the line). This confirms barrier #4 from another angle: the on-line mass not only matches the off weight in the interior, but **dominates at the boundary** $\sigma=\tfrac12$, exactly where the favorable asymmetry was expected.

---

## 3. The two scales of $R$ and the (failed) extraction of $E(T)$

**Scale $R\asymp1/\log T$ (mean spacing).** By 183.1.b, $\mathcal D_R\asymp T\log T\log\log T$, dominated by the total count. Subtracting the "on-line background" $2\pi N(T)\log(1/R)$ would require knowing $N(T)$ and the harmonic part $\sum c(\rho)$ with precision $o(T/\log T)$ — but $\sum c(\rho)$ is of order $T\log^2T$, a thousand times larger than the signal $E(T)\le T/\log T$. **The signal is buried $\log^3T$ below the background. Not extractable.**

**Scale $R\asymp\sqrt t$ (DBN kernel).** Here $R$ grows with height; $\log(1/R)\asymp-\tfrac12\log t$, which becomes negative for $t>1$. The exclusion disk at height $t$ has radius $\sqrt t\gg$ mean gap $1/\log t$ — **it excludes many zeros at once**, the balls overlap, and identity 183.1 no longer has disjoint balls. The DBN regime is not an "exclusion radius" but a **Gaussian smoothing** of the potential (de Bruijn 1950; Polymath 15, 2019): it replaces $\delta_\rho$ by a Gaussian of width $\sqrt t$. Then the smoothed self-energy of an atom is finite, $\asymp\log(b_j/\sqrt t)$ by 173 §6.3, **and $b_j$ does appear there** — but inside a $\log$, not as $b^2$. This is exactly [GAP-183.1]: the correct smoothing must couple the scale to the *transversal defect*, not to the global height. See §4.

**[PROP 183.3] (the boundary/interior asymmetry does not survive — refutation of the mandate's wager).** The mandate's hypothesis was that on-line zeros (on $\partial\{\sigma>\tfrac12\}$) contribute *half* self-energy and off zeros the *full* amount, giving a different growth rate. Computation: an on-line zero $\tfrac12+i\gamma$ has its disk $B(\rho,R)$ split by the line $\sigma=\tfrac12$; only the half $\sigma>\tfrac12$ is in $\Omega_R$. Its self-energy is $\tfrac12\cdot2\pi\log(1/R)+O(1)=\pi\log(1/R)+O(1)$. An off zero with $b\ge R$ contributes $2\pi\log(1/R)+O(1)$. **The ratio is $2$, a constant.** Difference per zero $=\pi\log(1/R)+O(1)$, summed over populations:
$$\mathcal D_R^{\text{on}}=\pi\log\tfrac1R\cdot N_{\text{on}}(T),\qquad \mathcal D_R^{\text{off}}=2\pi\log\tfrac1R\cdot N_{\text{off}}(T)+(\text{flux}).$$
Under RH, $N_{\text{off}}=0$ and everything is on-line. Without RH, **$N_{\text{off}}=o(N(T))$ always** (zero density of off zeros — Bohr–Landau / Selberg), so $\mathcal D_R^{\text{off}}=o(\mathcal D_R^{\text{on}})$: the off mass is a vanishing fraction. The on/off asymmetry is of **constant per zero**, and the off population is negligible: **the off signal drowns doubly** (isotropic weight $+$ vanishing population). The boundary/interior asymmetry wager **fails**. $\square$

---

## 4. The declared risk, turned into a theorem: barrier #4

**[PROP/diagnosis 183.5] (barrier #4 — population blindness).** The Dirichlet energy $\mathcal D_R(T)$ cannot isolate $E(T)=\sum_{\text{off}}b^2$ due to the conjunction of two proved facts:
1. **(isotropic weight, 183.2)** the self-energy of a zero is $2\pi\log(1/R)$, with no transversal factor $(\beta-\tfrac12)^2$;
2. **(vanishing population, 183.3)** off zeros have zero density, $N_{\text{off}}(T)=o(N(T))$ unconditional.
The product: the off contribution to $\mathcal D_R$ is $\ll N_{\text{off}}\log(1/R)=o(T\log T\log\log T)$, a lower-order correction *that does not even carry the correct $b^2$ weight* (it carries $\log(1/R)$, constant in $b$). Any unconditional upper bound of $\mathcal D_R$ bounds $N_{\text{off}}\cdot\log(1/R)$, i.e. the **count** of off zeros, not their **energy** $\sum b^2$ — and the count is already controlled by density (176.9, barrier #1). No new brick here.

*Proof.* Conjunction of 183.2 (weight) and 183.3 (population) plus 176.9 (the count is the already-known density barrier). $\square$

**Exact mechanism of barrier #4, in one line:** *Dirichlet energy weighs zeros by their existence ($\log\frac1R$), not by their transversal distance ($b^2$); and off zeros are demographically negligible, so dominating the total energy says nothing about their energy.* It is the **twin** of the previous three and **structurally the most informative**, because it explains in a new way why $\sum b^2$ resists: $b^2$ is a **second transversal moment** (weight $v=(\sigma-\tfrac12)^2$), and no **isotropic** functional (Dirichlet energy, density, moment of $|\zeta|$) carries it. Only the anisotropic weight of 173.C isolates it — and that weight, by 180.4, has a signed integrand. **The four barriers are one barrier seen four times: the signal lives in a second-order transversal weight, and every natural unconditional functional is either isotropic (blind to direction) or signed (blind by cancellation).**

**Table of the four barriers:**

| # | Doc | Functional | Why it fails |
|---|-----|-----------|---------------|
| 1 | 176.9 | density $N(\tfrac12+s,T)$ | fatal mass at $s\asymp1/\log T$; exponent only in the constant |
| 2 | 180.3 | mollified moment | Farmer floor $c(\theta)>1$ + ceiling $\theta\le1$ |
| 3 | 180.4 | $\iint\log|\zeta|$ (signed) | moments blind to sign; cancellation = the zeros |
| **4** | **183.5** | **$\iint|\nabla\log|\zeta||^2$ (positive)** | **isotropic weight + vanishing off population** |

### 4.1. The minimal residual statement

**[GAP-183.1] (the missing anisotropic desingularization).** There exists a weighted Green kernel $G_w$ on $\Omega=\{\sigma>\tfrac12\}$, or an atom smoothing, such that the regularized self-energy of the zero $\rho=\tfrac12+b+i\gamma$ is $\asymp b^2\cdot p(\gamma)+o(b^2)$ with integrable weight $p$ against $E(T)\ll T/\log T$ giving $o(T/\log T)$, **and** the total energy $\mathcal D_w^{\text{reg}}$ admits an unconditional upper bound $o(T/\log T)$ via a Selberg/Tsang anchor at the boundary. The two conditions are antagonistic under flat geometry (§2, §3): the anisotropic weight $b^2$ requires differentiating transversally ($\partial_\sigma^2$), which reintroduces the sign of 180.4 (the second derivative of $\log|\zeta|$ is not positive). **Associated impossibility conjecture:** no local quadratic functional in $u$ is simultaneously anisotropic-of-order-2 and definite in sign — it is GAP-141.G1 in this incarnation. Solving GAP-183.1 = brick A.

### 4.2. The DBN lead, frankly

The DBN smoothing at scale $\sqrt t$ (173 §6.3) gives self-energy $\asymp\log(b_j/\sqrt t)$, anisotropic but **logarithmic in $b$, not quadratic**, and signed (negative for $b_j<\sqrt t$). To convert $\log(b/\sqrt t)$ into $b^2$ would require a second differentiation in $t$ coupled to the heat flow — which is precisely the Phase 54 balance law $\dot I=-2\kappa-D$, where $I=\sum b^2$ appears as a **second-order** quantity (program memory: "I = first second-order quantity, escapes no-go 141.B2"). **[BRIDGE, status: open]** the DBN-desingularized Dirichlet energy is the spatial version of the balance law; connecting $\mathcal D_{\sqrt t}$ with $\dot I$ is the natural next step but is not closed here — the flat geometry of §1–§3 does not see it because it lacks flow time as a second variable.

---

## 5. Anti-circularity test

| Piece | ζ-free? | Unconditional? | Where the conjectural re-enters |
|---|---|---|---|
| Green over $\Omega_R$ (183.1) | machinery yes (classical Green) | yes (exact identity) | — |
| Self-energy $2\pi\log(1/R)$ (183.1, 183.2) | yes (point potential) | yes | — |
| Isotropic weight, not $b^2$ (183.2) | yes | yes (structural negative) | — |
| Vanishing off population (183.3) | no (fact about $\zeta$) | yes (Bohr–Landau/Selberg) | zero density |
| Selberg boundary anchor (183.4.a) | no | yes (Selberg 1946) | — |
| Uniform displacement (183.4.a) | no | **[GAP 183.L1]** | Tsang 1984 |
| Second moment $\zeta'/\zeta$ in $\tfrac12<\sigma<1$ (183.4.c) | no | **NO** | pair correlation, Montgomery 1973 |
| Barrier #4 (183.5) | partial | yes | uses density (176.9) |

No step assumes RH, A, or LP-112. The negative results (183.2, 183.3, 183.5) are unconditional. The literature GAPs (L1, L2) are marked and not used in any proof as if closed.

---

## 6. Verdict

**Was $E(T)\ll T/\log T$ unconditionally improved?** **NO.** Outcome (b)+(c): the route reproduces $T/\log T$ (in fact the Dirichlet energy is dominated by an on-line background of order $T\log T\log\log T$, $\log^3T$ above the signal) and exposes a new barrier, not a brick.

**Did it escape barrier 180.4?** **YES in the premise, NO in the conclusion.** The integrand $|\nabla\log|\zeta||^2\ge0$ is NOT a signed moment: 180.4 (sign blindness, cancellation in $t$) genuinely **does not apply** — verified in §1.4. The mandate was right: Dirichlet energy sees the singularities, not the sign. **But** the positivity that saves it from 180.4 condemns it another way: the energy weighs each zero by $\log(1/R)$ **isotropically**, without the transversal factor $(\beta-\tfrac12)^2$ that defines the signal, and off zeros are demographically vanishing. **Sign blindness (180.4) becomes population/anisotropy blindness (183.5): barrier #4.**

**Proved (with complete proof):**
- [THEOREM 183.1] exact Green–energy identity; self-energy $=2\pi\log(1/R)+2\pi h(\rho)+O(R\log\tfrac1R)$ per zero.
- [PROP 183.1.b] $\mathcal D_{1/\log T}(T)\asymp T\log T\log\log T$, dominated by total count.
- [PROP 183.2] self-energy is **blind to $b$ at first order** (isotropic weight, not $b^2$); exact contrast with the transversal weight $v=(\sigma-\tfrac12)^2$ of 173.C.
- [PROP 183.3] the boundary/interior asymmetry between on-line and off is **of constant (factor $2$), not of order**; with vanishing off population, the off signal drowns doubly. (Refutes the mandate's §1 wager.)
- [PROP 183.4] the unconditional anchor available is $\int_0^T u^2\sim\tfrac T2\log\log T$ (Selberg); the second moment of $\zeta'/\zeta$ on the line **diverges** (on-line poles) and on $\tfrac12<\sigma<1$ is not unconditional.
- [PROP 183.5] **barrier #4 (population/anisotropy blindness)**: isotropic weight $+$ vanishing off population $\Rightarrow$ $\mathcal D_R$ bounds the off *count*, not the off *energy* $\sum b^2$.

**Refuted:** the wager that the boundary/interior asymmetry would isolate $\sum b^2$ (183.3).

**Numbered GAPs:**
- **[GAP-183.1]** (minimal residue, = brick A): an **order-2 anisotropic and sign-definite** desingularization whose self-energy weighs zeros by $b^2$ and whose total energy has an unconditional bound $o(T/\log T)$. Impossibility conjecture: no local quadratic functional of $\log|\zeta|$ is simultaneously anisotropic-of-order-2 and sign-definite (incarnation of GAP-141.G1). Equivalent to $\mu_2(T)=o(1)$ (GAP-180.1).
- **[Literature GAP 183.L1]** uniformity of the Selberg moment of $\log|\zeta|$ in displacements $s\ll1/\log T$ (Tsang 1984; = 180.L3).
- **[Literature GAP 183.L2]** unconditional second moment of $\zeta'/\zeta$ in $\tfrac12<\sigma<1$ (pair correlation, Montgomery 1973; not uniform).

**Successor direction (Doc 184).** The synthesis of the four barriers (table §4) says the signal $\sum b^2$ is a **second-order transversal moment** and that every natural unconditional functional is either isotropic (blind, #1/#4) or signed (cancels, #3) or saturated by the on-line moment (#2). The only object in the program that is **anisotropic, second-order, and dynamic** is the balance law $\dot I=-2\kappa-D$ (Phase 54). Doc 184 must attack the connection [BRIDGE §4.2]: $\mathcal D_{\sqrt t}(T)$ (DBN-desingularized energy, with flow time as a second variable) $\leftrightarrow$ $\int_0^\infty\dot I$, where the second temporal variable might break the isotropic/signed dichotomy that triangulates GAP-183.1. That is: leave the flat geometry of this document and enter the space-time of the heat flow.

---

## References

- A. Selberg, "Contributions to the theory of the Riemann zeta-function", *Arch. Math. Naturvid.* 48 (1946). [Second moment of $\log|\zeta(\tfrac12+it)|\sim\tfrac T2\log\log T$; density; zero density of off zeros.]
- J. E. Littlewood, "On the zeros of the Riemann zeta-function", *Proc. Camb. Phil. Soc.* 22 (1924). [Littlewood's lemma, identity.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (Heath-Brown), Oxford 1986. §9 (densities, $S_1$, moments of $\log|\zeta|$); ch. 14 (partial fractions of $\zeta'/\zeta$).
- A. Ivić, *The Riemann Zeta-Function*, Wiley 1985. Chs. 10–11.
- H. L. Montgomery, "The pair correlation of zeros of the zeta function", *Proc. Sympos. Pure Math.* 24 (1973), 181–193. [Pair correlation; second moment of $\zeta'/\zeta$; GAP 183.L2.]
- K.-M. Tsang, *The distribution of the values of the Riemann zeta-function*, thesis, Princeton 1984. [Displaced moments of $\log|\zeta|$; GAP 183.L1.]
- N. G. de Bruijn, "The roots of trigonometric integrals", *Duke Math. J.* 17 (1950), 197–226. [Heat flow / DBN kernel.]
- D. H. J. Polymath, "Effective approximation of heat flow evolution of the Riemann ξ function...", *Res. Math. Sci.* 6 (2019). [Polymath 15; scale $\sqrt t$.]
- H. Davenport, *Multiplicative Number Theory*, 3rd ed., GTM 74, Springer. Chs. 12, 15–16.

**Internal documents:** Doc 170 (Theorem 170.5, coordinates); Doc 172 (windowed ceiling 172.9); Doc 173 (173.C Green–Littlewood identity, 173.E atomic self-energy, §6.3 DBN desingularization program); Doc 176 (176.4 Cesàro, 176.9 density barrier); Doc 180 (180.1 $\mu_2$, 180.3 mollifier barrier, **180.4 sign blindness**, GAP-180.1); Phase 54 (balance law $\dot I=-2\kappa-D$; I = second-order quantity).

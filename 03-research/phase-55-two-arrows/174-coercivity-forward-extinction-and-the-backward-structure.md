# Document 174 — Coercivity, forward extinction and the backward structure of rigidity

**Program:** Riemann Hypothesis — Phase 55 (two arrows)
**Mandate:** Problem B of the director via the dynamical route: coercivity (B2), backward flow, collision budget (B3), Lyapunov/moments (B1). Do NOT audit; construct. Do NOT prove RH.
**Prerequisites (certified, not re-derived):** Doc 167 (balance law $\dot I=-2\kappa-D$, $D\ge0$; Thm 2.3 CERTIFIED by Doc 168), Doc 168 (repairs: single chart, Cor 2.5 conditional, gift lemma $H_t|_{i\mathbb R}>0$), Doc 170 (envelope $E(T)\ll T/\log T$; rate/total no-go, Thm 170.8), Doc 144 (Hadamard counterexample $m=\infty$, $I<\infty$).
**Contract:** [NEW-DEFINITION] free; [THEOREM]/[PROP]/[LEMMA] complete proof or no label; [BRIDGE] frank; [GAP] declared.

---

## 0. Single chart and conventions (fulfilling repair 2 of Doc 168)

**Chart $H_t$ (Polymath 15) throughout the document.** $H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du$, $\partial_tH_t=-\partial_z^2H_t$, $H_0=\tfrac18\Xi(\cdot/2)$. Zeros of $H_0$ = zeros of $\Xi$ dilated by 2: band $|\mathrm{Im}\,z|<1$ (strict, Hadamard–de la Vallée Poussin), density $N(T)=\frac{T}{2\pi}\log\frac{T}{4\pi e}+O(\log T)$. Conversion to the ζ chart: $b_\zeta=\beta/2$, $\tau_\zeta=t/4$; the balance law is scale-invariant (Doc 168 §2), the constants are not — all constants in this document are in the $H_t$ chart, and at the end of each relevant statement the ζ version is given.

Upper zeros $z_k=\alpha_k+i\beta_k$, $\beta_k>0$; $\kappa(t)=\#$upper zeros; $I(t)=\sum_k\beta_k^2$; $M(t)=\max_k\beta_k^2$ (when $\kappa<\infty$). Certified law (Thm 167-2.3): on intervals with $\kappa<\infty$ constant and simple zeros,
$$\dot I=-2\kappa-D,\qquad D\ge0\ \text{explicit, term by term}.$$
Hard inputs: [dB] de Bruijn 1950; [N] Newman 1976; [CSV] Csordas–Smith–Varga 1994; [KKL] Ki–Kim–Lee 2009 ($\forall t>0$: finitely many non-real zeros); [RT] Rodgers–Tao 2020 ($\Lambda\ge0$); [P15] Polymath 2019. Gift lemma (Doc 168 §3.3): $H_t(i\beta)>0$ for all $t,\beta$ ⟹ the imaginary axis is never touched ⟹ parity $\kappa\in2\mathbb Z$ sealed throughout the flow, $\kappa\ge2$ while $\kappa>0$.

**Structural fact that governs the whole document (not to be lost):** "$0<I(0)<\infty$ impossible" is **FALSE** in the general Pólya class — there exists a function of the class with a single off quadruple (e.g. $(z^2-w)(z^2-\bar w)e^{-z^2/N}$-type, or the Hadamard counterexample of Doc 144 with a single factor). Any proof of arrow B must use the arithmetic initial condition of ζ. This document builds the map of WHICH dynamical property can carry it and WHICH routes remain closed.

---

## 1. The forward map (B2): coercivity, resolved frankly

### 1.1. $D\ge cI$ is FALSE — the exact counterexample

**[PROP 174.1] (non-coercivity of the dissipation).** For the configuration of an isolated quadruple $\{z_1,\bar z_1,-z_1,-\bar z_1\}$, $z_1=\alpha+i\beta$ (no real zeros), the dissipation of the balance law is exactly
$$D=\frac{4\beta^2}{\alpha^2+\beta^2},\qquad I=2\beta^2,\qquad \frac{D}{I}=\frac{2}{\alpha^2+\beta^2}\;\xrightarrow{\alpha\to\infty}\;0.$$
There is no $c>0$ with $D\ge cI$ in the class.

*Proof.* From the dynamics: for $z_1$, the neighbors are $\bar z_1$ (conjugate: contributes the universal $-2$), $-\bar z_1$ (mirror: contributes $0$), $-z_1$ (antipode). $\dot\beta_1=-2\bigl[\tfrac{2\beta}{4\beta^2}+\tfrac{2\beta}{4|z_1|^2}\bigr]=-\tfrac1\beta-\tfrac{\beta}{|z_1|^2}$. With two upper zeros ($z_1$ and $-\bar z_1$, same height): $\dot I=4\beta\dot\beta_1=-4-\tfrac{4\beta^2}{|z_1|^2}$. Since $-2\kappa=-4$, we get $D=4\beta^2/|z_1|^2$. The cross terms $(\beta_k-\beta_l)^2$ of the formula of Thm 167-2.3 vanish (equal heights) and the $(\beta_k+\beta_l)^2$ reproduce exactly the antipode term — consistency verified. $\square$

**Reading.** The quadruple alone barely dissipates through interaction: $D\to0$ at large height. The coercivity of the *dissipation* is false. **But question B2 was ill-posed in the variable $D$:** the rate that matters is not $D$ but the quantized term $-2\kappa$, which is *stronger than coercive*:

### 1.2. Coercivity restored by quantization + band

**[THEOREM 174.2] (exponential coercivity without $D$).** Let $J\subset(0,\infty)$ be an interval with $\kappa<\infty$ and simple zeros a.e. (true for every $t>0$ except for locally finite collisions, [KKL] + repair 5 of Doc 168). Then on $J$:
$$\dot I\;\le\;-\frac{2I}{M(t)}\;\le\;-2I,$$
and consequently $I(t)\le I(t_0)\,e^{-2(t-t_0)}$ and, using $M(t)\le M(t_0)-2(t-t_0)$ (Lemma 174.3 below),
$$I(t)\;\le\;I(t_0)\Bigl(1-\frac{2(t-t_0)}{M(t_0)}\Bigr)_+\qquad\text{(exact linear extinction at } t_0+M(t_0)/2\text{)}.$$

*Proof.* $I=\sum\beta_k^2\le\kappa\cdot\max\beta_k^2=\kappa M$, hence $-2\kappa\le-2I/M$; and $M(t)<1$ for $t\ge0$ (strict band at $t=0$, non-increasing by Lemma 174.3). $\dot I\le-2\kappa-0\le-2I/M\le-2I$. Integrating $\dot I\le-2I/(M_0-2(t-t_0))$ gives $\log I\le\log I_0+\log\frac{M_0-2(t-t_0)}{M_0}$. $\square$

**Resolution of B2, stated plainly:** the Lyapunov inequality $\dot L\le-cL$ with $L\ge cI$ **exists and is $L=I$ itself, with $c=2$** — but the coercivity does NOT come from the interaction dissipation $D$ (false, Prop 174.1), but from the product of two facts: (i) each mode dissipates at exact constant rate $2$ (quantization, Thm 167-2.3), (ii) each mode carries energy $<M\le1$ (band). *Constant dissipation per mode + bounded energy per mode ⟹ exponential rate.* In the ζ chart: $\dot I_\zeta\le-2I_\zeta/M_\zeta$ with $M_\zeta<1/4$, i.e. $\dot I_\zeta\le-8I_\zeta$ in ζ time.

### 1.3. The maximum principle of the dynamics (the de Bruijn band from the particles)

**[LEMMA 174.3] (maximum principle; = Thm 13 of [dB], new proof via dynamics).** On an interval with $\kappa<\infty$ and simple zeros, $M(t)=\max_k\beta_k(t)^2$ satisfies $D^+M\le-2$. In particular $M(t)\le M(t_0)-2(t-t_0)$ and every upper zero lands before $t_0+M(t_0)/2$.

*Proof.* $M$ is the maximum of finitely many smooth functions, hence Lipschitz, with $D^+M=\max\{2\beta_k\dot\beta_k:\beta_k^2=M\}$. For $k$ with $\beta_k$ maximal, in the decomposition of $\dot\beta_k$ (proof of Thm 167-2.3): the own conjugate gives exactly $-2$ to $2\beta_k\dot\beta_k$; the antipode and the real zeros give $\le0$; the terms with other upper zeros enter as $-4\beta_k(\beta_k-\beta_l)/d^2$ (with $w\in\{z_l,-\bar z_l\}$, $\mathrm{Im}\,w=\beta_l$) and $-4\beta_k(\beta_k+\beta_l)/d^2$ (with $w\in\{\bar z_l,-z_l\}$): **for the maximal one, $\beta_k-\beta_l\ge0$ and $\beta_k+\beta_l>0$, all $\le0$ with no need to symmetrize.** Total sum $\le-2$. Convergence: $\kappa<\infty$ + RvM, as in Thm 167-2.3. $\square$

*Literature frankness:* the statement is de Bruijn's 1950 decreasing-band theorem (Thm 13: zeros in $|\mathrm{Im}|\le\Delta$ ⟹ in $|\mathrm{Im}|\le\sqrt{\Delta^2-2t}$); what is new is only the proof via the particle system, which moreover localizes it (it holds zero by zero for the current maximum, not only for the global sup of the class).

### 1.4. The exact landing time of the isolated quadruple (the director's question, closed)

**[THEOREM 174.4] (closed model of the quadruple: exact solution).** The system of 4 zeros $\{\pm z_1,\pm\bar z_1\}$ under $\dot z_k=2\sum_{j\ne k}1/(z_k-z_j)$ is exactly the backward heat flow on $H_t(z)=z^4+a(t)z^2+c(t)$, with $\dot a=-12$, $\dot c=-2a$. In the variable $w:=z_1^2$ ($\mathrm{Re}\,w=\alpha^2-\beta^2$, $\mathrm{Im}\,w=2\alpha\beta$):
$$\frac{d}{dt}\mathrm{Re}\,w=6,\qquad \frac{d}{dt}(\mathrm{Im}\,w)^2=-8\mathrm{Re}\,w,$$
so $(\mathrm{Im}\,w)^2(t)=(\mathrm{Im}\,w_0)^2-8\mathrm{Re}\,w_0\,t-24t^2$ and landing (double real zero at $\pm\sqrt{\mathrm{Re}\,w(t_c)}$, simultaneous by parity — the normal form of Thm 167-1.4(2) realized) occurs at
$$\boxed{\;t_c\;=\;\frac{-\mathrm{Re}\,w_0+\sqrt{(\mathrm{Re}\,w_0)^2+\tfrac32(\mathrm{Im}\,w_0)^2}}{6}\;=\;\frac{\beta_0^2}{2}-\frac{\beta_0^4}{4\alpha_0^2}+O\Bigl(\frac{\beta_0^6}{\alpha_0^4}\Bigr)\quad(\alpha_0\gg\beta_0).\;}$$

*Proof.* For a monic polynomial, $\dot z_k=H''/H'(z_k)=2\sum_{j\ne k}(z_k-z_j)^{-1}$ ⟺ $\partial_tH=-\partial_z^2H$ (degree 4: $\partial_z^2H=12z^2+2a$, so $\dot a=-12$, $\dot c=-2a$). $w,\bar w$ are the roots of $X^2+aX+c$: $\mathrm{Re}\,w=-a/2$, $(\mathrm{Im}\,w)^2=c-a^2/4$; differentiate. Landing is $\mathrm{Im}\,w=0$ (the two $w$'s collide at $\mathrm{Re}\,w(t_c)>0$ and $z^2=\mathrm{Re}\,w$ gives the two real doubles $\pm x_0$). Expansion: $\sqrt{R^2+6\alpha^2\beta^2}$ with $R=\alpha^2-\beta^2$. **Cross-check against the certified law:** from the model, $I=2\beta^2=|w|-\mathrm{Re}\,w$ and $\dot I=2\mathrm{Re}\,w/|w|-6=-4-4\beta^2/|z_1|^2$ — matches Prop 174.1 exactly. $\square$

**Answer to "is $t_{\rm landing}=b^2/4$ exact?": NO — it is $\beta_0^2/2$, not $\beta_0^2/4$.** For the isolated conjugate pair ($H=z^2+c_0-2t$, the model of Doc 168 §1): $t_c=\beta_0^2/2$ **exact**. For the quadruple: $t_c=\beta_0^2/2$ only asymptotically ($\alpha\gg\beta$), with **negative** correction $-\beta_0^4/4\alpha_0^2$ (the intra-quadruple interaction accelerates landing, consistent with $D>0$). The correct invariant form is $t_c=I_0/(2\kappa)\cdot(1+o(1))=I_0/4$ per quadruple: the director's "$b^2/4$" statement is correct **if $b^2$ denotes the total energy of the quadruple $I_0=2\beta_0^2$**, and is false by a factor of 2 if it denotes the squared height. In the ζ chart: $\tau_c=b_\zeta^2/2$ — the same $1/2$, by scale invariance.

### 1.5. The forward structure theorem

**[THEOREM 174.5] (universal forward extinction; where RH lives).** For every $t_0>0$, unconditionally:
1. $\kappa(t_0)<\infty$, $I(t_0)<\infty$ [KKL], and while $\kappa>0$: $\dot I\le-2\kappa\le-4$ (parity sealed by the gift lemma) **and** $\dot I\le-2I$ (Thm 174.2): the dissipation is constant-per-mode AND exponential at the same time.
2. Finite-time extinction: $\Lambda\le t_0+\min\bigl\{\tfrac14I(t_0),\;\tfrac12M(t_0)\bigr\}$ (Cor 167-2.4 repaired + Lemma 174.3), and each individual quadruple lands in time $\lesssim\beta^2/2$ (Thm 174.4; clusters land even sooner, §3.2).
3. **Forward, EVERYTHING dies, with explicit rates and no arithmetic hypothesis.** The only information the ¬RH scenario can carry is the boundary condition at $t\to0^+$: the value $I(0^+)\in[0,\infty]$ and $\kappa(0^+)\in\{0,2,4,\dots,\infty\}$. **The RH question lives entirely at $t=0$ and at $t=0^-$; the half-axis $t>0$ is trivial modulo [KKL].**

*Proof.* (1)–(2): combination of what has already been proved; the continuity of $I$ across collisions is that of Cor 167-2.4 (audited). (3) is the reading of (1)–(2) + Prop 167-3.2 (finiteness as a boundary condition). $\square$

**Conceptual consequence (the course correction of this phase):** the director's "rigidity" is NOT a forward stability problem — forward there is universal overstability (finite-time extinction, quantized rate, no coercivity left to prove because it is already there). The problem is one of **backward uniqueness/classification of the initial data**: which initial conditions are reachable by arithmetic. The rest of the document attacks that.

---

## 2. The backward front: takeoffs, the missing invariant, and where arithmetic enters

### 2.1. Certified status of the $t<0$ side

The only thing proved (post-audit 168): **conditional on** $\kappa<\infty$ and simple zeros a.e. on $(t,0)$,
$$I(t)\;\ge\;I(0^+)+4|t|,\qquad\text{and (Thm 174.2 read backward, if moreover }M\le\bar M\text{ on }(t,0)\text{)}\quad I(t)\;\ge\;I(0^+)\,e^{2|t|/\bar M}.$$
The unconditional version is NOT proved (partial KILL of Doc 168: the case $I<\infty$, $\kappa=\infty$ on $(t,0)$ falls outside Thm 167-2.3). [RT] gives $\kappa(t)>0$ for all $t<0$; the gift lemma gives $\kappa(t)\ge2$.

### 2.2. The structure of takeoffs: the inverted closed model and the lattice fixed point

**[CALCULATION 174.6] (takeoff time of the isolated pair).** Time-reversal of the pair model: a pair of real zeros with gap $g$ at $t=0$, isolated, originates from a complex pair that landed at $t_c=-g^2/8$: in $H=z^2+c_0-2t$ with $c_0=-g^2/4$, the zeros are real $\pm\sqrt{2t+g^2/4}$ for $t>-g^2/8$ and complex before. **Backward, takeoffs occur at small gaps with takeoff time $\asymp g^2$** — the fold normal form (Prop 167-1.6/2.6) read backward. [CSV] is the rigorous arithmetic version of this at $t=0$: a Lehmer pair (near-collision) forces $\Lambda\ge$ a bound — i.e. *recent takeoff*.

**[PROP 174.7] (the perfect lattice is a fixed point: density does NOT buy takeoffs).** $H(z)=\cos z$ evolves as $H_t=e^{t}\cos z$: the zeros do not move and $\kappa(t)\equiv0$ for **all** $t\in\mathbb R$, backward included.

*Proof.* $\partial_t(e^t\cos z)=e^t\cos z=-\partial_z^2(e^t\cos z)$. Equivalently from the particles: on the lattice $\{\pi(k+\tfrac12)\}$ the symmetrized sum $\sum'1/(x_k-x_j)$ cancels by symmetry: $\dot x_k=0$. $\square$

**Reading — the arithmetic bridge, precisely localized.** A configuration with RvM density but *perfectly regular* gaps never takes off: backward it can remain real forever. Backward takeoffs are bought exclusively with **gap fluctuations**. For ζ, fluctuations are an unconditional fact (Gaussian moments of $S(t)$, Selberg 1946 — blocks with excess zeros exist, so gaps strictly below the mean occur infinitely often), and their fine statistics (density $\sim\delta^3$ of normalized gaps $\le\delta$) is the GUE prediction, conditional ([M73]); the existence of infinitely many Lehmer pairs is open. **This is where arithmetic enters the backward flow: through the gap statistics of the $\gamma$'s, not through primes directly** — exactly as the mandate anticipated, and now with the mechanism isolated (Prop 174.7: without fluctuation, no takeoff).

**[GAP-174.C] (the backward dual of KKL).** Is $\kappa(t)=\infty$ for all $t<0$ (for ζ, or under RH)? Heuristic in favor: at fixed time $|t|$, the takeoff threshold $g\lesssim\sqrt{8|t|}$ is *absolute* while the mean gap $4\pi/\log\gamma\to0$: at sufficient height, typical gaps fall below the threshold. Against: Prop 174.7 shows that the mean-density argument is **fallacious** (the lattice does not take off: the isolated-pair model does not apply in the dense regime, where collective repulsion can sustain reality). The statement is genuinely open and is the correct structural question about the half-axis $t<0$: if $\kappa(t)=\infty$ for $t<0$, then the conditional bound $I(t)\ge4|t|$ is vacuous (with $I(t)=\infty$) and all backward information is **local** (by windows). Weaker decidable form: does $\kappa(t)\to\infty$ as $t\to-\infty$?

### 2.3. The separating invariant: what exists, and the exact statement of what is missing

**What distinguishes RH ($I(0)=0$) from ¬RH with $0<I(0)<\infty$, backward:**

**(a) The monotone invariant that DOES exist.** By Lemma 174.3, $\mathfrak B(t):=M(t)+2t$ is non-increasing forward, i.e. **backward $M(t)\ge M(0)+2|t|$**: the maximum height grows at least linearly with universal slope 2. Partial separation: in the ¬RH-finite scenario, $M(t)\ge b_{\max}^2+2|t|$; under RH only $M(t)\ge2|t|$ is guaranteed — the ¬RH scenario carries a persistent **additive surplus $b_{\max}^2$**. This is a genuine comparison invariant but one-sided: separating would require the **upper** bound under RH, and that fails:

**(b) Why the upper bound fails as stated (the cluster calculation).** Backward, a takeoff from a cluster of $k$ simultaneous near-collisions in a window $\ll\beta$ grows as $\dot\beta\approx+k/\beta$ (the $k$ conjugates at distance $\approx2\beta$ add up), i.e. $\beta^2\approx2k|t-t_c|$: the local takeoff slope is $2k$, not $2$, with $k$ unbounded for ζ (the near-collision multiplicity in windows of size $\sqrt{|t|}$ grows with height by RvM). A bound $M(t)\le2|t|(1+o(1))$ under RH is false without cluster control.

**[GAP-174.B] (the missing separating lemma — precise statement).** *Let $Z_0$ be a real configuration (RH) in the class, with RvM density and gap concentration function $\nu(\delta,T):=\#\{n\le N(T):g_n\le\delta\}$. Does there exist $F$, depending only on $\nu$, such that for $t<0$ (where the dynamics is defined) every complex component at time $t$ with ancestor in window $W$ satisfies $\beta(t)^2\le F\bigl(|t|,\;\#\{\text{near-collisions of }Z_0\text{ in }W\text{ at scale }\sqrt{8|t|}\}\bigr)$, with $F(|t|,k)=2k|t|(1+o(1))$?* If such a bound holds, the scenario $0<I(0)<\infty$ is backward-detectable as an **orphan pair**: at times $|t|\ll b_{\max}^2/(2k_{\rm loc})$, the inherited quadruple has a height unreachable from any local census of ancestors (small gaps of the configuration at time $0^+$ after landing). [NEW-DEFINITION: **orphan pair** = a complex pair at time $t<0$ whose forward trajectory does not land in $(t,0]$; ¬RH with $I<\infty$ ⟺ orphans exist at every small $t<0$; RH ⟺ every backward pair has an ancestor (gap) localized with $g\lesssim\sqrt{8|t|}\cdot\sqrt{k}$.]

**(c) The frank verdict on separation: the rate/total wall reappears, now dynamical.** The flow is deterministic in both directions (in the class, the zeros of $H_t$ determine $H_t$ modulo normalization, and the flow is invertible while the dynamics is defined): **backward adds no information — it transports the initial dichotomy.** Any "computable backward invariant that separates" computes, as $t\to0^-$, exactly $I(0)$ — and that is the "signed moment → quadratic moment" wall (Doc 167 §5.1) in another chart. More precisely: what backward does reorganize is *who carries the information*: the **rate** of backward growth (takeoffs, slopes $2k$) is governed by gap statistics — certifiable on average, Doc-170-type envelope — while the **total** (the additive surplus $b_{\max}^2$, the orphans) is exactly the part not separable by averages (Thm 170.8). The rate/total dichotomy of Doc 170 (Coordinate 2) was not an artifact of the explicit formula: **it is a property of the flow.** What survives as a program: GAP-174.B is a pure particle-dynamics statement (ζ-free), decidable in principle, and its arithmetic half (the census of ζ's ancestors) is gap statistics — the correct object for Phase 56.

---

## 3. The collision budget (B3): the budget theorem and the refutation of the weld

### 3.1. The exact budget

**[THEOREM 174.8] (life budget).** Suppose $I(0^+)<\infty$. Let $\{t_j\}$ be the multiset of landing times of the quadruples in $(0,\Lambda]$ and $\ell_j\le t_j$ the lifetime (Lebesgue measure of the set of times $>0$ at which quadruple $j$ is off). Then
$$\sum_j \ell_j\;=\;\tfrac12\int_0^\Lambda\kappa(t)\,dt\;\le\;\tfrac14\,I(0^+)\;<\;\infty.$$
In particular $I(0^+)<\infty\Rightarrow$ the lifetimes are $\ell^1$; and the integrability of $\kappa$ at $0^+$ (Prop 167-3.2.2) is the summability of the lifetimes. False converse a priori: $\int\kappa<\infty$ does not control $\int D$.

*Proof.* $\kappa(t)=\sum_j2\cdot\mathbf 1_{\{j\text{ off at }t\}}$ (each quadruple = 2 upper modes), so $\int_0^\Lambda\kappa=2\sum_j\ell_j$. Integrating the balance law on $(\varepsilon,\Lambda)$ (valid a.e. by [KKL] + local finiteness of collisions, repair 5 of 168; $I$ continuous across collisions): $I(\varepsilon)=\int_\varepsilon^\Lambda(2\kappa+D)\ge2\int_\varepsilon^\Lambda\kappa$; monotone convergence as $\varepsilon\to0^+$. $\square$

**Reading of the two arrows on a single coin:** the arrow "$m<\infty$" is $\kappa\in L^\infty(0^+)$; the arrow "$I(0^+)<\infty$" (GAP 167.A) is $\kappa\in L^1(0^+)$ ⟺ summable lifetimes. The budget converts the $\ell^2$ energy of the heights into an $\ell^1$ budget of times — the exchange currency is the Lehmer exponent 2 ($\ell_j\asymp\beta_j^2$, Thm 174.4).

### 3.2. Interference of sub-resolution quadruples: NO self-obstruction

**[CALCULATION 174.9] (the $\ell^2$ cluster collapses faster, not slower).** $k$ quadruples at heights $\beta_i\approx b$ with horizontal separations $w\ll b$ (sub-resolution cluster): for each zero, the $k$ conjugates (own + neighbors) are at distance $\approx2b$ and add up to
$$\dot\beta\;\approx\;-\frac{1}{\beta}-\;(k-1)\cdot\frac{2b}{4b^2}\;\approx\;-\frac{k+1}{2b}\quad\Rightarrow\quad \frac{d(b^2)}{dt}\approx-(k+1),\qquad t_{\rm landing}\approx\frac{b^2}{k+1}.$$
The terms $(\beta_k-\beta_l)$ among cluster members are $\approx0$ (equal heights) and the horizontal repulsion ($\dot\alpha\sim k/w$) disperses the cluster without singularity: velocities are finite as long as the zeros are distinct, and the only forward collisions are landings (real–real collisions are excluded by repulsion: $\dot g=4/g+O(1)>0$ for the minimum gap). **Conclusion: the infinite accumulation of sub-resolution quadruples is dynamically consistent** — the cluster accelerates its own landing (factor $k+1$), extra slack in the budget of Thm 174.8, no infinite velocity, no forbidden collapse.

### 3.3. [REFUTATION] "$I<\infty\Rightarrow m<\infty$" is FALSE in the class — the dynamical weld of the two arrows does not exist

The mandate's candidate ("if you find a dynamical contradiction for $m=\infty\wedge I<\infty$, you will have proved $I<\infty\Rightarrow m<\infty$") is **refuted in the Pólya class, with a counterexample**: the Hadamard configuration of Doc 144 (repaired version of Doc 168 §5.1, with real zeros at the exact RvM points and quadruples at $\gamma_j=2^j$, $b_j=e^{-\gamma_j}$) has $m=\infty$, $I=\sum b_j^2<\infty$, belongs to $\mathcal C$, **and enters the DBN flow** (the semigroup $e^{-t\partial_z^2}$ acts in order $<2$). Its dynamics is that of Calculation 174.9 with trivial clusters ($k=1$, super-exponential separations): perfectly regular, lifetimes $\ell_j\approx b_j^2/2$ very summable, budget of Thm 174.8 satisfied with infinite slack. **There is no class-wide dynamical obstruction: any proof of $I<\infty\Rightarrow m<\infty$ — if the implication is even true for ζ — must use arithmetic input beyond RvM density.** This closes (negatively, with proof) idea B3 in its strong version; what replaces it is Theorem 174.8 (budget, true and unconditional on its domain) and the reformulation: the two arrows are not welded in the dynamics; they are welded — if at all — in the initial condition (consistent with the key structural fact of §0 and with Doc 167 §4c: finiteness is Fredholm, not dynamical).

---

## 4. The moment system (B1): the hierarchy closed downward

### 4.1. The complete hierarchy

**[THEOREM 174.10] (hierarchy of even moments).** Let $I_{2n}(t):=\sum_{k\,\rm upper}\beta_k(t)^{2n}$, $n\ge1$ ($I_2=I$). On intervals with $\kappa<\infty$ and simple zeros:
$$\dot I_{2n}\;=\;-2n\,I_{2n-2}\;-\;D_{2n},\qquad D_{2n}\ge0\ \text{term by term},\qquad(I_0:=\kappa).$$

*Proof.* $\dot I_{2n}=\sum_k2n\beta_k^{2n-1}\dot\beta_k=-4n\sum_k\sum_{w\ne z_k}\beta_k^{2n-1}\frac{\beta_k-\mathrm{Im}\,w}{|z_k-w|^2}$. Own conjugate: $\beta_k^{2n-1}\cdot2\beta_k/4\beta_k^2=\beta_k^{2n-2}/2$, contribution $-2n\beta_k^{2n-2}$ per mode: total $-2n\,I_{2n-2}$. Mirror: $0$. Antipode and real zeros: $\le0$. Cross terms, symmetrizing $(k,l)+(l,k)$ over the same denominator (the exact denominator coincidence of Doc 168 §2.5): $\beta_k^{2n-1}(\beta_k-\beta_l)+\beta_l^{2n-1}(\beta_l-\beta_k)=(\beta_k-\beta_l)(\beta_k^{2n-1}-\beta_l^{2n-1})\ge0$ (factors of the same sign), and $(\beta_k+\beta_l)(\beta_k^{2n-1}+\beta_l^{2n-1})\ge0$. $\square$

**Verification in the closed model:** isolated pair $\beta^2=\beta_0^2-2t$: $I_{2n}=(\beta_0^2-2t)^n$, $\dot I_{2n}=-2n(\beta_0^2-2t)^{n-1}=-2nI_{2n-2}$ exact, $D_{2n}=0$ — the free cascade is realized with equality.

### 4.2. Corollaries: the virial family interpolating energy and band

**[COR 174.11].** On $(t_0,\Lambda)$, with $\kappa\ge2$ (parity + gift lemma):
1. *(accelerated decay of high moments)* $I_{2n-2}\ge I_{2n}/M\ge I_{2n}$ ⟹ $\dot I_{2n}\le-2n\,I_{2n}$ ⟹ $I_{2n}(t)\le I_{2n}(t_0)e^{-2n(t-t_0)}$: **the profile $\{\beta_k\}$ flattens in every $\ell^{2n}$ norm at rate $2n$** — the cloud loses its large heights first.
2. *(virial family)* By power-mean inequality, $I_{2n-2}\ge\kappa^{1/n}I_{2n}^{(n-1)/n}\ge2^{1/n}I_{2n}^{(n-1)/n}$, so $\dot I_{2n}\le-2n\,2^{1/n}I_{2n}^{(n-1)/n}$ and integrating:
$$\Lambda\;\le\;t_0+\frac{I_{2n}(t_0)^{1/n}}{2^{1+1/n}}\qquad\text{for every }n\ge1.$$
$n=1$ recovers $\Lambda\le t_0+I/4$ (Cor 167-2.4 repaired); $n\to\infty$ recovers $\Lambda\le t_0+M/2$ (de Bruijn band, Lemma 174.3): **the hierarchy interpolates exactly between the energy virial and the band theorem — the two known results are the extremes $n=1$ and $n=\infty$ of a single family.**

*Proof.* (1): $M<1$. (2): $(I_{2n}/\kappa)^{1/n}\le(I_{2n-2}/\kappa)^{1/(n-1)}$ (monotonicity of power means) gives the form used after rearranging; the ODE $u'\le-cu^{(n-1)/n}$ gives $u^{1/n}$ decreasing at rate $c/n$, extinction at $nu_0^{1/n}/c$ with $c=2n\cdot2^{1/n}$. $\square$

### 4.3. Entropy (conditional on smallness) and the weighted moment (not closed)

**[PROP 174.12] (entropy).** $S(t):=\sum_k\beta_k^2\log(1/\beta_k)$. If $\sup_k\beta_k\le e^{-3/2}$ on the interval, then
$$\dot S\;\le\;-2\sum_k\log\frac1{\beta_k}\;+\;\kappa\;\le\;-\kappa\Bigl(\log\frac1{M}-1\Bigr).$$
*Proof.* $\dot S=\sum\varphi(\beta_k)\dot\beta_k$ with $\varphi(\beta)=2\beta\log(1/\beta)-\beta$. Own conjugate ($\dot\beta\ni-1/\beta$): $-\sum(2\log(1/\beta_k)-1)$. The other terms are $\le0$ if $\varphi\ge0$ (⟸ $\beta\le e^{-1/2}$) and $\varphi$ increasing (⟸ $\varphi'=2\log(1/\beta)-3\ge0$ ⟸ $\beta\le e^{-3/2}$): same signs and symmetrizations as Thm 174.10 with a monotone weight. $\square$
**Use:** near extinction ($M\to0$) the entropy dissipates at rate $\kappa\log(1/M)\gg\kappa$: $S$ is the functional that "sees" sub-resolution ($\log(1/\beta)\sim\log\log\gamma$ at the LP-134 scale) — backward, $S$ grows super-linearly relative to $I$: a candidate weight for the ancestor census of §2.3.

**[CALCULATION 174.13] ($\langle\alpha^2\beta^2\rangle$ does not close; exact value in the model).** $J:=\sum_k\alpha_k^2\beta_k^2$ satisfies $\dot J=-2\sum_k\alpha_k^2+(\text{transport }2\alpha_k\dot\alpha_k\beta_k^2)+(\dots)$, and the transport involves $\dot\alpha_k$ (conditionally convergent, with no sign): **the system does not close in pure vertical moments** — the obstruction is the horizontal flow (the gas's expansion: in the closed quadruple, $d(\alpha^2-\beta^2)/dt=6$, $d(\alpha^2)/dt=4-2\beta^2/|z|^2>0$). In the isolated quadruple, exact: $\alpha^2\beta^2=(\mathrm{Im}\,w)^2/4$ ⟹ $\boxed{d(\alpha^2\beta^2)/dt=-2(\alpha^2-\beta^2)}$ (Thm 174.4). [GAP-174.D: closing $J$ requires coupling with the first horizontal moment of the real gas; we do not pursue it — the accessible content of Phase C lies in the vertical hierarchy.]

### 4.4. Phase C (profile classification): what the moment system says

From the hierarchy + budget: an initial profile $\{(\gamma_j,b_j)\}$ is dynamically consistent iff (i.e.: the dynamics does NOT classify beyond) — summable lifetimes if $I<\infty$ (Thm 174.8), ordered $\ell^{2n}$ decay (Cor 174.11.1), no equilibria with $\kappa>0$ (strict $\dot I<0$: **there are no off-line stationary states, not even metastable ones** — de-excitation is unconditional). Everything else (which profiles ζ realizes) is initial condition: the classification of Phase C is arithmetic or it is nothing. With the real gap statistics (RvM + Selberg fluctuations) the only proved coupling is that of §2: backward-reachable profiles from RH all have pairs with an ancestor; the ¬RH-finite profile is exactly the one with orphans.

---

## 5. Anti-circularity test

| Object | RH-free? | ζ-free? | Where ζ re-enters |
|---|---|---|---|
| Prop 174.1 (non-coercivity), Thm 174.4 (closed model, exact $t_c$) | yes | yes | does not re-enter |
| Lemma 174.3 (maximum), Thm 174.2 (coercivity $\dot I\le-2I$), Thm 174.5 (forward) | yes | yes (class + [KKL] for the anchor $t_0>0$) | does not re-enter |
| Thm 174.8 (budget), Thm 174.10 + Cor 174.11 (hierarchy), Prop 174.12 | yes | yes | does not re-enter |
| Prop 174.7 (lattice = fixed point) and Calculation 174.6 (takeoff $-g^2/8$) | yes | yes | does not re-enter; fixes WHERE ζ would enter |
| §2.3 backward separation, orphans, GAP-174.B | yes | **no** in its arithmetic half | ζ enters through gap statistics ([S46] unconditional; GUE conditional) |
| §3.3 refutation of the weld | yes | yes (class counterexample) | the implication for ζ remains open, not refuted |

Pattern confirmed and refined relative to Doc 167: the LAW (now: the whole hierarchy, the budget, the maximum) is ζ-free; arithmetic has **a single identified dynamical entry point: gap fluctuations** (Prop 174.7 isolates it: without fluctuation there is no takeoff). There are no primes in any proof of this document.

---

## 6. Verdict

### New theorems
- **[THEOREM 174.10 + COR 174.11] (moment hierarchy):** $\dot I_{2n}=-2nI_{2n-2}-D_{2n}$, $D_{2n}\ge0$, for all $n\ge1$; decay $e^{-2nt}$ per norm; virial family $\Lambda\le t_0+I_{2n}^{1/n}/2^{1+1/n}$ that **interpolates exactly between the energy virial ($n=1$) and the de Bruijn band ($n=\infty$)** — the two known results are the extremes of a single family. The best theorem of the document.
- **[THEOREM 174.2 + LEMMA 174.3] (B2 resolved):** $D\ge cI$ is false (Prop 174.1, exact counterexample $D/I=2/|z|^2$), but $\dot I\le-2I/M\le-2I$: exponential coercivity exists with $L=I$, $c=2$, by quantization + band, not by interaction dissipation. Maximum principle $D^+M\le-2$ (new dynamical re-proof of de Bruijn's Thm 13).
- **[THEOREM 174.8] (budget):** $\sum_j\ell_j\le I(0^+)/4$ — the two arrows are $\kappa\in L^\infty$ vs $\kappa\in L^1$ at $t\to0^+$, and the lifetime↔energy exchange currency is the Lehmer exponent 2.
- **[THEOREM 174.4/174.5] (closed forward):** exact solution of the quadruple, $t_c=\beta_0^2/2-\beta_0^4/4\alpha_0^2+O(\cdot)$ (answer to the director: $\beta^2/2$, not $\beta^2/4$; $=I_0/4$ per quadruple); forward structure: universal extinction with explicit rates — **the RH question lives entirely at $t\le0$**.
- **[PROP 174.7] (lattice fixed point):** density does not buy backward takeoffs; the entry point of arithmetic into the flow is gap fluctuations, isolated with proof.

### Refutations and negative closures (with proof)
- **§3.3:** "$I<\infty\Rightarrow m<\infty$" is **false in the class** (repaired Hadamard counterexample, which flows); the director's dynamical weld of the two arrows does not exist — B3 strong version closed. No self-obstruction of $\ell^2$ clusters (Calculation 174.9: acceleration $b^2/(k+1)$, not forbidden collapse).
- **§2.3(c):** no computable backward invariant separates the scenarios without computing $I(0)$: the backward flow transports the dichotomy, it does not selectively amplify it — **Doc 170's rate/total dichotomy is a property of the flow**, not of the explicit formula.

### Declared [GAPs], with statement form
- **GAP-174.B (the central one):** upper bound on takeoff for real configurations: $\beta(t)^2\le2k\,|t|(1+o(1))$ with $k$ = local near-collision multiplicity of the initial configuration at scale $\sqrt{8|t|}$. It is a pure particle-dynamics statement (ζ-free); with it, ¬RH-with-finite-$I$ ⟺ existence of backward **orphan pairs**, and the arithmetic half of the bridge is reduced to the ancestor census = gap statistics of ζ.
- **GAP-174.C:** is $\kappa(t)=\infty$ for all $t<0$? (backward dual of KKL; Prop 174.7 shows that density does not decide it).
- **GAP-174.D:** closure of the weighted moment $J=\langle\alpha^2\beta^2\rangle$ (horizontal transport; not pursued).

### References
de Bruijn, N.G. (1950), *The roots of trigonometric integrals*, Duke Math. J. 17, 197–226 (Thm 13: decreasing band). — Newman, C.M. (1976), Proc. AMS 61, 245–251. — Csordas, G., Smith, W., Varga, R.S. (1994), *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis*, Constr. Approx. 10, 107–129. — Ki, H., Kim, Y.-O., Lee, J. (2009), *On the de Bruijn–Newman constant*, Adv. Math. 222, 281–306. — Rodgers, B., Tao, T. (2020), *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8, e6 (§2: zero dynamics). — Polymath, D.H.J. (2019), Res. Math. Sci. 6, 31. — Selberg, A. (1946), *Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. 48 (moments of $S(t)$, unconditional). — Montgomery, H.L. (1973), Proc. Symp. Pure Math. 24 (pair correlation, conditional on RH). — **[literature GAP]:** the connection of the zero flow with rational Calogero–Moser is folklore (cf. Tao's expositions around [RT]); we use no result from that literature. The hierarchy $\dot I_{2n}=-2nI_{2n-2}-D_{2n}$ and the budget $\sum\ell_j\le I/4$ we do not know stated anywhere. — Internal docs: 144, 167, 168, 170.

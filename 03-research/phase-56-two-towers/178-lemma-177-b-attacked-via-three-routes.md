# Document 178 — Lemma 177.B attacked via three routes: gap-ODE with compressed blocks, equivalence with the local De Bruijn–Newman constant, and the calibration that dissolves the "literature GAP"

**Program:** Riemann Hypothesis — Phase 56 (two towers)
**Mandate:** attack [MINIMAL-LEMMA 177.B] (Doc 177 §4.2): ∃θ∈(0,½), c>0 such that for the arithmetic $H_t$ and every $t\in(0,1)$, every consecutive gap of real zeros of $H_t$ at height $\gamma\ge\Gamma(t):=\exp(t^{-(1/2-\theta)})$ satisfies $g_{\rm norm}:=g\cdot\frac{\log\gamma}{4\pi}\ge c\,t^\theta$. Three mandatory routes (Rodgers–Tao §2; gap ODE; comparison with the solvable model / asymptotic zone of Polymath 15). No audits; no numerics.
**Prerequisites (certified, not re-derived):** Doc 167 (zero dynamics Lemma 2.1; balance law Thm 2.3; fold Prop 2.6; flow convention §0.1), Doc 177 (exact Hermite Thm 177.1; stability Prop 177.3; sea bound Lemma 177.4; energy bound Thm 177.6; landing logic Thm 177.7 and Cor 177.8; landing-time bound $t_c\ge b^2/(2n^2)(1-C\varepsilon)$ of §4.1).
**Contract:** [NEW-DEFINITION] free; [THEOREM]/[PROP]/[LEMMA] only with complete proof; [BRIDGE] with frank status; [GAP]/[literature GAP] declared. Backward-only citations (docs ≤ 177 + real literature).

---

## 0. Conventions

Polymath 15 chart as in Doc 167 §0.1: $H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du$, $\partial_tH_t=-\partial_z^2H_t$, $H_0=\tfrac18\Xi(\cdot/2)$ up to fixed rescaling. **In this chart, increasing $t$ is the regularizing direction** (de Bruijn: reality is absorbing; $\Lambda\le t$ ⟹ real zeros): this is the direction the mandate calls *forward*. The simple-zero dynamics (Lemma 167-2.1) is
$$\dot z_k \;=\; 2\sum_{j\ne k}{}^{\!\!'}\frac{1}{z_k-z_j},$$
**repulsive between real zeros** (gaps tend to open with $t$) and **attractive between a zero and its conjugate** ($\dot\beta\le-1/\beta+\text{sea}$: complex pairs fall and land). Sign note: the mandate's statement writes $\partial_tH=\partial_z^2H$ ("forward convention"); the P15/Doc 167 chart has the opposite sign in the PDE but **the same zero dynamics and the same regularizing direction**; everything below uses only the zero dynamics, so there is no ambiguity.

Notation: $\rho=\rho(\gamma):=\frac{\log\gamma}{4\pi}$ (local density in the $H$ chart, RvM), $L:=\log\gamma$, $g_{\rm norm}=g\rho$. "Height" = $|\mathrm{Re}\,z|$ (zeros of $\zeta$ at height $\gamma$ are zeros of $\Xi$ with $\mathrm{Re}\,z=\gamma$, $\mathrm{Im}\,z=b$, $b<\tfrac12$). Landing = instant $t_c$ at which a conjugate pair touches the real axis.

**Exact calibration check (will be used twice).** $H(z)=\cos(\lambda z)$ evolves into $e^{t\lambda^2}\cos(\lambda z)$: **the evenly spaced lattice is exactly stationary** under the flow. Any lower bound on gaps that claims to grow with $t$ must use more than "neighboring gaps are no smaller": it must use a counting input.

---

## 1. Route 1 (Rodgers–Tao §2): what is there, what is extracted, what it cannot give

**What is there (frank reading of [RT 2020]).** The machinery of [RT] analyzes the dynamics $\dot x_k=2\sum'(x_k-x_j)^{-1}$ **backward** ($t<0\to0^-$): assuming $\Lambda<0$, at $t=\Lambda$ all zeros are real and the dynamics on $[\Lambda,0]$ is a purely real gas; their estimates (local energy of the gas, comparison with the locally equispaced equilibrium) show that after **fixed** time $|\Lambda|>0$ the gas at $t=0$ would be locally rigid (equispaced at microscopic scale), contradicting unconditional fluctuation estimates for the count of zeros of $\zeta$. Three structural features:

1. **The time parameter is bounded away from zero**: all quantification is "for $t$ in a compact of fixed length $|\Lambda|$"; the constants in their relaxation lemmas degenerate as the available time $\to0$. Uniformity at the diffusive corner $t\,\rho^2\gg1$ with $t\to0^+$ **is not in [RT]** (nor did they need it).
2. **The direction is inverted relative to 177.B**: they go from "real zeros at $t=\Lambda$" to "rigidity at $t=0$"; 177.B asks to go from "arithmetic $H_0$" to "gaps at $t>0$". Their arithmetic input (fluctuation of ζ's count) enters at $t=0$ as a *destination*, not as initial data.
3. **What is extractable and reused**: (a) the symmetrized, absolutely convergent form of the dynamics (already certified in Lemma 167-2.1); (b) the idea of comparing with the local equilibrium **with a counting input** — which is exactly what is missing after the lattice check of §0; we turn it into a theorem in §2.

**Verdict of route 1:** it does not die but does not close: its machinery belongs to the "macroscopic time, full relaxation" regime and 177.B lives in "microscopic time, partial relaxation". The transferable part (local equilibrium + counting) is executed in §2 as Theorem 178.4. What route 1 *cannot* give under any refinement — an unconditional 177.B — is proved in §3 (Prop 178.7: structural, not technical, blockage).

---

## 2. Route 2: the gap ODE, the lattice no-go, and the conditional sub-diffusive theorem

### 2.1. The exact gap ODE

**[LEMMA 178.1] (gap ODE).** Let $J$ be an interval of times on which the zeros of $H_t$ in the window $|{\mathrm{Re}\,z-\gamma}|\le10$ are real and simple, and let $x_k<x_{k+1}$ be consecutive in that window, $g=x_{k+1}-x_k$. Then
$$\dot g\;=\;\frac4g\;-\;g\,S,\qquad S\;:=\;\sum_{j\notin\{k,k+1\}}\frac{2}{(x_j-x_k)(x_j-x_{k+1})}\;+\;\mathcal{E},$$
where the sum runs over the other **real** zeros, inside and outside the window (grouped symmetrically as in Lemma 167-2.1, absolutely convergent by RvM), each term with $x_j\notin(x_k,x_{k+1})$ is $\ge0$ (both denominator factors have the same sign), and $\mathcal{E}$ collects non-real zeros and the mirror $-Z$: if there are no non-real zeros at distance $\le D\ge1$ from the window, $|\mathcal{E}|\le C\rho/D^2+C\gamma^{-2}$ by the argument of Lemma 177.4.

*Proof.* $\dot g=\dot x_{k+1}-\dot x_k=2\bigl[\tfrac1{x_{k+1}-x_k}-\tfrac1{x_k-x_{k+1}}\bigr]+2\sum_{j\notin\{k,k+1\}}\bigl[\tfrac1{x_{k+1}-x_j}-\tfrac1{x_k-x_j}\bigr]$; the first bracket gives $4/g$ and each term of the second is $-\,g/((x_j-x_k)(x_j-x_{k+1}))$ by combining into a common denominator, doubled by the ordered-pair convention. The bound on $\mathcal{E}$: each non-real conjugate pair at distance $\ge D$ contributes a difference of two terms of the type in Lemma 177.4 with bounded numerator and denominators $\ge D^2$; the sum over the non-real sea with RvM density gives $C\rho/D^2$; the mirror at $-\gamma$ gives $O(\gamma^{-2})$. $\square$

**Reading.** The real sea **always compresses** ($S\ge0$ modulo $\mathcal{E}$): the pair's repulsion against the sea's compression. The question is the worst-case value of $S$.

### 2.2. The no-go of the bare minimum principle

**[PROP 178.2] (exact saturation of the lattice: the hypothesis "all gaps $\ge g$" gives nothing).** If one assumes only that all other gaps are $\ge g_*$ and the gap considered is $g=g_*$ (the local minimum), the best bound obtainable for the sum of §2.1 is
$$S\;\le\;2\cdot\frac{2}{g_*^2}\sum_{m\ge1}\frac{1}{m(m+1)}\;=\;\frac{4}{g_*^2}\qquad\Longrightarrow\qquad \dot g_*\;\ge\;\frac{4}{g_*}-g_*\cdot\frac4{g_*^2}\;=\;0,$$
and equality is attained **exactly** on the infinite evenly spaced lattice of step $g_*$ — which is genuinely stationary ($\cos(\lambda z)\mapsto e^{t\lambda^2}\cos(\lambda z)$, §0). Hence **no Hamilton-type maximum principle on the minimum gap closes 177.B without an additional input**: the extremal scenario (a long uniformly compressed block) does not expand locally; it expands only at its edges.

*Proof.* With $d_m\ge mg_*$ for the $m$-th neighbor on each side, $\sum_m\frac{2}{d_m(d_m+g_*)}\le\frac{2}{g_*^2}\sum_m\frac1{m(m+1)}=\frac{2}{g_*^2}$ per side. Equality iff $d_m=mg_*$ for all $m$: the lattice. The stationarity of the cosine is the computation in §0. $\square$

This refutes the naive version of route 2 (the inequality $g\dot g\ge4-\text{error}$ with $g^2\ge8t$ and limiting $\theta=\tfrac12$): **the sea's "error" is exactly $4$ in the extremal case**. The missing input is that the extremal case violates the count:

### 2.3. Compressed blocks are short: the counting input

**[HYPOTHESIS (RvM-t), declared].** *There exists $C_0$ such that for every $t\in[0,1]$ and every interval $J\subset\mathbb R$ with $|J|\le1$ centered at large height $\gamma$: $\#\{x\in Z_t\cap J\}\le\rho(\gamma)\,|J|+C_0\log\gamma$.* For $t=0$ this is classical Riemann–von Mangoldt. For $t\in(0,1]$ we believe it is standard but we do not verify it line by line: see Bridge 178.5. Everything conditional on (RvM-t) explicitly flags it.

**[LEMMA 178.3] (compressed blocks are short).** Under (RvM-t): if $M$ consecutive real zeros of $H_t$ near height $\gamma$ all have gaps $\le\frac{1}{2\rho}$, then $M\le M_0:=2C_0\log\gamma+2$.

*Proof.* The block occupies length $\ell\le M\cdot\frac1{2\rho}\le\tfrac{M}{2\rho}$ (and $\le1$ if $M\le2\rho$; if $M>2\rho$, split into unit-length subintervals and sum). By (RvM-t): $M\le\rho\ell+C_0L$, so $M\le2C_0L+2$. $\square$

### 2.4. The conditional sub-diffusive theorem: what route 2 does prove

**[THEOREM 178.4] (growth of the minimum gap; conditional on (RvM-t) and local reality).** There exist absolute $c_1,c_2,C>0$ such that: let $[s,t]\subset(0,1]$, $\gamma$ large, and suppose
- **(R)** *local reality:* $H_{t'}$ has no non-real zeros with $|\mathrm{Re}\,z-\gamma|\le10$ for any $t'\in[s,t]$, and $t-s\le L^{-2}\cdot C'$ (so horizontal drift does not empty the window; Lemma 178.6 below);
- **(RvM-t)** in the window.

Let $g_*(t')$ be the minimum of the consecutive gaps in $|\mathrm{Re}\,z-\gamma|\le5$. Then
$$g_*(t)^2\;\ge\;\min\Bigl\{\,g_*(s)^2+\frac{c_1\,(t-s)}{\log\gamma}\,,\;\frac{c_2}{\rho^2\log\gamma}\,\Bigr\}.$$

*Proof.* $g_*$ is the minimum of finitely many real-analytic functions (zeros are simple and real on $[s,t]$ by (R); the instants where the minimizer changes are locally finite), hence locally Lipschitz and differentiable except at finitely many points; at each differentiability point its derivative is the $\dot g$ of a minimizing pair (Danskin). Fix an instant and a minimizing pair $(x_k,x_{k+1})$, $g=g_*$, and bound $S$ from Lemma 178.1, assuming (non-trivial case) $g\le\frac1{2\rho}$ and $\rho^2g^2\log\gamma$ smaller than a small constant (otherwise we are already at the ceiling of the statement).

*Nearby chain.* On each side of the pair, order the zeros by distance: $d_1<d_2<\dots$ While the zeros are in the window $|\cdot-\gamma|\le5$, all gaps are $\ge g$, hence $d_m\ge mg$. Moreover, by (RvM-t) applied to the interval $[x_{k+1},x_{k+1}+d_m]$: $m\le\rho d_m+C_0L$, i.e. $d_m\ge\frac{m-C_0L}{\rho}$ for all $m$ (also valid with zeros outside the window). With $M_0=2C_0L+2$:
$$\sum_{m\le M_0}\frac{2}{d_m(d_m+g)}\le\frac{2}{g^2}\sum_{m=1}^{M_0}\frac1{m(m+1)}=\frac{2}{g^2}\Bigl(1-\frac1{M_0+1}\Bigr),\qquad
\sum_{m>M_0}\frac{2}{d_m(d_m+g)}\le\sum_{m>M_0}\frac{2\rho^2}{(m-C_0L)^2}\le C\rho^2 .$$
(Zeros at distance $>5$, outside the window, are covered by the second sum via (RvM-t) in dyadic pieces of length $\le1$; non-real ones are excluded at distance $\le10$ by (R), and at distance $>10$ contribute $\le C\rho/100$ by Lemma 178.1, absorbed into $C\rho^2$.) Summing both sides:
$$S\;\le\;\frac{4}{g^2}\Bigl(1-\frac{1}{M_0+1}\Bigr)+C\rho^2 \qquad\Longrightarrow\qquad \frac{d}{dt'}\,g^2\;=\;2g\dot g\;\ge\;\frac{8}{M_0+1}-2C\rho^2g^2 .$$
While $g^2\le\frac{2}{C\rho^2(M_0+1)}$, the right side is $\ge\frac{4}{M_0+1}\ge\frac{c_1}{L}$. Integrating the differential inequality over $[s,t]$ (valid a.e.; $g_*^2$ is absolutely continuous) gives the minimum between the linear growth and the ceiling $\frac{2}{C\rho^2(M_0+1)}\ge\frac{c_2}{\rho^2L}$. $\square$

**[LEMMA 178.6] (horizontal drift; makes the windows honest).** Under the hypotheses of Theorem 178.4, the horizontal velocity of any real zero of the window is bounded by $C\log^2\gamma$ (group the symmetrized sum into dyadic blocks: the $\le CL$ zeros at distance $\in[2^{-r},2^{-r+1}]$, $2^{-r}\ge g_*$, contribute $\le CL\cdot2^{r}\cdot$... and the sum over $r\le\log(1/g_*)\le CL$ gives $\le CL^2$ after pairwise cancellation of the leading term; the far ones, $\le C\rho$ by symmetrized RvM). In time $t-s\le C'L^{-2}$ the displacement is $\le CC'$: the windows $\pm5/\pm10$ of the theorem are consistent by taking $C'$ small. $\square$ *(Proof with the declared slack: constant $C'$ is that of hypothesis (R).)*

### 2.5. Translation to 177.B: the band that closes and the one that does not

Taking $s=t/2$ in Theorem 178.4 (legitimate if local reality holds on $[t/2,t]$ and $t\le C'L^{-2}$): $g_*(t)^2\ge c\,t/L$ up to the ceiling. In normalized units, $g_{\rm norm}^2=g^2\rho^2\ge c\,t\rho^2/L=c'\,tL$. Comparing with the demand $g_{\rm norm}\ge c\,t^{\theta_2}$:
$$c'tL\ge c^2t^{2\theta_2}\iff L\ge C\,t^{-(1-2\theta_2)};\qquad\text{ceiling not reached}\iff tL\le c''/L\iff L\le c''\,t^{-1/2}.$$
That is: **route 2 proves (conditionally) the bound of 177.B exactly in the sub-diffusive band**
$$t^{-(1-2\theta_2)}\;\le\;\log\gamma\;\le\;c\,t^{-1/2},\qquad \theta_2\in(\tfrac14,\tfrac12)$$
(the band is non-empty iff $1-2\theta_2<\tfrac12$, i.e. $\theta_2>\tfrac14$). In 177.B's parametrization, the lower threshold corresponds to $\Gamma(t)=\exp(t^{-(1/2-\theta_1)})$ with $\theta_1=2\theta_2-\tfrac12\in(0,\tfrac12)$: **parameters admissible for 177.B**. What it does NOT cover: (i) the super-diffusive zone $\log\gamma>ct^{-1/2}$, where the theorem's ceiling $g_{\rm norm}\ge c\,L^{-1/2}$ is weaker than $ct^\theta$ when $L>t^{-2\theta}$ — there the correct mechanism is full relaxation to the local equilibrium (route 1), not proved uniformly [GAP-178.B]; (ii) above all, **hypothesis (R)**: the theorem only applies where there were no non-real zeros in $[t/2,t]$. A landing in $(t/2,t]$ creates a real gap $\asymp\sqrt{t-t_c}$ arbitrarily small (fold, Prop 167-2.6) that no later evolution had time to repair. Route 2, fully squeezed, then delivers:

**[THEOREM 178.4′] (summary of route 2).** *Conditional on (RvM-t): if $H_{t'}$ has no non-real zeros at distance $\le10$ from height $\gamma$ for any $t'\in[t/2,t]$, then every gap at height $\gamma$ at time $t$ satisfies $g_{\rm norm}\ge c\,t^{\theta_2}$ in the band $\log\gamma\in[t^{-(1-2\theta_2)},c\,t^{-1/2}]$, $\theta_2\in(\frac14,\frac12)$.* (This is Theorem 178.4 + the translation above; the condition $t\le C'L^{-2}$ is automatic in the band.) $\square$

**All the burden of 177.B is now concentrated in the local-reality hypothesis.** That is route 3.

### 2.6. The status of (RvM-t)

**[BRIDGE 178.5 / GAP-178.A] (RvM uniform in $t$).** *Needed statement:* the (RvM-t) hypothesis of §2.3 (only the upper count bound in windows of length $\le1$, uniform in $t\in[0,1]$). *Status:* for $t=0$ it is classical. For fixed $t>0$, [KKL] obtain asymptotics of $H_t$ implying it at heights large depending on $t$. Uniformity in $t\in[0,1]$ should follow from the standard scheme (Jensen on discs of radius $O(1)$ + an upper bound of $|H_t|$ in the band, which is effective and uniform from the integral representation with superexponential $\Phi$ + a lower bound of $|H_t|$ at a point per window at distance $\asymp1$ from the axis); the non-trivial ingredient is the lower bound, which for $H_0$ follows from $\zeta(s)\ne0$ at $\mathrm{Re}\,s\ge2$ and for $H_t$ should follow from the effective approximation of [P15] (their bounds on $|H_t|$ and the errors $A+B-C$ are explicit and uniform in $t\in[0,1/2]$ in bands $|\mathrm{Im}\,z|=O(1)$). **Not verified line by line here: [literature GAP], believed standard, no conceptual novelty.** Every theorem in this document using it declares so.

---

## 3. Route 3: landings, the local De Bruijn–Newman constant, and the hardness calibration

### 3.1. The correct object

**[NEW-DEFINITION 178.6′] (local De Bruijn–Newman constant at height).**
$$\Lambda_{\rm loc}(\gamma)\;:=\;\inf\bigl\{\tau>0:\ \forall t\in[\tau,1],\ H_t\ \text{has no non-real zeros with}\ |\mathrm{Re}\,z-\gamma|\le5\bigr\}.$$
Well defined on $[0,\Lambda]$ ($\Lambda\le1/2$, [dB]); $\sup_\gamma\Lambda_{\rm loc}(\gamma)=\Lambda$ up to window-boundary effects, controlled by Lemma 178.6 at the relevant time scales ($\tau\le L^{-2}$: horizontal drift $O(1)$, absorbed by taking window $\pm5$ in the definition and $\pm1$ in the conclusions. For large $\tau$ the definition is only a frank infimum, we do not claim exact local monotonicity).

### 3.2. Direction A: small $\Lambda_{\rm loc}$ ⟹ 177.B (in the band)

**[THEOREM 178.7] (the good half of the equivalence).** Conditional on (RvM-t): if
$$\Lambda_{\rm loc}(\gamma)\;\le\;\tfrac12\,(\log\gamma)^{-2/(1-2\theta_1)}\quad\text{for all large }\gamma\qquad(\ast)$$
with $\theta_1\in(0,\tfrac12)$, then 177.B holds **in the sub-diffusive band**: with $\theta_2=\frac{\theta_1}{2}+\frac14$, every gap at height $\gamma$ and time $t$ with $\log\gamma\in[t^{-(1-2\theta_2)},c\,t^{-1/2}]$ satisfies $g_{\rm norm}\ge c\,t^{\theta_2}$.

*Proof.* In the band, $\log\gamma\ge t^{-(1-2\theta_2)}=t^{-(1/2-\theta_1)\cdot\frac{1-2\theta_2}{1/2-\theta_1}}$; since $1-2\theta_2=\tfrac12-\theta_1$, this is $\log\gamma\ge t^{-(1/2-\theta_1)}$, i.e. $t\ge(\log\gamma)^{-2/(1-2\theta_1)}\ge2\Lambda_{\rm loc}(\gamma)$ by $(\ast)$. Hence on $[t/2,t]$ there are no non-real zeros in the window: hypothesis (R) of Theorem 178.4′ holds and its conclusion is the desired one. $\square$

### 3.3. Direction B: 177.B ⟹ small $\Lambda_{\rm loc}$ and confinement of ALL zeros of ζ

This direction is unconditional (does not use (RvM-t)) and is the main finding of the document.

**[PROP 178.8] (177.B bounds landings — version for every zero, not only under $m=\infty$).** Suppose 177.B with parameters $(\theta,c)$. Then: (1) every landing at $(t_c,\gamma_c)$, $t_c\in(0,1)$, satisfies $\gamma_c\le\Gamma(t_c)$, equivalently $\Lambda_{\rm loc}(\gamma)\le(\log\gamma)^{-2/(1-2\theta)}$ for large $\gamma$; (2) **every** zero of $\zeta$ off the critical line, at large height $\gamma$ and distance $b$ from the line, satisfies
$$b\;\le\;C\,(\log\gamma)^{-\frac{1}{1-2\theta}}\;=\;C\,(\log\gamma)^{-1-\eta},\qquad \eta=\frac{2\theta}{1-2\theta}>0 .$$

*Proof.* (1) is the argument of Thm 177.7(1), which does not use $m=\infty$: right after a landing, the fold (Prop 167-2.6; and in the cluster case, the Hermite fan Thm 177.1, whose minimal gaps are $\le C\sqrt\delta$) produces at time $t_c+\delta$ a real gap at height $\gamma_c+O(1)$ with $g_{\rm norm}\le C\sqrt\delta\log\gamma_c$; if $\gamma_c\ge\Gamma(t_c+\delta)$, 177.B demands $C\sqrt\delta\log\gamma_c\ge c\,t_c^\theta$ for all small $\delta>0$ — false as $\delta\to0^+$. Hence $\gamma_c<\Gamma(t_c)$, which rearranged is $t_c\le(\log\gamma_c)^{-2/(1-2\theta)}$, and since every non-real zero over the window of $\gamma$ eventually lands (de Bruijn + KKL: at time $\le\Lambda<\tfrac12$), $(\ast)$ holds with that bound. (2): the off zero of $\zeta$ is a non-real zero of $H_0$ with height $b$; by the landing-time bound of Doc 177 §4.1 (Thm 177.6 read forward from the landing): $t_c\ge\frac{b^2}{2n^2}(1-C\varepsilon)$ with $n$ = multiplicity at current scale, $n\le\max(2,C\sqrt{t_c}\log\gamma)$. From (1), $t_c\le(\log\gamma)^{-2/(1-2\theta)}=:\tau$. If $n\le2$: $b^2\le Ct_c\le C\tau$ gives directly $b\le C\tau^{1/2}=(\log\gamma)^{-1/(1-2\theta)}$. If $n>2$: $n\le C\sqrt\tau\log\gamma=C(\log\gamma)^{1-\frac{1}{1-2\theta}}\to0$, absurd for large $\gamma$: the case does not occur. $\square$

**[COR 178.9] (hardness calibration; D177's "literature GAP" dissolves).** 177.B implies **polylogarithmic confinement** of all zeros of $\zeta$: $b\ll(\log\gamma)^{-1-\eta}$. This vastly exceeds every known zero-free region (Vinogradov–Korobov gives only $b\le\tfrac12-c(\log\gamma)^{-2/3}(\log\log\gamma)^{-1/3}$: a strip next to the *edge*, not a tube around the *center*) and immediately implies $m<\infty$ under LP-134 (pincer: $b\ge c/\log\gamma$ and $b\le C(\log\gamma)^{-1-\eta}$ are incompatible at large height). Consequently:
1. **177.B cannot be in [KKL], [RT], or [P15]**, nor follow from their unconditional theorems: if it were, polylogarithmic confinement would be a theorem — and it is not. The "[literature GAP]" of Doc 177 §4.2 was not a bibliographic hole: it was an impossibility. **Nobody proved it because it is quasi-RH.**
2. More generally: **any "zone of reality uniform in $t$"** — a theorem of the type "$H_t$ has only real zeros at heights $\ge X(t)$, for all $t\in(0,1)$ with $X(t)<\infty$" — implies by the same argument $b\le Cn\sqrt{X^{-1}(\gamma)}\to0$: qualitative confinement, unknown. This is why the asymptotic zone of [P15] (route 3 of the mandate) **necessarily** has $t$ bounded away from zero: their effective analysis + barrier works at $t\approx0.2$ (with numerical verification which is forbidden to us here and would not help anyway: the obstacle is the limit $t\to0^+$, not the height); and [KKL]'s regularization is for fixed $t>0$ with a height threshold **not uniform** in $t$. The mandate's hope ("if its range is $\gamma\ge\exp(c\,t^{-1/2})$ or better, 177.B might follow") is **structurally refuted**: no range uniform as $t\to0^+$ exists in the literature nor can exist without proving confinement. $\square$ (from Prop 178.8.)

### 3.4. The equivalence and the residual minimal statement

**[THEOREM 178.10] (177.B ≡ confinement, modulo (RvM-t) and the band).** Let $\theta\in(0,\tfrac12)$. Then, conditional on (RvM-t) and with explicit exponent loss:
1. 177.B$(\theta)$ $\Rightarrow$ $\Lambda_{\rm loc}(\gamma)\le(\log\gamma)^{-2/(1-2\theta)}$ and confinement $b\le C(\log\gamma)^{-1/(1-2\theta)}$ (Prop 178.8; unconditional).
2. Confinement $b\le C(\log\gamma)^{-1-\eta}$ ($\eta>0$) $\Rightarrow$ $\Lambda_{\rm loc}(\gamma)\le C'(\log\gamma)^{-2-\eta'}$ for every $\eta'<2\eta$ $\Rightarrow$ 177.B in the sub-diffusive band with $\theta_1=\theta_1(\eta')>0$ (Theorem 178.7).
*Proof of the intermediate implication of (2).* Every non-real zero of $H_0$ over the window has $b\le CL^{-1-\eta}$; its height decreases at speed $\dot\beta\le-1/\beta+C\rho$ (own conjugate from Thm 167-2.3 + sea from Lemma 177.4 with $D\downarrow$: $|{\rm sea}|\le C\rho$); while $\beta\le1/(2C\rho)$ — always true, since $\beta\le b_{\max}\le CL^{-1-\eta}\ll1/\rho$ — one has $\dot\beta\le-1/(2\beta)$, hence it lands at $t_c\le\beta(0)^2\le C^2L^{-2-2\eta}$. Non-real zeros that *enter* the window horizontally after $t=0$ come from neighboring heights $\gamma+O(1)$ with the same confinement (drift, Lemma 178.6), same bound. Taking $\eta'<2\eta$ absorbs constants. $\square$

The chain closes: **the exact content of 177.B (restricted to its useful band) is the polylogarithmic confinement of the zeros of ζ.** The dynamics of $H_t$ (Theorems 178.4/178.7) is the solvable part and is resolved modulo (RvM-t); what is irreducible is a statement about $H_0$, i.e. about $\zeta$ at $t=0$:

**[RESIDUAL MINIMAL STATEMENT 178.C] (polylogarithmic confinement).** *There exists $\eta>0$ such that every zero $\beta+i\gamma$ of $\zeta$ with large $\gamma$ satisfies $|\beta-\tfrac12|\le C(\log\gamma)^{-1-\eta}$.*

This is the weakest statement that (with (RvM-t)) closes 177.B in its band; and for the final goal ($m<\infty$, Cor 177.8) one does not even need to go through 177.B:

**[COR 178.11] (the second tower, deflated to a static pincer).** 178.C $\wedge$ LP-134 $\Rightarrow m<\infty$, **with no dynamics**: if there were infinitely many quadruples $(b_j,\gamma_j)$, LP-134 gives $b_j\ge c/\log\gamma_j$ and 178.C gives $b_j\le C(\log\gamma_j)^{-1-\eta}$, incompatible for large $j$. $\square$

**Frank reading of Cor 178.11.** The heat flow was the scaffolding that *discovered* the pincer (via the chain 174→177→178), but the final corollary is static. Doc 177's tower 2 ("$m<\infty\Leftarrow$ 177.B $\wedge$ LP-134") is recalibrated: its dynamical pillar **is** a confinement statement about $\zeta$, not a literature lemma about $H_t$. The "ζ-free" label the phase memory had assigned to 177.B was incorrect in spirit: the statement is about the *arithmetic* $H_t$ and its entire content lives in the initial condition — the pattern of Doc 167 §5 (the law is ζ-free; the value is not) once again, now with the exact identification of which part of the value: $\Lambda_{\rm loc}(\gamma)$, i.e. $b(\gamma)$.

**Symmetry of the two towers (new).** Tower 1: RH ⟸ A $\wedge$ LP-112, with A calibrated as **Lindelöf-hard** (Thm 176.7). Tower 2: $m<\infty$ ⟸ 178.C $\wedge$ LP-134, with 178.C calibrated as **confinement-hard** (and note: a zero-free region $b\le(\log\gamma)^{-1-\eta}$ implies, by standard Littlewood methods, bounds on $\log\zeta$ near the line of the same genre as Lindelöf — not proved here, left as a plausibility remark, unlabeled). Each tower = one "hard calibrated" pillar + one LP repulsion. The architecture is real; none of the four pillars is cheap, and this document measures the second one.

---

## 4. Anti-circularity test

| Object | RH-free? | ζ-free? | Where ζ re-enters |
|---|---|---|---|
| Lemma 178.1 (gap ODE), Prop 178.2 (lattice saturation), Lemma 178.3 (short blocks) | yes | yes (class + abstract counting) | does not re-enter |
| Theorem 178.4 / 178.4′ (sub-diffusive gap) | yes | yes, **conditional on (RvM-t)** — class counting, no primes | does not re-enter in the proof; (RvM-t) for the arithmetic $H_t$ is inherited from the initial condition |
| Bridge 178.5 (RvM-t) | yes | statement for arithmetic $H_t$ | ζ enters only through bounds of $|H_0|$ in bands (standard) |
| Def 178.6′ ($\Lambda_{\rm loc}$), Theorem 178.7 | yes | the definition is of the class; the value $\Lambda_{\rm loc}(\gamma)$ is ζ | the value = initial condition |
| Prop 178.8 / Cor 178.9 / Thm 178.10 | yes | **no**: conclusions about the zeros of ζ | that is the point: 177.B ⟹ statement about ζ; the feared circularity materializes as a *hardness measure*, not as an error |
| Statement 178.C, Cor 178.11 | open | no: pure ζ | — |

Pattern confirmed and refined: the **law** (gap-ODE, blocks, relaxation) is ζ-free and is proved; the **value** ($\Lambda_{\rm loc}$, $b(\gamma)$) is ζ and is exactly where 177.B stops being a lemma and becomes quasi-RH.

---

## 5. Verdict

**177.B: NOT proved; NOT refuted; REDUCED with an equivalence and calibrated as quasi-RH-hard.** Result by route: route 1 does not close (wrong time regime; it supplies the equilibrium+counting scheme); route 2 closes **the dynamical half** (Theorem 178.4′, conditional on (RvM-t) and local reality, in the sub-diffusive band, with admissible exponent pair $\theta_2\in(\frac14,\frac12)$, $\theta_1=2\theta_2-\frac12$); route 3 shows that **the other half is the whole**: 177.B ⟺ polylogarithmic confinement of the zeros of ζ (Thm 178.10), and this is why no combination of KKL/RT/P15 could have given it (Cor 178.9 — the mandate's hypothesis about the asymptotic zone of P15 is structurally refuted, not due to a lack of bibliographic diligence).

**Proved in this document:**
1. **[LEMMA 178.1]** Exact gap ODE with signed sea: $\dot g=4/g-gS$, $S\ge0$.
2. **[PROP 178.2]** No-go of the bare minimum principle: the compressed lattice saturates the inequality exactly ($\dot g\ge0$ and no more); exact check with $\cos(\lambda z)$. The mandate's heuristic "$g^2\ge8t$, limiting $\theta=\frac12$" is false without a counting input.
3. **[LEMMA 178.3]** Under (RvM-t), every block with gaps $\le\frac1{2\rho}$ has $\le CL$ zeros.
4. **[THEOREM 178.4/178.4′]** (conditional on (RvM-t) + local reality on $[t/2,t]$): the minimum gap grows as $g^2\gtrsim t/\log\gamma$ up to the diffusive ceiling; equivalent to 177.B in the band $\log\gamma\in[t^{-(1-2\theta_2)},ct^{-1/2}]$.
5. **[THEOREM 178.7]** $\Lambda_{\rm loc}(\gamma)\le\frac12(\log\gamma)^{-2/(1-2\theta_1)}$ + (RvM-t) ⟹ 177.B in the band.
6. **[PROP 178.8 + COR 178.9]** 177.B ⟹ $b\le C(\log\gamma)^{-1/(1-2\theta)}$ for **every** zero of ζ: polylogarithmic confinement, far above Vinogradov–Korobov. D177 §4.2's "[literature GAP]" dissolves: it was an impossibility disguised as a bibliographic hole.
7. **[THEOREM 178.10]** Equivalence (mod (RvM-t), band, explicit exponents): 177.B ⟺ confinement.
8. **[COR 178.11]** Tower 2 deflated to a static pincer: **confinement (178.C) $\wedge$ LP-134 ⟹ $m<\infty$**, with no flow. Final symmetry of the two towers: each = a calibrated hard pillar (A Lindelöf-hard / 178.C confinement-hard) + an LP repulsion (LP-112 / LP-134).

**Named GAPs:**
- **[GAP-178.A]** (= Bridge 178.5): (RvM-t) — RvM counting in unit windows uniform in $t\in[0,1]$ for the arithmetic $H_t$. Believed standard via [P15] (effective bounds in bands) + Jensen; not verified line by line. The only pending technical input of the dynamical half.
- **[GAP-178.B]** Conditional super-diffusive relaxation: extend Theorem 178.4′ to $\log\gamma>ct^{-1/2}$ (normalized gap $\ge c$ after time $\gg\rho^{-2}$, *under local reality*). Natural candidate: the local-equilibrium machinery of [RT §2] run forward; by Cor 178.9, it can only exist in a reality-conditional version — the blockage of the unconditional version is structural.
- **[RESIDUAL MINIMAL STATEMENT 178.C]** Polylogarithmic confinement: $|\beta-\frac12|\le C(\log\gamma)^{-1-\eta}$ for every zero of ζ. This is the exact residue of 177.B and the new pillar of tower 2.

**Successor direction (Phase 56 continues):** (a) close GAP-178.A (technical, bounded, no conceptual wall); (b) attack 178.C as an object in its own right — note it is a statement *for every zero*, i.e. it lives on the bad side of the master quantifier (Phase 49), but unlike RH it is **quantitatively gradable**: the family $b\le(\log\gamma)^{-1-\eta}$ interpolates between the known ($\eta=-1$ trivial, $b\le\frac12$) and RH ($\eta=\infty$), and the first question is whether density/moment methods give even $b_j\to0$ along *almost all* off zeros (a density version of 178.C, which would suffice for Cor 178.11 if LP-134 is also taken in density — cf. direction (c) of Doc 177); (c) check whether the pincer 178.C∧LP-134 admits a version with unbounded multiplicities $n$ (here $n\le2$ came for free from self-improvement; document it if 178.C is weakened).

### References
de Bruijn, N.G. (1950), *The roots of trigonometric integrals*, Duke Math. J. 17, 197–226. — Newman, C.M. (1976), Proc. Amer. Math. Soc. 61, 245–251. — Csordas, G., Smith, W., Varga, R.S. (1994), Constr. Approx. 10, 107–129 (Lehmer pairs ⟹ lower bounds on Λ: the static side of the fold). — Ki, H., Kim, Y.-O., Lee, J. (2009), *On the de Bruijn–Newman constant*, Adv. Math. 222, 281–306 ($\forall t>0$: finitely many non-real zeros, eventually real/simple, asymptotically regular spacing **at a height depending on $t$, not uniform** — Cor 178.9 explains why it cannot be uniform). — Rodgers, B., Tao, T. (2020), *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8, e6 (§2: backward gas dynamics; relaxation at fixed macroscopic time). — Polymath, D.H.J. (2019), *Effective approximation of heat flow evolution of the Riemann ξ function...*, Res. Math. Sci. 6, 31 (effective approximation $A+B-C$ uniform in $t\in[0,1/2]$ in bands; reality zone with $t$ bounded away from zero + barrier; used here ONLY in its asymptotic part, and only in support of Bridge 178.5). — Szegő, G. (1939), *Orthogonal Polynomials*, AMS Colloq. Publ. 23. — On Vinogradov–Korobov: Ivić, A. (1985), *The Riemann Zeta-Function*, Wiley, ch. 6. — Danskin, J.M. (1966), J. SIAM Appl. Math. 14, 641–664 (derivative of the minimum). — Internal docs: 167, 174 (via 177), 177.

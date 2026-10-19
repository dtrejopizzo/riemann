# Document 177 — GAP-174.B decided: the Hermite takeoff constant, the global energy bound, and the forward logic of landings

**Program:** Riemann Hypothesis — Phase 55 (two arrows)
**Mandate:** decide GAP-174.B (Doc 174 §2.3): does backward takeoff satisfy $\beta(t)^2\le 2k|t|(1+o(1))$ with $k$ = local near-collision multiplicity at scale $\sqrt{8|t|}$? Construct/decide; do not audit.
**Prerequisites (certified, not re-derived):** Doc 167 (balance law $\dot I=-2\kappa-D$, $D\ge0$ explicit term by term, Thm 2.3; fold Prop 2.6), Doc 174 (closed quadruple model Thm 174.4; maximum principle Lemma 174.3; perfect lattice = fixed point Prop 174.7; refutation of "$I<\infty\Rightarrow m<\infty$" in the class §3.3; statement of GAP-174.B §2.3), Doc 144 (Hadamard counterexample).
**Contract:** [NEW-DEFINITION] free; [THEOREM]/[PROP]/[LEMMA] complete proof or no label; [GAP] declared. No numerics: everything in closed or asymptotic form with error control.

---

## 0. Conventions

Chart $H_t$ (Polymath 15): $\partial_tH_t=-\partial_z^2H_t$, equivalently $H_{t}=e^{-(t-t_0)\partial_z^2}H_{t_0}$. For $f$ entire of order $<2$ the operator $e^{s\partial_z^2}$ ($s>0$) is the Gaussian convolution
$$\bigl(e^{s\partial_z^2}f\bigr)(z)=\frac{1}{\sqrt{4\pi s}}\int_{\mathbb R}f(z+y)\,e^{-y^2/4s}\,dy=\mathbb E\bigl[f(z+\sqrt{2s}\,Z)\bigr],\quad Z\sim N(0,1),$$
(de Bruijn 1950 §2), so that the **backward in $t$** evolution of $H_{t_0}$ is the gaussian running "forward": $H_t=e^{\sigma\partial_z^2}H_{t_0}$ with $\sigma:=t_0-t>0$. Simple-zero dynamics: $\dot z_k=2\sum'_{j\ne k}(z_k-z_j)^{-1}$ in $t$; in backward time $\sigma$ the signs flip. Upper zeros $z_k=\alpha_k+i\beta_k$, $\beta_k>0$; $I=\sum\beta_k^2$. Local density $\rho$ = zeros per unit length in the window ($\rho\asymp\frac1\pi\log\gamma$ for ζ in the $H$ chart).

**Scale invariance of the takeoff constant.** Under $z\mapsto\lambda z$, $t\mapsto\lambda^2t$ the dynamics is invariant and $\beta^2/|t|$ is invariant: any constant $c$ in a law $\beta^2=c\,|t|$ is the same in the $H$ chart and in the ζ chart ($b_\zeta=\beta/2$, $\tau_\zeta=t/4$). The constants in this document need no conversion.

**Multiplicity convention.** We work with $n$ := **number of zeros of the ancestor cluster** (the real zeros that collapse backward). The statement of GAP-174.B uses $k$ ambiguously ($k$ conjugates in §2.3(b) of Doc 174, i.e. $n=2k$; or $k=n-1$ if calibrated with the pair $n=2$, $k=1$). We decide this in the clean variable $n$ and translate at the end: **under either reading, the constant $2k$ is refuted for $n\ge3$.**

---

## 1. The exact local model: the collapse is Hermite and the constant is $c(n)=4\,h_{\max}(n)^2$

### 1.1. Multiple takeoff in closed form

**[THEOREM 177.1] (exact multiple takeoff; the self-similar Hermite solution).** Let $H_{t_{\rm col}}(z)=(z-x_0)^n$ locally (backward collision of $n$ real zeros at $x_0$ at time $t_{\rm col}$; the pure isolated case). Then for $\sigma=t_{\rm col}-t>0$ (backward),
$$H_t(z)\;=\;e^{\sigma\partial_z^2}(z-x_0)^n\;=\;(-\sigma)^{n/2}\,H_n\!\Bigl(\frac{z-x_0}{2\sqrt{-\sigma}}\Bigr)\qquad\text{(formal branch; exact polynomial identity)},$$
with $H_n$ the physicists' Hermite polynomial, and the zeros are **exactly**
$$z_j(t)\;=\;x_0+2i\sqrt{\sigma}\,h_j,\qquad j=1,\dots,n,$$
where $h_1<\dots<h_n$ are the (real, symmetric) zeros of $H_n$. That is: the cluster takes off **vertically, stacked over the line $\mathrm{Re}\,z=x_0$**, in $\lfloor n/2\rfloor$ conjugate pairs at heights $2\sqrt\sigma\,h_j$ (plus one zero remaining real if $n$ is odd), with self-similar profile $\propto\sqrt\sigma$. In particular
$$\boxed{\;\beta_{\max}(t)^2\;=\;c(n)\,\sigma,\qquad c(n):=4\,h_{\max}(n)^2\;}$$
where $h_{\max}(n)$ is the largest zero of $H_n$. Forward ($t>t_{\rm col}$) the same identity gives the $n$ **real** zeros $x_0+2\sqrt{t-t_{\rm col}}\,h_j$: the cluster's landing creates the real Hermite fan.

*Proof.* The semigroup identity: by rescaling $z=\lambda u$, $\partial_z=\lambda^{-1}\partial_u$, and the classical identity $e^{-\partial_x^2/4}x^n=2^{-n}H_n(x)$ (equivalent to Rodrigues' formula via the Weierstrass transform; Szegő 1939, (5.5.7)), one gets $e^{s\partial_z^2}z^n=(-s)^{n/2}H_n\bigl(z/(2\sqrt{-s})\bigr)$ for all $s\in\mathbb C$ (both sides are polynomials in $z$ whose coefficients are polynomials in $s$: the identity for $s<0$ extends algebraically; direct check: $n=2$ gives $z^2+2s$, $n=3$ gives $z^3+6sz$, zeros $0,\pm i\sqrt{6\sigma}$ with $s=\sigma>0$ ✓). The zeros of $H_n(w)$ are real and simple; with $w=(z-x_0)/(2\sqrt{-\sigma})=(z-x_0)/(2i\sqrt\sigma)$, $H_n(w)=0\iff z=x_0+2i\sqrt\sigma h_j$. $\square$

**Cross-check (power moment).** For the backward dynamics of a degree-$n$ polynomial: $\frac{d}{d\sigma}\sum_kz_k^2=-2\sum_k\sum_{j\ne k}\frac{z_k\cdot 2}{z_k-z_j}\cdot\frac12\dots$ — cleanly: $\sum_k z_k\dot z_k\big|_{\rm backward}=-2\sum_{k\ne j}\frac{z_k}{z_k-z_j}=-2\cdot\binom n2$ (symmetrizing $z_k/(z_k-z_j)+z_j/(z_j-z_k)=1$), so $\frac{d}{d\sigma}\sum z_k^2=-2n(n-1)$. In the model: $\sum_jz_j^2=-4\sigma\sum_jh_j^2=-4\sigma\cdot\frac{n(n-1)}2=-2n(n-1)\sigma$ ✓ (the sum of squares of the zeros of $H_n$ is $n(n-1)/2$, from the sub-leading coefficient of $H_n$). Exact consistency.

### 1.2. The exact constant: table and asymptotics

$$c(2)=2,\qquad c(3)=6,\qquad c(4)=2\,(3+\sqrt6)\approx10.90,\qquad c(5)=2\,(5+\sqrt{10})\approx16.32,$$
(from $H_2=4x^2-2$, $H_3=8x^3-12x$, $H_4=16x^4-48x^2+12$, $H_5=32x^5-160x^3+120x$). Asymptotics (Plancherel–Rotach 1929; Szegő 1939 §6.32): $h_{\max}(n)=\sqrt{2n+1}+2^{-1/3}(2n+1)^{-1/6}a_1+o(n^{-1/6})$ with $a_1\approx-2.3381$ the first Airy zero, so
$$\boxed{\;c(n)\;=\;8n+4-2^{8/3}|a_1|\,(2n+1)^{1/3}+O(n^{-1/3})\;=\;8n\,\bigl(1+O(n^{-2/3})\bigr).\;}$$
Convergence to $8n$ is slow ($c(n)/n=1,2,2.72,3.26,\dots\to8$), but the **bound** $c(n)\le 8n+4$ holds for all $n$ (since $h_{\max}(n)<\sqrt{2n+1}$, a classical bound on Hermite zeros).

### 1.3. REFUTATION of the original statement's constant $2k$

**[PROP 177.2] (the constant of GAP-174.B is false for $n\ge3$).** In the reading $k=n-1$ (calibrated with the pair: $n=2$, $k=1$, $\beta^2=2\sigma$ ✓), the trident $n=3$ gives exactly $\beta^2=6\sigma>2k\sigma=4\sigma$. In the reading $n=2k$ of Doc 174 §2.3(b), the quadruple $n=4$ ($k=2$) gives $\beta_{\max}^2=(6+2\sqrt6)\sigma\approx10.90\,\sigma>4\sigma$. Asymptotically the true constant is $\sim8n$ ($=16k$ in the $n=2k$ reading): **a factor of 8 over the conjectured one**. $\square$ (This is Theorem 177.1 with the table of §1.2.)

**Why the heuristic of Doc 174 §2.3(b) failed.** That one counted only the $k$ conjugates at distance $\approx2\beta$ (each contributing $\lesssim1/\beta$ to $\dot\beta$), **assuming the $k$ pairs at the same height**. The real takeoff is stacked at distinct heights ($2\sqrt\sigma h_j$, distinct $h_j$), and backward **the zeros on the same side push the top one upward** (the sign of the forward attraction flips; exact algebra in §2.3). The top zero sits at the edge of the Hermite gas semicircle and receives the coherent push of the whole cluster: this produces $8n$, not $2n$. The structure of the statement (linear in $|t|$, linear in multiplicity) **survives**; the constant is corrected.

### 1.4. The model with remainder: error control

**[PROP 177.3] (stability of the model).** Let $H_{t_{\rm col}}=(z-x_0)^nG(z)$ with $G$ entire of order $<2$, $G$ with no zeros in $|z-x_0|\le d$ and $|G'/G|\le C_G/d$ in $|z-x_0|\le d/2$ (in the class, $C_G/d\lesssim\rho$ by RvM, with $\rho$ the local density plus the far-gas term). Then for $\sqrt\sigma\,\sqrt n\ll d$ the $n$ zeros of $H_t$ near $x_0$ are at distance $O\bigl(\sqrt{n\sigma}\cdot\frac{\sqrt{n\sigma}}{d}\bigr)$ from those of the model $x_0+2i\sqrt\sigma h_j$; in particular
$$\beta_{\max}(t)^2\;=\;c(n)\,\sigma\,\Bigl(1+O\bigl(\tfrac{\sqrt{n\sigma}}{d}\bigr)\Bigr).$$

*Proof (full outline).* Gaussian representation: $H_t(x_0+\zeta)=\mathbb E\bigl[(\zeta+\sqrt{2\sigma}Z)^n\,G(x_0+\zeta+\sqrt{2\sigma}Z)\bigr]$. On the scale $|\zeta|\le A\sqrt{n\sigma}$, write $G(x_0+\cdot)=G(x_0)\,(1+r(\cdot))$ with $|r(y)|\le C|y|/d$ for $|y|\le d/2$; the Gaussian tail $|y|>d/2$ contributes a relative $O(e^{-cd^2/(n\sigma)})$ (here order $<2$ enters to dominate $G$ in the tail). Then $H_t(x_0+\zeta)=G(x_0)\bigl[P_\sigma(\zeta)+E(\zeta)\bigr]$ with $P_\sigma=e^{\sigma\partial^2}\zeta^n$ and $|E|\le C'\frac{\sqrt{n\sigma}}{d}\max_{|\zeta'|\asymp|\zeta|}|P_\sigma|$ on circles avoiding the zeros of $P_\sigma$ by distance $\gtrsim\sqrt\sigma$ (the rescaled Hermite zeros are $\sqrt\sigma$-separated except for the local density factor of the semicircle, $\sqrt\sigma/\sqrt n$ in the bulk — take adapted circles). Rouché gives the announced zero bijection with the stated displacement. $\square$

---

## 2. The three global obstructions

### 2.1. (i) The far sea: the vertical push is absolutely convergent and $O(\rho)$

**[LEMMA 177.4] (sea bound).** Let $z=\alpha+i\beta$ be an upper zero and $S\subset Z$ the zeros at distance $\ge D$ from $z$, with local RvM density $\rho$ and band $|\mathrm{Im}|\le1$. The contribution of $S$ to $d\beta/d\sigma$ is, in absolute value,
$$\Bigl|2\sum_{w\in S}\frac{\beta-\mathrm{Im}\,w}{|z-w|^2}\Bigr|\;\le\;C\,(\beta+1)\,\frac{\rho}{D}\,\bigl(1+O(\tfrac1{\rho D})\bigr),$$
and if $S$ is **all** of the real sea ($D\downarrow0$ excluding the cluster): $\le C\rho$ uniformly in $\beta$.

*Proof.* The imaginary part of $\sum 1/(z-w)$ is absolutely convergent under RvM (numerator bounded by $\beta+1$, denominator $\ge\max(D,|{\alpha-\mathrm{Re}\,w}|)^2$): $\sum_{|x-\alpha|\ge D}\frac{\beta+1}{(x-\alpha)^2}\approx(\beta+1)\rho\int_D^\infty\frac{ds}{s^2}=(\beta+1)\frac\rho D$ (the correction from logarithmic density growth is absorbed into $C$). For the full sea: $\sum_x\frac{\beta}{(\alpha-x)^2+\beta^2}\le\rho\bigl(\#\{|x-\alpha|\le\beta\}\cdot\frac1\beta\cdot\frac1\rho+\int_\beta^\infty\frac{\beta\,ds}{s^2}\bigr)\le C\rho$. $\square$

**Reading.** The far sea contributes to $\frac{d}{d\sigma}\beta^2$ at most $C\rho\beta$: integrated, a **multiplicative** correction $1+O(\rho\sqrt{c(n)\sigma})$ over the local law. It is harmless exactly in the range $\sigma\ll1/(n\rho^2)$ — for ζ at height $\gamma$: $|t|\ll(n\log^2\gamma)^{-1}$. Outside that range the window $\sqrt{8|t|}$ contains $\gtrsim\rho\sqrt{|t|}$ zeros and the current multiplicity $n(t)$ grows: the correct statement is local-in-$|t|$ with $n=n(t)$ (§2.2).

### 2.2. (ii) Backward merging of clusters: $n$ must be the multiplicity at current scale — and the bound's quadratic form makes it monotone under merging

Backward, two clusters at distance $\Delta$ interact appreciably when $\sqrt{n\sigma}\gtrsim\Delta$: from then on they count as one ($n_{\rm tot}=n_1+n_2$). This **does not break** the statement, for two reasons:

1. **The correct definition is at current scale**: $n(t):=\#\{\text{zeros in the window of radius }A\sqrt{c(n)\,|t|}\text{ around the pair}\}$ (self-consistent by dyadic pigeonhole: the smallest admissible radius exists). This was already in the GAP-174.B statement ("at scale $\sqrt{8|t|}$"); here it is confirmed to be mandatory, not optional.
2. **Superadditivity**: any bound of the form $\beta_{\max}^2\le G(n)\,\sigma$ with $G$ superadditive ($G(n_1)+G(n_2)\le G(n_1+n_2)$) glues monotonically across a merge at $\sigma_*$: $I_{\rm tot}(\sigma)\le\sum_iG(n_i)\sigma_*+G(n_{\rm tot})(\sigma-\sigma_*)\le G(n_{\rm tot})\,\sigma$. Both $G(n)=c(n)\approx8n$ and the $G(n)=2n^2$ of Theorem 177.6 are superadditive. The merge is quantitatively realized in the exact model of §2.3: two stacked pairs asymptotically converge to the 4-cluster law, $c(4)\sigma$.

### 2.3. (iii) Stacking: exact algebra, closed solution, and the quantified "theft"

**The requested algebra.** Two pairs at the same abscissa $\gamma$, heights $0<\beta_1<\beta_2$ (zeros $\gamma\pm i\beta_1$, $\gamma\pm i\beta_2$; the mirrors at $-\gamma$ contribute $O(\gamma^{-2})$, ignored). Velocity of the upper zero $z=\gamma+i\beta_2$ backward:
$$\frac{d\beta_2}{d\sigma}\;=\;2\Bigl[\frac1{\beta_2-\beta_1}+\frac1{\beta_2+\beta_1}+\frac1{2\beta_2}\Bigr]\;>\;0:$$
the term $\frac2{\beta_2-\beta_1}$ comes from the zero **on the same side** immediately below: forward it attracts it downward, **backward it launches it upward**, almost-singularly if they are stacked close together. *Stacking accelerates the rise.* The question is whether it breaks linearity or exceeds the merged-cluster law. Answer: no — the system is exactly solvable:

**[PROP 177.5] (stacked quadruple, closed solution).** The vertical quadruple $\{\gamma\pm i\beta_1,\gamma\pm i\beta_2\}$ remains vertical (parity of the local polynomial $w^4+aw^2+c$ in $w=z-\gamma$, real coefficients, preserved by the heat flow) and, with $S=\beta_1^2+\beta_2^2$, $P=\beta_1^2\beta_2^2$:
$$\frac{dS}{d\sigma}=12,\qquad\frac{dP}{d\sigma}=2S\qquad\Longrightarrow\qquad S=S_0+12\sigma,\quad P=P_0+2S_0\sigma+12\sigma^2,$$
$$\beta_{2}^2(\sigma)\;=\;\tfrac12\Bigl(S+\sqrt{S^2-4P}\Bigr),\qquad (S^2-4P)'=16S>0.$$
Exact consequences: (a) the discriminant grows — the two pairs **separate** backward, they never merge in height; (b) asymptotically $\beta_2^2=(6+2\sqrt6)\,\sigma\,(1+o(1))=c(4)\,\sigma\,(1+o(1))$: the top pair realizes **exactly** the Hermite law of the merged cluster $n=4$, whatever the initial data; (c) the "energy theft" is real and quantified: of the total budget $dS/d\sigma=12$, the top pair asymptotically takes the fraction $\frac{6+2\sqrt6}{12}=\frac{3+\sqrt6}{6}\approx90.8\%$ and the bottom one $(6-2\sqrt6)\sigma\approx9.2\%$; (d) **unconditional bound at all times**: $\beta_2^2\le S\le S_0+12\sigma$ — never above the additive law of the total cluster.

*Proof.* This is Thm 174.4 with both $w$-quadratic roots real negative ($w_i=-\beta_i^2$), read backward: $a'=12$, $c'=2a$; $S=a$, $P=c$. Verticality: $e^{\sigma\partial^2}$ preserves real coefficients and parity in $w$. (b): $S\sim12\sigma$, $P\sim12\sigma^2$, $\sqrt{S^2-4P}\sim\sqrt{96}\,\sigma$, $\beta_2^2\sim(6+2\sqrt6)\sigma=2(3+\sqrt6)\sigma=4h_{\max}(4)^2\sigma$ ✓. $\square$

**Verdict on (iii):** stacking pushes **upward** backward (the requested sign count), accelerates the top pair's rise above its individual law $2\sigma$, **but never above the merged-cluster law** $c(n_{\rm tot})\sigma$ — and in the exact model it saturates it. The lemma needs no separation hypothesis between pairs *within the same cluster* (the stacking is already inside the Hermite constant); it needs separation only between the cluster and the rest, which is the current-scale definition of §2.2. The ancestor census does not change in nature: the constant changes ($8n$, not $2k$).

---

## 3. From the model to the global theorem: the unconditional energy bound

What can be proved today without Hermite extremality is the **quadratic-in-$n$, linear-in-$\sigma$** version — sufficient for the whole orphan logic.

**[THEOREM 177.6] (universal rise bound, term by term).** Let $J\ni\sigma$ be a backward interval on which the dynamics is defined, with simple zeros, and let $W$ be an admissible cluster: $n=2\kappa_W+r_W$ zeros ($\kappa_W$ upper pairs, $r_W$ real) in a disc of radius $r_W^{\rm geo}$, with the other zeros (incl. the mirror cluster) at distance $\ge D$ and exterior RvM density $\rho$. Let $I_W=\sum_{k\in W,\,\beta_k>0}\beta_k^2$. Then
$$\frac{dI_W}{d\sigma}\;\le\;2\kappa_W\bigl(4\kappa_W+2r_W-3\bigr)\;+\;C\rho\,\frac{I_W+\sqrt{\kappa_WI_W}}{D}\;\le\;2n^2+C\rho\,\frac{I_W+\sqrt{nI_W}}{D},$$
and while $C\rho(\sqrt{n^2\sigma}+1)\sigma/D\le\varepsilon$:
$$\boxed{\;\beta_{\max}(\sigma)^2\;\le\;I_W(\sigma)\;\le\;\bigl(I_W(0)+2n^2\sigma\bigr)\,(1+C\varepsilon).\;}$$

*Proof.* This is the balance law of Thm 167-2.3 restricted to $W$ and read backward, bounding each block by its vertical alignment: $\frac{dI_W}{d\sigma}=4\sum_{k\in W\uparrow}\sum_{w\ne z_k}\frac{\beta_k(\beta_k-\mathrm{Im}\,w)}{|z_k-w|^2}$. (1) Own conjugate: $+2$ per mode, total $2\kappa_W$. (2) Cross terms within $W$, symmetrizing ordered pairs as in 167-2.3: each of the four terms is $\frac{(\beta_k\mp\beta_l)^2}{d^2}\le1$ because the corresponding distance dominates the vertical difference/sum ($|z_k-z_l|\ge|\beta_k-\beta_l|$, $|z_k-\bar z_l|\ge\beta_k+\beta_l$, etc.): total $\le8\kappa_W(\kappa_W-1)$. (3) Real zeros of $W$: $4\beta_k^2/|z_k-x|^2\le4$ each: $\le4\kappa_Wr_W$. Internal sum: $2\kappa_W+8\kappa_W(\kappa_W-1)+4\kappa_Wr_W=2\kappa_W(4\kappa_W+2r_W-3)\le2\kappa_W(2n-3)\le2n^2$ (using $2\kappa_W\le n$). (4) Exterior (sea, mirror, antipode): Lemma 177.4 per upper zero, $4\beta_k\cdot C(\beta_k+1)\rho/D$, summed $\le C\rho(I_W+\sqrt{\kappa_WI_W})/D$ (Cauchy–Schwarz). Grönwall with the small term gives the boxed result. $\square$

**Calibrating the slack.** The monomial collapse realizes $\frac{dI_W}{d\sigma}=n(n-1)$ exactly (§1.1, upper half of the moment $2n(n-1)$): the bound $2n^2$ loses at most a factor $\approx2$ **in energy**; in **maximum height** the conjectural truth is $c(n)\approx8n$ (linear), and the proved bound $2n^2$ is quadratic because it allows all the cluster's energy to concentrate in one pair. Closing that gap is:

**[GAP-177.A] (Hermite extremality — the precise remainder of GAP-174.B).** *For every admissible cluster of $n$ zeros (arbitrary initial geometry with $I_W(0)=0$, i.e. all real in a window of width $w_0$), does $\beta_{\max}(\sigma)^2\le c(n)\,\sigma\,(1+O(w_0/\sqrt\sigma)+o(1))$ hold with $c(n)=4h_{\max}(n)^2$, i.e. is the monomial collapse (= Hermite profile, unique self-similar takeoff) extremal for the maximum height?* Evidence: (a) exact and saturated for $n\le4$ vertical (Prop 177.5(b,d)); (b) the Hermite profile is the equilibrium of the log-gas in a quadratic potential — the self-similar rescaling of the flow — and other data converge to it after the transient; (c) the proved quadratic bound implies it up to a constant for bounded $n$. We have no proof for general $n\ge5$ (the difficulty: a skewed initial datum could transiently overload the top pair; Prop 177.5(d) excludes this in the vertical case $n=4$ via $\beta_2^2\le S$, and the analogue $\beta_{\max}^2\le I_W\le n(n-1)\sigma$ of the exact moment only holds if $\sum\alpha^2$ does not grow — the horizontal transport does not close, GAP-174.D).

---

## 4. The forward logic: landings, near-doubles, and the minimal lemma on $g(t)$

### 4.1. Clean re-derivation of the time chain (correcting the direction)

A non-real pair present at $t=0$ at height $b$ (¬RH scenario): its **backward** history has it higher ($M(t)\ge b^2+2|t|$, Lemma 174.3 inverted) — the takeoff lemma bounds its *competitors* (the pairs with an ancestor), not itself: this is how the orphan is detected (§5). Its **forward** future is a landing at $t_c\in(0,\Lambda]$, and by Theorem 177.6 read from the landing: $b^2=\beta(0)^2\le I_W(0)\le2n^2t_c\,(1+C\varepsilon)$, i.e.
$$t_c\;\ge\;\frac{b^2}{2n^2}\,(1-C\varepsilon),\qquad\text{and by Lemma 174.3:}\quad t_c\le\tfrac12 M(0).$$
**Each landing creates a real near-double**: by the fold (Prop 167-2.6 / 167-1.6), for $t>t_c$ the newborn gap is $g(t)=\Theta(\sqrt{t-t_c})$ (constant $2\sqrt2$ in the isolated case, Calculation 174.6 inverted). This is the direction **stronger** than backward: it needs not the full gap statistics of ζ, but only lower bounds on gaps of $H_t$ for $t>0$ — territory where [KKL] gives unconditional theorems.

### 4.2. What KKL gives and what is missing — the minimal lemma

**Status of the literature (frank).** [KKL 2009] prove, for each **fixed** $t>0$: $H_t$ has finitely many non-real zeros, and the real zeros are eventually simple; moreover (this is the input Rodgers–Tao describe in their introduction) the real zeros of $H_t$ become asymptotically regular — locally like an arithmetic progression with mean spacing — at sufficiently large heights *depending on $t$*. [RT 2020] exploit the reverse: if $\Lambda<0$, the zeros of ζ would be asymptotically locally equispaced, contradicting unconditional count-fluctuation estimates. **[Literature GAP]:** we know of no form in [KKL], [P15], or [RT] that is *quantitative and uniform as $t\to0^+$* of the type "normalized gap $\ge g(t)$ at heights $\ge\Gamma(t)$ with explicit $g,\Gamma$". That is exactly the gap, and we name it:

**[MINIMAL-LEMMA 177.B] (quantitative KKL at the corner $t\to0^+$; not proved here).** *There exist $\theta\in(0,\tfrac12)$ and $c>0$ such that, for the arithmetic $H_t$ and every $t\in(0,1)$: every consecutive gap of real zeros of $H_t$ at height $\gamma\ge\Gamma(t):=\exp\bigl(t^{-(1/2-\theta)}\bigr)$ satisfies $g_{\rm norm}:=g\cdot\frac{\log\gamma}{4\pi}\ge c\,t^{\theta}$.*

**Structural plausibility (why $\theta<1/2$ is the natural boundary):** the diffusive relaxation time of the local gap is $\asymp(\text{mean spacing})^2=(4\pi/\log\gamma)^2$; the lemma asks for regularization only when $t\gg(\log\gamma)^{-2}\iff\gamma\le\exp(t^{-1/2})$ — i.e. **strictly within the regime where heat has already had time to act**. The threshold $\Gamma(t)=\exp(t^{-(1/2-\theta)})$ lies below $\exp(t^{-1/2})$: the lemma is the quantitative form of "gaps relax diffusively," the same mechanism [P15] uses numerically and [RT] use at $t<0$. It is not a statement about ζ at $t=0$: it is dynamics of $H_t$ in the interior, the good side.

### 4.3. The conditional theorem: pathology only accumulates at the boundary, and the corner closes with LP-134

**[THEOREM 177.7] (conditional on Lemma 177.B; "landings only accumulate at $t=0^+$," quantified).** Suppose Lemma 177.B. Then every landing at $(t_c,\gamma_c)$ with $t_c\in(0,1)$ satisfies $\gamma_c\le\exp\bigl(C\,t_c^{-(1/2-\theta)}\bigr)$. Consequently: (1) for every $\varepsilon>0$, landings in $[\varepsilon,\Lambda]$ occur in the bounded region $\gamma\le\exp(C\varepsilon^{-(1/2-\theta)})$ — landings **can only accumulate at $t=0^+$** (at interior times this was already forbidden by [KKL]; the new part is the explicit height bound); (2) if $m=\infty$, the infinitely many quadruples $(b_j,\gamma_j)$ have $t_j\to0^+$, $\gamma_j\ge\exp(c\,t_j^{-(1/2-\theta)})$ and, via the forward Theorem 177.6 with $n_j\le C\rho(\gamma_j)\sqrt{n_jt_j}$ (multiplicity at current scale, i.e. $n_j\le C\sqrt{t_j}\log\gamma_j$ unless $n_j\le 2$),
$$b_j^2\;\le\;2n_j^2\,t_j\,(1+o(1))\;\le\;C\,t_j^{2}\log^2\gamma_j\;\le\;C\,(\log\gamma_j)^{2-\frac{4}{1-2\theta}},\qquad\frac{4}{1-2\theta}>4,$$
i.e. $b_j\le(\log\gamma_j)^{-1-\eta}$ with $\eta=\eta(\theta)>0$: **the pathology lives in the corner $(t,b)\to(0,0)$ with super-exponential heights and polylogarithmically small off-heights, below the scale $1/\log\gamma$.**

*Proof.* Landing at $(t_c,\gamma_c)$: by the fold, for $\delta\in(0,t_c]$ the normalized gap at $t_c+\delta$ at height $\gamma_c$ is $\le C\sqrt\delta\,\log\gamma_c$. If $\gamma_c\ge\Gamma(t_c)$ ($\ge\Gamma(t_c+\delta)$, $\Gamma$ decreasing in $t$), the lemma requires $C\sqrt\delta\log\gamma_c\ge c(t_c+\delta)^\theta$ for all $\delta\le t_c$; with $\delta=t_c$: $\log\gamma_c\ge c't_c^{\theta-1/2}$, i.e. $\gamma_c\ge\exp(c't_c^{-(1/2-\theta)})$ — but then taking $\delta\to0^+$: $C\sqrt\delta\log\gamma_c\ge ct_c^\theta$ fails for $\delta<(ct_c^\theta/C\log\gamma_c)^2>0$: contradiction **unless** $\gamma_c<\Gamma(t_c)$. So every landing has $\gamma_c<\Gamma(t_c)=\exp(t_c^{-(1/2-\theta)})$… and conversely, if $\gamma_c<\Gamma(t_c)$ there is no restriction: the valid bound is $\gamma_c\le\Gamma(t_c)$, which is (1). [Sign note: the lemma forbids small gaps *above* $\Gamma$; the landing creates arbitrarily small gaps right after $t_c$; hence the landing site is *below* $\Gamma(t_c)$.] For (2): $m=\infty$ with [KKL] ($\kappa(\varepsilon)<\infty$ for all $\varepsilon$) forces $t_j\to0^+$; and if moreover $\gamma_j\to\infty$ (at bounded heights only finitely many quadruples fit, by local finiteness), the chain with $t_j\ge\Gamma^{-1}$-dual: $\gamma_j\le\exp(t_j^{-(1/2-\theta)})$ gives $t_j\le(\log\gamma_j)^{-\frac{2}{1-2\theta}}$, and the forward takeoff bound ($b_j^2\le2n_j^2t_j$, Theorem 177.6 from the landing, valid in the far-sea range: $t_j\ll(n_j\log^2\gamma_j)^{-1}$, which the chain itself guarantees a posteriori) with $n_j\le\max(2,C\sqrt{t_j}\log\gamma_j)$ gives the exponent. $\square$

**Required double consistency (why doesn't this contradict the refutation of Doc 174 §3.3?).** The Hadamard counterexample ($m=\infty$, $I<\infty$; $\gamma_j=2^j$, $b_j=e^{-\gamma_j}$, $t_j\approx b_j^2/2$) has $\log\gamma_j=j\log2$ while $\exp(t_j^{-(1/2-\theta)})$ is a gigantic tower: its landings occur **far below** the threshold $\Gamma(t_j)$ — Lemma 177.B does not forbid them (consistent with the class ✓), and its $b_j=e^{-\gamma_j}\ll(\log\gamma_j)^{-1-\eta}$ comfortably satisfy the corner of Theorem 177.7 ✓. And note: the counterexample **violates LP-134** ($b_j\log\gamma_j\to0$). This shows that the two following pieces are both necessary and that the cut is correctly made:

**[COR 177.8] (conditional closure of the finiteness half).** *Lemma 177.B ($\theta<\tfrac12$) $\;\wedge\;$ LP-134 ($\liminf b\cdot\log\gamma>0$ over quadruples of ζ) $\;\Longrightarrow\;m<\infty$.* Indeed: if $m=\infty$, Theorem 177.7(2) gives $b_j\log\gamma_j\le(\log\gamma_j)^{-\eta}\to0$, contradicting LP-134 for large $j$. $\square$

**Frank reading of Cor 177.8.** This is not a proof of $m<\infty$: LP-134 is a conjectural repulsion (and Lemma 177.B is open). It is the **new weld**: the dynamical half (177.B: gaps of $H_t$ in the interior, $t>0$, where theorems exist) + the minimal arithmetic half (LP-134: axis repulsion at $t=0$) imply finiteness. Compared to the pre-177 state: the arithmetic half shrank from "full gap statistics of ζ" to **a single polylogarithmic repulsion**, and the missing dynamics is a diffusive-regularization statement about $H_t$, not about ζ. This is strictly better than the backward census of Doc 174 (which needed the full concentration function $\nu(\delta,T)$).

---

## 5. The orphan theorem (with the corrected constant)

**[NEW-DEFINITION 177.9] (orphan, quantitative).** A non-real pair at time $t<0$ with height $\beta$ and current-scale multiplicity $n(t)$ is an **orphan of order $\varepsilon$** if $\beta^2>(1+\varepsilon)\,2n(t)^2\,|t|$. (With GAP-177.A proved, the constant improves to $c(n(t))\approx 8n(t)$.)

**[THEOREM 177.10] (orphan dichotomy; conditional only on the separation hypothesis of Thm 177.6 on the stretch $(t,0)$).**
1. **(RH ⟹ no orphans.)** If $Z_0$ is real and on $(t,0)$ the backward dynamics is defined with admissible clusters (separation at current scale, §2.2), every non-real pair at time $t$ took off from an ancestor cluster of $n(t)$ real zeros in its window and satisfies $\beta(t)^2\le2n(t)^2|t|\,(1+C\varepsilon)$: there are no orphans of order $>C\varepsilon$. The ancestor is locatable: a group of gaps with $g\lesssim\sqrt{2n^2|t|}$ in the real configuration.
2. **(¬RH-finite ⟹ orphans for all $t\to0^-$.)** If $0<I(0)<\infty$ with $m\ge1$ inherited quadruples of heights $b_j$, then for $|t|<\dfrac{b_{\max}^2}{4\,n(t)^2}$ the tallest quadruple is an orphan of order $\ge1$: its backward height satisfies $\beta(t)^2\ge b_{\max}^2>2\,n(t)^2|t|\cdot2$, unreachable from any local ancestor. Since $n(t)\le\max(2,C\rho\sqrt{|t|})$, the detection window is $|t|\lesssim\min\bigl(b_{\max}^2,\;\rho^{-2}\bigr)$: non-empty.
3. Consequently, modulo the separation hypothesis: **¬RH-with-finite-$I$ $\iff$ orphans exist for all sufficiently small $t<0$**, and the arithmetic half of the backward bridge is the ancestor census = concentration function $\nu(\delta,T)$ of gaps of the real configuration — with the corrected threshold $\delta\asymp\sqrt{2n^2|t|}$ (not $\sqrt{8|t|}$: the census must count **quadratically weighted clusters**, not individual gaps).

*Proof.* (1) is Theorem 177.6 with $I_W(t^*)=0$ at the takeoff $t^*\in(t,0)$, plus monotone merging (§2.2). (2): $\beta_{\max}(t)^2\ge\beta_{\max}(0)^2=b_{\max}^2$ does not hold zero-to-zero (individual heights are not monotone), but it does for the maximum: $M(t)\ge M(0)+2|t|\ge b_{\max}^2$ (Lemma 174.3 backward); the carrier of $M$ is the orphan. (3): combine (1)+(2) with the definition. $\square$

**What changes relative to Doc 174 §2.3:** the logic survives intact; what changes are (a) the threshold's constant ($2n^2$ proved; $8n$ conjectural-Hermite; never $2k$), (b) the census window's scale, (c) and — most importantly — the **forward route of §4 is strictly more economical** than this backward census: it needs only LP-134 from arithmetic instead of full $\nu(\delta,T)$. Backward remains as the conceptual characterization (what ¬RH-finite dynamically *is*: orphans); forward as the proof route.

---

## 6. Anti-circularity test

| Object | RH-free? | ζ-free? | Where ζ re-enters |
|---|---|---|---|
| Thm 177.1 (exact Hermite, $c(n)$), Prop 177.2 (refutation of $2k$), Prop 177.5 (closed stacking) | yes | yes | does not re-enter |
| Lemma 177.4 (sea), Thm 177.6 (bound $2n^2$), Thm 177.10 (orphans) | yes | yes (class + RvM) | does not re-enter |
| Thm 177.7 / Cor 177.8 | yes | **no**: Lemma 177.B is about the arithmetic $H_t$; LP-134 is ζ | ζ enters through (i) diffusive regularization of $H_t$ at $t>0$ and (ii) LP-134 repulsion at $t=0$ — two separate and minimal entries |
| GAP-177.A (Hermite extremality) | yes | yes | does not re-enter; pure particle dynamics |

No primes in any proof. The pattern of Docs 167/174 persists: the law is ζ-free; arithmetic enters through the initial condition — and this document reduces it to its known minimal form (LP-134 + an interior lemma).

---

## 7. Verdict

**GAP-174.B: REFUTED in its constant, PARTIALLY-PROVED in its structure.**

1. **[THEOREM 177.1 + PROP 177.2] (local model resolved; refutation of the constant).** Multiple takeoff from a near-collision of $n$ real zeros is exactly self-similar-Hermite: heights $2\sqrt{|t-t_{\rm col}|}\,h_j$, $h_j$ = zeros of $H_n$, and $\beta_{\max}^2=c(n)|t-t_{\rm col}|$ with $c(n)=4h_{\max}(n)^2=8n+4-2^{8/3}|a_1|(2n+1)^{1/3}+O(n^{-1/3})$; exact table $c(2)=2$, $c(3)=6$, $c(4)=2(3+\sqrt6)$, $c(5)=2(5+\sqrt{10})$. The constant $2k$ of the original statement is false from $n=3$ on (asymptotic factor 8): the heuristic of Doc 174 ignored that backward the zeros on the same side push upward (stacking).
2. **[THEOREM 177.6 + PROP 177.5] (proved global bound, with a current-scale separation hypothesis).** Unconditionally in the class: $\beta_{\max}(\sigma)^2\le I_W(\sigma)\le2n^2\sigma(1+C\varepsilon)$ for admissible clusters, with monotone backward merging (superadditivity) and a controlled far sea ($O(\rho)$, absolutely convergent). Stacking accelerates but never exceeds the merged-cluster law (closed solution of the vertical quadruple: the top pair steals $90.8\%$ of the energy and exactly saturates $c(4)\sigma$). Left open: **[GAP-177.A]**: lowering from $2n^2$ to $c(n)\approx8n$ in general (Hermite extremality) — desirable but **not necessary** for the orphan logic nor for Cor 177.8.
3. **[THEOREM 177.10] (orphans, closed modulo separation):** ¬RH-with-finite-$I$ ⟺ backward orphan pairs, with threshold $2n(t)^2|t|$ and quadratically weighted ancestor census.
4. **[THEOREM 177.7 + COR 177.8] (the most valuable finding: the forward route is stronger).** Each landing creates a near-double on the real side; with the **[MINIMAL-LEMMA 177.B]** (quantitative KKL: normalized gaps of $H_t\ge ct^\theta$, $\theta<\tfrac12$, at heights $\ge\exp(t^{-(1/2-\theta)})$ — exactly the diffusive-relaxation regime, [literature GAP]: not located in KKL/P15/RT), landings only accumulate at $t=0^+$ with super-exponential heights and $b_j\le(\log\gamma_j)^{-1-\eta}$; and **177.B $\wedge$ LP-134 $\Rightarrow m<\infty$**. The arithmetic half of the bridge drops from "full gap statistics of ζ" to "a single polylogarithmic repulsion of the axis (LP-134)." Double consistency verified against the counterexample of Doc 144/174 (violates LP-134 and lives below the threshold $\Gamma$: both pieces necessary, neither redundant).

**Direction for Phase 56:** (a) attack Lemma 177.B with the techniques of [RT §2]/[P15] (local relaxation of the gas at $t>0$, uniform at the diffusive corner) — this is dynamics of $H_t$, not arithmetic of ζ; (b) GAP-177.A via a rearrangement inequality on the log-gas (extremality of the Hermite equilibrium); (c) check whether LP-134 admits an averaged form sufficient for Cor 177.8 (the argument only uses large $j$ along the sequence of quadruples: LP-134 in density 1 would suffice).

### References
de Bruijn, N.G. (1950), *The roots of trigonometric integrals*, Duke Math. J. 17, 197–226 (§2: Gaussian representation; Thm 13: decreasing band). — Csordas, G., Smith, W., Varga, R.S. (1994), *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis*, Constr. Approx. 10, 107–129 (near-doubles at $t=0$ ⟹ lower bounds on Λ: the static arithmetic version of the forward fold). — Ki, H., Kim, Y.-O., Lee, J. (2009), *On the de Bruijn–Newman constant*, Adv. Math. 222, 281–306 (Λ<1/2; $\forall t>0$ finitely many non-real zeros, eventually real and simple; asymptotic spacing regularization for fixed $t>0$ — **the quantitative uniformity as $t\to0^+$ that Lemma 177.B requires is not stated there as far as we know: [literature GAP]**). — Rodgers, B., Tao, T. (2020), *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8, e6 (Λ≥0 via: $\Lambda<0$ would force local equispacing of the zeros of ζ, against unconditional count-fluctuation estimates). — Polymath, D.H.J. (2019), Res. Math. Sci. 6, 31. — Szegő, G. (1939), *Orthogonal Polynomials*, AMS Colloq. Publ. 23 ((5.5.7); §6.32: bounds and Plancherel–Rotach asymptotics of Hermite zeros). — Plancherel, M., Rotach, W. (1929), Comment. Math. Helv. 1, 227–254. — The identity "heat on polynomials = rational Calogero motion of roots" and Hermite self-similarity are folklore (cf. Tao's expositions around [RT]); the use here (takeoff constant $c(n)$, closed stacked quadruple, term-by-term bound $2n^2$, weld 177.B∧LP-134⟹m<∞) we do not know published. — Internal docs: 144, 167, 168, 170, 174.

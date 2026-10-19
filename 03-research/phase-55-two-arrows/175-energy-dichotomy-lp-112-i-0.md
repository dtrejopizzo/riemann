# Document 175 — The energy dichotomy: LP-112 ⟹ I ∈ {0, ∞}

**Program:** Riemann Hypothesis — Phase 55 (two arrows)
**Mandate:** formalize and prove the energy dichotomy — that ζ's self-approximation (LP-112) forces $I\in\{0,\infty\}$ —, quantifying the Rouché–Hurwitz replica (the replica copies the *distance to the line*, not just the zero); explore the replication-density ↔ Theorem 170.5 bridge; frank status of LP-112; portrait of the finite-energy state.
**Prerequisites read at source:** Doc 112 complete (LP-112, LP-112⁻, Theorem 2.3, Prop. 2.6, Obs. 2.4, §2.6), Doc 113 (LP-112 against the literature; Bohr 1922; Bagchi's support), Doc 170 (coordinates, Theorem 170.5, Cor. 170.6, Thm 170.8, §5 envelope), Doc 172 (header, verdict: the $T/\log T$ envelope = noise floor).
**Contract:** [NEW-DEFINITION] free; [THEOREM]/[PROP]/[LEMMA] complete proof or no label; [GAP] declared with statement form. A false victory is worse than failure.

**Coordinates (identical to Doc 170).** Off-critical zero $\rho=\tfrac12+b+i\gamma$ with $b\in(0,\tfrac12)$, $\gamma>0$; one representative per quadruple $\{\rho,\bar\rho,1-\rho,1-\bar\rho\}$ (the one in the upper-right half-plane). Energy:
$$I \;=\; I(0^+)\;:=\;\sum_j b_j^2,\qquad E(T):=\sum_{\gamma_j\le T} b_j^2 .$$
$I=0$ ⟺ no off zeros ⟺ RH. $N(\sigma,T)$ = number of zeros with $\beta\ge\sigma$, $0<\gamma\le T$. Note: every zero has $\beta<1$ (Hadamard–de la Vallée Poussin), so $b\in(0,\tfrac12)$ strictly and there is always slack on both sides within the open strip $\{\tfrac12<\sigma<1\}$.

---

## 0. Executive summary and verdict

**THE THEOREM WAS PROVED** (conditional on LP-112, declared as such):

1. **[THEOREM 175.2]** LP-112 ⟹ $I\in\{0,\infty\}$. Stronger: the weak version LP-112⁻ suffices (a single $\tau$ for each $(D,\varepsilon)$), via a summable-radii induction ([COR 175.4]); and **fixed precision** $\varepsilon<\eta$ (no need for $\varepsilon_k\to0$) in **a single disc** (that of the off zero) suffices ([Obs. 175.3]). The mechanism: the Rouché–Hurwitz replica copies the abscissa with error $\le\delta(\varepsilon)\le C\varepsilon^{1/m_0}\to0$ ([LEMMA 175.1], quantified with multiplicity), so each replica contributes $b^2\ge b_0^2/4$ to the energy and the sum diverges.
2. **New architecture (strict improvement over P44/D112):** $\mathrm{RH}\;\Longleftarrow\;\bigl(I(0^+)<\infty\bigr)\;\wedge\;\mathrm{LP\text{-}112}$. It is strictly weaker than the old $(m<\infty)\wedge$LP-112 because $m<\infty\Rightarrow I<\infty$ and the converse is false ($b_j=1/j$ gives $m=\infty$, $I<\infty$). Moreover the energy dichotomy **implies** the cardinal dichotomy (D-109): $I\in\{0,\infty\}\Rightarrow m\in\{0,\infty\}$.
3. **[THEOREM 175.6] (unconditional, the new bridge):** if ζ has an off zero $\rho_0$ with abscissa $\tfrac12+b_0$, the set $A_\varepsilon$ of good self-approximation shifts in the zero's disc satisfies, for every $\varepsilon<\eta$,
$$\mathrm{meas}\bigl(A_\varepsilon\cap[0,T]\bigr)\;\ll\; r\,T^{1-b_0/8}\log T \quad\text{and}\quad \mathrm{meas}\bigl(A_\varepsilon\cap[0,T]\bigr)\;\le\;\frac{8r}{b_0^2}\,E(T+\gamma_0+r)\;\ll\;\frac{r}{b_0^2}\cdot\frac{T}{\log T}.$$
This **improves Prop. 2.6 of Doc 112** (zero density with no rate, via Bagchi's limit theorem) to an explicit, unconditional rate with an elementary proof (Rouché + Selberg density, no distributional machinery). Reading: *the self-approximation of a ζ with an off zero is rare at a quantified rate* — the energy certificate ALREADY limits universality theory. The structural identity: **$E(T)$ counts self-approximation witnesses**: every $2r$-separated set of good shifts has $\#\le 4E(T)/b_0^2$.
4. **[PROP 175.8] (finite-energy state):** if $0<I<\infty$, the good witnesses of ANY off zero form a set of **finite total measure** ($\le 8rI/b_0^2$ over all of $(0,\infty)$) with at most $4I/b_0^2$ separated elements: the finite-energy world is *anti-recurrent* in the window of each off zero, even at fixed precision. $I$ is literally a **witness budget**.
5. **LP-112 remains the only gap** and this document *quantitatively worsens it* (§4): its witnesses, under ¬RH, not only have zero density — they have density $\ll T^{-b_0/8}\log T$. The D112/D113 wall (producing an element of an exceptional set) remains intact and is now sharper.

---

## 1. LP-112: the precise statement, with the disc where it is needed

We reproduce the two versions of Doc 112 §2.2 and isolate the minimal instance this document uses.

**Lemma LP-112 (sequential pointwise almost-periodicity; OPEN — Doc 112).** *For every closed disc $D\subset\{\tfrac12<\sigma<1\}$ there exists a sequence $\tau_k\to\infty$ such that*
$$\sup_{s\in D}\,\bigl|\zeta(s+i\tau_k)-\zeta(s)\bigr|\;\longrightarrow\;0.$$

**Lemma LP-112⁻ (weak version — Doc 112).** *For every closed disc $D\subset\{\tfrac12<\sigma<1\}$ and every $\varepsilon>0$ there exists ONE $\tau>\mathrm{height}(D)$ with $\sup_D|\zeta(s+i\tau)-\zeta(s)|<\varepsilon$.*

**Three clarifications about the disc (the requested frankness):**

(a) *Doc 112's quantifier already covers the zero's height.* LP-112 quantifies over **all** closed discs of the open strip, with no height restriction: in particular over $D=\bar D(\rho_0,r)$ centered at an off zero $\rho_0$ at arbitrary height $\gamma_0$. Nothing needs to be reformulated: the version we use is an *instance* of Doc 112's, not an extension. (If $\rho_0$ fell on the boundary of a given disc, it is replaced by the concentric disc at $\rho_0$ of admissible radius: the strip is open and $0<b_0<\tfrac12$ strict leaves slack on both sides.)

(b) *The minimal instance.* All that Theorem 175.2 needs is:

**[NEW-DEFINITION] LP-112[$\rho_0$] (instance localized at fixed precision).** For the disc $D_0:=\bar D(\rho_0,r)$ of §2 (radius $r=r(\rho_0)$ fixed below) and for ONE fixed $\varepsilon<\eta(r)$, there exists an **unbounded** sequence $\{\tau_k\}$ with $\sup_{D_0}|\zeta(s+i\tau_k)-\zeta(s)|\le\varepsilon$.

LP-112 ⟹ LP-112[$\rho_0$] trivially; LP-112⁻ ⟹ (the conclusion of) LP-112[$\rho_0$] only after the induction of Corollary 175.4 — the weak version gives one $\tau$ per disc, and unboundedness is recovered by changing discs at each step.

(c) *The delicate point is exactly that $D_0$ contains a zero of the target* (§4): if $D$ contains no zeros of ζ, LP-112 on $D$ is a consequence of RH (Bagchi) and, under ¬RH, remains the "generic-friendly" case; with a zero inside, the target leaves the support of Bagchi's measure and everything distributional works AGAINST it (Prop. 2.6 of D112; here Theorem 175.6, with rate).

---

## 2. The energy dichotomy theorem, quantified

### 2.1. Rouché–Hurwitz with rates and multiplicity

**[LEMMA 175.1] (replica with rate).** Let $g$ be holomorphic on a neighborhood of $\bar D(z_0,R)$, with a zero of multiplicity $m_0\ge1$ at $z_0$ and no other zeros in $\bar D(z_0,R)$. For $0<\delta\le R$ let
$$\eta(\delta)\;:=\;\min_{|z-z_0|=\delta}|g(z)|\;>\;0 .$$
Then:

(i) *(Rouché at radius $\delta$)* If $f$ is holomorphic on $\bar D(z_0,R)$ and $\sup_{\bar D(z_0,R)}|f-g|<\eta(\delta)$, then $f$ has **exactly $m_0$ zeros** (with multiplicity) in $D(z_0,\delta)$; in particular at least one zero $z'$ with $|z'-z_0|<\delta$.

(ii) *(explicit rate)* Write $g(z)=c\,(z-z_0)^{m_0}h(z)$ with $c=g^{(m_0)}(z_0)/m_0!\ne0$, $h(z_0)=1$. There exists $\delta_1\in(0,R]$ with $|h|\ge\tfrac12$ on $\bar D(z_0,\delta_1)$, and then $\eta(\delta)\ge\tfrac{|c|}{2}\delta^{m_0}$ for $\delta\le\delta_1$. Defining
$$\delta(\varepsilon)\;:=\;\Bigl(\frac{4\varepsilon}{|c|}\Bigr)^{1/m_0},$$
for every $\varepsilon\le\tfrac{|c|}{4}\delta_1^{m_0}$ and every $f$ with $\sup_{\bar D(z_0,R)}|f-g|\le\varepsilon$, $f$ has exactly $m_0$ zeros in $D\bigl(z_0,\delta(\varepsilon)\bigr)$. The replica is at distance $\le\delta(\varepsilon)=C\varepsilon^{1/m_0}\to0$ as $\varepsilon\to0$.

*Proof.* (i): on the circle $|z-z_0|=\delta$ we have $|f-g|\le\sup_{\bar D(z_0,R)}|f-g|<\eta(\delta)=\min_{|z-z_0|=\delta}|g|\le|g|$; Rouché's theorem ([T39, §3.42]; [C78, VIII.3]) applied to the pair $(g,\,f-g)$ on that circle gives that $f=g+(f-g)$ has in $D(z_0,\delta)$ the same number of zeros with multiplicity as $g$, namely $m_0$ (the zero $z_0$ counted $m_0$ times; there are no others by hypothesis). (ii): $h:=g/(c(z-z_0)^{m_0})$ extends holomorphically with $h(z_0)=1$; by continuity there is $\delta_1$ with $|h|\ge\tfrac12$ on $\bar D(z_0,\delta_1)$, whence $|g(z)|\ge\tfrac{|c|}{2}\delta^{m_0}$ on $|z-z_0|=\delta\le\delta_1$. With $\varepsilon\le\tfrac{|c|}{4}\delta_1^{m_0}$ we have $\delta(\varepsilon)\le\delta_1$ and $\eta(\delta(\varepsilon))\ge\tfrac{|c|}{2}\cdot\frac{4\varepsilon}{|c|}=2\varepsilon>\varepsilon$, and (i) applies. $\square$

This is Hurwitz's theorem ([C78, VII.2.5]) in quantitative form: the zeros of the limit attract zeros of the approximants, with multiplicity, at speed $\varepsilon^{1/m_0}$. Multiplicity $m_0\ge1$ does not get in the way: it only slows the rate, and for the dichotomy $\delta(\varepsilon)\le r$ suffices — the rate is not even needed, only the fixed radius (Obs. 175.3).

### 2.2. The theorem

Fix, for an off zero $\rho_0=\tfrac12+b_0+i\gamma_0$ ($b_0\in(0,\tfrac12)$, $\gamma_0>0$), the **zero's constants**:
$$r\;:=\;\tfrac12\min\Bigl(b_0,\;\tfrac12-b_0,\;\mathrm{dist}\bigl(\rho_0,\,Z(\zeta)\setminus\{\rho_0\}\bigr)\Bigr)\;>\;0,\qquad D_0:=\bar D(\rho_0,r),\qquad \eta:=\eta(r)=\min_{|s-\rho_0|=r}|\zeta(s)|>0.$$
($r>0$ because the zeros of ζ are isolated; $D_0\subset\{\tfrac12+\tfrac{b_0}2<\sigma<1\}$ because $r\le b_0/2$ and $r\le\tfrac12(\tfrac12-b_0)$, and $\beta_0=\tfrac12+b_0<1$; ζ does not vanish on $D_0\setminus\{\rho_0\}$.) Note: **no finiteness is assumed** — unlike Theorem 2.3 of D112, which froze the constants with H(m), here the constants belong to ONE zero, and a zero exists as soon as $I>0$. This is why the energy dichotomy is cleaner than the cardinal one.

**[THEOREM 175.2] (energy dichotomy).** *If LP-112 holds (its instance on the disc $D_0$ of a single off zero suffices), then*
$$I(0^+)\;>\;0\;\Longrightarrow\;I(0^+)\;=\;\infty.$$
*Equivalently: LP-112 ⟹ $I\in\{0,\infty\}$.*

*Proof.* Suppose $I>0$: an off zero exists; fix one, $\rho_0$, with its constants $(r,\eta,m_0,c)$ as above, where $m_0$ is the multiplicity of $\rho_0$ and $c=\zeta^{(m_0)}(\rho_0)/m_0!$. Apply LP-112 to the disc $D_0$: there exists $\tau_k\to\infty$ with
$$\varepsilon_k\;:=\;\sup_{s\in D_0}\bigl|\zeta(s+i\tau_k)-\zeta(s)\bigr|\;\longrightarrow\;0 .$$

**Step 1 (replica with controlled abscissa).** Let $k_0$ be such that $\varepsilon_k<\eta$ for $k\ge k_0$. By Lemma 175.1(i) with $g=\zeta|_{D_0}$, $f=\zeta(\cdot+i\tau_k)|_{D_0}$ and $\delta=R=r$: $\zeta(\cdot+i\tau_k)$ has exactly $m_0$ zeros in $D(\rho_0,r)$; equivalently, ζ has $m_0$ zeros (with multiplicity) in $D(\rho_0+i\tau_k,\,r)$. Pick one, $\rho_k$. Then
$$\bigl|\mathrm{Re}\,\rho_k-(\tfrac12+b_0)\bigr|\;<\;r\;\le\;\tfrac{b_0}2\qquad\Longrightarrow\qquad b(\rho_k)\;:=\;\mathrm{Re}\,\rho_k-\tfrac12\;\in\;\bigl(\tfrac{b_0}2,\,\tfrac{3b_0}2\bigr),$$
i.e. $\rho_k$ is an off zero with $b(\rho_k)\ge b_0/2$. More precisely, by Lemma 175.1(ii): for large $k$ ($\varepsilon_k\le\tfrac{|c|}4\delta_1^{m_0}$),
$$\bigl|\rho_k-(\rho_0+i\tau_k)\bigr|\;\le\;\delta(\varepsilon_k)\;=\;\Bigl(\tfrac{4\varepsilon_k}{|c|}\Bigr)^{1/m_0}\;\longrightarrow\;0,\qquad\text{in particular}\qquad b(\rho_k)\;\longrightarrow\;b_0 .$$
**The replica copies the distance to the critical line with error $O(\varepsilon_k^{1/m_0})\to0$** — the director's observation, now quantified. (For divergence of the energy, the coarse version $b(\rho_k)\ge b_0/2$ suffices, which already holds with the fixed radius $r$.)

**Step 2 (the replicas are distinct quadruples).** $\tau_k\to\infty$ carries no lower separation bound, and none is needed: pass to the subsequence defined inductively by $\tau_{k_{j+1}}:=\min\{\tau_k>\tau_{k_j}+2r+1\}$ (it exists because $\tau_k\to\infty$; relabel). Then the intervals $\bigl(\gamma_0+\tau_j-r,\;\gamma_0+\tau_j+r\bigr)$, which contain $\mathrm{Im}\,\rho_j$, are pairwise disjoint and lie above $\gamma_0$ (for $\tau_j>r$). Two members of the same quadruple in the upper half-plane ($\rho$ and $1-\bar\rho$) have the **same** imaginary part; imaginary parts in disjoint intervals force distinct quadruples, all distinct from the quadruple of $\rho_0$.

**Step 3 (the energy diverges).** Each replica quadruple contributes to $I$ the term $b(\rho_j)^2\ge b_0^2/4$ (the quadruple's representative has the same $b$). Hence
$$I\;\ge\;\sum_{j=1}^{\infty} b(\rho_j)^2\;\ge\;\sum_{j=1}^{\infty}\frac{b_0^2}{4}\;=\;\infty.\qquad\blacksquare$$

**[Obs. 175.3] (fixed precision suffices; one disc suffices).** The proof only used $\varepsilon_k<\eta$ for large $k$, not $\varepsilon_k\to0$ (the rate $\delta(\varepsilon_k)\to0$ of Step 1 is a refinement, not an input). So the real hypothesis of Theorem 175.2 is **LP-112[$\rho_0$]** (Def. §1(b)): infinitely many shifts at FIXED precision $\varepsilon<\eta$, in ONE disc. This is strictly less than LP-112 in two directions (one disc instead of all, fixed $\varepsilon$ instead of $\to0$) and is worth recording: any future attack on sequential rigidity has this minimal target. The quadruple's symmetry is not used: one replica per shift suffices (the whole quadruple replicates, by the functional equation, but that adds nothing — it would only multiply the bound by 4).

**[COR 175.4] (the weak version LP-112⁻ also suffices).** *LP-112⁻ ⟹ $I\in\{0,\infty\}$.*

*Proof.* Suppose $I>0$ and inductively build a sequence of off zeros $\rho^{(k)}=\tfrac12+b^{(k)}+i\gamma^{(k)}$ with strictly increasing heights and $b^{(k)}\ge b_0/2$ for all $k$. Base: $\rho^{(0)}:=\rho_0$, $b^{(0)}=b_0$. Step: given $\rho^{(k)}$ with $b^{(k)}\ge b_0/2$, define the **summable radius**
$$r_k\;:=\;\min\Bigl(b_0\,2^{-k-2},\;\tfrac12\min\bigl(b^{(k)},\,1-\beta^{(k)},\,\mathrm{dist}(\rho^{(k)},Z(\zeta)\setminus\{\rho^{(k)}\})\bigr)\Bigr)\;>\;0,$$
$D_k:=\bar D(\rho^{(k)},r_k)\subset\{\tfrac12<\sigma<1\}$, $\eta_k:=\min_{\partial D_k}|\zeta|>0$. Apply LP-112⁻ to $(D_k,\,\eta_k/2)$: there exists $\tau>\mathrm{height}(D_k)\;(>2r_k+1)$ with $\sup_{D_k}|\zeta(\cdot+i\tau)-\zeta|<\eta_k/2<\eta_k$, and Lemma 175.1(i) produces a zero $\rho^{(k+1)}$ of ζ with $|\rho^{(k+1)}-(\rho^{(k)}+i\tau)|<r_k$; in particular $\gamma^{(k+1)}>\gamma^{(k)}+\tau-r_k>\gamma^{(k)}$ (strictly increasing heights ⟹ distinct quadruples, as in Step 2) and
$$b^{(k+1)}\;\ge\;b^{(k)}-r_k\;\ge\;b_0-\sum_{j=0}^{k}b_0\,2^{-j-2}\;\ge\;b_0\Bigl(1-\tfrac12\Bigr)\;=\;\frac{b_0}{2}.$$
(The point of summability: with fixed radii of type $r_k=b^{(k)}/2$ the abscissa could degrade geometrically, $b^{(k)}\ge b_0 2^{-k}$, and $\sum (b^{(k)})^2$ could converge; the budget $\sum_k r_k\le b_0/2$ prevents the leak. Also $b^{(k+1)}\le b^{(k)}+r_k\le 2b_0<\tfrac12+b_0$, and $\beta^{(k+1)}<1$ automatically since it is a zero of ζ.) Then $I\ge\sum_k (b^{(k)})^2\ge\sum_k b_0^2/4=\infty$. $\blacksquare$

**[COR 175.5] (the two dichotomies and the new architecture).**
1. $I\in\{0,\infty\}\Rightarrow m\in\{0,\infty\}$ (if $m\ge1$ then $I>0$, hence $I=\infty$, hence $m=\infty$ because a finite sum of squares bounded by $\tfrac14$ is finite). The energy dichotomy **implies** D-109; Theorem 175.2 subsumes Theorem 2.3 of D112 under the same hypothesis.
2. $\boxed{\ \mathrm{RH}\;\Longleftarrow\;\bigl(I(0^+)<\infty\bigr)\;\wedge\;\mathrm{LP\text{-}112}\ }$ — indeed, under LP-112, $I\in\{0,\infty\}$; with $I<\infty$ we are left with $I=0$, i.e. no off zeros. **Strict** improvement over P44's architecture $(m<\infty)\wedge$LP-112: $m<\infty\Rightarrow I<\infty$ trivially, and the converse fails ($b_j=1/j$ over arbitrary heights: $m=\infty$, $I=\pi^2/6$-type $<\infty$). The first arrow (finiteness) weakens from a **cardinal** statement to an **$\ell^2$ moment** statement — exactly the quantity on which the program has its only unconditional second-order certificate (Theorem 170.5).

**Frankness about the novelty.** The proof of Theorem 2.3 of D112 already produced, under full LP-112, infinitely many off zeros at distance $<r$ from $\rho_0+i\tau_k$ — the bound $b\ge b_0-r$ was *implicit*. What is new in this document is: (i) making explicit and quantitative that the replica copies the abscissa (Lemma 175.1(ii), rate $\varepsilon^{1/m_0}$, multiplicity included); (ii) that the correct conclusion is about $I$, not $m$, and that this **weakens the first arrow of the architecture** (Cor. 175.5.2 — this is the strategic content); (iii) that LP-112⁻ also suffices, which requires the summable-radii induction of Cor. 175.4 (non-trivial: without summability the abscissa leaks away); (iv) the unconditional bridge of §3, which is independent of LP-112.

---

## 3. The bridge: replication density ↔ the energy theorem (unconditional)

The mandate's question: does the certificate $E(T)\ll T/\log T$ (Theorem 170.5) ALREADY limit how good the self-approximation of a ζ with an off zero can be? **Yes — and the limitation is an unconditional theorem with a rate.**

**[NEW-DEFINITION] (set of good shifts).** For $\rho_0,r,\eta$ as in §2.2 and $0<\varepsilon<\eta$:
$$A_\varepsilon\;:=\;\Bigl\{\tau>0:\ \sup_{s\in \bar D(\rho_0,r)}\bigl|\zeta(s+i\tau)-\zeta(s)\bigr|\le\varepsilon\Bigr\}$$
(the set of Prop. 2.6 of Doc 112).

**[THEOREM 175.6] (self-approximation of a ζ with an off zero is rare, with a rate).** *Suppose ζ has an off zero $\rho_0=\tfrac12+b_0+i\gamma_0$, and let $r\le b_0/2$, $\eta$, $A_\varepsilon$ be as above, $\varepsilon<\eta$. Then, unconditionally:*

(i) *(measure, via direct Selberg)* $\;\mathrm{meas}\bigl(A_\varepsilon\cap[0,T]\bigr)\;\le\;2r\,N\bigl(\tfrac12+\tfrac{b_0}2,\;T+\gamma_0+r\bigr)\;\ll\;r\,T^{\,1-b_0/8}\log T$;

(ii) *(measure, via energy)* $\;\mathrm{meas}\bigl(A_\varepsilon\cap[0,T]\bigr)\;\le\;\dfrac{8r}{b_0^2}\,E\bigl(T+\gamma_0+r\bigr)\;\ll\;\dfrac{r}{b_0^2}\cdot\dfrac{T}{\log T}$;

(iii) *(separated count)* every $2r$-separated subset $\{\tau_k\}\subset A_\varepsilon$ satisfies
$$\#\{k:\tau_k\le T\}\;\le\;\min\Bigl(N\bigl(\tfrac12+\tfrac{b_0}2,\,T+\gamma_0+r\bigr),\;\frac{4}{b_0^2}E(T+\gamma_0+r)\Bigr)\;\ll\;\min\Bigl(T^{1-b_0/8}\log T,\;\frac{T}{b_0^2\log T}\Bigr).$$

*Proof.* The replica map: for $\tau\in A_\varepsilon$, since $\varepsilon<\eta$, Lemma 175.1(i) (with $\delta=R=r$) gives a zero $\rho$ of ζ with $|\rho-(\rho_0+i\tau)|<r$; that zero has $\mathrm{Re}\,\rho\in(\tfrac12+b_0-r,\,\tfrac12+b_0+r)\subset(\tfrac12+\tfrac{b_0}2,\,1)$ — it is off with $b(\rho)\ge b_0/2$ — and $\mathrm{Im}\,\rho\in(\gamma_0+\tau-r,\,\gamma_0+\tau+r)$. Since the disc $D(\rho_0+i\tau,r)$ has radius $r<b_0/2\le\tfrac14$ and lies in $\{\sigma>\tfrac12\}$, only the upper-right member of each quadruple can fall in it: the replicated zero identifies a quadruple. Let
$$\mathcal Z(T)\;:=\;\bigl\{\text{quadruples with } b\ge \tfrac{b_0}{2},\ 0<\gamma\le T+\gamma_0+r\bigr\}.$$
For each quadruple $z\in\mathcal Z(T)$ (representative $\beta+i\gamma$), the set of $\tau$ for which that quadruple can serve as a replica is $T_z=\{\tau:\ |\beta+i\gamma-\rho_0-i\tau|<r\}\subset(\gamma-\gamma_0-r,\ \gamma-\gamma_0+r)$, an interval of length $\le2r$. Then $A_\varepsilon\cap[0,T]\subset\bigcup_{z\in\mathcal Z(T)}T_z$, whence $\mathrm{meas}(A_\varepsilon\cap[0,T])\le 2r\,\#\mathcal Z(T)$. Now, two bounds for $\#\mathcal Z(T)$:
$$\#\mathcal Z(T)\;\le\;N\bigl(\tfrac12+\tfrac{b_0}2,\,T+\gamma_0+r\bigr)\qquad\text{and}\qquad \#\mathcal Z(T)\;\le\;\sum_{\gamma_j\le T+\gamma_0+r}\frac{b_j^2}{(b_0/2)^2}\;=\;\frac{4}{b_0^2}\,E(T+\gamma_0+r)$$
(the second is Chebyshev on the energy). Selberg's density theorem [S46] gives $N(\tfrac12+\tfrac{b_0}2,T')\ll T'^{\,1-b_0/8}\log T'$ (exponent $1-\tfrac14\cdot\tfrac{b_0}{2}$), and Theorem 170.5 gives $E(T')\ll T'/\log T'$. This proves (i)–(ii). For (iii): if $|\tau_k-\tau_{k'}|>2r$, the discs $D(\rho_0+i\tau_k,r)$ and $D(\rho_0+i\tau_{k'},r)$ are disjoint, so separated shifts receive distinct quadruples and the replica map is injective from $\{\tau_k\le T\}$ into $\mathcal Z(T)$. $\blacksquare$

**Readings (the four requested by the mandate):**

1. **Improvement over Prop. 2.6 (D112).** That one gave upper density **zero** for $A_\varepsilon$ via Bagchi's limit theorem + Portmanteau — qualitative, no rate, with distributional machinery. Theorem 175.6 gives the explicit rate $\mathrm{meas}(A_\varepsilon\cap[0,T])/T\ll r\,T^{-b_0/8}\log T$ with a two-line proof (Rouché + zero density). The conceptual bridge is the **counting identity (iii)**: *energy is a counter of self-approximation witnesses* — any future improvement of the certificate $E(T)$ automatically transfers to a rarity bound for self-approximation. This is the requested energy ↔ universality bridge: two theories that the program carried on separate tracks (Docs 170–172 vs Docs 112–113) are now joined by an unconditional inequality.

2. **Which of the two bounds wins?** For **fixed** $b_0$ (the theorem's situation: the off zero is a fixed object), direct Selberg (i) wins with a power saving $T^{-b_0/8}$. The energy-based version (ii) is the conceptually new one but numerically weaker ($T/\log T$ is the $b_0$-uniform envelope — consistent with Doc 172's verdict: the Selberg envelope IS the $T/\log T$ floor read in energy; (ii) cannot beat (i) because 170.5 is proved WITH [S46]). The value of (ii) is structural, not quantitative: it makes visible that the object limiting replication is exactly the object of the architecture's first arrow ($I$, via $E$).

3. **The dimensional strengthening, with its declared gap.** The replica gives the exact dual lower bound of (iii): if $\{\tau_k\}\subset A_\varepsilon$ is $2r$-separated, then $E(T)\ge\tfrac{b_0^2}{4}\,\#\{k:\tau_k\le T-\gamma_0-r\}$ — *positive density of witnesses ⟹ positive density of energy*. **LP-112 does NOT bring density for free** (it is purely sequential: $\tau_k\to\infty$ with no counting bound — stated explicitly, as the mandate requests). If positive witness density (i.e. strong recurrence in $D_0$) were postulated, the contradiction with (iii) is immediate — but that is not new: it is the easy half of Bagchi (strong recurrence + off zero = absurd), re-proved here with a rate: **any $2r$-separated family of witnesses with count $\gg T^{1-b_0/8}\log T$ is unconditionally impossible.** The gap between what LP-112 needs (unbounded count: $\#\to\infty$, as slow as desired) and what the bridge forbids (count $\gg T^{1-b_0/8}\log T$) is huge: **the bridge neither closes LP-112 nor threatens it** — consistent with Prop. 2.7 of D112 (the sequential version is not self-blocking). The bridge bounds the enemy from above; it does not touch its non-emptiness.

4. **Reverse direction of the bridge.** (iii) read backward: if someone proved that self-approximation in the disc of a hypothetical off zero ALWAYS has separated count $\gg T/(b_0^2\log T)$ (a "universal quantitative weak recurrence"), then $E(T)\gg T/\log T$, contradicting... nothing: 170.5 is $\ll$, compatible. A contradiction would need $\gg T^{1-b_0/8+\delta}$ against (i). [GAP 175.B, statement form: *"every function in Bagchi space with a zero in $D_0$ that is a limit of vertical translates of itself along an unbounded sequence is so along a sequence of count $\ge\Phi(T)$"* for some explicit $\Phi$ — a "density automaticity" theorem for sequential recurrence. We know of nothing similar in the universality literature; Birkhoff recurrence gives syndetic returns for compact systems, but the flow of translations of ζ is neither compact nor is the target generic-recurrent. If $\Phi$ could be taken $\gg T^{1-b_0/8}\log T$, LP-112[$\rho_0$] would be **false** under ¬RH and the whole architecture would collapse to "RH ⟸ I<∞" — too good; the expectation is that no such $\Phi$ exists.]

---

## 4. Frank status of LP-112

Summary verified against Docs 112–113 and the literature cited there at source.

**What is a theorem.**
- **RH ⟹ LP-112.** Under RH, ζ does not vanish on $\{\tfrac12<\sigma<1\}$; for every disc $D$ of the strip, $\zeta|_D$ is non-vanishing, hence belongs to the support of Bagchi's measure, and strong recurrence (the "easy-under-RH" half of [Bag87]; exposition [Ste07, §8.3]) gives **positive** lower density of $\{\tau:\sup_D|\zeta(\cdot+i\tau)-\zeta|<\varepsilon\}$ for every $\varepsilon>0$ — much more than a sequence.
- **Strong recurrence ⟺ RH (Bagchi).** *RH ⟺ for every admissible compact $K\subset\{\tfrac12<\sigma<1\}$ and every $\varepsilon>0$, the set of $\tau$ with $\sup_K|\zeta(\cdot+i\tau)-\zeta|<\varepsilon$ has positive lower density.* [Bag81] (thesis, Indian Statistical Institute, Calcutta), [Bag87] (Acta Math. Hungar. 50, 227–240); modern exposition [Ste07, Thm. 8.3]. The ⟹ direction is the preceding point (full support = genericity); the ⟸ direction is the Rouché × density amplifier: strong recurrence + off zero produces $\ge cT$ off zeros up to height $T$, against $N(\sigma,T)=o(T)$ — exactly the "positive density" version of our Theorem 175.6(iii). **Verified: the equivalence is with STRONG recurrence (positive density, all compacts); the precedent is Bohr 1922 for $L(s,\chi)$ (D113 §2.1).**
- **Under ¬RH, the witnesses of LP-112 in the zero's disc are exceptional with a rate** (Prop. 2.6 of D112: zero density; Theorem 175.6 here: $\ll T^{-b_0/8}\log T$).

**What is NOT known.**
- LP-112 is **not known to be equivalent to RH**: it is sequential (it does not require density) and thus escapes Bagchi's amplifier (Prop. 2.7 of D112: a sparse countable family of replicated zeros contradicts no density theorem). Nor is it known how to refute it under ¬RH: zero density ≠ empty. Status: RH ⟹ LP-112 ⟹ $I\in\{0,\infty\}$ (this doc) ⟹ $m\in\{0,\infty\}$; no arrow is known to be reversible.

**The subtlety of the disc with zeros (the heart of the status).** Voronin's universality [Vor75] and all its descendants approximate **non-vanishing targets**: the support of Bagchi's measure in $H(D')$ is $S=\{f:\ f\ne0\text{ on }D'\}\cup\{0\}$ (limits of random Euler products that are non-vanishing are non-vanishing or $\equiv0$ — Hurwitz's theorem; [Bag81], [Lau96, ch. 6], [Ste07]). Self-approximating ζ in a disc WITHOUT zeros is, under RH, a special case of that genericity. Self-approximating ζ in a disc that CONTAINS an off zero is categorically different: the target is **outside the support**, and:
1. **Rouché does not forbid it** — worth stating precisely, since it is a possible misunderstanding. Rouché only says: every $\varepsilon$-good approximant ($\varepsilon<\eta$) must vanish in $D(\rho_0,r)$; i.e. $\zeta$ must have a zero near $\rho_0+i\tau$. Under ¬RH that is *possible* (off zeros are available — in fact Theorem 175.2 EXPLOITS exactly that necessity: the Rouché obstruction is the replication mechanism, not an impediment). Self-approximation with zeros is not analytically impossible; it is **distributionally exceptional**.
2. The real obstruction is genericity/measure: everything that produces good shifts (Kronecker–Weyl equidistribution, Bagchi's limit theorem, moments) produces *generic* shifts, and the generic one does not vanish near $\rho_0+i\tau$ (measure zero). Producing ONE element of a zero-density set defined by an individual condition is Principle 3.1 of P43 — the wall, in sequential instance (D112 §2.4–2.5). Theorem 175.6 worsens the exceptionality with a power rate.
3. **Calibrating positive precedent:** self-approximation IS a theorem for the Hurwitz zeta function $\zeta(s,\alpha)$ ($\alpha$ transcendental, or rational $\ne\tfrac12,1$) — [GK14] (Garunkštis–Karikovas, *Self-approximation of Hurwitz zeta-functions*) and the strong universality of [Bag81] —, **even in discs with zeros**, because its measure has full support in $H(D)$ (with no Euler product there is no support compression): the point is generic for its own flow. For ζ, **Euler compresses the support and turns the same statement into exceptional** (D113 §3.1). LP-112 is, exactly, the question of whether Euler compression leaves a residual sequence or not. No precedent in the literature in either direction (D113, verdict).

**References.** [Vor75] S.M. Voronin, *Теорема об «универсальности» дзета-функции Римана*, Izv. Akad. Nauk SSSR Ser. Mat. 39 (1975), 475–486. [Bag81] B. Bagchi, *The statistical behaviour and universality properties of the Riemann zeta-function and other allied Dirichlet series*, thesis, Indian Statistical Institute, Calcutta, 1981. [Bag87] B. Bagchi, *Recurrence in topological dynamics and the Riemann hypothesis*, Acta Math. Hungar. 50 (1987), 227–240. [Ste07] J. Steuding, *Value-Distribution of L-Functions*, Springer Lecture Notes in Math. 1877, 2007 (ch. 8: strong recurrence and self-approximation). [Lau96] A. Laurinčikas, *Limit Theorems for the Riemann Zeta-Function*, Kluwer, 1996. [GK14] R. Garunkštis, E. Karikovas, *Self-approximation of Hurwitz zeta-functions*, Funct. Approx. Comment. Math. 51 (2014). [S46] A. Selberg, *Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. 48 (1946). [T39] E.C. Titchmarsh, *The Theory of Functions*, 2nd ed., Oxford, 1939, §3.42 (Rouché). [C78] J.B. Conway, *Functions of One Complex Variable*, 2nd ed., Springer GTM 11, 1978 (VII.2.5 Hurwitz, VIII.3 Rouché). [T86] E.C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (Heath-Brown), Oxford, 1986. Discrete universality: A. Reich, *Werteverteilung von Zetafunktionen*, Arch. Math. 34 (1980), 440–451.

---

## 5. The portrait of the finite-energy state (without assuming LP-112)

What does $0<I<\infty$ say on its own? (The director's "Phase C," replication version.)

**[PROP 175.7] ($\ell^2$ structure).** If $I<\infty$:
1. *(finitely many large ones per level)* for every $b>0$, $\;\#\{j:\ b_j\ge b\}\;\le\;I/b^2\;<\;\infty$;
2. *(accumulation on the line)* $b_j\to0$ for any enumeration (tails of a convergent series); if $m=\infty$, off zeros accumulate on $\{\mathrm{Re}=\tfrac12\}$ and only there;
3. $m=\infty$ remains possible ($b_j=1/j$ realizes $I<\infty$, $m=\infty$, and such configurations are indistinguishable by average data — Theorem 170.8); $I<\infty$ does NOT imply $m<\infty$: the new first arrow is genuinely weaker than the old one.

*Proof.* (1) Chebyshev. (2) immediate. (3) Doc 170 §5. $\square$

**[PROP 175.8] (anti-recurrence of the finite-energy state).** *If $0<I<\infty$, then for EVERY off zero $\rho_0$ (with its constants $r\le b_0/2$, $\eta$) and every $\varepsilon<\eta$:*
$$\mathrm{meas}\bigl(A_\varepsilon\bigr)\;\le\;\frac{8r}{b_0^2}\,I\;<\;\infty\quad\text{(total measure over }(0,\infty)\text{)},\qquad \#\{2r\text{-separated subset of }A_\varepsilon\}\;\le\;\frac{4I}{b_0^2}\;<\;\infty .$$
*In particular there is NO unbounded sequence of $\varepsilon$-good shifts in the disc of any off zero: the finite-energy state is anti-recurrent in each of its off windows, even at fixed precision.*

*Proof.* Those of Theorem 175.6(ii)–(iii) with $T\to\infty$: $\#\mathcal Z(\infty)\le 4I/b_0^2$ (Chebyshev on the full series), $A_\varepsilon\subset\bigcup_{z}T_z$ with $\le 4I/b_0^2$ intervals of length $\le2r$; a set contained in finitely many bounded intervals admits no unbounded sequence. $\square$

**The complete portrait.** The world $0<I<\infty$ is: *almost all off zeros sub-resolution* (at each fixed distance from the line, finitely many — Prop 175.7.1, with explicit budget $I/b^2$; the unconditional envelope 170.5 moreover says that even the total energy up to $T$ grows as at most $T/\log T$, in ANY world), *pure accumulation on the line* (175.7.2), *possibly with infinitely many zeros* (175.7.3), and **anti-recurrent**: each off zero is a point from which ζ permanently moves away — past a finite height, ζ never again resembles itself in that window, even with fixed error $\varepsilon<\eta$ (175.8). $I$ works as an accounting budget: each separated $\varepsilon$-good return consumes $\ge b_0^2/4$ units of energy, and only $I$ is available.

**Does PARTIAL replication ($\varepsilon$ fixed, not $\to0$) contradict the portrait?** Pushed to the end: Prop. 175.8 IS the exact contrapositive of the strong version of Theorem 175.2 (Obs. 175.3). The precise boundary:
- recurrence at precision $\varepsilon<\eta$ with an **unbounded** sequence in ONE off window ⟹ $I=\infty$ (incompatible with $0<I<\infty$);
- recurrence at precision $\varepsilon\ge\eta$ says nothing (Rouché needs to win on the boundary: with $\varepsilon\ge\eta$ the approximant may not vanish — the threshold $\eta$ is exact, not improvable by this method: $f=\zeta-\zeta(\,\cdot\,)\cdot$(correction masking the zero) illustrates that with margin $\ge\eta$ the zero can be dodged);
- finitely many good returns are always compatible ($\le 4I/b_0^2$ of budget).

There is no internally reachable contradiction without LP-112: the portrait is consistent. But it is sharply clear **what would break it** — and that is the minimal target:

**[GAP 175.A] (the minimal instance of LP-112, statement form).** *Let $\rho_0$ be a zero of ζ with $\mathrm{Re}\,\rho_0\in(\tfrac12,1)$, $r=r(\rho_0)$, $\eta=\eta(r)$ as in §2.2. Prove: there exists an unbounded sequence $\{\tau_k\}$ with $\sup_{|s-\rho_0|\le r}|\zeta(s+i\tau_k)-\zeta(s)|<\eta$.* — This, together with $I(0^+)<\infty$, implies RH (in fact it implies $I=\infty$, contradicting $I<\infty$ and forcing no such $\rho_0$ to exist). It is strictly weaker than LP-112 (one disc, one $\varepsilon$) and its witnesses, if they exist, live in a set of measure-density $\ll T^{-b_0/8}\log T$ (Theorem 175.6): the P43 §3.1 wall, now with the rate of its own exceptionality written out.

---

## 6. Final message

**Was the theorem proved? YES**, with a complete and quantified proof, **conditional on LP-112 and declared as such**: the hypothesis is exactly LP-112 (in fact LP-112⁻ suffices, and in fact the minimal instance LP-112[$\rho_0$] at fixed precision in a single disc suffices — Obs. 175.3, GAP 175.A). No step of the proof is conditional on anything else; all the program's uncertainty remains compressed into LP-112, which this document does not prove and whose witnesses, under ¬RH, are left quantitatively more exceptional than before (rate $T^{-b_0/8}\log T$).

**The new architecture holds:**
$$\boxed{\;\mathrm{RH}\;\Longleftarrow\;\bigl(I(0^+)<\infty\bigr)\;\wedge\;\mathrm{LP\text{-}112}\;}$$
a strict improvement over P44/D112's old $(m<\infty)\wedge\mathrm{LP\text{-}112}$: the first arrow goes down from cardinal (m<∞, with no partial certificate at all) to $\ell^2$ moment ($I<\infty$, whose envelope $E(T)\ll T/\log T$ IS the program's only unconditional second-order certificate, Theorem 170.5 — the missing arrow is "rate→total," not "nothing→everything"). The second arrow remains intact and identical.

**Three results with labels:**
1. **[THEOREM 175.2 + COR 175.4]** (conditional on LP-112, even on LP-112⁻): $I(0^+)\in\{0,\infty\}$ — the energy dichotomy; the Rouché–Hurwitz replica copies the distance to the line with error $\le(4\varepsilon_k/|c|)^{1/m_0}\to0$ and each replica costs $\ge b_0^2/4$ of energy. Subsumes the cardinal dichotomy D-109 and turns the director's Problem B ($I<\infty\Rightarrow I=0$) into a theorem conditional on LP-112.
2. **[THEOREM 175.6]** (unconditional, new): if ζ has an off zero, its self-approximation in the zero's disc is rare with a rate — $\mathrm{meas}(A_\varepsilon\cap[0,T])\ll r\,T^{1-b_0/8}\log T$ and every separated set of witnesses has $\#\le 4E(T)/b_0^2\ll T/(b_0^2\log T)$. Energy ↔ universality bridge; improves with a rate and an elementary proof Prop. 2.6 of D112; any future improvement of $E(T)$ transfers automatically.
3. **[PROP 175.8]** (unconditional): the state $0<I<\infty$ is anti-recurrent — total measure of good shifts $\le 8rI/b_0^2$, at most $4I/b_0^2$ separated witnesses over ALL of $(0,\infty)$; $I$ = witness budget. Exact contrapositive of the theorem; fixes the minimal target GAP 175.A.

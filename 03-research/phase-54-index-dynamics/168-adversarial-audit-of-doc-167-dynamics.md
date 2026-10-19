# Document 168 — Adversarial audit of Doc 167 (dynamics of the index κ)

**Program:** Riemann Hypothesis — Phase 54
**Object:** Full Doc 167, with closed re-derivation of every load-bearing piece. No numerics. Protocol: kill by (i) parameters treated as constants, (ii) unverified exception clauses, (iii) sum/derivative exchanges, (iv) quantifiers, (v) exponential constants.

---

## 0. Verdict per piece

| Piece | Verdict | Damage |
|---|---|---|
| **(a) Thm 2.3, law İ = −2κ − D, D ≥ 0** | **SURVIVES** (re-derived term by term; sign of D hermetic; verified exactly in closed model) | none in the core |
| **(b) Thm 1.4, κ = degree; walls; fold** | **SURVIVES but deflationary** — it is the argument principle + Hurwitz on a compact rectangle; "topological" is packaging, not new power. "Codimension 1" of the walls: decorative, without a proved manifold structure | minor |
| **(c) Prop 3.2 + GAP 167.A** | **TOUCHED** — KKL verified ✓; Prop 3.2.1 has a gap at t→0⁺ (entry from Re→∞ not excluded); separation 3.2.3 cites a counterexample that **does not satisfy Def 1.1.3** as stated (repairable); the "average-side" claim is unsubstantiated hope and contradicted by the document's own §5.1 | medium |
| **(d) Corollaries** | **Cor 2.4: final constant FALSE** (κ(0)/16 → κ(0)/4; mixing of normalizations, failure mode (i)). **Cor 2.5: exception clause FALSE/unjustified** (case I<∞, κ=∞; failure mode (ii)) — the unconditional inequality I(t) ≥ 4|t| **is not proved**. The ζ-free table in §5: honest and correct | serious in (d), but partly repairable |

---

## 1. Zero dynamics (Lemma 2.1): verified, with its exact hypotheses

**Re-derivation.** With the Polymath 15 normalization, $H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du$ satisfies $\partial_t H_t = -\partial_z^2 H_t$ (differentiating under the integral is legitimate: the integrand decays superexponentially). At a simple zero $z_k(t)$, the implicit function theorem gives $\dot z_k = -\partial_t H/\partial_z H = \partial_z^2 H/\partial_z H$ evaluated at $z_k$. For $H$ entire of order 1, **even and real**, Hadamard gives $H(z)=cz^q\prod_j(1-z^2/z_j^2)$ — **without an $e^{bz}$ factor** (parity), as the document claims. Writing $H=(z-z_k)g$: $H''/H'(z_k)=2g'(z_k)/g(z_k)=2\sum'_{j\ne k}(z_k-z_j)^{-1}$ with the sum **paired** $z_j\leftrightarrow -z_j$ (each far pair contributes $O(|z_j|^{-2})$, absolutely summable by RvM-type density). This matches [RT §2] and [P15].

**Critical protocol point (sum/derivative exchange and Im of the conditional sum).** The **real** part of the velocity is only conditionally convergent (it requires the symmetric pairing — correct in the document). But the **imaginary** part, which is the only thing entering İ, is
$$\mathrm{Im}\,\frac{1}{z_k-w} = -\frac{\beta_k-\mathrm{Im}\,w}{|z_k-w|^2},$$
and for $w=x_j$ real and far this is $-\beta_k/|z_k-x_j|^2 = O(x_j^{-2})$: the series for $\dot\beta_k$ is **absolutely convergent without pairing**. There is no illegitimate exchange hidden in the imaginary part. *This point, which was the candidate for failure (i)/(iii), holds up.*

**Exact hypotheses under which it holds:** (1) simple zeros at the instant considered; (2) density $\sum_j|z_j|^{-2}<\infty$; (3) nothing else. It holds equally for isolated complex zeros (holomorphy + implicit function theorem), including $t<\Lambda$. For $t>0$ the hypotheses are supplied by [KKL] except at collision instants; the **local finiteness of collision instants** is not in [KKL] — the document asserts it in passing (Lemma 2.1, end). It is plausible (joint analyticity of $H_t(z)$ in $(t,z)$ + non-increasing integer κ bounds the landings by $\kappa(t_0)/2$; real–real collisions are excluded by repulsion, §2 below), but the joint-analyticity argument **is not written** in the document. Minor flag: the logical chain is reconstructible, not present.

**Verification in a closed model** (independent control of signs and normalization): $H_t(z)=z^2+c_0-2t$ satisfies $\partial_tH=-\partial_z^2H$. For $c_0>0$: even at $\pm i\beta$, $\beta^2=c_0-2t$; landing at $t_c=c_0/2$; afterward, real zeros $\pm\sqrt{2t-c_0}$. Dynamics: $\dot z_1 = 2/(z_1-z_2)$ ✓ exact. And with $I=\beta^2$, $\kappa=1$: $\dot I = -2 = -2\kappa$, $D=0$ ✓ exact. Prop 2.6 ($\beta^2 = 2(t_c-t)$) is realized with equality. **The rate −2 per mode is correct.**

---

## 2. The balance law (Thm 2.3): full re-derivation — the sign of D is hermetic

$\dot\beta_k = -2\sum_{w\ne z_k}\dfrac{\beta_k-\mathrm{Im}\,w}{|z_k-w|^2}$, $\dot I = \sum_{k\,\text{sup}}2\beta_k\dot\beta_k$ (a **finite** sum under the theorem's hypothesis $\kappa<\infty$: there is no $\sum$/$d_t$ exchange to justify — the document states the theorem exactly on the domain where the operation is trivially legitimate; good).

Classification of $w$, verified term by term:

1. **$w=\bar z_k$:** $\mathrm{Im}\,w=-\beta_k$; term $\beta_k\cdot 2\beta_k/|2i\beta_k|^2 = 1/2$; contribution $-4\cdot\tfrac12 = \mathbf{-2}$ per upper zero. **Total $-2\kappa$. Verified** (and confirmed by the closed model in §1). The exact factor is $-2$, independent of position.
2. **$w=-\bar z_k$:** $\mathrm{Im}\,w=+\beta_k$ ⟹ contribution $0$ ✓.
3. **$w=-z_k$:** $\beta_k(2\beta_k)/4|z_k|^2$ ⟹ contribution $-2\beta_k^2/|z_k|^2\le 0$ ✓.
4. **$w=x_j$ real:** contribution $-4\beta_k^2/|z_k-x_j|^2\le0$, absolutely convergent series (RvM) ✓.
5. **Cross terms between distinct quadruples — the predicted death point (GAP-B analogue).** Here I looked for the failure with intent and **it does not exist**, for a structural reason the document uses without underlining it: after symmetrizing $(k,l)+(l,k)$, the two terms of each pair share **exactly the same denominator**:
 - $w=z_l$ seen from $z_k$: denominator $|z_k-z_l|$; $w=z_k$ from $z_l$: $|z_l-z_k|$ — **identical** ⟹ $\beta_k(\beta_k-\beta_l)+\beta_l(\beta_l-\beta_k) = (\beta_k-\beta_l)^2 \ge 0$ over the common denominator.
 - $w=\bar z_l$ from $z_k$: $|z_k-\bar z_l|$; $w=\bar z_k$ from $z_l$: $|z_l-\bar z_k| = |\overline{z_l-\bar z_k}| = |\bar z_l - z_k|$ — **identical** ⟹ $(\beta_k+\beta_l)^2\ge0$.
 - Analogous for $-\bar z_l$ ($|z_k+\bar z_l|=|z_l+\bar z_k|$) and $-z_l$ ($|z_k+z_l|$).

 If the denominators did not coincide, the grouping would leave sign-free residues and the "dissipation" would be false — it is the conjugation symmetry that closes the sign, not an arbitrary choice of grouping. **D ≥ 0 is genuinely term by term.** The accounting of factors ($-4$ over unordered pairs $=$ $-2$ over ordered ones; $-2\beta_k^2/|z_k|^2 = -4\beta_k^2\cdot\frac{1}{2|z_k|^2}$) matches the formula in the statement.

**Verdict (a): THEOREM 2.3 CERTIFIED** on its stated domain ($t$ in an interval with κ finite and constant and simple zeros). Additional point not flagged by the document: the law is **scale invariant** ($z\to\lambda z$, $t\to\lambda^2 t$ leaves $\dot I$ and $-2\kappa$ invariant), which protects it from the normalization problem that does kill constants in the corollaries (§3). "There is no source term" is correct: the sum is exhausted by the 5 categories, with no remainder.

---

## 3. Domain of validity: here are the two deaths

### 3.1. [PARTIAL DEATH — Cor 2.5] The exception clause "if κ or I are infinite, it holds trivially" is false as stated

Cor 2.5 claims $I(t)\ge 4|t|$ for all $t<0$, via: (case 1) well-defined dynamics and κ finite on $(t,0)$ ⟹ Thm 2.3 + κ≥2 ⟹ ✓; (case 2) "if κ or I are infinite on $(t,0)$ the conclusion holds trivially." Case 2 covers $I(t)=\infty$ (trivial ✓) and $\kappa=\infty$ on a set of positive measure **if the integral form of the law held there** — but **it does not**: Thm 2.3 is stated and proved only for $\kappa<\infty$. The uncovered case is exactly:

> $I(u)<\infty$ for all $u\in(t,0)$ but $\kappa(u)=\infty$ — **possible** in the analytic class (it is the Hadamard-type configuration of Doc 144: $\sum\beta_j^2<\infty$ with infinitely many pairs).

In that case nothing can be concluded with what has been proved: (α) $\dot I=\sum 2\beta_k\dot\beta_k$ is now an infinite series and the $d_t/\sum$ exchange requires uniform convergence that has not been established (failure mode (iii), now indeed present); (β) the rescue by truncating to $N$ quadruples **breaks the sign of D**: the cross terms between the $N$ chosen elements and the rest are left without a symmetrizing partner, and are sign-free — exactly the GAP-B mechanism of Doc 139. There is also no KKL-type result for $t<0$ excluding $\kappa=\infty$ (KKL is only for $t>0$).

**Consequence:** the unconditional inequality $I(t)\ge4|t|$, and with it the quantitative half of the slogan "RH ⟺ takeoff with minimal quantized slope 4," **is not proved**. What survives: (i) the conditional version (κ finite and zeros a.e. simple on $(t,0)$); (ii) the equivalence **RH ⟺ $I(0^+)=0$**, which only uses the $t>0$ side (KKL + monotonicity + Hurwitz at $t=0$) and is sound. **Possible repair:** either a truncation lemma with control of cross terms via the decreasing de Bruijn band (Thm 13 of [dB], which gives $\beta_k(u)^2 \le \beta_k(t)^2 - 2(u-t)$ ... caution: that theorem controls the **sup**, not the sum), or extending Thm 2.3 to $\kappa=\infty$, $I<\infty$ by proving absolute convergence of all blocks under $\sum\beta_l^2<\infty$ + RvM — plausible (the cross blocks are dominated by $\sum_l(\beta_k^2+\beta_l^2)/|z_k-\bar z_l|^2$, summable except for control of minimum gaps) but **is a new lemma, not a trivial one**.

### 3.2. [DEATH of a constant — Cor 2.4] Mixing normalizations: textual failure mode (i)

The document fixes the P15 normalization: $H_0(z)=\tfrac18\,\Xi(z/2)$ (line in §0.1, and it is the one from [RT]/[P15], verified). Then **the zeros of $H_0$ are those of $\Xi$ dilated by 2**: the band is $|\mathrm{Im}\,z|<\mathbf{1}$, **not** $1/2$. (External consistency: the de Bruijn band theorem — zeros in $|\mathrm{Im}|\le\Delta$ ⟹ in $|\mathrm{Im}|\le\sqrt{\Delta^2-2t}$ — gives $\Lambda\le\Delta^2/2 = 1/2$ exactly with $\Delta=1$ ✓; with $\Delta=1/2$ it would give $\Lambda\le1/8$, a known falsehood. Also the literature records $\Lambda=4\lambda(0)$ between normalizations — the factor 4 in $t$ is real.)

Consequences:
- **Final Cor 2.4:** "$\Lambda\le \kappa(0)/16$, using $\beta\le1/2$" is **false in the declared normalization**: there $\sup\beta<1$ and the chain gives $\Lambda\le I(0^+)/4 \le \kappa(0)/4$. (In $\Xi$ coordinates with its proper time $t_\Xi=t_H/4$ the /16 would be correct — but then $\Lambda_\Xi\ne\Lambda$ and all values cited in §0.1 change.) The part $\Lambda\le t_0+I(t_0)/4$ is coherent **if** $I$ is measured on $Z(H_t)$; the slippage occurs only when "β ≤ 1/2" is introduced.
- **Def 1.1 (𝒞):** with band $|\mathrm{Im}\,z|\le1/2$ and density $N_Z(T)=\frac{T}{\pi}\log\frac{T}{2\pi e}+O(\log T)$, which is that of $\Xi$ — **$Z_t = Z(H_t)\notin\mathcal{C}$ literally** (band 1, density $\frac{T}{2\pi}\log\frac{T}{4\pi e}$). Thm 1.4 and Thm 2.3 do not use the exact values (only $\sum|z|^{-2}<\infty$ and a bounded band), so **no theorem dies from this**, but the document is internally inconsistent and the inconsistency has already cost a constant (the /16). The law İ = −2κ − D survives by being scale invariant; the constants are not.

### 3.3. Convergence of I and statement of the domain

Thm 2.3 is correctly confined to κ<∞: there is **no** domain slippage within the theorem itself. The slippage is in the corollaries: Cor 2.5 uses it where κ<∞ is exactly what is not known ($t<0$, and $t\to0^+$ with $m=\infty$ possible). Prop 3.2.2 ($I(0^+)<\infty \iff \int_0^s[2\kappa+D]\,du<\infty$) is correct for the $t>0$ side (κ(u)<∞ by KKL; $I$ monotone; monotone convergence to pass to the limit $t\to0^+$), **modulo** the local finiteness of collisions from §1 (reconstructible). The detail "κ(t)≥2 by parity" in Cor 2.4/2.5 requires avoiding $W_{\mathrm{Sieg}}$, which the document only discusses at $t=0$; **it closes with a line the document did not write**: $H_t(i\beta)=\int_0^\infty e^{tu^2}\Phi(u)\cosh(\beta u)\,du>0$ because $\Phi>0$ — the real flow **never** touches the imaginary axis, for any $t$. (Audit gift: this lemma seals the parity along the entire flow.)

---

## 4. κ as degree (Thm 1.4) and the walls: correct, deflationary

- **Is the degree well-defined on a non-compact boundary?** The question does not arise: the rectangle $R$ is **compact**, and the joint hypothesis (proper path + κ<∞) places all upper zeros in a fixed compact set. The protocol's concern (log T density at infinite height) is deactivated **by hypothesis, not by theorem** — the real content of "proper" is assuming away what would need to be excluded. The document is honest about this (§1.1, "minimal honest hypothesis"), and for the DBN flow with κ<∞ on compact intervals of $(0,\infty)$ the property follows from velocity $O(\log T)$ at height $T$ (sub-linear: no escape/entry in finite time) — a sketched argument, valid.
- **Does "topological" add anything?** Not in proving power: (3) is the argument principle, (1) is Hurwitz, (2) is counting. It is a **correct reformulation**; its value is organizational (it identifies the only two modes of change of κ). The document half-admits this ("discreteness is cheap," §4a). The $\mp2$ jump is fine: the landing at $x_0$ and its mirror $-x_0$ are simultaneous by parity of $F$, each subtracting 1 from the upper count ✓; the case "a pair lands on a pre-existing simple real zero" gives multiplicity ≥3, still $W_{\mathrm{col}}$ ✓.
- **Fold (Prop 1.6):** Weierstrass + discriminant + assumed transversality — correct and standard; it is the quadratic formula. The connection with CSV94 is one of inspiration, not dependence: CSV94 gives lower bounds on Λ from Lehmer pairs; the normal form here is self-contained. "Lehmer = 2 is the degree of the discriminant": consistent with Prop 2.6 (verified exactly in the closed model, §1).
- **Decorative without proof:** "codimension 1" of $W_{\mathrm{col}}$ (𝒞 does not have an established manifold structure). It is not used in a load-bearing way. And the phrase "κ classifies the connected components..." is tautological as formulated.

---

## 5. GAP 167.A: the separation and the "average-side" test

### 5.1. The separation $I(0^+)<\infty \subsetneq \kappa(0)<\infty$: essentially correct, with a repairable citation defect

The real counterexample of Doc 141.R2/144 has $\gamma_j=2^j$, $\delta_j=e^{-\gamma_j}$ (not the $\min(1/4,\,1/(j\,a(2^j)))$ of later versions; both are $\ell^2$). $\sum_j\delta_j^2<\infty$ trivially with $m=\infty$: the separation **as configurations** is correct. **But:** as constructed (real zeros $t_n=n/\log(n+2)$), its count is $N_F(T)\asymp T\log T$ **only up to order of magnitude** — Def 1.1.3 of Doc 167 requires the exact RvM asymptotic $\frac{T}{\pi}\log\frac{T}{2\pi e}+O(\log T)$, which the construction **does not** verify (different constant, error not controlled at $O(\log T)$). The counterexample, cited against Def 1.1 of Doc 167, **is not in 𝒞**. Trivial repair: take as $t_n$ the solution of $\frac{t}{\pi}\log\frac{t}{2\pi e}=n$ (same convergence argument, genus and order). Repairable in five lines, but the citation chain as it stands is invalid — third instance of the pattern "parameters treated as if they fit." Does it enter the DBN flow? Yes in the relevant sense: $e^{-t\partial_z^2}$ acts on entire functions of order $<2$ (the series $\sum(-t)^nF^{(2n)}/n!$ converges), so the hierarchy of Prop 3.2 is a hierarchy of the flow and not merely a static one.

### 5.2. Is $I(0^+)$ visible to vertical statistics? — the test the session predicted

Closed analysis. A quadruple $\{\gamma\pm ib,\,-\gamma\pm ib\}$ ($\Xi$ coordinate) contributes to an explicit-formula functional with even test $h$:
$$h(\gamma+ib)+h(\gamma-ib) = 2h(\gamma) + b^2 h''(\gamma) + O(b^4).$$
Two-edged conclusion:
1. **At first order, invisible** — it is no-go 141.B2: the linear signal in $b$ cancels. Classical vertical statistics (pair correlation, moments of $S(t)$, densities) operate at this order: **blind to $I$**.
2. **At second order, $I$ is exactly what appears**: $\sum_j b_j^2\,h''(\gamma_j)$. This is structurally notable (it is the quadratic trace of the Lehmer = 2 exponent, and it is where Weil positivity lives), and it distinguishes $I$ from the linear quantities that died in Phase 46. **But it does not make it certifiable**: (α) the quadratic term comes **weighted** by $h''(\gamma_j)$, with $h$ decaying and $h''$ sign-free — extracting $\sum b_j^2$ unweighted is impossible with admissible tests; (β) it is submerged in the main term $\sum 2h(\gamma_j)$ over ALL zeros, known only to an error much larger than $b_j^2$ (which can be sub-resolution, $e^{-\gamma_j}$); (γ) bounding $\int_0^s\kappa(u)\,du$ requires bounding the number of non-real zeros of $H_u$ near $u=0$ — an off-zero density problem for the deformation, for which no averaging tool exists. And Doc 167 §5 nuance 1 itself locates the wall at "signed moment → quadratic moment": **that phrase applies literally to GAP 167.A**. The label "on the average side of the master quantifier" describes the **syntactic form** of the statement ($\ell^2$, sum, no sup), not real accessibility with existing tools.

**Verdict GAP 167.A:** valid separation (after repairing the citation), well-named objective and genuinely weaker than $m<\infty$; the hope of attackability by averages is **downgraded from claim to wish**, with internal tension in the document (GAP 167.A vs §5.1). The one point in its favor: $I$ is second order, not first order — it is the first quantity in the program whose invisibility does NOT follow from the zero-integral mechanism of 141.B2; its inaccessibility comes from weighting and sub-resolution, a different and frankly weaker wall. That deserves to be recorded.

---

## 6. Ki–Kim–Lee: VERIFIED

External verification (Polymath wiki; AMS Bulletin survey by Newman–Wu type "Constants of de Bruijn–Newman type"; Tao's blog; Wikipedia): Ki–Kim–Lee, *On the de Bruijn–Newman constant*, Adv. Math. **222** (2009) 281–306, proves (1) $\Lambda<1/2$ and (2) **for every $\lambda>0$, all zeros of $\Xi_\lambda$ except finitely many are real and simple** (key step: for every $\lambda,\varepsilon$, zeros with real part outside the critical zone have bounded height). The attribution of Doc 167 (§0.1 and Prop 3.1: for every $t>0$, finitely many non-real zeros, almost all real and simple, **unconditionally**) is **correct**. Two clarifications that Doc 167 does not load onto KKL but should be fixed: (a) KKL does **not** give local finiteness of collision instants in $t$ (that must be derived, §1); (b) KKL is only for $t>0$ — nothing for $t<0$, which is where Cor 2.5 would need it (§3.1). Normalization note: the literature contains coexisting normalizations with $\Lambda=4\lambda(0)$; the values cited in §0.1 of Doc 167 ($\le\tfrac12$, $<\tfrac12$, $\ge0$, $\le0.22$) are those of the standard $H_t$ normalization, mutually consistent — the document's inconsistency is not in §0.1 but between §0.1 and Def 1.1/Cor 2.4 (§3.2).

Verification sources: [Polymath wiki — De Bruijn-Newman constant](https://michaelnielsen.org/polymath/index.php?title=De_Bruijn-Newman_constant), [Tao, "The De Bruijn-Newman constant is non-negative"](https://terrytao.wordpress.com/2018/01/19/the-de-bruijn-newman-constant-is-non-negativ/), [Rodgers–Tao, arXiv:1801.05914](https://arxiv.org/pdf/1801.05914), [KKL on ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0001870809001133), [Wikipedia — de Bruijn–Newman constant](https://en.wikipedia.org/wiki/De_Bruijn%E2%80%93Newman_constant).

---

## 7. List of required repairs (in order of severity)

1. **Cor 2.5:** restrict the statement to its conditional version (κ<∞ and zeros a.e. simple on $(t,0)$), or prove the extension lemma of Thm 2.3 to $\kappa=\infty,\ I<\infty$ (absolute convergence of the cross blocks under $\ell^2$ + RvM + a lower bound on gaps — **new lemma, not trivial**, and note that without a lower bound on local gaps the denominators $|z_k-z_l|$ can ruin summability). Relabel "RH ⟺ takeoff with minimal slope" as conditional.
2. **Cor 2.4:** correct $\kappa(0)/16 \to \kappa(0)/4$ (P15 normalization, $\sup\beta<1$), or re-coordinatize the whole document in the $\Xi$ variable with rescaled time and Λ values divided by 4 — choose ONE chart.
3. **Def 1.1:** band $\le 1$ and density $N_Z(T)=\frac{T}{2\pi}\log\frac{T}{4\pi e}+O(\log T)$ if the chart is that of $H_t$ (the theorems do not change; the constants do).
4. **Prop 3.2.3:** rebuild the Hadamard counterexample with $t_n$ = exact RvM points so that it lies in 𝒞.
5. **Lemma 2.1 / Prop 3.2.2:** write the local finiteness of collisions argument (joint analyticity + non-increasing κ + real–real repulsion: $\dot g = 4/g + O(\log T)$ ⟹ $g$ cannot vanish going forward).
6. **Add the gift lemma:** $H_t>0$ on the imaginary axis for every $t$ (positivity of $\Phi$ and $\cosh$) — seals $W_{\mathrm{Sieg}}$ and the parity κ≥2 along the whole flow, closing the gap in Cor 2.4/2.5 at that point.
7. **GAP 167.A:** downgrade "on the average side" to [WISH] and record the real new fact: $I$ is the first second-order quantity of the program — it escapes the zero-integral no-go (141.B2) but runs into the weight/sub-resolution wall.

---

## 8. Final verdict

- **(a) Thm 2.3 — CERTIFIED.** The full re-derivation confirms $\dot I=-2\kappa-D$ with $D\ge0$ term by term; the sign of D is protected by the exact coincidence of denominators under conjugation (not by discretionary grouping); the rate $-2$ per mode is verified with equality in the closed model $z^2+c_0-2t$; the imaginary part of the dynamics is absolutely convergent (no illegitimate exchange). It is the most solid theorem this phase has produced, and it is genuinely ζ-free.
- **(b) Thm 1.4 — CORRECT, deflationary.** Argument principle + Hurwitz on a compact set; the non-compactness of the band is avoided by hypothesis ("proper" + κ<∞), not by theorem. Fold correct. No new power, good organization.
- **(c) Prop 3.2 + GAP 167.A — TOUCHED, repairable.** KKL verified; gap at t→0⁺ (3.2.1, entry from infinity); cited counterexample outside 𝒞 (repairable); "average side" unsubstantiated and in tension with the document's own §5.1.
- **(d) Corollaries — TWO CASUALTIES.** Cor 2.4: final constant false due to mixing normalizations ($/16\to/4$). Cor 2.5: exception clause unverified — the unconditional version of $I(t)\ge4|t|$ is not proved; the conditional version survives, as does RH ⟺ $I(0^+)=0$. The circularity table in §5 is honest.

**Three findings:**
1. **[Partial KILL] The exception clause of Cor 2.5 is false in the case $I<\infty,\ \kappa=\infty$** (possible via Hadamard): there Thm 2.3 does not apply, the $d_t/\sum$ exchange is not justified, and truncation breaks the sign of D via unpaired cross terms (GAP-B mechanism). Historical failure mode (ii)+(iii), localized in a single phrase ("holds trivially").
2. **[Constant KILL] Mixing of $\Xi$/$H_t$ charts:** in the declared P15 normalization, the zeros of $H_0$ live in the band $|\mathrm{Im}\,z|<1$ (not $1/2$) with density $\frac{T}{2\pi}\log\frac{T}{4\pi e}$; Cor 2.4 gives $\Lambda\le\kappa(0)/4$, not $\kappa(0)/16$, and $Z_t\notin\mathcal{C}$ literally. The law İ=−2κ−D survives by scale invariance; the constants do not.
3. **[Structural finding in favor] $I$ is the first second-order quantity of the program:** its footprint in the explicit formula is $\sum_j b_j^2 h''(\gamma_j)$, which **escapes** the zero-integral no-go 141.B2 (which kills the first order); its current inaccessibility is due to the weight $h''$ + sub-resolution, a different and a priori weaker wall. That, together with the gift lemma $H_t|_{i\mathbb{R}}>0$ (parity sealed along the whole flow), is what is usable from this audit.

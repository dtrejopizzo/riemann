# Doc 151 — Adversarial audit of Docs 145 and 148

**Program:** Riemann Hypothesis — Phase 48: audit and purity.
**Mandate:** kill before use. Every load-bearing piece of Docs 145 (spectrality of the semilocal object; collapse of H⁺) and 148 (GAP-135.A as a frame problem) is attacked with the tools of Bochner, spectral measures, and Beurling–Landau. Post-W_λ discipline: no deference.
**Sources read in full:** Doc 145, Doc 148, Doc 142 (Theorems A/B, trilemma §8, GAP-142.A/B), Doc 135 §1–§7 (exact normalizations, §5 fine structure, Obs. 5.7), Doc 131 §4–§7 (Def. 4.1 spectral-EF, Thm. 4.4, Def. 6.1 Axiom H, Thm. 6.3, Desideratum 6.9 = H⁺), P48 `main.tex` (Conjecture 7.1).
**Contract:** [THEOREM]/[PROPOSITION] only with a complete proof here; [BRIDGE] with status; [GAP] named; [DATUM] real literature; [literature GAP] flagged. No numerics: closed form only.

---

## 0. Verdict per piece

| Piece | Statement | Verdict |
|---|---|---|
| **A.a** (D145 Thm 2.2) | $\mathcal B_w$ spectrally-positive representable $\iff w\ge0$ a.e. | **HOLDS** for the continuous notion (Def. 2.1). Wording erratum: the phrase "equivalently, sum of squares of evaluations" confuses the atomic notion with the continuous one (§1.2). The load-bearing direction (negative part ⟹ no positive measure ⟹ a fortiori no atomic one) is the one used and is correct. |
| **A.b** (D145 Thm 2.4) | $\Omega$ is not the transform of a positive measure; $\mathcal A$ indefinite | **HOLDS.** $\Omega(0)=\psi(\tfrac14)-\log\pi<0$ verified by Gauss (exact closed form); continuity + Thm 2.2 close the argument. |
| **A.c** (D145 Thm 3.4) | $X_S^{\mathrm{ar}}$ is not spectral-positive, "two independent proofs" | **HOLDS only via proof (A).** Proof (B) has a real [GAP] (§1.4): the step "window tests $<\log2$ with $\hat f(1)=0$ realize $\mathcal A<0$" is not proved and collides with GAP-142.A (open). "Two independent proofs, both complete" is **false**. Moreover: what is decided is spectral-**positive**; GAP-142.B in its literal formulation (Def. 4.1, spectral-EF) **remains open** (§2.3). |
| **A.d** (D145 Thm 4.1 + Cor 4.2) | semilocal-finite class of H⁺ empty; H⁺ collapses toward RH | **PARTIAL.** (i) Emptiness is proved only for $a=\Lambda\cdot\mathbf 1_S$; the class of H⁺ at finite $S$ allows any $a\ge0$. **Repaired here** ([PROP. R.2], §2.2: complete proof for every $a\ge0$). (ii) "The only nonempty instance with weight $\Gamma$ is complete $\zeta$": **not proved** (§2.4). (iii) Branch (1) of the trilemma is excluded by a reading stipulation, not by a theorem (§2.3). (iv) On the pure world there is NO overclaim: H⁺ requires a standard polar block, the pure ones do not have it, they were never in the class (§2.1). |
| **B.a** (D148 Prop 1.1+1.3+Obs 1.4) | two-prime Weil = Gram of $E(\Lambda)$; thresholds = Beurling–Landau | **HOLDS.** The identification is **exact, with no simplification of weights**: the arithmetic weights $2L_p\,p^{m/2}$ are absorbed in full via $e^{t/2}$ + Poisson (§4). Density $D^{\pm}(\Lambda)=\log(pq)/2\pi$ re-derived (§3.1). The direction confusion of Prop. 1.3 was honestly corrected in Obs. 1.4 and the final version is correct. |
| **B.b** (D148 Prop 2.2) | $E(\Lambda)$ is never a Riesz sequence | **HOLDS.** Re-derived in closed form (§3.2), for every $T>0$ and every choice of phases. |
| **B.c** (D148 Prop 2.4) | $\mu(T)=0$ throughout the intermediate region (no frame) | **DIES.** Double death: (1) the step "nearby terms $\asymp\sigma_n^2$" in its sketch is **false** — lattice neighbors receive mass $\Theta(1)$, not $O(\sigma_n^2)$ (§3.3); (2) **counterexample with a complete proof** ([THEOREM R.1], §3.4): $\mu(T)>0$ with an explicit constant in closed form for $\log q<2T\le\log q+\theta$, $\theta:=\mathrm{dist}(\log q,(\log p)\mathbb Z)>0$. Prop. 2.4 claimed $\mu(T)=0$ throughout THE WHOLE region: refuted. Prop. 2.3 (reduction to the $2\times2$ Gram minor) falls with it: an analysis/synthesis category error (§3.3). |
| **B.d** (D148 §3.2, §4) | "arithmetic is an epiphenomenon"; GAP-135.A essentially known | **DIES.** The constant and the validity window of Theorem R.1 are governed by $\theta=\min_{m\ge1}\bigl|\log(q/p^m)\bigr|$ — an **arithmetic** quantity (multiplicative closeness of $q$ to powers of $p$). Prop. 3.2(b) was conditional on Prop. 2.4 and falls with it. 3.2(a) (the **kernel** is of pure density) survives. The overall verdict "(a) KNOWN" is reversed: GAP-135.A **reopens**, with the likely answer **opposite** to that of Doc 148 (§3.5). |

---

## 1. Theorem 2.2 of Doc 145: discrete vs. continuous, and the quantification of the test class

### 1.1. The two notions, sharply separated

There are two distinct statements under the name "positive spectral representation":

- **(C) continuous:** there exists a Borel measure $\mu\ge0$ of polynomial growth with $\mathcal B(f)=\int|\hat F|^2\,d\mu$ for every $f\in C_c^\infty(G)$. (Def. 2.1 of Doc 145, as written.)
- **(D) discrete/program version:** $\mu=\sum_k m_k\delta_{\xi_k}$ atomic, $m_k\ge0$, polynomial density — i.e. $\mathcal B(f)=\sum_k m_k|\hat F(\xi_k)|^2$, the sense of Def. 1.2 (divisor on the line).

Obviously (D) ⟹ (C). The converse is **false**: $w\equiv1$ satisfies (C) with $\mu=$ Lebesgue and does not satisfy (D) (no atomic measure of polynomial density coincides with Lebesgue against all Fejér kernels $|\hat F|^2$, $F\in C_c^\infty$; pointwise evaluations do not reproduce an absolutely continuous density against a family that separates intervals). Hence the correct logical chain of Doc 145 is:

$$\text{(D) fails} \impliedby \text{(C) fails} \iff w\not\ge0 \text{ a.e.} \quad\text{(Thm 2.2)}.$$

**Verification of the direction used.** Thm 2.4 and Thm 3.4(B) use exactly the safe contrapositive: $\Omega(0)<0$ ⟹ not-(C) ⟹ not-(D). Thm 3.4(A) does not even go through this: it uses non-positivity of the form (Prop. 3.1 = Doc 142 Thm. B) against "(D) ⟹ $Q\ge0$". **Both uses are valid.** What is NOT valid is the phrase in Thm 2.4 "equivalently, $\mathcal A$ is not a sum of squares of evaluations": the negation of (C) and that of (D) are not equivalent (that of (C) is strictly stronger); since the strong one is proved here and the weak one is used, the error is one of wording, not of content. **Non-fatal erratum; replace "equivalently" with "in particular".** The same applies to the parenthetical in Def. 2.1, which should be read as "the atomic case is an instance", not as an identification.

### 1.2. The proof of Thm 2.2, audited step by step

(⟸) $w\ge0$ ⟹ (C) with $d\mu=w\,d\xi/2\pi$: trivial and correct. (⟹): the Lebesgue-point argument is correct with two refinements I verified:

1. **The test is not $C_c^\infty$ but Schwartz** ($\hat F_{\delta}$ of compact support ⟹ $F$ entire, not compact). The stated approximation works: $|\mathcal B_w(F)-\mathcal B_w(G)|\le\frac1{2\pi}\int(|\hat F|+|\hat G|)\,|\hat F-\hat G|\,|w|$ with $|w|\le C(1+|\xi|)^M$ is controlled by Schwartz seminorms, and $C_c^\infty$ is dense in $\mathcal S$. Valid.
2. **The limit of the average:** $\int\hat\phi(u)^2\,[w(\xi_0+\delta u)-w(\xi_0)]\,du\le\|\hat\phi^2\|_\infty\,\delta^{-1}\int_{|v|\le\delta}|w(\xi_0+v)-w(\xi_0)|\,dv\to0$ at any Lebesgue point of $w$; a.e. point of $E=\{w<0\}$ is a Lebesgue point with $w(\xi_0)<0$ if $|E|>0$. Valid. (The subscript $R$ of $F_{\delta,R}$ is vestigial: never used. Cosmetic.)

**Verdict A.a: Theorem 2.2 is correct as a theorem about notion (C), with the erratum of §1.1.** The label "Bochner on the multiplier side" is honest [DATUM: Bochner, *Lectures on Fourier Integrals*, Princeton 1959; Reed–Simon II, Thm IX.9 (Bochner–Schwartz) for the distributional version].

### 1.3. Quantification of the test class: over which class is "spectral-positive" defined?

This was the most dangerous point of attack, and I verified it against the three sources:

- Doc 131, Def. 6.1 (Axiom H): "$Q_X(f,f)\ge0$ **for all** $f\in C_c^\infty(G)$".
- Doc 131, Def. 4.1 / Doc 145, Def. 1.1 (spectral-EF): the identity $\sum_{\rho\in Z}\hat f(\rho)=W_X(f)$ is required **for all** $f\in C_c^\infty(G)$.
- P48, Conjecture 7.1 (H⁺): hypothesis about the object, conclusion "$X$ satisfies $H$" — again all of $C_c^\infty(G)$.

**There is no class restriction in any definition** (no $\hat f(1)=0$, no window). The polar block is part of $W_X$, not a condition on the tests. Hence the hypothetical danger ("a $w$ with a negative part invisible to a restricted class") **does not affect the verdict of Thm 3.4**, whose proof (A) uses a legitimate test from the full class (the family $f_T$ of Doc 142, $f_T\in C_c^\infty(G)$ with no restrictions).

**But the danger is realized INSIDE proof (B).** That is §1.4.

### 1.4. [GAP-151.C] Proof (B) of Thm 3.4 is not complete

Proof (B) restricts to the subclass $\mathcal R=\{f:\mathrm{supp}\,F$ in an interval of length $\ell<\log2$, $\hat f(1)=0\}$, on which $Q_S=\mathcal A$ exactly (this part is correct: the lags $mL_p\ge\log2>\ell$ annihilate $P_S$, and $\hat f(1)=0$ kills the polar term). It then states: if $\mu\ge0$ represented $Q_S$ on the full class, then $\mathcal A(f)=\int|\hat F|^2d\mu\ge0$ on $\mathcal R$ — correct — and that this "contradicts Theorem 2.4". **Here lies the gap:** Theorem 2.4 gives indefiniteness of $\mathcal A$ over the **full** class; the contradiction requires $f\in\mathcal R$ with $\mathcal A(f)<0$, i.e. that the negativity of $\Omega$ in $(-\xi_*,\xi_*)$ be **attainable with windows shorter than $\log2$ and zero exponential moment**. This:

1. **is not proved** in the document (the phrase "the low-frequency spectral mass is obtained with wide tests" is exactly what the subclass forbids: $\ell<\log2$ forces spectral width $\gtrsim1/\ell$, and the proof of Thm 2.2 needs $\delta\to0$, impossible here);
2. **collides with GAP-142.A**, which is precisely the open question of the sign of $\mu_\varnothing(T)$ in intermediate windows (Doc 142 proves positivity for $2T\le\tfrac1{150}$ and negativity for $T\ge T_1$ large; the range $\ell<\log2$ is in no man's land);
3. the "alternatively the wide family $f_T$" of the text itself abandons $\mathcal R$ ($P_S\ne0$ there) and reduces (B) to (A).

**Conclusion:** the claim "two independent proofs, both complete" is false. Theorem 3.4 stands **only** via route (A): spectral-positive ⟹ $Q_S\ge0$ (Doc 131 Prop. 6.2) against $Q_S(f_T)<0$ (Doc 142 Thm. 5.1, whose proof I verified line by line: $c_T\le C_\eta e^{-T/8}$, dominated convergence of the archimedean term with the dominator of Lemma 2.4(b), convergence of the prime term to $B_S\|\eta\|_2^2$ — solid). The "archimedean localization of the obstruction" that (B) intended is a reasonable [DESIDERATUM], not a theorem; name it **GAP-151.C** (does there exist $f$ with window $<\log2$, $\hat f(1)=0$ and $\mathcal A(f)<0$? — it is a fragment of GAP-142.A).

---

## 2. The real scope of the collapse of H⁺

### 2.1. What H⁺ exactly says, and the pure world

P48, Conjecture 7.1 (identical to Doc 131, Desideratum 6.9): *"If $X$ is hermitian, spectral, with datum $a\ge0$ supported on prime powers (Euler product), **standard polar block**, and **archimedean weight of $\zeta$-type**, then $X$ satisfies $H$."*

The hypotheses include the polar block $[0]+[1]$ and the archimedean weight of $\zeta$-type. The pure objects of Doc 135 ($F_{p,\alpha}\star F_{q,\alpha'}$, two-sided purity) have $c=0$ (no polar block) and $\omega\equiv-2\log(pq)$ constant (Doc 131, Prop. 6.6'): **they do not satisfy the hypotheses of H⁺**. P48 itself calls its two-prime theorem "the constructive **sibling** of $H^+$", not an instance. Hence, on the axis the task pointed to: **"H⁺ collapses" does not erase any content of the pure world, because H⁺ never said anything about it.** The two-prime theorem, the $n$-prime theorem, and the whole constructive family remain intact and independent of the verdict of Doc 145. No overclaim here.

### 2.2. The real overclaim of Corollary 4.2, and its repair

Cor. 4.2 states "the semilocal class of H⁺ is empty", but what is proved (Thm 3.4) covers only the objects $X_S^{\mathrm{ar}}$ with $a=\Lambda\cdot\mathbf 1_S$. The class of H⁺ at finite $S$ is $\{(a,[0]+[1],\omega_\zeta):a\ge0$ supported on $\{p^m:p\in S\}\}$ with $a$ **arbitrary**. Theorem B of Doc 142 is not cited for general $a$, and in fact its proof does not apply as is ($G_T$ is not $\ge0$ term by term, and a giant $a$ on a single prime could, in principle, dominate). The gap is real but **repairable**, and the repair is the following, with a complete proof.

**[LEMMA R.2.a] (spectral Ramanujan: spectrality on the line bounds the datum).** Let $X=(a,[0]+[1],\omega_\zeta)$ be hermitian, $a\ge0$ supported on prime powers, **spectral-positive** (Def. 1.2: divisor $Z\subset\{\mathrm{Re}=\tfrac12\}$, polynomial density, $\sum_{\rho\in Z}\hat f(\rho)=W_X(f)$ with absolute convergence, $\forall f\in C_c^\infty(G)$). Then there exists $C_X<\infty$ with
$$a(p^m)\;\le\;C_X\,p^{m/2}\qquad\text{for every }p^m.$$

*Proof.* Fix $b\in C_c^\infty(\mathbb R)$ real, $\mathrm{supp}\,b\subset(-\tfrac14\log2,\tfrac14\log2)$, and define $h:=-b''+\tfrac14 b$, so that $\hat h(z)=(z^2+\tfrac14)\hat b(z)$ is entire with zeros at $z=\pm\tfrac i2$. Choose $b$ with $h(0)=-b''(0)+\tfrac14b(0)\ne0$ (possible: an even bump with $b''(0)<0$). For each $p^m$ let $F_m(t):=h(t-mL_p)$ and $f_m$ the corresponding test. Then: (i) $\hat f_m(1)=\hat F_m(-\tfrac i2)=e^{mL_p/2}\hat h(-\tfrac i2)=0$ and $\hat f_m(0)=\hat F_m(\tfrac i2)=0$: **polar block $=0$ exact for every $m$** (the translation multiplies the transform by a phase that does not move the zeros). (ii) The support of $F_m$ has length $<\log2$ and is centered at $mL_p$: the arithmetic side of $W_X(f_m)$ touches only $n=p^m$, with contribution $-a(p^m)\,p^{-m/2}\cdot 2h(0)$ (normalization of Doc 142, Obs. 1.3(ii); the mirror $F_m(-mL_p)=0$). (iii) The archimedean linear term is $\frac1{2\pi}\int\hat F_m(\xi)\Omega(\xi)\,d\xi$ with $|\hat F_m|=|\hat h|$ Schwartz and $|\Omega(\xi)|\le\log(4+|\xi|)+6$ (Doc 142, Lemma 2.4(b)): bounded by $\|\hat h\,\Omega\|_{L^1}$, **uniform in $m$**. (iv) The spectral side: $\bigl|\sum_{\rho\in Z}\hat f_m(\rho)\bigr|\le\sum_{\gamma}|\hat h(\gamma)|\le C_k\sum_\gamma(1+|\gamma|)^{-k}<\infty$ by polynomial density and Paley–Wiener decay, **uniform in $m$** (the phase $e^{i\gamma mL_p}$ is unimodular: here it is crucial that $Z$ lie ON the line; with an off-line divisor the factor would be $e^{(\beta-1/2)mL_p}$ and the bound would be lost). Solving in the explicit formula: $a(p^m)p^{-m/2}\,2|h(0)|\le$ (iii) + (iv) $=:2|h(0)|\,C_X$. $\square$

**[PROPOSITION R.2] (emptiness, repaired for every $a\ge0$).** There exists no hermitian object $X=(a,[0]+[1],\omega_\zeta)$ with $a\ge0$ supported on prime powers of a **finite** set $S$ that is spectral-positive.

*Proof.* Suppose one exists. By Prop. 6.2 of Doc 131, $Q_X\ge0$ on the full class. By Lemma R.2.a, $a(p^m)\le C_Xp^{m/2}$. Take the family $f_T$ of Doc 142 Thm. 5.1 with the strengthening $\eta\ge0$ (allowed: $\eta\in C_c^\infty(0,\tfrac38)$, $\eta\ge0$, $\eta\not\equiv0$; $\eta_2\ge0$ as there). Then $G_T(t)=\int\eta_c(u)\eta_c(u-\tfrac tT)\,du$ with $\eta_c=\eta-c_T\eta_2$ satisfies, for every $t$,
$$G_T(t)\;\ge\;\underbrace{\int\eta\,\eta(\cdot-\tfrac tT)}_{\ge0}\;-\;2c_T\|\eta\|_2\|\eta_2\|_2\;+\;\underbrace{c_T^2\int\eta_2\,\eta_2(\cdot-\tfrac tT)}_{\ge0}\;\ge\;-2c_T\|\eta\|_2\|\eta_2\|_2$$
(autocorrelations of $\ge0$ functions are $\ge0$ at every lag). The prime term of $Q_X(f_T)$, with active lags $mL_p\le T$, satisfies
$$P^{(a)}(f_T)\;=\;\sum_{p\in S}\sum_{mL_p\le T}\frac{a(p^m)}{p^{m/2}}\,2\mathrm{Re}\,G_T(mL_p)\;\ge\;-4c_T\|\eta\|_2\|\eta_2\|_2\cdot C_X\cdot\#\{(p,m):mL_p\le T\}\;\ge\;-C'_X\,c_T\,T,$$
and $c_T\,T\le C_\eta Te^{-T/8}\to0$. The polar term is $0$ exact, and $\mathcal A(f_T)\to\Omega(0)\|\eta\|_2^2$ as in Doc 142. Hence $\limsup_T Q_X(f_T)\le\Omega(0)\|\eta\|_2^2<0$: contradiction with $Q_X\ge0$. $\square$

With R.2, the statement of Cor. 4.2 moves from overclaim to theorem. **Note what saved it:** the spectral-positive hypothesis was used TWICE (positivity of the form AND a Ramanujan bound on the datum) — the second was not in Doc 145 and is necessary for general $a$.

### 2.3. The trilemma: branch (1) is closed by stipulation, not by a theorem

GAP-142.B, as formulated in Doc 142 §7, asks about spectrality **in the sense of Doc 131, Def. 4.1** (spectral-EF: divisor anywhere, positive multiplicities, polynomial density). Doc 145 answers a different question (spectral-**positive**) after arguing (Obs. 1.3) that this is "the only substantive reading of H⁺". Three audit remarks:

1. **What is proved is exactly:** $X_S^{\mathrm{ar}}$ is not spectral-positive (Thm 3.4 via (A); now R.2 for every $a\ge0$). Under the adopted reading, the operative branch of the trilemma is (2) and the reasoning of Doc 145 is valid.
2. **What is NOT proved:** that $X_S^{\mathrm{ar}}$ is not spectral-EF. Obs. 3.5 of Doc 145 itself concedes this ("Spectral-EF: possibly"), but the headline ("the semilocal object is NOT spectral") and the "Final message" suppress it. Under the EF reading of H⁺, branch (1) — H⁺ refuted by Theorem B — **remains logically open**: it depends on whether an EF divisor exists, which is precisely the "divisor uniqueness theorem" that Doc 142 left missing. Obs. 1.3 dismisses the EF reading by claiming it would make H⁺ "trivially false for reasons unrelated to the semilocal case"; but that falsehood requires exhibiting an object of the spectral-EF class with an off-line divisor — whose only candidate is $X_S^{\mathrm{ar}}$ itself. The reading argument is therefore a **reasonable stipulation**, not a proof; the document should have said so.
3. **Two internal frictions the final version must correct:** (i) Obs. 1.4 claims "off-line divisor ⟹ $Q_X$ indefinite" citing Lemma 4.3 of Doc 131, but Doc 131 declares the block→full form transport as [BRIDGE] except for finite or lattice divisors (§6.1, parenthetical after Thm. 6.3); for general infinite divisors it remains Hypothesis-D-type. (ii) Obs. 2.5/3.5 proposes as an EF divisor the trivial zeros $s=-2,-4,\dots$ — which have **unbounded real parts** and hence are not even admissible under Def. 1.1 (which requires bounded real parts). This, far from damaging the verdict, is **evidence in favor** of non-spectral-EF-ness in a bounded band; but it must be decided, not hinted at. Name it **GAP-151.B**: does $W_{X_S^{\mathrm{ar}}}$ admit an EF divisor in the band $|\mathrm{Re}\,\rho-\tfrac12|\le A$ with polynomial density? (The surviving content of literal GAP-142.B. The expected obstruction: an atomic measure in a band cannot reproduce the continuous density $\Omega\,d\xi$ plus the "half-mast" atoms of truncated primes — the kind of uniqueness that is missing.)

### 2.4. "The only nonempty instance is complete $\zeta$": not proved

Thm 4.1(c) infers from finite emptiness that the class of H⁺ with weight $\Gamma$ reduces to $\zeta_{\mathrm{ob}}$. With R.2 what is obtained is: **every object of the class must have $a$ supported on infinitely many primes.** From there to "it is $\zeta$" there is a jump: the class could contain other data $a\ge0$ of infinite support with exactly the weight $\Omega$ (the analogy with the degree-1 classification of the Selberg class — [DATUM: Kaczorowski–Perelli, *On the structure of the Selberg class, I: $0\le d\le1$*, Acta Math. 182 (1999), 207–241] — suggests that with weight exactly $\Gamma_{\mathbb R}$ and a standard pole the object is essentially $\zeta$, but that theorem lives in the Selberg class with analytic continuation and a functional equation, hypotheses the EF category does not include; **it is not pluggable**). The honest, proved statement is:

> **H⁺ has no instances with $S$ finite (R.2). Every instance has an Euler product of infinite support, and for the instance $\zeta_{\mathrm{ob}}$, spectral-positive ⟺ RH (Weil). The semilocal rung does not exist.**

The slogan "H⁺ collapses toward RH" is defensible as a summary of this; the phrase "unique instance" must be downgraded or proved. Likewise, under the adopted reading H⁺ is trivially **true** (spectral-positive ⟹ H is Prop. 6.2: the "conjecture" has the conclusion inside the hypothesis), as Obs. 4.3 already notes: the net result of Docs 142+145 is that **H⁺ was ill-posed as a conjecture** — trivial under one reading, undecided-and-probably-empty-of-candidates under the other. That is the correct pruning statement.

---

## 3. Doc 148: density, separation, and the death of Prop. 2.4

### 3.1. The Beurling–Landau density, re-derived

Definition [DATUM: Beurling; Landau 1967; Seip 2004, ch. 2]: $D^+(\Lambda)=\lim_{r\to\infty}\sup_{x}\frac{\#(\Lambda\cap[x,x+r])}{r}$, $D^-$ with $\inf$. For $\Lambda_r=\{(\phi_r+2\pi k)/L_r:k\in\mathbb Z\}$: $\#(\Lambda_r\cap[x,x+r])=\frac{rL_r}{2\pi}+O(1)$ **uniform in $x$**. For the union: $\Lambda_p\cap\Lambda_q$ has at most one point (two coincidences would give $L_p/L_q\in\mathbb Q$; Doc 135, Lemma 1.7), hence
$$\#(\Lambda\cap[x,x+r])=\frac{r(L_p+L_q)}{2\pi}+O(1)\ \text{uniform}\implies D^-(\Lambda)=D^+(\Lambda)=\frac{\log(pq)}{2\pi}.$$
Both densities exist and coincide **even though $\Lambda$ is not separated** (Beurling's definitions do not require separation). Landau's necessary conditions (sampling: $D^-\ge T/\pi$; interpolation: $D^+\le T/\pi$) and the identification of the critical point $2T=\log(pq)$ of Doc 148 are correct; the completeness direction used in the sub-critical region does not need Landau: the Jensen proof of Doc 135 (Thm. 5.4(a)) is rigorous and I verified its bookkeeping ($n(r)\ge\frac{L_p+L_q}{\pi}r-C_0$ against type $\frac{2TR}\pi$; correct). The self-correction in Obs. 1.4 (sub-critical = complete, super-critical = $\infty$-dim kernel) is the correct association. **B.a holds.**

### 3.2. Separation and Riesz, re-derived

For $\xi\ne\eta$ and any $T>0$:
$$\|e_\xi-e_\eta\|_{L^2(-T,T)}^2=\int_{-T}^{T}\bigl|1-e^{i(\eta-\xi)t}\bigr|^2dt=4T-\frac{4\sin((\eta-\xi)T)}{\eta-\xi}=4T\Bigl(1-\mathrm{sinc}\,\bigl((\eta-\xi)T\bigr)\Bigr)\xrightarrow[\eta\to\xi]{}0,$$
with asymptote $\tfrac23T^3(\eta-\xi)^2$. If $E(\Lambda)$ were a Riesz sequence with lower bound $A$, the coefficient vector $(1,-1)$ supported on $\{\xi,\eta\}\subset\Lambda$ would give $\|e_\xi-e_\eta\|^2\ge2A$ — impossible if $\Lambda$ contains distinct pairs arbitrarily close together. And it does contain them, **for every choice of phases**: the set of differences $\bigl\{\tfrac{\phi_p+2\pi k}{L_p}-\tfrac{\phi_q+2\pi l}{L_q}\bigr\}$ is a translate of the dense subgroup $\tfrac{2\pi}{L_p}\mathbb Z+\tfrac{2\pi}{L_q}\mathbb Z$ (dense because $L_p/L_q\notin\mathbb Q$, Kronecker), hence it accumulates at $0$ with pairs $\xi\ne\eta$ (equality occurs at most once). This holds for **every $T>0$** — the near-collisions sit at high frequency, but the Riesz bound is uniform over all pairs, so the frequency is irrelevant. The citation to Young is correct in spirit [DATUM: R. M. Young, *An Introduction to Nonharmonic Fourier Series*, rev. ed. 2001, ch. 4: separation necessary for bases/Riesz sequences of exponentials], and in any case the above computation is self-contained. **B.b holds.**

### 3.3. Prop. 2.4: the exact dead step, and the conceptual error

**The dead step.** The sketch takes $F_n(t)=c_n\bigl(e^{i\xi_nt}-e^{i\eta_nt}\bigr)\psi(t)$, $\sigma_n=|\xi_n-\eta_n|\to0$, and normalizes: $\|F_n\|_2^2=c_n^2\int4\sin^2(\sigma_nt/2)|\psi|^2\sim c_n^2\sigma_n^2\int t^2|\psi|^2$, hence $c_n\asymp\sigma_n^{-1}$. It claims that "the nearby terms (neighbors in $\Lambda_p,\Lambda_q$ at distance $\gtrsim2\pi/L_r$) give $\asymp\sigma_n^2$". **False.** At the neighbor $\zeta_0=\xi_n+2\pi/L_p\in\Lambda_p$:
$$\hat F_n(\zeta_0)=c_n\Bigl[\hat\psi\bigl(\tfrac{2\pi}{L_p}\bigr)-\hat\psi\bigl(\tfrac{2\pi}{L_p}+\sigma_n\bigr)\Bigr]=-c_n\,\sigma_n\,\hat\psi'\bigl(\tfrac{2\pi}{L_p}\bigr)+O(c_n\sigma_n^2)\;\xrightarrow[n\to\infty]{}\;-\frac{\hat\psi'(2\pi/L_p)}{\bigl(\int t^2|\psi|^2\bigr)^{1/2}}\;\ne\;0$$
for generic $\psi$: the amplification $c_n\asymp\sigma_n^{-1}$ turns the $O(\sigma_n)$ side lobe into $\Theta(1)$. Hence $Q_X(F_n)\ge2|\hat F_n(\zeta_0)|^2\to\mathrm{const}>0$: **the family does not witness $\mu(T)\to0$**. (The [GAP] the document itself flagged was in the Bessel tail; the fatal error comes earlier, in the immediate neighbors. Note also that the sketch needs $\hat\psi'(0)=0$, i.e. $\psi$ even, for its estimate at $\xi_n$ — not stated; minor compared to the above.)

**The conceptual error (why it was never going to work).** $\mu(T)$ is the lower **frame** bound (analysis operator): $\sum_{\xi\in\Lambda}|\langle F,e_\xi\rangle|^2$ is **monotonically increasing when points are added to $\Lambda$**. An exact collision (duplicated vector) ADDS a term $\ge0$: it improves the frame and destroys Riesz. Near-collisions degrade the **synthesis** bounds (Riesz, Gram minor — which is what Prop. 2.3 computes) but do not push the analysis inequality downward. Prop. 2.3 ("$\mu(T)$ is controlled by the $2\times2$ Gram minor"; "standard for frames") transplants a synthesis quantity to an analysis bound: a **category error**; no such standard fact exists (the standard one is for Riesz sequences). Prop. 2.3 falls with 2.4.

### 3.4. [THEOREM R.1] The counterexample: there is a frame gap in an explicit sub-window

**[THEOREM R.1].** Let $p<q$ be primes, $L_p=\log p$, $L_q=\log q$, arbitrary phases $\phi_p,\phi_q$, $\Lambda=\Lambda_p\cup\Lambda_q$, and
$$\theta\;:=\;\mathrm{dist}\,\bigl(L_q,\;L_p\mathbb Z\bigr)\;=\;\min_{m\ge1}\bigl|\log\tfrac{q}{p^m}\bigr|\;>\;0\qquad(\text{irrationality of }\tfrac{L_q}{L_p}).$$
For every window $2T$ with $\log q<2T\le\log q+\theta$ and every $f\in C_c^\infty(G)$ with support of $F$ in an interval of length $2T$:
$$Q_X(f,f)\;\ge\;c(p,q,T)\,\|f\|_w^2,\qquad c(p,q,T)\;=\;\min\Bigl(\frac{L_q}{2N},\;(2-\sqrt3)\,L_p\Bigr)\;>\;0,\quad N:=\Bigl\lfloor\frac{2T}{L_p}\Bigr\rfloor+2.$$
In particular $\mu(T)>0$ on $(\log q,\;\log q+\theta\,]$: **Proposition 2.4 of Doc 148 is false.**

*Proof.* By invariance of $|\hat F|$ under translation of the window, assume $\mathrm{supp}\,F\subset[-T,T]$, $\|F\|_2=1$, and write $\varepsilon:=Q_X(f,f)$, $s:=2T-L_q\in(0,L_p]$ (note $s\le\theta\le L_p/2<L_p$).

**(0) Periodization with phases.** For $r\in\{p,q\}$ let $F_r(t):=F(t)e^{i\phi_rt/L_r}$ (so $\hat F\bigl(\tfrac{\phi_r+2\pi k}{L_r}\bigr)=\hat F_r\bigl(\tfrac{2\pi k}{L_r}\bigr)$, and $|F_r|=|F|$) and $P_r(t):=\sum_{m\in\mathbb Z}F_r(t+mL_r)$ its periodization. Parseval for the Fourier series of $P_r$ on $\mathbb R/L_r\mathbb Z$ gives, with no overlap assumption whatsoever,
$$\sum_{\xi\in\Lambda_r}|\hat F(\xi)|^2\;=\;L_r\int_{\mathbb R/L_r\mathbb Z}|P_r|^2,\qquad\text{hence}\qquad \varepsilon\;=\;2L_p\!\int|P_p|^2+2L_q\!\int|P_q|^2 .$$

**(1) Side $q$: the mass concentrates at the edges.** Since $2T=L_q+s<2L_q$, each class mod $L_q$ has at most two representatives in $[-T,T]$. Define the edges $A:=(-T,-T+s)$, $B:=(T-s,T)$ — note the exact identity $B=A+L_q$ (since $-T+L_q=T-s$) — and the center $M:=[-T+s,\,T-s]$, of length $L_q-s>0$. For a.e. $\tau\in M$: $\tau\pm L_q\notin(-T,T)$, so $P_q(\tau)=F_q(\tau)$ (a single term). Then
$$\|F\mathbf 1_M\|_2^2\;=\;\int_{M}|P_q|^2\;\le\;\int_{\mathbb R/L_q\mathbb Z}|P_q|^2\;\le\;\frac{\varepsilon}{2L_q}\;=:\;\varepsilon_1,\qquad \|F\mathbf 1_A\|_2^2+\|F\mathbf 1_B\|_2^2\;\ge\;1-\varepsilon_1 .$$

**(2) Side $p$: the two edges cannot cancel mod $L_p$.** Decompose $F=F_A+F_B+F_M$ (restrictions to $A,B,M$) and $P_p=P_p[F_A]+P_p[F_B]+P_p[F_M]$. Since $|A|=|B|=s<L_p$, the projection $\mathbb R\to\mathbb R/L_p\mathbb Z$ is injective on $A$ and on $B$: $P_p[F_A]$ and $P_p[F_B]$ are **isometric** transplants to arcs $\bar A,\bar B$ of length $s$ on the circle. Since $B=A+L_q$, we have $\bar B=\bar A+\delta$ with $\delta\equiv L_q\ (\mathrm{mod}\ L_p)$, and the circular distance of the shift is $\min(\delta,L_p-\delta)=\theta$. Two arcs of length $s$ shifted by $\theta\ge s$ are **disjoint** (modulo a null set if $s=\theta$). By disjoint supports,
$$\bigl\|P_p[F_A]+P_p[F_B]\bigr\|_{L^2(\mathbb R/L_p\mathbb Z)}^2=\|F_A\|_2^2+\|F_B\|_2^2\;\ge\;1-\varepsilon_1 .$$
For the center: $P_p[F_M]$ sums at most $N=\lfloor 2T/L_p\rfloor+2$ translates, hence (Cauchy–Schwarz on the finite sum) $\|P_p[F_M]\|^2\le N\|F_M\|_2^2\le N\varepsilon_1$. By the triangle inequality,
$$\Bigl(\int|P_p|^2\Bigr)^{1/2}\;\ge\;\sqrt{1-\varepsilon_1}-\sqrt{N\varepsilon_1}.$$

**(3) Dichotomy.** If $\varepsilon>\tfrac{L_q}{2N}$, we are done. If $\varepsilon\le\tfrac{L_q}{2N}$, then $\varepsilon_1\le\tfrac1{4N}\le\tfrac14$ and $N\varepsilon_1\le\tfrac14$, hence $\bigl(\int|P_p|^2\bigr)^{1/2}\ge\sqrt{3}/2-1/2$ and
$$\varepsilon\;\ge\;2L_p\Bigl(\frac{\sqrt3-1}{2}\Bigr)^2\;=\;(2-\sqrt3)\,L_p .$$
In either case $\varepsilon\ge c(p,q,T)$. $\square$

**Exact remarks.** (i) For $p=2,q=3$: $\theta=\min(\log\tfrac32,\log\tfrac43)=\log\tfrac43$, and the theorem gives a frame gap for $\log3<2T\le\log4$ — a sub-window of length $\log\tfrac43$ of the intermediate region $(\log3,\log6)$, with $c=\min(\tfrac{\log3}{8},(2-\sqrt3)\log2)$ in closed form. (ii) The proof uses NEITHER Baker's theorem NOR the irrationality measure: it uses only $\theta>0$ and support geometry; high-frequency near-collisions are invisible to it because they only affect the **phases** of the periodizations, never the supports. This structurally explains why the mechanism of Prop. 2.4 never existed. (iii) [literature GAP] I know of no published theorem that exactly covers "frames of exponentials over incommensurable $\alpha\mathbb Z\cup\beta\mathbb Z$ in windows super-critical for one progression and sub-critical for the union"; the double-periodization argument is elementary and could be folklore of non-uniform periodic sampling (Kohlenberg is the commensurable case), but I cannot point to the reference. Modesty, not priority, is claimed.

**[BRIDGE R.1′] (the rest of the intermediate region; status: argument, not theorem).** For $\theta<s<L_p$ (i.e. $\log q+\theta<2T<\log pq$) the arcs $\bar A,\bar B$ overlap over a length $s-\theta$, and the two near-cancellation conditions combine into: (a) $|F_A|$ small on an edge strip of width $\theta$ (the part of $\bar A$ not covered by $\bar B$); (b) $F_A(u)\approx e^{i\gamma}F_A(u\mp\theta)$ on the overlap (quasi-invariance under the shift $\theta$, with fixed phase). Iterating (b) from strip (a) in $\lceil s/\theta\rceil$ steps, each with error $O(\sqrt\varepsilon)$, gives $\|F_A\|\lesssim(s/\theta)\sqrt\varepsilon$, whence $\mu(T)\gtrsim(\theta/s)^2$ — **frame throughout the whole intermediate region, with a constant degrading polynomially in $s/\theta$** and dropping to $0$ exactly at the critical point $2T=\log pq$ (where the kernel $D_pD_qg$ appears), replicating the discontinuity of the single-progression case ($\mu=L_q$ constant up to $2T=L_q$, then $0$). Missing: the bookkeeping of circle-wraparound cases and the rigorous accumulation of errors. Name it **GAP-151.A**: prove $\mu(T)\asymp_{p,q}\min\bigl(1,(\theta/s)^2\bigr)$-type on $\log q<2T<\log pq$. This is exactly GAP-135.A reopened, now with the direction of the answer reversed relative to Doc 148 and with the correct Diophantine quantity identified ($\theta$ and the orbit of $L_q$ mod $L_p$ — the natural apparatus is that of the three-distance theorem/continued fractions of $L_q/L_p$ [DATUM: three-distance theorem, Sós–Świerczkowski 1957–58], not the irrationality measure).

### 3.5. Consequences for verdicts B.c and B.d

- **B.c dies twice:** the sketch is broken at an identified step (§3.3) and the statement is refuted by Theorem R.1 on the sub-window $(\log q,\log q+\theta]$. Obs. 5.7 of Doc 135 (the optimism that $\mu(T)>0$) is **partially vindicated with a theorem**, not refuted.
- **B.d dies:** arithmetic is NOT an epiphenomenon. The quantity $\theta=\min_m|\log(q/p^m)|$ — how close $q$ is to a power of $p$ — governs the proved window and (via R.1′) the constant in the rest. What does survive from Prop. 3.2 is part (a): the **kernel** (sign, not magnitude) is of pure density; that was already in Doc 135. Prop. 3.4 (effective band, $\mu_R(T)\gtrsim R^{-2\kappa}$) is **superseded** on the sub-window (R.1 is stronger: no band and no Baker) and unmotivated on the rest if R.1′ closes; its rhetorical premise ("only the version with band is positive") is false.
- The overall verdict of Doc 148 — "GAP-135.A is essentially known" — **is reversed**: the parts that were known (density thresholds, non-Riesz) were already in Doc 135 or are elementary; the part Doc 148 believed it had resolved negatively ($\mu(T)=0$) is false; and what remains (GAP-151.A and the exact determination of $\mu(T)$) is plausibly **modest, genuine new mathematics**. The negative [BRIDGE] of §5 of Doc 148 (does not scale to $\zeta$: infinite total density breaks the interval-frame framework) **survives** — it did not depend on Prop. 2.4 — so the reopening of GAP-135.A does not turn it into a link toward RH.

---

## 4. The weights in the Gram ↔ Weil identification (attack resolved in favor of Doc 148)

It was feared that the identification in Prop. 1.1 might ignore the weights $\log p/p^{m/2}$ of the Weil form. Verified against the exact normalizations: **there is no such loss; the identification is an identity.** The bookkeeping, step by step:

1. **Arithmetic side (Doc 131, Prop. 6.6′; Doc 135 §6):** the pure object has $W_X(f)=L_p\sum_m c_mf(p^m)+L_q\sum_nc'_nf(q^n)$ with $c_m=2\alpha^m$, $|c_m|=2p^{m/2}$ under purity. The exponential weights $p^{m/2}$ and the prefactors $L_p$ are there.
2. **The unitary change:** $F(t)=f(e^t)e^{t/2}$ — the factor $e^{t/2}$ turns $p^{m/2}f(p^m)$ into $F(mL_p)$ (with the phase $\phi$ absorbed in the twist): the Ramanujan weights **cancel exactly** against the weight of the change of variables. It is the same cancellation that makes $\|f\|_w=\|F\|_{L^2}$.
3. **Poisson (Doc 131, Thm. 6.6):** $\sum_{\rho\in Z(\alpha)}\hat f(\rho)=L\sum_m\alpha^mf(p^m)$ — the prefactor $L$ lives on the arithmetic side; the spectral side is the sum **with no weights** over the progression. Applied to $g=f\star\tilde f$ under purity: $Q_X(f,f)=2\sum_{\Lambda_p}|\hat F|^2+2\sum_{\Lambda_q}|\hat F|^2$ — which is the formula that opens §5 of Doc 135 (a line of its Thm. 3.1). The "2" is multiplicity ($Z(\alpha)=Z(p/\bar\alpha)$ under purity), not a decaying weight.

Conclusion: the exponential system of Doc 148 is genuinely **unweighted**, the thresholds do not move, and the frame bound $A$ is exactly $2\mu(T)$ with the $\mu(T)$ of Doc 135 (Obs. 5.7). The weights $\log p/p^{m/2}$ the attack recalled belong to the normalization of the **destructive** regime (the $P_S$ of Doc 142, datum $a=\Lambda$), which is a different object. **B.a certified also on this front.**

---

## 5. Consequences for Docs 145/148 and the program map

### 5.1. Doc 145 — required corrections (the central verdict survives)

1. **Thm 2.4 and Def. 2.1:** downgrade "equivalently" to "in particular" (discrete vs. continuous, §1.1). Non-fatal.
2. **Thm 3.4:** remove "two independent proofs, both complete"; proof (B) is downgraded to [BRIDGE/GAP-151.C] (§1.4). The theorem stands via (A).
3. **Headline and Final message:** "NOT spectral" should read "NOT spectral-**positive**"; EF-spectrality (the literal question of GAP-142.B) remains open as **GAP-151.B** (§2.3), with the new observation that Def. 1.1 (bounded real parts) disqualifies the "trivial zeros" divisor of Obs. 2.5.
4. **Cor. 4.2:** extend from $a=\Lambda\mathbf 1_S$ to every $a\ge0$ using [LEMMA R.2.a] + [PROP. R.2] of this audit (§2.2) — with this, the statement "semilocal-finite class empty" becomes true as written.
5. **Thm 4.1(c):** "the only nonempty instance is $\zeta$" → "every instance has infinite Euler support; the semilocal rung does not exist; for $\zeta_{\mathrm{ob}}$, spectral-positive ⟺ RH" (§2.4).
6. **Intact:** Thm 2.2 (with erratum), Thm 2.4, the survivors of §5 (Theorem A, transmission, cone — verified that none uses representation), and the pruning of the semilocal interpolation route, which with R.2 becomes **stronger** than before.

### 5.2. Doc 148 — required retractions (the central verdict falls)

1. **Retract** Prop. 2.3, Prop. 2.4, Prop. 3.2(b), the "quantitative verdict" of §2.3, rows 3 and 4 of the table in §4, and the slogan "arithmetic is an epiphenomenon".
2. **Record** Theorem R.1 (frame gap on $(\log q,\log q+\theta]$, closed-form constant) and GAP-151.A (remaining region, quasi-invariance route).
3. **Survive:** Prop. 1.1 (exact identification, §4), Prop. 1.3+Obs. 1.4 (thresholds), Prop. 2.2 (never Riesz), Prop. 3.2(a) (pure-density kernel), Theorem 3.1 (qualitative kernel), and all of §5 (non-scaling to $\zeta$).
4. The correct status of GAP-135.A: **open, partially resolved in the positive (R.1), with a candidate for the complete answer "frame throughout the intermediate region" (R.1′), and governed by the orbit of $L_q$ mod $L_p$ — not by the irrationality measure (against Doc 135) nor by anything trivial (against Doc 148).**

### 5.3. For `06-papers/ERRATA.md` and the map

- Erratum E-145.1 (discrete/continuous), E-145.2 (proof (B) incomplete), E-145.3 (scope of Cor. 4.2 — repaired by Doc 151 R.2), E-148.1 (Prop. 2.3/2.4 false; counterexample Doc 151 R.1), E-148.2 (overall verdict reversed).
- New GAPs: **GAP-151.A** (frame throughout the intermediate region; quasi-invariance by $\theta$), **GAP-151.B** (EF-spectrality in a bounded band of $X_S^{\mathrm{ar}}$; divisor uniqueness), **GAP-151.C** (archimedean negativity in window $<\log2$ with dead pole; sub-question of GAP-142.A).
- None of the corrections touch the structural theorems of the arc (short-window Theorem A, transmission identity, two-prime theorem, local purity): all re-verified at their points of contact during this audit.

---

## Final message

**Verdicts.** **A.a HOLDS** (with discrete/continuous erratum: the equivalence of Thm 2.2 is for general positive measures; the atomic version only inherits the negative direction — the one used). **A.b HOLDS** ($\Omega(0)=-\gamma-\tfrac\pi2-3\log2-\log\pi<0$, Gauss verified). **A.c HOLDS ONLY VIA PROOF (A)** — proof (B) has a real gap (the negativity of $\mathcal A$ in windows $<\log2$ with $\hat f(1)=0$ is not proved and is GAP-142.A territory); and what is decided is spectral-*positive*: the literal question of GAP-142.B (spectral-EF, Def. 4.1) remains open. **A.d PARTIAL**: emptiness proved only for $a=\Lambda\mathbf 1_S$ — **repaired here with a complete proof for every $a\ge0$** (Lemma R.2.a "spectral Ramanujan" + Prop. R.2); "unique instance = $\zeta$" not proved; on the pure world there is no overclaim (H⁺ requires a polar block; the pure ones do not have it). **B.a HOLDS** (Gram↔Weil identification **exact**: the weights $2L_pp^{m/2}$ cancel in full via $e^{t/2}$+Poisson; $D^\pm(\Lambda)=\log(pq)/2\pi$ re-derived). **B.b HOLDS** (never Riesz, for every $T$ and every phase; closed form $\|e_\xi-e_\eta\|^2=4T(1-\mathrm{sinc})$). **B.c DIES** (sketch broken + counterexample with a theorem). **B.d DIES** (arithmetic governs: $\theta=\min_m|\log(q/p^m)|$). The overall verdict of Doc 148 ("GAP-135.A essentially known") **is reversed**; that of Doc 145 (branch (2) of the trilemma, pruning of the semilocal interpolation) **survives with corrected and reinforced scope**.

**Three findings.**
1. **[THEOREM R.1] Prop. 2.4 of Doc 148 is FALSE:** for $\log q<2T\le\log q+\theta$, with $\theta=\mathrm{dist}(\log q,(\log p)\mathbb Z)>0$, the two-prime form has frame gap $\mu(T)\ge\min\bigl(\tfrac{\log q}{2N},(2-\sqrt3)\log p\bigr)>0$ (complete proof by double periodization; for $p=2,q=3$: frame on $\log3<2T\le\log4$). The error of Doc 148 was a category error: near-collisions degrade synthesis (Riesz), but the frame functional is **monotonic when points are added** — duplicates improve it. GAP-135.A reopens with the likely answer reversed (frame throughout THE WHOLE intermediate region, via quasi-invariance by $\theta$: GAP-151.A) and with the correct Diophantine quantity ($\theta$ and the three-distances of $L_q/L_p$, not the irrationality measure).
2. **Doc 145 decides less than its headline claims but its core is solid:** "not spectral" = "not spectral-**positive**" (the EF-spectrality of Def. 4.1 — the literal question of GAP-142.B — remains open: GAP-151.B, with the new observation that the trivial zeros are not even an admissible divisor because of unbounded real parts); proof (B) of Thm 3.4 is not complete ("two independent proofs" is false); branch (1) of the trilemma is closed by reading stipulation, not by a theorem. None of this topples the verdict: proof (A) + Doc 142 Thm. B suffice.
3. **[PROP. R.2] The collapse of H⁺, repaired and reinforced:** the emptiness of the semilocal-finite class of H⁺ holds for **every** datum $a\ge0$ (not only $a=\Lambda\mathbf 1_S$), via a new lemma with its own value — **spectral Ramanujan**: spectrality with a divisor on the line forces $a(p^m)\le C\,p^{m/2}$ (the Ramanujan bound emerges from spectrality, it is not assumed) — plus the $\eta\ge0$ strengthening of Theorem B. What remains is the honest statement: H⁺ has no finite-Euler instances; every instance requires infinite support; the semilocal rung does not exist; and H⁺ as a conjecture was ill-posed (trivially true under the spectral-positive reading, undecided under the EF one).

---

## References

**Internal (backward-only):** Doc 145; Doc 148; Doc 142 (Theorems A/B, Lemmas 2.1–2.4, §7–§8); Doc 135 (Thm. 3.1, §5: Lemma 5.1, Thm. 5.2/5.4, Prop. 5.6, Obs. 5.7, Lemma 1.7; §6 toy normalization; §7.2 B1–B4); Doc 131 (Def. 4.1, Thm. 4.4, Lemma 4.3, Def. 6.1, Prop. 6.2, Thm. 6.3, Thm. 6.6, Prop. 6.6′, Thm. 6.7, Desideratum 6.9, §7.1); P48 `06-papers/P48-weil-positivity-finite-primes/main.tex` (Conjecture 7.1, breakpoints B1–B2).

**Literature [DATUM]:**
- S. Bochner, *Lectures on Fourier Integrals*, Annals of Math. Studies 42, Princeton, 1959. (Functionals of positive type and spectral measures.)
- M. Reed, B. Simon, *Methods of Modern Mathematical Physics II*, Academic Press, 1975, Thm IX.9. (Bochner–Schwartz.)
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Lund (1952), 252–265.
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers I*, Rend. Mat. Acc. Lincei (9) 11 (2000), 183–233.
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS, 2004, Thm 5.12. (Explicit formula, archimedean weight.)
- E. T. Whittaker, G. N. Watson, *A Course of Modern Analysis*, 4th ed., CUP, 1927, §12.3. (Gauss's digamma.)
- H. J. Landau, *Necessary density conditions for sampling and interpolation of certain entire functions*, Acta Math. 117 (1967), 37–52.
- A. Beurling, *Collected Works*, vol. 2, Birkhäuser, 1989. (Balayage; density.)
- K. Seip, *Interpolation and Sampling in Spaces of Analytic Functions*, AMS Univ. Lect. Ser. 33, 2004.
- R. M. Young, *An Introduction to Nonharmonic Fourier Series*, rev. ed., Academic Press, 2001. (Necessary separation for Riesz; Bessel.)
- R. P. Boas, *Entire Functions*, Academic Press, 1954. (Jensen; density-based completeness.)
- J. Kaczorowski, A. Perelli, *On the structure of the Selberg class, I: $0\le d\le1$*, Acta Math. 182 (1999), 207–241. (Cited ONLY as a non-pluggable analogy in §2.4.)
- V. T. Sós, S. Świerczkowski (1957–58): three-distance theorem. (Cited as the natural apparatus for GAP-151.A.)
- [literature GAP] A. Kohlenberg, *Exact interpolation of band-limited functions*, J. Appl. Phys. 24 (1953): non-uniform periodic sampling, commensurable case; I know of no incommensurable version of Theorem R.1 in the literature — it could be folklore.

*End of Document 151.*

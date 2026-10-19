# Document 194 — Adversarial audit of D189, D190 and D192

**Program:** Riemann Hypothesis — Phase 59 (full closure)
**Mandate:** adversarial audit with destructive intent on three closure documents of Phase 58: D189 (R2 slit / boundary flux — whose [Thm 189.2] is ALREADY in paper P49, section `sec:flux`, which makes its correctness editorially load-bearing), D190 (non-collapsibility criterion) and D192 (attack on CONJ 179.6). Method: backward-only, independent reconstruction BEFORE reading each proof, no numerics, absolute candor.

---

## 0. Executive summary of the verdict

| Piece | Verdict | Note |
|---|---|---|
| [LEMMA 189.1] deterministic kernel | **CERTIFIED** (with observation O-194.1: the statement is improvable — $\chi'/\chi$ is REAL on the line, not just its real part) | in P49: correct as is |
| [THM 189.2] flux = LP-134 coin | **CERTIFIED** — dual route reconstructed term by term, same constant $\pi$, error $O(\log^2T)$ correct and not improvable by the method | in P49: correct as is |
| [LEMMA 189.2.a] | CERTIFIED (correct citation of 180.4.b) | — |
| [PROP 189.3] unconditional bound | **CERTIFIED-WITH-ERRATUM** (E-194.2: the intermediate arithmetic of the dyadic sum is badly written; the final constant $\tfrac14$ is correct) | — |
| [PROP 189.4] sealing of R2 | **DOWNGRADED to [BRIDGE 189.4]** — (i),(ii),(iv) are theorems; (iii) is a scheme over "the existing machineries," not a proof. R2 remains "sealed in essence, schematic in the reabsorption" | the paper does NOT state it as a theorem; no impact |
| [PROP 190.2] trichotomy | **DOWNGRADED to finite verification + unproven closure clause** — the 6 individual verdicts CERTIFIED against the cited documents; the "Prop" is a classification-by-inspection, valid and modest; the closure clause under combinations is rhetorical (E-194.4) | the paper already presents it with the correct scope |
| [DEF 190.1] | condition (c) is INFORMAL ⟹ D190 is a **FRAMEWORK** (valuable), not a theorem | — |
| [E-192.1] quantifier | **CERTIFIED** — the logic is correct; literal 179.6 IS full LP-134 | — |
| [LEMMA 192.3]+[COR 192.4] | **CERTIFIED** (constant 17 verified; observation O-194.5: the mirrors at $-\gamma$ are not mentioned, harmless) | — |
| [Test 192.2] D–H | **CERTIFIED-WITH-DEBT** (E-194.6: Prop. 150.2, which supports it, exists and says what is claimed, but D150 was never re-audited by a third party; low-risk debt, input = textbook) | — |
| D192 global | survives; no statement refuted | — |

**No result refuted.** Two status downgrades (189.4, 190.2), both partially self-declared by the documents themselves; the impact on P49 is **null in the statements and minor in one sentence of the abstract** (§5).

---

## 1. D189 — attack on [LEMMA 189.1]

### 1.1. Independent reconstruction (done before rereading the proof)

$\zeta(s)=\chi(s)\zeta(1-s)$ ⟹ $\tfrac{\zeta'}\zeta(s)=\tfrac{\chi'}\chi(s)-\tfrac{\zeta'}\zeta(1-s)$. At $s=\tfrac12+it$: $1-s=\bar s$, and by Schwarz reflection ($\zeta$ real on $(1,\infty)$, real coefficients; the identity $\zeta(\bar s)=\overline{\zeta(s)}$ holds as an identity of meromorphic functions over all of $\mathbb C$, poles and zeros included — zeros go to conjugate zeros, poles to poles, and the logarithmic derivative inherits it outside the discrete set of singularities). Hence $\tfrac{\zeta'}\zeta(\tfrac12-it)=\overline{\tfrac{\zeta'}\zeta(\tfrac12+it)}$ and
$$2\,\mathrm{Re}\,\tfrac{\zeta'}\zeta(\tfrac12+it)\;=\;\tfrac{\chi'}\chi(\tfrac12+it).$$

**The point the mandate orders to attack: is $\chi'/\chi(\tfrac12+it)$ real?** The document writes "$=\mathrm{Re}\,\tfrac{\chi'}\chi$," which would be suspicious if the (real) left-hand side were equated to a complex number. Independent verification: from $\chi(s)\chi(1-s)=1$ it follows that $\tfrac{\chi'}\chi(s)=\tfrac{\chi'}\chi(1-s)$ (differentiating $\log\chi(s)+\log\chi(1-s)=0$). At $s=\tfrac12+it$: $\tfrac{\chi'}\chi(\tfrac12+it)=\tfrac{\chi'}\chi(\tfrac12-it)=\overline{\tfrac{\chi'}\chi(\tfrac12+it)}$ (Schwarz: $\chi$ is real on the real axis, a product of real-on-real functions). **Conclusion: $\chi'/\chi(\tfrac12+it)\in\mathbb R$ identically.** The document's identity is therefore CORRECT and inserting "Re" on the right-hand side is redundant but not erroneous: the chain $2\mathrm{Re}(\zeta'/\zeta)=\chi'/\chi=\mathrm{Re}(\chi'/\chi)$ closes exactly. Internal consistency is moreover forced by the equation itself: the left-hand side is real, so the right-hand side must be, and it is for the structural reason above — no miracle, no sign erratum.

**[O-194.1] (observation, not an erratum).** Lemma 189.1 and P49's `lem:kernel` should record the reality of $\chi'/\chi$ on the line as part of the statement or the proof: as they stand, a scrupulous reader could object that equating a real number to $\tfrac{\chi'}\chi$ without comment is an apparent non sequitur. It is one line of text; the mathematics is correct.

### 1.2. Stirling, sign and direction of the normal

$\chi(s)=2^s\pi^{s-1}\sin(\tfrac{\pi s}2)\Gamma(1-s)$; the classical asymptotic (Titchmarsh §4.12) gives $\tfrac{\chi'}\chi(\tfrac12+it)=-\log\tfrac t{2\pi}+O(t^{-2})$, $t\ge1$ — verified against the standard form $\chi(\tfrac12+it)=(t/2\pi)^{-it+\ldots}e^{i(\ldots)}$, whose logarithm differentiated in $t$ produces exactly $-\log(t/2\pi)$ to error $O(t^{-2})$. Hence
$$\partial_\sigma u(\tfrac12+it)=\mathrm{Re}\,\tfrac{\zeta'}\zeta(\tfrac12+it)=-\tfrac12\log\tfrac t{2\pi}+O(t^{-2})\;<\;0\quad(t>2\pi e),$$
with $\partial_\sigma u=\mathrm{Re}(\zeta'/\zeta)$ by $u=\mathrm{Re}\log\zeta$ and $\partial_\sigma\mathrm{Re}\,f=\mathrm{Re}\,f'$ (Cauchy–Riemann). The sign is the one the document asserts. The normal: $R_T\subset\{\sigma>\tfrac12\}$, the OUTWARD normal at $\sigma=\tfrac12$ points toward decreasing $\sigma$, $\partial_n=-\partial_\sigma$, hence $\mathcal F_{1/2}=-\int u\,\partial_\sigma u\,dt=+\tfrac12\int\omega(t)\,u\,dt+O(1)$ with $\omega=\log\tfrac t{2\pi}$. **Consistent across the statement, the proof, and the use in §2; and consistent with the expected positivity** (an off quadruple adds positive mass to $u$ on the line, and the weight is positive for $t>2\pi$ — the flux must come out positive, and 189.2 confirms it with $\sum b\log(\gamma/2\pi)\ge0$). The term $O(t^{-2})\cdot u$: integrable because the singularities of $u$ are logarithmic (locally integrable) and $\int_1^\infty t^{-2}|u|\,dt<\infty$ by the Selberg mean bound on dyadic blocks. Correct.

**Cross-check of the "twin":** the document's partial-fraction computation ($\mathrm{Re}[\tfrac1{-b+i\tau}+\tfrac1{b+i\tau}]=\tfrac{-b}{b^2+\tau^2}+\tfrac{b}{b^2+\tau^2}=0$) is correct algebra; its correct status is the one the document gives it (sanity heuristic; the global proof is the functional equation, which sidesteps the conditional convergence of $\sum_\rho$). Well handled.

**[LEMMA 189.1]: CERTIFIED** (with O-194.1). For P49: Lemma `lem:kernel` can be published as is; the line on the reality of $\chi'/\chi$ is recommended.

## 2. D189 — attack on [THM 189.2] (the paper's load-bearing piece)

### 2.1. Route (a): Abel over Littlewood — full reconstruction

Input: $L(t)=\int_0^t u=2\pi\tilde J(t)+\varepsilon(t)$, $|\varepsilon|\ll\log(t+2)$ — this is Littlewood's lemma at $\sigma_0=\tfrac12$ with error $O(\log T)$, identical to the certified [180.4.b] in D188; the citation is legitimate and the normalization (one term per quadruple, only $\beta>\tfrac12,\gamma>0$) is the program's standard. Integration by parts with $\omega'(t)=1/t$, cut at $2\pi$ (where $\omega$ changes sign; the segment $[0,2\pi e]$ is $O(1)$ because $\int_0^{2\pi e}|u|<\infty$):
$$\int\omega\,dL=\omega(T)L(T)-\int_{2\pi}^T\frac{L(t)}t dt+O(1).$$
Error budget, attacked as the mandate orders: $|\omega(T)\varepsilon(T)|\ll\log^2T$ and $\int_{2\pi}^T\frac{|\varepsilon(t)|}t dt\ll\int_{2\pi}^T\frac{\log t}t dt\ll\log^2T$. **Could it be $O(\log T\log\log T)$?** Not with this method: Littlewood's error is a genuine $O(\log T)$ at EACH height (it comes from $\log|\zeta|$ on the horizontal sides of Littlewood's rectangle, unconditional size $\log t$), and integrating it against $dt/t$ up to $T$ makes the extra $\log T$ factor unavoidable. The $O(\log^2T)$ in the statement is correct and candid; any improvement would require improving the error term of Littlewood's lemma itself, which is not the business of this document. For the paper: the implicit constant is effective if Littlewood's is (it is); no issue.

Main term: with Tonelli (everything $\ge0$),
$$\omega(T)\tilde J(T)-\int_{2\pi}^T\frac{\tilde J(t)}t dt=\sum_{\gamma\le T}b\Big[\omega(T)-\log\frac T{\max(\gamma,2\pi)}\Big]=\sum_{\gamma\le T}b\log\frac{\gamma}{2\pi},$$
using $\gamma_1\approx14>2\pi$ (true even for hypothetical off zeros: $N(t)=0$ for $t<14$, a classical unconditional fact). Multiplying by $\tfrac12$: $\mathcal F_{1/2}=\pi\sum b\log\tfrac\gamma{2\pi}+O(\log^2T)$. **The reconstruction matches the document line by line.**

### 2.2. Route (b): the twin's well — the same constant?

Independent local computation: $\int_{-\infty}^\infty\log\big(1+\tfrac{b^2}{x^2}\big)dx$; by parts, $=\big[x\log(1+\tfrac{b^2}{x^2})\big]_{-\infty}^\infty+\int\tfrac{2b^2}{x^2+b^2}dx=0+2b^2\cdot\tfrac\pi b=2\pi b$. ✓ — mass $2\pi b$, localized at $|\tau|\lesssim b$, where the weight $\tfrac12\omega(t)$ is constant to relative error $O(b/\gamma\cdot\tfrac1{\log\gamma})$ (slow variation): contribution $\tfrac12\omega(\gamma)\cdot2\pi b=\pi b\log\tfrac\gamma{2\pi}$. **Identical constant $\pi$ as route (a).** The two routes are consistent; route (b) is only a contrast heuristic (as the document declares) and (a) is the proof. The definition of $\mathcal F$ with $\partial_n=-\partial_\sigma$ is consistent in statement, proof and P49 (`thm:flux` declares the normal explicitly).

**[THM 189.2]: CERTIFIED.** This is the piece that entered the paper and SURVIVES the full audit. [COR 189.2.b] too: positivity is immediate from 189.2, and the Cauchy–Schwarz argument for "A does not control the flux" is correct (the factor $N_{\rm off}\log^2T$ is not controlled without a population — consistent with E-188.5).

## 3. D189 — [PROP 189.3] and the mandated attack on [PROP 189.4]

### 3.1. [PROP 189.3] — CERTIFIED-WITH-ERRATUM

The method (dyadic blocks + Jensen on the Hardy–Littlewood second moment) is correct and the conclusion $\mathcal F_{1/2}\le(\tfrac14+o(1))T\log T\log\log T$ checks out: block $k$: $\int u\le\tfrac{T_k}4\log\log T_k+O(T_k)$ (Jensen with concavity, correct); weight $\le\tfrac12\log T_k$ (the $\tfrac12$ prefactor of $\mathcal F$); $\sum_k T_k\log T_k=(2+o(1))T\log T$ after truncating at $k\le\log\log T$; total $\tfrac12\cdot\tfrac14\cdot2\cdot T\log T\log\log T=(\tfrac14+o(1))T\log T\log\log T$. ✓

**[E-194.2] (drafting erratum, not a result erratum).** The line "Summing $\sum_k\log T_k\cdot[\ldots]\le(\tfrac12+o(1))\cdot\tfrac T4\cdot\log T\log\log T\cdot2$" is badly written: as it appears, it omits the $\tfrac12$ prefactor of the weight and the grouping of factors is unintelligible (the final "$\cdot2$" and the initial "$(\tfrac12+o(1))$" do not correspond to identifiable steps). The correct computation is the one in the previous paragraph and gives the same constant $\tfrac14$. Fix the line; the statement stands.

The comparison with classical Littlewood (the same method with $\omega\equiv1$ gives $J\le(\tfrac1{4\pi}+o(1))T\log\log T$, and Abel on it gives $\sum b\log\gamma\ll T\log T\log\log T$) is correct: the bound is indeed NOT new. The discussion in §3 ("the weight cannot buy anything") is correct as an argument FOR deterministic slowly-varying weights; see 3.2.

### 3.2. [PROP 189.4] — the sealing: proof or scheme? DOWNGRADED

Mandate fulfilled with a partially negative answer. Dissection of the four clauses:

- (i) = [Lemma 189.1]: theorem. (ii) = [Thm 189.2]: theorem. (iv) = [Prop 189.3]: theorem.
- **(iii) — "every unconditional upper bound by the existing machineries factors, via dyadic decomposition of the deterministic weight, into Littlewood's problem" — is NOT a proof.** It is a classification of methods. The argument in §3 rigorously proves: *for every deterministic, slowly-varying weight $W>0$, $\int Wu\,dt$ decomposes dyadically into copies of Littlewood*. That is a correct lemma about a formal class of functionals. But "the existing machineries" is NOT a mathematical class: the document itself admits this twice — in the §6 table ("formal class in (iii), informal in the moral — same status as barrier #3") and in [GAP-189.1] ("a randomly-correlated weight formally escapes [PROP 189.4.iii]"). A proposition one of whose clauses has a formal exception acknowledged in the same document is not a proposition: it is a bridge with three theorem-pillars and an inspection deck.

**Verdict: [PROP 189.4] DOWNGRADED to [BRIDGE 189.4].** Correct phrasing of the state of R2: *"R2 sealed in its essentials — the channel is first-order with deterministic kernel [theorems 189.1/189.2], its natural bound is Littlewood reparametrized [theorem 189.3] —, schematic in the universal reabsorption: clause (iii) covers the class of deterministic, slowly-varying weights and formally leaves GAP-189.1 open (ζ-correlated weights), with low priority because every examined candidate re-enters."* This does NOT reopen R2 as a route to $E(T)$ (the flux content is first-order — that IS a theorem, 189.2 — and $E$ is second-order), but the sentence "the reabsorption mechanism is proved, not asserted" from D189 §7's verdict is too strong: proved for the formal class, asserted for the rest. **[E-194.3]:** correct that sentence in D189 §7 and check the twin sentence in P49 (§6 below).

The attribution to 141.B2 ("escapes the premise, not the moral") and the document's final taxonomy of the wall (§5) are a reading, not a theorem, and are correctly presented as such.

### 3.3. D189 §4 (Green does not resolve it) — light verification

The three-piece balance uses only the already-certified E-188.x budgets and this document's results; the argument "one equation, two large unknowns, the small one already measured externally" is correct order-of-magnitude arithmetic. No objection. (Not a labeled statement; nothing to certify.)

---

## 4. D190 — the non-collapsibility criterion

### 4.1. [DEF 190.1] — condition (c) is informal: D190 is a FRAMEWORK

Reconstruction of the required standard: for "trichotomy" to be mathematical, (c) must define a class of evaluations (e.g., "functionals of the form $\sum_\rho g(\gamma)$ with $g$ in the admissible class of the explicit formula, moments $\int|\zeta M|^2$ with $M$ of length $\le T^\theta$, traces of the family $\{H_t\}$...") and (c) would be "Φ is evaluable in that class with error smaller than the signal." D190.1(c) instead says "boundable unconditionally **by known machinery**... Formally: the evaluation must not require, as input, a statement equivalent to A, to Dic, or to RH." The second half ("must not require input equivalent to the conclusion") is indeed precise and is what does the work in the class-3 verdicts. The first half ("known machinery," "comparable scale") is a historical inventory, not a definition. **Conclusion: [DEF 190.1] defines a verification program, not a closed mathematical object. D190 is a FRAMEWORK — and a good one — not a body of propositions.** This is NOT a fatal flaw: it is exactly what a "structural audit of the repertoire" can be; but the [PROP] label oversells it.

### 4.2. [PROP 190.2] — verification of the six verdicts and of the closure clause

The six verdicts of §2, checked against the cited documents (all audited in D184–D188 per the phase record):

1. **Weil Q (§2.1, exact-but-inaccessible):** correct — "to definitize ≡ κ=0 ≡ RH" is the certified verdict of Phase 53 (D164/165); the use of 141.B2 and GAP-141.G1 is consistent. ✓
2. **Balance İ=−2κ−D (§2.2, ζ-free):** correct — the law is ζ-free (certified D167), the Hadamard configuration with $0<I<\infty$ exists in the class (D174 §3.3, intact after E-186); the indistinguishability argument (two initial conditions, same laws ⟹ no class-invariant functional reads $I(0)$) is correct logic. ✓ — this is the only one of the six with a genuine impossibility PROOF, and the document flags it as such.
3. **D152 impurity (§2.3, averaged):** correct — D172 (collapse over E, Poisson blindness) and ceiling 172.9 certified in the Phase 54 record; the reading "satisfies (b) averaged up to Selberg and not a single log more" is faithful. ✓
4. **Green–Littlewood 173.C (§2.4, exact-but-inaccessible):** correct — 173.C certified (D185), 180.4 with E-188.1; "exactness does not buy accessibility" is the correct reading of the bidirectionality. ✓
5. **DBN flux (§2.5):** correct — Rodgers–Tao is literature; the confinement of the pathology to the corner (D177) and the downgrade of 178.10 (D187: forward direction certified, equivalence not) are used with the correct post-audit status. ✓
6. **T_λ (§2.6):** correct in essence — D64 is the equivalence. **Quibble [O-194.4a]:** the sentence "the direction 'T_λ accessible ⟹ RH' is the content of D64" is a gloss: D64 says $T_\lambda=0\,\forall\lambda\iff$RH; inaccessibility is a reasonable inference (evaluating the exact zero/prime cancellation of D72 IS deciding the bit), not a literal citation. Harmless.

**The closure clause — [E-194.4], the real weak point.** The "proof" of coverage of $\mathfrak A^*$ ends: "closure under the program's operations: combining objects from class 1 with each other stays in class 1 (invariance is preserved); combining with averaged evaluations inherits class 2; inserting the exact datum falls into class 3." The first claim is correct (class invariance is preserved under any functional combination). The second and third are NOT proved and are not obvious: "the program's operations" are not listed, and the inheritance of class 2 under combination with class-1 objects (does an averaged functional MODULATED by a ζ-free law still lose μ₂?) is plausible but is exactly the kind of claim this very phase demands be proved or labeled. **The trichotomy is therefore: finite verification of 6 candidates (solid) + partial closure proved (class 1) + asserted closure (classes 2–3).**

**Does the document respect its "not universal" disclaimer in every sentence?** Audited sentence by sentence: §0.3 ✓ (bold), §3 ✓ (SCOPE paragraph, exemplary); §4 "Binary answer... incomplete for RH" — bounded in the same sentence by "(Prop 190.2, declared scope)" ✓; §4 "the two towers are two PROJECTIONS of the same deficit" — presented as "strategic implication," and the §6 table labels it "Reading of Prop 190.2," not a theorem ✓. One minor slip: §3 "what is proved is that the three mechanisms of the repertoire exhaust the *known* mechanisms" — "proved" is excessive for an exhaustiveness (Phase 49) that was itself a taxonomy; it should say "argued." **[O-194.4b]**, minor.

**D190 verdict:** [DEF 190.1] = program definition (formal part: the anti-circularity clause; informal part: "known machinery"). **[PROP 190.2] DOWNGRADED from proposition to "verified classification of the repertoire": the six cases certified, class-1 closure proved, classes-2/3 closure asserted.** The content survives IN FULL with the candid label; D190 as a document is a high-quality FRAMEWORK whose value (GAP-190.A with a three-property contract, the reading of the two towers as projections) does not depend on the [PROP] label. Paper P49 — abstract checked — already presents it with the correct scope ("every functional in the repertoire we examine... This trichotomy is a no-go over the examined repertoire only"): **no editorial impact**.

---

## 5. D192 — conjecture 179.6

### 5.1. [E-192.1] — quantifier logic, redone from scratch

Let $S=\{(b_j,\gamma_j)\}$ be the (countable, $\gamma$-ordered) set of off quadruples of a member of the category, and $x_j=b_j\log\gamma_j$.

- **Literal 179.6:** "there is no infinite sequence of quadruples with $x\to0$." Every infinite subfamily of $S$ is such a sequence; hence the literal statement ⟺ no infinite subset of $\{x_j\}$ converges to 0 ⟺ $\liminf_j x_j>0$ (if the liminf were 0, extracting the minimizing subsequence gives the forbidden object; the converse is immediate; the case of finite $S$: liminf $=+\infty$ by convention 141.1, both forms vacuous). **= full LP-134.** ✓
- **LP-134∞ (Def 179.1):** $\exists c>0$ with $x_j\ge c$ for infinitely many $j$ ⟺ $\neg(x_j\to0$ over the ENTIRE sequence$)$. ✓ (correct negation of convergence for infinite sequences).
- **Separation:** the configuration with $x_{2^k}=1$ and $x_j=1/j$ elsewhere satisfies LP-134∞ (infinitely many $\ge1$) and violates the literal statement (the subsequence $j\ne2^k$ tends to 0). ✓ The document's counterexample is correct.

**[E-192.1]: CERTIFIED.** The correction is real, the strong/∞ distinction is well drawn, and the verification that [Cor 178.11] already used the ∞ form (D187 §1.11) is consistent with the phase record. Tower 2's architecture is not damaged.

### 5.2. [LEMMA 192.3] and [COR 192.4] — the computations

Identity: $\tfrac1{w-b}+\tfrac1{w+b}-\tfrac2w=\tfrac{2w}{w^2-b^2}-\tfrac2w=\tfrac{2[w^2-(w^2-b^2)]}{w(w^2-b^2)}=\tfrac{2b^2}{w(w^2-b^2)}$. ✓
Bound: $\mathrm{Re}\,s\ge1\Rightarrow\mathrm{Re}\,w\ge\tfrac12\Rightarrow|w|\ge\tfrac12$; $|w^2-b^2|\ge|w|^2-b^2\ge\tfrac14-\tfrac1{100}=0.24$ for $b\le\tfrac1{10}$; $|\Delta|\le\tfrac{2b^2}{0.5\cdot0.24}=\tfrac{2b^2}{0.12}\approx16.7\,b^2\le17b^2$. ✓ **The constant 17 is correct** (and candidly generous).

**[O-194.5] (observation):** the quadruple also has the mirrors at $-\gamma_j$; its discriminant with respect to the double conjugate satisfies the same bound with $w'=s-(\tfrac12-i\gamma_j)$, $|w'|\ge\tfrac12$ — the lemma holds for the full quadruple with constant $34$, or, keeping $17$, "per pair." The document compares only the upper pair; for the use (order of magnitude of the signal) this is irrelevant. Note, not correct.

Signal/noise: signal $\asymp b_j^2=\varepsilon_j^2/(\log\gamma_j)^2$; noise: $-\tfrac{\zeta'}\zeta(1+i\gamma)\ll\log\gamma$ (classical, via $\sum_\rho$ with RvM density — correct); Mertens gives error $O(1)$ for a finite sum. Ratio $\varepsilon_j^2/(\log\gamma_j)^3\to0$. ✓ [COR 192.4] follows. The identification "it is GAP-179.A on a worse chart (without the resonant factor $(\log\gamma)^2$)" is correct exponent arithmetic: on the line the resonant signal is $(b L)^2=\varepsilon^2$; on the half-plane it is $b^2=\varepsilon^2/L^2$. ✓ **CERTIFIED.**

Routes (b) and (c) (§2.2–2.3) contain no new proved statements except [MINIMAL STATEMENT 192.5], correctly labeled GAP with both halves acknowledged as unknown (and the second collapsing into GAP-179.B). The pointing-out that 179.6 should be stated in the Hermitian/$a\ge0$ subcategory (a lesson from F_{p,α}) is a legitimate hypothesis correction that D179 should inherit. No objection.

### 5.3. The use of D150 — verified at the source

Read `phase-48-audit-and-purity/150-adversarial-audit-of-docs-144-and-146.md`:
- **Prop. 150.2 EXISTS** (§4.3) and says exactly what D192 attributes to it: $\gg_\varepsilon T$ zeros of D–H with $b\asymp\varepsilon$ for each fixed $\varepsilon$, hence $\liminf\delta_\rho=0$; proof by joint Voronin universality (two inequivalent Dirichlet L-functions) + Rouché; D150 cites the textbook character of the input (Karatsuba–Voronin 1992, Steuding LNM 1877) and correctly records that the case $\varepsilon=\varepsilon(T)\to0$ (log scale) remains OPEN — exactly the reservation D192 §1.3 inherits and declares. ✓
- **Audit status [E-194.6]:** D150 is itself an audit document (it refuted the "FAT" verdict of D146), but **was never re-audited by a third party** — the D184–188 rounds covered Phases 55–57, not Phase 48. D192's D–H test conclusion inherits that debt. Risk rating: LOW — the proof of 150.2 depends on a published textbook theorem plus Rouché, and the error D150 corrected (liminf/limsup in D146) is independent of its own construction; but the program's contract requires flagging the debt, not absolving it. **Action: add to the audit-debt list "D150/Prop 150.2 (supports test 192.2 and the refuting half of GAP-141.DH)."**
- The finding "D–H can never refute 179.6∞" is correct logic: the fat zeros of [DH36] ($\beta>1$, hence $x_j\ge\tfrac12\log\gamma_j\to\infty$) are infinite and unconditional, hence D–H's ENTIRE sequence never converges to 0. ✓ The candid reading that this makes the minimal form LESS falsifiable is correct and is the document's best finding.

**D192 verdict: CERTIFIED in all its labeled pieces**, with debt E-194.6 hanging over test 192.2 and observation O-194.5. The document's own verdict ("neither proved nor refuted; calibrated-conditional; reduced to the same wall") is exact and inflates nothing.

---

## 6. Impact on paper P49

Verified against `06-papers/P49-two-towers-architecture/main.tex` (abstract, `sec:flux`, `lem:kernel`, `thm:flux`):

1. **[Thm 189.2 / `thm:flux`] and [Lemma 189.1 / `lem:kernel`]: NO CHANGE NEEDED.** Both certified; identity, constant $\pi$, error $O(\log^2T)$, normal convention ("outward normal $-\partial_\sigma$," declared in the statement) — all correct. Optional recommendation (O-194.1): a line recording that $\chi'/\chi$ is real on the line (from $\chi(s)\chi(1-s)=1$ + Schwarz), to shield the real=real equality from the referee. The abstract cites the identity "$2\Re(\zeta'/\zeta)=\Re(\chi'/\chi)$" — correct as is.
2. **Barriers section:** verify that the reabsorption of the flux (the counterpart of [PROP 189.4]) is phrased as in the current abstract ("the boundary kernel is deterministic" — descriptive, not "universally proved"): the abstract passes the audit; if the body of `sec:flux`/`sec:barriers` contains the phrase "the reabsorption mechanism is proved" or its English equivalent, replace it with the E-194.3 formula ("proved for deterministic slowly-varying weights; formally open for ζ-correlated weights, all examined candidates re-enter"). **Only editorial touch-up required, and it is one sentence.**
3. **Trichotomy:** the abstract already says "every functional in the repertoire we examine" + "no-go over the examined repertoire only, not a universal impossibility" — consistent with the §4.2 downgrade; no changes.
4. None of D192 is in P49; no impact.

## 7. Final table of errata and observations

| Item | Type | Content | Action |
|---|---|---|---|
| O-194.1 | observation | $\chi'/\chi(\tfrac12+it)$ is real (from $\chi(s)\chi(1-s)=1$); record it in 189.1 and `lem:kernel` | 1 line, optional but recommended |
| E-194.2 | drafting erratum | intermediate arithmetic of [PROP 189.3] badly written; final constant $\tfrac14$ correct | rewrite the dyadic-sum line |
| E-194.3 | downgrade | [PROP 189.4]→[BRIDGE 189.4]: (iii) proved only for deterministic slowly-varying weights; "mechanism proved, not asserted" (D189 §7) is excessive | correct D189 §7; review the twin sentence in P49 (§6.2) |
| E-194.4 | downgrade | [PROP 190.2]→verified classification: classes 2–3 closure asserted, not proved; "exhaust... proved" (§3)→"argued" | re-label; content intact |
| O-194.4a/b | minor observations | gloss on D64 in §2.6; "proved" instead of "argued" in D190 §3 | cosmetic |
| O-194.5 | observation | Lemma 192.3 covers the upper pair; the full quadruple doubles the constant (≤34) or is stated "per pair" | note |
| E-194.6 | audit debt | Prop 150.2 (D150) supports test 192.2 and was never re-audited; low risk (textbook input) | add to the debt list; audit D150 if the D–H test scales to publication |

## 8. Global verdict

**No theorem refuted in the three documents** — the first round of the phase with that result in central pieces, consistent with D189/D192 building on already-audited material (D188/D187) and D190 being a taxonomy. What falls is STATUS, not content: two [PROP]s (189.4, 190.2) were bridges/classifications with a proposition label — the reverse of the program's historical pattern (before: false proofs with true statements; here: self-declared partial proofs with a one-grade-inflated label). The core P49 needs — [Lemma 189.1], [Thm 189.2] — is CERTIFIED with no mathematical reservations; the paper requires exactly a one-sentence touch-up (E-194.3) and an optional line (O-194.1). D192's new pieces (E-192.1, 192.3/192.4) are certified; their only debt is inherited (E-194.6, D150).

**Internal documents cited:** D64, D131, D141, D146, D150 (read at source, §4.3), D152, D164–167, D170–174, D176–181, D183, D184–188, D189–190, D192; P49 `main.tex` (read: abstract, `sec:flux`).

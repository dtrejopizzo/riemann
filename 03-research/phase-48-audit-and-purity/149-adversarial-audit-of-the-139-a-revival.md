# Doc 149 — Adversarial audit of the 139.A revival: Doc 147 does NOT revive the theorem

**Program:** Riemann Hypothesis — Phase 48, "audit and purity"
**Mandate:** destroy or certify the repair of Doc 147 (exponential dominance for the ¬RH branch of the logistic criterion, Problem 139.A). Object audited: Doc 147 in full ([Lemma 2.1], [Prop. 3.1], `hyp:band` Def. 4.1, [Thm. 4.2], the anti-false-victory verification §5, and the §6.2 claim of unconditionality with real-center axis).
**Inputs (read in full, citations only backward):** D147; D139 (GAP-A, Lemma 139.1, GAP-B, §4.4, Problem 139.A); D136 (Def. 3.1–3.2, Lemmas 5.2–5.3, Theorems 4.1–4.4, 5.4, spectral side (1.1)–(1.2)); D107/D108 via D136's citations. Nothing is fabricated; every claim of error comes with the computation in closed form.

---

## 0. Verdict per piece, one line each

| Piece | Verdict |
|---|---|
| **[Lemma 2.1]** (exponential-vs-polynomial dominance) | **SURVIVES-WITH-ERRATUM** — the lower bound (2.4) is genuine only after repairing the gap of the Fourier transform's zeros with the modulation (which the doc relegates to a parenthesis and which clashes with the evenness of §3.4); the constants also depend on γ₀, not "only on Φ and δ₀". The lemma controls **moduli**; it contains and can contain no **sign** information — and everything that follows needs sign. |
| **[Prop. 3.1]** (witness without a divergent constant) | **DIES** in three exact steps: (i) equation (3.4) contains a **conjugation error** — evenness gives ĝ(σ₀′) = conj(ĝ(σ₀)), so the target term is Re[ĝ(σ₀)²] (sign oscillating with a₀), not |ĝ(σ₀)|²; (ii) mechanism (†) uses an **unsigned upper bound** (mean-value) as a **signed** main term — the "discrepancy against the autonomous term" is a category error: neg.ind requires Q₂(v,v) < 0, and in Q₂ there is no term "what it would be worth if ρ⁰ were on-line"; (iii) the budget (3.6) tacitly assumes that ρ⁰'s quadruple **exhausts** the off zeros ("4 off zeros" in the proof): a toy presented as general. The statement is plausibly true **under finite defect** with a different proof (§5.4 below); under general ¬RH it is open. |
| **[Thm. 4.2] (¬RH branch under `hyp:band`)** | **DIES**, regardless of `hyp:band`: it inherits the corpse of Prop. 3.1; the transplant of the two-hump witness to the cell's span {B·σᵃ} is asserted, not derived ((3.6) is never re-derived for the cell); and the cell's tail **at fixed M** (the doc fixes M ≥ D+4) is not poly(a₀) under general ¬RH: it carries band factors e^{βa₀} from unknown off zeros — closing it requires M growing with a₀, and then Lemma 139.1 **literally reopens GAP-A**. Moreover it **OVER-CLAIMS**: stated for general ¬RH, provable (after repairs) at most under "finite defect + β* attained". |
| **`hyp:band` as a hypothesis** | **SURVIVES** (the only piece that fares better than the mandate feared) — after correcting a quantifier slip (literal (4.1), with free c, contradicts (∗)'s own decay): there is no Lemma 139.1-bis for pointwise lower bounds in a real direction with definite-sign mass; it is satisfiable and indeed provable for explicit families (§3.3). But `hyp:band` only gives **modulus**, and the ¬RH branch dies from **phase/sign**: the hypothesis survives, the implication "`hyp:band` ⟹ ¬RH branch" does not. |
| **§5 (anti-false-victory, b₀ = O(1), zero of maximal real part)** | **OVER-CLAIMS** — the Vandermonde conditioning analysis is correct within its scope, but "verified" is false: it presupposes that β* = sup{β} is **attained** (not guaranteed under general ¬RH: an accumulation scenario β_n ↗ β*, consistent with the density theorems), contradicts Prop. 3.1 (which uses the zero of **minimal height**), and touches neither the sign nor the equal-rate pairs. |
| **§6.2 (real-center axis ⟹ both branches unconditional)** | **DIES** at step (b) of the protocol — a *pars pro toto* fallacy: re-centering the bump at ½+δ₀ makes the **numerator** trivial (|B(0)| = 1) and moves all the content to the **denominator** (the bump's values on the line Re = ½, where the sea lives): the load-bearing quantity is the off/on **ratio**, and after re-centering the ratio requires an exponentially small **upper** bound on the critical line — the same directional asymmetry of `hyp:band` in different clothes, not an identity. Parts (a) test-accessibility and (c) preservation of the RH branch and canonicity **survive** (§4.3): the axis is a harmless and even advisable enlargement — but it trivializes nothing. |
| **Status of 139.A** | **STILL OPEN.** Doc 147's "CLOSED-PARTIAL" is not sustainable; P47's abstract stands as D139 left it. |

---

## 1. Protocol 1: re-derivation of [Lemma 2.1] and the Fourier-lower-bound issue

### 1.1. The derivation, from scratch

With the critical-band representation (D147 (2.1), = `rem:theta` of P47):
$$\hat f(s)=\int_{-a_0}^{a_0}F(u)\,e^{(s-\frac12)u}\,du,\qquad F=a_0^{-1/2}\,\Phi(\cdot-a_0/2),\ \Phi\in C_c^\infty([-1,1]).$$
At ρ⁰ = ½+δ₀+iγ₀:
$$\hat f(\rho^0)=a_0^{-1/2}\,e^{(\delta_0+i\gamma_0)a_0/2}\cdot c,\qquad
c:=\int_{-1}^{1}\Phi(t)\,e^{\delta_0 t}\,e^{i\gamma_0 t}\,dt \;=\; \widehat{\Phi e^{\delta_0\cdot}}(-\gamma_0).$$
The modulus of the exponential factor is exact: e^{δ₀a₀/2}. The whole content of the lower bound (2.4) is the claim |c| ≥ c₁ > 0.

### 1.2. Where the fine point lies and how the doc fares

The number c is the value of the Fourier transform of a C_c^∞ function at frequency γ₀. Two facts, both against the lemma's literal statement:

1. **c depends on γ₀ and decays superpolynomially in γ₀** (Paley–Wiener for Φe^{δ₀·} ∈ C_c^∞; Hörmander I, Thm. 7.3.1). The lemma's phrase "constants that depend only on Φ and δ₀" is **false**: c₁ = c₁(Φ, δ₀, γ₀). Since γ₀ is fixed by the configuration, this is not fatal — it is an erratum, but one that matters because the same phrase reappears in Prop. 3.1 ("NOT on a parameter tending to infinity": true, but the constants do depend on the whole configuration).
2. **c can vanish exactly.** $\widehat{\Phi e^{\delta_0\cdot}}$ is entire of exponential type 1, not constant: it has infinitely many zeros (Hadamard; Boas, *Entire Functions*, Ch. 2), and nothing prevents γ₀ — which belongs to **the adversary** — from landing on one. For the flat bump Φ ≥ 0, positivity only protects the **real** point (γ = 0): ∫Φe^{δ₀t}dt > 0 without cancellation. This is exactly the phenomenon the mandate flags: lower bounds of transforms at complex points are delicate because the transform's zeros move with the test.

**The doc's repair (modulation Φ ↦ Φe^{−iγ₀t}) is correct in itself**: it moves the evaluation to the real point, c = ∫Φe^{δ₀t}dt ≥ e^{−δ₀} > 0, and the class is closed under modulation [D107]. But it is relegated to a parenthesis within the proof, **it changes the test** (the lemma as stated, with F = flat bump, is false for γ₀ in the zero set), and — decisive for §3.4 — **the complex modulation destroys the reality/evenness of F** that §3.4 needs. The compatible real-even version (humps at ±a₀/2 modulated by cos(γ₀u)) does exist and gives
$$\hat f(\sigma_0)=\tfrac12\,a_0^{-1/2}e^{(\delta_0+i\gamma_0)a_0/2}\Big[\underbrace{\textstyle\int\Phi e^{\delta_0t}dt}_{>0}+\underbrace{e^{i\gamma_0a_0}\textstyle\int\Phi e^{\delta_0t}e^{2i\gamma_0t}dt}_{\text{oscillates with }a_0}\Big]+O\big(e^{-\delta_0a_0/2}\big),$$
with lower bound |ĝ(σ₀)| ≥ c₁e^{δ₀a₀/2}a₀^{−1/2} whenever $|\widehat{\Phi e^{\delta_0\cdot}}(-2\gamma_0)|<\int\Phi e^{\delta_0t}dt$ — verifiable for large γ₀ by smoothness, adjustable for small γ₀. None of this is in the doc.

### 1.3. Verdict of protocol 1

**[Lemma 2.1] SURVIVES-WITH-ERRATUM**: (2.4) is true for the corrected test (modulation compatible with evenness), the "≥ and not just ≤" guarantee exists and comes from definite-sign mass evaluated at the real point — the only place where the Fourier lower bound is cheap. (2.5) is correct as is. **But the whole lemma lives in the world of moduli.** The off/on ratio → ∞ is true and closes nothing: what the negativity of Q₂(v,v) needs is the **sign** of a concrete term, and the sign is a phase that Lemma 2.1 does not even mention. The lemma is a sound brick used as the keystone of an arch that does not exist.

---

## 2. Protocol 2: the perturbation term (†), the conjugation in (3.4), and the hunt for the hidden constant

### 2.1. The conjugation error in (3.4) — the exact step where Prop. 3.1 dies

§3.4 takes g_v real with F **even** and claims: "ĝ_v(σ₀) = ĝ_v(σ₀′) (evenness ⟹ symmetry σ ↔ 1−σ)", and from there (3.4):
$$\hat f(\sigma_0)\,\overline{\hat f(\sigma_0')}\;\overset{\text{D147}}{=}\;|\hat f(\sigma_0)|^2.$$
Let us re-derive. Evenness of F gives the functional symmetry ĝ(1−s) = ĝ(s); reality of F gives ĝ(s̄) = conj(ĝ(s)). With σ₀ = ½+δ₀+iγ₀ and σ₀′ = 1−σ̄₀ = ½−δ₀+iγ₀:
$$\hat g(\sigma_0')=\hat g(1-\bar\sigma_0)\overset{\text{evenness}}{=}\hat g(\bar\sigma_0)\overset{\text{reality}}{=}\overline{\hat g(\sigma_0)}
\qquad\Longrightarrow\qquad
\hat g(\sigma_0)\,\overline{\hat g(\sigma_0')}=\hat g(\sigma_0)^2,$$
**a complex square, not a squared modulus**. Note that 1−σ₀ = ½−δ₀−iγ₀ ≠ σ₀′: the evenness symmetry does NOT take σ₀ to σ₀′; it does so composed with conjugation, and conjugation is applied exactly one too many times. The contribution of the orbit {P₀, ιP₀} with a real even witness is, in closed form (using §1.2):
$$2m_0^2\,\mathrm{Re}\big[\hat h(P_0)\overline{\hat h(\iota P_0)}\big]
=\tfrac{m_0^2}{2}\,\hat\varphi(0)^2\,\mathrm{Re}\big[\hat g(\sigma_0)^2\big]
=\tfrac{m_0^2}{2}\,\hat\varphi(0)^2\,a_0^{-1}e^{\delta_0a_0}\,|c_+|^2\cos\!\big(\gamma_0a_0+2\arg c_+\big)\,(1+o(1)),$$
with c₊ the constant of §1.2. **The sign oscillates with a₀** through the phase γ₀a₀. Exact consequences:

- Identity (3.4) "= |f̂(σ₀)|² ≥ c₁²a₀^{−1}e^{δ₀a₀}" is **false**.
- The doc's own next paragraph ("that product is real and positive (=|ĥ(P₀)|² ≥ 0)... seems to kill the idea") commits **the same error with the opposite conclusion**. The doc asserts, three lines apart, that essentially the same quantity is positive (+|ĥ|²) and negative (−c_W|f̂|² in the proof of Prop. 3.1). The truth is: neither — it is Re[ĥ(P₀)²], of oscillating sign. That a document holds both signs for the same term is by itself grounds for withdrawal.
- The irony: **the truth is more useful than either of the doc's claims** — an oscillating sign is selectable: there exist windows of a₀ (progressions of step 2π/γ₀) where cos < −½ and the target term is genuinely −c·a₀^{−poly}e^{δ₀a₀}. That phase adjustment (choosing a₀ modulo 2π/γ₀, legitimate: the witness may use positions, Obs. 5.1 of D136) is the real mechanism of the classical Weil criterion — and **it is nowhere in Doc 147**.

### 2.2. (†) re-derived: a mean-value bound, unsigned, and with the wrong rate

Let P(δ) := f̂(½+δ+iγ)·conj(f̂(½−δ+iγ)). Then P(0) = |f̂(½+iγ)|² and
$$P'(\delta)=\Big(\int uF\,e^{\delta u}e^{i\gamma u}du\Big)\overline{\hat f(\tfrac12-\delta+i\gamma)}
-\hat f(\tfrac12+\delta+i\gamma)\overline{\Big(\int uF\,e^{-\delta u}e^{i\gamma u}du\Big)},$$
whence, with F of humps at ±a₀/2 (‖uFe^{δu}‖₁ ≤ C a₀^{1/2}e^{δa₀/2}, |f̂(½±δ+iγ)| ≤ C a₀^{−1/2}e^{δa₀/2}):
$$\big|P(\delta_0)-P(0)\big|\;\le\;C\,\delta_0\,e^{\delta_0 a_0}. \tag{2.A}$$
Three conclusions, in order of increasing severity:

1. **Narrow verification in the doc's favor:** in (2.A) there is no C_M, no b₀(M)^{−1}, no M. In that literal sense, the claim "there is no divergent constant in M" is true. Lemma 139.1's rigidity does not bite here.
2. **The hidden constant is there, but it is not M — it is an exponential declared polynomial.** The coefficient printed in (†) is "δ a₀ e^{a₀/2}‖F‖₁ sup_band|f̂|" with the claim "‖F‖₁, sup|f̂| are O(poly(a₀))". False: the supremum over the band |Re−½| ≤ δ₀ includes Re = ½+δ₀, where |f̂| ≍ a₀^{−1/2}e^{δ₀a₀/2} — **exponential**. This is GAP-A's lesson in new clothing: in D136 it was a "constant" that was a function of M; here it is a "polynomial" that is exponential in a₀. And with the printed factor e^{a₀/2}, the total rate of the rest of (†) is (1+δ₀)/2 > δ₀ for every δ₀ < 1: **the error term of (†), read as the doc writes it, swallows the very main term e^{δ₀a₀} it is meant to extract.** With the repaired reading (2.A) the error's rate is exactly δ₀ — equal to the main term's: nothing is extracted that way either.
3. **The category error (the fatal blow):** (†) is a bound on |deviation|, unsigned. The doc uses it as follows: "the discrepancy |ĥ(ρ⁰_off)|² − |ĥ(ρ⁰_on)|² is what is negative when compared against the autonomous term... the term O(δa₀e^{a₀/2}) is the carrier of the defect's sign." But **what neg.ind(Q₂|_{V_p}) ≥ 1 needs is Q₂(v,v) < 0, period** — the real spectral sum, (1.1) of D136. The arithmetic/autonomous side **equals** the spectral side (it is the explicit formula): there is no term in the formalism for "the value ĥ would have if ρ⁰ were on-line" that gets subtracted from anything. The counterfactual comparison is not a term of the form; it is narrative. The real quantity is the one in §2.1: Re[ĝ(σ₀)²]·(...), directly computable, with oscillating sign — and the doc never computes it, because the direct computation contradicts both its "+|ĥ|²" and its "−c_W|f̂|²" at once.

### 2.3. The budget (3.6) and the omitted maximal-rate terms

Even granting the sign of the first term of (3.6), the budget is incomplete **at the same exponential rate**:

- **Pairs (z₁,z₂) of the quadruple itself** (z₁ = ½+δ₀+iγ₀, z₂ = ½−δ₀+iγ₀): σ = ½+iγ₀, τ = ±δ₀. With g, φ real even of support a₀ (the design declared in Prop. 3.1), φ̂(±δ₀) ∈ ℝ and the orbit {(z₁,z₂),(z₂,z₁)} contributes
$$\tfrac12\,|\hat g(\tfrac12+i\gamma_0)|^2\,\hat\varphi(\delta_0)^2\;\asymp\;+\,a_0^{-2}\,e^{\delta_0a_0}\;>\;0,$$
**positive, of the same rate δ₀ and the same polynomial order a₀^{−2} as the "dominant" negative term**. It does not appear in (3.6). (It is killable: either fixed support for φ — an asymmetric design the doc does not use —, or Vandermonde annihilation in τ at ±δ₀, iγ₀ — the GAP-B patch used with nodes the doc does not list.)
- **The proof of (3.6) declares "its number is finite (4 off zeros × ...)" and sums the sea only over on-line ρ**: it assumes ρ⁰'s quadruple exhausts the off zeros. Under general ¬RH there are (possibly infinitely many) additional off zeros ρ = ½+β+iγ with β up to near ½ and uncontrolled sign, living in the "tail" of (3.6) with band factors e^{βa₀} — **not poly(a₀)**. If even one off zero exists with β > δ₀ (ρ⁰ is chosen by minimal height, not maximal β!), its unsigned term e^{βa₀} defeats the main one e^{δ₀a₀}. This is the same pattern D139 documented in GAP-B: "proved in the toy, cited in general." Full detail in §5.

**Verdict of protocol 2: Prop. 3.1 DIES at (3.4) (conjugation), at mechanism (†) (unsigned bound used as a signed term; a "polynomial" that is exponential), and at (3.6) (toy budget under a general hypothesis).**

---

## 3. Protocol 3: `hyp:band`, the zeros of B̂, and whether a Lemma 139.1-bis exists

### 3.1. The precise statement and a quantifier slip

Literal (4.1) asks for |B^{(M)}_w(½+δ+ic)| ≥ c_δ e^{c′δa₀} with c unbounded. **As written it contradicts (∗) itself**: along the line Re = ½+δ, bound (∗) gives |B(½+δ+ic)| ≤ C_M e^{δa₀}(1+|c−c_center|/w)^{−M} → 0 as |c| → ∞ — no function of the class satisfies a uniform lower bound in c. The repaired reading (the only one the application uses): the lower bound is demanded **at the shifted point the cell evaluates**, ½+δ+iε with |ε| ≤ b (mesh), after choosing the center c in the mesh near γ₀. I record the correction as E-149.1 (not fatal: the application never used the ∀c).

### 3.2. Is there a Lemma 139.1-bis? No — and this is the one point where Doc 147 gains ground

Lemma 139.1's mechanism (D139) needs a **family of bounds along the whole real axis, uniform in M**: if C_M ≤ A^M for infinitely many M, B vanishes for |t| > Aw — contradicting discrete real zeros. A **pointwise lower bound at a single point in a real direction** has no such leverage: there is no M → ∞ limit to take, and the point is one. Moreover it is elementarily satisfiable:

**[COMPUTATION 149.2] (explicit family satisfying the repaired `hyp:band`).** Let G_a ≥ 0, C_c^∞, support in [−a, a], even, with mass ≥ η > 0 on [a/2−1, a/2+1] and ‖G_a‖₁ = 1, and B_a(z) := ∫G_a(u)e^{(z−½)u}du. Then:
(i) |B_a(½+ic)| ≤ ‖G_a‖₁ = 1 for all c (the second clause of (4.1), free);
(ii) B_a(½+δ) = ∫G_a e^{δu}du ≥ η·e^{δ(a/2−1)} — positive integrand, **no zero problem**: the lower bound at the real point is cheap precisely because the mass has definite sign;
(iii) for the shifted point: Re B_a(½+δ+iε) ≥ cos(εa)·η e^{δ(a/2−1)} − (bounded remainder), > 0 if |ε| ≤ π/(3a) — **the mesh must be b ≲ 1/a₀**, available in D136's dyadic grid, with increasing N₀. ∎

The zeros of B̂ — the threat the mandate asks us to track — only bite at points of **shifted ordinate** (γ₀ − c ≠ 0) or after the Vandermonde combination; the first is controlled with a 1/a₀-fine mesh or with the genericity of the center (Lemma 5.3 of D136: discrete zero set, avoidable); the second is (R2), treated in §5. **Who controls where B̂'s zeros fall relative to ρ⁰:** nobody needs to control it if the decisive evaluation is at the real point with positive mass; the adversary controls (β, γ₀), but γ₀ is neutralized by the ordinate center (an axis the grid DOES have) and β by... the band factor, which is clause (ii). Conclusion: **there is no Lemma 139.1-bis; `hyp:band` (repaired) is satisfiable, provable, and the doc's residue R1 is even over-cautious.**

### 3.3. Why this saves nothing

`hyp:band` delivers a large |ĝ(σ₀)|. The ¬RH branch needs a large **negative** term. Between modulus and sign stands the phase arg ĝ(σ₀) ≈ γ₀a₀/2 + O(1), which rotates with a₀ (§2.1) and which no modulus lower bound fixes. Doc 147's logical chain is: `hyp:band` ⟹ (2.4)-in-the-cell ⟹ (3.6) ⟹ Q₂(v,v) < 0; the link (3.6) is broken by the sign and by the omitted terms (§2), and `hyp:band` is irrelevant to both. **The hypothesis survives; the conditional theorem does not.**

There is also a second dependency the doc does not audit: the ideal-cell → grid step (Theorem 4.4 of D136) uses b ≤ μ/(4√2 L) with μ = spectral margin and L = the Gram's Lipschitz constant. In the non-normalized regime, μ ≍ e^{δ₀a₀} but L ≍ a₀·(entry size) ≍ e^{2a₀·(range)} — **both exponential in a₀**; the required mesh is b ≲ e^{−ca₀}, available but never re-quantified in D147. Erratum E-149.3: the whole mesh package must be re-derived in the exponential regime before being cited as "unchanged" (D147, proof of Thm. 4.2: "Theorem 4.4 ... unchanged" — no).

---

## 4. Protocol 4: the real-center axis (§6.2) — the unconditional claim

### 4.1. (a) Test-accessibility: SURVIVES

The extended grid sweeps c_Re ∈ ℚ∩[0,½] on a dyadic mesh: it mentions no zero positions; the cell that "finds" δ₀ exists in 𝒢_N for large N without anyone knowing β (it is the same existence argument as for ordinate centers: the maximum over the grid includes the good cell). No uniformity over the mesh is needed: one negative cell suffices. The inclusion 𝒢_N ⊆ 𝒢_{N+1} is preserved with nested meshes. ✔

### 4.2. (b) The slip |B(0)| = 1: HERE IT DIES

The load-bearing quantity of the whole mechanism is the **ratio** (D147 Lemma 2.1: "the off/on ratio grows like e^{δ₀a₀/2}"):
$$\mathcal R \;:=\; \frac{|\hat g(\sigma_0)|}{\sup_{\rho\ \mathrm{on}}|\hat g(\tfrac12+i\gamma)|}\,.$$
With the bump centered on the critical line: numerator ≍ e^{δ₀a₀} (band factor, `hyp:band`), denominator ≍ poly — exponential ratio. With the bump re-centered at ½+δ₀ (the §6.2 proposal): numerator = |B(0)| = 1 — **and the denominator is the values of B on the re-centered line Re = −δ₀, which is now where ALL the on-line sea lives**. For the ratio to remain exponential one needs
$$\sup_{y\,\in\,\text{window}}\big|B(-\delta_0+iy)\big|\;\le\;e^{-c\,\delta_0 a_0},$$
an exponentially small **upper** bound along a segment of a vertical line. This: (i) **is not the identity |B(0)| = 1** — it is a second, independent, non-trivial condition; (ii) is exactly the directional asymmetry of the Phragmén–Lindelöf indicator that `hyp:band` encoded (h_B(π) ≪ h_B(0) in the re-centered coordinate; Levin, *Lectures on Entire Functions*, Lectures 8–9), **the same hypothesis in different clothes**; (iii) has its own rigidity cost: by the three-lines theorem (Hadamard; cf. Boas §1.4), 1 = |B(0)| ≤ sup_{Re=−δ₀}|B|^{1/2}·sup_{Re=+δ₀}|B|^{1/2}, so smallness on the sea's line forces |B| ≥ e^{+cδ₀a₀} on Re = +δ₀ — the growth does not vanish, it moves to the other side, where one would again have to budget for any pairs falling there (off zeros with β > δ₀, if any: §5). The doc's "evaluated at its maximum" is not even true: B(0) = 1 is the normalization, not the maximum; the maximum of a type-a₀ bump in the real direction is at the edge of the strip.

**Conclusion (b):** "`hyp:band` becomes the trivial identity |B(0)| = 1" is a *pars pro toto* fallacy: it verifies the numerator of the ratio and forgets the denominator. The phrase "both branches are unconditional theorems" is **unsustainable**; with the real axis, the ¬RH branch remains exactly as conditional (and besides is still dead by §2, which the real axis does not touch: the sign of the target term is the same problem under any centering).

### 4.3. (c) Preservation of the RH branch, monotonicity and canonicity: SURVIVES

Re-centering in Re amounts to multiplying g by x^{c_Re} with c_Re real: C_c^∞(ℝ₊*) is closed under this, so the extended cells live in the same class and the spectral side (1.1) with absolute convergence [D107, Lemma 2.2(b)] applies to them. Under RH the sum is diagonal and Q₂ ≥ 0 over **the entire** span of the class [D108, Prop. 2.2]; every compression of a PSD operator is PSD; the fill is positive: x₀(N) ≡ 0 also with the extended axis — **the RH branch does not break**. Monotonicity: nested dyadic meshes in c_Re ⟹ 𝒢_N ⊆ 𝒢_{N+1} ⟹ Prop. 3.3(c) intact; the fill's bound x₀ ≤ ½ does not change; bug E-139.1 (radical) remains as it was. **The real-center axis is, as a design enlargement, harmless and reasonable** — it just does not prove what §6.2 says. (Additional erratum E-149.4: D136's own (3.1)/(∗) normalizes B(0) = 1 while measuring the band from Re = ½ — point 0 is at distance ½ from the band center; this normalization inconsistency is the ground where §6.2's confusion grows.)

---

## 5. Protocol 5: GAP-B revisited — the zero of maximal real part and the accumulation scenario

### 5.1. The internal contradiction

Prop. 3.1 and Thm. 4.2 are stated with ρ⁰ = the off zero of **minimal height** (inherited from D136 §1.1). §5 of the doc itself discovers that the construction needs the zero of **maximal real part** β* ("Prop. 3.1 should use ρ* = ½+β*+iγ*, not the one of minimal height") — and records this as a "refinement" without restating or re-proving anything. As written, the two labeled results use the wrong zero: with the minimal-height one, any off zero with β > δ₀ (legitimate under ¬RH) contributes an unsigned term e^{βa₀} ≫ e^{δ₀a₀} that no clause of (3.6) bounds. This alone already invalidates the statements as written.

### 5.2. Does the maximum exist? The sup may not be attained

β* := sup{β : ζ(½+β+iγ) = 0, β > 0}. Under general ¬RH the set of off zeros may be infinite (the sub-resolution scenario already flagged in D144): β_n ↗ β* with γ_n → ∞ and **sup not attained**. The doc half-concedes this ("exists finite under a ¬RH whose defect touches the band" — an undefined phrase — "under general ¬RH β* ≤ ½") and proceeds as if it were attained. Let us see what happens if not:

**[COMPUTATION 149.5] (the accumulation scenario defeats every compact-support witness with fixed-order-M cells).** Let the configuration be β_n = β* − εₙ with εₙ ↓ 0 arbitrarily fast and ordinates γ_n the minimal ones compatible with the density theorems (Ingham: N(σ,T) ≪ T^{4σ(1−σ)}log T for σ > ½, so γ_n ≫ n^{1/θ} with θ = 4β*(1−β*) < 1 — the density theorems bound the **count**, not the speed of approach εₙ, which is left free to the adversary). The witness chooses a realized zero ρ_w with β_w = β* − ε_m fixed. The zeros with β ∈ (β_w, β*) are infinite; with a cell bump of polynomial decay order M − D (M fixed, as the doc prescribes: "M stays fixed at M ≥ D+4"), the unsigned term of zero n is worth up to
$$e^{\beta_n a_0}\,\big(1+|\gamma_n-\gamma_w|/w\big)^{-(M-D)}\quad\text{against the main term}\quad e^{\beta_w a_0}\,a_0^{-\mathrm{poly}}.$$
Maximizing over n with εₙ = e^{−n}: the bad/main ratio contains e^{(ε_m−e^{−n})a₀}·γ_n^{−(M−D)}; at n ≍ log a₀ the exponential factor is ≍ e^{ε_m a₀} and the polynomial one is only (log a₀)^{−C}: **the ratio diverges**. Vandermonde annihilation does not help: the cell's degree D is bounded and the offenders are infinite; annihilating the D worst leaves the (D+1)-th, barely further away. Increasing M with a₀ to gain decay reintroduces C_M and Lemma 139.1's balance e^{2M} → ∞: **GAP-A reopened literally.** ∎

**Conclusion:** under general ¬RH, Doc 147's argument (and any repair within cells of bounded D, M) **tacitly requires** that β* be attained AND isolated (only finitely many zeros with β > β* − η for some η > 0): an "isolated fat zero". That is a structural hypothesis about the zero set that ¬RH does not imply, that no density theorem gives, and that has exactly the flavor of "m < ∞"-type hypotheses — i.e., **the circularity with LP-141 the mandate feared is there, undeclared.** §6.3's "verified in §5 with the zero of maximal real part" is false as a verification: it is a wish with a theorem's name.

### 5.3. What is actually right in §5

The conditioning analysis is correct within its scope: if the annihilation nodes have Re ≤ ½ + β_w and the prescription point is the one of maximal Re, then b₀ = min|B(nodes)| is fixed by an on-line node and does not decay with a₀, and the Lagrange constant is O(1) at separated nodes. That answers the narrow question of R2 (Vandermonde does not reintroduce the divergence **through the b₀ door**). What §5 does not touch: the sign (§2.1), the equal-rate pairs (§2.3), and the existence of the maximum (§5.2). Three doors open out of four.

### 5.4. The frank repair that remains alive (second repair, named, not executed)

For the Phase 48 record — what a Doc 15x could actually prove, and within what limits:

**Candidate statement (finite defect):** *Under ¬RH with finite defect (4m̄ off zeros), let ρ* be the off zero of maximal real part β* (it exists: finite set). Then there exists a grid cell (with or without real axis) with neg.ind ≥ 1.* Proof ingredients this audit identifies as sufficient and available: (1) prescription Vandermonde **at scale** (ĝ(σ*) = R, ĝ(σ*′) = −R with R ≍ |B(σ*)| ≍ e^{β*a₀/2}, O(1) coefficients by proven `hyp:band` and §5.3) — this fixes the **sign** mechanically, without (†) and without phase adjustment: the target term is exactly −(m₀²/2)φ̂(0)²R² < 0, as in D136 Step 2 but without normalizing to 1; (2) σ and τ annihilation of **all** pairs of rate e^{β*a₀} (finite under finite defect: off×off pairs of the off set, including the (z₁,z₂) and (z₁,z₃) of §2.3 — nodes σ = ½+mixed-β and τ ∈ {±mixed-δ, ±mixed-iγ}); (3) asymmetric support or fixed-support τ-bump so that the τ coordinate does not manufacture exponentials; (4) tail budget with the remaining off zeros at rate ≤ e^{(β*+β')a₀/2} < e^{β*a₀} (β′ < β* the second distinct real value — here is where finite defect matters) and polynomial on-line sea; (5) re-quantification of Theorem 4.4 in the exponential regime (E-149.3). **Under general ¬RH the branch remains open**, with the exact boundary of §5.2: either a "gap in β" theorem (unavailable, likely RH-hard), or Gevrey-class cells (bumps with decay e^{−c|t|^{1/s}}, 1 < s < 1/θ(β*), legitimate by Denjoy–Carleman) plus the density theorems as input — a new route, with a design change to Def. 3.1, which this audit records as **Problem 149.A** without prejudging its success (the εₙ scenario of 149.5 shows that not even Gevrey suffices if the sup is not attained; one would additionally need to choose the test zero as a function of a₀ and prove dominance by subsequences — none of this is trivial).

---

## 6. Consequences for P47 and the logistic criterion

1. **139.A remains OPEN.** Doc 147's "CLOSED-PARTIAL" verdict is revoked. The chain `hyp:band` ⟹ Thm. 4.2 has its central link (Prop. 3.1) broken at (3.4) and at (†), the cell transplant undesigned, and an undeclared tacit structural hypothesis ("β* attained and isolated"). The criterion's state is the one D139 left:
$$\mathrm{RH}\iff\lim_k\sigma_{loc}^{(k)}=0:\quad \text{RH branch: THEOREM};\quad \text{¬RH branch: OPEN (139.A)}.$$
2. **P47 should not be touched in the direction §6.3 of D147 proposes.** Neither should `hyp:pw` be replaced by `hyp:band` as a *sufficient* hypothesis (it is not: the sign is missing), nor should "both branches theorems" be restored (false with or without the real axis). The only importable item from D147 into P47, in frank wording: (a) the structural diagnosis §1.3 (normalizing to 1 was the error; the non-normalized framework is correct) — that IS a real conceptual advance; (b) repaired `hyp:band` as a **provable design lemma** (§3.2, without the status of a bridge hypothesis); (c) the real-center axis as a harmless grid enlargement (§4.3), if desired, without any claim of unconditionality.
3. **Where the wall now stands, with exact coordinates:** no longer at a Paley–Wiener constant (D147 did dissolve that: there is no 139.1-bis, the modulus is cheap), but at two new and deeper sites: (i) **phase**: the sign of the target plane is a phase that rotates with a₀, controllable only by scaled Vandermonde prescription or by choosing a₀ within windows — executable under finite defect; (ii) **accumulation**: under general ¬RH, non-extremal off zeros of uncontrolled sign at near-maximal rate demand a spectral gap in β that nobody has. The ¬RH branch of the logistic criterion is today, frankly: *sketchable-theorem under finite defect (Doc 15x pending, list §5.4); open in general, with a named obstruction (Problem 149.A / scenario 149.5)*.
4. **Errata for the record** (ERRATA.md): E-149.1 (quantifier of (4.1)); E-149.2 = the conjugation error of (3.4) and of the "ι-fixed contributes +" paragraph — **CRITICAL**; E-149.3 (Theorem 4.4 not re-quantified in the exponential regime); E-149.4 (normalization B(0)=1 vs. band centered at ½, D136 (3.1), feeds §6.2's fallacy); E-149.5 (Lemma 2.1: constants depend on γ₀; the statement with a flat bump is false at the transform's zero set); E-149.6 (Prop. 3.1/Thm. 4.2 state "minimal off zero" while §5 requires maximal real part — internal contradiction); E-149.7 ((3.6): "poly(a₀)" term for a tail that under general ¬RH is exponential; (z₁,z₂)/(z₁,z₃) maximal-rate pairs omitted).
5. **The historical pattern, confirmed for the third time:** W_λ (a constant with the wrong sign survived for months); D136 (a constant that was not a constant); D147 (a polynomial that was exponential + one too many conjugations + a maximum that may not exist). Repairs of repairs concentrate the error at the exact point where the document claims to have been most careful: §3.4 titles itself "the verification that there is NO hidden divergent constant" and contains the conjugation error; §5 is titled "anti-false-victory" and presupposes the unguaranteed maximum. The operating rule for Phase 48: **sections titled "verification" are audited first.**

---

## References

**Internal (backward-only):** D147 (all); D139 (GAP-A, Lemma 139.1, GAP-B, §4.4, Problem 139.A, E-139.5); D136 (Defs. 3.1–3.2, Lemmas 5.2–5.3, Thms. 4.1–4.4, 5.4, Prop. 5.5, Obs. 5.1, (1.1)–(1.2), (3.1)); D108 (Prop. 2.2); D107 (Lemmas 2.2(b), 5.2(b), Thm. 5.5, Prop. 6.1, x∂ₓ closure and modulation); D144 (sub-resolution); P43 (autonomy); ERRATA.md (Phase 38).

**Literature (real, published; standard statements only):**
- R. P. Boas, *Entire Functions*, Academic Press (1954) — Ch. 1 §1.4 (three lines/Phragmén–Lindelöf), Ch. 2 (Hadamard, infinitude of zeros of nontrivial exponential-type functions), Thm. 6.8.1 (Paley–Wiener).
- B. Ya. Levin, *Lectures on Entire Functions*, AMS TMM 150 (1996) — Lectures 8–9 (indicator h(θ), directional growth; basis of the §4.2 analysis).
- L. Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer (1990) — Thm. 7.3.1 (Paley–Wiener for C_c^∞; superpolynomial decay with test-dependent constants, §1.2).
- A. E. Ingham, *On the estimation of N(σ,T)*, Quart. J. Math. Oxford 11 (1940) — N(σ,T) ≪ T^{4σ(1−σ)}log T (input to Computation 149.5; bounds counts, not the speed of accumulation in β).
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. 53 (2004) — Thm. 5.8 (N(t+1)−N(t) ≪ log t).
- A. Weil, *Sur les "formules explicites"…*, Comm. Sém. Math. Lund (1952) — the direction ¬RH ⟹ ∃f: Q(f) < 0; note that his actual mechanism adapts the test to the zero (phase included), it does not follow from evenness alone — D147's attribution of (3.3) to Weil with "c_W > 0 automatic" does not correspond to the classical argument.
- E. C. Titchmarsh, *The Zeros of Certain Integral Functions*, Proc. London Math. Soc. 25 (1926) — zero density of compact-support transforms (context §1.2: the zeros exist and move with the test).

*End of Doc 149.*

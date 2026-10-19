# Document 192 — Attack on Conjecture 179.6 (141.E-minimal): Euler continuation rigidity against vanishing near-doubles

**Program:** Riemann Hypothesis — Phase 58 (full audit)
**Mandate:** attack [CONJ 179.6] — the Euler face of the arithmetic front of the second tower — by the continuation-rigidity mechanism of D131 (Thm. 6.7, local purity), with the Davenport–Heilbronn test (GAP-141.DH) as a prior calibration of the mechanism. Apply the corrections from the D187 audit (E-187.7, degradation of 179.5, isolation clause of 179.4). Full candor; no numerics.
**Prerequisites (certified, not re-derived):** D131 (Thm. 6.7 local purity; Prop. 6.8 D–H; Wish 6.9 H⁺; two-bump Mertens test); D141 (Conj. 141.E, GAP-141.G1, GAP-141.DH, Calculation 141.M5); D150 (corrected GAP-141.DH verdict: liminf δ=0 via Prop. 150.2, unconditional fat zeros β>1, LP-134^(log) for D–H OPEN); D179 (Def. 179.1, Prop. 179.2, GAP-179.A, Conj. 179.6) with the D187 corrections (§2.1–2.5); D178/187 (Cor 178.11 certified: 178.C ∧ LP-134∞ ⟹ m<∞).

---

## 0. Conventions (self-contained)

ζ = Riemann zeta. **Off quadruple**: zero ρ=β+iγ with β>½, γ>0, plus its three mirrors; b:=β−½. **LP-134** (Def. 141.1): liminf_{off} b·log γ > 0. **LP-134∞** (minimal form, Def. 179.1): ∃c>0 with b_j log γ_j ≥ c for infinitely many j — equivalently, ¬(b_j log γ_j → 0 over the entire sequence). **D131-H⁺ category / "Euler category"**: Euler product convergent in Re s>1 with Hermitian local data + meromorphic continuation + functional equation (Selberg class type [S92, CG93, KP99]).

**[CONJ 179.6 = 141.E-minimal]** (text of D179 §5.3): *in the Euler category with continuation, there is no infinite sequence of off quadruples with b_j·log γ_j → 0.*

### 0.1. [E-192.1] Quantifier erratum in D179 — corrected before starting

D179 states that Conj 179.6 is "equivalent to LP-134∞ for members of the category." **False as written.** "No infinite sequence with b_j log γ_j → 0" forbids every convergent *subsequence* to 0, i.e. it is equivalent to liminf b log γ > 0 = **full LP-134**, not to LP-134∞ (which only denies convergence of the *entire* sequence). A configuration with fat zeros at j=2^k and b_j log γ_j = 1/j elsewhere satisfies LP-134∞ and violates 179.6 literally. We distinguish:

- **[CONJ 179.6-strong]** (the literal one): liminf b log γ > 0 in the category. = Conj. 141.E with log scale.
- **[CONJ 179.6∞]** (the one the tower needs): no member of the category has b_j log γ_j → 0 over its entire sequence of quadruples. With [Cor 178.11, certified in D187 §1.11]: 178.C ∧ 179.6∞(ζ) ⟹ m<∞.

Everything below attacks 179.6∞ (the minimal one) and records what it would say for the strong one. The erratum is reported for the phase record; it does not damage the architecture (D187 §1.11 already used the correct ∞ form).

---

## 1. Prior calibration: the Davenport–Heilbronn test (GAP-141.DH)

**Test design.** The Davenport–Heilbronn function f_DH [DH36] has a ζ-type functional equation but NO Euler product (a linear combination of two Dirichlet L-functions; D131 §6.6). If D–H **violates** the analogue of 179.6, Euler-ness is essential to the mechanism and the conjecture is aimed correctly; if D–H **satisfies** it, the mechanism is not Euler and the conjecture is aimed wrongly.

**State of the facts, after the D150 correction (which REFUTED the "FAT" verdict of D146):**

1. **[DH36, unconditional]:** infinitely many off zeros with β>1, i.e. b ≥ ½ ⟹ b log γ → ∞ over that subsequence. D–H trivially satisfies the LP-134∞-analogue (the fat zeros exist).
2. **[Prop. 150.2, unconditional]** (joint Voronin + Rouché universality): for each fixed ε>0, ≫_ε T zeros of D–H with b ≍ ε. Hence **liminf_{off} b = 0**: D–H **violates band separation** and violates every "liminf b·(bounded scale) > 0" form.
3. **The critical scale — is there a subsequence with b_j log γ_j → 0 in D–H?** This is exactly case (b)-vs-(d) of Prop. 144.9, declared OPEN by D150 §4.4: Prop. 150.2 gives b ≍ ε at positive-density heights *for each fixed ε*, but the regime ε = ε(T) → 0 requires **effective universality** (control of the size of the first admissible τ as a function of ε), not available. **[Literature gap, inherited from D150 and not closed here]:** no effective result is known on the approach of b vs. height for D–H zeros ([BS07] and the Vaughan/Spira line are computations and localizations at low height, not an effective asymptotic); none is claimed.

**[VERDICT OF TEST 192.2 — the test decides at HALF scale].**
- **For 179.6-strong (liminf):** the test IS decided and is **favorable to the Euler mechanism**. D–H (without Euler) has liminf b = 0 (Prop. 150.2): it violates the scale-free version of rigidity. The strong conjecture for the Euler category is not void of discriminating content: there is a natural object with functional equation that does the forbidden thing as soon as Euler-ness is removed. But beware of scale honesty: 150.2 gives liminf b = 0, **not** liminf b log γ = 0 — at log scale the strong test also remains open.
- **For 179.6∞ (the minimal one):** the test is **OPEN in both directions**, and is moreover structurally more demanding: ¬179.6∞ requires b_j log γ_j → 0 over the *entire* sequence, and D–H can NEVER satisfy that — the fat zeros of [DH36] are infinite and persist. **Test finding: D–H cannot be a counterexample to the 179.6∞-analogue even if its effective universality were proved.** The minimal form is invulnerable to the only known natural counterexample; the test only bites against the strong form.

**Calibration reading.** (i) The Euler mechanism is **supported but not confirmed**: the Euler/non-Euler separation is realized in nature at scale ψ≍1 ("cheap fatness, no repulsion," D150 §5.2), exactly the direction 141.E predicts; at polylog scale — the only one that matters for the tower — the test is beyond the reach of the literature. (ii) Non-trivial logical byproduct: the D179 §1 hierarchy is reflected in testability — the strong form is falsifiable by effective D–H, the minimal form is not falsifiable by D–H at all (the fat zeros shield it). Weakening the conjecture made it **less falsifiable**, not more attackable: the GAP-179.A pattern again, now on the test side.

---

## 2. The quantitative attack

Let (b_j, γ_j) be a hypothetical sequence of quadruples of an L-function in the category (or of ζ) with ε_j := b_j log γ_j → 0.

### 2.1. Route (a): the doublet in the logarithmic derivative — the wall, measured exactly

An off quadruple is, at ordinate γ_j, the twin pair {½±b_j+iγ_j}. The quantity the Euler product controls directly is −ζ'/ζ(s) = Σ Λ(n) n^{−s} in Re s>1. Does the Euler half-plane distinguish a twin pair from a double zero on the line?

**[LEMMA 192.3] (invisibility of the discriminant from the Euler half-plane).** Let w := s−(½+iγ_j) with Re s ≥ 1 (hence |w| ≥ ½). The difference between the contribution of the twin pair and that of a double zero at ½+iγ_j to the logarithmic derivative is
$$\Delta_j(s)\;=\;\frac{1}{w-b_j}+\frac{1}{w+b_j}-\frac{2}{w}\;=\;\frac{2b_j^2}{w(w^2-b_j^2)},\qquad |\Delta_j(s)|\;\le\;\frac{2b_j^2}{|w|\,(|w|^2-b_j^2)}\;\le\;17\,b_j^2$$
for b_j ≤ 1/10. In particular, over the whole closed half-plane Re s ≥ 1 the discriminant signal is uniformly O(b_j²) = O(ε_j²/(log γ_j)²).

*Proof.* Direct algebraic identity (common denominator). The bound: |w−b_j||w+b_j| ≥ |w|²−b_j² ≥ ¼−1/100, and |w|≥½; 2b²/(½·(¼−b²)) ≤ 17b². ∎

**The wall, with numbers.** To detect Δ_j from arithmetic one must evaluate Σ Λ(n) n^{−s} near s = 1+iγ_j with error o(b_j²) = o(ε_j²/(log γ_j)²). What is known unconditionally: (i) Mertens/Chebyshev give Σ_{p≤x} (log p)/p = log x + O(1) — error O(1); (ii) the "sea" of the other zeros contributes to −ζ'/ζ(1+iγ) terms of total size O(log γ_j) (RvM density); (iii) no unconditional zero-free region (Vinogradov–Korobov included) resolves below b ≍ (log γ)^{−2/3−}. Signal-to-noise ratio:
$$\frac{\text{signal}}{\text{noise}}\;\asymp\;\frac{\varepsilon_j^2/(\log\gamma_j)^2}{\log\gamma_j}\;=\;\frac{\varepsilon_j^2}{(\log\gamma_j)^3}\;\longrightarrow\;0\ \text{(cubically, and with } \varepsilon_j\to0\text{ on top).}$$
**It is the same wall as GAP-141.G1/GAP-179.A, on its worst face.** Precise identification: GAP-141.G1 required an o(1) error relative to signal (bL)² with b ≍ 1/log γ in windows on the *line*; GAP-179.A (D179 §5.2) hardened it to o((b_jL_j)²) with (b_jL_j)² = ε_j² → 0 in infinitely many enemy windows; the half-plane version here loses **in addition** the (log γ)² factor of the resonant window (in Re s ≥ 1 there is no resonance to amplify: the signal is b², not (bL)²). Conclusion: **this is not a new gap — it is GAP-179.A degraded by the change of chart to the half-plane**. The Euler product, used as an *estimate*, is strictly worse than the explicit formula on the line. Route (a) dies; the dividend is Lemma 192.3, which converts "the signal is second order" (known) into an exact uniform bound with constant, and the no-go corollary:

**[COR 192.4].** No detection scheme using finitely many values of −L'/L in Re s ≥ 1 with precision worse than cb_j² can distinguish the twin pair (b_j, γ_j) from a double zero on the line; in particular no known unconditional prime-sum bound (error ≥ O(1)) detects quadruples with ε_j → 0. *Proof: Lemma 192.3 plus (i)–(ii).* ∎

### 2.2. Route (b): what does D131's Thm. 6.7 give here?

The Thm. 6.7 mechanism (two-bump Mertens test): the local impurity δ' of F_{p,α} (|α| = p^{½+δ'}) is detected because |c_M| > 2p^{M/2} **for large M** — quantitatively, p^{Mδ'} − p^{−Mδ'} > 2 requires M ≳ 1/(δ' log p): **test support ≍ 1/δ'**. Three reasons why this does NOT transfer to 179.6:

1. **Divisor geometry.** The 6.7 object has *complete vertical progressions* of zeros at Re = β — the impurity is global and periodic, and the coefficient c_M accumulates it coherently (c_M = α^M + (p/ᾱ)^M, pure exponential growth). The enemy of 179.6 has **one** quadruple per height, with *decreasing* b_j: its footprint in the coefficients is that of a single oscillating term x^{b_j}cos(γ_j log x) — with no coherent accumulation. Local purity is a whole-column dial; 179.6 is about individual zeros.
2. **The support count.** Transposing the 6.7 threshold: effective impurity b_j becomes visible only at support log x ≍ 1/b_j = (log γ_j)/ε_j, i.e. **x ≥ γ_j^{1/ε_j}**, super-polynomial in γ_j. This is exactly the Euler incarnation of Calculation 141.M5 (a signal of width b needs resolution e^{1/b}); Thm. 6.7 can afford that support because its category has ONE prime and zero noise — ζ has the on-line sea contributing O(log γ) per window (§2.1). **Thm. 6.7 is the zero-noise case of the problem; its proof measures the size of the wall, it does not get through it.**
3. **D131 itself warns of this** (§6.5, comment (iii)): "the Euler product does not imply H" — an impure F_{p,α} has Euler-ness, functional equation, and violates positivity with off zeros in a column at fixed b. That does not touch 179.6∞ (that configuration has constant b: LP-134 holds with room to spare), but it does teach that Euler rigidity, if it exists, is not multiplicativity alone: it is multiplicativity + **positivity of the data** (a = Λ ≥ 0, Wish 6.9) + continuation. Conj 179.6 inherits that condition: it must be stated in the subcategory a ≥ 0 (in the general Selberg class one must assume at least Hermitian local data, as the §0 definition does).

**Verdict of route (b): D131 gives the *shape* of the mechanism (impurity visible at support 1/impurity; continuation couples the local data) and no applicable quantitative theorem.** Continuation rigidity remains a conjecture with a plausible mechanism and zero estimates.

### 2.3. Route (c): deformation rigidity of the Selberg class

Real, backward-verifiable rigidity facts: degree d ∈ {0} ∪ [1,∞) with (0,1) empty [CG93]; d=1 classified (ζ and shifted Dirichlet L-functions) [KP99]; 1<d<2 empty [KP02-11]. The class is **discrete in its invariants**: there are no non-trivial continuous families (deforming the Euler data while preserving continuation + functional equation falls outside the class except at discrete arithmetic parameters).

**Does that give 179.6?** No, and the reason is one of quantifiers: deformation rigidity forbids *families of functions*; the enemy of 179.6 is **a single function** whose internal sequence of quadruples degenerates (b_j → 0 is a limit *within* the divisor of a single object, not a curve in the space of objects). For the class rigidity to bite one would need a bridge of the type "a sequence of internal near-degenerations induces a deformation of the local data in the limit" — which is exactly Conj. 141.E unproved, reformulated. **Minimal statement of this route, formulated for the record:**

**[MINIMAL STATEMENT 192.5 — spectral rigidity of the class, necessary form].** *If L ∈ S (Selberg class, Hermitian data) has quadruples with b_j log γ_j → 0, then the sequence of "local data renormalized to the γ_j window" has an accumulation point that is the data of an object with a double zero on the line — an object the class forbids (or whose existence would imply a continuous family, forbidden by [CG93/KP]).* Status: **[GAP-192.A]** — the first half (compactness of renormalized local data + identification of the limit) does not exist in the literature or in the program; the second half (the forbidding of the limit) does not exist either: a double zero ON the line is not forbidden in S (simplicity of zeros is an open conjecture, D179 §3.2). As it stands, route (c) reduces 179.6 to two unknown statements. Candor: it is the route with the best *shape* (the only one where the limit b→0 becomes an object) and the worst *footing* (neither of its two pieces has a proved analogue).

---

## 3. The reverse direction: is 179.6 even true? — the logical world it inhabits

**Search for a counterexample in the category.** (i) Epstein zeta functions with class number h>1: known off zeros (same Davenport–Heilbronn method) but **without Euler-ness** (the quadratic form is not multiplicative for h>1) — outside the category ✓ consistent. (ii) Linear combinations of characters (D–H included): no Euler-ness, outside ✓. (iii) Artin L-functions not provably entire: they have Euler-ness; their membership in S depends on holomorphy (Artin open), and under standard conjectures they are automorphic ⟹ GRH expected — no known off zero. (iv) **No member of the Selberg class is known with even a single off zero**, let alone with the vanishing sequence. Search result: empty, and empty for the correct structural reason (everything with known off zeros lacks Euler-ness).

**The logical world of 179.6.** Under the standard conjecture (GRH for S), 179.6 is **vacuously true** (there are no quadruples). Its entire content lives in the ¬GRH world: it says that *if* off zeros exist, they respect polylog repulsion (at least not all vanishing). It is a rung strictly weaker than RH-for-the-class and strictly stronger than nothing: the first statement in the chain GRH ⟹ LP-134(S) ⟹ 179.6-strong ⟹ 179.6∞ that has its own candidate mechanism (continuation) instead of positivity. That is what makes it attackable in principle — and is the only reason: no standard conjecture *other than GRH* implies it (density theorems/conjectures die at s ≍ 1/log T by Prop. 176.9, applicable member by member; simplicity of zeros gives no separation, D179 §3.2).

---

## 4. Anti-circularity test

| Object | RH-free? | ζ-free? | Where ζ/arithmetic re-enters |
|---|---|---|---|
| E-192.1 (quantifier) | yes (logic) | yes | does not re-enter |
| Verdict of test 192.2 | yes | yes (D–H + Voronin, cited) | the literature gap is D–H's, not ζ's |
| Lemma 192.3 / Cor 192.4 | yes | yes (partial-fraction algebra + Mertens) | the no-go uses only unconditional bounds |
| §2.2 (D131) | yes | yes (category) | the conjectural rigidity IS where Euler-ness must enter |
| Statement 192.5 / GAP-192.A | — | no (Selberg class) | compactness of local data: pure arithmetic, no candidate |

No proof uses RH or numerics. The pattern holds: what is proved (192.3/192.4) is a no-go; the arithmetic remains in the GAPs.

---

## 5. Verdict

**CONJ 179.6: NEITHER PROVED NOR REFUTED. Final status: CALIBRATED-CONDITIONAL (implied only by GRH-for-S, vacuously) and REDUCED in its only quantitative route to the SAME wall (GAP-179.A, half-plane face, strictly worse), with the Euler mechanism SUPPORTED at half scale by the D–H test.**

1. **[E-192.1]** The literal 179.6 of D179 is LP-134-strong, not LP-134∞; the tower only needs 179.6∞. Erratum reported; architecture intact (Cor 178.11 already used the correct form).
2. **[D–H test, 192.2 — the requested calibration]:** decided at band scale (**favorable**: D–H without Euler has liminf b = 0, Prop. 150.2 — Euler-ness is essential to the strong form of rigidity); **open at polylog scale** (case (b)-vs-(d) of 144.9, requires effective universality — [literature gap] inherited from D150, not closed). Finding: **D–H can never refute 179.6∞** (its fat zeros [DH36] are infinite): the minimal form is structurally unfalsifiable by the only known natural counterexample. The mechanism points correctly for the strong form; for the minimal one the test is mute.
3. **[LEMMA 192.3 + COR 192.4] (what is proved):** from the Euler half-plane, the twin-pair/double-zero discriminant is uniformly ≤ 17b²; no unconditional prime-sum estimate (error ≥ O(1) against signal ε_j²/(log γ_j)² and noise O(log γ)) detects it. **The wall of the quantitative-Euler route is GAP-179.A again — not a new one — and on a worse chart** (without the line's resonant (log γ)² factor): the Euler product used as an estimate is weaker than the explicit formula, not stronger.
4. **[D131 route]:** Thm. 6.7 gives the shape of the mechanism (impurity visible at support 1/impurity) and nothing quantitatively transferable: it is the zero-noise, complete-column case; the enemy of 179.6 is individual and vanishing. Continuation rigidity remains without a single estimate.
5. **[Class rigidity route, 192.5 / GAP-192.A]:** the discreteness of the Selberg class ([CG93], [KP99-11]) attacks the wrong quantifier (families, not internal degenerations); the bridge "internal near-degeneration ⟹ deformation of the data" is 141.E renamed. Candid reduction: 179.6 ⟸ (compactness of renormalized local data) ∧ (forbidding of the limiting double zero) — two pieces with no analogue in the literature, the second equivalent to an effective form of simplicity (= GAP-179.B again).

**Numbered GAPs:**
- **[GAP-192.A]** (class route): compactness/convergence of local data renormalized to the γ_j window for an L ∈ S with b_j log γ_j → 0, and identification of the limit as an object with a double zero on the line. No candidate tool; the "forbidding of the limit" half collapses into GAP-179.B (effective separation ≡ Liouville of the discriminant).
- **[GAP-192.B = literature gap, inherited from D150]:** effective universality for D–H (first admissible τ as a function of ε) — would decide the test at polylog scale and, with it, whether 179.6-strong is correctly aimed.
- **The residual wall is NOT new:** the quantitative route dies in GAP-179.A (io form of GAP-141.G1), confirming the D179 §5.2 hierarchy with one more face: line (G1) < line-io (179.A) < half-plane (192.4, without resonance). Three faces, one wall.

**Successor direction.** (i) The only route with new shape is GAP-192.A: attempt the compactness of local data with D131's topology (the category already has the notion of local data; the renormalization to a window is missing) — construction session, high risk, but it is the only place where "b_j → 0" becomes an object instead of an estimate. (ii) GAP-192.B is the only item decidable with foreseeable literature (effective universality is an active area); closing it would calibrate the strong form once and for all. (iii) For the tower: nothing in this session moves the 178.C ∧ LP-134∞ pincer — the arithmetic front remains a statement with three faces (179.4 dynamic / 179.B static / 179.6 Euler) and all three lead back to the same second-order wall; the asymmetry discovered here (the minimal form is the least falsifiable) suggests the next attack should go to the **strong** form via 192.B, not to the minimal one.

---

### References

**Internal (backward-only):** D131 (Thm. 6.7, §6.5 Mertens test, §6.6 Prop. 6.8, Wish 6.9); D141 (Conj. 141.E, GAP-141.G1, GAP-141.DH, Calculation 141.M5); D144 (Prop. 144.9, Cor. 144.10); D146 with the verdict corrected by D150 ([Prop. 150.2], corrected GAP-141.DH verdict §4.4, "cheap fatness" §5.2); D176 (Prop. 176.9); D178 (Cor 178.11); D179 (Def. 179.1, Prop. 179.2, §3.2, GAP-179.A, GAP-179.B, Conj. 179.6); D187 (E-187.7, §1.11, §2.3–2.5, degradation of 179.5).

**Literature:** H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series I, II*, J. London Math. Soc. 11 (1936), 181–185, 307–312. — A. Selberg, *Old and new conjectures and results about a class of Dirichlet series*, Proc. Amalfi Conf. (1989), Salerno 1992. — J. B. Conrey, A. Ghosh, *On the Selberg class of Dirichlet series: small degrees*, Duke Math. J. 72 (1993), 673–693. — J. Kaczorowski, A. Perelli, *On the structure of the Selberg class I: 0≤d≤1*, Acta Math. 182 (1999), 207–241; *VII: 1<d<2*, Ann. of Math. 173 (2011), 1397–1441. — E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (Heath-Brown), Oxford 1986, §10.25. — E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp. 76 (2007), 2045–2049. — R. Spira, *Some zeros of the Titchmarsh counterexample*, Math. Comp. (1968). — S. M. Voronin, *Theorem on the "universality" of the Riemann zeta-function*, Izv. Akad. Nauk SSSR 39 (1975).

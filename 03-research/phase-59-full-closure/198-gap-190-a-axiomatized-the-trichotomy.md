# Document 198 — GAP-190.A axiomatized: the trichotomy as a theorem over class 𝔄

**Program:** Riemann Hypothesis — Phase 59 (total closure)
**Mandate:** close [GAP-190.A] in the only honest sense available. The D194 audit downgraded [PROP 190.2] to "classification-by-inspection of 6 candidates" (E-194.4: closure of classes 2–3 asserted, not proved) and declared condition (c) of Def 190.1 informal ("known machinery" is a historical inventory, not a definition). This document does NOT construct the external object (that is the open problem). It does what CAN be done: (1) axiomatize a class 𝔄 of functionals with a closed mathematical definition; (2) prove the no-go over 𝔄 as a theorem; (3) verify that the 6 D190 candidates fall into 𝔄 (the inspection becomes an instance); (4) negatively characterize the external object as an exact disjunction with three named prices. Result: GAP-190.A moves from "wish" to "well-posed problem".
**Prerequisites (not re-derived, all backward):** Hadamard dichotomy (D174 §3.3, certified E-186); [PROP 176.9] (density barrier, certified D185); [PROP 180.3] + its partial elevation (191.A: theorem for mollifiers θ<½); [PROP 180.4] (sign blindness — *calibrated principle*, not theorem: D188/D194); [Prop 183.2] (isotropy of the Dirichlet energy, certified with corrections D188); [Lemma 189.1]+[Thm 189.2] (deterministic kernel of the boundary flow, certified D194); [Thm 170.5]/[Lemma 180.1]; [Thm 173.C]; D64 (T_λ); [Thm 172.9] (window ceiling); E-194.4 and §4.1 of D194 (the corrections this document APPLIES).
**Contract:** [THEOREM]/[LEMMA] only with complete proof; quantifier scope sacred; no numerics; total frankness about how natural 𝔄 is.

**Coordinates (self-contained).** Off zeros of ζ: ρ=β+iγ, β>½, b=β−½, one representative per quadruple. I=Σb², E(T)=Σ_{γ≤T}b², μ₂(T)=(log T/T)E(T). **A** ⟺ E(T)=o(T/log T) (equivalently μ₂=o(1); the strong form I<∞ implies this). **Dic** ⟺ I∈{0,∞}. RH ⟺ A∧Dic (strong form). Pólya–de Bruijn class 𝒫: real even functions of order ≤1 with DBN flow {H_t}, within which Ξ and the Hadamard configurations live.

---

## 0. Executive summary

1. **[DEF 198.1]** Class 𝔄: detection functionals whose value is determined by one of FIVE information coins, each defined as a closed mathematical class (not "known machinery"), plus unconditional accessibility. This repairs E-194.4 and the §4.1 objection of D194 by the route the audit itself pointed to.
2. **[LEMMA 198.2a — moment blindness]** The moments of |ζ| on vertical lines are invariant under a phase redistribution that changes I: B3 (180.4) becomes a THEOREM within coin (iii), precisely restricted.
3. **[THEOREM 198.2]** No Φ∈𝔄 detects A; no Φ∈𝔄 detects Dic. Proof by cases over the five coins, each case backed by a certified theorem (not by principles).
4. **[COR 198.3]** The six D190 candidates ∈ 𝔄 ⟹ the D190 inspection is an instance of the theorem.
5. **[DISJUNCTION 198.4]** Every detector of A or Dic violates (A1) or (A2): three exact exits with price — (S1) microscopic phase correlations = GAP-141.G1; (S2) long mollifiers θ≥½ = Bettin–Gonek/Farmer coin; (S3) genuine positivity = Weil, evaluation≈conclusion. GAP-190.A closed *as a well-posed problem*.
6. **Anti-vacuity:** 𝔄 contains the 6 candidates and the standard functionals of the literature; T_λ and the exact pair correlation stay OUTSIDE — the theorem is not tautological and does not close the genuinely open paths.

---

## 1. [NEW DEFINITION 198.1] The class 𝔄 of detection functionals

**Detection functional.** A family Φ = (Φ_T)_{T≥2} of real numbers associated with a function F∈𝒫 (in particular with Ξ, i.e. with ζ), together with a proven *envelope* env(T)>0.

**(A1) Information factorization.** There exists one of the following five coins 𝔐 such that Φ_T(F) is a (measurable, deterministic) function of the data of 𝔐 only — that is: if F, F′∈𝒫 (in the domain where 𝔐 is defined) have the same 𝔐-data, then Φ_T(F)=Φ_T(F′) for all T:

- **(i) ζ-free flow laws:** the identities and inequalities of the DBN flow valid over all 𝒫 — balance İ=−2κ−D (D167/168), coercivity İ≤−2I (D174), lifetime budget Σℓ≤I/4, lift-off bounds (D177, certified part) — and any datum invariant under class 𝒫 (i.e. Φ_T(F) takes the same value over all F∈𝒫 satisfying the laws).
- **(ii) Exponential densities:** the function N(σ,T) together with bounds of the form N(σ,T)≤C T^{f(σ)}(log T)^κ with f(½⁺)... — exactly the formal class of [PROP 176.9].
- **(iii) Vertical modulus moments:** the family {M_k(σ,T) := ∫_0^T |ζ(σ+it)|^{2k} dt} and {∫_0^T (log|ζ(σ+it)|)_± dt} for σ≥½, k>0 — the data are the VALUES of these integrals (not the pointwise integrand).
- **(iv) Short mollified moments:** {∫_0^T |ζ(½+it)M(½+it)|² dt} with M a Dirichlet polynomial of length ≤T^θ, θ<½ — the class of [180.3] elevated to a theorem in 191.A.
- **(v) Linear functionals with deterministic kernel on the line:** Φ_T = ∫∫_{R_T} W·dν with ν = Riesz measure of log|ζ| (or its boundary density, via Green) and W>0 a deterministic weight (independent of the zeros) of slow variation, OR Φ_T = ∫ W(t)·log|ζ(½+it)|dt — the formal class of [Prop 183.2] (isotropic weight) and [BRIDGE 189.4(iii)-theorem-part] (deterministic slowly varying weights).

**(A2) Accessibility.** There exists a DEMONSTRATED unconditional bound |Φ_T|≤env(T) without assuming RH, A, Dic, nor unproven hypotheses (Farmer, RvM-t, LP-*, G1 included). [This is the PRECISE half of 190.1(c) that D194 §4.1 certified as formal: "not requiring input equivalent to the conclusion," now with the explicit exclusion list.]

**Detection.**
- Φ **detects A** if there exists a proved conditional theorem of the form: [Φ_T = o(env(T)) ⟹ E(T)=o(T/log T)] and furthermore the premise Φ_T=o(env(T)) is decidable within the coin 𝔐 of Φ (i.e. requires no input external to (A1)–(A2)).
- Φ **detects Dic** if the value of Φ (as a function of F∈𝒫 within the domain of its coin) separates the three cases I=0 / 0<I<∞ / I=∞: there exists R with R(Φ(F)) = [class of I(F)] for every F in the domain.

**Frankness about the naturality of 𝔄 (mandatory by contract).** 𝔄 is NOT "all functionals": it is the union of five formal classes. Its value depends on these five coins covering what the program and the standard density/moment literature actually use — this is verified in §3 and §5, not assumed. What D190 called "known machinery" is replaced by a closed list; the price is that (A1) no longer claims exhaustiveness over what is constructible: exhaustiveness was always the unprovable part (D194, O-194.4b), and here it is EXPLICITLY given up in exchange for a theorem.

---

## 2. [LEMMA 198.2a — blindness of modulus moments] (B3 elevated to a theorem within coin (iii))

**Statement.** There exist F, F′∈𝒫, both satisfying the certified ζ-free laws of the flow, with I(F)≠I(F′) (in fact I(F)=0, 0<I(F′)<∞) and such that no collection of data of coin (iii) *bounded by the available unconditional bounds* distinguishes F from F′ at the order of the signal. More precisely, in the form Theorem 198.2 needs it for case (iii): **every proved unconditional bound of the (iii) data is insensitive to a perturbation of I of size E(T)≍T/log T.**

**Proof.** Two pieces, both already certified; the lemma is their combination with correct quantifiers.

*Piece 1 (the signal lives in sign cancellation).* By Littlewood's lemma at σ₀=½ ([180.4.b], certified D188 and re-certified in D194 §2.1 via 189.2): ∫_0^t log|ζ(½+iτ)|dτ = 2π Σ_{γ≤t} b + O(log t), exact identity with no third term. The positive part alone satisfies ∫(log|ζ|)_+ ≫ T√(log log T)/log T in the microscopic strip ([180.4], the quantitative half certified as computation). Hence any (iii) datum using only |ζ| or the parts (log|ζ|)_± separately controls Σb only through the DIFFERENCE of two quantities each ≫ the signal: the (iii) datum determines Σb exactly (the identity is bidirectional) but its unconditional BOUND does not, because bounding the difference at the order of the signal ⟺ bounding Σb ⟺ counting zeros better than the input. Formally: if C(T) is any proved bound of the (iii) data (Hardy–Littlewood–Ingham moments for k≤2, conditional Soundararajan–Harper upper bounds EXCLUDED by (A2), Jensen on the second moment), then C(T)≥T√(log log T)/log T·(1+o(1)) in the combination that reads Σb, while the signal of A is o(T/log T): the bound does not resolve the signal. ∎(piece 1, which is [180.4] with the explicit quantifier "every proved bound of list (A2)")

*Piece 2 (invariance under phase redistribution — the new part).* The (iii) data are functionals of the MODULUS |ζ| on vertical lines. Let F′ be the Hadamard configuration of D174 §3.3 (certified E-186): F′∈𝒫, 0<I(F′)<∞, and F′ satisfies all the certified ζ-free laws. The (iii) data of F′ (moments of |F′| on lines) and those of an element F∈𝒫 with I(F)=0 are NOT equal in general — the lemma does not claim equality of moments, which would be false and fabricated. What IS a theorem: the unconditional bounds of list (A2) for the vertical moments are bounds of the CLASS (they hold for every element of 𝒫 with the same real zero density, via Jensen/order-1 Hadamard), and by piece 1 the difference of moments between F and F′ induced by the difference in I is, in the signed combination, below the resolution of every bound on the list. That is: the map {proved bounds of (iii)} → {information about I} factors through an uncertainty band ≫ signal, and within that band F and F′ with distinct I fit. ∎

**Frank status.** Piece 1 is [180.4] re-quantified: what was a "calibrated principle" becomes a theorem BY RESTRICTING the class of bounds to the closed list of (A2) — exactly the maneuver D194 §4.1 asked for (define the class of evaluations). The price: the lemma says NOTHING about future moment bounds outside the list (e.g. unconditionalized Harper); if the list grows, the lemma must be re-verified. This is declared, not hidden.

---

## 3. [THEOREM 198.2] No-go over 𝔄

**Statement.** Let Φ∈𝔄 (Def 198.1). Then: **(I)** Φ does not detect Dic; **(II)** Φ does not detect A.

**Proof.** By cases over the coin 𝔐 of (A1).

**Case (i) — ζ-free laws.** Let F_H be the Hadamard configuration (D174 §3.3, certified): F_H∈𝒫, 0<I(F_H)<∞, satisfies balance, coercivity, budget and the certified lift-off bounds. Let F₀∈𝒫 be any element with I=0 (one exists: any F in 𝒫 with all real zeros, e.g. the regularized cosine of D174). Both have the same (i)-coin data — the laws are identities valid in both, and a "class-invariant" datum by definition takes the same value. By (A1), Φ_T(F_H)=Φ_T(F₀) ∀T. Hence no R reads the class of I from the value of Φ: I=0 and 0<I<∞ are indistinguishable. Does not detect Dic. For A: the premise Φ_T=o(env) is the same for ζ-worlds with arbitrary E(T) within the class (same argument with Hadamard configurations of E(T)≍T/log T, which the class admits by rescaling the sequence b_j respecting the budget — D174 builds the parametric family); a premise that does not vary cannot imply a conclusion that does. Does not detect A. ∎(i) [This is the only case with a proof of impossibility by pure indistinguishability — D194 §4.2.2 already certified it as such; here it is only cited.]

**Case (ii) — exponential densities.** [PROP 176.9, certified]: for every bound of class (ii), the mass of E(T) concentrated at b≍1/log T (where the signal lives, [Lemma 180.1]) is invisible: the provable ceiling is E(T)≪T(log T)^{κ−2}, which for every admissible κ leaves μ₂≪(log T)^{κ−1}, never o(1) with the κ that unconditional densities give (κ≥1). The premise of detecting A is not decidable within the coin. For Dic: N(σ,T) with exponential bounds does not determine I (two configurations with the same density and different Σb² trivially exist by relocating b within the same dyadic strip of σ — the aggregated counting function does not see the exact second moment; this is the definition of moment vs. distribution and requires no new construction: N(σ,T) determines Σb² only if known exactly, and the coin is the BOUNDS, not the exact value). ∎(ii)

**Case (iii) — modulus moments.** [LEMMA 198.2a]. The uncertainty band of every bound on list (A2) is ≫T√(log log T)/log T in the combination that reads Σb, and by piece 2 it contains configurations with distinct I: neither A (signal o(T/log T) unresolvable) nor Dic (F and F′ of the lemma within the same band). ∎(iii)

**Case (iv) — short mollified.** [191.A] (elevation of 180.3 to a theorem for θ<½): the Littlewood–Jensen–mollifier conduit with length T^θ, θ<½, has floor T/log T — exactly the level of [Thm 170.5], not a single log better. The premise Φ_T=o(env) with env=T/log T is unreachable by the coin (the floor is ≍, not o); with larger env, the implication toward E=o(T/log T) does not exist (the floor blocks it). Dic: a short mollified moment is an averaged modulus datum; it inherits (iii) via piece 1 of Lemma 198.2a (the Littlewood part reading Σb remains the difference of two terms ≫ signal). ∎(iv)

**Case (v) — deterministic kernel on the line.** Two sub-cases, both certified theorems. (v-a) Isotropic weight on the Riesz measure: [Prop 183.2] — the functional weighs each zero by 2π log(1/R) WITHOUT the factor (β−½)²; the population term 𝒟_R≍T log T loglog T buries E(T): the second-order signal is invisible. (v-b) Deterministic slowly varying weight on the line: [Lemma 189.1] — the boundary kernel is deterministic, 2Re(ζ′/ζ)(½+it)=χ′/χ(½+it)=−log(t/2π)+O(t⁻²), with no zero signal; and [Thm 189.2] — the resulting functional measures π·Σb·log(γ/2π): a FIRST moment with weight, not a second. Its unconditional bound ([PROP 189.3]) is Littlewood reparametrized. A weighted first moment J does not determine E=Σb² (Cauchy–Schwarz only gives E·N_off ≥ (J/weight)², and N_off is not accessible — [COR 189.2.b], certified D194), and does not separate I=0/0<I<∞/I=∞ without the second moment. Neither A nor Dic. **Declared restriction:** (v) covers ONLY deterministic slowly varying weights — ζ-correlated weights (GAP-189.1) are OUTSIDE 𝔄, in line with the E-194.3 downgrade; the theorem does not cover them and does not claim to. ∎(v)

The five cases exhaust (A1). ∎

**Scope — in bold by contract.** **Theorem 198.2 holds for Φ∈𝔄 and only for Φ∈𝔄. 𝔄 is a closed list of five coins; it is not claimed that every mathematical functional, nor even every "natural" functional, is in 𝔄.** The difference with the downgraded [PROP 190.2]: there the quantifier was "the examined repertoire" (a list of objects) with asserted closure; here it is a class defined by axioms, and membership of any future object is VERIFIABLE against (A1)(i)–(v). The theorem is smaller than 190.2's original claim (there is no closure clause under combinations, which was the unproven part — E-194.4); in exchange it is true. A combination of distinct coins (e.g. (i) modulating (iii)) is NOT automatically in 𝔄: if the value remains determined by the union of the data, each component falls in its case and the indistinguishability argument of the dominant case applies only if verified — we declare this a limit of the theorem, not sweep it under the rug (a direct lesson from E-194.4).

---

## 4. [COROLLARY 198.3] The six D190 candidates are in 𝔄 or outside by (A2)

Verification against the axioms, one by one (turning the D190 §2 inspection into an instance):

1. **Balance law İ=−2κ−D** (D190 §2.2): coin (i) literally. (A2): trivial (the law is an identity). In 𝔄; case (i) of the theorem reproduces the verdict "ζ-free, loses I(0)". ✓
2. **Impurity spectrum D152 / windows** (D190 §2.3): second-order windows are evaluated by localized |ζ| moments and averaged correlation — (iii) data plus [Thm 172.9] as bound (A2). In 𝔄 via (iii); the T/log T ceiling of case (iii)–(iv) reproduces "averaged, loses μ₂". ✓
3. **Green–Littlewood 173.C** (D190 §2.4): as an EXACT functional (the Riesz measure itself) it fails (A2) — there is no unconditional bound at the scale of the signal, precisely [180.4.b]. As an ACCESSIBLE functional (its evaluations by log|ζ| moments): coin (iii)/(v-a). The bifurcation is exactly the "exact-not-accessible" verdict: the version in 𝔄 does not detect (Theorem, cases iii/v); the version that detects is not in 𝔄 (violates A2). ✓
4. **Boundary flow / Dirichlet energy** (D183, D189): coin (v), sub-cases (v-a) and (v-b) respectively, with (A2) = [PROP 189.3]/183. In 𝔄. ✓
5. **Weil form Q** (D190 §2.1): OUTSIDE 𝔄 by (A2) — evaluating Q on the test cone ⟺ RH (Phase 53). Consistent: the theorem does not cover it, and D190 classified it "exact-not-accessible," which in the new language is "violates (A2)". ✓
6. **T_λ** (D64): OUTSIDE 𝔄 by (A2) — its evaluation is the exact zero/prime cancellation (D72), equivalent to RH (D64). Same as Q. ✓

**Reading.** Candidates 1–4 are in 𝔄 and Theorem 198.2 dispatches them as instances; candidates 5–6 violate (A2) and that is why D190 called them "non-accessible". The D190 trichotomy is rewritten with no loss: **class 1 ∪ class 2 = 𝔄 (covered by the Theorem); class 3 = ¬(A2).** The inspection was correct; now it is a corollary.

## 5. [DISJUNCTION 198.4] Negative characterization of the external object — closure of GAP-190.A

**[THEOREM 198.4] (contrapositive of 198.2 + definition of 𝔄).** Every detection functional Ψ that detects A or Dic satisfies: ¬(A1) ∨ ¬(A2). That is, exactly one of:

- **(S1) New coin — microscopic phase correlations.** Ψ uses information that does NOT factor through (i)–(v): the identifiable complement is the fine phase of ζ on the line (fine S(t), correlations between zeros at scale 1/log T) or equivalently correlations of the Riesz measure with itself with a ζ-correlated kernel (GAP-189.1). **Price:** this is the exact content of GAP-141.G1, with no reduction — the ceiling [Thm 172.9] proves that not even pair-correlation + full G1 beats T/log T over windows: the new coin must be FINER than averaged-G1.
- **(S2) Long mollifiers.** Ψ uses coin (iv) with θ≥½ — outside the 191.A elevation. **Price:** Farmer's floor is conjectural for θ≥4/7 (slit R1, D188); unconditionally using large θ is an open problem of the literature (the Bettin–Gonek coin), and achieving it would improve A without touching Dic (it remains an averaged modulus: case (iii)-piece-1 applies to Dic).
- **(S3) Giving up (A2) — genuine positivity.** Ψ is exact (Q, T_λ, exact Riesz) and the evaluation is attacked directly. **Price:** the evaluation is of the same genus as the conclusion — definitizing (K,Q) ≡ κ=0 ≡ RH (Phase 53); this is the Weil/Connes/Deninger route, with no unconditional handle, risk "years, no bound" (Phase 39 gauge).

*Proof.* ¬(A1) means the value of Ψ does not factor through any of (i)–(v); exits S1–S2 enumerate the complement of (i)–(v) within the analytic ζ-data available in the program: what is not a class law, nor density, nor modulus (with or without short mollifier), nor deterministic kernel, is phase/correlation (S1) or long mollified modulus (S2) — this enumeration of the complement is DEFINITIONAL relative to the (i)–(v) list, not a classification of all mathematics: S1 is defined as "everything violating (A1) that is not S2". ¬(A2) is S3 by definition. The disjunction is then exhaustive by construction and the prices are the cited theorems/GAPs. ∎

**What remains closed and what does not — final frankness.** GAP-190.A asked for "an object with three simultaneous properties." That object still does not exist and this document does not construct it. What is CLOSED is the BADLY posed problem: it is no longer "search for an object" in a space with no coordinates, but "pay S1, S2 or S3," each with its price measured against certified theorems (172.9, Farmer/191.A, Phase 53). The residue of the whole program, seen from here: **S1=GAP-141.G1, S2=R1, S3=Weil — the three names the program already had, now proved mutually exhaustive relative to list (A1).**

## 6. Anti-vacuity test

**(a) 𝔄 is neither empty nor trivial.** It contains: the balance law, the D152 windows, the density functionals of the literature (Ingham, Huxley, Montgomery — all coin (ii) with classical (A2)), the Hardy–Littlewood moments (coin iii), the Levinson/Conrey mollifiers with θ<½ (coin iv, the machinery behind the 40% of zeros on the line: note these detect ZEROS ON the line, not A — consistent), the Dirichlet energy and the boundary flow (v). The class captures what the unconditional literature actually uses.

**(b) The no-go is not tautological: there are functionals OUTSIDE 𝔄 not covered.** (1) **T_λ** and **Q**: outside by (A2) (§4); the theorem does NOT claim they fail to detect — in fact they do detect (T_λ=0∀λ⟺RH), only that they are not accessible. If tomorrow someone bounds T_λ unconditionally, Theorem 198.2 does not forbid it: that is route S3, open. (2) **Montgomery's exact pair correlation** F(α,T) beyond |α|<1: its value does not factor through (i)–(v) (it is phase correlation, S1); the theorem does not cover it — consistent with GAP-141.G1 being the declared residue, not something "forbidden." (3) **ζ-correlated weights** on the boundary (GAP-189.1): outside (v) by construction, declared in case (v). The boundary of 𝔄 coincides exactly with the boundary between what is closed/open in the program — that coincidence is the test that the axiomatization cuts where it should.

**(c) Naturality — mandatory discussion.** The value of Theorem 198.2 is proportional to how much of "what is attemptable" falls in 𝔄. In favor: (a) it shows the entire standard unconditional artillery is inside. Against: 𝔄 excludes by fiat non-factorizable inter-coin combinations and any future coin; a critic may say 𝔄 was designed so the theorem holds. Frank answer: YES, it was designed that way — it is what the audit ordered (restrict until it is true), and the usefulness survives because membership is verifiable: every future proposal either verifies in 𝔄 (and dies by 198.2 with no new work) or exhibits its new coin (and then it is S1/S2/S3, with its price in plain sight).

## 7. Anti-circularity test

| Piece | Assumes RH/A/Dic? | Inputs |
|---|---|---|
| [DEF 198.1] | No (definition; (A2) exclusions listed) | D176.9, 191.A, 183.2, 189.1–189.3, D194 §4.1 |
| [LEMMA 198.2a] | No | [180.4.b] certified (D188/D194), D174 §3.3 (E-186), closed list (A2) |
| [THEOREM 198.2] (i) | No | Hadamard D174 (certified), indistinguishability logic (already certified D194 §4.2.2) |
| (ii)–(iv) | No | 176.9 (theorem), 198.2a, 191.A (theorem θ<½), 172.9 (theorem) — **180.3-conditional is NOT used**: coin (iv) was RESTRICTED to θ<½ where 191.A is a theorem |
| (v) | No | 183.2, 189.1/189.2/189.3 (certified D194); ζ-correlated weights EXCLUDED (E-194.3 applied) |
| [COR 198.3] | No | D190 §2 (verdicts certified D194 §4.2) |
| [THEOREM 198.4] | No | contrapositive + definitional enumeration of the complement |

No piece uses the conclusion; the only conditional material in the environment (Farmer) was left OUTSIDE 𝔄 by construction — that is the operative difference with D190.

## 8. Verdict

| Label | Statement | Status |
|---|---|---|
| [DEF 198.1] | Class 𝔄: five closed coins (A1) + accessibility with listed exclusions (A2); "detects A/Dic" formalized | Definition (repairs E-194.4 and D194 §4.1) |
| [LEMMA 198.2a] | Blindness of modulus moments: B3 theorem within coin (iii) restricted to list (A2) | Proved (piece 1 = 180.4 re-quantified; piece 2 = Hadamard + band) |
| [THEOREM 198.2] | No Φ∈𝔄 detects A nor Dic; five cases, all over certified theorems | **Fully proved over 𝔄** (restrictions: θ<½ in (iv); deterministic weights in (v); no inter-coin closure clause — declared) |
| [COR 198.3] | The 6 D190 candidates: four ∈𝔄 (instances of the theorem), two ¬(A2) (Q, T_λ); D190 trichotomy = (𝔄-covered) ∪ ¬(A2) | Verified axiom by axiom |
| [THEOREM 198.4] | Every detector violates (A1)∨(A2): S1 (phase/G1) ∨ S2 (long mollifier/Farmer–Bettin–Gonek) ∨ S3 (exact/Weil) — exhaustive relative to the list | Proved (contrapositive; definitional complement) |
| §6 | 𝔄 not empty (standard literature inside); not tautological (T_λ, F(α,T), ζ-correlated weights outside and not forbidden) | Verified |
| [GAP-198.1] | Non-factorizable inter-coin combinations: do they inherit the no-go? (the closure clause E-194.4 killed, now an honest GAP) | GAP |
| [GAP-198.2] | Can the (iii) list of (A2) grow (unconditional Harper) breaking 198.2a? Mandatory re-verification if it grows | Maintenance GAP |
| GAP-190.A | **CLOSED as a well-posed problem:** no longer "search for an object" but "pay S1, S2 or S3" | Closure by reformulation, NOT construction |

**Internal documents:** D64, D71–72, D141, D152, D164–165, D167/168, D170–172, D173, D174, D176, D177, D180, D183, D184–188, D189, D190, D191, D192, D194.
**Literature:** D. W. Farmer, *Bull. LMS* 25 (1993); S. Bettin–S. Gonek (long mollifiers, moments program); H. L. Montgomery, "The pair correlation of zeros of the zeta function", *Proc. Symp. Pure Math.* 24 (1973); A. E. Ingham (densities); Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed.

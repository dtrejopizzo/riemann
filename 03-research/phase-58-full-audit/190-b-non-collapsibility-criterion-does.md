# Document 190 — The A↔B non-collapsibility criterion: does there exist an object that simultaneously produces μ₂ and I?

**Program:** Riemann Hypothesis — Phase 58 (full audit)
**Director's mandate (formalized here):** RH splits into two demands — **A** (spectral second moment: a functional that distinguishes the fine fluctuations μ₂, which requires anisotropy, sign sensitivity, and correlation resolution) and **B/Dic** (purity of state: complete elimination of interior states 0<I<∞, which requires global coercivity and dynamical closure). Implicit fact to examine: *one cannot simultaneously have a system closed by coercivity and a system that reconstructs exact second-order correlations, because coercivity destroys exactly the information μ₂ needs.* Critical test: does any object in the system simultaneously produce μ₂ and I without loss of information? If it exists, RH is potentially closable in this framework; if not, the system is structurally incomplete for RH.
**Prerequisites (not re-derived):** structural classification from the audit (D184–D188); [Thm 173.C] (Green–Littlewood); [Thm 170.5] (E(T)≪T/log T); [LEMMA 180.1] (E=(T/log T)μ₂); barriers 176.9 / 180.3-conditional / 172.9; balance law İ=−2κ−D (D167/168, certified); Hadamard dichotomy in the class (D174 §3.3, intact after E-186); [Cor 181.3] (conditional on A, LP-112 ⟺ RH); D64 (T_λ=0 ∀λ ⟺ RH); D152 (impurity spectrum); Rodgers–Tao 2020 (Λ≥0); Bagchi (universality/recurrence).
**Contract:** [THEOREM]/[PROP] only with complete proof; **the scope of quantifiers is sacred** — every no-go in this document is about the examined repertoire, NOT universal; no numerics.

**Coordinates (self-contained, identical to D170/173/176/180).** Off zeros of ζ: ρ=β+iγ, β>½, b=β−½∈(0,½), one representative per quadruple. I(0⁺)=Σb² (the instability energy). E(T)=Σ_{γ≤T}b². μ₂(T)=(log T/T)E(T) (microscopic mean-square displacement, D180). **A** ⟺ I<∞ ⟺ E(T)=O(1). **Dic** ⟺ I∈{0,∞}. **B** ⟺ (I<∞ ⟹ I=0) ⟺ Dic. **RH ⟺ A ∧ Dic.** Firm audited facts this session uses as internal axioms: (i) İ=−2κ−D is ζ-FREE (holds for the entire Pólya class; only I(0) carries ζ); (ii) the Hadamard configuration exists in the class with 0<I<∞ (Dic is FALSE in the class; every proof of Dic requires ζ-specific arithmetic); (iii) A ⟹ Lindelöf (176.7, certified); (iv) conditional on A, LP-112 ⟺ RH (181.3, certified); (v) the barriers of A post-audit: 1 theorem (176.9), 1 conditional-on-Farmer (180.3, → chink R1), 1 principle (sign blindness 180.4), 1 corollary (population, D183 corrected); live chinks R1 (non-standard mollifier) and R2 (anisotropic boundary flux).

---

## 0. Executive summary

1. **[DEF 190.1]** formalizes the "collapsing object": Φ must satisfy (a) recovery of I, (b) recovery of μ₂(T) for all T, (c) unconditional accessibility. The multiset of zeros is excluded as a trivial collapser: it satisfies (a)+(b) by definition and fails (c) by definition.
2. **Examination of the repertoire's six candidates** (Weil form Q, balance İ, impurity D152, Green–Littlewood 173.C, DBN flow {H_t}, moments T_λ): **none satisfies (a)∧(b)∧(c)**. Each verdict identifies the failing condition and the audited piece that proves it.
3. **[PROP 190.2 — repertoire trichotomy]:** every object Φ in the examined repertoire falls into exactly one of three classes: **(ζ-free: loses I(0))** ∪ **(unconditionally-averaged: loses μ₂)** ∪ **(exact-but-inaccessible: evaluating it is equivalent to RH or to an RH-hard problem)**. The intersection of the three demands is empty **in the repertoire**. This is NOT a universal no-go.
4. **Binary answer to the director: the current system is structurally incomplete for RH** — there is no collapser in the repertoire, and the exclusion mechanism is the one the director conjectured (coercivity/averaging destroys second-order information), with one refinement: the destruction operates through TWO distinct routes (ζ-freedom for the coercive side, isotropy/averaging for the correlational side), not through a single one.
5. **[GAP-190.A]** precise specification of the external object that would close the framework (the "Connes/Deninger object" from earlier phases, now with three simultaneous named properties). R2, if it paid off, would be a *first-order partial collapser* — it does not resolve μ₂ but would be the program's first accessible anisotropic functional.

---

## 1. [DEFINITION 190.1] Collapsing object

Let 𝔄 be the repertoire of constructible objects of the program: functionals, operators, measures, and flows defined from ζ, from its de Bruijn–Newman flow {H_t}, or from its zeros, via the program's machineries (Weil form, explicit formula, Littlewood's lemma, moments, densities, polynomials C_λ/T_λ).

**Φ ∈ 𝔄 is a COLLAPSER if it simultaneously satisfies:**

- **(a) Production of I (the coercive/global datum).** There exists a deterministic operation R_I with R_I(Φ)=I(0⁺). In particular Φ distinguishes I=0 from 0<I<∞ from I=∞: Φ carries the information of Dic.
- **(b) Production of μ₂ (the correlational/local profile).** There exists R_μ with R_μ(Φ)(T)=μ₂(T) for all T. In particular Φ resolves the transverse second order at microscopic scale u=b·log T≍1: Φ carries the information of A *with profile*, not just the limit value.
- **(c) Accessibility (unconditional control).** Some norm, trace, or moment of Φ is boundable **unconditionally** by known machinery (ζ moments, density theorems, explicit formula with integrable tests, monotonicity/balance of the DBN flow) at a scale comparable to or finer than the signal (a) and (b) require reading. Formally: evaluating R_I(Φ) and R_μ(Φ) must not require, as input, a statement equivalent to A, to Dic, or to RH.

**Exclusion of the trivial collapser.** The multiset Z={ρ} of zeros tautologically satisfies (a) and (b) (I and μ₂ are functions of Z) and tautologically fails (c): no unconditional machinery evaluates individual b_j (the program's master quantifier, Phase 49: every unconditional access to Z goes through sums Σg(γ) with g in the admissible class, and the admissible class averages). Condition (c) is exactly what separates "the object exists" from "the object is useful".

**The tension the mandate asks to formalize.** Accessibility ⟹ evaluation is an average (explicit formula with integrable test, moment in T, trace) ⟹ loss of the individual. This is the master quantifier (average→uniform, value→inertia; Phase 49, D154–157) in second-order form. This document's question is whether any repertoire object escapes it: whether the loss from averaging can be compensated by structure (anisotropy, sign, exactness).

**Scale observation (why (a)∧(b) is already almost RH-complete).** If Φ satisfies (a) and (b) with evaluable R_I, R_μ, then RH ⟺ (R_I(Φ)=0). A collapser is not a step toward RH: it is a *complete repackaging* of RH with an unconditional handle. This is why the director's question is the correct form of the structural test: not "can we prove RH?" but "does the framework even contain an object whose handle lets us grasp it?".

---

## 2. The repertoire's six candidates, one by one

### 2.1. The Weil form Q/W — fails (c); (a) only in index form

Q produces I indirectly: κ=neg.ind(Q)=2m (Phase 26) counts off zeros, and the transverse Hessian reads b². But evaluating Q's positivity **is** the Weil criterion: RH ⟺ Q≥0. Here (c) fails in its purest form: Q's "controllable norm" in the direction that matters (the test cone) is exactly the conclusion. Phase 53 said this in Krein language: definitizing (K,Q) ≡ κ=0 ≡ RH. Also (b) fails partially: Q through integrable tests is isotropic in b at first order (no-go 141.B2: first order integrates to zero); the second order exists in Q (the Hessian) but its extraction requires localized tests the explicit formula does not control unconditionally (GAP-141.G1). **Verdict: exact-but-inaccessible — collapser ⟺ conclusion.**

### 2.2. The balance law İ=−2κ−D — fails (a) by ζ-freedom

The law is coercive, certified, and ζ-FREE (D167/168): it holds for the whole Pólya class. By the Hadamard configuration (D174 §3.3, intact after audit E-186), there exists in the class an element with 0<I<∞ that satisfies ALL proved dynamical laws (balance, coercivity İ≤−2I, lifetime budget, moment hierarchy at its certified extremes n=1,∞). Formal conclusion: **no functional built from the balance law alone determines I(0)** — two initial conditions of the class with different I(0) satisfy the same laws. The law loses exactly the datum (a) asks for; it also loses (b) (μ₂ is a profile in T of the initial condition, invisible to an evolution law). This proves half of the director's conjecture, coercive-side: **dynamical closure was bought at the price of ζ-freedom, and ζ-freedom is the total loss of the state datum.** Verdict: **ζ-free — loses I(0).**

### 2.3. The impurity spectrum D152 / second-order windows — fails (b)→(c) by noise

This is the only candidate designed for μ₂: the second-order window produces signal Θ(c²) per off zero. But the noise per window is Θ(1) (S(t) dominates, H1 dead in every world, D170/171), collapse onto E is proved (D172: the pinned moment ≡2/3 is blind to zeros; exact Poisson blindness), and ceiling 172.9 establishes that even with pair correlation + full G1 one does not beat E≪T/log T via windows. That is: D152 satisfies an *averaged* version of (b) — it recovers E(T) up to Selberg's precision and not a log further — and that precision is exactly μ₂≪1, not μ₂=o(1). It does not produce I (the total sum diverges from window control: no-go 170.8). Verdict: **unconditionally-averaged — loses μ₂ (resolution dies in the noise floor, GAP-141.G1).**

### 2.4. The Green–Littlewood identity 173.C — formally satisfies (a) and (b), fails (c): currency change

Φ = the Riesz measure of log|ζ| (equivalently D(T)=∬log|ζ|). By [Thm 173.C], I is its **exact** transverse second moment; by layer-cake 176.8 and 180.1, μ₂(T) is also recovered exactly. It is the candidate closest to a collapser: (a)✓, (b)✓ with no loss (the identity is exact, certified in D185). But (c) fails by [PROP 180.4] (sign blindness, audited): every unconditional evaluation of ∬log|ζ| by moments is blind to sign, the positive part alone is worth ≫T√(log log T)/log T in the microscopic strip, and the sign cancellation in t is encoded EXACTLY in the zeros (Littlewood is an identity, not an inequality: there is no third term). Evaluating Φ better than T/log T ⟺ counting zeros better than Selberg ⟺ the original problem. **Verdict: exact-but-inaccessible — another currency, same price.** This case is the most instructive: it shows exactness does not buy accessibility, because the identity also transports the hardness.

### 2.5. The full DBN flow {H_t} — trivial collapser in disguise; fails (c)

{H_t}_{t>0} contains ALL the information (H_0 determines ζ by continuity; the zeros of H_t for t>0 are real and in principle computable, and Λ≥0 [Rodgers–Tao 2020] says the present t=0 is the exact edge of the real zone). It trivially satisfies (a) and (b). But the fine information of H_t as t→0⁺ IS the information of ζ: the rate at which complex pairs land (the "lifetimes" ℓ_j, the budget Σℓ≤I/4) is a bijective reparametrization of the b_j. What is unconditionally accessible from the flow is: Λ≥0, the balance law (ζ-free, §2.2), and gap bounds away from the corner; the corner (t→0⁺, where the pathology lives per D177, confinement certified) is exactly what is uncontrolled — 177.B is a GAP, and by [Thm 178.10-downgraded, D187] its full form is quasi-RH-hard. **Verdict: exact-but-inaccessible — it is Z with an extra coordinate t; condition (c) reduces it to §2.2 (the ζ-free part) plus §2.1 (the hard part).**

### 2.6. The moments C_λ/T_λ (Phase 32, D64) — fails (c): evaluation ⟺ RH

[D64]: T_λ=0 ∀λ ⟺ RH. T_λ thus produces the bit I=0 (a, partially) and its structure as a quadratic form in the c_k (D71) plus its trace via the Weil formula (D72: T_λ = A_λ^off − Σ_p(...)B_λ(log p)) connects it to the second order. But its evaluation is an exact arithmetic cancellation zeros/primes: the primes side is accessible, the A_λ^off side is the unknown, and the difference is controlled only by proving the cancellation — which is RH (the direction "T_λ accessible ⟹ RH" is D64's content, not a shortcut). Also (a) fails in a fine sense: T_λ is sensitive to the bit (are there off zeros?) but not to the value I (the family {T_λ} does not separate off configurations with different energy without resolving the transform — again the multiset). **Verdict: exact-but-inaccessible — an RH equivalence in moment notation.**

---

## 3. [PROPOSITION 190.2] The non-collapsibility criterion (repertoire trichotomy)

**Statement.** Let Φ be an object from the examined repertoire 𝔄* = {Q/Weil and its equivalent forms; laws and functionals of the DBN flow built from the certified ζ-free laws; window/density/mollifier/moment functionals of the four barrier families; integral identities of block 173/176; moments C_λ/T_λ}. Then Φ falls into at least one of three classes, and hence is NOT a collapser:

1. **(ζ-free)** Φ is invariant under the Pólya class ⟹ Φ does not determine I(0): fails (a).
2. **(unconditionally-averaged)** Φ is evaluated via exponential densities, standard mollified moments, correlation windows, or signless moments ⟹ Φ does not resolve μ₂=o(1): fails (b) at the required resolution.
3. **(exact-but-inaccessible)** Φ determines I and μ₂ exactly ⟹ every evaluation of Φ at the signal's scale is equivalent to counting zeros at that scale: fails (c).

**Proof.** (1) Is the Hadamard dichotomy, certified: the configuration of D174 §3.3 (intact after E-186) realizes 0<I<∞ within the class while satisfying all proved ζ-free laws; two class elements with different I(0) are indistinguishable to any class-invariant Φ, so R_I(Φ) does not exist. (2) Is the union of audited barriers, each a proved result on its family: [PROP 176.9] (theorem: no exponential density gives A — the fatal mass lives at s≍1/log T); [PROP 180.3] (conditional on Farmer's floor for the standard class — hence chink R1, see §4); [Thm 172.9] (theorem: ceiling T/log T via windows even with pair correlation + full G1); [PROP 180.4] (proved principle: signless moments have a floor ≫T√(log log T)/log T, and the cancellation is identically the zeros). In each family, the best outcome is μ₂≪1, and GAP-180.1 asks for μ₂=o(1): resolution is missing by a factor the barriers forbid recovering within the family. (3) For each exact Φ in the repertoire the argument is individual and is in §2: Weil (positivity=conclusion, Krein D164/165), Green–Littlewood (bidirectional identity 180.4(b): bound⟺zeros, no third term), fine-DBN (the corner is 177.B, quasi-RH-hard by the certified forward direction of 178.8), T_λ (D64 is the equivalence). In all four cases the "evaluation" required by (c) is a statement of the same genus as the conclusion — verified piece by piece, not by a general principle. The coverage of 𝔄* by the three classes is by inspection of §2's (finite) list plus closure under the program's operations: combining class-1 objects among themselves stays in class 1 (invariance is preserved); combining with averaged evaluations inherits class 2; inserting the exact datum falls into class 3. ∎

**SCOPE — in bold because the contract demands it.** **This is NOT a universal no-go. Proposition 190.2 characterizes the EXAMINED repertoire: the objects actually constructed by the program and their combinations under known operations. It is not claimed — nor can it be claimed with this document's techniques — that no mathematical functional exists satisfying (a)∧(b)∧(c). The quantifier is "for all Φ∈𝔄*", not "for all Φ".** The class of all functionals is not an object we know how to quantify over; what is proved is that the repertoire's three mechanisms exhaust the *known* mechanisms (Phase 49's exhaustiveness over the five crossings, plus the barriers of Phases 54–58), and that within the repertoire the intersection (a)∩(b)∩(c) is empty.

**[GAP-190.A] — specification of the external object.** The collapser, if it exists, must simultaneously have the three properties no object of 𝔄* combines:
1. **ζ-loaded in the state:** distinguishes initial conditions within the Pólya class (cannot be an evolution law or a class invariant) — it must read the initial condition's arithmetic, whose only proved entry point is gap fluctuations (D174.7).
2. **Anisotropic with sign at microscopic scale:** its coupling to an off zero is ∝b (or b²) with coherent sign, not |·|, resolvable at u=b·log T≍1 — the property none of the four barrier families have (isotropy, or canceling sign, or line saturation).
3. **With an unconditional handle:** some trace/norm of it bounded below the signal WITHOUT input of the RH/A/Dic genus — the property Weil, 173.C, fine-DBN, and T_λ lack.
This is the "Connes/Deninger object" of Phases 40–43 and 49, now with a contract: in the language of those phases, a cohomological invariant over Spec ℤ reading *inertia* (prop. 1) with *polarization* (prop. 2) and *demonstrable finiteness* (prop. 3). All three at once is precisely what Phase 43's polarization metric failed to achieve (it carried ζ: it had 1 and 2 but not 3).

---

## 4. Answer to the director and strategic consequence

**Binary answer: the current system is structurally incomplete for RH.** There is no collapser in the repertoire (Prop 190.2, scope declared). The mandate's implicit fact is examined and *refined*: it is correct that coercivity and second-order reconstruction do not coexist in the repertoire, but the mechanism is not one but two. The program's coercivity is ζ-free (that is its source of provability) and ζ-freedom — not coercivity per se — is what erases I(0) and μ₂. Symmetrically, correlational accessibility is averaged (that is ITS source of provability) and averaging erases the fine second order. **What gets proved gets proved because it forgets; what remembers does not get proved.** That is the precise form of the master quantifier at this phase.

**The chinks.** R1 (non-standard mollifiers): if it broke Farmer's floor, it would break barrier 180.3 — but it would still fall within class 2 unless the new family were also anisotropic; it would improve μ₂≪1 toward o(1) without touching (a): it would be progress on A, not a collapser. R2 (boundary flux σ=½): if it produced an unconditional Σb·log γ, it would be the **program's first accessible anisotropic functional** — but it is first order with weight: a *partial collapser* that breaks the isotropy barrier (property 2 of GAP-190.A halfway: sign yes, second order no) without giving μ₂ or I. It is not another currency (unlike 173.C, its evaluable side would not be identically the zeros): it is a new half-property. Worth the half-document it costs (D188).

**Strategic implication.** Without a collapser, the two towers are NOT two independent routes: they are two PROJECTIONS of the same deficit — the energy tower projects the deficit onto (b)+(c) (A: resolve μ₂ accessibly) and the dynamic/static tower onto (a)+(c) (Dic/178.C: load ζ into the coercive side accessibly). Proving one does not smooth the way for the other: the deficit is the same object seen from two sides. The three exits:
- **(i)** Search for the external object of GAP-190.A (three simultaneous properties, explicit contract) — the Connes/Deninger direction, now with a verifiable specification; risk: years, no bound (Phase 39's gauge).
- **(ii)** Attack the arithmetic pillars directly: LP-134∞/CONJ 179.6 (Euler category), 178.C, μ₂=o(1) via R1/R2 — measurable incremental progress, no promise of closure.
- **(iii)** Declare the structural classification a final result and publish (P49 with D184–188 + this criterion as closing chapter).
**Recommendation:** execute R2 first (cost: half a document; payoff: either a new anisotropic functional — the first brick of the genus GAP-190.A asks for — or a fifth barrier completing the classification); decide between (i) and (iii) with R2's and R1's results in hand. Exit (ii) without R2 would repeat formulations the ceilings 172.9/176.9 already forbid.

---

## 5. Anti-circularity test

| Piece | Assumes RH/A/Dic? | Inputs |
|---|---|---|
| [DEF 190.1] | No (definition) | — |
| §2 (six verdicts) | No | Certified results D64, D152/172, D167/168, D173/176 (audited D185), D174 §3.3 (audited D186), D178 (audited D187), D180 (audited D188), Rodgers–Tao |
| [PROP 190.2] class 1 | No | Hadamard dichotomy (ζ-free, certified) |
| [PROP 190.2] class 2 | No; 180.3 conditional-on-Farmer DECLARED (chink R1) | 176.9, 172.9, 180.3, 180.4 |
| [PROP 190.2] class 3 | No — all four cases individually verified, no unproved general principle | §2.1, 2.4, 2.5, 2.6 |
| §4 | Strategic reading, not a theorem | — |

No piece uses the conclusion as input; the only conditional (Farmer's floor within class 2) is declared and is exactly chink R1, already recorded in D188.

## 6. Verdict

| Label | Statement | Status |
|---|---|---|
| [DEF 190.1] | Collapser: (a) produces I, (b) produces μ₂(T) ∀T, (c) unconditionally accessible; trivial case excluded | Definition |
| §2 | None of the six repertoire candidates is a collapser | Verified piece by piece on audited results |
| [PROP 190.2] | Trichotomy: 𝔄* ⊆ (ζ-free: loses I(0)) ∪ (averaged: loses μ₂) ∪ (exact: inaccessible ≈ RH); (a)∩(b)∩(c)=∅ **in the examined repertoire, NOT universal** | Proved (class 2 modulo Farmer = R1, declared) |
| [GAP-190.A] | External object: ζ-loaded in the state + anisotropic-with-sign at microscopic scale + unconditional handle — all three at once | GAP (specification of the Connes/Deninger object) |
| [GAP-190.B] | Does R2 (boundary flux) produce an unconditional Σb·log γ? If so: first accessible anisotropic functional (first-order partial collapser) | GAP (immediate successor, D188) |
| Answer to the director | The system is structurally incomplete for RH in its current repertoire; the two towers are two projections of the same deficit | Reading of Prop 190.2 |

**Internal documents:** D64, D71–72, D112, D141, D152, D154–157 (Phase 49), D164–165, D166–169, D170–172, D173, D174, D175, D176, D177, D178–179, D180, D181, D183, D184–188.
**Literature:** B. Rodgers, T. Tao, "The de Bruijn–Newman constant is non-negative", *Forum Math. Pi* 8 (2020). B. Bagchi, "A joint universality theorem for Dirichlet L-functions", *Math. Z.* 181 (1982) / 1981 thesis (recurrence and universality). D. W. Farmer, *Bull. LMS* 25 (1993) (mollifier floor; conditionality declared via D188/R1).

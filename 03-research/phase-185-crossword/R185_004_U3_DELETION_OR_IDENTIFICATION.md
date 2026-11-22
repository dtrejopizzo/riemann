# R185_004 — U3: deletion or identification (piece U3 of the barrier theorem, CROSSWORD-TO-D §4.2)

RH is not asserted, nor is its negation.
Inputs: CROSSWORD-TO-D §3.1, §4.2; R185_001; R185_002 (Thm C, Thm D, Prop E, Thm F, Conj G); R162_2601 (O2601.1,
Thm H, Thm Λ̃); R164_401 (Thm R, confirmed in R164_190); R163_1001/R164_190 (Thm O, Prop I = Hamburger);
R166_701 (T1–T6); R166_802 (Thm 1–3); R169_101 (Prop 3, Prop 5); R163_803 (Thm C = BFdisc); R184_001; R184_005
(Prop 4.1); R184_014.

## State

| piece | statement | label |
|---|---|---|
| Lemma 1 | localization: Λ_d∣[1,Y] ⟺ N_d∣[1,Y]; deletion beyond X fixes both on [1,X] | PROVED |
| Lemma 2 | monotonicity and structural stability of deletion (positivity, support, integrality, B_int, multiplicativity) | PROVED |
| Lemma 3 | exact "completeness": Λ_d∗1_ℕ = log·1_ℕ on [1,Y] ⟺ Λ_d = Λ on [1,Y] ⟺ N_d = ⌊·⌋ on [1,Y] | PROVED |
| Obs 4 | in 𝒟, the EF of ζ type with conductor 1 (and polar data of ζ, finite order) already identifies ζ by itself | PROVED (Thm R) |
| Table §2 | classification of the primitives | PROVED row by row (inspection of each definition) |
| Thm U3 | trichotomy for 𝔐_Λ: (i) closed under deletion, (ii) identification, (iii) quantitative class | PROVED as a theorem about 𝔐_Λ (definition §3) |
| Thm U3(iii) | middle branch: (iii-a) BFdisc falsifier; (iii-b) subsystems of ℕ = RH; (iii-c) boundary θ ≤ ⅓ | (iii-a) PROVED for atoms Q alone, CONDITIONAL with ζ's window; (iii-b) PROVED (RH inclusion); (iii-c) OPEN |
| Cor 6 | "U3 holds unless a theorem a priori stronger than RH is proved" | PROVED (exact conditional form in §5) |
| exhaustiveness of 𝔐_Λ | that the primitives of the corpus are exactly the atoms L, D, C, Q | ARGUED (inventory, not a theorem) |

**Verdict.** U3 is **PROVED as a theorem about the class of statements 𝔐_Λ** (defined in §3), with two explicit
residuals: (a) branch (iii-a) uses the BFdisc falsifier, which does not have ζ's window or support in log ℕ, and its
compatibility with window atoms is CONDITIONAL; (b) branch (iii-c), quantitative classes with θ ≤ ⅓ with no support
in log ℕ, is OPEN. Resolving (iii-c) **positively** (rigidity: no discrete system with θ ≤ ⅓ has zeros off the
line) implies RH by R166_701 T6 / R184_001, and is a priori stronger. Hence: **U3 holds unless a theorem a priori
stronger than RH is proved.** No row D label moves.

---

## 0. Framework

**Arithmetic data.** 𝒟 is the class of discrete Beurling systems d: generalized primes 1 < q₁ ≤ q₂ ≤ … with no finite
accumulation point, multiplicities m_q ∈ ℤ_{≥0}, ζ_d(s) = ∏_q (1 − q^{−s})^{−m_q} absolutely convergent for σ > σ_d.
Measures: dN_d (generalized integers, with dN_d({1}) = 1), dΠ_d = Σ m_q Σ_k k^{−1} δ_{q^k}, Λ_d = log·dΠ_d. Internal
identities (valid for every d, with no zeros): dN_d = exp_∗(dΠ_d), log·dN_d = Λ_d ∗ dN_d, μ_d ∗ dN_d = δ₁. ζ ∈ 𝒟 is ℕ.

**Deletion.** For S ⊂ {q : q > X}, d∖S sets m_q = 0 for q ∈ S. A statement P is **closed under deletion beyond X at ζ**
if P(ζ) ⟹ P(ζ∖S) for every S ⊂ ℙ ∩ (X,∞). (This is the hypothesis of R185_002 Thm F; it suffices at ζ, because witness
exclusion is posed with ζ's window.)

**Identification.** P **intrinsically identifies ζ beyond X** if P(d) ∧ (d ≡_X ζ) ⟹ N_d = ⌊·⌋ on [1,∞). P **identifies
ζ with EF** if {d ∈ 𝒟 : P(d) ∧ EF₁(d)} = {ζ}, where EF₁ = EF of ζ with factor π^{−s/2}Γ(s/2), conductor 1, simple poles
at 0 and 1 with residues ±1, finite order.

**Exclusion.** Ex(P) := "no d ∈ 𝒞_P := {d : P(d)} has a zero at σ > ½" (in the sense of continuation that the context
provides), and, within the row D framework, Ex_W(P) := "P together with ζ's window excludes the witness" (R166_802).
Since ζ ∈ 𝒞_P, **Ex(P) ⟹ RH always**; what U3 measures is whether the converse holds (P adds nothing: identification)
or whether Ex(P) is false (falsifier) or strictly stronger.

## 1. Three lemmas

**Lemma 1 (localization). PROVED.** For d, d′ ∈ 𝒟 and Y ≥ 1: Λ_d = Λ_{d′} on [1,Y] ⟺ N_d = N_{d′} on [1,Y]. If S ⊂ (X,∞),
d∖S ≡_X d.

*Proof.* The measures live on [1,∞) and the multiplicative convolution of measures on [1,∞) restricted to [1,Y] only
uses their restrictions to [1,Y]. Thus dN_d∣[1,Y] = exp_∗(dΠ_d∣[1,Y])∣[1,Y]. Conversely, log·dN = Λ ∗ dN and
dN({1}) = 1 give Λ∣[1,Y] by recursion on the order (discrete support): Λ(x) = log x·dN({x}) − Σ_{1<u<x, u∣x} Λ(u)
dN({x/u}) (finite sum). A generalized integer ≤ X only has prime factors ≤ X, so deletion beyond X does not change
N∣[1,X]. ∎

**Lemma 2 (deletion: monotonicity and structure). PROVED.** For S beyond X: 0 ≤ Λ_{d∖S} ≤ Λ_d, 0 ≤ dN_{d∖S} ≤ dN_d
(as measures), Π_{d∖S} ≤ Π_d. If d has support in log ℕ, integrality Λ(p^k) = m_p log p with m_p ∈ ℤ_{≥0}, multiplicative
coefficients c_n ∈ ℤ_{≥0} (B_int, R185_002 Def E), the same holds for d∖S.

*Proof.* dN_{d∖S} = exp_∗(dΠ_{d∖S}) and exp_∗ is monotone over measures ≥ 0. Structurally: ζ_{d∖S} = ζ_d·∏_{q∈S}(1−q^{−s})^{m_q}
is a sub-Euler-product, with coefficients c_n·1[n has no factors in S] (generalizes R185_002 Thm F.1). ∎

**Lemma 3 (exact completeness). PROVED.** For d ∈ 𝒟 and Y ≤ ∞, the following are equivalent, as measures on [1,Y]:
(a) Λ_d ∗ 1_ℕ = log·1_ℕ; (b) Λ_d = Λ; (c) N_d = ⌊·⌋; (d) μ_d = μ; (e) for Y = ∞: ζ_d = ζ.

*Proof.* 1_ℕ = dN_ζ is invertible in the algebra of measures on [1,Y] with atom 1 at 1 (inverse μ). (a) ⟹ Λ_d =
(log·1_ℕ) ∗ μ = Λ on [1,Y]. (b) ⟺ (c) is Lemma 1 with d′ = ζ. (c) ⟺ (d): μ_d = dN_d^{∗−1}. (e) is (c) with Y = ∞ plus
the Mellin transform. This is the measure version of R169_101 Prop 3/5 (Eratosthenes window→tail). ∎

**Obs 4 (EF already identifies in 𝒟). PROVED** (by R164_401 Thm R, confirmed in R164_190). Every d ∈ 𝒟 satisfies
hypotheses (a) and (b) of Thm R: N_d = δ₁ = N_ζ on [1, min(q₁,2)) and N_d ≥ 0 everywhere. Hence EF₁(d) ⟹ d = ζ.

*Consequence.* The notion "P identifies ζ with EF" from the goal is **vacuous in 𝒟**: every P true at ζ satisfies it.
That is why the theorem is formulated with **intrinsic** identification (without EF), and EF is added only at the
end as the Thm O/Hamburger/Thm R stage of the W-identification wall. This reinforces the conclusion: in 𝒟, EF is the
external datum that, added to anything, turns the question into literal RH.

## 2. Table of primitives (true at ζ, provable without zeros)

Type: **L** = local (depends on Λ∣[1,Y], Y finite); **D** = closed under deletion (upper bound with weights ≥ 0, or
structural condition stable by Lemma 2, or internal identity valid throughout 𝒟); **C** = completeness at infinity
(Lemma 3 with Y = ∞ or on [X,∞)); **Q** = quantitative at infinity (lower bound or asymptotic with error).

| primitive | type | closed under deletion? | identifies (intrinsic)? | identifies with EF₁? | proof |
|---|---|---|---|---|---|
| Λ ≥ 0 | D | yes | no | yes (vacuous, Obs 4) | Lemma 2 |
| support in {log p^k} (log ℕ) | D | yes | no | yes (Hamburger/Prop I) | Lemma 2 |
| integrality Λ(p^k) = log p (m_p ∈ {0,1}) | D | yes | no | yes | Lemma 2 |
| B_int (c_n ∈ ℤ_{≥0}, multiplicative) | D | yes | no | yes | R185_002 Thm F |
| multiplicativity of c_n | D | yes | no | yes | Lemma 2 |
| internal Selberg Λ_d log + Λ_d∗Λ_d = μ_d∗log² | D (internal identity) | yes (holds in all 𝒟) | no | yes | formal identity |
| internal Möbius μ_d ∗ N_d = δ₁ | D | yes | no | yes | same |
| upper Chebyshev ψ_d(x) ≤ Cx | D | yes | no | yes | Lemma 2 |
| upper sieves S1–S3 (R167_102/103) | D | yes (upper bounds with weights ≥ 0) | no | yes | Lemma 2; R185_002 Thm C(iii) |
| window data Λ∣[1,X] | L | yes, beyond X | no | yes | Lemma 1 |
| Λ ∗ 1 = log on [1,Y], Y < ∞ | L | yes, beyond Y | only on [1,Y] | yes | Lemma 3 |
| **Λ ∗ 1_ℕ = log on all of ℕ** | C | **no** | **yes** | yes | Lemma 3 |
| **Euler product = ζ exactly** | C | **no** | **yes** | yes | Lemma 3(e) |
| **Möbius with the μ of ℕ: μ_d = μ** | C | **no** | **yes** | yes | Lemma 3(d) |
| **N(x) = ⌊x⌋ for x ≥ X** | C | **no** | **yes** (with d ≡_X ζ) | yes | Lemma 3 |
| Selberg with the μ of ℕ (Λ log + Λ∗Λ = μ∗log² with ℕ's μ) | C | no | yes | yes | equivalent to Lemma 3(d) given Λ_d |
| lower Chebyshev ψ_d(x) ≥ cx (x ≥ X) | Q | no (S = ℙ∩(X,∞) violates it) | no | yes | — |
| PNT with error, N_d = Ax + O(x^θ) | Q | no | no (θ > 0: R184_005; θ = 0: OPEN, C1) | yes | R184_005 Prop 4.1 |
| EF₁ (via theta/Poisson) | datum external to the window | no (ζ∖S violates EF) | — | it is EF itself | Obs 4 |
| Hamburger uniqueness / Thm O / Thm R | identification metatheorem | — | — | yes | R164_401 |

Reading: **no** primitive is both not closed under deletion and non-C except those of type **Q** (lower counting and
asymptotics). That is the "middle zone" of the goal.

## 3. The class 𝔐_Λ

**Def 5.** An atom is a statement in one of the four classes L, D, C, Q of §2, in the following sense:
- L: P(d) depends only on the ≡_Y class of d for some Y < ∞ (includes any nonlinear operation on Λ∣[1,Y] and its
  convolutions, because by Lemma 1 these only use Λ∣[1,Y]);
- D: the set {d : P(d)} is stable under d ↦ d∖S for every S beyond some X_P (includes upper bounds Σ c_n Λ_d(n)
  ≤ U, c ≥ 0, any increasing functional bounded above, and the structural conditions of Lemma 2);
- C: P(d) ∧ (d ≡_X ζ) ⟹ N_d = ⌊·⌋ on [X, ∞) for some X (by Lemma 3 covers Λ∗1_ℕ = log, Euler = ζ, μ_d = μ);
- Q_θ: P is a consequence of "N_d(x) = A_d x + O(x^θ)" or is a lower counting bound ψ_d(x) ≥ cx on [X,∞)
  (the threshold θ ∈ [0,1) is part of the atom).

𝔐_Λ := closure of the true-with-no-zeros atoms under ∧ and ∨. (Nonlinear zero-free operations fall within each atom;
the goal asked for closure under them: Def 5 achieves this because types L and D are classes of *sets* of data, not
of formulas, and are stable under any operation preserving dependence on [1,Y] or stability under deletion.)

Normal form: P = ∨_j K_j, K_j = conjunction of atoms. Type of K: (i) only L and D atoms; (ii) some C atom; (iii) no
C and some Q.

**Prop 0 (abstract dichotomy, tautological). PROVED.** For *any* statement P with P(ζ): either there exists X with
{ζ∖S}_{S>X} ⊂ 𝒞_P, or for every X there exists S > X with ¬P(ζ∖S). (This is only recorded to make clear that the
content of U3 is not in the partition but in the description of the second branch.)

## 4. Theorem U3

**Thm U3 (deletion or identification, in 𝔐_Λ). PROVED.** Let P ∈ 𝔐_Λ be true at ζ, in normal form ∨_j K_j, and let
J₀ ≠ ∅ be the set of j with K_j(ζ). Then exactly one of the following holds:

**(i) Deletion.** Some K_j with j ∈ J₀ is of type (i). Then there exists X such that ζ∖S ∈ 𝒞_P for every S ⊂ ℙ ∩ (X,∞).
In particular 𝒞_P contains the family of sub-sums of R185_002 Thm F (including S = ℙ∩(X,∞)), and by Thm F + R166_802
Thm 1–2 **P together with ζ's window does not exclude the witness except via a single K with U_K < 0, which is E1.**
NO-GO (class).

**(ii) Identification.** All K_j, j ∈ J₀, are of type (ii) or (iii), and at least one with j ∈ J₀ is of type (ii).
Then 𝒞_{K_j} ∩ {d ≡_X ζ} = {ζ} for that j, and the contribution of K_j to Ex(P) is exactly RH: Ex(K_j ∧ window) ⟺
"ζ has no zeros at σ > ½". The rest of 𝒞_P can only make Ex(P) stronger. **W-identification**; with EF₁ it is literally
Thm O / Thm R.

**(iii) Quantitative class.** All K_j, j ∈ J₀, are of type (iii). Let θ_P be the minimum threshold among the Q atoms in
some K_j, j ∈ J₀. Then:
- **(iii-a) falsifier, θ_P > ⅓, with no support-in-log-ℕ atom:** 𝒞_{Q_{θ_P}} contains a discrete system from R163_803
  Thm C (BFdisc) with infinitely many zeros at σ = (1+θ)/2 > ½. If, moreover, some member of that family satisfies the
  L/D atoms of K_j, Ex(P) is **false**: NO-GO by class falsifier. For θ_P > ½ the same holds via DMV/Broucke Thm 6.3
  (CITED, R184_001 item 8).
- **(iii-b) subsystems of ℕ:** K_j contains the D atoms "support in log ℕ" and "integrality". Then 𝒞_{K_j} ⊂
  {ζ_{𝒫′} : 𝒫′ ⊂ ℙ} (Lemma 2 and m_p ∈ {0,1}), ζ_{𝒫′} = ζ·∏_{p∈ℙ∖𝒫′}(1 − p^{−s}). If Σ_{p∉𝒫′} p^{−1/2} < ∞, the
  second factor is holomorphic and zero-free for σ > 0 except at σ = 0, so the zeros of ζ_{𝒫′} at σ > ½ are those of ζ.
  This subfamily exists within every Q_θ with θ > 0 (R184_005 Prop 4.1: p_k ≥ 2^{2^k}, error O(log x)) and is closed
  under ζ's window if the p_k > X. Hence Ex(K_j) restricted to it ⟺ RH: **the exclusion is RH unchanged**
  (identification by zeros, not by integers). Members with Σ_{p∉𝒫′} p^{−1/2} = ∞ give GRH-type statements about
  sub-products and are a priori stronger.
- **(iii-c) boundary, θ_P ≤ ⅓ with no support in log ℕ:** there is no known falsifier (BFdisc stops at ⅓) nor proven
  rigidity. **OPEN** (O184.001a/b). Any positive answer ("no discrete system in 𝒞_{K_j} has zeros at σ > ½") contains
  the case ζ, hence implies RH (R166_701 T6), and since it quantifies over other systems it is **a priori stronger**
  than RH (R184_001).

*Proof.* (i): by definition of L and D there is X_j with {ζ∖S}_{S>X_j} ⊂ 𝒞_{K_j} (L with Y ≤ X_j by Lemma 1; D by
definition; the conjunction of stable sets is stable). Since 𝒞_{K_j} ⊂ 𝒞_P, Thm F of R185_002 applies exactly as
written (its proof only uses that the family {ζ∖S} lies within the class and shares the window) together with R166_802
Thm 1–2.
(ii): by Def 5(C), K_j(d) ∧ d ≡_X ζ ⟹ N_d = ⌊·⌋ on [1,∞) (Lemma 1 on [1,X], the atom on [X,∞)), hence d = ζ by Lemma
3(e). Exclusion over {ζ} is RH. (iii-a): R163_803 Thm C (PROVED, R163_891) gives, for each θ ∈ (⅓,½), a d with
N_d = ρx + O(x^{θ+ε}) and zeros at (1+θ)/2; by definition of Q_θ, d ⊨ Q_{θ+ε}. (iii-b): a convergent Euler product
computation; R184_005 Prop 4.1 gives the family (PROVED). (iii-c): R184_001 items 8–9 and R166_701 T6. The
exhaustiveness of the three cases is the partition by types of J₀. ∎

**What the theorem says about O2601.1.** O2601.1 asks for "a property of the exact values of Λ, used nonlinearly
(Euler), that forbids E". By Thm U3: if the property is structural (B_int, integrality, multiplicativity) it is D and
falls into (i) (this is Thm F); if it uses the completeness of ℕ at infinity it is C and falls into (ii); if it uses
it with error it is Q and falls into (iii). R185_002's Conj G ("everything not closed under deletion factors through
1∗Λ = log") is **PROVED within 𝔐_Λ** in the form: not closed under deletion ⟹ type C (goes through Λ∗1_ℕ = log,
Lemma 3) or type Q (lower counting, R185_002 Thm D). Outside 𝔐_Λ it remains ARGUED.

## 5. Honest conclusion

**Cor 6. PROVED.** For every P ∈ 𝔐_Λ true at ζ, at least one of the following holds:
(1) P does not exclude the witness with ζ's window except through E1 (branch i);
(2) exclusion by P is equivalent to RH (branches ii and iii-b, in its subfamily);
(3) P is refuted by a class falsifier (branch iii-a, with window compatibility as a hypothesis);
(4) P is at the boundary (iii-c), and exclusion by P is a statement implying RH and a priori stronger.

Barrier form: **U3 holds in 𝔐_Λ unless a theorem a priori stronger than RH is proved** (rigidity of discrete systems
with θ ≤ ⅓). Label of U3: **PROVED relative to Def 5**, CONDITIONAL at (iii-a) on window/falsifier compatibility,
OPEN only at the boundary (iii-c), whose positive closure is stronger than RH. The claim that 𝔐_Λ exhausts the
corpus's methods is ARGUED (it is Table §2 plus the I1–I18 inventory).

## For the audit

1. **Obs 4 empties the "with EF" version of the goal.** Check that every d ∈ 𝒟 satisfies N_d = N_ζ on [1, min(q₁,2))
   with min(q₁,2) > 1 (yes: q₁ > 1 and there are no generalized integers in (1,q₁)) and N_d ≥ 0 off ℕ: then Thm R
   applies. If accepted, "identifies with EF" does not discriminate between statements and the only useful notion is
   the intrinsic one.
2. **Def 5 is semantic.** L and D are defined by properties of the sets 𝒞_P, not by syntax. This makes the theorem
   rigorous but shifts the work to the Table: a "new" statement only escapes if it is neither L, D, C nor Q. That the
   corpus has no atoms outside these four types is inventory (ARGUED).
3. **Branch (iii-a).** BFdisc lives in {n^{1/(1−θ)}}, not in log ℕ, and does not have ζ's window. If K_j contains ζ's
   window (type L), the falsifier does not apply as is: one must glue ζ's window to the BFdisc tail and check that
   (i)–(ii) of R163_803 Thm C survive. This is not done: CONDITIONAL.
4. **Branch (iii-b).** The argument only covers the 𝒫′ with Σ_{p∉𝒫′} p^{−1/2} < ∞. Nothing is asserted about thick
   𝒫′ (e.g. primes ≡ 1 mod 4, whose ζ_{𝒫′} is (ζL)^{1/2}·H, with branch points only if GRH fails). This suffices for
   "Ex(K_j) ⟹ RH and the fine subfamily adds nothing".
5. **∨ in normal form.** Disjuncts false at ζ only enlarge 𝒞_P; they never help exclude. Check that branch (i) only
   uses a disjunct true at ζ.
6. **Selberg/Möbius.** The internal version (μ_d, holds throughout 𝒟, type D) and the version with ℕ's μ (type C) are
   distinguished. A proof using "Selberg" must declare which; confusing the two is the usual source of circularity.
7. **Zero exclusion vs witness exclusion.** (i) uses Ex_W (R166_802 framework); (ii)–(iii) use Ex over zeros. The two
   connect via R166_802 Thm 2 (transfer), PROVED in the record; not reproved here.

## For Paper 46/48

- **Paper 48 §sec:walls (W-identification):** add Lemma 3 (exact completeness in measures) and Obs 4 (in the positive
  discrete class, EF₁ alone identifies ζ by Thm R). Propose Thm U3 as `thm:deletion-or-identification`, with Def 5
  explicit and branch (iii) as a remark with the three sub-cases and their labels.
- **Paper 48 Problem 6 (BF^disc_θ):** cite Cor 6: the boundary θ ≤ ⅓ is exactly U3's residual; its positive resolution
  implies RH and is a priori stronger.
- **Paper 46 §7 (alongside Thm finZ and Thm F):** one sentence: "structural conditions on Λ are closed under
  deletion; those that are not go through Λ∗1_ℕ = log (identification) or through a lower count (exponent)".
- Vocabulary: do not write "U3 proved" without "relative to 𝔐_Λ (Def 5)"; do not write "absolute barrier".

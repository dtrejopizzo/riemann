# CPOS_CLASS_001 — C-pos class theorem: no imported positivity with a comb-uniform construction (phase 201)

NO-GO / NUMERICAL. This is a method theorem (what class of proofs cannot work and what remains), not a closure of the program.

## Summary (≤250 words)

We formalize the class of arguments that phase 201 went through family by family: a classical positivity theorem 𝒯
("H(O) ⇒ P(O) ≥ 0") applied to an object O_{g,a} built from the test g and the comb a by a recipe 𝒞 **uniform in a**,
together with a bridge 𝔞_T^a(g) ≥ Φ(P(O_{g,a})). C-pos class theorem: (i) if the bridge and H hold throughout theory 𝔗₁
(resp. 𝔗₂), the DH falsifier (T = 9/5, rem:FDH) (resp. Epstein x²+5y², T ≥ 1.59, lem:shape-epstein) gives a
contradiction — PROVED, it is lem:transfer plus the soundness correction of DH_TRANSFER; (ii) if the bridge is a
theorem of 𝔗₁, then H(O_{g⋆,DH}) is FALSE at the certified witness: H is the only gate of the sign — PROVED; (iii) the
gate H is (γ) blind to a ⇒ impossible (PROVED), (α) affine in a ⇒ either its margin on ζ is ≤ C_H·λ_A(T) (as exact as
𝔞, branch 2) or the family (1+δ)Λ violates it (Φ.14; PROVED given κ_T ≠ 0, CONDITIONAL in general), on top of C-E′ by
convexity; or (β) non-linear in a, in which case verifying H(O_{g,ζ}) is at least as strong as 𝔞_T^ζ(g) ≥ 0 on every
test where it is used (branch 2, REF-D) unless the verification uses a non-uniform input — ARGUED as a trichotomy.
Corollary: phase 201 is closed as a **strategy** by this theorem, not by exhausting the inventory; the escapable
hypotheses are listed (§4). What remains: constructions 𝒞 that are non-uniform in a. Linear ones (Λ∗1 = log), group
ones (Euler, G1), completeness ones (C-data) and window ones (C-emb (a)) are already closed; the only infinite
non-uniformity registered is the exterior datum with exact values (inequality (★★) of AUDIT_L_SHARP_16 §6). Whether
it is the only one: ARGUED/OPEN.

## Corpus check

- Index `05-meta-and-planning/ROUTES-TRIED-INDEX/`: C-pos (phase 201, FAMILIES_C), Φ200, Φ.14, C-E′, G1, C-MvN, C-emb,
  R-F1, R-Q6 and DH_TRANSFER already appear as restrictions. This memo does **not** propose a new route: it unifies
  C-pos (identity version, PROVED) and C-pos (ii) (ARGUED) into a class statement and crosses it with lem:transfer and
  thm:shape. The new reason relative to C-pos: it moves from "identity with an intrinsically positive invariant" to
  "hypothesis + monotone bridge," which is the actual logical form of the uses of Schrödinger, Kreĭn, Verblunsky,
  Bochner, Lévy (FAMILIES_C §4.2).
- Master grid and crossword: the row "sign must enter non-uniformly" matches thm:shape(C) and restriction 5 of
  AUDIT_L_SHARP_16 §6. Nothing is retried.

## 1. Framework

**Theories.** 𝔗₁ = degree-1 theory of DH_TRANSFER §1.2: triples (L, θ, r), FE with (ε, δ, q), bounded real
coefficients, order 1, pole with residue r ≥ 0, no multiplicativity. ζ ∈ 𝔗₁, F_DH ∈ 𝔗₁ (δ = 1, q = 5, r = 0). 𝔗₂ = the
degree-2 analogue (Γ_ℝ(s)Γ_ℝ(s+1)); ζ·L(χ₋₂₀), Ξ_Q ∈ 𝔗₂. By Φ.12 (PROVED) the window form is additive under
product, so a claim about 𝔞^ζ has a shadow in 𝔗₂. We also use the space of **combs** from def:shape-obj: the
archimedean part m fixed and the weight vector (v_n)_{n<N} free; this is where cΛ, a_P, Λn^{−α} live (they are not
L-functions).

**Data.** g ∈ P_T (A = B = 0); 𝔞_T^a(g) the window form of datum a (archimedean + comb; zero pole in P_T).
λ_A(T; a) = inf 𝔞_T^a over the unit sphere of P_T.

**Certified falsifiers.**
- (F-DH) PROVED (rem:FDH, CERT_DH_001): ∃g_DH ∈ P_{9/5}, 𝔞^{DH}_{9/5}(g_DH) < 0; propagates to T ≥ 9/5 (lem:monoT).
- (F-Ep) PROVED (lem:shape-epstein, LEMMA_E_EPSTEIN): 𝔞^{Q}_T < 0 on P_T for every T ≥ 1.59 (includes T = 8/5).
- (F-cΛ) Φ.14: λ_A(T; cΛ) ≤ λ_A(T; Λ) − (c−1)⟨Λ, w_T⟩ exactly (lem:degen). Negative for the right sign and size of
  c−1 if κ_T := ⟨Λ, w_T⟩ ≠ 0: PROVED under that hypothesis, CONDITIONAL without it (thm:shape (A′), O₄^ε).
- (F-a_P) 𝔞^{a_P} = 𝔞^ζ + Σ_p 𝔠_p (Lemma B.1, SPEC_007); witnesses in P_T (Theorem O3, R11_2): per the record,
  numerical except for the explicit certificates of MAP_200 H39. Here they are used only as illustration; they do
  not carry any PROVED part.

**Definition (uniform imported positivity).** An *imported positivity* is a quintuple 𝔓 = (𝒞, 𝒪, H, P, Φ):
- 𝒞: (g, a) ↦ O_{g,a} ∈ 𝒪, *uniform in a*: a single formula, defined for every a in a class 𝒜₀ ⊇ 𝔗₁ ∪ 𝔗₂ (or ⊇ the
  line {cΛ}), in which a enters only as a parameter (no properties of a are used beyond the axioms of the theory);
- 𝒯: theorem "H(O) ⇒ P(O) ≥ 0" for O ∈ 𝒪 (Schrödinger with no bound states, Kreĭn, Verblunsky |α_n| < 1, Bochner,
  Beurling–Deny, Pick, …);
- Φ: ℝ → ℝ non-decreasing with Φ(x) ≥ 0 for x ≥ 0;
- **bridge** (B_𝒜): 𝔞_T^a(g) ≥ Φ(P(O_{g,a})) for every g ∈ P_T and every a ∈ 𝒜, with ζ ∈ 𝒜 ⊆ 𝒜₀.
The *deduction* is: H(O_{g,ζ}) ∀g ⇒ P ≥ 0 ⇒ Φ(P) ≥ 0 ⇒ 𝔞_T^ζ(g) ≥ 0 ∀g.

Remark: the identity version of C-pos is the case Φ = id, (B) with equality, H ≡ true.

## 2. C-pos class theorem

**Theorem.** Let 𝔓 be a uniform imported positivity and T ≥ 9/5 (resp. T ≥ 1.59 for 𝔗₂).

**(i) [PROVED]** (B_𝒜) with 𝒜 ∋ F_DH and H(O_{g_DH, DH}) cannot both hold. The same with Ξ_Q in 𝔗₂ and with (1+δ)Λ
if κ_T ≠ 0. In particular, if (B) holds uniformly on 𝔗₁ ∪ 𝔗₂, then H is false at the falsifiers; and if H holds for
every a (or every a in 𝒜), then 𝒜 excludes the falsifiers: 𝒜 ⊊ 𝔗₁.

*Proof.* With a = F_DH and g = g_DH: H ⇒ P(O) ≥ 0 (by 𝒯) ⇒ Φ(P) ≥ 0 ⇒ 𝔞^{DH}_{9/5}(g_DH) ≥ 0 by (B), against
(F-DH). This is lem:transfer with 𝔛 = {window forms of 𝒜}, 𝖯 = "H(O_{·,a}) and (B_a)", q₀ = 𝔞^ζ, q₁ = 𝔞^{DH}. Same
with (F-Ep) and, under κ_T ≠ 0, with (F-cΛ). ∎

**(ii) [PROVED]** If the bridge (B) is proved using only theorems of 𝔗₁ (in the sense of DH_TRANSFER Thm 3.1: each
premise is a theorem of 𝔗₁, possibly with constants depending on (θ, r, C)), then (B) holds for F_DH and by (i)
H(O_{g_DH, DH}) is FALSE. Hence, in every deduction of this type, H is a property of the object O_{g,ζ} that (a)
holds at ζ (if the deduction is correct) and (b) fails at O_{g_DH, DH}. Likewise in 𝔗₂ with Ξ_Q. The hypothesis H is
the *only* gate of the sign; P, Φ, 𝒯 and (B) are blind to it.

*Proof.* Soundness: F_DH is a model of 𝔗₁ (DH_TRANSFER §1.1), so every theorem of 𝔗₁ holds at F_DH; apply (i). ∎

Note. If (B) uses premises outside 𝔗₁ (Euler, a_n ≡ 1), the gate may be in (B) rather than H; that case is exactly
"non-uniform construction/bridge" and is treated in §5. It is the first escapable hypothesis (§4, (h1)).

**(iii) Trichotomy of the gate H.** Fix g, let χ_g(a) ∈ {V, F} be the truth value of H(O_{g,a}). By (ii),
χ_{g_DH}(ζ) = V and χ_{g_DH}(DH) = F. There are three exhaustive cases according to how H depends on a.

**(γ) H does not depend on a [PROVED, branch 4].** If χ_g(a) = χ_g(a′) for all a, a′ ∈ 𝒜₀, then
χ_{g_DH}(DH) = χ_{g_DH}(ζ) = V, contradicting (ii). If H depends only on g (for example a shape condition on the
test), then either it holds at g_DH and the deduction is false, or it fails at g_DH and the deduction does not cover
P_T: the DH negative test is left out, and by lem:monoT/continuity of λ_A the excluded set contains an open set of
tests; the conclusion ∀g ∈ P_T is not obtained. So H blind to a is blind to ζ (branch 4 of Φ200). ∎

**(α) H affine in a [PROVED under κ_T ≠ 0 / CONDITIONAL in general; branch 1 or 2].** Suppose
H(O_{g,a}) ⟺ ℓ_g(a) ≥ 0 with a ↦ ℓ_g(a) affine over the space of combs (typical case: H is "the spectral measure of O
is ≥ 0," and O depends linearly on a, as in Bochner, linearized Verblunsky, Lévy, first-order Riccati — FAMILIES_C
§4.5).

*Claim α1 (convexity ⇒ C-E′, PROVED).* {a : ℓ_g(a) ≥ 0 ∀g} is convex. If it contains Λ_K and Λ_ψ (each with its
verified gate) and is stable under adding a Λ_cosh with ℓ ≥ 0, it contains Λ_Q = ½(Λ_K + Λ_ψ) + Λ_cosh (LEMMA_E,
H26) and (B) would give 𝔞^Q ≥ 0, against (F-Ep). Hence every affine gate must *fail* at one of the Euler factors or
be destroyed by the cosh term: it is not "positivity stable under averages of log-derivatives of Euler factors"
(C-E′).

*Claim α2 (transversality ⇒ exact margin, PROVED with hypothesis).* Let F⋆ be a real minimizer of 𝔞_T^Λ on P_T,
w_T its weight vector (lem:degen), κ_T = ⟨Λ, w_T⟩. Along a_δ = (1+δ)Λ, both 𝔞^{a_δ}(F⋆) = λ_A − δκ_T and
ℓ_{F⋆}(a_δ) = ℓ_{F⋆}(Λ) + δ ℓ′ (ℓ′ := linear part of ℓ in direction Λ) are affine. If κ_T ≠ 0, (B) at a_δ plus 𝒯
require: for every δ with ℓ_{F⋆}(a_δ) ≥ 0, λ_A − δκ_T ≥ 0. Taking δ = λ_A/κ_T + ε (sign of κ_T) gives
ℓ_{F⋆}(Λ) + δℓ′ < 0, that is

  ℓ_{F⋆}(Λ) ≤ |ℓ′|·λ_A(T;Λ)/|κ_T|,

unless (B) does not hold on the line {cΛ} (then 𝒜 ⊉ {cΛ}: the restriction a ∈ 𝒜 must exclude the multiples, i.e. the
deduction uses the exact normalization a_n ≡ 1, which is not uniform). With λ_A ≤ 4·10⁹ T e^{−15.449T} (thm:shape(B),
PROVED, CITED inputs) the affine gate has at ζ an exponentially small margin in the direction of the comb: it is a
reformulation of 𝔞^ζ(F⋆) ≥ 0 with the same precision (branch 2, REF-D). The same for any direction a′ with
⟨a′, w_T⟩ ≠ 0 (Φ.14). Without κ_T ≠ 0 the statement is CONDITIONAL (AUDIT_197 (e)).

Conclusion (α): an affine gate is either comb-generic (the affine family violates it: branch 1) or as fine as the
objective at the minimizer (branch 2). ∎

**(β) H non-linear in a [ARGUED; branch 2 or non-uniform gate].** Let H be arbitrary (not affine), with χ(ζ) = V and
χ(DH) = F. The deduction needs to *verify* H(O_{g,ζ}) for all g ∈ P_T. Two subcases:
- (β1) The verification is itself a theorem of 𝔗₁ (or of uniform 𝒜₀). Then it holds for DH: contradiction with (ii).
  PROVED (soundness).
- (β2) The verification uses an input outside 𝔗₁. That input, applied to O_{g,ζ}, implies 𝔞^ζ_T(g) ≥ 0 via 𝒯 + (B):
  H(O_{g,ζ}) ∀g is a claim *at least as strong* as L′♯ on the window (REF-D in disguise or stronger), in the precise
  sense: H ∀g ⊢ 𝔞_T^ζ ≥ 0 on P_T with a uniform proof. Moreover, at the minimizer, (B) with monotone Φ gives
  Φ(P(O_{F⋆,ζ})) ≤ λ_A, so the "value" of the gate is confined to precision e^{−15.449T} (thm:shape(B′)).
The ARGUED part is the classification: that there is no non-linear H whose verification for ζ is *easier* than the
objective while being logically stronger. Logically this is not excluded (a stronger statement can be more
tractable); what is excluded (PROVED) is that the ease comes from 𝔗₁. All the difficulty is shifted to the
non-uniform input of (β2).

**Conclusion of the theorem.** No imported positivity with construction 𝒞 and bridge (B) uniform in the comb can
give the sign of 𝔞^ζ: the sign enters (PROVED) at a step that is not a theorem of 𝔗₁ — the verification of H for ζ
or a non-uniform bridge — and (ARGUED) that step is, at best, a reformulation of equal or greater strength unless it
uses the exact multiplicativity of Λ (a_n ≡ 1, Euler, conductor 1) **inside the construction**. Overall label:
(i), (ii), (γ) PROVED; (α) PROVED under κ_T ≠ 0, CONDITIONAL without it; (β) ARGUED; trichotomy as a class ARGUED.

Verification against P47: (i) is a literal instance of lem:transfer (𝔛 = window forms on P_T, closed semi-bounded;
q₁ with negative background explicitly given by rem:FDH / lem:shape-epstein). (ii)+(iii) is thm:shape(C) specialized
to the class "imported positivity": a deduction whose set of properties is invariant under O₁₀ (removal of Euler,
lem:shape-epstein) or under the DH substitution cannot prove eq:target. (α2) is thm:shape(A′)/(B′) with O₄^ε
(κ_T ≠ 0 conditional, matches). No new normalization is used.

## 3. Corollary: phase 201 closed as a strategy

**Corollary (phase 201).** Every family in FAMILIES_A/B/C whose proposed use has the form "classical positivity
theorem + object built uniformly from (g, a)" falls under (i)–(iii): the gate H is blind (γ), affine (α: Bochner,
Lévy/Beurling–Deny, linear Verblunsky, weak counting S-1), or non-linear with a verification that is REF-D (β:
"no bound states," GL/Kreĭn solvability, Riccati/SUSY, |α_n| < 1). Hence the closure of phase 201 is a **class
theorem** (PROVED in (i), (ii), (γ); ARGUED in the trichotomy), not the exhaustion of an inventory: no new family of
this format can give the sign, whether listed or not.

**Escapable hypotheses (honesty).** The corollary does not cover:
- (h1) **Non-uniform construction or bridge**: 𝒞 or (B) use properties of Λ that are not axioms of 𝔗₁/𝔗₂ (Euler,
  a_n ≡ 1, conductor 1, residue 1 together). This is the main exit; §5.
- (h2) **Non-monotone Φ or a bridge with undefined error**: 𝔞^a ≥ Ψ − E(a) with E not bounded by Φ(P). C-pos (ii)
  says that E is linear in a (branch 1) or operator positivity on the window (branch 2): ARGUED, not PROVED.
- (h3) **Class of combs**: (α2) uses the line {cΛ} outside 𝔗₁; if 𝒜 is restricted to genuine L-functions, only the
  discrete falsifiers DH, Ξ_Q remain and transversality does not apply. An affine gate that holds on 𝔗₁ but is not
  stable on the line cΛ is not excluded by (α2), though it is by (i) if it holds for DH.
- (h4) **Non-positive H**: integrality, rationality, or a group condition. Integrality of coefficients is not
  uniform on 𝔗₁ (DH has a_n ∈ {±1, ±κ, 0}) and is therefore a case of (h1); C-MvN and G1 close it when it reads only
  (ℕ^×, ·).
- (h5) **Registered gaps of Φ200**: Ξ2 (non-standard internal normalization, Loeb, OPEN), Ξ1 (categorical dimension
  sensitive to Cl), rows 16–17 of SPEC_006 (Lorscheid, arithmetic Monge–Ampère) with no concrete object.
- (h6) **Windows**: (i) is PROVED only for T ≥ 9/5 (DH) or T ≥ 1.59 (Epstein). Below that there is no certified
  falsifier in 𝔗₁; there the theorem is vacuous (and the sign of ζ is known up to ½log15 by certificates).

## 4. What "construction non-uniform in a" means

**Definition.** 𝒞 is non-uniform if its definition (not just its analysis) uses a property of a that fails at some
certified falsifier. Review of the candidates, with the index restriction that closes them:

1. **Λ∗1 = log** inside O (Möbius/Dirichlet over the comb). It is linear in Λ: R-F1 (PROVED, "every A_μ on the
   exterior form sees Λ only via Λ∗1 = log") and Beurling survives (G1). Falls under (α).
2. **Euler product as group structure** (free ℕ^×, plethysm, Hopf, Schur): G1 (PROVED) — Beurling shares the free
   monoid. Falls under branch 1.
3. **Completeness ⟨𝒫⟩ = ℕ, h = 1**: C-data/C-𝔖 — equality between data (branch 5) or signless discontinuous weight.
4. **Isomorphism class of (ℚ, ℚ^×)** (Murray–von Neumann dimensions, group traces): C-MvN (PROVED), L(G) = R
   common to Beurling, a_P, K.
5. **The embedding log: ℚ^× → ℝ with its exact numerical values.** This is the only non-uniformity that is neither
   a datum, nor linear, nor an abstract group (MAP_200 O4). Inside the window it is **finite**: by lem:spec-collapse
   𝔞_T depends only on (Λ(n))_{n<N}, and C-emb (a) / P-fin / Thm 3′ turn any functional into one analytic in
   finitely many values — closed. **Outside the window** (exterior, n ≥ N = μ) the information is infinite:
   c_N = −μ(N) on [μ, 2μ), gauge 𝒢_T, quotient 𝒬_μ, prolate tail. R-Q6 (PROVED): the descent of 𝒲 to the quotient
   by the gauge already uses exact Λ; a_P, cΛ, DH already fail there.

Question from the mandate: is the exterior the only available infinite non-uniformity? **ARGUED, not PROVED.** In
favor: (1)–(4) are closed by theorems, (5)-window is finite by lem:spec-collapse, and the exterior is the only
component of the datum of ζ that is (a) infinite, (b) not an invariant of the abstract pair, (c) already discarded
in the quotient for the falsifiers (R-Q6). Against / gaps: Ξ2 (non-standard) and Ξ1 (Cl-sensitive) have not been
reduced to the exterior; and restriction 28 of AUDIT_L_SHARP_16 records that the Möbius gap 2 ≤ N < μ is shared by
a_P, so not all of the exterior is non-uniform: only its coupling with the archimedean leak-scale tail is.

## 5. What remains: the table from phase 199

**Exact statement (AUDIT_L_SHARP_16 §6, "single remaining object," OPEN).** On admissible data in the window
a = ½log μ, with Ψ̌ = Zr written exactly as (FF.1) = comb of translations Σ_{N≥μ} c_N N^{−1/2} τ_{log N} g + gauge
mirror Φ_{φ₀}(−·) (polar ≡ 0):

  𝒲_ext[Ψ̌] ≥ κ μ^{−A} dist²(r, 𝒢̄)   (L′♯ ⟺ (★★)),

where (i) the m = 1 Langer/prolate tail is controlled (Theorem C, CC_001, asymptotic; NUMERICAL below N ≈ 130), and
(ii) the remaining content is the **non-local content of Möbius cells at the leak scale** — the comb-vs-gauge
remainder, gauge-dependent as a function and canonical only as a coset mod 𝒢̄ — whose coupling 𝒲_ext with (i) is the
(1, n) resonance (−0.48/−0.30/−0.20 W* at μ = 15, NUMERICAL). Equivalent operator form (AUDIT_15): Schur plank with
exact resolvent and uniform leak margin (0.612 at μ = 15, J = 50). There is no estimate of (ii) beyond the numerics
at μ = 15. In BRIDGE_001 the same table appears as (P0a)/(L_ext): 𝒲_ext[Zr_f] ≥ κμ^{−A}dist²(r_f, 𝒢̄) for f
admissible in the kernel, with the base identity I1: W_T(Ef) = 𝒲_ext[Zr_f] (PROVED).

**What distinguishes it from everything closed by this theorem.**
- Its construction 𝒞 (the operator Z, the gauge 𝒢_T, the decomposition FF.1) **is not uniform in a**: it uses the
  exact c_N = −μ(N), and R-Q6 (PROVED) says that cΛ, a_P and DH already fail upon descending to the quotient. It is
  not an imported positivity in the sense of §1: there is no classical theorem 𝒯 with hypothesis H; the "P ≥ 0" is
  requested directly on a non-uniform object.
- It is not linear in the comb in the sense of (α): the inequality is quadratic in the exterior datum r and the
  weight 𝔴_μ(ω) involves H(ω) = Σ_{n≤ω}1/n with exact values.
- It is not finite (lem:spec-collapse does not apply outside the window) nor an invariant of (ℚ, ℚ^×) (C-MvN): it
  depends on log N ∈ ℝ.
- Restriction 5 of AUDIT_16: it must use a_n ≡ 1, residue 1, conductor Γ_ℝ 1 and aliasing at n ≈ λ/u **together**
  and fail for cΛ, a_P, Beurling — exactly the "non-uniformity" this theorem requires.
- Restriction 28: the Möbius gap 2 ≤ N < μ is shared by a_P; so the non-uniform part is in the (1, n) coupling at
  the leak scale, not in the gap.

What is **not** claimed: that (★★) is easier than L′♯ (it is equivalent by I1 + A Thm 3.1), nor that it is the only
exit (§4, ARGUED). What is claimed: it is the only registered object that satisfies the conclusion of the C-pos
class theorem, i.e. whose construction is non-uniform through exact values of the comb over an infinite range.

## 6. Entry for the index (ROUTES-TRIED-INDEX)

"Phase 201, CPOS_CLASS_001 — C-pos class theorem: imported positivity (𝒯: H ⇒ P ≥ 0) on an object O_{g,a} built
uniformly from the comb + monotone bridge 𝔞^a ≥ Φ(P): NO-GO. (i),(ii),(γ) PROVED (lem:transfer + 𝔗₁ soundness; DH
T=9/5, Epstein T≥1.59); (α) affine PROVED under κ_T ≠ 0 (Φ.14, C-E′); (β) non-linear = REF-D or non-uniform input,
ARGUED. Closes phase 201 as a strategy (not by inventory). Escapable only via (h1)–(h6); registered exit:
exterior/(★★) of AUDIT_L_SHARP_16 §6."

## 7. Text for Paper 47, sec:spec

> **Theorem (no imported positivity).** Let $(g,a)\mapsto O_{g,a}$ be a construction defined by one formula for every
> weight datum $a$ of the degree-one theory $\mathfrak T_1$ (functional equation, $\Gamma$-factor, bounded real coefficients,
> residue $\ge0$, no Euler product), let $H(O)\Rightarrow P(O)\ge0$ be a positivity theorem, and suppose
> $\mathfrak a_T^a(g)\ge\Phi(P(O_{g,a}))$ with $\Phi$ nondecreasing and $\Phi\ge0$ on $[0,\infty)$. (i) \emph{(proved)} If this
> bridge is a theorem of $\mathfrak T_1$, then for $T\ge\frac95$ the hypothesis $H(O_{g,a})$ fails for $a=F_{\mathrm{DH}}$ at the
> witness of Remark~\ref{rem:FDH}; likewise in degree two with Lemma~\ref{lem:shape-epstein} for $T\ge1.59$. (ii) \emph{(proved)}
> If $H$ does not depend on $a$, no such deduction proves \eqref{eq:target}. (iii) \emph{(proved if $\kappa_T\ne0$, conditional
> otherwise)} If $H$ is affine in $a$, its margin at $\Lambda$ on a minimizer is at most a constant times $\lamA$. (iv) \emph{(argued)}
> Otherwise verifying $H$ for $\zeta$ uses a premise outside $\mathfrak T_1$ and is at least as strong as \eqref{eq:target}.
> Parts (i)--(ii) are instances of Lemma~\ref{lem:transfer}, (iii) of Theorem~\ref{thm:shape}(A$'$).

(Verified: lem:transfer requires q₀, q₁ in the same class with the property, and q₁'s negative background — given by
rem:FDH and lem:shape-epstein, both "proved"; thm:shape(A′) labels O₄^ε conditional on κ_T ≠ 0, matches (iii). \lamA
and eq:target are existing macros/labels in P47. Not integrated: the editor decides.)

Final labels: C-pos class theorem (i),(ii),(γ) PROVED; (α) PROVED under κ_T ≠ 0 / CONDITIONAL; (β) and trichotomy
ARGUED; "exterior = only infinite non-uniformity" ARGUED; (★★) OPEN. L′♯ OPEN. Row D OPEN.

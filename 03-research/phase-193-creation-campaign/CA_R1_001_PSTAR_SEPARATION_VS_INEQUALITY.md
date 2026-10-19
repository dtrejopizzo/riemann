# CA_R1_001 — Re-examination of 𝖯⋆ (CA_I_001 Cor 6): O14 settled; can the separation become an inequality?

Phase 193, re-examination round 1. Pen and paper, **no numerics**.
CONDITIONAL / ARGUED / OPEN / NO-GO / REF-D. **No sign contact. No negative value for ζ.** Checked against P47 eq:form, thm:nolocal,
def:shape-ops, lem:shape-scale, prop:wit-sens, thm:wit-Tc; CA_I_001 (0.1), Thm 1–3, Rem 3.3; CA_H_002 Thm 2.2.

## 0. Jump-measure form of Beurling–Deny (PROVED; extends CA_I_001 Lemma 3.1)
For a window form 𝔞(F) = (arch part with Lévy density ν) − Σ_n v^a_n c_F(log n) + ∫_ℝ c_F K du (K even, loc. integrable on (0,2T)),
write 𝔞 = m(0)‖F‖² + ∫_0^{2T}(∫(F(t)−F(t+u))²dt) dJ(u) + (diagonal terms), with the **jump measure**
  J_T := ν(u)du − K(u)du + ½Σ_{log n<2T} v^a_n δ_{log n} on (0,2T).
**Markov at T ⟺ J_T ≥ 0 on (0,2T).** (⇐: (|F(t)|−|F(t+u)|)² ≤ (F(t)−F(t+u))². ⇒: the bump pair f₁ − f₂ of Lemma 3.1 at any
density point u₀ of {dJ < 0}, and for a negative atom at log n the same pair at distance log n.) So "Markov ∀T" is exactly:
**a ≥ 0 on ℕ and K ≤ ν a.e. on (0,∞).** It is a cone condition, stable under J ↦ J + (any positive measure).

## 1. Task 1 — O14 settled
**Prop 1.1 (exact Markov criterion for the truncated form; PROVED).** σ_T is continuous, even, σ_T → +∞ (m ~ log|τ|, finite comb), so
g_T := (η − σ_T)_+ ≥ 0 is continuous with compact support and min(σ_T,η) = η − g_T. The form is q_T(F) = η‖F‖² − ∫∫F(t)F(s)ǧ_T(t−s),
ǧ_T(u) = (1/2π)∫g_T(τ)cos(τu)dτ (entire in u). Bounded form, so Beurling–Deny ⟺ **ǧ_T(u) ≥ 0 for all |u| < 2T.**
**Prop 1.2 (Markov at small windows; PROVED).** For 2T < log 2 (empty comb) g_T = (η − m)_+ is nonincreasing in |τ| (m increasing in |τ|,
P47 §bar-loc); with τ_η := sup{τ : m(τ) < η}, integration by parts gives ǧ_T(u) = (1/πu)∫_0^{τ_η} m′(τ) sin(τu) dτ > 0 for 0 < u ≤ π/τ_η.
Hence q_T is Markov at every T ≤ min(½log 2, π/(2τ_η)). For larger T the sign of ǧ_T on (0,2T) is **OPEN** (genuinely a computation).
**Prop 1.3 (O14 is excluded from 𝖯⋆ independently of Markov; PROVED).** (a) Every form object satisfying the 𝖯⋆ clause "ξ̃ with Γ_ℝ"
has an unbounded window form on L²(I_T) (the term ∫ν∫(F(t)−F(t+u))² with ν ~ κ/2u is infinite on L² ∖ 𝒟_T; comb atoms and loc.
integrable K are bounded perturbations); q_T is bounded. (b) The O14 family is not the window family of any single object: window
families of an object are consistent under extension by zero (thm:wit-Tc(i)), i.e. ǧ_{T′} = ǧ_T on (−2T,2T); both are entire, so this forces
g_{T′} = g_T, but for 2T < log 2 < 2T′, g_{T′}(0) = η − C₀ + v₂ ≠ η − C₀ = g_T(0) (for η > C₀ − v₂, which includes all η > 0). ∎
**Verdict O14:** closed. O14 is not an instance of 𝖯⋆ (fails the Γ_ℝ/object clause), whatever its Markov status. **𝖯⋆ is preserved by no
declared single modification O1–O15** (O13 is not a form modification). Cor 6 of CA_I_001 is upgraded from "(O14 OPEN)" to complete.

## 2. Task 2 — separation vs inequality
**Theorem 2.1 (Markov carries no upper bound on the comb; PROVED).** By §0 every consequence of "Markov ∀T" survives J ↦ J + μ, μ ≥ 0.
For every T > ½log 2 there is F₊ ∈ 𝒫_T (P47 lem:shape-scale proof, CA_I_001 Thm 2) with 𝔞^{(a)}_T(F₊) = 𝔞^{(Λ)}_T(F₊) − c v₂‖φ‖² for
a = Λ + c1_{n=2} (O2) and for a = (1+c)Λ (O4, using supp c_{F₊} ∩ log ℕ = {log 2}). Both keep Markov ∀T; both have λ_A(T) → −∞.
Every lower bound on λ_A needs an upper bound on J; Markov supplies only J ≥ 0. ∎
**Theorem 2.2 (every proper sub-conjunction of 𝖯⋆ has a falsifier; PROVED, citing P47/CA_I_001).** Drop the residue: cΛ, c large
(Markov ∀T, (S⁺), Γ_ℝ kept; Thm 2.1) and c small at T ≥ 0.60 (lem:shape-scale). Drop (S⁺): O2 (residue, Markov kept). Drop Markov: O7
quartets (comb Λ, (S⁺), residue, FE, Γ_ℝ, entire kept; lem:shape-quartet). Drop entireness: Remark 3.3 twist ((S⁺), residue, Markov ∀T, FE
kept; K = −2k cosh δu ≤ 0 ≤ ν, λ_A → −∞). Hence any proof of "𝖯⋆ ⇒ λ_A ≥ −ε(T)" uses all four clauses.
**Theorem 2.3 (W-identification of 𝖯⋆; PROVED from CA_H_002 Thm 2.2 + CA_I_001 Thm 3).** (S⁺) + residue ⇒ comb = Λ exactly; then
Markov ∀T + entire FE (within rational twists) ⇒ K ≡ 0 (Thm 3). The four clauses are used **only** to force the exact identities a = Λ,
K = 0: the residue enters as the exact value c = 1 (both sides of 1 falsified, Thm 2.2), and Markov enters only through rigidity of
exponential polynomials (K ≤ ν at u → ∞ ⇒ K ≡ 0), never as a size bound at the window T (its size bound K ≤ ν is satisfied by the
λ_A → −∞ family of Rem 3.3). Once a = Λ, K = 0, Markov ∀T is automatic (Thm 1) and carries zero further information.
**Candidate theorem and its status.** "𝖯⋆ ⇒ λ_A(T) ≥ −ε(T), ε → 0": its instance set in the declared universe is {ζ}, and Thm 2.3 shows
no clause is used quantitatively. **REF-D by identification** (W-identification), exact reason: Markov's only quantitative content is the
cone J ≥ 0 (Thm 2.1), the comb is bounded above only by the identity a = Λ, and the a.c. part only by the identity K = 0.
**Strongest non-identifying remnant (ARGUED, CONDITIONAL).** The class {a = Λ, 0 ≤ K ≤ ν} (Markov ∀T, (S⁺), residue, Γ_ℝ, no FE) contains
ζ and is not identifying, but it is not sign-stable: if the minimizer h at T has c_h(u₀) < 0 at some u₀ ∈ (0,2T) ∖ log ℕ, K = ν1_{|u−u₀|<δ}
lowers 𝔞_T(h) by ≍ ∫ν|c_h| while the ζ margin is ≤ 4·10⁹Te^{−15.449T} in the positive branch of thm:wit-Tc(v). Not pursued.
**Precise OPEN statement, weaker than or equal to D, O4-invariant (OPEN).** D_∃c: *for every T there is c > 0 with λ_A(T; cΛ) ≥ 0.*
J_T := {c : λ_A(T;cΛ) ≥ 0} is a closed interval (concavity, CA_I_001 Prop 1.2(b)), bounded for T > ½log 2 (Thm 2.1), excludes small c for
T ≥ 0.60, and is nonincreasing in T (extension by zero for fixed c). Hence D_∃c ⟺ ∃c* > 0 with λ_A(T; c*Λ) ≥ 0 ∀T (nested compact
intervals). D ⇒ D_∃c; D_∃c ⇒ D iff ∩_T J_T ⊂ {1}, which is exactly the O4^ε question (κ_T ≠ 0 at some window, prop:wit-sens), OPEN.
D_∃c uses only the non-identifying half of 𝖯⋆ ((S⁺) + Markov); it is a target, not a proof.

## 3. Verdict
O14: CLOSED (excluded by the Γ_ℝ/object clause, Prop 1.3; Markov criterion Prop 1.1, small-T Markov Prop 1.2, large T OPEN and irrelevant).
𝖯⋆ ⇒ λ_A ≥ 0: **REF-D by identification** (Thms 2.1–2.3, PROVED). The CA_I_001 discard was correct; its ARGUED step is now PROVED.
New: jump-measure criterion (§0), Thm 2.1, Thm 2.2 (each clause necessary), D_∃c (OPEN, O4-invariant).

## 4. Self-review
1. §0 assumes the form without the polar term (CA_I_001 §8.1 caveat); unchanged. 2. Prop 1.3(b) uses only g(0), no numerics; C₀ < 0 and v₂ > 0.
3. Thm 2.1 for (1+c)Λ: c_{F₊} sees only log 2 since |K| < log(3/2) — P47 proof verbatim. 4. "Within rational twists" in Thm 2.3: outside
that class (general a.c. K from other objects) the K ≡ 0 step is Thm 3's exponential-polynomial argument only; for non-rational objects
(S⁺) already excludes O8/O10–O12. 5. D_∃c might equal D (if κ_T ≠ 0 somewhere); labelled "weaker than or equal". 6. No value of λ_A computed;
no negative value for ζ asserted.

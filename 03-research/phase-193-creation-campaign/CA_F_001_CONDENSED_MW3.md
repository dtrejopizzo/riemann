# CA_F_001 — Condensed / liquid variant of MW-3, developed (front F, phase 193)

Pen and paper. **No sign contact. No negative value for ζ.** Replaces the one-line ARGUED screen F3 of CA_F_000.

## 0. Definitions
- MW-3 (index 03_, l.28): "local positivity at every place ⇒ global positivity of the window form", the ∞-dimensional analogue of
  Hasse–Minkowski. Note that classical HM is about *isotropy*. For a real form, positive definiteness is a condition at ∞ alone.
- The window form, P46: 𝔞_T(F) = m_T(F) − Σ_{n<e^{2T}} v_n Re c_F(log n), with F ∈ P_T and c_F the autocorrelation. Writing it as a
  measure: 𝔞_T(F) = ∫ Re c_F dν_ζ, with ν_ζ = 𝖬_arch − Σ_p Σ_k v_{p^k} δ_{k log p}.
- A **place decomposition** is ν_ζ = ν_∞ + Σ_{p<e^{2T}} ν_p, where ν_p = α_p − Σ_k v_{p^k}δ_{k log p}, the α_p are measures with no
  atoms on log ℕ_{≥2}, and ν_∞ = 𝖬_arch − Σ_p α_p.
  - It is *bare* if every α_p = 0.
  - It is *locally positive* if ν_v ∈ 𝒦*_T (P46 l. 8250) for every place v.
- Condensed setting (Clausen–Scholze, CITED). A T1 compactly generated space X gives the condensed set X̲(S) = C(S,X), for S profinite.
  The functor X ↦ X̲ is fully faithful on compactly generated spaces. A condensed ℝ-vector space carries a continuous form q if
  q: V×V → ℝ̲ is a morphism.

## 1. The condensed upgrade adds no positivity information (PROVED)
**Lemma 1.** Let V be a compactly generated ℝ-vector space with continuous quadratic form q, and let V̲ be its condensed set. The following
are equivalent: (a) q(x) ≥ 0 for every x ∈ V; (b) for every profinite S and f ∈ V̲(S) = C(S,V), the function s ↦ q(f(s)) is ≥ 0 on S;
(c) (b) for S = ∗.
*Proof.* (a)⇒(b) holds pointwise. (b)⇒(c) is trivial. (c)⇒(a) holds because V̲(∗) = V. ∎
**Lemma 2 (liquid completion).** Suppose q is continuous for a p-liquid (or any Hausdorff) topology in which V is dense in its completion
V̂. Then q ≥ 0 on V ⟺ q̂ ≥ 0 on V̂.
*Proof.* Use density, continuity, and closedness of [0,∞). ∎
**Consequence.** A positivity statement about the window form in the condensed or liquid category is literally the same statement as in
P46. It is REF-D unless the condensed framework supplies a *new hypothesis*. The only new hypotheses it offers are local-global
(sheaf/descent) ones, and those are treated in §2–3.

## 2. Bare local positivity is false at every finite place (PROVED)
**Proposition 3.** Let T > ½log2 and p < e^{2T}. Then ν_p^{bare} = −Σ_k v_{p^k}δ_{k log p} ∉ 𝒦*_T.
*Proof.* Let a = log p < 2T. P46 prop:cone(ii) gives F_+ = φ + V_aφ ∈ P_T, with φ of support width w < min(a, 2T−a) and c_{F_+}(a) = 1.
The autocorrelation of F_+ is supported in {|u| < w} ∪ {|u ∓ a| < w}. For w < min_k |k log p − a| over k ≥ 2 (that is, w < log p),
we get ∫Re c_{F_+} dν_p^{bare} = −v_p·1 < 0. ∎
So no finite place is locally positive by itself. The archimedean place is not locally positive either: on P_T, inf 𝖬_arch can be
negative at T ≥ 0.60 (P46 cor:Tarch, λ_P^{inf}(T) < 0). Hence "local positivity everywhere" fails for the bare decomposition at *every*
place. MW-3 in its literal form has a false hypothesis.

## 3. Allotted local positivity is a convex decomposition (REF-D, PROVED by reduction)
**Proposition 4.** If a locally positive place decomposition exists, then λ_A(T) ≥ 0, since 𝒦*_T is a convex cone. Conversely, the
problem "find α_p with ν_p ∈ 𝒦*_T for all v" is an instance of the convex-split problem of CA_B_007 §3, with pieces indexed by places.
Its feasibility implies the target, and certifying any piece needs the bottom of a form of the same type: the form of a one-prime comb
with continuous allotment.
*Proof.* Linearity of ν ↦ ∫Re c_F dν. Each ν_p is itself the measure of a window form, with comb supported on p-powers and archimedean
part α_p. Certifying it is a WP-type statement for that object. CA_B_007 Prop 2 and CA_B_008 §2: any affine split writes the target
through its own spectral data. ∎
**Remark (where a condensed or sheaf structure could add something).** Descent would supply α_p canonically, for example from the
local Tate–Weil distribution at p, which is a real distribution on ℚ_p^×. The local Weil functional W_p on 𝒮(ℚ_p^×) gives
W_p(g∗g̃) = −Σ_k log p·p^{−k/2}(g∗g̃(p^k) + g∗g̃(p^{−k})). Its pullback to the window is exactly ν_p^{bare}, so Proposition 3 applies.
The canonical local terms are the bare ones (CA_C_002 Prop 1, class 𝓗).

## 4. Verdict
- Condensed/liquid MW-3 is **NO-GO (PROVED)** for three classes:
  - the condensed restatement (Lemmas 1–2: REF-D);
  - bare local positivity (Proposition 3: false at every finite place);
  - allotted local positivity (Proposition 4: convex split, REF-D).
- The index cell "MW-3 condensed variant untried" is closed by these three statements.
- What would escape is a positivity of the *global* object that is not a sum of local positivities. That is the polarization question
  of CA_F_003.

## 5. Self-review
- *Is Lemma 1 too trivial to matter?* It is meant to be trivial. It shows the condensed language is not itself a mechanism. Any claim
  that "condensed MW-3" carries content must name the extra hypothesis.
- *Proposition 3 needs a test with c_F(a) = 1 that avoids the other p-powers.* The bound w < log p ≤ min_k |k−1|·log p ensures this,
  and P46 prop:cone(ii) supplies membership in P_T (Tate conditions via lem:transl). The same check passes for p = 2, w < log 2.
- *Could the archimedean allotment be chosen canonically and positively?* That is Proposition 4. Any choice either is the bare one
  (Proposition 3 kills it) or needs a certification of the same type as the target. It is not a falsifier of a conclusion; it is a
  reduction. Label: REF-D.
- O-screen: the local data at p ≥ P is kept by O6 (a_P). A local-global principle whose inputs are the local data at the places
  present is closed under O6, and a_P fails WP_T on [0.60, ½log P] (P46 prop:shape-eulerdel). This independently kills any
  local-global principle with only local inputs.

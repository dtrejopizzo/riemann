# INTEGRATION_O1_001 — Integration of O1 into Paper 46 (phase 204p, editor)

Backup: `04-papers/46-row-d-sign-radial-intersection-form/main_pre_o1.tex`.

## 1. Verification against P46's definitions

- **lem:transfer (l.7734), literal:** "q₀,q₁ ∈ 𝔛 both have 𝖯 … bottom of q₁ negative." 𝖯 is a single property; for
  𝖯 = ∧P_i, the falsifier must satisfy all the P_i. **O1.A(a) is correct (PROVED, trivial).**
- **lem:shape-quartet (l.8560) — DISCREPANCY.** P46 says that ξ_{z,k} preserves the comb, **the functional equation**,
  reality and the pole. prop:shape-inputs(iv) (l.8781): "O₇ and O₈ keep (F): the quartet models keep (E) as a comb
  identity but add an absolutely continuous arithmetic part." O1 §2.1/§2.3 claims that quartets violate F: **FALSE
  according to P46**. The quartets satisfy F and the comb; what they break is E in the form of a Dirichlet series over
  ℕ (atomic arithmetic side; ξ'/ξ + rational). Consequences:
  - "F is mandatory" remains true, but because of **a_P** (prop:shape-inputs(i)), not because of the quartets.
  - The quartets force E **as a Dirichlet series** (not merely as a comb identity).
  - Φ200′(b) and the remark text proposed by O1 ("quartet models show that the FE must be among the inputs") were
    corrected during integration. Φ200′ remains valid with this re-attribution.
- **cor:shape(b) (l.9057) and thm:shape(B) (l.9023):** already say "uses the Euler product over ℕ, the FE at conductor
  1 [and integrality] jointly." O1 **reinforces** it (locates it at the sign step, Def. O1.2), it does not contradict it.
- **Prop O1.B / Kaczorowski–Perelli:** KP (Acta Math. 182, 1999) classifies degree 1 as ζ(s+iθ) and L(s+iθ,χ), χ
  primitive mod q. Conductor 1 ⇒ ζ(s+iθ). θ = 0 is fixed **by the pole at s = 1** (included in F: "reality and the
  pole"; and in the Selberg-class axiom); reality of coefficients also fixes it (n^{−iθ} real ∀n ⇒ θ = 0). I3 is not
  needed for θ. O1.B should say "ζ(s+iθ), θ = 0 by the pole/reality." P46 **has no KP bibitem**; since in P46 (E) is
  already a Dirichlet series over ℕ, **Hamburger** suffices (hypothesis: ordinary Dirichlet series, finite order /
  (s−1)ζ entire of finite order, FE of ζ ⇒ constant multiple of ζ; Titchmarsh §2.13), which P46 already cites
  (\cite{Hamburger1921}). The remark uses only Hamburger; "up to a constant" (the residue fixes the constant).
- Def O1.2 / Lemma O1.E: compatible with cor:shape(a) ("non-linearly", lem:shape-lin(i)). OK.

## 2. Changes in main.tex

- Inserted after l.9354 (end of thm:noimport), lines 9355–9370: `\begin{remark}[conjunctions; (i)--(iii) proved, (iv)
  argued]\label{rem:conjunctions}` with (i) transfer = common falsifier; E∧F ⇒ ζ by Hamburger; (ii) sign step with ≥2
  inputs without a common falsifier, includes (F) (via a_P) and (E) as a Dirichlet series (via quartets); refines
  cor:shape(b); (iii) chaining vs composing; (iv) inventory (Lemma R ∧ gap, Poisson–Möbius, co-Poisson mirror ∘
  lattice), memos P2_SCHUR_001, BUILD_R2_001, PROOF_L_SHARP_FF_001, O1_COMPOSITION_001. 12 source lines.
- No other line touched. No mention of equivalences.

## 3. Compilation
pdflatex ×2: 0 errors, 0 undefined references, **190 pages**.

## 4. Pending (pending review)
- Correct O1_COMPOSITION_001 §2.1 (proof of O1.A(c)), §2.3 Φ200′(b) and the META/index text: quartets satisfy F;
  F is mandatory because of a_P; quartets force E-as-Dirichlet.
- Add a θ = 0 note to O1.B.

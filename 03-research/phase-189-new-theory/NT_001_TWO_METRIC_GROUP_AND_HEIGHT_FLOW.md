# NT_001 — The two-metric group (ℚ_{>0}, ℓ, h), the Weil kernel on it, and the height flow

Phase 189, new theory, construction step 1. Pen and paper, no numerics. no
equivalence of D with any other statement is used or mentioned.
Neutral names only: "height flow", "denominator damping", "two-metric group".

## Corpus check
grep (03-research, 04-papers, 05-meta-and-planning) for: "Q_{>0} / ℚ_{>0}" + "positive definite", "Schur multiplier",
"Poisson kernel on", "height damp", "H(r)^", "conditionally negative definite", "Kakutani", "Steinhaus", "ζ(σ)²/ζ(2σ)".
Relevant hits and how this memo differs:
- **R160_C5_R1 Thm 2.1/2.3, §4 (and G1_B4_R2 Prop E3, G1_B7_R4 "positive trace datum")**: the smeared Weil datum φ_ε as a
  function on the discrete group ℚ_{>0}; positivity on ℚ_{>0} and on dense subgroups; Schur coupling with ONE fixed positive
  definite function ω (Liouville on squares) — shown to be a restatement. **Corpus-known: "D ⟺ PD on ℚ_{>0}" (here Thm 1.1).**
- **D.195 (phase 114)**: per-prime Poisson feature operator A_p = √(1−r_p²)(I − r_pU_p)^{-1}, r_p = p^{-1/2}, acting on L²(ℝ) by
  translations — a dilation of the *prime symbol*; it never damps the *Weil kernel* on ℚ_{>0}.
- **G2_B8_R3 Remark B**: Schur/Hadamard products of Euler factors listed as arithmetic-blind *certificates*.
- **D.187**: Steinhaus Bohr lift of Λ-powers (moments), not a deformation of the target.
- L2_BUILD_028–031, N_BUILD_021–022 (phase 188): A_M = Arch − Div − Near; Div Bohr-diagonal; Near = finite-resolution defect.
**New here (no hit):** the height function h = log H as the second metric with the product-formula inequality ℓ ≤ h and the
defect h − ℓ = 2 log(denominator); the one-parameter *height flow* K ↦ K·H^{−σ} applied to the Weil kernel; monotonicity of
every finite-section bottom along the flow (Thm 1.3); the invariant σ*(a) of a comb (Def 1.6) and its behaviour on the
falsifiers (Thm 1.5); the first-contact derivative lemma (Lemma 1.7). The flow is a *deformation of the target*, not a
certificate, so G2_B8_R3 Remark B does not apply to it as stated (see §5).

## 0. Standing data (from the record, checked against Paper 47 §2–3 and L2_BUILD_024/025)
- F₀: the explicit primitive profile of L2_BUILD_024 §2 / 025 §1: g = e^{bt}1_{[0,a]}, |b| > ½, G₀ = g*g̃*g*g̃ centred,
  F₀ = (¼ − ∂²)G₀ ∈ P_{T₀}, 2T₀ = 4a < log 2, normalized ‖F₀‖₂ = 1. c₀ := c_{F₀} (autocorrelation), supp c₀ ⊂ [−2T₀, 2T₀],
  c₀(0) = 1, ĉ₀ = F̂₀² > 0, with double zeros at ±i/2 (Tate).
- B(d) := 𝔞(F₀, τ_dF₀) = A(d) − ½Σ_{n≥2} v_n[c₀(d − log n) + c₀(d + log n)], v_n = 2Λ(n)n^{−½}, A(d) := 𝔞_∞(F₀, τ_dF₀)
  (archimedean bilinear form of eq:Aform). B is real, even, continuous (024 §1, CONFIRMED).
- a₀ := B(0) = A(0) = 𝔞_∞(F₀) (no n ≥ 2 has log n ≤ 2T₀). a₀ > 0 (prime-free window, Paper 47; also Lemma 2.6 of NT_002).
- Theorem S (L2_024 + 025, CONFIRMED with FIXes): D ⟺ B is positive definite on ℝ.
- For a general real comb a = (a(n))_{n≥2} (falsifiers), B_a, K^{(a)} etc. are defined by the same formula with
  v_n replaced by 2a(n)n^{−½}.

## 1. Definitions (the new objects)
**Def 1.1 (two-metric group).** G := ℚ_{>0} (discrete, free abelian on the primes). For r = a/b with (a, b) = 1 put
  ℓ(r) := |log r| (archimedean length),  H(r) := ab (naive height),  h(r) := log H(r) = Σ_p log p·|v_p(r)|,
  den(r) := min(a, b) (the denominator of r or of 1/r, whichever is ≥ 1).
**Def 1.2 (Weil kernel on G).** K(r) := B(log r), r ∈ G. For a comb a: K^{(a)}(r) := B_a(log r).
**Def 1.3 (height flow).** For σ ≥ 0: K_σ(r) := K(r)·H(r)^{−σ}. "D(σ)": K_σ is positive definite on G, i.e. every finite matrix
  [K_σ(x/y)]_{x,y∈X}, X ⊂ G finite, is positive semidefinite. Same for K^{(a)}_σ, "D_a(σ)".
**Def 1.4 (section bottoms).** λ_X(σ) := λ_min[K_σ(x/y)]_{x,y∈X}; λ_inf(σ) := inf_X λ_X(σ) ∈ [−∞, a₀].
**Def 1.5 (Poisson multipliers).** For ρ = (ρ_p)_p ∈ [0,1)^{primes}: P_ρ(r) := Π_p ρ_p^{|v_p(r)|}. H^{−σ} = P_ρ with ρ_p = p^{−σ}.
**Def 1.6 (positivity depth).** σ*(a) := inf{σ ≥ 0 : D_a(σ)} ∈ [0, ∞].

## 2. The two metrics (PROVED)
**Prop 2.1.** (i) ℓ ≤ h on G, with equality iff r ∈ ℕ ∪ ℕ^{−1}. (ii) h − ℓ = 2 log den. (iii) h is conditionally negative
definite (CND) on G; hence every P_ρ, in particular H^{−σ} (σ ≥ 0), is positive definite on G. (iv) H^{−σ} = e^{−σℓ}·den^{−2σ}.
*Proof.* (i) Product formula: log r = Σ_p v_p(r) log p, so |log r| ≤ Σ_p |v_p(r)| log p = h(r), with equality iff all nonzero
v_p(r) have the same sign, i.e. r or 1/r is an integer. (ii) For r = a/b ≥ 1 reduced: h − ℓ = log(ab) − log(a/b) = 2 log b = 2 log den.
(iii) On ℤ, (k, l) ↦ |k − l| is CND (it is the restriction of |x − y| on ℝ, a metric of negative type: Σc_ic_j|x_i − x_j| =
−2∫(Σ_{x_i≤t}c_i)²dt ≤ 0 when Σc_i = 0). h(x/y) = Σ_p log p·|v_p(x) − v_p(y)| is a nonnegative combination of CND kernels,
hence CND. For a single prime, k ↦ ρ^{|k|} is PD on ℤ (Fourier series (1 − ρ²)/|1 − ρe^{iφ}|² ≥ 0); a finite product of PD
functions in independent coordinates is PD, and P_ρ restricted to any finite X involves finitely many primes. (iv) from (ii). ∎
**Reading.** The two metrics agree exactly on the integers (and their inverses): Div lives on {ℓ = h}. A near-coincidence
m ≈ kn, m ≠ kn, is a ratio r = m/k close to an integer n with *large height*, i.e. a point where ℓ(r/n) is tiny and the
defect h − ℓ = 2 log den is large. The height flow damps every r by e^{−σℓ}·den^{−2σ}: the first factor is a real-line
(Bochner) damping; the second is the new **denominator damping**, which is 1 on Div and suppresses Near.

## 3. The flow and its monotonicity (PROVED)
**Thm 1.1 (corpus-known; restated).** D ⟺ K is positive definite on G ⟺ D(0).
*Proof.* (⟹) Given X ⊂ G finite, multiply by a common denominator Q: m_x := Qx ∈ ℕ, K(x/y) = B(log m_x − log m_y), and
D ⟹ B PD (Theorem S). (⟸) PD of K on G gives A_M ⪰ 0 for every M, and 028 §1 + Theorem S give D. (Fixed-profile analogue of R160_C5_R1 Thm 2.1, which concerns a different, smeared datum φ_ε quantified over ε.) ∎
**Thm 1.2 (flow exists, is a semigroup, and preserves positivity).** K_{σ+τ} = K_σ·H^{−τ}; D(σ) ⟹ D(σ′) for all σ′ ≥ σ.
*Proof.* Schur product theorem with the PD matrix [H(x/y)^{−τ}] (Prop 2.1(iii)). ∎
**Thm 1.3 (monotone quantity: every section bottom is nondecreasing along the flow, whatever its sign).**
For every finite X and σ ≤ σ′: λ_X(σ) ≤ λ_X(σ′). Hence λ_inf is nondecreasing.
*Proof.* Put A = [K_σ(x/y)], P = [H(x/y)^{−(σ′−σ)}] (PSD, unit diagonal), λ = λ_min(A). A − λI ⪰ 0, so (A − λI)∘P ⪰ 0, and
(λI)∘P = λI. Hence A∘P ⪰ λI, i.e. λ_X(σ′) ≥ λ_X(σ). ∎
**Thm 1.4 (D is the bottom of the flow).** D ⟺ D(σ) for every σ > 0 ⟺ λ_inf(σ) ≥ 0 for every σ > 0.
*Proof.* (⟹) Thm 1.1 + 1.2. (⟸) For finite X, [K_σ(x/y)] → [K(x/y)] entrywise as σ ↓ 0; the PSD cone is closed. Thm 1.1. ∎
So the target is the *bottom end* of a monotone one-parameter family of strictly weaker positivity statements D(σ).

**Thm 1.5 (the flow separates the falsifiers; PROVED, with Paper 47 thm:finmod/cor:void CITED).**
(i) For every comb a for which D fails, σ*(a) > 0.
(ii) Amplification at 2: a_c := Λ + c·1_{n=2} (c > 0). Then a₀ is unchanged and σ*(a_c) ≥ log₂((c/√2 − |B(log 2)|)/a₀) → ∞.
(iii) Every D(σ) with σ > 0 is strictly weaker than D on the space of combs: there are combs (finite modifications of Λ) with
D_a(σ) and not D_a.
*Proof.* (i) D_a fails ⟹ some finite X has λ_min[K^{(a)}(x/y)] < 0 ⟹ by continuity in σ, λ_X(σ) < 0 for small σ > 0.
(ii) c₀(±log n) = 0 for n ≥ 2 (2T₀ < log 2), so B_{a_c}(0) = a₀. B_{a_c}(log 2) = B(log 2) − ½·2c·2^{−½}c₀(0) = B(log 2) − c/√2.
On X = {1, 2} the matrix is [[a₀, κ],[κ, a₀]] with κ = 2^{−σ}B_{a_c}(log 2) (H(2) = 2); it is PSD iff |κ| ≤ a₀.
(iii) Take a_c of (ii) with c/√2 > |B(log 2)| + a₀: D_{a_c}(0) fails on {1,2}. For σ large, Σ_{r≠1}|K^{(a_c)}(r)|H(r)^{−σ} → 0 by dominated
convergence (Lemma 2.0 bounds, the atom adds a compactly supported term), so D_{a_c}(σ) holds by Gershgorin. ∎
**Remark (what σ* measures).** σ*(a) is a quantitative "positivity depth" in the height direction. Falsifiers have σ* > 0,
amplified ones σ* → ∞; the target is σ*(Λ) = 0. This is the invariant the theory is built to compute.

## 4. First contact (PROVED)
**Lemma 1.7 (contact vectors).** Let X be finite, A = [K_σ(x/y)]_X ⪰ 0 and s ∈ ker A. Then
  (d/dσ) sᵀ[K_σ(x/y)]s = −sᵀ(h∘A)s ≥ 0,
with equality iff, writing A = Σ_i u_iu_iᵀ, every vector w_i := s⊙u_i has, for every prime p, zero mass on each half-line
{x : v_p(x) ≤ t} (all t ∈ ℤ).
*Proof.* d/dσ H^{−σ} = −h·H^{−σ}. sᵀAs = Σ_i(Σ_x s_xu_i(x))² = 0 ⟹ Σ_x w_i(x) = 0 for every i. sᵀ(h∘A)s = Σ_i w_iᵀ[h(x/y)]w_i,
and for zero-sum w, w ᵀ[h(x/y)]w = Σ_p log p·Σ_{x,y}w_xw_y|v_p(x) − v_p(y)| = −2Σ_p log p Σ_t(Σ_{v_p(x)≤t}w_x)² ≤ 0. ∎
**Reading.** At a first contact σ = σ*(a) > 0 (if attained on a finite section) the flow pushes *transversally* off the
boundary unless the contact vector is "valuation-balanced" at every prime — a rigid arithmetic condition on the contact set.
For the target one needs to exclude contact at every σ > 0.

## 5. Requirements check (input map L2_011, N_018 meta-theorem, falsifiers) — honest
- **Euler × FE × integrality.** Integrality: used essentially (G = ℚ_{>0} free on primes; h = Σ log p|v_p|; product formula).
  Euler product: H^{−σ} = Π_p (local Poisson factor) — a product over primes, used non-linearly (Schur multiplier); its
  Fourier side is |L(σ + iτ, χ)|²/ζ(2σ) (NT_002). FE: enters only through A (archimedean kernel), as in D itself. **Not yet joint.**
- **N_018 meta-theorem (shift-multiplier calculus = 𝔄_T identities + Bochner/C–S).** The denominator damping den^{−2σ} is not a
  function of log r; K_σ does not descend to ℝ; it is not a shift multiplier and lies outside the scope of N_018. But Thms 1.2–1.4
  are Schur/Bochner facts: they *organize* the target, they do not prove it. Any proof of D through the flow must move positivity
  *down* in σ (backward flow), which no positivity-preserving operation does; that step must carry arithmetic.
- **Falsifiers.** a_P, Λ + c1_{n₀}, W-tail, Beurling (on ℕ-indexed tests), M_m: all have well-defined flows; Thm 1.5 shows D(σ)
  distinguishes them quantitatively (σ* > 0). Everything PROVED in this memo holds for every comb (class statements); they are
  infrastructure, not sign.

## 6. Review
- Thm 1.1 is corpus-known (R160_C5_R1 Thm 2.1); restated, credited. ✓
- Prop 2.1(iii): CND of |k − l| and closure under nonnegative sums are standard; PD of P_ρ on finite X is a finite product. ✓
- Thm 1.3: the inequality λ_min(A∘P) ≥ λ_min(A)·min P_ii holds for Hermitian A of ANY sign and PSD P (proof given). ✓ This is
  the genuinely useful monotone quantity: the flow can only raise every finite bottom.
- Thm 1.5(ii): needs only 2T₀ < log 2 (profile hypothesis) for B_{a_c}(0) = a₀; fine. (iii) depends on NT_002 Thm 2.5 — check there.
- Lemma 1.7: derivative of a PSD-path at a null vector; correct. "Attained on a finite section" is an assumption, stated.
- Danger: calling D(σ) "weaker" invites a false claim that D(σ) for some σ > 0 is a partial result toward D. It is a partial
  result only in the sense of Thm 1.4 (D = ∩_σ D(σ)); there is no implication D(σ) ⟹ D for any fixed σ > 0 (Thm 1.5(iii)).
- No negative value of 𝔞_T for ζ is computed or claimed. **No sign contact.**


## Erratum note (after NT_001_004_REVIEW)
Thm 1.1 citation re-scoped; Thm 1.5(iii) re-routed through a_c + dominated convergence (referee FIX 1–2).

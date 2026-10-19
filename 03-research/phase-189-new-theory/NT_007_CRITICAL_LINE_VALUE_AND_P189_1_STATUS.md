# NT_007 — The value of the height flow on the ℓ² line: V(τ₀) = −(F̂₀²·(log|ζ(½+iτ)|)′)′(τ₀)/ζ(2) + Re ℛ₁(τ₀); a Λ-specific necessary
# inequality; status of P189.1 and admissibility of the inputs

Phase 189, construction step 7. Notation of NT_005–006. Labels as there.

## Corpus check
grep "log|ζ(½+it)|", "(log|ζ|)′′", "concav", "Re(ζ′/ζ)′", "Im ζ′/ζ" + "Weil": hits — R160_PD_R1 Lemma 2.1 (Re(−ζ′/ζ)(½+iy) = ½m(y)); phase
55/176 (Green–Littlewood attack: log|ζ| potential theory, different object); N_013 (packet limits critical); L2_010 (centre). No memo derives
a pointwise necessary inequality on (F̂₀²(log|ζ|)′)′ from window positivity, nor the decomposition of P189.1 below. **New:** Thm 7.1,
Cor 7.2, Prop 7.3 (P189.1 = curve positivity + off-curve regularity), the admissibility table §3.

## 1. The value on the ℓ² line (PROVED)
Write ℓ(τ) := log|ζ(½ + iτ)| (real-analytic off the zeros on the line).
**Thm 7.1.** For τ₀ with ζ(½ + iτ₀) ≠ 0:
  V(τ₀) := lim_{σ→1}Φ^{curve}_σ(τ₀) = −(1/ζ(2))·(d/dτ)[F̂₀(τ)²ℓ′(τ)]|_{τ=τ₀} + Re ℛ₁(τ₀).
*Proof.* (ζ(2σ−1)/ζ(2σ))G(σ, τ₀) with ζ(2σ−1) = 1/(2(σ−1)) + O(1) and G(1, τ₀) = 0 (Cor 6.2) tends to ∂_σG(1, τ₀)/(2ζ(2)).
At σ = 1: z = −τ₀, w = ½ + iτ₀, dz/dσ = i, dw/dσ = 1.
- d/dσ F̂₀(z)² = 2iF̂₀(z)F̂₀′(z) = −2iF̂₀(τ₀)F̂₀′(τ₀) (F̂₀ even ⇒ F̂₀′ odd).
- M(w) = 2i Im(ζ′/ζ)(½ + iτ₀) = −2iℓ′(τ₀), since d/dτ log ζ(½ + iτ) = i(ζ′/ζ) gives ℓ′ = −Im(ζ′/ζ).
- dM/dσ = (ζ′/ζ)′(w) + (ζ′/ζ)′(1 − w) = 2Re(ζ′/ζ)′(½ + iτ₀) = 2·d/dτ Im(ζ′/ζ)(½ + iτ) = −2ℓ″(τ₀).
So ∂_σG(1) = Re[(−2iF̂₀F̂₀′)(−2iℓ′) + F̂₀²(−2ℓ″)] = −4F̂₀F̂₀′ℓ′ − 2F̂₀²ℓ″ = −2(F̂₀²ℓ′)′. ℛ is analytic at σ = 1 (Prop 5.3). ∎
**Reading.** On the ℓ² line the height flow is: (archimedean + Euler, fused by the FE into the derivative of log|ζ| on the critical line,
weighted by the profile) + (integer-discreteness remainder ℛ₁). Near a zero on the line, ℓ′ ~ 1/(τ − γ) and −(F̂₀²ℓ′)′ ~ +F̂₀(γ)²/(τ − γ)²:
positive spikes, the expected sign.

## 2. A Λ-specific necessary inequality (PROVED as an implication)
**Cor 7.2.** If D holds, then for every τ₀ with ζ(½ + iτ₀) ≠ 0:
  (F̂₀²ℓ′)′(τ₀) ≤ ζ(2)·Re ℛ₁(τ₀).                                                     (𝒱)
*Proof.* Under D, for σ > 1, Φ_σ is continuous with Φ_σ∘ι = Φ^{curve}_σ (Prop 5.5) and Φ_σ ≥ c_σa₀ ≥ 0 (NT_002 Cor 2.8, measure form, valid
for σ > 1). Let σ ↓ 1 (Φ^{curve} regular there, Cor 6.2): V(τ₀) ≥ 0. ∎
(𝒱) is a one-variable inequality, explicit on both sides: the left side is Λ-specific through ζ on the critical line (it does not exist for
finite modifications, whose curve symbol has a pole at σ = 1 — NT_006 Thm 6.3); the right side is an absolutely convergent arithmetic sum
of Euler–Maclaurin defects. **Sign-contact protocol:** a certified τ₀ violating (𝒱) would certify failure of D; flag immediately. None
is computed (no numerics); none claimed.

## 3. Status of P189.1 (D(σ) for every σ > 1) — PROVED decomposition, target OPEN
**Prop 7.3.** For σ > 1: D(σ) ⟸ [(a) Φ^{curve}_σ(τ₀) ≥ 0 for all τ₀] ∧ [(b) Φ_σ has a continuous version on 𝕋^∞ whose restriction to ι(ℝ)
is Φ^{curve}_σ]. For σ > 3/2, (b) holds unconditionally (NT_005 Thm 5.1–5.2) and D(σ) ⟺ (a). Under D both hold for every σ > 1.
*Proof.* (b) + density of ι(ℝ) + (a) ⇒ the continuous version is ≥ 0 everywhere ⇒ the L² density is ≥ 0 a.e. ⇒ D(σ) (NT_003 Thm 3.4). ∎
So P189.1 splits into a **Λ-specific curve problem (a)** — where Euler, FE and integrality act jointly (Thm 5.2 + Thm 6.1) and which at
σ ↓ 1 becomes (𝒱) — and a **regularity problem (b)** for 1 < σ ≤ 3/2: continuity of the height symbol off the curve. (b) is about the
size of K_σ (the near-coincidence sums Σ_r H(r)^{−σ}χ(r)Ξ(log r) for characters close to, but not on, the curve).
What was tried for (b) in this step: absolute bounds fail below 3/2 with the unconditional prime number theorem error (NT_003 Prop 3.1;
exact obstruction: ∫e^{(3/2−σ)u}|E(u)|du = ∞ for E(u) = exp(−c√u)); Haar/L² methods give only a.e. statements (no pointwise control).
**(b) is OPEN.** A uniform (not a.e.) cancellation estimate for Σ_{r: ℓ(r)∈[u,u+1]}H(r)^{−σ}χ(r)Ξ(log r) for χ in a neighbourhood of the
curve would suffice; no such estimate is available unconditionally.

**Admissibility of the inputs (coordinator's question).**
| input | used where | closed under | admissible for σ > 1? |
|---|---|---|---|
| explicit Chebyshev bound ψ(x) < 1.04x (CITED) | NT_002 Thm 2.5, Lemma 2.0 | only bounded modifications (a large atom violates the explicit constant) | yes: NT_003 Thm 3.5 (tolerance > 0 with margin) is exactly the robustness this class has; cor:void needs unbounded amplification (NT_001 Thm 1.5(ii)) |
| PNT with dlVP error (CITED) | NT_003 Prop 3.1 at σ = 3/2 | all finite modifications | yes for σ > 1 in the same sense (only used for an ℓ¹ statement, not for sign) |
| W-tail majorant (0 ≤ a ≤ Λ, a = Λ on n < n₀) | not used | — | the W-tail combs satisfy D(σ) for σ > 1 when a₀ is large depending on n₀ (finite comb: K^{(a)}_σ ∈ ℓ¹ for σ > 1, Gershgorin) — so W-tail does not obstruct D(σ), σ > 1, but the same argument shows such majorant inputs cannot distinguish Λ there |
| FE of ζ (CITED) | NT_006, NT_007 | no modification (Thm 6.3: every finite modification and every truncation acquires a pole at σ = 1) | yes, and it is the Λ-specific input |
| integrality: ℕ-discreteness (Euler–Maclaurin), coprime counting ζ(2σ−1) | NT_005 | — (structural) | yes |
Conclusion: for σ > 1 class inputs with explicit constants are not excluded by cor:void/W-tail (they are excluded only as proofs of D itself);
the Λ-specific content of the theory is carried by the FE through the curve formula.

## 4. Requirement check (whole step 5–7)
- Euler × FE × integrality jointly and non-linearly: Thm 5.2 + Thm 6.1 — the product ζ(2σ−1)·[ζ′/ζ(w) − ζ′/ζ(1−w)] (coprime counting ×
  FE-antisymmetrized Euler log-derivative), plus the ℕ-discreteness remainder. **Met at the level of an exact identity.**
- Falsifiers: a_P, Λ + c1_{n₀}, truncations/W-tail all lose regularity at σ = 1 (Thm 6.3); Beurling (ℕ-indexed tests) and Epstein/DH-type
  combs have no ζ-FE with Euler product of conductor 1 in this frame (for DH-type sums the curve formula holds with their L′/L, and
  regularity at σ = 1 requires the line identity m + 2Re L′/L(½+iτ) ≡ 0 — that identity holds for any Dirichlet series with the same
  Γ_ℝ functional equation, so the regularity property alone does NOT exclude Epstein/DH: ARGUED; their failure must come from (a)).
- N_018: Thm 5.2 is not a shift-multiplier identity on ℝ (it uses the coprime-pair structure of ℚ_{>0} and the discreteness of ℕ);
  Cor 7.2 is an implication from D. No proof of D is claimed.

## 5. Review
- Thm 7.1: three derivative computations checked (F̂₀ even; ℓ′ = −Im ζ′/ζ; Re(ζ′/ζ)′ = d/dτ Im ζ′/ζ on the line). The O(1) part of
  ζ(2σ−1) multiplies G(1) = 0 ✓.
- Cor 7.2: relies on Prop 5.5 (conditional on D, as an implication) and on Cor 2.8 measure form (δ = σ > 1 allowed) ✓.
- Prop 7.3: (b) is genuinely needed — without continuity, a.e. positivity cannot be read off the Haar-null curve. ✓
- §4 Epstein/DH caveat: honest; the FE-regularity is shared by every Dirichlet series with the same functional equation; Λ-specificity
  of Thm 6.3 is only against finite modifications and truncations of Λ.
- ℛ₁ grows at most like (1 + τ₀²) (Prop 5.3); no uniformity in τ₀ is claimed.
- No negative value certified. **No sign contact. Row D OPEN.**

## Erratum note (after NT_005_007_REVIEW)
(4) §4 Epstein/DH caveat reversed: regularity at σ = 1 fails for them as well (different Γ-factor/conductor); see NT_006 erratum.
(5) Admissibility table, W-tail row: wrong as stated. For finite combs the Gershgorin constants blow up as σ ↓ 1; each truncation satisfies
D(σ) only above some σ₀(F₀, n₀) > 1, and fails D(σ) as σ ↓ 1 (NT_006 Cor 6.5). So W-tail-type majorant inputs are excluded near σ = 1
(the argument cannot be uniform down to σ = 1), consistent with the Λ-specificity of the regularity at σ = 1.

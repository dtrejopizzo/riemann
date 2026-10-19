# NT_005–007 — review

Referee: independent, pen and paper only.
Labels: CONFIRMED / FIX / DOWNGRADE.

## NT_005
| item | verdict | notes |
|---|---|---|
| Thm 5.1 (min over 𝕋^∞ = inf over curve, σ > 3/2) | CONFIRMED | ι(ℝ) dense in 𝕋^∞ (product topology) by ℚ-independence of {log p} + Kronecker (finite sub-tori suffice for basic open sets); Φ_σ continuous by ℓ¹ (NT_002 Prop 2.1, σ > 3/2). |
| Thm 5.2 variables s, w, z | CONFIRMED | z = −τ₀ + i(σ−1) = −i(1−s) ✓; ¼ + iz/2 = (1−w)/2, ¼ − iz/2 = w/2 ✓; v_n n^{1−s} = 2Λ(n)n^{−w} requires v_n = 2Λ(n)n^{−½} ✓ (NT_002 comb). Prefactor: Σ_k k^{−s̄}k^{1−s} = ζ(2σ−1), divided by ζ(2σ) ✓. Main factor F̂₀²[m + 2ζ′/ζ(w)] ✓. |
| Thm 5.2 range | **FIX** | Â(s) = ∫A(u)e^{(1−s)u}du converges only for \|σ−1\| < 5/2 (A ~ e^{−5\|u\|/2}); the proof itself notes −3/2 < σ < 7/2. The theorem is stated for all σ > 3/2: restrict to 3/2 < σ < 7/2 (or define Â by continuation and E^A with the integral over (1,∞)). Nothing downstream needs σ ≥ 7/2. Same restriction in Prop 5.3 (∫_0^1 piece is O(L^{−5/2}) only for σ < 7/2) and Cor 5.4 ("σ > 0" → "0 < σ < 7/2"). |
| "coprime counting" reading of ζ(2σ−1)/ζ(2σ) | CONFIRMED (as reading) | The sum is over all (m,k), not coprime pairs; ζ(2σ−1)/ζ(2σ) arises as Σ_k k^{1−2σ} divided by the common-factor normalization. The coprime interpretation is via grouping (m,k) = (da,db); acceptable wording. |
| Prop 5.3 (remainder analytic in σ > 0, growth (1+\|s\|)²) | CONFIRMED with FIX (constants) | E^c bound \|s\|²L^{−σ−1} ✓. E^A on [1,∞): for σ > 3/2 the range 1 ≤ x ≪ L gives L^{−5/2}, not L^{−σ−1}; displayed bound should read L^{−min(σ+1,5/2)}. Sums still converge (Σ_k k^{−σ}L^{−5/2}, σ > 0). Conclusion (real-analytic in σ, locally uniform, polynomial growth in τ₀, not small in τ₀) stands. |
| Cor 5.4 (meromorphic continuation, singularity list) | CONFIRMED (range FIX above) | Poles: σ = 1 (ζ(2σ−1)), zeros/pole of ζ at w, poles of m; m's poles at w = 0, 1 (z = ∓i/2) killed by F̂₀² double zeros ✓; ζ(2σ) ≠ 0 for σ > 0 real ✓. |
| Prop 5.5 (if D, continuation = symbol for σ > 1) | CONFIRMED with FIX (wording) | Under D: Q_σ = Π_p Poisson factors with r_p = p^{−σ}, uniformly convergent for σ > 1 ⇒ Q_σ continuous, analytic in σ ⇒ Q_σ⋆μ₀ continuous, real-analytic in σ ✓; identity theorem on (1,∞) minus a discrete set ✓. Add: since Φ_σ∘ι is finite for all σ > 1, every singularity of Φ^{curve}_σ(τ₀) in σ > 1 must then be removable (state this explicitly; "away from singularities" is imprecise). |

## NT_006
| item | verdict | notes |
|---|---|---|
| m vs Γ_ℝ convention | CONFIRMED | γ = Γ_ℝ′/Γ_ℝ = −½log π + ½ψ(w/2); m(z) = γ(w) + γ(1−w); at σ = 1, m = Re ψ(¼ + iτ₀/2) − log π, the record's m ✓. |
| Thm 6.1 identity m + 2ζ′/ζ(w) = ζ′/ζ(w) − ζ′/ζ(1−w) | CONFIRMED | log-derivative of ξ_ℝ(w) = ξ_ℝ(1−w): γ(w) + ζ′/ζ(w) = −γ(1−w) − ζ′/ζ(1−w) ✓. |
| Oddness σ ↦ 2−σ, evenness in τ₀ | CONFIRMED | With τ₀ fixed: z ↦ z̄, w ↦ conj(1−w), G ↦ Re conj[F̂₀(z)²M(1−w)] = −G ✓ (equivalently the stated composite with τ₀ ↦ −τ₀ plus evenness). |
| Cor 6.2 G(1,τ₀) = 0, cancellation of pole of ζ(2σ−1) | CONFIRMED | M = 2i Im ζ′/ζ, F̂₀² real ⇒ Re = 0 off zeros ✓. Note: "F̂₀(τ₀)² > 0" needs F̂₀(τ₀) ≠ 0; only ≥ 0 is used. |
| Thm 6.3(i) finite modifications: residue −F̂₀²Σδ(n)n^{−½}cos(τ₀log n)/ζ(2) | CONFIRMED | Both signs: mean-zero almost-periodic polynomial ✓. |
| Thm 6.3(ii) truncations | CONFIRMED + strengthening | Residue (F̂₀²/2ζ(2))[m(τ₀) − 2Σ_{n<N}Λ(n)n^{−½}cos(τ₀log n)]. At τ₀ = 0: m(0) = ψ(¼) − log π ≈ −5.37 < 0 and the sum is ≥ 0, so the residue is **strictly negative at τ₀ = 0 for every N** (F̂₀(0) > 0). With the Prop 5.5 argument (valid for finite combs, whose K is ℓ¹ on G for σ > 1), Φ^{(a)}_σ(ι(0)) → −∞ as σ ↓ 1: every truncation fails D(σ) for σ close to 1, for every fixed profile. Recommend adding as Cor 6.3′ (PROVED modulo the σ>1 continuation for finite combs, which is routine). |
| Prop 6.4 | CONFIRMED | |
| ARGUED caveat (Epstein/DH not excluded by regularity) | **FIX (direction wrong)** | DH (conductor 5, Γ_ℝ(s+1)) and Epstein (Γ(s), conductor √\|D\|) do NOT have ζ's archimedean factor, so with the fixed m of ℚ the line identity m + 2Re L′/L(½+iτ) ≡ 0 FAILS for them (log-conductor and ψ-shift mismatch): regularity does exclude them. Conversely, the line identity forces L_a(w) + L_a(1−w) = −γ(w) − γ(1−w), i.e. f = exp(−∫L_a) satisfies ζ's FE; by Hamburger's theorem (CITED; needs meromorphy/finite order) f = cζ. So regularity at σ = 1 is *more* Λ-specific than stated: CONDITIONAL rigidity under a finite-order continuation hypothesis on L_a. Rewrite §4 of NT_007 and §2 "Reading" accordingly. |

## NT_007
| item | verdict | notes |
|---|---|---|
| Thm 7.1 V(τ₀) = −(F̂₀²ℓ′)′/ζ(2) + Re ℛ₁ | CONFIRMED | Checked: dF̂₀(z)²/dσ = −2iF̂₀F̂₀′; M = −2iℓ′ (ℓ′ = −Im ζ′/ζ); dM/dσ = 2Re(ζ′/ζ)′ = −2ℓ″; ∂_σG = −2(F̂₀²ℓ′)′; limit ∂_σG/(2ζ(2)) ✓. Spike sign near a line zero ✓. |
| Cor 7.2 (𝒱), domain off zeros | CONFIRMED (implication from D) | Uses Prop 5.5 + NT_002 Cor 2.8 measure form (δ > 1) and continuity of Φ^{curve} at σ = 1 for fixed τ₀ off zeros ✓. Floor c_σa₀ → 0, so only V ≥ 0 survives ✓. |
| Prop 7.3 split (a)/(b) | CONFIRMED | D(σ) ⟸ (a)∧(b) via density + continuity + NT_003 Thm 3.4; for σ > 3/2 (range < 7/2, see FIX) D(σ) ⟺ (a). (b) OPEN, honestly labelled. |
| Admissibility table, W-tail row | **FIX** | "W-tail combs satisfy D(σ) for σ > 1 when a₀ is large depending on n₀" is false uniformly in σ: for finite combs Gershgorin constants blow up as σ ↓ 1, and by the strengthening of Thm 6.3(ii) above every truncation fails D(σ) near σ = 1 for any fixed profile. Correct statement: for each σ > 1 there is a₀(σ, n₀) (equivalently σ ≥ σ₀(F₀, n₀) > 1). Also W-tail combs are generally infinite; Gershgorin claim proved only for finite ones. |
| Other rows (Chebyshev, PNT/dlVP, FE, integrality) | CONFIRMED | cor:void statements are about proofs of D itself; their use for σ > 1 does not conflict. |
| §4 Epstein/DH caveat | FIX | see NT_006 row above. |

## Novelty vs corpus and literature
- Thm 5.1: Bohr–Jessen/Bagchi-type density of t ↦ (p^{−it}) in 𝕋^∞ — classical; new only as applied to Φ_σ. Thm 5.2 + Prop 5.3: summation-formula decomposition of Dirichlet-series test forms; standard technique (Euler–Maclaurin, Mellin), new in this frame (corpus grep consistent with the memos' check: L2_025/L2_026 differ).
- Thm 6.1: FE log-derivative identity is classical (cf. Weil explicit formula; corpus 108_91, R160_PD_R1 Lemma 2.1). New: its role as odd main factor of the height flow and regularity at σ = 1. Thm 6.3 is a genuinely new consistency/falsifier statement in the frame; it is consistent with cor:void (finite modifications fail).
- Thm 7.1/(𝒱): expressions with (log|ζ(½+it)|)″ appear in the literature (e.g. convexity/monotonicity of |ξ| on the line); the weighted form with F̂₀² and the remainder ℛ₁ is new in the record. Novelty modest; not a sign result.

## Overall
No error in the core identities (Thm 5.1, 5.2 main term, 6.1, 6.2, 6.3, 7.1, Cor 7.2). FIXes: σ < 7/2 range (NT_005), E^A bound exponent, Prop 5.5 wording, Epstein/DH caveat reversed (Hamburger rigidity), W-tail admissibility row. One strengthening found: truncations fail D(σ) near σ = 1 (residue negative at τ₀ = 0). No sign contact. Row D OPEN.

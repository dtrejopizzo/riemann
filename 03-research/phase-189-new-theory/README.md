# Phase 189 — A new theory aimed at the near-coincidence part of row D: the two-metric group and the height flow

Started .
Pen and paper only. Neutral names: "two-metric group", "height flow", "denominator damping", "centre collapse".
Paper 47 and the master grid are NOT edited by this phase (phase 188 is integrated separately).

## The object
D ⟺ the Weil kernel K(r) = B_{F₀}(log r) is positive definite on the discrete group G = ℚ_{>0} (phase 188: A_M ⪰ 0 ∀M).
The sign lives in Near: ratios r close to an integer n but of large height.

## The new structure
- **Two metrics on G:** ℓ(r) = |log r| (archimedean) and h(r) = log H(r), H(a/b) = ab (height). Product formula: ℓ ≤ h, equality
  exactly on ℕ ∪ ℕ^{−1} (where Div lives); h − ℓ = 2 log den(r). Near = small ℓ, large h.
- **Height flow:** K_σ := K·H^{−σ} = (real damping e^{−σℓ}) × (denominator damping den^{−2σ}); h is conditionally negative definite,
  so the flow is positivity-preserving and every finite-section bottom is nondecreasing in σ. D = D(0) = ∩_{σ>0} D(σ).
- **Bohr symbol:** Φ_σ(θ) on 𝕋^∞ = Ĝ; the damping kernel is the Euler product |L(σ, χ_θ)|²/ζ(2σ); D(σ) ⟺ (for σ > 3/2) Weil positivity on the
  Dirichlet-series tests Σχ(m)m^{−σ}τ_{log m}F₀; Div becomes −2Re L′/L(½ + σ, χ_θ).

## Memos
| memo | content | main labels |
|---|---|---|
| NT_001 | two-metric group, height flow, monotonicity, σ*(a), falsifiers separated, first-contact lemma | PROVED (Thm 1.1 corpus-known) |
| NT_002 | Bohr symbol, coprime/Euler identity, Euler-vector criterion, Harnack contraction c_δ = ζ(2δ)/ζ(δ)², necessary floor, **base theorem: D(σ) for σ ≥ 3/2 + O(T₀/log(1/T₀))** | PROVED (class-level); constants implicit |
| NT_003 | phase diagram: lines 3/2 (Chebyshev/absolute), 1 (ℓ²/robustness), ½ (Kakutani, ℓ²-failure); random Steinhaus Weil-chaos positivity for σ > 1; amplification tolerance > 0 above 1; every positive amplification fails below ½ | PROVED / CONDITIONAL (on D and centre criticality) + ARGUED |
| NT_004 | centre collapse identity ((Λχ)*1 replaces Λ exactly on Euler tests at exponent ½), ζ-test positivity c_A N, twisted collapse = correlations χ(a)χ̄(a+h); NO-GO as sign carrier | PROVED / NO-GO |

| NT_005 | curve reduction (σ > 3/2: min over torus = inf over curve); exact curve formula = coprime counting ζ(2σ−1)/ζ(2σ) × Re[F̂₀(z)²(m + 2ζ′/ζ(w))] + discreteness remainder; continuation | PROVED |
| NT_006 | FE in the flow: main factor = F̂₀²[ζ′/ζ(w) − ζ′/ζ(1−w)], odd under σ ↦ 2−σ; ℓ² line σ = 1 is the fixed line; curve symbol regular at σ = 1 for Λ, pole for every finite modification/truncation (Λ-specific) | PROVED (FE CITED) |
| NT_007 | value on σ = 1: V = −(F̂₀²(log|ζ(½+iτ)|)′)′/ζ(2) + Re ℛ₁; D ⟹ V ≥ 0 (inequality 𝒱); P189.1 = curve positivity (a) + off-curve regularity (b, OPEN); admissibility table | PROVED / OPEN |
| NT_008 | ℛ₁ explicit: = a₀ − 2Re(−ζ′/ζ)(3/2+iτ₀) + O(√T₀ log(1/T₀)) on |τ₀| ≤ C/T₀ (sparse scales = integrality) | PROVED (routine bookkeeping) |
| NT_009 | weak (𝒱) unconditional at resolution (T₀log(1/T₀))^{1/3}, margin ½a₀; pointwise (𝒱) ⟸ one-sided convexity bound on log|ζ(½+iτ)| (OPEN) | PROVED / OPEN |
| NT_010 | σ-derivative at 1: V₁ = −(2/ζ(2))(γ−ζ′/ζ(2))X + Re∂ℛ; D ⟹ strict (𝒱); positivity does not propagate upward; (b) ⟺ uniform convergence of the flow | PROVED (one ARGUED bound) / OPEN |
| NT_011 | ℓ″ sign split (Hadamard): positive part only from off-line zeros within |δ|; model ζ̃ = ζ·R (same FE, same line identity, moments within O(δ), ℓ̃″ +3/(2δ²)) ⇒ NO-GO for pointwise (𝒱) in class FE + line identities + mean values | PROVED / NO-GO |
| NT_012 | weak (𝒱) at width K√(T₀ log(1/T₀)) (Titchmarsh §9.6 local formula); limit of the method | PROVED (CITED input) |
| NT_013 | part (b): reduction to Near; σ-collapse at general σ; sufficient |Ξ| ≪ e^{ϑu}, ϑ<½; partial-curve obstruction (ARGUED); NO-GO for absolute methods with sub-power PNT errors | PROVED / ARGUED / NO-GO / OPEN |
| NT_014 | part (b) ⟺ zero-free half-plane (forward PROVED, converse ARGUED) ⇒ NO-GO | PROVED / ARGUED / NO-GO |
| NT_SYNTHESIS | phase summary; remaining door = Euler product on the critical line (Target E) | — |

## Status
Row D: OPEN. No certified negative value; no sign contact. Proved range of the flow: σ ≥ σ₁(F₀) ≈ 3/2⁺ (class-level).
Value-sensitive band ½ ≤ σ ≤ 1: HEURISTIC reading of the CONDITIONAL NT_003 Thm 3.6 (referee downgrade).
Referee: NT_001_004_REVIEW.md — all PROVED labels stand; six fixes applied . All proved items are class-level.

## Next step (P189.1)
Prove D(σ) for all σ > 1 for one fixed narrow profile: the almost-sure positivity of the Steinhaus Weil chaos X_σ (NT_003 Thm 3.4)
in the class-robust but non-absolutely-convergent range 1 < σ ≤ 3/2, using PNT-level cancellation of Ξ inside the denominator-damped
Near sums (the 1/(σ − 3/2) term of NT_002 Thm 2.5 must be replaced by a cancellation estimate). Then attack the band ½ ≤ σ ≤ 1 along
non-Euler directions (NT_004 §4 reading: curve-character shift correlations).
| HOSTILE | NT_001_004_REVIEW.md: all PROVED items CONFIRMED; 6 FIXes (constants/ranges/citation scope), Thm 3.6 readings DOWNGRADED to heuristic; no sign contact |
| HOSTILE 5–7 | NT_005_007_REVIEW.md: core identities CONFIRMED; FIXes: σ<7/2 range, E^A exponent, Prop 5.5 wording, Epstein/DH caveat reversed (Hamburger), W-tail row; strengthening: truncations fail D(σ) near σ=1 (residue <0 at τ₀=0); no sign contact |
| HOSTILE 8–10 | NT_008_010_REVIEW.md: Thm 8.1/V₁/Prop 10.4 CONFIRMED; FIXes (A off-diag log, uniform-σ clause, Titchmarsh 9.6 citation + finite-part reading, Cor 10.2 CONDITIONAL, Prop 10.3 comparison); pointwise (𝒱) = local zero-exclusion (𝒞_zeros), identity/mean-value route NO-GO; no sign contact |
| HOSTILE 11–14 | NT_011_014_REVIEW.md: Thm 11.2 CONFIRMED (𝓜 must exclude holomorphy/Hadamard: R has 4 off-line poles), Thm 12.1/13.2/13.3/14.1 CONFIRMED; Prop 12.2, 13.5, NT_014 converse/⟺ → ARGUED; synthesis §4 HEURISTIC; Target E σ-transport route EXCLUDED (L2_026/027, NT_014, cor:void); no sign contact |

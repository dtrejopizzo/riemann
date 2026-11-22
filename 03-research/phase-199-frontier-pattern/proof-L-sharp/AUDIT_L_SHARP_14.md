# AUDIT_L_SHARP_14 — audit of PROOF_L_SHARP_CC_001 (uniform prolate envelope, layer diagonal)

Phase 199,
Script: `AUDIT_L_SHARP_14_check.py` (Bouwkamp tridiagonal for ϑ_k; Taylor series at t = 1 for the regular solution with ψ(1) = 1;
DOP853 to t = 60 with analytic tail; all checked quantities are scale-invariant, so no eigenvector of the concentration problem is needed;
½(1−χ_k) = ∫_1^∞ψ² by evenness + L²(ℝ) normalisation).

## Verdict: ACCEPTED WITH ERRATA. Theorem C(iii) label: **PROVED under explicit hypotheses** (ϑ_k ≤ c²/4 and c large enough that the η-bound is < 1, i.e. c ≳ 820 (N ≳ 130) for k = 0), errata below; for 200 ≤ c < 820 the statement is PROVED but **vacuous** (|η|-bound ≥ 1); at N = 15 (c = 94.2) it is NOT covered (|e₁|-bound > 1).

## Item by item
1. **Conventions.** ODE on t > 1: −[((1−t²)ψ′)′ + (ϑ − c²t²)ψ] = ((t²−1)ψ′)′ + (c²t² − ϑ)ψ = 0. P = (t²−1)(c²t²−ϑ_k) uses the
   **differential** eigenvalue ϑ_k, and χ_k only enters via the mass ½(1−χ_k). Correct. OK.
2. **(2.1)** a′ = εa + Ωb, b′ = −εb − Ωa, (log G)′ = 2ε cos 2φ, φ′ = Ω − ε sin 2φ: re-derived. PROVED.
3. **(2.2)** ρ(sin 2φ)′ = 2ε cos 2φ − ερ sin 4φ: re-derived. PROVED.
4. **E decreasing.** E′ = 2ψψ′ − 2ψψ′ − (pψ′)²P′/P² ≤ 0 (P′ > 0 since q > 0 under ϑ < c²); E(1+) = ψ(1)² since (pψ′)²/P = pψ′²/q → 0.
   PROVED; numerically E monotone on all 7 runs. (Bonus: ψ(1)²/G_∞ → π/2 numerically, consistent with J₀ asymptotics.)
5. **§3 bounds.** (i), (ii) (t·P^{−1/2} decreasing; second term unimodal, TV ≤ 2·max), (iii) incl. the integrals
   ∫s p^{−3/2} = p^{−1/2}, ∫ds/(s√p) = π/2, ∫√p/s³ = π/4: all re-derived. PROVED.
6. **Thm CC.1.** Sign bookkeeping x = ρ sin 2φ + ∫ρ′sin 2φ − ∫ερ sin 4φ correct; coefficients 2.5γ/2 = 1.443 ≤ 1.45,
   γ³(3/2+π/2)/2 + γ⁵π/16 = 2.767 ≤ 2.77. PROVED. Numerics: max|x|/σ ∈ [0.32, 0.37] (bound valid, ≈3× generous).
7. **1.57 (Langer).** √γ·e^{σ/2} at z = 2, c = 200: 1.0746·e^{0.369} = 1.555 ≤ 1.57. PROVED. Observed max ratio 1.00–1.07.
8. **10.3 (Bessel zone).** z < 2: √35·√3 = 10.25; z ≥ 2: 1.57·√1.5 = 1.92. PROVED. Observed 1.12–1.18.
9. **Lemma CC.2 (35).** ERRATUM (minor): κ = γ + γ⁴/(2c) ≈ 1.1591, not 1.156 (the √p ≤ γ/c bound on ζ ≤ 1 gives γ³√p/2 ≤ γ⁴/(2c) = 0.0044).
   Then E(ζ₁) ≥ 0.2582ψ(1)², G(t₁) ≥ 0.1789ψ(1)², ψ(1)² ≤ 34.7 G_∞ ≤ 35. Constant **survives**. Observed ψ(1)²/G_∞ = 1.571 (bound 22× generous).
10. **Normalisation C_c² = (2/π)(1−χ_k)(1+e₁).** Logic correct (mass law). Observed relative deviation −0.0065 (k=0), −0.016 (k=4),
    −0.068 (k=24, ν = 0.236), −0.0016 (c = 804): within e₁-bound, and visibly O(ν + log c/c), not O(log c/c) alone — the memo's
    "(1+O(log c/c))" in the summary line holds only for fixed k; for k ∝ c it is (1+O(ν)). Wording erratum.
11. **Lemma CC.3.** IBP form re-derived (m/Ω = W/q). PROVED; the explicit constants 0.27, 2.77, 2.01 checked only for order of magnitude
    (consistent with numerics, not line-checked).
12. **§6 table.** Row sums re-added: e₁: 5.14 log(c/2) + 106.2 ✓; e₂: 16.14 → 16.2, 417.1 → 417 ✓; η combination
    (e₂−e₁)/(1+e₁) ✓; 523 = 106.2 + 417 ✓. Bessel-zone row W=1: 35·(2/c²)·4c/π = 89.1/c ✓; W = 𝔴: actual ≈ 244/c at c=200 and
    → 267/c, so 374/c is a valid upper bound ✓. e^x−1 row 4.93 = 2·2.31·1.45·γ·(2/π)/… consistent ✓. ν-row: (1−ν)^{−1/2}−1 ≤ 0.77ν on ν ≤ ¼ ✓.
    **ERRATUM (substantive wording):** "At c = 200 the bound is meaningful but crude" is FALSE: at c = 200, |η| ≤ 9.1 (k=0), 20.5 (k=24);
    the bound is < 1 only for c ≳ 820 (0.88 at c = 900, 0.37 at c = 2000). At c = 94.2 (N = 15) |e₁|-bound = 1.35 > 1: not covered.
13. **CC.4 numerics.** η_actual = −0.023 (c=201,k=0), −0.019 (k=4), +0.007 (k=24), −0.050/−0.038 (c=94.2, k=0/4), −0.006/−0.005 (c=804).
    The statement is TRUE numerically with η ≈ O(log c/c) small; the proven bound is ~400× larger than the truth at c=200.
14. **Uniformity in k ≤ k₀(c).** The proof is uniform in k (only ν enters). But for k ∝ c, η-bound contains 1.54ν, which is O(1):
    "uniform" means a uniform *bound*, not an asymptotic (1+o(1)). Statement "η = O((log c + k)/c)" is correct as written. OK.
15. **Phase (d)** not used for (iii); (iv) remains unproved. Agreed.

## Resulting label for Paper 46 thm:ext-layer(iii)
**PROVED under explicit hypotheses** (ϑ_k ≤ c²/4, c ≥ 200, with the bound |η| ≤ (21.4 log c + 1.54ϑ_k/c + 523)/(c(1−|e₁|))),
with errata: κ = 1.159 (constant 35 unchanged); remove "meaningful at c = 200"; state that the bound is non-vacuous only for
c ≳ 820 (N ≳ 130), and that N = 15 lies outside. "(1+o(1)) for fixed k, N→∞" is PROVED. Any numerical use of (iii) at N ≤ 130 stays NUMÉRICO.
No sign of row D is claimed. Row D OPEN.

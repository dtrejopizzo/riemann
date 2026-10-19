# L2_BUILD_010 — The ζ′/ζ(½) lead for (E₀)/(Ω₀): exact criticality, no slack

## Corpus check
grep "ζ′/ζ(½) / zeta'(1/2) / 2.686 / regularized / frequency 0":
**phase-159 G2_B1_R1 (Lemma 2, classical)**: C₀ = m(0) = −2ζ′/ζ(½); "the complete comb is exactly critical
at the centre"; "Σ 2Λ(n)/√n" = −2ζ′/ζ(½) = −C₀ in the regularized sense. So the lead's constant is
corpus-known. New here: its exact role in 𝒯₀/(E₀), the proof that the zero-sum vanishes identically at
τ = 0 for ANY zero configuration (no location used), and the precise reason the correction is not controlled
by zero-free regions.

## 1. Identity on the critical line (PROVED; inputs CITED: Hadamard product of ξ, functional equation)
For real τ with ζ(½+iτ) ≠ 0, s = ½+iτ:
  2 Re(−ζ′/ζ)(s) = m(τ) − 2 Σ_ρ Re 1/(s − ρ)   (sum symmetric in ρ ↔ 1−ρ̄, absolutely convergent in pairs).
*Proof.* ξ′/ξ(s) = 1/s + 1/(s−1) − ½log π + ½ψ(s/2) + ζ′/ζ(s) = Σ_ρ 1/(s−ρ) (pairs ρ, 1−ρ̄; the constant B
of the Hadamard product satisfies Re B = −Σ Re 1/ρ and cancels in this pairing). On Re s = ½,
Re[1/s + 1/(s−1)] = ½/(¼+τ²) − ½/(¼+τ²) = 0 and Re ψ(¼+iτ/2) − log π = m(τ) (eq:m). ∎
**At τ = 0 the zero sum vanishes for every zero configuration:** for ρ = β+iγ and ρ′ = 1−ρ̄ = 1−β+iγ,
Re 1/(½−ρ) + Re 1/(½−ρ′) = [(½−β) + (β−½)]/((½−β)² + γ²) = 0. Hence −2ζ′/ζ(½) = m(0) = C₀ exactly
(ζ(½) ≠ 0). This is the corpus identity, now with the cancellation mechanism explicit.

## 2. What it gives for 𝒯₀ (PROVED)
For h_T as in 009 (ĥ_T = (τ²+¼)²|Ĝ₀|² ≥ 0, double zeros at ±i/2, concentrated at |τ| ≲ 1/T), the explicit
formula (CITED, Paper 45 Thm 8.4 / Paper 47 Thm Z) in the polar-annihilated form gives
  Σ 2Λ(n)n^{−1/2}h_T(log n) = (1/2π)∫ ĥ_T(τ) m(τ) dτ − Z_T,   Z_T := Σ_ρ ĥ_T(γ_ρ)  (γ_ρ = −i(ρ−½)),
i.e. 𝔞_T(φ₀) = Z_T (the polar terms vanish because ĥ_T(±i/2) = 0). The "regularized centre value" enters
only through (1/2π)∫ĥ_T m = μ₀(T)‖φ₀‖² (the archimedean term itself). Therefore:
 (a) **leading constant**: prime side / ‖φ₀‖² → m(0) = C₀ and μ₀(T) → C₀: the two sides of 𝒯₀ agree to
     leading order AND to every order in the curvature expansion at τ = 0, because they are the same
     integral (1/2π)∫ĥ_T m. There is no slack constant: (E₀) holds with equality at the level of all
     τ-local terms (in the polar-free normalisation: m^♯(0) = C₀+4 on both sides).
 (b) **the whole sign** of 𝒯₀ is the sign of Z_T(φ₀) = Σ_ρ ĥ_T(γ_ρ).
So the lead does not yield (E₀) strictly; it shows (E₀) is exactly critical, decided by the zero sum.

## 3. Can Z_T be controlled with zero-free information only? NO-GO (PROVED for the declared class)
Declared class 𝒞_zf: bounds on |Z_T(φ₀)| using only (i) no zeros with |γ| < 14, (ii) a zero-free region
β ≤ 1 − c/log|γ|, (iii) N(H) ≪ H log H.
(a) On-line zeros give ĥ_T(γ) ≥ 0. An off-line pair at height γ, distance δ = β − ½ ∈ (0, ½), contributes
    ĥ_T(γ−iδ) + ĥ_T(γ+iδ) = 2Re[(…)Ĝ₀(γ−iδ)\overline{Ĝ₀(γ+iδ)}](…), which can be negative, with modulus up
    to ≍ e^{2δT}·|γ|⁴·|Ĝ₀(γ)|²-scale; for the clamped mode Ĝ₀(γ) ≍ T·(γT)^{−3} at |γ| ≫ 1/T.
(b) Hence a 𝒞_zf bound must allow, at each height γ ≥ 14, an off-line pair with δ up to ½ − c/log γ, whose
    contribution has modulus ≍ e^{2δT}·γ⁴|Ĝ₀(γ)|² (ARGUED scale), not small compared with the size of
    𝔞_T(φ₀) itself; the class therefore cannot fix the sign of Z_T for large T. The load-bearing statement
    is cor:void's C_zeros clause (CITED; PROVED there by explicit modified weights): arguments using only
    such zero-location information decide no window T > 0.75.
(c) Using actual verified zeros up to H (CITED) controls Z_T only up to the tail beyond H: 009 §1(ii);
    thm:finZ is the matching certificate-level NO-GO.

## 4. Push to finite T — not possible along this lead
(Ω₀) at T is equivalent to Z_T(φ₀) ≥ 0 (§2b), with no constant slack. The finite-T correction is the entire
quantity. Nothing further follows from the centre value.

## 5. Review
- §1: correct; the pairing ρ ↔ 1−ρ̄ is the functional equation + reflection; convergence in pairs standard.
  The vanishing at τ = 0 is the reason C₀ = −2ζ′/ζ(½) — corpus-known identity, mechanism made explicit.
- §2: the explicit formula is used as an identity per test function (CITED), not as any equivalence
  between row D and other statements. (a) is the key negative finding: the "regularized constant" is
  the archimedean term, so it cannot provide slack.
- §3(b) estimates are schematic in the exponents (the draft chain is messy); the load-bearing NO-GO is
  cor:void (CITED). Label: NO-GO via cor:void; the explicit exponent bookkeeping is ARGUED.
- No sign certified; no negative value of 𝔞_T produced.
Verdict: lead examined rigorously; it closes negative (exact criticality, sign = zero sum, not controllable
by zero-free data).

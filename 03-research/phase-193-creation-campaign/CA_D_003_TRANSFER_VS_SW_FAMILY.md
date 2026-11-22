# CA_D_003 — Does Hardy-amplitude transfer (CA_D_001) explain positivity on the s_w family? And a pre-screen of the amplitude-one residual

Pen and paper. **No sign contact. No negative value for ζ.** Inputs: CA_C_005 (+review: criticality is established for the *span*, not
the smooth family), CA_C_006, EI_002 Thm 1, P46 prop:shape-family, CA_D_001–002.

## 1. Answer: NO. Theorem 1/1′ does not apply to the s_w family, for three exact reasons (PROVED)
The family is G_M = F₀ * Σ_m m^{−½}w(m/M)δ_{log m} ∈ P_T, with T = T₀ + ½log M and X′ = Me^{2T₀}. Its form is
Q_M = (1/π)∫F̂₀²|ζ_w|²Θ′_{X′} (EI_002 Thm 1).
(a) **Q_M is an amplitude-one statement.** G_M is itself a primitive test, and Q_M = 𝔞_T(G_M) is row D evaluated at G_M.
Theorem 1 evaluates 𝔞_T at 𝒵_{X′}F = FT⁻¹(F̂·Z_{X′}). That function is not compactly supported: it has a tail on [T,∞). For Q_M to be a
transferred value one would need F̂₀ζ_w = F̂·Z_{X′} with F ∈ P_T. Then F̂ = F̂₀ζ_w/Z_{X′} = F̂₀ζ_wZ_{<X′}/ζ, which has poles at the on-line
ordinates unless ζ_w vanishes there. It is not of exponential type. By CA_D_002 Thm 2 (vague closure ∩ P_T = {0}), G_M is not even a
limit of transferred tests. So positivity on the family is **not** explained by transfer.
(b) **The amplitudes differ.** Transfer needs amplitude |Z_{X′}| = |ζ|e^{−C_{X′}}. The factor e^{−C_{X′}} ≈ e^{−√2B_{X′}} suppresses the
central cell, and Theorem 1's positivity comes from that suppression (CA_D_002 Thm 2′). The family has amplitude |ζ_w| ≈ |cζ + polar|,
with no e^{−C} factor. At bounded height the polar term M^{½}|W(½−iτ)| dominates (EI_002 review), so the family puts O(M) mass exactly
on the central cell, where transfer is blind.
(c) **The phases do not match.** The transfer identity needs the test's phase to equal −Θ_{X′} (mod π). For the main part cF̂₀ζ the phase is
−θ (FE), which is the *archimedean* phase only. The partial-transfer identity that does hold is Theorem 1 at T₀ < ½log 2 (no comb,
Θ = θ, Cor 1.1):
  ∫θ′F̂₀²|ζ|² ≥ 2T₀∫F̂₀²(|ζ|² − 1) ≥ 0.  (PROVED)
Inserting it into Q_M with ζ_w = cζ + P_M + ρ_M (P_M the polar term) gives exactly
  πQ_M = c²[∫θ′F̂₀²|ζ|²] − c²∫(comb_{X′})F̂₀²|ζ|² + (terms with P_M, ρ_M).
The bracket is ≥ 0 by transfer. It is FE-class generic (Theorem 1″). It is also **not the critical part**: it is ≥ 2T₀c²∫F̂₀²(|ζ|²−1),
which is of order log M as soon as the test sees heights up to M, not M^{−3}.

**Note on mechanism (B).** The criticality CA_C_005 sees on the span cannot be attributed to the FE-generic transfer
positivity. Transfer supplies the archimedean–ζ piece with a large, non-critical margin. The cancellation to M^{−3} must happen among
−c²∫comb·F̂₀²|ζ|², the polar term P_M and ρ_M. All three live at bounded height, on the central cell, which is outside transfer's reach. So
(B) is **not shown to be FE-generic by CA_D_001**. Whether it is zero-side remains C's E6 question (endorsed as low value, (R)(4)).

## 2. The OPEN item: a ζ-specific amplitude-one statement on {Z_T² < 1}. Pre-screen
{Z_T² < 1} consists of (i) neighbourhoods of the on-line ordinates and (ii) the central cell and other comb-coherent sets.
| candidate | screen | verdict |
|---|---|---|
| (i) any statement localized at the ordinates γ (values F̂(γ), residues of Z_T′/Z_T) | it is a function of the zero set: (R)(4), C_zeros; M_m quartets separate it | **DEAD** |
| (ii-a) positivity of 𝔞_T restricted to tests spectrally supported on I_T | P_T has no such tests (exponential type, Nyquist width π/(8T) < π/T); a soft localization is "local on the negative set": (R)(5), W-loc (thm:nolocal) | **DEAD** |
| (ii-b) the centre packet γ = 0 | (E_γ) at γ = 0 is exactly critical (L2_010; P46 prop:Egamma-exact) | retry → **DEAD** |
| (ii-c) correlated: ∫_{Z_T²<1}Θ′Φ ≥ −∫_{Z_T²≥1}Θ′Φ, splitting by the transfer multiplier | the split by Z_T² is not a P_T operation (CA_D_002 §2.4); as a statement it is 𝔞_T(F) ≥ 0 itself: REF-D | **REF-D** |
| (ii-d) amplitude-one comparison through the unimodular factor e^{−iΘ} = Z_X/Z_T (a spectral first moment of F*ε, ε = FT⁻¹(e^{−iΘ})) | ε is two-sided; first-moment positivity of F*ε is D1 of CA_D_000 (a coordinate, (B″), linear in Θ) | **coordinate** |
No candidate survives the (R)(4)/(R)(5) pre-screen. The residual identified in CA_D_002 is therefore not a new open route. It locates
where row D lives in the phase picture: the central cell, where the comb is coherent and transfer is blind. This coincides with the known
"exact at the centre" clause (R)(7) and with the (S)/near-coincidence residue (R9).

## 3. Self-review
1. (a) relies on CA_D_002 Thm 2, which uses Selberg (CITED) only inside a NO-GO. ✓ Without it, the type argument still excludes exact
   equality F̂₀ζ_w = F̂Z_{X′}: F̂ would have poles at ordinates where ζ_w ≠ 0. That ζ_w is nonzero at some ordinates is ARGUED; it is needed
   only for exact equality.
2. (c): the "large non-critical margin" of the bracket is a lower bound by 2T₀c²∫F̂₀²(|ζ|²−1). That this is ≫ M^{−3} needs
   ∫F̂₀²(|ζ|²−1) > 0, which is ρ_{F₀} = ‖R_{F₀}‖² > 0 and holds for F₀ ≠ 0 since R_{F₀} ≢ 0. ✓ Its size relative to the other terms is ARGUED.
3. No statement about λ_A. No (R) clause moved. ✓

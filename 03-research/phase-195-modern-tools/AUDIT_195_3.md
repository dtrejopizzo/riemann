# AUDIT_195_3 — audit of INV_S_001 and INV_T_001 (phase 195)

Checked against Paper 46 main.tex: def:PD (l.622), prop:weak, thm:D1, def:W (l.1179), thm:Z (l.1194), thm:A (l.398), thm:margin + cor:margin1 (l.3485–3534), prop:env, sec:spec / lem:spec-collapse (l.8941–8954), Introduction l.142–166 (thm:log5A); INV_R_001 (R1) and AUDIT_195_2.

## (a) T1 gauged identity — VERIFIED; "exactly (ν,β) of def:PD" — CORRECTED
- Green: Δ|f|²=4|f′|² for holomorphic f, outward normals, decay in τ ⇒ ∫_{½}∂_σ|f|² = ∫_{σ_1}∂_σ|f|² − 4𝓓(f). Subtracting for f=I_2Φ, I_1Φ and using |I_1|=|q|=1 on the line gives (T1) with the stated constants. PROVED (holomorphy of q is not even needed for the identity itself).
- Admissibility on C_c^∞(I_T): autocorrelations F⋆F̃ span (by polarization) a dense subspace of C_c^∞((−2T,2T)), so band-equality ⟺ the Fourier transform of ψ_q − s_T vanishes on the open interval (−2T,2T). Correct.
- **Overstatement.** The resulting freedom is ν̂ for ν a *tempered distribution* (even) with supp ν ⊆ {|u|≥2T}. def:PD requires ν a *finite even signed Borel measure*. So the gauge freedom strictly contains the def:PD freedom; "exactly" is false as stated. Correct statement: the gauge freedom is the distributional closure of the (ν,β) of def:PD; on 𝒫_T the β-part is as claimed. The value-level identification is restored by thm:D1 (finite atomic certificates already reach λ_P), see (d).
- Sign convention: ψ_q := ∂_σlog|q| at σ=½; then LHS(T1)=(1/2π)∫ψ_q|F̂|², and admissibility is ψ_q ≡ s_T (=2∂_σu_S of L1). Consistent.

## (b) T1′ entire gauge q_T — VERIFIED (and simpler than the memo's proof)
Direct computation on s=½+iτ: n^{−s}−n^{s−1} = −2i n^{−½} sin(τ log n), so the exponential factor is unimodular; ∂_σRe(n^{−s}−n^{s−1}) = −2 log n · n^{−½}cos(τ log n), giving −v_n cos(τ log n) after the factor Λ(n)/log n. With γ_∞=Γ_ℝ(s)/Γ_ℝ(1−s): ∂_σlog|γ_∞| = Re ψ(¼+iτ/2) − log π = m(τ). Hence ∂_σlog|q_T| = s_T **exactly** (not only band-equal). γ_∞ is holomorphic on σ>0 (zeros at s=1,3,…), |γ_∞|≍|τ|^{σ−½} uniformly on bounded strips, so T1's hypotheses hold for every σ_1>½. PROVED. q_T is a holomorphic rewriting of the symbol; it carries no information beyond s_T (lem:spec-collapse).

## (c) T3 NO-GO — VERIFIED with a CITATION ERROR
(a),(b) correct: |q|≤1 near the line and =1 on it ⇒ ∂_σlog|q| ≤ 0 ⇒ 𝔞_T(F) ≤ 0 on the admissible class.
(c) cites **thm:A** for λ_A(T)>0 at T≤log 2. thm:A is the Lévy-energy representation and proves no positivity. The correct internal source is **thm:log5A** (certified: λ_A ≥ 2.5·10⁻¹² for 0<T≤½log5), plus the classical case T≤½log2 (Yoshida/Bombieri, CITED). With this fix the NO-GO is PROVED for every T ≤ ½log5 (not only ≤ log 2); for larger T it is CONDITIONAL on the standing positivity premise (memo says so; label should read CONDITIONAL, not PROVED).
Energy orientation example: q=e^{ε(s−½)}, ψ_q=ε; by T2, 𝓓(G_λ)−𝓓(qG_λ) → π·(1/4π)∫2ε|F̂|² = (ε/2)∫|F̂|²dτ. VERIFIED. Expansive lowers the localized energy; the "contractive ⇒ energy domination" heuristic has the wrong orientation. Confirmed.

## (d) T4 — (⇒) VERIFIED with a cleaner route; (⇐) UPGRADED for finite-atomic certificates
(⇒): if log|q| ≥ c(σ−½) one-sidedly then ψ_q ≥ c, and (T1) gives 𝔞_T(F) ≥ c‖F‖² directly for F in the admissible class — no appeal to def:PD needed; density gives c ≤ λ_A. The claim "c ≤ λ_P" needs ν to be a finite measure (else only a generalized certificate); state c ≤ λ_A.
(⇐), new, PROVED for finite-atomic certificates f = s_T + Σ2a_j cos(u_jτ) + β·ĝ ≥ c′ > c (these exist with c′ → λ_P by thm:D1): put G(τ)=∫_0^τ f, ℓ(s) := iG(−i(s−½)). G continues holomorphically to |Im| < ½ (m(τ)=Reψ(¼+iτ/2)−logπ is analytic for |Im τ|<½; cosines and ĝ_j are entire of exponential type), Re ℓ=0 on the line, ∂_σRe ℓ = f there, Re ℓ = (σ−½)f − (σ−½)³f″/6 + … with f″ bounded, so log|q| ≥ c(σ−½) on a uniform layer; |q|=e^{Re ℓ} has polynomial growth in |τ| (from the τlogτ growth of ∫m). So q=e^ℓ is an admissible expansive gauge of value c.
**Consequence:** sup{c : admissible expansive unimodular gauge of value c} = D_T = λ_P. PROVED (combining (⇒), (⇐)-finite-atomic, thm:D1).

## (e) Track S
- N_T on (½log3,½log5) = {2,3,4}, v_2=√2 log2, v_3=(2/√3)log3, v_4=log2: VERIFIED.
- S1: linearity of the transform; archimedean singular data on iπℤ (poles of K), prime atoms at ±log n; place-additive. VERIFIED (elementary). Correctly reduces 𝒦_St to the INV_Q/INV_R phenomenon.
- S2 closed form: ψ(¼) = −γ−π/2−3log2; ψ(¼)−logπ = −5.372183…; Σv_n = 2.941974…; total −8.314157… (mpmath, NUMÉRICO). VERIFIED. Proof: monotonicity of Reψ(x+iy) in |y| (series formula) and min-max with codim-2 constraint — correct. Parter–Widom T^{−2} expansion ARGUED, as labelled.
- S3: In thm:margin the constant 21 is the cutoff just below γ_2 = 21.022 (only ρ_1 is killed by ϖ, by (Z1)); 42/e comes from optimizing k in (k/21T)^{2k} (cor:margin1). Replacing ϖ by a polynomial killing all ordinates ≤ Γ (verified on the line below H_PT) gives (k/ΓT)^{2k} → e^{−2ΓT/e}, with Γ-dependent constants and the e^T(Γ/H_PT)^{2k} off-line term still negligible. ARGUED (confirmed plausible; constants C_Γ not checked). thm:margin itself is only an upper bound and nowhere in main.tex is 15.449 called a sharp or intrinsic rate (grep: l.89, 256, 3519, 3538, 4126, 6810, 7093, 8548, 8666–8680, 8866–8872, 9138, 9178 all read "≤ 4·10⁹Te^{−15.449T}").
- **Recommendation (paper NOT edited):** add a footnote to cor:margin1: "The exponent 42/e reflects the test family of Lemma testfam (one factor ϖ killing ρ_1, cutoff 21 < γ_2); killing all ordinates up to Γ < H_PT gives exponent 2Γ/e with Γ-dependent constant. The rate is a property of the test family, not of λ_A." Optional, clarifying only; no statement is wrong.
- §4 "proved partial statement" is exactly step (4) of thm:margin; memo says so. §1 "no semiclassical parameter" is a remark, not a theorem. Verdict NO-GO 𝒦_St CONFIRMED.

## (f) "Every Green/gauge identity method on the strip is exactly def:PD"
- PROVED in the class 𝒦_gauge := {sourceless Green identity (T1), F-independent unimodular holomorphic gauges with polynomial growth, lower bound obtained from a pointwise bound ψ_q ≥ c}: the values reachable are exactly the certificate values, sup = λ_P (d). Admissible gauges correspond to distributional ν (⊋ def:PD), with values ≤ λ_A.
- ARGUED outside that class: F-dependent gauges, sourced identities (Blaschke = L3/R162_2201, already indexed), and bulk-energy bounds not routed through a pointwise ψ_q (T2 makes bulk = line flux, which strongly suggests nothing new, but not a proof in a declared class).
- FALSE as literally stated ("exactly … def:PD" at the level of the freedom) because of the measure/distribution gap.

## Verdict
INV_S_001: CONFIRMED (one recommendation for a footnote). INV_T_001: CONFIRMED with corrections — T3 citation (thm:A → thm:log5A), T3 for T>½log5 CONDITIONAL, "exactly def:PD" → distributional closure, T4(⇐) upgraded to PROVED for finite-atomic certificates. No sign. Row D: OPEN.

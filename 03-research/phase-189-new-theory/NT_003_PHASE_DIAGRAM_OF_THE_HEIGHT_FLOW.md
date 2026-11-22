# NT_003 — Phase diagram of the height flow: the lines σ = 3/2, 1, ½; random (Steinhaus) Weil positivity; amplification
# tolerance and value sensitivity

Phase 189, construction step 3. Notation of NT_001–002. Labels as there.

## Corpus check
grep "Kakutani" (phase 159 G1_* memos: Kakutani dichotomy for *Gaussian/product measures on zero configurations* — different
object), "Steinhaus" (D.187 Bohr–Rankin moments; R170_802 selection transfer; R160_D2_R2 — moments of Λ-chaos, no Weil-kernel
positivity), "multiplicative chaos" (grid rows: listed as REF only), "tolerance / amplification" (Paper 46 thm:finmod, cor:void;
N_021 Thm 2; R160_C5_R1 Thm 3.3 — class closure under finite modification), "centre exactly critical" (L2_010, N_013).
**New:** the regime lines of the height flow (Props 3.1–3.3), the Steinhaus formulation of D(σ) for σ > 1 (Thm 3.4), the
amplification-tolerance invariant and its positivity for σ > 1 (Thm 3.5), the value-sensitivity statement below the Kakutani
line (Thm 3.6, CONDITIONAL) linking the flow to the centre criticality of L2_010/N_013.

## 1. Three lines (PROVED unless marked)
**Prop 3.1 (the 3/2 line = absolute convergence = Chebyshev scale).** K_σ ∈ ℓ¹(G) for σ ≥ 3/2 unconditionally (σ > 3/2 by Lemma 2.0;
σ = 3/2 using the prime number theorem with any error term E(u) → 0 integrable against du/u… see the note below). More precisely,
writing Ξ(u) := Σ_n v_nc₀(u − log n) (main term ∫c₀(u − v)2e^{v/2}dv = 2e^{u/2}∫c₀e^{−w/2} = 0, Tate), the comb part of K is
½[Ξ(log r) + Ξ(−log r)] and, for any comb with |Ξ_a(u)| ≤ Ce^{ϑ|u|}: K^{(a)}_σ ∈ ℓ¹ for σ > 1 + ϑ and ∈ ℓ² for σ > ½ + ϑ.
*Proof.* Rationals with ℓ(r) ∈ [u, u+1] carry H^{−σ}-mass ≤ C e^{(1−σ)u}ζ(2σ−1) (count: for each den b, ≤ e^{u+1}b numerators,
H ≥ e^u b²); the archimedean part is summable for σ > 1 (Lemma 2.0 proof). ∎ (The ℓ¹ bound for σ > 1 + ϑ needs only this count.)
**Reading.** Unconditionally ϑ = ½ (Chebyshev) gives 3/2; any power saving ϑ < ½ in the smoothed prime count moves the absolute
line to 1 + ϑ. Under D, |K| ≤ a₀ (|B| ≤ B(0) for PD B), so ϑ = 0: ℓ¹ for σ > 1, ℓ² for σ > ½ (CONDITIONAL on D).
**Prop 3.2 (the ½ line, unconditional).** For σ ≤ ½, K_σ ∉ ℓ²(G) (for every comb: only B(0) = a₀ > 0 and continuity are used).
*Proof.* Pick δ > 0 with B ≥ a₀/2 on [−δ, δ]. Coprime pairs (a, b) with b ∈ (Y, 2Y], |a/b − 1| ≤ δ/2 number ≥ cδY² for Y ≥ Y₀
(lattice-point count with Möbius, CITED standard), each with H = ab ≤ 5Y² and |K| ≥ a₀/2. Dyadic block ≥ (a₀²/4)cδY²(5Y²)^{−2σ}
= c′Y^{2−4σ} ↛ 0 for σ ≤ ½. ∎
**Prop 3.3 (Kakutani line).** The probability measure Q_σ dθ (σ > 1) and its limit for ½ < σ ≤ 1 (product of the local Poisson
measures) is equivalent to Haar iff σ > ½ and mutually singular with Haar iff σ ≤ ½. Moreover Q_σ ∈ L²(𝕋^∞) iff σ > ½
(Σ_r H^{−2σ} = ζ(2σ)²/ζ(4σ)).
*Proof.* Kakutani's dichotomy (CITED) for product measures Π_p P_{ρ_p}dθ_p vs Π_p dθ_p: equivalence iff Π_p∫√P_{ρ_p} > 0; and
∫√P_ρ dθ/2π = √(1−ρ²)Σ_k binom(−½,k)²ρ^{2k} = 1 − ρ²/4 + O(ρ⁴); so iff Σ_p p^{−2σ} < ∞ iff σ > ½. ∎
So **σ = ½ is simultaneously** the ℓ² line of the damped Weil kernel (Prop 3.2), the Kakutani line of the damping measure, and the
exponent where the comb weights n^{−½} of the Weil form match the test weights (NT_004: only there does 1*Λ = log eliminate Λ).

## 2. Random Weil positivity for σ > 1 (PROVED)
**Thm 3.4.** For σ > 1 (unconditional ℓ² regime, Prop 3.1 with ϑ = ½ gives ℓ² for σ > 1):
  D(σ) ⟺ Φ_σ ≥ 0 Haar-a.e. ⟺ the random variable X_σ(χ) := Σ_{r∈G}K(r)H(r)^{−σ}χ(r) (L²-convergent) is ≥ 0 almost surely,
where χ is a Steinhaus random completely multiplicative function (χ(p) i.i.d. uniform on the circle). Moreover
  E X_σ = a₀,  Var X_σ = Σ_{r≠1}|K(r)|²H(r)^{−2σ},  and X_σ = ζ(2σ)^{−1}·lim_{N} 𝔞(Σ_{m≤N}χ(m)m^{−σ}τ_{log m}F₀) in L²(Ω)
along N → ∞ whenever the latter limit exists in L² (Prop 2.3 grouping).
*Proof.* Plancherel on 𝕋^∞; a measure with L² density is ≥ 0 iff the density is ≥ 0 a.e.; for K_σ ∈ ℓ², PD ⟺ the Fourier–Stieltjes
measure is ≥ 0 ⟺ density Φ_σ ≥ 0 a.e. ((⇐): Σs_xs̄_yK_σ(x/y) = ∫|Σs_xχ_θ(x)|²Φ_σdθ). Haar measure on 𝕋^∞ = law of a Steinhaus χ. ∎
**Reading (new kind of positivity).** For 1 < σ ≤ 3/2 the target D(σ) is the *almost-sure positivity of a multiplicative chaos*
built from the Weil kernel: E = a₀ > 0, fluctuations from the near-coincidence and divisor parts. The curve characters χ(n) = n^{−iτ}
(the only ones that see Arch and Near coherently, L2_028 §2(c)) form a Haar-null set and are invisible in this regime; Div becomes
a sum of independent local terms −2Re Σ_kΛ(p^k)p^{−k(½+σ)}χ(p)^k. The chaos becomes critical as σ ↓ ½ (Prop 3.3), where Steinhaus
Euler products at ½ + σ' approach the critical multiplicative-chaos regime (Saksman–Webb, Harper: CITED as context only).

## 3. Amplification tolerance and value sensitivity
**Def 3.0.** For σ and n₀ ≥ 2, tol(σ; n₀) := sup{c ≥ 0 : D_{Λ + c′1_{n₀}}(σ) for all |c′| ≤ c}.
**Thm 3.5 (σ > 1: positive tolerance from a margin; PROVED).** Let m(σ) := ess inf Φ_σ > 0 (σ > 1). Then
  tol(σ; n₀) ≥ m(σ)·n₀^{σ+½}/(2e^{2σT₀}(5T₀n₀ζ(2σ−1) + ζ(2σ))) > 0.
*Proof.* The perturbation ΔK(r) = −c′n₀^{−½}[c₀(log r − log n₀) + c₀(log r + log n₀)] (from v_{n₀} ↦ v_{n₀} + 2c′n₀^{−½}, factor ½ in B)
is supported on r within 2T₀ of n₀^{±1}; the Near count of NT_002 Thm 2.5 (with r = n₀ itself added) gives Σ_r|ΔK|H^{−σ} ≤
2|c′|n₀^{−½−σ}e^{2σT₀}(5T₀n₀ζ(2σ−1) + ζ(2σ)) < ∞ for σ > 1, and ess inf(Φ_σ + ΔΦ_σ) ≥ m(σ) − ‖ΔΦ_σ‖_∞. ∎
So for σ > 1 every D(σ) with a margin is *robust* under small finite modifications: the region σ > 1 is class-robust, and
cor:void-type closure does not by itself exclude class proofs there (it excludes only classes closed under *unbounded* amplification,
by NT_001 Thm 1.5(ii)).
**Thm 3.6 (below the Kakutani line every positive amplification fails; CONDITIONAL).** Assume D for Λ and the centre criticality of
L2_010/N_013 in the form (C₀): lim_{ε↓0} (1/2π)⟨σ_∞F̂₀², P_ε⟩ = 0 for the Poisson kernel P_ε(τ) = ε/(ε² + τ²) (the packet value of the
Weil symbol at the centre τ = 0 is 0). Then for every σ < ½, n₀ ≥ 2, c > 0: D_{Λ + c1_{n₀}}(σ) fails. In particular tol(σ; n₀) = 0 and
σ*(Λ + c1_{n₀}) ≥ ½ for every c > 0.
*Argument.* For β > ½ the vector s^{(β)} = (m^{−β})_{m≥1} ∈ ℓ², ‖s‖² = ζ(2β), and grouping by reduced ratio (Prop 2.3):
s^{(β)ᵀ}K^{(a)}_σs^{(β)} = ζ(2β)Σ_rK^{(a)}(r)H(r)^{−(σ+β)} (absolutely convergent for σ + β > 1 when |K| is bounded, i.e. under D for Λ
plus the compactly supported perturbation). Take β ↓ 1 − σ (> ½ since σ < ½), so σ′ := σ + β ↓ 1.
(i) Λ-part: Σ_rK(r)H^{−σ′} = (1/2πζ(2σ′))⟨σ_∞F̂₀², |ζ(σ′ + iτ)|²⟩, and |ζ(σ′+iτ)|² = P_ε(τ)/ε·(1 + O(ε + |τ|)) with ε = σ′ − 1
near τ = 0, bounded elsewhere against the decay of F̂₀²: the 1/ε coefficient is (1/2πζ(2))⟨σ_∞F̂₀², P_ε⟩ → 0 by (C₀), so this part is
o(1/(σ′ − 1)) (ARGUED: uniformity of the O-term against the distribution σ_∞F̂₀²).
(ii) Perturbation: Σ_r ΔK(r)H(r)^{−σ′} = −2c n₀^{−½}·½Σ_{r≈n₀}c₀(log(r/n₀))H(r)^{−σ′}; with r = a/b, H ≈ n₀b², the a-sum is a Riemann
sum: ≈ (φ(b)/b)·n₀b·(n₀b²)^{−σ′}∫c₀(w)e^{(1−σ′)w}dw, and Σ_bφ(b)b^{−2σ′} = ζ(2σ′−1)/ζ(2σ′) ~ 1/(2ζ(2)(σ′−1)). Since
∫c₀ = F̂₀(0)² > 0, (ii) ~ −c n₀^{−½}F̂₀(0)²/(2ζ(2)(σ′ − 1)) → −∞ (ARGUED: Riemann sums with coprimality, standard).
Hence the Rayleigh quotient → −∞. ∎ **Label: CONDITIONAL (on D for Λ and (C₀)) + ARGUED (two asymptotics).**
**Reading (HEURISTIC, downgraded by referee; not a criterion).** The height flow has a *value-sensitive band*: above σ = 1 the targets D(σ) are
robust under small finite modifications (Thm 3.5), below σ = ½ they are destroyed by every positive single-atom modification
(Thm 3.6), exactly because the Euler directions s^{(β)} then reach the pole σ′ = 1 where the centre packet of the Weil symbol is
probed — and for Λ that packet is exactly critical (L2_010, N_013). The band ½ ≤ σ ≤ 1 is where the arithmetic content of D must
enter the flow. This places the sign of D, inside the new theory, in a precise strip of the height parameter.

## 4. Phase diagram (summary)
| σ | kernel K_σ | damping measure | D(σ) | robustness |
|---|---|---|---|---|
| σ ≥ σ₁(F₀) (≤ 3/2 + O(T₀/log(1/T₀))) | ℓ¹, continuous symbol | a.c., continuous | PROVED (NT_002 Thm 2.5) | class-level |
| 3/2 < σ < σ₁ | ℓ¹ | a.c. | OPEN (min of an explicit continuous function) | robust (Thm 3.5) |
| 1 < σ ≤ 3/2 | ℓ² (uncond.) | a.c. | OPEN ⟺ a.s. positivity of Weil chaos (Thm 3.4) | robust given margin |
| ½ < σ ≤ 1 | ℓ² only under D | a.c. (Kakutani) | OPEN | value-sensitive band (single atoms not ℓ¹) |
| 0 < σ < ½ | not ℓ² (PROVED) | singular | OPEN; positive amplifications fail (CONDITIONAL) | not robust |
| σ = 0 | — | — | = D | not robust (cor:void) |

## 5. Review
- Prop 3.1 at σ = 3/2 exactly: requires Σ over r of |Ξ(log r)|H^{−3/2} < ∞, i.e. ∫|Ξ(u)|e^{−u/2}du < ∞ — this needs E(u) integrable,
  which holds with the de la Vallée-Poussin error E(u) ≪ exp(−c√u) (CITED). Statement for σ = 3/2 kept, labelled CITED-dependent. ✓
- Prop 3.2: correct and unconditional; note it says nothing about PD, only ℓ² (so no L² density). ✓
- Prop 3.3: Hellinger expansion computed by hand; Kakutani CITED. ✓
- Thm 3.4: the L² convergence of the m,k-double series is not claimed in general (only the grouped series). ✓
- Thm 3.5: needs m(σ) > 0, which is OPEN for σ < σ₁; the theorem is conditional on that margin — stated so. ✓
- Thm 3.6: genuinely conditional: D for Λ is used (|K| ≤ a₀) and (C₀) is the corpus's centre criticality (L2_010 CITED/PROVED identity
  −2ζ′/ζ(½) = C₀; N_013 CONDITIONAL on Hardy–Riesz summability CITED and a contour step ARGUED). The two asymptotics are ARGUED.
  It is NOT a sign claim for Λ; it is a statement about falsifiers inside a world where D holds. ✓
- Overreach check: "the sign lives in ½ ≤ σ ≤ 1" is a reading of Thms 3.5–3.6, not a theorem; labelled reading.
- No negative value of 𝔞_T for ζ certified. **No sign contact.**


## Erratum note (after NT_001_004_REVIEW)
Thm 3.5 constants corrected (ζ(2σ), n₀^{σ+½}); readings derived from the CONDITIONAL Thm 3.6 ("value-sensitive band") are HEURISTIC (referee FIX 5, DOWNGRADE).

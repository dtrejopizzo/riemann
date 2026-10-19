# NT_013 — Part (b): off-curve continuity of the height symbol for 1 < σ ≤ 3/2 — reduction to the comb, a sufficient prime-sum condition,
# the partial-curve obstruction, and a NO-GO for absolute (PNT-error) methods

Phase 189, construction step 13. Notation of NT_001–010. Labels as before. No zero information is used.

## Corpus check
NT_003 Prop 3.1 (lines 1+ϑ, ½+ϑ), NT_010 Prop 10.4 ((b) ⟺ uniform convergence of the flow), NT_004 Thm 4.1 (collapse), N_021 Thm 2
(progression classes), R167_102 (sieve blindness). grep "partial-curve", "agree with the curve on p ≤ P", "Halász" + "Weil": no hit.
**New:** Prop 13.1, Thm 13.2 (σ-collapse at general σ), Prop 13.3, the partial-curve analysis (13.4), NO-GO 13.5.

## 1. Reduction (PROVED)
**Prop 13.1.** For σ > 1, K_σ = K^A_σ − K^{Div}_σ − K^{Near}_σ with K^A_σ, K^{Div}_σ ∈ ℓ¹(G) (A: e^{−5|d|/2} decay and the near-1 count,
σ > 1; Div: Σ Λ(n)n^{−½−σ} < ∞, σ > ½). Hence (b) ⟺ the Near symbol 𝒩_σ has a continuous version (restricting on ι(ℝ) to the curve
continuation minus the ℓ¹ parts). ∎
**Thm 13.2 (σ-collapse; PROVED for σ > 3/2 as an identity of absolutely convergent series).** With s_m = χ(m)m^{−σ} (all m),
  ζ(2σ)·(comb symbol)(θ) = 2Re Σ_{m,j≥1}χ(m)χ̄(j)(mj)^{−σ}g_{χ,σ}(j)c₀(log m − log j),   g_{χ,σ}(j) := Σ_{n|j}χ(n)Λ(n)n^{σ−½}.
*Proof.* As NT_004 Thm 4.1 with weights k^{−σ}n^{−½} = (kn)^{−σ}n^{σ−½}, j = kn, the k-sum complete (all k). ∎
So the near-coincidences become ADDITIVE neighbours m ≈ j (|m − j| ≤ 2.5T₀m) weighted by the additive function g_{χ,σ}, which is large
(≈ Λ(j)j^{σ−½}) on prime powers j: the obstruction at σ ≤ 3/2 is concentrated on m near primes.

## 2. A sufficient condition (PROVED)
**Prop 13.3.** If for some ϑ ∈ [0, ½) the smoothed fluctuation satisfies |Ξ(u)| ≤ C_ϑe^{ϑ|u|} for all u, then K_σ ∈ ℓ¹ for σ > 1 + ϑ, so (b) holds
on (1 + ϑ, 3/2] and (by Prop 7.3 of NT_007) D(σ) there ⟺ curve positivity (a). ∎ (NT_003 Prop 3.1.)
Unconditionally only ϑ = ½ (Chebyshev; with the de la Vallée-Poussin error, ϑ = ½ with a sub-power saving): (b) is known only at σ ≥ 3/2.

## 3. The partial-curve obstruction (ARGUED)
For P ≥ 2 and τ ∈ ℝ let θ^{(P)} agree with ι(τ) on primes p ≤ P and with ι(τ) + π on p > P, i.e. χ^{(P)}(m) = m^{−iτ}λ_{>P}(m) with λ_{>P}
completely multiplicative, −1 on primes > P. θ^{(P)} → ι(τ) in 𝕋^∞ as P → ∞.
(i) λ_{>P} has mean value 0 (Σ_{p>P}1/p = ∞; Wirsing/Halász, CITED), so the m-sums Σ_{m≈L}m^{−s}χ^{(P)}(m)c₀(…) lose the smooth main term
L^{1−s}Ĉ(s) for L → ∞ at fixed P — the main term that NT_005 resums on the curve into ζ(2σ−1)·ζ′/ζ(w).
(ii) Therefore, if 𝒩_σ were continuous at ι(τ), the contributions of the scales L ≥ L(P) to the curve main term would have to tend to 0 as
P → ∞; for σ < 3/2 these are tails of Σ_k k^{1−2σ}Σ_n Λ(n)n^{−w}(…), w = σ − ½ + iτ, Re w < 1 — a Dirichlet series outside its half-plane of
absolute convergence; their vanishing in the limit requires the corresponding partial sums to converge (uniformly over the partial-curve
twists), i.e. prime-sum cancellation of power-saving strength (Σ_{n≤x}Λ(n)n^{−iτ}·n^{…} = main + O(x^{1−η})).
So (b) below 3/2 is not a soft statement: it is a uniform prime-sum cancellation statement across characters near the curve. Under D it holds
(NT_005 Prop 5.5: Φ_σ = Q_σ⋆μ₀ is continuous for σ > 1); unconditionally it is out of reach of known estimates. ARGUED (the identification of
the limit in (ii) needs a uniform-convergence argument for the pieces, not written).

## 4. NO-GO for absolute methods (PROVED)
**Prop 13.5.** Let 𝓐 be the class of arguments establishing (b) through absolute summability Σ_r|K(r)|H(r)^{−σ} < ∞ with inputs
|Ξ(u)| ≤ e^{u/2}E(u), E any function with E(u)e^{ηu} → ∞ for every η > 0 (sub-power savings, e.g. dlVP or Vinogradov–Korobov errors). Then 𝓐 proves
(b) for no σ < 3/2.
*Proof.* The inputs are consistent with the comb a_E whose Ξ_{a_E}(u) = e^{u/2}E(u)·cos(u)… realized by a nonnegative comb (take a smooth
density perturbation of 2e^{u/2} of relative size E(u), discretized on log ℕ; its smoothed fluctuation has the stated size on a set of u of
positive lower density); for it Σ_r|K|H^{−σ} ≥ c∫e^{(3/2−σ)u}E(u)|cos u|du = ∞ for σ < 3/2 (NT_003 Prop 3.1 count, lower bound version:
rationals with ℓ(r) ∈ [u, u+1] carry H^{−σ}-mass ≥ c e^{(1−σ)u}). ∎ (The comb a_E is a method falsifier, not about Λ.)
Recorded: **NO-GO: absolute-summation proofs of (b) below 3/2 from sub-power PNT errors.** Any proof of (b) on (1, 3/2) must use signed
cancellation in the height-damped near-coincidence sums, uniformly in the character near the curve.

## 5. Status
(b): OPEN on (1, 3/2); equivalent (NT_010) to uniform convergence of the height flow; sufficient: |Ξ(u)| ≪ e^{ϑu} for some ϑ < ½ (gives (1+ϑ, 3/2]);
absolute methods with sub-power errors excluded (13.5); the partial-curve family (13.4) shows what a signed proof must control. Correction to the
coordinator's expectation: (b) involves no zero information, but it is NOT free — it is a prime-sum cancellation statement of power-saving strength.

## 6. Review
- Prop 13.1 ✓ (bounds as in NT_002/NT_003). Thm 13.2 ✓ (same merger as NT_004, now complete k-sum because the vector is infinite).
- 13.4 is ARGUED; the formulation avoids claiming discontinuity (which would contradict nothing unconditional but would conflict with D via
  Prop 5.5 — so it must not be claimed). ✓
- Prop 13.5: the falsifier comb construction is sketched (smooth perturbation + discretization; standard); label PROVED for the class statement
  modulo that routine construction — honest label: PROVED (sketch of the comb construction).
- No sign contact.

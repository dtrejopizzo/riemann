# NT_001–NT_004 — review

Pen and paper.
Verdicts: CONFIRMED / FIX / DOWNGRADE. Nothing outside this file and one README line was edited.

## Global verdict
The algebra and analysis are sound. No error invalidates a PROVED label. Four constant/range slips (FIX), one
citation to re-scope (FIX), two wording downgrades. **No sign contact; Row D OPEN** — the memos' own assessment is accurate.

## 1. NT_001
| item | verdict | note |
|---|---|---|
| Prop 2.1(i),(ii),(iv) product formula, h − ℓ = 2 log den | CONFIRMED | |
| Prop 2.1(iii) h is CND; H^{−σ} PD | CONFIRMED | Negative type of \|k−l\| on ℤ via −2∫(Σ_{x_i≤t}c_i)²; nonnegative sums; per-prime Poisson factor (1−ρ²)/\|1−ρe^{iφ}\|² ≥ 0. Classical (it is also the statement \|L(σ,χ)\|²/ζ(2σ) ≥ 0). |
| Thm 1.1 D ⟺ D(0) | CONFIRMED with FIX (citation) | The proof given (common denominator → A_M; Theorem S of L2_024/025 + 028 §1) is self-contained and correct. **R160_C5_R1 Thm 2.1 is NOT the same statement**: it is about a smeared datum φ_ε(x/y) built from a probe ψ, quantified over all ε (and per window), not about B_{F₀}(log r) for a fixed F₀. Re-word as "analogue (different datum)", rest on Theorem S. |
| Thm 1.2 semigroup, Thm 1.3 monotone section bottoms | CONFIRMED | (A−λI)∘P ⪰ 0 and P_ii = 1 ⇒ λ_min(A∘P) ≥ λ for A of any sign. Correct. |
| Thm 1.4 D = ∩_{σ>0} D(σ) | CONFIRMED | Continuity at σ↓0 is entrywise on each finite section (H(x/y)^{−σ} → 1); PSD cone closed. No uniformity needed. |
| Thm 1.5(i) | CONFIRMED | |
| Thm 1.5(ii) depth bound at 2 | CONFIRMED | c₀(±2log2)=0, c₀(0)=1 ⇒ ΔB(log2) = −c/√2 exactly; B(0) unchanged (2T₀<log 2). 2×2 section {1,2}, H(2)=2 ⇒ need 2^{−σ}\|B(log2) − c/√2\| ≤ a₀; the stated σ* ≥ log₂((c/√2 − \|B(log 2)\|)/a₀) is a valid lower bound (meaningful once c/√2 > \|B(log2)\| + a₀). Note B(log 2) may contain an n=3 term (log(3/2) < 2T₀ possible); irrelevant to the bound. |
| Thm 1.5(iii) | FIX (route) | Via NT_002 Thm 2.5 it is not clean: the displayed bound of Thm 2.5 carries a σ-independent C₁(1+a₀T₀²) and the cited thm:finmod falsifier is a statement about windows, not about B_a for this F₀. Correct, simpler route: use the comb a_c of (ii) itself (D_{a_c}(0) fails for c/√2 > \|B(log2)\| + a₀) and D_{a_c}(σ) for large σ by Gershgorin + dominated convergence (Σ_{r≠1}\|K^{(a)}(r)\|H(r)^{−σ} → 0, since H ≥ 2 and Lemma 2.0 gives summability). Statement survives. |
| Lemma 1.7 first-contact derivative | CONFIRMED | Requires attained contact on a finite section (stated). |

## 2. NT_002
| item | verdict | note |
|---|---|---|
| Lemma 2.0 | CONFIRMED | 2e^{−(d−2T₀)/2}·1.04e^{d+2T₀}·½ = 1.04e^{3T₀}e^{d/2}; coprime sum ≤ 2ζ(σ−½)ζ(σ+½), σ > 3/2. |
| Prop 2.1 (λ_inf = min Φ_σ, ℓ¹ case) | CONFIRMED | Standard (Plancherel on discrete G). |
| Prop 2.2 Q_σ = \|L(σ,χ)\|²/ζ(2σ), c_σ = ζ(2σ)/ζ(σ)² | CONFIRMED | Min of each factor at φ=π: (1−ρ)/(1+ρ); product = ζ(2σ)/ζ(σ)². Classical identity, new use. |
| Prop 2.3 Euler-vector criterion (Bohr averaging) | CONFIRMED for σ > 3/2 / FIX in README | Grouping (m,k)=(da,db) exact; absolute convergence ζ(2σ)Σ\|K\|H^{−σ}. The README states the equivalence without the range σ > 3/2; for 1 < σ ≤ 3/2 only the a.e./Steinhaus version (NT_003 Thm 3.4) holds. |
| Prop 2.4 𝒟_σ = −2Re L′/L(½+σ,χ) | CONFIRMED | |
| Lemma 2.6 a₀ ≥ ½log(1/T₀) − C | CONFIRMED | (modulo normalization 𝔞_∞ = (1/2π)∫mF̂², as used throughout the record). |
| Thm 2.5 base theorem | CONFIRMED with FIX | Near count: for fixed n,b, #{a ≠ nb: \|log(a/nb)\| ≤ 2T₀} ≤ 2nb(e^{2T₀}−1) ✓ (floors, a=nb excluded); reduced/non-reduced over-count argument ✓ (each r counted at its reduced rep, where H ≥ nb²e^{−2T₀}). Total ½·2·Σ_n v_n n^{1−σ}·5T₀e^{2σT₀}ζ(2σ−1) = 10T₀e^{2σT₀}ζ(2σ−1)(−ζ′/ζ)(σ−½) ✓; near σ=3/2 this is ~ 10T₀ζ(2)/(σ−3/2) ✓. Div 2(−ζ′/ζ)(½+σ) ✓, −2ζ′/ζ(2) ≈ 1.140 < 1.15 ✓. Arch near-diagonal C(a₀+1)T₀² ✓ (dyadic from b ≥ 1/(5T₀)). Arch far: K(u) = 2e^{−u/2} + 2e^{−5u/2}/(1−e^{−2u}), leading term killed by Tate ✓, \|A(d)\| ≤ 2e^{5T₀}e^{−5d/2} ✓. **FIX:** "2(e^{2T₀}−1) ≤ 5T₀ (2T₀ < log 2)" is false near 2T₀ = log 2 (LHS → 2, RHS → 1.73); it needs T₀ ≤ T_abs (which the theorem assumes) — correct the justification; same for 2.5T₀ in NT_004 Prop 4.4. Arch paragraph constants implicit: label "PROVED, constants implicit" honest. σ₁(F₀) ≤ 3/2 + CT₀/(a₀ − C′) follows. Class theorem, no sign — agreed. |
| Thm 2.7 Harnack contraction | CONFIRMED | Φ_{σ+δ} = c_δ∫Φ_σ + ∫(Q_δ−c_δ)Φ_σ, ∫Φ_σ = a₀, mass 1−c_δ. δ > 1 needed for Q_δ ∈ ℓ¹-coefficients/continuity ✓. |
| Cor 2.8 floor Φ_δ ≥ a₀ζ(2δ)/ζ(δ)² | CONFIRMED / FIX | Measure form for δ > 1 correct (Herglotz–Bochner on G). **FIX:** the "equivalently, 𝔞(Σχ(m)m^{−δ}τ_{log m}F₀) ≥ a₀ζ(2δ)²/ζ(δ)² for all δ > 1" uses Prop 2.3, valid only for δ > 3/2 (absolutely convergent test form); for 1 < δ ≤ 3/2 it is an a.e. statement in χ. Also "equivalently" → "in particular". |

## 3. NT_003
| item | verdict | note |
|---|---|---|
| Prop 3.1 (lines 1+ϑ, ½+ϑ) | CONFIRMED | Block mass e·e^{(1−σ)u}ζ(2σ−1) ✓; ℓ² uses ζ(4σ−1) ✓. σ = 3/2 endpoint: needs Σ_n Λ(n)/n-cancellation via Ξ and an integrable PNT error (dlVP, CITED) — CITED-dependent as stated. |
| Prop 3.2 σ ≤ ½ ⇒ K_σ ∉ ℓ² | CONFIRMED | Unconditional; only B(0)>0 + continuity. |
| Prop 3.3 Kakutani line | CONFIRMED | Hellinger: √(1−ρ²)Σ binom(−½,k)²ρ^{2k} = 1 − ρ²/4 + O(ρ⁴) ✓; Σ_p p^{−2σ} < ∞ ⟺ σ > ½ ✓; Σ_r H^{−2σ} = ζ(2σ)²/ζ(4σ) ✓. |
| Thm 3.4 Steinhaus chaos, σ > 1 | CONFIRMED | ℓ² for σ > 1 unconditional (ϑ = ½). PD ⟺ L² density ≥ 0 a.e.; EX = a₀, Var = Σ_{r≠1}\|K\|²H^{−2σ} ✓. The test-limit identification is hedged ("whenever the limit exists") — keep. |
| Thm 3.5 amplification tolerance | CONFIRMED with FIX (constants) | Correct count gives Σ\|ΔK\|H^{−σ} ≤ 2\|c′\|n₀^{−½−σ}e^{2σT₀}(5T₀n₀ζ(2σ−1) + ζ(2σ)) (the "+1" should be ζ(2σ); exact atom a = n₀b for all b). Hence tol ≥ m(σ)n₀^{σ+½}/(2e^{2σT₀}(5T₀n₀ζ(2σ−1)+ζ(2σ))). The printed n₀^{σ−½} is weaker but the "+1" makes it not a strict consequence; replace. Theorem is conditional on the OPEN margin m(σ) > 0 — stated. |
| Thm 3.6 (σ < ½) | CONFIRMED as CONDITIONAL + ARGUED; DOWNGRADE of its readings | Hypotheses: D for Λ and (C₀); two asymptotics ARGUED. Infinite vector s^{(β)} legitimate (absolute convergence for 2β > 1, σ+β > 1 ⇒ truncations converge). **Use check:** it is used nowhere as a criterion to close/rank routes inside the proofs. It IS used as guidance in: README "value-sensitive band (reading of Thms 3.5–3.6)" and "Next step", NT_003 §3 "Reading" and phase-diagram row, NT_004 §4 "Consequence … the sign must be sought along NON-Euler directions". These are planning readings; **DOWNGRADE the wording** "must be sought" → "a natural place to look (heuristic, from CONDITIONAL Thm 3.6)". It must never be used to discard a route. |

## 4. NT_004
| item | verdict | note |
|---|---|---|
| Thm 4.1 centre collapse | CONFIRMED | Two halves of the comb conjugate after a↔b ⇒ −Re Σ s_as̄_bΣv_nc₀(…); j = bn; c₀ ≠ 0 ⇒ j < ae^{2T₀} < 2N; n ≥ 2 ⇒ b ≤ j/2 < N: b-sum complete, **no truncation error** ✓. χ̄(b) = χ̄(j)χ(n) ✓; g_χ = (Λχ)*1 ✓. Close relative of N_022 §1 (1*Λ = log), new in the Euler-vector, near-coincidence-keeping form. |
| Thm 4.2 comb bounded (χ=1) | CONFIRMED | ∫f_a = a^{½}∫e^{−w/2}(log a − w)c₀ = 0 by the double zero of F̂₀² at ±i/2 ✓; c₀ ∈ C² ✓; EM error a^{−3/2}log a ✓. |
| Thm 4.3 𝔞(G_N^1) = c_AN + O(√N) | CONFIRMED (asymptotic); c_A > 0 "PROVED up to routine bookkeeping" acceptable | Titchmarsh 4.11 (uniform for \|τ\| ≤ N) ✓, cross term O(√N) ✓, tail \|τ\| > N negligible ✓. Positivity scaling: ‖G₀‖₁² ~ a⁸, ‖Ĥ₀‖² ~ a⁵, low part relative O(a^{3/2}) ✓. |
| Prop 4.4 | CONFIRMED with FIX | \|h\| ≤ 2.5T₀a needs small T₀ (see Thm 2.5 FIX). |
| Prop 4.5 NO-GO | CONFIRMED | (i) b-sum complete (b ≈ a/n₀), zero integral by Tate, EM error O((a/n₀)^{−3/2}), total O(n₀^{3/2}) uniformly in N ✓. (ii) residue-class splitting with P fixed ✓. NO-GO as sign carrier stands. |

## 5. Novelty (grep of 03-research, 04-papers, 05-meta)
- No prior hit for: height H(a/b) = ab or h = log H as a second metric on ℚ_{>0}; the multiplier H^{−σ} applied to the Weil kernel;
  "height flow"/"denominator damping"; ζ(2σ)/ζ(σ)² as a floor. (Only unrelated "height" hits: phase 68 gauge "height flow" wording,
  R157_006 Arakelov naive height, phase 103/104 log H(s) notation.)
- Steinhaus in corpus: D.187 (Bohr–Rankin moments), R160_D2_R2 (moments of Λ-chaos), G2_B7_R2 Thm C (Wintner, CITED), R170_802.
  None formulates PD of a Weil kernel as a.s. positivity of a chaos — Thm 3.4 formulation is new.
- R160_C5_R1: PD on ℚ_{>0} of a smeared datum φ_ε (Thm 2.1, 2.3, Example E Schur coupling with Liouville ω). NT_001 Thm 1.1 is the
  fixed-profile analogue; the PD-on-ℚ_{>0} framing is corpus-known.
- **Genuinely new (as organization):** the height flow with monotone section bottoms and depth σ*; base theorem D(σ) for
  σ ≥ 3/2 + O(T₀/log(1/T₀)); Harnack floor family; identification of the ½ line (ℓ²/Kakutani); chaos formulation; amplification
  tolerance; exact centre collapse on Euler tests with kept near-coincidences. **Mathematically standard ingredients**: Schur,
  Bochner/Herglotz, Kakutani, Euler products (Prop 2.2 is a classical identity). None carries sign; all PROVED items are class-level.

## 6. Summary of required edits (not applied here)
1. NT_001 Thm 1.1: re-scope R160_C5_R1 citation (analogue, different datum). 2. NT_001 Thm 1.5(iii): use a_c + dominated convergence.
3. NT_002 Thm 2.5 / NT_004 Prop 4.4: "≤ 5T₀", "≤ 2.5T₀" need T₀ ≤ T_abs, not 2T₀ < log 2. 4. NT_002 Cor 2.8: test-form version only δ > 3/2.
5. NT_003 Thm 3.5: "+1" → ζ(2σ), n₀^{σ−½} → n₀^{σ+½}. 6. README: add "σ > 3/2" to the Bohr-symbol equivalence; soften readings
derived from CONDITIONAL Thm 3.6 (also NT_004 §4 "must be sought").

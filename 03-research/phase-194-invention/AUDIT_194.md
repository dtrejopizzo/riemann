# AUDIT_194 — Review of INV_A_001, INV_B_001, INV_B_002 (phase 194)
 Pen and paper.
Checked against P46 def:PD (l.622), def:W + eq:nuw (l.1179–1190), thm:Z (l.1194), thm:shape (l.8853), and the ROUTES-TRIED-INDEX.
**No admissible sign step found in any of the three memos.**

## A. INV_A_001 (arithmetic Lévy structure)
| Item | Claimed | Verdict |
|---|---|---|
| (0.1) −Λ′/Λ Laplace form, C₀ = ½logπ + γ/2, compensator −e^{−2u} on J_∞ | PROVED | **CONFIRMED** (ψ(z) = −γ + ∫(e^{−t}−e^{−zt})/(1−e^{−t})dt, t = 2u; sign of −½ψ(s/2) checks). |
| (0.2)/(0.3) φ_σ inf. divisible, Lévy measure L_σ | PROVED | **CONFIRMED after the memo's own correction**: L_σ ~ 1/(2u²) at 0, so the uncompensated (0.2) diverges; only the Lévy–Khintchine form with drift −itb_σ is valid. The memo leaves the wrong formula in place with an inline "CORRECTION" — must be rewritten. Content is classical: Γ(σ+it)/Γ(σ) = char. fn of log-Gamma (CITED), ζ(σ+it)/ζ(σ) = Khinchine (CITED); product of char. fns. Not new. Already indexed as P60-1 (Lévy–Khintchine, PARTIAL) and CA_I_001 Thm 1 / audit item 88 (C2 Lévy–Khintchine per place). |
| Thm 2 rigidity 𝔐 = {J_ζ} | PROVED mod Hamburger | **CONFIRMED but RETRY**: identical to G5G-R162_2601c (Hamburger rigidity: atomic log-derivative + FE conductor 1 + finite order ⇒ cζ; PARTIAL, no sign) and N_009 (CONDITIONAL Hamburger). (M1) positivity and (M2) purity are not used in the proof beyond fixing the Γ-factor; Hamburger's hypotheses (Dirichlet series abs. conv. σ>1, (s−1)f entire finite order, FE with Γ(s/2)π^{−s/2}) are met. No new reason given ⇒ not a new route. |
| Cor 2.1 exclusions | PROVED / ARGUED | Epstein, ζ_K, L(χ) CONFIRMED (Γ-factor/sign of atoms). Quartets: CONFIRMED only for E with singularities left of σ = 1, ARGUED in general (as labelled). All overlap CA_I_001 Cor 6 / CA_H_002 Thm 2.2 separations (REF-D as a route). |
| Prop 4.1 (positivity for σ<0) | PROVED | CONFIRMED, trivial (conj of a char. fn is a char. fn). No content in 0 ≤ σ ≤ 1. |
| Prop 4.2 H odd about σ = ½ | PROVED | CONFIRMED (FE + real coefficients). It is CA_M_001 Prop 4.1 restated (memo says so). |
| Prop 4.3 damped form = symbol on line ½+ε | identity | CONFIRMED as definition (multiplying μ_T by e^{−ε|u|} = Poisson in τ). Caveat: c_Tδ₀ kept undamped is a choice; the "symbol on line ½+ε" equality holds only up to that polar/δ₀ bookkeeping (see Step 3). |
| Θ⁺ FALSE | PROVED | **CONFIRMED with a missing hypothesis**: needs T > ½log2 (else c_F(log2) = 0 and no prime atom is visible); Bernstein uniqueness used correctly. |
| Step 1 large-ε | OPEN/PROVED | comb bound needs ε > ½ (−ζ′/ζ(½+ε) finite); G1 (damped polar term) is real and uncomputed. |
| Step 3 "𝔞^{(ε)}+𝔞^{(−ε)} = 0 up to singular part" | identity | **BROKEN as stated**: the undamped c_Tδ₀ (and the polar terms) are not odd, so the sum is 2c_T‖F‖² + polar + singular, not singular alone. The "half-jump" formula is then the classical Sokhotski jump of Re ξ′/ξ across σ = ½ = zero measure — i.e. thm:Z (ii) read with a Poisson kernel. |

**Θ, G1–G3.** Θ (𝔞^{(ε)} ≥ 0 on 𝒫_T ∀ε ≥ 0) is **REF-D**: for ε > 0 it is positivity of the Poisson/Herglotz extension of the zero measure (index W1/REF-D: Kreĭn/de Branges/Herglotz, Thm Z). Note e^{−ε|u|} is NOT in 𝒲_T (not flat on [−2T,2T]), so Θ is not literally thm:Z — it is the Herglotz variant, also indexed. G2 "one-sided maximum principle": **circular** — H = Re ξ′/ξ is harmonic in ½<σ<1 only off zeros there; a maximum principle on the half-strip presupposes the absence of those singularities, which is the target itself (and unbounded strip needs Phragmén–Lindelöf growth not supplied). G3: genuine technical gap but only matters if G2 had content. Problem (R): fails (R)(4) (certificate on the zero side) and adds no Λ-dependent step ((R)(3)/(10)): the only ζ-specific input is rigidity, which is a separation, not an inequality.

## B. INV_B_001 (pair surface 𝒮)
| Item | Verdict |
|---|---|
| ⟨Γ_g,Γ_g⟩ = W(g∗g̃) = 𝔞_T(g) | **CONFIRMED but tautological**: pol: ∫∫g(a)g(b)2cosh((a−b)/2) = F̂(i/2)+F̂(−i/2) ✓; fin: δ-pairing gives Σ v_nF(log n) with v_n = 2Λ(n)n^{−½}, F even ✓; ℝ: A_ℝ is *defined* as the archimedean term. Exactly CA_F_003 Lemma 1 (memo admits). The "transversal meetings over ℕ×ℕ" derivation is HEURISTIC and actually wrong as a count: each reduced ratio a/b is met by infinitely many (bj,aj), weight (ab)^{−½}Σ_j 1/j diverges like log X, and the multiplicity is 1 per prime power, not log p — Λ is inserted by hand. |
| Sign convention | **INCONSISTENT**: §2 sets ⟨Γ_g,Γ_g⟩ = +𝔞_T, §3 states HI as −⟨D,D⟩_int ≥ 0 ⟺ 𝔞_T ≥ 0. One of the two must change. 𝒜^⊥ = {F̂(i/2)+F̂(−i/2)=0} equals 𝒫_T only for even F (fine here). |
| measure "dx dy/(xy)^{½}·(xy)^{−½}·xy = dx dy" | garbled; irrelevant to results. |
| h⁰_X = ∫F̂|ζ_X(½+it)|²dt/2π ≥ 0 | **CONFIRMED**, Bochner-trivial (F̂ = |ĝ|²). Leading growth X·∫F e^{u/2} is ARGUED (Euler–Maclaurin), not PROVED; on 𝒫_T it vanishes and the next term is F(0)log X + mean-value terms. |
| Step 1 at ½log3 | CONFIRMED (v_2F(log2) = √2 log2 F(log2); n = 3 at boundary). |
| HI_𝒮, CS, Nef, PRR-log | **RETRY**: HI via h⁰/RR = P134–148 / G1H-135 R135_007 "Hodge-index transfer theorem (cond. h⁰)"; CS = ES-21 / P33-6 (NO-GO); "Weil positivity vs Hodge index" = P40-3 (CIRCULAR); coupled infinite-prime Hodge index = G8H-R160_C7_R1 (REF-D). PRR-log is the missing h⁰ hypothesis of R135_007 renamed. The only new element is the explicit h⁰_X, which INV_B_002 then kills. HI_𝒮 restricted to N_T is literally 𝔞_T ≥ 0 on 𝒫_T: REF-D. |
| §5 Epstein "Γ_mΓ_n ≠ Γ_mn" | **ILL-POSED**: Γ_a are ratio graphs in ℝ_{>0}²; Γ_a∘Γ_b = Γ_{ab} holds for any weights. What changes for Epstein is the weight system, not the composition law. Separation claim must be restated on weights (then it is Thm 5 of phase 193: constructible ⇒ holds for x²+5y²). Beurling separation by the additive lattice is the semiring principle, stated, not proved. |

## C. INV_B_002 (PRR-log test)
| Item | Verdict |
|---|---|
| (a) dilation | CONFIRMED (substitution correct). |
| (b) log-convexity in k (Hölder) | CONFIRMED. Laplace asymptotic: max of |ĝ|² is not at 0 unless g ≥ 0; "F̂(±i/2) after contour shift" is meaningless (μ_X lives on ℝ). Remove. NO-GO in class: CONFIRMED. |
| (c) first cumulant | CONFIRMED up to normalisation: ∫F̂dt = 2πF(0), so divide by F(0), not F̂(0). |
| §2 Var with g-linear observable = G0 | CONFIRMED (Gram minus rank-one = G0, REF-D). The "otherwise only first cumulant" clause over the whole MGF class is ARGUED, not PROVED. |
| §3 log-convexity in σ | PROVED only for F ≥ 0 (then H_X = Σ c_{mn}(mn)^{−σ} with c ≥ 0); for signed F^{∗k} false in general. |
| PRR-log′ | **ILL-POSED**: at k = 0, H_X(0,σ) = ∫_ℝ|ζ_X(σ+it)|²dt = ∞. Needs a normalised weight. Even repaired, the memo's own Cauchy–Schwarz shows it yields a bound |𝔞_T| ≤ √(κ_kkκ_σσ), no sign → CS-type, cf. ES-21/P33-6. Dead as sign source. |
| Effectivity sign (F ≥ 0 ⇒ finite part ≤ 0) | **CONFIRMED** (v_n > 0). NO-GO for naive effectivity: CONFIRMED. |
| "h⁰ off the multiplicative diagonal" | OPEN, **ill-specified**. Removing ratio-prime-power pairs destroys the Gram structure (so its positivity is no longer free); and by the coprime-ratio expansion h⁰_X = Σ_{(a,b)=1}(ab)^{−½}F(log a/b)(log X − log max(a,b) + γ + o(1)) the prime powers enter with weight 1·log X, not Λ. Whether Λ(n) can emerge exactly (e.g. via Σ_{d|n}Λ(d) = log n from the −log max(a,b) term) is the one concrete computation not in the index; if it reproduces Near(s) of CA_M_001 Prop 1.1 it is REF-D. |

## D. Ranking of residues
1. **h⁰ off the multiplicative diagonal** (INV_B_002 §4) — only residue with a concrete, unindexed object and aligned with the semiring principle (pairs m ≈ kn). First task: write it as an exact identity (coprime-ratio expansion, log max(a,b) term), check whether Λ arises with exact weights and whether it equals CA_M_001's Arch − Near. Pass/fail of (R)(3),(4),(10),(11) decidable at that step.
2. **Lévy rigidity + G1** (INV_A_001) — G1 (damped polar term) is a finite computation; but the route's sign content is REF-D (Herglotz/thm:Z), so low value.
3. **Θ / G2** — REF-D; G2 circular. Do not build.
4. **HI_𝒮 / PRR-log / PRR-log′** — retry of R135_007 / ES-21 / P33-6 / P40-3; PRR-log′ ill-posed. Do not build.

# CA_K_000 — Front K seeds: theory of frustrated quadratic forms (spin glasses, diamagnetism, signed graphs, SDP) (phase 193)

Pen and paper; **no numerics run**. no equivalence of the target with any statement about
another object is used.
**No sign contact. No certified negative value for ζ.**

Read before seeding: CA_J_002 (Thm 1.3 frustration, Lemma 1.2), CA_J_SYNTHESIS, CA_I_SYNTHESIS + CA_I_001 (Thm 1 Markov, Prop 1.2,
Thm 2, Thm 3, Cor 6), CA_H_002 (Thm 3.1/3.2 anatomy), CA_E_001 (Lemmas 0–1, Thm 1, Thm 2), CAMPAIGN_LEDGER, P47 subsec:oneprofile,
prop:AM, eq:symbol, eq:m (C₀ = −5.372…), cor:Tarch (T*_{∞,P} ∈ [0.58,0.60]; P47 l. 196 "beyond the threshold the primes supply
positivity"), thm:sos, prob:region (R)(1)–(11); ROUTES-TRIED-INDEX README (PRINCIPIO RECTOR) and 06_.

## 0. Corpus check (grep over all *.md, *.tex)
Guerra 0, Parisi 0, spin glass 0, Aizenman 0, Goemans 0, Harary 0, diamagnetic 0, Kato's inequality 0, Sherrington 0 hits.
Non-zero and relevant:
- "frustrat": E78_1 (numerical gauge frustration of a different matrix B_L), CA_J_002 Thm 1.3 (𝔸_M, PROVED). Not retried.
- "signed graph": P120 P3_IHARA_PRIME_CYCLE_DICHOTOMY (unsigned Ihara realizations cannot carry mixed-prime cycles; "a signed
  trace would be a new input"). Neighbour of K6/K7 (different object: non-backtracking operator, not 𝔸_M).
- "Doob / ground-state transform": **Paper 41** (full-kernel Doob coordinate; 31 no-gos; Weil positivity = one sharp Poincaré
  inequality for a ferromagnetic jump process). Seed K11 is therefore a retry.
- "Lasserre", "sum of squares", thm:sos: P47 thm:sos (arithmetic squares fail at T ≥ ½log3; with a free PD part = certificates, class (D)).
- "Talagrand": 1 hit, unrelated (concentration).
- NG-69 (exact signed index, gauge-robust, unforced): neighbour of K6.

## 1. Setting (as CA_J_000 §1; checked against P47 subsec:oneprofile, prop:AM, eq:symbol, eq:m)
F₀ ∈ 𝒫_{T₀} the P47 profile, ‖F₀‖ = 1, 2T₀ < log 2, c₀ = c_{F₀}, ĉ₀ = F̂₀² > 0, F̂₀(τ) = (τ² + ¼)|ĝ(τ)|⁴.
𝖡(d) = α(d) − ½Σ_{n≥2}v_n[c₀(log n − d) + c₀(log n + d)], α(d) = (1/2π)∫ m ĉ₀ cos(τd)dτ, m(τ) = C₀ + ∫_0^∞(1 − cos τu)K(u)du,
C₀ = −5.3721…, v_n = 2Λ(n)n^{−½}. 𝔸_M = [𝖡(log m − log k)]_{m,k≤M} = Arch_M − Comb_M, Comb_M = Div_M + Near_M (prop:AM(iii));
**Comb_M has zero diagonal** (prop:AM(iii)), so 𝖡(0) = α(0). Target (eq:target) ⟺ 𝔸_M ⪰ 0 ∀M ⟺ 𝖡 PD on ℝ (thm:oneprofile, prop:AM(i)).
t-picture: 𝔞_T(F) = m(0)‖F‖² + ∫_0^∞K(u)∫(F(t) − F(t+u))²dt du·(½ normalisation as in CA_I_001 (0.1)) − Σ_{n∈𝒩_T}v_nc_F(log n).
Two readings of "frustration": **t-picture** (sites t ∈ I_T, couplings K(u) ≥ 0 and v_n ≥ 0: ferromagnetic = Markov, CA_I_001 Thm 1;
frustration enters only through the codimension-2 Tate constraint 𝒫_T) and **integer picture** (sites m ≤ M, couplings 𝖡(log m/k):
frustrated, CA_J_002 Thm 1.3; no constraint).

## 2. Screen key
As CA_I_000. (R)k = clause k of prob:region; (P1)–(P6) = CA_B_SYNTHESIS; O-labels = P47 def:shape-ops; B′/B″ = thm:shape; FE-gen =
survives Epstein / ζ_K; G0 = squares are Gram factorizations; G1 = monoid-functorial; H-anat = CA_H_002 Thm 3.2 (additive weight ×
monoid coefficient, linear in Λ); REF-D = restatement of the target or property of its minimizer; [crit] = must resolve
λ_min(𝔸_M) = M^{−3+o(1)} (EXP_005 C1, NUMÉRICO quoted); PR = PRINCIPIO RECTOR (does the seed use + and · in interaction?).

## 3. Seeds and full pre-screen
| # | seed | Idx | (R) hit | (P1)–(P6) | O-survival | B′/B″ | FE-gen | G0/G1 | H-anat | REF-D | [crit] | PR | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| K1 | Guerra interpolation (RS/1RSB bound): one-sided bound from a sign of the derivative along a path from a solvable endpoint (archimedean Markov form, or Euler-decoupled Div) to 𝔸_M | 0 hits; neighbour: concavity of λ_A in the comb (CA_B_008, CA_I_001 Prop 1.2(b)), coupling ray non-monotone (G2_B8_R2 Thm R) | (R)(3) (derivative linear in Λ), (R)(5) | P1: risk (endpoint lower bound); P2 fails if derivative is linear | derivative identity survives all O | B″ for the identity | yes | Gaussian IBP needs a Gaussian field with covariance = form ⇒ G0 | yes | sign of derivative = minimizer statement | no | + (path in comb weight) × · (comb) side by side | **DEVELOP (CA_K_002 §1–§3)**: decide whether any deterministic interpolation has a derivative with a sign |
| K2 | Talagrand/Parisi: Ghirlanda–Guerra identities, positivity of overlaps, ultrametricity | 0 | (R)(3) | — | — | — | — | needs random couplings | — | — | — | none | DISCARD: all identities are averages over Gaussian disorder; the couplings φ(q) are deterministic; the only symmetry group (twists by Ĝ) acts unitarily (CA_K_002 Prop 2.1) so overlaps are trivial |
| K3 | Aizenman–Sims–Starr cavity: λ_min(𝔸_{M+1}) from λ_min(𝔸_M) + one-site cavity field; multiplicative cavity S → S ∪ {p} | retry: P47 thm:coer-schur / thm:wh-schur (Schur reductions); CA_E_001 Thm 1 induction (prime-direction cavity) | (R)(5) | — | — | identity | yes | — | — | **REF-D** (Schur complement ≥ 0 is the target) | yes but REF-D | additive cavity (M→M+1) or multiplicative (new prime), never both | DISCARD (retry, CA_K_002 §4 one line) |
| K4 | Grothendieck inequality, Goemans–Williamson, Nesterov 2/π: ±1 (cut) values vs SDP | 100 hits for "Grothendieck" are the topos/K-theory sense; 0 for the inequality | (R)(3) | P5 fails | all | — | yes | the vector side is the Gram/Bochner embedding u_m = m^{iτ} ∈ L²(ν): G0 | — | λ_min = SDP value exactly (eigenvalue problem is its own SDP) | no | none | DISCARD: Grothendieck relates ±1 optima to vector optima for bilinear forms; for the bottom of a quadratic form the SDP is exact and its dual certificate is 𝔸 − λI ⪰ 0 itself (class (D), G0). Sign-vector positivity x^T𝔸x ≥ 0 ∀x ∈ {±1}^M is strictly weaker than the target |
| K5 | Lasserre / SOS hierarchies, NC-SOS | thm:sos; CA_E_001 Cor 1.2 | (R)(3) | — | — | — | — | G0 | — | level 1 of Lasserre on a quadratic form = PSD = target | no | none | DISCARD: thm:sos (no arithmetic SOS at T ≥ ½log3; with free PD part = certificate); CA_E_001 Cor 1.2 (commutative: positive = CP) |
| K6 | Harary balance, switching classes, ℤ/2 holonomy ("flux") of the sign pattern around +/· cycles; elliptope cycle conditions (Barrett–Johnson–Loewy) | neighbours: CA_J_002 Thm 1.3, E78_1, NG-69 | (R)(5) (pattern of observables) | P5? | flux of a cycle = sign of 𝖡 at one ratio: changes with the comb (not B″) but insufficient | — | — | — | the flux is the conjunction "𝖡 > 0 near 0 (additive) ∧ sgn𝖡(log q) (monoid point)" | — | no | **yes formally** (the cycle m→…→2m is the telescoping ∏(k+1)/k = 2) | **DEVELOP (CA_K_001 §3)**: compute the gauge-invariant content exactly |
| K7 | Signed / connection Laplacian, Cheeger inequalities for frustration (Atay–Liu 2020; Bandeira–Singer–Spielman 2013): frustration as a *source* of positivity | P120 P3 (Ihara, unsigned) | (R)(3), [crit] | — | all | B′ (inequality with loss) | yes | — | — | the needed spectral bound is a rescaling of the target | **fails** (constant loss) | uses the sign pattern (+/· cycle) | **DEVELOP (CA_K_001 §4)**: the exact signed-Laplacian decomposition 𝔸 = L_σ − (D − 𝖡(0)I) |
| K8 | Diamagnetic inequality (Kato; Simon; Hess–Schrader–Uhlenbrock): λ_min(frustrated) ≥ λ_min(|couplings|), in both pictures | 0 hits; t-picture Beurling–Deny = CA_I_001 Thm 1(i) | (R)(3) | P2 | survives all O in the comparison form | B″-type comparison | yes | — | — | — | void (see 001) | +: |·| of additive weights, ·: twist of comb | **DEVELOP (CA_K_001 §1–§2)**: check direction, decide whether the archimedean Markov part is the "|couplings|" version |
| K9 | Lieb flux-phase theorem, paramagnetic inequalities | 0 | — | — | — | — | — | needs reflection positivity | — | — | — | — | DISCARD: Lieb's theorem needs RP (dead: CA_J_001 Thm 1–2, RP_p false) and concerns the sum of the lowest half of the spectrum, not λ_min; paramagnetic reversal is folded into CA_K_001 Thm 2.2(ii) |
| K10 | Heat flow on the solenoid Ĝ: interpolation μ_t = ν₀ ∗ h_t from the Kronecker line (Div+Near) to Haar (Div) — damping near-coincidences q by a multiplicative height ℓ(q) | neighbour: CA_H_002 Thm 3.1 (line − Haar), CA_E_001 Thm 2 (Gaussian kernels on G) | (R)(3) | P2 fails | all | B″ | yes | — | **yes**: derivative = Σ_q ℓ(q)e^{−tℓ(q)}c₀(log q)M_s(q), additive weight × monoid coefficient | — | no | +/·-genuine weight (multiplicative height of additive near-identities), linear in Λ | **DEVELOP as part of CA_K_002 §3** (least-dead +/· interpolation) |
| K11 | Ground-state (Doob) transform of the Markov form: λ_A = λ₀ + constrained spectral gap of a ferromagnetic jump process | **retry: Paper 41** (Doob–variance identity, 31 no-gos: radical saturation, measure capacity, counterfactual invariance) | — | — | — | — | — | — | — | Paper 41 (2.7) | — | — | DISCARD (retry) |
| K12 | Frustration-free decompositions (H = Σ local h_i ⪰ 0 with common ground state) | thm:sos; CA_F_001 Prop 3 (bare local positivity false at every p) | (R)(3), (R)(5) local | — | — | — | — | G0 | — | — | — | · only (local Euler factors) | DISCARD |
| K13 | TAP / Plefka / high-temperature expansion of the bottom | CA_J J10 (Dobrushin / cluster) | (R)(3) | — | — | B′ | — | — | — | — | **fails** (perturbative) | none | DISCARD |

**Survivors for depth.** K8 + K6 + K7 (diamagnetism, holonomy, signed Laplacian) in **CA_K_001**; K1 + K10 (with K2, K3 as remarks)
in **CA_K_002**. Every other seed is discarded with its killing clause in the table.

## 4. PRINCIPIO RECTOR for this front
The frustrated cycle of CA_J_002 is C_m = (m, m+1, …, 2m): its additive edges carry ratios (k+1)/k, whose product telescopes to the
multiplicative element 2. The question of the front is whether the *gauge-invariant* datum of this cycle (its ℤ/2 or U(1) holonomy),
or a diamagnetic/interpolation comparison that sees it, can carry the sign. Each developed seed states how it uses the telescoping
identity (+ produces ·) and whether it uses it beyond the conjunction "𝖡 > 0 near 0" ∧ "value of 𝖡 at log 2".

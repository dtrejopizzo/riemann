# EXTERIOR_DATUM_001 — why p = g*_50 has an O(1) (1,2) resonance: the Möbius lattice of edge lines (NUMÉRICO + pen and paper)

Phase 199, analyst + prover. ,
no zero datum is used,
Data: Mori VIII μ = 15 even form, p = g*_50 (ROUGH_COMPLEMENT_001 `pvecs`), **same gauge as ROUGH/TEST_BRIDGE** (M = 28 even
Legendre min-leak filler on |u| < 1/λ with the two Tate constraints φ(0) = 0, ∫f = 0, = Π within the family, U_001 U.2.1),
same quadrature (14 Möbius cells × 900 GL nodes, ω ∈ [1,48], Δω = 0.002, arb 400/240 bits), same X-matrix discretization.
Scripts: `EXTERIOR_DATUM_001_exterior.py` (arb; decomposition columns), `EXTERIOR_DATUM_001_analysis.py` (double, ×10³⁵).
Output: `EXTERIOR_DATUM_001_data/` (analysis.json, analysis.log, meta). Units: W* = W(g*); ρ in 10⁻³⁵.

**Outcome.**
1. **Δr lives in the outer window, not in the filler, not in the Tate repair, not in the higher prolates.** With
   ρ_p = ρ_{pro04} + ρ_{pro8+} + Δr_in + Δr_out (pro04 = ã₀ψ₀ + ã₄ψ₄ = 1.106ψ₀ − 1.822ψ₄, p's own coefficients; pro8+ =
   Σ_{8≤k≤56}ã_kψ_k; Δr_in = filler − prolate part on |u| < 1/λ; Δr_out = E⁻¹p − prolate part on [1/λ,λ]):
   Δr_in has rms ≤ 7·10⁻⁴ (the min-leak filler *is* the prolate continuation to 10⁻³⁹), the Tate shift (unconstrained −
   constrained filler) has X₁₁ = 10⁻⁴ W*, pro8+ has (1,2)/X₁₁ = +0.048. **Δr_out carries everything:** (1,2)/X₁₁ = −0.387.
2. **The (1,2) of p is a cross resonance prolate@dilate 1 × Δr_out@dilate 2.** p's (1,2) = −0.952 W* =
   pro04 (+0.065) + 2·cross (−0.518) + Δr (−0.499). Directional split of the cross: pro04 in dilate 1 × Δr_out in dilate 2 =
   **−0.481**, the reverse = +0.0001; same for n = 3 (−0.296 / 0.000) and n = 5 (−0.197 / 0.000). The pure prolate tail
   (what PRECHECK evaluated) has (1,2)/X₁₁ = **+0.040** — Theorem C's phase value +0.033 reproduced; Theorem C is right for
   what it covers.
3. **Mechanism (PROVED structure + NUMÉRICO confirmation): the Möbius lattice.** f₁ = E⁻¹p = Σ_{m≤14} μ(m)h(mu)·1_{mu<λ},
   h(v) = v^{-½}p(log v); term m switches on at u = λ/m with the *same edge profile as the edge at u = λ*, dilated by m.
   Hence the singular content of ρ_p is a lattice of lines at ω-frequency c/m: ρ_sing(ω) = Σ_m (μ(m)/m)·σ(ω/m), σ = edge
   profile (m = 1 line = the prolate's Langer tail). Line m in ρ(ω) and line nm in ρ(nω) are the **same function σ(ω/m)**,
   so the (1,n) pair is an *exact* resonance (no stationary phase, no c^{−½}) with sign μ(m)μ(nm) = μ(n) for (m,n) = 1.
   n = 2: lines (1,2), (3,6), (5,10), (7,14), all with μμ = −1. Measured signs of p's (1,n): −, −, +0.04, −, +, − for
   n = 2..7 vs μ(n) = −, −, 0, −, +, −: 6/6. Band test (ω-frequency ↔ u-position): ρ^{(m)}(ω) ≈ a_m ρ^{(1)}(ω/m)/m with
   a_m = −0.45, −0.50, −0.45, +0.42, −0.40 (m = 2, 3, 5, 6, 7; corr −0.64 … −0.77), sign = μ(m) in 9/10 squarefree m (ω ≥ 2; m = 10 is the miss, |a| = 0.02);
   μ(m) = 0 bands (4, 8, 9, 12): |corr| ≤ 0.31.
4. **Theorem C′ (leading order, ARGUED): no diagonal domination term by term.** For the lattice class the (1,n) ratio is
   O(1)·μ(n), not O(μ^{−½}): R_n/X₁₁ = (2/n)Σ_{m≤μ/n}μ(m)μ(nm)ℓ_{m,n}/Σ_{m≤μ}μ(m)²ℓ_m (ℓ = profile weights); with a 1/ω
   profile and log weights −0.370 (n = 2) at μ = 15 (measured p: −0.350, Δr: −0.432), limit 2μ(n)/(nσ(n)) (−⅓ for n = 2);
   Σ_n|R_n|/X₁₁ diverges logarithmically. The correct plank is the **q-grouped form**: the dilate-summed lattice datum has
   coefficients C_{a/b} = Σ_{k≤μ/b}μ(bk)/(bk) (b = 1: M̃(μ) = Σ_{k≤μ}μ(k)/k = −0.006 at μ = 15), i.e. the O(1) resonances
   are the dilate-expansion image of a near-total Möbius cancellation (§4). OPEN as a theorem.
5. S(p) = λ∫𝔴_μ|Πρ_p|² (ω ≤ 48, min-leak gauge) = **4.245 W***, W(p) = 1.2325 W* ⇒ W/S = 0.290; |(1,2)|/S = 0.224,
   |off-diag|/S = 0.465. S(pro04) = 1.819, S(Δr) = 2.529, cross −0.103.
No sign of row D is claimed. L′♯ OPEN. Row D OPEN.

## 0. Corpus / index check, and why this is not a retry
Read: ROUGH_COMPLEMENT_001 (+ scripts), AUDIT_L_SHARP_11, PROOF_L_SHARP_Z_001, PRECHECK_T1_001 §1, MORI15_EXTREMAL_001 (l.83:
"jumps at u = λ/m are μ(m)g*(T)/√λ"; a_k), A_001 Prop 3.1/2.1, U_001 U.2, K_001. Index README l.476–477. grep
"Möbius jump / λ/m / jump lattice / resonance" in index and proof-L-sharp: the jumps are recorded (MORI15 l.83, ROUGH §1–2 c/n
lines of δ) but never linked to the dilate resonances; ROUGH's "δ is not a jump datum" concerns δ, not p. Not a retry: first
decomposition of p's exterior datum, first directional (dilate-1 vs dilate-n) attribution, first lattice explanation.

## 1. Pointwise comparison ω ∈ (1,4) (task 1; ×10⁻³⁵; same gauge as ROUGH)
| ω | ρ_p | ρ_{pro04} | Δr = ρ_p − ρ_{pro04} |
|---|---|---|---|
| 1.002 | −0.890 | −0.498 | −0.392 |
| 1.01 | −1.415 | −1.709 | +0.294 |
| 1.05 | +1.866 | +1.327 | +0.539 |
| 1.118 (s₂) | −0.758 | −1.045 | +0.287 |
| 1.2 | +0.992 | +0.730 | +0.263 |
| 1.5 | −0.810 | −0.597 | −0.213 |
| 2.0 | −0.053 | −0.342 | +0.288 |
| 2.24 (T₂) | −0.259 | −0.232 | −0.028 |
| 3.0 | +0.413 | +0.235 | +0.178 |
| 3.5 | −0.385 | +0.024 | −0.409 |
| 4.0 | −0.300 | −0.198 | −0.102 |
RMS by window (1,1.01) / (1,s₂) / (s₂,2) / (2,4) / (4,48):
p 3.16/1.35/0.58/0.29/0.082; pro04 4.15/1.61/0.46/0.21/0.041; pro8+ 1.03/0.47/0.21/0.045/0.010; Δr 1.03/0.48/0.22/0.21/0.076;
**Δr_out 0.045/0.056/0.050/0.203/0.075**; Δr_in ≤ 7·10⁻⁴; Tate shift 0.035/0.018/0.006/0.002/0.0004.
Reading: in (1,2) Δr is the higher-prolate correction pro8+ (in phase with the Langer tail; harmless); the non-prolate part
Δr_out is **absent from the caustic layer** and lives at ω ≥ 2 (rms comparable to the prolate tail there, 2× it beyond 4).
Edge values: f(λ−) = κ₀ = p(T)/√λ = −5.924·10⁻³⁵ (check f(λ−)/κ₀ = 1), prolate part at λ −7.533·10⁻³⁵ (pro04: −9.588·10⁻³⁵).

## 2. Origin of Δr (task 2)
| piece | X₁₁ | (1,2) | (1,3) | (1,5) | (1,2)/X₁₁ | pro04@1 × piece@2 / reverse |
|---|---|---|---|---|---|---|
| p | 2.718 | −0.952 | −0.653 | −0.342 | −0.350 | — |
| pro04 (two prolates) | 1.634 | +0.065 | −0.047 | −0.007 | +0.040 | — |
| pro_all (k ≤ 56) | 1.751 | +0.037 | −0.047 | −0.001 | +0.021 | — |
| (b) pro8+ (j ≥ 2) | 0.191 | +0.009 | +0.001 | −0.001 | +0.048 | −0.020 / −0.017 |
| (a) Δr_in (filler − prolate) | 0.0000 | 0.0000 | — | — | — | 0.000 / 0.000 |
| (c) Tate shift | 0.0001 | 0.0000 | — | — | — | −0.0001 / 0.000 |
| **Δr_out (E⁻¹p − prolate)** | 0.966 | −0.374 | −0.228 | −0.093 | **−0.387** | **−0.481 / +0.0001** |
| Δr (all) | 1.156 | −0.499 | −0.310 | −0.146 | −0.432 | −0.501 / −0.017 |
- (a) **Filler: no.** The min-leak filler equals the prolate continuation on |u| < 1/λ to rms 7·10⁻⁴ (relative 10⁻⁴). The
  premise "a function supported on 2/λ spreads its tail" does not apply: there is nothing non-prolate in the filler.
- (b) **Higher prolates: no.** pro8+ (ψ₈ … ψ₅₆, ã₈ = 3.3·10⁻⁵ but 1−λ₈ = 1.8·10⁻⁶²) is a set of Langer tails; it behaves like
  Theorem C (+0.048).
- (c) **Tate repair: no.** Multipliers 5·10⁻³⁹, 1.7·10⁻³⁸; shift X₁₁ 10⁻⁴.
- (d) **Origin = the interior Möbius cells of E⁻¹p** (not in the earlier list). The resonance is directional: the prolate
  tail (edge line m = 1, large in the caustic layer) at dilate 1 against Δr_out at dilate n, never the reverse.
- The naive 1/ω jump model ρ_J = Σ_m μ(m)κ₀ sin(cω/m)/(πλω) is **not** pointwise valid (corr(Δr_out, model) ≈ −0.05): kinks
  dominate, h′(λ)/h(λ)·λ/c = 53.9 (p′(T)/p(T) = 5079: Legendre endpoint growth). Its (1,2)/X₁₁ = −0.31 is suggestive only.
  The structure that survives is the dilation identity of §3, which holds for any edge profile.

## 3. The lattice structure (PROVED identity; NUMÉRICO confirmation)
**Lemma E.1 (PROVED, MECH Prop 3.1 + change of variables).** On [1/λ,λ], E⁻¹p = f₁ = Σ_{m≤⌊μ⌋} μ(m)h_m with
h_m(u) = h(mu)·1_{[1/λ,λ/m)}(u), h(v) = v^{-½}p(log v). Each h_m is a dilate of the single function h·1_{[m/λ,λ)}:
2∫h_m(u)cos(2πλωu)du = m⁻¹·ρ[h·1_{[m/λ,λ)}](ω/m). All h_m share the upper cut-off profile of h at v = λ.
- Consequence (ARGUED: singular content = upper-cut contribution; the m-lines are separated in ω-frequency, c/m − c/(m+1) =
  c/(m(m+1)) ≥ 0.45 for m ≤ 14): ρ_p = ρ_reg + Σ_m (μ(m)/m)σ(ω/m), σ = the upper-edge profile; the m = 1 line is the edge
  datum, which the prolate tail represents; lines m ≥ 2 exist only in E⁻¹p (not in any prolate) — they are Δr_out.
- In the dilate expansion, line m at dilate 1 and line nm at dilate n are identical functions of ω, (μ(m)/m)σ(ω/m) and
  (μ(nm)/(nm))σ(ω/m): **exact coherence**, coefficient μ(m)μ(nm)/(nm²). Theorem C's resonance needs a Fresnel point and
  carries c^{−½}; this one does not.
**NUMÉRICO (band attribution, ω ∈ [2,48], Tukey taper; also [1.2,48]).** Fitted ρ^{(m)}(ω) ≈ a_m ρ^{(1)}(ω/m)/m:
m = 2: −0.45 (corr −0.64), 3: −0.50 (−0.69), 5: −0.45 (−0.77), 6: +0.42 (+0.60), 7: −0.40 (−0.77), 11: −0.25, 13: −0.13,
10: −0.02, 14: +0.07; μ = 0 bands 4, 8, 9, 12: a = −0.08, +0.14, −0.03, +0.18. Prediction a_m = μ(m): sign right for every
squarefree m ≤ 7, amplitude ≈ ½ (band 1 also holds near-band Bessel content that the lines m ≥ 2 do not dilate; NUMÉRICO,
not resolved). Plain resonant overlap ∫ρ(ω)ρ(2ω)dω on [2,24]: largest band pair (1,2), then (2,4), (3,6); resonant pairs
b = 2a carry 64 % (ω ≥ 2) / 71 % (ω ≥ 1.2) of the band-pair sum.

## 4. Theorem C′ — the class and the leading (1,n) resonance (task 3; ARGUED, leading order)
**Class 𝒜_μ.** Admissible window data f = E⁻¹g on [1/λ,λ] plus min-leak gauge filler (= prolate continuation, §2(a)).
Exterior datum: ρ = ρ_pro + ρ_lat, ρ_lat(ω) = Σ_{2≤m≤μ}(μ(m)/m)σ_g(ω/m), and the m = 1 line inside ρ_pro.
**Proposition C′.1 (leading order, ARGUED).** Assume the lines are mutually non-resonant except through exact dilation
(distinct c/m) and σ_g has profile mass I(a) = ∫_a^∞ σ_g², weights ℓ. Then, per pair,
 X₁₁ ≈ Σ_{m≤μ} μ(m)²m⁻¹ I_ℓ(1/m),  (1,n) ≈ 2Σ_{m≤μ/n} μ(m)μ(nm)(nm)⁻¹ I_{ℓ−log n}(1/m),
so R_n/X₁₁ has the sign of μ(n) and size O(1):
- σ ∝ 1/ω, ℓ = log(μω/m) (archimedean, minus log n for the pair): ratio = (2/n)Σμ(m)μ(nm)(log(μ/mn)+1)/Σμ(m)²(log(μ/m)+1)
  = −0.370, −0.151, 0, −0.070, +0.032, −0.040 (n = 2..7, μ = 15); μ → ∞: 2μ(n)/(nσ(n)) (Σ over squarefree m coprime to n;
  CITED density 6/π²·∏_{p|n}p/(p+1)), n = 2: −⅓.
- profile supported at ω/m ≥ 1, flat weight: ratio → 2μ(n)/σ(n) (n = 2: −⅔).
Measured: p −0.350, Δr −0.432, g* −0.479 (ROUGH). Same sign, same order; the exact constant depends on σ_g (OPEN).
**Corollary C′.2 (the answer to "does the diagonal still dominate?").** Term by term, **no**: Σ_{n≥2}|R_n|/X₁₁ ≍
Σ μ²(n)/(nσ(n))·(log) does not become small as μ grows; the bracket D − Σ_n R_n of Theorem C has no analogue on 𝒜_μ.
What replaces it (ARGUED, formal): grouping all dilate pairs by the rational ratio q = n/m, the dilate-summed lattice datum
φ_lat(s) = e^{s/2}Σ_n ρ_lat(ne^s) = e^{s/2}Σ_q C_q σ_g(qe^s) with C_{a/b} = Σ_{k≤μ/b} μ(bk)/(bk); the comb part brings
D_q = Σ_k μ(bk)log(ak)/(bk). For b = 1, C_a = M̃(μ) = Σ_{k≤μ}μ(k)/k (= −0.0059 at μ = 15; → 0, CITED, PNT) and
D_a = log a·M̃(μ) + Σ_{k≤μ}μ(k)log k/k (→ −1, CITED, PNT). So the O(1) negative (1,n) resonances are the dilate-expansion image
of a near-cancellation of the lattice in the summed datum; the quadratic form of 𝒜_μ at leading order is
Σ_q (σ-mass)·[½C_q²(log μq + 1) − C_qD_q] + pole + cross with ρ_pro. **The plank the real extremal needs is a bound on this
q-grouped form (Möbius partial sums C_q, D_q, coupled to the edge line in ρ_pro), not a diagonal-vs-resonance bracket.**
Status: OPEN (the profile σ_g, the cross with ρ_pro and the non-asymptotic remainder are not controlled).
- Semiring note: the resonance condition is m′ = nm — the multiplicative coincidence between the additive dilate index n of
  the exterior form and the Möbius index m of E⁻¹. This is the (ℕ,+,·) interplay at m ≈ kn that the semiring principle
  asks for; it is arithmetic (μ(m)μ(nm)), with archimedean weight (arch(1,2) = −1.185 of −0.952; comb +0.233).

## 5. S(p) vs W(p) (task 4)
S(p) = λ∫_1^{48}𝔴_μ|ρ_p|² (min-leak gauge, = Π within the family) = 4.245 W* (ROUGH 1.223 + 3.021 ✓); W(p) = 1.2325 W*;
**W/S = 0.290, S/W = 3.44.** |(1,2)|/S = 0.224; |Σ off-diag|/S = 0.465 (p). Split: S(pro04) = 1.819, S(Δr) = 2.529, cross
−0.103: **60 % of S(p) is the lattice part Δr**; the Δr-involving terms of p's (1,2) are 2·cross −0.518 + Δr −0.499 = −1.017
against a total −0.952 (pro04 alone +0.065). (TEST_BRIDGE/AUDIT_10's C/S = 0.19 is the Schur cross of the P3a split, a different quantity; not recomputed.)

## 6. Labels and records
PROVED: Lemma E.1 (E⁻¹ as a Möbius sum of dilates with a shared edge), edge value f(λ−) = p(T)/√λ, line coincidence m′ = nm.
ARGUED: singular-content lattice form of ρ, Prop C′.1 leading order, Cor C′.2 grouped form. CITED: PNT-level Möbius sums.
NUMÉRICO: §1–§3, §5 (μ = 15, one vector). OPEN: Theorem C′ as a theorem; σ_g; amplitude ½ in the band test; μ-trend.
**Falsified (NUMÉRICO):** "Δr comes from the gauge filler", "from the higher ψ_{4j}", "from the Tate repair";
"the 1/ω jump model describes Δr pointwise". **Do not retry:** bounding the (1,n) resonances of admissible data by single
Langer-tail (Fresnel) estimates; diagonal-domination brackets D − Σ|R_n| on 𝒜_μ (fails termwise at leading order).
No sign of row D claimed. L′♯ OPEN. Row D OPEN.

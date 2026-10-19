# AUDIT_L_SHARP_12 — audit of EXTERIOR_DATUM_001 (phase 199)

CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO. Checked against: A_001 Prop 3.1 (MECH Prop 3.1), ROUGH_COMPLEMENT_001,
TEST_BRIDGE_001, Z_001 / AUDIT_L_SHARP_11, PRECHECK_T1_001, and `EXTERIOR_DATUM_001_data/analysis.{json,log}` (re-read; the
Möbius-model numbers recomputed by hand in Python/sympy).

**Verdict: ACCEPTED WITH CORRECTIONS.** The structural core (Möbius-sum-of-dilates identity, 1/m weight, line coincidence
m′ = nm with sign μ(n), directional attribution, decomposition, S/W) stands. Three factual slips (Lemma E.1 cut-offs, the
n = 4 sign entry, M̃(15)), one miscount (band test 8/9, not 9/10), and the Theorem C′ model agreement and the q-grouped
"near-cancellation" reading are downgraded. No sign of row D. L′♯ OPEN. Row D OPEN.

## 1. Lemma E.1 (Möbius sum of dilates) — PROVED, statement corrected
Prop 3.1: f(u) = Σ_{m≤λ/u} μ(m)(mu)^{−½} g(log(mu)). With h(v) := v^{−½}p(log v) (the pulled-back window function, supported on
v ∈ [1/λ, λ] since supp p ⊂ [−T,T]), f₁ = Σ_m μ(m) h(mu)1_{mu≤λ} on [1/λ,λ]; u ≥ 1/λ forces m < λ² = 15, so m ≤ 14. ✓
Change of variables v = mu: 2∫h(mu)1_{[1/λ,λ/m)}(u)cos(2πλωu)du = m⁻¹·ρ[h·1_{[m/λ,λ)}](ω/m). ✓ (1/m weight correct.)
**Correction.** "Each term is a dilation of the same edge profile h" is true only for the *upper* cut (v = λ, h(λ) = p(T)/√λ,
checked f(λ−)/κ₀ = 1). The functions being dilated are h·1_{[m/λ,λ)}: the *lower* truncation moves with m (v = m/λ). So the
m-th piece is not a dilate of one fixed function; it is a dilate of h restricted to [m/λ,λ). What is common to piece m in dilate 1
and piece nm in dilate n is exactly h·1_{[nm/λ,λ)} (a whole function, not only the edge), the difference h·1_{[m/λ,nm/λ)} is not
shared. "h" = the pulled-back window function itself, truncated at v = λ (i.e. at u = λ/m in the u-variable), not a separate profile.

## 2. Lines — what they are
A "line m" is the truncation tail of h_m at u = λ/m, i.e. oscillation e^{±icω/m} (c = 2πλ²) with amplitude given by the local
jet of h at v = λ (jump h(λ), kink h′(λ)λ/c, …). It is a **jump/kink tail, not a Langer chirp**. Only the m = 1 line is
identified with the prolate's Langer tail, and that identification is ARGUED (it sits in the caustic layer where the prolate
tail is a Bessel/Fresnel object, AUDIT_11). Since h′/h·λ/c = 53.9 > 48 = ω_max, the kink term dominates the jump term on the
whole measured range: σ is NOT a 1/ω profile on [1,48] (memo's own corr ≈ −0.05). The lattice form ρ_sing = Σ(μ(m)/m)σ(ω/m) is
algebraically right for the upper-cut part (ARGUED as "singular content"; the lower cuts at u = 1/λ are smoothed by the filler, cf.
the fitted junction jump J₁₅ = −0.287κ₀ in analysis.json, not discussed in the memo).

## 3. Resonance — algebra VERIFIED, numerics corrected
Line m in ρ(ω): (μ(m)/m)σ(ω/m). Line nm in ρ(nω): (μ(nm)/(nm))σ(nω/(nm)) = (μ(nm)/(nm))σ(ω/m). Same function; coefficient
μ(m)μ(nm)/(nm²); μ(m)μ(nm) = μ(n) iff m squarefree and (m,n) = 1, else 0. ✓ No stationary point, no c^{−½}: PROVED as an
identity of upper-cut parts; its dominance in the (1,n) entry is NUMÉRICO.
Directionality is a genuine prediction (reverse pairing needs a line at frequency nc, which no m ≥ 1 provides): log l.25
pro04@1 × Δr_out@n = −0.4808/−0.2959/−0.1966, reverse 0.0001/0.0000/0.0000 ✓.
- **Signs (1,n) of p, n = 2..7** (analysis.json): −0.952, −0.653, **+0.108**, −0.342, +0.137, −0.190. The memo writes "+0.04"
  for n = 4 — wrong (that is not p's value). μ(4) = 0, so the honest count is **5/5 on μ(n) ≠ 0**, and n = 4 is *not* small
  (|(1,4)| = 0.108 > ½|(1,7)|): μ(n) = 0 does not suppress (1,n) as the lattice predicts. Probability of 5/5 by coin: 1/32.
- **Band test** (ω ≥ 2): squarefree m ∈ {2,3,5,6,7,10,11,13,14} = **9 bands, not 10**; signs right 8/9 (10 misses, a = −0.020;
  14 is right, a = +0.072). At ω ≥ 1.2: also 8/9 (14 misses). Only m ≤ 7 (5 bands, |corr| 0.60–0.77) separate from the
  μ = 0 bands (|corr| 0.04–0.31); for m = 10, 13, 14 |corr| = 0.04, 0.17, 0.09 — below the μ = 0 maximum 0.31, i.e. noise.
  Null: independent fair signs, P(≥8/9) = 10/512 ≈ 0.02; bands share ρ^{(1)} as regressor and are not independent, so the real
  significance is weaker. Honest statement: **5 strong bands, all signs μ(m); the tail of the lattice is not resolved.**
- Amplitude ½: unexplained (OPEN). Note the 1.2-window gives a₂ = −0.58, a₅ = −0.34, a₇ = −0.25: the "½" is window-dependent.

## 4. Decomposition (1,2) — VERIFIED
pro04 +0.0648 + 2·cross(pro04,Δr) 2·(−0.2588) = −0.5176 + Δr −0.4989 = −0.9517 = p's (1,2) ✓. Directional −0.481 vs 0.0001 ✓
(for Δr_out, not Δr; Δr's directional −0.501/−0.017 includes pro8+). Filler/Tate/pro8+ falsifications ✓ (X₁₁ ≤ 10⁻⁴, +0.048).

## 5. Theorem C′ model — ARGUED, agreement downgraded
Stated formula with Σ_{m≤μ} (μ = 15) gives n = 2..7: **−0.352, −0.175, 0, −0.086, +0.030, −0.038**; the memo's −0.370, −0.151,
0, −0.070, +0.032, −0.040 are reproduced only with the lattice cut-off m ≤ 14 (correct one, mu < λ; the text must say m ≤ 14,
m ≤ ⌊14/n⌋). The limit 2μ(n)/(nσ(n)) is right (density n/σ(n) of squarefree coprime-to-n among squarefree, CITED; extra 1/n from
the shorter range; n = 2: −1/3). But: (i) the model uses the 1/ω profile that §2 of the memo itself falsifies pointwise; (ii) the
cut-off convention alone moves n = 2 by 0.018, n = 3 by 0.024 — the size of the "model −0.370 vs measured −0.350" agreement;
(iii) X₁₁ for p contains pro04 (not a lattice object). Conclusion: sign and order O(1)·μ(n) — ARGUED, consistent; the numerical
match is not evidence. Cor C′.2 (no termwise diagonal domination): ARGUED, supported by data (offdiag −1.973 vs X₁₁ 2.718).

## 6. q-grouped plank and M̃ — numerology-grade reading
**Factual error:** M̃(15) = Σ_{k≤15}μ(k)/k = 304/5005 = **+0.0607**; −0.0060 is **M̃(14)**. The "near-total cancellation" is an
accident of the cut-off (flips sign and grows ×10 when k = 15 enters). Σ_{k≤14}μ(k)log k/k = −0.83 (→ −1, CITED PNT-level).
The statement "the O(1) negative resonances are the image of the near-cancellation of the Möbius lattice" is **not PROVED and not
ARGUED to theorem standard**: it is a formal regrouping (algebraically fine as an identity of the lattice datum) plus a reading
based on one small partial sum. Label: formal identity ARGUED; the explanatory claim = HEURISTIC (numerology-grade), OPEN.

## 7. S(p) — VERIFIED
S(p) = 4.2447, W(p) = 1.2325 ⇒ W/S = 0.2904, S/W = 3.444; |(1,2)|/S = 0.224; |offdiag|/S = 1.9727/4.2447 = 0.465;
S(pro04) + S(Δr) + cross = 1.819 + 2.529 − 0.103 = 4.245 (the cross is already the 2× term) ✓.

## Labels after audit
PROVED: Lemma E.1 as corrected (dilates of h·1_{[m/λ,λ)}, shared upper cut), 1/m weight, line coincidence m′ = nm, sign μ(n).
NUMÉRICO: decomposition, directionality, 5/5 signs (μ ≠ 0), band test 8/9 (5 strong), S/W. ARGUED: lattice singular form,
C′.1 sign/order, C′.2. HEURISTIC/OPEN: model constant, amplitude ½, q-grouped "near-cancellation" explanation.

## Constraint 24 (new): Möbius-lattice structure of exterior data
(24a) Any admissible datum f = E⁻¹g has exterior datum carrying ≤ 14 (at μ = 15) truncation lines at ω-frequency c/m with
coefficients μ(m)/m; in the dilate form, line m@1 and line nm@n coincide exactly ⇒ (1,n) pairs of size O(1)·μ(n) at leading
order, directional (pro@1 × lattice@n). (24b) **Single-line models are invalid for admissible data**: Fresnel/Langer single-tail
estimates (Theorem C class) cover only the m = 1 line; any bound on (1,n) must include the lattice lines m ≥ 2. (24c) Profile
σ on ω ≤ 48 is kink-dominated, not 1/ω. (24d) μ(n) = 0 entries are not suppressed in practice ((1,4) = +0.108).
No sign of row D. L′♯ OPEN. Row D OPEN.

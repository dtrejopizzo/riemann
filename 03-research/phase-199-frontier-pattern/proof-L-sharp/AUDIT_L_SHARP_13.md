# AUDIT_L_SHARP_13 — audit of PROOF_L_SHARP_AA_001 (Theorem D, Möbius-lattice form)

Phase 199, ,
no "E1". Checked against EXTERIOR_DATUM_001 (Lemma E.1, C′.2), AUDIT_L_SHARP_12, A_001 Prop 3.1 / MECH Prop 3.1, E_001
(Thm E.2, Cor E.3, Rem 3.2), J_001 Prop J.1, and against the numerics of GRAM_INERTIA_001 (companion, Part B).
**Verdict: ACCEPTED WITH CORRECTIONS (identities); §1 Remark and §4 framing REJECTED as stated (see C5).**

## 1. (D.1) exactness and the moving lower cut — VERIFIED (PROVED)
On 1/λ ≤ u ≤ λ: H(mu) ≠ 0 ⇔ 1/λ ≤ mu < λ ⇔ m < λ/u (lower inequality automatic); m < λ/u ≤ μ, so Σ_{m<μ}μ(m)H(mu) =
Σ_{mu<λ}μ(m)(mu)^{-1/2}g(log mu) = E⁻¹g (MECH/A_001 Prop 3.1; identical to `f1at` in EXTERIOR_DATUM_001_exterior.py). For |u| > λ
all terms vanish. Hence f − ΣμH(m·) ⊂ [−1/λ,1/λ]. On |u| < 1/λ, H(mu) ≠ 0 ⇔ u ∈ [1/(mλ), λ/m) ∩ (0,1/λ) = [1/(mλ),1/λ) (since
λ/m > 1/λ ⇔ m < μ), so φ₀ = filler − Σ_m μ(m)h(mu)1_{[1/(mλ),1/λ)}(u) exactly as stated. The AUDIT_12 point (moving lower cut
h·1_{[m/λ,λ)}) is correctly absorbed: H(m·) = (h·1_{[m/λ,λ)})(m·) + h(m·)1_{[1/(mλ),1/λ)}, second piece inside φ₀. Numerical
check (GRAM step 1): h(λ⁻) = −5.9105e-35 vs κ₀ = p(T)/√λ = −5.92355e-35 (last GL node, not the endpoint) ✓.

## 2. (D.2), jets, tail — VERIFIED with one slip
F[H(m·)](ω) = m⁻¹Ĥ(ω/m) ✓ (valid for all ω, not only ω > λ). Jet jump at u = λ/m: d^k/du^k[μ(m)h(mu)] = μ(m)m^k h^{(k)}(mu) →
μ(m)(h(λ), m h′(λ), m²h″(λ), …) ✓. Tail by two integrations by parts of 2∫_{1/λ}^{λ}h(v)cos(2πxv)dv:
h(λ)sin(2πλx)/(πx) + h′(λ)cos(2πλx)/(2π²x²) + O(x⁻³) ✓, and the general term 2Re[e^{2πiλx}(−1)^k h^{(k)}(λ)(2πix)^{-k-1}] ✓
(k = 0, 1 checked). **Slip C1:** "lower-cut terms of all m … carry the single phase 2πω/λ" is false term-by-term: the lower cut of
H(m·) is at u = 1/(mλ) (phase 2πω/(mλ)); only the aggregate Σ lines + φ̂₀ has its singular support at {1/λ} ∪ {λ/m}, because φ̂₀
carries the opposite singularities at 1/(mλ). **Slip C2:** "core data suffice for the σ-part" (absolute convergence in D(ii)):
core data kill h(λ) only; h(1/λ) ≠ 0 in general (p: h(1/λ⁺) ≈ −2.3e-34 ≠ 0), so σ ~ 1/x from the lower cut and the per-class
series Σ_b σ((b/a)e^x) is only conditionally/L² convergent. Read D(ii) in the Abel/L² sense always (the memo's fallback).

## 3. (D.3)–(D.5) — VERIFIED as identities; numerical table has TWO WRONG ENTRIES
(m,n) = (ak,bk), (a,b) = 1 is a bijection; n is unconstrained because ne^x > λ for x > a ✓. μ(ak) = μ(a)μ(k)1_{(a,k)=1} ✓ ⇒
C_{b/a} = (μ(a)/a)M̃_a(μ/a) depends on a only ✓; D_{b/a} split ✓; Σ_{k≤14}μ(k)log k/k = −1.0106 ✓. Exact rationals (k: ak ≤ 14):
| a | 1 | 2 | 3 | 5 | 6 | 7 | 10 | 11 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|
| C (exact) | −89/15015 | −17/105 | **−1/6** | **−1/10** | 1/6 | −1/14 | 1/10 | −1/11 | −1/13 | 1/14 |
| AA_001 | −0.0060 | −0.162 | −0.100 ✗ | −0.033 ✗ | +0.167 | −0.071 | +0.100 | −0.091 | −0.077 | +0.071 |
(C3) C_{b/3} = −1/3 + 1/6 = −1/6 = −0.167; C_{b/5} = −1/5 + 1/10 = −1/10. M̃(14) = −89/15015, M̃(15) = 304/5005 ✓.
(C4) |M̃(y)| ≤ 1 proof sketch: yM̃(y) − 1 = {y} + Σ_{2≤k≤y}μ(k){y/k}, so the bound is |yM̃ − 1 − {y}| ≤ ⌊y⌋ − 1 (the memo omits
{y}); conclusion |M̃| ≤ 1 still follows (upper: ≤ y; lower: ≥ 2 + 2{y} − y ≥ −y). Statement PROVED, sketch corrected.
(D.5) bilinear expansion with E.2/E.3 ✓ (exact, given C2).

## 4. The three NO-GO points — (a), (b) VERIFIED; (c) VERIFIED WITH A RESTRICTION
(a) Θ_∞(0) = ψ(¼) − log π = −γ − π/2 − 3log 2 − log π = −5.372 < 0 ✓; only Lévy part PD ✓. (b) G = Gram of 𝒲_ext itself ✓
(circular). (c) Transport: a_P: 1/D = ∏_{p≠P}(1−p^{-s}) ⇒ μ_D = μ·1_{P∤m} ✓. cΛ: (1−x)^c ⇒ μ_c(p) = −c, μ_c(p²) = c(c−1)/2 ✓,
(1,4) sign sgn(c(c−1)) ✓. **Restriction C5a:** by E_001 Rem 3.2 the falsifier's Z_D also carries the dilate weights a_D(n)
(a_P: 1_{P∤n}; cΛ: d_c(n)), so C^D_{b/a} = Σ_k μ_D(ak)a_D(bk)/(ak) depends on the numerator b too: "the same lattice arises" is
true for the line set, not for the class structure; "depends only on a" is ζ-specific (a_n ≡ 1). Resonance signs survive
(a_D ≥ 0). **Restriction C5b:** "|C| ≤ 1 holds on both falsifiers": for a_P CITED (coprime bound); for cΛ (c > 1) no uniform
bound is proved — only the limit Σμ_c(k)/k → 0 (CITED-level). The NO-GO conclusion stands with "|C| ≤ 1" replaced by "M̃-type
smallness/limits".

## 5. C5 — the decisive correction (from GRAM_INERTIA_001, NUMÉRICO)
AA §1 Remark: "lines m ≥ 2 … are O(1)". **FALSE for admissible data.** With p = g*_50, μ = 15, same quadrature:
sup_{[1,48]}|ρ_m| = 3.3e32 (m = 1) … 1.8e34 (m = 4) in the units where sup|ρ_p| = 7.2; φ̂₀ is 2.6e33. Ĥ is the transform of a
*truncated* smooth bump whose bulk is O(1) (max|h| = 1.61), so σ(ω/m) at ω/m = O(1) is O(10⁻³), while ρ_p is O(10⁻³⁵). The
lattice decomposition (D.2) is exact but cancels to **33 digits**; G entries are ≈10⁶⁷ W*, vᵀGv = W(p) ≈ 1.33 W* (pipeline).
Consequences: (i) EXTERIOR's "O(1) lines" were the *singular* (jump) content only, not Zσ^{(m)}; (ii) the D(iv) framing
"control the non-integer classes (O(1/a) coefficients) against the diagonal" is mis-scaled: every class block is 10⁶⁰–10⁶⁷,
the total is 1; (iii) on the line span G is numerically PD (10 lines: inertia (10,0,0)) and v = μ ⊕ 1 is its numerically null
direction (11×11 eigvec = v/|v| to 4 digits). So the sign is not decided by the inertia of the lattice Gram nor by the
coefficients C_q; it is decided entirely inside the 33-digit cancellation subspace, i.e. by the admissibility/band
limitation that ties φ₀ to the lines.

## 6. Labels after audit
PROVED: D(i) (D.1, D.2, jets, tail), D(ii) identities (Abel/L² reading, C2), |M̃| ≤ 1 (sketch corrected C4), NO-GO (a), (b),
(c) with restrictions C5a/C5b. NUMÉRICO: coefficient table **corrected** (C3). REJECTED: "lines m ≥ 2 are O(1)" (C5); D(iv)'s
O(1/a)-vs-diagonal programme as stated (mis-scaled). OPEN: L′♯. No sign of row D claimed. **Row D OPEN.**
Constraint 25 (new): any lattice/class form for admissible data must be written in a basis that respects the
cancellation Σμ(m)σ^{(m)} + φ̂₀ = O(ρ_p); coefficient-level (C_q, M̃) or Gram-inertia arguments on {Zσ^{(m)}} cannot see the sign.

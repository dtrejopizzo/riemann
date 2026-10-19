# AUDIT_L_SHARP_11 — audit of PROOF_L_SHARP_Z_001 (Theorem C, caustic layer ω ∈ (1,2))

Phase 199,
Checked against TEST_BRIDGE_001 (+ AUDIT_L_SHARP_10), PRECHECK_T1_001, Y_001 / AUDIT_L_SHARP_9,
W_001, BRIDGE_001 Lemma B.0, Slepian/Dunster prolate asymptotics, and against the new NUMÉRICO decomposition of
ROUGH_COMPLEMENT_001. Constants re-checked in mpmath (`AUDIT_L_SHARP_11_checkZ.py`).

**Verdict.** The single-tail mathematics of Z_001 is correct (Prop Z.3, Lemma Z.5, Hessian, phase Ψ_n, κ-weight all verified
line by line; constants reproduce to 6–9 digits, two small slips). One **factor-2 labelling error** ("two-sided" is one-sided).
Z.2 can be upgraded (Slepian's identity). The **data-attribution of §5 ("the TEST_BRIDGE deficit sits in the rough
complement / non-prolate component") is falsified in its rough-complement reading** by ROUGH_COMPLEMENT_001: the smooth
low-block part p = g*_50 alone has (1,2)/X₁₁ = −0.350 (6.5× Theorem C's bound) and carries 62 % of g*'s (1,2) pair, while δ has
only 2.8 % of its exterior mass in (1,2). The conclusion "the caustic layer is Λ-independent at leading order" is correct
only as "κ-insensitive within the uniform κ-scaling, for one prolate tail"; it does not transfer to the extremal. Row D OPEN.

## 1. sec θ parametrization and Langer mass (item 1) — VERIFIED
- ω = sec θ: dω = sec θ tan θ dθ, ω√(ω²−1) = sec θ tan θ ⇒ dω/(ω√(ω²−1)) = dθ; (1,∞) ↦ (0,π/2), so m = (2/π)dθ has total
  mass 1 and the layer (1,2) ↦ (0,π/3) carries exactly 2/3. ✓ log(μω²/√(ω²−1)) = log 2μ − log sin 2θ ✓ (≥ log 2μ, min at
  ω = √2; consistent with Lemma B.0).
- ∫_0^{π/3}(−log sin 2θ)dθ = −½∫_0^{2π/3}log sin φ dφ = (π/3)log 2 − ¼Cl₂(2π/3) (using ∫_0^x log sin = −x log 2 − ½Cl₂(2x),
  Cl₂(4π/3) = −Cl₂(2π/3)) ✓. Hence D_layer = (2/3)log 4μ − Cl₂(2π/3)/(2π); Cl₂(2π/3) = 0.6766277376, /(2π) = 0.1076886 ✓.
  Quadrature: D_layer(4, 15, 100, 1000) = 1.7407038, 2.6218744, 3.886621, 5.4216778 (closed form = quadrature to 8 digits) ✓.
- Full line: ∫_1^∞𝔴 dm without H-cells = log 4μ ✓; with H-cells, Σ_{cells<4000} = 5.0462 + tail ≈ 0.005 ⇒ D(15) ≈ 5.051 ✓.
- **(A1) Factor-2 error.** With one-sided mass (1−λ_k)/2, ∫_{1<ω<2}𝔴|r_k|² = ((1−λ_k)/2)·D_layer = (1−λ_k)[⅓log 4μ − 0.053844].
  This is the **one-sided** value. The memo labels it "two-sided" (end of §3 and Theorem C). The bilateral value is
  (1−λ_k)[(2/3)log 4μ − 0.107689]. Outcome item 4 ("per side") is the correct reading. Cl₂/(4π) = 0.0538443 ✓.

## 2. Regular singular point, Bessel form, width c⁻² (item 2) — VERIFIED
- Prolate ODE ((ω²−1)ψ′)′ + (c²ω² − χ)ψ = 0: ω = 1 is a regular singular point, indicial equation ρ² = 0 ⇒ exponents (0,0) ✓.
  The classical turning point ω_t = √χ/c ≈ √((2k+1)/c) < 1 is inside the window; on ω ≥ 1 there is no Airy point ✓.
- Local equation 2sψ″ + 2ψ′ + (c²−χ)ψ = 0 ⇒ ψ = J₀(√(2(c²−χ)s)) ✓; transition z ≍ 1 ⇔ ω − 1 ≍ c⁻² ✓ (not c^{−2/3}).
- Phase z = c√(ω²−1) − ((2k+1)/2)arcsec ω + O(k²/c) ✓ (∫cx/√(x²−1) and ∫dx/(x√(x²−1)) = arcsec). WKB amplitude
  ((ω²−1)(c²ω²−χ))^{−¼} ✓.
- Z.1 remains CITED (uniform Bessel expansion, Olver Ch. 12 / Dunster 1986): k fixed only; uniformity in k up to the plunge
  (k ≈ 4μ, which the ladder 4.08/1.99/1.79 uses) is **not** covered.
- **(A2) Z.2 upgradeable.** For ψ̃_k normalized on [−1,1], ∂_cλ_k = (2/c)λ_kψ̃_k(1)² (CITED: Slepian 1965; Osipov–Rokhlin–Xiao
  2013, ch. 2). Hence ψ̃_k(1)² = (c/2)∂_c log λ_k = (c/2)(−∂_c(1−λ_k))/λ_k, and for the ℝ-normalized ψ_k = √λ_k ψ̃_k:
  ψ_k(1)² = (c/2)(−∂_c(1−λ_k)). With the CITED asymptotic ∂_c log(1−λ_k) = −2 + O(k/c) this gives ψ_k(1)² = c(1−λ_k)(1 + O(k/c)),
  i.e. C_c² = 2(1−λ_k)/π — CONDITIONAL on that asymptotic, without the Bessel-zone mass bookkeeping. Recommend this proof.
- Z.4 (Bessel correction O(log c/c) relative): zJ₀² − 1/π = (1/π)sin 2z + O(z⁻²) ✓; argument fine, stays ARGUED.

## 3. Amplitude product at (s_n, T_n) (item 3) — VERIFIED
- Resonance: d/dy[z(e^y) − z(ne^y)] = 0 ⇔ s²/√(s²−1) = n²s²/√(n²s²−1) ⇔ s² = 1 + n⁻² ✓; T_n² − 1 = n² ✓.
- s_n^{½}|a(s_n)| = C n^{½}, T_n^{½}|a(T_n)| = C n^{−½}, product C² ✓ (exact).
- Hessian: with u = e^{2y}, d/dy[u/√(u−1)] = u(u−2)/(u−1)^{3/2}; at u = 1+n⁻² and v = n²+1: F″ = −c(n⁴−1)(n²+1)/n³ ✓.
- Pair (1,n): X_{1n}+X_{n1} = 2∫Lφ₁φ_n dy, φ₁φ_n = n^{−½}(s^{½}a(s))((ns)^{½}a(ns))cos·cos, ½ from cos·cos, ⇒
  n^{−½}L_nC²√(2π/|F″|)cos(Ψ_n − π/4) ✓; √(2π/c) = μ^{−½} ✓ ⇒ w_n = n/((n²+1)√(n²−1)) ✓.
- Constants: w₂ = 0.2309401 ✓, w₃ = 0.1060660 ✓, **w₅ = 0.0392546 (memo 0.03928; slip)**, Σw_n = 0.6173837 ✓,
  **Σw_n log n = 0.912641 (memo 0.913203; slip, 0.06 %)**. Neither changes any conclusion.
- Phase: Ψ_n = c(1/n − n) − ((2k+1)/2)(arctan(1/n) − arctan n) = −c(n²−1)/n + ((2k+1)/2)(π/2 − 2arctan(1/n)) ✓;
  F″ < 0 ⇒ cos(Ψ_n − π/4) ✓; outcome item 3 writes the same cosine with argument negated ✓.
- Ratios used in §5: R̂₂ = 0.22254, R̂₃ = 0.09810 per unit one-sided mass; /log 60 = 0.0544, 0.0240 ✓. s₂ at z = c/2 = 47.12 ✓.
- Remark (bookkeeping, A3): the pair (1,n) has its second point T_n = √(n²+1) ≥ √5 in the cells ω ≥ 2 where the κ-dependent
  diagonal sits; attributing the whole pair to "the layer" is a convention. Harmless for one tail; matters for (§6).

## 4. Assembly and growth (item 4) — VERIFIED (leading order, ARGUED)
- Worst-case bound (4/π)μ^{−½}Σw_n log(μ(1+n⁻²)) = 0.5893, 0.5726, 0.3709, 0.1745 at μ = 4, 15, 100, 1000 ✓; brackets
  1.741 ± 0.589, 2.622 ± 0.573, 3.887 ± 0.371, 5.422 ± 0.175 ✓ ⇒ positive at leading order for these μ, grows as (2/3)log 4μ per
  unit one-sided mass, bracket/log 2μ → 2/3 ✓.
- "Positive for every μ ≥ 4" is a leading-order statement with unwritten remainders O(log c/c) and SP remainders uniform in
  n ≲ c; the memo's own n = 5 quadrature check (−0.0005 vs −0.0039) shows the SP is unreliable for the phases at n ≥ 5 at
  μ = 15 (immaterial for the bound since |cos| ≤ 1 is used). Labels as in memo (ARGUED) are right.

## 5. Data comparison (item 5) — PARTLY FALSIFIED by ROUGH_COMPLEMENT_001
- The single-tail bound |(1,2)|/X₁₁ ≤ 0.054 is correct, and the pure ψ₄ tail (PRECHECK) −1.3 % is consistent ✓.
- Z_001 infers: the −0.48/−0.30 of TEST_BRIDGE "sits in the non-prolate component of the even-window datum (parity / rough
  complement / jump datum)". ROUGH_COMPLEMENT_001 (NUMÉRICO, g* = p + δ, p = g*_50):
  (1,2)/X₁₁ = **−0.350 for p alone**, −0.351 for δ alone, −0.479 for g*; g*'s (1,2) pair −1.529 W* = p (−0.952) + 2·cross
  (−0.493) + δ (−0.084). δ has 2.8 % of its exterior mass in ω ∈ (1,2) and S_layer(δ) = 0.007 W* vs S_layer(p) = 1.22 W*.
  ⇒ **the "rough complement" reading is falsified**: the smooth low-block part already violates Theorem C's bound by ×6.5; δ is
  not a layer object. What remains true: p's exterior datum is not a single Langer tail either (35 % of its min-gauge leak is
  outside the first 81 even prolates), so "non-prolate component of the even datum" survives only in the sense "the Möbius /
  parity image of the rung span is not a prolate tail" — which is AUDIT_10's K5 (jump/Gibbs image), now attached to p, not δ.
- §7.1 "the extremal's caustic-layer deficit (−0.55 S)": still not ω-resolved (AUDIT_10 K4). Say "resonant-pair deficit".

## 6. κΛ (item 6) — algebra VERIFIED; the conclusion must be narrowed
- H₁(ω) = Σ_{n≤ω}log n/n = 0 on (1,2) ⇒ layer diagonal κ-free (exact) ✓.
- Resonant frequency τ_n = c·s_n²/√(s_n²−1) = 2πμ·n(1+n⁻²); Θ_∞ ≈ log(τ/2π) ⇒ ½log(τ_n²/(2π)²) − κlog n =
  log μ + (1−κ)log n + log(1+n⁻²) ✓ (independently re-derived).
- **(A4) Narrowing.** "The caustic layer is Λ-independent at leading order" is proved only as: for a single prolate tail the
  layer diagonal is exactly κ-free and the κ-dependence of the resonances is O(μ^{−½}) relative (ARGUED). Only the uniform
  κ-scaling of the comb was tested, not other arithmetic weights. On the actual extremal the (1,n) pairs carry comb parts
  −(log m + log n)⟨φ_m,φ_n⟩ of O(W*) (g*: +0.375, +0.421, +0.399, +0.285 W* on pairs n = 2, 3, 5, 7; ROUGH_COMPLEMENT §3),
  not O(μ^{−½}); these pairs are not shown to be layer-localized, so the statement does not transfer. "By the semiring
  principle it is not a sign source" is a heuristic reading, not a theorem; label it so.

## 7. Corrections to apply
(A1) "two-sided" → "one-sided" in §3 end and Theorem C (or double the bracket). (A2) Z.2: use Slepian's ∂_cλ identity
(CONDITIONAL on ∂_c log(1−λ_k) → −2). (A3) note the pair bookkeeping. (A4) narrow the κΛ conclusion as above. (A5) Slips:
w₅ = 0.039255, Σw_n log n = 0.912641. (A6) §5/§7: replace "rough complement / caustic-layer deficit" attribution by
"non-prolate exterior of the rung span (p) and its cross term with δ; not ω-resolved".
Theorem C as a single-tail statement stands (Z.3, Z.5 PROVED; Z.1 CITED; Z.2 CONDITIONAL after A2; Z.4, Z.6 ARGUED).
**Do not retry:** attributing the μ = 15 resonant deficit to the rough complement δ (falsified, ROUGH_COMPLEMENT_001).
No sign claimed. L′♯ OPEN; row D OPEN.

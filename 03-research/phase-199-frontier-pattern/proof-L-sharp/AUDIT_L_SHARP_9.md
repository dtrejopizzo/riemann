# AUDIT_L_SHARP_9 — audit of PROOF_L_SHARP_Y_001 (Theorem B′, multi-cell Langer chirps, plank P2)

Phase 199,
Checked against X_001 + AUDIT_L_SHARP_8 (K₂ coefficients 1/6/2/12, constraint 20), BRIDGE_001
(B.0, planks), E_001 (E.1/E.1′/E.2/Cor E.3), J_001, SYNTHESIS §3.3 (M3), PRECHECK_T1_001, Stein 1993 VIII.1.2.
Scratch checks (numpy, not stored) are NUMÉRICO and only check algebra.

**Verdict.** Lemmas Y.1–Y.4, Theorem Y.5 and Cor Y.6 **stand as PROVED as asymptotic statements** (fixed profile, fixed η, X,
c → ∞). The phase analysis is exact. Three corrections: (C1) the bound is **not uniform in X** (E ∝ XΛ/c, 𝓡_res ∝ H_XΛ) and is
**vacuous at μ = 15 for every X ≥ 2**; (C2) "μ ≳ 10³" is the best case; typical profiles need μ ≈ 10⁴–10⁵; (C3) Cor Y.9 holds
only for μ ≥ μ₀(κ) ("every μ ≥ 4" is wrong) and is X.7(ii) re-run on a Langer phase (no new content). Leading-order resonance
numeric in §6 is 0.47 (sum from n = 1), 0.17 with the correct sum n ≥ 2 (not 0.43). Constraint 21 added. Row D OPEN.

## 1. Multi-cell expansion and truncation (priority 1) — PROVED
- u_m(y) = (ms)^{½}a(ms)e^{iφ_c(ms)}1_{y>0}. Under (Z₁), A_m(0) = m^{½}a(m) = 0 and A_m′(0) = m^{3/2}a′(m) = 0, so the truncated
  dilate is C¹ with A″ ∈ L¹ (jump of a″ allowed). That is exactly what X.5a(a) needs (two integrations by parts use only A, A′
  continuous). So with (Z₁) **no truncation term exists**; the harmonic-cutoff sawtooth enters only through the diagonal weight
  Σ_m m^{-1}1_{t>m} = H(t). C² is more than enough (C¹ + A″ ∈ L¹ suffices). Confirmed.
- Pole terms: a⌊t⌋/t and aH(t) continuous by (Z₁), one integration by parts — correct.
- Caveat: (Z₁) is a *hypothesis on data*, false for real prolate tails (§8).

## 2. Diagonal (priority 2) — PROVED
- Diagonal pair (m,m): E.1′ at α = β = 1 gives H(min) = H(t); the comb diagonal −2Σ m^{-1}ℓ_m‖u_m‖² = −2∫H₁|a|². The integrand
  H(t)log(τ/2π) − 2H₁(t), τ/2π = μt²/√(t²−1), is 𝔴_μ exactly; the log² cancellation is pointwise in t ⇒ cell by cell. Confirmed.
- Error Σ_m 1/(mΩ_m) ≤ 1/(2c) + 0.645/c = 1.145/c (Ω_m ≥ max(2c, cm), min τ = 2c at t = √2): checked.
- **Uniformity in X:** E_diag ≤ 1.6K̄‖a‖/c is X-free *given* K_a; K_a, K₂^♯ are profile constants. Uniform in X only on classes
  with bounded K_a/‖a‖. The non-uniformity of Theorem B′ lives off the diagonal (§4).

## 3. Phase analysis (priority 3) — PROVED, constants confirmed
- Right variable: y = log s, dilate m samples t = ms; ψ_{mn}(y) = φ_c(ms) − φ_c(ns), ψ′ = τ(ms) − τ(ns), τ(t) = ct²/√(t²−1),
  ψ″ = c[ms·g(ms) − ns·g(ns)], g(t) = t(t²−2)/(t²−1)^{3/2}. Re-derived.
- m = 1: τ(s) = τ(ns) ⟺ s² = 1 + n^{-2}; τ_n = c(n²+1)/n; ψ″(y_n) = −c(n⁴−1)/n − c(n⁴−1)/n³ = −c(n⁴−1)(n²+1)/n³. Checked
  symbolically and numerically (n ≤ 40). Strict concavity: s < √2 ⇒ sg(s) < 0; s ≥ √2 ⇒ tg(t) increasing. inf|ψ″_{1n}|/(cn) = 1.114
  (NUMÉRICO; the proved 0.4 is safe).
- 2 ≤ m < n: τ′ = cg ≥ 0.7698c on [2,∞) (g(2) = 0.7698, g(2√2) = 0.9163 checked) ⇒ gap ≥ 0.77cs(n−m); numerical inf 0.873. |ψ″| ≤ cns. Confirmed.

## 4. van der Corput (priority 4) — PROVED with X-dependence
- Hypotheses: ψ_{1n} real, |ψ″| ≥ 0.4cn on the whole y-support (one sign); G_{1n} ∈ C¹, vanishes at y = 0 (a(1) = 0, a(n) = 0 by
  Z₁) and at the far end. Stein VIII.1.2 Cor (c₂ = 5·2 − 2 = 8): |∫Ge^{iψ}| ≤ 8λ^{-½}(|G(b)| + ‖G′‖₁). Prefactor 2·8/√0.4 = 25.30. Confirmed.
- ‖G′‖₁ ≤ β_η‖a‖² + 2ΛK_a‖a‖: Cauchy–Schwarz ∫|A_1′A_n|dy = √n∫|sa′(s)||a(ns)|ds ≤ ‖ta′‖‖a‖ — confirmed.
- **Not uniform as X → ∞:** 𝓡_res ∝ H_X·Λ, Λ = log(μT_ηX) + 2log X ⇒ log²X growth; E contains 15√X K̄/c and 24XΛ/c. For real
  tails (X = ∞) the theorem gives nothing. Lossy steps: (a) global λ = 0.4cn instead of the local Hessian ≍ cn³ at y_n (loses n,
  produces H_X instead of Σn^{-2}); (b) |weight| ≤ Λ instead of log(μ(1+n^{-2})) at the stationary point; (c) per-pair
  Cauchy–Schwarz ∫|A_mA_n| ≤ ‖a‖² for every non-resonant pair (produces the X and √X; true overlap is ≲ ‖a‖²/√(mn) for spread profiles);
  (d) Stein's 8 vs the Fresnel constant √(2π).

## 5. Resonant weight (priority 5) — PROVED (algebra), leading size ARGUED
- ½log(τ_n²/(2π)²) − log n = log(μ(n²+1)/n²) = log(μ(1+n^{-2})). Confirmed; SYNTHESIS's c^{-½}n^{-2}log(μn) is corrected.
- Leading size for Langer density: (4M/π)μ^{-½}n^{-2}log(μ(1+n^{-2})) re-derived. Relative to M log 2μ at μ = 15: the doc's
  (2π/3) bound gives **0.47** (not 0.43); the correct sum over n ≥ 2 gives **0.17** (NUMÉRICO), consistent with PRECHECK's ±10 %.

## 6. Constants (priority 6)
- At μ = 15 (c = 94.2), X = 2, η = ½, K_a/‖a‖ = 1, H_X = 1.5: |𝓡_res|/‖a‖² ≤ 43.6 and the single term 24XΛ/c = 2.6, against
  log 2μ = 3.40. **Vacuous by a factor ≈ 13.** Equality of the bound with log 2μ needs c^{½} × 13 ⇒ μ ≈ 2·10³ in the best case;
  with K_a/‖a‖ ≈ 2, X = 10: μ ≈ 10⁴–10⁵ (C2).
- Reaching μ ~ 15–100 requires replacing (a)+(b)+(d) by **stationary phase with explicit remainder** (leading 0.17 at μ = 15;
  remainder (cn³)^{-½}·(amplitude C²-norm on the Fresnel window)) and (c) by an overlap-weighted Schur bound. Plausible only on
  regular profiles; the remainder needs exactly the amplitude regularity that fails near t = 1 (§8). OPEN.

## 7. Cor Y.9 (priority 7) — PROVED for μ ≥ μ₀(κ); redundant
- Single cell [N+δ,N+1−δ]: 𝔴^κ ≈ (1−κ)log²N + log N·log μ + O(log N) < 0 once log N > (log μ + O(1))/(κ−1); error polylog(N)/c
  (X_001 + AUDIT_8 constants) with N = μ^{O(1/(κ−1))} ⇒ polylog(μ)/μ → 0. Correct **for μ ≥ μ₀(κ)**; "every μ ≥ 4" is wrong, and
  "≤ −c′log²N" only holds well past the threshold. It is X.7(ii) of AUDIT_8 on a Langer phase: not a new falsifier.

## 8. Real tails at μ = 15 (priority 8)
- **Jumps (no Z₁):** Prop Y.7 size Σ_k|a(k)|²log(ck)/(ck); Langer |a|² = (2M/π)/(t√(t²−1)) ⇒ ≈ 0.007M vs floor 3.4M: **≈ 0.2 %** (ARGUED). Negligible.
- **Mass near t = 1:** to see resonances n ≤ N one needs η ≲ 1/(2N²); the excluded Langer mass is (2/π)√(2η) ≈ (2/π)/N and there
  K_a ≍ η^{-1/4}·(rung index) → ∞ — the c^{-½} gain is lost exactly where the resonances live. Leading size of all resonances 0.17 relative (ARGUED). OPEN.
- **Tail beyond X:** E ∝ 24XΛ/c is already ≥ 2.6/3.4 at X = 2: no X is admissible at μ = 15. OPEN.
- **Edge P3b (dominant):** −51 % of the chirp value at μ = 15 (PRECHECK_T1). Excluded by hypothesis f(λ) = 0.
- Langer-class membership of prolate continuations holds only for rungs k ≪ c (phase c√(t²−1) − (k+½)arcsec t + O(1/c)); near the plunge χ ~ c² and the phase is not of this form (ARGUED).

## 9. Constraint 21
**21 (resonances).** On Langer chirps the only c^{-½} cross-dilate effects are the (1,n) pairs, with exact stationary point
s_n = √(1+n^{-2}), Hessian −c(n⁴−1)(n²+1)/n³ and weight log(μ(1+n^{-2})) (PROVED); pairs 2 ≤ m < n are non-stationary (PROVED).
Their smallness is a regularity statement (Fresnel scale, ARGUED ≤ 0.58 block ratio) and every proved bound so far is
non-uniform in X and vacuous at μ ≤ 10³. Any use of P2 at μ = 15 must (i) be uniform in X, (ii) use stationary phase with
explicit remainder, (iii) handle t → 1 (η → 0) and the edge. (Z₁)-data say nothing about integer jumps or the t → 1 layer.

## 10. Labels
PROVED: Y.1, Y.2, Y.3, Y.4, Y.5, Y.6 (asymptotic, fixed η, X, profile), Y.9 for μ ≥ μ₀(κ). CITED: Stein c₂ = 8. ARGUED: §6 leading
size (0.17 at μ = 15 corrected), Y.7, Y.8. NUMÉRICO: g(2), g(2√2), 1.114, 0.873, Hessian. OPEN: X-uniform P2, μ ~ 15 constants,
t → 1 layer, edge P3b, gauge Π, L′♯. **Row D OPEN.**

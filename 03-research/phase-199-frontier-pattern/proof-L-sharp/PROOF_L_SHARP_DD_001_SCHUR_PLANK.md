# PROOF_L_SHARP_DD_001 — Strategy DD: the Schur-complement plank (PROVED reductions + NO-GO for the norm class + NUMÉRICO check)

Phase 199, , no zero
datum is used, and
Numerics only on existing μ = 15 data (BB_001, ROUGH_COMPLEMENT_001 §5, TEST_BRIDGE_001). No new scripts.

**Outcome.**
1. Exact plank (PROVED, standard): if QGQ ≻ 0 on V_J^⊥, then W ≥ 0 on the Galerkin space ⟺ S_V := PGP − PGQ(QGQ)⁻¹QGP ⪰ 0 on V_J.
   L′♯ on the Galerkin space follows from S_V ⪰ κ·ℓ on V_J. The sufficient form is ‖QGv‖² ≤ θ c_Q W(v) with θ < 1 and W(v) ≥ κ′ℓ(v).
2. (a) Coercivity. PROVED only on the complement of a Slepian (T,Ω_*) block of dimension N_* ≈ (2/π)T e^{𝒜_T+λ+C_∞+1}.
   This dimension is superpolynomial in μ: about 2.3·10⁶·e^{C_∞} at μ = 15. For V_J^⊥ itself (J = 50), the norm method
   is FALSIFIED by the data: λ_min(QArQ) − ‖QCQ‖_+ = 1.40 − 2.90 < 0, whereas the measured value is 1.09 > 0.
   A μ-uniform c_Q at J ≍ poly(μ) needs the Ar/C cancellation, so it is OPEN (NO-GO for the "symbol growth versus comb
   norm" class, ARGUED via Kronecker: sup_{|t|>τ} of the comb trig polynomial tends to 𝒜_T).
3. (b) Coupling via the polarized half-line identity. PROVED as a bound, but its constants are useless.
   The bound is ‖QGv‖ ≤ K_μ·ζ(½+s)λ^{−s}‖ξ^s r_v‖·sup_{w∈V^⊥}(‖ξ^s r_w‖/‖w‖), with K_μ ≥ 𝒜_T ≈ 9.94. The w-side
   is NOT at leakage scale: rough w ∈ V^⊥ have ℓ(w) ≍ ‖w‖², and Lemma 4.2 gives the upper bound ≤ C₀μ²‖w‖² with
   C₀ ≥ 8.8. The predicted ratio K_μ²(sup)²/c_Q is ≥ 90, and ≈ 1.8·10⁵ with proved constants. The required value is
   W(p)/ℓ(p) = 0.82. The bound fails by 2 to 5 orders of magnitude.
   It does not reintroduce the 34-digit cancellation: the exterior scale is right. The measured value is
   ‖QGp‖/√ℓ(p) = 0.644 = O(1). The loss comes from Cauchy–Schwarz on an indefinite form (the TV-robust class; A §5,
   BARRIER_EST Thm 4).
4. Circularity. If (a) is proved with the only available J, which is superpolynomial, then (b) on V_J is exactly
   A_001 §4's finite block (the Mori band) again. DD adds no content beyond A §4 + BB §5.
No sign claimed. L′♯ OPEN; row D OPEN.

## 0. Corpus / index check
Index: P72 (Feshbach HF/LF split, PARTIAL), P90 (Feshbach eigenline rotation, NO-GO), G7A (Schur reformulations, REF-D),
BB_001 (do not bound the depression by ‖QCp‖/‖QArp‖ separately), A_001 §4–§5 (Lemma 4.1, the N_* block, the Bochner/C–S
NO-GO), BRIDGE_001 (Ω_* = exp(4√μ+…)), Z_001/CC_001 + AUDIT_14 (Theorem C asymptotic; N = 15 not covered).
New reason (why this is not a retry): this is the first attempt to prove (rather than measure) the two Schur planks with
explicit constants, and to bound the off-diagonal coupling in exterior variables, which BB_001 identified as the only
scale free of the 34-digit cancellation. The result is that it reduces to known walls; the bookkeeping is recorded so
that DD is not retried.

## 1. Plank (PROVED)
G Hermitian on the Galerkin space H = V ⊕ V^⊥, P/Q the projectors. If QGQ ⪰ c_Q > 0 on V^⊥, then for v ∈ V:
min_{δ⊥V} W(v+δ) = ⟨v,S_V v⟩. Hence λ_A ≥ 0 ⟺ S_V ⪰ 0 (Feshbach; BB (BB.1)). Since (QGQ)⁻¹ ⪯ c_Q⁻¹,
  ⟨v,S_V v⟩ ≥ W(v) − ‖QGv‖²/c_Q,                                                                         (DD.1)
so (b) ‖QGv‖² ≤ θc_Q W(v), together with W(v) ≥ κ′ℓ(v), gives S_V ⪰ (1−θ)κ′ℓ on V. This uses ℓ(v) ≤ ℓ(v+δ*)
only for the admissible representative; the minimal-leak gauge, U_001 Thm U.2.1, is CITED. The leakage comparison between
v and v+δ is the same open gauge step as in ROUGH_COMPLEMENT (constraint list AUDIT_13/14), so L′♯ itself is CONDITIONAL
on it even when (a) and (b) hold.

## 2. (a) Coercivity of QGQ
**2.1 (PROVED, from A Lemma 4.1).** Let S_N be the span of the first N Slepian functions of the time-frequency pair
(I = (−T,T), |t| < Ω_*), with concentration eigenvalues χ_N^S ↓. For g ⊥ S_N: ‖P_<g̃‖² ≤ χ_N^S‖g‖². Lemma 4.1 then
gives W_T(g) ≥ (1 − (K+λ+1)χ_N^S)‖g‖². So c_Q ≥ ½ as soon as χ_N^S ≤ 1/(2(K+λ+1)), that is, for
N ≥ N_* + O(log(K+λ)·log(TΩ_*)) (Landau–Widom plunge, CITED). Here N_* = (2/π)TΩ_* and Ω_* = e^{𝒜_T+λ+C_∞+1}.
At μ = 15: 𝒜_T = 9.9438, T = 1.3540, λ = 3.8730, so N_* ≈ 2.35·10⁶·e^{C_∞}. Asymptotically N_* = exp(4√μ(1+o(1))),
which is superpolynomial.
**2.2 (OPEN).** V_J = span{Eψ_{4j}} is not a Slepian span. Transferring 2.1 to V_J^⊥ needs S_N ⊂ V_J up to small angle.
By A §4, the E-images of ψ_k sit below Ω_* only for k ≲ (2/π)Ω_*, because of the jumps of Eψ_k at x_n. So this transfer is
itself unproved even for J ~ N_*.
**2.3 (NO-GO for the norm class at J = 50, NUMÉRICO falsifier).** The bound "QGQ ⪰ λ_min(QArQ) − ‖(QCQ)_+‖" gives
1.40 − 2.90 = −1.50 < 0. Phrased via the growth estimate: m(τ_J) with τ_J ≈ πJ/(2T) = 58 gives
log 58 ≈ 4.06 < 𝒜_T = 9.94. The measured c_Q = 1.09 therefore comes from Ar/C cancellation on V_50^⊥ (QCQ is indefinite
with spec [−2.52, 2.90], and its positive part is matched by Ar). Smallest J for which the norm route proves c_Q > 0:
J ≳ N_*, ARGUED to be sharp in the class. Kronecker (log p independent over ℚ) puts the comb trig polynomial within ε of
its mass on t-windows of width ≍ 1/log μ ≍ 1/T at arbitrarily large |t|, so window-localized functions in V_J^⊥ see
symbol ≈ log|t| − 𝒜_T + O(1). Hence no c_Q that is polynomial in μ follows from "symbol growth vs comb norm" (ARGUED).
Comparison: proved J_* ≈ 2·10⁶ versus measured success at J = 50.

## 3. (b) Coupling in exterior variables
**3.1 (PROVED, polarization of A Thm 1.1).** For admissible real f, f′ with f(λ) = f′(λ) = 0 and g = Φ_f|_I,
g′ = Φ_{f′}|_I: W_T(g,g′) = 𝒲_ext(Ψ_f,Ψ_{f′}). Both sides are real symmetric bilinear forms, so polarize the quadratic
identity. Ψ_f = Z r_f (A Rem 1.1(ii)).
**3.2 (PROVED).** Z is unbounded on L²(λ,∞); it is bounded only on a weighted space. Write
Ψ̌ = Σ n^{−½}S_{−log n}r̃|_{(a,∞)}. Then ‖r̃1_{(a+log n,∞)}‖² = ∫_{nλ}^∞|r|² ≤ (nλ)^{−2s}‖ξ^s r‖², which gives
‖Z r‖ ≤ ζ(½+s)λ^{−s}‖ξ^s r‖ for s > ½. Unweighted leakage alone does not control Ψ. The weight costs a factor
‖ξ^s r‖/(λ^s‖r‖) ≥ 1.
**3.3 (PROVED, conditional on a kernel norm).** Let |𝒲_ext(Ψ,Ψ′)| ≤ K_μ‖Ψ‖_𝓗‖Ψ′‖_𝓗 on Z-images. Here 𝓗 is the norm
of the symbol Θ (|Θ| ≤ log(2+|t|) + C_∞ + 𝒜_T, pole ≤ λ). Then, for v ∈ V_J in the core,
  ‖QGv‖ = sup_{w∈V^⊥, core} 𝒲_ext(Zr_w,Zr_v)/‖w‖ ≤ K_μ·‖Zr_v‖_𝓗·sup_w ‖Zr_w‖_𝓗/‖w‖.                    (DD.2)
K_μ ≥ 𝒜_T: the prime part alone attains the comb mass on suitable exterior tests (ARGUED, same Kronecker argument).
**3.4 Where it fails.** The v-side is leakage-scale (good). The w-side is not. V^⊥ contains the rough Legendre modes,
whose admissible representatives have leakage comparable to their mass: ℓ(w) ≍ ‖w‖², with Lemma 4.2 bounding it above by
C₀μ²‖w‖². C₀ = 4(1/5 + 4c_B) ≥ 8.8 because c_B ≥ ½ by Cauchy–Schwarz on (−1,1). So sup_w ≥ O(1) and ≤ √C₀·μ.
(DD.1)+(DD.2) then need K_μ²·(sup)²·(weight factors)/c_Q < W(v)/ℓ(v):
| quantity (μ = 15) | value |
|---|---|
| K_μ² (lower) | ≥ 𝒜_T² = 98.9 |
| (sup)² | ∈ [O(1), C₀μ² ≥ 1980] |
| predicted ratio / c_Q (c_Q = 1.09) | ≥ 90 … ≈ 1.8·10⁵ |
| required W(p)/ℓ(p) (ROUGH_COMPLEMENT §5) | 0.82 |
| Theorem C value (2/3)log 4μ − 0.1077 (prolate tails; asymptotic, N = 15 not covered, AUDIT_14) | 2.62 |
Failure margin: 2 to 5 orders of magnitude. The failing step is Cauchy–Schwarz on the indefinite form 𝒲_ext through a
symbol/kernel norm. This is the TV-robust class (A §5, BARRIER_EST Thm 4): a bound that is blind to the sign of the comb
cannot see that W(p,·) restricted to V^⊥ is O(√ℓ(p)) with an O(1) constant. Not circular, but the class is NO-GO.

## 4. Check with data (NUMÉRICO, μ = 15, J = 50, W* = 4.763·10⁻⁷⁰)
- ‖QGp‖² = 2.982·10⁻⁷⁰ = 0.626 W*. With ℓ(p) = 1.508 W*, the measured coupling constant is
  ‖QGp‖/√ℓ(p) = 0.644. This confirms that exterior variables have the right scale (no 10³⁴ loss), unlike ‖QCp‖ = 0.2008.
- The crude (DD.1) on p gives ‖QGp‖²/c_Q = 0.574 W* and θ = 0.574/W(p) = 0.574/1.2325 = 0.466 < 1. So the plank holds on p
  with a factor-2.5 loss relative to the true depression 0.2325 W* (ratio 0.189, ROUGH_COMPLEMENT (RC)). The effective
  resolvent Rayleigh value is 0.371 = 1/2.69, inside spec R ⊂ [1/7.10, 1/1.09].
- Proved constants versus needed: K_eff² = 0.415 is needed, while ≥ 98.9 is provable. That is a gap of ≥ 240 before the
  w-side sup, and ≈ 4.8·10⁵ with the Lemma 4.2 constants.
- The 49 other directions of V_50 have O(1) coupling (BB §4, σ₁…σ₃₀ = 1.24…0.45) and O(1) W. The plank there is
  an O(1) matrix inequality with no leakage smallness, and it is not checked here.

## 5. Labels / do not retry
PROVED: (DD.1); 2.1 (coercivity off a Slepian block of superpolynomial size N_*); 3.1 (polarized half-line identity);
3.2 (weighted bound for Z); 3.3 (conditional form). NO-GO (NUMÉRICO falsifier): norm coercivity of QGQ on V_50^⊥ (1.40 − 2.90 < 0).
NO-GO (class, ARGUED): μ-polynomial c_Q from "log-symbol growth vs comb norm"; coupling via Cauchy–Schwarz with a kernel
norm of 𝒲_ext (w-side not leakage-scale, K_μ ≥ 𝒜_T). CONDITIONAL: L′♯ from (a)+(b) also needs the leakage comparison
ℓ(v) vs ℓ(v+δ*). OPEN: c_Q at J = poly(μ); a sign-sensitive bound of W(·,v)|_{V^⊥} at the scale √ℓ(v) with constant
< √(c_Q·0.82) (measured 0.644). **Do not retry:** Schur/Feshbach planks closed by operator norms or symbol/kernel norms of
G, C, Ar or 𝒲_ext; transferring A Lemma 4.1 to prolate complements of size poly(μ). No sign claimed. L′♯ OPEN; row D OPEN.

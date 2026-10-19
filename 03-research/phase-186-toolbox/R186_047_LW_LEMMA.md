# R186_047 — Lemma (L-W): coercivity of 𝔞_T on the complement of the component prolates (PROVED; constants certified by quadrature in the three windows: c_W ≥ 0.14/0.20/0.004 with the V of R186_044 and ≥ 0.59/0.55/0.32 with V′)

Phase 186, round 21. Sources cross-checked (to avoid repeating): R186_044 (§2 def. of V_T, V_T^P, W_T; Thm 1–2; §5(iv) statement of (L-W)), R186_045 §4 (plan W1), R186_042 (Thm 2.1 Pos/Neg pencil, §3.2 sub-Shannon sea, N_i ≤ 0.95), R186_025/105 (Thm A/B: coercivity of 𝔞_∞ on 𝒱_k; the corpus has **no** explicit PROVED bound of λ_min(Pos_T|𝒫_T)), R186_024/104 ((L1)), R186_026 (Tate Gram matrix: not used), R186_115 §2 (cross leakage), Paper 47 (eq:symbol, eq:form, 𝒫_T, prop:band, lem:mbounds, prop:negtrace). Self-contained script: `r047_LW.py` (copies and re-verifies r044's constructions; `python3 r047_LW.py` ≈ 6 min with M = 44/44/112; `fast` ≈ 30 s with M ≤ 36).

## 0. Verdict

1. **(L-W) is a theorem** (§2, Theorem): for every T and every symbol of the class (σ = σ₊ − σ₋ with finite negative set U = ∪ J_i), 𝔞_T|_{W_T} ≥ c_W(T) := Pos_lb(T) − Neg_ub(T), where Neg_ub = Σ_i s_i λ₁^{(i)} (s_i = max_{J_i}σ₋, λ₁^{(i)} = second per-parity eigenvalue of the component time-band operator S_i) and Pos_lb = ∫₀^∞(1 − μ̄(s))⁺ds with μ̄(s) = the norm of the **deflated** time-band operator of the sublevel set {σ_T ≤ s}. Both are spectral data of time-band operators of (T, U_T, σ_T): neither the head h* nor any cancellation is involved. **Cross leakage is not needed**: on W the bound on Neg is a sum of per-component Rayleigh bounds (Neg_T = Σ_i Neg_i, Lemma 2); the Gram bound with leakage (√λ_max(S_iS_k), §2.3) is valid but worse (0.39–0.56 vs 0.11–0.19) because the polar component (s₀ = 6.4–8.3) inflates the cross terms.
2. **Numbers (NUMERICAL, Legendre Galerkin M = 44/44/112, every component resolved; table §3).** c_W = +0.41, +0.34, +0.49 at ½log3, log 2, ½log5 (V from R186_044, dim 4/12/16) against the exact λ_min(A_WW) = 0.785, 1.365, 1.142. With V′ = V + weighted prolates (top of Neg_i per parity; dim 8/24/32): c_W = +0.55, +0.40, +0.53. What is lost is almost entirely in Pos_lb (0.58/0.45/0.61 against λ_min(Pos|_W) = 0.79/1.36/1.14): the layer-cake method does not see that W, besides avoiding U, is medium-frequency (centroid 18–36, R186_044).
3. **Certified version (V explicit = span of the Galerkin prolates, which are Legendre polynomials; every constant is a quadrature of explicit integrals, without using "λ^{Gal} ≤ λ"): PROVED in all three windows.** With the V of R186_044: c_W^cert = +0.136, +0.201, +0.004 (½log3, log 2, ½log5; the last is marginal and is not claimed as a useful margin); with V′: +0.594, +0.548, +0.318. The certification's loss is in Pos: the Hilbert–Schmidt bound on ‖(1−Π)S_{L_s}(1−Π)‖ (exact at s = 0: 0.0793 against λ_max = 0.0776 at ½log3) loses a factor of 1.5–3 at s ≈ 0.2–0.6, where the "shells" around ∂U contribute many small eigenvalues; the trace loses 2–6× (Pos_lb^tr = 0.09/0.05/0.02). If more margin were wanted, the exact point is this: **an upper bound on the norm of a deflated time-band operator of a union of 10–20 sub-Shannon intervals** better than HS (Landau–Pollak for unions: not in the corpus nor in the cited literature).
4. **Consequence (PROVED; constants certified with V′, c_W ≥ 0.32):** in Theorem 2 of R186_044 (with V′ instead of V, dim 4·#comp; with V, c_W^cert ≥ 0.14, 0.20, 0.004), the hypothesis A_WW ≻ 0 is now proved, so **λ_A(T) > 0 ⟺ C_T ∧ ρ_T < 1** in dimension 2·#comp (every block σ-computable; the Schur one inherits). Suitable for Paper 47 as a complement to Thm A/B (§5).
5. **Contact with the sign: none.** (L-W) bounds Pos and Neg **separately** (with no cancellation) and holds for any symbol of the class, including the falsifier M₁ (same components up to 0.2, R186_115): the sign lives entirely in ρ_T (R186_044 Thm 2). Row D: OPEN.

## 1. Own verifications

1.1 Construction (copied from r044 and checked): λ_A = 9.49·10⁻⁴ (½log3), 1.04·10⁻⁷ (log 2), 3.8·10⁻¹² (½log5, M = 112; r044 with M = 40: 3.84·10⁻¹²); components identical to R186_044 §2 (½log5: 8, now all resolved with M = 112: Nyquist 0.8M/T = 111 > 109). λ_min(A_WW) with the V of R186_044: 0.785 / 1.365 (R186_044: 0.785 / 1.365); at ½log5, 1.142 against R186_044's 0.847 because there only 5 of 8 components were resolved (dim V 10 against 16; smaller W ⇒ larger minimum, consistent).
1.2 Lemma 1 (W = 𝒫_T ∩ V^⊥): max|⟨ψ_i, w⟩| over the basis of W = 10⁻¹⁶–10⁻¹⁷.
1.3 Bounds against exact values (all bounds on the correct side): Neg_ub ≥ ‖Neg_WW‖ (0.17 ≥ 0.0007; 0.11 ≥ 0.0044; 0.13 ≥ 0.0245); Pos_lb ≤ λ_min(Pos_WW) (0.58 ≤ 0.79; 0.45 ≤ 1.36; 0.61 ≤ 1.14); 1 − μ̄(0) = 0.92/0.92/0.90 against the exact 1 − sup_{V^⊥}μ_F(U) = 0.92/0.92/0.90 (Lemma 3 is exact at s = 0 by construction) and 1 − sup_W μ_F(U) = 0.997/0.988/0.953.
1.4 Stability in M: ½log3 with M = 36/44: λ₁^{(i)} equal to 4 digits, Neg_ub 0.1704/0.1704, Pos_lb 0.569/0.585 (the difference is the number of "resolved" pieces of the sublevel sets, which grows with M). N_i = 0.58/0.63 (½log3), 0.30–0.54 (log 2), 0.41–0.65 (½log5): R186_042's sub-Shannon sea confirmed; λ₀^{(i)} = 0.30–0.85, λ₁^{(i)} = 0.008–0.073.
1.5 Per-sector traces (certification): tr S_E = T|E|/π and tr(S_E J) = π⁻¹∫_{E₊} sin(2τT)/τ dτ (J = reflection); verified: tr_even + tr_odd = 2N_i and tr_sec − λ₀^{Gal} = λ₁^{Gal} + 10⁻⁴ (eigenvalue tail).

## 2. Statement and proof

**Framework.** F ∈ L²(I_T), F̂(τ) = ∫F e^{iτt}, ‖F‖² = (2π)⁻¹∫|F̂|², μ_F(A) := (2π)⁻¹∫_A|F̂|². σ_T = σ₊ − σ₋ (eq:symbol), U = {σ_T < 0} = ∪_{i=0}^{n−1} J_i ⊂ [0,∞) (prop:band: finite, J₀ ∋ 0), E_i := J_i ∪ (−J_i), B_A := 1_A(D), R := 1_{I_T}. S_A := R B_A R (time-band, compact, 0 ≤ S_A ≤ 1, tr S_A = T|A|/π); Pos := Rσ₊(D)R, Neg := Rσ₋(D)R = Σ_i Neg_i, Neg_i := Rσ₋1_{E_i}(D)R; 𝔞_T = Pos − Neg (R186_034 Thm 2.1). J = reflection t ↦ −t: commutes with R, with every even multiplier, and preserves 𝒫_T (swaps the two Tate functionals). ψ_i^± := eigenvector of the maximum eigenvalue λ₀^{(i),±} of S_{E_i} in the even/odd sector; λ₁^{(i),±} := the second one; λ₁^{(i)} := max_±. V := span{ψ_i^±}, V^P := P_𝒫V, **W := (V^P)^⊥ ∩ 𝒫_T** (R186_044 §2). s_i := max_{J_i}σ₋.

**Lemma 1 (PROVED).** W = 𝒫_T ∩ V^⊥; W is J-invariant and 𝔞_T|_W splits by parity. *Proof.* For F ∈ 𝒫_T, ⟨F, P_𝒫v⟩ = ⟨P_𝒫F, v⟩ = ⟨F, v⟩. V is J-invariant (the ψ are J-eigenvectors) and so is 𝒫_T. ∎

**Lemma 2 (Neg on W; PROVED).** For F ∈ W: Neg(F) ≤ Neg_ub‖F‖², Neg_ub := min(Σ_i s_iλ₁^{(i)}, ‖Σ_i s_iS̃_{E_i}‖), S̃_{E_i} := S_{E_i} − Σ_±λ₀^{(i),±}|ψ_i^±⟩⟨ψ_i^±| ⪰ 0. *Proof.* σ₋ = Σ_iσ₋1_{E_i} (disjoint supports) ⇒ Neg = Σ_iNeg_i; σ₋1_{E_i} ≤ s_i1_{E_i} pointwise ⇒ Neg_i ≤ s_iS_{E_i} (the multiplier order is preserved under compression). F = F₊ + F₋ by parity, F_± ∈ W (Lemma 1), ⟨F,S_{E_i}F⟩ = Σ_±⟨F_±,S_{E_i}F_±⟩ (S_{E_i} commutes with J). Since F_± ⊥ ψ_i^± and S_{E_i} is compact self-adjoint within the sector, ⟨F_±,S_{E_i}F_±⟩ ≤ λ₁^{(i),±}‖F_±‖² (spectral theorem), and ⟨F,S_{E_i}F⟩ = ⟨F,S̃_{E_i}F⟩ for F ⊥ V. Sum up (or bound the operator sum by its norm). ∎
*Variant 2′ (V′ = V + {φ_i^±}, φ_i^± = top of Neg_i per parity):* Neg(F) ≤ Σ_i ν₁^{(i)}‖F‖² with ν₁^{(i)} the second per-parity eigenvalue of Neg_i (same proof without the factor s_i). Improves the polar one (s₀λ₁^{(0)} = 0.09–0.15 becomes ν₁^{(0)} = 0.01–0.03).
*Cross leakage (not necessary; PROVED as an alternative):* Gram lemma: if A_j ⪰ 0, ‖Σ_jA_j‖ ≤ λ_max(M), M_jk = ‖A_j^{1/2}A_k^{1/2}‖ (ΣA_j = B*B with B = col(A_j^{1/2}); ‖BB*‖ ≤ ‖(‖X_jk‖)_{jk}‖). With A_i = s_iS̃_{E_i} (deflated): M_ii = s_iλ₁^{(i)}, M_ik = √(s_is_k)·‖S_{E_i}^{1/2}S_{E_k}^{1/2}‖ = √(s_is_k)·‖B_{E_k}RB_{E_i}‖ ≤ √(s_is_k)·HS_{ik}, HS_{ik}² = ∫_{E_i}∫_{E_k} sin²(T(τ−τ′))/(π²(τ−τ′)²) ≤ |E_i||E_k|/(π²dist²). This is the requested "sinc(T·dist)" bound; numerically it is worse than the sum (§0.1).

**Lemma 3 (Pos on W by layer-cake; PROVED).** Let L_s := {τ ∈ ℝ: σ_T(τ) ≤ s} (s ≥ 0; bounded and a finite union of intervals by prop:band and lem:mbounds; L₀ = Ū). For F ∈ W, ‖F‖ = 1:
 Pos(F) = ∫₀^∞ μ_F({σ₊ > s})ds = ∫₀^∞ (1 − μ_F(L_s))ds ≥ Σ_k (s_{k+1} − s_k)(1 − μ̄(s_{k+1}))⁺ =: Pos_lb
for any partition 0 = s₀ < s₁ < …, where μ̄(s) := ‖S_{L_s} − Σ_{i: E_i ⊂ L_s}Σ_± λ₀^{(i),±}|ψ_i^±⟩⟨ψ_i^±|‖. *Proof.* Cavalieri layers for σ₊ ≥ 0 against μ_F; {σ₊ > s} = ℝ∖L_s. μ_F(L_s) = ⟨F,S_{L_s}F⟩ = ⟨F, S̃_{L_s}F⟩ ≤ λ_max(S̃_{L_s}) for F ⊥ V (the subtracted terms vanish). s ↦ sup_W μ_F(L_s) is nondecreasing (L_s grows), so the right-hand Riemann sum underestimates the integral. ∎ (At s = 0 it is exact: μ̄(0) = sup_{V^⊥}μ_F(U).)

**Theorem (L-W) (PROVED).** For every T > 0 and every symbol of the class, 𝔞_T|_W ≥ c_W := Pos_lb − Neg_ub. In particular A_WW ≻ 0 whenever c_W > 0, and then (R186_044 Thm 2) λ_A > 0 ⟺ C_T ∧ ρ_T < 1. *Proof.* 𝔞_T = Pos − Neg and Lemmas 2–3 per parity. ∎
Remark: the Galerkin limit is that of R186_044 §7 (A_WW bounded below because Neg is compact and, now, by the explicit c_W; c_P = λ_min(Pos|𝒫_T) is not needed, which in the corpus only has a Nazarov-type bound with no explicit constant, R186_042 Lemma 2.6; here NUMERICAL: c_P = 0.24 at log 2, 0.18 at ½log5 ≪ λ_min(Pos|_W)).

**Certified version (V explicit; PROVED with constants by quadrature).** Let V^{(M)} := span of the Galerkin ψ_i^{±,(M)} (explicit Legendre polynomials), Π its orthogonal projection, W^{(M)} := 𝒫_T ∩ (V^{(M)})^⊥ (exactly the object R186_044 computes). For F ⊥ V^{(M)}: ⟨F,S_AF⟩ ≤ ‖(1−Π)S_A(1−Π)‖ ≤ [tr(S_A²) − 2tr(ΠS_A²) + tr(ΠS_AΠS_A)]^{1/2}, where tr S_A² = HS_{AA}², tr(ΠS_A²) = Σ_j‖S_Ae_j‖², tr(ΠS_AΠS_A) = Σ_{jk}⟨e_j,S_Ae_k⟩² with {e_j} an explicit orthonormal basis of V^{(M)} (integrals of polynomials × sinc: quadrature). For Neg, per sector: ‖(1−Π)S_{E_i}(1−Π)‖ ≤ tr_sec S_{E_i} − ⟨ψ_i,S_{E_i}ψ_i⟩ = tr_sec − λ₀^{Gal} (explicit per-sector traces, §1.5; ⟨ψ,Sψ⟩ exact since ψ is a polynomial). No "Galerkin ≤ true" inequality is involved.

## 3. Verification in the three windows (`r047_LW.py`, M = 44/44/112)

| T | #comp | dim V^P | Neg_ub (Lemma 2) | ‖Neg_WW‖ exact | Pos_lb (Lemma 3) | λ_min(Pos_WW) exact | **c_W** | λ_min(A_WW) | c_W (V′) | λ_min(A_WW)(V′) |
|---|---|---|---|---|---|---|---|---|---|---|
| ½log3 | 2 | 4 | 0.170 | 0.0007 | 0.585 | 0.785 | **+0.41** | 0.785 | +0.55 | 1.250 |
| log 2 | 6 | 12 | 0.110 | 0.0044 | 0.452 | 1.365 | **+0.34** | 1.365 | +0.40 | 1.704 |
| ½log5 | 8 | 16 | 0.128 | 0.0245 | 0.615 | 1.143 | **+0.49** | 1.142 | +0.53 | 1.589 |

Certified version (V explicit; Neg by per-sector traces, Pos by HS; 72 levels in [0, 1.5]):

| T | Neg_ub^cert (V) | Pos_lb^HS (V) | **c_W^cert (V)** | Neg_ub^cert (V′) | Pos_lb^HS (V′) | **c_W^cert (V′)** |
|---|---|---|---|---|---|---|
| ½log3 | 0.186 | 0.322 | **+0.136** | 0.033 | 0.627 | **+0.594** |
| log 2 | 0.195 | 0.397 | **+0.201** | 0.054 | 0.602 | **+0.548** |
| ½log5 | 0.288 | 0.292 | **+0.004** | 0.089 | 0.406 | **+0.318** |

Readings. (i) Neg_ub loses against the exact value by a factor of 5–240: the exact value sees that F ∈ W also cannot load every component at once (sup_W μ_F(U) = 0.003–0.047) and that σ₋ is far from s_i over almost all of J_i; the per-component sum is the price of not using leakage. (ii) Pos_lb loses 0.2–0.9: it is the only structural loss (§0.3). (iii) λ_min(A_WW) = λ_min(Pos_WW) to 3 digits: **on W the form is essentially Pos**; all of D's difficulty lies in V^P ⊕ (coupling), as R186_044 states.

## 4. Honesty

4.1 **The sign.** (L-W) does not touch it and cannot touch it: it bounds Pos and Neg separately, and the bound is the same for ζ and for M₁(δ) (R186_044 table: λ_min(A_WW) = 1.63 for M₁; U_{M₁} differs from U_ζ by ≤ 0.2). It is a reduction lemma: it leaves row D per window as "C_T ∧ ρ_T < 1" in dimension 2·#comp, where ρ_T fully inherits λ_A (1 − ρ_T = 0.21, 3.7·10⁻⁴, 10⁻⁸).
4.2 **Labels.** Lemmas 1–3, the Gram lemma, the Theorem: PROVED (inequalities). Constants in §3's first table: NUMERICAL (Galerkin: λ^{Gal} ≤ λ, so Neg_ub^{Gal} could be smaller than the true value; stability in M to 4 digits, §1.4; for U ⊂ [0, 10.5] with M = 44 the Galerkin traces agree with the analytic ones to 15 digits). Second table: PROVED with certified constants (Gauss quadrature: 160 nodes per piece in τ, 400 in x, 64² in HS; the only error source is quadrature rounding, ≪ 10⁻³). At ½log5 with the V of R186_044, the certified margin of 0.004 is of the order of the levels' discretization error (72 levels): V′ is recommended there. Plan W1 of R186_045: the piece "Pos_T ≥ c_P on W (Thm B)" **did not exist** (Thm B is about 𝒱_k, not about 𝒫_T nor W; c_P on 𝒫_T only has Nazarov with no constant): it is replaced by Lemma 3, which is the new tool.
4.3 **What is not claimed.** c_W(T) > 0 is not proved for all T (the bound is evaluated per window; as T → ∞, #comp grows and Σ_is_iλ₁^{(i)} grows while Pos_lb does not: the lemma is per window, like Thm A/B). No margin of D is improved.

## 5. For Paper 47 (without touching it)

Can be integrated as "Proposition (coercivity on the prolate complement)" after thm:coer-B: statement = Theorem (L-W) with Lemmas 2–3; constants from §3 as NUMERICAL (or the certified version at ½log3 as PROVED); cross-check against eq:form (normalization (2π)⁻¹∫σ|F̂|²), the definition of 𝒫_T and prop:band (finiteness of U). Together with R186_044 Thm 2 it gives the clean statement "λ_A > 0 ⟺ H_T ≻ 0 ∧ ρ_T < 1 (dim 2·#comp)". It complements Thm A/B: those are high-pass coercivity by Tate blocks (codim 2k − 2 ≈ 22–50); this one is coercivity outside the prolate span (codim 2·#comp = 4–16), which is the basis in which the Schur part is the head.

## 6. Audit notes
- Lemma 3 uses L_s = {σ_T ≤ s} on the whole line (symmetric); the sublevel grid is h = 2·10⁻³ up to τ = 300 (prop:band: τ_last ≤ 109 at ½log5); if σ(300) ≤ s, μ̄ = 1 is taken (valid). Partition of 36 levels in [0, 1.5]; right-hand Riemann sum.
- Pieces of L_s beyond Legendre resolution (center > 0.8M/T): norm by trace T|P|/π and leakage by HS (Gram); with M = 112 this does not occur at ½log5 until s ≈ 0.9, where μ̄ ≈ 1 already.
- In V′, Lemma 3 deflates only by ψ (not by φ): Pos_lb is the same; a possible improvement not exploited.
- `fast` (M ≤ 36) leaves the distant components unresolved (log 2: 1; ½log5: 3), which enter via trace (s_i·tr S_i = 0.10 and 1.02): there c_W comes out negative; it is only a smoke test, the numbers in §3 are from the full run (M = 44/44/112).
- No equivalence with other statements; no use of zeros; the falsifier M₁ is cited only to note that the bound does not distinguish it (as it should be for a sign-free lemma).

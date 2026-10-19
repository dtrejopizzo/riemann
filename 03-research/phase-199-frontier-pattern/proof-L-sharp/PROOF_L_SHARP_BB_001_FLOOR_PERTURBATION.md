# PROOF_L_SHARP_BB_001 — Strategy BB: is the rough floor δ the first-order comb response of the prolate part? (PROVED + NUMÉRICO)

Phase 199, prover + analyst. ,
no zero datum is used,
Numerics only on existing data (Mori VIII μ = 15 even blocks A, J; MORI15 g*; ROUGH_COMPLEMENT p = g*_50, δ = g* − p; rungs
QF 1.5). Scripts: `PROOF_L_SHARP_BB_001_{split,feshbach,blocks}.py`; outputs `PROOF_L_SHARP_BB_001_data/`.

**Outcome.**
1. **Strategy BB in its stated form is FALSIFIED (NUMÉRICO, μ = 15).** With G = Ar − C (C = γI − sym A = compressed comb
   Σ_n 2Λ(n)n^{−½}(S_{log n}+S_{−log n})/2, Ar = sym J + γI = archimedean (Ω-truncated) + pole), the comb moves p out of
   V_50 at O(1): ‖QCp‖ = 0.2008, and the archimedean part does the same, ‖QArp‖ = 0.2008, the two cancelling to
   ‖QGp‖ = 1.73·10⁻³⁵ (**34 digits**). Hence (Ar − λ*)p is not small, and the BB leading order δ_BB = (QArQ)⁻¹QCp has
   norm 1.35·10³⁴‖δ‖ and cosine 0.045 with δ ((QGQ)⁻¹QCp: 1.28·10³⁴, cosine 0.115). The BB "comb-induced depression"
   ⟨QCp,(QArQ)⁻¹QCp⟩ = 3.7·10⁶⁷ W*. δ is not a perturbative response to the comb; it is the 34-digit residue of an
   Ar-versus-C cancellation in the single direction p.
2. **What is true (PROVED, linear algebra; NUMÉRICO check 2·10⁻¹⁵):** the exact Feshbach/Schur form
   δ = −(QGQ − λ*)⁻¹QGp, W* = W(p) − ⟨QGp,(QGQ−λ*)⁻¹QGp⟩ + λ*‖δ‖², with the second-order term = W(δ) = 0.2325 W*
   (the forced-cross identity of ROUGH_COMPLEMENT §5 in resolvent form). On V_50^⊥ the forms are coercive:
   spec QGQ ⊂ [1.09, 7.10], spec QArQ ⊂ [1.40, 4.76] (NUMÉRICO), so the resolvent is positive and the depression term has
   a definite sign — but its driver is QGp = Q(Ar − C)p, quadratic in the **mismatch** Ar − C, not in C.
3. **Off-diagonal coupling (NUMÉRICO):** singular values of Q·X·P_V (V = V_50): G 1.24 … 0.45 (σ₃₀), and σ₅₀ ≈ 0 (the p
   direction); C 1.55 … 0.49; Ar 1.63 … 0.08. V_50 is **not** an approximately invariant subspace of G, Ar or C; only the
   one direction p decouples. The smallness of QGp is a property of the eigen-direction, not of "prolate smoothness".
4. **Λ-input (iv) (PROVED at fixed p, trivial):** for G_c = Ar − cC, QG_c p = QGp + (1−c)QCp, so ‖QG_c p‖ = 0.2008|1−c| up
   to 10⁻³⁵: the BB depression does not scale like c² — it vanishes to second order exactly at the calibration c = 1 of
   the eigen-direction. This is a statement about p (projected from the c = 1 extremal), not about the c-family minimizer;
   no sign information for cΛ or a_P follows.
No sign of row D claimed. L′♯ OPEN; row D OPEN.

## 0. Corpus / index check
Index: P72 (Feshbach leakage HF+LF split, PARTIAL, phase-72), P90 (static Feshbach eigenline rotation, NO-GO), G7A
(Schur complement reformulations, REF-D), ROUGH_COMPLEMENT_001 (forced cross), EXTERIOR_DATUM_001 ((1,2) resonance via
Δr_out), GRAM_INERTIA_001 (Möbius basis cancels 33 digits). Why not a retry: P72/P90 split by frequency on model
operators; this is the first test of the specific hypothesis "rough floor = archimedean resolvent of the comb's action on
the smooth part of the certified extremal", using Mori's separate A (comb) and J (archimedean+pole) blocks. Result
negative; the Schur identity itself (§2) is standard and is not offered as a route.

## 1. Setup (from MORI15 §1)
Mori's blocks: A = γI − C_p (γ = 74/16, C_p prime comb), J = (arch_Ω − γ·band) + pole + U. Put C := γI − sym A,
Ar := sym J + γI, so G = sym(A+J) = Ar − C (U ≈ 10⁻⁸⁰⁰ ignored). Even sector, d = 832 Legendre modes on [−T,T],
T = ½log 15. Mori's form has no Tate side constraints in the even sector (the pole term is in J); the Euler–Lagrange
equation is the eigen-equation G g* = λ* g*, λ* = W* = 4.763·10⁻⁷⁰ (‖g*‖ = 1). The "Tate multipliers" seen earlier are
therefore absent in this normalization. Q := L²-projector onto V_50^⊥ (V_50 = rung span, TEST_BRIDGE), P = I − Q,
p = Pg*, δ = Qg*. Invariance under γ: Q(γp) = 0, so QCp, QArp do not depend on γ.

## 2. Exact equation for δ (PROVED)
Applying Q to (G − λ*)(p + δ) = 0: (QGQ − λ*)δ = −QGp. If QGQ − λ* is invertible on V^⊥ (true when λ_min(QGQ) > λ*,
NUMÉRICO 1.09 ≫ 5·10⁻⁷⁰): δ = −R QGp, R := (QGQ − λ*)⁻¹ > 0. Substituting in W(g*) = W(p) + 2⟨QGp,δ⟩ + ⟨δ,QGQδ⟩:
  W* = W(p) − ⟨QGp, R QGp⟩ + λ*‖δ‖².                                                                       (BB.1)
More generally (Schur): min_{δ⊥V} W(p+δ) = W(p) − ⟨QGp,(QGQ)⁻¹QGp⟩ for every p ∈ V when QGQ ≻ 0, so positivity of W on
the whole Galerkin space ⟺ (QGQ ≻ 0 and the Schur complement S_V = PGP − PGQ(QGQ)⁻¹QGP ≻ 0 on V). Check: (BB.1)
reproduces δ to 1.9·10⁻¹⁵ relative and ⟨QGp,R QGp⟩ = 0.232495 W* = W(δ) (ROUGH_COMPLEMENT: 1.232495 − 0.232495 = 1).
Note that "−0.47" is 2W(p,δ) = −2W(δ); the Schur depression is W(δ) = 0.23, not 0.47.

## 3. The BB hypothesis: (Ar − λ*)p small? (NUMÉRICO, arb 400 bits for the right-hand sides)
| quantity | value |
|---|---|
| ‖Cp‖, ‖Arp‖ | 1.6536 (both) |
| ‖QCp‖, ‖QArp‖ | 0.200842 (both) |
| ‖QGp‖ | 1.7268·10⁻³⁵ (34.07 digits of cancellation) |
| ‖δ‖ | 6.80·10⁻³⁶ |
| ‖(QArQ)⁻¹QCp‖/‖δ‖, cosine with δ | 1.35·10³⁴, 0.045 |
| ‖(QGQ)⁻¹QCp‖/‖δ‖, cosine | 1.28·10³⁴, 0.115 |
| ⟨QCp,(QArQ)⁻¹QCp⟩/W* | 3.7·10⁶⁷ |
| Legendre spectrum QCp (0–50 / 50–100 / 100–200 / 200–400 / 400–800 / 800+) | 54 / 15 / 13 / 10 / 4.9 / 3.2 % |
| Legendre spectrum δ (same bands) | 1.5 / 4.9 / 28 / 50 / 11 / 4.6 % |
Reading. The comb's action on p does contain rough content (QCp has a slowly decaying tail, 3 % beyond degree 800 —
consistent with truncation kinks of the shifted copies p(x ± log n) at x = ±(T − log n), ARGUED), but it is dominated by
smooth non-V_50 content (54 % below degree 50: shifted bumps are not in span{ψ_{4j}}), and all of it is matched by the
archimedean part to 34 digits. Consequently no per-prime attribution of δ is meaningful: each Q C_n p is O(10⁻¹) (at least
one ≥ 0.2/9), i.e. 10³⁴ times δ. The question "does the n = 2 shift alone reproduce δ" has answer no at every order
accessible to a linear response picture; the per-n quadrature was therefore not run.
The identification "shift by log n ↔ dilation by n in the exterior variable" is correct as kinematics (x is a log-scale),
ARGUED, but it cannot explain δ's exterior datum through a first-order mechanism.

## 4. Coupling structure (NUMÉRICO, double)
Singular values of the V_50 → V_50^⊥ blocks (σ₁, σ₂, σ₃, σ₅, σ₁₀, σ₂₀, σ₃₀, σ₅₀):
G 1.24, 1.20, 1.13, 1.01, 0.84, 0.68, 0.45, 2·10⁻¹⁶; C 1.55, 1.48, 1.46, 1.35, 1.18, 0.79, 0.49, 3·10⁻¹³; Ar 1.63, 1.43,
1.19, 1.11, 0.77, 0.34, 0.08, 2·10⁻¹⁵. The last singular value is the p direction (true value 1.7·10⁻³⁵, step 1). So
the Schur complement S_V on V_50 is an O(10⁻⁷⁰) difference of O(1) matrices in 49 of 50 directions: (BB.1) is exact
but not a perturbative expansion. spec QCQ ⊂ [−2.52, 2.90] (the comb is indefinite on V^⊥, as expected), spec QArQ ⊂
[1.40, 4.76] (archimedean coercivity on the rough complement, consistent with A Lemma 4.1).

## 5. What L′♯ reduces to in this picture (OPEN)
The correct inequality is the Schur form: ⟨QGp,(QGQ)⁻¹QGp⟩ ≤ W(p) − κℓ for p = Pg (and, for a uniform statement,
S_V ≻ κ·leak on V), measured ratio 0.189 at g* (= ROUGH_COMPLEMENT (RC)). It is not "prolate value beats a comb-squared
depression": the driver QGp is the defect of the joint archimedean/comb balance, which is 34 digits smaller than either
part. Any route that bounds the comb's contribution separately (by its norm, or quadratically through the archimedean
resolvent) loses ~10⁶⁷ W* at μ = 15.

## 6. Labels / do not retry
PROVED: (BB.1) and the Schur reformulation (standard linear algebra, given QGQ ≻ λ*); the c-family identity
QG_c p = QGp + (1−c)QCp. NUMÉRICO: all tables (one μ, Galerkin d = 832, J = 50). ARGUED: kink content of QCp.
NO-GO (NUMÉRICO falsifier at μ = 15): "δ ≈ (A_arch − λ*)⁻¹ C p at leading order", "(A_arch − λ*)p small because p is
near-prolate", "the n = 2 shift reproduces δ", "depression ∝ c² in cΛ". **Do not retry:** any perturbative expansion of the
extremal around the prolate span treating the comb (or the archimedean part) as the small parameter; bounding the
Schur depression by ‖QCp‖ or ‖QArp‖ separately. OPEN: S_V ≻ κ·leak on V_J (the (RC) inequality); μ-trend. No sign
claimed. L′♯ OPEN; row D OPEN.

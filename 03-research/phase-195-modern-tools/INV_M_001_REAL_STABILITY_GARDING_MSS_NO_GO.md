# INV_M_001 — Real stability, Gårding cones, MSS interlacing on the Euler-product block form (track M, phase 195)

Pen and paper; **no numerics**. **No sign contact. No
negative value for ζ.** The negative quantities below are values of the kernel 𝖡 at nonzero shifts or Rayleigh differences, never values
of the window form.

## 0. Index / corpus check (new reason written)
- Index hits: L22, L50 (Jensen, one-variable hyperbolicity, closed); P6-31 phase 11 (interlacing = TP, wrong sign); L32, P70, frente J
  (Lee–Yang / strong Rayleigh / GKS, dead by CA_J_002 Thm 1.3); G4A-159 G2_B8 (Euler-factor-local Lee–Yang/Pólya–Schur certification,
  DEAD T ≥ 0.5925); MW-4 (hyperbolicity as one of 8 paradigms, wrong direction); CA_E_SYNTHESIS row E9 (MSS / real stability killed by
  citation of retry + class argument, **no theorem written**); AUDIT_PHASE193_CERTAINTY rows 16, 71.
- **New reason (survey B1):** the object is the *multi-affine polarized symbol in per-prime block variables* produced by the separability
  theorem CA_E_001 Thm 1 — several variables, one block per prime — not a one-variable real-rootedness (Jensen), not TP (phase 11), not a
  ±1-gauge correlation inequality (frente J). E9 was closed without a theorem; this memo supplies the theorem.
- Grid / crossword: no cell with multivariate stability of the block form (grep "stab", "Gårding", "Borcea", "MSS" in grid/ and
  CROSSWORD-TO-D-*: no hit beyond the rows above).

## 1. The block form, exactly (PROVED, bookkeeping)
Notation of P46: profile F₀ supported in I_{T₀}, 2T₀ < log 2 (prop:AM); 𝖡(d) = 𝔞(F₀, V_dF₀), real, even, continuous;
φ(q) = 𝖡(log q) on G = ℚ_{>0}^×. Target (thm:oneprofile, prop:AM(i)): φ PD on G. Separability (CA_E_001 Thm 1): ⟺ for every finite S and
every product vector s = ⊗_{p∈S} c_p (c_p finitely supported on ℕ₀),
  Q_S(c) := Σ_{x,y∈ℕ₀^S} Π_p c_p(x_p) \overline{c_p(y_p)} · 𝖡(Σ_p (x_p − y_p) log p) ≥ 0.
**Block form.** Fix block lengths N_p and put c_p = (1, z_{p,1}, …) — or, in the survey's normalisation, c_p ∈ span{1, z_p e_{log p}},
i.e. c_p = (1, z_p). For S = {2,3}, ℓ := (log 2, log 3), α, β ∈ {0,1}²:
  p_𝖡(z₂, z₃; w₂, w₃) := Σ_{α,β} 𝖡(⟨α − β, ℓ⟩) z^α w^β      (multi-affine in the four variables, real coefficients),
and Q_S = p_𝖡(z, z̄) on the box {1,2,3,6}. Explicitly, with b₀ = 𝖡(0), b₁ = 𝖡(log 2), b₂ = 𝖡(log 3), b₃ = 𝖡(log 6), b₄ = 𝖡(log 3/2):
  p_𝖡 = b₀(1 + z₂w₂ + z₃w₃ + z₂z₃w₂w₃) + b₁(z₂ + w₂ + z₂z₃w₃ + z₃w₂w₃) + b₂(z₃ + w₃ + z₂z₃w₂ + z₂w₂w₃)
        + b₃(z₂z₃ + w₂w₃) + b₄(z₂w₃ + z₃w₂).
For general blocks c_p ∈ ℂ^{N_p} the same construction with variables z_{p,j}, w_{p,j} gives the polarized symbol
p_A(z, w) = s(z)ᵀ A s(w), A = [φ(m/k)] on the S-smooth box, multi-affine in each z_{p,j}, w_{p,j}.
**Window note (PROVED).** Shifts V_{log m}F₀, m ∈ {1,2,3,6}, lie in a window I_T iff T ≥ T₀ + ½ log 6 ≈ 0.896 + T₀. At **T = log 2** the
mixed product box does not fit; the admissible Euler-product vectors with P = {2,3} are the one-prime blocks {1,2} (T ≥ T₀ + ½log 2) and
{1,3} (T ≥ T₀ + ½log 3). So "T = log 2, P = {2,3}" decides stability of p_𝖡 (window-free, as Thm 1 is) *and* of its one-prime faces, which
are what the window log 2 actually sees. The obstruction below lives on a one-prime face, hence at T = log 2.

## 2. Decision: p_𝖡 is NOT real stable (Theorem M1, PROVED; one input CITED)
**Lemma M0 (strict 2×2; CITED via P46).** For 2T₀ small and T = log 2, b₀ > |b₁| and b₀ > |b₂|.
*Proof.* thm:band with D = log 2 (resp. log 3) and T ≥ T₀ + D/2: 𝔞_T on span{V_{−D/2}F₀, V_{D/2}F₀} is the matrix [[b₀, b_D],[b_D, b₀]]
(the Gram of two shifts). λ_A(T) > 0 strictly for T ≤ 0.8 (P46 cites [Zhu2026, Thm 1.2]); log 2 ≤ 0.8 and T₀ + ½log 3 ≤ 0.8 for small
T₀. Hence both 2×2 matrices are positive definite. ∎

**Theorem M1 (non-stability; PROVED given M0).** p_𝖡 is not real stable. Explicit witness: put
  ζ := (−b₁ + i√(b₀² − b₁²)) / b₀   (Im ζ > 0, |ζ| = 1),
then p_𝖡(ζ, 0; ζ, 0) = 0, and for every small ε > 0 there is w(ε) → ζ with p_𝖡(ζ, iε; w(ε), iε) = 0 and all four coordinates in the open
upper half-plane.
*Proof.* p_𝖡(z₂, 0; w₂, 0) = b₀ + b₁(z₂ + w₂) + b₀z₂w₂; at z₂ = w₂ = z: b₀z² + 2b₁z + b₀ = 0, roots (−b₁ ± i√(b₀² − b₁²))/b₀, non-real by
M0. For the open half-plane: w ↦ p_𝖡(ζ, iε; w, iε) is affine with w-coefficient b₁ + b₀ζ + O(ε) ≠ 0 (b₁ + b₀ζ = i√(b₀² − b₁²)), so its
root w(ε) is continuous with w(0) = ζ. ∎
**Rayleigh form.** For multi-affine real polynomials, real stability ⟺ Δ_{ij}p := ∂_ip ∂_jp − p ∂_i∂_jp ≥ 0 on ℝⁿ for all i, j (Brändén
2007, CITED). At the origin, Δ_{z₂,w₂}p_𝖡(0) = b₁² − b₀² < 0, Δ_{z₃,w₃}p_𝖡(0) = b₂² − b₀² < 0.

**Theorem M2 (structural form; PROVED, elementary).** For any S, any blocks and any real symmetric A = [φ(m/k)] on the box: if A is
positive definite on some 2-dimensional coordinate face {x, x + e_p} then p_A is not real stable; the diagonal q_A(z) := p_A(z, z) is not
real stable either. *Proof.* Specialise all other variables to 0 (stability is preserved by real specialisation, Borcea–Brändén, CITED);
the face gives a 2×2 block [[a, b],[b, a′]] with aa′ > b², and b² − aa′ < 0 violates Rayleigh (for q_A: aw² + 2bw + a′ has non-real
roots). ∎
**Reading.** Real stability of a polarized Gram symbol is a *reverse Cauchy–Schwarz* (Lorentzian, signature (1, n−1)) condition; the
target is *elliptic* (PD). The two are incompatible on every face where the target is strict. So stability is not merely unproved for the
block form: under (and unconditionally on the faces certified by Zhu) it is **false**. This is the clean NO-GO the survey asked for.

## 3. Gårding cones (PROVED / REF-D)
(a) A PD quadratic form in n ≥ 2 variables is hyperbolic in no direction (hyperbolic quadratics have signature (1, n−1), Gårding 1959,
CITED); so neither Q_S nor any one-prime face of it is a hyperbolic polynomial with a Gårding cone. (b) The hyperbolic polynomial whose
Gårding cone is relevant is det on Sym_n (cone = PSD cone), or its restriction to any linear space ℒ ∋ I of (tensor-Toeplitz) box
matrices (cone = PSD ∩ ℒ). "A ∈ Γ" is then 𝔸_M ⪰ 0 itself: **REF-D** (lem:shape-restate class). (c) Any hyperbolic h with Γ_h ⊂ PSD gives a
*sufficient* certificate A ∈ Γ_h, a statement on the values of 𝖡 only, valid verbatim for every comb: comb-generic (B″), and a cone
condition on the profile values, so it inherits thm:shape(A) under O_4/O_6 exactly as the linear certificates (no new ζ-input).
**Answer to (2):** no hyperbolicity cone exists for the block form itself; the only Gårding cone available is the PSD cone, and
membership is the target restated.

## 4. MSS interlacing families (PROVED, logical)
MSS (2015, CITED) gives: for a family {f_σ} with a common interlacing, **some** σ has λ_max(f_σ) ≤ λ_max(Σ f_σ) (and dual statements for
other roots). Row D needs **every** product vector to give Q_S ≥ 0, i.e. a universal statement; an interlacing family over Euler-product
vectors yields one good member, a quantifier mismatch (∃ vs ∀). Moreover the real-rootedness of mixed characteristic polynomials uses
PSD rank-one summands, i.e. positivity as input (circular). NO-GO for the target as stated; the method could only produce a *falsifier
search* direction (∃ a bad member), which is NUMÉRICO-type and not strictly necessary.

## 5. Relation to the frustrated cycle (m, 2m) — honest answer: NOT tied
Rayleigh differences involve b₁² — the sign of the doubling edge 𝖡(log 2) is invisible (gauge z ↦ −z leaves Δ unchanged). The witness of
M1 exists whether b₁ < 0 (the frustrated (m,2m) edge, CA_J_002 Thm 1.3 / Lemma J0′) or b₁ > 0. So the non-stability is a **signature**
obstruction, not a frustration obstruction; the +/· interplay (semiring principle) never enters. The (m,2m) edge is relevant only in the
ferromagnetic/TP readings (frente J, phase 11), which are a different class.

## 6. Screen against thm:shape and the six clauses of sec:spec
| item | verdict |
|---|---|
| (1) comb-generic / B″ | ✗ M1–M2 hold for every comb whose one-prime 2×2 faces are strict (incl. O_4: cΛ, c near 1; O_6: a_P keeps the face {1,2} for P > 2 or {1,3}) |
| (2) cone on log ζ | n/a (no cone produced; §3(c) cones are on 𝖡-values) |
| (3) integrality | n/a |
| (4) sparse-stable | ✗ statement depends on 𝖡 values only, survives O_6 |
| (5) FE coupling ≠ ζ(½+iτ) | ✗ adding an archimedean variable t (A(t) = Arch − t·Prime) gives p_{A(t)}, non-stable at t = 1 by M2 |
| (6) crossing ∂log | n/a |
| O_4 / O_6 | witness survives both (strictness is open in the coefficients) |
Net: no sign step; NO-GO for the class "real-stability / Gårding / interlacing-family arguments on Euler-product block symbols".

## 7. Labels
- Block form §1: PROVED. Window note: PROVED.
- M0: CITED (P46 thm:band + Zhu strict bound T ≤ 0.8).
- M1, M2: PROVED (given M0; M2 unconditional on any strict face).
- §3 Gårding: (a) CITED, (b) REF-D, (c) ARGUED (class transfer).
- §4 MSS: PROVED (quantifier mismatch).
- §5: PROVED (Δ sign-blind).
- Route status: **NO-GO** (stability is false for the block form; Gårding = PSD restatement; MSS wrong quantifier). No residue opened.

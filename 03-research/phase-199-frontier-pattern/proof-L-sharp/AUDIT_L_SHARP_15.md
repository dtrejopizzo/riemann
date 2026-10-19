# AUDIT_L_SHARP_15 — audit of PROOF_L_SHARP_DD_001 (Schur plank), PROOF_L_SHARP_EE_001 (exterior variational), TEST_2X2_001

Phase 199, "E1" is
not a criterion. Checked against A_001 (Lemma 4.1, 4.2,
Cor 4.3), BB_001, ROUGH_COMPLEMENT_001 §5, EXTERIOR_DATUM_001, AA_001, Z_001/CC_001, AUDIT_13/14, and `TEST_2X2_001_data/galerkin_2x2.json`.
No new runs: every number below is re-derived by hand from the memos' own inputs.

**Verdict.** DD: ACCEPTED WITH CORRECTIONS (one substantive: its plank fails as an operator statement at J = 50, see D4).
EE: ACCEPTED WITH CORRECTIONS (the 0.324 is a different split from ROUGH/TEST; reduction to AA_001 accepted).
TEST_2X2: ACCEPTED WITH CORRECTIONS (b_J reading is an interlacing theorem; the vector-level exterior bracket is tautological on the
minimizer; "exterior basis is the right one for a proof" downgraded to ARGUED). None of the three contains a PROVED statement
beyond standard identities, elementary bounds and NO-GOs. No sign of row D. L′♯ OPEN. Row D OPEN.

## 1. DD_001
D1. **Plank (DD.1)** — Feshbach/Schur, standard. PROVED. The CONDITIONAL on the leakage comparison ℓ(v) vs ℓ(v+δ*) is correctly flagged.
D2. **2.1 coercivity off a Slepian block** — verified. For g time-limited to I and g ⊥ first N prolates of (I, Ω_*):
‖P_<g̃‖² ≤ χ_{N+1}‖g‖² (min–max for TPT; DD's index χ_N is off by one, harmless). Lemma 4.1 then gives W ≥ (1 − (K+λ+1)χ)‖g‖²
(Lemma 4.1's proof actually yields K+λ; the statement with +1 is weaker, fine). c_Q ≥ ½ needs χ ≤ 1/(2(K+λ+1)): beyond the plunge,
N ≥ N_* + O(log(K+λ)·log(TΩ_*)) (Landau–Widom, CITED). N_* = (2/π)(1.3540)e^{9.9438+3.8730+1} = 0.862·2.72·10⁶ ≈ 2.35·10⁶·e^{C_∞} ✓.
Label PROVED, but it is a repackaging of A_001 Cor 4.3 (𝒯_*) in Slepian coordinates, not a new estimate; and it is on S_N^⊥, not V_J^⊥
(DD 2.2 correctly marks the transfer OPEN). Superpolynomial (exp(4√μ(1+o(1)))) — ARGUED via 𝒜_T ~ 4√μ, not line-checked.
D3. **Norm NO-GO at J = 50** — 1.40 − 2.90 = −1.50 < 0 vs measured b_50 = 1.0895 (TEST table) ✓: NUMÉRICO falsifier of the method.
τ_J ≈ πJ/(2T) = 58.0, log 58 = 4.06 < 9.94 ✓, but τ_J treats V_J^⊥ as band-limited, which DD 2.2 itself denies: heuristic.
"Kronecker" class NO-GO: ARGUED (no quantitative simultaneous-approximation statement is given) — label correct as ARGUED; it must not
be cited as NO-GO without "(ARGUED)".
D4. **Coupling in exterior variables.** 3.1 polarization: PROVED (bilinear symmetric forms). 3.2: Σ n^{−½}(nλ)^{−s} = ζ(½+s)λ^{−s},
s > ½ ✓ PROVED (elementary). 3.3 CONDITIONAL on K_μ, and K_μ ≥ 𝒜_T is ARGUED. Ratios: 𝒜_T² = 98.9; 98.9/1.09 = 90.7 ✓;
C₀μ² ≥ 8.8·225 = 1980 ✓ (c_B ≥ ½ by C–S on (−1,1) with ∫B = 1 ✓); 98.9·1980/1.09 ≈ 1.8·10⁵ ✓. Required 0.82 = 1.2325/1.508 ✓.
Numbers: 2.982/4.763 = 0.626 ✓; √(0.626/1.508) = 0.644 ✓; 0.626/1.09 = 0.574 ✓; 0.574/1.2325 = 0.466 ✓; 0.2325/0.626 = 0.371 ✓;
98.9/0.415 = 238 (memo "≥ 240": round to ≈ 240).
**Erratum E-DD1 (wording):** "K_eff² = 0.415 is needed" — 0.415 is the *measured* ‖QGp‖²/ℓ(p); the *allowed* value is
c_Q·W(p)/ℓ(p) = 1.09·0.817 = 0.891. Consistency: 0.415/0.891 = 0.466 = θ ✓ (so 0.644 and θ = 0.466 are one number).
**Correction C-DD2 (substantive):** "the plank holds on p" is a single-vector statement. The sufficient form must hold on all of V_J;
TEST_2X2 gives sup_{v∈V_50} ‖QGv‖²/(b_50 W(v)) = θ_50 = **1.0075 > 1**. So the crude plank (DD.1)+(b) **fails at J = 50 as an operator
inequality** (by 0.75 %), and holds on V_J only via the exact resolvent (θ′_50 = 0.388). DD §4's "the plank holds on p" must read
"holds on p only; fails on V_50 (TEST θ_50 = 1.0075)".
D5. Circularity remark (§DD.4) accepted.

## 2. EE_001
E1. **Prop EE.1** (EL in Galerkin): PROVED — it is Courant–Fischer for a pencil on a finite space; attainment in V_μ CONDITIONAL. Content
is a reformulation (as the memo says).
E2. **EE.2 / Lemma E.1.** Lemma E.1 is PROVED (AUDIT_13 §1, identity (D.1)). The derived statement "Δr_out = L_μσ + ρ_reg with σ the
m = 1 line" is PROVED for the singular (edge) content only; "σ is to leading order the line in ρ_pro" is ARGUED (EXTERIOR §3), and
AUDIT_13 C1/C2 apply: lower-cut phases are 2πω/(mλ) term-by-term, and σ ~ 1/x makes the dilate series only Abel/L² convergent. Label:
structure PROVED (singular part), identification with ρ_pro's line ARGUED. "Resonant by construction" follows from the dilation identity
D_n D_{1/m} = D_{n/m}, hence NO-GO for "B′ on the complement" is correct within that class (the class is narrow; label NO-GO (class)).
E3. **Bracket.** A + 2C + B = 1.954 − 1.380 + 0.752 = 1.326 ✓ (vs Galerkin 1.2325: +7.6 %, same closure as TEST); C²/(AB) =
0.4761/1.4694 = 0.324 ✓; mass a, b, |c| = 3.68, 1.89, 1.50 ✓; S: 1.074, 0.297, 0.322 ✓; pencil bottoms 1.04 / 0.18 ✓ (rounding).
**Correction C-EE1:** this bracket splits **p itself** (prolate tails pro04 vs Möbius complement Δr). It is NOT the split of ROUGH/TEST
(g* = p + δ), nor DD's (V_J vs V_J^⊥ at operator level). The memo's sentence "complement is weaker than the prolate block" refers to
Δr, not to V_J^⊥.
E4. The three reasons for non-uniformity: (1) c non-decaying under coherence — ARGUED (Cor C′.2 log growth); (2) no uniform b on free
complement data — supported by constraint 3 and GRAM_INERTIA null vector: accepted (NUMÉRICO + PROVED symbol fact); (3) graph collapse:
on {(ρ_pro, L_μσ)} the 2×2 matrix is the Gram of two vectors in a one-parameter family, so the bracket reduces to the scalar 𝔔[p] —
correct, PROVED (trivial linear algebra). Reduction to AA_001 vᵀGv ≥ κS: ARGUED (identification of the q-grouping), accepted.

## 3. TEST_2X2_001
T1. Table: entries match `galerkin_2x2.json`; spot-checked η_J = θ_J b_J: 1.0075·1.0895 = 1.098 ✓; 1.587·0.5992 = 0.951 ✓.
T2. **Reading of b_J (correction C-T1).** For ANY J-dimensional V ⊂ H, Courant–Fischer gives λ_min(QGQ|V^⊥) ≤ λ_{J+1}(G), with equality
iff V is the bottom-J spectral subspace. So b_J ≈ λ_{J+1}(G) (b_1 = 3.59·10⁻⁶² = 7.5·10⁷ W* vs λ₂ ≈ 0.92–1.04·10⁸ W*) says that V_J is
*nearly the best possible* J-block, not the wrong block. Non-coercivity below J ≈ 20 is **spectral and basis-independent**: G has
≈ 20 eigenvalues below O(1) (geometric prolate ladder), and no choice of V_J with J < 20 can make the complement O(1)-coercive.
The hypothesis "b_J is tiny because V_J is the wrong block" is REJECTED; the memo's wording "contains the (J+1)-th prolate-type
eigendirection" is right in substance and should cite interlacing (PROVED).
T3. **Exterior vector-level bracket (correction C-T2).** On the minimizer, Galerkin c = W(p,δ) = −W(δ) + λ*‖δ‖² ≈ −b, so c² < ab ⟺
b < a ⟺ W(g*) = a + 2c + b > 0 (to O(λ*)). Check: c_gal/b_gal = −0.232/0.232; c²/(ab) = 0.232²/(1.2325·0.232) = 0.188 = ROUGH (RC)
ratio 0.189 = depression/W(p). Hence the vector-level 2×2 test is **a restatement of W(g*) > 0**, not evidence for the operator-level
coupling. The exterior numbers (no cancellation, ≤ 0.43 digits; closure +7…+13 % on a, within margins 0.51–0.59) are correct
NUMÉRICO and do show the exterior is the cancellation-free *scale*; but "exterior basis is the right one for a proof" is ARGUED, since
the operator-level sup over δ ∈ V_J^⊥ (the only thing a proof needs) is not computed. θ′_ext ≈ 0.15 uses the S-majorant normalization.
T4. Feshbach check (≥ 20 digits for J ≥ 2; J = 1 to 15): consistent with the arb pipeline; accepted NUMÉRICO.
T5. "μ-trend not available": correct and important — every constant in all three memos is at μ = 15 only.

## 4. Reconciliation of the coupling constants
| constant | object | split | normalization | value |
|---|---|---|---|---|
| ‖QGp‖/√ℓ(p) (DD) | operator sup over V_50^⊥, vector p | V_J ⊕ V_J^⊥ (window) | √leakage | 0.644 ⇔ θ_p = 0.466 (crude, 1/c_Q) |
| θ_50 (TEST) | operator sup over V_50 × V_50^⊥ | same | b_J·W | 1.0075 (crude) |
| θ′_50 (TEST) | exact resolvent, sup over V_50 | same | W | 0.388 |
| depression ratio (ROUGH/TEST) | exact resolvent on p | same | W(p) | 0.189 (= c²/(ab) vector level, tautological) |
| θ′_ext ≈ 0.15 (TEST) | vector level p vs δ = Qg* | same, exterior evaluation | S-majorant | 0.15 |
| C²/(AB) (EE) | inside p: pro04 vs Δr | prolate tails vs Möbius complement | any (Gram ≈ diag) | 0.324 |
They are **not** one quantity. DD 0.644 and θ = 0.466 are the same number (0.644²/(1.09·0.817) = 0.466). TEST 0.15 and the 0.189
ratio are vector-level along the minimizer (restatements). EE 0.324 is a different split of p and does not enter the Schur plank.
**Single remaining inequality (OPEN):** on the Galerkin space at μ, for all v ∈ V_J (J = poly(μ)),
 ⟨QGv,(QGQ)⁻¹QGv⟩ ≤ (1 − κ) W(v)  and  W(v) ≥ κ′μ^{−A}ℓ(v),
with QGQ ≻ 0 on V_J^⊥. Measured margin at μ = 15, J = 50: 1 − θ′_50 = **0.612** (sup over V_50); on p alone 0.811. The crude
(norm) version has margin 1 − 1.0075 < 0. Note the exact-resolvent form for all v is a restatement of positivity of G on the
Galerkin space; the content is the *uniform leakage-scale margin* κ, not < 1.

## 5. Constraint update
27. **(plank in exterior variables)** The Schur plank S_V ⪰ κℓ on V_J is the remaining form; its crude version with 1/c_Q fails on
V_50 (θ_50 = 1.0075) even though it holds on p (0.466); any proof must keep the resolvent (QGQ)⁻¹, or a sign-sensitive substitute.
Coercivity of QGQ: PROVED only off a Slepian block of size ≈ exp(4√μ); below J ≈ 20 at μ = 15 non-coercivity is forced by
interlacing (basis-independent). Coupling at operator level in exterior variables: **OPEN** (not computed; vector-level numbers are
restatements of W(g*) > 0). Norm/kernel Cauchy–Schwarz on 𝒲_ext: NO-GO (ARGUED class, factors 90–1.8·10⁵).

## 6. Labels summary
PROVED: (DD.1); DD 2.1 (repackaged A Cor 4.3); DD 3.1, 3.2; EE.1 on Galerkin; EE.2 singular structure; graph collapse; TEST θ′ < 1 ⟸ G ≻ 0;
b_J ≤ λ_{J+1}(G) (interlacing, added here). CONDITIONAL: DD 3.3 (K_μ), EE.1 in V_μ, L′♯ via (a)+(b) (gauge step). ARGUED: Kronecker NO-GO,
K_μ ≥ 𝒜_T, σ ≈ ρ_pro line, EE non-uniformity (1), reduction to AA_001, "exterior basis right for a proof". NO-GO: norm coercivity at J = 50
(NUMÉRICO); B′ on resonant complement (class); crude Schur plank on V_50 (NUMÉRICO, added here). NUMÉRICO: all tables (μ = 15 only).
No sign of row D is claimed. L′♯ OPEN. Row D OPEN.

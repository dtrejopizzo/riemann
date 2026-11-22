# R186_046 — Theorem X per window: constants, converse and arithmetic form

Phase 186, round 21 (reserve from R186_045 §5). NO-GO / NUMERICAL. Paper 46, the grid and the crossword are not touched. Self-contained script: `r046_X.py` (M = 48, 7 s).
Read: R186_045 §2 (Theorem X), §3.4 (Lemmas T/T′); R186_032 §4 (Ω, S2); R186_042 (sub-Shannon sea, Landau–Widom table);
R186_043/044 (coupling, Schur ρ_T); R183_031 Thm 1; R166_501 (G),(N); Paper 46 prop:band, prop:negtrace, prop:align,
lem:roughEF; r034_det.py, r043_wh.py (constructions copied, not imported).

## 0. Verdict

1. **Theorem X with constants (§2): PROVED mod. CITED.** For F in the prolate space E_η(U₀,T) ∩ 𝒫_T (dimension
 N_η − 2, N_η = T|U₀|/π − (2/π²)Σ_i log c_i·log((1−η)/η) + o(log T), Landau–Widom), λ_A(T) ≥ 0 exactly imposes
 ⟨S_T⟩_F ≤ ⟨σ_{T₀}⟩_F + ℓ_T(F), with ℓ_T(F) = (1/2π)∫_{U₀^c}σ_T|F̂|² the leakage, bounded above by η·sup_{U₀^c}σ_T
 (on the leakage region) and below by −(the mass of σ_T⁻ in U_T∖U₀ seen by F). Corrects a sign error of R186_045 §2.2(iii):
 the bound is S_T ≤ σ_{T₀} = −|σ_{T₀}|, not "≤ −σ_{T₀}". It is identity + λ_A ≥ 0: it carries no sign.
2. **Pointwise, X is false at the 0 component** (S_T(0) = Σ_{new}v_n > 0 always): X is intrinsically averaged
 at resolution π/T, and for T ≤ ½log7 the resolution η = 0.1 gives N_η ≤ 1 < 2 = #Tate: **E_η ∩ 𝒫_T = 0, X is vacuous**; with η = 0.5,
 dim ≤ 5 (NUMERICAL).
3. **Converse: NO-GO with a number (§3).** The weakest condition of the requested form (X on E_η ∩ 𝒫_T with margin)
 holds in every window with c_η = 0.03–0.13 ≫ λ_A = 10⁻⁷…10⁻¹², and the complement W = 𝒫_T ⊖ (E_η ∩ 𝒫_T) has
 λ_min(𝔞_T|W) = −3.3 (½log3 → ½log5): the sign lives in W and in the coupling, not in U₀. Where it fails: (i) a new
 negative set (70% of Neg(h*) at ½log5 is in the new component [4.24, 6.46] ∉ U₀) and (ii) even with no new
 components (log 2 → ½log5, new prime 4), in the U₀ prolates with λ_j < 1−η (plunge zone). Iterating to the full U_T with
 η = 0.5 still gives margin 10⁻³…10⁻⁴ ≫ λ_A: the sign stays in the complement at every finite resolution ⇒ the condition
 must be 𝔞_T ≥ 0 on 𝒫_T: **D rewritten**. Agrees with W-loc (R186_044 Thm 2) and Lemma T′.
4. **Arithmetic property (§4, NUMERICAL):** the new primes do NOT cancel σ_{T₀} on U₀ component by component (averages with
 both signs; only 1 of 8 components at ½log5 → ½log7 cancels in sign and magnitude); the phases at the centers
 2πk/log 2 are equidistributed (Weyl: mean 10⁻⁵). The arithmetic form of X at resolution π/T is lem:roughEF + the absence
 of zeros in U₀ (= (N′), R183_031 Thm 1): **it is not a new statement about Λ**. M₁ (same primes) satisfies X on
 E_{0.5}(U₀)∩𝒫_T with c_η = +0.08, +0.07 while λ_A(M₁) = −1.5·10⁻³, −5.0·10⁻³: **window X does not distinguish M₁**.
5. **Contact with the sign: none.** Row D: OPEN. What remains as a lemma ∀T is in §5.

## 1. Framework and basic identity

Notation (Paper 46 eq:symbol/eq:form; r034): σ_T(τ) = m(τ) − Σ_{log n<2T} v_n cos(τ log n), v_n = 2Λ(n)/√n; I_T = [−T,T];
𝒫_T = {F ∈ L²(I_T) : ∫F e^{±t/2} = 0}; 𝔞_T(F) = (1/2π)∫σ_T|F̂|²; λ_A(T) = inf_{𝒫_T,‖F‖=1} 𝔞_T(F). For T₀ < T:
 S_T(τ) := Σ_{2T₀ ≤ log n < 2T} v_n cos(τ log n), σ_T = σ_{T₀} − S_T, U₀ := {σ_{T₀} < 0} (symmetric, finite union of
 intervals J_i ∪ −J_i, prop:band), |U₀| := two-sided measure, N_Sh(U₀) := T|U₀|/π.
Boundary convention: at T = ½log p exactly, prime p is not yet contact (c_F(2T) = 0 for F ∈ L²(I_T)); it enters with a
continuous contribution from 0 (lem:contA). Hence the "new primes" from ½log3 → ½log5 are {3, 4}, not {4, 5}; 5 enters at ½log5 → ½log7.
For F ∈ L²(I_T) write w_F := |F̂|²/(2π‖F‖²) (total mass-1 density) and ⟨g⟩_F := ∫_{U₀} g w_F.

**Lemma 1.1 (identity; PROVED, elementary).** For every F ∈ L²(I_T) in the form's domain,
 (1/2π)∫_{U₀} S_T|F̂|² = (1/2π)∫_{U₀} σ_{T₀}|F̂|² + ℓ_T(F) − 𝔞_T(F), ℓ_T(F) := (1/2π)∫_{U₀^c} σ_T|F̂|².
*Proof.* σ_T = σ_{T₀} − S_T on U₀, and 𝔞_T = (1/2π)∫_{U₀}σ_T|F̂|² + ℓ_T. ∎
This is R186_004 Cor 1.2 (exact Δ_{T₀,T}) written in frequency. The Lemma uses nothing about Λ.

**Lemma 1.2 (Slepian; CITED).** S_{U₀} := R_T 1_{U₀}(D) R_T on L²(I_T) has eigenvalues 1 > λ_1 ≥ λ_2 ≥ … > 0, and for
F ∈ E_η := span{ψ_j : λ_j ≥ 1−η} we have ∫_{U₀^c} w_F ≤ η (not just for the eigenvectors: S_{U₀}|E_η ≥ 1−η). Since |F̂|²
is even for F real, U₀ and the ψ_j are treated via the pair J_i ∪ −J_i.

## 2. Theorem X per window

**Theorem X(T₀,T) (PROVED mod. CITED in (c)).** Let T₀ < T, U₀, E_η as above, and suppose λ_A(T) ≥ 0. Then:
(a) For every F ∈ E_η ∩ 𝒫_T, ‖F‖ = 1 (subspace of dimension ≥ N_η − 2, N_η := dim E_η; Tate costs ≤ 2):
 ⟨S_T⟩_F ≤ ⟨σ_{T₀}⟩_F + ℓ_T(F) = −⟨|σ_{T₀}|⟩_F + ℓ_T(F). (X_η)
 Equivalently, in matrix form on an orthonormal basis Q of E_η ∩ 𝒫_T: Q^T M_S Q ≤ Q^T(M_{σ₀} + L)Q, with
 M_S, M_{σ₀} the forms of S_T, σ_{T₀} restricted to U₀ and L = 𝔞_T − (M_{σ₀} − M_S) the leakage form (all σ-computable).
(b) Leakage bounds: −∫_{U_T∖U₀} σ_T⁻ w_F ≤ ℓ_T(F) ≤ η·sup{σ_T(τ) : τ ∈ U₀^c, |τ| ≤ R} + ∫_{|τ|>R} σ_T w_F for every R
 > τ_last(T). The lower bound is the new negative mass (created by S_T outside U₀) seen by F; the upper bound is the prolate
 leakage from the logarithmic growth of m (σ_T ≤ m + Σ_{𝒩_T}v_n). Dividing (X_η) by ⟨1⟩_F ≥ 1−η: the prolate average
 of S_T over U₀ is ≤ −(average of |σ_{T₀}|) + O(η)/(1−η) − (new negativity)/(1−η).
(c) (CITED Landau–Widom 1980, in R186_042's table normalization: #{λ_n > α} = 2c/π + π⁻² log c·log((1−α)/α) + o(log c),
 c = T·half-width; applied to each pair J_i ∪ −J_i with c_i = T|J_i|/2; for finite unions CITED-NOT-VERIFIED, cf. R186_112):
 N_η = T|U₀|/π − (2/π²)·Σ_i log c_i·log((1−η)/η) + o(log T) (T → ∞, U₀ fixed).
 That is: λ_A(T) ≥ 0 imposes ≈ T|U₀|/π − O(log T) independent linear inequalities on the sum of new primes,
 one per width-π/T frequency packet in U₀ — this is the "resolution π/T" of R186_045 §2.2(iii).
(d) For F = ψ_j an eigenvector, (X_η) reads: Σ_{2T₀≤log n<2T} v_n c_{ψ_j}(log n) ≥ −(1/2π)∫_{U₀}σ_{T₀}|ψ̂_j|² − ℓ_T(ψ_j), where
 c_ψ(u) = ∫ψ(t)ψ(t−u)dt: each inequality is a finite linear combination of values of Λ on (e^{2T₀}, e^{2T}).
*Proof.* (a) Lemma 1.1 with 𝔞_T(F) ≥ λ_A(T)‖F‖² ≥ 0; dim(E_η ∩ 𝒫_T) ≥ N_η − 2 because 𝒫_T has codimension 2. (b) ∫_{U₀^c}w_F
≤ η (Lemma 1.2); σ_T ≥ −σ_T⁻ and σ_T⁻ ⊂ U_T. (c) Landau–Widom + additivity of the count on separated components at scale
≫ 1/T (CITED). (d) Parseval. ∎
**Correction to R186_045 §2.2(iii).** There it is written "≤ −σ_{T₀}(τ)·(1+o(1)) < 0"; with σ_{T₀} < 0 on U₀ the right-hand side is
positive. The correct statement is S_T ≤ σ_{T₀} = −|σ_{T₀}| (in prolate average): the sum of new primes must be
**negative** and at least as large as |σ_{T₀}|, up to leakage. Same content, corrected sign.

**Remark 2.1 (X is not pointwise; PROVED).** S_T(0) = Σ_{new} v_n > 0 (every cosine equals 1), while σ_{T₀}(0) =
C_0 − Σ_{𝒩_{T₀}}v_n < 0: at the 0 component, σ_T(0) < σ_{T₀}(0) < 0 (at ½log3 → ½log5: −8.31 < −6.35). So X fails
pointwise at J_0 ∋ 0 for every T₀ < T, and can only hold on average: at small T because Tate (2 directions)
consumes the only prolates of J_0 (N_Sh(J_0) = 2Tτ₁/π ≈ 1.2–2.4 for T ≤ ½log7); at large T through the positivity of the
J_0 packets via the leakage and the average of S_T (§4.3). It is the window form of prop:negtrace(ii): "the band does not
decide."

**Remark 2.2 (NUMERICAL: X's real content for T ≤ ½log7).** With η = 0.1, N_η = 1 in every window (½log3 →
log 2, ½log5, ½log7; log 2 → ½log5, ½log7; ½log5 → ½log7): E_η ∩ 𝒫_T = 0 and (X_η) is vacuous. With η = 0.5, dim(E_η ∩ 𝒫_T) =
1, 2, 2, 3, 4, 5 respectively. Slepian vs Shannon count: #{λ_j > ½} = 3, 4, 4, 5, 6, 7 against N_Sh = 3.04, 3.53, 4.27,
5.96, 7.21, 8.52 (Landau–Widom log term with c_i ∈ [0.9, 3]: pre-asymptotic regime, as in R186_042). X's "resolution
π/T" is, in these windows, 1 to 5 inequalities.

## 3. Converse: the weakest condition and where it fails

**Proposition 3.1 (Schur decomposition; PROVED).** Let E := E_η ∩ 𝒫_T, W := 𝒫_T ⊖ E, c_E := λ_min(𝔞_T|E), c_W :=
λ_min(𝔞_T|W), κ := ‖𝔞_T|_{E×W}‖. Then
 λ_A(T) ≥ (c_E + c_W)/2 − √(((c_E − c_W)/2)² + κ²),
and condition (X_η) with margin (c_E ≥ c > 0) implies λ_A(T) ≥ c′ > 0 **if and only if** moreover c_W > 0 and c_E·c_W > κ² (Haynsworth).
*Proof.* 2×2 block Weyl; the "only if" is the inertia of the block matrix [[c_E, κ],[κ, c_W]] (Schur). ∎
So the weakest condition of the requested form is: (R) := (X_η) with margin + c_W > 0 + κ² < c_E c_W. The last two are
conditions on σ_T **outside E**, i.e. on (σ_T)⁻ in U_T∖U₀ and on the U₀ prolates with λ_j < 1−η.

**Theorem 3.2 (NO-GO with a number; NUMERICAL on PROVED).** In the six computed windows (ζ, M = 48, η = ½):

| T₀ → T | new primes | λ_A(T) | c_E (X with margin) | c_W | κ | Neg(h*) in U₀ / in new comp. |
|---|---|---|---|---|---|---|
| ½log3 → log 2 | 3 | 1.03e-7 | +0.128 | −0.023 | 0.45 | 0.006 / 0.241 |
| ½log3 → ½log5 | 3, 4 | 3.65e-12 | +0.072 | −3.29 | 0.37 | 0.066 / 0.159 |
| ½log3 → ½log7 | 3, 4, 5 | ≈ 0 (3.6e-14, unresolved) | +0.035 | −4.09 | 0.27 | 0.200 / 0.119 |
| log 2 → ½log5 | 4 | 3.65e-12 | +0.0020 | −0.32 | 0.27 | 0.224 / 0.000 |
| log 2 → ½log7 | 4, 5 | ≈ 0 | +0.0036 | +1.7e-10 | 0.51 | 0.063 / 0.256 |
| ½log5 → ½log7 | 5 | ≈ 0 | +0.00060 | +3.2e-9 | 0.54 | 0.057 / 0.262 |

Reading. (i) (X_η) always holds with margin c_E ≫ λ_A (ratio 10⁶–10¹²): **the condition on U₀ is never the
bottleneck**. (ii) c_W < 0 or c_W ≈ 0 (≤ 10⁻⁹) and κ² ≫ c_E·c_W in every case: Prop. 3.1 gives nothing, and not for lack of
refinement but because the sign is in W. (iii) At ½log3 → ½log5 the minimizer h*_T has 70% of its negative mass in the
new component [4.24, 6.46] created by primes 3 and 4 outside U₀ = (0, 3.31) ∪ (6.95, 10.53): no condition on
U₀ sees that component. (iv) At log 2 → ½log5 (new prime 4) **no new component with mass is created** (U_T is a deformed U₀ plus two
components at 62 and 108 with mass 0 at h*) and yet c_W = −0.32: the negativity lives in the U₀ prolates with λ_j < ½ (plunge), beyond the
reach of (X_η) for every η with E_η ∩ 𝒫_T ≠ 0. (v) At ½log7, λ_A = 3.6·10⁻¹⁴ with the next three eigenvalues 3.7·10⁻¹⁴, 9.5·10⁻¹⁴: numerical
floor of M = 48 (Nyquist τ ≈ 50 does not resolve the components at 62–200); used only as "≈ 0", not as a value. ∎

**Iteration (PROVED + NUMERICAL).** If the condition is formulated on the full U_T (U_T prolates with λ_j ≥ ½, ∩ 𝒫_T), the
margin remains 1.5·10⁻³ (log 2), 4.2·10⁻³ (½log5), 6.9·10⁻⁴ (½log7) ≫ λ_A, and on the new components alone 2.8·10⁻²,
9.2·10⁻², 6.2·10⁻³: at every finite resolution η > 0 the sign stays in the complement. The only condition of the form "𝔞_T ≥ 0
on a prolate subspace" that implies λ_A ≥ 0 is the one with η → 1 and all of U_T: that is 𝔞_T ≥ 0 on 𝒫_T, row D per window.
**NO-GO**: X's quantitative converse is D rewritten (falls under W-loc: R186_044 Thm 2, and under Lemma T′). The structural reason is
R186_042: the negative set is a sub-Shannon sea (N_i = T|J_i|/π ≤ 1), so that E_η(U_T) at any fixed η does
not contain the cancellation directions, which are combinations of prolate tails of distinct components (R186_044 §2).

## 4. The arithmetic property

**4.1 Pointwise per component (NUMERICAL).** Mean of S_T and of σ_{T₀} over each component J_i of U₀⁺ (801 nodes):

| T₀ → T | component | ⟨S_T⟩_J | ⟨σ_{T₀}⟩_J | cancels (sign and magnitude)? |
|---|---|---|---|---|
| ½log3 → ½log5 | (0, 3.31) | −0.31 | −2.20 | no (S_T(0) = +1.96) |
| | (6.95, 10.53) | −0.43 | −0.41 | **yes** (6% excess) |
| ½log3 → ½log7 | (6.95, 10.53) | −0.42 | −0.41 | **yes** (4% excess) |
| log 2 → ½log7 | (4.82, 7.27) | −0.84 | −0.47 | yes (78% excess) |
| | (9.67, 11.97) / (16.25, 18.49) | −0.23 / −0.52 | −0.51 / −0.69 | no / no |
| | (27.6, 28.9) / (45.1, 46.1) | +0.17 / +0.11 | −0.27 / −0.15 | no / no (opposite sign) |
| ½log5 → ½log7 | 8 components | 3 yes, 5 no; at (108.5, 109.0): +0.82 vs −0.06 | | |

Cancellation "with exact sign and magnitude" occurs in ½log3's dominant component (center 8.74 ≈ 2π·2/log 2, where
prop:align makes it nearly forced: at τ = 9.06, cos(τ log 3) = −0.86, cos(τ log 4) = +0.99 ⇒ S_T = −0.40) and fails for most
of the others; the far components receive S_T of the opposite sign. Since λ_A(T) ≥ 0 holds (certified up to ½log5, Paper 46),
positivity **is not** achieved by local cancellation of σ_{T₀} in U₀: it is achieved by the global balance of §3 (leakage,
new components, coupling). Resolution dependence: with η = ½ the 1–5 inequalities (X_η) hold with margin
0.0006–0.13 (table §3), and with η = 0.1 there is no inequality: **X becomes less informative the finer the resolution** in
these windows, the opposite of what the T → ∞ asymptotic suggests.

**4.2 Weyl (PROVED elementary + NUMERICAL).** The centers of the components of U_{T₀} with 𝒩_{T₀} = {2,3} are at distance
< δ_2/log 2 from 2πk/log 2 (prop:align). For a new prime p, cos((2πk/log 2) log p) = cos(2πk·θ_p), θ_p = log p/log 2
irrational ⇒ equidistribution (Weyl) ⇒ mean over k ≤ 10⁵: −1·10⁻⁵ for p = 3, 5, 7. Consequence (PROVED): **no fixed new
prime has a definite sign on the centers of U_{T₀} as T₀ grows**; the cancellation X demands cannot come from
phase alignment of individual primes (confirms R186_023/"single-mode alignment" FALSIFIED), only from the aggregate
Σ_{2T₀<log n<2T} smoothed at scale π/T.

**4.3 A statement about Λ? (PROVED as an identification; honest).** The prolate average of σ_T at resolution π/T is, by
lem:roughEF (Paper 46, PROVED) applied to ψ ∈ 𝒫_T, 𝔞_T(ψ) = Σ_ρ Φ_ψ(ρ)Φ_ψ(1−ρ): the zero measure seen by |ψ̂|². So
(X_η) in arithmetic form says: "the sum of new primes smoothed by |ψ̂_j|² over U₀ reproduces m − (smoothed zero
measure)", and since U₀ at small T₀ lies in |τ| < γ₁ (up to tails), it is "the smoothed sum of primes = m in the gap (−γ₁, γ₁)
at resolution π/T" — exactly (N′)/R183_031 Thm 1 (gap density → 0 at rate πN₀/T). **It is not a new statement about
Λ: it is the explicit formula plus the location of the zeros, per packet.** Test M₁ (NUMERICAL, table): M₁ has the same
primes; its Λ_{M₁} adds the continuous density 4cos(γ₁u)cosh(δu). With the full Λ_{M₁}, (X_η) on E_½(U₀^{M₁}) ∩ 𝒫_T
holds with c_E = +0.084 (log 2), +0.071 (½log5) while λ_A(M₁) = −1.5·10⁻³, −5.0·10⁻³ (n₋ = 2): **window X at resolution
η = ½ does not distinguish M₁ from ζ**; with the atomic part alone (same primes) the indistinguishability is tautological. The ζ/M₁
difference is in W (plunge of U₀^{M₁} and the (9.7, 11.9) component), not in E_η. Verifiable for small primes: yes (§4.1); for all T:
only as a consequence of positivity, never as input (R183_031 prolate NO-GO; W-sieve).

## 5. Falsifier, inheritance and a lemma for all T

**5.1 Inheritance (PROVED, Lemma T′ of R186_045).** Every condition (R) of §3 implying λ_A(T) ≥ c′ > 0 is a continuous functional
of 𝔞_T|𝒫_T, so its margin is ≤ L·λ_A(T). Confirmed with a number: (X_η) alone has margin c_E = 0.03–0.13 (does not inherit) **and does not
imply**; the full (R) is the inertia of the Schur matrix, whose margin is exactly 1 − ρ_T (R186_044 Thm 2), which inherits.
Dichotomy: **either the condition is only on U₀ (own margin, does not imply) or it implies (and inherits)**. There is no third option within
the class "inequalities on S_T in prolate average."
**5.2 Explicit falsifier.** M₁(δ = 0.1) satisfies (X_½) at ½log3 → log 2 and ½log3 → ½log5 with λ_A < 0: any "converse"
using only (X_η) on U₀ is falsified by M₁ (family P/Q of R166_405: falls under W3/W-identification if the class is added).
**5.3 What remains as a lemma for all T (OPEN; precise statement).** *Tail lemma X_∞(T₀):* for fixed T₀, fixed η and T → ∞,
for every F ∈ E_η(U₀,T) ∩ 𝒫_T, ⟨S_T⟩_F ≤ ⟨σ_{T₀}⟩_F + ℓ_T(F), with ℓ_T(F) ≤ η·sup_{U₀^c}σ_T + o(1) **and** with the lower
bound of ℓ controlled: ∫_{U_T∖U₀}σ_T⁻ w_F ≤ ε(η, T₀) → 0. The first part is (N′) per packet (R183_031 Thm 1 gives it under bounded
inertia n₋ ≤ N₀, which is positivity itself); the second is new as a statement and is what §3 shows to be indispensable: **the
new negative mass created by Λ in (e^{2T₀}, e^{2T}) outside U₀, seen by the U₀ prolates, must be o(1)**. It is Ω's S2
(R186_032 §4) written with two terms: cancellation in U₀ (explicit formula) and non-creation of negativity outside (with no
analogue in the corpus; sieves give exponent ½, R166_802). Label: OPEN; not claimed to be input from (m, Λ).

## 6. Own verifications

- x-form vs τ-form (½log3, M = 16): max|A_x − A_τ| = 1.4·10⁻⁴ (|A| ≤ 2.35), as in r043 (1).
- λ_A: 1.03·10⁻⁷ (log 2; R186_045: 1.04·10⁻⁷), 3.65·10⁻¹² (½log5, M = 48; r034 M = 40: 3.86·10⁻¹²; variational bound, decreases with M);
 M₁(0.1) at log 2: −1.50·10⁻³, n₋ = 2 (R187/r043: −1.52·10⁻³, n₋ = 2).
- Negative sets: U⁺_{½log3} = (0, 3.305) ∪ (6.945, 10.531) (2 comp.), U⁺_{½log5}: 8 comp., |U⁺| = 13.752 (r034: 13.75,
 Shannon 7.04); U⁺_{log 2}: 6 comp. (R186_045: #comp = 6).
- Lemma 1.1's identity implemented as L := A − (M_{σ₀} − M_S) and verified via the minimizer's decomposition in E
 (⟨S⟩, ⟨σ₀⟩, leakage, 𝔞): in every row "X: … [holds]" with 𝔞_T(f) = c_E > 0.
- Closed-form bhat vs quadrature: 0.36206352 both. S_T(0) = v_3 + v_4 = 1.9617 = 2log3/√3 + 2log2/2 ✓; σ_{½log3}(0) = C_0 − v_2 =
 −6.352 ✓; σ_{½log3}(9.06) = −0.615, S_{½log5}(9.06) = −0.402 (by hand: −1.09 + 0.69 = −0.40 ✓).
- Landau–Widom: normalization taken from R186_042 (table), with c_i = T|J_i|/2 by copy; for c_i < 1 the log is clipped (order
 control only; not used in any proof).
- "New component" heuristic: J ⊂ U_T is "from U₀" if its center falls within some component of U₀ or its endpoints are
 < 30% away from those of a U₀ component; at ½log3 → ½log5 the assignment ([0,2]: U₀; [4.2,6.5]: new; [8.7,11.3]: U₀) is
 unambiguous; at log 2 → ½log5, none new (6 of 6 assigned, the last two of U_T, at 62 and 108, new but of mass 0).

## 7. Audit notes

- Nothing here touches the sign: Theorem X is Lemma 1.1 + λ_A ≥ 0; the converse's NO-GO is Prop. 3.1 (linear algebra) + numbers
 in six windows; the identification in §4.3 is lem:roughEF.
- Landau–Widom for unions of intervals remains CITED-NOT-VERIFIED (R186_112); it enters only in X(c) as an asymptotic count.
- λ_A(½log7) is neither resolved nor certified: no conclusion is drawn from its value, only from c_E, c_W, κ (O(1)).
- The sign correction to R186_045 §2.2(iii) does not change its content or label.
- No equivalence with other statements is used; "zeros" appears only via lem:roughEF (identity) and R183_031 (CITED).

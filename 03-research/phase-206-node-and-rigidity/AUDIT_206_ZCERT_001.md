# AUDIT_206_ZCERT_001 — Review of ZCERT_001 (zero-side certificate of the node)

Phase 206. Material: ZCERT_001.md and ZCERT_001_data/ (zcert.py, tstar.py, finegrid.py,
post.py, run.log, json), H1PLUS_001 (1.4), P47 main.tex (eq:Aform, lem:archcount, lem:combsine, cor:margin1,
cor:H1minus, rem:chiev-sine, rem:finitesign, bibitems), CALIB_R4_001, AUDIT_ZENODO_FRONTIER.
Own recomputation: `AUDIT_206_ZCERT_001_data/audit_repro.py` (+ `audit_repro.log`).

## Summary (≤250 words)

ZCERT_001 **passes** on the essentials, with four corrections. (1) The form Z_T = Σ_ρΦ_F(ρ)² is correct: for even F,
Φ_F(1−ρ) = Φ_F(ρ), so Φ(ρ)², Φ(ρ)Φ(1−ρ) always coincide; |Φ|² coincides on the line. The normalization (factor 2 for
±γ) is confirmed by the calibration 0.0018523932 vs 0.0018523954 (prime side). (2) The closed form of Φ_k and
c_k = Φ_k(1) are correct; z = ±ω_k is a removable singularity. (3) τ(T) is correct and conservative; recomputed by hand:
τ(2) = 3.50·10⁻³⁴, τ(4) = 2.62·10⁻³³ (they match). The counting of the quadruple is correct. (4) The Cholesky is in Arb
balls (not floats): a proof. I reproduced T = 2, 4, 4.2 with independent code (a different basis for c^⊥): same values, node
certified. (5) Continuum in T: OPEN (not ARGUED); the grid is PROVED. (6) **Major correction:** the "1e−70" of CALIB_R4
is NOT noise or an artifact: it is the true floor of W at ½log15 (Mori, certificate 2.40·10⁻⁷⁰, audited). The phrase in
ZCERT §4.4 "infimum 0 in infinite dimension" is FALSE at ½log15 and must be withdrawn. (7) **New result** obtained in this
audit: λ^W_ev(4) ≤ 1.46·10⁻³¹ (PROVED with CITED inputs), 14 decades better than cor:margin1 (≈2·10⁻¹⁷). Minor correction:
T* grows as ≈ 3·log H/25, not log H/25. Remark rem:zcert: acceptable with the changes of §8; the bibitem Trudgian2014 is missing.

## 1. The form Z_T

**Rederivation.** H1PLUS_001 (1.4): 𝔄_ev(F) = Z_T(F) − 2⟨F,χ_ev⟩², Z_T(F) := Σ_ρΦ_F(ρ)², Φ_F(ρ) = ∫_{−T}^{T}F(x)e^{(ρ−½)x}dx,
derived from lem:roughEF (explicit, with h = F∗F̃: Σ_ρ ĥ(ρ) with ĥ(ρ) = Φ_F(ρ)Φ_F(1−ρ) in the window-form
normalization; the poles give Φ_F(0)Φ_F(1) = 2⟨F,χ⟩²-type in the even sector). For even real F:

  Φ_F(1−ρ) = ∫F(x)e^{(½−ρ)x}dx = ∫F(−y)e^{(ρ−½)y}dy = Φ_F(ρ).

Hence Φ_F(ρ)Φ_F(1−ρ) = Φ_F(ρ)² **identically**, both on and off the line: there is no "Φ² vs Φ(ρ)Φ(1−ρ)" ambiguity in
the even sector. Also Φ_F(ρ̄) = conj(Φ_F(ρ)) (F real), so the sum over the quadruple {ρ, ρ̄, 1−ρ, 1−ρ̄} is
2Re Φ(ρ)² + 2Re Φ(ρ)²·… = real. The variant Σ|Φ_F(ρ)|² coincides on the line (Φ real) and **differs off it**: it is not
the form; ZCERT uses the correct one. For the bound τ this is irrelevant because ZCERT bounds |Φ(ρ)²| ≤ |Φ(ρ)|² term by term
(without exploiting cancellation). Label: **PROVED** (given (1.4), PROVED in H1PLUS_001/AUDIT_204).

**Constant.** ZCERT writes Z_on = 2Σ_{γ_n>0}Φ_F(γ_n)² (factor 2 for ρ, ρ̄; the zeros 1−ρ = ρ̄ on the line are not
counted again: correct, on the line 1−ρ = ρ̄). The numerical calibration is conclusive: T = ½log5, block {1,3},
F ⊥ c, K = 2000 gives 0.0018523932 versus 0.0018523954 from the prime side (AUDIT_206_001). The difference 2.2·10⁻⁹
is positive in the right direction (truncating at K only lowers) and of the order of the tail Σ_{γ>γ_K}Φ² ~ ω²/(Tγ_K³)·log γ_K.
A missing factor of 2 or 1/2π would give O(1) error. **PROVED-consistent / NUMERICAL for the constant**, more than enough:
the constant is that of P47 for 𝔄 (=𝔞_T of eq:Aform) on c^⊥, which is what the node needs. Editorial pending: P47
does not define "W^ev_T" under that name in def:W; the remark should talk about 𝔄_ev and Z_T, not W (see §8).

**On c^⊥.** c_k = ⟨χ_ev, e_k⟩ (rem:chiev-sine) and, for even F, ⟨F,χ_ev⟩ = ∫F cosh(x/2) = Φ_F(1) = Φ_F(0). Therefore
F ⊥ c ⟺ Φ_F(1) = 0 ⟺ 𝔄_ev(F) = Z_T(F). Correct.

## 2. Closed form Φ_k

Rederived: for k odd sin(ω_k(x+T)) = s_k cos(ω_k x), s_k = (−1)^{(k−1)/2}; ∫_{−T}^{T}cos(ωx)cos(zx)dx =
sin((ω−z)T)/(ω−z) + sin((ω+z)T)/(ω+z); with ωT = πk/2, sin(πk/2 ∓ zT) = s_k cos(zT). Sum: s_k cos(zT)·2ω/(ω²−z²).
With the basis factor s_k: s_k² = 1. And e^{(ρ−½)x} = e^{izx} with z = −i(ρ−½); since F is even only cos(zx) enters.
**Correct.**

- z → ±ω_k: cos(ω_kT) = cos(πk/2) = 0 (k odd): 0/0 removable; limit = T^{−1/2}·T (by L'Hôpital,
  −T sin(ω_kT)·2ω_k/(−2ω_k) → T·s_k·…, in modulus |Φ_k(±ω_k)| = T^{1/2}) — consistent with ‖e_k‖ = 1 and Cauchy–Schwarz
  (|Φ_k(γ)| ≤ ‖e_k‖·‖cos(γ·)‖ ≤ (T+…)^{1/2}). In the code, z = γ_n ≥ 14.13 and ω_max ≤ 15π/(2·0.75)… on the grid
  ω_max = πN/2T ≤ t₀ = 6.29 < γ_1: there is never division by (nearly) zero. In the 2N/4N blocks ω_max ≤ 4t₀ ≈ 25.2 > γ_1:
  possible proximity γ_n ≈ ω_k; with balls there is no risk of silent error (the ball would widen and the Cholesky
  would fail), so there is no false positive. **PROVED.**
- c_k = Φ_k(1): z = −i/2, cos(−iT/2) = cosh(T/2), ω²−z² = ω² + ¼: c_k = 2ω_k cosh(T/2)/(√T(ω_k²+¼)) = rem:chiev-sine.
  **Matches.**

## 3. Bound τ(T)

**Lemma Z.1.** ρ = β+iγ, z = γ − i(β−½). |cos(zT)| ≤ cosh(Im(z)T) = cosh((β−½)T) ≤ cosh(T/2) ≤ e^{T/2}. Correct.
|ω²−z²| ≥ |z|² − ω² = γ² + (β−½)² − ω² ≥ γ² − ω². ZCERT uses γ² − ¼ − ω_max², weaker: conservative (unnecessary,
harmless). The brief proposed ≥ γ²/2: ZCERT is better and valid. Cauchy–Schwarz in k: |Σx_k a_k|² ≤ ‖x‖²Σ|a_k|²; the basis
{e_k} is orthonormal, so ‖F‖ = ‖x‖ exactly (no normalization error). **PROVED.**

**Lemma Z.2.** Stieltjes: Σ_{γ>H}γ^{−4} = ∫_H^∞t^{−4}dN = [N t^{−4}]_H^∞ + 4∫N t^{−5} ≤ 4∫_H^∞N(t)t^{−5}dt (boundary
term −N(H)H^{−4} ≤ 0; N(t)t^{−4} → 0). With N(t) ≤ (t/2π)log t: (4/2π)∫log t·t^{−4} = (4/2π)(log H/(3H³) + 1/(9H³)).
Correct. **Validity of N(t) ≤ (t/2π)log t:** with any explicit Trudgian-type form,
N(t) ≤ (t/2π)log(t/2πe) + 7/8 + a log t + b log log t + c (a ≤ 0.112, b ≤ 0.278, c ≤ 3.4 in all published
versions; the Platt–Trudgian 2021 Math. Comp. version has 0.1038, 0.2573, 9.3675). The difference
(t/2π)log t − (t/2π)log(t/2πe) = (t/2π)log(2πe) ≈ 0.45t dominates by far for t ≥ 100. Note: ZCERT omits the 7/8 when
citing, without consequence. **Citation correction:** the constant 3.385 is not that of Trudgian 2014 (J. Number Theory 134,
280–292), which gives 0.112 log t + 0.278 log log t + 2.510; either works. Recommendation: cite Trudgian 2014 with
constant 2.510, or simply "N(t) ≤ (t/2π)log t for t ≥ 100, a consequence of [Trudgian 2014]." **PROVED + CITED.**

**Counting.** N(t) counts zeros with 0 < γ ≤ t with multiplicity, including both abscissas β and 1−β: it covers ρ and 1−ρ̄.
The factor 2 covers γ < 0 (ρ̄, 1−ρ). Each term bounded in modulus: nothing is undercounted. Zeros on the line with γ > H
or not listed: Φ_F(½+iγ) = ∫F cos(γx) ∈ ℝ ⇒ term ≥ 0, discarded. Correct (F even real). Multiple zeros on the
line: also ≥ 0. Height bounds H: Platt–Trudgian 2021 (Bull. LMS 53, 792–797): all zeros with 0 < γ ≤ 3·10¹² on the
line. Correct. Factor (H²/(H²−¼−ω_max²))²: bound of (γ²−¼−ω²)^{−2} ≤ γ^{−4}·(…)² for γ > H. Correct.

**Hand recomputation.**
- T = 2: N = 8, k ∈ {1,3,5,7}, Σ4ω_k² = 4(π/4)²·84 = 207.3; e²/2 = 3.695; S = 2·(4/2π)(28.73/(3·2.7·10³⁷) +
  1/(9·2.7·10³⁷)) = 4.57·10⁻³⁷. τ(2) = 3.695·207.3·4.57·10⁻³⁷ = **3.50·10⁻³⁴**. ZCERT: 3.5e−34. ✓
- T = 4: N = 16, Σk² (k odd ≤ 15) = 680, Σ4ω² = 4π²·680/64 = 419.5; e⁴/4 = 13.65; τ(4) = **2.62·10⁻³³**. ✓

**File discrepancy (minor).** `run.log` contains τ from the old version (N(t) ≤ t log t), 2π times larger;
`zcert.py` already has the 1/2π version; `post.py` recomputes `zcert_results.json`, `finegrid.json`, `tstar.json`. Table
§4.1 uses the new version. `edge.log` still has the old one (declared). No flag changes because of this except T = 4.21
(declared). OK, but `run.log` should be marked as "obsolete τ" in the data README.

## 4. Numerical rigor

- **Zeros.** `acb.zeta_zeros` (Arb; Johansson) returns isolated, certified balls for the first K zeros; the
  imaginary parts used are balls. That they are on the line is certified by the routine itself (Turing's method) and also by
  Platt–Trudgian. **CITED** (Johansson 2017 IEEE TC; bibitem Johansson2017 already exists in P47, l. 11448).
- **Matrix.** `build` assembles M_on in arb_mat (balls). Rigorous.
- **Trick L·ccᵀ.** If M + L ccᵀ − εI ≻ 0, for x ⊥ c: xᵀMx − ε‖x‖² = xᵀ(M + Lccᵀ − εI)x > 0. Correct (for every L > 0).
  Since c is in balls, ⊥ is with respect to the true c, contained in the ball: a successful Cholesky holds for every
  matrix in the ball, including the true one. Correct.
- **Cholesky.** `chol_ok` is a hand-written Cholesky over `arb`; `d > 0` in arb is True only if the entire ball is > 0.
  It is a **proof** (not floats). μ_num (mpmath) only chooses ε. ✓
- **Truncation in K.** Each term 2Φ_k(γ)Φ_l(γ) is a rank-1 matrix ⪰ 0: M_on(K) ⪯ M_on(K′) ⪯ full form of
  zeros on the line. ε is a rigorous lower bound. ✓
- **T on the grid.** `finegrid.py` accumulates T += 0.01 in float; arb(T) uses the exact binary value (e.g. 4.2399999…). The
  certificate is for that binary T, not the decimal one. Harmless but should be stated ("at points T_j = 0.75 + 0.01j
  rounded in double precision"), or recomputed with arb('4.24'). N(T) uses t₀ = 6.289836 in float; no grid point
  falls within 10⁻⁴ of a jump 2Tt₀/π ∈ ℤ except the design point 4.245 (2Tt₀/π = 16.9983), without ambiguity.
- **Independent reproduction** (`audit_repro.py`): different basis for c^⊥ (b_j = c_0e_j − c_je_0, exactly ⊥ c
  in balls), compression PᵀMP, ball Cholesky of PᵀMP − εPᵀP with ε = 0.99μ, 2000 Arb zeros at 900 bits:

| T | N | dim | μ (mpmath) | ε cert (balls) | τ | node |
|---|---|---|---|---|---|---|
| 2 | 8 | 3 | 1.7128357e−11 | 1.69571e−11 | 3.498e−34 | PROVED |
| 4 | 16 | 7 | 1.4342789e−31 | 1.41994e−31 | 2.616e−33 | PROVED |
| 4.2 | 16 | 7 | 2.7647147e−32 | 2.73707e−32 | 2.760e−33 | PROVED |

  Matches ZCERT (1.71284e−11, 1.43428e−31, 2.75341e−32 at K = 500 at 4.20; with K = 2000 it gives 2.7647e−32, slightly
  larger: monotonicity in K ✓). Margin ε/τ at T = 4.2: ≈ 10. **Theorem Z on the grid: PROVED** (given the CITED facts).

## 5. T* and the continuum

- **Non-monotonicity at 4.21.** The phenomenon reproduced by structure: Φ_k(γ) = T^{−1/2}cos(γT)·r_k(γ); when γ_1T
  (or some low γ_n) passes near π(j+½), the factor cos(γ_nT) cancels that zero's contribution to all modes at
  once and the form loses a dominant rank-one piece. γ_1·4.21 = 59.52 ≈ 18.95π: near 19π − 0.16, not a node; the
  more likely culprit is γ_2 = 21.022: 21.022·4.21 = 88.50 = 28.17π ≈ (28+½)π − 0.33π. Plausible; not an error.
  Label: NUMERICAL (explanation ARGUED).
- **Jump at k = 17.** Logical: the new mode has ω_17 ≈ t₀ (at the archimedean threshold, lem:archcount) and the
  restricted form gains a nearly degenerate direction; 4 decades is consistent with "≈ 4–5 decades per mode."
- **Continuum.** |∂_TΦ_k(γ)| contains −γ T^{−1/2}sin(γT)·2ω/(ω²−γ²) ~ 2ω_k/(√T γ), plus ∂_Tω_k. So
  |∂_T M_on(k,l)| ≲ Σ_γ 4ω_kω_l/(Tγ²) ·(1+…) = O(ω²(log γ_K)²/T): O(1)–O(10) on the scale of T ∈ [1,4]. With
  μ ~ 10⁻³², the grid step needed would be ≲ 10⁻³³: infeasible. The change in c is also O(1)·e^{T/2}. Also
  E_N(T) is not nested in T (the e_k depend on T), and extension by zero (lem:monoT) only transports negative
  vectors, not positivity. **There is no argument** for the continuum: the correct label is **OPEN**, not ARGUED (ZCERT
  §5 writes "ARGUED … OPEN as a continuum statement": unify as OPEN). The only viable idea on record: replacing a
  global Lipschitz bound with a Rayleigh argument using a fixed witness vector does not work (it gives an upper bound, not a
  lower one). It remains OPEN.
- **Usefulness.** prop:H and the finite reformulation (RFIN_TRACT) require every T; grid points close nothing. The
  value of the result is (a) quantitative: how far the block margin (μ_N) reaches, and (b) the new upper bound of §6.
  It is not a step toward a closure; ZCERT §6 says so honestly.
- **T* vs H.** τ ∝ e^{T}·log H/H³, log τ ≈ −3 log H + T + O(log T). With log μ_N ≈ −25T: T* ≈ (3 log H − …)/26, not
  log H/25. With H = 3·10¹²: 3·28.7/26 ≈ 3.3 plus the constant offset (log μ_N(0) ≈ +5, log τ ∼ +6 log): order
  4 ✓. Correct the formula in ZCERT §6 and in the index entry. With the superexponential decay, T* grows even more
  slowly than linearly in log H. The conclusion ("more height does not reach far") holds.

## 6. 1e−70 vs 1.7e−21 — major correction to ZCERT §4.4 — and the new upper bound

**The 1e−70 is not noise.** The brief suggests that 1e−70 < 10⁻⁴⁰ (CALIB_R4's precision) makes it noise. On review:
CALIB_R4_001 l. 38 literally says the Legendre blocks give 6e−23 and that "the true value is λ^W ≈ 5e−70";
that 5e−70 does **not** come from its 40-digit computation: it is Mori's datum (½log15), verified in
AUDIT_ZENODO_FRONTIER: λ_min even ≥ 2.3979·10⁻⁷⁰ certified in Arb at 1280 bits (CITED). Therefore:
- It is compatible with ZCERT: the 4N block gives 1.7·10⁻²¹ and CALIB_R4 (Legendre M = 30, 15 even modes) gives 6·10⁻²³; both are
  Galerkin upper bounds for the infimum in the full space, which is ~10⁻⁷⁰. Consistent order: more modes ⇒ smaller.
  (Note: Mori's infimum is of W on the full 𝒟, ZCERT's is of 𝔄_ev = Z_T on c^⊥; inf_{c^⊥}Z_T ≥ inf_𝒟 W^ev; the
  comparison direction is correct.)
- **ZCERT §4.4 contains an error:** "the full form on c^⊥ is positive but not uniformly so (infimum 0 in infinite
  dimension …); the floor of CALIB_R4 is a property of its truncation, not an intrinsic floor." At T = ½log15 the
  infimum is ≥ 2.4·10⁻⁷⁰ > 0 (Mori, CITED; holds for every T ≤ ½log15). What is correct: the blocks show no floor
  **in the range of dimensions computed** (≤ 9 at ½log15), which is compatible with a floor of 10⁻⁷⁰ reached at
  dimension ≈ 30 (ZCERT's own extrapolation, 2.4 decades/mode, gives exactly dim ≈ 30 for 1e−70, consistent
  with Mori's converged 832 modes). Withdraw "infimum 0"; replace with "no visible floor up to dim 9; the floor
  certified at ½log15 is 2.4·10⁻⁷⁰ (Mori)." The "≈ 5 decades per mode" decay is local in dimension and not extrapolable.
- The index needs no correction regarding CALIB_R4 (the 5e−70 cited there is correct); the proposed ZCERT
  entry does (remove "no floor").

**New upper bound (result of this audit).** ZCERT gives only lower bounds. For the numerical minimizing vector
x* (in c^⊥ ∩ E_N, exact in balls by construction with a basis ⊥ c), I bounded Z_T(F*) rigorously from above:
Z_on in balls (2000 zeros), tail on the line γ > γ_K by the expansion f(γ) = −(2/γ²)Σ_j S_{2j+1}γ^{−2j},
S_m = Σx_kω_k^m (convergent, ω_max < γ_K), bounded geometric remainder, Σ_{γ>γ_K}γ^{−4} by Lemma Z.2 with
N(t) ≤ (t/2π)log t, and Z_off ≤ τ‖x‖². Result (`audit_repro.log`):

| T | upper bound for Z_T(F*)/‖F*‖² | cor:margin1 (λ^W ≤ 4·10⁹Te^{−15.449T}) |
|---|---|---|
| 2 | 1.7130·10⁻¹¹ + τ | 8·10⁹·e^{−30.9} ≈ 3.0·10⁻⁴ |
| 4 | 1.4361·10⁻³¹ + 2.6·10⁻³³ ≤ **1.47·10⁻³¹** | 1.6·10¹⁰·e^{−61.8} ≈ 2·10⁻¹⁷ |
| 4.2 | 2.7687·10⁻³² + 2.8·10⁻³³ ≤ **3.05·10⁻³²** | ≈ 4·10⁻¹⁸ |

Since F* is even and F* ⊥ χ_ev, W^ev(F*) = Z_T(F*) (H1PLUS (1.4) and line 9: Z_T = W^ev_T) and therefore

  **λ^W(T) ≤ inf_{F even ⊥χ} Z_T(F)/‖F‖² ≤ 1.47·10⁻³¹ at T = 4 and ≤ 3.05·10⁻³² at T = 4.2**

(PROVED with CITED inputs: Arb zeros, Platt–Trudgian, Trudgian). Improves cor:margin1 by 14 decades at T = 4. Convention
warning: cor:margin1 bounds λ^W ≤ λ_P ≤ λ_A; the new bound is **only for λ^W** (and for the infimum of 𝔄_ev on
c^⊥), not for λ_A (the test F* is not primitive: it does not annihilate Φ'_F(±i/2)). The editor must verify that the
normalization of λ^W in def:W (‖F‖² vs ‖h‖, factor 2π) matches 𝔄 = 𝔞_T of eq:Aform; the ½log5 calibration confirms that of 𝔄.
It also quantifies the gap with the floor: at T = 4 the real floor of W is ≤ 1.5·10⁻³¹ and (by the decay in blocks 2N:
1.0·10⁻⁶⁰ as a Galerkin upper bound if certified likewise) probably ≪ 10⁻⁶⁰. The 2N/4N bounds would only be
certifiable from above if the tail K is controlled with the same expansion; not done here (optional ACTION).

**Decay rate vs cor:margin1.** No contradiction: cor:margin1 is an upper bound (for a test family), μ_N is a block
value ≥ λ^W. The slope 22→28 of log μ_N is larger than 15.449: cor:margin1's family is suboptimal, as its
own footnote admits. NUMERICAL for the functional form (−10.7T − 5.9T log T is a 6-point fit; do not extrapolate).
For (H_N): it only says that μ_N of the canonical block does not admit e^{−cT} with c ≤ 25 on [2,8] — evidence, not proof.

## 7. rem:zcert against P47

- eq:Aform: 𝔞_T is the full form (archimedean + Lévy − comb); 𝔄_ev its even restriction: correct to use 𝔄.
- lem:archcount: N(T) = ⌈2Tt₀/π⌉ − 1 with t₀ = 6.2898…; ZCERT uses 6.289836: consistent. lem:archcount declares t₀
  numerically; for the remark it suffices to define the block as "the odd sines k ≤ N(T)" — the convention only fixes which
  block is certified; it does not require an exact t₀ (any N gives a valid statement).
- cor:H1minus holds for T ≥ 0.12: "n₋ = 1" only for T ≥ 0.12 (all grid points satisfy this). ✓
- **Problems with the proposed remark:** (a) "n₋(𝔄_N(T)) = 1" requires that block E_N contain a negative direction;
  cor:H1minus gives n₋(𝔄_ev) ≥ 1 on all of 𝒟^ev, not on E_N. In the block, the negativity is seen with F = Σc_ke_k (projection
  of χ_ev) only if 𝔄(Pχ) < 0; rem:finitesign gives this NUMERICALLY (−1.81, −5.77, −23.8). Correct to write "n₋ ≤ 1" (PROVED);
  "= 1" would require certifying 𝔄_N(Pχ) < 0 in balls, which ZCERT does not do. **Correct to
  n₋ ≤ 1.** (b) "decays faster than e^{−cT} for any fixed c" is a 6-point fit: say "in the range tested
  (T ≤ 8) the local decay rate increases from 22 to 28." (c) "no lower floor appears when the block is enlarged" must be
  qualified per §6 (floor 2.4e−70 at ½log15 at dim ~30). (d) Missing \cite{Johansson2017} for Arb and \cite{Trudgian2014}
  (no bibitem exists; add: T. S. Trudgian, *An improved upper bound for the argument of the Riemann zeta-function on
  the critical line II*, J. Number Theory 134 (2014), 280–292). PlattTrudgian2021 exists and is correct (Bull. LMS 53
  (2021) 792–797). (e) Add the new upper bound for λ^W as a PROVED sentence (§6).

## 8. Verdict by item

| Item | Label |
|---|---|
| (1.4) read on c^⊥ ∩ 𝒟^ev, Z_T = Σ_ρΦ_F(ρ)², Φ_F(1−ρ) = Φ_F(ρ) | PROVED |
| Constant (factor 2 for ±γ) | PROVED-consistent; calibration NUMERICAL 1e−9 relative |
| Closed form Φ_k, removability, c_k = Φ_k(1) | PROVED |
| Lemma Z.1 | PROVED |
| Lemma Z.2 (N(t) ≤ (t/2π)log t) | PROVED + CITED (correct constant 3.385→2.510 or cite without a constant) |
| Zeros ≤ 3·10¹² on the line | CITED (PlattTrudgian2021) |
| Listed zeros | CITED (Arb, Johansson2017) |
| Ball Cholesky, trick L·ccᵀ | PROVED (code verified; reproduced) |
| Theorem Z (implication) | PROVED |
| Node n₋ ≤ 1 at grid points (binary) T ≤ 4.24, 4.245 | PROVED (given CITED facts); reproduced T = 2, 4, 4.2 |
| "= 1" on the block | NOT proved in ZCERT (use ≤ 1) |
| Continuum T ∈ (0, 4.2457) | OPEN |
| Superexponential rate | NUMERICAL (fit) |
| "Infimum 0 / no floor" (§4.4) | **WITHDRAW** (false at ½log15: floor 2.4e−70, Mori CITED) |
| T* ~ log H/25 | correct to ≈ 3 log H/26 |
| λ^W(4) ≤ 1.47·10⁻³¹, λ^W(4.2) ≤ 3.05·10⁻³² (new, this audit) | PROVED with CITED inputs |

**Index entry (replaces ZCERT §7's proposal):**

> **ZCERT (phase 206; audit AUDIT_206_ZCERT_001) — zero-side certificate of the node (REF-D, CITED input).**
> Closed Φ_k; 2000 Arb zeros + ball Cholesky + tail τ ≈ 10⁻³³ (H = 3·10¹²): n₋(𝔄_N) ≤ 1 PROVED on grid T ≤ 4.245;
> continuum OPEN; fails at N = 17. Byproduct: λ^W(4) ≤ 1.47·10⁻³¹ (vs 2·10⁻¹⁷ from cor:margin1). "No floor" withdrawn
> (Mori floor 2.4e−70 at ½log15). Do not retry "extending T* with more height": T* ≈ 3 log H/26, sublinear.

**Final version of the remark for the editor:**

```latex
\begin{remark}[zero-side certificate of the even block; computed with cited inputs]\label{rem:zcert}
For odd $k$ the Dirichlet sines of Lemma~\ref{lem:combsine} have the closed transform
$\Phi_k(\rho)=\int_{-T}^{T}e_k(x)e^{(\rho-\frac12)x}dx=T^{-1/2}\cos(zT)\,\frac{2\omega_k}{\omega_k^2-z^2}$,
$z=-i(\rho-\tfrac12)$, so $c_k=\Phi_k(1)$ (Remark~\ref{rem:chiev-sine}). For even real $F$,
$\Phi_F(1-\rho)=\Phi_F(\rho)$, and on $\{F\ \mathrm{even}:\langle F,\chi_{\mathrm{ev}}\rangle=0\}$ the even form
equals $\sum_\rho\Phi_F(\rho)^2$ (Lemma~\ref{lem:roughEF}). Zeros on the critical line contribute
nonnegatively; zeros off the line have $|\gamma|>3\cdot10^{12}$ \cite{PlattTrudgian2021} and, by the closed
form and $N(t)\le\frac t{2\pi}\log t$ \cite{Trudgian2014}, contribute at most $\tau(T)\|F\|^2$ with
$\tau(T)\le3\cdot10^{-33}$ for $T\le4.25$. With the first $2000$ zeros in ball arithmetic \cite{Johansson2017}
and a ball Cholesky factorisation, the form is bounded below on $E_N^{\mathrm{ev}}(T)\cap c^\perp$
($N=\lceil2Tt_0/\pi\rceil-1$) by $\varepsilon(T)>\tau(T)$ at the grid points $T=0.75,0.76,\dots,4.24$ and
$T=4.245$; hence $n_-(\mathfrak A_N(T))\le1$ there. Bounding the same sum from above at the numerical minimiser
gives $\lambda^W(4)\le1.5\cdot10^{-31}$, far below Corollary~\ref{cor:margin1}. In the range tested the
certified block minimum decays at a local rate increasing from $22$ to $28$ per unit of $T$; at
$T=\frac12\log15$ it is still $10^{-21}$ on the first $10$ odd sines, against the certified bottom $\approx2.4\cdot10^{-70}$
of the full form. Nothing is claimed between grid points. This is a verification with cited inputs, not a
mechanism.
\end{remark}
```
(Bibitem to add: `\bibitem{Trudgian2014} T.~S.~Trudgian, \emph{An improved upper bound for the argument of the
Riemann zeta-function on the critical line II}, J.~Number Theory \textbf{134} (2014), 280--292.` The editor must
verify the "certified bottom" citation against item L104/Mori already CITED in P47 and the normalization of λ^W in def:W.)

## 9. Audit reproducibility

`AUDIT_206_ZCERT_001_data/audit_repro.py` (`python3 audit_repro.py 2 4 4.2`, ≈ 65 s), output `audit_repro.log`.
Independent of zcert.py except for the closed formula (rederived in §2). Dependencies: python-flint, mpmath.

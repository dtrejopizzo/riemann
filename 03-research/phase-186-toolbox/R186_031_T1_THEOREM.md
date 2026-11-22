# R186.031 — Theorem T₁: positivity on 𝒫_T for T ∈ [½log2, T₁] by the semilocal mechanism (norm route)

Front: reserve (b) of R186_029, promoted by R186_107 §Front 2.
Frame: S = {∞,2}, level λ = 1, T ∈ [½log2, ½log3) (contacts N_T = {2}, so E_S = 𝔞_T on 𝒫_T; Paper 46 eq:form,
note N4). Starting identity (D3 at λ = 1, R186_017/099 PROVED; (84)_S, R186_014 PROVED given CC Thm 4.7 CITED):
 𝔞_T(h) = Son_S(h) − C_S(h), Son_S(h) = ‖Π_S ϑ(g_h)‖²_HS ≥ 0, C_S(h) = ∫_ℝ c_h(a) ε_S(e^{|a|}) da, c_h(a) = ∫h(y)h(y+a)dy.
Standalone script: `r031_t1_norms.py` (Galerkin from r183_030 with embedded ε grids; reproduces the tables of §5).

## Status

| # | Statement | Label |
|---|---|---|
| N | **Lemma N.** λ_A(T) ≥ λ_min(Son_S\|𝒫_T) − λ_max(C_S\|𝒫_T)⁺ for T ∈ [½log2, ½log3); in particular, if C_S ≤ 0 on 𝒫_T then 𝔞_T ≥ Son_S ≥ 0 (regime η = 0, CC mechanism) | PROVED (given (84)_S at λ=1, CITED CC 4.7) |
| ½ | **Lemma ½.** For T < a < 2T and every h ∈ L²(I_T): \|c_h(a)\| ≤ ½‖h‖²; the constant ½ is optimal even on 𝒫_T | PROVED |
| D | **Corollary D (direct route).** For ½log2 < T < log2: λ_A(T) ≥ λ_A^∞(T) − v₂/2 = λ_A^∞(T) − 0.49013, with λ_A^∞ = primitive archimedean background | PROVED |
| Dom | The semilocal route "E_∞ − \|ΔC\| − \|ΔSon\|" of R186_029 (b) is **dominated** by D: ΔSon − ΔC = −v₂c_h(log2) identically | PROVED (one line) |
| B | The boundary bound (B_T) of R186_029: \|c_h(a)\| ≤ B_T‖h‖²(2T−\|a\|)^{1/2} ∀h ∈ 𝒫_T — **FALSE** | PROVED (counterexample §4) |
| B′ | Form-norm version: \|c_h(2T−δ)\| ≤ C(𝔞_T^∞(h) + K‖h‖²)/log(1/δ) | ARGUED; useless (range δ_T ≲ e^{−v₂CK/λ_A^∞}) |
| T₁ | Values: T₁^N (Lemma N, Galerkin inputs) = **0.481–0.483**; T₁^D (Cor. D, Galerkin input λ_A^∞) = **0.367**; regime η = 0: T₀ ∈ [½log2, 0.37] **undecidable** (sign of λ_max(C_S) depends on the ε grid) | NUMERICAL (M = 24/32, two grids) |
| Y | Young bound ‖C_S‖ ≤ ‖ε_S(e^{\|·\|})‖_{L¹(−2T,2T)} = 2.84 (½log2) … 3.97 (½log3) against λ_min(Son_S) ≤ 0.257: the norm route **without** numerics on ε_S gives T₁ < ½log2 | NUMERICAL (L¹ of the grid) + PROVED (trivial) |
| V | **Verdict: NO-GO as a route.** No input has an analytic source beyond ½log2 (λ_min(Son_S), λ_max(C_S), λ_A^∞(T)); T₁ < ½log3 (thm:C) < log2 (Paper 42, certified Feshbach); the margin N(T) ≤ λ_A(T) inherits the collapse of R186_021 | NO-GO (route); tools N, ½, D, B kept |

**No contact with the sign.** Everything proved consists of inequalities between quantities whose positivity is
already certified in the range (Paper 42 up to log 2; thm:C at ½log3); the only non-numerical contribution is
negative (B false; Dom; Y).

## 1. Lemma N (PROVED)

Son_S(h) = Tr ϑ(g)^*Π_Sϑ(g) ≥ 0 is the form of a positive operator (R186_009/014). For h ∈ 𝒫_T unit norm,
𝔞_T(h) = Son_S(h) − C_S(h) ≥ λ_min(Son_S|𝒫_T) − λ_max(C_S|𝒫_T); if λ_max ≤ 0, use 0. C_S|𝒫_T is compact self-adjoint
(−C_{ε_S} HS, R186_012/014), so λ_max exists. ∎ It is the CC mechanism (N_I = −c(1−K_I), R186_101 §d2): at ½log2 the
direction ζ with K_I > 1 dies under the restriction and C_∞ ≤ 0 on 𝒫_{½log2} (CITED CC Thm 1 + R186_101 NUMERICAL).

## 2. Lemma ½ and Corollary D (PROVED)

For a ∈ (T, 2T): c_h(a) = ∫_{J₁}h(y)h(y+a)dy with J₁ = [−T, T−a], y+a ∈ J₂ = [a−T, T]; J₁ ∩ J₂ = ∅ because a > T.
Cauchy–Schwarz and the arithmetic mean: |c_h(a)| ≤ ‖h1_{J₁}‖‖h1_{J₂}‖ ≤ ½(‖h1_{J₁}‖² + ‖h1_{J₂}‖²) ≤ ½‖h‖². Optimal: h_δ of §4.
Cor. D: 𝔞_T = E_∞ − v₂c_h(log2) with v₂ = 2log2/√2 = 0.98026 and log2 ∈ (T, 2T) for ½log2 < T < log2. ∎
Numerics (§5): sup_{𝒫_T}|c_h(log2)|/‖h‖² = 0.377 (0.35), 0.459 (0.36), 0.491 (0.38), 0.500 (≥ 0.45): the constant ½
saturates on 𝒫_T almost immediately; the extremal (mass at the edges ±T) is not the minimizer of 𝔞_T, hence the loss
(at 0.36: bound 0.020 against λ_A = 0.482).

## 3. Domination (PROVED) and vacuity of (b)

E_S = E_∞ + (Son_S − Son_∞) − (C_S − C_∞) and E_S = E_∞ − v₂c_h(log2) (the comb is exact, C′ of R186_008) ⟹
ΔSon − ΔC = −v₂c_h(log2). So every bound "E_∞ − |ΔC| − |ΔSon|" is ≤ E_∞ − v₂|c_h(log2)|: the semilocal decomposition
contributes nothing to a norm bound unless λ_min(Son_S) is bounded from below **without going through Son_∞** — and
the record has no such bound (R186_029 (c): OPEN, external question). Moreover, the form of (b) in R186_029 is
vacuous at the endpoint: ‖κ_S(e^{|·|})‖_{L¹(−log2,log2)} = 0.61 (RS grid; the peak β₁log⁺ at log2 alone contributes
≈ 0.4) > λ_A^∞(½log2) = 0.549 — the falsifier "‖κ_S‖_{L¹} > 0.5" of 029/107 triggers at T = ½log2, not at 0.36.

## 4. The boundary bound (B_T) is false (PROVED)

h_δ := (2δ)^{−1/2}(1_{[−T,−T+δ]} + 1_{[T−δ,T]}), ‖h_δ‖ = 1, in the form domain (log test: ∫log(2+|τ|)|ĥ|² < ∞).
For a = 2T − θδ, θ ∈ (0,1]: c_{h_δ}(a) = (2δ)^{−1}·|[−T,−T+δ] ∩ [−T+θδ−δ, −T+θδ]| = θ/2. Tate moments
A(h_δ), B(h_δ) = O(δ^{1/2}); the projection onto 𝒫_T (Gram matrix of {e^{±t/2}} on I_T nondegenerate) corrects h_δ by
O(δ^{1/2}) in L² and c_h by O(δ^{1/2}). So sup_{h∈𝒫_T,‖h‖=1}|c_h(2T−θδ)| ≥ θ/2 − O(δ^{1/2}), while
(2T−a)^{1/2} = (θδ)^{1/2} → 0: no finite B_T. ∎ What is true is the form of 𝔞_T^∞(h_δ) ≈ Lev(c_{h_δ}) ≍ log(1/δ) → ∞
(thm:A), so version B′ (1/log(1/δ) in the form norm) is the correct form — but the range it produces, with
K ≍ C_m + 2κ_T ≈ 11 (R183_023 Prop 3.0), is δ_T ≲ exp(−v₂CK/λ_A^∞) ≈ e^{−20C}: no value. The finiteness of ∫c_hκ_S
never needed a boundary term (log⁺ ∈ L¹): the obstacle of the route was not (B_T), it was the absence of an
analytic source for the inputs.

## 5. Decisive numerics (NUMERICAL; M = 24, RS grid; M = 32 and grid S differ ≤ 4e-3 throughout)

| T | λ_A | λ_A^∞ | λ_min(Son_S) | λ_max(C_S) | N = λ_min − λ_max | D = λ_A^∞ − v₂/2 | ρ* | ‖ε_S‖_{L¹} |
|---|---|---|---|---|---|---|---|---|
| ½log2 | 0.5486 | 0.5486 | 0.2569 | +0.0029 (S: −0.0013) | 0.254 | +0.0585 | 0.001 | 2.84 |
| 0.36 | 0.4825 | 0.5105 | 0.2303 | +0.0130 (S: −0.0009) | 0.217 | +0.0204 | 0.009 | 3.07 |
| 0.37 | 0.4148 | 0.4830 | 0.2071 | +0.0164 (S: +0.0014) | 0.191 | −0.0071 | 0.017 | 3.20 |
| 0.40 | 0.2289 | 0.4046 | 0.1389 | +0.0222 | 0.117 | −0.086 | 0.055 | 3.52 |
| 0.45 | 0.0678 | 0.2860 | 0.0635 | +0.0287 | 0.035 | −0.204 | 0.245 | 3.78 |
| 0.48 | 0.0270 | 0.2209 | 0.0398 | +0.0370 | +0.0028 | −0.269 | 0.465 | 3.86 |
| 0.485 | 0.0225 | 0.2104 | 0.0368 | +0.0404 | −0.0035 | −0.280 | 0.508 | 3.86 |
| ½log3 | 0.0010 | 0.0845 | 0.0147 | +0.0833 | −0.069 | −0.406 | 0.944 | 3.97 |

Readings. (i) T₁^N ≈ 0.481 (RS) / 0.483 (S): crossing of λ_max(C_S) (grows 0.003 → 0.083 from the log peak at a = log2
entering the support) with λ_min(Son_S) (archimedean collapse 0.257 → 0.0147, R186_021). (ii) T₁^D ≈ 0.367.
(iii) η = 0: λ_max(C_S) changes sign with the grid up to T ≈ 0.365 (RS: +0.003…+0.015; S: −0.001…0) — consistent
with R186_102 m3; T₀ undecidable, possibly T₀ = ½log2. (iv) Fraction certified by N: N/λ_A = 0.46 (½log2), 0.51
(0.40–0.45), 0.10 (0.48), < 0 afterward: N(T) ≤ λ_A(T) always (Lemma N) and the loss worsens exactly where ρ* ↑ 1.
(v) Young: 2.84 ≫ 0.257 throughout T.

## 6. Honesty (questions 3–4)

1. **Is T₁ > ½log2 from operator inequalities?** No. The only analytic fact is Son_S ≥ 0 (regime η = 0), and
 C_S ≤ 0 on 𝒫_T is neither provable nor numerically stable beyond ½log2 (λ_max(C_S) ≈ +0.003 already at ½log2 with
 the refined grid). With pure norms (Young, L¹ of ε_S): T₁ < ½log2 (Y). With Galerkin λ_max(C_S) and λ_min(Son_S):
 T₁^N ≈ 0.48; but those two numbers cost the same as computing λ_A directly and have no analytic version
 (λ_min(Son_S): OPEN, R186_029 (c)).
2. **Does it inherit thm:margin / ρ* → 1?** Yes: N(T) ≤ λ_A(T) and N crosses zero via the same collapse of
 λ_min(Son_S) that drives ρ* to 1 (R186_021); T₁^N = 0.48 is the T where ρ* ≈ 0.47, not a structural threshold.
3. **What does it add beyond thm:C (½log3) and Paper 42 (log 2)?** Nothing in range: T₁^N < ½log3 < log2. In
 method: a proof "by mechanism" would only exist in regime η = 0, which is exactly CC at ½log2 and does not extend.
4. **"CONDITIONAL" boundary bound of 029/107:** withdraw it — it is false (B) and, even if true, irrelevant (Dom, §3).

**NO-GO as a route** (class: operator-norm bounds in the Son_S − C_S decomposition; reason: Dom + Y + absence of an
analytic source for λ_min(Son_S)). Kept as tools: Lemma N, Lemma ½ (optimal), Corollary D, falsification of (B_T).

## Audit notes

1. Lemma N uses (84)_S at λ = 1 via CC 4.7 (CITED) and D3; without it it still holds with 𝔞_T replaced by
 Tr ϑ(f)Π_S − comb₂ − ∫fε_S.
2. Lemma ½: check J₁ ∩ J₂ = ∅ ⟺ a > T; for a ≤ T only |c_h| ≤ ‖h‖² holds. In our range log2 > T always.
3. §4: the Tate correction is O(δ^{1/2}) because A(h_δ) = (2δ)^{−1/2}·O(δ); check that it does not alter c_h at
 2T − θδ by more than O(δ^{1/2}).
4. §5: λ_max(C_S) near ½log2 is of the order of the grid error (R186_101 MAJOR-1): only "sign undecidable" is claimed.
5. No new sign claim.

## For Paper 46 (not integrated; decision taken)

As an observation after prop:negtrace: "the semilocal decomposition does not improve the direct bound
λ_A ≥ λ_A^∞ − v₂/2 (identity ΔSon − ΔC = −v₂c_h(log2)); |c_h(a)| ≤ ½‖h‖² for a ∈ (T,2T) is optimal on 𝒫_T." Nothing
more.

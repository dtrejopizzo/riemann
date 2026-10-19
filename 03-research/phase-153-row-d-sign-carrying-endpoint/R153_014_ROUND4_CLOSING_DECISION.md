# R153.014 — Closing decision, round 4 of phase 153: the decay law of the sign in the certified window


## 1. Verdicts of record

| item | statement | label |
|---|---|---|
| `λ(T) = λ_min(A_T|P_T)` on `[0.30, log 2]` | decreases from `6.9·10⁻¹` (0.30) to `≈ 9.9·10⁻⁸` (log 2); minimiser **even** at every `T`; kinks at `½log2`, `½log3`; **one safe digit** in `λ` at the right end (K = 480 Richardson `9.87·10⁻⁸` vs `9.92·10⁻⁸`), 3 digits in `c(T)` | `DIAGNOSTIC-NUMERIC` |
| rate `c(T) = −d log λ/dT` | rises from `≈ 5` to `≈ 76` at `log 2`, peak `≈ 93` near `T = 0.689` | `DIAGNOSTIC-NUMERIC` |
| (P-Slepian) `c → 2γ_1 ≈ 28` | **REFUTED**: predicts 27.6 at `log 2` vs 75.8 measured, wrong monotonicity. The minimiser does not hide in the origin gap. | `REFUTED` (review's prediction) |
| zero profile of the minimiser | `Σ_γ|F̂(½+iγ)|²/⟨A_T F,F⟩ = 0.997` over 600 zeros (explicit formula verified two ways). Shares at `γ_1…γ_7`: `5.7·10⁻⁷, 1.4·10⁻⁵, 1.0·10⁻⁴, 2.5·10⁻³, 7.7·10⁻³, 2.7·10⁻², 1.15·10⁻¹` (peak at `γ_7 = 40.9`); median mass height 65. "Annihilates the first ~20 zeros" | `DIAGNOSTIC-NUMERIC`; "~20" `WITHDRAWN` |
| **Mechanism of the profile (new, audit)** | `F̂` has exponential type `T`; its Nyquist degrees of freedom `(T/π)H` exceed the zero count `N(H)` exactly up to `H⋆ = 2πe^{2T+1}` (66 at `log 2`, 48 at 0.60, 25 at 0.45), matching the measured mass medians (65, 57, 42). The minimiser clears the zeros up to height `≍ e^{2T}` and leaks just above. `Ω_eff ≍ 2πe^{2T+1}`, not `c/2`. | `DIAGNOSTIC` (heuristic with data); to be proved as an inequality |
| **Theorem 4.1** second-order expansion | `A_T^{(a)} = 2A_T + a²D_T + O(a⁴)` as operators on `L²(−T,T)`, `D_T = ad_t²(A_T)` = multiplier `+g_T''(τ)`: primes enter with the **same** sign as in `A_T` times `(log n)²`, archimedean `g_Γ''`; no polar term (`ad_t²` kills constants). Remainder uniform in operator norm (`‖R‖/a⁴ = 0.131`, verified). Construction's `−g''`/"reversed sign" | `PROVED` (operator identity); sign text `REPAIRED`; the `O(a²)` motion of the constraint space `P_T^{(a)}` is the unproved step for the constrained minimum: `OPEN` |
| `c ≈ 75` from the `T*(a)` slope | mechanism **CONFIRMED**: `2μ(T*) + a²q_D(T*) = 0` with `μ(T) = λ_min(A_T|P_T^{(2)})` (codimension-4 limit of `P_T^{(a)}`), `q_D < 0`; matched-window check `c_μ = 86.6` → slope 0.0239 vs 0.0241 measured (1%). The constant: `c_μ` runs 56 → 100 on `[0.69, 0.81]`, `T*(a)` is curved; "75" is a chord. `μ/λ ≈ 5·10³` at 0.69. | `DIAGNOSTIC-NUMERIC`; "confirmed 75" `DOWNGRADE` to "mechanism confirmed, constant is a chord" |
| rate formula | `dλ/dT = −(1/T)(2π)⁻¹∫τ g_T'(τ)|F̂|²dτ + Tate drift`; at `log 2`: Gamma shape `−1.447`, transport `n=2` `+1.876`, transport `n=3` `−0.429`, Tate drift `4·10⁻⁹`; **sum `−8.08·10⁻⁶ = −c·λ`** (negative, correct; the review's sign query was a misreading). HF vs finite differences agree to 3–4 digits (same Galerkin matrix). | `PROVED` on the Galerkin level / `DIAGNOSTIC-NUMERIC` values |
| **Main finding of the round** | the decay rate of the sign is a **cancellation over 5–6 orders of magnitude between O(1) archimedean and prime transport terms**; the residual equals the leak of the minimiser onto zeros above `≍ e^{2T}`. No term-by-term bound on `c(T)` is possible (observed, consistent with D.133). | `DIAGNOSTIC` (observed, not proved as impossibility) |
| boundary behaviour of `F_T` | `F_T(±T) ≠ 0`: jump `≈ −0.019` (1.1% of `F(0)`) at `T = 0.60`, K-stable to 480; fitted exponent `α = 1.25` is outside the boundary layer; D.133's rank-two endpoint term at the minimiser is `−9.8·10⁻⁷ ≈ 9λ` at `log 2` — **not** negligible. Construction's "endpoint term vanishes at the minimiser" | `WITHDRAWN`; D.133's obstruction stands in full |
| Tate constraints | near-inactive: `λ` equals the second unconstrained even eigenvalue to 8 digits | `DIAGNOSTIC-NUMERIC` (new) |
| `c(T) ≤ c_0` uniformly | is RH with a modulus; by Doc 143 §4.4 zero-computable, and its localized analogue is equivalent to LP-143 (conjecturally false). Nothing in this round is a prime-computable bound. | `RESTATEMENT` |

FATAL rule: clean (zeros used only diagnostically; PROVED items use none). No sign claimed for `ζ` beyond `T ≤ log 2`.

## 2. What round 4 established

1. The sign in the certified window decays like `e^{−∫c}` with `c(T)` climbing to `≈ 76` at `log 2`, and this decay is not an archimedean concentration phenomenon (Slepian refuted); it is the leak of a minimiser that has spent its `(T/π)H` degrees of freedom clearing the zeros up to height `≍ e^{2T}` — the same scale at which the primes enter the operator. This is the classical support/height duality of the explicit formula seen from inside the operator; it is the sharpest quantitative picture of "the sign" the corpus has.
2. The rate is a cancellation of O(1) terms to relative precision `e^{−cT}`; therefore no induction in `T` can be run term by term, with or without sign (D.133 now with a number).
3. Theorem 4.1 gives the exact second-order structure of the falsifier family around `ζ`; the `T*(a)` law of round 2 is explained mechanically (codimension-4 minimum `μ`), constant not universal.
4. Two corrections to the record: the endpoint term does not vanish at the minimiser; the construction's "~20 zeros" was wrong (peak at `γ_7`).

## 3. Repairs (from R153_013, nine items) — the substantive ones are recorded in §1; to be written into R153_012 at the next pass. Corpus-check for "Slepian" was under-reported (≥ 18 files incl. `phase-106/106_24` PSWF endpoint): add the references.

## 4. Open items added

| id | statement | label |
|---|---|---|
| (P153.11) | prove the clearing inequality: for `F ∈ P_T`, `Σ_{γ ≤ H}|F̂(½+iγ)|²` cannot be small for `H ≫ 2πe^{2T+1}` (a Nyquist/Ingham statement with the zero-count; expected to be a RESTATEMENT of Ingham–Beurling sampling; check Doc 143 §2.2) | `OPEN` |
| (P153.12) | the `O(a²)` motion of `P_T^{(a)}` and the constrained second-order expansion | `OPEN` |
| (P153.13) | is `λ(T)` asymptotically `e^{−κ e^{2T}}`-type (double exponential, if the leak height scales like `e^{2T}` and the leak like a Slepian at that height) or `e^{−cT}`? Only for `T` beyond `log 2` — not computable in the certified window; diagnostic only if pursued | `OPEN`, low |

## 5. Decision

Round 4 closed. Phase 153 remains closed; row D label unchanged. The round's honest yield is a quantitative map of the sign's decay and a proved second-order theorem, plus the firm negative: the bridge cannot be term-by-term.

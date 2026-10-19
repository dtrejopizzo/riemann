# R155.055 — Round 8d : the margin decays — an explicit unconditional upper bound on `λ^A(T)`

*Round 8d of phase 155 (item P9 of `R155_056`). Script `scripts/r8d/r8d_margin_bound.py`
(9 s, README in `scripts/r8d/`). Labels: PROVED / DIAGNOSTIC / HEURISTIC / OPEN. Pure mathematics; the script
checks constants only.*

**Notation (Paper 47 §1, kept exactly).** `I_T = (−T,T)`, `F̂(τ) = ∫F e^{iτt}`, `c_F` the autocorrelation,
`m(τ) = Re ψ(¼+iτ/2) − log π`, `σ_T = m − Σ_{n∈N_T} v_n cos(τ log n)`, `v_n = 2Λ(n)/√n`, `N_T = {n ≥ 2 : log n < 2T}`,
`𝔞_T(F) = (1/2π)∫σ_T|F̂|²`, `A(F) = ∫F e^{t/2}`, `B(F) = ∫F e^{−t/2}`, `P_T = {A = B = 0}`,
`W_T(F) = 𝔞_T(F) + 2Re(A B̄)`, `Φ_F(s) = ∫F(t)e^{(s−½)t}dt`. Paper 47 writes **`λ^A(T)`** for the bottom of `𝔞_T` on
the unit sphere of `P_T` (the quantity the orders call `λ^P(T)`), `λ^P ≤ λ^A` for the bottom over the larger class
`𝒦_prim` (`thm:A`), and `λ^W ≤ λ^P` for the complete form on `L²(I_T)` (`rem:Kprim`). **Every upper bound below is
proved for `λ^A` by an explicit `F ∈ P_T` and therefore holds for all three: `λ^W(T) ≤ λ^P(T) ≤ λ^A(T) ≤ 𝔞_T(F)/‖F‖²`.**

## 0. Corpus check (done before building)

`grep -rn "λ^P(T) → 0\|lambda.*to 0\|margin.*decay\|Landau–Widom\|Landau-Widom" 03-research/phase-15-arithmetic-hodge-index* 04-papers/47*`:

* **No prior file proves `λ(T) → 0` or any explicit upper bound tending to `0`.** `R153_012` (round 4 of phase 153)
 is a DIAGNOSTIC Galerkin *measurement* of `λ(T)` on `[0.30, log 2]` with the log-derivative `c(T) = −d log λ/dT`
 sweeping `5 → 93`; no proof, no `T > log 2`.
* `R155_053` Prop. 4.1 (PROVED): `RH ⟺ lim_{T→∞} λ^W_T ≥ 0`; **`λ^W ↓ 0` is there labelled HEURISTIC (Zhu's law).**
 Theorem 1 below upgrades that HEURISTIC to PROVED, with a rate, and adds the unconditional `limsup ≤ 0`.
 `R155_053` Prop. 4.3 (`limsup λ^A ≤ C₀ − A_S` for *finitely supported* combs) is a different object (a fake comb).
* Paper 47 `cor:mono`: `λ^P` nonincreasing at fixed contact set; upper bound `C₀ + A_T + φ((3π/2T)²)`, positive
 (`1.291`, `2.327`) and growing like `4e^T` — useless for decay. `main.tex:2735` (Zhu's Landau–Widom conjecture
 `−log λ ≍ e^{2T}`), `§9.3` item 4 (non-induction in `T`), `rem:galerkin` (no value at `log 2`). `R155_047`,
 `00-references/PROLATE-REFERENCES.md`: Landau–Widom only as a cited asymptotic, never used in a proof.
* Paper 45 Thm 9.4 (explicit formula, `PROVED` there for real `F ∈ C_c^∞`), Thm 10.4 (sufficiency of primitive
 tests; if RH fails some compactly supported primitive `F` has negative Weil form). Paper 46 import (X19).

## 1. Imports (all labelled; nothing about zeros is asserted otherwise)

* **(X19)** [Paper 46 §12 table; Rosser–Yohe–Schoenfeld 1968; Platt–Trudgian 2021]: `ρ₁ = ½ + iγ₁`,
 `γ₁ = 14.134725141734…`, is a simple zero on the line; `ξ` has no zero `ρ ≠ ρ₁, ρ̄₁` with `|Im ρ| ≤ 21`. Only
 `γ₁ ∈ [14.13, 14.14]` and the gap `(γ₁, 21]` are used from this clause.
* **(X19′)** [same source, D. J. Platt and T. S. Trudgian, *The Riemann hypothesis is true up to `3·10¹²`*, Bull.
 LMS 53 (2021), 792–797; **a clause Paper 46 did not import, recorded here as a separate import of record**]:
 every zero with `|Im ρ| ≤ H₀ := 3·10¹²` lies on the critical line. Used in step (4) of Theorem 1 only; it
 affects the bound by a factor `1 + 10^{−70}` (the `e^{T}` price of an off-line zero starts at height `H₀`).
* **(X-N)** [J. B. Rosser, *Explicit bounds for some functions of prime numbers*, Amer. J. Math. 63 (1941),
 Thm 19; **new to the corpus, to be entered in the phase import ledger**]: for `t ≥ 2`,
 `|N(t) − (t/2π)log(t/2πe) − 7/8| ≤ 0.137 log t + 0.443 log log t + 1.588`, `N(t)` counting zeros `0 < γ ≤ t` with
 multiplicity. (Alternative with the same consequence: T. S. Trudgian, *J. Number Theory* 134 (2014), Thm 1:
 `0.112 log t + 0.278 log log t + 2.510` for `t ≥ e`.) **Lemma N (PROVED):** `N(t) ≤ (t/2π) log t` for `t ≥ 21`.
 *Proof.* `(t/2π)log(t/2πe) = (t/2π)log t − 0.45166 t`, so `(t/2π)log t − N(t) ≥ 0.45166 t − 0.875 − 1.588 −
 0.137 log t − 0.443 log log t`, which equals `6.11` at `t = 21` and is increasing (derivative
 `0.45166 − 0.137/t − 0.443/(t log t) > 0`). ∎ (Script (A): Rosser's upper bound at `t = 21` is `4.06`, Trudgian's
 `4.73`, against `(21/2π)log 21 = 10.18`; slack `6.11` resp. `5.45`.)
* **(EF)** Paper 45 Thm 9.4: for real `F ∈ C_c^∞`, `supp F ⊆ [−T,T]`, `Σ_ρ Φ_F(ρ)Φ_F(1−ρ) = 2Φ_F(0)Φ_F(1) + 𝔞_T(F)`
 in symmetric order (Paper 47 `eq:W`: `W_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ)`).
* **(SUF)** Paper 45 Thm 10.4, used only in Corollary 2(iii).

## 2. Lemmas

**Lemma 1 (monotonicity without fixing contacts; PROVED).** `T ↦ λ^A(T)` is nonincreasing on `(0,∞)`; so are
`λ^P` and `λ^W`.
*Proof.* For `T < T′` and `F ∈ L²(I_T)`, extend by zero: `F ∈ L²(I_{T′})`, the Tate moments are unchanged, and
`𝔞_{T′}(F) − 𝔞_T(F) = −Σ_{n∈N_{T′}∖N_T} v_n c_F(log n) = 0` because `c_F` is supported in `[−2T,2T]` and `log n ≥ 2T`
for the new contacts. Hence `P_T ⊂ P_{T′}` isometrically with the same form values. Same for `𝒦_prim` (`c_F`
unchanged) and for `W_T` (`A, B` unchanged). ∎ (Paper 47 `cor:mono` states this at fixed contact set; `§9.2` end
states it for `λ^W` on the dual side.)

**Lemma 2 (explicit formula for rough tests; PROVED).** Let `F ∈ L²(I_T)` be real with
(a) `∫ log(2+|τ|)|F̂|² < ∞` and (b) `Σ_ρ |Φ_F(ρ)Φ_F(1−ρ)| < ∞`. Then `Σ_ρ Φ_F(ρ)Φ_F(1−ρ) = 2Φ_F(0)Φ_F(1) + 𝔞_T(F)`
(absolutely convergent sum). In particular for `F ∈ P_T`: **`𝔞_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ)`**, and for `ρ = ½ + iγ` on
the line the term is `|F̂(γ)|²`.
*Proof.* Let `η_ε ≥ 0`, `η_ε ∈ C_c^∞(−ε,ε)`, `∫η_ε = 1`, `F_ε := F ∗ η_ε ∈ C_c^∞`, `supp F_ε ⊆ [−T−ε, T+ε]`. Apply (EF)
to `F_ε` at window `T+ε`. Since `Φ_{F∗η}(s) = Φ_F(s)Φ_η(s)` and `|Φ_{η_ε}(s)| ≤ e^{ε|Re s − ½|} ≤ e^{ε/2}` in the
strip, with `Φ_{η_ε}(s) → 1` pointwise, the zero side converges to `Σ_ρ Φ_F(ρ)Φ_F(1−ρ)` by dominated convergence
(the symmetric-order sum equals the absolutely convergent one). Polar term: `Φ_{F_ε}(0)Φ_{F_ε}(1) → Φ_F(0)Φ_F(1)`.
Archimedean term: `|F̂_ε|² = |F̂|²|η̂_ε|² ≤ |F̂|²`, `|m(τ)| ≤ |C₀| + log(1+|τ|)` (`lem:mbounds`), so dominated
convergence gives `(1/2π)∫m|F̂_ε|² → (1/2π)∫m|F̂|²`. Prime term: `c_{F_ε} = c_F ∗ (η_ε ⋆ η_ε^†) → c_F` uniformly
(`c_F` is uniformly continuous), the sum runs over `n < e^{2T+2ε}` (finitely many, bounded in number for `ε ≤ 1`), and
for `e^{2T} ≤ n < e^{2T+2ε}` one has `c_F(log n) = 0`; so it converges to `−Σ_{n∈N_T} v_n c_F(log n)`. ∎

**Lemma 3 (the test family; PROVED).** Fix `T > 0`, an integer `k ≥ 5`, and let `b_k := (k/2)·1_{[−1/k,1/k]}`,
`φ_k := b_k^{∗k}` (`k`-fold convolution). Then:
(i) `φ_k ≥ 0`, `∫φ_k = 1`, `supp φ_k ⊆ [−1,1]`, `φ_k ∈ C^{k−2}(ℝ)`, `φ_k^{(j)}(±1) = 0` for `j ≤ k−2`, and
`‖φ_k‖₂² ≥ ½` (Cauchy–Schwarz: `1 = (∫_{−1}^1 φ_k)² ≤ 2∫φ_k²`).
(ii) `φ̂_k(x) = (sin(x/k)/(x/k))^k`; for real `x`, `|φ̂_k(x)| ≤ min(1, (k/|x|)^k)`; for complex `z`,
`|φ̂_k(z)| ≤ (k/|Re z|)^k e^{|Im z|}` (since `|sin(a+ib)|² = sin²a + sinh²b ≤ cosh²b`).
(iii) Put `G(t) := φ_k(t/T)`, `P(c) := (c² − ¼)(c² + γ₁²)`, and **`F := P(D)G = G⁗ + (γ₁² − ¼)G″ − (γ₁²/4)G`**, `D = d/dt`.
Then `F` is real, supported in `[−T,T]`, `F ∈ L^∞` (`k = 5`) or `C^{k−6}` (`k ≥ 6`), and **`F ∈ P_T`**: four integrations
by parts (boundary terms carry `G^{(j)}(±T) = 0`, `j ≤ 3`) give `∫F e^{ct} = P(c)∫G e^{ct}` for every `c ∈ ℂ`, and
`P(±½) = 0`.
(iv) `F̂(τ) = (τ² + ¼)(τ² − γ₁²)·T φ̂_k(Tτ)`; `Φ_F(s) = P(s−½)Φ_G(s)`, `Φ_G(½+β+iγ) = T φ̂_k(T(γ − iβ))`. In particular
`Φ_F(ρ₁) = Φ_F(ρ̄₁) = 0`.
(v) With `Y := Tγ₁/√2` and `ε_k(Y) := (1/π)k^{2k}Y^{1−2k}/(2k−1)`:
`‖F‖² ≥ (γ₁⁴/64)·T·(½ − ε_k(Y))` whenever `ε_k(Y) < ½`.
*Proof of (v).* On `|τ| ≤ γ₁/√2`: `(τ²+¼)² ≥ 1/16`, `(τ²−γ₁²)² ≥ γ₁⁴/4`. So
`‖F‖² = (1/2π)∫|F̂|² ≥ (γ₁⁴/64)(1/2π)∫_{|τ|≤γ₁/√2}T²|φ̂_k(Tτ)|²dτ = (γ₁⁴/64)·T·(1/2π)∫_{|x|≤Y}|φ̂_k|²`, and
`(1/2π)∫_{|x|≤Y}|φ̂_k|² = ‖φ_k‖₂² − (1/2π)∫_{|x|>Y}|φ̂_k|² ≥ ½ − (1/π)∫_Y^∞(k/x)^{2k}dx = ½ − ε_k(Y)`. ∎

**Lemma 4 (zero sums by counting; PROVED, uses (X19), Lemma N).** For `p ≥ 2` and `H ≥ 21`:
`S(H,p) := Σ_{γ > H} γ^{−p} ≤ (p/2π)·H^{1−p}·[log H/(p−1) + 1/(p−1)²]` (sum over positive ordinates, with
multiplicity).
*Proof.* `Σ_{γ>H}γ^{−p} = ∫_{H^+}^∞ t^{−p}dN(t) = [t^{−p}N(t)]_{H}^∞ + p∫_H^∞ t^{−p−1}N(t)dt ≤ p∫_H^∞ t^{−p−1}(t/2π)log t\,dt`
(the boundary term is `−H^{−p}N(H) ≤ 0`, the term at `∞` vanishes by Lemma N), and
`∫_H^∞ t^{−p}log t\,dt = H^{1−p}[log H/(p−1) + 1/(p−1)²]`. ∎

## 3. The theorem

**Theorem 1 (explicit unconditional decay of the margin; PROVED).** Let `T > 0`, `k ≥ 5` an integer,
`p := 2k − 8`, `Y := Tγ₁/√2`, and suppose `ε_k(Y) < ½`. Then
```
λ^W(T) ≤ λ^P(T) ≤ λ^A(T) ≤ B(T,k) :=
 2·1.0012 · T² · (k/T)^{2k} · [ S(21,p) + e^{T} S(3·10¹²,p) ]
 ───────────────────────────────────────────────────────────── (3.1)
 (14.13⁴ · T / 64) · (½ − ε_k(Y))
```
with `S(H,p) ≤ (p/2π)H^{1−p}[log H/(p−1) + 1/(p−1)²]` (Lemma 4). Consequently **`limsup_{T→∞} λ^A(T) ≤ 0`**, and
the same for `λ^P`, `λ^W`.

*Proof.* Take `F` of Lemma 3. (1) `F ∈ P_T` (Lemma 3(iii)), so `λ^A(T) ≤ 𝔞_T(F)/‖F‖²`.
(2) Hypotheses of Lemma 2: (a) `|F̂(τ)|² ≤ 1.0012·τ⁸T²(k/(T|τ|))^{2k}` for `|τ| ≥ 21` (below: `(τ²+¼)² ≤ (1 + 1/1764)²τ⁴
≤ 1.0012τ⁴`, `(τ²−γ₁²)² ≤ τ⁴`), which is `O(|τ|^{8−2k})`, `8 − 2k ≤ −2`, so `∫log(2+|τ|)|F̂|² < ∞`; (b) below.
Hence `𝔞_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ)`.
(3) The zeros `ρ₁, ρ̄₁` contribute `0` (Lemma 3(iv)); by (X19) there is no other zero with `|γ| ≤ 21`.
(4) Zeros with `21 < |γ| ≤ H₀` are on the line (X19′): term `= |F̂(γ)|² ≤ 1.0012·T²(k/T)^{2k}|γ|^{8−2k}`.
(5) Zeros with `|γ| > H₀`, `ρ = ½+β+iγ`, `|β| < ½`: `|P(β+iγ)| ≤ (γ²+β²+¼)(γ²+β²+γ₁²) ≤ (1+10^{−22})γ⁴`, `P` is even,
and `|Φ_G(ρ)|, |Φ_G(1−ρ)| ≤ T(k/(T|γ|))^k e^{T|β|}` (Lemma 3(ii),(iv)); so
`|Φ_F(ρ)Φ_F(1−ρ)| ≤ 1.0012·T²(k/T)^{2k}|γ|^{8−2k}e^{T}`.
(6) Summing (4)–(5) over `±γ` (factor `2`) with Lemma 4, `p = 2k−8 ≥ 2`:
`𝔞_T(F) ≤ 2·1.0012·T²(k/T)^{2k}[S(21,p) + e^{T}S(H₀,p)]`; this sum is finite, which is (b) of Lemma 2, so step (2)
is justified a posteriori (the bound in (6) is a bound on `Σ_ρ|Φ_F(ρ)Φ_F(1−ρ)|`).
(7) Divide by Lemma 3(v) with `γ₁⁴ ≥ 14.13⁴`. For the limit: Corollary 1. ∎

**Corollary 1 (closed form; PROVED).** For every `T ≥ 1`,
```
λ^A(T) ≤ 4·10⁹ · T · e^{−15.449 T}, 15.449 < 42/e = 2·21/e = 15.4494…. (3.2)
```
*Proof.* Take `k := ⌈21T/e⌉ ≥ 8`. Write `k = 21T/e + θ`, `θ ∈ [0,1)`. Then
`(k/(21T))^{2k} = exp(2k[log(1+θe/21T) − 1]) ≤ exp(−42T/e + 2θ²e/21T) ≤ e^{−15.4494T + 0.259}` for `T ≥ 1`. Next
`(k/T)^{2k}S(21,p) = 21⁹(k/(21T))^{2k}·(1/2π)·((2k−8)/(2k−9))·[log 21 + 1/(2k−9)] ≤ 21⁹·0.5797·(k/(21T))^{2k}` for `k ≥ 8`.
The `H₀` term is `e^{T}(21/H₀)^{2k−9}·[log H₀ + 1/7]/[log 21] ≤ 10·e^{T}(7·10^{−12})^{2k−9}` times the first
(the ratio of brackets is `9.48`), and `2k − 9 ≥ 15.449T − 9`, so it is `< 10^{−70}` of the first for all `T ≥ 1`.
Finally `ε_k(Y) ≤ 0.0157` for all `T ≥ 1`: for fixed `k`, `ε_k` decreases in `T`, so it suffices to check the left
endpoint of each `k`-interval — `T = 1` for `k = 8` (`ε_8 = 0.0060`; the interval's own left endpoint `0.906 < 1` is
excluded) and `T = (k−1)e/21` for `k ≥ 9`, where `k/Y ≤ 0.7731k/(k−1)` gives `ε_9 = 0.01566` (at `T = 8e/21 =
1.0354`, the supremum), `ε_10 = 0.0093`, decreasing thereafter; script (C) confirms `sup = 0.01566` at the endpoints
(a grid of step `10⁻³` reports `0.0155`). Since `½ − 0.01566 = 0.48434 ≥ 0.484`, the constant below survives. Then
`B ≤ 2·1.0012·0.5797·21⁹·e^{0.259}/(14.13⁴/64 · 0.484) · T e^{−15.4494T} = 3.96·10⁹·T e^{−15.4494 T}`. ∎
(Script (C): on `T ∈ [1,40]` the exact `min_k B(T,k)` is at most `0.036` of the right side of (3.2); the constant
`1.5·10⁸` would do numerically, `4·10⁹` is what the displayed inequalities give.)

**Remark 3.1 (variants, PROVED by the same proof).** (a) Without the factor `(D² + γ₁²)` (i.e. `F = (D² − ¼)G`,
using of (X19) only that no zero has `|γ| < γ₁`), the `ρ₁` term `(γ₁²+¼)²T²(k/(Tγ₁))^{2k}` dominates and the rate is
`e^{−2γ₁T/e} = e^{−10.40T}`; killing `ρ₁` moves the binding height from `γ₁` to the gap edge `21` and the exponent
to `2·21/e`. (b) The exponent is set by the *gap edge* `H` beyond the last killed zero: exactly `2H/e` per unit `T`
(with `k ≈ TH/e`), see §6 for general `H`.

### 3.2 Values

Script (B), exact `min_{k≥5} B(T,k)` of (3.1):

| `T` | `k_opt` | `21T/e` | **PROVED bound on `λ^A(T)` (hence `λ^P`, `λ^W`)** | Paper 47 `cor:mono` bound | consistency |
|---|---|---|---|---|---|
| `½ log 3 = 0.5493` | 5 | 4.24 | `4.75·10⁴` | `1.291` | `≥ 8.8577·10⁻⁵` (Thm C) ✓ (vacuous) |
| `log 2 = 0.6931` | 6 | 5.35 | `3.13·10³` | `2.327` | vacuous |
| `0.80` | 6 | 6.18 | `6.10·10²` | — | vacuous |
| `1.00` | 8 | 7.73 | `2.81·10¹` | — | vacuous |
| `1.50` | 12 | 11.59 | `1.69·10⁻²` | — | first non-trivial value (`< 1`) |
| `2.00` | 15 | 15.45 | `9.65·10⁻⁶` | — | below Thm C's `½log3` floor |
| `2.50` | 19 | 19.31 | `5.19·10⁻⁹` | — | |
| `3.00` | 23 | 23.18 | `2.71·10⁻¹²` | — | |
| `5.00` | 39 | 38.63 | `1.69·10⁻²⁵` | — | |
| `10.0` | 77 | 77.25 | `9.40·10⁻⁵⁹` | — | |

Crossings: `B = 1` at `T = 1.226`; `B = 8.8577·10⁻⁵` at `T = 1.852`; `B = 10⁻⁷` at `T = 2.303`.
**At the five requested windows `T ≤ 1.5` the theorem is vacuous or nearly so** (it beats `cor:mono` only from
`T ≈ 1.3`): it is an asymptotic statement, and the consistency check against Theorem C is trivially satisfied.

### 3.3 Where Theorem 1 sits

* **Trivial half of Zhu.** Zhu's Conj. 12.1 (arXiv:2608.24827; Paper 47 `main.tex:2735`) is `−log λ ≍ e^{2T}`.
 Theorem 1 gives `−log λ^A ≥ 15.449T − log(4·10⁹T)`: **linear, not exponential, in `T`** — exponentially weaker than
 the conjectured law; it is the direction that does not need the zeros' positions beyond height `21`. It is *not*
 evidence for the law; it only shows the margin is not bounded below.
* **What Route B with (X19) alone could give at best.** The out-of-band energy of a unit `F ∈ L²(I_T)` beyond `|τ| > 21`
 is at least `1 − λ₀(21T)` of the prolate operator, `≍ e^{−42T}` (Slepian–Fuchs/Landau–Widom asymptotic,
 `CITED-NOT-VERIFIED`, `00-references/PROLATE-REFERENCES.md`), so **no test function that uses only the gap
 `(γ₁, 21]` can beat `e^{−(42+o(1))T}`**; Theorem 1 realises `e^{−42T/e}`. The factor `e` is the price of the sinc-power
 bound `|sinc y| ≤ 1/|y|` (worst case `|sin| = 1` at every zero). `HEURISTIC` as a ceiling (needs the prolate asymptotic).

### 3.4 DIAGNOSTIC: the same test function, evaluated exactly

Script (D) evaluates `𝔞_T(F)/‖F‖²` for the `F` of the theorem by quadrature of the *symbol* (`m` through the
digamma function, plus the finite comb; **no zeros enter**):

| `T` | `k` | exact `𝔞_T(F)/‖F‖²` (quadrature) | PROVED `B(T,k)` | loss |
|---|---|---|---|---|
| `0.5493` | 5 | `4.90·10⁻¹` (±7 %, slow `τ^{−2}` tail) | `4.75·10⁴` | `10⁵` |
| `0.6931` | 6 | `1.04·10⁻²` | `3.13·10³` | `3·10⁵` |
| `0.80` | 6 | `3.25·10⁻³` | `6.10·10²` | `2·10⁵` |
| `1.00` | 8 | `1.13·10⁻⁵` | `2.81·10¹` | `2·10⁶` |
| `1.50` | 12 | `8.84·10⁻¹¹` | `1.69·10⁻²` | `2·10⁸` |
| `2.00` | 15 | `≈ 8·10⁻¹⁵` (±10 %, **roundoff-limited**: a 15-digit cancellation between the `m`-integral and the comb; panel widths `0.5/0.25/0.125/0.0625` give `8.58/8.38/7.90/8.02·10⁻¹⁵`, no convergence) | `9.65·10⁻⁶` | `10⁹` |

Three readings. (i) Consistency: at `½log3` the exact value `0.49 ≥ 8.8577·10⁻⁵` (Theorem C), as it must be.
(ii) The **proof loses 5–9 orders of magnitude** on its own test function: the sinc-power bound (`|sin| ≤ 1` at every
zero, while the true `|sinc(Tγ/k)|^k` is much smaller at the actual ordinates), the counting bound `N(t) ≤ (t/2π)log t`
(`≈ 10` at `t = 21` against the true `N(21) = 1`), and the weight `τ⁸` in place of `(τ²+¼)²(τ²−γ₁²)²`.
(iii) These exact values are themselves Rayleigh quotients of admissible `F ∈ P_T`, i.e. **upper bounds on
`λ^A(T)` modulo quadrature error** — `λ^A(1.0) ≤ 1.14·10⁻⁵`, `λ^A(1.5) ≤ 9·10⁻¹¹` — but they are `DIAGNOSTIC-NUMERIC`,
not certified (no interval arithmetic, tail of the `τ`-integral bounded analytically only). Cross-check of Lemma 2's
normalisation: the zero sum over the first 60 ordinates from `mpmath.zetazero` (*not an import of record; proves
nothing*) reproduces `𝔞_T(F)` to `1.7·10⁻⁵` relative at `T = 1` and `9·10⁻⁷` at `T = 1.5`; at `T = 2` the discrepancy
is `2.1·10⁻³` relative against a stated zero-tail of `4·10⁻²⁰` — quadrature/roundoff in the symbol integral, not zeros,
which is why the `T = 2` row is flagged roundoff-limited.

## 4. Route A (prime side, no zeros): why it cannot give decay

**Lemma 5 (the prime side of a primitive test is the Chebyshev remainder; PROVED).** For real `F ∈ P_T` with
`∫log(2+|τ|)|F̂|² < ∞`, writing `E(u) := ψ_{Ch}(e^u) − e^u` (Chebyshev's `ψ_{Ch}(x) = Σ_{n≤x}Λ(n)`),
```
𝔞_T(F) = C₀‖F‖² + Lév(c_F) + 2∫_0^{2T} c_F(u)e^{−u/2}du − 2∫_{(0,2T)} e^{−u/2}c_F(u)\,dE(u). (4.1)
```
*Proof.* `Σ_{n∈N_T}v_n c_F(log n) = 2∫_{(0,2T)}e^{−u/2}c_F(u)\,dψ_{Ch}(e^u)` (Stieltjes; `u ↦ ψ_{Ch}(e^u)` jumps by `Λ(n)`
at `u = log n`; `c_F(2T) = 0`). Split `dψ_{Ch}(e^u) = e^u du + dE(u)`. The main term is `2∫_0^{2T}c_F e^{u/2}du`, and
`∫_{−2T}^{2T}c_F(u)e^{u/2}du = A(F)\overline{B(F)} = 0` on `P_T` (substitute `s = t−u` in the double integral), so
`∫_0^{2T}c_F e^{u/2} = −∫_{−2T}^0 c_F e^{u/2} = −∫_0^{2T}c_F(u)e^{−u/2}du` (`c_F` even for real `F`). Insert into
`thm:A`'s `eq:Aform`. ∎

**Consequence (PROVED as stated, DIAGNOSTIC as a verdict).** On `P_T` the whole arithmetic of the prime comb reduces to
the last term of (4.1), and `E` is the object whose unconditional control *is* the zero-free-region theory
(`E(u) = −Σ_ρ e^{ρu}/ρ − log 2π − ½log(1−e^{−2u})`, `X20a`-type remainders `|E(u)| ≤ e^{u}ε(u)`, `ε(u) = exp(−c(log
e^u)^{3/5}…)`). With only such a bound, integrating (4.1)'s last term by parts gives `|…| ≤ C ε(2T)e^{T}(T‖F‖² + …)`,
which **tends to `+∞`**: Route A yields an upper bound of the shape `C₀ + O(1) + O(e^{T}ε(2T))` on `λ^A(T)`, *worse*
than `cor:mono` for large `T` and never `→ 0`. With only `|comb| ≤ A_T` and exact `m`, the best Route-A bound is
`inf_{P_T}(1/2π)∫(m + A_T)|F̂|² = λ^{∞,P}_{min}(T) + A_T → C₀ + A_T ∼ 4e^{T}` (`R155_023` Thm 1), also `→ +∞`. Any
prime-side proof that `λ^A(T) → 0` must therefore bound `∫e^{−u/2}c_F\,dE` by `o(‖F‖²)` for some `F ∈ P_T`, which by
Lemma 2 is a statement about `Σ_ρ Φ_F(ρ)Φ_F(1−ρ)` — Paper 47 `§9.3` item 5 in the present setting. **Route A is
closed; Route B is the only route, and Theorem 1 is its output.**

## 5. Consequences

**Corollary 2 (structure of the margin; PROVED).**
(i) *No uniform margin.* There is no `c > 0` with `λ^A(T) ≥ c` for all `T` (nor for `λ^P`, `λ^W`); for `T ≥ 1` every
lower bound must lie below `4·10⁹Te^{−15.449T}`. Every argument for `RH` through Weil positivity on windows must prove
`λ ≥ 0` with a margin tending to `0` at least this fast — and, if Zhu's law holds, like `exp(−ce^{2T})`.
(ii) *The limit exists.* By Lemma 1 and Theorem 1, `L^A := lim_{T→∞}λ^A(T)` exists in `[−∞, 0]`; likewise
`L^P ≤ L^A`, `L^W ≤ L^P`.
(iii) *RH is the value of the limit.* `RH ⟺ L^W = 0 ⟺ L^P = 0 ⟺ L^A = 0 ⟺ L^A ≥ 0`. *Proof.* Under RH, `W_T ≥ 0` on
`C_c^∞` tests (Weil's criterion), and for `F` in the form domain `W_T(F) = lim_{ε→0} W_{T+ε}(F ∗ η_ε) ≥ 0` by the
mollification argument of Lemma 2 (dominated convergence in the archimedean term, finitely many comb terms, `A, B`
continuous); so `0 ≤ λ^W ≤ λ^P ≤ λ^A ≤ B(T,k) → 0`, all three limits are `0`. If RH fails, (SUF)
gives a compactly supported primitive `F`, `supp F ⊆ [−T₀,T₀]`, with `𝔞_{T₀}(F) = W_{T₀}(F) < 0`, so `λ^A(T₀) < 0` and
`L^A ≤ λ^A(T₀) < 0` by Lemma 1. ∎ This sharpens `R155_053` Prop. 4.1 (`RH ⟺ lim λ^W ≥ 0`): the limit is a genuine limit,
it is `0` under RH with the explicit rate (3.2) — the HEURISTIC `λ^W ↓ 0` of `R155_053` is now PROVED —
and unconditionally `limsup ≤ 0`. Whether `L^A = −∞` when RH fails (Bombieri-type amplification of an off-line
zero) is not on record: `OPEN` (the corpus's converse is non-effective, `R155_053 §3`).
(iv) *Certificates must be exponentially precise.* By weak duality every dual feasible point `(ν, β)` of Paper 47 at
window `T` has `inf_τ f ≤ λ^P(T) ≤ B(T,k)`; every flat-top certificate of `thm:Z` has `inf_τ Σ_ρ ŵ(τ−γ_ρ) ≤ B(T,k)`.
At `T = 3` this is `2.7·10⁻¹²`, while the certificate must stay `≥ 0` on `[0, 2πe^{A_T}]`, `A_3 ≈ 80`. This is the
quantitative form of `§9.3` item 4 (*not an induction upward in `T`*): the target at `T′ > T` is not "the same
inequality with more contacts" but an inequality whose admissible slack has shrunk by `e^{−15.4(T′−T)}` at least,
and by `exp(−c(e^{2T′} − e^{2T}))` if Zhu is right. A `T`-uniform argument can only be an argument for `≥ 0` with no
room, i.e. an argument that is *exact* in the limit — consistent with `§9.3` item 1 (*not an identity*) only if the
approximation error itself is controlled by the same decaying scale.
(v) *For the reverse track.* Combined with Thm finZ (Paper 47 §7): no finite zero set carries a certificate, and now
no certificate at any window carries a margin larger than `B(T,k)` — the two ends of the same fact, that positivity
of `W` is a property of the *infinite* zero measure with *no slack*.

## 6. The hiding heuristic, and what an unconditional version would be

**General-`H` form (PROVED under the stated imports).** Let `0 < γ₁ < … < γ_J` be the positive zero ordinates below a
height `H` (imported, each simple or with multiplicity absorbed into the product), and suppose no zero has
`γ_J < |γ| ≤ H`. Put `F := (D² − ¼)Π_{j≤J}(D² + γ_j²)G`, `G = φ_k(t/T)`, `k ≥ 2J + 3`, `p := 2k − 4J − 4 ≥ 2`. The proof
of Theorem 1 gives verbatim (norm restricted to `|τ| ≤ γ₁/√2`, where `Π(γ_j² − τ²)² ≥ 4^{−J}Πγ_j⁴`; tail weight
`≤ (1+o(1))|γ|^{4J+4}`)
```
λ^A(T) ≤ 2(1+δ_H)·T²(k/T)^{2k}[S(H,p) + e^{T}S(H₀,p)] · 64·4^{J} / (Π_{j≤J}γ_j⁴ · T · (½ − ε_k(Y))),
```
and with `k ≈ TH/e` the rate is **`exp(−2HT/e)`**, valid only when `TH/e ≥ 2J + 3`. For `J = N(H)` (all zeros below
`H` killed) this is `T ≳ (e/π)log(H/2πe)`, against the Nyquist/Jensen constraint `T ≥ ½log(H/2πe)` for an entire
function of type `T` to vanish at `2N(H)` points of `[−H,H]`: the polynomial construction is Nyquist-consistent up
to the factor `2e/π = 1.73`. For `H = H₀ = 3·10¹²`: Nyquist `T ≥ 12.95`, this construction `T ≥ 22.4`.

**The heuristic (HEURISTIC).** Under RH, `λ^W(T) = min_F Σ_γ|F̂(γ)|²/‖F‖²`. `F̂` has type `T`, main lobe `≈ π/T`; below the
resolution height `X = 2πe^{2T}` (`§9.2`) the zeros are separated by more than the lobe, above it `Σ_γ ŵ(τ−γ)` sees only
the density `m(τ) ≈ log(τ/2π) > 0`. A band-limited `F̂` of type `T` has `2XT/π` degrees of freedom on `[−X,X]`
(Nyquist/Jensen), and must vanish at the `2N(X)` zeros there; `2N(X)/(2XT/π) = log(X/2πe)/(2T)`, which equals
`1 − 1/(2T)` at `X = 2πe^{2T}`: the zeros below the resolution height *saturate* the Nyquist count (that is what
"resolution scale" means), and the
extremal problem becomes: minimise the energy of `F̂` beyond `X` subject to vanishing at the zeros below `X`, with
the residual `Σ_{|γ|>X}|F̂(γ)|² ≈ (1/2π)∫_{|τ|>X}m|F̂|²`. Prolate-type concentration gives `exp(−cTX) = exp(−c′Te^{2T})`,
which is Zhu's `−log λ ≍ e^{2T}` up to the polynomial factor. **Why HEURISTIC:** (1) it needs the positions of all
zeros to height `2πe^{2T}` (only imports); (2) the interpolation step (vanishing at `≈ 4Te^{2T}` prescribed points
with controlled energy) is a Beurling–Malliavin/Paley–Wiener-space interpolation with explicit constants, nowhere in
the corpus; (3) the exact factor `c` depends on the fine zero statistics (the Nyquist count is *saturated*, so the
interpolation is at the edge of possibility, and gaps/clusters decide `c`). **The unconditional version one would
state (not computed):** *with the list `Z(H₀)` of the `N(H₀) ≈ 1.03·10¹³` ordinates up to `H₀ = 3·10¹²` as an import
of record (Platt–Trudgian), and an explicit interpolation-with-energy lemma, for every `T` with `T₀ ≤ T ≤
½log(H₀/2π) = 13.05`: `λ^A(T) ≤ exp(−c e^{2T})` with explicit `c, T₀`.* Beyond `T = 13.05` the resolution height exceeds
the verified range and the statement is conditional on the zeros there. This is the only route to the non-trivial
half of Zhu's law in a window, and it is `OPEN`.

## 7. Weakest steps

1. **Lemma 2 (mollification of Thm 9.4).** Relies on Paper 45 Thm 9.4 being valid at window `T+ε` for `F_ε` with
 the prime sum over `n < e^{2T+2ε}`; and on `|Φ_{η_ε}(s)| ≤ e^{ε/2}` in the strip (`|Re s − ½| < ½`). Check that
 Thm 9.4's sum is over *all* nontrivial zeros with multiplicity (yes, `Lemma 9.2` contour) and that the
 `2Φ_F(0)Φ_F(1)` convention matches Paper 47 `eq:W` (`A B̄` with `A = Φ_F(1)`, `B = Φ_F(0)`). The DIAGNOSTIC
 zero-sum check (§3.4) agrees to `10⁻⁵`, so the normalisation is right numerically.
2. **Step (5), off-line zeros.** Uses `|β| < ½` (the critical strip; `E2`-type import that no zero has `Re ρ ∉ (0,1)`
 is standard and is already in Paper 45's import list) and `H₀` from (X19′). The term is `< 10⁻⁷⁰` relative, so any
 slip here is immaterial to the numbers but not to the logic.
3. **Lemma 3(iii), `k = 5`.** `F` is then only `L^∞` (piecewise constant highest derivative); the integration by parts
 uses `G ∈ C³` with `G^{(j)}(±T) = 0`, `j ≤ 3`, and `G⁗ ∈ L^∞` — fine, but the audit should confirm `φ_5 ∈ C³`
 (five boxes: `C^{k−2}`). For `k ≥ 6` nothing is delicate. Only the vacuous small-`T` rows use `k < 8`.
4. **Lemma N.** [Amended per R155_059: the original draft attributed Backlund's 1918 constants `0.137, 0.443, 4.35`
 (range `t ≥ 200`) to Rosser with Rosser's range — a hybrid that is not a published statement.] Now stated as
 Rosser 1941 Thm 19 with constant `1.588`, `t ≥ 2` (Trudgian 2014 as alternative); slack `6.11` at `t = 21`,
 increasing. (X-N) is new to the corpus and must be entered in the import ledger.
5. **The constant `1.0012`** covers `(τ²+¼)² ≤ 1.0012τ⁴` for `|τ| ≥ 21`; `(τ² − γ₁²)² ≤ τ⁴` is exact. Fine.
6. **Corollary 1 rounding.** `2θ²e/(21T) ≤ 0.259` for `T ≥ 1`; `(2k−8)/(2k−9)·[log 21 + 1/(2k−9)]/(2π) ≤ 0.5797` for `k ≥ 8`
 (`= 0.5797` at `k = 8`); `ε ≤ 0.0155 → ½ − ε ≥ 0.484`; product `3.96·10⁹ < 4·10⁹`. Script (C) checks the exact
 `min_k B` against (3.2) on `[1,40]`: ratio `≤ 0.036`.
7. **Corollary 2(iii), failure direction.** Uses (SUF) exactly as stated in Paper 45 (compactly supported primitive `F`
 with negative form); the window `T₀` is `supp`-dependent and non-effective, which is why `L^A = −∞` is left `OPEN`.
8. **§3.3 ceiling `e^{−42T}`** and **§6** are HEURISTIC (prolate asymptotics cited, not verified; Nyquist count
 heuristic). Nothing PROVED depends on them.
9. **§3.4** values are not certified (double precision, Gauss–Legendre panels of width `0.25` to `τ = 4000`, analytic
 tail bound); they are recorded to show the size of the proof's loss, not as results.

## 8. Table of the explicit bound (Theorem 1 / Corollary 1)

| `T` | `min_k B(T,k)` (3.1), PROVED | `4·10⁹Te^{−15.449T}` (3.2), PROVED for `T ≥ 1` | exact value of the same `F` (DIAGNOSTIC) |
|---|---|---|---|
| `0.5493` | `4.75·10⁴` | — | `4.9·10⁻¹` |
| `0.6931` | `3.13·10³` | — | `1.0·10⁻²` |
| `0.80` | `6.10·10²` | — | `3.3·10⁻³` |
| `1.00` | `2.81·10¹` | `7.8·10²` | `1.1·10⁻⁵` |
| `1.50` | `1.69·10⁻²` | `5.1·10⁻¹` | `8.8·10⁻¹¹` |
| `2.00` | `9.65·10⁻⁶` | `3.0·10⁻⁴` | `≈ 8·10⁻¹⁵` (roundoff-limited) |
| `2.50` | `5.19·10⁻⁹` | `1.7·10⁻⁷` | — |
| `3.00` | `2.71·10⁻¹²` | `9.1·10⁻¹¹` | — |
| `5.00` | `1.69·10⁻²⁵` | `5.8·10⁻²⁴` | — |
| `10.0` | `9.40·10⁻⁵⁹` | `3.3·10⁻⁵⁷` | — |

**Labels.** Lemmas 1–5, Theorem 1, Corollaries 1–2(i)–(iv): PROVED (under the labelled imports (X19), (X19′), (X-N),
(EF), (SUF)). §3.3 ceiling, §6 heuristic: HEURISTIC. §3.4 and the last column: DIAGNOSTIC. `L^A = −∞` under ¬RH, the
Nyquist-range unconditional theorem of §6: OPEN. Row-D label unchanged; endpoint of record unchanged
(`8.8577·10⁻⁵` at `½log3`); no sign for `ζ` at any new window; Paper 47 untouched (proposed additions: Lemma 1 as a
remark after `cor:mono`; Theorem 1 + Corollary 2(i)–(iii) as a new subsection of `§9`, replacing the HEURISTIC clause of
`R155_053` Prop. 4.1; Lemma 5 as a remark in `§9.3` item 5).

## 9. Amended per R155_059

audit `R155_059_AUDIT_R8D.md` applied in place; no new claims. Changes:

1. **(X-N) citation corrected.** The draft's constants `0.137, 0.443, 4.35` were Backlund's (1918, `t ≥ 200`), not
 Rosser's; the memo misattributed them with Rosser's range. Now: Rosser 1941 Thm 19, `0.137 log t + 0.443 log log t
 + 1.588`, `t ≥ 2` (Trudgian 2014 `0.112/0.278/2.510`, `t ≥ e`, as alternative). Lemma N (`N(t) ≤ (t/2π)log t`,
 `t ≥ 21`) unchanged in statement; slack at `t = 21` is `6.11` (Rosser) / `5.45` (Trudgian); script step (A) rerun
 with the new constants (`rosser(21) = 4.06`, `trudgian(21) = 4.73`). (X-N) to be entered in the import ledger.
2. **Corollary 1 constants.** `sup_{T≥1} ε_k = 0.01566`, attained at the left endpoint `T = 8e/21 = 1.0354` of the
 `k = 9` interval (the draft's `0.0155` was a grid value); `½ − 0.01566 = 0.48434 ≥ 0.484`, so `3.963·10⁹ < 4·10⁹`
 survives. The `k = 8` value `0.0060` is stated to be at `T = 1`. The `H₀`-term factor `≤ 9` corrected to `≤ 10`
 (`9.48`); immaterial. Script (C) now evaluates `ε_k` at the exact interval endpoints.
3. **Corollary 2(iii).** Added the sentence extending Weil positivity under RH from `C_c^∞` tests to the form domain
 by the mollification of Lemma 2.
4. **DIAGNOSTIC table.** `T = 2` entry flagged `≈ 8·10⁻¹⁵ (±10 %, roundoff-limited)` with the audit's panel-refinement
 scatter; the previously omitted `T = 2` zero-sum cross-check discrepancy `2.1·10⁻³` recorded in §3.4 and §8.
5. **Import ledger.** The clause "every zero with `|Im ρ| ≤ 3·10¹²` is on the line" (Platt–Trudgian) is recorded as
 **(X19′)**, distinct from Paper 46's (X19) (which imports only `ρ₁` simple, `γ₁`, and the gap to `21`); Theorem 1
 steps (4)–(5) and §7 item 2 now cite (X19′).
6. **Script/README.** Docstring "eq. (1.7)" → "(3.1)"; runtime harmonised to the measured value (README).

Nothing in Theorem 1, Corollaries 1–2 or Lemmas 1–5 changed in statement. Labels unchanged.

---

**[Erratum per TEX_HOSTILE_REVIEW_R4 R4-1]**

* **Bug.** `scripts/r8d/r8d_margin_bound.py` (function `B`, the log-space rewrite of `(k/T)^{2k}Σ_{γ>H}γ^{-p}`)
 used `(k/(TH))^{2k}·H⁸`; the correct identity is `(k/T)^{2k}H^{1−p} = (k/(TH))^{2k}H⁹`, since `1 − p = 9 − 2k`.
 Every scripted value of `B(T,k)` in §3.2 and in the table of §7 (column "PROVED bound") was therefore too small
 by the factor `H`: `21×` for the gap term (and `3·10¹²×` for the negligible `H_PT` term). Fixed (`H⁸ → H⁹`,
 `8·log H → 9·log H`) and re-run (7.6 s).
* **Corrected values** (`min_k B(T,k)`): `½log3` `9.974·10⁵`; `log 2` `6.574·10⁴`; `0.80` `1.280·10⁴`;
 `1.0` `5.897·10²`; `1.5` `3.538·10⁻¹`; `2.0` `2.027·10⁻⁴`; `2.5` `1.091·10⁻⁷`; `3.0` `5.700·10⁻¹¹`;
 `4.0` `1.464·10⁻¹⁷`; `5.0` `3.557·10⁻²⁴`; `10` `1.974·10⁻⁵⁷` (same `k_opt` as before).
* **Corrected crossings:** `B = 1` at `T = 1.430` (not `1.226`); `B = 8.8577·10⁻⁵` at `T = 2.054` (not `1.852`);
 `B = 10⁻⁷` at `T = 2.506` (not `2.303`). The value "`2.7·10⁻¹²` at `T = 3`" of §5(iv) reads `5.700·10⁻¹¹`.
* **Script (C):** the worst ratio of `min_k B` to the right side `4·10⁹Te^{−15.449T}` of (3.2) on `[1,40]` is
 `0.7550` (not `0.036`); still `≤ 1`, so **Corollary 1 survives** as stated.
* **Diagnostic (D):** the proof loses `6.3`–`9.6` orders of magnitude on its own test function over
 `½log3 ≤ T ≤ 1.5` (not `5`–`9`); the sentence "it beats `cor:mono` only from `T ≈ 1.3`" was computed against
 the buggy values and is withdrawn (not re-derived).
* **Unaffected:** Theorem 1 and the explicit expression (3.1), whose hand derivation carries `21⁹` correctly; the
 constant `3.97·10⁹` of Corollary 1; Corollary 2; Lemmas 1–5; all labels.
* **Process note:** the audit `R155_059` (L138 "✓") passed the scripted crossings and missed the bug.

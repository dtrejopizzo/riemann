# Round 030-A — Rigidity of the weight without temperedness: the gap on Z, formulated and attacked

Object: `a^w_T(F) = Arch(F) − Σ_{n≥2} w_n c_F(log n)` on `P_T`; `v_n = 2Λ(n)/√n`; `d = w − v`;
`D(τ) = 2Σ d_n cos(τ log n)`; `Ω(τ) = C_0 + ∫_0^∞(1 − cos τu)K(u)du = Re ψ(¼ + iτ/2) − log π` (P47 lem:K, eq:Aform),
so that `Arch(F) = (2π)^{-1}∫Ω|F̂|²` for compactly supported `F ∈ L²`. `Z` = real zeros of `Φ_M(½+iτ)`, a given discrete
set. Quasi-radical family `X = Π_T(M∗φ)` of ROUND_021_A (1.1)–(1.3), ROUND_024_A §2.

## 0. Cross-check of antecedents

- **G2_B9_R3 Theorem R′ / Theorem N (phase 159).** Rigidity PROVED for `d` with `D_d` a tempered measure not charging `Z`
  (`𝒯_meas`). Its proof goes through a dichotomy stated in [H] terms; here only the direct part is used (§3, Prop. 1),
  which does not need it. What is asked without temperedness is **not** resolved there: §7 of that memo and R160_M2_R1 Prop 6.1 (iii)
  leave it open ("arithmetic step").
- **ROUND_025_B §1.** (R′) "`D ≤ 0` outside `Z`" ARGUED; box `|w_n| ≤ C(log n+1)`. Its counterexample `w = (1−s)v` is
  **wrong** (§2.2): it assumed `Arch(X) > 0` on the family, but `Ω < 0` on `|τ| < τ_0`.
- **Index 212-25…212-29.** Explicit dampings (`v cos(ω log n)`): falsified (212-29). Dual state (212-28)
  numerical. They do not touch rigidity.
- **Index l.553/4459 (f_t = ζ + t·g, R163_901), l.5496 (R164_401 Thm R), l.5531 (R162_2601c), l.5977
  (BARRIER_D1_001), l.559 (Beurling), l.6710 (quasicrystals L30, L59, L60, L101, L102).** Atomic Hamburger
  rigidity (FE conductor 1 ⟹ cζ) is PROVED as a tool. Quantitative Hamburger via analytic norms is NO-GO.
  The `f_t` have coefficients outside `ℕ`. **None is retried.** §4 only cites Hamburger as a conditional reading.
- **New here.** (i) Correction of 025_B. (ii) The exact shape of the gap in a finite window, with the upper bound
  `P ≤ G` on the masses. (iii) The reduction to a problem of crystalline pairs with integer spectral support.

## 1. Finite window: exactly which inequalities the family gives

Fix `ℓ < T` and real `φ ∈ C_c^∞(−ℓ/2, ℓ/2)`. Let `X = Π_T(M∗φ)`. By ROUND_021_A (1.2)–(1.3):
`c_{M∗φ}` is doubly exponentially small outside `|u| ≤ ℓ + C_M`, and
`a^v_T(X) ≤ η(T,ℓ)‖φ‖²` with `η ≍ e^{cT}exp(−2πe^{2(T−ℓ−C_M)})`. With the box `|d_n| ≤ C(log n+1)` (025_B §2):

  **(I_{T,ℓ})** `Σ_{n ≤ e^{ℓ+C_M}} d_n c_{M∗φ}(log n) ≤ η'(T,ℓ)‖φ‖²`, with `η' = η + C e^{2T}·T·exp(−2πe^{2(T−ℓ−C_M)})`.

  In spectral form: `(2π)^{-1}∫ D_{ℓ}(τ)|Φ_M(τ)|²|φ̂(τ)|²dτ ≤ η'‖φ‖²`, with `D_ℓ = 2Σ_{n ≤ e^{ℓ+C_M}} d_n cos(τ log n)`
  plus an explicit tail `≤ η'`. The polynomial is finite. It holds if `T − ℓ ≥ ½log T + C`, i.e.
  `ℓ = T − O(log T)` (ARGUED on the cited bounds).
- **Resolution.** `|φ̂|²` is, in the best case, a Fejér kernel of width `≍ 1/ℓ` centered at any `x`. The
  points of `Z` in `[−L, L]` are separated by `≍ 2π/log L`. For `log L ≪ ℓ`, window `T` resolves each point of `Z`.
- **What it does not see.** Near a simple `γ ∈ Z` one has `|Φ_M|² ≍ (τ−γ)²`. An atom `aδ_γ + bδ′_γ` of `D` contributes
  0 to (I) (`(|Φ_M|²|φ̂|²)(γ) = 0` and its derivative too). Only `δ″` or higher would be visible. This is exact,
  not a resolution problem: **no** window and no `ℓ` sees masses of order ≤ 1 on `Z`.

## 2. Lines of attack

### 2.1 (a) All windows at once; Fejér and counting — DOES NOT CLOSE

Combining (I_{T,ℓ}) for every `T`: `−|Φ_M|²D` is a measure ≥ 0 (Bochner–Schwartz). Therefore `D = −N + P`, with
`N ≥ 0` on `ℝ∖Z` and `P` supported on `Z`, of order ≤ 1 at the simple points (PROVED, given (R′)). Mean zero: `D̂` vanishes
on `(−log 2, log 2)`; with Fejér `K ≥ 0`, `supp K̂ ⊂ (−log 2, log 2)`, one gets `N∗K = P∗K`. **Counting contradicts nothing.**
`Z ∩ [−L, L]` has `≍ L log L` points. The box only gives `|D_ℓ| ≲ e^{ℓ/2}ℓ` pointwise, an enormous available mass.
Fejér at scale `1/ℓ` does not see `P`. There is no large-sieve inequality separating "peaks on `Z`" from "compensation outside"
without sign information on `Z`. **Witness that the pattern exists:** `v` itself. By (1.1) of 021_A,
`(Ω − D_v)|Φ_M|² = 0` as a distribution (polarizing `a^v(X) ≈ 0`; PROVED in a window with error `η`). Thus
`D_v = Ω − G`, with `G` supported on `Z`: a Dirichlet polynomial with integer frequencies that is "smooth outside `Z`
plus atoms on `Z`" exists. So (a) cannot exclude the pattern for size reasons.

### 2.2 Correction: the multiples `(1 ± s)v` ARE excluded by (R′) — PROVED (sketch)

`d = −sv`, `s ∈ (0, 1]`: `−∫D|X̂|² = s∫D_v|X̂|² = s∫Ω|X̂|² + O(η)`. Choose `φ̂` concentrated on `|τ| < τ_0`, with
`τ_0 = 6.2898…` and `Ω(0) = −5.372…` (script `free_weight_scripts/r030_arch_symbol_root.py`). `Φ_M ≠ 0` there, because
`min Z > τ_0`, and that minimum is the only thing used about `Z`. Then `a^{(1−s)v}_T(X) ≈ s(2π)^{-1}∫Ω|Φ_M|²|φ̂|² < 0`. With `d = +sv`
one uses `|τ| > τ_0`, where `Ω > 0`. The counterexample of 025_B §1 is **withdrawn**.

### 2.3 (b) Other near-null generators — DOES NOT CLOSE; upper bound `P ≤ G`

- Derivatives, translations and `S_ζ h` with admissible `h` have `X̂ = ζ-factor·Φ_h·φ̂`. The factor vanishing on `Z` is common
  to the whole family `S_ζ`. Changing `h` changes the weight outside `Z`, never on `Z`. Still blind to order ≤ 1 (PROVED).
- Dividing: `Φ_h` with poles on `Z` gives `X̂(γ) ≠ 0`. Then `X` is no longer near-null:
  `a^v_T(X) = (2π)^{-1}⟨G, |X̂|²⟩ + O(η)`, and by (2.1) that is exact in the window. The hypothesis gives
  `⟨G − P, |X̂|²⟩ + ⟨N, |X̂|²⟩ ≥ −η`. Varying `X̂(γ)` and `X̂′(γ)` with the rest near-null:
  **`P ≤ G` as forms of order ≤ 1 at each `γ`** (ARGUED: requires tests interpolating jets on `Z` with norm
  controlled on `P_T`; see the interpolator of P47 thm:nyq). It is an **upper** bound on `P`. It does not give `P = 0`.
- Tests not of the form `S_ζ h` but near-null: if `a^v_T(X) → 0`, then `⟨G, |X̂|²⟩ → 0`. Every near-null test
  has `X̂` small on `Z` in the sense of `G`. **Blindness on `Z` is intrinsic to near-nullity**, not to the family
  (ARGUED from `a^v = ⟨G, |·̂|²⟩` in a window).

### 2.4 (c) Local and two-packet tests — DOES NOT CLOSE

With support of length `< log 2`, the comb does not enter: `a^w = Arch`, which does not depend on `d`. With two packets separated
by `log n` and of width `h`: `Arch ≍ log(1/h)‖F‖²` versus `d_n‖f‖²`. That gives the box `|d_n| ≤ C log n` and nothing better:
the archimedean margin of a localized test is `≫ 1`, while what must be detected lies in a near-null test.
Combined with (a), it only bounds `‖P‖` locally by the box (PROVED), which was already compatible with §2.1.

### 2.5 (d) The possible counterexample: what it must satisfy

`d ≠ 0` serves as a counterexample to rigidity **if and only if** (modulo the ARGUED parts of 2.3):
(C1) `d` is real, supported on `n ≥ 2` and satisfies `|d_n| ≤ C log n`;
(C2) `D = −N + P`, with `N ≥ 0` outside `Z` and `P` supported on `Z`, of order ≤ 1;
(C3) `P ≤ G` at each point;
(C4) positivity in the remaining (non-near-null) directions, which (I) does not control.
Formal tests:
- `d = −sv` and `d = +sv`: violate (C2) by §2.2.
- `w_n = v_n m(log n)`: `D_w = (Ω − G)∗m̂` shifts the atoms off `Z`. Violates (C2) unless `m̂ = δ`.
  The twists `cos(α log n)` move `G` to `Z ± α` (consistent with 212-29).
- `v·log^j n`: `D` contains derivatives `Ω^{(j)} − G^{(j)}`. The `δ^{(j)}` with `j ≥ 2` are visible: violates (C2).
- Systems with the same `Ω` and atoms `G_B` on `Z_B ≠ Z` (Beurling type, `f_t` of R163_901): outside `Z`,
  `D = −G_B ≤ 0`; on `Z`, `P = G`. **They pass (C2) and (C3).** Only (C1) excludes them: their spectrum is not in `log ℕ`
  (index l.5496: coefficients outside `ℕ`).
**Exact form of what is open (OPEN).** Is there a nonzero pair `(N, P)` as in (C2)–(C3) such that `−N + P` has
transform supported on `±log ℕ_{≥2}` with real coefficients satisfying the box? It is a Fourier uniqueness problem
between a discrete set (`Z`) and the spectrum `log ℕ`. The corpus sources (L30, L59, L60, L101, L102) do not
resolve it; L101 does not apply (index l.6710).

## 3. Results

**Prop. 1 (tempered rigidity without dichotomy; PROVED, sketch).** Let `w` be admissible for every `T`. If `D_d` is a
locally finite measure with `|D_d|(Z) = 0`, then `d = 0`.
*Proof:* by (R′), `D_d ≤ 0` on `ℝ∖Z`. Since there is no mass on `Z`, `D_d ≤ 0` on `ℝ`. With Fejér: `0 = D_d∗K ≤ 0`, and it is
identically zero with `K > 0` on an open set, hence `D_d = 0` and `d = 0`. Coincides with R′ of G2_B9_R3, but without the
[H] step. Temperedness enters only so that `D_d∗K` makes sense as a measure. In a window (I) suffices, thanks to the finite polynomial.
**Prop. 2 (reduction; PROVED given (R′), ARGUED at (C3)).** Without temperedness: `w` admissible for every `T` ⟹ `d` satisfies
(C1)–(C3). In particular, `w ≠ v` ⟹ `D_d` has a nonzero atomic part of order ≤ 1 on `Z`, with
`P ≤ G`, and `P ∗ K = N ∗ K`.
**Minimal hypothesis for the theorem:** `P = 0`, i.e. `D_d` without atoms or dipoles on `Z`. It is strictly weaker
than 𝒯_meas: it suffices that `D_d` be, in a neighborhood of each `γ`, a distribution of order ≥ 2 or a function.

## 4. Verdict

- **Theorem:** Prop. 1 (rigidity under "`D_d` does not charge `Z`"). PROVED, with (R′) ARGUED in the chain of windows
  (status inherited from 025_B §1). It is new in one sense only: it removes the [H] step of R′.
- **Without temperedness: NO-GO for lines (a), (b) and (c) as posed.** The exact obstruction is this: every
  test with small `a^v_T` has `X̂` small on `Z` in the sense of `G` (§2.3). The bounds given by non-near-null
  tests have margin `≫ 1` (§2.4). Therefore no inequality of the form `a^w_T ≥ 0` evaluated on individual
  tests separates `P` from `0` below `G`. The only thing that could do it is the integer spectral structure (C1).
- **CONDITIONAL:** if a uniqueness theorem holds of the type "a measure supported on `Z`, of order ≤ 1, plus a
  measure ≤ 0 outside `Z`, with spectrum in `±log ℕ_{≥2}`, is zero", then rigidity without temperedness holds. A
  Hamburger-type reading (FE + coefficients in `ℕ` ⟹ identification; PROVED tool of R162_2601c) would point there,
  but it requires `Σ w_n n^{-s}` to be the logarithmic derivative of a series with functional equation, and that does not follow from
  (C1)–(C3). OPEN.
- **Existence of a second admissible weight:** the sources do not exclude it. The natural candidates (§2.5) die at
  (C1) or at (C2). None survives, none was constructed, and there is no proof that none exist.

## 5. Controls (step that excludes them)

- **Doubled weight** `w = 2v`, `d = v`: `D = Ω − G > 0` on `|τ| > τ_0` outside `Z`. Violates (C2). Step: §2.2 / (R′). PROVED.
- **Deletion of `p^k`:** `d = −v_{p^k}δ_{p^k}`, `D = −2v_{p^k}cos(kτ log p)`, which is `> 0` on intervals of length
  `π/(k log p)`. Those intervals contain open sets disjoint from `Z`, because `Z` is discrete. Violates (C2). Step: (R′).
  PROVED. It is a measure (function) that does not charge `Z`, so Prop. 1 also excludes it.
- **Beurling type** (same `Ω`, atoms on `Z_B`): **passes (C2)–(C3)**. Only (C1), the support in `log ℕ`, excludes it, which
  is a hypothesis of the statement and not a step of the argument. If formulated as `w` on integers with `D_d = G − G_B`, it does not
  exist (R164_401: coefficients outside `ℕ`). The argument does not exclude it by itself: it is exactly the gap.

Labels: (I_{T,ℓ}) ARGUED; §2.1 decomposition PROVED given (R′); §2.2 PROVED (sketch); `P ≤ G` ARGUED;
Prop. 1 PROVED (sketch); Prop. 2 PROVED/ARGUED; rigidity without temperedness OPEN; counterexample OPEN.

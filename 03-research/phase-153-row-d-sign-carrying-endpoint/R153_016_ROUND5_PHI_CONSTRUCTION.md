# R153.016 — Round 5, builder: the truncated Weil symbol `σ_T`, its negative set, the prime bands `Φ_2, Φ_3`, and the attempted mesh-free endpoint proof

*Builder: Opus 5. 2026-09-19. Orders: R153_015 (lead). Scripts: `scripts/round5/`.*

**One-line result.** The symbol object is built and three new exact identities are proved (reduced symbol, autocorrelation/Krein reformulation, explicit `τ_1`). The hand proof **does not close at either endpoint**, and the reason is now a theorem, not a guess: the negative set `N_T` is *not* a neighbourhood of `0` — it extends to `τ ≈ 16.75` at `½log3` and `τ ≈ 59.54` at `log 2`, while the entire uncertainty budget of type-`T` functions is `|τ| ≲ π/(2T) ≈ 2.3`. Every uncertainty/domination argument is therefore vacuous by more than an order of magnitude, at both endpoints. As a by-product `Ξ_{0.45}` is shown to **satisfy** the width condition that `ζ` violates, which kills the width reading of Theorem A.

---

## 1. Corpus check (mandatory)

| item | hit | what is already there | what is new here |
|---|---|---|---|
| Symbol of the Weil form | `03-research/phase-60-discriminant/RH-PROOF-PAPER.md:46` — "the archimedean symbol is `Ω̃(t) = −log π + Re ψ_Γ(1/4+it/2)`; the prime symbol is `D_λ(t) = Σ_{n≤λ²}Λ(n)n^{−1/2}cos(t log n)`" (identical to `σ_T`, one prefactor apart), and the same line in `phase-61-open-problems/RH-PROOF-PAPER.md:46` | the symbol exists verbatim, for the **band-limited** space `E_λ` (spectral support), together with its no-go | the symbol here is attached to the **compactly supported, two-moment** space `P_T` of Paper 42, i.e. to a *certified* operator; `N_T`, the well/band table, `τ_0`, `τ_1` and the width ratio are new |
| Deficit window `Ω_Γ`, `g_Γ(τ_Γ)=1` | `04-papers/42-arithmetic-lefschetz-programme/main.tex:6332–6340` (`τ_Γ=0.2860886…`, weights `w_±`, band coherence, width `log(3/2)`) | the split of `g_Γ−1` into `w_±` on `Ω_Γ` for the *leakage* problem | that split is against the constant `1` (Gamma–Tate source estimate), not against `m_0 + primes`; `σ_T` and `N_T` are a different decomposition |
| Truncation deficit `Ω(0) − B_S` | `03-research/phase-46*/142-ataque-gap135B-semilocal.md:155,175–178,206` — `B_{\{2,3\}} ≈ 6.3485`, `Q_S(f_T) → Ω(0) − B_S < 0` | the semilocal object is negative once the primes in `S` are switched on **without** the support restriction | `σ_T(0) = −7.6210…` at `log 2` is the *same* phenomenon read at frequency `0`; the new content is that the support restriction `T = log 2` is what saves it, quantified by `τ_0 T` |
| Archimedean domination = blindness | `03-research/phase-36*/108-puente-criba-indice.md:324,330` ("la dominación arquimediana y la ceguera son el mismo fenómeno", Thm 3.3) | absolute domination fails; negativity is second-order cancellation | confirmed independently here: `‖σ_T^-‖_{L¹}` beats every floor by a factor `≳ 10` |
| Slepian budget | `phase-106*/106_16_LOCAL_LOGARITHMIC_PRIME_GAMMA_SCALE.md:121,197`; `R153_012_ROUND4_DECAY_LAW.md:82–97,283` (P-Slepian **REFUTED**) | prolate concentration already used, and already refuted as the *rate* mechanism | here it is used as an *inequality*, not a rate; it is refuted again, for a different and sharper reason |
| Compact polar potential | `main.tex:4088–4114` (`F = (−d²/dt²+¼)G`, `G ∈ C_c^∞(I_T)`, Green kernel `e^{−|t|/2}`) | the lemma | its use to **eliminate the two constraints** from the quadratic form (§2.2) is new |

Conclusion of the check: the symbol picture pre-exists for other spaces and other purposes; a symbol-plus-uncertainty attempt on `P_T` does not. Nothing below duplicates a prior result.

---

## 2. The construction

### 2.1 The truncated Weil symbol (PROVED)

Normalisations. `F̂(τ) = ∫_ℝ F(t)e^{−iτt}dt`, `‖F‖² = (2π)^{-1}∫|F̂|²dτ`. `S_aF(t) = F(t+a)` has multiplier `e^{iaτ}`, so `S_a + S_{−a} ↦ 2cos(aτ)`. From `main.tex:4117` (`eq:localizedprimitiveoperator`), for `F ∈ C_c^∞(I_T)` extended by zero,

  `⟨A_T F,F⟩ = (2π)^{-1} ∫_ℝ σ_T(τ)|F̂(τ)|² dτ`,
  `σ_T(τ) := g_Γ(τ) − m_0 − 2 Σ_{n<e^{2T}} w_n cos(τ log n)`, `w_n = Λ(n)/√n`.

*Proof.* `G_{Γ,T}` is the zero-extension compression of the multiplier `g_Γ` (`main.tex:4127`), so on zero-extended `F` its quadratic form is the full multiplier integral; `m_0 I` and each symmetric shift pair are multipliers; Plancherel. ∎

**Simplification (new, PROVED).** With `g_Γ(τ) = Re ψ(¼+iτ/2) − ψ(¼)` and `m_0 = log π + γ + π/2 + 3log2 = log π − ψ(¼)`,

  **`g_Γ(τ) − m_0 = Re ψ(¼ + iτ/2) − log π`.**

So `σ_T` is *exactly* the classical archimedean Weil symbol minus the truncated prime symbol — the `Ω̃ − 2D_λ` of phase 60, with no residual constant. The `−ψ(¼)` bookkeeping of Paper 42 cancels identically. In particular `σ_T(0) = Re ψ(¼) − log π − 2Σw_n = −5.3721834192… − 2Σw_n`.

Numerically: at `T = ½log3` (only `n = 2`, since `n < e^{2T} = 3`) `2Σw_n = 0.98025814`, `σ(0) = −6.35244156`; at `T = log 2` (`n = 2,3`) `2Σw_n = 2.24882634`, `σ(0) = −7.62100976` (matches the lead's `≈ −7.6`).

**Prime bands.** `Φ_n(τ) := −2w_n cos(τ log n)`, period `2π/log n`. `Φ_2` has period `9.0647` and amplitude `0.98026`; `Φ_3` has period `5.7192` and amplitude `1.26857`. `Φ_n > 0` exactly on `cos(τ log n) < 0`. At `T = log 2` both are positive on `τ ∈ (π/(2log2), 3π/(2log3)) = (2.26618, 4.28937)` — the lead's window, confirmed — and `σ_{log2} > 0` there although `g_Γ − m_0 < 0` on all of it. **This is the display of "the primes pay Gamma's deficit": it happens on one band, `(2.2775, 4.8160)`, and nowhere else below `τ = 11.97`.**

### 2.2 Reduced symbol: the constraints disappear (new, PROVED)

By `lem:compactpolarpotential` (`main.tex:4088`), `F ∈ P_T ∩ C_c^∞` ⟺ `F = (−d²/dt²+¼)G`, `G ∈ C_c^∞(I_T)` **unconstrained**. Then `F̂(τ) = (τ²+¼)Ĝ(τ)` (sign check: `−d²/dt² ↦ τ²`, so the multiplier is `τ²+¼ > 0`, as required for the Green kernel `e^{−|t|/2}` to be positive), and

  **`⟨A_T F,F⟩ = (2π)^{-1}∫ ρ_T(τ)|Ĝ(τ)|²dτ`, `ρ_T := (τ²+¼)² σ_T`, `G ∈ L²(I_T)` arbitrary.**

`A_T ≥ 0` on `P_T` ⟺ the zero-extension compression to `I_T` of the multiplier `ρ_T` is `≥ 0`. This is the clean form: a *one-space, no-constraint* problem. It also gives immediately `‖G‖ ≤ (μ+¼)^{-1}‖F‖` with `μ = (π/2T)²` (Dirichlet Poincaré twice on `I_T`).

### 2.3 Autocorrelation form and the exact LP reformulation (PROVED, RESTATEMENT)

Put `Φ := |F̂|²`. Since `supp F ⊂ [−T,T]`, `Φ` is the Fourier transform of the autocorrelation `A_F(t) = ∫F(u)F(u+t)du`, supported in `[−2T,2T]`: `Φ ≥ 0` is entire of exponential type `2T` and in `L¹`. Conversely (Krein–Fejér factorisation of nonnegative type-`2T` `L¹` functions) every such `Φ` is `|F̂|²` with `supp F ⊂ [−T,T]`. The two moment conditions read `Φ(±i/2) = 0` (double zeros). Hence

  **`A_T ≥ 0` on `P_T` ⟺ `∫σ_T Φ ≥ 0` for every `Φ ∈ 𝒦_{2T} := {Φ ≥ 0 on ℝ, entire of type 2T, Φ ∈ L¹, Φ(±i/2) = 0}`.**

This is an exact linear-programming statement: a Beurling–Selberg problem for the symbol `σ_T`. *Consequence (proved, and it is the structural obstruction of this round):* a proof by minorant, i.e. producing `m ≤ σ_T` with `∫mΦ ≥ 0` for all `Φ ∈ 𝒦_{2T}`, cannot be based on Bochner: `∫mΦ ≥ 0` for **all** nonnegative `L¹` functions of type `2T` on the full line is equivalent to `m̂` being a positive-definite measure, i.e. to `m ≥ 0` everywhere, which forces `σ_T ≥ 0` — false. Any working minorant must use the compact support of `F`, i.e. must already solve the compression problem. This is why no soft argument exists.

### 2.4 The explicit `τ_1` (PROVED)

From the series `ψ(¼+iy) = −γ + Σ_{k≥0}[1/(k+1) − 1/(k+¼+iy)]`,
`Re ψ(¼+iτ/2) = −γ + Σ_{k≥0}[1/(k+1) − (k+¼)/((k+¼)²+τ²/4)]`, each summand strictly increasing in `τ²`. Hence `τ ↦ g_Γ(τ)−m_0` is strictly increasing on `[0,∞)` from `−5.37218…` to `+∞`, and since `|2Σw_n cos(τ log n)| ≤ 2Σ w_n =: 2S_T`:

  **`σ_T(τ) > 0` for all `|τ| > τ_1(T)`, where `τ_1(T)` is the unique root of `Re ψ(¼+iτ/2) − log π = 2S_T`.**

`τ_1(½log2) = 6.2898`, `τ_1(½log3) = 16.7481`, `τ_1(log 2) = 59.5440`, `τ_1(½log5) = 133.3`, `τ_1(½log7) ≈ 807`. Because `Re ψ(¼+iy) = log y + O(y^{-2})`, `τ_1(T) ≍ 2π e^{2S_T}` and `2S_T ~ 4e^{T}` (PNT), so **`τ_1(T)` grows doubly exponentially in `T`**.

---

## 3. (T1) `σ_T` and `N_T`: the tables

`N_T := {σ_T < 0}`. Computed with `scipy` digamma on a `10⁻⁴` grid with bracketed `brentq` roots (`scripts/round5/r5_wells.py`); `DIAGNOSTIC-NUMERIC` for the numbers, `PROVED` for the containment `N_T ⊂ [−τ_1,τ_1]`.

**`T = ½log3` (only `Φ_2`), `σ(0) = −6.352442`, `τ_1 = 16.7481`:**

| sign | interval | extremum of `σ` | `∫σ` |
|---|---|---|---|
| **NEG** | `[0, 3.30501]` | `−6.35244` | `−7.2641` |
| pos | `[3.30501, 6.94490]` | `+0.69935` | `+1.6422` |
| **NEG** | `[6.94490, 10.53102]` | `−0.62758` | `−1.4541` |
| pos | `[10.53102, 16.7481]` | `+1.75770` | `+7.1215` |

`D_T = 6.35244`, `sup N_T = 10.53102` (three sign changes).

**`T = log 2` (`Φ_2` and `Φ_3`), `σ(0) = −7.621010`, `τ_1 = 59.5440`:** eleven sign changes,
`2.27751, 4.81599, 7.27165, 9.66624, 11.96583, 16.25109, 18.49377, 27.55780, 28.93805, 45.14914, 46.12911`.

| sign | interval | extremum | `∫σ` |
|---|---|---|---|
| **NEG** | `[0, 2.27751]` | `−7.62101` | `−7.4581` |
| pos | `[2.27751, 4.81599]` | `+1.12716` | `+1.8277` |
| **NEG** | `[4.81599, 7.27165]` | `−0.74073` | `−1.1639` |
| pos | `[7.27165, 9.66624]` | `+0.65951` | `+1.0121` |
| **NEG** | `[9.66624, 11.96583]` | `−0.79142` | `−1.1691` |
| pos | `[11.96583, 16.25109]` | `+2.97306` | `+7.6931` |
| **NEG** | `[16.25109, 18.49377]` | `−1.06540` | `−1.5555` |
| pos | `[18.49377, 27.55780]` | `+2.34775` | `+13.9106` |
| **NEG** | `[27.55780, 28.93805]` | `−0.40432` | `−0.3686` |
| pos | `[28.93805, 45.14914]` | `+3.84856` | `+31.2588` |
| **NEG** | `[45.14914, 46.12911]` | `−0.23259` | `−0.1513` |
| pos | `[46.12911, 59.5440]` | `+4.21536` | `+29.7214` |

`D_T = 7.62101`, `sup N_T = 46.12911`, `‖σ_T^-‖_{L¹} = 23.733`, `‖ρ_T^-‖_{L¹} = 2.105·10⁶`.

Orientation: `½log5` (`n=2,3,4`): 15 sign changes, `sup N = 108.95`, `σ(0) = −8.31416`. `½log7` (`n=2,3,4,5`): 33 sign changes, `sup N = 199.7`, `σ(0) = −9.75368`.

**First, decisive structural fact.** `N_T` is **not** a neighbourhood of `0`. The lead's expectation ("a neighbourhood of `0` plus whatever else") understates it: at `log 2` there are six disjoint wells reaching to `τ = 46.13`, and their union has measure `≈ 10.0` out of `[0, 59.54]`. The far wells are shallow (depth `0.23`–`1.07`) but they are exactly where `(τ²+¼)²` is large, so in the reduced symbol `ρ_T` they are catastrophic: `max_{N}|ρ_T| = 1.01·10⁶` is attained at `τ ≈ 46`, not at `τ = 0` (where `|ρ_T| = σ(0)/16 = 0.476`). **The `(τ²+¼)²` suppression, which was the lead's hoped-for lever, cures the deep well at the origin completely and creates a far worse problem at the far wells.**

---

## 4. (T2) The uncertainty inequality — what is actually provable

**Lemma U (PROVED).** Let `supp F ⊂ [−T,T]`, `Φ = |F̂|²`. Then `‖Φ‖_∞ ≤ 2T‖F‖²·2π/(2π)`, precisely `sup_τ|F̂(τ)|² ≤ (∫|F|)² ≤ 2T‖F‖²_{L²}`. Consequently, for any measurable `E`,
  `(2π)^{-1}∫_E Φ ≤ (T|E|/π)‖F‖²`,  in particular `θ(T,τ_*) := (2π)^{-1}∫_{|τ|<τ_*}Φ /‖F‖² ≤ 2Tτ_*/π`.
*Proof.* Cauchy–Schwarz on `∫_{-T}^{T}|F|`; Plancherel. ∎

**θ is not improvable by more than a bounded factor in this range.** The exact optimum is the prolate eigenvalue: `θ_opt(T,τ_*) = λ_0(c)`, `c = Tτ_*` (Slepian). Computed (Nyström, 400-point Gauss–Legendre, `DIAGNOSTIC-NUMERIC`):

| `T` | `τ_0` = first root of `σ_T` | `c = Tτ_0` | elementary `2c/π` | exact `λ_0(c)` |
|---|---|---|---|---|
| `½log2` | `6.28984` | `2.17989` | `1.38776` | `0.908654` |
| `½log3` | `3.30501` | `1.81546` | `1.15576` | `0.844460` |
| `log 2` | `2.27751` | `1.57865` | `1.00500` | `0.785584` |

The moment-zero route (b) of the blueprint is subsumed by §2.2 and, as shown in §3, **hurts**: `(τ²+¼)²` multiplies the far wells by up to `4.5·10⁶`.

**Proposition W (PROVED — the width ratio).** Define `R(T) := 2Tτ_0(T)/π`. Then `R(log 2) > 1` and `R(½log3) > 1`; equivalently `σ_T(π/(2T)) < 0` at both endpoints. *Proof.* Two rigorous evaluations of `σ_T(π/(2T))`, one by `mpmath` digamma at 40 digits and one by the increasing series of §2.4 truncated at `K = 2·10⁵` with tail bound `< 3.3·10⁻¹¹`:
`σ_{½log3}(2.85960087) = −0.4008683` (series: `−0.4008645`);
`σ_{log2}(2.26618007) = −0.0223560` (series: `−0.0223522`).
Both are negative by margins exceeding every error bound. ∎ Numerically `R(½log3) = 1.15576`, `R(log 2) = 1.00500`.

So the elementary bound `θ ≤ R(T)` is **vacuous at both endpoints** — at `log 2` by exactly `0.5 %`. The threshold `T·τ_0(T) = π/2` is crossed at `T_c = π/(2·2.277506) = 0.689803`, i.e. `0.48 %` below `log 2 = 0.693147`. Paper 42's certified endpoint sits just past the point where the elementary uncertainty budget runs out — which is a good structural match to `λ_min(A_{log2}|P_T) ≈ 9.9·10⁻⁸` (R153_014:9), but is *not* a proof of anything and must not be reported as one.

---

## 5. (T3) The hand proof: it does not close, at either endpoint

**Criterion C (PROVED as a criterion).** Suppose `N_T ⊂ (−τ_*,τ_*)`, `ε_* := inf_{|τ|≥τ_*}σ_T > 0`, `θ := θ(T,τ_*) ≤ 2Tτ_*/π < 1`. Then `⟨A_TF,F⟩ ≥ [ε_*(1−θ) − D_Tθ]‖F‖²`, and in the sharper `L¹` form `⟨A_TF,F⟩ ≥ [ε_*(1−θ) − (T/π)‖σ_T^-‖_{L¹}]‖F‖²`. Same statement with `(σ_T, F)` replaced by `(ρ_T, G)`.

**It fails, and not narrowly.** Criterion C requires `τ_* ≥ sup N_T`; but `sup N_T = 10.531` at `½log3` and `46.129` at `log 2`, whence

| `T` | `τ_* = sup N_T` | `2Tτ_*/π` | verdict |
|---|---|---|---|
| `½log3` | `10.5310` | `3.6828` | vacuous (`θ`-bound `> 1`) |
| `log 2` | `46.1291` | `20.3554` | vacuous |
| `½log5` | `108.950` | `55.815` | vacuous |
| `½log7` | `199.74` | `123.8` | vacuous |

Even with the exact prolate constant `λ_0(Tτ_*)` (which is `> 1 − 10⁻¹⁰` for `c ≥ 3.7`) the criterion is empty: the well structure of `σ_T` reaches out to `τ_1(T)`, while the concentration constant only starts to bite for `Tτ_* ≲ 1.5`, i.e. `τ_* ≲ 2.3` at `log 2`. **The shortfall is a factor `20.4` in the budget at `log 2` and `3.68` at `½log3`; it is not a matter of a sharper constant.** The `L¹` variant is no better: `(T/π)‖σ_T^-‖_1 = 5.235` at `log 2`, against a floor `ε_*` that is `0` (by continuity, `σ_T` vanishes at each of its eleven roots) — so the two-region form is exactly vacuous, and the band-refined form gives `Σ_i D_i λ_0(c_i) = 7.62·0.786 + 0.741·0.501 + 0.791·0.474 + 1.065·0.464 + 0.404·0.297 + 0.233·0.213 ≈ 7.31`, against a total positive budget bounded by `max σ_T`-type quantities of order `4`. Fails by `≈ 2×` even in the most optimistic band-by-band accounting, and that accounting is not even a valid bound (the `λ_0(c_i)` cannot all be saturated simultaneously, but no rigorous joint bound is available).

**Verdict (T3).** `½log3`: **does not close**, shortfall factor `3.68` in the uncertainty budget. `log 2`: **does not close**, shortfall factor `20.4`. No mesh-free proof of `thm:certifiedendpoints` is obtained. Label: `OPEN`; the attempt is `REFUTED` as a route.

**What finer input would be needed.** Not a better `θ`. One needs a *joint* bound on the masses `m_i = (2π)^{-1}∫_{W_i}Φ` of a single `Φ ∈ 𝒦_{2T}` over the six wells simultaneously, i.e. exactly the multi-interval Slepian/LP problem — which by §2.3 is equivalent to the original compression problem. Paper 42's 760-dimensional certificate is therefore not an artefact of laziness: **§2.3 shows no soft substitute exists.**

---

## 6. (T4) The uniform question

Statement: *for every `T > 0`, `∫σ_TΦ ≥ 0` for all `Φ ∈ 𝒦_{2T}`* — this is Weil positivity restricted to support `2T`, and it is equivalent to RH by exhaustion. How the obstruction evolves:

* Depth at the origin: `|σ_T(0)| = 5.3722 + 2S_T` with `2S_T ~ 4e^{T}` — grows **exponentially**.
* Extent: `sup N_T ≤ τ_1(T) ≍ 2πe^{2S_T}` — grows **doubly exponentially** (`16.7`, `59.5`, `133`, `807` at `½log3, log2, ½log5, ½log7`).
* Uncertainty budget: `π/(2T)` — **shrinks** like `1/T`.
* Well width at the origin: `τ_0(T)` shrinks (`3.305 → 2.278 → 1.982 → 1.350`), and the width ratio `R(T) = 2Tτ_0(T)/π` oscillates: it jumps **down** each time a new prime power enters (`R = 1.005` just below `log 2`, `R = 0.874` just above) and climbs linearly in `T` between thresholds.

So the hand argument dies for an **analytic** reason (the uncertainty budget `π/(2T)` is dwarfed by the extent `τ_1(T)` of the negative set), not because the `cos(τ log n)` bands stop aligning — the bands never align in the first place: for `T ≥ log 2` the *only* interval where all present bands are simultaneously positive is `(2.266, 4.289)`, and it is already the one positive band adjacent to the origin well. `DIAGNOSTIC` for the growth rates, `PROVED` for `τ_1 ≍ 2πe^{2S_T}` and for `R(T)` at the two endpoints.

---

## 7. (T5) Falsifier check: `Ξ_a`

`σ_T^{(a)}(τ) = Re ψ(¼+a/2+iτ/2) + Re ψ(¼−a/2+iτ/2) − 2logπ − 2Σ_{n<e^{2T}} w_n(n^a+n^{−a})cos(τ log n)`; the four moment conditions give weight `(τ²+(½+a)²)(τ²+(½−a)²)` in place of `(τ²+¼)²`.

At `T = log 2`: `2S^{(0.45)} = 4.910213`, `σ^{(0.45)}(0) = −49.8289` (vs `−7.6210` for `ζ`), `τ_1 = 852.4`, fifteen sign changes, `sup N = 63.318`. Every well is deeper by a factor `≈ 2.4`; the total `‖(σ^{(a)})^-‖` grows accordingly.

**The decisive finding.** `τ_0^{(0.45)}(log 2) = 2.207353`, so `R^{(0.45)}(log 2) = 2T τ_0/π = 0.97406 < 1` — **`Ξ_{0.45}` satisfies the width condition that `ζ` violates** (`R = 1.00500 > 1`), and the four moment zeros suppress the origin *more* than `ζ`'s two (`weight(0) = (0.95)²(0.05)² = 0.00226` vs `ζ`'s `0.0625`). Yet the form is certifiably negative for `Ξ_{0.45}` at `log 2` (R153_005:14) and positive for `ζ`. Therefore:

1. The hand argument fails for `Ξ_a` too — as it must — but it fails **for the same reason and by a similar factor** (`2T·sup N/π = 27.9`), so it does not discriminate. It is a blunt instrument, consistent with the phase-136 meta-theorem.
2. The separation of `ζ` from `Ξ_a` at `({∞,2,3}, log 2)` is **not** a width phenomenon and **not** a moment-zero phenomenon. It is a depth phenomenon: `σ^{(a)}(0)/σ(0) = 6.54` at `a = 0.45`, `2.62` at `a = 0.30`, `2.05` at `a = 0.10`, driven by `n^a+n^{−a} ≥ 2` in every prime weight simultaneously with a *shallower* archimedean well (the two shifted digammas do not compensate). Theorem A's mechanism is the doubled prime weight, not the geometry of `P_T^{(a)}`. This is a genuine sharpening of R153_005's reading and should go to Paper 46 §28.3.

`DIAGNOSTIC-NUMERIC` for the values; `PROVED` for `R^{(0.45)}(log 2) < 1 < R^{(0)}(log 2)` (same two-evaluation argument as Proposition W).

---

## 8. Labels, FATAL rule, open items

| item | label |
|---|---|
| `σ_T` identity with exact normalisations; `g_Γ − m_0 = Re ψ(¼+iτ/2) − log π` | `PROVED` |
| Reduced symbol `ρ_T = (τ²+¼)²σ_T` on unconstrained `L²(I_T)` (§2.2) | `PROVED` |
| Autocorrelation/Krein LP reformulation (§2.3) and the no-soft-minorant corollary | `PROVED` |
| `σ_T > 0` for `|τ| > τ_1(T)`, `τ_1` explicit, monotonicity of `g_Γ` | `PROVED` |
| Lemma U (`θ ≤ 2Tτ_*/π`) and Criterion C | `PROVED` |
| Proposition W: `σ_T(π/(2T)) < 0` at `½log3` and `log 2`; `R(T) > 1` | `PROVED` |
| `R^{(0.45)}(log 2) < 1 < R^{(0)}(log 2)` | `PROVED` |
| well/band tables, `D_T`, `‖σ^-‖_1`, `λ_0(c)`, `T_c = 0.689803` | `DIAGNOSTIC-NUMERIC` |
| mesh-free hand proof of `A_T ≥ 0` at `½log3` or `log 2` | `OPEN`; the uncertainty route is `REFUTED` |
| "the primes pay Gamma's deficit" as a *global* inequality on `P_T` | `RESTATEMENT` of the endpoint theorem, with no independent proof |

**FATAL rule: clean.** No zero-free region, no moment bound, no cancellation imported from known theorems; zeros of `ζ` are not used anywhere. **No sign is claimed for `ζ` beyond `T ≤ log 2`**; §5 proves nothing about `A_T`, it refutes a proof strategy.

**New open items.**
* (P153.14) The multi-interval Slepian problem for `𝒦_{2T}`: a joint bound on `(m_1,…,m_k)` over the wells of `σ_T`. By §2.3 this is equivalent to the compression problem, so it is a reformulation, not a route — record it as such.
* (P153.15) Is `T ↦ R(T) = 2Tτ_0(T)/π` crossing `1` at `T_c = 0.689803` related to the criticality `λ_min ≈ 10⁻⁷` at `log 2`, or is the `0.5 %` agreement a coincidence? Testable: compute `λ_min(A_T|P_T)` at `T = T_c` and check whether the `c(T)` peak of R153_012 (`≈ 93` near `T = 0.689`) sits at `T_c`. **`R153_014:10` already records the peak at `T ≈ 0.689`.** This is the one lead of round 5 worth pursuing.

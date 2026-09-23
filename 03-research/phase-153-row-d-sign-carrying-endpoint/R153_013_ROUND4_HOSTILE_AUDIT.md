# R153.013 — Round 4, hostile audit of `R153_012_ROUND4_DECAY_LAW.md`

*Hostile auditor, round 4 of phase 153. Date 2026-09-19. Model: Claude Opus 5.
Orders: lead, round 4. Everything below was recomputed from `scripts/round4/` and from independent
scripts of my own; no number is taken on the builder's word. Audit scripts: `/tmp/aud{1..8}.py`
(reproduced inline where they matter).*

## 0. Verdict table

| # | Claim (R153_012) | Verdict | Reason |
|---|---|---|---|
| 1 | `λ(T)` table, `K = 160/240/320`, minimiser **even** at every `T ∈ [0.30, log 2]` | **STANDS** | Reproduced to all printed digits at `T = 0.42, 0.5493, 0.62, log 2`, two `K` each; even/odd gap `10²` at `log 2` |
| 2 | "4 Galerkin digits, **2 true digits** of `λ`" via `1/K` Richardson (`λ(log2) ≈ 9.91·10⁻⁸`) | **DOWNGRADE** | `K = 480` added: Richardson(320,480) `= 9.867·10⁻⁸`, a `log K/K` fit gives `9.80·10⁻⁸`. The Richardson constant drifts `1.14 → 1.26 → 1.41·10⁻⁶`, so the `1/K` model is wrong (as §5.2 itself says). True value `≈ 9.8–9.9·10⁻⁸`: **one safe digit, the second uncertain by ±1** |
| 3 | `c(T)` has no plateau, sweeps `5 → 93`, kinks at the two thresholds, terminal fall `92.8 → 75.8` | **STANDS** (mechanism identified) | Reproduced. New: the "terminal fall" is the *same pre-threshold dip* I measure before `½log3` (`c = 49.2 → 40.5 → 34.5` on `T = 0.543 → 0.547 → 0.549`); it is a local threshold feature, not an asymptotic statement. This supports (P153.15) and should be stated there |
| 4 | (P-Slepian) `c → 2γ_1 ≈ 28.3` **REFUTED** | **STANDS** | Independently confirmed; `c` is `75–93` at the right end and *increases* in `T` |
| 5 | "the minimiser annihilates the first **~20 / two dozen** zeros" | **REFUTED as stated** | Per-zero shares at `log 2` (`K = 240/320`): `γ_1 5.7e−7`, `γ_2 1.4e−5`, `γ_3 1.0e−4`, `γ_4 2.5e−3`, `γ_5 7.7e−3`, `γ_6 2.7e−2`, **`γ_7 1.15e−1` (the peak)**. Only `6` zeros lie below `γ = 40` and they carry `3.7 %`. The correct statement is "the first ~5 zeros" |
| 5b | mass share at `γ_1 < 10⁻⁵`; leak at `γ ∈ [40,230]`; `Σ_γ|F̂|²/⟨A_TF,F⟩ = 0.997` | **STANDS** | `5.7·10⁻⁷` at `γ_1`; `90 %` of the mass below `γ = 230` (`96` zeros); `Σ_{600}/λ = 0.9972` (`K=240`), `0.9955` (`K=320`); over the first **500** zeros `0.9956 / 0.9925`. The two computations (Gamma+primes vs zeros) agree to `0.3–0.8 %` |
| 5c | The profile is compatible with the uncertainty principle | **STANDS, and sharpened** (§2 below) | Nyquist/Riemann–von Mangoldt crossover `N(H) = (T/π)H` at `H = 2πe^{2T+1} = 66` for `T = log 2`, against a measured **median of the Weil mass at `γ = 65.1`** |
| 6 | **Theorem 4.1** operator identity `A_T^{(a)} = 2A_T + a²D_T + O(a⁴)`, `D_T = ad_t²(A_T) = −g_T''(D)`, no polar term in the operator | **STANDS / PROVED** | Verified in operator norm: `‖A^{(a)}−2A−a²D‖/a⁴ = 0.1313, 0.1313, 0.1314` at `a = 0.01, 0.03, 0.1` (`T = 0.75`, `K = 120`) — the remainder is **uniform**, which is stronger than the text claims and disposes of the lead's uniformity worry |
| 6b | The *displayed* formula `D_T = −¼Reψ'' + 2Σ Λ(n)n^{−½}(log n)² cos(τ log n)`, and "the prime weights acquire `(log n)²` **with the sign reversed** relative to `A_T`" | **REFUTED — sign error in the text** | That display is `+g_T''`, not `−g_T''`. Correct: `D_T = +¼Reψ''(¼+iτ/2) − 2Σ Λ(n)n^{−½}(log n)²cos(τ log n)`, i.e. `D_T = −g_Γ''(D) − Σ_n w_n(log n)²(S_{log n}+S_{−log n})` — **same sign as in `A_T`**, not reversed. Confirmed three ways (Taylor of `cosh(aL)`, my operator-norm test above, and the code itself: `core.gsym(order=2)` returns `g''` and `second.qD` returns `−⟨g''⟩`). **The code is right; only the prose is wrong.** No numerical consequence |
| 7 | `P_T^{(2)}` = codim-4 space, `= lim_{a→0}P_T^{(a)}` | **STANDS** (with a required statement) | The four moments are `∫Fe^{±t/2}=∫tFe^{±t/2}=0`; `span{e^{(±½±a)t}}` = `span{e^{±t/2}cosh at, e^{±t/2}sinh(at)/a} → span{e^{±t/2}, te^{±t/2}}`, four independent limits. In a parity block these collapse to **two** rows, which is exactly what `core.lam_min(codim=4)` imposes (`mom(0.5)`, `dmom(0.5)`) — correct, but the doc never says why only `β = +½` appears in the code |
| 8 | `μ/λ ≈ 5·10³` at `T = 0.69` | **STANDS** | `μ = 7.327e−4`, `λ = 1.368e−7`, ratio `5356` |
| 9 | `2μ(T*) + a²q_D(T*) = 0` reproduces `T*(a)` | **STANDS** | My own root-finding at `a = 0.005`: `T*` exact `= 0.76943`, `T*` 2nd-order `= 0.76943`, residual `1.17e−9`; matches R153_003's `K=160` value `0.76974` |
| 9b | The application of Thm 4.1 to the **moving** constraint is legitimate | **DOWNGRADE to `DIAGNOSTIC`** | `P_T^{(a)} = P_T^{(2)} + a²·span{t²e^{±t/2}, t³e^{±t/2}} + O(a⁴)`: the constraint space itself moves at order `a²`, the *same* order as `a²q_D`. The doc silently drops that contribution. Empirically it is `≤ 5·10⁻⁴` of `a²q_D`, but this is **observed, not proved**. (Good news: the space is even in `a`, so there is no `O(a)` term — worth recording) |
| 10 | `c_μ ≈ 79.3` on `[0.69,0.81]`, predicted slope `2/(c_μ + dlog|q_D|/dT) = 0.0262` vs fitted `0.0268`, "agreement to 2 %", **`c ≈ 75` CONFIRMED** | **RESTATEMENT + DOWNGRADE** | Two mismatched averages. (i) `c_μ` is *not* constant: pointwise `55.7, 63.2, 68.3, 74.6, 81.2, 87.1, 88.9, 86.0, 76.9, 73.1, 96.6, 99.8` on `[0.69,0.81]` — a `1.8×` sweep, i.e. `μ` has no plateau either, exactly the criticism §2 makes of `λ`. (ii) The `T*(a)` data used for `0.0268` span `a ∈ [10⁻³,10⁻¹]`, i.e. `T* ∈ [0.685,0.808]`, and the relation is **curved**: local slope `0.0240` on `a ∈ [10⁻³,10⁻²]` and `0.0296` on `[10⁻²,10⁻¹]`. The honest test is local: on `T ∈ [0.769,0.808]` I get `c_μ = 86.6`, predicted slope `2/(86.6−2.9) = 0.0239` against a measured local slope `0.0241` — **agreement to 1 %, with different numbers than the doc's**. So: the *mechanism* (`T*` is the level set of `μ`, slope `= 2/(c_μ + dlog|q_D|/dT)`) is **CONFIRMED**; the *constant* `75` is **not** — it is a chord of a rate that runs `56 → 100` |
| 11 | The window `[0.69,0.81]` includes the `n = 4` contact | **STANDS** | `core.contacts` is built from all prime powers; `n = 4` enters for `T > log 2`, `n = 5` for `T > ½log5 = 0.8047`. The lead's worry is unfounded — but the window **straddles two thresholds**, which is part of why the chord average is meaningless (item 10) |
| 12 | **SIGN**: the rate sum at `log 2` is `+8.08e−6` and contradicts `dλ/dT < 0` | **NO ERROR — the lead's premise is a misreading** | `R153_012` line 220 reads `−8.08309e−6` (negative). `−1.447046 + 1.875819 − 0.428780 = −7e−6`; my rerun of `rate.py` gives `SUM = −8.083094e−06`, finite difference `−8.083735e−06`, and `c = −(dλ/dT)/λ = 8.083e−6/1.0438e−7 = 77.44 > 0`. Signs, convention and magnitude (`−c·λ`) are all consistent |
| 13 | Rate formula verified "to 4–5 digits" | **DOWNGRADE (cosmetic)** | My independent finite differences at `T = 0.65`, `h = 10⁻³/10⁻⁴/10⁻⁵`, `K = 240` and `320`: relative agreement `1.4–4.2·10⁻⁴`, i.e. **3–4 digits**, `K`-stable (`c_HF = 67.850` at `K=240`, `67.917` at `K=320`). Also note the check is Hellmann–Feynman *for the Galerkin matrix* against a finite difference of the *same* Galerkin matrix — it validates the term decomposition, not the continuum limit |
| 14 | "**No term-by-term bound on `c(T)` can exist**" | **RESTATEMENT (observed, not proved)** | What is established: at four values of `T` the `O(1)` archimedean and transport terms cancel to `5–6` digits. As a general impossibility it is not proved. The doc's own label (`DIAGNOSTIC-NUMERIC`) is right; the **bold prose in §5.1 overstates it** and must be reworded to "no term-by-term bound can be expected / any such bound loses `10⁵` at the `T` tested" |
| 15 | `F_T(±T) = 0`, `α = 1.250` (`T=0.60`) / `2.163` (`log 2`), "no jump, `|A|/‖F‖_∞ < 5·10⁻⁴`" | **DOWNGRADE / partly REFUTED** | The `<5·10⁻⁴` figure is quoted from `T = log 2` only. At **`T = 0.60`** the same test gives `A ≈ −0.019`, `K`-stable at `K = 160/240/320/480` (means `−0.0190, −0.0193, −0.0190, −0.0188`), i.e. `|A|/F(0) = 1.1 %` — **23× the quoted bound, and it does not shrink with `K`**. `α` is measured on `h ∈ [0.04,0.20]`, whereas the `K`-stable profile at `T=0.60` reads `F(−T+h) = −0.075, −0.047, −0.033` at `h = 0.02, 0.01, 0.005` — local exponent `0.68, 0.51`, falling, not `1.25`. **`α ≈ 1.25` is a fit outside the boundary layer**; the endpoint value is small but not demonstrably zero |
| 16 | "Therefore D.133's rank-two endpoint form vanishes at the minimiser" | **REFUTED (quantitatively)** | The scale that matters is `λ`, not `‖F‖_∞`. With `F` unit-normalised in `L²` and `A = F(±T)`, D.133 (0.1) contributes `−(4w_N/T)A²`. At `T = log 2` (`N = 4`, `w_4 = ½log2`), `A ≈ −7·10⁻⁴` gives `≈ −9.8·10⁻⁷` — **`9×` the value of `λ = 1.04·10⁻⁷` and `12 %` of `dλ/dT`**. At `T = 0.60` with `A ≈ −0.019` it is `−9·10⁻⁴`, `22 %` of `dλ/dT`. The endpoint term is *small in the trace norm and large on the scale of the eigenvalue*. §5.2's conclusion must be withdrawn |
| 17 | `α` is `T`-dependent (`1.25 → 2.16`) | **Lead's suspicion upheld: fitting artefact** | The two fits are taken at a fixed `h`-window while the layer scale `1/Ω_eff` moves with `T`; the local exponents are non-monotone at both `T` (`0.84→1.39→1.18` and `2.14→2.33→1.81`). (P153.13) should be promoted from "is it really `T`-dependent?" to "the measurement does not resolve the layer; `α` as reported is a window artefact" |
| 18 | Corpus-check line "`grep -rIl \"Slepian\"` → 5 files" | **REFUTED (materially incomplete)** | The same grep returns `≥ 18` files, including **`phase-106/106_24_PSWF_ENDPOINT_AND_H1_LEAKAGE.md`** (exact PSWF *endpoint* identities and the exterior `H¹` budget — directly on both §3 and §5.2), `106_26`, `phase-115/115_11`, `phase-29/02-convergence.md`, `phase-32-ccm/65-ppp-recurrencia-prolate.md`, and two planning files. `259` markdown files in `03-research` mention prolate/PSWF. The `"boundary exponent"` grep line is accurate |
| 19 | FATAL rule: zeros diagnostic only; no sign for `ζ` beyond `log 2` | **STANDS** | Verified: Theorem 4.1 and the rate formula use no zero data; `§3` is the only zero-consuming section and nothing depends on it. `μ(T) > 0` for `T ∈ (log 2, 0.86]` is not positivity of `A_T` since `P_T^{(2)} ⊊ P_T` and `μ ≥ λ` — the doc should say this in one explicit sentence rather than leaving it to the reader |
| 20 | (new, mine) The two Tate constraints are **nearly inactive** at the minimiser | **NEW FINDING** | At `T = log 2`, `K = 240`: the unconstrained even block has spectrum `−2.831, 1.0437817e−7, 2.145e−3, …` and the constrained minimum is `1.0437817e−7` — **the same number to 8 digits**. The constrained ground state is (to that precision) the *second unconstrained eigenvector*: the Lagrange multipliers essentially vanish. This is the structural reason the "Tate drift" term of §5.1 is `10⁻⁹`, and it means `λ(T) = λ_2(A_T|even)` with one negative direction removed. It deserves a line in the record |

## 1. Item 5 (the lead's first priority): the sign in the rate formula

There is **no sign error**. The lead's premise — "the builder reports `+8.08e−6`" — is a misreading of
R153_012's table, which prints `−8.08309e−6`. Rerun of `rate.py` (verbatim), `K = 240`:

```
T=0.6931 lam=1.043782e-07 (even)
    Gamma            -1.447046e+00
    transport n=2     1.875819e+00
    transport n=3    -4.287804e-01
    Tate drift       -4.105632e-09
    SUM              -8.083094e-06   finite-diff -8.083735e-06   c_HF=77.440
```

`dλ/dT < 0`, `c = −(dλ/dT)/λ = +77.44`, and `−c·λ = −8.08·10⁻⁶` exactly as the lead's own consistency
check demands. There is no dilated variable, no derivative of `−λ` or of `λ·T`: the convention is the plain
one. My own finite differences at `T = 0.65` (three step sizes, two `K`) agree with the Hellmann–Feynman sum
to `1.4–4.2·10⁻⁴` relative — three to four digits, not the claimed four to five.

Correspondence with D.133 is as the builder states and I confirm by inspection: the first integral splits into
D.133 item (1) (Gamma shape derivative) and item (2) (one transport derivative per earlier contact), the
multiplier term is item (4), and item (3) — the rank-two endpoint form — is genuinely absent *between*
thresholds because the contact set is locally constant there. What is **not** justified is the further claim
that item (3) also vanishes *at* a threshold because `F_T(±T) = 0`: see §3.

## 2. Item 2: the zero profile — the claim STANDS, with one wrong number and a mechanism

`Σ_{γ ≤ 600}|F̂(½+iγ)|²/⟨A_TF,F⟩ = 0.9972` (`K=240`) and `0.9955` (`K=320`); over the first 500 zeros,
`0.9956` and `0.9925`. So the builder's `0.997` is reproduced, and the explicit formula is verified to better
than `1 %` by two computations that share no input (`Gamma + primes` on one side, zero ordinates on the other).
Mass share at `γ_1` is `5.7·10⁻⁷ < 10⁻⁵`: that part of the claim stands.

The **"first ~20 zeros are annihilated" is false**. The shares at `log 2` are
`γ_1 … γ_7 = 5.7e−7, 1.4e−5, 1.0e−4, 2.5e−3, 7.7e−3, 2.7e−2, 1.15e−1`: the mass is already `2.7 %` at `γ_6`
and **peaks at `γ_7 = 40.9`**. Six zeros lie below `γ = 40`, carrying `3.7 %` in total; `90 %` of the mass lies
below `γ = 230`, where there are `96` zeros. "The first ~5 zeros" is the defensible statement.

*Is it plausible at all, for an `F` supported in `[−log 2, log 2]`?* **Yes, and the numbers say why.** `F̂` is
entire of exponential type `T = 0.693`; the number of degrees of freedom such a function has on a frequency
interval `[0,H]` is the Nyquist count `(T/π)H`, while the number of constraints it must fight is the
Riemann–von Mangoldt count `N(H) = (H/2π)(log(H/2π) − 1)`. Annihilation is affordable exactly while
`N(H) < (T/π)H`, i.e. while `log(H/2π) < 2T + 1`, that is up to

  `H_* = 2π e^{2T+1} = 66.0` at `T = log 2`.

The measured **median of the Weil mass is `γ = 65.1`**. Above `H_*` the zeros outnumber the available nulls and
the function must leak; the leak then dies off only because `F̂` itself decays, which puts the `90 %` point at
`γ ≈ 230` and the `99 %` point at `γ ≈ 592`. The same formula gives `H_* = 57` at `T = 0.60` (median `48`) and
`H_* = 42` at `T = 0.45` (median `25`) — the right magnitude and the right monotonicity at every `T` sampled.
So there is no conflict with the uncertainty principle: the minimiser is not concentrated in the origin gap, it
is a *near-interpolating* function that spends its Nyquist budget on the low ordinates. This strengthens §3's
verdict and makes (P153.12) precise: the correct asymptotic object is the density crossing
`N(H) = TH/π`, and `Ω_eff(T) ≍ 2πe^{2T+1}`, not `γ_1`. (Note that this predicts `Ω_eff` growing *exponentially*
in `T`, whereas §3 asserts `Ω_eff ≈ c(T)/2 ≈ 38–46`; the two readings disagree and the doc should not assert
`Ω_eff = c/2` as if established.)

## 3. Item 6/15/16: the boundary — the weakest section of round 4

Reproduced `boundary.py` exactly, then extended it to `K = 480` and to `h` down to `5·10⁻⁴`:

```
T=0.60   K=160/240/320/480   jump est (mean, k>K/4) = -0.0190 -0.0193 -0.0190 -0.0188   F(0)=1.657
T=log2   K=160/240/320/480   jump est                = -0.00049 -0.00065 -0.00070 -0.00073  F(0)=1.694
```

The quoted bound `|A|/‖F‖_∞ < 5·10⁻⁴` is the `log 2` number only; at `T = 0.60` the same estimator gives
`1.1 %`, stable under a `3×` refinement of `K`. And at `log 2` the estimator is **growing** with `K`
(`4.9 → 7.3·10⁻⁴`), not shrinking. The `K`-stable part of the profile at `T = 0.60`
(`F(−T+h) = −0.075, −0.047, −0.033` at `h = 0.02, 0.01, 0.005`) has local exponent `0.68` then `0.51`, while
the reported `α = 1.250` comes from `h ∈ [0.04, 0.20]`, i.e. from *outside* the layer. Conclusion: the data
support `|F_T(±T)|` small, they do not support `F_T(±T) = 0`, and they do not determine `α`.

That matters because §5.2 draws a structural conclusion from `F_T(±T) = 0`. On the scale that the conclusion
lives on — `λ`, not `‖F‖_∞` — the endpoint term is **not** negligible: `−(4w_N/T)F(T)²` is `−9.8·10⁻⁷` at
`T = log 2` against `λ = 1.04·10⁻⁷` and `dλ/dT = −8.1·10⁻⁶`. The sentence "D.133's rank-two endpoint form
vanishes at the minimiser" must be withdrawn; the honest statement is that it is `O(10 λ)` and of the same
order as the other terms' residual, so D.133's obstruction is untouched **and is not even numerically small**
at the minimiser. (The doc's own item 13 — "D.133 is not bypassed" — survives; it is item 12 that fails.)

## 4. Required repairs

1. **Fix the sign in Theorem 4.1's display** (item 6b). `D_T = +¼Reψ''(¼+iτ/2) − 2Σ_n Λ(n)n^{−½}(log n)²cos(τ log n)`,
   operator form `−g_Γ''(D) − Σ_n w_n(log n)²(S_{log n}+S_{−log n})`, and **delete "with the sign reversed"**:
   the `(log n)²`-weighted primes enter with the *same* sign as in `A_T`. State instead the true reason
   `q_D < 0`: both the reweighted primes and `−g_Γ''` push the same way, the primes dominating.
2. **Add the uniformity statement that is actually true and easy**: `‖A^{(a)} − 2A_T − a²D_T‖ ≤ Ca⁴`
   uniformly for `|a| ≤ a_0 < ½` (Cauchy estimates on the symbol, analytic in `|Im| < ½`; numerically
   `C ≈ 0.13`). Then **separate** the legitimate step (operator expansion on `L²(−T,T)`) from the step that is
   not proved (`min` over the *moving* `P_T^{(a)}` vs `min` over `P_T^{(2)}`), record that `P_T^{(a)}` is even
   in `a` so there is no `O(a)` term, and label the `a²` constraint-motion contribution `OPEN` with the
   measured bound `≤ 5·10⁻⁴ · a²|q_D|`.
3. **Relabel item 8**: `c ≈ 75` is a chord, not a rate. Replace with: "`c_μ(T)` runs `56 → 100` on `[0.69,0.81]`;
   the local relation `dT*/dlog(1/a) = 2/(c_μ + dlog|q_D|/dT)` is confirmed to `1 %` when the `T`-window is
   matched to the `a`-range (`c_μ = 86.6` and slope `0.0239` vs measured `0.0241` for `a ≤ 5·10⁻³`)."
   Note that `T*(a)` vs `log(1/a)` is curved, so R153_003's single fitted `0.0268` should itself be downgraded.
4. **Correct "~20 zeros" to "~5 zeros"**, give the per-zero table out to `γ_7`, and replace the assertion
   `Ω_eff ≈ c/2` with the Nyquist-crossing `H_* = 2πe^{2T+1}` which actually matches the measured medians.
5. **Withdraw** "the rank-two endpoint form vanishes at the minimiser" and restate §5.2 as: `|F_T(±T)| ≲ 10⁻²`
   at `T = 0.60`, `≲ 10⁻³` at `log 2`, boundary exponent unresolved, endpoint term `O(10λ)`.
6. **Soften** "no term-by-term bound can exist" to the observed statement; keep the `10⁵` number, drop the
   impossibility claim.
7. **Redo the corpus line for "Slepian"** and read `106_24_PSWF_ENDPOINT_AND_H1_LEAKAGE.md` before any further
   work on the boundary exponent or the multi-null extremal problem.
8. **Weaken the precision claim** for `λ` to one safe digit (two at `log 2` only if `K = 480` is quoted), and
   add the `K = 480` row; `c(T)` at three digits stands.
9. Add the near-inactivity of the Tate constraints (item 20) to the record — it is a free structural fact and
   it explains §5.1's `10⁻⁹` drift term.

## 5. Honest reading of round 4

Round 4 did not find a decay law; it destroyed the two candidate laws and replaced them with a mechanism.
`λ(T)` on `[0.30, log 2]` is not an exponential — its logarithmic derivative sweeps a factor of nearly twenty,
dips before each prime-power threshold and jumps after it — so "the sign decays at rate `c`" is not a
well-posed statement on this window, and the two rates the corpus had been carrying (`2γ_1 ≈ 28` from a
Slepian origin-gap picture, `≈ 75` from the `Ξ_a` threshold fit) are respectively wrong and a chord of a
non-constant rate `c_μ` on a *different*, codimension-four space. What survives as real gain is threefold: an
exact and uniform second-order operator identity `A_T^{(a)} = 2A_T + a²D_T` with `D_T = −g_T''(D)` (a genuine
new object, whose displayed sign the builder got wrong while the code got it right), which reduces the entire
`Ξ_a` threshold phenomenon to the level sets of one eigenvalue; a prime-computable, zero-free, four-digit-exact
formula for `dλ/dT` whose terms are `O(1)` and cancel to five or six digits, which converts D.133's qualitative
"no signed induction" into a quantitative "any term-by-term estimate loses `10⁵`"; and a mechanism for the
minimiser that is now quantitative — it is not a gap-concentrated function but a near-interpolating one that
spends its Nyquist budget `(T/π)H` against the zero count `N(H)` and starts leaking exactly at
`H_* = 2πe^{2T+1}`, which matches the measured median of the Weil mass at every `T` sampled. Against that, the
boundary section does not survive contact: the endpoint value is only small, not zero, it is twenty times
larger at `T = 0.60` than the single number the doc quotes, the exponent `α` is measured outside the layer it
claims to describe, and the structural conclusion drawn from it — that D.133's rank-two term drops out — is
false by an order of magnitude on the only scale that matters. Round 4 is therefore a genuine advance on the
*mechanism* of the decay and a negative result on its *law*, and its one PROVED theorem needs a sign corrected
and a domain-degeneration argument supplied before it can be quoted.

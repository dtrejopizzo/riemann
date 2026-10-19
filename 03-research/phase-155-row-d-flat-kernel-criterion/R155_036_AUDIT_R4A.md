# R155.036 — Audit of R155_032 (round 4a: even-sector Schur / nested enclosures at `log 2`)

*Reruns: `r4a_02_nested_enclosure.py` at `R4A_PANELS=5000 R4A_KMAX=5` (48.6 s, exit 0) and at `16000/k≤7` (97.5 s, to restore the archive this audit overwrote);
`r4a_01_structure.py` not rerun (its JSON audited entry by entry, every printed number recomputed).
Verdict: **the mathematics and the enclosures stand**; the withdrawal in §4/§6 is correct and
mandatory; four defects, all in prose/bookkeeping, one of them a numeric contradiction (§6 `det`).*

## §1 Verdicts

| item | verdict |
|---|---|
| **Prop. 4a.2** polarisation `W(e_i,e_j)=¼(W[e_i+e_j]−W[e_i−e_j])` | **CORRECT**, `PROVED`. `W_T` (with the pole term) is an exact quadratic form of `F`: `A`,`B` are linear functionals, so `2A(F)B(F)` is quadratic and polarisation is exact, not approximate. `P_T` is a linear subspace, so `e_i±e_j∈P_T` whenever the `e_i` are; and the code does **not** rely on that — `r4a_lib.py:W` pays the pole defect `±2\|A\|\|B\|` for every quadratic value, exactly as `r3c_04_enclosure_iv.py:264-267`, with `A,B` themselves enclosed by the interval series `moments()`. Tolerance: the archived vectors have `A,B ~ 10⁻¹⁵` (`b_odd_components ≤ 9.2e−16`, `b_eq_PiF_relerr 4.5e−15`), so the paid-for pole interval is `~10⁻³⁰` — five orders below the panel widths. **No hidden `P_T` assumption.** |
| the "false for cross-correlations" motivation | **CORRECT**. `c_G(0)−c_G(u)≥0` is Cauchy–Schwarz for an autocorrelation and genuinely fails for `c_{F,G}`; polarisation is the right and cheapest fix. |
| **`L_lo`,`L_hi` linearity and direction** | **CORRECT** (`r4a_lib.py:_panels`, `:W`). `L_•[k]=∫K_•(s)s^k ds` over the `M` panels, `⟨L_•,G⟩=∫K_•(s)G(s)ds`; `K_lo≤K≤K_hi` pointwise (tangent-below/chord-above for the convex `1/sinh` part, chord-below/tangent-above for the concave `1/cosh` part) and `G≥0` **pointwise** ⇒ lower bound from `L_lo`, upper from `L_hi`. The code does exactly this (`lo += L_lo[k]*G[k]`, `hi += L_hi[k]*G[k]`). Signs of the *coefficients* `G[k]` are irrelevant; only `G(s)≥0` is used, and only quadratic values are ever passed. `G[0]=0` with `c(0)` carried separately by `C0*c0 + c0*Ktail` ✓. Singular end `[0,δ]` added one-sidedly to `hi` only ✓. |
| **Prop. 4a.3** interval Cholesky + bisection | **CORRECT**, standard (Alefeld–Herzberger/Rump). `cholesky_pd` is a genuine interval factorisation with the pivot test `s.a>0`; success ⇒ every real symmetric matrix in the hull is `≻μI`. Bisection bracket `[0,0.1]` is safe for all reported values. Nit: `lam_min_lower` returns the bisection left endpoint (a float), used as the certified bound — it is a member of the tested set, so sound. |
| Rayleigh transfer to `‖F‖²` | **SOUND but not computed**. The docstring promises `λ_min(M)/λ_max(Gram)`; the code only prints `max\|Gram−I\| ≤ 1.07e−15` (reproduced exactly). At that deviation the correction is `<10⁻¹⁴` relative, far below the `10⁻⁶` widths, so Thm 4a.B's `‖F‖²` form is safe — but the note should say "Gram deviation bounded, transfer negligible", which §3 does. |
| **Thm 4a.1** `b=P_VΠ_TF*` | **CORRECT**, two lines, `PROVED`. Numerical check `4.54e−15` reproduced. |
| **Prop. 4a.4** `Π_T=−Σv_n Re(R_Tτ_{log n}R_T)`, partial isometries, non-compact | **CORRECT**; the non-compactness proof is **sketchy for `#contacts≥2`**. `R_Tτ_aR_T` is isometric exactly on `L²(−T,T−a)` and kills `L²(T−a,T)` ✓; defects infinite-dimensional for `0<a<2T` ✓; `‖Π_T‖≤A_T=2.24883` ✓ (reproduced). The clean argument the note should give instead of "the two ranges are not annihilating": on `f` supported in `(−T,−T+a₀)` with `a₀=min log n`, every `R_Tτ_{−log n}R_T f=0`, so `Π_T f=−½Σ_{n}v_nτ_{log n}f` restricted — in particular for a single dominant support window the operator acts as a fixed non-zero multiple of an isometry on an infinite-dimensional subspace ⇒ non-compact. **Claim true, proof to be rewritten.** |
| **Prop. 4a.5** `\|π_ij\|≤A_T`, `Σ_jπ_ij²≤A_T²` | **CORRECT** (Cauchy–Schwarz + Bessel), `PROVED`. |
| interior analyticity / endpoint singularity | **CONDITIONAL**, correctly labelled; the "REFUTED as stated" for `\|i−j\|`-decay is `DIAGNOSTIC` evidence and is labelled as such ✓. |
| Theorem C `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` | **UNAFFECTED — confirmed.** It is a certified *lower* bound from interval arithmetic on a different window and a different (archimedean) form; no Galerkin eigenvalue enters it. The withdrawal touches only Galerkin *upper* bounds. |
| Labels §6 | **Correct**, with the one numeric error below. |

## §2 Reproductions

**`r4a_02` rerun, `M=5000`, `k≤5`, `T=log2` (48.6 s, README claims 49.6 s ✓):**
certified `λ_min ≥ 3.421021e−2, 2.109142e−3, 3.997996e−4, 8.237932e−5, 2.460003e−5`, all `PD`,
entry widths `1.03e−5 … 4.44e−5`, `max\|Gram−I\| = 1.07e−15`. These are **weaker than** and
**consistent with** the `M=16000` table of §0 (`3.421189e−2, 2.113566e−3, 4.045259e−4, 9.076318e−5,
4.095108e−5`): same float midpoints, widths shrinking with `M`, so the §0 table is credible and the
method converges as claimed. **The `M=16000, k≤7` run was then regenerated (97.5 s here) and reproduces the §0 table to every printed digit** — `3.421189e−2, 2.113566e−3, 4.045259e−4, 9.076318e−5, 4.095108e−5, 2.215585e−5, 6.568676e−6`, widths `5.3e−6 … 4.68e−5`. §0 is fully reproduced. `k=1`: `3.421189e−2 ∈ [0.0341712660, 0.0342537492]` = the `thm:w11`
interval, and strictly tighter ✓; `w₁₁ ∈ [0.0342119,0.0342172]` of Thm 4a.A is likewise inside it ✓.
`det` at `M=5000`: `[2.0962e−4, 2.1213e−4]` ⊃ the §3 claim `[2.1005e−4, 2.1151e−4]` ✓.

**`r4a_01.json`, all of §2 and §4 recomputed:** `λ`-labels, the full `8×8` `π_ij` table (every entry
to the printed 4 decimals), `shift_2+shift_3 = PiE` to `1.4e−16`, `v₂=0.98026`, `v₃=1.26857`,
`w₁₁=0.03421218`, `‖b‖=0.16316`, odd components `≤9.2e−16`, `A_T=2.248826`, both trend rows
(`N=18` `k=1…8`; `N=36` `k=1…17`) **exact to every printed digit**, odd sector `3.232e−5`/`1.119e−5` ✓.
Structure numbers of item 5 of the order: `π₁₃ = +0.1867 − 0.1410 = +0.04573` ✓;
`det` with the `log 2` atom alone `= 0.03421·(0.46817−0.40089) − 0.1867² = −0.0326` ✓ ("−0.033");
`π₃₃=−0.4009` against `λ₃=0.46817`, `(3,3)` entry of `W` `= 0.06728` ✓.

## §3 Errors (file:line)

1. **`R155_032:317` — numeric contradiction.** §6 labels row for Thm 4a.A prints `det ≥ 2.136·10⁻⁴`,
 which is **above the upper end** of the enclosure stated at `R155_032:197` (`[2.1005e−4,
 2.1151e−4]`) and above the float value `2.1043e−4`. Fix to `det ≥ 2.10·10⁻⁴`.
2. **`R155_032:123-125` — "`67 %` of `‖b‖`", "`e₃` carries only `8 %`".** These are fractions of
 **mass** (`b₇²/‖b‖²=0.6724`, `b₃²/‖b‖²=0.0786`); as a fraction of the norm `b₇/‖b‖ = 0.820`.
 Same defect R155_028 §3.1 flagged in R155_026. Write "`67 %` of the mass".
3. **`R155_032:289-290` — row norms misprinted.** Recomputed from `PiE` (`N=18`, `log 2`):
 `0.249, 0.446, 0.821, 0.623, 0.427, 0.544, 0.377, 0.141`; the note prints
 `0.25, 0.42, 0.81, 0.62, 0.39, 0.50, 0.37, 0.11`. Four entries wrong in the second digit
 (source unclear — not the `N=36` or `0.62`/`0.65` rows either). Claim (all `≪ A_T`, no decay)
 unaffected.
4. **`R155_032:35-36, :320` — "`k=8` … will not be by this method" is overstated.** What is shown is
 that at `M=16000` the entry widths (`4.7e−5`) are `47×` the float bottom (`9.94e−7`), and widths
 fall only slowly with `M` (`1.03e−5→5.3e−6` for `M:5000→16000`, i.e. `~M^{−0.55}` empirically), so
 `k=8` is out of reach **at feasible panel counts** with this sandwich. It is not proved impossible,
 and (worse for the claim) the `N=18` `k=8` float value is itself a polluted top-mode number, so it
 is not even the right target. Restate as "not achievable at feasible cost; and not the right
 target, by §4".
5. Minor: `R155_032:36` "an order below the entry widths" — it is `1.6` orders (`47×`).
6. Minor: `r4a_02_nested_enclosure.py` writes `r4a_02_<T>.json` unconditionally, so **any rerun at a
 different `PANELS/KMAX` silently overwrites the archived certificate**. This audit's `M=5000` run
 did exactly that; the `M=16000, k≤7` file has been regenerated. Fix: key the output filename by
 `(T, panels, kmax)`, or refuse to overwrite. Until then the archived JSON is not a stable record.

## §4 The withdrawal (order item 6): **correct, and mandatory**

The data are as printed. Two readings must be separated:

- It is **not** "spectral pollution" in the technical sense. `W_T|P_T` is bounded below and the `E_k`
 are nested, so Rayleigh–Ritz gives *legitimate monotone upper bounds* on the infimum; no spurious
 eigenvalue can appear. The `k=dim` drop is the honest statement that **the minimiser is not in the
 span of the low modes** — an edge/endpoint-singularity effect (the note's §5 diagnosis), i.e. the
 approximation is *unconverged*, not wrong.
- The decisive fact is the **`N`-inconsistency at fixed dimension**: `k=8` gives `9.94e−7` at `N=18`
 and `3.38e−5` at `N=36` — a factor `34` for the same subspace dimension, because the bases differ;
 and the bottom falls `9.94e−7 → 1.05e−7` from `N=18` to `N=36`. A sequence of upper bounds that has
 not stabilised supports **no** value, and is compatible with a positive tiny infimum *and* with a
 negative one. **§4.3's conclusion is right, and §6's "withdrawn as unsupported" is the correct
 label.** This is the most valuable output of round 4a.

**Every place in the record that must now carry the caveat** (all are Galerkin *upper* bounds at
`log 2`, and the first of them is literally the same number `9.9416e−7`):

| file:line | what |
|---|---|
| `R155_023:152` | `λ_min(A_T\|P_T)(log2) = +9.9416·10⁻⁷` (and `r3a_04`'s `9.96·10⁻⁷`) — **identical to the `N=18` `k=8` top-mode value**; unconverged |
| `R155_023:161` table, column `λ_min(a_T\|P_T)` / `λ_min(W_T)`, and `:204` table | all `log 2` entries |
| `R155_023:218, :323, :336` | the "`10³`/`10⁶`" gap statements rest on it |
| `R155_026:167` (`λ_min(W_T\|P_T) = +9.942e−06`… row) and `:159` table header | the `log 2` column |
| `R155_026:38-39` | the ratios `λ_min(S)/λ_min(W_T\|P_T) = 6.5, 4.2, 3.4, 2.7` — **both numerator and denominator are unconverged**; the *sign agreement* survives, the *ratios* do not |
| `R155_026:174, :176, :335, :338, :361` | "the bottom of `W_T` is nowhere near `F*`", `λ_min(S)=2.6·10⁻⁶` |
| `R155_029` | wherever the `10⁻⁶`–`10⁻⁷` bottom is quoted as a target margin |
| `main.tex:2258` | "the Galerkin bottom `λ_A(log2) ≈ 10⁻⁷`" — **must not be printed as a number** |
| `main.tex:2262-2263` | "`w₁₁` … `10³`–`10⁵` times `λ_min(W_T\|P_T)`" — the ratio is unsupported; keep only "orders of magnitude above, by an unconverged Galerkin estimate" |

`R155_026:176` already observed that these values "lose an order between `N=18` and `N=36`"; round 4a
converts that observation into a withdrawal. **Theorem C is untouched** (certified lower bound).

## §5 Readiness for Paper 47 (§7 proposals)

1. **Thms 4a.A/4a.B → `§8` new subsection: READY**, subject to §3.1 (`det`) and to publishing the
 `M=16000` run under a filename that cannot be overwritten. Permissible wording:
 > *For the seven explicit degree-17 polynomials on `(−\log2,\log2)` archived in
 > `scripts/r4a/r4a_01.json`, an interval-arithmetic enclosure of every entry of the matrix of the
 > complete Weil form (polarisation; only quadratic values are enclosed) together with a verified
 > interval Cholesky factorisation gives `W_{\log2}[F] \ge 6.56\cdot10^{-6}\|F\|^2` for every `F` in
 > their span, and `\ge 2.11\cdot10^{-3}\|F\|^2` on the 2-plane `\mathrm{span}\{F^*,e_3\}`, where the
 > positivity of the `2\times2` determinant `2.10\cdot10^{-4}` is a `76\%` cancellation between the
 > atoms at `2` and at `3`. This is positivity on an explicit finite-dimensional subspace; it is not
 > a positivity statement for `W_{\log2}`, and it does not affect the endpoint of record.*
 Do **not** write "the first `k` modes", "the low modes" or anything suggesting exhaustion: §4 shows
 the bottom sits on the top mode.
2. **Thm 4a.1 as a displayed remark: READY** (two lines, correct, sharpens `prop:schur`).
3. **Prop. 4a.4: READY after the non-compactness proof is rewritten** as in §1.
4. **The cautionary sentence: REQUIRED, not optional**, and it must be paired with the deletions at
 `main.tex:2258` and `:2262-2263`. Permissible wording:
 > *The Galerkin bottom of `W_{\log2}` on `\PT` is carried by the highest mode of each truncation and
 > falls by an order between `N=18` and `N=36`; these are upper bounds that have not stabilised, and
 > no numerical value of `\inf W_{\log2}|_{\PT}` is quoted here.*

## §6 Readiness

`R155_032` is **accepted** after the four fixes of §3 (1–4) and the script fix (§3.6). No sign for
`ζ`; endpoint of record unchanged (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`, Paper 47 Thm C, confirmed
unaffected). The round's real deliverable is not `k=7`; it is the withdrawal of §4 plus Thm 4a.1.

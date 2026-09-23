# R155.017 — Hostile audit of R155_013 (decay tail lemma) and of the amended R155_011

*Hostile auditor, phase 155, 2026-09-21. Targets: `R155_013_DECAY_TAIL_LEMMA.md`,
`R155_011_D_FOR_1000_ZEROS.md` [amended], `scripts/reverse/d1000/{amend,dense,p3}.py` + JSON.
Reference: Paper 47 `main.tex` §4 (`lem:mbounds` 622-640, `lem:F1` 647, `lem:gbounds` 443-451,
`lem:T` 686-700), §7 (Thm Z, 1036-1062), §8 (`prop:env` 985-999).
All reruns single-process, < 60 s.*

**Bottom line: Theorem D, Cor. D.2 and Cor. D.3 are correct as stated and the bookkeeping of §1.1
is right — the `2ĝ₀` regrouping is forced and the builder is right that a naive `ν̂_w` statement is
false. Every number in §4 and §6 reproduces from the JSON. The builder wins both halves of the §5
dispute with `R155_012` (the `E₂` factor 2 and the Bernstein pad). Four defects, none fatal: a
malformed display in Cor. D.2, an unstated truncation in `D_K`, an undeclared `w < 0` violation in
P3, and a `B₂` that is computed from the 1000-zero model and then used to pad the prime side.
The §6 verdict must be made explicitly conditional on the unrun comb-free experiment.**

---

## §1 Verdict table

| # | item | verdict |
|---|---|---|
| 1 | Theorem D (i)–(iii), lower bound, monotonicity, `§1.1` regrouping | **CONFIRMED / PROVED** |
| 2 | atomic part, sign and factor conventions vs `eq:fw` | **CONFIRMED** |
| 3 | `L_w`, `k₀,k₁`, `τ_stop` arithmetic (`10⁹…10²⁰`) | **CONFIRMED** (recomputed) |
| 4 | Cor. D.2, comb-free `τ_stop = 118…196` | **CONFIRMED** (arithmetic); **REPAIR** (the displayed bound is self-referential; the `373…491` counts are not reproducible without `U_spl`) |
| 5 | Cor. D.3, `D = O(e^{U/2})`, `E_at ≤ Σv_n` | **CONFIRMED** (one factor 2 slack, conservative) |
| 6 | §5 dispute with `R155_012`: `E₂` factor 2; Bernstein pad | **BUILDER RIGHT on both**; `R155_012 §2` and `§4` are in error |
| 7 | P3 numbers and verdict | numbers **CONFIRMED**; verdict **REPAIR — must be conditional** |
| 8 | labels, deviation declaration | **CONFIRMED**, one addition required (`B₂` provenance) |

---

## §2 Theorem D. CONFIRMED.

- **The regrouping is forced and correct** (`R155_013:67-80`). `ν_w`'s `cosh` part transforms to
  `4∫_{2T}^∞ w cosh(u/2)cos τu`; `2ĝ₀ = 4∫_0^{2T} cosh(u/2)cos τu` (`main.tex:444`), and `w ≡ 1` on
  the window, so the sum is `4∫_0^∞ w cosh(u/2)cos τu = Φ_w` exactly. The density jump `2cosh T` at
  `u = 2T⁺` is real and `ĝ₀ = 2cosh T sin2Tτ/τ + O(τ^{-2})` (`main.tex:451`) cancels it with the
  right sign and coefficient. **A `|ν̂_w| ≤ Dτ^{-2}` statement — the literal request of
  `R155_012 §12(2)` — is false; Theorem D's form is the correct repair.**
- **(ii) factors check.** `Φ_w = 2Ŵ`, `W(u) = w(|u|)cosh(u/2)` even; `|Ŵ| ≤ V(W')τ^{-2}` with
  `V(W') = ∫_ℝ|W''| = 2∫_0^∞|W''|`, hence `|Φ_w| ≤ 4∫_0^∞|W''|τ^{-2} = D_c` ✓. The factor 4 is
  `2` (from `Φ = 2Ŵ`) × `2` (evenness), as the prompt guessed.
- **(i) factors check.** `Ψ_w = ½R̂`, `R̂ = 2∫_{2T}^∞ R cos`, `V(R') = 2∫_{2T}^∞|R''|`, so
  `|Ψ_w| ≤ ∫_{2T}^∞|R''|τ^{-2} = D_K` ✓. Boundary terms: `w ≡ 1` on `[−2T,2T]` and `w ∈ C¹` give
  `R(2T) = R'(2T) = 0` ✓; `C²` across `±2T` is an *assumption* (`w ∈ C²(ℝ)`), not a consequence, and
  is correctly carried in the hypothesis list. In case (a) `R = K` beyond `U` with `K, K', K''`
  integrable ✓.
- **Decay threshold `s > ½` is exactly right, twice.** (ii) needs `w cosh(u/2) ∈ W^{2,1}`:
  `e^{-su}·e^{u/2} = e^{-(s-½)u}` ✓. (iii) needs `Σ Λ(n)n^{-½-s} < ∞` ⟺ `s > ½` ✓. The two
  thresholds coinciding is not a coincidence and the file says so.
- **Lower bound and monotonicity.** `σ_T ≥ log(τ/2π) − 1/τ − 1/(2τ²) − A_T` is `lem:mbounds`(ii)+(iii)
  verbatim (`main.tex:625-630`); `k₀ = 2cosh T/τ + sinh T/τ²`, `k₁ = 8T sinh T/τ` are `lem:gbounds`
  (`main.tex:448-449`), both decreasing ✓. Every term of `L_w` is nondecreasing ✓, so
  `τ_stop = min{τ : L_w ≥ 0}` is well defined and `f_w ≥ 0` on `[τ_stop,∞)` ✓.
- **Structural remark (not a defect).** Theorem D is `lem:T` (`main.tex:686-700`) with the trivial
  atom term `2Σ|a_j|` split into `E_at` (atoms) + `Dτ^{-2}` (a.c.). The novelty is genuine — `lem:T`
  has no a.c. non-exponential column — but Paper 47 should present it as an extension of `lem:T`,
  not only as an analogue of `lem:F1`; `cor:T2`'s "atoms cost exponentially" is precisely `E_at`.

## §3 The atoms. CONFIRMED, including the §5 dispute (a).

`ν_w`'s atomic part is `−Σ(v_n/2)w(log n)(δ_{log n}+δ_{−log n})`, transform
`−Σ v_n w(log n)cos(τ log n)` — identical to `main.tex:1050` (`eq:fw`, `−Σ_{n≥2}v_n w(log n)cos(τ log n)`,
with `n ∈ N_T` absorbed into `σ_T`). Sign and factor ✓. Two-sided mass is `Σ v_n|w(log n)|`, so
**`R155_012 §4`'s "E₂ is one-sided, short by a factor 2" is WRONG and the builder's rejection
(`R155_013:251-253`) is right, with proof.** `R155_012`'s corrected `E ≈ 80…145`, `log₁₀τ_env ≈ 35…63`
is an over-correction; the honest values are `‖ν‖_TV = 39.9…89.9`, `log₁₀τ_env = 18.5…40.3`
(`amend.json`, verified). `R155_012`'s `E₁` complaint is right and is implemented (`amend.py:29-31`
doubles the a.c. integral), and the `A_T` omission is right and fixed.

## §4 The numbers. All reproduce.

`amend.json`, read directly: `D = 5.0768e4, 2.6794e4, 2.6000e4, 4.4412e4, 3.0113e4, 3.3363e4`;
`E_at = 43.98, 22.05, 18.01, 24.78, 32.72, 36.94`; `τ_stop = 2.11e20, 6.31e10, 1.12e9, 3.43e12,
9.64e15, 6.58e17`; comb-free `151.95, 117.54, 117.67, 195.97, 170.10, 179.00`. **Every §4 table cell
matches.** Independent check of the two extremes: at `T = ½log3`, `A_T = 0.98028`, `β = 0`,
`log(151.95/2π) = 3.1861`, `− A_T = 2.2058`, `D/τ² = 5.0768e4/23089 = 2.1988`, plus `1/τ+1/2τ²
= 0.0066` ⇒ `L ≈ 0.0004 ≈ 0` ✓ (151.9 is correct for `D = 5.08e4`). At `D = 2.68e4`, `τ = 117.5`:
`log(18.70) = 2.9286 − 0.9803 = 1.9483` vs `2.6794e4/13806 = 1.9407` + `0.0085` ✓.
*The prompt's "does not close" was a row mismatch: `τ = 118` belongs to `D = 2.68e4`, not to
`5.08e4`.* Exponential regime likewise: `2πe^{A_T+E_at} = 2πe^{19.0} = 1.2e9` ✓ (`log3h_b60`),
`2πe^{44.96} = 2.1e20` ✓ (`log3h`).

**Defect 1 (`amend.py:57-63`).** `D_K` integrates only over `[0, U_max+2]`; the true `D_K` carries
`∫_{U_max+2}^∞|K''| ≈ |K'(9.7)| ≈ 4e−3` more. Negligible, but `D_K` as computed is a *lower* estimate
of a quantity used as an upper bound. Declare it, or extend the grid. Same remark for the
`2·10⁻⁵`-grid second differences of a piecewise-cubic `w`: correct to `O(du²·‖w⁗‖)` but not enclosed
— which §7 does label `DIAGNOSTIC`.

## §5 Corollaries.

- **Cor. D.2 — REPAIR (statement, not content).** The display
  `τ_stop ≤ max{2πe^{A_T+1}, (D₀/(log(τ/2π)−A_T))^{1/2}}` (`R155_013:174`) has `τ` free on the right:
  it is not a bound as written. The intended and correct statement is:
  *for `τ ≥ 2πe^{A_T+1}` one has `log(τ/2π)−A_T ≥ 1`, hence `τ_stop ≤ max{2πe^{A_T+1}, √D₀ + 2}`*, which
  gives `τ_stop = O(D^{1/2})` ✓. Fix before Paper 47.
- The condition-count `373, 388, 427, 491` is not reproducible from the file: `U_spl` is quoted only
  as `≈ 7.74…8.09`. My count of prime powers in `(2T, U]` at `U = 7.74, 7.80, 7.90, 8.09` is
  `374, 394, 425, 495`. Publish `U_spl` to six digits or state the counts as approximate.
- **Cor. D.3 — CONFIRMED.** `(w cosh)'' = w''cosh + w'sinh + ¼w cosh` with `|sinh| ≤ cosh ≤ cosh(U/2)`
  on the support gives `D_c ≤ 4cosh(U/2)(‖w''‖₁+‖w'‖₁+¼‖w‖₁)` ✓. `((1−w)K)'' = (1−w)K'' − 2w'K' − w''K`
  gives `D_K ≤ κ₀‖w''‖₁ + 2κ₁‖w'‖₁ + ∫_{2T}^∞|K''| = … + |K'(2T)|`; the file writes `2|K'(2T)|`, a
  harmless factor-2 slack in the safe direction. `D = O(e^{U/2})`, `τ_stop = O(e^{U/4})` ✓. The
  reading against `R155_012 §12` ("bounded profile controls `D`, only the comb controls `E_at`") is
  correct and is the most useful sentence in the file.

## §6 The Bernstein dispute. BUILDER RIGHT; `R155_012 §2` is wrong by 10³.

`B₂ = 3297.7`, `δ = 0.005`: `B₂δ²/8 = 3297.7 × 2.5e−5/8 = 1.0305e−2`. **The builder's `1.03e−2` is
correct; the auditor's `1.03e−5` (`R155_012 §2`, "hence `min ≥ +1.364e−3`") is off by exactly `10³`,
and its "repaired enclosure" is therefore not an enclosure — at `δ = 0.005` the pad swamps the value
and the honest conclusion would be `−8.9e−3 < 0`.** The builder's re-run is the right response:
`dense_log3h_b.json` (`δ = 2.5e−4`, `66 983` points on `[0,16.75]`, `30.4 s`) gives
`min_prime_dense = +1.3743932e−3`, pad `2.5763e−5`, **`certified = +1.3486e−3`** ✓ — arithmetic and
code (`dense.py:19-22`, no localisation, whole interval) both correct. `30 s` for `67k` points is on
the *fast* path (`f_prime_fast`), not GL 800; GL 800 is used only for the three spot checks. Plausible
and consistent with `R155_012 §2`'s own timings.

**Defect 2 (`dlib.py:114`).** `B₂` is `4∫u²|w||Z|du` with `Z` the **1000-zero** envelope, i.e. a bound
on `‖f_zero''‖∞`, and it is then subtracted from a **prime-side** minimum. The two sides agree only to
`3.6e−6…1.1e−5`; nothing bounds `‖f_prime'' − f_zero''‖`. The pad is therefore rigorous for the
truncated zero model and heuristic for the object actually being enclosed. This affects the builder
and the earlier auditor equally and must be stated in the §7 label row for `+1.3486e−3`.

## §7 P3 (§6 of `R155_013`). Numbers CONFIRMED; verdict REPAIR.

All eight rows reproduce exactly from `p3_p3_*.json` (LP value, dense zero min, argmin, prime value
at argmin, padded value, `‖w‖_∞`, `∫|w|`); runtimes `46.8…78.2 s`, sum `455 s = 7.6 min`, matching the
declared over-budget ✓. Zero/prime agreement `1e−6…5e−6` ✓.

- **Defect 3 (undeclared).** The JSONs also carry `wmin = −1.2e−3 … −5.3e−3`: the profile constraint is
  violated **below zero** as well as above one. §6 declares only `‖w‖_∞ > 1`. The class actually
  optimised over is `−5.3e−3 ≤ w ≤ 1.005`, not `0 ≤ w ≤ 1`. Say so.
- **Defect 4 (the verdict).** "*there is no such path in this class*" is supported; "**no path to a new
  endpoint at any `T ∈ (½log3, log2]`**" is not, and §8(1) of the same file concedes why: the
  comb-free class of Cor. D.2 is a *different* class and has not been run. The verdict must read:
  *the bounded-profile and unconstrained flat-top classes are measured negative on `[0,60]` at four
  windows; the comb-free class predicted by Cor. D.2 is untested.* As written, §6's last sentence
  over-reaches beyond its own `DIAGNOSTIC` label.

## §8 Labels.

Correct as given: `PROVED` only for Theorem D, Remarks D.1, Cors. D.2/D.3; `DIAGNOSTIC` for every
number; no sign, no endpoint, endpoint of record left at `λ_min(A_{½log3}) ≥ 8.8577e−5`. The
compute-budget deviation (`7.5 min` vs `5 min`) is declared, not hidden ✓. **Add one row**: the
`B₂` pads (§6 above) are zero-model quantities used on prime-side minima — `DIAGNOSTIC`, not an
enclosure of `f_prime`. The amended `R155_011` is honest: every strike is marked in place, the TK and
Theorem-N category errors are struck, the `λ^P−λ^W` reading is demoted, and the `+1.3703e−3` claim is
replaced by `+1.3486e−3` with the correct pad.

## §9 Readiness for Paper 47

**Theorem D: READY** for §4 beside `lem:T`/`lem:F1`, subject to (a) restating it as the a.c. extension
of `lem:T`, (b) keeping the hypothesis `w ∈ C²(ℝ)` explicit (the `C²` match across `±2T` is an
assumption), (c) `D_K`'s tail of integration stated exactly.
**Cor. D.2: READY** once the display at `R155_013:174` is repaired as in §5 above, and `U_spl` is
published so the condition count is checkable.
**Cor. D.3: READY** as stated (the `2|K'(2T)|` slack is admissible).
It is the correct smooth analogue of `lem:F1` on the a.c. part only; Remark D.2's admission that the
comb is met by mass and not by grading is accurate, and is where the remaining exponential lives.

*No label of record changes. Reruns: `≈ 25 s`.*

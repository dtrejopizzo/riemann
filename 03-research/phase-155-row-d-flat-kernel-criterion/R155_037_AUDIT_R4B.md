# R155.037 — Audit of R155_033 (round 4b) and `scripts/r4b/`

*Target: `R155_033_ROUND4B_PROBLEM_A_ARCH.md`, `scripts/r4b/`.
References: Paper 46 `main.tex` (§3 `thm:D1` l.473, `thm:O` l.537, `rem:OvsB` l.567;
§4 `lem:mbounds` l.630, `lem:F1` l.732; §7 `thm:Z` l.1131; §8 `prob:A` l.1761, `prop:TK` l.1779,
`prop:arch` l.2125, `lem:R1` l.2279, `thm:R` l.2298, `cor:R3` l.2330), `R155_023` (amended),
`R155_004 §6`. Both scripts rerun in full; nothing in `04-papers` or `scripts/` modified.*

## §0 Verdict

* **Theorem AL — SOUND, READY after one amendment.** The feasibility objection does not apply, and
 the `U`-endpoint is covered by hypothesis but must be spelled out.
* **Corollary AL′ — SOUND as an inequality; its headline reading is overstated, and the quantitative
 `V_r` blow-up display is WRONG (sign and prefactor).** Not ready.
* **Theorem R∞ — SOUND, constant verified.** One scope defect in the `§2.6` table.
* **Proposition NC — SOUND, proof verified line by line; numbers reproduced.** Three numerical
 inconsistencies inside `R155_033` (`38/48/55` vs `37/47/54`; `4/5/6` vs `4/5/5`; `≳30T` vs `68.5T`).
* **`r4b_01` reproduced bit-for-bit; `D = O(M^{−2})` "REFUTED" is NOT earned.** Downgrade.
* **"STRUCTURAL NEGATIVE" — half fair.** Correct for non-attainment, overstated for the rate.

---

## §1 Theorem AL (`R155_033:118–145`)

**(a) Feasibility — no defect; the objection is void.** Paper 46's `(D)` (`main.tex:425–433`) carries
**no moment equalities on `ν`**: the only constraints are `ν` finite, even, `supp ν ⊆ {|u| ≥ 2T}`,
`β ∈ ℝ²` free, and the pointwise inequality. The Tate/`ĝ_j` pairings are constraints on the **primal**
`μ`, not on the dual (`prop:weak` proof, `main.tex:445–452`). Hence sampling has nothing to preserve:
`ν_lat` is feasible because its atoms sit at `|u| = |j|d ≥ Md = 2T`, and the boundary atom at `±2T` is
explicitly declared harmless (`main.tex:449`, `c_F(±2T) = 0`). `β = 0` is legitimate because the primal
satisfies `∫ĝ_j dμ = 0`. **VALID — no multiplier adjustment and no Theorem-B box is needed.**

**(b) The `U` endpoint — covered, but only by an unstated hypothesis.** `R155_033:120` assumes
`G_e ∈ C^{r−1}(ℝ)`, `G_e^{(r)} ∈ L¹` *directly*, so the jump at `U` is excluded by fiat, not by
oversight. But the hypothesis is never unpacked and it binds in **two** places: `(1−w)K` must vanish to
order `r−1` at `u = 2T⁺` (so `w` has `C^{r−1}` contact with `1` from outside the window) **and** at
`u = U⁻` (so `w → 1` again at `U`, since `K(U) ≠ 0`). It is non-vacuous: `w ≡ 1` near both ends with a
negative dip in `(2T,U)` satisfies it and can still meet the `τ = 0` cap of `§2.2`. **Required amendment
(`R155_033:120`):** state *"`w ≡ 1` on `[0,2T]` and on `[U,∞)`, with `C^{r−1}` contact at both ends"*.
Without it the theorem reads as if any flat-top `w` qualifies, which is false.

**(c) Frequency bookkeeping — correct.** `d = 2T/M`, `P = 2π/d = πM/T`, Nyquist `P/2 = πM/2T`; the
branch `m(πM/2T) − V₀` is the `|τ| > P/2` fold, using `ν̂_lat` `P`-periodic, `|Ĝ_e| ≤ ‖G_e‖_{L¹} = V₀`,
and `m` increasing (`lem:mbounds`(i), `main.tex:630`). ✓

**(d) Constant — correct.** `Σ_{k≠0}|τ+kP|^{−r} ≤ 2Σ_{k≥1}((k−½)P)^{−r} = 2(P/2)^{−r}(1−2^{−r})ζ(r)`,
and `|Ĝ_e(ξ)| ≤ V_r|ξ|^{−r}` by `r` integrations by parts in the paper's convention. ✓

**Verdict: `PROVED` once (b) is written into the statement. READY.**

## §2 Corollary AL′ and the reading (`R155_033:151–168`, `§0.1(β)`)

* `thm:O` does cover `v = 0`: the sentence *"holds for every finite weight family, including `v = 0`"*
 is in the statement (`main.tex:544`) and the proof's contradiction at `𝒩_T = ∅` rests on `K(u) ~ 1/u`
 alone (`main.tex:562–565`). Consistent with `rem:OvsB`. ✓ The flat-top class of `§2.2` sits inside the
 `ν`-class, so it is covered. ✓
* **ERROR (`R155_033:167`).** The display
 `V_r ≥ (2T/π)^r M^r (δ − 0.28·M^{−1.17})/(2(1−2^{−r})ζ(r))` is wrong twice. From
 `c_w ≤ Ceil_∞(M) + ε_r(M)` and `c_w ≥ λ^{∞,P} − δ` one gets `ε_r(M) ≥ Def(M) − δ`, hence
 `V_r ≥ (πM/2T)^r (0.28·M^{−1.17} − δ)/(2(1−2^{−r})ζ(r))` — the bracket is `Def − δ`, **not** `δ − Def`
 (as printed it is vacuous/backwards), and the prefactor is `(π/2T)^r M^r`, **not** `(2T/π)^r M^r`.
 The conclusion survives the correction: optimising at the largest `M` with `Def(M) > δ` gives
 `V_r ≳ (π/2T)^r δ^{−r/1.17}·const → ∞` as `δ ↓ 0`.
* **Overclaim (`R155_033:24–27`, `§0.1(β)`).** *"none of the Problem-A deficit is the lattice"* holds
 only at **fixed** `w`. In the joint optimisation the term `V_r(w)M^{−r}` **is** the lattice cost, as
 `§2.3`'s own consistency check concedes. Rewrite as *"at fixed smoothness the lattice is free at rate
 `M^{−r}`; the deficit is the trade-off between the edge approximation and `V_r M^{−r}`"*.
* **"Closing it forces `V_r ↑ ∞`" is NOT proved by `thm:O`** (which forbids attainment only); the
 quantitative version depends on the `DIAGNOSTIC` ceilings. `§4:316` is acceptable only after the
 formula is fixed; `§0.1(β)` as written is not.

## §3 Theorem R∞ (`R155_033:83–91`)

Constant **verified**: `thm:R` has `Δ = [m(P/2) − C₀] + 2A_T + 2|β₀|ĝ₀(0) + 2|β₁|ĝ₁(0)`
(`main.tex:2303–2306`); at `𝒩 = ∅`, `A_T = 0`, so `Δ_∞ = Δ − 2A_T` ✓, and `2·0.9803 = 1.9606 ≈ 1.96` ✓.
**Scope defect (`R155_033:225`):** the row *"`D_∞(M) → 0` with no rate — `PROVED` (`thm:D1` + `thm:R∞`
+ `cor:R3`)"* is unproved at `log 2`: `cor:R3` (`main.tex:2330`) assumes `λ^P > 0` and `thm:Bbeta`,
while `λ^{∞,P}(log 2) = −0.15428 < 0`. Restrict that row to windows with `λ^{∞,P} > 0`.

## §4 `§2.4` "the Jackson route does not start" (`R155_033:170–181`)

Directionally right, **mislabelled and imprecise**. `prop:TK` uses the vanishing of **all** modes
`|j| < M` (orthogonality to every `|q|²`, `deg ≤ M−1`, Fejér–Riesz, `main.tex:1793–1800`), not merely
*"zero mean over a period"* (mode `0` only) as `R155_033:177–179` says. And `§4:317` labels *"the
Jackson route does not start"* `PROVED (prop:TK)`: `prop:TK` proves a ceiling, not the non-existence of
a route. **Label → `READING`/`OBSERVED`**; wording → *"low-mode vanishing, a spectral-gap constraint,
not a smoothness constraint"*.

## §5 `r4b_01` (archimedean ceilings) — reproduced, inference downgraded

Rerun of `scripts/r4b/r4b_01_ceil_inf.py`: **all 14 values reproduce to the printed digits**
(`+5.98976584e−02 … +8.05229792e−02`; `−1.77910710e−01 … −1.56325330e−01`), identical to `r4b_01.json`
and to the `§2.5` table. Runtime ≈ 4 min wall on this box, not the `≈60 s` of `scripts/r4b/README.md` —
fix that line.

The **direction** of the inference is valid: `prop:TK` bounds *every* lattice certificate value, so
`λ^{∞,P} − Ceil_∞(M)` is a genuine lower bound on the class deficit. But **"`D = O(M^{−2})` REFUTED"
(`R155_033:214`, `§2.6:227`) is not earned**, for four independent reasons:
1. `λ^{∞,P}` is a Galerkin (`N = 18`) **upper** bound — an inflated reference inflates the deficit;
2. `Ceil_∞` is a numerical `sup_β` (grid + Nelder–Mead); under-optimisation **lowers** `Ceil` and again
 inflates the deficit. Both error directions push the same, unsafe way;
3. at `½log3`, `M = 8/12/16` the optimiser leaves the seed box: `β = (7.92,−8.00), (8.10,−7.51),
 (9.16,−7.90)` against the stable `(2.29,−6.29)` for `M ≥ 24`. Those three points anchor the fitted
 exponent; and `§2.5` reading 4's "`β` stabilises" is true only for `M ≥ 24`;
4. the local slope still drifts (`−1.02 → −1.29`) over `M ≤ 64`; excluding `M^{−2}` is an extrapolation.
**Downgrade to `DIAGNOSTIC`:** *"no numerical support for an `M^{−2}` law; the measured rate over
`8 ≤ M ≤ 64` is `≈ 0.28 M^{−1.17}`, essentially `T`-independent for `M ≥ 24`."* The `T`-independence
(`<1 %` at `M ≥ 24`) is reproduced and is the strongest datum of the round.

## §6 Proposition NC (`R155_033:249–266`) — proof valid, numbers reproduced, three inconsistencies

Proof audited step by step and **correct**: `A_∞(F) ≥ C₀b + m(τ₁)(1−b)` with `b = ‖B_{τ₁}F‖²`;
`A_∞(F) < 0 ⟹ b > θ(τ₁) = m(τ₁)/(m(τ₁)−C₀) ∈ (0,1)`; `⟨S_{T,τ₁}F,F⟩ = b` since `Q_TF = F`; min–max on
an `n`-dimensional `V` gives `λ_{n−1}(S) > θ`; `tr S_{T,τ₁} = 2Tτ₁/π` and Markov give
`#{λ_n > θ} < 2Tτ₁/(πθ)`. The restriction to `P_T ⊂ L²(I_T)` is handled correctly (`n₋` only decreases).

Rerun of `r4b_02_negcount.py` **and** an independent recomputation of
`inf_{τ₁>τ₀}(2/π)τ₁(m(τ₁)−C₀)/m(τ₁) = 68.5135` at `τ₁ = 14.8815`:

| `T` | trace bound | prolate count (`τ₁ = 6.682`, `θ = 0.0111`) |
|---|---|---|
| `½log3` | `37.635 → 37` | `4` |
| `log2` | `47.490 → 47` | `5` |
| `0.80` | `54.811 → 54` | `5` |

Top eigenvalues at `log2` reproduce `§3.3` exactly (`0.9987, 0.9645, 0.7114, 0.2415, 0.0303, 0.0019`);
an independent Nyström run reproduces the counts `4/5/5`.

**ERRORS.**
* `R155_033:43` (`§0.4`) and `§4:323`: **`38, 48, 55`** and prolate **`4, 5, 6`** — wrong; the correct
 floors are **`37, 47, 54`** and **`4, 5, 5`**, as in the `§3.3` table, `scripts/r4b/README.md` and both
 runs. An internal contradiction inside the same document.
* `R155_033:285–286`: *"`inf_{τ₁} 2Tτ₁/(πθ(τ₁)) ≥ (2T/π)·τ₀·(1 + |C₀|/m(τ₁))`"* carries the bound
 variable `τ₁` into a `τ₁`-free infimum, and *"`≥ 4T/π·τ₀·O(|C₀|/log τ₁)`"* is a lower bound written
 with an `O(·)` — not a statement. The value *"`≳ 30T`"* is wrong: the exact minimum is **`68.5135·T`**
 (`PROVED` as `(2T/π)·inf_{τ₁>τ₀}(m−C₀)/m`; the constant `DIAGNOSTIC`).
* `R155_033:60` and `§4:322`: NC does **not** replace the `HEURISTIC` half of `R155_023` Prop 3(ii).
 That heuristic is the *lower* bound / asymptotic; the *upper* half was already amended to `PROVED`
 (`n₋ ≤ 2Tτ₀/π + O(log T) + 2`, `R155_023:327`) and is far sharper than NC (`≈4` vs `37`). NC's merit
 is **explicitness in `T`** only — say exactly that.

The `§3.3` structural diagnosis (logarithmic growth of `m` caps `θ`, so a two-level majorisation cannot
reach `1`) is correct and is the honest content of the round. `(H1)` stays `HYPOTHESIS`. ✓

## §7 Labels, "STRUCTURAL NEGATIVE", Paper 46 proposals

* **"Problem A is hard because of the primes — REFUTED" (`§4:321`): half fair.** `thm:O` at `v = 0` is
 genuine and `rem:OvsB` is consistent with it (it names both the `1/u` singularity and the prime atoms
 as lying inside the window; deleting the primes leaves the `1/u`). But `thm:O` is about
 **attainment**, not about the **rate** `D`, and nothing here compares the prime-on and prime-off
 rates. Restate as: *"the primes are not necessary for the obstruction: non-attainment and the edge
 singularity survive at `v = 0`"* — that is `PROVED`. Drop `REFUTED`.
* **ERROR (`§4:311`).** *"Dictionary (2.1) — `PROVED` (`thm:Z` at `v = 0`)"* misattributes: (2.1)
 deletes the primes **and** the polar term, whereas Paper 46's flat-top dual point is `(ν_w, β = (2,0))`
 with `+2∫w cosh(u/2)cos(τu)du` inside `f_w` (`main.tex:1128`, `eq:fw`). The algebra of (2.1) is
 correct, but it is **not** `thm:Z` and carries **no** explicit-formula / zero-sum reading.
* `τ = 0` cap (`§2.2`): verified independently — `∫_{2T}^∞K = 2.364155` (`½log3`), `2.025908` (`log2`);
 required `5.4547`/`5.2179`; factors `2.307`, `2.576`. The document's *"≥ 2.6"* rounds a lower bound
 **up**; write `≥ 2.5`.
* **Paper 46 proposals.** `§5.1` acceptable **only** with the two-sided smooth-contact hypothesis of
 §1(b) written in and the `§0.1(β)` overreach removed. `§5.2` only as a `DIAGNOSTIC` paragraph with
 "`M^{−2}` is out" softened per §5. `§5.3` acceptable after the `37/47/54` fix and the Prop 3(ii)
 attribution fix.

## §8 Readiness

| item | verdict |
|---|---|
| **Theorem AL** | **READY** — feasibility sound (no moment equalities in `(D)`), `U` endpoint sound *once the hypothesis is stated*; amend `R155_033:120` |
| **Corollary AL′** (the inequality) | `PROVED`; **the `V_r` display `:167` must be corrected** before use |
| "all the deficit is continuous" / "`V_r ↑ ∞` forced" | **NOT READY** — overclaim + `DIAGNOSTIC`-conditional |
| **Theorem R∞** | `PROVED`, constant verified; restrict the `§2.6` "`→0`" row to `λ^{∞,P} > 0` |
| `§2.4` Jackson reading | downgrade `PROVED → READING`; "zero mean" → "low modes vanish" |
| `Ceil_∞` table, `T`-independence | `DIAGNOSTIC`, **reproduced exactly** |
| `D = O(M^{−2})` "REFUTED" | **downgrade to `DIAGNOSTIC`** (unsafe error directions, drifting slope, unconverged `β` at `M ≤ 16`) |
| **Proposition NC** | **READY**, `PROVED`; fix `38/48/55 → 37/47/54`, `4/5/6 → 4/5/5`, `≳30T → 68.51·T`, restate `:285–286` |
| `(H1)`, row-D label, endpoint of record | unchanged — correctly so |

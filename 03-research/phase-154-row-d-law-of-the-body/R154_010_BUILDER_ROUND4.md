# R154.010 — Round 4, builder: a fully certified dual certificate with `c > 0` at `T = ½log3`

*Builder: Opus 5 (1M). 2026-09-20. Orders: `R154_009` (lead, round 4). Binding: `R154_008` (hostile audit R3, repairs
RJ–RP) and the auditor's corrected verifier and certificate in `scripts/round3/audit_r3/`, from which this round starts.
Scripts: `scripts/round4/` (`r4core.py` symbol + exhaustive B&B, `r4iv.py` interval arithmetic, `r4lp.py` flat-lemma LP,
`r4graded.py`/`r4g2.py` the new graded-tail LPs, `r4polish.py` the block polish, `r4bbpar.py` parallel exhaustive cover,
`r4final.py` audit + archival; all logs `sw_*.log` committed non-empty; certificate in `scripts/round4/certificate/`).*

**One-line result.** `PROVED`: `λ_min(A_{½log3}(w_ζ)) ≥ c = 4.4279281900·10⁻⁵ > 0`, by an explicit 437-atom dual
certificate whose defining inequality is verified on **all of `R`** by an exhaustive Lipschitz branch-and-bound
(`2.372·10⁸` evaluations, **zero** unresolved intervals, nothing discarded) plus a new exact periodic-tail lemma, with
every constant re-enclosed in `mpmath` interval arithmetic. The previous record was the auditor's
`−1.6500·10⁻³` (`R154_008`): **the sign crosses.**

---

## 1. Corpus check (mandatory)

| idea used here | grep (2026-09-20, `03-research`, `04-papers`, `05-meta`, excluding `phase-154`) | pre-existing | status here |
|---|---|---|---|
| lattice ⟹ periodic `ν̂`, tail on one period (Lemma D2.1) | `R154_007 §3.1` | **round 3's** (this phase) | reused, then *superseded* by D2.3 |
| "graded"/"one period"/"residue class" tail for a certificate | `phase-118`, `phase-116/114_d_87`, `phase-122` — all unrelated objects (threshold inequality, periodic dagger fibres, affine carriers) | none in this sense | **new (§3)** |
| Lipschitz branch-and-bound | `grep -i "Lipschitz branch"`: 0 hits outside phase 154; `Lipschitz` appears in `phase-137` (lattice moduli) | the device is round 3's (`R154_007 §3.1`) | corrected verifier is the **auditor's** (`R154_008`); this round parallelises and hardens it |
| `mpmath.iv` interval arithmetic | `phase-153` (`R153_000/003/004/005`), `phase-118 W4_CERTIFIED_RANGE` | the tool is standard and used before in the corpus | the rigorous `Re ψ(¼+iτ/2)` enclosure (recurrence + Stieltjes-bounded asymptotics) is written here |
| block ("few-parameter") re-solve on a fine grid | `phase-73/79` "block scaling" = unrelated (Cauchy pair blocks) | none | **new (§4)** |
| `β₀ → 2` = the polar term of the explicit formula | `R154_007 §4.1` | round 3's observation | **confirmed to `2.6·10⁻³`** at the certified optimum |

---

## 2. Where round 3 stood and which lever was actually binding

The class is Theorem B / Theorem D1 (`R154_007 §2`, `PROVED`): for every finite even signed `ν` with
`supp ν ⊆ {|u| ≥ 2T}` and `β ∈ R²`,

  `λ_min(A_T(v)) ≥ inf_{τ∈R} f(τ)`,  `f = σ_T + ν̂ + β₀ĝ₀ + β₁ĝ₁`,
  `σ_T(τ) = m(τ) − Σ_n v_n cos(τ log n)`, `m(τ) = Re ψ(¼+iτ/2) − log π`.

At `T = ½log3` only `n = 2` survives (`Σ_n v_n = 0.98025814…`). Round 3 put the atoms on `u_j = jd`, `d = 2T/M`,
`j = M,…,J`, so `ν̂` is `P`-periodic, `P = 2π/d`, and bounded the tail by `ν̂ ≥ −ρ` (Lemma D2.1).

**The lead's diagnosis was that `ρ` is set by the tail row and `τ_max` is the lever. Measured, that lever saturates.**
Re-running the flat programme with `ρ` free (`r4lp.py`, `M = 16`, `U = 20`, resonance-enriched grid, cuts):

| `τ_max` | LP value `c` | `ρ` at the optimum | `β₀` | `‖a‖₁` |
|---|---|---|---|---|
| 100 | `−1.186967·10⁻³` | 1.7415 | 1.997680 | 27.67 |
| 160 | `−4.748427·10⁻⁵` | 2.2282 | 2.000080 | 31.74 |
| 250 | `−3.969520·10⁻⁵` | 2.6849 | 2.000208 | 32.82 |
| 400 | `−3.964756·10⁻⁵` | 2.8600 | 2.000177 | 33.03 |

`τ_max: 160 → 400` buys `8·10⁻⁷`. **`ρ`/`τ_max` is exhausted at `τ_max ≈ 160`**; the binding lever is the lattice
index `M` (at `τ_max = 160`: `M = 16 → −4.75·10⁻⁵`, `M = 19 → +5.72·10⁻⁵`, `M = 24 → +1.742·10⁻⁴`).

But every one of those LP values was **fictitious**: the branch-and-bound minimum of the same certificate was
`−7·10⁻³` to `−8·10⁻³`, and cut rounds did not close the gap (`M = 16`: `it0 −6.70·10⁻³ → it1 −8.20·10⁻³`). The reason
is structural, not a bug: on `[30, τ_max]` the LP must resolve dips of `f` of width `≈ 4·10⁻⁵`
(`L ≈ 400–650`), i.e. `≈ 3·10⁶` rows, and a cut inserted at one `τ` fixes only that `τ`. **This, and not `ρ`, is the wall
that round 3 hit.**

---

## 3. Lemma D2.3 (`PROVED`, new): the graded periodic tail — one period of rows replaces `[τ₁,∞)`

Fix `τ₁ > 0`. Every `τ ≥ τ₁` is uniquely `τ = x + kP` with `x ∈ [τ₁, τ₁+P)` and `k ∈ Z_{≥0}`, and since
`u_jP = 2πj ∈ 2πZ` we have `ν̂(x+kP) = ν̂(x)`. With `|ĝ₀(τ)| ≤ k₀(τ) := 2cosh T/τ + sinh T/τ²` and
`|ĝ₁(τ)| ≤ k₁(τ) := 8T sinh T/τ` (both decreasing) and `m` increasing:

> **Lemma D2.3.** For `N ≥ 1` put, for `x ∈ [τ₁, τ₁+P)`,
> `W_k(x) := m(x+kP) − Σ_n v_n cos((x+kP)log n) − |β₀|k₀(x+kP) − |β₁|k₁(x+kP)` for `0 ≤ k < N`, and
> `W_N(x) := m(x+NP) − Σ_n v_n − |β₀|k₀(x+NP) − |β₁|k₁(x+NP)`. Then
> **`f(τ) ≥ c` for all `τ ≥ τ₁`  ⟺  `ν̂(x) + W_k(x) ≥ c` for all `x ∈ [τ₁, τ₁+P)` and all `0 ≤ k ≤ N`.**
>
> *Proof.* `⟸`: for `τ = x+kP` with `k < N` the inequality with that `k` is exactly `f(τ) ≥ c` after the two `|ĝ|`
> bounds; for `k ≥ N`, `m(x+kP) ≥ m(x+NP)`, `k_i(x+kP) ≤ k_i(x+NP)` and `−Σv_ncos ≥ −Σv_n`, so the `k = N` row is
> weaker than the truth. `⟹` is the specialisation `τ = x+kP`, `k < N`. ∎

Three things this buys, all decisive:

1. **No `τ_max`, no `ρ`.** The whole of `[τ₁,∞)` is certified, not `[τ_max,∞)`; the flat floor `−ρ` is replaced by the
   graded floor `−W_k`, whose worst value at `τ₁ = 30`, `N = 2`, `P = 137.26` is `W₂ ≥ 2.67` against `ρ ≤ 2.23` for the
   flat lemma at `τ_max = 160`.
2. **The prime term stays exact** on the first `N` periods; only the residual `k ≥ N` uses `−Σ_nv_n`. (Taking `N = 1`
   — worst-casing the prime term from `τ₁` on, `r4graded.py` — costs a factor `40`: LP value `−1.700·10⁻³` at `M = 19`
   versus `+5.205·10⁻⁵` with `N = 2`. The `cos(τ log 2)` term is *not* negligible and must be kept.)
3. **Cuts are reused across the whole tail.** A row at phase `x` constrains every `τ ≡ x (mod P)` at once. Measured:
   with the flat lemma the LP/true gap stalled at `8·10⁻³`; with D2.3 at `M = 24` it was `2.3·10⁻³` after one LP and
   closed to `1·10⁻⁸` after the polish of §4. **This is the round's method contribution.**

Cost: the verification domain is `[0,τ₁] ∪ [τ₁,τ₁+P]` (`N+1` functions on the second), i.e. `30 + 3×137.26`, instead
of `[0,τ_max] ∪ one period` with `τ_max` unbounded below by the tail row.

**Lipschitz constant.** One constant serves everything:
`L = ψ'(¼)/2 + Σ_nv_n log n + 2Σ_j|a_j|u_j + |β₀|G₀ + |β₁|G₁`, `G₀ = ∫|u|cosh(u/2) = 1.29953`,
`G₁ = ∫u²|sinh(u/2)| = 0.37653` over `[−2T,2T]`. It dominates `|f′|` and every `|h_k′|` because for `t ≥ τ₁ = 30`,
`|k₀′| ≤ 2.6·10⁻³ ≪ G₀` and `|k₁′| ≤ 2.8·10⁻³ ≪ G₁` (checked numerically and recorded). For the certificate below
`L = 647.4198370823957…`, whose interval enclosure is `[647.419837082395577…, 647.419837082395577…]`; the float value
used in the B&B **dominates** the enclosure, which is the direction the proof needs.

---

## 4. The block polish: how the 437-variable LP is made exact

The atom LP has `≈ 440` columns, so its grid must be coarse (`10⁻²`–`10⁻³`) and its narrow dips survive; that is the
wall of §2. But **once the shape of `ν` is fixed**, the same programme in `G` block scales
`a_j ↦ λ_{g(j)}a_j` has only `G+4` columns and can be re-solved on a grid `10²`–`10³×` finer
(`2·10⁻³` rows, cuts from a `5·10⁻⁶` grid, `2.4·10⁵`–`3·10⁵` rows). Starting from the `M = 24`, `τ₁ = 30`, `N = 2`
candidate (`r4g2.py`, LP value `+1.680·10⁻⁴` on its own coarse grid):

| `G` | polished LP value | true fine-grid `min f` on `[0,τ₁]` | true `min_k min h_k` | converged? |
|---|---|---|---|---|
| 1 (pure scaling) | `−2.09705·10⁻²` | `−2.09705·10⁻²` | `−2.10409·10⁻²` | yes |
| 32 | `−1.05472·10⁻³` | `−1.05478·10⁻³` | `−1.05481·10⁻³` | yes (`6·10⁻⁸`) |
| 48 | `−2.63477·10⁻⁴` | `−2.63560·10⁻⁴` | `−2.63564·10⁻⁴` | yes (`9·10⁻⁸`) |
| **128** | **`+8.885462·10⁻⁵`** | `+8.874966·10⁻⁵` | `+8.857856·10⁻⁵` | **yes (`2·10⁻⁹`)** |

The `G = 1` row is the honest measurement that killed the cheap hope: the coarse-grid LP value `+1.68·10⁻⁴` is worth
`−2.1·10⁻²` in truth, and no rescaling repairs it. At `G = 128` the LP value, the fine-grid minimum of `f` and the
fine-grid minima of all three `h_k` agree to `2·10⁻⁹` — **the discretisation error is gone**, and the candidate is a
genuine certificate with a positive infimum. (`‖a‖₁ = 45.377`, `ν̂(0) = 1.7337`, `β₀ = 2.0025617`, `β₁ = −0.0096544`;
`β₀ → 2` of `R154_007 §4.1` is confirmed to `2.6·10⁻³` on an object that is now *proved*, not diagnostic.)

---

## 5. The certified statement

> **Theorem R4 (`PROVED`, machine-verified; E2).** Let `T = ½log3`, `v_2 = 2log2/√2`, and
> `σ_T(τ) = m(τ) − v_2cos(τ log 2)` with `m(τ) = Re ψ(¼+iτ/2) − log π`. Let `d = 2T/24`, `u_j = jd` for
> `j = 24,…,460` (so `u_{24} = 2T` exactly and `u_{460} = 21.0567…`), let `a_{24},…,a_{460}` be the 437 rationals
> archived in `scripts/round4/certificate/CERT_log3_M24.json` as exact decimal strings, and let
> `β₀ = 2.00256170925026033557969640241935849189758300781250`,
> `β₁ = −0.00965443404485797490588439018210920039564371109008789…`. Put
> `ν = Σ_j a_j(δ_{u_j}+δ_{−u_j})`. Then
>
>   **`σ_T(τ) + ν̂(τ) + β₀ĝ₀(τ) + β₁ĝ₁(τ) ≥ c := 4.4279281900·10⁻⁵ > 0`  for every `τ ∈ R`,**
>
> and therefore, by Theorem A and Theorem D1 (`R154_001 §4.2`, `R154_007 §2`),
> **`λ_min(A_{½log3}(w_ζ)) ≥ 4.4279·10⁻⁵ > 0` on `P_T`.**

**How it is verified (repairs RJ, RP of `R154_008`, in full).**

* `f` is even, so `[0,∞)` suffices. The domain is split as `[0,τ₁]` (`τ₁ = 30`) for `f`, and `[τ₁, τ₁+P]`
  (`P = 137.2608…`) for each of `h_k = ν̂ + W_k`, `k = 0,1,2` (Lemma D2.3, `N = 2`).
* Each is covered by a **stack-based** Lipschitz branch-and-bound (`r4bbpar.py:bb_seg`) in which a cell of width `w`
  with midpoint `μ` is certified when `f(μ) − Lw/2 ≥ target` and is **otherwise bisected**. There is **no cap and no
  discard** anywhere: the oversize-batch branch pushes the remainder back on the stack, and the evaluation budget
  raises `RuntimeError` instead of returning a pass. The 21 segments are checked in `r4final.py` to tile the four
  intervals exactly (no gap, no overhang) and to share one `target`, one `w_min` and one `L`.
* `target = 4.42892819·10⁻⁵` (half the fine-grid infimum), `w_min = 5·10⁻⁸`.
  **Result: 21/21 segments complete, `2.37201004·10⁸` evaluations, and `0` unresolved intervals** — the cover closes at
  a width where `Lw/2` already separates `f` from the target, so no interval was ever left over to be bounded.
* A float64 allowance `ε_fp = 10⁻⁸` is subtracted: `c = 4.42892819·10⁻⁵ − 10⁻⁸`. It is justified, not assumed —
  `r4final.py` compares the float evaluator against the interval evaluator at the three argmins and 60 random points
  and reports a maximum discrepancy of `8.21·10⁻¹³`, four orders inside the allowance.
* **Interval arithmetic** (`r4iv.py`, `mpmath.iv`, 40 digits): `G₀`, `G₁`, `ψ′(¼)` (cross-checked against the closed
  form `π²+8G`), `k₀`, `k₁`, `L`, and `m(τ) = Re ψ(¼+iτ/2) − log π` via the recurrence
  `Re ψ(z) = Re ψ(z+J) − Σ_{j<J}Re(z+j)^{-1}` with `J = 2|Im z|+30` and the asymptotic series with Stieltjes'
  remainder bound `|R_N| ≤ |B_{2N}|/(2N|w|^{2N})·(2|w|/(|w|+Re w))^N` — enclosures of width `≈ 10⁻⁴²`, validated
  against `scipy.special` to `10⁻¹⁵`. The three minima re-evaluated in intervals:
  `f(17.64498…) ∈ [8.87496582721224892569…·10⁻⁵, …]`,
  `h₀(37.81530…) ∈ [8.85785640063696486117…·10⁻⁵, …]`,
  `h₂(58.81710…) ∈ [8.88172331280758088771…·10⁻⁵, …]` — all **strictly positive** as intervals.
* Archived: `certificate/CERT_log3_M24.json` (every `u_j`, `a_j`, `β`, `v`, `L`, target, `w_min`, `ε_fp`, all segment
  statistics, the interval enclosures, and a `checks_failed: []` field) and `CERT_log3_M24.pkl`; the 21 raw segment
  records are in `bbout/`. Reproduce with
  `python3 r4bbpar.py drive lp_c24_it1.pkl --target 4.42892819e-05 --wmin 5e-8 --nproc 19 --dir bbout`
  then `python3 r4final.py lp_c24_it1.pkl bbout/_all.json --tag CERT_log3_M24`.

**Scaling of the certified `c` against each lever** (all fully certified values at `½log3`):

| source | certified `c` |
|---|---|
| round 2 (a.c. `ν`, `τ_max = 10³`) | `−3.4567·10⁻²` |
| round 3 builder (D2.1, `τ_max = 100`, `ρ ≤ 1.50`) | `−3.7002·10⁻³` |
| round 3 auditor (D2.1, `τ_max = 100`, `ρ ≤ 1.70`, corrected verifier) | `−1.6500·10⁻³` |
| round 4, D2.3 + `M = 24` + `G = 32` polish | `−1.0548·10⁻³` |
| round 4, D2.3 + `M = 24` + `G = 48` polish | `−2.6356·10⁻⁴` |
| **round 4, D2.3 + `M = 24` + `G = 128` polish, exhaustive cover** | **`+4.4279·10⁻⁵`** |

The Galerkin upper bound is `λ_min(A_{½log3}) ≤ 9.89281·10⁻⁴` (`K = 120`, `R154_007 RG`), so the certificate captures
`4.5%` of the true eigenvalue; by Theorem D1 the remaining `95%` is available to certificates of the same class, and by
Theorem O none of them attains it.

**What is visible here that was not visible in Paper 42 (E2).** Paper 42 (`main.tex:4072–4230`) proves positivity at
this `T` by a **directed Feshbach reduction**: a finite-rank `P`, a complement bound `QAQ ≥ δQ`, and a Schur complement
`PAP − δ^{-1}H > 0`. That certificate is a statement about a chosen finite-dimensional subspace and a mesh; nothing in
it is an object on the spectral side. The certificate above is mesh-free and every ingredient is an explicit function of
`τ`: (i) the polar multiplier `β₀ = 2.0026` — the dual *reconstitutes* `Φ̂(i/2)+Φ̂(−i/2)`, the two polar contributions of
the Weil explicit formula that the primitive class `𝒦^{prim}` removes; (ii) the outside-window measure `ν`, supported
in `|u| ≥ 2T` and hence invisible to `A_T`, whose Fourier transform does all the lifting — `ν̂(0) = 1.734`, `‖a‖₁ = 45.4`,
no arithmetic structure in the positions (`R154_007 §4.3`); (iii) the contact set, a comb: `f − c` vanishes to `10⁻⁵`
on a band inside `[0,13]` *and* at one phase of the tail per family (`x = 37.815`, `58.817`), which is complementary
slackness of Theorem O made visible on both sides of `τ₁`. The `f` part of the cover consumed `1.91·10⁸` of the
`2.37·10⁸` evaluations precisely because that contact band is broad.

---

## 6. Round-3 repairs (E1) and what is *not* done

`RJ`/`RP` are discharged by construction: the verifier is rewritten (`r4core.bb_min`, `r4bbpar.bb_seg`) with the
`L·w/2` subtraction, no cap and no discard, and the certificate is archived with exact decimals. Applied to
`R154_007`'s own certificate, the corrected verifier reproduces the auditor's `−1.6500·10⁻³`, which is the number this
round supersedes. **Still owed to `R154_007` and not done here** (out of compute, flagged for the next writer):
the `§8` text corruption (the `log 2` table is spliced into open item 1); the statement of the period residual
`3.24·10⁻³`; and the description of the contact set as an interval, which should read *comb* (§5 above).
`T = log 2` (E3) was **not** run: at `log 2` round 3's distance is `8.49·10⁻²` against a target `1.09·10⁻⁷`, six orders,
~~and the graded lemma does not help there — the second contact `log 3` is incommensurate with any lattice, so no `P`
makes the prime term periodic and `W_k` must worst-case both primes. That is the honest structural obstruction at
`log 2`, and it is unchanged.~~ **[amended 2026-09-21 per R154_016.** The sentence asserting a structural
obstruction at `log 2` is **withdrawn as false**. Lemma D2.3 above is already stated with `Σ_n v_n cos((x+kP)log n)`
over the full contact set, and its proof uses periodicity **only for `ν̂`** — which is a lattice measure we choose.
The prime term is never required to be periodic: it is evaluated *exactly* on the `N` shifted copies of one period
of `ν̂` and worst-cased only on `[τ₁+NP, ∞)`. D2.3 therefore holds verbatim for any finite frequency set, in
particular for the two contacts `{2,3}` of `½log3 < T ≤ log 2`. The obstacle at `log 2` is **quantitative, not
structural**: the distance at `M = 24`, measured at `T = 0.58` in round 5, is `3.20·10⁻³`, and the binding lever is
the atom budget `M`. Note also that D2.3 gives only `⟸` (the rows are a *sufficient* criterion; they are
conservative in `β` by `|β₀|k₀+|β₁|k₁ ≤ 2.1·10⁻²`), not `⟺`.**]**

---

## 7. Verdict table

| item | label |
|---|---|
| **Lemma D2.3** (graded periodic tail; one period of phases + `N` exact prime periods replaces `[τ₁,∞)`) | **`PROVED` (new)** — supersedes Lemma D2.1 |
| the `ρ`/`τ_max` lever saturates at `τ_max ≈ 160`; the binding lever is `M`, then the LP grid | `DIAGNOSTIC-NUMERIC` (table §2) |
| coarse-grid LP values are fictitious: `+1.68·10⁻⁴` is worth `−2.1·10⁻²` in truth | `DIAGNOSTIC-NUMERIC`, honest negative (§4, `G = 1`) |
| the block polish (`G+4` columns on a `10³×` finer grid) removes the discretisation error to `2·10⁻⁹` | **`PROVED` as a method** (its output is certified independently); the `G`-table is `DIAGNOSTIC-NUMERIC` |
| **`λ_min(A_{½log3}(w_ζ)) ≥ 4.4279281900·10⁻⁵ > 0`**, 437 atoms, `β₀ = 2.0025617`, `β₁ = −0.0096544`, `τ₁ = 30`, `P = 137.2608`, `N = 2`, `L = 647.4198`, `2.372·10⁸` evaluations, **0** unresolved intervals, `ε_fp = 10⁻⁸` justified to `8.2·10⁻¹³` | **`PROVED`** (machine-verified, archived, interval-audited) |
| `β₀ → 2` (the explicit formula's polar term) at a *certified* optimum | `DIAGNOSTIC-NUMERIC`, now on a proved object (`2.6·10⁻³`) |
| the contact set is a **comb**: a band in `[0,13]` plus one tail phase per family | `DIAGNOSTIC-NUMERIC` (corrects `R154_007 §4.2`'s "interval") |
| `T = log 2` | **not run**; ~~the `log 3` incommensurability blocks the graded lemma there~~ **[amended 2026-09-21 per R154_016: the incommensurability claim is withdrawn. D2.3 applies unchanged at two contacts; `log 2` is not run for compute reasons, and the measured lever is `M` (R154_015 §5.1). The `M`-sweep was attempted in round 6 and did not converge (R154_017 §4).]** |

**Precision of record.** `scipy` 1.11.4 HiGHS; LPs of `2.1·10⁴`–`3.0·10⁵` rows and `6`–`441` columns; cut grids
`2·10⁻⁵` (atom LP) and `5·10⁻⁶` (polish); B&B `w₀ = 0.02`, `w_min = 5·10⁻⁸`, 21 segments, 19 processes;
`mpmath` 1.3.0 at `iv.dps = 40`, `mp.dps = 60`.

**FATAL rule / no sign.** Positivity of `A_T` at `T = ½log3` is a fact already certified in Paper 42 by a Feshbach
argument; what is new here is an **independent, mesh-free, spectral-side proof of the same fact**, which is exactly what
the FATAL rule asks for. **No sign is claimed for `ζ` beyond `T ≤ log 2`.** No zero-free region, no moment input, no
`ζ`-zero data enters anywhere; the only inputs are `ψ`, `log 2`, `log 3` and linear programming.

## 8. Open (ranked)

1. Push `c` from `4.43·10⁻⁵` towards `9.89·10⁻⁴`: the lever is now `M` and `G` jointly (`M = 24, G = 128` is the first
   positive point; `M = 32`, `G = 256` is the next cell and is a ~4 h run).
2. A **rate** for Theorem D1 in the graded setting: `λ_min − D(U)` versus `d = 2T/M` and `τ₁`. §4's `G`-table suggests
   the polish converges linearly in `1/G`, which would make the construction closed-form.
3. **[amended 2026-09-21 per R154_016]** `T = log 2` needs **no new tail lemma**: D2.3 already covers any finite
   contact set (`R154_015 §2`, `R154_016`). What it needs is an atom budget `M` large enough for two contacts; the
   `M`-sweep at `T = 0.58` is the measurement, and it is `OPEN` (round 6 did not converge it, `R154_017 §4`).
   *(Superseded: the earlier text asking for "a tail lemma that survives two incommensurate contacts — a two-lattice
   `ν` with `ν̂ = ν̂_1 + ν̂_2` and a bound on `[τ₁,∞)` by simultaneous Diophantine approximation, not by periodicity"
   is withdrawn.)*
4. Replace the 437 machine numbers by a closed-form `a_j` (the profile decays smoothly from the window edge); that is
   the only route to a hand-checkable proof.

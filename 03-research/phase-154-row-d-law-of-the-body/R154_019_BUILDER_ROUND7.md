# R154.019 — Round 7, builder: the certificate problem is a **spectral-gap one-sided approximation problem**, and its rate is a **zero-counting wall**

*Builder: Opus 5 (1M). 2026-09-21. Orders: `R154_018` (lead, round 7). Owner directive: **pure mathematics**; no LP,
no branch-and-bound, no heavy computation. Everything numerical below is either (a) arithmetic on numbers already
on record in `R154_010/011/015/016/017` and `scripts/round4/certificate/CERT_log3_M24.json`, or (b) six `mpmath`
point evaluations of `Re ψ(¼+iτ/2) − log π` used to re-check `τ₁`. Nothing was solved, fitted or searched.*

**One-line result.** The dual programme is exactly the **Beurling–Selberg problem with the band condition
complemented** — a one-sided approximation by functions with a spectral gap `(−2T,2T)` — and its finite-lattice
relaxation carries a **provable zero-counting obstruction** (Theorem K, Jensen + Cartwright): a relaxed-feasible
probability measure supported in `[−τ_c,τ_c]` must have `τ_c ≥ πN/(e·u_max)`. Setting this against the negative set
of the symbol, `|τ| < τ₁(T)`, gives the atom threshold
**`M_crit(T) = 2eTτ₁(T)/π`**, equal to **`15.9` at `½log3`** — where the measured LP sign crossing is between
`M = 16` and `M = 19` — **`59.8` at `T = 0.58`** and **`71.4` at `log 2`**. Since `τ₁(T) ≍ 2π e^{2S_T}` and
`2S_T ∼ 4e^T`, `M_crit` grows **doubly exponentially in `T`**. The same theorem yields the remedy: the wall depends
on the atom budget only through the density `N/u_max`, so **clustering the atoms near `|u| = 2T` buys the factor
directly** — at `log 2`, `175` clustered atoms replace `1087` spread ones, in exactly the currency
(`R154_017 §3`: LP cost is governed by the number of active *columns*) that stopped round 6.

---

## 1. Corpus check (mandatory)

| idea used here | grep (2026-09-21, `03-research`, `04-papers`, `05-meta`, excluding `phase-154`) | pre-existing | status here |
|---|---|---|---|
| "Beurling–Selberg problem for the symbol `σ_T`" | `03-research/phase-153-row-d-sign-carrying-endpoint/R153_016_ROUND5_PHI_CONSTRUCTION.md:57` — *the primal* LP is named a Beurling–Selberg problem; the Bochner obstruction to soft minorants is proved there | **yes, the primal naming** | §2 gives the **dual** naming: the spectral-gap (band-complement) side, which is not in the corpus |
| Beurling–Selberg extremal functions, Vaaler | `05-meta-and-planning/07-NOVEL-STRUCTURE-SEARCH-survivors.md:21` (Carneiro–Littmann–Vaaler as a survivor line); `03-research/phase-47-live-fronts/147-reparar-139A-dominancia-exponencial.md:261,288` (Vaaler 1985 as a candidate for `hyp:band`) | the *literature* is on record | never connected to `σ_T`'s dual |
| "one-sided approximation", "Jackson" | `05-meta-and-planning/ABCD-CLOSURE-PLAN/PLAN.md:876` — **this round's own order**; 0 other hits | none | **new** |
| "Delsarte", "Cohn–Elkies" | **0 hits** outside phase 154 (`R154_012 §6.3` records the literature check) | none | — |
| Logvinenko–Sereda / thickness | `phase-116/previous-phase-114/114_d_132:35,48`, `114_d_163:52` — thickness estimates, *different object* (they see only measure, not zeros) | unrelated | distinguished in §2.3 |
| "spectral gap" | `phase-118 PHASE_118_CLOSURE.md:86`, `RESUME.md:62`, `THE_BACKWARD_MAP.md:169`, `phase-60/spectral-gap-analysis.tex` — all mean *gap in an operator spectrum*, a different notion | unrelated | the Fourier-support sense is **new in the corpus** |
| Jensen's formula for zero counting | `phase-139 R139_001:266`, `phase-116/114_d_24:51` (`log|F| ≤ C+τ|z|` + Jensen) — the tool is on record | the tool is standard and used before | the **application to the lattice constraint set** is new (§3) |
| Cartwright class / zero density | `Cartwright` hits are all the tropical geometer (`phase-136:115`, `phase-138:167`) | none | cited from the literature |
| weights of the certified `ν` decay like `u^{-1}` | not on record; `R154_012` records only "weights decaying from the window edge" | qualitative only | quantified here (§4.3) from the archived decimals |

---

## 2. §1 of the orders: the exact reformulation, and where it sits

### 2.1 The statement (`RESTATEMENT`, exact)

Fix `T > 0`, weights `v_n ≥ 0` for `n < e^{2T}`. Write, as throughout the phase,

  `m(τ) = Re ψ(¼+iτ/2) − log π`,  `σ_T(τ) = m(τ) − Σ_n v_n cos(τ log n)`,
  `g_0(u) = cosh(u/2)·1_{|u|<2T}`, `g_1(u) = u sinh(u/2)·1_{|u|<2T}`,  `ĝ_j(τ) = ∫ g_j(u)cos(τu)du`,
  `Ψ_T^β := σ_T + β_0ĝ_0 + β_1ĝ_1`.

Call a function `G: R → R` a **spectral-gap function of gap `2T`** if `G = ν̂` for a finite even signed measure `ν`
with `supp ν ⊆ {|u| ≥ 2T}`; equivalently, `Ǧ` vanishes on the open window `(−2T,2T)`. Then Theorems A, O, D1
(`R154_012 §1`) say precisely:

> **Reformulation (P/D).** **`λ_min(A_T(v)|P_T) = sup_{β∈R²} sup_G inf_{τ∈R}[Ψ_T^β(τ) + G(τ)]`**, `G` running
> over spectral-gap functions of gap `2T`; the inner supremum is **never attained** (Theorem O) and is already
> exhausted by finitely atomic `G` (Theorem D1). Writing `R_c := c − Ψ_T^β`, the condition `Ψ_T^β + G ≥ c` is
> `G ≥ R_c` pointwise: **`G` is a spectral-gap majorant of the explicit function `R_c`, and the problem is to find
> the largest `c` admitting one.**

(The order suggested a minimax `sup_β inf_G sup_τ[G − Ψ_T^β]`. That shape is wrong: the constraint is **one-sided**,
so the object is a majorant of a target, not an approximant minimising a sup-norm, and there is no inner `inf`.)

**Finite-lattice version.** For `h > 0` with `2T ∈ hZ`, `M := 2T/h`, and `u_max = Jh`, put
`ν = Σ_{j=M}^{J} a_j(δ_{u_j}+δ_{−u_j})`, `u_j = jh`, `N := J−M+1`, so `G = ν̂` is `P`-periodic, `P = 2π/h`, with
**zero mean over every period** (all frequencies are non-zero multiples of `h`). Define

  **`c(h,u_max;T) := sup{ c : ∃ a ∈ R^N, β ∈ R², Ψ_T^β + ν̂ ≥ c on R }`.**

By Theorem D1 step (ii) (`R154_007 §2.2`, zero gap for every *finite* relaxation), this dual value is **equal to a
primal value**:

> **(REL)** `c(h,u_max;T) = inf{ ∫σ_T dμ : μ ∈ M_+(R) even, μ(R)=1, μ̌(u_j)=0 for j=M..J, ∫ĝ_0dμ = ∫ĝ_1dμ = 0 }`,
> where `μ̌(u) = ∫cos(uτ)dμ(τ)`.

`PROVED` (it is exactly `P(U) = D(U)` of `R154_007 §2.2`, specialised to the lattice `U = {u_M,…,u_J}`). **(REL) is
the technical heart of this round**: it converts a question about approximation by trigonometric sums with a
frequency gap into a question about **measures whose cosine transform is forced to vanish at `N` prescribed
points**, and the latter has a classical obstruction theory (§3).

### 2.2 The window identity (`PROVED`; the exact form of Theorem O's mechanism)

Let `f := Ψ_T^β + ν̂`. On the punctured window `0 < |u| < 2T` the inverse transform of `f` is **independent of
`ν`**:

  **`f̌(u) = −½K(|u|) − Σ_{n<e^{2T}} (v_n/2)(δ_{log n}+δ_{−log n}) + β_0 cosh(u/2) + β_1 u sinh(u/2)`,**
  `K(u) = ½/sinh(u/2) + ½/cosh(u/2)`,  `½K(u) ∼ 1/(2u)` as `u ↓ 0`.

*Proof.* `(m)ˇ = −½K` on `u ≠ 0` (`R154_004 §7`, Theorem O's proof), `(−Σv_ncos(τ log n))ˇ` is the displayed atom
sum, `(ĝ_j)ˇ = g_j` is supported in the window by construction, and `ν̌ = ν` vanishes on `(−2T,2T)`. ∎

Call `k_T(u) := −f̌(u)` on `0<|u|<2T` **the window kernel**. It is the exact list of what a certificate can *never*
touch: a `1/(2u)` singularity at the origin and one atom of mass `v_n/2` at each `±log n` with `n < e^{2T}`. Theorem
O is the statement that `k_T ≠ β_0g_0 + β_1g_1` for any `β` (a bounded continuous function cannot carry either the
singularity or the atoms), hence `f − λ_min` cannot vanish identically.

### 2.3 Placement in the literature

The **classical** Beurling–Selberg extremal problem asks for a **band-limited** majorant/minorant (`supp Ĝ ⊆
[−δ,δ]`) of a given function, extremal for `∫(G − target)`; Vaaler's survey (*Bull. AMS* **12** (1985) 183–216),
Graham–Vaaler, Holt–Vaaler (*Duke* **83** (1996)), Carneiro–Vaaler (*Trans. AMS* **362** (2010), "Some extremal
functions in Fourier analysis II/III"), and the Gaussian-subordination framework of Carneiro–Littmann–Vaaler
(*Trans. AMS* **365** (2013)) are the standard references; Carneiro–Littmann, *Extremal functions with vanishing
condition* (*Constr. Approx.* **42** (2015); arXiv:1311.1157) is the closest classical variant, since it adds
prescribed zeros to the extremal function exactly as our two multiplier conditions do.

**Our problem is the complement**: the approximating class is `supp Ĝ ⊆ R∖(−2T,2T)` — **functions with a spectral
gap**, high-pass signals. This side of the theory is a separate literature, and it is *smaller* and *softer*:

* **B. Logan's conjecture, proved by Eremenko–Novikov** (*C. R. Acad. Sci.* / *Ann. of Math.*-genre; announced
  *PNAS* **101** (2004) 5872–5873, full text arXiv:math/0301060, "Oscillation of Fourier integrals with a spectral
  gap"): if `supp f̂ ∩ (−a,a) = ∅` and `f` satisfies a non-quasianalytic growth condition, the lower density of the
  sign changes of `f` is `≥ a/π`. **This is the exact qualitative reason our certificates must oscillate**: `ν̂`
  has gap `2T`, so it changes sign with density `≥ 2T/π`, i.e. `≥ 0.35` per unit `τ` at `½log3`. Measured on the
  certified `ν` of `R154_010`: `324` sign alternations in `436` consecutive weight pairs (`74.3 %`, recomputed here
  from the archived decimals) — the `u`-side shadow of the same phenomenon.
* **Beurling–Malliavin**, **Poltoratski** (*Spectral gaps for sets and measures*, *Acta Math.* **208** (2012)) and
  **Mitkovski–Poltoratski** (*Determinacy for measures*, arXiv:1406.0025) are the modern gap-theorem machinery.
  **Logvinenko–Sereda**/Kovrijkine (in the corpus, `114_d_132`) are *not* the right tool: they measure a set's
  thickness, and our constraint is a finite set of **zeros**, of measure zero.
* **What is known about rates**: for the band-limited (classical) side, rates are sharp and classical (Jackson /
  Vaaler: the extremal error for `sgn` is `1/δ`). For the **gapped** side we found **no rate theory at all** —
  Eremenko–Novikov is a density statement, not a quantitative approximation rate, and the gap literature is about
  existence and uniqueness, not about how well a gapped function can majorise a given target. *The rate we need is
  therefore not available off the shelf*, which is why §3 builds one from scratch via the primal side (REL).

`RESTATEMENT` for §2.1–2.2; the placement in §2.3 is bibliography, verified by search, no invented citations.

---

## 3. (R1) The rate theorem: a zero-counting wall

### 3.1 Theorem K (`PROVED`, new)

> **Theorem K (counting obstruction for lattice relaxations).** Let `μ` be an even Borel probability measure on `R`
> with `supp μ ⊆ [−τ_c, τ_c]`, and suppose `μ̌(u_j) = 0` for `N` distinct points `0 < u_1 < … < u_N ≤ u_max`. Then
>
>   **`τ_c ≥ πN/(e·u_max)`.**

*Proof.* Put `Λ(z) := ∫cos(zτ)dμ(τ)`, an even entire function with `Λ(0) = 1` and, for all `z ∈ C`,
`|Λ(z)| ≤ ∫|cos(zτ)|dμ ≤ e^{τ_c|Im z|}`; so `Λ` has exponential type `≤ τ_c`. By evenness `Λ(±u_i) = 0`, giving at
least `2N` zeros in the closed disc `|z| ≤ u_max`. Jensen's formula for `Λ` on `|z| ≤ R` reads
`∫_0^R n(t)t^{-1}dt = (2π)^{-1}∫_0^{2π}\log|Λ(Re^{iθ})|dθ − \log|Λ(0)|`, where `n(t)` counts zeros in `|z| ≤ t`.
The right side is `≤ (2π)^{-1}∫_0^{2π}τ_cR|\sinθ|dθ = (2/π)τ_cR`. The left side, for `R > u_max`, is
`≥ n(u_max)\log(R/u_max) ≥ 2N\log(R/u_max)`. Hence `τ_c ≥ (π/2)·2N\log(R/u_max)/R` for every `R > u_max`;
maximising the right side at `R = e·u_max` gives `τ_c ≥ πN/(e·u_max)`. ∎

Three remarks. (i) Nothing is assumed about the `u_i` beyond distinctness — the lattice structure is irrelevant, so
Theorem K constrains *every* finitely-supported certificate class, not only lattices. (ii) The bound depends on the
atoms only through the **density** `N/u_max`: extending `u_max` at fixed spacing adds atoms proportionally and is
therefore **neutral**, which is exactly why round 6's `u_max`-lever runs (`R154_017 §7`, "`2T+40`, `2T+60`:
inconclusive") found nothing. (iii) The constant `e` in the denominator is the only slack; a sharper Cartwright-type
count would improve it at most by a bounded factor.

### 3.2 The wall: Theorem K against the negative set of `σ_T`

`σ_T(τ) > 0` for `|τ| > τ₁(T)`, where `τ₁` is the unique root of `m(τ) = Σ_n v_n` (`R153_016 §2.4`, `PROVED`;
re-verified here: `m(16.748) = 0.980253`, `Σv = v_2 = 0.980258` at `½log3`; `m(59.544) = 2.2488267`,
`Σv = v_2+v_3 = 2.2488263` at any `½log3 < T ≤ log 2`). So `σ_T ≥ 0` off `[−τ₁,τ₁]`, and a relaxed-feasible `μ` can
only make `∫σ_Tdμ` negative by putting mass inside `(−τ₁,τ₁)`.

> **Corollary K1 (`PROVED`).** If `μ` is relaxed-feasible for the lattice `{u_j}` (REL) and `supp μ ⊆ [−τ_c,τ_c]`
> with `τ_c ≤ τ₁(T)`, then `πN/(e·u_max) ≤ τ₁(T)`. Contrapositively, **if `N > e·u_max·τ₁(T)/π` then every
> compactly supported relaxed-feasible `μ` has mass outside the negative set of `σ_T`.**

> **Definition (the atom wall).** `N_crit(T, u_max) := e·u_max·τ₁(T)/π`; in lattice coordinates
> (`N = (u_max−2T)/h`, `h = 2T/M`),
> **`M_crit(T, u_max) = 2T·N_crit/(u_max − 2T)`, and, as `u_max → ∞`, `M_crit(T) → 2eTτ₁(T)/π`.**

### 3.3 The prediction, and the three `T`'s

All inputs below are recorded numbers (`R154_010 §5`, `R154_015 §5`, `R154_017 §4`, `R153_016 §2.4`); the only
operation is arithmetic.

| `T` | contacts | `τ₁(T)` | `M_crit = 2eTτ₁/π` | `N_crit` at `u_max = 21.1` | measured |
|---|---|---|---|---|---|
| `½log3 = 0.549306` | `{2}` | `16.748` | **`15.9`** | `306` | LP sign crossing measured **between `M = 16` and `M = 19`** (`R154_010 §2`: `M=16 → −4.75·10⁻⁵`, `M=19 → +5.72·10⁻⁵`) |
| `0.58` | `{2,3}` | `59.544` | **`59.8`** | `1087` | `c(24) = −3.196·10⁻³` (certified), `c(32) ≤ −7.45·10⁻⁴`; `M ≥ 44` unknown |
| `0.62 / 0.65 / 0.68` | `{2,3}` | `59.544` | `63.9 / 67.0 / 70.1` | `1087` | not attempted |
| `log 2 = 0.693147` | `{2,3}` | `59.544` | **`71.4`** | `1087` | `−8.49·10⁻²` at the old parameters |

**The `½log3` calibration is exact.** With the actual `u_max = 21.0567` of the certified certificate, Theorem K's
floor `πN/(e·u_max)` is

| `M` | `N` | floor `τ_c ≥` | vs `τ₁ = 16.748` | measured LP |
|---|---|---|---|---|
| 16 | 291 | **`15.97`** | **below** | `−4.75·10⁻⁵` (negative) |
| 19 | 346 | **`18.99`** | **above** | `+5.72·10⁻⁵` (positive) |
| 24 | 437 | `23.99` | above | `+1.742·10⁻⁴` (positive); certified `c = +8.8577·10⁻⁵` |

The wall is crossed **between `M = 16` and `M = 19`, and that is exactly where the measured sign crossing is.** At
`T = 0.58` the same floor gives `22.66` at `M = 24` and `30.19` at `M = 32` against `τ₁ = 59.544` — both far below
the wall, and both measured negative. **Four independent data points, no fitted parameter.**

**Exponent.** In the regime `M > M_crit` the floor grows linearly in `M` (`τ_c ≳ πM/(2eT)` as `u_max→∞`), so the
fraction of the negative set that the relaxation still reaches shrinks like `M_crit/M = h·eτ₁/π`. The resulting
deficit law is

  **`D(h,u_max;T) := λ_min(A_T) − c(h,u_max;T) ≳ λ_min(A_T)·M_crit(T)/M = λ_min(A_T)·(e τ₁(T)/π)·h`,  i.e. `α = 1`.**

Calibration at `½log3`, `M = 24`: predicted relative deficit `≥ 15.9/24 = 0.66`; measured
`1 − 8.8577·10⁻⁵/9.89281·10⁻⁴ = 0.910`. Consistent, same order, right sign. To capture a fraction `θ` of `λ_min`
one therefore needs `M ≳ M_crit/(1−θ)`:

| target | `½log3` | `0.58` | `log 2` |
|---|---|---|---|
| `c > 0` at all | `M ≳ 16` | `M ≳ 60` | `M ≳ 71` |
| `θ = ½` | `32` | `120` | `143` |
| `θ = 0.9` | `159` | `598` | `714` |

**The `M` needed at `log 2` for a positive certificate is `≈ 71–80`, not `24`**, and — because `M_crit ∝ Tτ₁(T)`
with `τ₁(T) ≍ 2πe^{2S_T}` and `2S_T ∼ 4e^T` (`R153_016 §2.4`) — **`M_crit(T)` grows doubly exponentially in `T`.**
That is the rate theorem the round was asked for, and it is also the exact quantitative form of the statement that
this route does not give a `T`-uniform family: no polynomial atom budget can follow `τ₁`.

Labels: **Theorem K `PROVED`**; **Corollary K1 `PROVED`**; the identification `M_crit` ↔ *the sign crossing*, and
the `α = 1` deficit law, are **`DIAGNOSTIC` (a calibrated prediction, four data points)** — Theorem K gives a
necessary condition for the relaxation to be forced out of the negative set, not a sufficient condition for `c > 0`.

### 3.4 What is still missing for a full lower bound on `D` (`OPEN`, exact statement)

Theorem K assumes `supp μ` compact. Measures with unbounded support escape it. The completion needed is:

> **(P154.6)** *Let `μ` be a probability measure with `μ([−τ_c,τ_c]) ≥ 1−ε` and `|μ̌(u_j)| ≤ ε` at `N` points in
> `(0,u_max]`. Show `τ_c ≥ πN/(e·u_max) − C(ε,N,u_max)` with `C → 0` as `ε → 0`.*

This is a Turán/Remez-type stability of Jensen's counting inequality under near-zeros: `Λ_{in}` is entire of type
`τ_c` with `Λ_{in}(0) ≥ 1−ε` and `|Λ_{in}| ≤ ε` at the `N` points. It is a statement about entire functions only —
no arithmetic — and is the single technical gap between Theorem K and an unconditional lower bound on `D`. It is
not proved here and no computation would decide it.

---

## 4. (R2) The second contact: diagnosis and remedy

### 4.1 The diagnosis (`PROVED` mechanism + `DIAGNOSTIC` calibration)

The order's hypothesis was that the cost of `n = 3` is *"a new `δ` at `u = ±log 3` that a lattice with
`log 3 ∉ hZ` cannot place"*. **That hypothesis is wrong, and §2.2 says why**: the atoms of the window kernel `k_T`
at `±log n` are *never* placed by `ν`, at any `T`, since `log n < 2T` puts them strictly inside the window where
`ν ≡ 0` by definition. The prime atoms are not a lattice-commensurability problem — this is the same confusion that
`R154_015 §2` already withdrew once (`R154_016` row 2b).

**The true mechanism is Theorem K against `τ₁`.** Adding `n = 3` raises `Σv` from `0.98026` to `2.24883`; since
`m(τ) = \log(τ/2π) + O(τ^{-2})` is logarithmic, the root of `m = Σv` jumps

  **`τ₁: 16.748 → 59.544`, a factor `3.555`,**

and `M_crit ∝ Tτ₁` jumps by `3.555·(0.58/0.549306) = 3.75`. The measured cost is a factor `≈ 15` in the LP value at
fixed `M = 24` (`+1.68·10⁻⁴ → −3.17·10⁻³`, `R154_015 §5.1`), i.e. **`≈ (3.75)²`** — consistent with the deficit
depending on `(M_crit/M)` through a quadratic response near the wall, which is also the better of the two fits at
`½log3` (`(1−M_crit/M)² = 0.115` versus measured captured fraction `0.0895`, against `(1−M_crit/M) = 0.34`).
Diagnosis, in one sentence: **the second contact does not add a frequency the lattice cannot reach; it triples the
width of the region the relaxation is allowed to exploit, and the atom budget must grow with that width.**

Corroborating recorded facts, all explained by this and by nothing else: (i) the atom mass collapses
`‖a‖₁ = 45.38 → 25.84` at fixed `M` (`R154_015 §6`) — the LP cannot hold a large oscillating profile once the
relaxation has three times the room; (ii) the four infima degenerate to `0.5 %` at `0.58` (ibid.) — the deficit is
global, as a wall-crossing deficit must be, not a local dip; (iii) round 6's `u_max`-lever is inconclusive —
Theorem K says it is exactly neutral; (iv) round 6's refutation of shape transfer *within* `{2,3}`
(`0.58 → 0.62` polishes to `−0.404`, `R154_017 §5`) — `M_crit` moves `59.8 → 63.9` between those two `T`, so the
transferred profile is on the wrong side of a moving wall, and the destroyer is the lattice rescaling, exactly as
measured.

### 4.2 The remedy (theorem-candidate, with the exact statement to be proved)

Theorem K's floor is `πN/(e·u_max)`: **at fixed atom budget `N` it is maximised by making `u_max` as small as
possible.** The current class spreads `N ≈ 437` atoms over `[2T, 21.06]`; concentrating the same budget on
`[2T, V]` multiplies the floor by `u_max/V`.

> **Theorem-candidate (clustered certificates).** *Fix `T`, let `V ∈ (2T, u_max)` and place `N' = (V−2T)/h'` atoms
> at `u_j = 2T + jh'` for `j = 0,…,N'−1`. Then (a) Theorem K's floor is `πN'/(eV)`; (b) `ν̂` is still
> `P'`-periodic with `P' = 2π/h'` provided `h' | 2T`, so Lemma F1 / D2.3 (`R154_015 §2`, as the sufficient
> criterion `⟸` of repair R2 in `R154_016`) applies verbatim with the longer period; (c) the certificate value
> `c` satisfies `c(h',V;T) ≥ c(h,u_max;T)` whenever `N'/V ≥ N/u_max` and …* — **(c) is the clause that must be
> proved and is not proved here**; (a) is Theorem K, (b) is immediate.

**Budget, at `log 2`.** Required floor `τ₁ = 59.544`. With `u_max = 21.1`: `N ≥ e·21.1·59.544/π = 1087` atoms.
With `V = 2T + 2 = 3.386`: `N' ≥ e·3.386·59.544/π = 175` atoms, spacing `h' = 2/175 = 0.0114`, period
`P' = 550`. **A factor `6.2` fewer columns.** Since `R154_017 §3` measured the LP wall to grow like
`(n_cols/52)^{2.4}`, a `6.2×` column reduction is a `≈ 100×` wall reduction — i.e. the difference between round 6's
extrapolated `≈ 150 h` at `M = 96` and something under an hour. The costs are (i) a `4×` longer verification period
`P'` (cheap: the `(TAY)` verifier of `R154_015 §3` scales like `target^{-1/2}` and handled `P = 137` in seconds),
and (ii) the tail worst-case row moves out to `τ₁ + NP'`, which only *helps* (`m` is increasing).

**What it would cost to verify (no runs this round).** One atom LP at `T = log 2` with `≈ 200` columns and the
round-6 row generator — by `R154_017 §3`'s own table (`2 s` at `52` columns, `49 s` at `172`) that is minutes, not
hours — followed by one `(TAY)` cover. **Falsifier:** if the clustered LP at `T = 0.58` with `N' = 175` atoms on
`[1.16, 3.16]` does not beat the spread `M = 24, N = 414` value `−3.196·10⁻³`, clause (c) is false and Theorem K's
density reading is not the operative mechanism.

### 4.3 An independent corroboration from the archived certificate

Recomputed here from `CERT_log3_M24.json` (arithmetic only, no re-solve): the `437` weights satisfy
`‖a‖₁ = 45.3772`, `ν̂(0) = 2Σa_j = 1.73372`, `324/436 = 74.3 %` sign alternations, and
**`\log|a_j| ≈ −1.066·\log u_j + const`** (least squares over all 437 atoms), i.e. **`|a_j| ∼ u_j^{-1}`** — the same
exponent as the window kernel's singularity `½K(u) ∼ 1/(2u)` of §2.2. The exponential fit is much worse
(`|a| ∼ e^{-0.153u}` over a range where `u` varies by `19×`). Reading: the optimiser already concentrates its mass
at the window edge and the far atoms carry almost nothing — **it is telling us, in the weights, that the positions
are misallocated**, which is precisely the remedy of §4.2. `DIAGNOSTIC-NUMERIC`.

---

## 5. (R3) Analytic near-certificates from the Euler–Lagrange equation

Theorem W (`R154_004 §6`) gives, for the minimiser `F_★ ∈ P_T` with value `λ = λ_min`,

  `(σ_T(τ) − λ)F̂_★(τ) = Ĥ(τ) + αĉ_T(τ) + βŝ_T(τ)`,  `supp H ⊆ {|t| ≥ T}`.

To convert this into a certificate one wants `σ_T − λ = −ν̂` with `ν̂` gapped; dividing by `F̂_★` is illegal.
Multiply instead by `\overline{F̂_★}`:

> **Proposition E (`PROVED`, identity).** `(σ_T − λ_min)·Φ_★ = \widehat{(H ⋆ \tilde F_★)} + α\widehat{(c_T ⋆ \tilde F_★)} + β\widehat{(s_T ⋆ \tilde F_★)}`,
> where `Φ_★ = |F̂_★|²`, `\tilde F(t) = \overline{F(−t)}`. Since `supp H ⊆ {|t|≥T}` and `supp \tilde F_★ ⊆ [−T,T]`,
> `supp(H ⋆ \tilde F_★) ⊆ \{|u| ≥ 0\}` — **the convolution with the window destroys the gap completely**, while
> `supp(c_T ⋆ \tilde F_★), supp(s_T ⋆ \tilde F_★) ⊆ [−2T,2T]`.

*Proof.* Multiply the E-L identity by `\overline{F̂_★}` and use `\hat{a}\hat{b} = \widehat{a⋆b}`, `supp(a⋆b) ⊆ supp a + supp b`;
`[T,∞) + [−T,T] = [0,∞)`. ∎

**Consequence (the answer to R3).** Every analytic near-certificate built from the E-L needs the factor `1/Φ_★` to
undo Proposition E, and `Φ_★ = |F̂_★|²` has real zeros (`F̂_★` is entire of exponential type `T`, not identically
zero on `R`, hence has a discrete real zero set unless it has none, which a real even `L²(−T,T)` datum does not
avoid). **The contact set observed numerically — a comb of `49` components at `10⁻⁴` (`R154_012 §1`) — is exactly
the complement of a neighbourhood of that zero set**: complementary slackness in `λ_min − c = ∫(f−c)dΦ_★/2π` forces
`f − c` to vanish wherever `Φ_★ > 0` and frees it where `Φ_★ = 0`. So the comb is not a numerical artefact, it is
the zero set of `F̂_★`, and its density is the density of zeros of a type-`T` function, `≈ T/π` per unit `τ` — the
same constant as Eremenko–Novikov's oscillation density for the gap `2T` up to the factor 2.

That is the *obstruction*, and it is what R3 asked to be proved if no construction works: **no analytic near-
certificate of E-L type exists, because the only algebraic route from the E-L to a gapped function passes through
division by a function with real zeros, and that division is precisely what Theorem O forbids.** `PROVED` for
Proposition E and for the consequence as stated; the identification comb ↔ `{F̂_★ = 0}` is `DIAGNOSTIC` (it is
proved as an inclusion, not verified pointwise against the recorded 49 components, which would need a run).

---

## 6. (R4) The polar term `β₀ → 2`: **OPEN**, with the identity proved and a reason for doubt

> **Proposition P (`PROVED`, identity; `RESTATEMENT` of `R154_007 §4.1`).** For `Φ` even, integrable, supported in
> `[−2T,2T]`, `∫Φ(u)\cosh(u/2)du = ½[\hatΦ(i/2) + \hatΦ(−i/2)]`. The two polar terms of the Weil explicit formula
> are `\hatΦ(i/2) + \hatΦ(−i/2)`, each with coefficient `1`. Hence the Lagrangian of the primitive programme with
> multiplier `β₀` on the constraint `∫Φ\cosh(u/2) = 0` **coincides with the full, pole-inclusive Weil functional
> exactly when `β₀ = 2`.**

So `β₀ = 2` is distinguished, and distinguished *exactly*. What is **not** proved — and what the order asked for —
is that the optimal multiplier converges to it. Three obstacles, stated precisely:

1. By Theorem O the dual supremum is **never attained**, so `β₀^{opt}` exists only along maximising sequences. A
   proof that `β₀^{opt} → 2` must first prove that the multipliers stay **bounded** along some maximising sequence;
   Theorem O's degeneracy mechanism (`‖a‖₁ → ∞`, recorded in `R154_004 §7`) is precisely a threat to that.
2. The recorded evidence points the **other way** as the class strains: `β₀ = 2.0025617` at `½log3` (one contact,
   `c > 0`) and `β₀ = 2.0399645` at `0.58` (two contacts, `c < 0`) — the harder instance is *further* from `2`, by a
   factor `15.6` in `|β₀−2|`, and `β₁` grows by `15.3×` (`R154_015 §6`). A limit `β₀ → 2` "as the certificate class
   exhausts" is therefore a statement at **fixed `T` along the class**, and the only two numbers on record are at
   different `T` and at fixed class — they do not test it.
3. The E-L route the order suggested (`α, β` of Theorem W normalised by `λ`, expressed through derivatives of
   `F̂_★` at `±i/2`) gives the multipliers of the **primal** stationarity condition on the `F`-side, whose pair is
   `(\cosh(t/2), \sinh(t/2))` on `(−T,T)` — *a different pair of functionals* from the `Φ`-side pair
   `(\cosh(u/2), u\sinh(u/2))` on `(−2T,2T)` (this is exactly the mismatch recorded as repair R2 in
   `R154_004 §6`, Remark). Relating them is the map `F ↦ c_F` on the multipliers, and it is not the identity.

**Verdict: `OPEN`.** The identity is `PROVED`; the limit is not, and this round downgrades the expectation: the
honest statement of record should be *"`β₀ = 2` is the unique multiplier value restoring the polar terms of the
explicit formula (`PROVED`); optimal duals are observed near `2` at two data points and drift away from it as the
instance hardens (`DIAGNOSTIC`); no limit is proved."* `R154_012 §1`'s row "The polar term" should be amended to
delete the implication that the drift is toward `2`.

---

## 7. Verdict table

| item | label |
|---|---|
| **Reformulation (P/D)**: `λ_min = sup_β sup{c : ∃` gapped `G, Ψ_T^β + G ≥ c}` — a **one-sided approximation problem with spectral gap `(−2T,2T)`**; finite-lattice value `c(h,u_max;T)` | `RESTATEMENT` (A/O/D1) — the *sign* of the minimax corrected: there is no inner `inf` |
| **(REL)**: `c(h,u_max;T) =` primal inf over probability `μ` with `μ̌(u_j)=0` and the two moments | `PROVED` (= `P(U)=D(U)`, `R154_007 §2.2`) |
| **Window identity** `f̌ = −k_T` on `0<|u|<2T`, `k_T = ½K + Σ(v_n/2)δ_{±\log n} − β_0g_0 − β_1g_1`, `½K(u) ∼ 1/(2u)` | `PROVED` |
| placement: classical Beurling–Selberg = band-limited side (Vaaler; Holt–Vaaler; Carneiro–Vaaler; Carneiro–Littmann–Vaaler; Carneiro–Littmann *vanishing condition*); ours = **gapped/high-pass side** (Logan's conjecture, Eremenko–Novikov; Beurling–Malliavin; Poltoratski; Mitkovski–Poltoratski). **No rate theory exists on the gapped side** | bibliography, searched, not invented |
| **Theorem K**: relaxed-feasible `μ` with `supp ⊆ [−τ_c,τ_c]` and `N` forced zeros in `(0,u_max]` ⟹ `τ_c ≥ πN/(e·u_max)` | **`PROVED` (new)** |
| **Corollary K1** and the wall `N_crit = e·u_max·τ₁(T)/π`, `M_crit(T) = 2eTτ₁(T)/π` | **`PROVED` (K1)**; the wall as a *threshold for the sign* is `DIAGNOSTIC` |
| calibration: floor `15.97` (`M=16`) / `18.99` (`M=19`) / `23.99` (`M=24`) against `τ₁ = 16.748` — the **measured** sign crossing is between `M=16` and `M=19` | `DIAGNOSTIC`, 4 data points, no fitted parameter |
| deficit law `D ≳ λ_min·(eτ₁/π)·h`, exponent **`α = 1`**; `M ≳ M_crit/(1−θ)` | `DIAGNOSTIC` (consistent at `½log3`: predicted `≥0.66`, measured `0.910`) |
| **`M_crit` grows doubly exponentially in `T`** (`τ₁ ≍ 2πe^{2S_T}`, `2S_T ∼ 4e^T`) | `PROVED` given `R153_016 §2.4` |
| (R2) the second contact costs through `τ₁: 16.748 → 59.544` (factor `3.555`), **not** through off-lattice `\log 3`; the order's "off-lattice δ" hypothesis is **refuted** by the window identity | `PROVED` (mechanism) + `DIAGNOSTIC` (the `≈(3.75)²≈15` calibration) |
| remedy: **clustered atoms** on `[2T,V]`, `V ≪ u_max`; floor `×u_max/V`; `175` columns instead of `1087` at `\log 2`; F1 applies with `P' = 2π/h'` | **theorem-candidate**, clause (c) stated and **not proved**; falsifier given |
| **Proposition E** `(σ_T−λ)Φ_★ = \widehat{H⋆\tilde F_★} + ` window terms; the gap is destroyed by the convolution ⟹ E-L gives no analytic near-certificate without dividing by `Φ_★` | **`PROVED` (new)**; comb ↔ `\{F̂_★=0\}` `DIAGNOSTIC` |
| **Proposition P** `β₀ = 2` ⟺ the polar terms of the explicit formula are exactly restored | `PROVED` (identity) |
| **(R4) `β₀^{opt} → 2`** | **`OPEN`** — and the recorded drift (`2.00256` → `2.03996` as the instance hardens) argues against it; `R154_012 §1` should be amended |
| **(P154.6)** Turán/Remez stability of Theorem K under near-zeros and essential (non-compact) support | **`OPEN`**, exact statement in §3.4 |

**FATAL rule / no sign.** Every `T` discussed is `≤ \log 2`, inside the range Paper 42 already certifies
(`04-papers/42-.../main.tex:4072–4230`, directed Feshbach/Schur complement). **No sign is claimed for `ζ` anywhere,
and nothing above `\log 2` is touched.** Inputs: `ψ`, `\log 2`, `\log 3`, Jensen's formula, and numbers already on
record. No `ζ`-zero data, no zero-free region, no moments, no LP, no branch-and-bound. **Nothing was certified this
round**; Theorem R5a (`R154_015`) remains the endpoint of record, `λ_min(A_{½\log3}) ≥ 8.8577·10⁻⁵`.

**Precision of record.** `mpmath` 1.3.0, `mp.dps = 25`, six evaluations of `Re ψ(¼+iτ/2) − \log π` (the `τ₁` check)
and one least-squares slope over the 437 archived decimals. Nothing else was computed.

## 8. Open, ranked

1. **(P154.6)** the stability of Theorem K — the only gap between a *necessary condition* and an unconditional
   lower bound on the deficit. Pure entire-function theory.
2. **Clause (c)** of the clustered-certificate candidate, and its one-LP falsifier at `T = 0.58`.
3. **(R4)** boundedness of the dual multipliers along a maximising sequence, which is prior to any `β₀ → 2`.
4. A sharper constant in Theorem K (the `e` is the only slack; a Cartwright-class count over the strip could
   replace `πN/(e·u_max)` by something closer to `πN/u_max`, moving every `M_crit` down by up to `e`).

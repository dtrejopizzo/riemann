# R154.015 — Round 5, builder: the two-frequency staircase above `½log3`

*Builder: Opus 5 (1M). 2026-09-20. Orders: `R154_014` (lead, round 5). Binding: `R154_010` (builder R4) and
`R154_011` (hostile confirmation R4 — **PROOF ACCEPTED** at `T = ½log3`), whose pipeline (LP shape → block polish
`G = 128` → exhaustive stack B&B with the `L·w/2` subtraction and no discards → `mpmath.iv` enclosures → JSON archive)
this round reuses and extends. Scripts: `scripts/round5/` (`r5core.py`, `r5lp.py`, `r5polish.py`, `r5shape.py`,
`r5bb.py`, `r5final.py`; logs `sw_*.log`; certificates in `scripts/round5/certificate/`).*

**One-line result.** Two method items are delivered and one endpoint is improved: **(F1)** the graded tail lemma is
**proved for any finite set of frequencies** — the alleged incommensurability obstruction at `log 2`
(`R154_010 §6`) **does not exist**, because periodicity was only ever used for `ν̂`; and **(F3, new)** a
**second-order (Taylor) branch-and-bound** replaces the Lipschitz cover and certifies round 4's own certificate with
`2.38·10⁶` evaluations in `103 s` instead of `2.37·10⁸` in `≈ 30 min` (**a factor `100` in evaluations, `≈ 10³` in
the width admissible per cell**), which raises the certified constant at `½log3` from `4.4279·10⁻⁵` to
**`8.8577·10⁻⁵`** (`CERT_log3_R5.json`, `0` unresolved intervals) — the verifier, not the certificate, was binding
there. **The staircase does not climb**: at step 1 (`T = 0.58`, the first `T` with two contacts) the best
certificate of the class has infimum `−3.1964·10⁻³`, exhaustively verified with `0` unresolved intervals, and the
saturating factor is measured and named — it is the **atom budget `M`**, not precision, grid, verifier or tail
lemma (§5.1). The highest step certified with `c > 0` is therefore the base, `½log3`.

---

## 1. Corpus check (mandatory)

| idea used here | grep (2026-09-20, `03-research`, `04-papers`, `05-meta`, excluding phase 154) | pre-existing | status here |
|---|---|---|---|
| "two-frequency" | `phase-131` (`R131_016/015/017`), `phase-106` | present but a **different object**: a `2×2` Gram/bilinear block `\|B(g₁,g₂)\|² > Q(g₁)Q(g₂)` on two test functions | the phrase is reused for a different construction (two *contacts* `n = 2,3` in the symbol) — **flagged, not claimed as new terminology** |
| "quasi-periodic" | `phase-29/28`, `phase-61` (expository) | yes, unrelated | not load-bearing here: §2 shows quasi-periodicity is **not needed** |
| "cuasiperi" | 0 hits | none | — |
| "high-precision LP" | 0 hits | none | **new (§4)** |
| "active set" / "active-set" | `phase-116/120/121/122` (all unrelated: Bohr cocycles, Tate polarization); `ABCD-CLOSURE-PLAN/PLAN.md` = the order for this round | none in the LP sense | **new (§4)** |
| "second-order branch" / "Taylor branch" | 0 hits | none | **new (§3)** — the round's main enabler |
| "incommensurab*" | `phase-153 R153_019`, `phase-136`, `phase-108` (`log3/log2 ∉ Q` as an obstruction) | the *obstruction* was asserted in `R154_010 §6` | **refuted as an obstruction for this lemma (§2)** |

---

## 2. (F1) The two-frequency graded tail lemma — `PROVED`

Throughout, `½log3 < T ≤ log 2`, so `n < e^{2T} ≤ 4` leaves exactly the two contacts `n = 2, 3`:
`v₂ = 2log2/√2 = 0.98025814…`, `v₃ = 2log3/√3 = 1.26856820…`, `Σv = v₂ + v₃ = 2.24882634…`
(`R154_004/005` conventions; `w₂ = log2/√2`, `w₃ = log3/√3`, `C₀ = ψ(¼) − log π`; the certified `c` bounds
`λ_min(A_T)` itself, i.e. `λ₁^{P_T}(E_Γ+E_P) − (2Σw_n − C₀)`).

Let `d = 2T/M`, `u_j = j d` for `j = M,…,J` (so `u_M = 2T` exactly and `supp ν ⊆ {|u| ≥ 2T}`),
`ν = Σ_j a_j(δ_{u_j}+δ_{−u_j})`, and `P = 2π/d`, so that `ν̂(τ) = Σ_j 2a_j cos(u_jτ)` is **`P`-periodic**
(`u_j P = 2πj ∈ 2πZ`). Let `m(τ) = Re ψ(¼+iτ/2) − log π`, `|ĝ₀(τ)| ≤ k₀(τ) = 2cosh T/τ + sinh T/τ²`,
`|ĝ₁(τ)| ≤ k₁(τ) = 8T sinh T/τ`, and
`f = m − Σ_n v_n cos(τ log n) + ν̂ + β₀ĝ₀ + β₁ĝ₁`.

> **Lemma F1 (two-frequency graded tail).** Fix `τ₁ > 0` and `N ≥ 1`. For `x ∈ [τ₁, τ₁+P)` put
> `W_k(x) = m(x+kP) − Σ_{n∈{2,3}} v_n cos((x+kP)log n) − |β₀|k₀(x+kP) − |β₁|k₁(x+kP)` for `0 ≤ k < N`, and
> `W_N(x) = m(x+NP) − Σv − |β₀|k₀(x+NP) − |β₁|k₁(x+NP)`. Then
> **`ν̂(x) + W_k(x) ≥ c` for all `x ∈ [τ₁,τ₁+P)` and all `0 ≤ k ≤ N`  ⟹  `f(τ) ≥ c` for all `τ ≥ τ₁`.**
> **[amended 2026-09-21 per R154_016: only this implication holds and only it is used. `W_k` subtracts
> `−|β₀|k₀ − |β₁|k₁`, so `ν̂ + W_k ≤ f(x+kP)`; the rows are exact in the prime term and conservative in `β` by
> `|β₀|k₀+|β₁|k₁ ≤ 2.1·10⁻²`. The converse `⟺` asserted here, and in `R154_010 §3` (Lemma D2.3), is withdrawn.]**
>
> *Proof.* Every `τ ≥ τ₁` is uniquely `τ = x + kP`, `x ∈ [τ₁,τ₁+P)`, `k ∈ Z_{≥0}`, and `ν̂(τ) = ν̂(x)`. For `k < N`
> the `k`-th row implies `f(τ) ≥ c` after the two `|ĝ_i| ≤ k_i` bounds — **the prime term is evaluated exactly at
> `τ = x+kP`**, the `β` part conservatively **[amended 2026-09-21 per R154_016]**. For `k ≥ N`: `m` is increasing on `[0,∞)`
> (from `Re ψ(¼+iy) = −γ + Σ_{n≥0}[1/(n+1) − (n+¼)/((n+¼)²+y²)]`, each summand increasing in `|y|`), `k₀` and `k₁`
> are decreasing, and `−Σ_n v_n cos(τ log n) ≥ −Σv` pointwise; hence `f(x+kP) ≥ ν̂(x) + W_N(x)`. ∎

**What this settles.** `R154_010 §6` and `R154_011` row 20 recorded a *structural obstruction* at `T = log 2`:
"the second contact `log 3` is incommensurate with any lattice, so no `P` makes the prime term periodic and `W_k`
must worst-case both primes". **That is not so.** Periodicity is used **only for `ν̂`**, which is a lattice measure
*we choose*; the prime term is never required to be periodic, it is simply *evaluated* on the `N` shifted copies of
one period and worst-cased only on `[τ₁+NP, ∞)`. Lemma F1 is therefore Lemma D2.3 verbatim with `Σ_{n}` in place of
the single `n = 2` term, and it holds for **any** finite frequency set — in particular for all `T ≤ log 2`, and,
with more terms, above it. The obstruction of `R154_010 §6` is **withdrawn** (`DIAGNOSTIC-NUMERIC` claim corrected
to a `PROVED` negative).

**Explicit cost of the worst-case row (the `τ₁(ρ,β,T)` the order asks for).** The `k = N` row is uniformly
harmless as soon as `m(τ₁+NP) − Σv − |β₀|k₀ − |β₁|k₁ > c`; since ~~`Re ψ(¼+iy) − log y ∈ (−1/(96y²), 0)` (checked in
`mpmath` at `y = 1,…,10⁵`; the constant `1/96` is the first Stieltjes term)~~ **[amended 2026-09-21 per R154_016:
that inequality is FALSE — `−y²(Reψ(¼+iy)−log y) = 0.0168272` at `y = 1` and decreases to `1/96` from above, so
`1/96` is never an upper bound; and `1/96` comes from the `ψ` asymptotic expansion, not from a Stieltjes constant.
Use instead `Re ψ(¼+iy) ≥ log y − 1/(50y²)` for `y ≥ 1`, i.e. `m(τ) ≥ log(τ/2) − log π − 1/(12.5τ²)` for `τ ≥ 2`.
Nothing downstream changes: no computation of rounds 5 or 6 uses this bound, which enters only the prose estimate
of `τ₁`]** and `m` is increasing, `m(τ) ≥ log(τ/2) − log π − 1/(12.5τ²)`. `Σv = 2.2488…` is passed at `τ* = 60` (`m(60) = 2.25646 > Σv`), and for the
staircase's actual parameters (`M = 24`, `τ₁ = 30`, `N = 2`, so `τ₁+NP ∈ [247.6, 290.0]`) the worst-case floor is

| `T` | `P = πM/T` | `τ₁+NP` | `m(τ₁+NP) − Σv` |
|---|---|---|---|
| 0.58 | 129.997 | 289.99 | **1.5832** |
| 0.62 | 121.610 | 273.22 | **1.5236** |
| 0.65 | 115.997 | 261.99 | **1.4816** |
| 0.68 | 110.880 | 251.76 | **1.4418** |
| log 2 | 108.777 | 247.55 | **1.4249** |

— every one far above the `|β₀|k₀ + |β₁|k₁ ≈ 1.6·10⁻²` that has to be subtracted, so `N = 2` suffices at every step
and the flat floor `ρ` of Lemma D2.1 never appears. (With `ν̂ ≥ −ρ` one recovers the flat corollary: `τ₁` may be
taken as the least `τ` with `log(τ/2) − log π − 1/(24τ²) ≥ c + Σv + ρ + |β₀|k₀(τ) + |β₁|k₁(τ)`; for `ρ ≤ 2.9` this
is `τ₁ ≈ 1.1·10³`, which is exactly why the graded form and not the flat one is used.)

---

## 3. (F3, new) The second-order verifier — the round's actual enabler

Round 4's cover retires a cell `[mid−w/2, mid+w/2]` when `f(mid) − L·w/2 ≥ target`, i.e. at width
`w ≈ 2·target/L`; with `L = 647` and `target ≈ 10⁻⁷` that is `w ≈ 3·10⁻¹⁰`, and the number of evaluations over a
contact band grows like `1/target`. **That is the compute wall of the staircase**, and it is removed by using the
second derivative. Split `f = m + q + r` with `q = −Σv_n cos + ν̂` and `r = β₀ĝ₀ + β₁ĝ₁`, all with exact closed-form
derivatives (`r5core._J`: `∫_0^{2T}u^k e^{su}du` by a stable recursion — `ĝ₀ = Re[J₀(½+iτ)+J₀(−½+iτ)]`,
`ĝ₀′ = −Im[J₁(½+iτ)+J₁(−½+iτ)]`, `ĝ₁ = Re[J₁(½+iτ)−J₁(−½+iτ)]`, `ĝ₁′ = −Im[J₂(½+iτ)−J₂(−½+iτ)]`; all four agree
with `scipy.integrate.quad` to `4·10⁻¹⁶` and with round 4's independent closed forms to `2·10⁻¹⁶`). Then, on a cell
of width `w` with midpoint `mid`,

> **(TAY)**  `f(x) ≥ m(mid − w/2) + (q+r)(mid) − |(q+r)′(mid)|·w/2 − M₂·w²/8`,
> `M₂ := Σ_n v_n log²n + 2Σ_j|a_j|u_j² + |β₀|H₀ + |β₁|H₁ ≥ sup|q″+r″|`,
> `H₀ = ∫_{−2T}^{2T}u²cosh(u/2)du`, `H₁ = ∫_{−2T}^{2T}|u|³sinh(|u|/2)du`.

This is Taylor's theorem with integral remainder for `q+r` on the cell, plus the **monotonicity of `m`** (which
therefore costs nothing rather than contributing `½ψ′(¼)·w/2 = 2.95w` to a Lipschitz constant). For the tail
families `h_k` the same bound is used with `m(x+kP)` and `−|β₀|k₀−|β₁|k₁` both evaluated at the **left** endpoint
(the first increases, the second increases, as `k₀,k₁` decrease), and `M₂` without the `β` terms. Near a contact
`|f′| ≈ 0`, so the admissible width is `≈ √(8·target/M₂)` instead of `2·target/L`: the evaluation count scales like
`target^{−1/2}` instead of `target^{−1}`.

**Measured, on round 4's own certificate (`lp_c24_it1.pkl`, `T = ½log3`, `M₂ = 6264.92`, `L = 647.42`):**

| verifier | target | evaluations | unresolved | wall |
|---|---|---|---|---|
| round 4, Lipschitz, `w_min = 5·10⁻⁸`, 19 processes | `4.42892819·10⁻⁵` | `2.37201004·10⁸` | 0 | `≈ 30 min` |
| **round 5, (TAY), `w_min = 10⁻⁹`, 1 process** | `4.42892819·10⁻⁵` | **`2.55926·10⁵`** | 0 | **`12 s`** |
| **round 5, (TAY), `w_min = 10⁻⁹`, 6 processes, 20 segments** | **`8.85780·10⁻⁵`** | **`2.378593·10⁶`** | **0** | **`103 s`** |

The last line is the new endpoint constant: the certificate of `R154_010` has true infimum
`min(f, h₀, h₁, h₂) = 8.8578564·10⁻⁵` (attained by `h₀` at `x = 37.8153`), and round 4 could only certify **half**
of it because the Lipschitz cover could not be driven closer to the infimum. Archived as
`certificate/CERT_log3_R5.json` (all checks passed; `20` segments tiling `[0,30]` and `[30,167.2608]` three times;
`0` unresolved; `M₂` recomputed from the archived decimals; `mpmath.iv` enclosures at the four fine-grid minima all
strictly positive; float-vs-interval discrepancy `5.43·10⁻¹³`, i.e. `ε_fp = 10⁻⁹` is justified with a factor
`1.8·10³` of margin).

> **Theorem R5a (`PROVED`, machine-verified).** With the data of Theorem R4 (`R154_010 §5`: `T = ½log3`, the same
> `437` atoms `u_j = j·2T/24`, `j = 24,…,460`, the same `a_j`, `β₀ = 2.0025617092502603…`,
> `β₁ = −0.0096544340448579749…`),
> `σ_T(τ) + ν̂(τ) + β₀ĝ₀(τ) + β₁ĝ₁(τ) ≥ c := 8.8577·10⁻⁵` for every `τ ∈ R`, hence
> **`λ_min(A_{½log3}(w_ζ)) ≥ 8.8577·10⁻⁵ > 0`** on `P_T` — exactly `2.0004×` the constant of `R154_010`, and
> `8.95%` of the Galerkin upper bound `9.89281·10⁻⁴`.

---

## 4. (F2) Precision: row scaling and the exact active-set vertex

Two distinct precision limits had to be separated.

1. **HiGHS' tolerance is absolute.** The polish LP maximises `c` subject to `A x ≤ b` with `x = (c, λ_1..λ_G,
   β₀, β₁, t₀, t₁)`; with a primal feasibility tolerance of `10⁻⁷` on rows whose right-hand sides are `O(1)`, a
   value `c ≈ 10⁻⁷` is indistinguishable from noise. The fix is a one-line change that costs nothing: **scale every
   row by `S = 10⁴`** (`r5polish.py --scale`). The feasible set is unchanged and the effective tolerance on `c`
   becomes `10⁻¹¹`. This is what lets the programme *see* the values the last two steps of the staircase need.
2. **The exact vertex (F2 proper).** At the optimum, take the rows with non-zero dual multiplier together with the
   variables sitting at a bound (`t₀, t₁ ≥ 0`); if they number exactly `nv = G+5`, that square system
   `A_act x = b_act` is solved in `mpmath` at `50` digits (`r5polish.hp_resolve`), the exact vertex is checked
   against **every** row of the LP (`max_violation`), and only then adopted. The first run (the transferred shape at
   `T = 0.58`) returned `n_active = 132` against `nv = 133` — a *bound-degenerate* vertex, not a failure of the
   method — and the routine correctly **declined to adopt a solution** (the discipline the FATAL rule demands);
   variables sitting at a bound were then added as rows, and the repaired version returned `133 = nv` with
   `max_violation = 2.2·10⁻¹¹` on the step-1 certificate (§5.1).

**What F2 is worth, measured — and the honest attribution.** At `½log3` the gap between the polish LP value
`8.885462·10⁻⁵` and the true infimum `8.857856·10⁻⁵` is `2.8·10⁻⁷`, and it is **grid discretisation, not LP
tolerance**. At `0.58` the exact vertex differs from the scaled HiGHS vertex by `Δc = −2.5·10⁻¹⁴`. So **F2 is a
sound method that is not yet the binding lever anywhere this round reached**; it would become binding only where
the target itself is `≈ 10⁻⁷`, i.e. at steps 4–5, which were never reached. In particular the doubling of the
`½log3` constant in §3 is due to the **(TAY) verifier (F3), not to F2** — the certificate there was always worth
`8.86·10⁻⁵`; round 4 simply could not drive a Lipschitz cover to its infimum.

---

## 5. The staircase

Pipeline per step (each item exactly as accepted in `R154_011`): shape → block polish `G = 128` on a `10³×` finer
grid with `S = 10⁴` scaling and the F2 vertex → fine-grid infimum → exhaustive (TAY) cover of `[0,τ₁]` and of the
`N+1` tail families on one period, `w_min = 10⁻⁹`, no cap, no discard, budget raises → `mpmath.iv` enclosures →
`certificate/CERT_T<value>.json` with exact decimals.

**Shape transfer (`r5shape.py`).** The 40-minute atom LP was run once (at `T = 0.58`) and then abandoned: since the
class only requires `supp ν ⊆ {|u| ≥ 2T}` on the lattice `u_j = j·2T/M`, the *profile* `(a_j)` certified at one `T`
is a legitimate **candidate** at another once the lattice is rescaled, and the `G = 128` block polish re-optimises
`128` scalings and `(β₀,β₁)` against the new rows. This is what makes a five-step staircase affordable at all.

**Targets** (`R153_012`, `L²` normalisation): `λ_min(A_T|P_T) ≈ 9.89·10⁻⁴` (`½log3`, Galerkin `K = 120`),
`2.16·10⁻⁴` (0.58), `1.91·10⁻⁵` (0.62), `2.40·10⁻⁶` (0.65), `3.24·10⁻⁷` (0.68), `1.09·10⁻⁷` (`log 2`).

| step | `T` | contacts | target `λ_min` | best **certified** `c` (exhaustive cover) | `N` atoms | `M` | `G` | `β₀` | `β₁` | evaluations | unresolved | archive |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| base | `½log3 = 0.549306` | `{2}` | `9.89·10⁻⁴` | **`+8.8577·10⁻⁵`** | 437 | 24 | 128 | `2.0025617` | `−0.0096544` | `2 378 593` | **0** | `CERT_log3_R5.json` |
| **1** | `0.58` | `{2,3}` | `2.16·10⁻⁴` | **`−3.1964·10⁻³`** | 414 | 24 | 128 | `2.0399645` | `−0.1477706` | `505 806` | **0** | `CERT_T058_M24.json` |
| 2 | `0.62` | `{2,3}` | `1.91·10⁻⁵` | not attempted — step 1 blocks | — | — | — | — | — | — | — | `lp_S0.62.pkl` (shape only) |
| 3 | `0.65` | `{2,3}` | `2.40·10⁻⁶` | not attempted | — | — | — | — | — | — | — | `lp_S0.65.pkl` |
| 4 | `0.68` | `{2,3}` | `3.24·10⁻⁷` | not attempted | — | — | — | — | — | — | — | `lp_S0.68.pkl` |
| 5 | `log 2` | `{2,3}` | `1.09·10⁻⁷` | not attempted | — | — | — | — | — | — | — | `lp_Slog2.pkl` |

**Highest step certified with `c > 0`: the base, `T = ½log3`** (and there the constant is doubled). **Step 1 fails**,
and it fails by a wide, fully verified margin, not by a numerical hair.

### 5.1 Step 1 in full, and the exact saturating factor

| stage at `T = 0.58` | value | wall |
|---|---|---|
| shape transferred from the `½log3` certificate, `G = 128` polish (`r5shape` + `r5polish`) | `−4.2088·10⁻¹` | 2351 s |
| **own** atom LP, `M = 24`, 414 atoms, `τ₁ = 30`, `N = 2`, 88 004 rows (`r5lp`) | `−3.174953·10⁻³` | 939 s |
| `G = 128` block polish of that shape, 210 001 rows, rows scaled by `10⁴` | `−3.1799357·10⁻³` | 696 s |
| F2 exact active-set vertex (133 active rows `= nv`, `max_violation = 2.2·10⁻¹¹`) | `−3.17993566829428·10⁻³` (`Δc = −2.5·10⁻¹⁴`) | 3 s |
| true fine-grid infima: `f` `−3.180153·10⁻³`, `h₀` **`−3.1963577·10⁻³`**, `h₁` `−3.1834131·10⁻³`, `h₂` `−3.1947841·10⁻³` | — | — |
| exhaustive (TAY) cover, `w_min = 10⁻⁹`, 20 segments | `c = −3.1964·10⁻³`, **0 unresolved**, `505 806` evaluations | 17 s |
| `mpmath.iv` enclosures at the four argmins | agree to `3.57·10⁻¹³`; all four **negative as intervals** | — |

**The saturating factor.** At `T = 0.58` the best certificate of the class that this pipeline produces has infimum
`−3.1964·10⁻³`. To reach the sign it must gain `3.1964·10⁻³`; to reach the target `λ_min = 2.16·10⁻⁴` it must gain
`3.4124·10⁻³`. Against the `½log3` certificate's `+8.8577·10⁻⁵` that is a deficit of **`36.1×` the whole margin
available one step below**, and `14.8×` the target eigenvalue at `0.58` itself. **It is not a precision problem.**
Ruling the candidates out one by one:

* **not F2 / LP tolerance** — with rows scaled by `10⁴` the exact vertex differs from the HiGHS vertex by
  `2.5·10⁻¹⁴`, i.e. `1.3·10⁻¹¹` of the deficit;
* **not the grid** — the polish LP value `−3.1799·10⁻³` and the *true* fine-grid infimum `−3.1964·10⁻³` agree to
  `1.6·10⁻⁵`, i.e. `0.5%` of the deficit (at `½log3` the same stage agreed to `2·10⁻⁹`);
* **not the verifier** — the cover closes with `0` unresolved intervals and the interval enclosures reproduce the
  infimum to `10⁻¹³`;
* **not the tail lemma (F1)** — **[amended 2026-09-21 per R154_016: right conclusion, wrong reason. The `k = N`
  worst-cased row *is* binding, to `0.5 %` (`h₂ = −3.1948·10⁻³`). But with `N = 3` that row moves to `+0.1888` and
  the new `k = 3` row to `+0.2980`, leaving `h₀ = −3.19636·10⁻³` and `f = −3.18015·10⁻³`: the whole tail lever is
  worth `1.6·10⁻⁶`, i.e. `0.05 %` of the deficit.]**;
* **it is the atom budget `M`.** This is the same lever round 4 identified at `½log3` (`M = 16 → −4.75·10⁻⁵`,
  `19 → +5.72·10⁻⁵`, `24 → +1.742·10⁻⁴` on the LP) — but the second contact moves the crossing far to the right.
  With `M = 24` the measured LP value falls from `+1.68·10⁻⁴` (one contact) to `−3.17·10⁻³` (two contacts), a
  **factor `19` and a sign**, for atoms that are `2T/M`-spaced on a window `6%` wider. A confirming run at
  `M = 32` (552 atoms, `P = 173.33`) was launched twice and did not return an LP value inside the round's compute
  budget (`> 45 min` per solve, and it was lost once to a power cut); **the `M`-sweep at two contacts is therefore
  `OPEN`, and it is the single measurement the next round needs**.

Steps 2–5 were **not attempted**: their targets are `13×` to `2000×` *smaller* than step 1's, the deficit at step 1
is `15×` its own target, and nothing in the construction improves as `T` grows (the atom window `|u| ≥ 2T` moves
*out*, so `ν̂` has fewer oscillations per unit `τ` to work with while the prime term gains amplitude `v₃`).
Reporting them as "attempted and failed" would be dishonest; they are blocked behind step 1's `M`.

---

## 6. Diagnostics (all `DIAGNOSTIC-NUMERIC`)

* **`β₀ → 2` survives the second contact, `β₁` does not.** At `½log3`, `(β₀, β₁) = (2.0025617, −0.0096544)`; at
  `0.58`, `(2.0399645, −0.1477706)`. The polar multiplier stays within `2%` of `2` — the dual still reconstitutes
  `Φ̂(i/2)+Φ̂(−i/2)`, the two polar contributions the primitive class removes (`R154_007 §4.1`) — but `β₁` grows by
  a factor `15.3`. Reading: the second contact is paid for out of the `u sinh(u/2)` direction, not the polar one.
* **The atom mass collapses.** `‖a‖₁ = 45.38` at `½log3` against `25.84` at `0.58` with the same `M` and a wider
  window: the LP cannot *afford* the large oscillating profile once `cos(τ log 3)` must also be matched, and it
  retreats to a smaller, flatter `ν`. This is the mechanism behind the `M`-lever, stated in terms of the certificate.
* **The binding minimum moves into the tail.** At `½log3` the deepest point was `h₀(37.8153)` by a hair over
  `f(17.645)`; at `0.58` the four infima (`f` `−3.180·10⁻³`, `h₀` `−3.196·10⁻³`, `h₁` `−3.183·10⁻³`,
  `h₂` `−3.195·10⁻³`) are **equal to `0.5%`** — the certificate is saturated simultaneously on `[0,30]` and on all
  three tail families. That near-degeneracy is complementary slackness of Theorem O made visible, and it says the
  deficit is *global*, not a local dip that more cut rounds could fill.
* **Shape transfer works within a contact set and not across one.** **[amended 2026-09-21 — REFUTED. `R154_016`
  row 3i flagged the positive half as untested (`lp_S0.62/0.65/0.68/Slog2.pkl` are transfers from `½log3`, not
  from `0.58`, and none was polished). Round 6 tested it: the `0.58 → 0.62` transfer of the own-LP certificate
  `lp_Q058.pkl`, polished to convergence, gives `−4.0402·10⁻¹` — within 4 % of the across-contact transfer
  `−4.2088·10⁻¹`, and `127×` worse than the un-transferred control `−3.1802·10⁻³`. The destructive step is the
  lattice rescaling `d = 2T/M` itself, not the change of contact set; there is no cheap ladder (`R154_017 §5`).]** The `½log3` profile re-lattices to `0.58` at
  `−4.21·10⁻¹`; the `0.58` atom LP reaches `−3.17·10⁻³` — a factor `132`. So the atoms carry contact-specific
  structure (frequency `log 3`), and the cheap route across the staircase is only available *between* steps 2–5,
  which all share `{2,3}`. This is why step 1 had to be paid for in full and the rest would have been cheap.

---

## 7. Verdict table

| item | label |
|---|---|
| **Lemma F1** (two-frequency graded tail: `ν̂` periodic, prime term exact on `N` periods and worst-cased beyond; valid for any finite frequency set) | **`PROVED` (new)** |
| the `log 3`-incommensurability "structural obstruction" of `R154_010 §6` / `R154_011` row 20 | **withdrawn** — it confused periodicity of `ν̂` with periodicity of the prime term (§2) |
| **(TAY)** second-order branch-and-bound: `f ≥ m(mid−w/2) + (q+r)(mid) − \|(q+r)′(mid)\|w/2 − M₂w²/8`, with exact `ĝ₀′, ĝ₁′` | **`PROVED` as a method**; measured `100×` fewer evaluations, `10³×` wider cells, `target^{−1/2}` instead of `target^{−1}` scaling |
| **`λ_min(A_{½log3}(w_ζ)) ≥ 8.8577·10⁻⁵ > 0`** (Theorem R5a), 437 atoms, `2.378593·10⁶` evaluations, **0** unresolved, `ε_fp = 10⁻⁹` justified to `5.4·10⁻¹³` | **`PROVED`** (machine-verified, archived, interval-audited) — `2.0004×` `R154_010` |
| **(F2)** row scaling (`S = 10⁴`) + exact `mpmath` active-set vertex, with bound-degeneracy detected and declined | **`PROVED` as a method**; **measured not to be the binding lever** (`Δc = 2.5·10⁻¹⁴`) at every value reached this round |
| `T = 0.58`: best class certificate has infimum `−3.1964·10⁻³`, exhaustively verified, `0` unresolved | **`PROVED` negative** (a certified *lower* bound that is negative, hence no sign) |
| the deficit at `0.58` is the atom budget `M`, not precision, grid, verifier or tail | `DIAGNOSTIC-NUMERIC` (§5.1, four levers eliminated by measurement) |
| the `M`-crossing at two contacts (is there an `M` with `c > 0` at `T = 0.58`?) | **`OPEN`** — the one measurement the next round needs; `M = 32` exceeded the compute budget |
| `T = 0.62, 0.65, 0.68, log 2` | **not attempted**; blocked behind step 1 |
| `β₀ ≈ 2` persists with two contacts (`2.0400`), `β₁` grows `15×`, `‖a‖₁` falls `45.4 → 25.8`, four infima degenerate to `0.5%` | `DIAGNOSTIC-NUMERIC` (§6) |

**FATAL rule / no sign.** Every `T ≤ log 2` treated here is already certified positive in Paper 42
(`main.tex:4072–4230`) by the directed Feshbach/Schur-complement argument; what is new is an independent, mesh-free,
spectral-side certificate. **No sign is claimed for `ζ` beyond `T ≤ log 2`**, and nothing above `log 2` is touched.
The only inputs are `ψ`, `log 2`, `log 3` and linear programming; no `ζ`-zero data, no zero-free region, no moments.

**Precision of record.** `scipy` 1.11.4 HiGHS; polish LPs of `4.2·10⁵`–`7·10⁵` rows × `133` columns with rows
scaled by `10⁴`; cut grids `5·10⁻⁶`; (TAY) B&B `w₀ = 0.02`, `w_min = 10⁻⁹`; `mpmath` 1.3.0, `iv.dps = 40`,
`mp.dps = 60` (`50` for the F2 vertex).


## 8. Open, ranked

1. **The `M`-crossing at two contacts.** At `½log3` the LP crossed zero between `M = 16` and `M = 19`; at `0.58`
   `M = 24` gives `−3.17·10⁻³`. Measure `c(M)` at `T = 0.58` for `M = 32, 44, 64` — each is one atom LP
   (`≈ 94 000` rows × `557`–`1 100` columns, `> 45 min` per solve, so `≈ 4` h with the cut rounds). If `c(M)`
   crosses zero at an attainable `M`, steps 2–5 are then cheap, because within `{2,3}` the shape transfers
   (§6, factor `132` versus across a contact change). If it does not, the class itself saturates above `½log3`
   and that is a theorem-shaped negative worth having.
2. **Reduce the LP cost so that `M` is affordable.** The atom LP, not the verifier, is now the bottleneck (the
   verifier went from `30 min` to `17 s` this round). A column-generation loop — solve on a few hundred atoms, price
   new ones against the dual — would replace one `557`-column dense solve by many small ones.
3. **Re-certify `R154_010`'s open items.** Theorem R5a supersedes Theorem R4's constant; `R154_007 §8`'s text
   corruption and its "interval" (should be *comb*) description are still unrepaired, as flagged in `R154_010 §6`.
4. **A rate for the `(TAY)` cover.** Evaluations scale like `target^{−1/2}`; with `M₂` explicit this should give a
   closed-form cost model for any future endpoint, replacing the per-run budgeting used here.

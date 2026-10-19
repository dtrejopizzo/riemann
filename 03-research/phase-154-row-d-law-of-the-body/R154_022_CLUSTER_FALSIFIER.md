# R154.022 — Round 8: the clustered-atom falsifier at `T = 0.58`

* Orders: `R154_021` (single falsifier LP authorised),
`R154_020 §5` (amendments: upper/lower separation, report the F1 slack, run a matched control).
Compute actually used: **one process, two LP solves, 63 s of wall time** (budget 15 min).
Code: `scripts/round8/r8cluster.py`, reusing `scripts/round6/r6lp.py` (cutting planes) and
`scripts/round5/r5core.py` (symbol, Lemma-F1 tail rows, fine grid). Raw log `scripts/round8/r8.log`,
results `scripts/round8/r8_results.json`, duals `lp_R8CLU.pkl` / `lp_R8CTL.pkl`.*

---

## 0. Verdict

> **The clustering remedy of `R154_019 §remedy` is REFUTED at the authorised falsifier point.**
> At equal atom count (`175`) the clustered class is **4.0× worse** in true minimum than the matched
> spread control, not `≥ 3×` better; and the Lemma-F1 slack in the clustered class is `6.0·10⁻¹`,
> `6.3×` the control's and **seven orders of magnitude above the `10⁻⁷` target**. The tail lemma, not
> the LP, is the binding object in the clustered class — exactly the cost `R154_020 §5` flagged.

Label: **`DIAGNOSTIC-NUMERIC`**. Nothing is certified; no sign; the endpoint of record is unchanged
(`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`, R5a). The FATAL rule is clean: nothing here is above `log 2`.

---

## 1. The two runs

Both: `T = 0.58`, contacts `{2,3}` (`v₂ = 0.980258`, `v₃ = 1.268568`), `τ₁ = 59.544`, `N = 2` graded
tail blocks, `β₀, β₁` free, tail rows from Lemma F1 at the run's own period `P`, `3 097` starting rows
(`f` on `[0,τ₁]` at step `0.06`; each `h_k` on `[τ₁, τ₁+P)` at step `P/700`), `≤ 8` cutting-plane
iterations, `tol = 10⁻⁶`, HiGHS, exact local-minimum separation oracle (`r6lp.local_minima`, 5 refinements).

* **CLUSTERED (`R8CLU`).** `h′ = 2T/102 = 0.01137255` (the code's lattice requires `h′ | 2T`; the order's
  `2/175 = 0.0114286` is not a divisor of `1.16`, so `M = 102` is the nearest admissible spacing).
  `175` atoms `u_j = j·h′`, `j = 102…276`, i.e. `u ∈ [1.160000, 3.138824]` — `V = 2T + 1.9788` against the
  ordered `2T + 2.0`. Period `P′ = 2π/h′ = 552.487`. Separation step `0.06` (≈33 points per `2π/u_max = 2.00`).
* **CONTROL (`R8CTL`).** `175` atoms on the spread lattice, `h = 2T/10 = 0.116`, `j = 10…184`, i.e.
  `u ∈ [1.160, 21.344]`. Period `P = 54.165`. Separation step `0.010` (≈29 points per `2π/u_max = 0.294`).
  *Deviation recorded:* the order said "the standard lattice `j·2T/24` over `[2T, 2T+20]`", which is
  `414` atoms, not `175`; the two halves are incompatible. I followed the binding amendment
  `R154_020 §5(iii)` — **equal atom count with the round-5/6 `u_max ≈ 21.1`** — since that is what
  isolates *clustering* from *budget*. The price is that the control's spacing is `2T/10`, not `2T/24`.

"True minimum" below is the minimum on a **`10⁻³` grid** over `[0,τ₁]` (for `f`) and over
`[τ₁, τ₁+P)` for each of `h₀, h₁, h₂` — i.e. the whole verification range `[0, τ₁+3P]`, which contains
the ordered `[0, τ₁+2P′]`. It agrees with the separation oracle's refined minimum to `1.4·10⁻⁷`
(clustered) and `2.3·10⁻⁵` (control), so the grid is not the limiting resolution.

---

## 2. The two-row table

| quantity | **CLUSTERED** `R8CLU` | **CONTROL** `R8CTL` |
|---|---|---|
| atoms / spacing | `175` / `h′ = 0.01137255 = 2T/102` | `175` / `h = 0.116 = 2T/10` |
| `u`-window, `u_max` | `[1.1600, 3.1388]`, `3.13882` | `[1.1600, 21.3440]`, `21.344` |
| period `P` | `552.487` | `54.165` |
| **LP value** (row relaxation, **upper** bound on `c`) | `−3.162749·10⁻²` | `−1.443743·10⁻¹` |
| **true min, `10⁻³` grid** (**lower** than `c`; the honest deficit) | **`−8.995186·10⁻¹`** | **`−2.235995·10⁻¹`** |
| argmin / block | `240.032` in `h₂` | `78.233` in `h₂` |
| per-block minima `f / h₀ / h₁ / h₂` | `−0.03530 / −0.76970 / −0.32955 / −0.89952` | `−0.16822 / −0.14438 / +0.58346 / −0.22360` |
| `β₀` | `7.377969` | `2.329953` |
| `β₁` | `−6.446728` | `+0.072832` |
| `‖a‖₁` | `13.9415` | `10.8641` |
| **F1 slack** `\|β₀\|k₀(τ₁) + \|β₁\|k₁(τ₁)` | **`5.999406·10⁻¹`** | **`9.567872·10⁻²`** |
| cutting-plane iterations / final rows | `8` / `4 088` | `8` / `3 719` |
| final LP↔true-min gap | `2.079` (not converged) | `0.128` (not converged) |
| wall (LP / fine grid) | `23.6 s / 6 s` | `26.7 s / 6 s` |

---

## 3. Reading

**3.1 The decision rule fires on REFUTED.** The rule was: clustered true-min better than control by a
factor `≥ 3` in deficit ⟹ corroborated; clustered `≤` control ⟹ refuted. Measured:
`−0.89952` against `−0.22360`, i.e. the clustered deficit is **`4.02×` larger**. Not marginal, not
inside any plausible solver tolerance, and the same sign on every block except `f`. **Clause (c) of the
remedy — that concentrating the atoms buys the same LP value at `V/u_max` of the atom count — is false
in the only currency that was ever falsifiable.**

**3.2 The LP value points the other way, and must not be quoted alone.** `R8CLU`'s LP value
(`−3.16·10⁻²`) is `4.6×` *better* than `R8CTL`'s (`−1.44·10⁻¹`). This is the trap `R154_020 §5(i)`
anticipated: the row relaxation is an **upper** bound, and its quality is set by how well `3 097+` rows
sample the verification interval. The clustered run's interval is `10.2×` longer (`P′ = 552` against
`54.2`), so its rows are `10×` sparser per unit `τ` and its relaxation is correspondingly looser — the
gap `2.08` against `0.13` measures exactly that. Reporting the clustered LP value as an improvement
would have been a pure sampling artefact. **On the quantity that bounds `c` from below, clustering loses.**

**3.3 The F1 slack is the wall, and it is worse than feared.** `R154_020 §5` warned that `P′ = 2π/h′`
makes Lemma F1's conservatism term the binding object. Measured at `τ₁`: `0.5999` clustered against
`0.0957` control — a `6.3×` penalty, driven by the optimiser's need for large multipliers
(`β₀ = 7.378`, `β₁ = −6.447`, against `2.330` and `0.073`) to hold up the long tail. For comparison
`R154_016 E2` recorded `1.81·10⁻²` at `M = 24` and the `log 2` target is `1.09·10⁻⁷`. So the clustered
class is `33×` further from the tail lemma's budget than the class that was already `10⁵×` short.
**Corollary for the programme: no amount of LP work inside the clustered class can help while the tail
lemma's own conservatism exceeds the deficit being chased by two orders of magnitude.** Any revival of
the remedy must first replace Lemma F1 by a bound whose slack does not scale with `P`.

**3.4 What is *not* shown.** (i) Neither run converged; both true minima are therefore *lower bounds on
the deficit* of their class, and a converged clustered run could only be **better** than `−0.900` — but
it would have to improve by `4×` merely to tie the control, and the F1 slack (§3.3) is unaffected by
convergence. (ii) Both `175`-atom classes are far worse than the certified spread class at `T = 0.58`
(`c(24) = −3.196·10⁻³`, `414` atoms): equal atom count at this `T` is nowhere near the sign, so the
experiment discriminates *between* the two `175`-atom classes and nothing more. (iii) `β₀` here
(`7.378` clustered, `2.330` control) is not comparable with the `2.0400` of `R154_012`: different class,
different row set, unconverged. It is **not** evidence about the `β₀ → 2` question (Prop. P), which
stays `OPEN`. (iv) No B&B was run — the exhaustive `(TAY)` cover remains a separate, unexecuted step,
and on this evidence there is no reason to spend it on the clustered class.

**3.5 Diagnosis, offered.** The failure mode is the one `R154_017 §3` named: `175` frequencies packed
into `[1.16, 3.14]` give a near-collinear column block (all `\cos(u_jτ)` with `u_j` within a factor
`2.7` of each other), so the effective dimension of `ν̂` is far below `175`, while the verification
burden grows like `1/h′`. Theorem K counts atoms; the LP pays for *independent* atoms and for the
period they induce. That gap between "atom count" and "useful dimension" is what clause (c) assumed away.

---

## 4. Consequences for the map

| item | before | after this round |
|---|---|---|
| clustering remedy, clause (c) | theorem-candidate `OPEN`, falsifier specified | **`REFUTED`** (this round, `DIAGNOSTIC-NUMERIC`) |
| Theorem K / K0 / K1 | `PROVED` (support bound) | unchanged — K is not touched; what fails is the *engineering* inference drawn from it |
| "`175` columns instead of `1 087` at `log 2`" (`R154_019 §275`) | budget claim | **withdrawn**: at equal count the clustered class is `4×` worse, and its tail lemma `6.3×` looser |
| Lemma F1 slack | noted as a risk (`R154_020 §5`) | **measured as the binding obstruction** in any small-`h′` class |
| endpoint of record | `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` | unchanged |

**Recommendation for the next round:** close the clustered-atom line. The one reusable product of round 8 is
the negative measurement of §3.3 — *the graded tail lemma's conservatism scales with the period and is
the first thing that must be fixed before any refinement of the atom lattice can matter.* That is a
clean, `OPEN`, purely analytic problem (sharpen `k₀, k₁` in Lemma F1, or replace the worst-cased tail by
an exact `N`-period continuation), and it does not require an LP to attack.

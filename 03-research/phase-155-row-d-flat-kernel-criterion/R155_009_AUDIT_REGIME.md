# R155.009 — Audit of R155.008 (the regime law over 103 windows)

*Phase 155. Target: `R155_008_REGIME_LAW_100_WINDOWS.md`,
`scripts/reverse/regime_table.csv`, `scripts/reverse/regime/`. Read first: Paper 46 §2, §5, §7
(Thm. Z, Cor. 7.4, Rem. 7.6), §8 (Prop. env, the three scales, Prop. TK), `R155_005`, `R155_006`.
The 496 s 103-window run was **not** rerun (the load constraint); everything below is either a
rerun of a ≤ 60 s script, a recomputation from the archived JSON/CSV, or a proof check.*

**Global verdict: ACCEPT WITH REPAIRS, and REJECT the headline reading of §5/§6.**
The four propositions are essentially right (two definitional errors, one false analyticity claim,
one proof gap in the §7bis corollary). The numerics reproduce, except **two published statistics that
do not** (§4 below). The interpretation — "the step at a prime entry was a moving-domain artefact",
"extrapolation works" — is **not established by this experiment**: at six of the seven entries the
verification domain was frozen by the `τ ≤ 60` cap, so continuity there is a restatement of Prop. C
and not evidence; at the one entry where the domain *was* allowed to move (`n = 3`) the archived data
show a factor **3.17**. And the whole sweep runs in a class that is **56× weaker at `½log3` than
`R155_005`'s own class**, a fact the deliverable never states.

---

## 1. Verdict table

| item | claim | verdict |
|---|---|---|
| **E** entry law | `PROVED` | **ACCEPT the content, REPAIR the statement** (one-sided limits wrong; `τ_env` is the *multiplier-free* threshold only) |
| **D** `D(T)=e^{A_T−2T}` | `PROVED` | **ACCEPT** (trivial substitution; reproduced to `1.7e−13` over 103 rows) |
| **C** continuity | `PROVED` | **ACCEPT the proposition, REJECT the corollary and the "artefact" reading**; "real analytic off `{½log n}`" is **false** |
| **M** `W_{T'}⊆W_T ⇒ λ^W ↓` | `PROVED` | **ACCEPT**, but it is Paper 46 Cor. `mono` with a one-line reason added, not a new result |
| **Lemma R** rigidity | `PROVED` | **ACCEPT** modulo citing the inversion lemma; **REJECT consequence (b)** ("no finite zero universe admits a flat-top certificate") — the proof step is a non sequitur |
| §2.4 cross-check (Thm. Z, 8 regimes) | `DIAGNOSTIC` | **ACCEPT**, reproduced from `crosscheck_regime.json` / `analysis2.log` |
| §2.4 `1.6e−4` prime-cut artefact | `DIAGNOSTIC` | **ACCEPT**, reproduced in `analysis_primecut_eU.log`; a real and useful trap |
| §3 table, `c_cert`, Bernstein, grid inflation | `DIAGNOSTIC` | **ACCEPT** (all reproduced), one count wrong (`79` → `82`) |
| §4(A) universal profile `0.0785` | `DIAGNOSTIC` | **REJECT as printed**: the true sup-norm deviation is **0.1332** (0.0785 is a 17-point sampling artefact) |
| §5.2 "nothing jumps but the domain" | `DIAGNOSTIC` | **REJECT as evidence** (domain frozen at all six entries measured) |
| §5.3 "its **true** interval `[0,τ_env]`" | `DIAGNOSTIC` | **REJECT the word "true"**: for these `w`, `‖ν_w‖_TV ≈ 48.7`, so Prop. env gives `τ_env ≈ 2.4·10^{22}`, not `16.7…502` |
| §6 extrapolation | `DIAGNOSTIC` | **ACCEPT the numbers, REJECT "the prediction works for the value"**: the `R155_006 §6` conditioning test was not run. I ran it (§5 below): 1.2–1.6× loss, one predicted weight infeasible |
| §7bis(4) cancellation budget | `DIAGNOSTIC` | **ACCEPT**, reproduced exactly from `toy10.json` (note: the minima are over `[0, 16.75]`, not `ℝ`) |
| labelling / no sign claim / row-D label | — | **ACCEPT.** Every zero-derived number is `DIAGNOSTIC`; no sign is claimed beyond `log 2`; no statement about zeros; circularity no-go cited in both the file and the READMEs |

---

## 2. The proofs, line by line

**(E) `R155_008:331–336`. Content correct, statement wrong twice.**
* `reglib.py:141` defines `N_T` by `log n < 2T − 1e-12`, i.e. **strict**: at `T = ½log n` the entering
 `n` is *excluded*. With that definition `A_T` is left-continuous, so `A_T − A_{T^-} = 0` and the
 printed identity `A_T − A_{T^-} = v_n at T = ½log n` (`:333`) is **false**; the jump is
 `A_{T^+} − A_T = v_n`. Identically, `τ_env(½log n)/τ_env((½log n)^-) = e^{v_n}` (`:335`) must read
 `τ_env((½log n)^+)/τ_env((½log n)^-)`. Either fix the limits or define `N_T` with `≤` (then "left-
 continuous" must become "right-continuous"). One-word repair, but the statement as printed is wrong.
* `τ_env := 2πe^{A_T}` is Paper 46 Prop. env's **multiplier-free** part only; the proposition's
 threshold is `2πe^{A+‖ν‖_TV+o(1)}` (`main.tex:939`). Prop. E is therefore a statement about
 `2πe^{A_T}`, which for any actual `w`-certificate is *not* the verification threshold (see §3 below).
 Say so, or the proposition reads as a claim about certificates that it does not support.
* Arithmetic checked independently: `v_4 = 0.693147, v_5 = 1.439549, v_7 = 1.470994, v_8 = 0.490086,
 v_9 = 0.732408, v_11 = 1.446005`; `e^{v_n} = 2.00000, 4.21869, 4.35346, 1.63253, 2.08008, 4.24603`,
 and the archived `τ_env` ratios agree to all printed digits (rerun of `fit_regime.py`, 2 s). 6/6 ✓.
 `n = 3`: ratio **3.55576** = `e^{v_3}` exactly (the file's "3.554, the small gap being the 5·10⁻⁴
 offset", `:249`, is a rounding of `59.54/16.75`; there is no gap).
* `A_T = (4+o(1))e^T` ✓ (`Σ_{n<x}Λ(n)n^{-1/2} ∼ 2√x`).

**(D) `:338–344`. ACCEPT.** `τ_env/2πe^{2T} = e^{A_T−2T}` is substitution.
Recomputed over the 103 CSV rows: `max|index − e^{A_T−2T}| = 1.7·10⁻¹³`, `max|τ_env − 2πe^{A_T}| = 0`.
`D(½log3) = 0.888`, `D(1.20) = 455.3` ✓.

**(C) `:345–353`. The proposition is correct and it is the only real content of §5.**
It proves: *for the fixed shape family of §2.1 and a fixed coefficient vector*, `T ↦ f_{w_T}(τ)` is
continuous. That is exactly right and it is what makes the class comparable across windows. Three
repairs:
1. "**real analytic** off `{½log n}`" (`:346–347`) is **false** for this family. The cubic B-splines
 are only `C²`, and their nodes `u_j = 2T + jh` move with `T`, so `w(log n)` is a piecewise
 polynomial in `T` with breakpoints wherever `log n` crosses a knot `2T + (j±2)h`. Continuity (and
 `C²`) is all that is available. Delete "real analytic", or restrict the claim to the `ψ_s` part.
2. The **Corollary** (`:354–357`) — "at a prime entry nothing in the certificate problem jumps except
 the domain" — is broader than the proposition. The proposition fixes the coefficient vector inside
 one `T`-independent shape family; it says nothing about `W_T` (which does change: `W_{T'} ⊊ W_T`)
 nor about `λ^W(T)`, whose continuity is **not** proved anywhere in this file. What is proved:
 *the value of the §2.1 sub-class at a fixed verification domain is continuous in `T`.*
 As it stands, §9 proposal 1's "the class `W_T` varies continuously" is an overclaim.
3. The consequence "`R155_005`'s step was a moving-domain artefact" is a **hypothesis the experiment
 does not test** — see §3.

**(M) `:359–366`. ACCEPT.** Inclusion direction right: `w ≡ 1` on `[−2T',2T']` ⟹ `w ≡ 1` on
`[−2T,2T]`, and Paper 46's decay hypothesis (`main.tex:983–986`) is imposed on `|u| ≥ 2T` with
`C, δ` existentially quantified, so enlarging `C` on the compact `[2T,2T']` gives `W_{T'} ⊆ W_T` ✓.
`λ^W(T) = sup_{W_T} inf f_w` ⟹ non-increasing ✓ (`f_w` does not depend on `T`). The remark that the
§2.1 sub-class is *not* nested (moving knots) is correct and is the right explanation of the in-regime
wobble. Note this is Paper 46 Cor. `mono`/§8.3(4) (`main.tex:384, 1197`) restated on the dual side.

**Lemma R `:409–422`. ACCEPT with one citation, REJECT consequence (b) `:423–430`.**
* The proof is correct: positive definiteness from Bochner, the `3×3` Gram inequality
 `|φ(u+a)−φ(u)|² ≤ 2φ(0)(φ(0)−Re φ(a))`, flat top ⟹ every `a ∈ (0,2T]` is a period ⟹ (continuity)
 `w ≡ 1`. The one unstated step is `∫ŵ = 2πw(0) < ∞`: this needs the standard theorem "`w ∈ L¹`
 continuous with `ŵ ≥ 0` ⟹ `ŵ ∈ L¹` and inversion holds" (Fejér/Gauss summability). Cite it.
* The statement is best given as a reductio: *no even continuous `w ∈ L¹` that is `≡ 1` on a window has
 `ŵ ≥ 0`* — the conclusion `w ≡ 1` contradicts `w ∈ L¹`. As printed ("Then `w ≡ 1` … in particular no
 such `w` is integrable") the hypotheses are self-contradictory, which is fine logically but reads badly.
* Consequence (a) (never termwise; the certificate is cancellation) ✓ — this is the valuable half.
* Consequence (b), "**a finite zero universe admits no flat-top certificate whatsoever**" (`:426–428`),
 is **not proved**. The argument given is: `ŵ` is negative somewhere and `→ 0` at infinity, "so it is
 negative for `τ` far from all `γ_j`". Non sequitur: far from all `γ_j` every term tends to `0`, and
 the sign of the sum there is decided by the *tails*, not by where `ŵ` dips. A correct proof exists
 only under an extra hypothesis, e.g. `w` compactly supported of type `U`, where `ŵ(t) ∼ c cos(Ut+ϕ)t^{-4}`
 and `f_N(τ) ≈ t^{-4}Σ_j c cos(U(τ−γ_j)+ϕ)` oscillates in sign — and even that needs the amplitude
 `|Σ_j e^{-iUγ_j}|` not to vanish identically. For general decaying `w ∈ W_T` with an eventually
 positive `ŵ` the claim is **open**; nothing excludes a finite sum of translates being `≥ 0`.
 Downgrade to: *(b′) for compactly supported `w` with oscillatory transform tail, no finite zero set
 gives `f_N ≥ 0`* (with the amplitude caveat), and state the general case as a question.
* §7bis(1) and (3) are correct and trivial, and are labelled as such.

---

## 3. §5 does not show what it says it shows

The claimed refutation of `R155_005 §0.4/§4.1` rests on the six ratios `0.999…1.011` of §5.2. But
`run_regime.py:11` sets `TAUCAP = 60.0` and `taumax = min(τ_env, 60)`. From the CSV:
`capped = 1` at **82** of 103 windows (the file says `79`, `R155_008:200` — **error**), and in
particular at *both* windows of every one of the six entries in §5.2 (`τ_env ≥ 119 > 60` above and
`≥ 59.5` below, with `τ_max = 60` on both sides from the entry of `4` on). So at those six entries the
LP's domain is **identical** below and above, and the only thing that changes is the prime-comb
coefficient set, which Prop. C already proves is continuous. §5.2 therefore measures Prop. C; it is
not independent evidence, and it cannot refute a claim about what happens when the domain moves.

The single entry in the range at which the domain *did* move is `n = 3` (`τ_max: 16.75 → 59.54`,
uncapped both sides). Recomputed from the archived CSV:

```
n=3 tau_env x3.55576 c_fine: -1.8498e-02 -> -5.8619e-02 ratio 3.169
n=4..11 (all capped at 60): ratios 0.999, 1.011, 1.007, 1.003, 1.002, 1.002
```

So the archived data are consistent with "the step is the domain" — and are equally consistent with
"the step is the entry" — because the experiment removed the domain everywhere except at the one entry
where a factor `3.17` appears. The honest statement is the one §5.3 half-makes: *with the domain held
fixed the objective is continuous (Prop. C); when the domain is allowed to move the value falls, by
`3.17×` at `n = 3` and by `2.4×`/`4.6×` in the two-window probe.* "The domain is the whole of it"
(`:262`) is unsupported.

**§5.3's "true interval" is wrong.** `domain_probe.py` re-evaluates on `[0, 2πe^{A_T}]`. For a flat-top
`w` the Prop. env threshold is `2πe^{A_T+‖ν_w‖_TV}` (`main.tex:939`); I computed `‖ν_w‖_TV` for the
window-1 `L = 20` weight from `regime_windows.json`:

```
TV(nu_w) (a.c. part, both sides, 2*int_{2T}^{U} |1/2(1-w)K + 2w cosh(u/2)| du) = 48.698
2 pi e^{A_T + TV} = 2.36e+22 (the file's "true interval" is 16.75)
```

i.e. the interval on which a pointwise argument is entitled to stop is 21 orders of magnitude beyond
what §5.3 probes. This does not damage the negative conclusion (it strengthens it), but the words
"its **true** interval" (`:288`) and "the honest form of the jump law" (`:296`) must go.

---

## 4. Reproduction: what matches and what does not

Reruns (this machine, ≤ 60 s each; the 103-window run was **not** repeated):
`fit_regime.py` (2 s) reproduces §4, §5.1, §5.2, §6 **to every printed digit**. Recomputation from
`regime_table.csv` (103 rows × 28 cols) and `regime_windows.json`:

| statistic | file | audit | verdict |
|---|---|---|---|
| `max|index − e^{A_T−2T}|` | — | `1.7e−13` | ✓ |
| grid inflation `c_LP − c_fine` | `8.1e−4 ± 3.3e−4` | `8.19e−4 ± 3.31e−4` (range `2.3e−4…1.65e−3`) | ✓ |
| Bernstein slack | `0.0133 ± 0.0022` | `0.01330 ± 0.00219` | ✓ |
| `c_cert = c_fine − bern`, all negative | "margin ≥ `5e−3`" | `max c_cert = −0.02806` | ✓ (understated) |
| `∫w` | `3.128 ± 0.067` | `3.1284 ± 0.0673`; `max|∫w − ∫|w|| = 1.7e−8` | ✓ |
| rate | `0.173 ± 0.014` | `0.1728 ± 0.0135` | ✓ |
| contacts | `23.8 ± 1.7` | `23.82 ± 1.66` | ✓ (threshold `f < c + 1e−5`, `run_regime.py:58` — an arbitrary constant; the count is not a canonical quantity) |
| `last_node = 7.75` | 102/103 | 102/103 | ✓ |
| `capped` | **79**/103 | **82**/103 | ✗ `R155_008:200` |
| `‖w‖_∞ = 1` "exactly" | 102/103 | 98 within `1e−6`, 99 within `1e−3`, 102 within `1e−2`; 6 windows have `‖w‖_∞ > 1` | ✗ as worded (`:237`, `:507`); say "within `10⁻²`" |
| global-profile deviation | **`0.0785`** sup, mean `0.041` | **`0.1332`** sup, mean `0.0599` on the `321`-point `v`-grid the file itself uses (`fit_regime.py:9`) | ✗ `R155_008:35, 224` |
| same, `L = 5` | `0.095` | `0.1378` | ✗ `:235` |

The `0.0785` is exactly the maximum over the **17 printed sample points** `v = 0, ½, …, 8`
(`0.0785`, mean `0.0410` — I reproduce it on that subgrid, and on the `33`-point subgrid). It is a
sampling artefact of the way the number was read off, and the file calls it "(sup norm)". The correct
figure is `0.133`, i.e. **13 %** of the profile's sup norm, not `8 %`. The universality claim survives
qualitatively and is weaker than advertised by a factor `1.7`.

Other reproductions from the archive (no rerun needed): `crosscheck_regime.json` and `analysis2.log`
match the §2.4 table (`2.58e−7 … 2.82e−6`) ✓; `domain_probe.json` matches §5.3 ✓; `toy10.json` matches
§7bis(4) to all digits ✓; `analysis_primecut_eU.log` documents the `1.605e−4` artefact ✓ and the
`e^U`-cut toy table saturating at `1.61e−4` ✓.

Two smaller inaccuracies:
* §2.3 (`:101–102`): "`min f` moves … by `< 1·10⁻⁹` from `Γ = 800` to `Γ = 20000`". `resid_check.json`
 gives `minf(800) = −0.064787958523`, `minf(20000) = −0.064787963189`: **`4.7e−9`**, and the pointwise
 deviations are only reported against `Γ = 400` (`1.006e−7` vs `9.98e−8`), so no `10⁻⁹` bound on
 `sup_τ|f_{800} − f_{20000}|` is in the data. Harmless at `|c| ≈ 10⁻²`; the sentence is still false.
 Also: `resid_check.py` is run at **one** window (`T = 0.62`) and is quoted as justifying `Γ = 800`
 for all 103; `U = 2T + 8.25` grows with `T`, so say "checked at one window".
* `reglib.py:8` says the cubic B-spline has "support 2h"; it has support `4h` (`Win.U = u_J + 2h`,
 `reglib.py:33`, and `R155_008:80` says `4h` correctly). Docstring bug only.
* §2.2 "≤ 3002 rows": `3001` grid rows + budget + edge = `3003`. Trivial.

---

## 5. The reconciliations the file owes, and does not give

**(a) `c_fine(½log3) = −1.85·10⁻²` here vs `−3.317·10⁻⁴` in `R155_005`.** `win_log3h.json` records
`R155_005`'s class at the same window: `M = 8, h = 0.1373, J = 91, U = 14.007`. `R155_008` uses
`h = 0.25, J = 30, U = 9.349` — coarser **and** shorter. The new class is therefore **56× weaker at the
one window where the two can be compared**, and `R155_008` never says so. This matters everywhere:
the "universal profile", the in-regime laws, the continuity ratios and the extrapolation are all
measured at a value floor set by `(h, J, U, L)`, not by the window. The file half-admits this
("the constant is a property of `(h,J,U,L)`", `:241`) and then reads the same data as a law of the
problem in §0.2–§0.4 and §9.1. The class choice is defensible (comparability across `T` was the
`R155_006 §5` repair) but the price must be stated in §0.

**(b) Why the zero-side LP is worse than the prime-side certificate (`λ_min ≥ 8.8577e−5`, Paper 46
Thm. C).** The file only says "far weaker" (`:203`). The mechanism is available and should be named:
Paper 46 Prop. TK (`main.tex:1237`) shows that lattice classes of step `d = 2T/M` are ceiling-limited,
with `Ceil(8) = −5.4·10⁻³ < 0` at `½log3` — "no lattice certificate of step `≥ 2T/8` can prove
positivity at `½log3`". Here `h = 0.25` against `2T/8 = 0.1373`, i.e. an effective `M = 2T/h ≈ 4.4`,
**coarser than the class Paper 46 already proves cannot certify**, and the measured `−1.8·10⁻²` sits
squarely in that regime (`λ_min(C_8) = −1.33·10⁻²`). Prop. TK does not literally apply (the spline/`ψ`
class is a density, not an atomic lattice measure), so this is a reading, not a theorem — but it is
the explanation of the floor and it makes the whole sweep's negativity unsurprising. A file whose
§0.4 conclusion is "the pattern that extrapolates is the pattern of not closing" must say that its
class was below the known ceiling before the first LP was run.

**(c) `R155_006 §6`'s conditioning objection was not answered.** §6 fits the *profile* and, separately,
fits the *value*; it never evaluates `inf f` of the predicted weight — which is precisely the test
`R155_006` ran (4 % profile error ⟹ factor 7 in value). I ran it (extrapolate `(y,x)` affinely inside
regime `k`, evaluate the zero side at the first window of `k+1`, `Γ = 800`, grid `0.02`, ~30 s):

```
|N|2->3 T=0.6936 inf f(pred w)=-1.1772e-01 inf f(last-window w)=-7.2623e-02 LP opt=-7.1755e-02 1.6x / 1.01x L1(pred)=22.4 (> L=20: infeasible)
|N|3->4 T=0.8052 -1.8225e-01 -1.4631e-01 -1.3908e-01 1.3x / 1.05x L1=16.8
|N|4->5 T=0.9735 -2.8351e-01 -2.1848e-01 -2.1100e-01 1.3x / 1.04x L1=19.9
|N|5->6 T=1.0402 -2.7492e-01 -2.1809e-01 -2.1195e-01 1.3x / 1.03x L1=15.9
|N|6->7 T=1.0991 -2.7078e-01 -2.3936e-01 -2.3444e-01 1.2x / 1.02x L1=12.2
|N|7->8 T=1.1994 -3.7380e-01 -3.0070e-01 -2.9160e-01 1.3x / 1.03x L1=20.8
```

So the honest end-to-end prediction loses `1.2–1.6×` (not `0.3–11 %`), the "same as last window"
weight loses `1–5 %`, and one extrapolated weight is **outside the budget** (`L1 = 22.4 > 20`), i.e.
not a member of the class. The conditioning is mild here only because every value is `10³`–`10⁴` times
its own distance from `0`; `R155_006`'s factor `7` was measured near `10⁻²`. §6(i) must be rewritten
as "the *fitted* value and the *fitted* profile extrapolate; the value of the extrapolated weight is
1.2–1.6× worse than the optimum, and the affine extrapolate can leave the budget".

**(d) The `R155_005 §4.4` Nyquist reading.** Correctly reported as not reproduced (`:389`), with the
right arithmetic (`2π/U ≈ 0.67` would allow ≈ 89 contacts on `[0,60]`, 24 appear). Accepted — but note
the contact count depends on the ad-hoc `1e−5` threshold in `run_regime.py:58`, so "not reproduced" is
the safe claim and "the Nyquist reading does not survive" is one step further than the data support.

---

## 6. `R155_006` repairs: adoption check

| repair (`R155_006`) | adopted? |
|---|---|
| GL order `200 → 800` on the B-spline integrals | **yes** (`reglib.py:f_prime_side(..., gl_n=800)`; `crosscheck_regime.py`, `toy10.py`) |
| Bernstein grid lemma; every value certified | **yes** (`reglib.bernstein_slack`, `refine_min`, `c_cert` in the CSV; `δ = 0.005`) |
| in-regime fitting only | **yes** (`fit_regime.py`; no training set straddles an entry) |
| `≥ C¹` across the edge | **yes, `C²`** (`Σy_i = 1` equality row; `ψ_s'(0)=ψ_s''(0)=0`; splines start at `j = 2`) |
| report true norms `‖w‖_∞`, `∫|w|` | **yes** (CSV columns `winf`, `absmass`) |
| `L` not comparable across `M`-dependent lattices | **yes**, fixed `h`, `J`, `U` in the variable `v = u−2T` |
| delete "`min f^prime = −8.69e−5`" | **yes**, absent |
| re-measure the `∫w` invariant at `L = 20` on a certified grid | **yes** (`3.128 ± 0.067`, grid inflation `8e−4`) |
| §6 conditioning (predict `w`, then evaluate `inf f`) | **no** — see §5(c) |
| §11(b) "the contact comb is a class statement" | **yes**, and re-measured (not reproduced) |
| §12(ii) warning on the `0 ≤ w ≤ 1` conjecture | **yes**, quoted and sharpened (`:509–515`) |

Labelling: `DIAGNOSTIC` on every zero-derived number, in the file, in both READMEs and in every script
docstring; circularity no-go cited (`phase-4-krein-space-realization/proofs/00-PROOF-LOG.md:168`, `phase-136 MAP_1:141`);
no sign claim for `T > log 2`; endpoint of record unchanged (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`);
Paper 46 Thm. C used as the honest comparison. **ACCEPT, no label change.**

---

## 7. The five §9 proposals

1. **Regime dichotomy (E+D+C) for Paper 46 §8.2 — NEEDS REPAIR, then include.** Fix the one-sided
 limits of Prop. E; say `2πe^{A_T}` is the multiplier-free threshold (Prop. env's threshold for a
 flat-top certificate carries `‖ν_w‖_TV`, `≈ 48.7` for the weights measured here); delete "real
 analytic"; restate Prop. C's corollary as "the value of a `T`-independent shape family at a fixed
 domain is continuous in `T`", dropping "the class `W_T` varies continuously". With those four
 edits it is half a page of correct, zero-free mathematics and it does replace §8.2's qualitative
 "three scales" bookkeeping. The reading "primes are expensive, prime powers cheap"
 (`e^{v_p}` vs `e^{v_{p^k}}`) is correct and worth the sentence.
2. **Lemma R beside Cor. 7.4 — PAPER-READY (the lemma), DO NOT INCLUDE (consequence (b)).**
 The lemma plus consequence (a) — `ŵ` is never `≥ 0`, so a flat-top certificate is always a
 cancellation statement, and the entire "build `w` with `ŵ ≥ 0`" family is dead in three lines — is
 the best thing in this deliverable and belongs in §7. Add the citation for `ŵ ≥ 0, w ∈ L¹ ⟹ ŵ ∈ L¹`.
 Consequence (b) must not be printed as proved; at most as (b′) for compactly supported `w`, or as
 an open question.
3. **Prop. M in §8.3(4) — include as one sentence, not as a proposition.** True, but it is Cor. `mono`
 with the class inclusion made explicit; Paper 46 already states the monotonicity. The valuable
 half is the remark that the *sub*-classes used by optimisers are not nested, so their measured
 non-monotonicity carries no information.
4. **Sharpened bounded-profile conjecture (Problem A) — NEEDS REPAIR before it is stated.** The
 supporting numbers must be corrected: `0 ≤ w ≤ 1` "at 102 of 103 windows" is `‖w‖_∞ ≤ 1 + 10⁻²`
 at 102, `≤ 1 + 10⁻⁶` at 98; the profile universality is `0.133`, not `0.0785`; and the evidence
 comes from a class below Paper 46's own Prop. TK ceiling. As a *conjecture* with `R155_006 §12(ii)`'s
 caveat (`0 ≤ w ≤ 1` **plus** a decay modulus) it is worth a line in Problem A; it is, as the file
 itself says, evidence for another upper bound, i.e. another negative.
5. **Verification-budget lemma — DO NOT INCLUDE as stated.** The inequality
 `|f_w(τ) − Σ_{|γ|≤Γ}ŵ(τ−γ)| ≤ C(L,U)Γ^{-3}logΓ` is `R155_006 §11(a)(1)` with `k = 2` and is fine.
 The slogan — "a finite table can falsify a certificate, never verify one" — is **false as a
 dichotomy**: the very bound quoted is two-sided, so `min_{δ-grid} Σ_{|γ|≤Γ} ŵ(τ−γ) − ½U²‖f‖_∞δ² −
 C Γ^{-3}logΓ ≥ c` *verifies* `f_w ≥ c`, given RH below `Γ` — which is a known finite computation
 (and is exactly the hypothesis `R155_006 §11(a)(1)` attaches). What is true is the weaker and
 already-published statement of Cor. `zeros`: **without** RH below `Γ` the tail is controlled only
 after the factor `e^{U/2}`. Restate as that, or drop; the `≈100`-zero crossover number is a nice
 `DIAGNOSTIC` remark either way.

---

## 8. Survival list

**Survives as `PROVED` (after the stated edits):**
* Prop. D, `D(T) = e^{A_T−2T}` — unconditional, verified to `10⁻¹³`.
* Prop. E, with one-sided limits fixed and `τ_env` named as the multiplier-free threshold.
* Prop. C, as "continuity in `T` of the objective of a `T`-independent shape family at a fixed domain";
 without the corollary's extension to `W_T` / `λ^W`, and without "real analytic".
* Prop. M, as a one-sentence strengthening of Paper 46 Cor. `mono`.
* **Lemma R** + consequence (a). The one genuinely new and paper-ready statement of the file.

**Survives as `DIAGNOSTIC`:** the 103-window table and `c_cert` (all negative, margin ≥ `2.8·10⁻²`);
the eight-regime Theorem-Z cross-check (`2.6e−7…2.8e−6`); the `1.6·10⁻⁴` `e^U` prime-cut artefact
(a reproducible bug class worth keeping in the READMEs); the cancellation budget (`10` zeros ⟹ `4.0e−4`,
`10²` ⟹ `6.0e−6`, `10³` ⟹ `1.2e−7` floor), with "minima over `[0,16.75]`" stated; the `2.4×`/`4.6×`
domain probe, relabelled (not "the true interval"); the profile universality **at `0.133`**, and only
as a property of `(h, J, U, L)`.

**Does not survive:**
* "`0.0785` sup-norm universal profile" (`:35, :224`) and "`0.095`" at `L = 5` (`:235`) — 17-point
 sampling artefacts; true values `0.1332`, `0.1378`.
* "`capped = 1` at 79 of 103" (`:200`) — it is 82.
* "`‖w‖_∞ = 1` exactly at 102 of 103" (`:237`, `:507`) — 98 at `10⁻⁶`.
* "`< 1·10⁻⁹` from `Γ = 800` to `Γ = 20000`" (`:102`) — `4.7·10⁻⁹`, one window only.
* "the domain is the whole of it" / §5.2 as a refutation of `R155_005` (`:256–263`) — the domain was
 frozen at all six entries measured; the one entry with a moving domain gives `3.17×`.
* "its **true** interval `[0, τ_env]`" (`:288`), "the honest form of the jump law" (`:296`) —
 `‖ν_w‖_TV ≈ 48.7` ⟹ Prop. env's threshold is `≈ 2.4·10²²`.
* "the prediction works … for the value" (`:314`) — the end-to-end test loses `1.2–1.6×` and one
 extrapolate is infeasible.
* "a finite zero universe admits no flat-top certificate whatsoever" (`:426–428`) — proof gap.
* "a finite table can falsify a certificate, never verify one" (`:519`) — false as a dichotomy.
* Prop. E's `A_T − A_{T^-} = v_n` and the corresponding `τ_env` ratio (`:333–335`) — wrong one-sided
 limits under `reglib.py:141`'s strict `<`.

**Must be added before any of this is quoted again:** (i) the class of `R155_008` is `56×` weaker at
`½log3` than `R155_005`'s and coarser than Paper 46 Prop. TK's `M = 8` ceiling class; (ii) every
continuity/extrapolation reading is conditional on the frozen `τ ≤ 60` domain.

*Row D label: unchanged. Endpoint of record: `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` (Paper 46 Thm. C).
No sign claimed for any `T > log 2`. Nothing in `R155_008` or in this audit is a statement about zeros.*

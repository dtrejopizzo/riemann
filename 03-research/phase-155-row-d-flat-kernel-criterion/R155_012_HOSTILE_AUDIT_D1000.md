# R155.012 — Hostile audit of R155_011 (`D` for 1000 zeros)

*Hostile auditor, phase 155. Date 2026-09-21. Target: `R155_011_D_FOR_1000_ZEROS.md` and
`scripts/reverse/d1000/`. Reference: Paper 47 `main.tex` §5 (`lem:bern`), §7 (Thm Z (7.2),
`lem:Rrig`, `cor:nontermwise`, `lem:smooth`), §8 (`prop:env`, `prop:TK`, `thm:N`, `thm:R`),
and `R155_009`/`R155_010` standing rules.*

*Reruns performed: all ≤ 60 s, single process. The 35-minute far scans were **not** rerun; three
points of each far scan were re-evaluated pointwise (three independent routes) instead.*

**Bottom line: the arithmetic is sound and the headline numbers reproduce, but the two structural
arguments the builder advertises as "theorems, not measurements" — the Prop.-TK impossibility (§0.2,
§3.1, §6.4, §7) and the Theorem-N "above the ceiling" framing (§2.1) — are category errors: neither
theorem applies to this weight class. The negativity is established only by the far scan. Six further
repairs below; nothing that changes a label of record.**

---

## §1 Verdict table

| # | claim | verdict |
|---|---|---|
| 1(a) | prime-side evaluation correct | **CONFIRMED** |
| 1(b) | "Prop. TK proves it cannot be positive on ℝ" | **WRONG** |
| 1(c) | multiplier-free `16.75` is not the verification interval; honest `10^22.6–10^44.3` | **CONFIRMED (direction); REPAIR (constant — it is worse than stated)** |
| 2 | `λ^W` control and the `λ^P − λ^W` reading | **CONFIRMED (numbers); REPAIR (reading)** |
| 3 | two-prime windows negative on `[0,59.54]`, interval right | **CONFIRMED** (the prompt's premise that `59.54` over-defends `0.58`/`0.62` is itself false) |
| 4 | residual budget `1e−5`, constant `32Σ|x|/h³`, `Γ ≳ (‖x‖₁M³/c)^{1/3}` | **CONFIRMED (algebra + data); REPAIR (the constant does not explain the data — it overshoots ×10³)** |
| 5 | insight (i)–(v) | **REPAIR**: "12 negative lobes" is a code artifact; the first-lobe/zero-gap attribution is unsupported; contacts-on-Nyquist is *necessary*, not observed; top-5 share is `0.35–0.76` |
| 6 | rules, labels, budget | **CONFIRMED** except "effective order 24 above Theorem N's ceiling of 8", which is **WRONG** (same category error as 1(b)) |
| 7 | corpus check | **CONFIRMED** (good; one gap) |

---

## §2 Claim 1(a) — the prime side. CONFIRMED.

Reproduced (`d_log3h_b.json`, 1.5 s):

```
min over [0,16.75] of f_prime_fast + beta.ghat   = +1.3743944e-3  at tau = 11.1220
f_prime (per-B-spline, GL 800) at tau = 11.1224  = +1.3743930e-3
max |f_zero(1000) - f_prime| on a 0.05 grid      =  6.8521e-6
tau = 17.4356:  zero side -7.321096 | fast -7.321095 | slow (GL 800) -7.321095
```

- The multiplier columns in `check.py:20-25` are exactly `main.tex:444`
  (`ĝ₀ = 2∫₀^{2T}cosh(u/2)cos τu`, `ĝ₁ = 2∫₀^{2T}u sinh(u/2)cos τu`), GL 600 on `[0,2T]`; and
  `f_w = s_T + ν̂_w + 2ĝ₀` (`main.tex:220`) is respected, the free columns being `(β₀−2, β₁)`.
- Full prime-power sum verified: `prime_table(14.0)` returns **93 372** prime powers up to
  `1 202 609 ≈ e^14`; `primeside.py:15` uses `Umax = 14`, not `U ≈ 7.74`, so there is **no `e^U`
  truncation** and the `1.6e−4` artefact of `R155_008` is genuinely gone.
- GL order 800 per B-spline support is used in the slow path (`primeside.py:6,25-26`); the fast path
  agrees with it and with the zero side to `1e−6` at every point tested, on and off the LP interval.
- `−7.321 @ 17.436` is confirmed by **three** independent routes. The far scan need not be rerun.

Residual concern (**REPAIR**, does not change the sign): `check.py:41-45` takes the "fine" minimum
over a refinement of only the **60 smallest coarse nodes**, not over a `δ/50`-dense grid of the whole
interval, yet subtracts the pad `B₂(δ/50)²/8 = 4.1e−6` computed *as if* the grid were dense. The
honest `lem:bern` statement with the grid actually covering the interval (`δ = 0.005`, `B₂ = 3297.7`)
gives pad `1.03e−5`, hence `min_{[0,16.75]} f_w ≥ +1.364e−3`. Still positive; the reported
`+1.3703e−3` is not a valid enclosure as computed. For the negative runs the same slip is harmless
(a grid minimum is already an upper bound for the infimum).

## §3 Claim 1(b) — the Prop.-TK argument. WRONG.

`prop:TK` (`main.tex:1421-1425`) hypothesises that `ν` is *a finite even measure supported on the
lattice `{±jd : j ≥ M}`*. The proof (`main.tex:1437-1440`) uses that and only that: `ν̂` is then
`P`-periodic with Fourier modes `|j| ≥ M`, so `∫_{τ₀}^{τ₀+P} ν̂ φ = 0` for every `φ = |q(e^{idτ})|²`.

The certificate measure here is
`ν_w = [½(1−w)K + 2w cosh(u/2)]·1_{|u|≥2T} du − Σ_n v_n w(log n) δ_{log n}`. Neither piece qualifies:

1. the absolutely continuous part is not atomic, is not supported on any lattice, and its transform
   is **not periodic**, so `∫ν̂_w φ ≠ 0` and the orthogonality that *is* the whole proof fails;
2. even the atomic part sits at `{log n}`, not on `{j·2T/24}` — e.g. `log 4 / h = 1.3863/0.0457755
   = 30.284`, not an integer.

So `Ceil(24, ½log3) ≈ 5.9e−4` **is not an upper bound for this class**, and `+1.38e−3 > 5.9e−4` is
not a contradiction: it is simply a value from a larger class. The claims at
`R155_011:§0.2`, `§3.1` ("*proof, from the corpus's own theorem and with no experiment*"),
`§6` item 4 ("*therefore proves*"), and the `§7` label row ("*forced by Prop. TK*") are **all invalid
and must be struck**. Prop. TK extends to non-atomic `ν` only if `ν̂` still has mean zero against
every nonnegative degree-`≤M−1` trigonometric polynomial in `dτ`, which for a continuous shoulder and
an arithmetic comb is false.

What survives in its place, and is genuinely a theorem:
`cor:nontermwise`(ii) (`main.tex:1175`) forces a sign change of the *truncated zero sum* for a
compactly supported `w` with a jump in `w'''`, so **some** far negativity was guaranteed; but it does
not locate it, and it is a statement about the truncation, not about `f_w` itself. The negativity of
this particular `f_w` on ℝ is therefore established **only** by the far scan (`−7.321 @ 17.436`), which
is `DIAGNOSTIC` double precision. The conclusion "no new endpoint" is unaffected — it never depended
on TK — but the epistemic status of §0.2 drops from *theorem* to *measurement*.

## §4 Claim 1(c) — the envelope. CONFIRMED in direction, REPAIR in constant.

`prop:env`(i) requires `τ_env = 2πe^{A_T+‖ν‖_TV}`, and `‖ν_w‖_TV` for these weights is `E = 50.1…100.2`
(`chk_*.json`). So the LP defends `16.75` of an interval of length `10^22.6…10^44.3`. Direction and
order of magnitude CONFIRMED. Three defects, all in the **conservative** direction (the honest
threshold is larger than the builder reports), so the negative conclusion strengthens:

- `check.py:63`: `log10_tau_env_honest = E/log10 + log10(2π)` **omits `A_T`**, though §3.2 of the
  report says the threshold is `A_T + E`. Missing `0.43` decades (`½log3`), `0.98` (`log 2`).
- `check.py:57-58`: `E1` integrates `(1+|w|)K` over `u ≥ 2T` only; the TV norm is over ℝ and the
  measure is even, so `E₁` is short by a factor 2 (`≈ 4`, minor).
- `check.py:60`: `E2 = Σ 2Λ(n)/√n |w(log n)|` is likewise one-sided; short by a factor 2. This one is
  **not** minor: `E₂ = 23.0…45.0`, so the honest `E` is nearer `80…145` and `log₁₀τ_env` nearer
  `35…63`. `E₃` (`check.py:61`, the doubled `cosh` term) is correctly two-sided.

The reading "the LP defends `10⁻²²` of the interval" is right and if anything understated.

## §5 Claim 2 — `λ^W` control. Numbers CONFIRMED, reading REPAIR.

`chk_log3h.json`: `c_lp = −2.2410e−5`, `min_f_prime_fine = −3.2982e−5`,
`certified_prime_side = −4.1690e−5`. Reproduces the table exactly.

But the inferences are not licensed:

- A restricted class gives a **lower** bound on the sup, so `−2.24e−5` says `λ^W ≥ −2.24e−5` and
  nothing more. It is consistent with Theorem C's `λ^P ≥ 8.8577e−5` **trivially**, and it does **not**
  show `λ^W < λ^P`. Comparing one budgeted class value to another budgeted class value measures the
  value of the two multiplier columns *inside this LP*, not `λ^P − λ^W`.
- "the first measured gap" therefore overstates. The defensible sentence is: *within the C² flat-top
  class with `Σ|·| ≤ 60`, `|x| ≤ 3`, `|β| ≤ 50`, on `[0,16.75]`, releasing `(β₀−2, β₁)` changes the
  optimum from `−2.2e−5` to `+1.4e−3`.*
- And, as the prompt anticipates: since the `β`-free value is not a certificate on ℝ (§3, §4), the
  comparison is between two non-certificates, so it constrains neither `λ^W` nor `λ^P`.
- The report's own §6 "Neither, and explicitly open" already concedes the budget-dependence; §0.2 and
  the §7 label row do not. Align them.

## §6 Claim 3 — two-prime windows. CONFIRMED; the prompt's premise is wrong.

`A_T = Σ_{n<e^{2T}} 2Λ(n)/√n` depends on `T` only through *which prime powers* lie below `e^{2T}`.
For `T ∈ (½log3, log2]` that set is `{2,3}` throughout (`e^{1.16}=3.19`, `e^{1.24}=3.46`, `e^{1.386}=4`),
so `A_T = 2.24883` and `2πe^{A_T} = 59.53` at **all three** of `0.58`, `0.62`, `log 2`
(`main.tex:1004-1006` states exactly this). There is **no over-defence**: `59.54` is the correct and
identical multiplier-free envelope at each. Good.

Certified "on the interval only" — and for these runs that is the right and sufficient direction:
`inf_ℝ f ≤ inf_{[0,59.54]} f < 0`, so the negative values **are** statements about ℝ, without any pad.
(The report's use of the word "certified" for a `B₂δ²/8`-padded negative number is over-careful
rather than wrong.) Prime-side values reproduce: `−5.8650e−3`, `−2.3807e−2`, `−3.4395e−2`
(`chk_w058/w062/wlog2.json`), zero-side agreement `3.6e−6…8.5e−6`.

## §7 Claim 4 — residual budget. Algebra CONFIRMED, attribution REPAIR.

- Normalisation verified: `revlib2.beta_spline` integrates to `1.0000000000` in `z`, so a shoulder atom
  contributes `2 x_j h cos(u_j t) sinc⁴(th/2)` and `|sinc⁴(th/2)| ≤ (2/th)⁴`, giving
  `|ŵ_lattice(t)| ≤ 2h(2/(th))⁴ Σ|x| = 32Σ|x| h^{−3} t^{−4}`. **The constant `32Σ|x|/h³` is correct.**
- With `N(t) ~ (t/2π)log t`, `Σ_{|γ|>Γ}|ŵ| ≤ C‖x‖₁h^{−3}Γ^{−3}logΓ`, and `h = 2T/M` gives
  `Γ ≳ (‖x‖₁M³/c)^{1/3}` up to `(2T)^{−1}` and a `log` factor. **P1 is correct as an upper bound.**
- But it does **not** explain the measured residual, and §4 item 1 claims it does. At
  `h = 0.0458, Σ|x| = 48.96, Γ = 1419`: `32Σ|x|/h³ = 1.63e7` (matches the report's `1.6e7`), and the
  bound predicts `1.63e7 · Γ^{−3}logΓ/2π ≈ 6.6e−3`. The **measured** residual is `6.85e−6` — the bound
  overshoots by `10³`, because `sinc⁴` oscillates and the lattice sum cancels. So: the *ladder* is
  measured (`1.03 → 3.0e−3 → 6.9e−6`, slope `≈ Γ^{−2.6}`, consistent with `lem:smooth`'s `Γ^{−3}logΓ`),
  and the *constant* is an upper bound that is `10³` loose. The sentence "the constant is `≈10⁴` larger
  than the naive `10⁻⁹` **because** the amplitude is `32Σ|x|/h³`" is a post-hoc fit, not a derivation.
  State P1 as a bound and the `h⁻³` conflict as a *worst-case* conflict.
- Ladder values all reproduce from `chk_*.json` `ladder.max_abs_diff`
  (`1.1016e−5`, `6.852e−6`, `1.1273e−5`, `8.529e−6`, `3.560e−6`, `6.115e−6`) ✓.
- Under-training CONFIRMED: `chk_log3h_z100.json: min_f_prime_fine = −5.0652e−4` (LP value
  `+1.3843e−3`); `chk_log3h_z10.json: −1.3026` (LP `+1.1909e−3`). This is the most valuable
  observation in the file and it is correctly labelled.

## §8 Claim 5 — the insight. REPAIR (four items).

- **"12 negative lobes" is a code artifact.** `insight.py:31` truncates the lobe list to the first 24
  (`[:24]`); lobes alternate in sign, so **every** run reports exactly 12. `insight.json` confirms
  `n_neg_lobes = 12` for all five weights. The number carries no information; delete the column or
  recount without the cap.
- **The first-lobe / mean-gap attribution is unsupported.** Observed first negative lobe:
  `3.622, 2.730, 3.608, 2.848, 2.624`. The report attributes this to the mean gap of the lowest zeros
  (`3.03 @ γ≈50`). But a flat top of half-width `2T` alone puts the first zero of `ŵ` at `π/2T =
  2.86, 2.71, 2.53, 2.27` — the same range, with the *same monotone decrease in `T`* the report
  highlights in §5(v). The data cannot separate the two explanations, and the class-geometric one
  needs no zeros. **Withdraw the zero-gap reading; keep the positions as DIAGNOSTIC.**
- **"Contacts on the Nyquist comb `2π/U`, unrelated to zeros" is NECESSARY, not observed.** `f_w` is
  band-limited to `[−U,U]`, so its oscillation scale is bounded below by `2π/U`, and at the Chebyshev
  optimum (Theorem O) it equioscillates at that scale. The report files this under "Observed"
  (`§6`); it belongs under "Necessary". And the *question* is indeed degenerate at `½log3`: the whole
  interval `[0,16.75]` lies essentially below `γ₁ = 14.135`, so "which gap is the contact in" has one
  answer for 20 of the 21 contacts. That is worth saying plainly rather than reporting `frac_in_gap`
  trends (`insight.py:46`) that are just `τ/2γ₁`.
- **Top-5 share is `0.35–0.76`, not `0.50–0.76`.** Recomputed over all contacts in `insight.json`:
  `log3h_b 0.504–0.715`, `log3h_b60 0.497–0.740`, `w058 0.393–0.755`, `w062 0.399–0.711`,
  `wlog2 0.352–0.736`. Also the denominator is the first **60** zeros only (`insight.py:44`), so the
  share is *within the head*, not of the whole sum. §0.5's "five of the first sixty" is right; any
  reading as "the value lives on nine zeros" is not.
- CONFIRMED as stated: the three orders of cancellation (terms `≈1`, value `10⁻³`), the rotating
  identity of the top contributors, `ŵ(0) = 0.932` at `log3h_b` with a first negative lobe deeper than
  the central peak, and the §5(iv) rejection of Rem. 7.6's `log p` heuristic (the `log 2` weight is
  positive and comb-free across `[1.6,3.4]`). The `log 4` observation is correctly demoted to a
  one-window coincidence.

**§6's necessary/observed separation is the best part of the file but is mis-sorted twice**: item 4
(TK) is not necessary — it is *wrong* (§3 above); the Nyquist contacts are not observed — they are
necessary. Items 1, 2, 3, 5, 6 are correctly classified.

## §9 Claim 6 — rules. CONFIRMED, one category error.

- `DIAGNOSTIC` labelling: thorough and correct throughout §7; the front-matter disclaimer is
  unambiguous; no sign is claimed for `T > log 2`; no new endpoint is claimed; the endpoint of record
  `8.8577e−5` is explicitly left unchanged. ✓
- Budget deviation declared in §2.5 and consistent with the artefacts: `chk_*.json` `t` fields sum to
  `≈ 1 900 s`, plus the insight pass — the stated `≈ 35 min` is honest, not rounded down. ✓
- **"Effective order 24, above Theorem N's ceiling of 8" (`§2.1`, `README.md` files table) is a
  category error.** `thm:N` (`main.tex:1534`) is about measures supported on `{±j·2T/M : j ≥ M}`.
  The flat-top class is not in that family at any `M` (§3 above), so it is neither inside nor above
  Theorem N's impossibility region; `M = 24` here is a B-spline knot spacing, nothing more. Harmless
  to the conclusions (it claims no positive result) but it must not be repeated, and `R155_010 §2.3`'s
  rule "start above the TK ceiling" is **inapplicable** to flat-top classes, not "obeyed".

## §10 Claim 7 — corpus check. CONFIRMED.

The §1 table is honest and the precedents are correctly characterised: `phase-118 W5` is indeed the
primal identity and not (7.2); `phase-114/114_e_00_counterfactual_harness.py:86` is the only prior
finite zero model and it never evaluates the prime side; the ES-2 circularity no-go is respected by
the FIND/PROVE split, which is real here (the LP never touches `primeside.py`). One gap: the check
did not search for the *Prop.-TK-applicability* question, which is why the §3 error survived —
`R155_004`/`R155_010` compute `Ceil(M)` only for lattice-atomic certificates, and nothing in the
corpus licenses transferring it. Add "does the theorem I am invoking have this class in its
hypotheses" to the corpus-check protocol.

---

## §11 Survival list

**Lemma material for Paper 47.**

1. **(P1), with the statement repaired.** For a cubic-B-spline shoulder of step `h` with coefficients
   `x`: `|ŵ_lattice(t)| ≤ 32‖x‖₁h^{−3}t^{−4}`, hence
   `|Σ_{|γ|>Γ}ŵ(τ−γ)| ≤ C‖x‖₁h^{−3}Γ^{−3}logΓ` and `Γ ≳ (‖x‖₁M³/c)^{1/3}`. One page, no zeros in the
   proof, correct as an upper bound. **Must be stated as a bound**, with the remark that it is
   observed `10³` loose. Place beside `lem:smooth`. Strip the claim that it *explains* the measured
   residual and, since Theorem N does not cover this class, strip the "two-sided constraint with
   Theorem N" corollary as written.
2. **(P2), the envelope-budget lemma — the strongest proposal in the file.** `τ_env(w) = 2πe^{A_T+E(w)}`
   with `E = E₁+E₂+E₃` computable from `w`, `E₃ = 4∫|w|cosh(u/2)` dominant, and
   `‖w‖_∞ ≤ 1, supp w ⊂ [−U,U] ⟹ E₃ ≤ 8e^{U/2}`. Converts `R155_008`'s bounded-profile conjecture into
   a quantitative payoff. Fix the factors of §4 above before writing it.

**Diagnostic, keep as measured.** All of §3 and §4; the under-training pathology (100 zeros ⟹
prime-side `−5.07e−4`); the `λ`-free reading of the multiplier release; the `log 4` one-window
observation; the sign flip at `τ_max: 16.75 → 60`; the far-scan locations.

**Wrong, strike.** The Prop.-TK impossibility argument in §0.2/§3.1/§6.4/§7; "above Theorem N's
ceiling" in §2.1 and the README; "12 negative lobes"; the first-lobe/zero-gap attribution;
"`λ^P − λ^W` is the whole value" as a statement about `λ`; `+1.3703e−3` as an enclosure (use
`+1.364e−3`); the `log₁₀τ_env` constants (too small).

**Judgement of §8.** (P1) repair and ship. (P2) ship — it is the only proposal that touches the wall.
(P3) **run it**: `‖w‖_∞ ≤ 1` on `[0,60]` at `½log3` is one 60 s LP and it is the cheapest decisive
experiment available; it tests P2's hypothesis directly. (P4) low value — as §5 shows, the quantity
being swept is not `λ^P − λ^W`; run it only as a class diagnostic, and relabel. (P5) **agree, and
strengthen**: do not repeat the finite-universe experiment, and do not build another flat-top LP on a
short interval; the informative runs are the ones on `[0, ≥60]`, which are uniformly negative.

---

## §12 Answer to the lead: is there a path to a new prime-side-certified endpoint at `T ∈ (½log3, log2]`?

**Prop. env does not by itself kill the track, but nothing in this file opens it, and the measured
evidence is uniformly against.** Three points.

1. **Prop. env is a stopping criterion, not a work requirement.** The paper says so explicitly
   (`main.tex:1014-1018`): whether a certificate must do work on all of `[0,2πe^{A_T}]` is *not*
   asserted, and the periodic `lem:F1` closes the tail of the lattice certificate at `τ ≈ 442`, not at
   `10^40`. So "interval length" is not a theorem against flat-top classes — it is a theorem against
   the *TV-based* tail bound, which is the only tail bound this track currently has.
2. **The missing object is a decay-based tail lemma for flat-top weights.** `lem:Rrig`/`lem:smooth`
   give `ν̂_w(τ) = O(τ^{−k−2})` for a `C^k` edge, while `m(τ) ~ log(τ/2π) → ∞`. A bound
   `|ν̂_w(τ)| ≤ D(w)τ^{−2}` — explicit, one integration by parts, no zeros — would close the tail at
   `τ ≍ D^{1/2}`, i.e. at `O(10²)` rather than `10^{25}`, for **every** flat-top class. This is the
   smooth analogue of `lem:F1` and it is the single highest-value open item this track has. It is
   what (P2) is groping toward; it does not appear in the file as a proposal.
3. **But then the verification interval is `[0, ~10²]`, and every measured value there is negative.**
   `−2.86e−3` at `½log3` on `[0,60]`; `−5.87e−3`, `−2.38e−2`, `−3.44e−2` at `0.58`, `0.62`, `log 2` on
   `[0,59.54]` — all confirmed prime-side, all budget-saturated (`Σ|·| ≤ 60` and `|x| ≤ 3` both bind,
   so these are budgeted class values, not class optima). The `+1.37e−3` at `½log3` exists only
   because `16.75` happens to sit just short of the first deep trough at `17.44`.

**Recommendation.** The track has exactly one remaining lever, and it is a *pair*: the decay-based
tail lemma of (2) **together with** the bounded-profile class `0 ≤ w ≤ 1` of (P2)/(P3), which is the
hypothesis that keeps `D(w)` and `E(w)` small. Until (P3) returns a value on `[0,60]` that is not
negative, there is no path to a new endpoint at any `T ∈ (½log3, log 2]`, and the honest statement is
that the flat-top LP track has been measured and found negative on every honest interval, at every
window tested, including `½log3` where the endpoint of record already stands by other means.

---

*No label of record changes. Endpoint of record unchanged: `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` (Thm C).
Reruns for this audit: `≈ 5 s` total, single process; the 35-minute far scans were not repeated.*

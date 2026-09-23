# R155.019 — Hostile audit of R155_016 (comb-vanishing LP) and `scripts/reverse/comb/`

*Auditor, phase 155, round 2, 2026-09-21. Target: `R155_016_COMB_VANISHING_LP.md`,
`scripts/reverse/comb/{comblib,count,lp}.py`, `count.json`, `lp_*.json`. Rerun: `count.py` only
(1.1 s); the LPs were **not** rerun, their JSONs were re-read and post-processed.
No sign is claimed. Endpoint of record unchanged (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`, Paper 47 Thm C).*

## §0 Verdict

**The note survives.** No arithmetic error, no over-claim in the labels, one genuine over-statement
("`E_at = 0` exactly"), one under-statement (the negative verdict needs *no* Bernstein pad at all,
so the `B₂` defect of `R155_017` is irrelevant here), and two claims that must be demoted to
diagnostics with the margins written down (`D(w)` is a quadrature, not an enclosure; `U_eff`'s
constant is a two-point fit). The headline — *first flat-top run whose failure is a statement about
all of `ℝ`* — is **upheld, modulo the `D` quadrature**, with the tolerance folded in below.

---

## §1 The class and the forced coefficients — `PROVED`, verified

`g(2T)=1, g'(2T)=0, g''(2T)=0` for `Σ_{k=-1}^{1} x_k β((u−u_k)/h)`:
`g'` gives `x_{−1}=x_1`; `g''` gives `x_{−1}+x_1=2x_0`; `g` then gives `x_0/3+2x_0/3=x_0=1`.
Unique. **Confirmed.** The audit adds the step the note leaves implicit: the free splines start at
`j = 2`, and `β(±2)=β'(±2)=β''(±2)=0`, so they do not disturb the matching — the three-term ansatz
is not a restriction. `w` even, `C²`, `w''` piecewise linear hence BV, `supp w ⊂ [−U,U]`: the
hypotheses of **Theorem D case (a)** hold for the returned `w` (no positivity is required, and
`‖w‖_∞ = 2.35…3.00` with sign changes, so it is good that none is). **VERDICT: verdict stands.**

## §2 Counts, feasibility, saturation

`count.py` rerun (1.1 s), `count.json` overwritten identically. Reproduced exactly:
`½log3`, `M=48`, `U=6`: `m=96, dof=211, rank=85, nullity=126`, residual `0.0`; `M=24`:
`(U,m,dof,rank,null) = (3,10,38,10,28), (4,22,60,22,38), (5,45,82,41,41), (6,96,104,63,41),
(7,201,125,84,41), (8,450,147,106,41)`. Residuals `0` or `≤3.3·10⁻¹⁹` everywhere. **Table §2.3 is
correct.** New check: the same saturation holds at `0.58` (`113` at `M=48`, `U=6,7,8`), `0.62`
(`99`), `log 2` (`78`) — the note's "same numbers hold" is right in the qualitative sense, the
values differ per window.

**The saturation is real, and is more than measured — it is a rigorous nesting.** A comb-vanishing
`w` supported in `[−U,U]` is also comb-vanishing for any `U' > U`, so `null(U) ⊆ null(U')` *as
spaces of weights*. Equal dimensions therefore force **equality**, i.e. for these `(T,M)` every
comb-vanishing weight of support `≤ 8` already has support `≤ U_eff`. This upgrades (F1) from
"measured" to "a finite rank computation" (still double precision, SVD tol `10⁻⁹`), and explains —
does not merely correlate with — the `5·10⁻⁸` agreement of the `U=5` and `U=6` LP values.
**Recommend: state the nesting argument in the note; it is the lemma content.**

`U_eff ≈ log(1/h) + 1.9`: **a fit, not a law.** Two points, `c = 1.92` and `2.22`, with `U`
resolved only to `±0.5` (integer sweep), and the `u_first_tight` diagnostic (`3.43`, `4.62`) sits
`1.3–1.5` *below* the observed `U_eff`, so the stated mechanism is not the one being measured at
the quoted precision. The note already labels it `DIAGNOSTIC` and says the mechanism is not proved
— fair — but the "`+ c`, `c ≈ 1.9`" should read "`c ∈ [1.5, 2.5]` from two lattices".

## §3 LP values, pad, and the `B₂` defect

All §3 table entries reproduce from the JSONs (values, `B₂`, pad, argmin, `D_K+D_cosh`, `τ_stop`,
`L_w(TAUMAX)`, prime side). The `B₂` used in `pad = B₂δ²/8` is `d2_bound`, built from `Zenvelope`,
i.e. **from the 1000-zero model, not from `f_prime`** — the same defect `R155_017` found in
`amend.py`. **Flagged, and it does not matter here:** the conclusion is `min f < 0`, and a grid
minimum is already an *upper* bound for `min_ℝ f`; the pad only ever helps a *positivity* claim.
The "certified" column is therefore gratuitously pessimistic and should be relabelled
*grid value* + *(non-rigorous) pad*. The sign verdict (all four windows negative by `1.2·10⁻²…
8.9·10⁻²`, confirmed on the prime side) **stands, and stands without `B₂`**.

## §4 The "all of `ℝ`" statement, with tolerances folded in

(a) **`E_at = 0` is not exact.** The equalities are eliminated through an SVD null space with
tolerance `10⁻⁹·σ_max`, so the returned `w` satisfies the comb only to rounding. Measured on the
returned `x`: `max_n |w(log n)| = 5.4·10⁻¹⁶…1.0·10⁻¹⁵`, hence
**`E_at(w) ≤ 2.0·10⁻¹⁴`** at every row (against the counterfactual `Σ v_n = 71.0…72.9`).
`E_at` enters `L_w` additively, so `τ_stop` scales by `e^{E_at}`: the correction is
`≤ 2·10⁻¹⁴·τ_stop < 4·10⁻¹²` in `τ`, and `L_w(200)` drops by `≤ 2·10⁻¹⁴`. **The exponential
sensitivity is real but the residual is 15 orders below where it would bite.** Corrected wording:
*`E_at(w) ≤ 2·10⁻¹⁴` (double precision), whence `τ_stop` as tabulated `+ O(10⁻¹¹)`.*
(b) `L_w(TAUMAX) = +1.498, +0.270, +0.467, +0.258 > 0` and `τ_stop < TAUMAX` at all four rows:
**confirmed from the JSONs.** The note's disclosure of the invalid `c_log3h_U6_M48_b` row
(`τ_stop = 135.6 > 115`, `L_w(115) = −0.961`) is accurate and honest.
(c) grid minimum on `[0,200]` negative by `≥ 1.2·10⁻²`, prime side agreeing: **confirmed.**

**The one real caveat:** `D(w)` is a `du = 2·10⁻⁵` trapezoid of `∫|W''|`, not an enclosure, and
`L_w(200)` carries the term `D/200² ≈ 0.91`. At `0.58` and `log 2` the margin is `L_w = +0.26–0.27`,
i.e. the all-`ℝ` closure survives only a **`≈ 29 %` underestimate of `D`**. Plausible (the
integrand is piecewise smooth, the grid fine) but *unproved*. Honest form of the headline:

> For these four explicit weights, `E_at(w) ≤ 2·10⁻¹⁴` and — if the quadrature for `D(w)` is
> accurate to better than `29 %` — Theorem D gives `f_w > 0` on `[200,∞)`, while `f_w < −10⁻²`
> somewhere in `[0,200]` on both sides of the explicit formula. Subject to that one quadrature,
> the failure is a statement about all of `ℝ`.

This is still the **first** such statement in the track; the claim is upheld, not withdrawn.

## §5 Zero/prime agreement (`1.3·10⁻⁵…6.3·10⁻⁵`)

Checked by truncation refinement at `½log3`, argmin `5.755`: zero side gives `−1.16901e−2` (800
zeros), `−1.16550e−2` (900), `−1.16567e−2` (1000). Increments `3.5·10⁻⁵` then `1.7·10⁻⁶`:
the `1000`-zero truncation error is of exactly the observed order, and the residual `4.6·10⁻⁵` gap
is therefore truncation plus prime-side quadrature, not a modelling error. **Consistent; and
`10⁻⁵ ≪ 10⁻²`, so irrelevant to the verdict.** The note's attribution ("which is the 1000-zero
truncation error") is defensible but is an attribution, not a measurement — say "of the order of".

## §6 Diagnosis (§4 of the note)

Ratios `2.68×` (`M=24`) → `1.36×` (`M=48`) and the `3.0×` interval cost reproduce from the JSONs.
Argmins: `5.76, 7.41, 3.68, 4.42` at `M=48` — "binding minimum at `τ ≈ 4–8`" **correct for the four
windows**; across the `M=24` runs the argmins are `5.50, 9.77, 8.55, 1.66`, so "`τ ≈ 2–10`" is the
defensible range. **One omission that changes the reading:** the no-comb control's binding minimum
is at `τ = 42.9`, not at small `τ`. So it is the *comb* that moves the failure down to `τ ≈ 4–8`;
§4(3)'s "neither is the real obstruction, both fail at `τ ≈ 4–8`" is not what the data say.
The `γ₁ = 14.13` observation the prompt asks about **does not occur in the note** (grep: no hit in
`R155_016` or `scripts/reverse/comb/`); nothing to audit, and it should not be added — with argmins
at `3.7–7.4` the statement "below the first zero" would be true but vacuous: `f_w` there is not
"built only from tails", the flat top itself contributes `∫(1−w)K` and the `2∫w cosh` term at all
`τ`, and no decomposition in the note isolates a negative term.

## §7 Corpus paragraph, labels, compute

§1's distinction (prime-free window = *support shrinking* below `log 2`, comb-vanishing =
*support shaping* at fixed large window, applied to the complement of the flat top) is **fair and
correct**; `prime-free window` occurs where claimed (phases 114/115/118/138/153), and `R154_013`'s
record that the Yoshida 1992 volume is absent from `00-references` is confirmed (no Yoshida file
there) — the Yoshida row is properly hedged. `w(log n)=0` occurring only in `R155_013`: confirmed.
Labels in §5 of the note are correct as written, with the two amendments above (`E_at = 0` →
`≤ 2·10⁻¹⁴`; `D`, hence `τ_stop`/`L_w`, `DIAGNOSTIC` with the `29 %` margin stated).
Compute is declared (`README.md`, per-run timings, `≈ 6.5` min, one process); `count.py` rerun
matches. **No sign is claimed anywhere; no endpoint is touched.**

---

## §8 What survives as a lemma vs what is a diagnostic

| statement | status after audit |
|---|---|
| The three edge coefficients `x_{−1}=x_0=x_1=1` are the unique `C²` matching, and the free splines `j≥2` do not disturb it | **LEMMA** (`PROVED`; write the `β(±2)=β'(±2)=β''(±2)=0` step) |
| `WinC` weights satisfy Theorem D case (a) | **LEMMA** (`PROVED`) |
| **Comb-vanishing ⟹ bounded effective support**: for fixed `(T,h)`, `null(U)` is nested in `U`, so once `dim` stabilises the space is *identical* — no weight beyond `U_eff` exists | **LEMMA, provable** (currently a rank computation in double precision; a proof needs "≥3 consecutive interior zeros of a cubic spline in one cell force the local coefficients", which is elementary) |
| `U_eff = log(1/h) + c`, `c ≈ 1.9` | `DIAGNOSTIC` (two-lattice fit; the `u_first_tight` mechanism does not match at this precision) |
| `E_at(w) = 0` | amend to `E_at(w) ≤ 2·10⁻¹⁴`; conclusion unaffected (`τ_stop` `+O(10⁻¹¹)`) |
| all LP / certified values, `D`, `τ_stop`, `L_w(200)`, prime side | `DIAGNOSTIC`; the negative verdict needs neither `B₂` nor the pad and is **robust** |
| "first flat-top run whose failure is a statement about all of `ℝ`" | **UPHELD**, conditional on the `D(w)` quadrature to `29 %` |
| a certificate on `ℝ`, an endpoint, a sign | none obtained, none claimed — correct |

**Required edits to `R155_016`:** (1) `E_at = 0` → `≤ 2·10⁻¹⁴` in §3 notes and §5; (2) state the
`D`-quadrature margin (`29 %`) beside the all-`ℝ` headline; (3) rename the "certified" column and
note that negativity needs no pad; (4) add the nesting argument to (F1) and weaken `c ≈ 1.9`;
(5) fix §4(3): the no-comb control fails at `τ = 42.9`, so the small-`τ` failure is comb-induced.

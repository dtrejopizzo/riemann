# R155.006 — Audit of R155.005 (reverse-engineering `w_T` from the zeros)

*Phase 155. Target: `R155_005_REVERSE_ENGINEERING_FROM_ZEROS.md`
and `scripts/reverse/`. Context read: Paper 47 §7 (Def. 7.1, Thm. Z, Thm. Zexh, Cor. RH, Cor. zeros,
Rem. RHcert), §5/§6 (grid-inflation warning, two-prime windows), `R155_000`.*
**Global verdict: ACCEPT WITH REPAIRS.** The identity check and the qualitative negative reading
survive. Three of the quantitative conclusions (§0.3, §0.4/§5, §2.2) are wrong or mis-diagnosed;
every reproduction is below. All numbers here are `DIAGNOSTIC`.

## 0. What I ran (all cheap; nothing heavy)

| run | wall time | result |
|---|---|---|
| `python3 t_sanity.py` | 7.4 s | `max|diff| = 2.401017609558742e-08` (reproduces §3.0) |
| fine-grid probe of `win_log3h` `L=20` near `τ=13.25`, step `0.005`, `Γ=6000` | 12 s | see §4 below |
| prime-side quadrature-order probe (GL `200/800/2000`, `NIK 40/120`) at `½log3`, `L∈{20,2000}` | 60 s | see §3 below |
| fine-grid (`0.005`) minima of both sides, `L=2000`, GL 800 | 70 s | see §3 |
| in-regime affine extrapolation (train `058,062,065` → test `log2`) | 90 s | see §6 |
| corpus greps (`circular as tool`, `W5`, `phase-136 ES-2`) | — | see §10 |

## 1. Theorem Z verified numerically — **ACCEPT (with two label errors)**

* Reproduced: `t_sanity.py` runs in 7.4 s and prints `max|diff| = 2.4010e-08`, `mean −5.6e-11`,
 `std 5.8e-9`, exactly the §3.0 figure.
* **Normalisation audited and correct.** The paper's form of IK Thm. 5.12,
 `Σ_ρ ĥ(γ_ρ) = 2∫h cosh(u/2) − Σ_n v_n h(log n) + (1/2π)∫ m ĥ`, is the standard one: the polar pair
 `ĥ(±i/2) = ∫h e^{∓u/2}` sums to `2∫h cosh(u/2)`; the prime side `−Σ_n Λ(n)n^{−1/2}(h(±log n))` is
 `−Σ v_n h(log n)` for even `h` with `v_n = 2Λ(n)/√n`. The code uses `ŵ(t) = ∫w e^{itu}du`
 throughout (`what_box = 2 sin(2Tt)/t = ∫_{−2T}^{2T}e^{itu}du`; `what_psi = 2Re[e^{2iTt}Φ_s(s−it)]`
 with `Φ_s(z)=1/z+s/z²+s²/z³ = ∫_0^∞ψ_s e^{−zv}dv`, checked term by term; `what_bspline =
 2h cos(u_j t) sinc⁴(th/2)`, the cardinal cubic B-spline `∫β = 1` in `z`, `= h` in `u`) — no stray
 `1/2π`. `zero_side` loops over `d = τ−γ` **and** `d = τ+γ` with `γ` running over the positive
 ordinates, i.e. each zero counted once with `±γ`, as `Σ_ρ` requires. The `K`-expansion
 `2Σ_{i≥0}e^{−(2i+½)u} = ½/sinh(u/2)+½/cosh(u/2)` is verified algebraically. **No normalisation
 error found.** The 2.4e-8 agreement of two independently coded sides is strong evidence.
* **ERROR (label).** The `t_sanity` weight `w = 2e^{−2v} − e^{−4v}` is **C¹, not C²**
 (`w''(0⁺) = 8−16 = −8 ≠ 0`); the script's own comment says "a smooth C^1 flat-top". §0.1, §3.0 and
 the §6.2 table all call it "a hand-made C² weight". Fix the word in three places.
* **ERROR (unreproducible number).** §0.1 quotes `1.4·10⁻⁸`; §3.0 quotes `2.4·10⁻⁸` (10⁵ zeros) and
 `1.4·10⁻⁸` (5 598 zeros). The archived `t_sanity.py` computes only the 10⁵-zero pass; the
 `1.4·10⁻⁸` figure is not produced by any archived script. Either add the `Γ=6000` pass or drop it.
* **Scope gap (repairable, and it is the content of proposed item (i)).** Theorem Z(ii) is stated for
 `w ∈ W^reg = C_c^∞`. The spline weights are `C²_c`, not `C^∞`. The identity (i) holds for all
 `w ∈ W_cl`, and (ii) extends verbatim to `W_cl ∩ C^k_c`, `k ≥ 0`, since `ŵ = O(|t|^{−k−2})` with
 `k ≥ 0` already gives absolute convergence against `dN(t) ≍ log t dt`. State it.

## 2. Smoothness lemma — **ACCEPT AS A LEMMA, after two corrections**

* **Exponent bookkeeping is correct but stated with a gap.** For `w` with `w^{(k)}` continuous and
 `w^{(k+1)}` of bounded variation, `ŵ(t) = O(|t|^{−k−2})`: jump (`k = −1`) `O(t⁻¹)`; kink, i.e.
 continuous with a corner (`k = 0`) `O(t⁻²`); `C¹` (`k = 1`) `O(t⁻³)` — **this row is missing from
 §6.2**; `C²` (`k = 2`) `O(t⁻⁴)`. The spline class is `C²` and **not** `C³` (the third derivative
 jumps at the edge and at every knot), so `O(t⁻⁴)` is exactly right, not conservative.
* **Residual.** `Σ_{|γ|>Γ}|ŵ(τ−γ)| ≪ C_w ∫_Γ^∞ t^{−k−2}log t\,dt ≍ C_w Γ^{−k−1}log Γ` is correct
 **for `k ≥ 0` only**. For a jump (`k = −1`) the sum is not absolutely convergent and `Γ^{−1}logΓ`
 is an oscillation-dependent (conditional) statement; §6.2's table must say so, and §2.1 already
 half-says it ("converges only conditionally"). Fix the table row.
* **Off-line factor `e^{U/2}`: correct.** `ŵ` is entire of exponential type `U = sup supp w`, so
 `|ŵ(t+iy)| ≤ e^{|y|U}‖w‖_1` and `|Im γ_ρ| ≤ ½` gives the factor `e^{U/2} = e^7` for `U = 14`. Note
 the correct phrasing is an *upper bound* on the off-line contribution, not "contributes up to …
 times an on-line one" (which suggests a two-sided comparison that is not proved).
* **Numbers.** The measured `3.70e−9` (tame weight, `Γ: 6000 → 74921`) matches their own a priori
 estimate `6e−8·‖x‖₁` at `‖x‖₁ = 16.2` to a factor 3 — fine. §2.1 line 100 quotes `1.4·10⁻⁷` as
 "the measured residual", which is in fact the **`L=2000` wild weight's** residual, not the C²
 generic one (`3.7e−9`); misleading cross-reference, repair.
* **Verdict: this is the one thing here worth promoting to a lemma in Paper 47** (see §11(a)).

## 3. "The `+1.39e−6` is refuted by the prime side (`min f^prime = −8.69e−5`)" — **REJECT: the diagnosis is wrong, the conclusion is right for a different reason**

The task question was: is the `9.5·10⁻⁵` zero-vs-prime disagreement the far-zero residual, or a
grid/bug issue? Answer: **neither — it is a quadrature error on the prime side**, and `R155_005`'s
stated explanation ("the weight is so large that double precision no longer resolves `f_w`") is
false. Measured, at `½log3`, `τ`-grid `0.25`, all `10⁵` zeros:

```
max|f_zero − f_prime| by Gauss–Legendre order of the B-spline Γ/K integrals:
 L=20 : GL 200 -> 2.96e-07 GL 800 -> 6.28e-09 GL 2000 -> 5.48e-09
 L=2000 : GL 200 -> 7.35e-05 GL 800 -> 3.01e-07 GL 2000 -> 1.65e-07
zero side, chunk 96 vs chunk 13 (roundoff probe): 1.86e-12 <- zero side is stable
far-zero residual (archived xc json), L=2000: 1.38e-07 <- 3 orders too small
```

So: (a) it is **not** the far-zero residual (`1.4e−7 ≪ 9.5e−5`); (b) it is **not** double precision
(the zero side reproduces itself to `2e−12`, and raising only the quadrature order removes 99.6 % of
the gap); (c) it is the 200-node GL on the B-spline `cosh(u/2)cos(τu)` integrals, whose integrand
carries `cosh(7) ≈ 548` and is multiplied by coefficients up to `|x|_∞ = 482`. **`min f^prime =
−8.689e−5 at τ = 3.30` is therefore itself a quadrature artefact.** Recomputed at GL 800 on the same
`0.05` grid, `min f^prime = +8.92e−7 > 0`: the prime side does **not** refute the `+1.39e−6`.

What does refute it is the `τ`-grid, decisively. Fine grid `0.005`, `Γ = 6000`, both sides agreeing
to `5.2e−7`:

```
L=2000 : LP value +1.3922e-06 fine-grid min on [0,16] = -3.9534e-03 (tau=15.93)
 fine-grid min on [0,taumax=16.7456] = -1.7216 (tau=16.745)
 f(16.74) = +1.39e-06 (a grid point, active) -> f(16.745) = -1.72
L=20 : LP value -1.6756e-04 fine-grid min on [0,16] = -3.3174e-04 (tau=13.25)
 fine-grid min on [0,taumax] = -9.7878e-03 (tau=16.745)
```

The conclusion of §0.3/§3.1(2) ("the positive value is fictitious") **stands, and is stronger than
stated**: the honest value of the `L=2000` weight is `≤ −3.95·10⁻³` in the interior and `−1.72` at
the right end of the very interval the LP was solved on, i.e. worse by `10³–10⁶`, not by `10⁻⁴`.
Repairs required: rewrite §3.1(2) and the §0.3 sentence; raise the GL order in `revlib2.py`
(`n=200 → 800` costs nothing) and re-issue `xc_*.json`; delete "min `f^prime` = −8.69e−5" everywhere.

## 4. "Grid value `−1.676e−4` is worth `−3.317e−4` at `τ = 13.25` off-grid" — **ACCEPT, reproduced exactly**

```
f(13.24) = -1.675576841e-04 (LP grid point, active constraint, = c)
f(13.25) = -3.317439093e-04 (off-grid minimum)
f(13.26) = -1.675576841e-04 (LP grid point, active constraint, = c)
min over the LP grid, recomputed: -1.6755768414e-04 at tau = 5.82 (= the LP value)
```

This is textbook grid exploitation: the optimiser puts a spike **between two adjacent grid points**,
both of which it holds exactly at `c`. It is admissible for a band-limited `f` of type `U = 14`
(Bernstein allows `½U²‖f‖_∞δ²` of dip over `δ = 0.01`), so it is not a bug — it is the §5 warning of
Paper 47 realised at the finest grid the phase has used. Note the factor is **not** `2.0` once the
endpoint is included (`−9.79e−3` at `τ = 16.745`, a factor `58`).

## 5. The `c(T)` table and the LP — **ACCEPT the LP, REJECT "`c(T)`" as a class quantity**

* **The LP is correctly posed.** Verified line by line in `lp2.py`: the constraint rows encode
 `B_z + A^T z ≥ c` (sign convention correct), the budget row `Σ(z⁺+z⁻) ≤ L`, the edge row
 `Σ_i y_i = 1`; `c` free, all others `≥ 0`. Flat top: automatic (box + `ψ_s(0)=1, ψ'=ψ''=0`;
 B-splines start at `j = 2`, support `[2T, …]`, `β(±2)=β'(±2)=β''(±2)=0`). Decay: `s ∈ {2.5,4,8,16}`
 and compact splines, so `s > ½` with room, `ν_w` finite (Def. 7.1) — correct.
* **But `L` is not a norm on `w`.** `L = Σ|y| + Σ|x|` mixes `ψ`'s (`‖ψ_s‖_1 ≈ 3/s ≈ 1.2`) with
 splines (`∫|β| = h = 2T/M`), so `L` is a *basis- and `M`-dependent* coefficient budget, not a mass.
 Consequence: comparing `c(T)` "at `L = 100`" across windows compares different admissible sets
 (`h` runs `0.137 → 0.200`), and comparing `L` to Paper 47 §5's `‖ν‖_TV = 90.75` (§4.3) is
 apples-to-oranges. §4.3's "the analogy is close" is not supported; downgrade to a remark.
* **`M` is not converged, and `R155_005`'s own data show it.** At `T = 0.58`, `M = 8 → 16` moves
 `c(L=100)` from `−2.351e−2` to `−5.475e−3`, a factor `4.3`. Any statement of the form "`c(T)` is
 `−2.35e−2` at `0.58`" is a statement about `M = 8`, not about the window.
* **Every entry is an over-estimate by an *unbounded* factor, not ~2** (§3–§4 above). At `L ≥ 400`
 the LP value is pure grid exploitation and the corresponding "weights" certify nothing.
* **Is "no law in T" an artefact of `U ≈ 14` and `M`?** Partly. `v_last ≈ 12.2–12.6` in every run
 proves the range cap binds everywhere, and the `M = 16` row proves the resolution binds at `0.58`.
 What is **not** an artefact is that `τ_env = 2πe^{A_T}` jumps `16.75 → 59.54 → 119.09` at prime
 entries: the *domain* of the optimisation changes discontinuously, independently of `M`, `U`, grid
 and precision. So the qualitative statement "the problem changes kind at a prime entry" survives;
 the quantitative statement "four orders of magnitude" does not (it is `M`- and grid-bound).

## 6. Extrapolation — **REJECT the conclusion as stated: the affine test as run is a straw man**

`extrapolate.py` fits `w(v;T) = a(v)+b(v)T` on `{½log3, 0.58, 0.62, 0.65}`. `½log3` has `N_T = {2}`
and the others `N_T = {2,3}`: the training set straddles a prime entry, which `R155_005`
identifies as the reason for failure — and then keeps the unconditional conclusion "There is no law
for `w_T` in `T` in this class" (§0.4, §5 last line, §6.2 row). I ran the fair test he did not:
**train inside one regime, `{0.58, 0.62, 0.65}` (all `N_T = {2,3}`), test at `log 2` (same regime,
since `4` enters only at `T > ½log4 = log2`), `L = 20`, everything else identical:**

```
in-regime affine fit residual sup_v : [0.00563, 0.01314, 0.00751] (memo's: 0.424, 0.569, 0.104, 0.242)
sup_v |w_pred - w_true(log2)| : 0.0412 (profile sup norm ~1.3)
predicted-w min f^known at log2 : -0.2562 LP optimum: -0.03608 (7x worse; memo's: 61x)
```

So: **inside one prime regime the affine law in `T` fits the profiles to `1.3·10⁻²` and predicts the
next window's profile to `4 %`.** A law *does* exist there. What fails is the transfer of the
*value*: a 4 % perturbation of `w` still costs an order of magnitude in `inf f`. That is a
**conditioning** statement about the value functional (and good evidence for the §6.3(ii) intuition),
not a non-existence-of-law statement. §0.4, §5 and the §6.2 row must be rewritten to:
"the profile is affine in `T` within a prime regime to `1.3e−2`; the value functional is so
ill-conditioned that a 4 % profile error costs a factor 7 in `inf f`; across a prime entry even the
profile law breaks (residual `0.57`)". The negative conclusion **for extrapolating the value** is
robust; the conclusion "no law for `w_T`" is false as written.

## 7. Difficulty index — **ACCEPT (arithmetic), REJECT the gloss**

Checked: `A_T = Σ_{n<e^{2T}}v_n` gives `0.98026` (`n=2`), `2.24883` (`n=2,3`; matches Paper 47 §6.1
`A = 2.24883`), `2.94199` (`n=2,3,4`); `τ_env = 2πe^{A_T} = 16.7456, 59.536, 119.09` ✓;
`2πe^{2T} = 18.850, 20.041, 21.706, 23.053, 25.133, 28.161, 31.116` ✓; ratios
`0.888, 2.971, 2.743, 2.583, 2.369, 4.229, 3.827` ✓ — §0.5, §4.2 and §6.2 ("`0.89`", "`2.4–4.2`") are
arithmetically right, and the prime-power bookkeeping (`4 ∈ N_T` for `T > log 2`) is right.
The **gloss** is not: "`½log3` … the only window that works … the zeros alone bring `c` to within
`10⁻⁶` of zero" rests on `c(½log3) = −5.4e−7`, which §3–§4 show is a grid artefact (honest values
`−3.3e−4` at `L=20`, `−3.95e−3` at `L=2000`). Worse, both are **below the certified
`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`** of Paper 47 Thm. C: the reverse-engineered class is *worse* than
the certificate the corpus already owns at that window. Keep the ratio as a bookkeeping index; drop
"works".

## 8. Negative control (exponential columns) — **REJECT as archived: not reproducible, and confounded**

* **The archived run does not match the text.** §2.2 reports `c = −1.16e−2, −4.9e−3, −1.10e−3,
 −7.8e−4, −1.6e−4` for `Σ|x| ≤ 20,100,400,2000,20000` with `s_min = 0.55`, `K = 48…80`. The archived
 `run_lp.py` has `LBOUND = 20.0` (single `L`) and `R.basis(48) = ` log-spaced `s ∈ [1.5, 60]`, and
 `lp_results.json` records `s_min = 1.5`, `L = 20` only, with
 `c(½log3) = −6.353e−2` (free), `−6.434e−2` (`C⁰`), `−1.512e−1` (`C¹`). **None of the §2.2 numbers
 is in the archive.** Either archive the run that produced them or delete them.
* **Class mismatch with Theorem E.** Thm. E's class is `w = Σx_k e^{−s_k(|u|−2T)}` with `s_k > ½`;
 the archived control uses `s ≥ 1.5`, which cannot produce the long tails (`v_last ≈ 12`) the spline
 class demands (`e^{−1.5·12} = 1.5e−8`). The control therefore tests a strictly smaller class than
 Thm. E's, and its failure is partly a consequence of that truncation.
* **The `free` variant is not admissible for this experiment at all**: it leaves a jump at `2T`
 (`Σx = 1.24, −0.56, 0.334, 0.888, 0.527, 1.598, 0.62`), so `ŵ = O(t⁻¹)`, the zero sum is only
 conditionally convergent, and `f^known` truncated at `Γ` is not a controlled approximation — by the
 `R155_005`'s own §3.2 the truncation error is `~10⁻³`, i.e. larger than several of the reported `c`.
 Only the `C⁰`/`C¹` variants are meaningful, and they are the worse ones.
* **The structural argument in §2.2** ("every exponential column carries the same edge phase
 `e^{2iTt}`, so the class can only reshape the envelope, never the oscillation") is **wrong as
 stated**: the spline columns also carry a common phase factor, and what distinguishes them is
 `cos(u_j t)`, i.e. the *position* `u_j`. The honest statement is the second half: exponential
 columns are monotone and cannot localise mass at a chosen `u`, hence the effective dictionary is
 1-parameter in shape and the LP has no oscillation to trade. Rewrite.
* Not a bug — but not evidence about `λ^W` either, as `R155_005` correctly notes.

## 9. Circularity / labelling — **ACCEPT**

`DIAGNOSTIC` appears in the header (lines 9–10), the README, §6.1 (three independent reasons, all
correct), and every row of the §6.2 table. No sign is claimed for any `T > log 2`; the endpoint of
record is restated correctly (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`, Thm. C). The zero table is used only
as training data and never as a hypothesis. §3.2's observation that bounding the far-zero remainder
requires excluding off-line zeros above `Γ` — which is the conclusion — is correct and is the right
place to put the no-go. The cited no-goes exist and say what is claimed: `phase-4-handoff/proofs/
00-PROOF-LOG.md:168` ("Zero-side `K` presupposes the unknown zeros (circular as tool)", `✅ proved`)
and `phase-136-row-d-map/MAP_1_WALLS_AND_MASTER_DOCS.md:141` (ES-2). *Path nit*: the deliverable
writes `phase-4/00-PROOF-LOG:168`; the file is at `phase-4-handoff/proofs/`.
One residual risk to police: §0.5 and §6.2 contain quasi-positive readings ("the zeros alone bring
`c` to within `10⁻⁶` of zero") that a reader could mistake for a near-certificate. With §3–§4 those
readings are void; they must go.

## 10. Corpus check — **ACCEPT**

`phase-118` W5 is what the deliverable says it is: `W5_identity_check.py` line 1, *"Part A.1-A.2:
verify `<A_T F,F> = sum_rho h(gamma_rho)` numerically against …"*, i.e. the **primal** identity, with
`W5_cache_zeros.py` caching `mpmath.zetazero`; it is not `(7.2)`/Theorem Z and not an optimisation
over `w`. No other numerical verification of the explicit formula on flat-top tests exists in
`03-research`. So the claim "first numerical verification of Theorem Z in the corpus" is correct —
but it verifies a `PROVED` statement, so its value is as a regression test, which is how §6.2 labels
it. Correct.

## 11. Disposition

**(a) Worth adding to Paper 47 (one lemma, plus one corollary `R155_005` did not propose).**
1. *Smoothness/far-zero lemma, refining Cor. 7.4.* Let `w ∈ W_cl`, supported in `|u| ≤ U`, with
 `w^{(k)}` continuous and `w^{(k+1)}` of bounded variation (`k ≥ 0`). Then
 `|ŵ(t)| ≤ V(w^{(k+1)})|t|^{−k−2}`, Theorem Z(ii) holds for `w` (absolute convergence), and, under
 RH below `Γ`, `Σ_{|γ|>Γ}|ŵ(τ−γ)| ≤ C·V(w^{(k+1)})Γ^{−k−1}log Γ`; without RH below `Γ` the same sum
 is bounded only after the factor `e^{U/2}` of Cor. `zeros`, which is exactly why the criterion
 cannot be checked from a finite table. Elementary (two integrations by parts + Stieltjes against
 `N(t) = (t/2π)log(t/2πe)+O(log t)`), and it extends Thm. Z(ii) from `C_c^∞` to `C_c^k`, `k ≥ 0`.
 State the jump case (`k = −1`) separately as conditionally convergent.
2. *Grid lemma (new, and the phase needs it more than (1)).* `f_w` is band-limited of exponential
 type `U`; Bernstein gives `min_R f_w ≥ min_{δ-grid} f_w − ½U²‖f_w‖_∞δ²` (and a Markov-type
 refinement near a grid minimum). This turns Paper 47 §5's grid-inflation *warning* into a
 theorem, gives the LP an a posteriori certificate, and is exactly what the `τ = 13.25` and
 `τ = 16.745` failures above measure. Cheap and unconditional.

**(b) Diagnostic, keep as recorded (after the repairs above).** The shape of `w_T` (monotone shoulder
`≈ e^{−1.2v}`, no `log p` spacing) at small `L`; the tension "long support vs smooth transform";
`τ_env/2πe^{2T}` as a bookkeeping index; the contact comb at `2π/U` (a class statement, correctly
labelled); the tail-mass constancy `∫_{2T}^∞ w ≈ 5.0` at `L ≥ 100` — but note it is measured at
values of `L` where the optimiser is already exploiting the grid, so it may be a property of the
grid artefact, not of the problem; re-measure at `L = 20` with a `0.002` grid before calling it an
invariant. The regime-structure of `c(T)` (domain jumps at prime entries) qualitatively.

**(c) Wrong, delete or rewrite.** (i) "`min f^prime = −8.69e−5` refutes the positive value" — a
quadrature artefact (§3). (ii) "double precision no longer resolves `f_w`" — false (§3). (iii) "the
grid value is optimistic by a factor of order 2" — unbounded, measured `58×` and `10⁶×` (§3–§4).
(iv) "There is no law for `w_T` in `T` in this class" — false inside a prime regime (§6). (v) The
§2.2 exponential-column numbers — not in the archive (§8); and their "same edge phase" explanation.
(vi) "hand-made C² weight" — it is C¹ (§1). (vii) §4.3's `L ↔ ‖ν‖_TV = 90.75` comparison (§5).
(viii) "`½log3` … works / `c` within `10⁻⁶` of zero" (§7).

## 12. The two proposed next steps

**(i) Far-zero lemma — DO IT.** Elementary, unconditional, and it repairs a real gap in Paper 47 §7
(Thm. Z(ii) is stated only for `C_c^∞`). Half a page. Pair it with the Bernstein grid lemma above,
which is the more valuable of the two and costs the same.

**(ii) Weight-side Theorem O, `sup{inf f_w : ‖w‖_∞ ≤ A} < λ^W` for every `A` — plausible but
unproved, and it is *not* a lower-bound-side result for Problem A.** Two points.
*Plausibility.* The evidence is genuine but weaker than claimed: the exhausting family of Thm. Zexh
is built by replacing atoms of mass `a_j` with densities on shrinking intervals, whose height — hence
`‖w_h‖_∞` — blows up as `ε → 0`; so the known route to `λ^W` does leave every `‖w‖_∞ ≤ A` ball. The
obstruction to a proof is that `{w ∈ W_cl : ‖w‖_∞ ≤ A}` is **not** compact in any topology making
`w ↦ inf f_w` upper semicontinuous: `ν_w` contains `2w cosh(u/2)1_{|u|≥2T}`, and mass escaping to
large `u` is weighted by `cosh(u/2) → ∞`, which is precisely the escape mechanism of Thm. O. So a
compactness argument "in `W_T ∩ {‖w‖_∞ ≤ A}` against Theorem O" as §6.3 proposes will **not** close
as written; one needs a joint constraint `‖w‖_∞ ≤ A` *and* a decay modulus `|w| ≤ Ce^{−(½+δ)|u|}`
with `C, δ` fixed — and with such a modulus the class *is* compact and the statement becomes a
routine (and much weaker) corollary of Thm. O. Whether the `L^∞` bound alone suffices is genuinely
open; my prior is against, because `w ↑ 1` with `‖w‖_∞ = 1` is the very family of Rem. RHcert whose
formal limit is `2πΣ_ρδ_{γ_ρ}`. Also note §2.4 is *not* clean evidence for (ii): the `‖w‖_∞: 1 → 262`
degeneration is driven by the LP exploiting the `0.02` grid (§4), which rewards large coefficients
for free; re-measure on a Bernstein-certified grid before citing it.
*Species.* Even if proved, (ii) is a **class-dependent upper bound** — an obstruction of the same
species as Theorem TK (`R155_003`) and Lemma V′ — saying a restricted class cannot reach `λ^W`.
Problem A asks for a **lower** bound `c(T,d,U) ≥ λ^prim_T − D(T,d,U)` with explicit `D`. §6.3's
"it would be the first *lower* bound this phase has produced" is **wrong**: it is another negative.
This phase still has zero lower-bound-side results, and (ii) would not change that.

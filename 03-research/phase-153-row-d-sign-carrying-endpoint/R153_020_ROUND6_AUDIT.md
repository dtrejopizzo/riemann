# R153.020 — Round 6,  audit: the body `W_T`, the bands, and what "at the edge" means

* Target: `R153_019_ROUND6_BODY.md` against `R153_018` (review).
Everything below was recomputed from `scripts/round6/` (reruns of `t2_axis_lemma.py`, `t3_joint.py`,
`t4_log5.py`, `t3_band.py`, `prec.py`, plus four independent scripts of my own) and from
`scripts/audit/aud_spectral.py`. Reference: `R153_014`, `R153_017`, `R147_003` §A.6, `R147_005`,
Paper 42 `main.tex` 4072–4230.*

---

## 0. Verdict table

| # | claim | verdict |
|---|---|---|
| 1a | Lemma 3.1, `sup c_F(a) = −inf = cos(π/(⌈2T/a⌉+1))`, Jacobi-chain proof | **SUSTAINED, `PROVED`.** Proof correct; reproduced to 10 digits at 9 `(T,a)`; both ends stated; `m` convention correct at `2T/a ∈ Z` and at `a = 2T` |
| 1b | "different object from `R147_003` Lemma A.6, not a re-use" | **SUSTAINED.** A.6 is a min–max of `|cos|` over a `μ_m`-orbit with an even/odd split (`cos(π/2m)` for odd `m`); Lemma 3.1 has no odd branch and is a spectral edge. Coincidence of closed form only |
| 1c | novelty claim | **MINOR.** The values `0.5, 0.7071, 0.8090, 0.8660` of §3's table are numerically the row "round 1's claimed `\cos(π/m)`" that `R147_002` MAJOR 6 refuted. Harmless, but must be said, or a reader will think A.6 was re-derived |
| 2a | box bound `−1.277629`, truth `+1.03·10⁻⁷`, three pairwise relaxations | **SUSTAINED numerically** (my reruns agree to all printed digits) |
| 2b | "100% of the positivity is coupling" | **REPAIR (framing).** Tautological: the truth is `10⁻⁷`, so *any* non-zero deficit gives 100.0%. Delete the percentage; the content is "the projection-only box is short by `1.28`, an `O(1)` amount" |
| 2c | "≥ 56% irreducibly three-way" | **DOWNGRADE.** `DIAGNOSTIC-NUMERIC`, not theorem-level, and the denominator (`1.27763`) is not canonical. Reword: "the best of the three pairwise-projection relaxations still falls short by `0.7171`" |
| 3 | Krein bands; `w_3` at 96.4%, `w_2` at 99.85%; margin `= λ/(2x_n)` | **SUSTAINED numerically but NOT INFORMATIVE.** See §3: the upper margins are the Hellmann–Feynman first-order value to `0.3%` / `0.15%`. The percentages are restatements of `λ ≈ 10⁻⁷` |
| 3b | §4.2 "the band in `w_3` is wide and the band in `w_2` is narrow" | **FALSE as written.** Measured widths: `w_3` band `1.175·10⁻⁴`, `w_2` band `4.458·10⁻⁴`. The `w_2` band is **3.8× wider**. Only the *upper margins* run the other way |
| 3c | apex `v_2^* − w_2 = 8.5·10⁻⁶`, relative `1.7·10⁻⁵` | **SUSTAINED and the one genuinely new geometric number** — it is *not* the first-order quantity (see §3.3) |
| 4a | `λ_min(A_{½log5}) ≤ 3.20·10⁻¹²`, cascade, contacts `2,3,4`, `w_4 = (log2)/2` | **SUSTAINED.** `log 4 = 1.3863 < 2T = 1.6094`; `n = 5` correctly excluded (`c_F(2T) ≡ 0`); cascade = the three lowest eigenvalues of `A_{½log5}` |
| 4b | "`x_4` is numerically zero"; "the `w_4`-band is nearly flat"; "`w_4` sits essentially at the optimum of its band, not at its edge" | **FALSE. Required repair.** `x_4 = 2.80·10⁻⁵`, `K`-stable. The `v_4` band is `[0.346572948, 0.346573647]`, **width `6.99·10⁻⁷`**, and `w_4` sits at **91.8%**, i.e. `5.71·10⁻⁸` below the upper edge, against `λ/(2x_4) = 5.83·10⁻⁸`. Identical mechanism to `w_2, w_3`; no degeneracy |
| 5a | Prop 2.1 (half-space ⟺ closed convex hull) | **SUSTAINED, `PROVED`, trivial** — as the report itself says |
| 5b | Prop 2.2 proof ("the union is `W_T`") | **MINOR ERROR.** `⋃V_k` is dense, not exhausting: the argument gives convexity of `\overline{W_T}`, not of `W_T`. Restate |
| 5c | illegitimate use of convexity elsewhere | **ONE GAP.** "exposed point" (§4.2) needs attainment of the max; supply the one-line reason (`M_0` has compact resolvent, `S_n` bounded ⇒ `λ_min` is a genuine eigenvalue below the essential spectrum). With that, §4.2 is legitimate at `T = log 2` (where `d = 2` and Prop 2.2 applies) but **not** at `½log5`, where convexity is `OPEN` — §7 must not say "facet/flat" there without a hedge |
| 6 | `Ξ_a` falsifier | **SPLIT.** The *direct* computation (`aud_spectral.py`, doubled Gamma `Σ_± Re ψ(¼±a/2+iτ/2) − 2log π`, **four** moments `±½±a`) is the real test and it passes: I reproduce `−1.66880·10⁻²` (`a=0.30`), `−5.06944·10⁻²` (`a=0.45`), `+2.08756·10⁻⁷` (`a=0`). The *weight-vs-region* comparison `(2.0567, 2.8536)` vs `v_2 > 0.98028` uses the **ζ body**, a different body, and is not a falsifier test. Caveated in §8 but **leads §0** — must be demoted |
| 7a | labels, FATAL rule, "no sign beyond `log 2`" | **CLEAN.** No zeros used; Paper 42 Thm `certifiedendpoints` (`main.tex` 4165–4230) is correctly cited as the only certification, Galerkin correctly called an upper bound |
| 7b | T6 "expectation negative for a prime-free closed form", justified by non-commutativity | **OVERREACH.** `‖[S_2,S_3]‖/(‖S_2‖‖S_3‖) = 0.100` at `K = 200` — non-commutativity is real, but non-commuting pencils routinely have closed-form spectra, and `log3/log2 ∉ Q` is invoked without doing any work. Relabel as the auditor-visible opinion it is |
| 7c | corpus-check lines | **SUSTAINED**, two greps rerun (§7). One notation clash to record |

No FATAL. Nothing in round 6 claims a sign for `ζ` beyond `T ≤ log 2`.

---

## 1. Lemma 3.1 (item 1)

The proof is correct. The direct integral `L²(0,L) = ∫^⊕_{s∈(0,a)} C^{k(s)}`, `k(s) = #{j ≥ 0 : s+ja < L}`,
is the right fibration for `½(S_a+S_{-a})`, the fibre operator is `½J_{k(s)}` with `spec(J_k) = {2cos(πj/(k+1))}`,
and the spectrum is symmetric, so `sup = −inf = cos(π/(k_max+1))`. **The maximum is `cos(π/m)`, not `1`** —
the report states this correctly and gives both ends (§3, and `min` column in my rerun below).

**`m` convention at the boundary.** `k(s) = ⌈(L−s)/a⌉` for `s ∈ (0,a)`. If `L/a = M ∈ Z` then
`(L−s)/a ∈ (M−1,M)` so `k ≡ M = ⌈L/a⌉` on *full* measure; if `L/a = M+θ`, `0<θ<1`, then `k = M+1 = ⌈L/a⌉`
on `s < θa`, positive measure. **So `k_max = ⌈L/a⌉` in both cases and the convention is safe.**
Degenerate end `a = 2T`: `m = 2`, `cos(π/2) = 0`, and `shift_matrix` returns `0` — consistent.

Rerun of `t2_axis_lemma.py` (`K = 400`), max / min columns:

| `T` | `a` | `m` | `cos(π/m)` | numeric max | numeric min |
|---|---|---|---|---|---|
| `log2` | `log2` | 3 | 0.5000000000 | 0.5000000000 | −0.5000000000 |
| `log2` | `log3` | 3 | 0.5000000000 | 0.5000000000 | −0.5000000000 |
| `½log5` | `log2` | 4 | 0.7071067812 | 0.7071067812 | −0.7071067812 |
| `1.2` | `log2` | 5 | 0.8090169944 | 0.8090169944 | −0.8090169944 |
| `2.5` | `log2` | 9 | 0.9396926208 | 0.9396926208 | −0.9396926208 |

**Caveat to record:** `t2_axis_lemma.py` runs `constrained=False`. The *constrained* check is in
`t3_joint.py` (`max x_2 = 0.5000000000000332`, `min x_2 = −0.500000000000024`, ditto `x_3`, `K = 320`);
§3's "codimension 2 does not move the edge of the essential spectrum" should cite that line, not the table.

**Distinctness from `R147_003` A.6: sustained.** A.6 is `min_θ max_{k<m}|cos(θ+2πk/m)|`, equal to
`cos(π/m)` for **even** `m ≥ 4` and `cos(π/(2m))` for **odd** `m ≥ 3` (`R147_003:271–299`, `R147_005:61`).
Lemma 3.1 has no parity split and is a spectral edge of a Jacobi chain. Different object; same closed form
on one branch. **But note:** the refuted round-1 claim in `R147_002:190` was exactly "`cos(π/m)` for all `m`",
whose table (`0.5, 0.7071, 0.8090, 0.8660`) is §3's table verbatim. Add one sentence so no reader concludes
round 6 revived a refuted lemma.

## 2. The box, the relaxations, and what "coupling" means (item 2)

Exact definitions actually computed (`t3_joint.py`, `K = 320`), all reproduced by me:

* box `= min x_0 − 2w_2·max x_2 − 2w_3·max x_3 = −0.15321549 − 0.49012907 − 0.63428410 = −1.27762867`.
* `(x_0,x_2)` joint, `x_3` relaxed to its projection max: `λ_min(M_0 − 2w_2S_2) − 2w_3·½ = −0.71711167`.
* `(x_0,x_3)` joint, `x_2` relaxed: `λ_min(M_0 − 2w_3S_3) − 2w_2·½ = −0.92957342`.
* `(x_2,x_3)` joint, `x_0` relaxed to `min x_0`: `min x_0 + λ_min(−2w_2S_2−2w_3S_3) = −1.05414311`.
* truth `λ_min(A_{log2}) = +1.0307·10⁻⁷` (`K=320`).

These are the three pairwise-projection relaxations and they are exhaustive for that scheme, so
"no pairwise relaxation does better than `−0.7171`" is correct **for this scheme** — it is a numerical
observation, not a theorem (a theorem would quantify over all two-body constraints, not three specific ones).

**The tautology.** `1.27763/1.27763 = 100%` holds because the truth is `10⁻⁷`: the statement carries no
information beyond "the box bound is not zero". Likewise `0.7171/1.27763 = 56%` is a ratio to a
non-canonical denominator. What is genuinely informative, and should be the headline instead:
**projections + Gamma coercivity are short by `1.28` in the `w_ζ` direction, and the shortfall grows with `|v|`
(`1.54` at `v=(2,2)`, `2.26` at `(5,5)`) — so no projection-only argument can ever work.** That is a real
permanent negative and the report's own §9(4)(iii) says it better than §0 does.

One caveat: `min x_0` is *not* converged (`−0.1528574` at `K=240`, `−0.1532155` at `K=320`, `−0.15358` at
`K=480`, drifting down). The box bound therefore only gets *more* negative; the conclusion is safe, but
`−1.277629` must be printed as `≤ −1.2776` with the drift noted.

## 3. The Krein bands: the edge statement is a restatement (item 3)

### 3.1 Independent recomputation of the upper edges

I bisected the upper edge directly (`brentq`, `xtol = 10⁻¹⁵`) at two `K`, and separately computed
`x_n(F_min)` from the eigenvector of `A_{log2}` at the *same* `K`, so the comparison is `K`-matched:

| `K` | `λ_min` | `x_2` | `x_3` | `w_3^+ − w_3` | `λ/(2x_3)` | ratio | `w_2^+ − w_2` | `λ/(2x_2)` | ratio |
|---|---|---|---|---|---|---|---|---|---|
| 240 | `1.043780·10⁻⁷` | 0.0746430 | 0.0117696 | `4.41971·10⁻⁶` | `4.43421·10⁻⁶` | **0.9967** | `6.98104·10⁻⁷` | `6.99181·10⁻⁷` | **0.9985** |
| 480 | `1.016022·10⁻⁷` | 0.0745019 | 0.0118029 | `4.29019·10⁻⁶` | `4.30414·10⁻⁶` | **0.9968** | `6.80827·10⁻⁷` | `6.81876·10⁻⁷` | **0.9985** |

So the margins are the Hellmann–Feynman first-order value to **0.3%** and **0.15%** — tighter than the
report's "1–2%", which only looked loose because it mixed an extrapolated `λ` with a `K = 480` `x_3`.

### 3.2 Therefore "`w` sits at the edge" is not new information

`∂λ/∂v_n = −2x_n(F_min)` is exact (simple eigenvalue) and `λ` is `10⁻⁷`. Hence the upper margin in **every**
coordinate is forced to be `λ/(2x_n)` up to `0.3%`, and the percentages are
`96.4% = 1 − 4.29·10⁻⁶/1.175·10⁻⁴` and `99.85% = 1 − 6.81·10⁻⁷/4.458·10⁻⁴`: a small number `λ` divided by an
unrelated `O(10⁻⁴)` width. **Nothing beyond `λ ≈ 10⁻⁷` is being reported, and the percentage is not even
scale-invariant** — it depends on where the *lower* edge happens to sit, a quantity with no arithmetic meaning.
§5 and §0 must be rewritten to say: *the upper edges are first-order-predicted; what is measured is `x_n(F_min)`.*

**What would be non-trivial**, and is the correct target for a next round: a band edge at a distance from `w`
that is **not** `λ/(2x_n)` — i.e. a direction in which the first-order term vanishes and the curvature of
`v ↦ λ_min` decides, or a *lower* edge whose position is predicted by something arithmetic.

### 3.3 The apex is the one number that is not first-order

The normal distance from `w = (w_2,w_3)` to the boundary of the admissible region is
`λ/‖(2x_2,2x_3)‖ = 1.031·10⁻⁷/0.15086 = 6.83·10⁻⁷`. The measured apex offset is `v_2^* − w_2 = 8.5·10⁻⁶`,
**12.4× larger**, because the apex direction is nearly tangent to the boundary — so `8.5·10⁻⁶` encodes the
*curvature* of the admissible region at `w`, not `λ`. This is the only genuinely two-dimensional datum in
§5 and it should be promoted over the two percentages.

### 3.4 `w_3` "wide", `w_2` "narrow" — backwards

Rerun of `t3_band.py`: `w_3` band `[0.6341709042, 0.6342883908]`, width `1.175·10⁻⁴`;
`w_2` band `[0.4896839142, 0.4901297526]`, width `4.458·10⁻⁴`. The `w_2` band is **wider**. §4.2's closing
sentence ("the minimiser is nearly blind to the `n = 3` contact, which is exactly why the band in `w_3`
is wide and the band in `w_2` is narrow") is false about widths; it is true about *upper margins*, which is
a different statement. Repair the sentence.

`T = ½log3`: band `[0, 0.4932791]`, `w_2` at `3.15·10⁻³` below the upper edge — here `λ` is `O(10⁻²)`, not
`10⁻⁷`, so this is the one band whose margin is genuinely `O(1)` and not a `λ`-restatement. Worth saying.

## 4. `T = ½log5` (item 4)

Reproduced exactly: `λ_min = 3.3002, 3.2657, 3.2243 · 10⁻¹²` at `K = 240, 320, 480`; the "cascade"
`3.2·10⁻¹², 6.6·10⁻¹⁰, 3.2·10⁻⁷` is simply the **three lowest eigenvalues of `A_{½log5}`** (columns
`ev[0], ev[1], ev[2]` of `t4_log5.py`), correctly described. Contacts and shifts check out:
`n < e^{2T} = 5` gives `{2,3,4}`, `w_4 = Λ(4)/√4 = (log2)/2 = 0.3465736`, `log 4 = 1.38629 < 2T = 1.60944`,
so `S_4 ≠ 0`; `n = 5` would give `a = 2T` and `c_F(2T) ≡ 0`, and it is correctly excluded. Axis projections
`(±0.70711, ±0.5, ±0.5)` match Lemma 3.1 (`m = 4,3,3`). Galerkin-upper-bound caveat correct; no sign claimed.

**The `w_4` paragraph is wrong and must be replaced.** Recomputed (`K = 320`, `brentq`, `xtol = 10⁻¹⁵`):

* `x_4(F_min) = 2.80·10⁻⁵` — small but **`K`-stable to three digits**, not zero;
* argmax over `v_4` at `0.3465729847`, **`6.4·10⁻⁷` below** `w_4 = 0.3465735903` (not "at" it — the report's
  `0.346573` vs `0.3465736` is a six-digit print coincidence from a `bounds=(0,1)` bounded search);
* `v_4` band `= [0.3465729482, 0.3465736474]`, **width `6.99·10⁻⁷`** — the narrowest band in the round,
  not a flat direction;
* `w_4` sits at **91.8%** of that band, `5.71·10⁻⁸` below the upper edge, against `λ/(2x_4) = 5.83·10⁻⁸`
  (`λ = 3.2657·10⁻¹²`): **the same Hellmann–Feynman law as `w_2, w_3`**, agreement `2%`.

So the `R³ → R⁴` change is **not** "degeneracy, not a new facet". It is the same edge phenomenon with a
much smaller `x_n` and a correspondingly much smaller `λ`; the ratio `λ/(2x_4)` is what stays finite.
The claim "the Euler weight sits essentially at the optimum of its own band, not at its edge" is refuted by
the report's own numbers: `λ_max = 3.40·10⁻¹¹` vs `λ(w_4) = 3.27·10⁻¹²` is a factor `10`, which is not
"at the optimum" in any metric. And the phrase "close to a three-dimensional flat" leans on convexity of
`W_{½log5}`, which §2 declares `OPEN` — hedge it.

## 5. Convexity (item 5)

Prop 2.1 is correct and trivial, and it does dispose of the question, as the report says. Two defects:

1. **Prop 2.2's proof.** "The family is nested increasing and its union is `W_T`" is false: `⋃V_k` is a dense
   subspace, not the whole form domain, so `⋃_k x(V_k∩S)` is a dense subset of `W_T`. Since `x` is
   form-continuous, what follows is that **`\overline{W_T}` is convex**. Given Prop 2.1 this loses nothing —
   but the statement must be corrected to `\overline{W_T}`.
2. **Attainment.** §4.2's "single exposed point" presupposes the supremum is attained. It is: `M_0` has
   compact resolvent (the multiplier `Re ψ(¼+iτ/2) − log π → +∞`) and the `S_n` are bounded, so
   `M_0 − v·S` has discrete spectrum bounded below and `λ_min` is an eigenvalue. Add the line.

I found **no** place where convexity of `W_T` is used illegitimately at `T = log 2` (where `d = 2` and AYP
applies with `m = 3` real forms, `n ≥ 3` — the citation is correct). The one exposure is §7 at `½log5`
("facet structure", "three-dimensional flat") where `d = 3`, AYP fails, and convexity is `OPEN`.

## 6. The `Ξ_a` falsifier (item 6)

The direct test **uses the correct body**. `scripts/audit/aud_spectral.py` has the doubled Gamma symbol
`Σ_± Re ψ(¼ ± a/2 + iτ/2) − 2 log π`, weights `Λ(n)(n^a+n^{-a})/√n`, and the **four**-moment null space
`β ∈ {−½−a, −½+a, ½−a, ½+a}` (`lmin`, lines 68–75) — i.e. `P_T^{(a)}`, not `P_T`. I reran it (`K = 240`,
`T = log 2`): `λ_min = +2.087563·10⁻⁷` (`a=0`, `= 2λ(A_{log2})`), `−1.668799·10⁻²` (`a=0.30`),
`−5.069436·10⁻²` (`a=0.45`). **The falsifier passes, on the right body.**

The *other* statement — the weights `(2.0031, 2.6762)` and `(2.0567, 2.8536)` against "the admissible region
is empty for `v_2 > 0.98028`" — compares `Ξ_a`'s weight vector to the **ζ body's** admissible region.
Units are at least consistent (`0.98028 = 2v_2^*`, both in coefficient units), but the body is the wrong one,
so this is **not** a falsifier test and must be relabelled *"an order-of-magnitude orientation, not a test"*.
§8 does caveat it; §0 does not, and §0 is what will be read. **Required repair: §0 must review with the
`aud_spectral` numbers.**

## 7. Labels, corpus, FATAL (item 7)

Greps rerun. (i) `grep -rn "cos(π/m)\|cos(\\pi/m)" --include=*.md 03-research` — 19 hits, all in
`phase-147`, all about A.6; `R147_002:178–197` is the refutation, `R147_003:271–299` the corrected lemma.
The report's corpus row is accurate. (ii) `grep -rn "W_T\|support function" --include=*.md 03-research 04-papers`
— the "support function" hits are `phase-145`'s effective cone (no collision, as claimed), **but** `W_T`
collides with `𝒲_T` in `phase-120/122/124` (`P124_011:270`, `P122_002:148`, `P122_DEPENDENCY_GRAPH:129`),
where `q_T = R_T − ‖𝒲_TF‖²` — a *different* object (the Weil/prime operator of the Schur collar).
**Record the notation clash**; the geometric body itself is indeed new.

**FATAL rule: clean, confirmed.** No zero, no zero-free region, no moment bound imported. Paper 42
`main.tex` 4165–4230 (`thm:certifiedendpoints`) is the only certification and the report cites it correctly,
including the honest sentence that the Galerkin band is an *outer* bound and therefore certifies nothing.

**T6.** The heuristic is asserted, not argued. `‖[S_2,S_3]‖/(‖S_2‖‖S_3‖) = 0.100` (`K = 200`, my
computation) confirms non-commutativity, but non-commuting operator pencils frequently have closed-form
spectra (`J_k` itself is one), and `log3/log2 ∉ Q` is invoked with no quantitative role. Keep the conclusion
(`OPEN`, no closed form found), **delete the non-commutativity argument as evidence** or replace it with the
one real indication: the contact point moves continuously inside the sliver, so any closed form would have
to track `x(F_min(v))`, which is itself the unknown.

---

## 8. Required repairs

**R1.** §0 and §5: stop reporting "96.4%" and "99.85%" as findings. State instead: *the upper band edge in
every contact coordinate is `w_n + λ/(2x_n)` to `0.3%` (Hellmann–Feynman, exact first order); the round
measures `x_2 = 0.0745`, `x_3 = 0.0118`, `x_4 = 2.8·10⁻⁵`.* Promote the apex offset `8.5·10⁻⁶` (12× the
first-order normal distance) as the one non-first-order datum.
**R2.** §7: replace the `w_4` paragraph with the recomputed band `[0.3465729482, 0.3465736474]`,
`x_4 = 2.80·10⁻⁵`, `w_4` at `91.8%`, margin `5.71·10⁻⁸ ≈ λ/(2x_4)`. Withdraw "numerically zero",
"nearly flat", "at the optimum", "degeneracy, not a new facet".
**R3.** §4.2: fix the wide/narrow sentence (the `w_2` band is 3.8× wider than the `w_3` band).
**R4.** §0/§8: `≥56% three-way` → numerical observation about three specific relaxations; delete "100%".
**R5.** §2: Prop 2.2 proves convexity of `\overline{W_T}`; add the compact-resolvent line for attainment.
**R6.** §0: review the falsifier with the `aud_spectral` eigenvalues; mark the weight-vs-region comparison
as an orientation on a different body.
**R7.** §3: cite the *constrained* axis check (`t3_joint.py`), not the unconstrained table, for the
codimension-2 remark; and note that `min x_0` is not `K`-converged, so print `box ≤ −1.2776`.
**R8.** §1: one sentence distinguishing Lemma 3.1's table from `R147_002`'s refuted `cos(π/m)` row; record
the `W_T` / `𝒲_T` notation clash.
**R9.** §9(3): remove the non-commutativity argument, keep `OPEN`.

---

## 9. Honest reading of what round 6 established

Round 6 built the right object and measured it correctly, and its one durable result is negative and worth
having: the prime-free body `W_T` is **not** the box cut out by the exact axis projections
`±cos(π/(⌈2T/a⌉+1))` (Lemma 3.1, `PROVED`, genuinely new and correctly distinguished from phase 147's
Galois lemma) together with Gamma coercivity — in the arithmetic direction that box is short by `1.28`,
and the shortfall grows with `|v|`, so **no projection-only argument can ever reach Weil positivity**, at
any `T`. Prop 2.1 is correct and reduces the whole half-space question to a support function, which is a
clean reframing even though it is trivial to prove. Everything else in the round that is presented as a
*discovery* is, on recomputation, the exact first-order consequence of one already-known number: the
Hellmann–Feynman identity `∂λ/∂v_n = −2x_n(F_min)` forces the arithmetic weight to sit `λ/(2x_n)` below
each upper band edge, so "96.4%", "99.85%" and (after correction) "91.8% at `½log5`" all say only that
`λ(log2) ≈ 10⁻⁷` and `λ(½log5) ≲ 3·10⁻¹²`, quantities the corpus already had. The `½log5` paragraph is
worse than uninformative — it is wrong, describing as a flat direction a band of width `7·10⁻⁷` in which
the Euler weight again sits at the Hellmann–Feynman edge. The genuinely new numbers are three: the
minimiser's coordinates `x(F_min)`, the `O(1)` box deficit, and the apex offset `8.5·10⁻⁶`, which is the
only measurement in the round that is not first order in `λ` and is therefore the only place a next round
should push. No sign for `ζ` beyond `T ≤ log 2` is claimed, the FATAL rule is clean, and after repairs
R1–R9 the round should be recorded as: one new `PROVED` lemma, one trivial-but-useful reformulation, one
permanent negative about projection-only methods, and a set of diagnostics that are restatements of `λ`.

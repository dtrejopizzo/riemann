# Adversarial referee report R3 — `main.tex` (Paper 47), 57 pp., confirmatory pass after R2

Scope: (a) verification that each of the 22 exact edits of `TEX_ADVERSARIAL_REVIEW_R2.md` was applied
correctly (diffed against `main_pre_R2.tex.bak`); (b) full-rigour reading of the three new pieces
(`subsec:lat`/`thm:AL`; `thm:P`/`cor:P1`/`cor:P3`/`rem:P4`; the §8/§9/§10 + App. A/B/C restructure);
(c) re-run of the global overclaim and consistency checks.

**VERDICT: ACCEPT WITH MINOR REPAIRS.** One residual mathematical gap (R3-1, in `thm:AL`, live at
the paper's own headline window `T = ½log3`); the rest is exposition and cross-referencing. No
headline theorem is affected, no label changes, no sign is claimed beyond `log 2`.

---

## 1. R2 edits — ALL 22 VERIFIED APPLIED

Checked individually, by grep and by diff against the backup. No label was lost (`comm` on the two
label lists: 0 deletions, 9 additions — `sec:class`, `sec:archstr`, `app:encl`, `app:li`,
`app:diag`, `thm:P`, `cor:P1`, `cor:P3`, `rem:P4`); no duplicate labels; `main.log` reports no
undefined and no multiply-defined reference; every `\cite` ↔ `\bibitem` (set difference empty).

| R2 edit | status |
|---|---|
| 1 `thm:AL` restated / `cor:ALdef` rewritten / withdrawal paragraph | applied (L2153–2252) — see §2 |
| 2 `2.24889 → 2.24883` (L2709) | applied; `\Aconst` at `log 2` is now `2.24883` at L1056, L1954, L2609 and nowhere else |
| 3 `cor:KEP08` covers `T < ½log2` | applied, L1612–1615, via `thm:KEP3`(b)(1)⇒(4), `χ` supported in `{|u| ≥ log2}` |
| 4 abstract attributes the unconditional half to Zhu | applied, L103–104 |
| 5 "necessary / must exhibit" rescoped to `T > 0.74921` | applied, L2374 |
| 6 `D` collision: `thm:O`'s function → `ϱ` (L577–581), `thm:Zexh`'s denominator → `d_*` (L1149–1155, L1553–1554, L1598) | applied, and `d_*` is declared once in §1.5 (L320) |
| 7 "largest window with a single prime contact" | applied, L86 and L201 |
| 8 `−3.20·10⁻³` outside L1063 | applied (L219, L3012, L3326); the computed `−3.1964` survives only at L1063 |
| 9 "four enclosures" | applied, L1927 |
| 10 Galerkin bound no longer "a truth" | applied; the string "a truth" is gone |
| 11 `3.4211·10⁻²` in `thm:nest` | applied, L2881 |
| 12 `r_χ` factor `−½∫_ℝ χK` | applied, L1546–1548 |
| 13 `thm:finDet` Step 1 open interval `(0, 2T/ℓ)` | applied, L1274–1276 (and `d = |Z|` renamed `ℓ`, killing the `d` collision) — but see R3-4 |
| 14 `Γ_T` defined once | applied: L2312 defines, L2496 now reads "the form of Proposition~\ref{prop:nodes}" |
| 15 `rem:RHcert` row in the label table | applied, L3057, `\textsc{heuristic}` |
| 16 "for the methods of this paper" | applied, L2849 and L2909 |
| 17 `cor:nontermwise`: flat-top qualifier | applied, L1230 ("choose a flat-top `w` with `ŵ ≥ 0`") — but see R3-3 |
| 18 `prop:arch`(iv) weakened to an upper bound, with the Yoshida route named | applied, L2282–2290 — but see R3-7 |
| 19 `Coffey2005` key aligned with the volume year | applied, L3415 |
| 20 `arccosh√2 = 0.88137` limitation stated in the proof | applied, L2834–2836 |
| 21 `λ_min(A_T\|P_T)` in the abstract | applied via the macro `\lamA` (L41, L85) |
| 22 restructure §8/§9/§10 + App. A/B/C | applied — see §4 |

Global re-checks, all **CLEAN**: no numerical value of `inf W` at a two-prime window (`rem:galerkin`,
L2851–2858, is intact and its sentence is verbatim the rule); "primitive form" vs "complete form"
used correctly (`thm:C` primitive, `cor:KEP08` resting on `\cite{Zhu2026}` for the complete one);
no sign for `ζ` beyond `log 2`; the string "first beyond log 2" (and any variant of "first … beyond")
does not occur; no hardcoded section number anywhere — every cross-reference is a `\S\ref{}`, so the
"§8"-style pointers the brief worried about cannot have gone stale.

## 2. `subsec:lat` / Theorem AL′ (L2153–2252) — matches `R155_050 §2`, with one residual gap

Checked clause by clause against `def:W` (L1080–1090), `eq:nuw` (L1084–1087), `def:PD` (L450–458,
signed `ν`), `prop:weak` (L471, `č_F(±2T) = 0`), `thm:Dtail`, and the corrected statement of
`03-research/phase-155-row-d-flat-kernel-criterion/R155_050_AUDIT_AL_CORRECTION.md §2`.

Correct and present: the density is `½(1−w)K + 2w cosh(u/2)` (the R2 FATAL is genuinely repaired);
`supp w ⊆ [−U,U]` instead of `w ≡ 1` on `[U,∞)`, so `w ∈ 𝒲_T` really holds; `w^{(r−1)}` locally a.c.
with `w^{(r)} ∈ BV ∩ L¹`; "no sign condition and no bound `0 ≤ w ≤ 1`"; `κ_{±M} = ½`; the measure is
called **signed** with **countably many** atoms and finite TV `V_0 + O(d)`; `β = (2,0)`; feasibility
argued through `prop:weak`'s boundary-atom clause; `E_edge = 8cosh T/P + 2π² sinh T/P² + 16.9 cosh T/P³
= (4/π)cosh T·d + O(d²)` (I re-derived `8cosh T/P = (4/π)cosh T·d` and `4 × 4.21 = 16.84 ≤ 16.9`);
`ε_r = 2(1−2^{−r})ζ(r)V_r(πM/2T)^{−r}`; the cot regularity paragraph is stated correctly (the
subtracted `z^{−1}` is the omitted `k = 0` term, so the function is regular at `0`, odd, `|·| ≤ 2/P`
on `|z| ≤ ½`); `cor:ALdef`'s `(8T/π)cosh T·M^{−1}`, the plain-sampling constant
`cosh T√(4+16/π²) = 2.3708 cosh T` and the factor `1.862`; the `prop:TK` clause is labelled an
explicit *reading*, with the correct reason (`T_d` has degree `M` and `2ĝ₀` is not a trigonometric
polynomial); the withdrawal paragraph (L2249–2252) is present and names both defects. The archimedean
`0.28 M^{−1.2}` deficit is **not** compared with the edge rate — App. C, L3331–3338, states the
non-comparison explicitly ("it must therefore not be compared with the edge rate `Θ(M^{−1})` …; in
the full programme no ceiling has been computed"), exactly as `R155_050 §5` required.

**R3-1 — MINOR/MAJOR (the one residual gap). L2165, L2168, L2198: the comb-vanishing hypothesis
misses the boundary atom when `2T = log n`, which is precisely `T = ½log3`.**
`\NT = {n ≥ 2 : log n < 2T}` (L122, strict), so `eq:nuw` carries atoms at `±log n` for every `n` with
`log n ≥ 2T`, **including `log n = 2T`**. The hypothesis as printed is "`w(log n) = 0` for every `n`
with `log n > 2T`" (L2165, strict), so when `2T = log n` — `T = ½log3`, `n = 3`; `T = ½log2`, `n = 2`
— the atom at `±2T` survives, and it *cannot* be killed by strengthening the hypothesis, because
`def:W` forces `w(2T) = 1`. Hence "which by comb-vanishing is the whole density of `ν_w`" (L2168) and
"`ν_w = G(u)du` has no atoms" (L2198) are **false at exactly the paper's headline window**, and the
omitted atom contributes `−v_3 cos(2Tτ)` (`v_3 = 2log3/√3 ≈ 1.269`) to `ν̂_w`, i.e. an `O(1)` term, not
an `O(d)` one, to `f_lat − f_w`. Feasibility is unaffected (`prop:weak`); only the *value* statement is.
**Repair (one clause):** either add the hypothesis `2T ∉ {log n : n ≥ 2}`, or — better, since it costs
nothing — include the boundary atom in `ν_lat`, i.e. define
`ν_lat = Σ_{|j|≥M} d κ_j G(jd) δ_{jd} − Σ_{log n = 2T} (v_n/2)(δ_{2T} + δ_{−2T})`, and say that this
atom is reproduced exactly, so it cancels in `f_lat − f_w`.

**R3-2 — COSMETIC. L2237–2239 (`cor:ALdef`):** the bound `c_w − c_lat(M) ≤ (8T/π)cosh T·M^{−1} + …`
is stated "at fixed `w`" with no threshold, but it requires the second branch of the `min` in `thm:AL`
not to bind, i.e. `m(πM/2T) − 𝖠_T − ‖ν_lat‖_TV − 2ĝ₀(0) ≥ c_w − E_edge − ε_r`. That holds for all
large `M` (`m(πM/2T) → ∞`), but the corollary should say "for `M ≥ M_0(w)`".

## 3. Theorem P / Cor. P1 / Cor. P3 / Rem. P4 (L2425–2493) — CLEAN

Checked against `R155_047` as amended by `R155_048`. Diagonal `⟨S_c e_j, e_j⟩ = (2(2j+1)/π)∫_0^c j_j²`
✓; `Σ_j (2j+1)j_j(x)² = 1` gives `Σ_j R_j = 2c/π = tr S_c` ✓ (the basis loses no trace). **Ky Fan
direction is correct**: `Σ_{j<k} λ_j ≥ Σ_{j<k} R_j` (top-`k` eigenvalues dominate any `k` diagonal
entries), then `λ_k ≤ tr − Σ_{j<k}λ_j ≤ Σ_{j≥k} R_j = Λ_k`, using `λ_n ≥ 0` from
`S_c = (B_sQ_T)^*(B_sQ_T)` ✓. `cor:P1`'s constant `(2/π)c^{2j+1}/((2j+1)!!)²` is exact ✓, and the
`< 10^{−170}` tail disclosure is present (L2477). **0-based index is right**: `thm:P` quantifies over
`k ≥ 0`, `cor:P3` reads `min{k : Λ_k ≤ θ}`, and `prop:NC`'s min–max uses `λ_{n−1} > θ`; the two routes
give the identical index. Theorem values `5 / 7 / 8` at `½log3, log2, 0.80` from `Λ*` at
`τ₁ = 6.6159, 6.3576, 6.3576` ✓ (matches `r7a_02_closedform.py`); the grid values `5, 6, 7` at
`τ₁ = 6.4222, 6.4222, 6.3576` are kept in a separate `\textsc{diagnostic}` paragraph (L2470–2473)
with "No statement in this paper depends on that row" ✓, and the label table (L3056) repeats that.
`rem:P4` is correctly scoped to the **two-value** relaxation and names the multi-band family as the
untested refinement (Caveat 1 of `R155_048` applied) ✓.

Two-sided brackets: `thm:J`'s `L²` lower bounds are `⌈2Tτ₀/π⌉ − 1` with `2Tτ₀/π = 2.1996, 2.7755,
3.2034`, i.e. **2, 2, 3** ✓; combined with `5, 7, 8` this gives `[2,5]`, `[2,7]`, `[3,8]` ✓ and the
diagnostic variants `[2,5]`, `[2,6]`, `[3,7]` ✓ (L2528–2533). On `P_T` the printed
`0 ≤ n₋(A_∞|P_T) ≤ 5, 7, 8` is right, the lower half being vacuous (`⌈·⌉ − 3 ≤ 0` at the first two
windows) and flagged as such at L2519–2521. The old trace counts `37, 47, 54` survive only as the
comparison in `prop:NC` and `cor:P3` ✓, and the label table's `prop:NC` row quotes the trace bound
while the `thm:P` row quotes `5, 7, 8` ✓. No trace of the retired "`4,5,5` prolate counts" row.

## 4. The restructure — sound, four repairs

`sec:class` (§8), `sec:archstr` (§9), `sec:path` (§10), `sec:repro` (§11), `app:encl` (A),
`app:li` (B), `app:diag` (C). The label table is now **§11.2**, not §9; every row's label exists and
every `\textsc{}` matches the body (spot-checked 24 rows, including all five
`\textsc{proved (machine-verified)}` ones and the rewritten `thm:AL` row at L3054). The diagnostic
paragraphs of App. C (`rem:Zcheck`, `rem:comblp`, `rem:nodal`, `rem:signrule`, the `π_{13}`
cancellation, the `0.28M^{−1.2}` fit, the Schur measurements) occur **once only** — grep confirms no
duplicate in the core — and App. C carries its own label sub-table, explicitly "moved here from the
table of §11", with no row repeated between the two tables. No `\ref` mis-resolves: labels travel with
their bodies, no label was dropped, and the log is clean.

**R3-3 — MINOR. L1230 vs L3215: `cor:nontermwise` and `cor:Li` have been separated, and the
honesty of the pair depends on their adjacency.** R2's finding 13 was answered by the flat-top
qualifier, but the *reason* the qualifier is not vacuous — that the Li kernels evade the corollary by
not being flat-top — now sits 2000 lines away in Appendix B, with no pointer from the body.
**Repair:** append to L1230 "(the Li–Keiper kernels evade it precisely by not being flat-top;
Appendix~\ref{app:li})".

**R3-4 — COSMETIC. L1277 (`thm:finDet` Step 1):** with the R2 repair `a ∈ (0, 2T/ℓ)` the displayed
chain still reads `ra ≤ ℓa ≤ 2T`, which is now weaker than what holds and, read literally, still
puts `k = r` on the boundary where `ν̂ = g_Z` is not assumed. Write `ra ≤ ℓa < 2T`.

**R3-5 — MINOR. Appendix B is never referenced from the body** (`\ref{app:li}` occurs nowhere), and
its opening sentence, L3215, says "the strategy **the corollary** empties" with no `\ref` — a dangling
definite article left by the move. **Repair:** "…the strategy Corollary~\ref{cor:nontermwise}
empties…", plus the pointer of R3-3.

**R3-6 — MINOR. `prop:TAY` is used before it is stated.** It was moved to Appendix A (L3152) but is
invoked in the proof of `thm:C` (L907), in §1.2 (L198) and in §10.1 (L2683). There is no circularity —
Appendix A is self-contained and does not use `thm:C` — but a referee meets a load-bearing
proposition 2200 lines after the proof that needs it. **Repair:** at L907 write
"Proposition~\ref{prop:TAY} (Appendix~\ref{app:encl})". The same courtesy at L198. (`lem:bern`, also
moved to Appendix A, is used nowhere in the body, so it is fine there.)

**R3-7 — MINOR. L2282–2284 sits inside `\begin{proposition}` (prop:arch) and discusses item (iv)
before (iv) is stated at L2285.** The sentence "…and (iv) is stated as an upper bound only for that
reason: *strict* positivity at `T = ½log2`, available in \cite{Yoshida1992}, would add
`½log2 ≤ T*_∞`" is the R2 repair, correctly made, but it is prose inside a numbered statement and it
is out of order. **Repair:** move it to a remark immediately after `\end{proof}`.

**R3-8 — MINOR (exposition). §9 has exactly one subsection, §9.1 "The archimedean form alone",
spanning pp. 36–43** (L2258–2658: `prop:arch`, `prop:nodes`, `prop:NC`, `thm:P`, `cor:P1`, `cor:P3`,
`rem:P4`, `thm:J`, `thm:arena`, `cor:arena`, `rem:PF2`). Seven pages of index theory under a heading
that describes only its first two pages. Meanwhile `prop:schur`, `thm:w11`, `thm:nest`,
`prop:bprime`, `prop:shifts`, `lem:N`, `prop:G` — which R2's §4 assigned to §9 — remained in §10.4,
so §10 ("What a closing argument must do") is half results and half programme. **Repair:** either
split §9 into §9.1 (the form alone), §9.2 (the negative index: `prop:NC`–`thm:J`) and §9.3 (gaps and
the arena), or complete the move R2 prescribed. Either is a 10-minute edit; the present state is the
only place where the restructure is visibly half-done.

## 5. Nothing that R2 broke

No theorem is used before it is stated except `prop:TAY` (R3-6, and that is a pointer problem, not a
logical one). No proof forward-references an appendix for a *proof* it needs — App. A's `prop:TAY`
and `lem:bern` are proved there independently, App. B's `cor:Li` is used by nothing, App. C is
diagnostic throughout and enters no proof (checked: the four `\ref`s from the body into App. C are all
to measured quantities, L2358, L2571, L2947, L3066). Constants unchanged by the restructure and still
mutually consistent: `C₀ = −5.3721834`, `τ₀ = 6.28983599`, `𝖠_T = 0.98025814 / 2.24883`,
`B_* = 7.62101`, `c = 8.8577·10⁻⁵`, `68.51T → 37/47/54`, `T₀(0) = 0.74921`, `2π/τ₀ = 0.9989426`.

## 6. Residual edits, by line

| # | line(s) | severity | edit |
|---|---|---|---|
| R3-1 | 2165, 2168, 2198 | **MINOR/MAJOR** | boundary atom when `2T = log n` (live at `½log3`): add `2T ∉ {log n}`, or put `−Σ_{log n = 2T}(v_n/2)(δ_{2T}+δ_{−2T})` into `ν_lat` and say it cancels |
| R3-2 | 2237–2239 | COSMETIC | `cor:ALdef`: "for `M ≥ M_0(w)`" |
| R3-3 | 1230 | MINOR | point to Appendix~\ref{app:li} for why the flat-top qualifier bites |
| R3-4 | 1277 | COSMETIC | `ra ≤ ℓa < 2T` |
| R3-5 | 3215 | MINOR | "the corollary" → `Corollary~\ref{cor:nontermwise}` |
| R3-6 | 907, 198 | MINOR | "(Appendix~\ref{app:encl})" after `prop:TAY` |
| R3-7 | 2282–2284 | MINOR | move the (iv) commentary out of the proposition body |
| R3-8 | 2253–2658 | MINOR | subdivide §9, or finish the §9/§10.4 move |

Row-D label unchanged; endpoint of record unchanged (`λ_min(A_{½log3}|P_{½log3}) ≥ 8.8577·10⁻⁵`,
primitive form); no sign for `ζ` claimed at any window.

---

## Changes after R3 (applied , editor's log)

All eight edits applied; `main.tex` recompiles at **57 pp., 0 `^!` errors, no undefined or
multiply-defined references**. No label was added, removed or renamed except the two new
subsection labels `subsec:negindex`, `subsec:arena`.

| # | resolution |
|---|---|
| R3-1 | The **more general** option taken: the boundary case `2T = log n` is *not* excluded. `thm:AL`'s hypothesis now says so in one clause, justified by `def:W` forcing `w(2T)=1` (so the atom is a fixed multiple of `δ_{±2T}` and can be reproduced exactly); `ν_lat` carries `−Σ_{log n = 2T}(v_n/2)(δ_{2T}+δ_{−2T})`; "the whole density" → "the whole **absolutely continuous** density, the only surviving atom being the boundary one"; the Value step of the proof states the decomposition, names `T = ½log3` (`−(v_3/2)(δ_{2T}+δ_{−2T})`) as a live instance, and notes the exact cancellation in `f_lat − f_w`. Rate, sharp constant, `E_edge`, `ε_r` and feasibility unchanged. |
| R3-2 | `cor:ALdef` now reads "At fixed `w` and for `M ≥ M_0(w)` — large enough that the second branch of the minimum in Theorem~AL does not bind, which happens for all large `M` since `m(πM/2T) → ∞`". |
| R3-3 | `cor:nontermwise` ends "(the Li–Keiper kernels evade this corollary precisely by not being flat-top; see Appendix~\ref{app:li})". |
| R3-4 | `thm:finDet` Step 1 chain now `ra ≤ ℓa < 2T`. |
| R3-5 | Appendix B opens with a sentence stating its purpose, and "the strategy the corollary empties" → "the strategy Corollary~\ref{cor:nontermwise} empties"; `app:li` is now referenced from the body (R3-3). |
| R3-6 | Both body uses of `prop:TAY` (§1.2 and the proof of `thm:C`) now read "Proposition~\ref{prop:TAY}, Appendix~\ref{app:encl}". |
| R3-7 | The (iv) commentary is removed from `prop:arch`(iii) and reinstated verbatim as a `\begin{remark}` immediately after `\end{proof}`. |
| R3-8 | §9 split into **9.1 Thresholds and nodal structure** (`prop:arch`, `prop:nodes`), **9.2 The negative index** (`prop:NC`, `thm:P`, `cor:P1`, `cor:P3`, `rem:P4`, `thm:J`), **9.3 The arena, and a no-go** (`thm:arena`, `cor:arena`, `rem:PF2`). The §10.4 group (`prop:schur`, `thm:w11`, `rem:galerkin`, `thm:nest`, `prop:bprime`, `prop:shifts`, `lem:N`, `prop:G`) was **already** a single subsection, §10.4 "One direction at `T = log2`" (`subsec:schur`), so it was left in place. |

Row-D label unchanged; endpoint of record unchanged; no sign for `ζ` claimed beyond `log 2`.


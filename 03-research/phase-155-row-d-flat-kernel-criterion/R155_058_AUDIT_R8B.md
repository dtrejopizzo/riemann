# R155_058 — Audit of R155_053 (round 8B, P6 alignment)

**Object.** `R155_053_ROUND8B_P6_ALIGNMENT.md` (426 lines), checked against Paper 47
(`04-papers/47-row-d-dual-certificates/main.tex`) and Paper 46 (`04-papers/46-intersection-frame-defect/archive/main.md`)
at the lines the memo cites, plus the phase-155 record. One check script (`scratchpad/chk.py`, 2 s,
mpmath digamma + numpy grid, not committed) was used only to reproduce the memo's constants.
Rule applied (memory `feedback-check-against-paper-definitions`): every integration is checked against
the paper's *own* definitions (`eq:symbol` line 118, `eq:form` 124, `eq:W` 133, `def:PD` 450, `def:W` 1081,
`eq:nuw` 1084, `eq:fw` 1098), not against the memo's paraphrase.

**Summary of the verdict.** Two `PROVED` sentences are false or unsupported as written and must be
fixed (Thm 4.2(i) positive clause; Prop 2.3(v) negative replacement); one hypothesis is missing
(Prop 1.1(iii), `v ≥ 0`); several citations need sharpening (Thm 3.1(b) "thm:O", the `T ≥ ½ log 2`
quantifier in Thm 3.1(c), `thm:Z`(ii) needs `w` regular, `τ_env(w)` definition). Everything numerical
reproduces to the printed digits. The equivalence chain itself (Thm 3.1(c), Prop 4.1) is correct and on
record. With the fixes below, "P6 closed as an equivalence" is ACCEPTED, in the sense PATH-TO-D:313–316
calls "failure — likely and expected": there is no isolated arithmetic `X` strictly weaker than `D_T`;
the exact per-window statement is `λ^W_T > 0`.

---

## Per-claim verdicts

### Header / notation (memo lines 8–16)
**PASS.** Definitions match `main.tex:114–137`; `C₀ = −5.3721834` (`eq:m`, line 330; reproduced
`−5.37218341922…`); `λ^W ≤ λ^P ≤ λ^A` is `prop:weak` (line 462) + line 137; "any nonnegative weights"
is line 447. `|N_T| = ⌈e^{2T}⌉ − 2` correct in both the integer and non-integer case.

### Prop 1.1 (finite dependence; `D_T ⟺ v_T ∈ 𝒟_T`) — memo 34–56
- (i),(iv) **PASS** (definitional).
- (ii) **PASS.** The reduction to real tests is correct: for `F = F₁ + iF₂`, `Im(F̂₁ \overline{F̂₂})` is
 odd (Hermitian symmetry of each `F̂_j`) and integrates to `0` against even `σ_T`; `A(F_j), B(F_j)` are
 real. Each real unit `F` in the form domain gives the half-space `Σ v_n c_F(log n) ≤ C₀ + Lev(c_F)`
 (`eq:Aform`, line 384; there `Lev` uses `Re c_F`, which for real `F` is `c_F`). When `Lev = ∞` the
 constraint is void since the comb term is finite. Closed convex intersection: correct. The set
 `𝒟_T` is defined for all `v ∈ ℝ^{N_T}` — fine for (ii).
- (iii) **AMEND.** `thm:SC` (line 2003) is stated for **nonnegative** weights (`cor:mono` uses `v_n ≥ 0`
 and `|c_F| ≤ ‖F‖²`, line 1999–2001). The memo's `𝒟_T ∩ {Σ v_n < −C₀ − φ} = ∅` is asserted for
 arbitrary `v ∈ ℝ^{N_T}`, where `thm:SC` does not apply (for signed `v` the same proof gives
 `C₀ + Σ|v_n| + φ`). **Fix:** either restrict (iii) to `v ≥ 0` ("for the cone of nonnegative vectors,
 which contains every `v_T(a)`") or write `Σ|v_n|`. `0 ∉ 𝒟_T` for `T ≥ 0.74921` is `prop:arch`(ii)
 (line 2290–2292) — PASS.

### Cor 1.2 (regimes) — memo 58–63
**PASS.** `σ_T` constant on `(½ log n_k, ½ log n_{k+1}]` by `N_T = {log n < 2T}`; zero-extension
`P_T ⊂ P_{T'}` with the same `𝔞` inside a regime gives `λ^A` nonincreasing. The refusal to sign the
jump at a regime boundary is correct (Lemma 4.2b shows `c_F(log n)` takes both signs on `P_T`).

### Prop 1.3 (arithmetic content = uniformity) — memo 65–72
**PASS.** `RH ⟺ ∀T: 𝔞_T ≥ 0 on P_T` is `main.tex:137–142` (Paper 45 Thm 10.4 + Weil). (b) depends on
§4; see Thm 4.2 / Prop 4.3 below — the parts used ((ii) amplification, Prop 4.3) survive the audit.

### Rem 1.4 — **PASS** (`prop:decide`, line 2694–2699, says exactly this).

### Prop 2.1 (finite band, `τ_* ≤ τ₁`) — memo 78–95
**PASS.** `m_lo` increasing (`lem:mbounds`(ii), line 656–659; derivative `τ⁻¹+τ⁻²+τ⁻³ > 0`, line 671);
comb `≤ A` (`lem:mbounds`(iii)); real-analyticity of `Re ψ(¼+iτ/2)` in real `τ` and `σ → +∞` confine
the zero set to a compact interval — correct. Numerics reproduced: `τ₁ = 60.5432` (`A = 2.248826`),
`τ₁ = 120.0865` (`A = 2.941974`, `v₄ = log 2` correct: `2Λ(4)/√4 = log 2`); `2πe^A = 59.543 / 119.087`.
Item 6 of the memo (the paper's "threshold `2πe^{A}`" at `main.tex:1041` vs the exact envelope zero
`τ₁`) is a fair editorial point; `prop:env`(i) already carries `o(1)`, so nothing in the paper is false.

### Prop 2.2 (alignment structure, Diophantine bracket) — memo 97–131
**PASS**, every step re-derived:
- `σ(τ) < 0 ⟹ v₂cos(τ log 2) > m(τ) − v₃cos(τ log 3) ≥ m_lo(τ) − v₃ > 0` for `τ > τ_a`; symmetric for
 `3` with `τ_b < τ_a` (`v₂ < v₃`). Roots reproduced: `τ_a = 23.3409`, `τ_b = 17.7446`.
- The arc conditions `|τ log 2 − 2πk| < δ₂ < π/2`, `|τ log 3 − 2πl| < δ₃ < π/2`; `δ_j` decreasing since
 `m_lo` increasing; `k, l ≥ 1` since `τ log 2 > 16 > π/2` on `τ > τ_a`.
- Dividing by `log 2`, `log 3` and subtracting: `2π|k/log 2 − l/log 3| < δ₂/log 2 + δ₃/log 3`; multiply by
 `log 2·log 3/(2π)`: `|k log 3 − l log 2| < (δ₂ log 3 + δ₃ log 2)/(2π) < (π/2)(log 3 + log 2)/(2π) = log 6/4
 = 0.44794`. Correct. `e^{±0.4479} = 0.639, 1.565` correct.
- Arc length `< π/log 2 = 4.53`; arc spacing `2π/log 2 = 9.065`; count `⌊(τ₁−τ_a) log 2/2π⌋ + 2 = ⌊4.10⌋+2
 = 6` — reproduced. Second regime `⌊10.67⌋ + 2 = 12` — reproduced.
- `{2,3,4}`: `g(y) = 2v₄y² + v₂y − v₄`, roots `y₀ = 0.43702` (reproduced), `y₋ = −1.144 < −1`; vertex
 `−v₂/(4v₄) = −0.354`; `arccos y₀ = 1.1185`; `τ_b' = 34.4909` (reproduced); constant
 `(1.1185 log 3 + (π/2) log 2)/(2π) = 0.3689` (reproduced).
- Memo item 7 (arcs, not components) is the correct reading; the statement is about arcs. PASS.
- Editorial: the pairs `(k,l) = (5,8), (12,19)` are convergents `8/5, 19/12` of `log 3/log 2`
 (memo says "of `log 2/log 3`": the reciprocal, `5/8, 12/19` — equivalent). `(3,5)` and `(7,11)` are
 intermediate fractions (`11/7` is the mediant of `3/2` and `8/5`). Fine as `DIAGNOSTIC`.

### Table 2.2a and the proof-grade witnesses — memo 133–147
**PASS**; labels honest. Grid sign changes reproduced to three digits for `{2,3}`
(`2.277, 4.816, 7.272, 9.666, 11.966, 16.251, 18.494, 27.558, 28.938, 45.149, 46.129`) and `{2,3,4}`
(`…, 62.616, 63.776, 108.495, 108.950`); "same six to within 0.6" holds (largest shift `0.58` at `4.237`).
No `σ < 0` on `(τ_*+0.5, τ₁]` in either regime (grid). Witnesses: at `τ = 45.64206`, comb `2.21553`,
`m_up = 2.00492` (true `m = 1.98293`), margin `0.2106`; at `τ = 108.72265`, comb `2.93679`, `m_up = 2.86013`
(true `m = 2.85092`), margin `0.0767`. Both reproduced. `m_up` is `lem:mbounds`(ii) (PROVED), so
`σ < 0` at these points is a proved inequality evaluated in floating point.
**AMEND (label only):** in the §5 table write "PROVED modulo double-precision evaluation (margin
`0.21` / `0.077` ≫ rounding)" rather than bare PROVED — the memo's own item 4 says so; the table should too.

### Prop 2.3 (trace-class negative part; band does not decide) — memo 149–176
- (i) **PASS.** `Q_T σ₋(D) Q_T = (Q_T σ₋^{1/2}(D))(σ₋^{1/2}(D) Q_T)`, each factor Hilbert–Schmidt with
 `‖·‖²_{HS} = 2T·(2π)^{−1}∫σ₋ < ∞`; trace of a positive trace-class operator with continuous kernel on
 `I_T` is `∫_{I_T} k(0) = 2T·(2π)^{−1}∫σ₋`. Same argument as `R155_039:70–82`. Values reproduced:
 `tr Neg_{log 2} = 5.233`, `sup σ₋ = 7.621 = B_*` (`main.tex:1057`), `tr Neg_{½ log 5} = 7.039`.
- (ii),(iii),(iv) **PASS** (the split `𝔞_T = Pos_T − Neg_T`; `Neg_T ≥ 0` gives `‖Neg_T‖ ≤ tr Neg_T`).
- (v) **FAIL as written → AMEND (conclusion survives).** The "negative replacement" says: "replacing `σ₊`
 by `0` off the band gives the form `−Neg_T`" (memo 158–159, 168). False: `σ₊ = max(σ,0)` is **not**
 supported off the band. `σ > 0` on `(2.278, 4.816)`, `(7.272, 9.666)`, `(11.966, 16.251)`, `(18.494, 27.558)`,
 `(28.938, 45.149)` — all inside `[0, τ_*]`. Killing `σ₊` off the band leaves `Q_T (σ·1_{[−τ_*,τ_*]})(D) Q_T`,
 whose sign on `P_T` at fixed `T` is *not* determined by anything in the memo. **Fix:** replace `σ` off the
 band by `−c` (or by `σ − c·1_{|τ|>τ_*}`) with `c` large: on `L²(I_T)` the form is
 `≤ (sup σ₊)‖F‖² − c(1 − λ₀(Tτ_*))‖F‖² < 0` for `c > sup σ₊/(1 − λ₀)`, using the same prolate bound as the
 positive replacement. Then both replacements leave `σ|_{[−τ_*,τ_*]}` unchanged and give opposite signs
 on all of `L²(I_T)`, hence on `P_T`. (The symbol `−c` off the band is a legitimate bounded symbol; the
 proposition is about symbols, not about ζ.) The positive replacement (memo 169–172) is correct: `Q_T
 1_{band}(D) Q_T` is the prolate operator with top eigenvalue `λ₀(Tτ_*) < 1`, and `Q_T = I` on `L²(I_T)`.
- Heuristic mode count `2T·2τ_*/(2π) = 20.4` at `log 2` — reproduced; labelled HEURISTIC. PASS.

### Lemma 3.0 (`X_T^{band} ⟺ X_T`) — memo 190–193
**PASS with AMEND.** `prop:env`(i) (line 1034) gives `f_w ≥ m_lo(τ) − A_T − ‖ν_w‖_TV − 2k₀(τ)` for the
feasible triple `(ν_w, 2, 0)`, with `k₀(τ) = 2cosh T/τ + sinh T/τ²` (line 480). Since `m_lo` is increasing
and `k₀` decreasing, the right side has a unique zero; **define** `τ_env(w)` as that root (the paper's
`τ_env := 2πe^{A+‖ν‖+o(1)}` at line 1035 is not a definite number). Then `f_w ≥ 0` on `[τ_env(w), ∞)` and
the lemma is exact. The parenthetical "`τ_env(w) ≥ 2πe^{A_T}`" is not literally proved (the `o(1)` and
the `k₀` term go in opposite directions); write "`τ_env(w) ≥ τ₁(A_T + ‖ν_w‖_TV) − o(1)`" or drop it.

### Thm 3.1 (reduction chain) — memo 195–213
- (a) **PASS.** `def:W` paragraph (`main.tex:1091–1095`): for *every* `w ∈ 𝒲_T`, `(ν_w, 2, 0)` is dual
 feasible and `W_T ≥ inf f_w` on `L²(I_T)` (`prop:weak` + `prop:P`, line 624–629). `W_T = 𝔞_T` on `P_T`.
 "regular or not" is correct here.
- (b) **PASS**, with two AMENDs.
 1. `thm:Zexh`(i),(ii) (lines 1137–1141) are stated for `T ≥ ½ log 2`; the memo says so. Correct.
 2. "If `λ^W_T = 0` no certificate of value `≥ 0` *need* exist (`thm:O`)." Two problems: (α) `thm:O`
 (line 562–569) is stated for the **primitive** value `λ^P` with annihilators `h_j`; the complete-form
 version is only *alluded to* at lines 555–557 (strong duality, not non-attainment). (β) What the
 argument actually gives is stronger: if `λ^W_T = 0`, then **no** `w ∈ 𝒲_T` satisfies `X_T(w)`. The proof
 of `thm:O` transcribes verbatim (minimiser `F_⋆` of `W_T` exists by Bombieri Thm 3 / the compactness at
 lines 572–577; `ϱ = σ_T + ν̂_w + 2ĝ₀ − λ^W ≥ 0` and `∫ϱ|F̂_⋆|² = 0` force `ϱ ≡ 0`; on `0 < |u| < 2T` this
 reads `2g₀(u) = ½K(|u|) + atoms`, impossible since `g₀` is bounded continuous and `K ~ 1/u`).
 **Fix:** state and prove a one-paragraph "Lemma 3.1b (non-attainment for the complete form)"; then
 record the exact per-window statement, which the memo misses:
 ```
 ∃ w ∈ 𝒲_T with X_T(w) ⟺ λ^W_T > 0 (T ≥ ½ log 2).
 ```
 (⟸ is `thm:Zexh`(i); ⟹: `λ^W_T ≥ inf f_w ≥ 0` by weak duality and `inf f_w < λ^W_T` by non-attainment.)
 This is the sharpest form of "X_T is `λ^W_T > 0`", and it is exactly what Prop 4.1 uses.
- **Per-window converse `λ^A_T ≥ 0 ⟹ λ^W_T ≥ 0` (or `⟹ λ^P_T ≥ 0`): OPEN — CONFIRMED.** Grep of
 `main.tex` and phase 154–155 for any implication from `λ^A` to `λ^W`/`λ^P` returns only the memo itself.
 Paper 47 proves `λ^W ≤ λ^P ≤ λ^A` (`prop:weak`) and nothing in the other direction at fixed `T`; the only
 route from `D_T` to `λ^W_T > 0` is through `∀T` (Paper 45 Thm 10.4 ⟹ RH ⟹ `cor:RH` proof). The memo's
 OPEN label is correct and should stay.
- (c) **PASS with AMEND (quantifier).** `cor:RH` (line 1167) is `T ≥ ½ log 2` throughout (its proof via
 `thm:Zexh` needs `d_* > 0` on `u ≥ 2T`, which used `2T ≥ log 2 > 0.3`, line 1152). The chain must read
 `∀T ≥ ½ log 2 ∃w …`; for `T < ½ log 2` the comb is empty and `D_T` is `prop:arch`(iii), so nothing is lost,
 but the quantifier as printed ("∀T") is not what is cited. RH `⟹ λ^W_T > 0` is in the `cor:RH` proof
 (lines 1176–1182, Jensen count). Correct.

### Rem 3.1a — memo 215–226
**AMEND (iii):** `thm:Z`(ii) (`eq:Z`, line 1108) is stated for `w ∈ 𝒲_T^{reg}` only; the memo applies it
to "the inequality `X_T(w)` at such `τ`" without the regularity qualifier. Add "for regular `w`". (i),(ii)
PASS (`thm:Zexh`; `prop:env`(ii) + `lem:mbounds`(iii) Kronecker, lines 671–676).

### Thm 3.2 (`H_θ ⟺ β_max ≤ θ`; logical form of the negative) — memo 228–254
- (i) **PASS.** Paper 46 Thm 27.10 (`46/main.md:11476–11499`) is stated for `θ ∈ [½,1)` and proved by the
 Mellin/uniqueness argument (not Landau's theorem); Cor 27.10a (11501–11508) gives the `β_max` form.
 The memo's `θ ∈ (½,1)` plus "`H_½ ⟺ RH`" is covered.
- (ii),(iii) **PASS** (pure translation through (i) and Thm 3.1(c)).
- (iv) **PASS.** The memo correctly refuses to state "PNT does not imply RH" as a fact about ζ and casts
 the negative as a class/derivation statement in the sense of Paper 46 Thm 18.1 / Rem 18.1a
 (`46/main.md:4785–4820`: "a derivation from `𝔓` … is a derivation for every structure satisfying `𝔓`").
 I found no sentence in §§3–4 that slides into the factual reading (memo item 8): checked lines 228–354.
- (v) **PASS.** "`ψ(x) − x ≠ O(x^θ)` for every `θ < β₀`" follows from Thm 27.10 (⇒) contrapositive
 (if `ψ−x = O(x^θ)` then `≪_ε x^{θ+ε}` for all `ε`, so `β_max ≤ θ < β₀`). The effective-`T` OPEN flag is right.

### Prop 4.1 (`𝔈_T = −λ^W_T`; `RH ⟺ lim λ^W_T ≥ 0`) — memo 258–270
**PASS.** `𝔈_T = −sup_w inf_τ f_w = −λ^W_T` is `thm:Zexh`(i) (for `T ≥ ½ log 2`, as stated). Monotonicity
is `cor:KEP08` proof (lines 1611–1613). `RH ⟹ λ^W_T > 0 ∀T ⟹ lim ≥ 0`; `lim ≥ 0` + nonincreasing
`⟹ λ^W_T ≥ 0 ∀T ⟹ W_T ≥ 0 ∀T ⟹ RH` (Weil). Correct. Zhu's law reading labelled HEURISTIC. PASS.
With Lemma 3.1b above, "X_T strictly solvable ⟺ 𝔈_T < 0" upgrades to "X_T solvable ⟺ 𝔈_T < 0".

### Thm 4.2 (finite modifications) — memo 272–300
- **(i) Deletion — FAIL on the positive clause; the failure clause PASSES.**
 The memo asserts (`PROVED`): "`D_T(a)` holds for `T ≤ log 2`" for `a = Λ·1_{n≥N}`, citing `prop:arch`(iii)
 (`main.tex:2296`). But `prop:arch`(iii) reads: "For `2T < log 2` the contact set is empty, so `W_T = A_∞`
 and `λ_∞(T) ≥ 0` by the known positivity of `W_T` for `T ≤ log 2`." That establishes `A_∞ ≥ 0` (hence
 `A_∞|_{P_T} ≥ 0`) **only for `T < ½ log 2`**. For `T ∈ [½ log 2, log 2]`, `W_T ≠ A_∞` (contacts `2, 3` are
 present) and `𝔞_T^Λ ≥ 0` does not imply `A_∞ ≥ 0` on `P_T` (the comb term `−Σ v_n c_F(log n)` has both
 signs, Lemma 4.2b). Worse, the phase-155 record says the clause is **false** on most of that range:
 `T*_{∞,P} ≤ 0.5958` (Galerkin *upper* bound on the threshold, i.e. the Galerkin infimum of `A_∞|_{P_T}` is
 negative for `T > 0.5958`; `R155_023:23–24`, `R155_029:11`, DIAGNOSTIC in floating point; the remark at
 `main.tex:2312–2316` explicitly says strict positivity at `½ log 2` is *not* re-proved in Paper 47). So for
 `T ∈ (0.5958, log 2]` the deleted comb `a` fails `D_T(a)` by the record, and for `T ∈ [½ log 2, 0.5958]` the
 sign is not on record either way.
 **Fix:** "(i) `D_T(a)` holds for `T < ½ log 2` (`prop:arch`(iii)) and **fails for every**
 `T ∈ [T₀(0), ½ log N] = [0.74921, ½ log N]` (`prop:arch`(ii)); on `[½ log 2, 0.74921)` its sign is that of
 `λ^P_∞(T)`, not decided here (DIAGNOSTIC: negative for `T > 0.5958`, `R155_023`)." The failure interval,
 `N ≥ 5 ⟹ ½ log N ≥ 0.8047 > 0.74921`, is correct and is all that Cor 4.4 and Prop 1.3(b) use.
- **(ii) Amplification / Lemma 4.2b — PASS.** Checked: `J = (−T, −T+ℓ)`, `J+u₀`, `J+2u₀` pairwise disjoint
 iff `ℓ ≤ u₀`; `J ∪ (J+u₀) ⊂ I_T` iff `ℓ ≤ 2T − u₀`; with Paper 47's `c_F(u) = ∫F(t)\overline{F(t−u)}dt`
 (line 116) and `F_φ = φ + φ(·−u₀)`, `c_{F_φ}(u₀) = ⟨φ + φ_{u₀}, φ_{u₀} + φ_{2u₀}⟩ = ‖φ‖²` (three cross terms
 vanish). `φ ↦ F_φ` injective, so `V` is infinite-dimensional; `P_T ∩ V` has codimension `≤ 2` in `V`, hence
 contains a nonzero `F_φ`; `F_φ` smooth so `Lev < ∞`; `𝔞^{(a)}(F) = 𝔞^Λ(F) − (2c/√n₀) c_F(log n₀)` and
 `c_* = √n₀ max(𝔞^Λ(F),0)/(2 c_F(log n₀))` is right. For `n₀ = 2`, any `T > ½ log 2`. PASS.
- **(iii) Preservation — PASS.** `ζ_a := exp(Σ_n a(n) n^{−s}/log n)`: for `a = Λ` this is `log ζ` on
 `Re s > 1`. Deletion: exponent differs from `log ζ` by the **finite** sum `−Σ_{n<N} Λ(n) n^{−s}/log n`, an
 entire function; `E = exp(entire)` is entire and zero-free; `ζ_a = ζ·E` is then the meromorphic
 continuation. Amplification: `E = exp(c n₀^{−s}/log n₀)`, same. So `ζ_a` has exactly the zeros and the pole
 of ζ (residue `E(1)`). `−ζ_a'/ζ_a = Σ a(n) n^{−s}` consistently. `ψ_a = ψ + const` for `x ≥ N` (resp. `n₀`)
 preserves every `H_θ` and every error term. Deletion preserves `a ≤ Λ`. The functional equation is not
 preserved (`E(s) ≠ E(1−s)`) — correctly noted; this is exactly why the explicit formula of `ζ_a` acquires
 the extra term `+Σ_{n<N} v_n c_F(log n)` and the "same zeros" class does not transfer positivity. The
 task's worry ("is `Σ c n₀^{−s}·…` really an entire zero-free factor?") is resolved: yes, a single exponential
 of a finite Dirichlet polynomial.

### Prop 4.3 (finitely supported combs fail for large `T`) — memo 302–320
**PASS**, re-derived. `F_T = (−∂² + ¼)G_T`, `G_T = g(t/T)`, `g ∈ C_c^∞(−1,1)`: two integrations by parts
(boundary terms vanish) give `A(F_T) = ∫G_T(−¼+¼)e^{t/2} = 0`, `B(F_T) = 0`; `F̂_T = (τ²+¼)T ĝ(Tτ)`;
substituting `s = Tτ`, both numerator and denominator carry the same factor `T/(2π)`, giving the printed
ratio. Domination for `T ≥ 1`: `|σ(s/T)| ≤ |m(s/T)| + A_S ≤ C(1 + log(2+|s|))` (`m ≥ C₀`, `m ≤ log(τ/2π) + 1/τ +
½log(1+1/4τ²)` for `τ ≥ 1`, `m` bounded on `[0,1]`), and `(s²/T²+¼)² ≤ (s²+¼)²`, so the integrand is dominated
by `C(1+log(2+|s|))(s²+¼)²|ĝ|² ∈ L¹`. Pointwise limit `σ(0)/16·|ĝ|²` over `1/16·|ĝ|²`; `σ(0) = C₀ − A_S` by
continuity of `m` at `0`. `limsup λ^A_T(a) ≤ C₀ − A_S < 0`. Consistent with `prop:arch`(ii) (`A_S = 0`). PASS.
The HEURISTIC reading (for ζ, `σ_T(s/T) ↛ σ_T(0)` because new atoms `log n ~ 2T` enter) is correctly labelled.

### Cor 4.4 (classical prime-side results void per window) — memo 322–341
**PASS as METHOD-CONSTRAINT** (the label the memo gives, matching Paper 46 Thm 18.1's label at
`46/main.md:4785, 4805`). Closure properties check: `C_PNT(θ)` and `C_zeros` closed under both operations
(by Thm 4.2(iii)); `C_BT = {0 ≤ a ≤ Λ}` closed under deletion only — correct. Window ranges: deletion needs
`N ≥ e^{2T}`, i.e. `N ≥ 5` for `T ≥ 0.74921` (`e^{1.498} = 4.47`) — correct; amplification `n₀ = 2` for any
`T > ½ log 2` — correct. The "dichotomy" (memo 336–340) is a tautology dressed as a dichotomy — either
`𝒞 ⊆ 𝒞_D` or not — but that is what the task asked ("state the dichotomy"), and the content is the second
clause: every asymptotic / zero-theoretic / upper-sieve class is of the second kind. PASS.
**Editorial AMEND:** "no derivation … is sound" should be phrased as in Thm 18.1(ii): "a derivation of
`D_T` whose only prime input is `𝒞`-membership is a derivation of `D_T(a)` for every `a ∈ 𝒞`, hence proves
a false statement for the member of Thm 4.2 — so no such derivation exists". The memo's wording is
equivalent but the Thm 18.1 form avoids the word "sound".

### Rem 4.5 — **PASS by citation** (T2 begins at `46/main.md:4822`; not re-verified, not claimed to be).

### Prop 4.6 (irreducibility) — memo 343–354
**PASS as method constraint; AMEND label of one sentence.** (a) and (b) are consequences of Cor 4.4 and
Paper 46 T1/T2 respectively. The sentence "the minimal hypothesis with both properties is … `D_T` itself"
is interpretive, not a theorem (no minimality is proved); label it HEURISTIC alongside the last sentence,
or delete it. Per-window derivations of record (Paper 42, Zhu `cor:KEP08`, `thm:C`) — correct list.

### Numerics labelling (task item) — **PASS**, with the one label AMEND above (witnesses = floating point).
All numbers in the memo that I could recompute agree to the printed digits (see the PASS lines above);
the only labelled-PROVED numbers are (a) roots of monotone explicit equations and (b) two evaluations
of a proved inequality; both are honestly described in memo item 4.

### `X_T` name clash — **CONFIRMED, AMEND.** Paper 46 uses `X_T` for the Tate collar operator
(`46/main.md:673–677`, `790–796`, bordered form `[[L_T, X_T],[X_T^*, 𝔅_T]]`). Since Paper 47 §9 will be read
next to Paper 46 Part III/IV, rename now (suggest `𝖠_T(w)`, "alignment inequality", or `Al_T(w)`).

---

## Final verdict on "P6 CLOSED as an equivalence"

**ACCEPTED, conditional on three mandatory fixes and the amendments listed.**

Mandatory (false or unsupported `PROVED` text):
1. **Thm 4.2(i)**: replace "holds for `T ≤ log 2`" by "holds for `T < ½ log 2`"; add the DIAGNOSTIC note
 `T*_{∞,P} ≤ 0.5958`. (Nothing downstream uses the positive clause.)
2. **Prop 2.3(v)**: replace the negative replacement `σ₊ ↦ 0 off the band` (invalid: `σ₊ ≠ 0` on the band)
 by `σ ↦ σ − c·1_{|τ|>τ_*}`, `c > sup σ₊/(1−λ₀(Tτ_*))`.
3. **Prop 1.1(iii)**: add `v ≥ 0` (or `Σ|v_n|`), since `thm:SC` is stated for nonnegative weights.

Amendments (citation exactness / sharpening):
4. Thm 3.1(b): `thm:O` is stated for `λ^P`; write and prove the complete-form non-attainment (Lemma 3.1b,
 one paragraph, same proof) and then record the exact per-window equivalence
 `[∃w ∈ 𝒲_T: X_T(w)] ⟺ λ^W_T > 0` — this is the sharpest true form of P6's "X" and is currently missing.
5. Thm 3.1(c), Prop 4.1: quantify over `T ≥ ½ log 2` where `cor:RH`/`thm:Zexh` are stated.
6. Lemma 3.0: define `τ_env(w)` as the root of `m_lo − A_T − ‖ν_w‖_TV − 2k₀ = 0`; drop or correct the
 inequality `τ_env(w) ≥ 2πe^{A_T}`.
7. Rem 3.1a(iii): add "for `w ∈ 𝒲_T^{reg}`" (`thm:Z`(ii)).
8. §5 table: witnesses "PROVED modulo double-precision evaluation".
9. Prop 4.6: label the "minimal hypothesis" sentence HEURISTIC.
10. Rename `X_T`.

With these, the closing sentence of the memo is correct as mathematics: the equivalence chain
`∀T D_T ⟹ RH ⟹ ∀T λ^W_T > 0 ⟹ ∀T ∃w X_T(w) ⟹ ∀T D_T` is on record (`main.tex:137–142, 1167–1182,
1137–1141, 1091–1095`), the per-window quantity is `𝔈_T = −λ^W_T`, the per-window converse
`λ^A_T ≥ 0 ⟹ λ^W_T ≥ 0` is genuinely not on record, and the "void per window" is a method constraint of the
Paper 46 Thm 18.1 type, not a statement about ζ. No sign for ζ beyond `log 2` is claimed anywhere in the
memo (checked). Row-D label unchanged.

## What may enter Paper 47 §9 (after the fixes)

- **§9.x "Row D at a window is a finite condition."** Prop 1.1 (with `v ≥ 0` in (iii)), Cor 1.2, Prop 1.3.
 PROVED.
- **§9.x "The negative set of the symbol."** Prop 2.1 (with `τ₁` as the exact envelope zero, resolving
 memo item 6 against `prop:env`(iii) at line 1041), Prop 2.2 (Diophantine bracket `|k log 3 − l log 2| <
 log 6/4`, arc counts `6 / 12`), the two floating-point witnesses bracketing `τ_*` in `[45.642, 60.544]` and
 `[108.723, 120.087]`. Table 2.2a and the convergent observation as DIAGNOSTIC.
- **§9.x "The negative part is trace class."** Prop 2.3(i)–(iv) and the corrected (v). PROVED; the trace
 values DIAGNOSTIC.
- **§9.x "The alignment inequality and its exact strength."** Lemma 3.0 (with the definite `τ_env(w)`),
 Thm 3.1(a),(c), the new Lemma 3.1b (complete-form non-attainment) and the per-window equivalence
 `∃w X_T(w) ⟺ λ^W_T > 0`, Prop 4.1 (`𝔈_T`, `RH ⟺ lim λ^W_T ≥ 0`). The OPEN per-window converse should be
 stated as OPEN in the text. Thm 3.2 as a remark citing Paper 46 Thm 27.10/Cor 27.10a.
- **§9.x "Finite modifications" (METHOD-CONSTRAINT).** Thm 4.2 (fixed (i)), Lemma 4.2b, Prop 4.3, Cor 4.4,
 Rem 4.5 (citation), Prop 4.6(a),(b).
- **Not for the paper:** the HEURISTIC readings (Zhu's law limit, mode count `≈ 20`, "the new atoms are what
 can defeat this test", the "minimal hypothesis is `D_T` itself" sentence, the last sentence of Prop 4.6).

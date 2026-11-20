# ROUND 024 C — The three cheap checks left by the row D triage

Question: run the three checks that `TRIAGE_D_1…5` and the entry `212-triage-D` (Part V of the index) left
as "decide something": (a) `n_− ≤ 2` of D.53 (6.7) against Thm P and P47 thm:J / cor:nasym; (b) `n_odd(0.80)`; (c) Fejér
means of CA_E_001 Cor 1.1. No paper and not the index is touched.

## 0. Files opened

Opened: `TRIAGE_D_1.md` (item 38, §3), `TRIAGE_D_3.md` (item 111, §3), `TRIAGE_D_4.md` (item 150, §3);
`phase-114-closing-the-four-rows/114_d_53_…GATE.md` §§1–7; P47 `main.tex` §"Bounds on the negative index"
(thm:index l.2518, cor:P3 l.2662, thm:J l.2694, cor:nasym l.2722; parity l.2420–2434);
`phase-155…/R155_052_ROUND8A_INDEX_MULTIBAND.md` (summary and Thm 5.x), scripts `scripts/r8a/r8a_01_upper.py`, `r8a_lib.py`
and the archived JSON `r8a_01_0p80_par1_K30_K244_c24.json`; `phase-193…/CA_E_001_COMMUTATIVE_COLLAPSE.md` §§0–4,
`CA_E_001_REVIEW.md` (header); master index: entries 212-triage-D, 212-20-A and rows l.3688, l.5150.
Not opened: D.52 (only the citation made by D.53 is used), R155_047/048, BRIEF_CONSTRUCTOR and RULES_AVOID (there is no
construction in this memo), P48.

## (a) D.53 (6.7) against Thm P, thm:J, cor:nasym

**What each statement says (read against the definitions).**
- P47 thm:index (PROVED, certified): for the **archimedean form alone** `A_∞ = 𝔪_T` on `P_T`,
  `n_ev, n_odd ≤ 1` on `(0, 0.90]`; `n_−(A_∞|P_T) = 0/1/2` according to `T` relative to `T*_ev ∈ [0.58,0.60]`,
  `T*_odd ∈ [log 2, 0.81]`.
- P47 cor:P3 ("Thm P"; PROVED): **same form** `A_∞|P_T` and also `𝔪_T` on `L²(I_T)`:
  `n_− ≤ 5` at `T=½log3`, `≤ 7` at `log 2`, `≤ 8` at `0.80` (prolate bound, weaker than thm:index in that range).
- P47 thm:J (PROVED): lower bound `n_−(A_∞|P_T) ≥ ⌈2Tτ_0/π⌉ − 3`, vacuous up to `T ≈ 0.75` and `≥ 3` from
  `2Tτ_0/π > 5`, i.e. `T > 1.249`. cor:nasym (PROVED): `n_−(A_∞|P_T) ~ 4.004·T`, `T → ∞`.
- D.53 (6.1)–(6.7): `A_T = K_{g,T}` on `H_T^0` (mass zero) where, by (1.1)–(1.2), `K_g` is the **complete** kernel
  (Gamma plus all the prime-power hinges `a = k log p ≤ 2T`), in the pullback by derivatives:
  `−B_T(F,F) = ⟨K_{g,T}F′, F′⟩`. `N_T` are the moments `e^{±t/2}`, so `ker N_T` corresponds to `P_T`. (6.7) asks for
  `n_−(A_{T,P}) ≤ 2` for every partition and equality of indices with `𝒢_{T,P}`.

**Result.** The statements are **compatible and do not touch each other**: thm:index, cor:P3, thm:J and cor:nasym count
negative directions of the archimedean part alone; (6.7) bounds those of the complete kernel with the comb. No bound
on Arch falsifies or proves (6.7), except in the prime-free stretch `2T < log 2` (`T < 0.3466`), where the kernel of D.53 is
only the Gamma term: there thm:index gives index `0` on `P_T` (`T < 0.58`), consistent with (6.7).
Label: **PROVED** (reading of statements) for "there is no contradiction and no falsifier available"; the
identification of signs `n_−(A_T)` ↔ negative directions of the complete form on `H^1_0` is **ARGUED** (depends on the
convention of D.52, not opened).
- Growth consequence: cor:nasym forces that, if (6.7) holds for `T > 1.25`, the prime comb has
  eliminated at least `⌈2Tτ_0/π⌉ − 5` of the negative directions of Arch on `P_T` (at most 2 are gained when passing from
  `P_T` to `H_T^0`). This is the same observation as 212-20-A, now applied to (6.7): it is not a falsifier.
- What would truly decide (6.7): only a computation of the cell matrix **with the comb** at fixed `T` and `n_− ≥ 3`. That
  computation is not "cheap" in the triage sense (exact values of Λ, certified bounds on the complete kernel) and was
  not run. Label of (6.7): **OPEN**.

**Corrections to the index/triage.**
1. `TRIAGE_D_1.md` l.88: the condition "if Thm P is about the same operator A_T restricted to mass zero, item 38
   becomes CLOSED" is resolved negatively: **it is not the same operator** (Arch alone vs complete kernel). Item 38 stays REF.
2. Index, entry 212-triage-D, bullet "Computations that decide something": remove "cross-check first with Theorem P, “count
   5 at log 2”"; replace with "Thm P / thm:J / cor:nasym are about Arch and do not decide (6.7)".
3. Index l.5150 ("DEAD [count 5 at log 2]") and l.3688 ("n₋ ≤ 5/6/7 (5/7/8 series)"): according to P47 cor:P3 the bound is
   `5` at `½log3`, `7` at `log 2`, `8` at `0.80`. "5 at log 2" and "5/6/7" are transcription discrepancies.

## (b) `n_odd(0.80)`

**What it decides.** By strict monotonicity of `λ_odd` (P47 thm:index / R155_052 Lemma 4.3) and `T*_odd ∈ [log 2, 0.81]`:
`n_odd(0.80) = 0` ⟺ `T*_odd > 0.80` ⟺ (H1) holds at `0.80`. It is a datum of the archimedean side; it does not decide the sign of `a_T`.
Prior state: P47 thm:index fixes only `n_odd(0.80) ≤ 1` (l.2532, 2552); R155_052 point 5: OPEN, second eigenvalue
of the certifying matrix `−0.0047` (default `τ_N`), `−0.0019` (`τ_N = 30`); heuristic extrapolation `τ_N ≈ 60`.

**Execution.** Recorded script `r8a_01_upper.py` unmodified, copied to
a temporary directory
(mpmath interval arithmetic, 40 digits). Runs at `T = 0.80`, odd sector:
| K, K2, target c_N | τ_N | result | 2nd eigenvalue (midpoint) |
|---|---|---|---|
| 30, 44, 40 | — | fails `γ > 0` (K insufficient) | — |
| 44, 60, 40 | 50 | certified bound `≤ 1`, margin `0.1644` | `−0.000299` |
| 56, 76, 60 | — | library failure ("series did not converge; enlarge KM") | — |
Output: `r8a_run/r8a_01_0p80_par1_K44_K260_c40.json` and the `.log` files in the same folder.

**Result.** `n_odd(0.80) ≤ 1` re-certified (**PROVED**, already in P47); `n_odd(0.80) = 0` remains **OPEN**.
The series `−0.0047 → −0.0019 → −0.0003` as `τ_N` grows is compatible with the residue being fixed by the constant minorant
beyond `τ_N` and with certifying `0` at somewhat larger `τ_N` (**NUMERICAL**, diagnostic). Going further requires enlarging `KM`
in `r8a_lib.moments`, i.e. modifying the recorded script; this was not done.
Correction: none in the index (item 111 already said "decides something local"); add to item 111 of `TRIAGE_D_3.md` and to
the entry 212-triage-D the datum `τ_N = 50: −0.0003, still ≤ 1`.

## (c) Fejér means of CA_E_001 Cor 1.1 outside `ι(ℝ)`

**What the triage claims** (`TRIAGE_D_4.md` item 150, l.40 and l.66): a negative outside `ι(ℝ)` would show that
(eq:target) is stronger than positivity on `P_T` and would falsify that reformulation.

**Result (PROVED, without computation).** At fixed `S` and `N` the Fejér mean
`Φ_{S,N}(y) = Σ_{q∈G_S, |v_p(q)|<N} φ(q) \overline{y(q)} Π_p(1−|v_p(q)|/N)` is a finite sum, hence continuous in
`y ∈ Ĝ`, and depends only on the projection `y|_{G_S} ∈ 𝕋^S`. The `log p`, `p ∈ S`, are ℚ-linearly independent, so
`τ ↦ (p^{iτ})_{p∈S}` has dense image in `𝕋^S` (Kronecker). Therefore
`inf_{y∈Ĝ} Φ_{S,N}(y) = inf_{τ∈ℝ} Φ_{S,N}(ι(τ))`. A point "off the line" never gives a value not already
approximated by points of the line: the search outside `ι(ℝ)` **decides nothing new**. The on-line/off-line distinction
exists only in the full `Ĝ` (Lemma 1, support of `μ_φ`), not at finite level.
Moreover, by Cor 1.1 itself a negative at any `y` would falsify (eq:target) entirely, which by thm:oneprofile /
prop:AM(i) is a consequence of positivity on the `P_T` of every `T` (not a "stronger" form of it):
the triage reading is inverted (**ARGUED** as to the exact direction of thm:oneprofile, not reopened here).
Label of item 150: **NO-GO** as a check that decides something; the boxes on the line are the twisted `s_w` family
already used (CA_E_001 Cor 1.1, last sentence).
Corrections: `TRIAGE_D_4.md` item 150 (l.40, l.66) goes from "LOCAL/NUMERICAL — decides something" to "does not decide: equivalent by
density to the line"; remove "Fejér means outside ι(ℝ)" from the bullet "Computations that decide something" of 212-triage-D.

## Summary
| item | result | label | correction |
|---|---|---|---|
| (a) 38 | compatible; Thm P/J/nasym are about Arch, (6.7) about the complete kernel; nothing falsifies it | PROVED (reading); (6.7) OPEN | TRIAGE_D_1 l.88; 212-triage-D; index l.3688, l.5150 (5/7/8) |
| (b) 111 | `≤ 1` re-certified; `= 0` not reached (−0.0003 at τ_N=50) | PROVED ≤1; OPEN =0; NUMERICAL trend | add datum to item 111 / 212-triage-D |
| (c) 150 | outside ι(ℝ) ≡ on ι(ℝ) by density at finite S | PROVED; item NO-GO | TRIAGE_D_4 item 150; 212-triage-D |
None of the three touches the sign of `a_T`.

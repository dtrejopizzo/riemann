# R155.028 — Audit of R155_026 (round 3c: Schur reduction + enclosure at `log 2`)

*Reruns: `r3c_02_enclosure.py` (11.1 s here), `r3c_03_parity.py` (6.0 s). `r3c_01` not rerun
(99 s), audited from `r3c_01.json`. Verdict: **the mathematics and the enclosure stand**; three defects,
all in the prose/bookkeeping, none in Theorem 3c.3.*

## §1 Verdicts

| item | verdict |
|---|---|
| Prop. 3c.1 (★), (i)(⟹), (ii), (iii) caveat | **CORRECT**, `PROVED`. The correction of the earlier decision's "⟺" (only `w₁₁ ≥ 0`, plus the `w₁₁ = 0` ⇒ `β ≡ 0` case) is right. |
| Prop. 3c.1(i), coercive half "`w ≥ c‖·‖² ⟸ s ≥ c′‖·‖²`" | **OVERSTATED** (`R155_026:108-109`). `⟹` is fine (`x = −β/w₁₁`); `⟸` needs `β` bounded (`\|β(G)\| ≤ C‖G‖`), which holds under Cor. 3c.2 but not for a general form. Fix: restrict to `⟹`, or add "`β` bounded". |
| Cor. 3c.2 (congruence `LWL* = w₁₁ ⊕ S`) | **CORRECT** under `F* ∈ D(W)`; `⟨b,F*⟩ = 0` ⇒ `L^{-1}` as stated; signs preserved, eigenvalues not. |
| **THEOREM 3c.3** `W_{log2}[F*] ∈ [0.0341712660, 0.0342537492]` | **REPRODUCED EXACTLY** (rerun output identical to `r3c_02.json`, `I ∈ [3.1919548566, 3.1920373379]`). `PROVED` modulo float rounding — see §2. |
| Parity: `W_T` `R`-invariant on `P_T` (`R` swaps `A`,`B`; `c_F` `R`-invariant) | **CORRECT**, `PROVED`. `F*` even, parities `(+,−,+,−,+)` reproduced; cross terms `1.26e−15`. |
| §5 crude conditions, `λ₃ − c²/w₁₁ = −0.0639,−0.1008,−0.1540,−0.3099` | **REPRODUCED** from `r3c_04.json` (`crude_even_nofaults`); recomputed by hand from `λ₃`, `c`, `w₁₁` to 3e−4. |
| Sign consistency `sign λ_min(S) = sign λ_min(W_T\|P_T)` at 8 runs, ratios `6.5/4.2/3.4/2.7` | **REPRODUCED** from `r3c_01.json`. |
| `w₁₁` four windows, `N = 18/36` stability `2.7e−4 … 4.1e−3`; ratio `10³–10⁵` over `λ_min(W\|P_T)` | **REPRODUCED**. `(H1)` fails at `0.58` (`λ₁ = +0.02739 > 0`) — consistent with `T*_{∞,P} = 0.5958` (`R155_023:189`). |
| Labels (`PROVED`/`HYPOTHESIS`/`DIAGNOSTIC`), §6, and the "one direction, not the form" scope | **CORRECT and sufficient**. No sign for `ζ`, endpoint unchanged. |

## §2 Is the enclosure rigorous? (audit of `r3c_02_enclosure.py`)

Rigorous in structure, *not* interval arithmetic. Step by step:
- (a) `c` polynomial of degree `≤ 35` on `[0,2T]`: **correct** (`c(u)=∫_{−T+u}^{T}F(t)F(t−u)dt`, affine limits, integrand degree 34). 80-node Gauss is exact to degree 159 ✓. Chebyshev degree `2N+2 = 38 ≥ 35` ⇒ interpolation is **exact**, so `G₁ = Σ|cheb-deriv coeffs| = 6.8554` is a genuine `sup|g′|`. The residual `2.5e−15` is used only as a check (`assert`), as the note claims ✓.
- (b) `g ≥ 0` by Cauchy–Schwarz ✓; `g(0)=g′(0)=0` (c even) so `g = O(u²)` — the note only uses the weaker `g ≤ G₁u`, which is fine and conservative. `K ≤ 1/u + 1/2` ✓ (`sinh x ≥ x`; `½/cosh ≤ ½`). `∫_0^δ gK ≤ G₁(δ+δ²/4)`, `δ = 1e−7` ✓; the lower bound simply omits `[0,δ]` (legitimate, integrand `≥ 0`).
- (c) Panels: `K` decreasing ⇒ `K ∈ [K(β),K(α)]`; `g ∈ gmid ± G₁h/2` by the mean value theorem — **`g` need not be monotone and is not used to be**. So the panel bound is a valid enclosure. `3e6` geometric panels, `np.sum` (pairwise) ⇒ rounding `~1e−14`.
- (d) `∫_{2T}^∞K = log coth(T/2) + π − 2arctan e^T` — **verified analytically** (`∫ds/sinh s = log tanh(s/2)`, `∫ds/cosh s = 2arctan e^s`); `arch_core.py:18-20` implements it correctly at `x = 2T`.
- (e) Atoms: loop keeps `n` with `log n < 2T` strictly ⇒ `contacts = [2,3]` ✓ (`log 4 = 2T` excluded, and `c(2T)=0` anyway ✓); `Λ(4) = log 2` is correctly coded should it ever enter.
- (f) Pole defect: **not assumed zero** — `|2A B| ≤ 2|A||B| + 1e−12` is subtracted from the lower and added to the upper bound (`r3c_02_enclosure.py:73-75`) ✓. `A,B ≈ 3e−16`, so the `1e−12` guard dominates. Caveat: `A,B` come from 400-node Gauss on `F·e^{±t/2}` (non-polynomial) — error is `≪1e−12` but is not certified.

**Only non-rigorous element: floating point.** `EPS = 1e−9` is an *error budget*, not directed rounding or interval arithmetic. Estimated true rounding error `≲1e−13`, so the budget is ~4 orders generous and the margin to `0` is `3.4e−2` = `3.4e7 × EPS`. **Cheap hardening** (≈1 h): recompute the panel sum and the finite terms with `mpmath` at 30 digits (or `flint`/`arb` intervals) on a coarser panel grid (`3e4` panels suffice for width `1e−2`, still far from `0`), and replace `EPS` by a proved bound. Recommended before print.

**Reproducibility defect** (`r3c_02_enclosure.py:16-20`): the script *recomputes* `coef` from `arch_core` instead of loading the archived vector in `r3c_02.json`. The theorem is stated about the archived `a`, so the script should read it back and `assert` agreement (or just load it). One-line fix.

## §3 Errors found (file:line)

1. `R155_026:44` and `:266-267` — "**99.7 % of its mass**" / "92.4 % at 0.58" are **amplitudes, not masses**. From `r3c_01.json`: overlaps `0.9973` (`log 2`) and `0.9243` (`0.58`) ⇒ masses **99.46 %** and **85.43 %** (rest: `0.41 %`/`13.08 %` on the fifth eigenvector). Fix the wording or the numbers.
2. `R155_026:57` — corpus row "`Schur` | **2 documents only**" is **false**. `grep -rl "Schur complement" 03-research --include=*.md` returns **177 files** (654 for "Schur"). Materially, `phase-116/previous-phase-114/114_d_56_PARITY_FESHBACH_INERTIA_CERTIFICATE...` already combines **parity splitting + Feshbach (= Schur) elimination with interval enclosures** (see its lines 6, 17, 37, 164, 242), and `114_d_49_LEVY_GROUND_STATE_JET_DEFECT` is about the Lévy ground state. This is the closest prior art to §2 and §5(b) and is **not cited**. The novelty claim ("no overlap") must be re-argued against D.49/D.55/D.56, not against `P124_011` alone.
3. `R155_026:108-109` — the coercive "iff" of Prop. 3c.1(i), see §1.

Not errors: the "`⟺`" correction, the `n = 4` edge case, the `A_T = 2.24883` bound, the `(H1)` labelling, the `T = 0.58` caveat.

## §4 Readiness for Paper 47

- **Prop. 3c.1 + Cor. 3c.2 → §8: READY**, after (i) restricting the coercive clause to `⟹` (or adding "`β` bounded"), and (ii) a one-line attribution remark citing `114_d_56` (parity/Feshbach) and `P124_011`, so the paper does not claim a first.
- **Theorem 3c.3 → §5/§8 remark: READY IN SUBSTANCE, NOT IN FORM.** Publish only after the `mpmath`/`arb` hardening of §2 and the load-the-archived-`a` fix. Exact permissible wording:
 > *For the explicit degree-17 polynomial `F*` on `(−log 2, log 2)` with the coefficient vector archived in `scripts/r3c/r3c_02.json`, a two-sided machine enclosure of every term of the Lévy form gives `W_{log 2}[F*] ∈ [0.0341712660, 0.0342537492]`; in particular `W_{log 2}[F*] > 0`. This is a statement about one explicit direction; it is not a positivity statement for `W_{log 2}`, and it does not affect the endpoint of record `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`.*
 The note's §4 scope paragraph must travel with it. Do **not** write "the ground state" (that is (H1) + Galerkin convergence, neither proved) — write "the archived direction `F*`".
- **§7.3 (even-sector obstruction, `c²/w₁₁ > λ₃`): READY as an explicitly `DIAGNOSTIC` paragraph** (Galerkin, `N = 18`, upper bounds on infima); it must not be phrased as an obstruction theorem.
- **§3/§5 tables: NOT for print** — `DIAGNOSTIC` only, keep in the repository.

# Round 13 A — Small-scale reverse engineering: the window ½log 4 < T < ½log 5

Idea examined: in the window `½log 4 < T < ½log 5` the contacts are `n = 2, 3, 4`; the form with weight `cΛ` is
positive only in a narrow band of `c` around 1; look for the *reason* (exact identity
«`a_T` = manifestly nonnegative expression») that uses `c = 1`, `Λ(4) = Λ(2)`, `log 4 = 2 log 2` and
`Σ_{d|n}Λ(d) = log n` for `n ≤ 4`, with a form that can be stated for all `T`.

Verdict: **REPETITION**. Stopped before deriving. Below, the cross-check and the only new observation (a
selection observation, not a sign one).

## 1. Primary-source cross-check: what is in the window and what is a mechanism

| Piece | File / section | Type | Where it stops |
|---|---|---|---|
| `thm:log5A`, `thm:log5W` (positivity up to `½log 5`) | Paper 47 `main.tex` l. 4680–4710; appendix `subsec:encllog5` | **certificate** (ball arithmetic, `prop:lowercert`, `thm:parityschur`) | explains nothing; bound `2.5·10⁻¹²` |
| `thm:C` (explicit certificate, `½log 3`) and Theorem C of phase 154 | Paper 47 `thm:C`; phase 154 | certificate; «primitive form only» (phase 155, round 5) | first contact |
| Theorem A of phase 153 (`({∞,2,3}, log 2)`) | phase 153 | partial mechanism (Lévy energy, `thm:A`) | `T ≤ log 2`, without `n = 4` |
| `prop:align` (alignment structure with 2 and 3 contacts; with 4: `g(x) = v_2 cos x + v_4 cos 2x`, root `y_0`) | Paper 47 `main_pre_cite46.tex` l. 2896 | **localization mechanism** of the set `{σ < 0}` (uses `log 4 = 2 log 2`) | localizes the negative part; gives no sign (`prop:negtrace`: «the band does not decide») |
| Nodal explanation of the 2/3 cancellation | phase 155 round 5 | structural reading | no inequality |
| Schur reduction, `S_{T,k}` (`λ_A > 0 ⟺ S_{T,k} ≻ 0`) | Paper 47 l. 211; phase 186 R186_025/105 | exact reduction to finite dimension | the sign of `S_{T,k}` is a certificate |
| Per-prime split of round 6 (projected rank-one square `ℓ ≈ cos(2πt/log 2)`) | `ROUND_006_WINDOW_SPLIT_NUMERIC.md`; RULES_AVOID O1–O4 | NUMERICAL; dies at `T = 0.70` | generic in `c` up to 0.69 |
| Band in `c`, concavity, strict `c* < 1`, derivative `−Π(F*)` | `ROUND_006…` §10.3–10.4; 211 `ROUND_003_A.md` Prop. 2; RULES_AVOID P1 | PROVED structural | no sign |
| Weyl pin: `|1 − c*| ≤ (Λ_2 − λ_A)/min|μ_±|` | 211 `ROUND_003_A.md` Lemma 3 (instance at `½log 5 + 10⁻³`: `2·10⁻⁶`) | PROVED structural | inputs (P1)–(P2) as strong as the sign |
| **Identity `Λ∗1 = log` in the cell**: `P_w𝔇_R = [M_x, 𝔇_R] ⟺ w ≡ 1` on prime powers `< R`; `Q_R^{(c)} = Q₀ − c𝒦_R` with `Q₀, 𝒦_R` free of `Λ` | 211 `ROUND_021_A.md` Prop. 3.2 | PROVED | the requested window is exactly `R = 5`; the mechanism survives Beurling (§3.4(ii)(c)) |
| Sandwich: width of the band in `c` ≍ bottom `λ₀` | 211 `ROUND_021_A.md` Lemma 3.3 | PROVED | the band *is* the margin in another variable |
| Requested checks (only `n = 2`, powers of 2 — includes `Λ(4)` —, powers of 3, deletions `a_3`, `a_5`) | 211 `ROUND_021_A.md` §2.3, row `R = 5` | NUMERICAL | already measured |

## 2. Four-point filter (strict)

1. **Closest antecedent.** 211 `ROUND_021_A.md` Prop. 3.2 + Lemma 3.3 at `R = 5`, with 211 `ROUND_003_A.md`
   Prop. 2 and Lemma 3. Both read in primary sources.
2. **New object.** None. Each sub-question of the brief has a recorded answer:
   - *what degenerates at `c*`*: Danskin, `0 ∈ conv Π(E_T)` at the bottom of `a_T^{(c*)}` (003_A Prop. 2); it is a
     codimension-one tangency, not a missing square;
   - *why `c* → 1`*: Weyl pin (003_A Lemma 3) and sandwich (021_A Lemma 3.3): `|1 − c*|` and the width of the
     band are the margin up to constants;
   - *role of `Λ(4) = Λ(2)`, `log 4 = 2 log 2`, `Σ_{d|n}Λ(d) = log n` for `n ≤ 4`*: it is exactly Prop. 3.2 at
     `R = 5`; its effect is to **eliminate** `Λ` from the form, not to produce a sign, and it holds for every generalized
     integer system with its own `Λ_N`;
   - *checks*: 021_A §2.3.
3. **Why it would avoid the difficulty.** It does not: the recorded difficulty (021_A §3.4(i)) is that after using the
   identity no remainder is left; the sign is that of `Q₀ − 𝒦_R` on `V_R`, with bottom `≈ 6·10⁻⁹` at `R = 5`. A «structural
   proof in the window» has to prove that bottom, i.e. a finite-order certificate (accumulating is forbidden)
   or a mechanism for `Q₀ − 𝒦_R` that nobody has given.
4. **Connection with global positivity.** None stated: the «for all `T`» version of the identity is
   Prop. 3.2 for all `R`, already recorded and blind to Beurling.

RULES_AVOID patterns: P1 (almost-null subspace and tangency), S2 (a step that uses only divisors does not fail under
Beurling), B3/B9. Stopped here.

## 3. Selection observation (the only thing this round adds)

**Lemma S (PROVED, from 021_A Lemma 1.1 and Lemma 3.3).** Let `T` be in the window and `λ₀ > 0` the bottom of the form
of the cell with `c = 1`. Then the set `J` of `c` with form `⪰ 0` is a closed interval containing
`[1 − λ₀/‖𝒦‖, 1 + λ₀/‖𝒦‖]`. *Proof:* Lemma 3.3, lower bound. ∎

**Consequence (PROVED).** The premise «every structural proof is forced to use the exact value `c = 1`» is false
in the strict sense: positivity at `c = 1` implies positivity in an open neighbourhood of 1, and moreover the maximum of the
bottom is at strict `c* < 1` (003_A Prop. 2 with `Π(e) > 0`, NUMERICAL in the sign of `Π(e)`). No qualitative
property of the form distinguishes `c = 1` from neighbouring `c`; what is required is *quantitative precision*
`|c − 1| ≲ λ₀`, i.e. the margin. Hence an identity «form = SOS» that breaks exactly at `c ≠ 1`
(automatic case of R3-i) cannot be the reason for the sign; at most a rewriting in which the remainder keeps
a margin `≍ λ₀`.

**Consequence for the idea (ARGUED).** The sought «small-scale reason» is, in this window, the sign of the
`Λ`-free form `Q₀ − 𝒦_5`; a mechanism for it would have to use something of `ℕ` that Beurling does not have (the additive
structure of `{1,2,3,4}`: `4 = 2·2 = 1 + 3`, `3 = 1 + 2`) and not only Dirichlet convolution. This is the
already recorded requirement S2; there is no new explicit operation.

## 4. Result

- Verdict: **REPETITION** of 211 `ROUND_021_A.md` (Prop. 3.2, Lemma 3.3, §2.3 at `R = 5`) and 211 `ROUND_003_A.md`
  (Prop. 2, Lemmas 3–4); positivity in the window is a certificate (`thm:log5A`), not a mechanism.
- PROVED: Lemma S and its consequence (`c = 1` is not qualitatively distinguished; only quantitatively, by the
  margin). Everything else is CITED from the antecedents.
- ARGUED: that the only possible «reason» in the window is a mechanism for `Q₀ − 𝒦_5` coupling the additive
  structure of `{1,…,4}`.
- Nothing was built; no computation was done.
- Next explicit operation: none defensible from this idea. The pending step of 021_A («compare the
  almost-null direction of `Q₀ − 𝒦_R` with the preimage under `𝔇_R` of the bottom of the window form») is structural and
  blind to Beurling; it does not enable construction without a named additive ingredient.

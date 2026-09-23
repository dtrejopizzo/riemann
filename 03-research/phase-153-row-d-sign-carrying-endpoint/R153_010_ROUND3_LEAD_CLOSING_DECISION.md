# R153.010 — Lead closing decision, round 3 of phase 153 (tracks (P153.5) single pair and (P153.4) needle)

*Lead of record: Fable 5.1. Date 2026-09-19. Inputs: R153_006 (blueprint), R153_007 (track 1), R153_008 (track 2),
R153_009 (hostile audit). Scripts `scripts/round3/`.*

## 1. Verdicts of record

| item | statement | label |
|---|---|---|
| T1.1 divisor sum | `⟨A_T F,F⟩ = Σ_ρ F̂(ρ)F̂(1−ρ)` on `P_T`, `F̂(s) = ∫F(t)e^{(s−½)t}dt` (Paper 42 main.tex:1965) | `RESTATEMENT` |
| T1.2 / T1.4 / T1.5 | on-line pair contributes `2|F̂(½+iγ)|²`; quadruple `½±a±iγ_0` contributes `4 Re X = 4∫c_F(r)cosh(ar)cos(γ_0 r)dr`; sharp growth constant `cosh(2aT)`. Blueprint's coefficient 2 and `e^{2aT}` corrected. | `PROVED` |
| The form `Q_T` | `Q_T = A_T − C`, `⟨CF,F⟩ = 4 Re X`. Under H(a,γ_0) ("a quadruple at `½±a±iγ_0` and every other zero on the line"), `⟨Q_T F,F⟩ = Σ_{other}|F̂(½+iγ)|² ≥ 0`; hence `λ_min(Q_T) < 0` refutes H(a,γ_0). The blueprint's `B_T = A_T + R_T` is a different (and never negative) object; the paradox at `a = 0` dissolves: `T*(0,γ_1) = 0.234` refutes a **double** zero at `γ_1`. | `PROVED` (logic); builder's stated reason for rejecting `B_T` `WITHDRAWN` |
| T1.6 conditional exclusion | holds for all `T`, is non-circular, and does not need Paper 42; but H(a,γ_0) is already false for all `γ_0 ≤ 3·10¹²` (Platt–Trudgian), so it carries **zero new content** about ζ. FATAL rule passed. | `PROVED`, empty |
| `T*(a,γ_0)` | Weil-mass **concentration** threshold, not an off-lineness detection law: `a`-independent for small `T` (`cosh(2aT) ≤ 1.03`), `a`-dependent at `T ≈ 0.79` (`γ_100`: 0.793/0.781/0.768 for `a = 0/0.30/0.45`). Table in R153_007 §3. | `DIAGNOSTIC-NUMERIC`, relabelled |
| `γ_0^max(log 2) ≈ 201` | **does not exist**: `λ_min(Q_{log 2})` is not monotone in `γ_0` (negative at 120, 189, 190, 199, 200; positive `≈ +10⁻⁷` at 150, 170, 180, 191–198, 201–212, 250–262, 300–312, 400–412, 700). The excluded set is a union of narrow `γ_0`-windows with no established upper bound. | `REFUTED` (cut-off); exclusions themselves `DIAGNOSTIC-NUMERIC` |
| (P153.5) verdict | **answered negatively**: the single-pair perturbation of `A_T` does not give a detection law for off-lineness of ζ's zeros at short support | `CLOSED (negative)` |
| Track 2: parity | `A_T(b)` commutes with `t ↦ −t`; `λ_min = min(λ_even, λ_odd)`; Hellmann–Feynman `dλ/db = −2w_3 c'_{F_b}(b)`; slopes verified (`+0.28` even, `−0.58` odd) | `PROVED` (elementary) |
| The needle | an exact even/odd eigenvalue crossing near criticality (gap `≲ 10⁻¹³`), a corner with `O(1)` slopes; positivity interval `≈ (log 3 − 4·10⁻⁷, log 3 + 2.0·10⁻⁵)`; `argmax = log 3 + 1.39·10⁻⁵` (K = 240; quadrature error `5·10⁻¹⁰`, basis `4·10⁻⁷`); drifts with `T` (`+3.1·10⁻⁵` at 0.68, `+5.8·10⁻⁶` at 0.700, `−1.5·10⁻⁶` at 0.704), crossing `log 3` at `T_c = 0.703 ± 0.001`, arithmetically meaningless | `DIAGNOSTIC-NUMERIC` |
| (P153.4) verdict | the needle follows `T`, not `log 3`; arithmetic enters only through the weight `w_3`, which sets the slopes | `CLOSED (negative)`; (P153.4′) theorem candidate `OPEN` (needs sign of `c'_{F_b}(b)` per parity) |
| `λ_min(A_{log 2}) ≈ 9.9·10⁻⁸` vs `8.63·10⁻⁸` | comparison illegitimate: `8.63·10⁻⁸` is a Feshbach capacity margin, not an L² bound (R153_004 item 23) | `REFUTED` (comparison) |

## 2. Amendments to R153_005 (of record, effective now)

* Row "`b`-scan": replace by — "`λ_min(b)` at `T = log 2` is a corner formed by an exact even/odd eigenvalue crossing near criticality; it is positive on an interval of length `≈ 2·10⁻⁵` whose location drifts with `T` and passes through `log 3` at `T_c ≈ 0.703`. No arithmetic significance. `DIAGNOSTIC-NUMERIC`."
* §2 item 4: delete "the `b`-needle says the two-prime form is positive essentially only at `b = log 3`" and "the critical point sits at the arithmetic contact". Keep: "`λ_min(A_{log 2}|P_T) ≲ 10⁻⁷`; the endpoint is critical." Add: "the obstruction to extending past `log 2` is expected first in the **odd** parity block; organise (P153.3) by parity."
* Open item (P153.5): closed negative (this document). (P153.4): closed negative; replaced by (P153.4′).
* New open items: (P153.6) Turán-type extremal problem `4Φ(T,γ_0) < 1` behind `Q_T`; (P153.10) characterise `{γ_0 : λ_min(Q_{log 2}) < 0}` (union of windows; is it related to the spacing of ζ's zeros near `γ_0`?). Both `OPEN`, low priority: no path to the sign.

## 3. Honest reading of round 3

Both creative leads of R153_005 §5 deflated under audit. The single-pair form is exact and its logic is sound, but at short support it measures concentration of Weil mass at one ordinate, not distance from the line, and everything it excludes about ζ is already excluded by computation. The needle is a parity crossing. Round 3 removed two false hopes and one false sentence from the record; it added no sign. What phase 153 leaves standing is rounds 1–2: Theorem A and the certified separation of `ζ` from `Ξ_a` at `({∞,2,3}, log 2)`.

## 4. Repairs to be written into R153_007/008 at the next pass (from R153_009)

Ten items listed in R153_009 §"Required repairs"; the substantive ones are recorded in §1–§2 above (Q_T reason, `γ_0^max` withdrawal, `T*` relabelling, error statement for the argmax, the capacity-margin comparison).

## 5. Decision

Round 3 closed. Phase 153 remains **closed** with the results of R153_005 as amended in §2. Row D label unchanged.

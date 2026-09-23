# R150.005 — Lead closing decision, phase 150 (method theorems T3, T4, T5)

*Lead: Fable 5.1, 2026-09-19. Record: `R150_000` (blueprint), `R150_001` (round 1), `R150_002` (hostile audit),
`R150_003` (repairs), `R150_004` (hostile confirmation).*

## 1. Verdicts of record

| item | label of record | basis |
|---|---|---|
| **T3** (Beurling: the additive structure of `Z` is necessary) | **CONDITIONAL META-THEOREM** relative to hypothesis **(H-DMV)**; **blocking open item O-150.1** (read Diamond–Montgomery–Vorhauer, Math. Ann. 334 (2006), and verify BE3/BE7) | `R150_002` §1 (continuation inference from `N(x)` error term is false); `R150_003` §2 |
| T3 novelty | axiom list BE1–BE8 only; the observation itself is already in `114_d_246` l.160–162 and `114_d_240` l.243–246 | verified by auditor and builder |
| Falsifier triangle | **WITHDRAWN** as "joint necessity"; replaced by Prop. 2.10′: three falsifiers kill three different conclusions (`Ξ_Q` → Hodge-index conclusion; `Ξ_a` → `Re ρ = ½`; `ζ_𝒫` → zero-free strip) | `R150_003` §2 |
| Prop. 2.6′ | **DOWNGRADE** from PROVED to OBSERVATION (completeness claim unproven; T3 needs only soundness) | `R150_004` |
| **T4** (smooth regime) | **DOWNGRADE**: Lemma 4.2′ (`|Σ_{N<n≤2N} n^{-iγ}| ≫ N/(1+|γ|)` for `|γ| ≤ N^{1/2−ε}`) PROVED; coefficient-blind floor holds for C4 only; C6, C7 OPEN; Thm 4.7 (multiplicative phase makes bilinear forms rank one) **WITHDRAWN** (Type II ranges are coupled; contradicted by Friedlander–Iwaniec / Heath-Brown); `𝒞`-completeness REFUTED as a curated list | `R150_002` §2, `R150_003` §4 |
| **Def. 4.11 / Thm 4.12 / Thm 4.13** (polar-at-zeros vs entire-at-zeros coefficient sequences) | **PROVED, CLASSICAL** (von Koch–Landau; folklore convolution trick). Thm 4.13 restricted: the trick can only *add* zeros, each with its `2π/log 2` progression | `R150_004` (b) |
| **T5** (no single-fibre extraction from Parseval-type moments) | **PROVED**, scope narrow: single-fibre extraction only; large-value counting (Halász–Montgomery, hybrid large sieve → zero density) untouched | `R150_002` §3, `R150_003` §5 |
| Cor. 5.5 | **WITHDRAWN** (exponent error) → Prop. 5.5′ | `R150_003` |
| Prop. 5.7 | **round-1 statement RESTORED**: `‖b*b‖₂² = E(b)` for every complex `b` (Parseval, both equal `∫|b̂|⁴`); the round-2 "correction" fixed a non-error (`R150_004` D-1). Archimedean half of the correction stands. | `R150_004` |
| Prop. 5.8 | ANALOGY (analytic face of phase-36 Prop. 3.9) | `R150_003` |
| FATAL rule | not triggered (three independent checks) | all |
| Gates `Ξ_a`, `Ξ_Q`, `ζ_K`, Beurling | complete; all three theorems field-uniform; two gate cells (⇐ half of Thm 4.12 for `ζ_𝒫`, `Ξ_Q`) need an explicit formula to be more than asserted | `R150_004` |

**Row D: no label. No sign claimed. No new zero-free region, moment bound or cancellation.**

## 2. What the phase actually produced

1. **The wall in one sentence, now a theorem-shaped statement (Thm 4.12, classical):** for a *polar-at-zeros*
   sequence (`Λ`, `μ`: Mellin transform `−ζ'/ζ`, `1/ζ`), a bound `ψ(x) − x ≪ x^{θ+ε}` for all `x` is equivalent to
   `β_max ≤ θ`; for an *entire-at-zeros* sequence (cusp-form coefficients: Mellin transform `L` itself), power
   saving in partial sums (Voronoi: `Σ λ_f(n) ≪ N^{1/3}`) carries **no** information on zeros (Thm 4.13). Every
   known smooth-regime power saving acts on the second class or consumes zero information (zero density, BHP,
   Guth–Maynard). This is the auditor's correction of the lead's §9.3: **the obstruction is the pole structure at
   the zeros, not the regime**. It sharpens NG-B1/MW-2 into a classification but is not new mathematics.
2. **T5**: Parseval-type moments never extract a single fibre beyond the trivial bound, uniformly in `k` and family
   type. Trivial, correct, and it closes the door on every "Deligne extraction over `Z`" that feeds on an
   `L²`-orthogonality (Farey, archimedean `t`, quadratic twists, characters mod `q`). Its productive complement
   (large-value counting → zero density) is exactly where unconditional progress lives (Guth–Maynard).
3. **T3**: reduced to bookkeeping until O-150.1 is done. The corpus already had the observation twice.

## 3. Decision

* Phase 150 **CLOSED**. Paper 46 §18: add T5 (short), add the polar/entire classification as a remark to §18.1
  with the label CLASSICAL, add T3 only as "Remark (conditional on H-DMV)" until O-150.1 is read.
* The lead's plan §9.4 (i) is done and returned less than hoped: one trivial theorem (T5), one classical
  classification, one conditional meta-theorem. **The three method theorems do not move the sign.** They sharpen
  the description of the wall: *the sign is a statement about partial sums of a polar-at-zeros sequence in the
  smooth regime, where no orthogonality-based family method extracts and no known cancellation mechanism acts.*
* Recommendation to the owner (unchanged from plan §9.4): close row D **in the map** with T1, T2, T5 and the
  classification of Thm 4.12/4.13 as the exact statement of the wall, and write Paper 46 Part IV (phases
  134–150); or open MW-5 (Connes–Consani square, Forma B) only with a concrete idea for the smooth/punctual part
  of the square. Extending the `log 2` certificate to `½ log 5` remains available as a computer-assisted theorem
  that measures, not moves, the wall.

## 4. Open list

* **O-150.1 (blocking for T3):** read DMV 2006; verify which of BE1–BE8 the constructed systems satisfy.
* O-150.2: C6, C7 (sieve/Selberg-type and spectral mechanisms) — do they have a coefficient-blind floor in the
  smooth regime? OPEN.
* O-150.3: explicit-formula gate cells for `ζ_𝒫` and `Ξ_Q` in Thm 4.12 (⇐ half).
* O-150.4: closed negatively (Voronoi acts on entire-at-zeros sequences).
* O-150.6: Heath-Brown's quadratic large sieve does **not** escape Def. 5.2 (auditor) — closed.
* Carried: O-149.1–O-149.5, O-148.2, O-47.7, O-47.8.

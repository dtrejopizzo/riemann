# R130.005 — Final audit (round 2) and the closure-rule decision

for phase 130.

## 1. What was re-checked after round 2

| item | result |
|---|---|
| Def 8A.7b0 / Thm 8A.7b(a),(a′) corrected norm `‖F‖_tr = Λ(F)+N(F)` | re-derived: `Λ(F⋆G) ≤ Λ(F)Λ(G)` because `|w|^{±1/2}` are characters; `N(F⋆G) ≤ ‖G‖_1 N(F) ≤ ½Λ(G)N(F)`; hence `‖F⋆G‖_tr ≤ Λ(G)‖F‖_tr ≤ ‖F‖_tr‖G‖_tr`. `|λ_∓(F)| ≤ Λ(F)`. The FATAL F1 is repaired. |
| Def 9.14c0, Thm 9.14c′ | correct; the admissible class is the right one (`‖F_α‖_1 → 0` is what "spread" means), and the `ψ`-family belongs to it. Rem 9.14c″ states exactly what is not claimed. |
| Thm 10.8b (Mertens) | Steps 0–3 re-derived (they are the review's own computation); Step 4 self-pairing bound checked; numerics `scripts/mertens_check.py` = 1.0000. Label `CLASSICAL`, quarantined, counts toward no clause — correct treatment under A.10. |
| Thm 8A.12 (`E_H := λ(H)`, `H ∈ 𝓐_tr`) | regular representation of `L¹` is bounded, multiplicative, `†`-compatible, faithful; the presented-complex category over `𝓐_tr` is closed under `‖·‖_tr`-limits. Acceptable construction for A.2. |
| Thm 8A.9 repair, (8A.23a), (8A.24′) | now correct: rank `1` at non-unit shells, weight `= |σ|^{1/2}/|1−σ|_p`; O-A5-5 disposal honestly downgraded. |
| §14.0a carrier statement, §14.0b block, ledger | consistent with the theorems; two verdicts moved down, none up. |
| §9.3.6 vs 9.14c, Thm 10.6a hypothesis, §14.1 item 4, unitization in 10.9(c), odd component | all repaired as asked. |

Nothing found wrong in round 2. No new findings.

## 2. The renaming test (closure rule §4)

Is any of A.2–A.8 "merely a renaming of the scalar explicit formula"?

* The explicit formula is an **identity**: (prime-power + Gamma side) = (poles) − (zeros).
  Paper 43 constructs the left side from fixed-point data of dilations
  (P123.042, P123.035) and **never uses the identity**; no zero appears in
  §§2–11, §14 (re-verified by the audit, item 18, and by me).
* A.2–A.4: a category of graph correspondences with composition, excision,
  half-density dagger — no counterpart in the explicit formula. **Pass.**
* A.5: the trace `T` *is* the left side of the explicit formula (Remark 9.7a
  says so). A construction of that side from geometry is not a renaming of
  the identity; and the Banach algebra `𝓐_tr`, the germ, the colimit trace are
  statements the explicit formula does not contain. **Pass.**
* A.6: `𝓝 = 0` (size of the symbol, not location of zeros), the exact Tate
  sequence, the no-splitting theorem, the rulings as limits in the completion,
  the canonical splitting of the completion — none of these is a statement
  the explicit formula makes. **Pass.**
* A.7: the cone and its properness via the Tate component. **Pass.**
* A.8, as restated in §10.3.3 ("What A.8's closure actually consists of"):
  Thms 9.14a, 9.14b, 9.14c′, 10.8 and the laws. The explicit formula does
  not know the completion, the rulings as limits, nor that the analytic form
  is trivial on them at a finite chart (indeed globally the value is `1`, by
  Mertens — a different, elementary input). **Pass**, with the
  auditor's round-1 objection ("as currently written") answered by the
  restatement it requested.

## 3. Clause verdicts

A.1 PROVED (clause's own words; the clause names no stack covering — the
reading note stays). A.2 PROVED (Thm 8A.12). A.3, A.4 PROVED on `G`.
A.5 PROVED (O-A5-5 in its exact limited form). A.6 PROVED under the amended
clause; strengthened. A.7 PROVED (thin clause, thin reading, stated).
A.8 **PROVED WITH TARGET `Pic_b(B_T)`** — I concur with the construction's
judgement and with the audit's F3 that Thm 10.7(e)'s second slot is
definitional; the content is the four theorems plus the laws, and the target
enlargement is forced by a theorem (10.8), not chosen. `Pic_b(B_T)` is a
determinant target in the sense the specification allows ("a determinant,
perfect-complex or nuclear trace target"), and it is P123.008 §6's own.
A.9 PASSED for the formalism. A.10 PROVED.

## 4. Decision under the closure rule

Both conditions of §4 are met: A.1–A.10 proved on the declared carrier (a
fixed finite chart with the chart system as additional structure, §14.0a),
and the adversarial audit of record finds none of A.2–A.8 a renaming.

    ROW A: WEIL-STRENGTH-COMPLETE
           on the declared carrier (fixed finite chart S, chart system and
           colimit as additional structure; invertible sector), with A.6
           under the amendment and A.8 with the determinant
           target Pic_b(B_T) forced by Theorem 10.8.

Recorded beside the label, so that no one reads more into it:
1. The round-1 audit graded A.8 "NOT EARNED as written"; its requested
   restatement is in §10.3.3 and its dissent is reproduced verbatim there.
2. Not claimed, and not required by any clause: `𝓝_∞^W = 0` on the colimit;
   the constant `c_cut` of the imported cutoff theorem; non-invertible
   correspondences as objects; a continuous extension of `I_A` to
   `N_A^dist × N_A^dist`; effective descent along a stack covering.
3. Theorem 10.8b is `CLASSICAL` (Mertens) and is handed to row C; it is what
   makes the finite-chart vector-valuedness intelligible, and it counts for
   nothing in A.
4. No sign. Theorem 14.1 stands: the numerical form has no Hodge-index shape
   at any finite chart.

## Addendum (phase 133)

**[phase 133, amendment accepted]** The amendment of A.8 was accepted, as proposed in
[`PANEL_SYNTHESIS.md`](../phase-133-abc-review-panel/PANEL_SYNTHESIS.md) §4.2;
the review's ruling above (A.8 `PROVED WITH TARGET Pic_b(B_T)`, with the round-1
audit's dissent recorded) is superseded by that decision; the
grading now reads `REFUTED AS STATED (scalar extension) + PROVED AS AMENDED`;
the label stands unconditionally. Amended clause text, as accepted:
"`λ_RR` is a based Hermitian biextension into `Pic_b(B_T)` whose Tate component
is the ruling determinant (Def 10.6c), consistent with the test sector by
Thms 9.14a, 9.14c′; the scalar determinant `L_S` is trivial on the rulings
(Thm 10.8), so the extension of the *scalar* determinant demanded by the
original clause does not exist." No theorem, proof or other grading changes.
Record: `../phase-133-abc-review-panel/AMENDMENTS_A8_B7_RECORD.md`.

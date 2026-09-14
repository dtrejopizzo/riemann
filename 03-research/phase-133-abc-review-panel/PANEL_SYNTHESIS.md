# Phase 133 — ABC review panel: lead synthesis and decisions

Author: session lead (Fable 5.1), audit of record. Date: 2026-09-12.
Inputs: PANEL_1_PROOFS.md (correctness), PANEL_2_CONNECTIONS.md (consistency),
PANEL_3_LABELS_AND_RH_CHAIN.md (labels, renaming test, chain to RH),
PANEL_REPAIRS.md (apparatus repairs, grep-evidenced, `[phase 133]` marks).

## 1. The three verdicts, in one table

| mandate | FATAL | MAJOR | verdict on the labels |
|---|---|---|---|
| 1 — proofs | none | 4 (A1 `D_A^0` two meanings + Rem 8.6b false; A2 Thm 14.1 proof invoked non-Paley–Wiener functions; A3 unlabelled transfer import in Paper 43 Rem 3.6; B1 Paper 44 §11 "none" false for amended B.4) | all three sustained; 30+ load-bearing theorems re-derived; strongest single result Paper 45 Thm 9.4 |
| 2 — connections | none | 2 (dangling "Paper 43 Remark 9.5" ×6; explicit-formula relabel not propagated to three places) + 8 MINOR | one consistent theory; no cross-paper contradiction; row-D target not stated identically |
| 3 — labels & RH chain | none | protocol: A.8 and B.7 dissents resolved by lead ruling while A.6 and B.4 went to the owner as amendments; the panel sides with the dissenting auditor on both | labels honest **as recorded**, with qualifications; the **name** "Weil-strength-complete" overstates against the specification's §1 (equality of structural burden with Weil, which Paper 43 §11bis item 4 says is not established) |

All apparatus findings of panels 1–2 and the non-owner items of panel 3 are
repaired in PANEL_REPAIRS.md (`[phase 133]`, no grading or lead decision
touched); the row-D target is now boxed byte-identically in Papers 43, 44, 45.
The lead's own sentence in R132.007 §3 is qualified per PANEL_3.

## 2. What is unconditionally proved (panel 3 §6, adopted)

A commutative correspondence theory on the idele class group of a finite
chart, with composition, involution, a declared trace whose symbol is by
construction the prime-power-plus-Gamma side of the explicit formula, vanishing
numerical radical, a canonical hyperbolic Tate boundary, a Frobenius family
with true unit and an integral shadow reproducing `Λ` in degree, a correct
repository proof of Weil's explicit formula (Paper 45 Thm 9.4), the
identification of the Weil form with that trace on primitive radial classes for
the unique constant `c = 0` (Thm 9.6, Cor 9.6a), and the sufficiency of
primitive radial tests for Weil's criterion (Thm 10.4). **About the zeros of
`ζ`: nothing**, and all three papers say so.

## 3. Weil's proof against Spec Z (panel 3 §5, adopted as the programme's map)

Surface → substituted by a group; non-invertible correspondences → absent;
composition/transpose/unit → proved, but trace, boundary and rulings live in
three different objects; Frobenius → constructed with the degree divided out,
self-intersection non-existent; intersection pairing → constructed, indefinite
with infinite index on both sides; Hodge index → absent and provably not
available in the naive shape (Paper 43 Thm 14.1, Paper 44 Thm 8bis.4a);
Riemann–Roch as a dimension formula → no section space, no `h⁰`, no
nonnegativity, no inequality. **Missing for the sign, exactly:** a functor to
something carrying a nonnegative invariant plus a vanishing theorem, turning
the biextension equality (Paper 43 (10.10)) into an inequality. Phases 130–132
did not narrow that distance; they proved which shapes it cannot have.

## 4. Decisions of the lead

1. **Labels stand as recorded**, with panel 3's recommendation adopted: the
   label is never to be printed without its carrier line ("on the declared
   carrier; invertible sector"), which Paper 43 §14.0b already carries.
2. **Two items go to the owner**, exactly as A.6 and B.4 did, because the panel
   is right that they are the same logical situation.  **ACCEPTED by the owner
   (D. Trejo Pizzo) 2026-09-12** — both amendments below; `[phase 133,
   amendment accepted 2026-09-12]`:
   * **A.8** — proposed amendment: "`λ_RR` is a based Hermitian biextension
     into `Pic_b(B_T)` whose Tate component is the ruling determinant
     (Def 10.6c), consistent with the test sector by Thms 9.14a, 9.14c′; the
     scalar determinant `L_S` is trivial on the rulings (Thm 10.8), so the
     extension of the *scalar* determinant demanded by the original clause
     does not exist." Grading if accepted: `REFUTED AS STATED (scalar
     extension) + PROVED AS AMENDED`; if rejected: A.8 `PROVED IN THE
     RESTATED FORM; the clause as written NOT EARNED`, and row A's label
     conditional.
   * **B.7** — proposed amendment: "the discriminating test at `p, p²` is
     `PROVED`; the mechanism is located on the carrier (shell volume,
     trivial fixed-point weight, Thm 6.5) and on the `Z`-model (deck `μ_n`,
     Thm 6.4(iv)); a map between the two locations is `REFUTED` on a
     `C`-linear carrier (P123.022), so the clause's demand for a single
     mechanism producing the cyclotomic factor is unsatisfiable as stated."
     Grading if accepted: `REFUTED AS STATED + PROVED AS AMENDED`; if
     rejected: B.7 `PARTIAL` and row B's label conditional.
   **ACCEPTED by the owner 2026-09-12**, both of them: A.8 is now
   `REFUTED AS STATED (scalar extension) + PROVED AS AMENDED` and B.7 is now
   `REFUTED AS STATED + PROVED AS AMENDED`; rows A and B keep their labels
   unconditionally.  Papers 43 §10.3.3 and 44 §10 carried, until that decision,
   the `[phase 133]` sentence that the panel sides with the dissent and the
   decision is pending; those sentences now read "decided: amendment accepted".
   Evidence of every edit: `AMENDMENTS_A8_B7_RECORD.md`.
3. **Row D opens only after the owner's decision on 2** (taken 2026-09-12: both
   amendments accepted), with the boxed target
   and the two standing negatives as its contract, and with panel 3 §5's
   sentence on what is missing as its statement of the problem.

## 5. Record

Apparatus verification of PANEL_REPAIRS by the lead: see the appended
"Verification" section below (grep counts, script runs).

## Verification (lead, after PANEL_REPAIRS)

| check | result |
|---|---|
| `[phase 133]` marks | Paper 43: 20; Paper 44: 24; Paper 45: 6 |
| "Paper 43 Remark 9.5" | survives only inside the three `[phase 133]` notes quoting the corrected text ✓ |
| `D_A^0` in the old §8 sense | none; the §8 set is `D_A^{off}` ✓ |
| row-D target box | present in Paper 43 (1), Paper 44 (2), Paper 45 (1) ✓ |
| transfer import `Tr` | Paper 43 Rem 3.6 + §12 table row, clauses A.2, A.4 "PROVED modulo (Tr)" ✓ |
| scripts | `R130_ml_check.py`, `mertens_check.py` (=1.0000), `verify_131_contacts.py` (ROUND-6 PASS), `verify_132_explicit_formula.py` (26/26) ✓ |

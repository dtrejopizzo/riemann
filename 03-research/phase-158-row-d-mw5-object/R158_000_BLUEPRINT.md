# R158_000 — Blueprint, phase 158: building an MW-5 object

Decision: option (B′) of R157_007 §3 — try to build a concrete MW-5 object that the filter F1–F5
(R157_000, F4 as amended) can test. Ceiling stated in advance: row D complete = RH; a proof of positivity for such an
object would be a proof of RH. Prior, stated honestly: low. The deliverable is either an object with a precise one-round
test, or a proved statement of why the MW-5 cluster cannot be instantiated in a given class.

MW-5 in the record: "no arithmetic site with `H¹`, Frobenius and a positive form" (ROW-D-CLOSURE-PLAN l.45);
reopened in phase 136 (PHASE_136_MAP_SYNTHESIS_AND_PLAN l.72, l.132; MAP_5 l.34, 67); the `h⁰` readings were killed by the
frame-defect theorem (P47 Thm 19.25, now on the small domain, Cor 19.25b) and D-HS (R155_054). What is left (R157_004 row 37,
re-scoped): Deninger's foliated dynamical systems plus the residuals of the `h⁰` reading and the import reading.

## Round 1 (parallel)
| file | task |
|---|---|
| `R158_001_SPEC_SHEET.md` | The specification sheet: from Weil over `F_q` (`H¹`, Frobenius, Rosati/Hodge-index positivity, Lefschetz trace formula) and from the proved record (W1–W15, T1–T5, frame defect, O3, `cor:void`, `thm:SC`, `lem:Rrig`, `thm:arena`, `cor:convfail`, NG-E1 strong form), derive the exact list of properties an MW-5 object must have and must not have for its positivity to evade every proved obstruction. Corpus check first (NG-107 Deninger–Morishita, phase 136 maps, phases 139–146, 21.15 curve model). |
| `R158_002_ADELE_CLASS_FOLIATION.md` | The concrete candidate: the adèle class space `A_Q/Q^×` with the scaling flow (Connes' trace formula = explicit formula) viewed as a Deninger-type foliated dynamical system. Identify the cohomology (leafwise/transverse, Álvarez López–Kordyukov), the candidate positivity structure (transverse Hodge `*`, Kähler-type form, Hard Lefschetz as Deninger proposes), and the precise point where the positivity would have to come from. Decide whether a testable lemma can be stated and run it through F1–F5. Open literature only. |
Rules: pure mathematics; corpus grep first; audit each round; no sign claims; state primitive vs complete form.

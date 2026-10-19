# Phase 114 — Closing the four rows of the arithmetic Lefschetz programme

The phase set out to close all four rows (a)–(d) of the arithmetic Lefschetz programme (paper 42),
where row (d) is the target inequality B_nuc(f,f) ≤ 0 for all f in T^0, built without using any
zero, without presupposing RH, and without the sign of the Weil form as an input. Rows (a)–(c) were
completed and written up elsewhere; the bulk of this phase (hundreds of numbered notes, each with a
paired verifier) is a long campaign of candidate local constructions for row (d), run against a
standing method rule: no candidate is built unless it is first checked against what the theorems of
the programme's own gate section already forbid.

## Results
- Rows (a)–(c): completed and published in the paper-42 writeup, each via the same method (a no-go about the naive object, then a forced replacement built once in an infinite but tame category on an imported engine). PROVED (reported, not re-derived here).
- Row (d) sharp Douglas gate (D.170): row D is equivalent, over an exhaustive family of prime-power births, to a bounded-vector identity y_N = D_out,N^{1/2} v_N, ‖v_N‖≤1. PROVED (reduction).
- Exact operator Green identity and defect-difference identity (D.210, D.211, D.214). PROVED.
- A real gap (D.172 correction) found in the three-block Feshbach endpoint template, proved non-cosmetic by an explicit scalar counterexample, and fixed; the paper's T=½log5 certificate was correspondingly demoted to separate, weaker rigorous statements. NO-GO (for the original claim) / PROVED (for the corrected, weaker statements).
- The previously unidentified residual channel is identified (D.260) as the Mellin–Stieltjes transform of dΨ−dx. PROVED (identification).
- An exact joint regularized residual identity with a monotone ε↓0 limit (D.261, D.262), carrying every prime power, the Gamma term, support compression and the two Tate jets. PROVED.
- One unconditional side result (D.244): exact inertia (1, |S|−1) for the finite prime tangent Hodge form; proved but found not usable for closing row D. PROVED, dead end for row D.
- Terminal self-assessment (D.263): the whole campaign D.191–D.262 ends on two obstructions that were already proved in the paper before the campaign began (infinite rank not removed by two Tate equations; the archimedean multiplier is indefinite) — recovered candidate-by-candidate rather than once, because the campaign's unit of work was per-candidate rather than per-family. ARGUED (methodological diagnosis).
- Row D overall: OPEN. The minimal remaining load-bearing theorem is stated precisely: construct Z_{N,ε}, without pseudoinverses and without assuming RH, such that the residual R_{N,ε} = Z_{N,ε}* Z_{N,ε}.
- Two loose ends carried forward, explicitly not on the critical path: an unreconciled mismatch between a log5 certificate (paper) and log6 deep-interval work (this phase); and a paused (not failed) interval-track calculation (D.227) that reached within 0.09 of its budget.

## Documents
- `PHASE_114_CLOSURE.md` — the master closure note (summarized above); start here.
- `ROW_D_MASTER_GOAL.md`, `ROW_D_GOAL_PLAN.md`, `ROW_D_EXECUTION_PLAN_AFTER_REFEREES.md`, `ROW_D_OPERATOR_MAP.md`, `ROW_D_SHARP_DOUGLAS.md`, `ROW_D_TWO_PROJECTION_AUDIT.md` — the row-D goal statement, execution plan, operator map, and the sharp Douglas reduction.
- `114_a_*` (339 files: `.md` theorem statements paired with `.py` verifiers) — row (a) construction notes (H7/I7/A4/G-series audits on the Haran square, Picard/Cartier gates, holonomy and nuclear-envelope constructions); largely superseded by the published row (a)–(c) writeup.
- `114_d_*` (554 files: `.md`/`.py` pairs) — the row (d) candidate-construction campaign (D-numbered notes): de Branges/canonical-system audits, Gamma-kernel and Feshbach/Schur certificates, Tate-defect and Birman–Schwinger analyses, the log5/log6 interval work, culminating in D.170–D.263 cited above.
- `114_d3_*` (6 files) — imported index theorems and the R16 linear-vs-quadratic χ question, with acceptance tests and verdict.
- `114_e_*` (4 files) — a balanced-channel factorization attempt and its counterfactual harness, opened late and not carried to a verdict in this phase.

## Relation to other phases
Builds on phases 107–113 (the row-(a) graded family, the corner pairing, and the trace/duality results of phase 113); explicitly checks any new row-D candidate against the no-go theorems already proved in the programme's own paper before this phase; closes with no successor phase opened and row D left OPEN for whoever picks it up next, with three named prior audits (de Branges/canonical-systems, explicit-formula equivalences, phase 113's imported-h⁰ route) to check before proposing a new import.

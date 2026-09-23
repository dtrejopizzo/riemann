# R156_005 — Lead closing decision, phase 156 (2026-09-23)

Inputs: `R156_001` + `R156_004` (156c), `R156_002` + `R156_003` (156d-R1), blueprint `R156_000`.

## 1. Labels of record added by phase 156
| statement | label | where integrated |
|---|---|---|
| Parity–Schur identity `In(W_T) = In(A_T\|P_T) + In(𝔊_T)`; `λ^W > 0 ⟺ λ^A > 0 ∧ 𝔊_T ≻ 0`; `λ^W ≥ 0 ⟺ RD_T ∧ range ∧ 𝔊_T ⪰ 0` | PROVED | P47 `thm:parityschur` |
| `𝔊_T = S^Sch_T + J`, polar capacity | PROVED | P47 `prop:polarcap` |
| `λ^∞(T) < 0` for `T ≥ 0.4608`; `T*_∞ ≤ 0.4608 < 0.58 ≤ T*_{∞,P}` | PROVED (interval, `scripts/r156/audit_r156_witness_t.py`) | P47 `prop:archneg` |
| The per-window converse fails in comb models (deletion on `[0.4608, 0.58]`; `θΛ(2)` at `½log3`, `θ ≤ 0.8148`); method constraint | PROVED, comb-level (`audit_r156_theta_quintic.py`) | P47 `cor:convfail` |
| KEP chain is one-directional (R156_001 §5.1 FAIL corrected) | PROVED | P47 §10.6, §11.1(5) |
| Truncated Gaussian witness; Thm 19.25 on `C_c^∞ ⊕ ℝK` and `P_c^∞ ⊕ ℝK`; **residual R1 CLOSED** | PROVED given (X19),(E2),(E3d); constants via new import (X30) Davenport | P46 Lemma 19.25a, Cor 19.25b |
| On bare `𝒢_min` the Thm 12.3 hypothesis is satisfiable ⟺ RH | PROVED, new | P46 Rem 19.25c |
| Citation slip: "positivity for `T ≤ log 2`" is primitive-form only | CORRECTION | P47 intro, §5, §6.4, `prop:arch`(iii), `rem:twohalves`; R155_023/031, PATH-TO-D |
| P46 errata E1 (sign, Lemma 19.20(v)), E2 (Thm 19.23 window via `s_{F₀}`), E3 (zero-count gap flagged) | CORRECTION | P46 |
Not cleared: Galerkin `𝔤±`, `θ_* ≈ 0.99991`, `S^Sch ≈ −J` (DIAGNOSTIC, P47 `rem:polarcapdiag`); extension of the converse
failure to all of `(T*_∞, T*_{∞,P})`; per-field Cor 6.2.

## 2. Effect on the map
156a had already been done in the corpus (D.56, 3c.1/3c.3). 156b is blocked (arena N5, D.53). 156c answers the only OPEN
per-window equivalence of R155_060: the passage from the primitive to the complete form is a genuine 2×2 condition, and
it fails in models with the same structural data. 156d closes R1. The reduced statement of row D is written in
`05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-REDUCED-STATEMENT-2026-09-23.md`.

## 3. Orders (owner decisions)
(a) Choose (A) "row D closed in the map (final)" or (B) "continue" (§6 of the reduced statement).
(b) O-150.1: supply the Diamond–Montgomery–Vorhauer 2006 PDF, or drop it.
(c) Commit phase 156, the P46/P47 edits and the reduced statement.
Row-D label and endpoint of record unchanged.

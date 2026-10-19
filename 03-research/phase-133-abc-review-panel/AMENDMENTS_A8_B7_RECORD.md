# Phase 133 — record of the two accepted amendments (A.8, B.7)

Record of edits. Every edit below is marked in its file with
`[phase 133, amendment accepted ]`.

## 0. What was decided

Both amendments proposed by the phase-133 review panel in
[`PANEL_SYNTHESIS.md`](PANEL_SYNTHESIS.md) §4.2 were **accepted**:

* **A.8** (Paper 43, row A): "`λ_RR` is a based Hermitian biextension into
  `Pic_b(B_T)` whose Tate component is the ruling determinant (Def 10.6c),
  consistent with the test sector by Thms 9.14a, 9.14c′; the scalar determinant
  `L_S` is trivial on the rulings (Thm 10.8), so the extension of the *scalar*
  determinant demanded by the original clause does not exist."
  Grading: `REFUTED AS STATED (scalar extension) + PROVED AS AMENDED`.
* **B.7** (Paper 44, row B): "the discriminating test at `p, p²` is `PROVED`;
  the mechanism is located on the carrier (shell volume, trivial fixed-point
  weight, Thm 6.5) and on the `Z`-model (deck `μ_n`, Thm 6.4(iv)); a map
  between the two locations is `REFUTED` on a `C`-linear carrier (P123.022), so
  the clause's demand for a single mechanism producing the cyclotomic factor is
  unsatisfiable as stated."
  Grading: `REFUTED AS STATED + PROVED AS AMENDED`.

The rulings (`R130.005` for A.8, `R131.005` §2 adopted in `R131.019` for
B.7) are **superseded by this decision**; the dissents
are kept **verbatim** as history (Paper 43 §10.3.3, Paper 44 §10 table);
Paper 44 Remark 6.5a′ is untouched.  The labels
`ROW A: WEIL-STRENGTH-COMPLETE` and `ROW B: WEIL-STRENGTH-COMPLETE` stand
**unconditionally** on the declared carrier.

**No theorem, no proof and no other clause grading was changed.**

## 1. Files edited

| file | edit |
|---|---|
| `03-research/phase-123-weil-strength-abc/P123_A_ACCEPTANCE_SPECIFICATION.md` | A.8 clause text kept; amendment record + acceptance added; §3 table row A.8 regraded; new §7 "Phase-133 amendment" |
| `05-meta-and-planning/ABCD-CLOSURE-PLAN/PLAN.md` | §6: Spanish rendering of the B.7 text and acceptance, grading `REFUTADO TAL COMO ESTÁ ESCRITO + PROBADO COMO ENMENDADO`; new "Actualización (fase 133, enmiendas A.8 y B.7 aceptadas)" paragraph |
| `04-papers/43-row-a-torsion-theory/main.md` | header decision line; §10.3.3 `[phase 133]` sentence → decided; §10.3.3 decision paragraph; §14.0b clause block A.8 row and decision line |
| `04-papers/44-row-b-arithmetic-family/main.md` | header note; §10 table B.7 row regraded (old verdict + dissent kept verbatim); §10.4 decision block |
| `03-research/phase-130-row-a-closure/R130_005_FINAL_AUDIT_AND_LABEL.md` | addendum |
| `03-research/phase-131-row-b-closure/R131_019_FINAL_AUDIT_AND_LABEL.md` | addendum |
| `03-research/phase-133-abc-review-panel/PANEL_SYNTHESIS.md` | §4.2 marked "ACCEPTED" |
| `03-research/phase-133-abc-review-panel/README.md` | "pending" line replaced by the decision |
| `04-papers/README.md` | index lines for Papers 43 and 44 ("A.8 amended", "B.7 amended") |

## 2. Grep evidence (commands and their output)

```text
### 1. P123_A_ACCEPTANCE_SPECIFICATION.md
$ grep -n "amendment accepted \|^## 7\." 03-research/phase-123-weil-strength-abc/P123_A_ACCEPTANCE_SPECIFICATION.md
164:| A.8 | Paper 43 (phase 130): Theorem 10.7 (vector-valued Riemann-Roch biextension with target `Pic_b(B_T)`), Theorem 10.8 (the scalar determinant is trivial on the rulings), T
219:## 7. Phase-133 amendment
221:**[phase 133, amendment accepted ]** The phase-133 review panel

$ grep -n "^| A.8 |" 03-research/phase-123-weil-strength-abc/P123_A_ACCEPTANCE_SPECIFICATION.md
164:| A.8 | Paper 43 (phase 130): Theorem 10.7 (vector-valued Riemann-Roch biextension with target `Pic_b(B_T)`), Theorem 10.8 (the scalar determinant is trivial on the rulings), Theorems 9.14a, 9.14c' (consistency with the test sector) | `REFUTED AS STATED (scalar extension) + PROVED AS AMENDED` (amendment, above; accepted) **[phase 133, amendment accepted ]** |

### 2. PLAN.md
$ grep -n "Enmienda al punto 7\|fase 133, enmiendas" 05-meta-and-planning/ABCD-CLOSURE-PLAN/PLAN.md
98:**Update (phase 133, amendments A.8 and B.7 accepted).** `[phase 133, amendment accepted ]` Both amendments proposed in PANEL_S
254:**Amendment to item 7 — ACCEPTED; text proposed in phase 133 (PANEL_SYNTHESIS §4.2):** `[phase 133, amendment accepted ]` Item

### 3. Paper 43
$ grep -n "amendment accepted \|A.8 amended (\|REFUTED AS STATED" 04-papers/43-row-a-torsion-theory/main.md
8:)**: `REFUTED AS STATED (scalar extension) + PROVED AS AMENDED`, the
10:target, which is Theorem 10.8. **[phase 133, amendment accepted :
3927:amendment accepted : it was accepted
3933:not exist."  New grading: `REFUTED AS STATED (scalar extension) + PROVED AS
4180:.** Clause A.8 is therefore graded `REFUTED AS STATED (scalar
4996:  A.8  mixed Riemann-Roch ........................ REFUTED AS STATED
4998: [phase 133, amendment accepted; the previous entry read
5045: under the amendment and A.8 amended (
5046: ) [phase 133, amendment accepted; this line
5081:| ~~R-A6~~ | **DECIDED** | amendment accepted |

$ grep -n "decision on an amendment is" 04-papers/43-row-a-torsion-theory/main.md
3926:decision on an amendment is decided: amendment accepted.]**  **[phase 133,

### 4. Paper 44
$ grep -n "amendment accepted \|B.7 amended (" 04-papers/44-row-b-arithmetic-family/main.md
16:> trace; B.4 amended (accepted ), B.7 amended (
17:> ) — **[phase 133, amendment accepted : this read "B.7 by
5511:| B.7 discriminating test `p`, `p²`; mechanism located | **`REFUTED AS STATED` + `PROVED AS AMENDED` .[phase 133, amendment accep
5587: B.4 amended ; B.7 amended (
5588: ) [phase 133, amendment accepted; this

$ grep -c "Rem. 6.5a′" 04-papers/44-row-b-arithmetic-family/main.md   (unchanged)
1

### 5. Lead decision files, panel, READMEs
$ grep -n "Addendum (phase 133)" 03-research/phase-13-omega-class-multiplicative-chaos*/R13*_LEAD_FINAL_AUDIT_AND_LABEL.md
03-research/phase-131-row-b-closure/R131_019_FINAL_AUDIT_AND_LABEL.md:107:## Addendum (phase 133)
03-research/phase-130-row-a-closure/R130_005_FINAL_AUDIT_AND_LABEL.md:87:## Addendum (phase 133)

$ grep -n "ACCEPTED " 03-research/phase-133-abc-review-panel/PANEL_SYNTHESIS.md 03-research/phase-133-abc-review-panel/README.md
03-research/phase-133-abc-review-panel/README.md:15:Decisions: A.8 amendment and B.7 amendment (PANEL_SYNTHESIS §4.2) **ACCEPTED ** `[phase 133, amend
03-research/phase-133-abc-review-panel/PANEL_SYNTHESIS.md:54:   is right that they are the same logical situation.  **ACCEPTED 
03-research/phase-133-abc-review-panel/PANEL_SYNTHESIS.md:74: **ACCEPTED **, both of them: A.8 is now

$ grep -o "\*\*A\.8 amended\*\*[^(]*([^)]*)\|\*\*B\.7 amended\*\*[^(]*([^)]*)" 04-papers/README.md
**A.8 amended** — `REFUTED AS STATED (scalar extension) + PROVED AS AMENDED`
**B.7 amended** — `REFUTED AS STATED + PROVED AS AMENDED`, accepted (phase 133)

### 6. No theorem or proof text changed
$ git diff --stat
 ...6_198_OPERATOR_VALUED_GAMMA_BOUNDARY_PUSHOUT.md |   21 +-
 ...LBERT_COMPLETION_AND_GAMMA_COMPLIANCE_KERNEL.md |    6 +
 ...06_203_COMPLETE_RETURN_CHARGED_TATE_BOUNDARY.md |   10 +
 .../106_204_COVARIANT_CHARGE_MIXING_BOUNDARY.md    |    6 +
 .../scripts/W3_build_xy.py                         |   13 +-
 .../PLAN.md                                        |   10 +-
 .../README.md                                      |   15 +-
 .../42-arithmetic-lefschetz-programme/main.pdf     |  Bin 790326 -> 878720 bytes
 .../42-arithmetic-lefschetz-programme/main.tex     | 1155 +++++++++++++++++---
 04-papers/README.md                                |    4 +
 05-meta-and-planning/README.md                     |    9 +
 11 files changed, 1066 insertions(+), 183 deletions(-)
```

## 3. Untouched by design

* Paper 44 Remark 6.5a′ (`grep -c` above returns 1, the original occurrence).
* Every theorem and proof in Papers 43, 44, 45.
* Every other clause grading of the A and B acceptance specifications.

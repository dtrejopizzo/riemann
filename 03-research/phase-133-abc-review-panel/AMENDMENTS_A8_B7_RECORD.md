# Phase 133 — record of the two owner-accepted amendments (A.8, B.7)

Date: 2026-09-12.  Builder record.  Every edit below is marked in its file with
`[phase 133, amendment accepted 2026-09-12]`.

## 0. What was decided

On 2026-09-12 the repository owner (D. Trejo Pizzo) **accepted** both
amendments proposed by the phase-133 review panel and referred to him by the
lead in [`PANEL_SYNTHESIS.md`](PANEL_SYNTHESIS.md) §4.2:

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

The lead rulings (`R130.005` for A.8, `R131.005` §2 adopted in `R131.019` for
B.7) are **superseded by the owner's decision**; the hostile auditors' dissents
are kept **verbatim** as history (Paper 43 §10.3.3, Paper 44 §10 table);
Paper 44 Remark 6.5a′ is untouched.  The labels
`ROW A: WEIL-STRENGTH-COMPLETE` and `ROW B: WEIL-STRENGTH-COMPLETE` stand
**unconditionally** on the declared carrier.

**No theorem, no proof and no other clause grading was changed.**

## 1. Files edited

| file | edit |
|---|---|
| `03-research/phase-123-weil-strength-abc/P123_A_ACCEPTANCE_SPECIFICATION.md` | A.8 clause text kept; amendment record + owner's acceptance added; §3 table row A.8 regraded; new §7 "Phase-133 amendment" |
| `05-meta-and-planning/ABCD-CLOSURE-PLAN/PLAN.md` | §6: "Enmienda al punto 7 — ACEPTADA por el propietario … 2026-09-12" (Spanish rendering of the B.7 text, grading `REFUTADO TAL COMO ESTÁ ESCRITO + PROBADO COMO ENMENDADO`); new "Actualización 2026-09-12 (fase 133, enmiendas A.8 y B.7 aceptadas)" paragraph |
| `04-papers/43-row-a-torsion-theory/main.md` | header decision line; §10.3.3 `[phase 133]` sentence → decided; §10.3.3 "Owner's decision (2026-09-12)" paragraph; §14.0b clause block A.8 row and lead decision line |
| `04-papers/44-row-b-arithmetic-family/main.md` | header note; §10 table B.7 row regraded (old verdict + auditor's dissent kept verbatim); §10.4 lead decision block |
| `03-research/phase-130-row-a-closure/R130_005_LEAD_FINAL_AUDIT_AND_LABEL.md` | dated addendum |
| `03-research/phase-131-row-b-closure/R131_019_LEAD_FINAL_AUDIT_AND_LABEL.md` | dated addendum |
| `03-research/phase-133-abc-review-panel/PANEL_SYNTHESIS.md` | §4.2 marked "ACCEPTED by the owner 2026-09-12" |
| `03-research/phase-133-abc-review-panel/README.md` | "pending" line replaced by the decision |
| `04-papers/README.md` | index lines for Papers 43 and 44 ("A.8 amended", "B.7 amended") |

## 2. Grep evidence (commands and their output)

```text
### 1. P123_A_ACCEPTANCE_SPECIFICATION.md
$ grep -n "amendment accepted 2026-09-12\|^## 7\." 03-research/phase-123-weil-strength-abc/P123_A_ACCEPTANCE_SPECIFICATION.md
164:| A.8 | Paper 43 (phase 130): Theorem 10.7 (vector-valued Riemann-Roch biextension with target `Pic_b(B_T)`), Theorem 10.8 (the scalar determinant is trivial on the rulings), T
219:## 7. Phase-133 amendment (2026-09-12)
221:**[phase 133, amendment accepted 2026-09-12]**  The phase-133 review panel

$ grep -n "^| A.8 |" 03-research/phase-123-weil-strength-abc/P123_A_ACCEPTANCE_SPECIFICATION.md
164:| A.8 | Paper 43 (phase 130): Theorem 10.7 (vector-valued Riemann-Roch biextension with target `Pic_b(B_T)`), Theorem 10.8 (the scalar determinant is trivial on the rulings), Theorems 9.14a, 9.14c' (consistency with the test sector) | `REFUTED AS STATED (scalar extension) + PROVED AS AMENDED` (amendment of 2026-09-12, above; accepted by the owner D. Trejo Pizzo) **[phase 133, amendment accepted 2026-09-12]** |

### 2. PLAN.md
$ grep -n "Enmienda al punto 7\|fase 133, enmiendas" 05-meta-and-planning/ABCD-CLOSURE-PLAN/PLAN.md
98:**Actualización 2026-09-12 (fase 133, enmiendas A.8 y B.7 aceptadas).** `[phase 133, amendment accepted 2026-09-12]` El propietario (D. Trejo Pizzo) aceptó las dos enmiendas propuestas en PANEL_S
254:**Enmienda al punto 7 — ACEPTADA por el propietario (D. Trejo Pizzo) el 2026-09-12; texto propuesto en la fase 133 (PANEL_SYNTHESIS §4.2):** `[phase 133, amendment accepted 2026-09-12]` El punt

### 3. Paper 43
$ grep -n "amendment accepted 2026-09-12\|A.8 amended (owner\|REFUTED AS STATED" 04-papers/43-row-a-torsion-theory/main.md
8:2026-09-12)**: `REFUTED AS STATED (scalar extension) + PROVED AS AMENDED`, the
10:target, which is Theorem 10.8.  **[phase 133, amendment accepted 2026-09-12:
3927:amendment accepted 2026-09-12: the repository owner (D. Trejo Pizzo) accepted
3933:not exist."  New grading: `REFUTED AS STATED (scalar extension) + PROVED AS
4180:2026-09-12.**  Clause A.8 is therefore graded `REFUTED AS STATED (scalar
4996:  A.8  mixed Riemann-Roch ........................ REFUTED AS STATED
4998:       [phase 133, amendment accepted 2026-09-12; the previous entry read
5045:           under the 2026-09-12 amendment and A.8 amended (owner,
5046:           2026-09-12) [phase 133, amendment accepted 2026-09-12; this line
5081:| ~~R-A6~~ | **DECIDED** | amendment accepted 2026-09-12 |

$ grep -n "decision on an amendment is" 04-papers/43-row-a-torsion-theory/main.md
3926:decision on an amendment is decided: amendment accepted.]**  **[phase 133,

### 4. Paper 44
$ grep -n "amendment accepted 2026-09-12\|B.7 amended (owner" 04-papers/44-row-b-arithmetic-family/main.md
16:> trace; B.4 amended (owner-accepted 2026-09-12), B.7 amended (owner,
17:> 2026-09-12) — **[phase 133, amendment accepted 2026-09-12: this read "B.7 by
5511:| B.7 discriminating test `p`, `p²`; mechanism located | **`REFUTED AS STATED` + `PROVED AS AMENDED` (owner, 2026-09-12).**  **[phase 133, amendment accep
5587:           B.4 amended (owner, 2026-09-12); B.7 amended (owner,
5588:           2026-09-12) [phase 133, amendment accepted 2026-09-12; this

$ grep -c "Rem. 6.5a′" 04-papers/44-row-b-arithmetic-family/main.md   (unchanged)
1

### 5. Lead decision files, panel, READMEs
$ grep -n "Addendum 2026-09-12 (phase 133)" 03-research/phase-13*/R13*_LEAD_FINAL_AUDIT_AND_LABEL.md
03-research/phase-131-row-b-closure/R131_019_LEAD_FINAL_AUDIT_AND_LABEL.md:107:## Addendum 2026-09-12 (phase 133)
03-research/phase-130-row-a-closure/R130_005_LEAD_FINAL_AUDIT_AND_LABEL.md:87:## Addendum 2026-09-12 (phase 133)

$ grep -n "ACCEPTED by the owner" 03-research/phase-133-abc-review-panel/PANEL_SYNTHESIS.md 03-research/phase-133-abc-review-panel/README.md
03-research/phase-133-abc-review-panel/README.md:15:Owner decisions: A.8 amendment and B.7 amendment (PANEL_SYNTHESIS §4.2) **ACCEPTED by the owner (D. Trejo Pizzo) on 2026-09-12** `[phase 133, amend
03-research/phase-133-abc-review-panel/PANEL_SYNTHESIS.md:54:   is right that they are the same logical situation.  **ACCEPTED by the owner
03-research/phase-133-abc-review-panel/PANEL_SYNTHESIS.md:74:   **ACCEPTED by the owner 2026-09-12**, both of them: A.8 is now

$ grep -o "\*\*A\.8 amended\*\*[^(]*([^)]*)\|\*\*B\.7 amended\*\*[^(]*([^)]*)" 04-papers/README.md
**A.8 amended** — `REFUTED AS STATED (scalar extension) + PROVED AS AMENDED`
**B.7 amended** — `REFUTED AS STATED + PROVED AS AMENDED`, accepted by the owner 2026-09-12 (phase 133)

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

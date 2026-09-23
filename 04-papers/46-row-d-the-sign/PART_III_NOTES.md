# Paper 46, Part III — editorial notes

Record of what was appended to `main.md`, where each statement comes from, what
was entered as a correction in Parts I–II, and what was left out.  This file is
an editorial record; it states no mathematics.

## 1. Sections added

| § | title | lines in `main.md` | numbered statements |
|---|---|---|---|
| — | Part III header | 4033 | — |
| 17 | Detecting cones and the intrinsic characterization of the primitive sector | 4043–4736 | 35 (9 theorems, 7 corollaries, 3 lemmas, 1 proposition, 4 definitions, 11 remarks) |
| 18 | What a proof of the sign must use: two method constraints | 4737–5896 | 44 (14 theorems, 5 corollaries, 7 lemmas, 2 propositions, 2 definitions, 2 observations, 1 problem, 11 remarks) |
| 19 | The Riemann–Roch-defined `h⁰` and the frame defect theorem | 5897–6512 | 30 (12 theorems, 1 restatement, 3 corollaries, 2 lemmas, 4 propositions, 6 definitions, 2 remarks) |
| 19bis | The square as a tensor structure: the bidegree route and why it closes | 6513–7283 | 23 (9 thms, 1 restatement, 4 cors, 2 lemmas, 1 prop, 4 defs, 2 remarks) |
| 20 | The trace-positive cone | 7284–8330 | 40 (17 theorems, 1 restatement, 2 corollaries, 11 lemmas, 2 propositions, 5 definitions, 2 remarks) |
| 21 | The function-field model of the frame | 8331–9258 | 25 (10 theorems, 4 propositions, 3 lemmas, 5 definitions, 3 remarks) |
| 22 | The degree form on `Z⟨Frob_n⟩` and the computed Frobenius diagonal | 9259–9956 | 23 (7 theorems, 3 corollaries, 2 lemmas, 2 propositions, 4 definitions, 5 remarks) |
| 23 | The state of the sign | 9957–10207 | 0 (consolidation only: proved / restatement / refuted / open (24)–(36) / diagnosis / reproduction) |

Line numbers are as of the commit in which Part III was appended and will drift
with later edits; the section headings are stable.

Each of §§17–22 carries, at its head, a one-paragraph italic provenance note
naming the source files, and, at its foot, a **Withdrawn in this section**
table.  No source file name appears in any theorem, definition or proof.

## 2. Theorems and their sources

The mapping below is by source label; every statement carries its complete
proof from the source unless it is marked as a pointer.

**§17** — `03-research/phase-138-row-d-detecting-cones/R138_001_BUILDER_ROUND1.md`,
labels from `R138_005_LEAD_CLOSING_DECISION.md`, withdrawals from
`R138_002_HOSTILE_AUDIT.md` / `R138_004_HOSTILE_CONFIRMATION.md`.
Thm 17.5 ← D.15.1 · Thm 17.7, Cor 17.7a ← D.15.3 · Thm 17.8 ← D.15.2 ·
Thm 17.9 ← D.15.2b · Cor 17.10 ← D.15.2c · Lem 17.13, Thm 17.14 ← D.17.2,
D.17.2a · Lem 17.16, Cor 17.17 ← D.17.2c, D.17.2d · Prop 17.18,
Thm 17.19 ← D.17.3a, D.17.3b (repository: phase-114 D.185, phase-72 E72_49) ·
Thm 17.21 ← D.15.4 · Thm 17.22 ← D.15.4b · Cor 17.23, Cor 17.25 ← D.15.4c ·
Rem 17.24 ← D.15.4d · Thm 17.26 ← D.16.2‴ · Cor 17.27 ← D.16.3 ·
Rem 17.28 ← D.16-γ, D.15-β.

**§18** — `03-research/phase-137-row-d-canonical-coupling/R137_001/003/005` and
`03-research/phase-139-row-d-two-falsifiers/R139_001_BUILDER_ROUND1.md`; labels
from `R137_007` and `R139_005`.
Thm 18.1 (T1) ← R137_007 §2.2, R139_001 §D.19.7 · Thm 18.3 ← D.19.2 ·
Lem 18.4 ← D.19.3a · Thm 18.5, Cor 18.6 ← D.19.4a · Lem 18.7 ← D.19.4b ·
Thm 18.8 ← D.19.3 · Lem 18.9, Thm 18.10 ← D.19.5a, D.19.5 · Thm 18.11 ←
D.19.5b · Thm 18.12 ← D.19.6 · Def 18.13, Thm 18.14 ← D.19.7, D.19.7a ·
Lem 18.15 ← D.19.7c · Thm 18.16 (T2) ← D.19.7 · Cor 18.17 ← D.19.7d ·
Thm 18.18 ← D.20.1 · Lem 18.19, Thm 18.20 ← D.20.2a₀, D.20.2 ·
Prop 18.21 (the fork) ← R137_005 Proposition 1.1 · Lem 18.22–Cor 18.24 ←
R137_003 §2 · Thm 18.25 ← D.11.2′ · Prop 18.26, Cor 18.27 ← R137_005 §2 ·
Thm 18.28 ← D.11.3 · Thm 18.29 ← D.11.4′ · Cor 18.30 ← D.11.5′ ·
Obs 18.31 ← R137_005 Observation 2.1 · Prob 18.32 ← R139_005 §2 ·
Obs 18.33 ← R137_007 §2(2).

**§19** — `03-research/phase-141-row-d-frobenius-traces/R141_001_BUILDER_ROUND1.md`
§D.30 and `03-research/phase-142-row-d-the-clause/R142_001_BUILDER_ROUND1.md`
§§D.31–D.32 (with `R142_003` for §D.32); labels from `R141_005`, `R142_005`,
`R142_002`, `R142_004`.
Thm 19.2 ← D.30.1 · Prop 19.4 ← D.30.3 · Thm 19.6 ← D.30.5 · Prop 19.7 ←
D.30.6 · Thm 19.8, Cor 19.9 ← D.30.7, D.30.8 · Thm 19.11 ← D.30.10 ·
Thm 19.12, Cor 19.13 ← D.30.11, D.30.12 · Prop 19.14 ← D.30.15 · Thm 19.15 ←
D.30.16 · Lem 19.17, Prop 19.18 ← D.31.4, D.31.5 · Lem 19.20 ← D.31.7 ·
Thm 19.21 ← D.31.8 · Thm 19.22 ← D.31.9 · Thm 19.23 ← D.31.10 · Cor 19.24 ←
D.31.11 · **Thm 19.25 (frame defect) ← D.31.12** · Thm 19.28 ← §D.31.7 ·
Restatement 19.29 ← D.32.1 · Thm 19.30 ← D.32.4 (B4 verdict per `R142_004` J3).

**§19bis** — `03-research/phase-140-row-d-frobenius-square/R140_001_BUILDER_ROUND1.md`
§§D.22–D.24 and `R140_003_BUILDER_ROUND2.md`; labels from
`R140_005_LEAD_CLOSING_DECISION.md`, withdrawals from `R140_002` / `R140_004`.
Lem 19bis.2, Thm 19bis.3 ← D.22.2, D.22.3 · Thm 19bis.5, Cor 19bis.6 ← D.22.5,
D.22.6 (the general-number-field item closed) · Thm 19bis.8–Cor 19bis.10 ←
D.23.7–D.23.9 · Thm 19bis.12 ← D.23.12, carrying residue R2 of `R140_005` §3 ·
Restatement 19bis.13 ← D.23.13 · Thm 19bis.15, Thm 19bis.16 ← D.24.3a, D.24.4 ·
Thm 19bis.17 ← D.24.5 · Lem 19bis.18 ← D.24.6 · **Thm 19bis.19 ((b′) fails for
every bidegree-function) ← D.24.7** · Cor 19bis.20, Prop 19bis.21 ← D.24.8,
D.24.9 · Thm 19bis.22 ← D.24.11 (with D.24.10 folded in) · Cor 19bis.23 ←
D.24.12, split `PROVED` / `GUIDANCE` as the source splits it.

**§20** — `R141_001` §D.26, `03-research/phase-143-row-d-trace-positive-cone/R143_001_BUILDER_ROUND1.md`
§D.34, `03-research/phase-144-row-d-fixed-index/R144_001_BUILDER_ROUND1.md`
§§D.37–D.40; labels from `R143_005`, `R144_005`.
Lem 20.1–Thm 20.9 ← D.26.1–D.26.9 · Def 20.10–Lem 20.13 ← D.34.1–D.34.3 ·
Thm 20.14 ← D.34.4 · **Thm 20.15 ((T1′)) ← D.34.5** · **Thm 20.17 (transfer
12.3-B4) ← D.34.8** · Lem 20.18, Thm 20.19 ← D.34.6a, D.34.7 · Lem 20.21 ←
D.34.9′ · Thm 20.22 ← D.34.10 · Thm 20.23 ← D.34.12 · Thm 20.24 ← D.34.13 ·
Thm 20.25 ← D.34.14(i) · Prop 20.26 ← D.34.16 · Lem 20.27, Lem 20.28 ←
D.38.2, D.38.2a · Thm 20.29 ← D.38.3 · Restatement 20.30 ← D.38.3a ·
Thm 20.31 ← D.38.5 · Cor 20.32 ← D.38.5c · Cor 20.33 ← O-29 / D.34.15(ii) ·
Lem 20.34, Thm 20.35 ← D.37.2, D.37.4 · Lem 20.36–Thm 20.39 ← §D.40.

**§21** — `03-research/phase-145-row-d-function-field-model/R145_001_BUILDER_ROUND1.md`;
labels from `R145_005`, `R145_002`, `R145_004`, `CORPUS_CHECK_R145.md`.
Lem 21.2–Thm 21.5 ← D.41.1–D.41.4 · **Thm 21.7 (the dictionary,
`I_∞^C = +(D_E·D_F)`) ← D.41.6** · Thm 21.8 ← D.41.7 · Thm 21.9 ← D.41.9bis ·
Lem 21.11–Prop 21.13 ← D.41.10–D.41.12′ · Thm 21.14 ← D.41.13 ·
**Thm 21.15 (frame defect on the curve) ← D.41.14** · Thm 21.16 ← D.41.16 ·
Thm 21.17 ← D.41.17 · Thm 21.19 ← D.41.18/19 · Thm 21.20 ← D.41.8 and
MISMATCH 7 (the naming correction) · Prop 21.21 ← D.42.5 · Prop 21.22,
Rem 21.23 ← `R145_004` §4, `R145_005` §2 · (P145′) ← D.42.4.

**§22** — `03-research/phase-146-row-d-coupled-pairing/R146_001_BUILDER_ROUND1.md`
§§D.44–D.49 as repaired and `R146_003_BUILDER_ROUND2.md`; labels from
`R146_005`, `R146_002`, `R146_004`, `CORPUS_CHECK_R146(b).md`.
Lem 22.2 ← D.44.2 · Thm 22.3, Thm 22.4 ← D.45.1, D.45.2 · Prop 22.5 ←
D.45.1–2 structural identity · Thm 22.6, Cor 22.7 ← D.45.4, D.45.5 ·
Thm 22.9 ← D.45.7 · **Thm 22.11 (the computed diagonal) ← D.47.2** ·
Lem 22.13–Thm 22.15 ← D.47.4–D.47.6 · Cor 22.16 ← D.47.7 restricted to the
domain of record · **Thm 22.17 (`Spec Z` terminal) ← the replacement for the
withdrawn D.45.8**, with the consequence from `R146_005` §2(1) ·
Rem 22.18 ← `R146_005` §4.

**§23** — consolidation of the closing records of phases 136–146 and of
`05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-SYNTHESIS-PHASES-135-144.md`;
the one-paragraph diagnosis of §23.5 follows `R146_005` §4.

## 3. Imports added to §15

The §15 table gained a block headed **"Added by Part III (§§17–23)"** with
fifteen rows: **(X19)** verified first zero (Rosser–Yohe–Schoenfeld;
Platt–Trudgian) — entered for the first time although used from the record note
at Theorem 12.3 on; **(X20)** Landau's theorem (Laplace and Dirichlet-series
forms); **(X20a)** PNT with the Vinogradov–Korobov remainder; **(X21)**
Davenport–Heilbronn; **(X22)** Montgomery–Vaughan; **(X23)** the quantitative
zero-free region on `Re s = 1`; **(X24)** the real-zero / Siegel-zero input;
**(X25)** Artin holomorphy (conditional half of base change only); **(X25a)**
the classical Hecke–Artin analytic package; **(X25b)** Heilbronn `h(−D) → ∞`;
**(X26)** classical surface theory (Hartshorne V.1.6/1.8/1.9, Lazarsfeld §2.2);
**(X27)** Weil's RH for curves with Tate's `NS(A×B)` and `Γ_α·Γ_β = deg(α−β)`;
**(X28)** intersection theory and bigness on a smooth projective surface;
**(X29)** Toeplitz operators with continuous symbol; **(X29a)** the affine
anti-equivalence.

The tags `(X28)`–`(X30a)` of the working drafts were renumbered to
`(X27)`–`(X29a)` so that the list has no gap; no import was dropped.

## 4. Corrections entered in Parts I–II

| tag | what | where entered (line) |
|---|---|---|
| **P46-1** | the `M`-convention transposition: the `#P`-tuple printed in the proof of Proposition 12.6 is transposed relative to Proposition 14.1 and Theorem 11.8(iii); the convention of record is `M(F) = (Φ_F(1), Φ_F(0))` | §12.5, line 3211 |
| **P46-2** | the effective-class falsifier witness added as **Remark 12.3c** (for `Ξ_a` the Hodge-index inequality already fails on `τ_uK_a + τ_{−u}K_a`, with no zero, no prime and no `h⁰`), with the equimodularity ceiling | end of §12.3, line 3092 |
| **P46-3** | the splitting `D^W = Λ ⊥ P^W` with `K_odd`, pointed forward to Theorem 17.5 as the completion of §11.3 | head of §11.3, line 2301 |
| **P46-4** | RH ⟺ the Hodge-index inequality on the ample cone, from Theorem 11.14(iii) (the cone is absorbing at `K`), with the caveat that the ample cone is defined through `I_∞` and the equivalence is therefore a restatement | after Remark 11.14a, line 2674 |
| **R137** | §14.5 item (23): the word *equivalently* is wrong; the reduction is one-sided, to the largest index `Q(m)`; restated as open item (27) | §14.5 item (23), line 3898 |
| **R137** | Remark 13.6a's heuristic is a theorem in both directions, in the sharp form `e^{πq²} ≤ m ≲ e^{5.1q²}` | after Remark 13.6a, line 3588 |
| **R145** | naming correction: the frame's `K` corresponds to the **ample class** `½(F_1+F_2)`, not to the canonical class `K_{C×C} = (2g−2)(F_1+F_2)`; the name is a label and the geometric content is ampleness | head of §11.2, line 2153 |
| — | §14.5's open-items list: items (24)–(36) continue it in §23.4; items (20) and (22) are answered negatively by Theorem 19.25 | §14.5, line 3908 |
| — | the record note at Theorem 12.3 (frame defect) was **rewritten in paper language** (the working vocabulary removed) and now points to Theorem 19.25, Lemma 19.17, Theorem 19.2, Theorem 19.28, Restatement 19.29, §19.9 and §20; its mathematical content, including the certified witness, is unchanged | §12.2, line 2722 |
| — | §15 heading changed to "External inputs added by Parts II and III"; a Part III pointer added to the front matter | lines 9, 3960 |

## 5. Judged too weak to include, and why

* **The window results and crossing heights of §D.16** (the Connes–Consani
  window, the `2πe·e^{2T}` crossing height): pen-and-paper plus an interval
  certificate, outside the section's content list, and they would need their
  own script certification.
* **`h⁰_Z` for the falsifier (D.11.6′)**: rests on an unproved hypothesis and
  was itself the subject of a withdrawal; it appears only in a withdrawn row.
* **The D.21 ledger of Weil's proof against rows A–C** and the phase-137 items
  D.12 (semilocal positivity) and D.13 (the Connes–Consani dictionary): D.13 is
  largely analogy, D.12's positive content is one certified window already in
  the repository, and neither was in the section plan.
* **Moment-cone fine structure (D.26.9(iv),(v), D.26.10)**: one clause is a
  change of variable and the others re-derive Theorem 11.13 in trace
  coordinates.
* **`S_0` convexity (D.30.14(ii))**, **the optimality clause of D.31.8(ii)**,
  the almost-periodicity route of Remark D.34.2a, and the head/tail
  stratification D.38.4: sketches, or conditional on RH, and not load-bearing.
* **The numeric witness `N ≤ 15.96`**: a certified constant belonging to the
  witness discussion of §19, not needed where it arose.
* **The rank-two order `m² + a_ℓ mn + ℓn²` with `a_ℓ = ℓ+1−Λ(ℓ)` and the
  "measured genus" (D.44.3/D.44.4)**: the dictionary has no solution at a single
  prime; kept only as a `HEURISTIC` withdrawn row.
* **The model–tower comparison D.47.9**: real, but it belongs to the §21
  comparison and its headline was deflated to "the arithmetic instance of
  `g ≥ 2`"; only the un-normalization match is carried, in Proposition 22.14.
* **All claims withdrawn or refuted during the work** appear exclusively in the
  per-section withdrawn tables (eight rows in §17, and tables in §§18–22,
  eleven rows in §22), never in the running text.

Exclusions from §19bis (phase 140), added when that section was written: the
acceptance-test material of D.23.4/D.23.5 and D.24.3 — its `Ξ_Q` half was
weakened at the second pass (the step from `I_∞^{(Q)}(F,F) ≤ 0` to a failure of
the Hodge-index inequality is missing there) and Part III already carries the
falsifier suite in §§17–18; the comparison table W1–W8 with Weil's proof, which
duplicates §21's dictionary; and the synthesis page D.25, whose content is
redistributed into §19bis.5.  One judgement call is recorded: the "required
constant" step of Theorem 19bis.15 is a pointer in the source and is supplied
in-paper from the growth identity and Serre symmetry (Theorem 19.2), so the
statement is self-contained.

**Superseded note.**  The first version of this file recorded phase 140 as not
carried.  That exclusion is withdrawn: §19bis carries it in full.

## 6. Repairs of 2026-09-14

Answering the findings of `PART_III_HOSTILE_REVIEW_R1.md`.

| finding | repair | line(s) in `main.md` |
|---|---|---|
| 1 (`MAJOR`) | **§19bis added**, between §19 and §20: the Frobenius family over a number field with its integral shadow, the Pólya realization and the three Gram forms, the orbit restatement, the tensor square with `(r²/4)m²` and `χ = 1/8`, the failure of (b′) for every bidegree-function, and what an admissible `h⁰` must see — 23 numbered statements with complete proofs, a withdrawn table of nine rows, and no new import.  **Numbering choice: `19bis`**, not a renumbering of §§20–23, which would have moved every statement number and every equation tag in a thousand lines; the paper already uses `bis`/`ter` numbering from Papers 43–45 | 6513–7283 |
| 1, consequence | Proposition 19.7's title now names the witness it tests, "the bidegree witness of Theorem 19bis.19" | 5994 |
| 1, consequence | §23.1 gained item **8** (the tensor-square route, the two theorems of record, and the general-number-field item settled), and items 8–11 were renumbered 9–12; §23.2 gained the row for Restatement 19bis.13; §23.3 gained the rows for Theorem 19bis.19 and for the refuted value `χ = ¼` | 9999–10013; 9960; 9976–9977 |
| 2 | "Step 1 of Theorem 19.20's proof" → "of Theorem 19.25's proof" | 5964 |
| 3 | "Lemma 19.4 in the model" → "Lemma 19.17 in the model" | 8637 |
| 4 | four kind errors fixed: "Theorem 13.5b" → Lemma (5697); "Theorem 20.4" → Lemma (7335); "Definition 21.20" → Theorem (8374); "the second method constraint, Theorem 18.14" → Theorem 18.16 (4811) | 4811, 5697, 7335, 8374 |
| 5 | Proposition 21.21's label is now `PROVED` + `RESTATEMENT` | 9034 |
| 6 | §23.1 item 9 (now item 10) restores the hypothesis: "for every `E` with `Φ_E(0) > 0` … (Proposition 20.26(i),(ii))" | 10021–10022 |
| 7 | the dangling `§22.7` pointer in the `\deg_{det}Sh_Z` withdrawn row replaced by "which is all that is used here" | 9942 |
| 8 | the Horn-B cone conditions retagged `(T1_cone)`, `(T2_cone)` throughout §19.9 and §20, and at the one place in §23.1, so that they no longer collide with the method constraints of §18 or with `(T1′)` of §20 (18 lines) | 6460–6485, 7608–7768, 10023 |
| 9 | the §12.2 record note rewritten in paper language: the working vocabulary is gone, the mathematics and the certified witness are unchanged, and the statement is now cited as Theorem 19.25 with the diagnosis at Restatement 19.29 | 2722–2745 |
| 10 | the (X19) row moved to the head of the Part III import block, where its explanatory sentence sits | 3966 |

Line numbers are as of the state after these repairs.

## 7. Residual repairs of 2026-09-14 (second review)

Answering `PART_III_HOSTILE_REVIEW_R2.md`.

| finding | repair | line(s) in `main.md` |
|---|---|---|
| 1 | the claim that §19bis settles "the question §14.5 left open" is removed from Corollary 19bis.6 and from §23.1 item 8, and reworded as *the passage from `Q` to a general number field for the Frobenius family of Paper 44*; §19bis's opening now states that the section **narrows item (18) without closing it** — the pair-indexed candidate cannot be a function of the bidegree alone (Theorem 19bis.19) and what it must read instead is named (Corollary 19bis.23) | 6536–6541, 6695–6699, 10010–10013 |
| 1, bookkeeping | §14.5 item (18) carries a `[NARROWED]` note, and the Part III bookkeeping sentence now says item (18) is narrowed, not closed; the "items unchanged" list adjusted to (16), (17), (19), (21) | 3872–3873, 3915–3923 |
| 2 | "(Theorem 19bis.18)" → "(Theorem 19bis.19)" | 6544 |
| 3 | `certify_chi.py` added to the reproduction list of §23.6, with the phase-140 script directory | 10172–10175 |
| 4 | §23.4 gained three open items from §19bis: **(27a)** injectivity of `𝔫 ↦ Frob_𝔫` over a general number field; **(27b)** an intrinsic description of the moment cone `𝔐` (Proposition 19bis.21), explicitly distinguished from item (32); **(27c)** the Connes–Consani counting function, withdrawn as a refutation and standing `OPEN` with its two unresolved points (import (X17)) | 10107–10120 |
| 5 | the front-matter Part III paragraph names §19bis and reads "§§17–19bis, 20–23" | 9–17 |
| — | one stale pointer found during the rescan: "(§18.0 (18.2))" → "((18.2) of §18)", §18 having no subsection 0 | 5133 |

**Mechanical rescan after these repairs.** 220 numbered statements in Part III;
dangling statement references: none; dangling section references: none (the one
remaining form, `§1.13`, is the established usage of Parts I–II); import tags
cited in Part III with no row in §15: none.  `main.tex` untouched.

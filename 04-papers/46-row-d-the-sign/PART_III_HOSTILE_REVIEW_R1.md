# Paper 46, Part III (§§17–23) — hostile review, round 1

*Reviewer of record: hostile reviewer, 2026-09-14.  Target:
`04-papers/46-row-d-the-sign/main.md`, lines 4024–9389, with the writer's record
`PART_III_NOTES.md`.  Sources of truth read in full: `R137_007`, `R138_005`,
`R139_005`, `R140_005`, `R141_005`, `R142_005`, `R143_005`, `R144_005`,
`R145_005`, `R146_005`; spot-reads of `R141_001` §D.26, `R146_004`, `R145_004`.
No file other than this one was written; `main.md` was not edited.*

## Verdict

**ACCEPT WITH MINOR REPAIRS**, conditional on finding 1 (the single `MAJOR`)
being discharged — either by adding the phase-140 material or by recording it
explicitly as a deliberate exclusion in `PART_III_NOTES.md` §5 and adjusting the
two places in §19 and §23.1 that presuppose it.

Nothing in §§17–23 is unsound, overstated, or mislabelled in a way that would
convert a restatement into a reduction.  Every withdrawn or refuted claim on the
checklist was found **only** in a withdrawn table or a `REFUTED` row; all twelve
proofs read in full are complete and match the *repaired* (round-2/3) source
statements, not the round-1 ones.  The remaining findings are cross-reference and
bookkeeping defects.

---

## Findings

### 1. §§17–23 (whole Part), and `PART_III_NOTES.md` §5 — **MAJOR**

**Phase 140 (`R140_005`) is absent from Part III and is not recorded as an
exclusion.**  The notes map every section to phases 137–139 and 141–146; §D.22,
§D.23 and §D.24 appear nowhere.  Grep confirms: no occurrence of
`NS(P¹×P¹)`, "Pólya realization", `h⁰_□`, `Sh_Z`, "O-9" anywhere after line 3985.

What is lost, all of it labelled `PROVED` in `R140_005` §1:

* D.22: `Frob_𝔫` ideal-indexed for every number field, the inverse-semigroup
  law, `Sh_{O_K}(Frob_𝔫)`, **O-9 closed** — a closed open item of the campaign
  that §23.4 therefore neither lists as open nor records as closed;
* D.24.3a: the tensor-square `h⁰_□` clears phase 136's growth wall with exactly
  `(r²/4)m²`, and D.24.4 (`χ = 1/8` optimal for `ξ`; the lead's `χ = ¼`
  refuted);
* D.24.7/D.24.11: **no nonzero `h⁰` factoring through the bidegree satisfies
  (b′)**, and every `h⁰` built from pairings with `r(Div_□)` so factors;
* D.24.12: an admissible `h⁰` must read `Z(E)` through pairings `I_∞(E,X)` with
  `Z(X) ≠ 0` — the guidance that motivates the whole of §20;
* the "three Gram forms (A)/(B)/(C)" of D.23.12 and the `RESTATEMENT` D.23.13
  (Castelnuovo on a translate orbit ⟺ Bochner positivity of the Toeplitz
  kernel), plus residue R2, which `R140_005` §3 explicitly consigns "to be
  entered with Part III".

Two consequences inside the printed text:

* line 5991, **Proposition 19.7** is titled *"the bidegree witness does not reach
  this candidate"*.  The proposition is self-contained, but "the bidegree
  witness" names an object (D.24.7's `E_0 + tF`) that Part III never introduces;
  as printed the title refers to nothing.
* §23.1 ("What is proved") omits the two phase-140 theorems that are genuinely
  of record, so the consolidation is not a complete list of what phases 136–146
  established, which is the section's stated function.

*Fix.*  Either (a) add a short §20.0 (or a subsection of §19) carrying
D.24.3a, D.24.4, D.24.7/D.24.11 and D.24.12 with their proofs, and one line for
O-9 in the §23 record, and delete the residue R2 sentence from the carried list;
or (b) state in `PART_III_NOTES.md` §5 why phase 140 is excluded, retitle
Proposition 19.7 so it names its own witness, and add one sentence to §23.1
recording that the bidegree route was closed in the campaign but is not carried
here.  (a) is the honest option: D.24.7 is the theorem that forces §20 to exist.

### 2. §19.2, line 5961 — **MINOR** (cross-reference to a non-existent theorem)

> "any `h⁰` satisfying (b′) vanishes in degree `≤ 0` (Step 1 of **Theorem
> 19.20**'s proof)."

19.20 is *Lemma 19.20 (properties of `F_0`)*, whose proof contains no Step 1.
The intended target is Step 1 of **Theorem 19.25**.  *Fix:* renumber the
reference.

### 3. §21.3, line 7864 — **MINOR** (wrong source lemma in a theorem title)

> "**Lemma 21.11 (Lemma 19.4 in the model; `PROVED`, unconditional).**"

Lemma 21.11 is the model form of the **cosh lemma, Lemma 19.17**; 19.4 is
*Proposition* 19.4 (the ungated candidate fails (b′)), an unrelated statement.
*Fix:* "Lemma 19.17 in the model".

### 4. Cross-reference kind errors — **MINOR** (four places)

* line 5694: "By **Theorem** 13.5b" — 13.5b is a Lemma (correctly cited as such
  at line 6790).
* line 6562: "line of the proof of **Theorem** 20.4" — 20.4 is a Lemma.
* line 7601: "**Definition** 21.20 below" — 21.20 is a Theorem.
* line 4809 (Remark 18.1a): "the second method constraint, **Theorem 18.14**,
  says which properties are available to be named" — 18.14 is the verification
  table; the second method constraint is **Theorem 18.16**.

### 5. §21.6, Proposition 21.21 — **MINOR** (label incomplete)

Printed label: `PROVED`, frame-internal.  The statement is an **equivalence with
RH** (both directions proved, `R145_005` §1, Prop. D.42.5), and §23.2 duly lists
it in the restatement table.  Every other RH-equivalence in Part III carries
`PROVED` + `RESTATEMENT` (Theorems 20.23, Restatement 20.30).  *Fix:* add
`RESTATEMENT` to the label of Proposition 21.21, as §23.2 already implies.

### 6. §23.1 item 9 — **MINOR** (hypothesis dropped in the consolidation)

> "Index-locality: `t_n(E) > 0` for all `n ≥ N(E)`, unconditionally
> (Proposition 20.26)."

Proposition 20.26(i) requires `b = Φ_E(0) > 0`, and `R143_005` states D.34.16
as "unconditionally, **for `b > 0`**".  As printed the summary asserts an
unconditional statement stronger than the theorem it cites (and stronger than
the source), in the one section whose job is to be exact.  *Fix:* "for every `E`
with `Φ_E(0) > 0`".

### 7. §22, withdrawn table, row on `deg_det Sh_Z` — **MINOR** (dangling pointer)

The row says what survives is "used in §22.7 only in that form".  §22.7 does not
mention `Sh_Z`, `deg_det`, or the monomial identity at all.  *Fix:* delete the
clause, or restore the one sentence in §22.7 that it refers to.

### 8. §19.9, Theorem 19.30 — **MINOR** (tag collision)

The conditions on a Horn-B cone are tagged `(T1)` and `(T2)` — the same tags as
the two method constraints of §18 (Theorems 18.1, 18.16) and one character away
from `(T1′)` of §20.  Remark 20.17a then has to say "the conditions (T1),(T2) of
§19 are not the right axioms", which reads as a statement about the method
constraints.  The collision is inherited from the source (D.32.4) but the paper
is where it becomes confusing.  *Fix:* retag as `(E1′)`/`(E2′)` or
`(T1_cone)`/`(T2_cone)` and adjust the four references.

### 9. §12.2 record note, line 2721 (Parts I–II) — **MINOR** (vocabulary)

The note reads "Record note, **phase 142** (2026-09-13), `R142_001` Theorem
D.31.12, **hostile-confirmed** `R142_002`, **lead-verified** numerically."  This
is body text, not a provenance note, and carries three words of the working
vocabulary.  `PART_III_NOTES.md` §4 leaves it "as it stands" because it predates
Part III; since Part III now proves the same statement as Theorem 19.25, the
cleanest repair is to replace the note by a pointer to Theorem 19.25 with the
provenance in the ordinary italic form.  No other occurrence of
phase/round/builder/auditor/lead/FATAL/hostile was found outside provenance
paragraphs and file paths (checked by grep over lines 3986–9389).

### 10. §15, ordering of the Part III import block — **MINOR** (cosmetic)

The fifteen new rows are (X20), (X20a), (X21)–(X25b), then **(X19)**, then
(X26)–(X29a).  (X19) is out of sequence.  Numbering has no gaps, every row names
a precise source and at least one point of use, and the renumbering
(X28)–(X30a) → (X27)–(X29a) announced in the notes is consistent (no `(X30)`
remains anywhere).  *Fix:* move the (X19) row to the head of the block, where
its explanatory sentence already sits.

---

## What was checked and found correct

**1. Withdrawn / refuted claims (checklist of 18).**  Every one appears only in a
withdrawn table or as a `REFUTED` row, never as a theorem:

| claim | where it is | verdict |
|---|---|---|
| "two vs four polar exponents" A3-line (R144) | §20 withdrawn table; §23.3 row | correct, with the true separator (Lemma 20.34, Theorem 20.35) printed |
| "translation is the separating operation" (R138) | §17 withdrawn table; §23.3 | correct |
| "`Ξ_a` has more sections / anti-correlated" (R137 H2) | §18 withdrawn table | correct |
| `K_Q > 0` (R139) | §18 withdrawn table; refuted by Corollary 18.6 | correct |
| the P46-5 "erratum" of Prop. 12.6 (R139) | §18 withdrawn table, as a misreading, editorial residue only | correct |
| collapse to `NS(P¹×P¹)` (R140 H3) | absent entirely — see finding 1 | no misstatement, but absent |
| "Pólya cone is detecting" (R138 H1) | §17 withdrawn table; §23.3 | correct, refuted twice over |
| Thm D.31.14(i) (R142 H1) | §19 withdrawn table (the universal "every class of degree > `d_*`" row), restated existentially | correct |
| Thm D.31.2(ii) completeness (R142 H2) | §19 withdrawn table ("(★) is exactly the polar description…") | correct |
| "never PSD at any chart" (R146 C-A) | §22 withdrawn table; restated as Corollary 22.16 on the domain of record | correct, including the `S_f={2,p}`, `N=1`, `ε=0.34` PSD corner |
| "A3 does not enter" on the tower (R146 C-C) | §22 withdrawn table, with Doc 131 Thm 6.7 (`a = ½`) | correct |
| Hasse-test dictionary (R146 M6/M7) | §22 withdrawn table, `HEURISTIC`, with the `N_2 = 3.6784` vs `log 2` mismatch | correct |
| "adjunction forces `δ_n = n(2−2g)`" (R146 M1) | §22 withdrawn table, "withdrawn in its entirety" | correct |
| "the frame defect theorem will fail on curves" (R145) | §21 withdrawn table | correct |
| "`s_C = √7/3`" (R145 F1) | appears **only** as the `θ = π/2` value (lines 7952, 7964, 8085); the sharp constant is `√(7/11)` throughout (Prop. 21.13, Thm 21.15, §23.1, §23.6) | correct |
| "(P145) clause 4" | Prop. 21.21, printed as an equivalence with RH and withdrawn as a target | correct (label: finding 5) |
| O-30 as open | not in §23.4; printed as `REFUTED`-equivalent in Corollary 20.32 | correct |
| "strictly stronger than Thm 12.3" (R143 H4) | §20 withdrawn table; replaced by "incomparable" (Remark 20.17a) | correct |
| "Ψ entire / discrete exceptional set" (R144 M1) | §20 withdrawn table; replaced by "`m_* < ∞` always, `m_* = 1` on a non-empty open set" | correct |

**2. Labels (34 statements spot-checked across §§17–22).**  All agree with the
closing decisions.  In particular: `METHOD-CONSTRAINT` on Theorems 18.1 and
18.16 with the falsifier half `PROVED`; `PROVED-IN-REPOSITORY` on Theorem 17.19
(D.17.3); `RESTATEMENT` on Corollary 17.11, Restatement 19.29 (classical half),
Theorem 20.23, Restatement 20.30; `PROVED under RH` on Proposition 19.7,
Theorem 20.22 and Proposition 20.26(iii),(iv); `PROVED` on Theorem 20.9 —
correctly restricted to clauses (i)–(iii), the barycentric and dual descriptions
(the `RESTATEMENT`/unproved halves of D.26.9) being explicitly excluded in the
paragraph that follows and in the §20 withdrawn table; "given (X19)" carried on
Lemma 20.18, Theorems 19.22, 19.23, 19.25, 19.30, 20.19 and nowhere else; `OPEN`
on Remarks 17.15, 17.28, 22.18.  Theorem 20.22's proof states "RH is used exactly
twice", matching `R143_005` (three uses reduced to two once `(G⁺)` became
unconditional via Lemma 20.21), and Restatement 20.30 repeats the count.

**3. Proof completeness (twelve proofs read as printed).**  Theorem 17.5
(splitting, with `K_odd` explicit, all six clauses proved); Theorem 17.14 with
Lemma 17.13 (Landau criterion — the Laplace identity, the simple pole at `z = 0`
with the quartet sign argument, and the "no real zero" step are all present, and
the `c = 0` case is handled); Theorem 18.10 with Lemma 18.9 (Hodge index fails
for `Ξ_Q`, including the mollifier transport and Remark 18.10a on why Voronin's
zeros do not suffice); Theorem 18.18(iii) (`K_K` by contour shift — Stirling
exponent `πd/4`, Phragmén–Lindelöf, both shifts, `D^W(α)` for every `α`, and the
explicit "no theta series, no units" clause); Theorem 19.25 with Lemma 19.17,
Proposition 19.18, Lemma 19.20 and Theorem 19.23 (three steps, the `d = 400`
certified witness, the zero-list-free leakage bound `L ≤ 5.46×10⁻⁹¹`, and
Remark 19.27 recording that simplicity of `ρ₁` is load-bearing and that the
refutation fails at multiplicity 2); Theorem 20.15 ((T1′)) with Lemma 20.13 and
Theorem 20.14, including the four inputs listed and the counterexample `J` to the
literal (T1); Theorem 20.17 (transfer 12.3-B4 — Steps 1–3, the deletion of the
ample step, and the note that dropping `E' ≢ 0` is harmless); Theorem 20.22
(AM–GM floor, Cauchy–Schwarz, `(G⁺)`); Theorem 20.29 with Lemmas 20.27, 20.28;
Theorem 21.7 (the dictionary, sign `+`, all four clauses, with the `N_0 = 2−2g`
forcing and the `A125.009` gap closed); Proposition 21.21 (both directions);
Theorem 22.11 (D.47.2 — and the one-line unique-factorization gap flagged as
C-D in `R146_004` is **supplied** in the printed proof and honestly recorded in
Remark 22.11a).  No shortened or missing step was found in any of them.

**4. Imports (X19)–(X29a).**  Fifteen rows, no gaps, each with a precise source
(Widder II.5b / Landau §8; Davenport–Heilbronn JLMS 11; Montgomery–Vaughan JLMS
(2) 8; Hartshorne V.1.6/1.8/1.9 and Lazarsfeld §2.2; Tate Invent. Math. 2 Thm 2;
Grenander–Szegő Ch. 5 / Böttcher–Silbermann Prop. 2.14; Hartshorne II.2.3).
Every tag is used at least once in the body (counts: X19 20, X20 11, X20a 2,
X21 8, X22 2, X23 4, X24 5, X25 4, X25a 4, X25b 2, X26 1, X27 10, X28 7, X29 1,
X29a 1); no `(X30)` survives the renumbering.  §15's heading is "External inputs
added by Parts II and III" and the front matter carries the Part III pointer.
Only defect: ordering (finding 10).

**5. Corrections in Parts I–II.**  All seven verified at the stated lines and
none overstates: P46-1 (line 3207, the `M`-convention, "no statement of §§12.5
or 14 changes"); P46-2 (line 3088, Remark 12.3c, with "no `h⁰`, no primitivity
and no zero" and the equimodularity ceiling); P46-3 (line 2300, `K_odd` and the
splitting, pointed forward to Theorem 17.5); P46-4 (line 2673, with the caveat
that the ample cone is defined through `I_∞`); item (23) restated one-sidedly
(line 3894, with the explicit "nor is it implied by it" and the (X23)
conditionality); Remark 13.6a (line 3584, both directions, `e^{πq²} ≤ m ≲
e^{5.1q²}`, with "what remains heuristic is only the passage from one generator
to the lattice"); the `K` = ample class naming correction (line 2152, "the name
is to be read as a label").  The §14.5 bookkeeping at line 3904 correctly records
items (20) and (22) as answered negatively and (23) as surviving only as (27).

**6. Vocabulary.**  Clean inside Part III: every hit for
phase/round/builder/auditor/lead/FATAL/hostile lies in a provenance paragraph, a
file path, a reproduction block, or a withdrawn-table quotation.  No
RH-conditional statement is stated unconditionally in §§17–22 (the two candidates
— Proposition 19.7 and Theorem 20.22 — carry `under RH` in their labels and in
their proofs; Proposition 20.26 separates (i),(ii) from (iii),(iv)).  Certified
constants are named with their scripts at the point of use (`certify_sF.py`,
`certify_leakage.py`, `certify_s_star.py`, `certify_failing_index.py`,
`sC_and_points.py`, `tower_gram.py`, `cosh_test_cmn.py`) and §23.6 reproduces
them.  The one lapse is the pre-existing note of finding 9.

**7. §23.**  The proved list (11 items), the restatement table (7 rows), the
refuted table (11 rows) and the diagnosis paragraph match `R146_005` §§2 and 4
and `R144_005` §2 in substance: the intersection theory is complete, the
effective cone is the cone of Frobenius graphs and is too thin (`s < 1`, also on
curves), the missing ingredient is the `+` of `Z[π]` which `Spec Z` lacks, the
diagonal is computed but magnitude-only, every construction inside the frame is a
restatement or `Ξ_a`-uniform, and the closing sentence disclaims any sign.  Open
items (24)–(36) correspond to the `O-xx` items still open; O-29, O-30 and O-23 do
not appear (closed negatively, negatively, and affirmatively respectively, each
recorded at the right place: Corollary 20.33, Corollary 20.32, §21 withdrawn
table), and O-46.6 appears only as the withdrawn `Frob ⋆ Δ^rad` route.  The one
defect is finding 6.

**8. The writer's exclusions.**  With the single exception of finding 1, no
excluded item is load-bearing for an included statement.  Checked individually:
the §D.16 window results (nothing in §17 uses the crossing height); `h⁰_Z` for
the falsifier D.11.6′ (appears only in a withdrawn row); the D.21 ledger and
D.12/D.13 (not cited in §§18, 23); D.26.9(iv),(v) and D.26.10 (Theorem 20.9 is
proved from clauses (i)–(iii) alone, and the dual description is explicitly
unused); D.30.14(ii), D.31.8(ii), Remark D.34.2a, D.38.4 (no statement depends on
them); `N ≤ 15.96` (Proposition 20.26 does not need it); D.44.3/D.44.4 (withdrawn
`HEURISTIC` row); D.47.9 (only the un-normalization match is carried, in
Proposition 22.14, which is self-contained).

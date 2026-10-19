# Paper 46, Part IV (§§24–28) — adversarial confirmation pass (round 2)

*Reviewer of record: adversarial reviewer, 2026-09-19.  Target: `main.md`
lines 10210–12001, after the repairs recorded in `PART_IV_NOTES.md` §6bis.
Sources read for this pass: `PART_IV_ADVERSARIAL_REVIEW_R1.md` in full,
`PART_IV_NOTES.md` §§5–6bis, and the repaired sites in `main.md` with their
surrounding statements and proofs.  Format modelled on
`PART_III_ADVERSARIAL_REVIEW_R2.md`.  `main.md` was **not** edited.*

## Verdict

**ACCEPT.**  All eleven round-1 findings are discharged at the sites named, in
the form the review prescribed and not in a weaker form.  The three `MAJOR`
repairs (findings 1, 2, 3) each strictly weaken a claim, and none of them
propagates an unhedged form anywhere else in the text.  No new defect was found:
every cross-reference cited in §28 resolves to a declared statement, the boxed
wall statement claims exactly T1, T2, T5 and the classification, and no sentence
in §§24–28 asserts or hints a sign.  Three residual observations below are
cosmetic; none requires a repair before Part IV stands as the closing record.

---

## A. The eleven repairs, verified

| R1 finding | site (line) | state |
|---|---|---|
| 1 `MAJOR` — Thm 27.11 + §28.2 bullet 5 | 11522–11530, 11544–11548, 11863–11866 | **discharged.**  The theorem now quantifies over "any finite `S ⊂ \{s : \mathrm{Re}\,s > θ\}`" and concludes "implies no constraint on the zero set"; "any prescribed zero configuration" occurs nowhere in Part IV (grep: 0 hits).  The boxed bullet reads "any prescribed finite set of points in `\mathrm{Re}\,s > θ` can be added to the zero set at the same power saving".  Remark 27.11a is retitled "why only 'add' is available", names the `2π/\log 2` progressions and states that no zero of `D_a` is ever deleted or relocated.  The proof is unchanged and still correct |
| 2 `MAJOR` — Cor 26.19 | 11214, 11227–11229, 11242 | **discharged.**  `Σ_{d≠0}κ_Q(d)𝒞_4(d) = o(Q²N²)` is displayed as hypothesis **(26.9a)** in the statement; the conclusion is "`H(2,c)` **together with** (26.9a) implies RH"; the text records that `𝒞_4(d)` is complex and unbounded in sign for `d ≠ 0` and that no bound on it is proved in §26.  The difficulty verdict now reads "the off-diagonal control (26.9a) is not part of `H(k,c)` and is not implied by RH" — the self-contradiction is gone.  The hedge propagates: §28.1 item 15 (11812) and open item (44) (11910) both carry "together with the off-diagonal bound (26.9a)" |
| 3 `MAJOR` — Thm 27.10 proof | 11496–11498 | **discharged.**  The step is "absolute convergence of the Mellin integral together with uniqueness of analytic continuation"; the display is unchanged; the label line keeps "von Koch–Landau, as attribution of the **statement**, 1901" and adds that the step used is *not* Landau's abscissa theorem (one-signedness fails for `ψ(x) − x`) and that nothing in §27.2 depends on BE8 of §27.4.  The false dependency is removed |
| 4 `MINOR` — Rem 27.16 | 11682–11685 | **discharged.**  "if and only if" replaced by the soundness half alone, with "(soundness, immediate)" |
| 5 `MINOR` — Thm 27.4 display | 11368–11372 | **discharged.**  The `≤ … ≥` chain is split into two displays, "the first of these two using `\|ℱ\| + kL ≥ kL`"; both now parse |
| 6 `MINOR` — Lem 26.3 | 10839–10869 | **discharged.**  The `POINTER` is gone and the lemma is proved in place as a corollary of Prop. 26.2(3): Ramanujan expansion, Poisson against `\widehat w ∈ 𝒮(R)`, the `q = 1` frequency giving `N\widehat w(0)`, `‖b/q‖ ≥ Q^{-1}` for `q ≥ 2` with the reason (only `q_0 = 1` is tested), and the error `≪_A Q²N^{1−A(1−c)}` with the choice `A > (1+2c+A')/(1−c)`.  Independently re-derived: correct.  The `c < 1/2` restriction on (C) at `q_0 > 1` and `(C′)` `OPEN` are kept verbatim; `R149_003 §1.2` survives as a citation only.  Part IV now has exactly **two** `POINTER`s (grep: 10506, 10517 = Remarks 24.12, 24.13), both non-load-bearing, as the review directed |
| 7 `MINOR` — Part IV header | 10212–10221 | **discharged.**  `POINTER` is declared with the required clause, and the header names `METHOD-CONSTRAINT`, `RESTATEMENT`, `HYPOTHESIS`, `POINTER` as the additions to (1.12), used in Part IV only.  (1.12) itself untouched, as directed |
| 8 `MINOR` — §28.1 item 14 | 11785–11790 | **discharged.**  "on the whole domain of definition of `B`", with `q_w ∈ L¹(R)` named as the hypothesis of Theorems 25.6, 25.7 and Corollary 25.8 cited as removing it (see residual 1) |
| 9 `MINOR` — Def 27.9 / Thm 27.10 | 11508–11517 | **discharged.**  New Remark 27.10b gives the class-level statement by the identical argument, records that `θ ∈ [½,1)` is used in Definition 27.9 for the (⇐) direction only, and fixes what "the classification" denotes in §28.2 and §28.4 |
| 10 `MINOR` — working vocabulary | 10715, 10745–10760, 11910, 11897 | **discharged.**  Grep over lines 10210–end for `phase 148`, `Phase 148`, `phase 150`, `FATAL`: **no hits**.  Problem 25.13 is stated without a phase number; the §25 reading of record and withdrawn row read "what is proved is that this form is trivial on its own domain"; open item (44) reads "must be presumed erroneous until every error term and the `Q`-uniformity are re-derived"; §28.4 reads "§27 adds that…" |
| 11 `MINOR` — §28.3 closing bullet | 11926–11927 | **discharged.**  "(24)–(33), together with (34) = (P145′) and (36) above — stand as recorded there; (35) is answered negatively by item 13."  The vacuous exception and the double-naming are gone |

## B. The boxed wall statement, re-read in full

**§28.2.**  The preamble claims the box "uses only T1 (Theorem 18.1), T2
(Theorem 18.16), T5 (Theorem 27.3) and the classification (Theorems 27.10–27.11)".
Verified clause by clause: bullet 1 cites 27.10 + 27.10a; bullet 2 cites 18.1;
bullet 3 cites 18.16 + 18.17 (the Siegel-zero price, part of T2's package in §18);
bullet 4 cites 27.3 + 27.4 (the quantitative appendix to T5); bullet 5 cites 27.11.
**No other statement is cited inside the box**, and nothing more is claimed.  The
opening sentence names the sign as *an assertion*; every clause is about
admissible derivations; nothing in the box locates a zero.  The two readings that
follow are explicitly disclaimed ("neither is a claim about `ζ`") and cite
Corollary 27.11b, Theorem 21.15, Corollaries 24.11 and 25.9 — all declared.

**§28.4.**  "Row D is closed in the map: no label, no sign."  The delivered list
is exactly T1, T2, the frame defect theorem (19.25, 21.15), T5 (27.3) and the
classification (27.10–27.11) "as the exact statement of §28.2" — no sixth item.
The five-mechanism record cites 22.17, 24.1, 24.10, 25.6, 25.7, 26.13, 26.17,
all declared; the reopening criterion is six clauses with "**No such object
exists here, and none is proposed**"; the two further routes are named as
"measuring rather than moving the wall", with no number quoted.  §28.5 repeats
"numerics illustrate and falsify; they prove nothing", and Part IV closes on
"Row D is closed in the map, with no label and no sign."

**Vocabulary.**  Case-insensitive grep over lines 10211–12001 for
`breakthrough|new mathematics|we believe|suggests RH|we prove RH|the sign is
positive|therefore RH holds`: **0 hits**.  No sentence introduced by any of the
eleven repairs asserts or hints a sign; the two `MAJOR` repairs both weaken
claims, and the third removes an attribution.

## C. Cross-reference scan of §28

Every numbered statement cited anywhere in §§28.1–28.5 was matched against its
declaration: 18.1, 18.16, 18.17, 19.25, 21.15, 22.17, 24.1, 24.10, 24.11, 24.12,
25.3, 25.4, 25.6, 25.7, 25.8, 25.9, 25.10, 25.11, 25.13, 26.13, 26.17, 26.19,
27.3, 27.4, 27.10, 27.10a, 27.10b, 27.11, 27.11a, 27.11b, 27.15, 27.16 — **all
resolve, none dangling, no kind error** (each is cited by the kind it is declared
with).  Open items (37)–(44) run without gap or collision, (35) is removed and
answered in §28.1 item 13, (36) and (34)/(P145′) are each carried exactly once.

## D. Residual findings

All three are cosmetic; none is a defect of record.

1. **§28.1 item 14 (11785–11790) — cosmetic.**  The repair is correct but now
   cites the same statements twice in one sentence: "…on the whole domain of
   definition of `B` — Theorems 25.6 and 25.7 carrying `q_w ∈ L¹(R)`…, and
   Corollary 25.8 removing that restriction — at every finite rank and for both
   signs (Theorems 25.6, 25.7, Corollary 25.8)".  The trailing parenthesis is
   redundant and could be deleted.  No mathematical content is affected.
2. **Lemma 26.3 (10839–10843) — cosmetic.**  The statement carries a clause of
   its own proof ("the spacing at `q_0 = 1` is `Q^{-1}`, not `Q^{-2}`, so the
   Poisson step is uniform for every `c < 1`"), which the proof then repeats.
   Harmless; the lemma is now self-contained, which was the point.
3. **"The classification" (11516–11517 against 11838) — cosmetic.**  Remark 27.10b
   defines the phrase as Theorems 27.10–27.11 with the two printed instances
   *together with the class-level observation*, while §28.2's preamble and §28.4
   name only "Theorems 27.10–27.11".  The two are consistent — 27.10b is a remark
   attached to 27.10 — but a reader tracking the phrase must go to 27.10b to find
   its definition.  One cross-reference to 27.10b in §28.2's preamble would close
   this; it is not required.

## E. Unchanged from round 1

Everything confirmed in §§"What was checked and found correct" 1–8 of the round-1
review was spot-re-checked at the repaired sites and is unaffected: the label
table against `R147_005`/`R148_005`/`R149_005`/`R150_005`, the withdrawn tables of
§§24–27 (Theorem 4.7, Corollary 4.7a, Corollary 5.5 still appear only there), the
import tags, the `CERTIFIED` treatment of Hooley's `c_0`, the (H-DMV)
conditionality confined to Remark 27.16 and Proposition 27.17(3) with open item
(41) blocking, and the writer's exclusions of `PART_IV_NOTES` §5.  `main.tex`
untouched; no numbering collision with Parts I–III.

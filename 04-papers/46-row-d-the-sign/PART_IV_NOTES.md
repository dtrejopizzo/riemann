# Paper 46, Part IV — editorial notes

Record of what was appended to `main.md`, where each statement comes from, what
was entered as a correction, and what was left out.  This file is an editorial
record; it states no mathematics.

## 1. Sections added

| § | title | lines in `main.md` | numbered statements |
|---|---|---|---|
| — | Part IV header | 10210–10219 | — |
| 24 | The Galois group ring and its inertness at `ζ` | 10221–10545 | 19 (6 theorems, 2 corollaries, 1 lemma, 1 proposition, 1 definition, 7 remarks, 1 standing qualifier) |
| 25 | Mixed effectivity on the full square | 10547–10760 | 15 (4 theorems, 3 corollaries, 3 lemmas, 1 definition, 1 problem, 3 remarks) |
| 26 | The additive pencil and the Deligne extraction | 10762–11261 | 27 (11 theorems, 3 corollaries, 2 lemmas, 4 propositions, 1 definition, 1 problem, 5 remarks/readings) |
| 27 | Three method constraints and the classification of coefficient sequences | 11263–11694 | 25 (5 theorems, 2 corollaries, 1 lemma, 5 propositions, 4 definitions, 1 hypothesis, 7 remarks) |
| 28 | The closure of row D in the map | 11696–11940 | 0 (consolidation only: proved items 13–16, the boxed statement of the wall, open items (36)–(44) and the carried list, the decision, reproduction) |

Line numbers are as of the commit in which Part IV was appended and will drift
with later edits; the section headings are stable.

Each of §§24–27 carries, at its head, a one-paragraph italic provenance note
naming its source files, and, at its foot, a **Withdrawn in this section** table
(10 rows in §24, 10 in §25, 12 in §26, 13 in §27).  No source file name appears
in any theorem, definition or proof.  §§21–22 already record phases 145–146;
Part IV covers phases 147–150 and repeats nothing from them.

## 2. Theorems and their sources

The mapping is by source label; every statement carries its complete proof from
the source unless it is explicitly marked `POINTER`.

**§24** — `03-research/phase-147-row-d-galois-ring/R147_003b_BUILDER_ROUND3.md`
§§R3.1–R3.7 and `R147_001_BUILDER_ROUND1.md` (item D.50.2); labels, corrections
and withdrawals from `R147_005_LEAD_CLOSING_DECISION.md`, checked against
`R147_002`, `R147_004`, `R147_004b`; corpus row from `CORPUS_CHECK_R147b.md`.
Lem 24.1 ← D.50.2 as corrected (the radial realization, not "the carrier") ·
Def 24.2 ← D.55.1′ · Thm 24.3 ← D.55.2′ · Thm 24.4 ← D.55.3′ (with the
base-dependence correction C2 folded into (ii)) · Thm 24.5, Rem 24.5a ← D.55.4′ ·
Def 24.6, standing qualifier ← D.55.5′ and MINOR 15 · Thm 24.7, Rem 24.7a ←
D.55.5″ and C4 · Thm 24.8 ← D.55.6′ · Prop 24.9 ← D.55.8′ ·
**Thm 24.10 (the inertness at `ζ`) ← D.55.9′**, with Rem 24.10a ← D.55.9′(iii)
and Rem 24.10b ← the two cautions of C1 · Cor 24.11 ← `R147_005` §1(3) ·
Rem 24.12 ← D.55.7′(i),(ii), **`POINTER`** · Rem 24.13 ← D.55.10′, **`POINTER`** ·
Rem 24.14 ← the by-product of `R147_005` §2.

**§25** — `03-research/phase-148-row-d-mixed-effectivity/R148_003_BUILDER_ROUND2.md`
§§R1–R11, with definitions from `R148_001_BUILDER_ROUND1.md`; labels and
withdrawals from `R148_005_LEAD_CLOSING_DECISION.md`, checked against `R148_002`
and `R148_004`, and the lead note of 2026-09-14 (the three cosmetic residues,
including "absolutely convergent at `w`" for "finite at `w`", which is the form
used in Theorems 25.6 and 25.7).
Def 25.1 ← D.56.1′ · Thm 25.2 ← D.56.2′ · **Lem 25.3 ← D.56.3′** ·
Lem 25.4 ← D.56.3″ · Lem 25.5 ← D.56.3⁗ · **Thm 25.6 (the kill) ← D.56.4″** ·
Thm 25.7 ← D.56.4′ · Cor 25.8 ← D.56.3‴ · Cor 25.9 ← D.56.6, D.56.7 ·
Thm 25.10 ← D.55.6′ · Thm 25.11, Rem 25.11a ← D.56.8′(i), D.56.8(ii) ·
Rem 25.12 ← D.55.5′, D.55.7′, D.55.8′ · **Problem 25.13 ← O-148.2** as stated in
§R10, with the phase-41 doc-125 obstructions `IMPORTED`.

**§26** — `03-research/phase-149-row-d-additive-pencil/R149_001_BUILDER_ROUND1.md`
§§2–6 as repaired by `R149_003_REPAIRS.md`; labels of record from
`R149_005_LEAD_CLOSING_DECISION.md`, whose §4 amendments govern; audit
`R149_002`.
Def 26.1 ← D.59.0 · Prop 26.2 ← D.59.0a (item 3 `IMPORTED`, attribution Vaughan) ·
Lem 26.3 ← D.59.0c, **`POINTER`**, with D.59.0d/0e and the demotion of `(C′)` ·
**Thm 26.4, Rem 26.4a ← D.59.1** with the framing sentence of record of
`R149_003` §0 (a Hölder inequality, folklore chain) · Cor 26.5 ← D.59.1a ·
Thm 26.6 ← D.59.2 · Thm 26.7, Rem 26.7a ← D.59.3 as restated D.59.3′, with
Lem D.59.3a supplying the `M_Q` term · Prop 26.8 ← D.59.4 ·
Thm 26.9 ← D.60.0, D.60.1, D.60.3 · Cor 26.10 ← D.60.2 ·
Rem 26.10a ← D.60.5, D.60.7 as rescoped (D.60.7′, D.60.7b, D.60.7c) and
`R149_003` §3 (the `Ω`-check) · Lem 26.11a ← D.61.2 · Thm 26.11, Rem 26.11b ←
D.61.4, D.61.4a · Thm 26.12 ← D.61.5, label `RESTATEMENT` per the W-a warning ·
**Thm 26.13 ← D.61.6** · Thm 26.14 ← D.61.7 as repaired (D.61.7′) ·
**Thm 26.15 ← D.61.8**, **Thm 26.16 ← D.61.9** · **Thm 26.17 ← D.61.10′**, with
Lem D.61.10a as (T1) and Goldston–Montgomery as (T2) · Prop 26.18 ← D.62.1 ·
Cor 26.19 ← D.62.2′ (Granville 2007 + Corrigendum 2008 as the sharp half;
Bhowmik–Ruzsa as quasi-RH only) · **Problem 26.20 ← (P149), reclassified** ·
Prop 26.21 ← D.63.1, D.63.2, D.63.3.

**§27** — `03-research/phase-150-row-d-method-theorems/R150_001_BUILDER_ROUND1.md`
§§2, 4, 5 as repaired by `R150_003_BUILDER_ROUND2.md`; labels, downgrades and
withdrawals from `R150_005_LEAD_CLOSING_DECISION.md` and `R150_004_HOSTILE_CONFIRMATION.md`;
audit `R150_002`.
Def 27.1, Def 27.2 ← Def. 5.1, Def. 5.2 · **Thm 27.3 (T5) ← Thm 5.3** ·
Thm 27.4 ← Thm 5.4 · Prop 27.5 ← Prop. 5.5′ (round-1 Cor. 5.5 withdrawn) ·
Prop 27.6 ← Prop. 5.6 as corrected (the two normalisations separated) ·
**Prop 27.7 ← Prop. 5.7, round-1 statement restored per `R150_004` D-1**: the
identity `‖b*b‖₂² = E(b)` holds for every complex `b`, both sides being
`∫|b̂|⁴`; the archimedean half of the round-2 correction is retained as the
remark that the archimedean family is not covered · falsifier F5 ← §5.5 ·
Rem 27.7a ← `R150_003` §5.1 (scope: large-value counting untouched) and §5.7 ·
Cor 27.8 ← `R150_005` §2(2) · **Def 27.9, Thm 27.10, Thm 27.11 ← Def. 4.11,
Thm 4.12, Thm 4.13**, label `CLASSICAL` per `R150_004` (b), with Thm 4.13's
restriction recorded as Rem 27.11a and the mechanism table of `R150_003` §4.7
compressed into the reading of record · Lem 27.12, Rem 27.12a ← Lem. 4.2′ and
Cor. 4.3 with the corrected reading · Def 27.13, Thm 27.14, Rem 27.14a ←
Def. 4.4, Thm 4.5 and the coefficient-blindness table of §4.3 ·
Rem 27.15 ← Thm 4.8′ reduced to its two surviving legs, with the withdrawal of
Thm 4.7/Cor. 4.7a and the Friedlander–Iwaniec / Heath-Brown refutation ·
Hypothesis (H-DMV) ← `R150_003` §2.1 · Rem 27.16, Rem 27.16a ← Thm 2.8′,
Cor. 2.9′, Prop. 2.6′ and the corrected non-implication table ·
Prop 27.17 ← Prop. 2.10′.

**§28** — consolidation of §§17–27 and of the closing records `R147_005`,
`R148_005`, `R149_005`, `R150_005`, together with
`05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-CLOSURE-PLAN-2026-09-19.md`
§§3, 6, 8, 9.  From the plan only what the phases prove is carried: the six
clauses of §6 are used verbatim as the reopening criterion (§28.4); the plan's
§3.4 reformulation appears only through what §26 proves (Theorems 26.15, 26.17);
its §9.2 quantitative reformulation and its route rankings are **not** carried.

## 3. Imports

**No new import tag was added to §15.**  Part IV uses (X20) (Landau), (X20a)
(the Vinogradov–Korobov error), (X21) (Davenport–Heilbronn), (X22)
(Montgomery–Vaughan), (X24) (the real-zero input, through Corollary 18.17 only)
and (X25) (Artin holomorphy, in open item (39)), all already in the table.  The
classical facts named in the text and labelled `CLASSICAL` where they occur —
Hecke's entirety and functional equation for `Λ(s,χ)` ((H1)–(H3) of §24),
Ramanujan-sum orthogonality (Carmichael 1932), Montgomery–Hooley,
Pólya–Vinogradov, Bernstein's inequality, Plancherel on `(Z/q)^×`,
Goldston–Montgomery 1987, Siegel–Walfisz, the number-field large sieve (Huxley
1968; Schaal 1970), Granville 2007 with its Corrigendum 2008, Bhowmik–Ruzsa
2018, Bhowmik–Schlage-Puchta, von Koch–Landau — are cited in place with the
clause each serves, as (1.12) permits, and none of them is load-bearing for a
statement about the location of any zero.

One **hypothesis** label is introduced and is confined to a single remark:
**(H-DMV)** in §27.4, flagged as not checked against its source, with open item
(41) blocking.  This is the only place in Paper 46 where a statement rests on a
reading of a paper that has not been verified, and it is for that reason recorded
as a remark rather than as a theorem.

## 4. Corrections entered

All corrections of record for phases 147–150 are entered **inside Part IV**, in
the withdrawn tables of §§24–27 and at the places they correct; no line of
Parts I–III was edited when Part IV was appended.  The list, by section:

| where | what |
|---|---|
| §24, Thm 24.4(ii) | `\deg K_L = 1` is restricted to `F = Q`; over an imaginary quadratic base `\deg K_{Q_𝔄} = ½`.  Nothing downstream changes: the degree gate is computed directly from the sign, and every support-function ratio is homogeneous of degree `0` in the normalisation |
| §24, Rem 24.10b | two non sequiturs removed — "invariant sector, hence support function unchanged", and "if `ρ` is a zero of `ζ_F` then `m = 1`"; the conclusion stands by Theorem 24.10(i),(ii) |
| §24, Rem 24.12 | the "first support function to reach `1`" claim withdrawn: `s(γ,0) = 1` always, by (19.2) |
| §25, table | the Hilbert–Schmidt premise of the collapse withdrawn and replaced by the stronger Lemma 25.3(i); the `+` quadrant closed rather than left open; the "three restrictions of one trace" title withdrawn |
| §26, Lem 26.3 | `(C′)` demoted to a plausibility clause: its large-sieve justification is false exactly in the range where it was invoked.  `(E)` is upgraded to all `c < 1` |
| §26, (26.5) | the Montgomery–Hooley identification corrected at the constant level by the archimedean `(\log2π+1)xQ` |
| §26, Rem 26.11b | the squarefree weight `μ²` restored in `κ` |
| §26, Thm 26.17 | "nothing transports between the two squares" withdrawn; the two classical moment transports written out, and the wall relocated to the polar/positivity structure |
| §26, Cor 26.19 | the sharp half of the average-Goldbach equivalence re-attributed to Granville 2007 + Corrigendum 2008; Bhowmik–Ruzsa is the quasi-RH half |
| §26, Problem 26.20 | (P149) reclassified as the Hardy–Littlewood `k`-tuple conjecture with square-root error on average |
| §27, Prop 27.7 | the round-two "correction" of `‖b*b‖₂² = E(b)` withdrawn as a correction of a non-error; the round-one identity restored, with the archimedean family removed from the proposition |
| §27, Lem 27.12 | the range corrected from `\|γ\| ≤ N^{1/2}` to `\|γ\| ≤ N^{1/2−ε}` |
| §27, Rem 27.14a, Rem 27.15 | T4 reduced to Lemma 27.12 plus the one coefficient-blind mechanism; its bilinear leg withdrawn and refuted |
| §27, Rem 27.16 | T3 held as a remark conditional on (H-DMV), with open item (41) blocking |
| §28.3 | §23.4 item (35) (the Galois ring) is **answered negatively** by Theorem 24.10 and is removed from the open list; items (36) and (34)/(P145′) are carried unchanged; items (37)–(44) are new |

## 5. Judged too weak to include, and why

* **The full grid of enlarged constants `σ(γ,m)` of phase 147** (lower bounds
  `0.99846` at `m = 1`, `0.99961` at `m = 4`, `0.99996` at `m = 12`, with the
  corresponding degree thresholds): grid values are lower bounds, they bear on
  `L(s,χ)` and not on `ζ`, and the analytic statements `S(γ,π/2,m) = 1 ⟺ 4 ∣ m`
  and `σ(γ,m) < 1` are carried as a labelled pointer (Remark 24.12) rather than
  transcribed.
* **Theorem D.55.10′ (Epstein on the graded carrier)** and the round-one Frobenius
  constant `s_{\mathrm{Frob}} = 2/3` on `E/F_5`: the first is carried as a
  pointer (Remark 24.13), the second belongs to §21's model comparison and adds
  nothing to the closure.
* **The minor open items of phase 148** (a regularised trace on the algebra
  generated by the two sectors; a carrier in which the Weil density and the `L²`
  pairing coincide; finiteness of the mixed constant): recorded in the source,
  idle here, and none of them load-bearing.  Only the principal residue is
  carried, as Problem 25.13.
* **The Barban–Davenport–Halberstam / Montgomery–Hooley discussion beyond the
  main term**, the Green–Tao restriction computation (D.60.6), and the detailed
  Fiorilli–Martin / Hayani survival analysis (D.60.7 and its repairs): compressed
  into Remark 26.10a, since their content is a literature summary plus one
  exponent check, and the phase's own labels restrict them to `k = 1`.
* **The archimedean and quadratic-twist instance tables of phase 150**: each row
  is Proposition 27.6 or 27.7 with a family substituted, and the archimedean row
  is withdrawn from the `k = 2` proposition in any case.
* **The route rankings of the closure plan (§§4, 8) and its compressed catalogue
  of dead routes (§7)**: planning material, not proved mathematics; the only
  parts carried are the six clauses of the plan's success criterion, used as the
  reopening criterion in §28.4.
* **The plan's §9.2 reformulation of the wall in terms of the least eigenvalue of
  the Weil form**, and the proposal to extend the certified positivity range:
  the first is a restatement of a repository fact and is not proved in any phase
  of Part IV; the second is named in §28.4 only as an available computation that
  measures the wall, with no number quoted.
* **All claims withdrawn or refuted during phases 147–150** appear exclusively in
  the per-section withdrawn tables, never in the running text.

## 6. Mechanical checks run after appending

* Forbidden vocabulary: no occurrence in Part IV of "breakthrough",
  "new mathematics", "we believe", or any sentence claiming or hinting a sign;
  §§24–27 each close with a sentence stating that no sign is claimed, and §28
  closes Part IV with the same statement.
* Every statement of Part IV that is not labelled `POINTER` carries its complete
  proof in the text; the three `POINTER` items (Lemma 26.3, Remarks 24.12 and
  24.13) name their source file and section and carry the label of record.
* Cross-references to Parts I–III were checked against the statements they name:
  Definition 11.1, Definition 11.4, (11.1), (11.6), (11.7), Theorems 11.5,
  11.7(i),(ii), 11.8(v), 11.13(i), 12.3, 12.4, 17.14, 18.1, 18.5, 18.10, 18.16,
  18.20, 19.23, 19.25, 19.30, 21.15, 22.17, Lemmas 18.4, 19.17, Propositions
  19.18, 21.21, Corollaries 18.17, 19.24, Remark 18.12a, (19.2), §21.8, §23.1–23.6.
* Statement numbering continues Part III without collision: §§24–27 introduce
  numbers 24.1–24.14, 25.1–25.13, 26.1–26.21, 27.1–27.17, and §28 introduces
  none.
* `main.tex` untouched.

## 6bis. Round-1 repairs (`PART_IV_HOSTILE_REVIEW_R1.md`, applied 2026-09-19)

All eleven findings were applied to `main.md` §§24–28; no other file was edited.

1. **MAJOR — Theorem 27.11 and §28.2, fifth bullet.**  The conclusion now reads
   "for **any finite** `S ⊂ \{s : \mathrm{Re}\,s > θ\}` there is such a `b` whose
   Dirichlet series vanishes on `S`; the hypothesis therefore implies no
   constraint on the zero set."  "Any prescribed zero configuration" is deleted
   from the theorem and from the boxed bullet, the latter now reading "any
   prescribed finite set of points in `\mathrm{Re}\,s > θ` can be added to the
   zero set at the same power saving".  Remark 27.11a is retitled "why only
   'add' is available" and states the `2π/\log 2` progressions and that zeros are
   never removed.
2. **MAJOR — Corollary 26.19.**  The off-diagonal bound
   `Σ_{d≠0}κ_Q(d)𝒞_4(d) = o(Q²N²)` is now displayed as hypothesis **(26.9a)** in
   the statement; the conclusion is "`H(2,c)` together with (26.9a) implies RH",
   with a sentence recording that `𝒞_4(d)` is complex and unbounded in sign for
   `d ≠ 0` and that no bound on it is proved in §26.  The difficulty verdict no
   longer calls the off-diagonal control a demand of `H(2,c)`: it now reads "the
   off-diagonal control (26.9a) is not part of `H(k,c)` and is not implied by
   RH".  §28.1 item 15 and open item (44) carry the same hedge.
3. **MAJOR — Theorem 27.10, proof.**  "Landau's theorem on the abscissa, in
   Mellin form" is replaced by "absolute convergence of the Mellin integral
   together with uniqueness of analytic continuation"; the display is unchanged.
   The label line keeps "von Koch–Landau" as attribution of the statement (1901)
   and adds that the step used is not Landau's abscissa theorem, whose
   one-signedness hypothesis fails for `ψ(x) − x`, and that nothing in §27.2
   depends on BE8 of §27.4.
4. **MINOR — Remark 27.16.**  The biconditional is replaced by the soundness
   half only: "if `(\mathrm{ZFS}_δ)` is derivable from BE1–BE8 then it holds in
   every model (soundness, immediate)".
5. **MINOR — Theorem 27.4.**  The `≤ … ≥` chain is split into two displays, with
   "and, separately," between them and `|ℱ| + kL ≥ kL` named for the first of the
   two lower bounds.
6. **MINOR — Lemma 26.3.**  The `POINTER` is deleted and the lemma is proved in
   place as a corollary of Proposition 26.2(3): Ramanujan expansion, Poisson
   summation against `\widehat w ∈ 𝒮(R)`, the `q = 1` frequency giving
   `N\widehat w(0)`, `‖b/q‖ ≥ Q^{-1}` for `q ≥ 2` (spacing `Q^{-1}`, not `Q^{-2}`,
   because only `q_0 = 1` is tested), and the error `≪_A Q²N^{1−A(1−c)}`.  The
   `c < 1/2` restriction on (C) at `q_0 > 1` and `(C′)` `OPEN` are kept verbatim,
   and `R149_003_REPAIRS.md` §1.2 (Lemma D.59.0c) is retained as a citation, no
   longer as a pointer.  Remarks 24.12 and 24.13 remain `POINTER`s, as the review
   directs.  §6 above is superseded on this point: Part IV now has **two**
   `POINTER` items, both non-load-bearing.
7. **MINOR — Part IV header.**  `POINTER` is now declared, "for a statement whose
   proof is not reproduced here, which then names its source file, section and
   label of record", and the header states that `METHOD-CONSTRAINT`,
   `RESTATEMENT`, `HYPOTHESIS` and `POINTER` are the additions to (1.12) and are
   used in Part IV only.  Per the review, (1.12) itself was **not** edited and no
   repair was required for `HYPOTHESIS`.
8. **MINOR — §28.1 item 14.**  The entry now says "on the whole domain of
   definition of `B`", names the hypothesis `q_w ∈ L¹(R)` at almost every `w` in
   Theorems 25.6, 25.7, and cites Corollary 25.8 as removing it.
9. **MINOR — Definition 27.9 / Theorem 27.10.**  New **Remark 27.10b** states the
   class-level statement for a general polar-at-zeros `a` by the identical
   argument, records that `θ ∈ [½,1)` is used in Definition 27.9 for the (⇐)
   direction only, and fixes what "the classification" denotes in §28.2 and §28.4.
10. **MINOR — working vocabulary, five lines.**  Problem 25.13 now reads
    "Theorems 25.6 and 25.7 answer…"; the §25 reading of record reads "what is
    proved is that *this* form is trivial and zero-blind on *its* domain"; the
    §25 withdrawn row reads "what is proved is that this form is trivial on its
    own domain"; open item (44) reads "must be presumed erroneous until every
    error term and the `Q`-uniformity are re-derived" in place of the internal
    rule; §28.4 reads "§27 adds that…".
11. **MINOR — §28.3, closing bullet.**  Now "(24)–(33), together with
    (34) = (P145′) and (36) above — stand as recorded there; (35) is answered
    negatively by item 13."

**Re-run of the forbidden-vocabulary grep** over `main.md` lines 10210–end
(`breakthrough|new mathematics|we believe|suggests RH`, case-insensitive): **no
match**.  No sentence asserting or hinting a sign was introduced by any of the
edits; the two MAJOR repairs both weaken claims.
